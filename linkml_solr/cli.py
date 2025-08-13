from typing import List
import click
import time
import logging
import subprocess

from linkml_runtime.dumpers import YAMLDumper
from linkml_runtime.linkml_model import SchemaDefinition
from linkml_runtime.loaders import yaml_loader
from linkml_solr import SolrQueryEngine, SolrEndpoint, DEFAULT_CORE, DEFAULT_SOLR_URL
from linkml_solr.utils.solr_bulkload import bulkload_file, bulkload_chunked
import requests


@click.group()
@click.option("-v", "--verbose", count=True)
@click.option("-q", "--quiet")
def main(verbose: int, quiet: bool):
    """LinkML-Solr utility commands

    Args:

        verbose (int): Verbose.
        quiet (bool): Quiet.

    Returns:

        None.

    """
    if verbose >= 2:
        logging.basicConfig(level=logging.DEBUG)
    elif verbose == 1:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)
    if quiet:
        logging.basicConfig(level=logging.ERROR)

@main.command()
@click.option('--schema', '-s',
              help='Path to schema.')
@click.option('--core', '-C',
              default=DEFAULT_CORE,
              show_default=True,
              help='solr core.')
@click.option('--format', '-f',
              type=click.Choice(['csv', 'json', 'cbor']),
              default='csv',
              show_default=True,
              help='input format.')
@click.option('--url', '-u',
              default=DEFAULT_SOLR_URL,
              help='solr url.')
@click.option('--processor', '-p',
              help='Processor argument to pass when bulk loading to Solr')
@click.option('--chunk-size', '-c',
              default=100000,
              show_default=True,
              help='Number of rows per chunk for large files')
@click.option('--parallel-workers', '-w',
              default=4,
              show_default=True,
              help='Number of parallel workers for chunked loading')
@click.option('--chunked/--no-chunked',
              default=False,
              show_default=True,
              help='Use chunked parallel loading for large files')
@click.option('--auto-configure/--no-auto-configure',
              default=True,
              show_default=True,
              help='Automatically configure Solr for optimal performance')
@click.option('--ram-buffer',
              default=2048,
              show_default=True,
              help='RAM buffer size in MB (used with auto-configure)')
@click.argument('files', nargs=-1)
def bulkload(files, format, schema, url, core, processor, chunk_size, parallel_workers, chunked, auto_configure, ram_buffer):
    """
    Bulk load files into Solr with optional chunking and performance optimization
    """
    if schema is not None:
        with open(schema) as stream:
            schema_obj = yaml_loader.load(stream, target_class=SchemaDefinition)
    else:
        schema_obj = None
    
    # Auto-configure Solr for performance if requested
    if auto_configure:
        print("Configuring Solr for optimal bulk loading performance...")
        configure_solr_performance(url, core, ram_buffer, disable_autocommit=True)
    
    total_loaded = 0
    
    try:
        for f in files:
            print(f"Processing file: {f}")
            
            if chunked and format in ['csv', 'cbor']:
                # Use chunked loading for large files
                docs_loaded = bulkload_chunked(
                    csv_file=f,
                    base_url=url,
                    core=core,
                    schema=schema_obj,
                    chunk_size=chunk_size,
                    max_workers=parallel_workers,
                    format=format,
                    processor=processor
                )
                total_loaded += docs_loaded
                print(f"Loaded {docs_loaded} documents from {f}")
            else:
                # Use standard bulkload
                bulkload_file(f, format=format, schema=schema_obj, core=core, base_url=url, processor=processor, commit=False)
                print(f"Loaded file {f}")
        
        # Commit all changes at the end
        print("Committing all changes...")
        if commit_solr(url, core):
            print(f"Successfully committed {total_loaded} documents to Solr")
        else:
            print("Warning: Commit may have failed")
            
    except Exception as e:
        print(f"Error during bulk loading: {e}")
        # Try to commit what we have
        commit_solr(url, core)
        raise

@main.command()
@click.option('--schema', '-s',
              help='Path to LinkML yaml schema.')
@click.option('--core', '-C',
              default=DEFAULT_CORE,
              show_default=True,
              help='name of solr core.')
@click.option('--container', '-n',
              default='my_solr',
              show_default=True,
              help='name of docker container')
@click.option('--port', '-P',
              default='8983',
              show_default=True,
              help='http port number on which solr rules.')
@click.option('--sleep',
              default=10,
              show_default=True,
              help='Number of seconds to sleep after initiating server start before exiting.')
@click.option('--create-schema/--no-create-schema',
              default=True,
              show_default=True,
              help='create the solr schema from the linkml schema on startup')
@click.option('--kill/--no-kill',
              default=True,
              show_default=True,
              help='kill and remove any existing container')
@click.option('--url', '-u',
              default=DEFAULT_SOLR_URL,
              show_default=True,
              help='solr url.')
@click.option('--memory', '-m',
              default='4g',
              show_default=True,
              help='Docker memory limit (e.g., 4g, 8g)')
