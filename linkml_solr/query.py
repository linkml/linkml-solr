import logging
from typing import Union, Dict, Tuple, Type, List
import pysolr
from dataclasses import dataclass

from linkml_runtime.utils.formatutils import underscore
from linkml_model.meta import SchemaDefinition, ClassDefinition, YAMLRoot, ElementName, SlotDefinition

from linkml_solr.solrmodel import SolrEndpoint, SolrQuery, SolrQueryResult, RawSolrResult

from linkml_solr.mapper import LinkMLMapper

# https://stackoverflow.com/questions/1176136/convert-string-to-python-class-object
def class_for_name(module_name, class_name):
    # load the module, will raise ImportError if module cannot be loaded
    m = __import__(module_name, globals(), locals(), class_name)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, class_name)
    return c


@dataclass
class SolrQueryEngine(object):
    """
    ORM wrapper for SOLR endpoint
    """

    endpoint: SolrEndpoint
    schema: SchemaDefinition
    mapper: LinkMLMapper = None

    def __post_init__(self):
        if self.mapper is None:
            self.mapper = LinkMLMapper(schema=self.schema)
        if self.mapper.schema is None:
            self.mapper.schema = self.schema

    def query(self, target_class: Type[YAMLRoot] = None, **params) -> List[YAMLRoot]:
        """
        As search, but just returns items, discarding facet info etc
        :param target_class:
        :param params:
        :return:
        """
        return self.search(target_class, **params).items

    def search(self, target_class: Type[YAMLRoot] = None, **params) -> SolrQueryResult:
        """
        Query a SOLR endpoint for a list of objects

        :param target_class:
        :param params: key-value parameters. Keys should be in the schema
        :return:
        """
        sq = self.generate_query(**params)
        rawres = self.execute(sq)
        items = [self.fetch_object(row, sq, target_class=target_class) for row in rawres.docs]
        return SolrQueryResult(items=items)

    def generate_query(self, **params) -> SolrQuery:
        """
        Generate a solr query given query parameters

        :param prefixmap:
        :param params:
        :return:
        """
        sq = SolrQuery(prefixmap={})
        self._generate_query_for_params(sq, params)
        return sq

    def _generate_query_for_params(self, sq: SolrQuery, params: Dict) -> None:
        schema = self.schema
        mapper = self.mapper
        for sn, v in params.items():
            slot = mapper._get_slot(sn)
            if slot is not None:
                slot_range = slot.range
            else:
                slot_range = None
                logging.error(f'Unknown slot name: {sn}')
            solr_prop = mapper._slot_to_solr_prop(slot, sq.prefixmap)
            solr_val = mapper.pyval_to_solr_atom(v, range=slot_range, query=sq)
            sq.add_constraint(solr_prop, solr_val)

    def fetch_object(self, row: Dict,
                     original_query: SolrQuery = None,
                     target_class: Type[YAMLRoot] = None) -> YAMLRoot:
        """
        Given an ID, query out other fields and populate object
        :param row:
        :param original_query:
        :param target_class:
        :return:
        """
        mapper = self.mapper
        new_obj = {}
        for k, v in row.items():
            if v is not None and v != []:
                new_obj[k] = v
        cls = mapper._get_linkml_class(new_obj)
        if cls is None:
            cls = target_class
        return cls(**new_obj)

    def execute(self, query: SolrQuery) -> RawSolrResult:
        """
        Execute a solr query on endpoint

        Endpoint can be an in-memory graph or remote endpoint

        :param query:
        :return:
        """
        #solr = pysolr.Solr(self.endpoint.url, **solr_params)
        solr = pysolr.Solr(self.endpoint.url)
        params = query.http_params()
        print(params)
        results = solr.search('*:*', **params)
        print(results.docs)
        return results

