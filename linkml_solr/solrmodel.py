
from dataclasses import dataclass
from typing import Dict, List, Any, Optional

from linkml_model.meta import YAMLRoot

PREFIXMAP = Dict[str, str]
FIELD = str
RawSolrResult = Dict


@dataclass
class SolrEndpoint(object):
    url: Optional[str] = None
    type_property: str = 'type'


@dataclass
class SolrQuery:
    prefixmap: PREFIXMAP = None
    fields: List[FIELD] = None
    filter_query: Dict[FIELD, Any] = None

    def http_params(self) -> dict:
        params = {}
        params['fq'] = [f'{k}:{_quote(v)}' for (k,v) in self.filter_query.items()]
        if self.fields is not None:
            params['fields'] = ','.join(self.fields)
        return params

    def add_constraint(self, solr_prop, solr_val):
        if self.filter_query is None:
            self.filter_query = {}
        self.filter_query[solr_prop] = solr_val


@dataclass
class SolrQueryResult:
    num_found: int = 0
    items: List[YAMLRoot] = None
    facet_counts: Dict = None
    highlighting: str = None


def _quote(v, operator="OR"):
    if isinstance(v, list):
        if len(v) == 1:
            return _quote(v[0], operator)
        else:
            v2 = f" {operator} ".join([_quote(x) for x in v])
            return f'({v2})'
    else:
        return f'"{v}"'
