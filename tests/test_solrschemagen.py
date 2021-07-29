import os
import unittest

from linkml_solr.solrschemagen import SolrSchemaGenerator
from tests.test_models.amigo import *
import tests.test_models.amigo as amigo

from tests import INPUT_DIR, MODEL_DIR

SCHEMA = os.path.join(MODEL_DIR, 'amigo.yaml')

class SolrSchemaGenTestCase(unittest.TestCase):

    def test_gen(self):
        """ generate a schema """
        gen = SolrSchemaGenerator(SCHEMA)
        s = gen.serialize()
        print(s)

if __name__ == '__main__':
    unittest.main()
