import logging
import os
import unittest

from linkml.generators.yamlgen import YAMLGenerator
from tests.test_models.amigo import *
from tests.test_models.amigo_api import AmigoSolrAPI
import tests.test_models.amigo as amigo
import linkml_dataops

from tests import INPUT_DIR, MODEL_DIR

from linkml_solr import SolrQueryEngine, SolrEndpoint
from SPARQLWrapper import SPARQLWrapper, N3
from rdflib import Graph

DATA = os.path.join(INPUT_DIR, 'kitchen_sink_inst_01.yaml')
CONTEXT = os.path.join(MODEL_DIR, 'kitchen_sink.context.jsonld')
SCHEMA = os.path.join(MODEL_DIR, 'amigo.yaml')
NUCLEAR_MEMBRANE = 'GO:0031965'
NUCLEUS = 'GO:0005634'
MEMBRANE = 'GO:0016020'
PROTEIN_COMPLEX = 'GO:0032991'

class QueryTestCase(unittest.TestCase):

    def setUp(self) -> None:
        schema = YAMLGenerator(SCHEMA).schema
        qe = SolrQueryEngine(schema=schema,
                             discriminator_field=amigo.slots.document_category.name,
                             python_classes=[OntologyClass],
                             endpoint=SolrEndpoint(url='http://golr.geneontology.org/solr/'))
        self.sqe = qe

    def test_query(self):
        """ solr """
        # TODO: use mock server
        qe = self.sqe
        sq = qe.generate_query(document_category=OntologyClass.class_name, synonym='apoptosis')
        sq.facet_fields = ['isa_partof_closure']
        #print(sq)
        #print(sq.http_params())
        result = qe.search(target_class=OntologyClass,
                           facet_fields=['isa_partof_closure'],
                           isa_partof_closure=NUCLEAR_MEMBRANE) ## nuclear membrane
        assert len(result.items) > 0
        for oc in result.items:
            oc: OntologyClass
            print(f'Term: {oc.id} {oc.annotation_class_label}')
        logging.info(result.raw)
        for slt, countdict in result.facet_counts.items():
            print(f' FACET {slt}: {countdict}')
        for k, v in result.response.__dict__.items():
            logging.info(f'  *** {k} = {v}')
        for k, v in result.raw.items():
            logging.info(f'  RAW *** {k} = {v}')
        for k, v in result.raw['response'].items():
            logging.info(f'  RESPONSE >>>> {k} = {v}')
        #for x in result.facet_counts:
        #    print(f'Facet={x}')

    def test_intersection_query(self):
        qe = self.sqe
        result = qe.search(target_class=OntologyClass,
                           isa_partof_closure=[NUCLEUS, MEMBRANE, PROTEIN_COMPLEX])
        assert len(result.items) > 0
        n = 0
        for oc in result.items:
            oc: OntologyClass
            print(f'Term: {oc.id} {oc.annotation_class_label}')
            if oc.id == 'GO:0106083':
                n += 1
        assert n == 1

    def test_api(self):
        schema = YAMLGenerator(SCHEMA).schema
        qe = SolrQueryEngine(schema=schema,
                             discriminator_field=amigo.slots.document_category.name,
                             python_classes=[OntologyClass],
                             endpoint=SolrEndpoint(url='http://golr.geneontology.org/solr/'))
        qe = self.sqe
        api = AmigoSolrAPI(query_engine=qe)
        c = api.fetch_OntologyClass(NUCLEAR_MEMBRANE)
        print(c)
        self.assertEqual('nuclear membrane', c.annotation_class_label)
        self.assertEqual(NUCLEAR_MEMBRANE, c.annotation_class)
        results = list(api.query_OntologyClass(isa_partof_closure=[NUCLEAR_MEMBRANE, PROTEIN_COMPLEX]))
        for r in results:
            print(f'{r.id} {r.annotation_class_label}')
        assert len(results) > 1


if __name__ == '__main__':
    unittest.main()
