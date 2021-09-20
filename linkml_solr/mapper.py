import logging

from linkml_runtime.utils.formatutils import underscore
from linkml_runtime.linkml_model.meta import SchemaDefinition, ClassDefinition, YAMLRoot, ElementName, SlotDefinition
from rdflib import BNode, URIRef, Literal
from rdflib.term import Node

from linkml_solr.solrmodel import *

ASSERTED_TYPE_FIELD = '_type'


@dataclass
class Mapper(object):
    """
    Maps between URIs and RDF/SOLR entities and Python datamodel entities
    """
    None

@dataclass
class LinkMLMapper(Mapper):
    """
    LinkML Mapper
    """

    schema: SchemaDefinition

    def _get_slot(self, sn: str) -> Optional[SlotDefinition]:
        for slot in self.schema.slots.values():
            if underscore(slot.name) == sn:
                return slot


    def _get_python_field_for_slot(self, slot: SlotDefinition) -> str:
        return underscore(slot.name) # TODO: map to pythongen

    def pyval_to_solr_atom(self, v: Any, range: ElementName = None, query: SolrQuery = None) -> str:
        return str(v)

    def _get_linkml_class(self, in_obj: Dict) -> str:
        if ASSERTED_TYPE_FIELD in in_obj:
            cn = in_obj[ASSERTED_TYPE_FIELD]
            return self.schema.classes[cn]
        else:
            return None

    def _instance_of_linkml_class(self, v) -> bool:
        try:
            type(v).class_name
            return True
        except:
            return False

    def _lookup_slot(self, cls: ClassDefinition, field: str):
        for sn in cls.slots:
            s: SlotDefinition
            s = self.schema.slots[sn]
            if underscore(s.name) == field:
                return s
            if s.alias and underscore(s.alias) == field:
                return s
        logging.error(f'Did not find {field} in {cls.name} slots =  {cls.slots}')

    def _slot_to_solr_prop(self, slot, prefixmap):
        # TODO: allow mapping
        return underscore(slot.name)
