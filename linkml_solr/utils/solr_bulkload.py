from typing import List, Optional, Iterator
import logging
import subprocess
import duckdb
import tempfile
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
import threading
import time
import os
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


def get_optimal_worker_count(max_workers: Optional[int] = None) -> int:
    """
    Pick a default number of parallel upload workers.

    Empirically (Monarch KG, ~1.5M and ~15M row Solr loads) the marginal
    benefit drops off sharply past 4 workers — Solr indexing becomes the
    bottleneck. Use 4 by default; allow override via --parallel-workers.
    """
    if max_workers is not None:
        return max(int(max_workers), 1)
    return 4


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
                    chunk_size: int = 100000,
                    max_workers: Optional[int] = None,
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
    
    # Auto-detect optimal worker count
    actual_workers = get_optimal_worker_count(max_workers)
    cpu_count = os.cpu_count() or 'unknown'
    
    if max_workers is None:
        print(f"Auto-detected {actual_workers} workers (CPU cores: {cpu_count})")
    
    print(f"Processing {total_rows} rows in chunks of {chunk_size} with {actual_workers} parallel workers")
    
    total_loaded = 0
    preprocessing_start = time.time()
    
    # Submit all chunk processing and upload tasks in parallel
    with ThreadPoolExecutor(max_workers=actual_workers) as executor:
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
        
        # Calculate throughput metrics
        docs_per_sec = total_loaded / total_processing_time if total_processing_time > 0 else 0
        upload_docs_per_sec = total_loaded / upload_time if upload_time > 0 else 0
        
        print(f"Upload complete! Processing: {preprocessing_time:.2f}s, Upload: {upload_time:.2f}s, Total: {total_processing_time:.2f}s")
        print(f"Throughput: {docs_per_sec:,.0f} docs/sec overall, {upload_docs_per_sec:,.0f} docs/sec upload")
    
    return total_loaded


def _upload_docs_to_solr(docs: list, base_url: str, core: str,
                         processor: Optional[str], chunk_label: str) -> int:
    """Upload a batch of documents (list of dicts) to Solr via /update/json/docs."""
    if not docs:
        return 0
    session = get_http_session()
    url = f'{base_url}/{core}/update/json/docs?commit=false'
    if processor is not None:
        url = f'{url}&processor={processor}'
    try:
        json_data = json.dumps(docs, default=str)
        response = session.post(
            url,
            data=json_data,
            headers={'Content-Type': 'application/json'},
            timeout=300,
        )
        if response.status_code == 200:
            print(f"Uploaded {chunk_label}: {len(docs)} docs")
            return len(docs)
        print(f"Error uploading {chunk_label}: HTTP {response.status_code}")
        print(f"Response: {response.text[:500]}")
        return 0
    except Exception as e:
        print(f"Error uploading {chunk_label}: {e}")
        return 0


