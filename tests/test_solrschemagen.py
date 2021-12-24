import json
import os
import unittest

from linkml_solr.solrschemagen import SolrSchemaGenerator
from tests.test_models.amigo import *
import tests.test_models.amigo as amigo

from tests import INPUT_DIR, MODEL_DIR

SCHEMA = os.path.join(MODEL_DIR, 'amigo.yaml')

class SolrSchemaGenTestCase(unittest.TestCase):
    """
    Tests solr schema generation

    Does not require a solr service to be running
    """

    def test_gensolrschema(self):
        """ generate a flattened schema """
        gen = SolrSchemaGenerator(SCHEMA)
        s = gen.serialize()
        #print(s)
        doc = json.loads(s)
        fields = doc['add-field']
        test_fields = [
            {
                "name": "alternate_id",
                "type": "string",
                "multiValued": True
            },
            {
                "name": "taxon",
                "type": "string",
                "multiValued": False
            },
            {
                "name": "id",
                "type": "string",
                "multiValued": False
            }
        ]
        for field in test_fields:
            assert field in fields
        print(f'NUM = {len(fields)}')
        assert len(fields) > 150

    def test_gensolrschema_single_class(self):
        """ generate a schema for a single class"""
        gen = SolrSchemaGenerator(SCHEMA)
        s = gen.class_schema('annotation')
        doc = json.loads(s)
        fields = doc['add-field']
        print(f'NUM = {len(fields)}')
        test_fields = [
            {
                "name": "id",
                "type": "string",
                "multiValued": False
            }
        ]
        for field in test_fields:
            assert field in fields
        field_names = [f['name'] for f in fields]
        not_in = ['enabled_by']
        for x in not_in:
            assert x not in field_names


if __name__ == '__main__':
    unittest.main()