@click.option('--heap-size', '-j',
              default='3g',
              show_default=True,
              help='JVM heap size (e.g., 2g, 4g)')
def start_server(schema, kill, container, url, core, port, sleep: int, create_schema, memory, heap_size):
    """
    Starts a solr server (via Docker)
    """
    if kill:
        subprocess.run(['docker', 'kill', container])
        subprocess.run(['docker', 'rm', container])
    command = [
        'docker',
        'run',
        '--name',
        container,
        '-p',
        f'{port}:{port}',
        '-m',
        memory,
        '-e',
        f'SOLR_JAVA_MEM=-Xms{heap_size} -Xmx{heap_size}',
        'solr:8',
        'solr-precreate',
        core]
    subprocess.Popen(command)
    print(f'Sleeping for {sleep} seconds to allow server time to initialize...')
    time.sleep(sleep)
    print(f'Done sleeping!')
    if create_schema and schema:
        # TODO: use SchemaView
        from linkml.generators.yamlgen import YAMLGenerator
        schema_obj = YAMLGenerator(schema).schema
        qe = SolrQueryEngine(schema=schema_obj,
                             endpoint=SolrEndpoint(url=f'{url}/{core}'))
        qe.load_schema()

@main.command()
@click.option('--schema', '-s',
              help='Path to LinkML yaml schema.')
@click.option('--container', '-n',
              default='my_solr',
              show_default=True,
              help='name of docker container')
@click.option('--port', '-P',
              default='8983',
              show_default=True,
              help='http port number on which solr rules.')
@click.option('--url', '-u',
              default=DEFAULT_SOLR_URL,
              show_default=True,
              help='solr url.')
@click.argument('cores', nargs=-1)
def add_cores(cores, schema, container, url, port):
    """
    Starts a solr server (via Docker)
    """
    for core in cores:
        command = [
            'docker',
            'exec',
            container,
            'solr',
            'create',
            '-c',
            core]
        subprocess.Popen(command)

@main.command()
@click.option('--schema', '-s',
              help='Path to schema.')
@click.option('--core', '-C',
              default=DEFAULT_CORE,
              show_default=True,
              help='solr core.')
@click.option('--url', '-u',
              default=DEFAULT_SOLR_URL,
              show_default=True,
              help='solr url.')
@click.option('--debug',
              default=False,
              is_flag=True,
              help='Print generated schema to stdout rather before loading into Solr.')
@click.option('--dry-run',
              default=False,
              is_flag=True,
              help='Generate schema but do not load into Solr.')
@click.option('--top-class', '-t',
              default=None,
              show_default=True,
              help='Solr document in this core is one instance of this class')
def create_schema(schema, url, core, debug, dry_run, top_class):
    """
    Creates a solr schema from a LinkML schema
    """
    # TODO: use schemaview
    from linkml.generators.yamlgen import YAMLGenerator
    schema_obj = YAMLGenerator(schema).schema
    qe = SolrQueryEngine(schema=schema_obj,
                         endpoint=SolrEndpoint(url=f'{url}/{core}'),
                         top_class=top_class)
    gen = qe.load_schema(dry_run=dry_run,)
    if debug:
        print(gen.serialize())


def configure_solr_performance(url, core, ram_buffer_mb=2048, disable_autocommit=True):
    """
    Configure Solr for optimal bulk loading performance
    """
    config_url = f"{url}/{core}/config"
    
    if disable_autocommit:
        # Disable autocommit
        response = requests.post(config_url, 
                               headers={'Content-type': 'application/json'},
                               json={
                                   "set-property": {
                                       "updateHandler.autoCommit.maxTime": -1,
                                       "updateHandler.autoSoftCommit.maxTime": -1
                                   }
                               })
        print(f"Disabled autocommit: {response.status_code}")
    
    # Set RAM buffer size
    response = requests.post(config_url,
                           headers={'Content-type': 'application/json'},
                           json={
                               "set-property": {
                                   "updateHandler.indexConfig.ramBufferSizeMB": ram_buffer_mb
                               }
                           })
    print(f"Set RAM buffer to {ram_buffer_mb}MB: {response.status_code}")


def commit_solr(url, core):
    """
    Commit changes to Solr
    """
    commit_url = f"{url}/{core}/update?commit=true"
    response = requests.post(commit_url)
    print(f"Committed changes: {response.status_code}")
    return response.status_code == 200


@main.command()
@click.option('--url', '-u',
              default=DEFAULT_SOLR_URL,
              help='solr url.')
@click.option('--core', '-C',
              default=DEFAULT_CORE,
              help='solr core.')
@click.option('--ram-buffer',
              default=2048,
              help='RAM buffer size in MB.')
@click.option('--enable/--disable',
              default=False,
              help='Enable or disable autocommit.')
def configure_performance(url, core, ram_buffer, enable):
    """
    Configure Solr performance settings for bulk loading
    """
    configure_solr_performance(url, core, ram_buffer, not enable)


if __name__ == '__main__':
    main()
