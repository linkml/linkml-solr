from typing import List, Optional, Iterator
import logging
import subprocess
import duckdb
import cbor2
import tempfile
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from linkml_runtime.linkml_model.meta import SchemaDefinition, SlotDefinitionName
import requests

def _get_multivalued_slots(schema: SchemaDefinition) -> List[SlotDefinitionName]:
    return [s.name for s in schema.slots.values() if s.multivalued]


def bulkload_file(f,
                  format='csv',
                  base_url=None,
                  core=None,
                  schema: SchemaDefinition = None,
                  processor: str = None,
                  commit: bool = False,
                  ):
    """
    Bulkload a file using solr bulkload API

    :param f:
    :param format:
    :param base_url:
    :param core:
    :param schema:
    :param processor: Processor argument to pass when bulk loading to Solr
    :return:
    """
    mvslots = _get_multivalued_slots(schema)
    print(f'MV = {mvslots}')
    separator = '%09'
    internal_separator = '%7C'
    parts = [f'f.{s}.split=true&f.{s}.separator={internal_separator}' for s in mvslots]
    commit_param = 'true' if commit else 'false'
    url = f'{base_url}/{core}/update?{"&".join(parts)}&commit={commit_param}&separator={separator}'
    if (processor is not None):
        url = f'{url}&processor={processor}'
    if format == 'csv':
        ct = 'application/csv'
    elif format == 'json':
        ct = 'application/json'
    elif format == 'cbor':
        ct = 'application/cbor'
        url = f'{base_url}/{core}/update/cbor?commit={commit_param}'
    else:
        raise Exception(f'Unknown format {format}')
    command = ['curl', url, '-T', f'{f}', '-X', 'POST', '-H', f'Content-type:{ct}']
    print(command)
    subprocess.run(command)


def csv_to_cbor_chunk(csv_file: str, chunk_start: int, chunk_size: int, output_file: str) -> int:
    """
    Convert a chunk of CSV/TSV data to CBOR format using DuckDB
    
    :param csv_file: Input CSV/TSV file path
    :param chunk_start: Starting row (0-based)
    :param chunk_size: Number of rows to process
    :param output_file: Output CBOR file path
    :return: Number of documents processed
    """
    try:
        conn = duckdb.connect()
        
        # Auto-detect separator and read chunk with DuckDB
        sep = '\t' if csv_file.endswith('.tsv') else ','
        query = f"""
        SELECT * FROM read_csv_auto('{csv_file}', 
                                   delim='{sep}',
                                   ignore_errors=true,
                                   header=true)
        LIMIT {chunk_size} OFFSET {chunk_start}
        """
        
        result = conn.execute(query).fetchall()
        columns = [desc[0] for desc in conn.description]
        
        # Convert to list of dicts
        docs = [dict(zip(columns, row)) for row in result]
        
        with open(output_file, 'wb') as f:
            cbor2.dump(docs, f)
        
        conn.close()
        return len(docs)
    except Exception as e:
        print(f"Error processing chunk starting at {chunk_start}: {e}")
        return 0


def bulkload_chunked(csv_file: str,
                    base_url: str,
                    core: str,
                    schema: SchemaDefinition,
                    chunk_size: int = 100000,
                    max_workers: int = 4,
                    format: str = 'csv',
                    processor: str = None) -> int:
    """
    Load a large CSV file in chunks with parallel processing
    
    :param csv_file: Path to the CSV file
    :param base_url: Solr base URL
    :param core: Solr core name
    :param schema: LinkML schema definition
    :param chunk_size: Number of rows per chunk
    :param max_workers: Number of parallel workers
    :param format: Output format ('csv' or 'cbor')
    :param processor: Solr processor to use
    :return: Total number of documents loaded
    """
    # Get total row count using DuckDB (more reliable for large files)
    conn = duckdb.connect()
    sep = '\t' if csv_file.endswith('.tsv') else ','
    count_query = f"""
    SELECT COUNT(*) FROM read_csv_auto('{csv_file}', 
                                      delim='{sep}',
                                      ignore_errors=true,
                                      header=true)
    """
    total_rows = conn.execute(count_query).fetchone()[0]
    conn.close()
    print(f"Processing {total_rows} rows in chunks of {chunk_size}")
    
    total_loaded = 0
    temp_files = []
    
    try:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            
            for chunk_start in range(0, total_rows, chunk_size):
                actual_chunk_size = min(chunk_size, total_rows - chunk_start)
                
                if format == 'cbor':
                    # Convert chunk to CBOR
                    temp_file = tempfile.NamedTemporaryFile(suffix='.cbor', delete=False)
                    temp_file.close()
                    temp_files.append(temp_file.name)
                    
                    future = executor.submit(
                        csv_to_cbor_chunk,
                        csv_file,
                        chunk_start,
                        actual_chunk_size,
                        temp_file.name
                    )
                    futures.append((future, temp_file.name, 'cbor'))
                else:
                    # For CSV, create chunk file
                    temp_file = tempfile.NamedTemporaryFile(suffix='.csv', delete=False)
                    temp_file.close()
                    temp_files.append(temp_file.name)
                    
                    future = executor.submit(
                        _create_csv_chunk,
                        csv_file,
                        chunk_start,
                        actual_chunk_size,
                        temp_file.name
                    )
                    futures.append((future, temp_file.name, 'csv'))
            
            # Process chunks as they complete
            for future, temp_file, file_format in futures:
                try:
                    docs_processed = future.result()
                    if docs_processed > 0:
                        # Upload the chunk
                        bulkload_file(
                            temp_file,
                            format=file_format,
                            base_url=base_url,
                            core=core,
                            schema=schema,
                            processor=processor,
                            commit=False
                        )
                        total_loaded += docs_processed
                        print(f"Loaded chunk: {docs_processed} docs (Total: {total_loaded})")
                except Exception as e:
                    print(f"Error processing chunk {temp_file}: {e}")
    
    finally:
        # Clean up temporary files
        for temp_file in temp_files:
            try:
                os.unlink(temp_file)
            except:
                pass
    
    return total_loaded


def _create_csv_chunk(csv_file: str, chunk_start: int, chunk_size: int, output_file: str) -> int:
    """
    Create a CSV/TSV chunk file with header using DuckDB
    
    :param csv_file: Input CSV/TSV file path
    :param chunk_start: Starting row (0-based)
    :param chunk_size: Number of rows to process
    :param output_file: Output CSV file path
    :return: Number of rows processed
    """
    try:
        conn = duckdb.connect()
        
        # Auto-detect separator
        sep = '\t' if csv_file.endswith('.tsv') else ','
        
        # Export chunk directly to CSV
        query = f"""
        COPY (
            SELECT * FROM read_csv_auto('{csv_file}', 
                                       delim='{sep}',
                                       ignore_errors=true,
                                       header=true)
            LIMIT {chunk_size} OFFSET {chunk_start}
        ) TO '{output_file}' (FORMAT CSV, HEADER true)
        """
        
        conn.execute(query)
        
        # Count rows to return
        count_query = f"""
        SELECT COUNT(*) FROM read_csv_auto('{output_file}', header=true)
        """
        count = conn.execute(count_query).fetchone()[0]
        
        conn.close()
        return count
    except Exception as e:
        print(f"Error creating CSV chunk starting at {chunk_start}: {e}")
        return 0

