import logging
from json import JSONDecodeError
from typing import Union, Dict, Tuple, Type, List
import pysolr
from dataclasses import dataclass
import json
import requests

from linkml_runtime.dumpers import json_dumper
from linkml_runtime.utils.formatutils import underscore
from linkml_runtime.linkml_model.meta import SchemaDefinition, ClassDefinition, YAMLRoot, ElementName, SlotDefinition, SlotDefinitionName

from linkml_solr.solrmodel import SolrEndpoint, SolrQuery, SolrQueryResult, RawSolrResult, FIELD
from linkml_solr.solrschema import Transaction
from linkml_solr.solrschemagen import SolrSchemaGenerator

from linkml_solr.mapper import LinkMLMapper

# https://stackoverflow.com/questions/1176136/convert-string-to-python-class-object
def class_for_name(module_name, class_name):
    # load the module, will raise ImportError if module cannot be loaded
    m = __import__(module_name, globals(), locals(), class_name)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, class_name)
    return c


# TODO: inherit from linkml_runtime_api.QueryEngine
@dataclass
class SolrQueryEngine(object):
    """
    ORM wrapper for SOLR endpoint
    """

    endpoint: SolrEndpoint
    schema: SchemaDefinition
    mapper: LinkMLMapper = None
    discriminator_field: SlotDefinitionName = None

    def __post_init__(self):
        # TODO: use schemaview
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

    def search(self, target_class: Type[YAMLRoot] = None,
               solr_params: Dict = None,
               search_term: str = '*:*',
               facet_fields: List[FIELD] = None,
               **params) -> SolrQueryResult:
        """
        Query a SOLR endpoint for a list of objects

        :param search_term:
        :param solr_params:
        :param target_class:
        :param params: key-value parameters. Keys should be in the schema
        :return:
        """
        sq = self.generate_query(target_class=target_class, **params)
        sq.other_params = solr_params
        sq.search_term = search_term
        sq.facet_fields = facet_fields
        rawres = self.execute(sq)
        items = [self.fetch_object(row, sq, target_class=target_class) for row in rawres.docs]
        return SolrQueryResult(items=items, response=rawres,
                               raw=rawres.raw_response,
                               start=rawres.raw_response['response']['start'],
                               num_found=rawres.hits)

    def generate_query(self, target_class: Type[YAMLRoot] = None, **params) -> SolrQuery:
        """
        Generate a solr query given query parameters

        :param prefixmap:
        :param params:
        :return:
        """
        sq = SolrQuery(prefixmap={})
        if target_class is not None:
            if self.discriminator_field is not None:
                params[self.discriminator_field] = target_class.class_name
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
        schema_class = self.schema.classes[target_class.class_name]
        for k, v in row.items():
            if k == '_version_':
                # TODO
                continue
            if v is not None and v != []:
                slot = mapper._lookup_slot(schema_class, k)
                if slot is None:
                    if k == 'id':
                        # autogen field
                        continue
                    else:
                        raise ValueError(f'Cannot retrieve slot for field {k}')
                if not slot.multivalued and isinstance(v, list):
                    if len(v) == 1:
                        v = v[0]
                    elif len(v) == 0:
                        v = None
                    else:
                        raise Exception(f'Multi-values for scalar field {schema_class.name}.{k} == {v} {len(v)}')
                new_obj[k] = v
        cls = mapper._get_linkml_class(new_obj)
        if cls is None:
            cls = target_class
        logging.debug(new_obj)
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
        #logging.info(params)
        print(f'Params={params}')
        results = solr.search(query.search_term, **params)
        if solr.session is not None:
            solr.session.close()
        return results

    def add(self, objs: List[YAMLRoot], commit=True):
        """
        Adds an instance of a LinkML class as a Solr document

        :param objs: list of objects to add
        :return:
        """
        jstrs = [json_dumper.dumps(obj, inject_type=False) for obj in objs]
        nu_objs = [json.loads(s) for s in jstrs]
        print(f'Adding = {nu_objs}')
        solr = pysolr.Solr(self.endpoint.url)
        r = solr.add(nu_objs)
        if commit:
            solr.commit()
        return r

    def delete_all(self, commit=True):
        """
        Deletes all documents in core

        :param commit:
        :return:
        """
        solr = pysolr.Solr(self.endpoint.url)
        solr.delete(q='*:*')
        if commit:
            solr.commit()

    def _solr_request(self, req: Dict, path='schema'):
        response = requests.post(f'{self.endpoint.url}/{path}',
                                 headers={"Content-Type": "application/json"},
                                 data=json.dumps(req, indent=' '))
        if response.status_code != 200:
            logging.error(f'Failed to execute {path} {req}: {response.status_code} :: {response.text}')
        return response

    def _solr_query(self, path='schema', strict=True):
        response = requests.get(f'{self.endpoint.url}/{path}',
                                 headers={"Content-Type": "application/json"})
        if response.status_code != 200:
            # TODO: raise exception
            logging.error(f'Failed to execute {path}: {response.status_code} :: {response.text}')
        return response

    def _response_json(self, response, strict=True):
        try:
            return response.json()
        except JSONDecodeError as e:
            if strict:
                raise JSONDecodeError(e)
            else:
                return {}

    def _get_fields(self, strict=True):
        response = self._solr_query(path='schema/fields', strict=strict)
        obj = self._response_json(response, strict=strict)
        return [f['name'] for f in obj.get('fields', [])]

    def _get_fieldtypes(self, strict=True):
        response = self._solr_query(path='schema/fieldtypes', strict=strict)
        obj = self._response_json(response, strict=strict)
        return [f['name'] for f in obj.get('fieldTypes', [])]

    def load_schema(self):
        """
        Adds a schema to SOLR corresponding to a LinkML schema
        """
        existing_fields = self._get_fields(strict=False)
        existing_fieldtypes = self._get_fieldtypes(strict=False)
        logging.info(f'Current Fields={existing_fields}')
        if 'int' not in existing_fieldtypes:
            self._solr_request({"add-field-type": {
                'name': 'int',
                'class': 'solr.TrieIntField',
                'precisionStep': "0",
                "positionIncrementGap": "0"
            }}, path='schema')
        if 'date' not in existing_fieldtypes:
            self._solr_request({"add-field-type": {
                'name': 'date',
                'class': 'solr.TrieDateField',
            }}, path='schema')
        gen = SolrSchemaGenerator(self.schema)
        gen.serialize()
        post_obj = gen.post_request
        for f in post_obj['add-field']:
            if f['name'] not in existing_fields:
                self._solr_request({'add-field': f}, path='schema')

