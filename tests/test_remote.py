import os
import unittest

from linkml_runtime.dumpers import json_dumper, rdf_dumper, yaml_dumper
from linkml.generators.yamlgen import YAMLGenerator
from tests.test_models.dbont import Food

from tests import INPUT_DIR, MODEL_DIR

from linkml_solr import QueryEngine, SolrEndpoint

CONTEXT = os.path.join(MODEL_DIR, 'dbont.context.jsonld')
SCHEMA = os.path.join(MODEL_DIR, 'dbont.yaml')

class RemoteQueryTestCase(unittest.TestCase):

    def test_remote(self):
        """ solr """
        schema = YAMLGenerator(SCHEMA).schema
        qe = QueryEngine(schema=schema,
                         endpoint=SolrEndpoint(url='http://dbpedia.org/solr/'),
                         lang='en')
        objs = qe.query(type=Food.class_class_curie,
                        origin='dbr:Scotland',
                        target_class=Food)
        for obj in objs:
            yaml = yaml_dumper.dumps(obj)
            print(f'xxObjs = {obj}')
            print(f'Y = {yaml}')
            if obj.label == 'Black Dog Scotch Whisky':
                found = True

        assert found




if __name__ == '__main__':
    unittest.main()
