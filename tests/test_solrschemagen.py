import json
import os
import unittest

from linkml_solr.solrschemagen import SolrSchemaGenerator
from linkml.utils.schema_builder import SchemaBuilder

from tests.test_models.amigo import *
import tests.test_models.amigo as amigo

from tests import INPUT_DIR, MODEL_DIR

SCHEMA = os.path.join(MODEL_DIR, 'amigo.yaml')
KITCHEN_SINK_SCHEMA = os.path.join(MODEL_DIR, 'kitchen_sink.yaml')

class SolrSchemaGenTestCase(unittest.TestCase):
    """
    Tests solr schema generation

    Does not require a solr service to be running
    """

    def test_gensolrschema(self):
        """ generate a flattened schema """
        gen = SolrSchemaGenerator(SCHEMA)
        gen.serialize()
        s = gen.post_request
        #print(s)
        fields = s['add-field']
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


    def test_top_class(self):
        sb = SchemaBuilder("single-class-test-schema")
        sb.add_slot("slot_one", range="string")
        sb.add_slot("slot_two", range="string")
        sb.add_class("ClassOne", ["slot_one"])
        sb.add_class("ClassTwo", ["slot_two"])
        gen = SolrSchemaGenerator(sb.schema)
        s = gen.class_schema("ClassOne")
        doc = json.loads(s)
        fields = doc['add-field']
        assert('slot_one' in [f['name'] for f in fields])
        assert('slot_two' not in [f['name'] for f in fields])


    def test_inlined_class_slot_is_stored_json_string(self):
        """Solr reads a JSON object in a doc as a child document, so an inlined
        class slot becomes a stored, unindexed string field (one JSON string per
        record); a non-inlined class slot stays a plain string reference."""
        sb = SchemaBuilder("inlined-test-schema")
        sb.add_slot("id", range="string", identifier=True)
        sb.add_slot("resource_id", range="string")
        sb.add_class("Source", ["id", "resource_id"])
        sb.add_slot("sources", range="Source", multivalued=True, inlined_as_list=True)
        sb.add_slot("source_ref", range="Source", multivalued=True, inlined=False)
        sb.add_class("Association", ["sources", "source_ref"])
        gen = SolrSchemaGenerator(sb.schema)
        fields = {f['name']: f for f in json.loads(gen.class_schema("Association"))['add-field']}
        assert fields['sources'] == {
            "name": "sources",
            "type": "string",
            "stored": "true",
            "indexed": "false",
            "multiValued": True,
            "docValues": False,
        }
        assert fields['source_ref'] == {"name": "source_ref", "type": "string", "multiValued": True}



if __name__ == '__main__':
    unittest.main()
