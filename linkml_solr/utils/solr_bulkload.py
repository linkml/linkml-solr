from typing import List
import logging
import subprocess
from linkml.generators.yamlgen import YAMLGenerator
from linkml_runtime.linkml_model.meta import SchemaDefinition, SlotDefinitionName
from linkml_runtime.loaders import yaml_loader
from linkml_solr import SolrQueryEngine, SolrEndpoint

def _get_multivalued_slots(schema: SchemaDefinition) -> List[SlotDefinitionName]:
    return [s.name for s in schema.slots.values() if s.multivalued]


def bulkload_file(f,
                  format='csv',
                  base_url=None,
                  core=None,
                  schema: SchemaDefinition = None,
                  ):
    """
    Bulkload a file using solr bulkload API

    :param f:
    :param format:
    :param base_url:
    :param core:
    :param schema:
    :return:
    """
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

