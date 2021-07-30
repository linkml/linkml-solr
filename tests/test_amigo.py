import os
import unittest

from linkml_runtime.dumpers import json_dumper, rdf_dumper
from linkml_runtime.loaders import yaml_loader
from linkml.generators.yamlgen import YAMLGenerator
from tests.test_models.amigo import *
import tests.test_models.amigo as amigo

from tests import INPUT_DIR, MODEL_DIR

from linkml_solr import SolrQueryEngine, SolrEndpoint
from SPARQLWrapper import SPARQLWrapper, N3
from rdflib import Graph

DATA = os.path.join(INPUT_DIR, 'kitchen_sink_inst_01.yaml')
CONTEXT = os.path.join(MODEL_DIR, 'kitchen_sink.context.jsonld')
SCHEMA = os.path.join(MODEL_DIR, 'amigo.yaml')

class QueryTestCase(unittest.TestCase):

    def test_query(self):
        """ solr """
        # TODO: use mock server
        schema = YAMLGenerator(SCHEMA).schema
        qe = SolrQueryEngine(schema=schema,
                             discriminator_field=amigo.slots.document_category.name,
                             endpoint=SolrEndpoint(url='http://golr.geneontology.org/solr/'))

        sq = qe.generate_query(document_category=OntologyClass.class_name, synonym='apoptosis')
        print(sq)
        print(sq.http_params())

        result = qe.search(target_class=OntologyClass, isa_partof_closure='GO:0031965') ## nuclear membrane
        #print(f'Result={result}')
        for oc in result.items:
            oc: OntologyClass
            print(f'Term: {oc.id} {oc.annotation_class_label}')




if __name__ == '__main__':
    unittest.main()
