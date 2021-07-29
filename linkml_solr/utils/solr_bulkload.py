from typing import List
import click
import logging
import subprocess
from linkml.generators.yamlgen import YAMLGenerator
from linkml_model.meta import SchemaDefinition, SlotDefinitionName
from linkml_runtime.loaders import yaml_loader
from linkml_solr import SolrQueryEngine, SolrEndpoint

def _get_multivalued_slots(schema: SchemaDefinition) -> List[SlotDefinitionName]:
    return [s.name for s in schema.slots.values() if s.multivalued]


def bulkload_file(f,
                  format='csv',
                  base_url=None,
                  core=None,
                  schema: SchemaDefinition =None,
                  ):
    mvslots = _get_multivalued_slots(schema)
    print(f'MV = {mvslots}')
    separator = '%09'
    internal_separator = '%7C'
    parts = [f'f.{s}.split=true&f.{s}.separator={internal_separator}' for s in mvslots]
    url = f'{base_url}/{core}/update?{"&".join(parts)}&commit=true&separator={separator}'
    if format == 'csv':
        ct = 'application/csv'
    elif format == 'json':
        ct = 'application/json'
    else:
        raise Exception(f'Unknown format {format}')
    command = ['curl', url, '--data-binary', f'@{f}', '-H', f'Content-type:{ct}']
    print(command)
    subprocess.run(command)

@click.group()
@click.option("-v", "--verbose", count=True)
@click.option("-q", "--quiet")
def main(verbose: int, quiet: bool):
    """Main

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
              default='linkml-solr-test',
              help='solr core.')
@click.option('--format', '-f',
              default='csv',
              help='input format.')
@click.option('--url', '-u',
              default='http://localhost:8983/solr',
              help='solr url.')
@click.argument('files', nargs=-1)
def bulkload(files, format, schema, url, core):
    """
    Convert multiple golr yaml schemas to linkml
    :param files:
    :param schema:
    :return:
    """
    inputs = {}
    if schema is not None:
        with open(schema) as stream:
            schema_obj = yaml_loader.load(stream, target_class=SchemaDefinition)
    for f in files:
        bulkload_file(f, format=format, schema=schema_obj, core=core, base_url=url)

@main.command()
@click.option('--schema', '-s',
              help='Path to schema.')
@click.option('--core', '-C',
              default='linkml-solr-test',
              help='solr core.')
@click.option('--container', '-n',
              default='my_solr',
              help='solr core.')
@click.option('--port', '-P',
              default='8983',
              help='solr core.')
@click.option('--create-schema/--no-create-schema',
              default=True,
              help='create the solr schema from the linkml schema on startup')
@click.option('--url', '-u',
              default='http://localhost:8983/solr',
              help='solr url.')
def start_server(schema, container, url, core, port, create_schema):
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
    if create_schema:
        schema_obj = YAMLGenerator(schema).schema
        qe = SolrQueryEngine(schema=schema_obj,
                             endpoint=SolrEndpoint(url=f'{url}/{core}'))
        qe.create_schema()

@main.command()
@click.option('--schema', '-s',
              help='Path to schema.')
@click.option('--core', '-C',
              default='linkml-solr-test',
              help='solr core.')
@click.option('--url', '-u',
              default='http://localhost:8983/solr',
              help='solr url.')
def create_schema(schema, url, core):
    schema_obj = YAMLGenerator(schema).schema
    qe = SolrQueryEngine(schema=schema_obj,
                         endpoint=SolrEndpoint(url=f'{url}/{core}'))
    qe.create_schema()


if __name__ == '__main__':
    main()