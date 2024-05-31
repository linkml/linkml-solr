import logging
import os
import unittest
import requests

from linkml_runtime.dumpers import json_dumper, rdf_dumper
from linkml_runtime.loaders import yaml_loader
from linkml.generators.yamlgen import YAMLGenerator
from tests.test_models.books import *
import tests.test_models.books as amigo

from tests import INPUT_DIR, MODEL_DIR

from linkml_solr import SolrQueryEngine, SolrEndpoint
from linkml_solr.utils.solr_bulkload import bulkload_file

from SPARQLWrapper import SPARQLWrapper, N3
from rdflib import Graph

SCHEMA = os.path.join(MODEL_DIR, 'books.yaml')


@unittest.skip("skipping test_query, since it requires a solr instance already loaded with books")
class QueryTestCase(unittest.TestCase):
    """
    This test requires a solr instance running - see the Makefile
    for running in Docker
    """

    def test_query(self):
        """ tests querying from and adding to a solr endpoint """

        schema = YAMLGenerator(SCHEMA).schema

        qe = SolrQueryEngine(schema=schema,
                             endpoint=SolrEndpoint(url='http://localhost:8983/solr/books'))
        gen = qe.load_schema()
        bulkload_file(INPUT_DIR + '/books.json', format='json', schema=schema, core='books', base_url='http://localhost:8983/solr')
        sq = qe.generate_query(genre_s='fantasy')
        print(sq)
        print(sq.http_params())

        result = qe.search(target_class=Book, genre_s='scifi')
        logging.info(f'Result={result}')
        for book in result.items:
            print(f'Book:  {book.name} :: {book}')
        assert len(result.items) > 2

        book = Book(id='B1', name='made up book name2')

        qe.add([book])
        result = qe.search(target_class=Book, name=book.name)
        logging.info(f'Result={result}')
        print(f'ITEMS={result.items}')
        for book in result.items:
            print(f'Book2:  {book.name} :: {book}')
        assert len(result.items) >= 1






if __name__ == '__main__':
    unittest.main()
