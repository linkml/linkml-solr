
from dataclasses import dataclass
from typing import Dict, List, Any, Optional

from linkml_runtime.linkml_model.meta import YAMLRoot

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
    facet_fields: List[FIELD] = None
    filter_query: Dict[FIELD, Any] = None
    other_params: Dict[str, Any] = None
    search_term: str = '*:*'
    rows: int = 100

    def http_params(self) -> dict:
        params = {'rows': self.rows}
        if self.other_params is not None:
            for k, v in self.other_params.items():
                params[k] = v
        if self.filter_query is None:
            self.filter_query = {}
        params['fq'] = [f'{k}:{_quote(v)}' for (k,v) in self.filter_query.items()]
        if self.facet_fields is not None:
            params['facet'] = 'on'
            params['facet.field'] = self.facet_fields
            params['facet.limit'] = 25
            params['facet.mincount'] = 1
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
    start: int = 0
    items: List[YAMLRoot] = None
    facet_counts: Dict = None
    highlighting: str = None
    raw: Any = None
    response: Any = None

    def __post_init__(self):
        if self.response.facets is not None:
            ffs = self.response.facets.get('facet_fields', {})
            facet_counts = {}
            for slot, counts in ffs.items():
                facet_counts[slot] = {term: count for term, count in zip(*[iter(counts)]*2)}
            self.facet_counts = facet_counts


def _quote(v, operator="OR"):
    if isinstance(v, list):
        if len(v) == 1:
            return _quote(v[0], operator)
        else:
            v2 = f" {operator} ".join([_quote(x) for x in v])
            return f'({v2})'
    else:
        return f'"{v}"'
