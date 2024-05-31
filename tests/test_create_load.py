import os
import unittest

import pysolr
import requests

from linkml_runtime.dumpers import json_dumper, rdf_dumper
from linkml_runtime.loaders import yaml_loader, tsv_loader
from linkml.generators.yamlgen import YAMLGenerator
from linkml_runtime.utils.schemaview import SchemaView

from tests.test_models.gencc import GeneToDiseaseAssociation, Container
import tests.test_models.books as amigo


from tests import INPUT_DIR, MODEL_DIR

from linkml_solr import SolrQueryEngine, SolrEndpoint, DEFAULT_CORE
from linkml_solr import DEFAULT_SOLR_URL
from SPARQLWrapper import SPARQLWrapper, N3
from rdflib import Graph

SCHEMA = os.path.join(MODEL_DIR, 'gencc.yaml')
DATA = os.path.join(INPUT_DIR, 'gencc_example.tsv')

URL = f'{DEFAULT_SOLR_URL}/{DEFAULT_CORE}'

class CreateLoadTestCase(unittest.TestCase):
    """
    This test requires a solr instance running, with the test core precreated.

    Do this:

    make test-server
    make add-test-core
    """

    def test_create_load(self):
        """ tests full cycle """
        schema = YAMLGenerator(SCHEMA).schema
        sv = SchemaView(schema)
        qe = SolrQueryEngine(schema=schema,
                             endpoint=SolrEndpoint(url=URL))
        qe.load_schema()
        qe.delete_all()
        a = GeneToDiseaseAssociation(gene_symbol='foo')
        qe.add([a])
        results = qe.query(target_class=GeneToDiseaseAssociation)
        assert len(results) == 1
        container = tsv_loader.load(DATA, schemaview=sv, index_slot='associations', target_class=Container)
        print(f'ASSOCS={len(container.associations)}')
        assert len(container.associations) > 50
        qe.add(container.associations)
        results = qe.query(target_class=GeneToDiseaseAssociation, gene_symbol='MED12L')
        print(results)
        assert len(results) == 1
        FACET_FIELDS = ['moi_title', 'classification_title']
        result = qe.search(target_class=GeneToDiseaseAssociation,
                           facet_fields=FACET_FIELDS)
        for ff in FACET_FIELDS:
            print(f'FC[{ff}]={result.facet_counts[ff]}')



if __name__ == '__main__':
    unittest.main()
