from typing import List, Optional, Iterator
import logging
import subprocess
import duckdb
import tempfile
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import time
from linkml_runtime.linkml_model.meta import SchemaDefinition, SlotDefinitionName
import requests

# Global session for connection pooling
_session_lock = threading.Lock()
_global_session = None

def get_http_session():
    """Get a shared HTTP session with connection pooling"""
    global _global_session
    with _session_lock:
        if _global_session is None:
            _global_session = requests.Session()
            # Configure connection pooling for parallel uploads
            adapter = requests.adapters.HTTPAdapter(
                pool_connections=20,
                pool_maxsize=20,
                pool_block=True
            )
            _global_session.mount('http://', adapter)
            _global_session.mount('https://', adapter)
        return _global_session

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
    else:
        raise Exception(f'Unknown format {format}')
    # Use direct HTTP with connection pooling for better performance
    try:
        session = get_http_session()
        with open(f, 'rb') as file_data:
            response = session.post(url, data=file_data, headers={'Content-Type': ct}, timeout=300)
            print(f"Uploaded {f}: {response.status_code}")
            if response.status_code != 200:
                print(f"Error response: {response.text}")
            return response.status_code == 200
    except Exception as e:
        print(f"Error uploading {f}: {e}")
        return False


def csv_to_json_chunk(csv_file: str, chunk_start: int, chunk_size: int, output_file: str) -> int:
    """
    Convert a chunk of CSV/TSV data to JSON format using DuckDB
    
    :param csv_file: Input CSV/TSV file path
    :param chunk_start: Starting row (0-based)
    :param chunk_size: Number of rows to process
    :param output_file: Output JSON file path
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
        
        # Convert to list of dicts for JSON
        docs = [dict(zip(columns, row)) for row in result]
        
        with open(output_file, 'w') as f:
            json.dump(docs, f)
        
        conn.close()
        return len(docs)
    except Exception as e:
        print(f"Error processing chunk starting at {chunk_start}: {e}")
        return 0


def process_and_upload_chunk(csv_file: str, chunk_start: int, chunk_size: int, 
                           base_url: str, core: str, schema: SchemaDefinition,
                           format: str, processor: str) -> int:
    """
    Process a chunk (create temp file) and upload it to Solr in one parallel task
    """
    temp_file = None
    try:
        if format == 'json':
            temp_file = tempfile.NamedTemporaryFile(suffix='.json', delete=False)
            temp_file.close()
            docs_processed = csv_to_json_chunk(csv_file, chunk_start, chunk_size, temp_file.name)
        else:
            temp_file = tempfile.NamedTemporaryFile(suffix='.csv', delete=False)
            temp_file.close()
            docs_processed = _create_csv_chunk(csv_file, chunk_start, chunk_size, temp_file.name)
        
        if docs_processed > 0:
            success = bulkload_file(
                temp_file.name,
                format=format,
                base_url=base_url,
                core=core,
                schema=schema,
                processor=processor,
                commit=False
            )
            if success:
                print(f"Chunk {chunk_start}-{chunk_start+chunk_size}: {docs_processed} docs uploaded")
                return docs_processed
            else:
                print(f"Failed to upload chunk {chunk_start}-{chunk_start+chunk_size}")
                return 0
        else:
            return 0
            
    except Exception as e:
        print(f"Error processing chunk {chunk_start}: {e}")
        return 0
    finally:
        # Clean up temp file
        if temp_file and os.path.exists(temp_file.name):
            try:
                os.unlink(temp_file.name)
            except:
                pass


def bulkload_chunked(csv_file: str,
                    base_url: str,
                    core: str,
                    schema: SchemaDefinition,
                    chunk_size: int = 500000,
                    max_workers: int = 8,
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
    print(f"Processing {total_rows} rows in chunks of {chunk_size} with {max_workers} parallel workers")
    
    total_loaded = 0
    preprocessing_start = time.time()
    
    # Submit all chunk processing and upload tasks in parallel
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        
        for chunk_start in range(0, total_rows, chunk_size):
            actual_chunk_size = min(chunk_size, total_rows - chunk_start)
            
            # Submit the entire process+upload as one parallel task
            future = executor.submit(
                process_and_upload_chunk,
                csv_file,
                chunk_start,
                actual_chunk_size,
                base_url,
                core,
                schema,
                format,
                processor
            )
            futures.append(future)
        
        preprocessing_time = time.time() - preprocessing_start
        print(f"Preprocessing complete ({preprocessing_time:.2f}s) - starting parallel uploads...")
        upload_start = time.time()
        
        # Process results as they complete (truly parallel!)
        for future in as_completed(futures):
            try:
                docs_loaded = future.result()
                total_loaded += docs_loaded
                print(f"Progress: {total_loaded}/{total_rows} documents loaded")
            except Exception as e:
                print(f"Error in parallel chunk processing: {e}")
        
        upload_time = time.time() - upload_start
        total_processing_time = time.time() - preprocessing_start
        print(f"Upload complete! Processing: {preprocessing_time:.2f}s, Upload: {upload_time:.2f}s, Total: {total_processing_time:.2f}s")
    
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