def bulkload_duckdb(db_path: str,
                   table_name: str,
                   base_url: str,
                   core: str,
                   schema: SchemaDefinition,
                   chunk_size: int = 100000,
                   max_workers: Optional[int] = None,
                   where_clause: Optional[str] = None,
                   columns: Optional[str] = None,
                   order_by: Optional[str] = None,
                   processor: Optional[str] = None) -> int:
    """
    Load data from DuckDB (table or view) into Solr.

    Strategy: materialize the (filtered/ordered) source once into a temporary
    DuckDB snapshot, then stream rows through a single read-only cursor and
    hand each chunk to a thread pool that POSTs to Solr. This fixes three
    correctness/performance problems with the prior offset-based approach:

      * Without ORDER BY, parallel ``LIMIT/OFFSET`` workers returned
        overlapping/missing rows (silently dropping ~20% of input).
      * With ORDER BY, every worker re-sorted the full source, causing
        N-way simultaneous sorts and OOM on multi-GB inputs.
      * When the source was a view, every chunk recomputed the view.

    One materialization, one pass, bounded memory.
    """
    column_list = columns if columns else "*"
    actual_workers = get_optimal_worker_count(max_workers)
    cpu_count = os.cpu_count() or 'unknown'

    if max_workers is None:
        print(f"Auto-detected {actual_workers} upload workers (CPU cores: {cpu_count})")

    snapshot_fd, snapshot_path = tempfile.mkstemp(suffix='.duckdb', prefix='lsolr_snapshot_')
    os.close(snapshot_fd)
    os.unlink(snapshot_path)

    # Allow table_name to be either a bare identifier (qualified into the
    # attached "src" database) or a parenthesized subquery whose contents the
    # caller has already qualified with src.* themselves.
    from_clause = table_name if table_name.lstrip().startswith('(') else f"src.{table_name}"
    snapshot_query = f"SELECT {column_list} FROM {from_clause}"
    if where_clause:
        snapshot_query += f" WHERE {where_clause}"
    if order_by:
        snapshot_query += f" ORDER BY {order_by}"

    try:
        snapshot_start = time.time()
        print(f"Materializing snapshot from {table_name} into temp DuckDB...")
        wconn = duckdb.connect(snapshot_path)
        try:
            wconn.execute(f"ATTACH '{db_path}' AS src (READ_ONLY)")
            wconn.execute(f"CREATE TABLE snapshot AS {snapshot_query}")
            total_rows = wconn.execute("SELECT COUNT(*) FROM snapshot").fetchone()[0]
            wconn.execute("DETACH src")
        finally:
            wconn.close()
        snapshot_time = time.time() - snapshot_start
        print(f"Snapshot ready: {total_rows:,} rows in {snapshot_time:.2f}s")
        if order_by is None:
            print("Note: no --order-by supplied; snapshot order is whatever the source returned. "
                  "This is safe (every row appears exactly once) but not reproducible run-to-run.")

        if total_rows == 0:
            return 0

        upload_start = time.time()
        total_loaded = 0
        in_flight: list = []
        max_in_flight = max(actual_workers * 2, 2)

        rconn = duckdb.connect(snapshot_path, read_only=True)
        try:
            cursor = rconn.execute("SELECT * FROM snapshot")
            col_names = [d[0] for d in cursor.description]

            with ThreadPoolExecutor(max_workers=actual_workers) as executor:
                offset = 0
                while True:
                    rows = cursor.fetchmany(chunk_size)
                    if not rows:
                        break
                    docs = [dict(zip(col_names, row)) for row in rows]
                    label = f"chunk offset {offset}"
                    in_flight.append(executor.submit(
                        _upload_docs_to_solr, docs, base_url, core, processor, label
                    ))
                    offset += len(rows)

                    if len(in_flight) >= max_in_flight:
                        done, pending = wait(in_flight, return_when=FIRST_COMPLETED)
                        for fut in done:
                            try:
                                total_loaded += fut.result()
                            except Exception as e:
                                print(f"Upload worker error: {e}")
                        in_flight = list(pending)
                        print(f"Progress: {total_loaded:,}/{total_rows:,} documents uploaded")

                for fut in as_completed(in_flight):
                    try:
                        total_loaded += fut.result()
                    except Exception as e:
                        print(f"Upload worker error: {e}")
        finally:
            rconn.close()

        upload_time = time.time() - upload_start
        total_time = snapshot_time + upload_time
        docs_per_sec = total_loaded / total_time if total_time > 0 else 0
        upload_docs_per_sec = total_loaded / upload_time if upload_time > 0 else 0
        print(f"DuckDB upload complete! Snapshot: {snapshot_time:.2f}s, "
              f"Upload: {upload_time:.2f}s, Total: {total_time:.2f}s")
        print(f"Throughput: {docs_per_sec:,.0f} docs/sec overall, "
              f"{upload_docs_per_sec:,.0f} docs/sec upload phase")

        return total_loaded

    except Exception as e:
        print(f"Error in DuckDB bulk loading: {e}")
        return 0
    finally:
        try:
            if os.path.exists(snapshot_path):
                os.unlink(snapshot_path)
            wal = snapshot_path + '.wal'
            if os.path.exists(wal):
                os.unlink(wal)
        except OSError:
            pass


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
        ) TO '{output_file}' (FORMAT CSV, DELIMITER '\t', HEADER true)
        """
        
        conn.execute(query)
        
        # Count rows to return
        count_query = f"""
        SELECT COUNT(*) FROM read_csv_auto('{output_file}', header=true, ignore_errors=true)
        """
        count = conn.execute(count_query).fetchone()[0]
        
        conn.close()
        return count
    except Exception as e:
        print(f"Error creating CSV chunk starting at {chunk_start}: {e}")
        return 0

