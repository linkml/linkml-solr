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
from SPARQLWrapper import SPARQLWrapper, N3
from rdflib import Graph

SCHEMA = os.path.join(MODEL_DIR, 'books.yaml')

class QueryTestCase(unittest.TestCase):

    def test_query(self):
        """ solr """
        schema = YAMLGenerator(SCHEMA).schema
        qe = SolrQueryEngine(schema=schema,
                             #discriminator_field=amigo.slots.document_category.name,
                             endpoint=SolrEndpoint(url='http://localhost:8983/solr/books'))
        #qe.create_schema()
        sq = qe.generate_query(genre_s='fantasy')
        print(sq)
        print(sq.http_params())

        result = qe.search(target_class=Book, genre_s='scifi')
        #result = qe.search(target_class=Book)
        #print(f'Result={result}')
        for book in result.items:
            print(f'Book:  {book.name} :: {book}')
        assert len(result.items) > 2

        book = Book(id='B1', name='bar')

        qe.add([book])
        import pysolr
        solr = pysolr.Solr(qe.endpoint.url, always_commit=True)
        solr.ping()
        solr.add([{'id': 'xxx', 'foo': 'baz'}])
        x = solr.add([{'id': 'zzz', 'name': ['baz']}])
        import json
        rj = {"add": {"doc": [
                          {"id": 14,
                           "log_type": "debug",
                           "log_text": "A transaction of debug from Kimy"}],
                      "boost": 1.0,
                      "overwrite": True,
                      "commitWithin": 1000}}
        rj = [
            {"id": 14,
             "log_type": "debug",
             "log_text": "A transaction of debug from Kimy"}]
        rjs = json.dumps(rj)
        status = requests.post("http://localhost:8983/solr/books/update",
                      headers={"Content-Type": "application/json"},
                      data=rjs)
        print(f'Status={status} {status.text}')
        #solr.delete(q='*:*')
        solr.commit()
        results = solr.search('*:*', rows=100)
        print(results)
        print(results.docs)
        print(results.docs[-1])
        print(len(results.docs))
        print(x)
        solr.commit()






if __name__ == '__main__':
    unittest.main()
