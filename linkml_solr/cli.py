from typing import List
import click
import logging
import subprocess
from linkml.generators.yamlgen import YAMLGenerator
from linkml_runtime.linkml_model.meta import SchemaDefinition, SlotDefinitionName
from linkml_runtime.loaders import yaml_loader
from linkml_solr import SolrQueryEngine, SolrEndpoint, DEFAULT_CORE, DEFAULT_SOLR_URL
from linkml_solr.utils.solr_bulkload import bulkload_file


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
              default='csv',
              show_default=True,
              help='input format.')
@click.option('--url', '-u',
              default=DEFAULT_SOLR_URL,
              help='solr url.')
@click.argument('files', nargs=-1)
def bulkload(files, format, schema, url, core):
    """
    Convert multiple golr yaml schemas to linkml
    """
    inputs = {}
    if schema is not None:
        with open(schema) as stream:
            schema_obj = yaml_loader.load(stream, target_class=SchemaDefinition)
    for f in files:
        bulkload_file(f, format=format, schema=schema_obj, core=core, base_url=url)

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
def start_server(schema, kill, container, url, core, port, create_schema):
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
        'solr:8',
        'solr-precreate',
        core]
    subprocess.Popen(command)
    if create_schema and schema:
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
def create_schema(schema, url, core):
    """
    Creates a solr schema from a LinkML schema
    """
    schema_obj = YAMLGenerator(schema).schema
    qe = SolrQueryEngine(schema=schema_obj,
                         endpoint=SolrEndpoint(url=f'{url}/{core}'))
    qe.load_schema()


if __name__ == '__main__':
    main()
