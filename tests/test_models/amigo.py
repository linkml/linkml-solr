# Auto generated from amigo.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-07-23 17:49
# Schema: None
#
# id: https://w3id.org//None
# description: TODO
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NONE = CurieNamespace('None', 'http://kbase.us/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://w3id.org//None/')


# Types
class SearchableString(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "SearchableString"
    type_model_uri = URIRef("https://w3id.org//None/SearchableString")


# Class references



@dataclass
class Annotation(YAMLRoot):
    """
    Associations between GO terms and genes or gene products.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/Annotation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "annotation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/Annotation")

    document_category: Optional[str] = None
    id: Optional[str] = None
    source: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    assigned_by: Optional[str] = None
    is_redundant_for: Optional[str] = None
    taxon: Optional[str] = None
    taxon_label: Optional[Union[str, SearchableString]] = None
    taxon_label_searchable: Optional[Union[str, SearchableString]] = None
    taxon_closure: Optional[Union[str, List[str]]] = empty_list()
    taxon_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    taxon_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    taxon_subset_closure: Optional[Union[str, List[str]]] = empty_list()
    taxon_subset_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    taxon_subset_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    secondary_taxon: Optional[str] = None
    secondary_taxon_label: Optional[Union[str, SearchableString]] = None
    secondary_taxon_label_searchable: Optional[Union[str, SearchableString]] = None
    secondary_taxon_closure: Optional[Union[str, List[str]]] = empty_list()
    secondary_taxon_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    secondary_taxon_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    isa_partof_closure: Optional[Union[str, List[str]]] = empty_list()
    isa_partof_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    isa_partof_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    regulates_closure: Optional[Union[str, List[str]]] = empty_list()
    regulates_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    regulates_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    has_participant_closure: Optional[Union[str, List[str]]] = empty_list()
    has_participant_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    has_participant_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    synonym: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    synonym_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    bioentity: Optional[str] = None
    bioentity_label: Optional[Union[str, SearchableString]] = None
    bioentity_label_searchable: Optional[Union[str, SearchableString]] = None
    bioentity_name: Optional[Union[str, SearchableString]] = None
    bioentity_name_searchable: Optional[Union[str, SearchableString]] = None
    bioentity_internal_id: Optional[str] = None
    qualifier: Optional[Union[str, List[str]]] = empty_list()
    annotation_class: Optional[str] = None
    annotation_class_label: Optional[Union[str, SearchableString]] = None
    annotation_class_label_searchable: Optional[Union[str, SearchableString]] = None
    aspect: Optional[str] = None
    bioentity_isoform: Optional[str] = None
    evidence_type: Optional[str] = None
    evidence_type_closure: Optional[Union[str, List[str]]] = empty_list()
    evidence_with: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    evidence_with_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    evidence: Optional[str] = None
    evidence_label: Optional[Union[str, SearchableString]] = None
    evidence_label_searchable: Optional[Union[str, SearchableString]] = None
    evidence_closure: Optional[Union[str, List[str]]] = empty_list()
    evidence_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    evidence_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    evidence_subset_closure: Optional[Union[str, List[str]]] = empty_list()
    evidence_subset_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    evidence_subset_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    reference: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    reference_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    annotation_extension_class: Optional[Union[str, List[str]]] = empty_list()
    annotation_extension_class_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    annotation_extension_class_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    annotation_extension_class_closure: Optional[Union[str, List[str]]] = empty_list()
    annotation_extension_class_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    annotation_extension_class_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    annotation_extension_json: Optional[Union[str, List[str]]] = empty_list()
    panther_family: Optional[Union[str, SearchableString]] = None
    panther_family_searchable: Optional[Union[str, SearchableString]] = None
    panther_family_label: Optional[Union[str, SearchableString]] = None
    panther_family_label_searchable: Optional[Union[str, SearchableString]] = None
    geospatial_x: Optional[Union[int, List[int]]] = empty_list()
    geospatial_y: Optional[Union[int, List[int]]] = empty_list()
    geospatial_z: Optional[Union[int, List[int]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.document_category is not None and not isinstance(self.document_category, str):
            self.document_category = str(self.document_category)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.date is not None and not isinstance(self.date, str):
            self.date = str(self.date)

        if self.assigned_by is not None and not isinstance(self.assigned_by, str):
            self.assigned_by = str(self.assigned_by)

        if self.is_redundant_for is not None and not isinstance(self.is_redundant_for, str):
            self.is_redundant_for = str(self.is_redundant_for)

        if self.taxon is not None and not isinstance(self.taxon, str):
            self.taxon = str(self.taxon)

        if self.taxon_label is not None and not isinstance(self.taxon_label, SearchableString):
            self.taxon_label = SearchableString(self.taxon_label)

        if self.taxon_label_searchable is not None and not isinstance(self.taxon_label_searchable, SearchableString):
            self.taxon_label_searchable = SearchableString(self.taxon_label_searchable)

        if not isinstance(self.taxon_closure, list):
            self.taxon_closure = [self.taxon_closure] if self.taxon_closure is not None else []
        self.taxon_closure = [v if isinstance(v, str) else str(v) for v in self.taxon_closure]

        if not isinstance(self.taxon_closure_label, list):
            self.taxon_closure_label = [self.taxon_closure_label] if self.taxon_closure_label is not None else []
        self.taxon_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.taxon_closure_label]

        if not isinstance(self.taxon_closure_label_searchable, list):
            self.taxon_closure_label_searchable = [self.taxon_closure_label_searchable] if self.taxon_closure_label_searchable is not None else []
        self.taxon_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.taxon_closure_label_searchable]

        if not isinstance(self.taxon_subset_closure, list):
            self.taxon_subset_closure = [self.taxon_subset_closure] if self.taxon_subset_closure is not None else []
        self.taxon_subset_closure = [v if isinstance(v, str) else str(v) for v in self.taxon_subset_closure]

        if not isinstance(self.taxon_subset_closure_label, list):
            self.taxon_subset_closure_label = [self.taxon_subset_closure_label] if self.taxon_subset_closure_label is not None else []
        self.taxon_subset_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.taxon_subset_closure_label]

        if not isinstance(self.taxon_subset_closure_label_searchable, list):
            self.taxon_subset_closure_label_searchable = [self.taxon_subset_closure_label_searchable] if self.taxon_subset_closure_label_searchable is not None else []
        self.taxon_subset_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.taxon_subset_closure_label_searchable]

        if self.secondary_taxon is not None and not isinstance(self.secondary_taxon, str):
            self.secondary_taxon = str(self.secondary_taxon)

        if self.secondary_taxon_label is not None and not isinstance(self.secondary_taxon_label, SearchableString):
            self.secondary_taxon_label = SearchableString(self.secondary_taxon_label)

        if self.secondary_taxon_label_searchable is not None and not isinstance(self.secondary_taxon_label_searchable, SearchableString):
            self.secondary_taxon_label_searchable = SearchableString(self.secondary_taxon_label_searchable)

        if not isinstance(self.secondary_taxon_closure, list):
            self.secondary_taxon_closure = [self.secondary_taxon_closure] if self.secondary_taxon_closure is not None else []
        self.secondary_taxon_closure = [v if isinstance(v, str) else str(v) for v in self.secondary_taxon_closure]

        if not isinstance(self.secondary_taxon_closure_label, list):
            self.secondary_taxon_closure_label = [self.secondary_taxon_closure_label] if self.secondary_taxon_closure_label is not None else []
        self.secondary_taxon_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.secondary_taxon_closure_label]

        if not isinstance(self.secondary_taxon_closure_label_searchable, list):
            self.secondary_taxon_closure_label_searchable = [self.secondary_taxon_closure_label_searchable] if self.secondary_taxon_closure_label_searchable is not None else []
        self.secondary_taxon_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.secondary_taxon_closure_label_searchable]

        if not isinstance(self.isa_partof_closure, list):
            self.isa_partof_closure = [self.isa_partof_closure] if self.isa_partof_closure is not None else []
        self.isa_partof_closure = [v if isinstance(v, str) else str(v) for v in self.isa_partof_closure]

        if not isinstance(self.isa_partof_closure_label, list):
            self.isa_partof_closure_label = [self.isa_partof_closure_label] if self.isa_partof_closure_label is not None else []
        self.isa_partof_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.isa_partof_closure_label]

        if not isinstance(self.isa_partof_closure_label_searchable, list):
            self.isa_partof_closure_label_searchable = [self.isa_partof_closure_label_searchable] if self.isa_partof_closure_label_searchable is not None else []
        self.isa_partof_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.isa_partof_closure_label_searchable]

        if not isinstance(self.regulates_closure, list):
            self.regulates_closure = [self.regulates_closure] if self.regulates_closure is not None else []
        self.regulates_closure = [v if isinstance(v, str) else str(v) for v in self.regulates_closure]

        if not isinstance(self.regulates_closure_label, list):
            self.regulates_closure_label = [self.regulates_closure_label] if self.regulates_closure_label is not None else []
        self.regulates_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.regulates_closure_label]

        if not isinstance(self.regulates_closure_label_searchable, list):
            self.regulates_closure_label_searchable = [self.regulates_closure_label_searchable] if self.regulates_closure_label_searchable is not None else []
        self.regulates_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.regulates_closure_label_searchable]

        if not isinstance(self.has_participant_closure, list):
            self.has_participant_closure = [self.has_participant_closure] if self.has_participant_closure is not None else []
        self.has_participant_closure = [v if isinstance(v, str) else str(v) for v in self.has_participant_closure]

        if not isinstance(self.has_participant_closure_label, list):
            self.has_participant_closure_label = [self.has_participant_closure_label] if self.has_participant_closure_label is not None else []
        self.has_participant_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.has_participant_closure_label]

        if not isinstance(self.has_participant_closure_label_searchable, list):
            self.has_participant_closure_label_searchable = [self.has_participant_closure_label_searchable] if self.has_participant_closure_label_searchable is not None else []
        self.has_participant_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.has_participant_closure_label_searchable]

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.synonym]

        if not isinstance(self.synonym_searchable, list):
            self.synonym_searchable = [self.synonym_searchable] if self.synonym_searchable is not None else []
        self.synonym_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.synonym_searchable]

        if self.bioentity is not None and not isinstance(self.bioentity, str):
            self.bioentity = str(self.bioentity)

        if self.bioentity_label is not None and not isinstance(self.bioentity_label, SearchableString):
            self.bioentity_label = SearchableString(self.bioentity_label)

        if self.bioentity_label_searchable is not None and not isinstance(self.bioentity_label_searchable, SearchableString):
            self.bioentity_label_searchable = SearchableString(self.bioentity_label_searchable)

        if self.bioentity_name is not None and not isinstance(self.bioentity_name, SearchableString):
            self.bioentity_name = SearchableString(self.bioentity_name)

        if self.bioentity_name_searchable is not None and not isinstance(self.bioentity_name_searchable, SearchableString):
            self.bioentity_name_searchable = SearchableString(self.bioentity_name_searchable)

        if self.bioentity_internal_id is not None and not isinstance(self.bioentity_internal_id, str):
            self.bioentity_internal_id = str(self.bioentity_internal_id)

        if not isinstance(self.qualifier, list):
            self.qualifier = [self.qualifier] if self.qualifier is not None else []
        self.qualifier = [v if isinstance(v, str) else str(v) for v in self.qualifier]

        if self.annotation_class is not None and not isinstance(self.annotation_class, str):
            self.annotation_class = str(self.annotation_class)

        if self.annotation_class_label is not None and not isinstance(self.annotation_class_label, SearchableString):
            self.annotation_class_label = SearchableString(self.annotation_class_label)

        if self.annotation_class_label_searchable is not None and not isinstance(self.annotation_class_label_searchable, SearchableString):
            self.annotation_class_label_searchable = SearchableString(self.annotation_class_label_searchable)

        if self.aspect is not None and not isinstance(self.aspect, str):
            self.aspect = str(self.aspect)

        if self.bioentity_isoform is not None and not isinstance(self.bioentity_isoform, str):
            self.bioentity_isoform = str(self.bioentity_isoform)

        if self.evidence_type is not None and not isinstance(self.evidence_type, str):
            self.evidence_type = str(self.evidence_type)

        if not isinstance(self.evidence_type_closure, list):
            self.evidence_type_closure = [self.evidence_type_closure] if self.evidence_type_closure is not None else []
        self.evidence_type_closure = [v if isinstance(v, str) else str(v) for v in self.evidence_type_closure]

        if not isinstance(self.evidence_with, list):
            self.evidence_with = [self.evidence_with] if self.evidence_with is not None else []
        self.evidence_with = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.evidence_with]

        if not isinstance(self.evidence_with_searchable, list):
            self.evidence_with_searchable = [self.evidence_with_searchable] if self.evidence_with_searchable is not None else []
        self.evidence_with_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.evidence_with_searchable]

        if self.evidence is not None and not isinstance(self.evidence, str):
            self.evidence = str(self.evidence)

        if self.evidence_label is not None and not isinstance(self.evidence_label, SearchableString):
            self.evidence_label = SearchableString(self.evidence_label)

        if self.evidence_label_searchable is not None and not isinstance(self.evidence_label_searchable, SearchableString):
            self.evidence_label_searchable = SearchableString(self.evidence_label_searchable)

        if not isinstance(self.evidence_closure, list):
            self.evidence_closure = [self.evidence_closure] if self.evidence_closure is not None else []
        self.evidence_closure = [v if isinstance(v, str) else str(v) for v in self.evidence_closure]

        if not isinstance(self.evidence_closure_label, list):
            self.evidence_closure_label = [self.evidence_closure_label] if self.evidence_closure_label is not None else []
        self.evidence_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.evidence_closure_label]

        if not isinstance(self.evidence_closure_label_searchable, list):
            self.evidence_closure_label_searchable = [self.evidence_closure_label_searchable] if self.evidence_closure_label_searchable is not None else []
        self.evidence_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.evidence_closure_label_searchable]

        if not isinstance(self.evidence_subset_closure, list):
            self.evidence_subset_closure = [self.evidence_subset_closure] if self.evidence_subset_closure is not None else []
        self.evidence_subset_closure = [v if isinstance(v, str) else str(v) for v in self.evidence_subset_closure]

        if not isinstance(self.evidence_subset_closure_label, list):
            self.evidence_subset_closure_label = [self.evidence_subset_closure_label] if self.evidence_subset_closure_label is not None else []
        self.evidence_subset_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.evidence_subset_closure_label]

        if not isinstance(self.evidence_subset_closure_label_searchable, list):
            self.evidence_subset_closure_label_searchable = [self.evidence_subset_closure_label_searchable] if self.evidence_subset_closure_label_searchable is not None else []
        self.evidence_subset_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.evidence_subset_closure_label_searchable]

        if not isinstance(self.reference, list):
            self.reference = [self.reference] if self.reference is not None else []
        self.reference = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.reference]

        if not isinstance(self.reference_searchable, list):
            self.reference_searchable = [self.reference_searchable] if self.reference_searchable is not None else []
        self.reference_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.reference_searchable]

        if not isinstance(self.annotation_extension_class, list):
            self.annotation_extension_class = [self.annotation_extension_class] if self.annotation_extension_class is not None else []
        self.annotation_extension_class = [v if isinstance(v, str) else str(v) for v in self.annotation_extension_class]

        if not isinstance(self.annotation_extension_class_label, list):
            self.annotation_extension_class_label = [self.annotation_extension_class_label] if self.annotation_extension_class_label is not None else []
        self.annotation_extension_class_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.annotation_extension_class_label]

        if not isinstance(self.annotation_extension_class_label_searchable, list):
            self.annotation_extension_class_label_searchable = [self.annotation_extension_class_label_searchable] if self.annotation_extension_class_label_searchable is not None else []
        self.annotation_extension_class_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.annotation_extension_class_label_searchable]

        if not isinstance(self.annotation_extension_class_closure, list):
            self.annotation_extension_class_closure = [self.annotation_extension_class_closure] if self.annotation_extension_class_closure is not None else []
        self.annotation_extension_class_closure = [v if isinstance(v, str) else str(v) for v in self.annotation_extension_class_closure]

        if not isinstance(self.annotation_extension_class_closure_label, list):
            self.annotation_extension_class_closure_label = [self.annotation_extension_class_closure_label] if self.annotation_extension_class_closure_label is not None else []
        self.annotation_extension_class_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.annotation_extension_class_closure_label]

        if not isinstance(self.annotation_extension_class_closure_label_searchable, list):
            self.annotation_extension_class_closure_label_searchable = [self.annotation_extension_class_closure_label_searchable] if self.annotation_extension_class_closure_label_searchable is not None else []
        self.annotation_extension_class_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.annotation_extension_class_closure_label_searchable]

        if not isinstance(self.annotation_extension_json, list):
            self.annotation_extension_json = [self.annotation_extension_json] if self.annotation_extension_json is not None else []
        self.annotation_extension_json = [v if isinstance(v, str) else str(v) for v in self.annotation_extension_json]

        if self.panther_family is not None and not isinstance(self.panther_family, SearchableString):
            self.panther_family = SearchableString(self.panther_family)

        if self.panther_family_searchable is not None and not isinstance(self.panther_family_searchable, SearchableString):
            self.panther_family_searchable = SearchableString(self.panther_family_searchable)

        if self.panther_family_label is not None and not isinstance(self.panther_family_label, SearchableString):
            self.panther_family_label = SearchableString(self.panther_family_label)

        if self.panther_family_label_searchable is not None and not isinstance(self.panther_family_label_searchable, SearchableString):
            self.panther_family_label_searchable = SearchableString(self.panther_family_label_searchable)

        if not isinstance(self.geospatial_x, list):
            self.geospatial_x = [self.geospatial_x] if self.geospatial_x is not None else []
        self.geospatial_x = [v if isinstance(v, int) else int(v) for v in self.geospatial_x]

        if not isinstance(self.geospatial_y, list):
            self.geospatial_y = [self.geospatial_y] if self.geospatial_y is not None else []
        self.geospatial_y = [v if isinstance(v, int) else int(v) for v in self.geospatial_y]

        if not isinstance(self.geospatial_z, list):
            self.geospatial_z = [self.geospatial_z] if self.geospatial_z is not None else []
        self.geospatial_z = [v if isinstance(v, int) else int(v) for v in self.geospatial_z]

        super().__post_init__(**kwargs)


@dataclass
class AnnotationEvidenceAggregate(YAMLRoot):
    """
    A description of annotation evidence aggregate for GOlr and AmiGO.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/AnnotationEvidenceAggregate")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "annotation_evidence_aggregate"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/AnnotationEvidenceAggregate")

    document_category: Optional[str] = None
    id: Optional[str] = None
    bioentity: Optional[str] = None
    bioentity_label: Optional[Union[str, SearchableString]] = None
    bioentity_label_searchable: Optional[Union[str, SearchableString]] = None
    annotation_class: Optional[str] = None
    annotation_class_label: Optional[Union[str, SearchableString]] = None
    annotation_class_label_searchable: Optional[Union[str, SearchableString]] = None
    evidence_type_closure: Optional[Union[str, List[str]]] = empty_list()
    evidence_with: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    taxon: Optional[str] = None
    taxon_label: Optional[Union[str, SearchableString]] = None
    taxon_label_searchable: Optional[Union[str, SearchableString]] = None
    taxon_closure: Optional[Union[str, List[str]]] = empty_list()
    taxon_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    taxon_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    panther_family: Optional[Union[str, SearchableString]] = None
    panther_family_searchable: Optional[Union[str, SearchableString]] = None
    panther_family_label: Optional[Union[str, SearchableString]] = None
    panther_family_label_searchable: Optional[Union[str, SearchableString]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.document_category is not None and not isinstance(self.document_category, str):
            self.document_category = str(self.document_category)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.bioentity is not None and not isinstance(self.bioentity, str):
            self.bioentity = str(self.bioentity)

        if self.bioentity_label is not None and not isinstance(self.bioentity_label, SearchableString):
            self.bioentity_label = SearchableString(self.bioentity_label)

        if self.bioentity_label_searchable is not None and not isinstance(self.bioentity_label_searchable, SearchableString):
            self.bioentity_label_searchable = SearchableString(self.bioentity_label_searchable)

        if self.annotation_class is not None and not isinstance(self.annotation_class, str):
            self.annotation_class = str(self.annotation_class)

        if self.annotation_class_label is not None and not isinstance(self.annotation_class_label, SearchableString):
            self.annotation_class_label = SearchableString(self.annotation_class_label)

        if self.annotation_class_label_searchable is not None and not isinstance(self.annotation_class_label_searchable, SearchableString):
            self.annotation_class_label_searchable = SearchableString(self.annotation_class_label_searchable)

        if not isinstance(self.evidence_type_closure, list):
            self.evidence_type_closure = [self.evidence_type_closure] if self.evidence_type_closure is not None else []
        self.evidence_type_closure = [v if isinstance(v, str) else str(v) for v in self.evidence_type_closure]

        if not isinstance(self.evidence_with, list):
            self.evidence_with = [self.evidence_with] if self.evidence_with is not None else []
        self.evidence_with = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.evidence_with]

        if self.taxon is not None and not isinstance(self.taxon, str):
            self.taxon = str(self.taxon)

        if self.taxon_label is not None and not isinstance(self.taxon_label, SearchableString):
            self.taxon_label = SearchableString(self.taxon_label)

        if self.taxon_label_searchable is not None and not isinstance(self.taxon_label_searchable, SearchableString):
            self.taxon_label_searchable = SearchableString(self.taxon_label_searchable)

        if not isinstance(self.taxon_closure, list):
            self.taxon_closure = [self.taxon_closure] if self.taxon_closure is not None else []
        self.taxon_closure = [v if isinstance(v, str) else str(v) for v in self.taxon_closure]

        if not isinstance(self.taxon_closure_label, list):
            self.taxon_closure_label = [self.taxon_closure_label] if self.taxon_closure_label is not None else []
        self.taxon_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.taxon_closure_label]

        if not isinstance(self.taxon_closure_label_searchable, list):
            self.taxon_closure_label_searchable = [self.taxon_closure_label_searchable] if self.taxon_closure_label_searchable is not None else []
        self.taxon_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.taxon_closure_label_searchable]

        if self.panther_family is not None and not isinstance(self.panther_family, SearchableString):
            self.panther_family = SearchableString(self.panther_family)

        if self.panther_family_searchable is not None and not isinstance(self.panther_family_searchable, SearchableString):
            self.panther_family_searchable = SearchableString(self.panther_family_searchable)

        if self.panther_family_label is not None and not isinstance(self.panther_family_label, SearchableString):
            self.panther_family_label = SearchableString(self.panther_family_label)

        if self.panther_family_label_searchable is not None and not isinstance(self.panther_family_label_searchable, SearchableString):
            self.panther_family_label_searchable = SearchableString(self.panther_family_label_searchable)

        super().__post_init__(**kwargs)


@dataclass
class Bioentity(YAMLRoot):
    """
    Genes and gene products associated with GO terms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/Bioentity")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "bioentity"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/Bioentity")

    document_category: Optional[str] = None
    id: Optional[str] = None
    bioentity: Optional[str] = None
    bioentity_label: Optional[Union[str, SearchableString]] = None
    bioentity_label_searchable: Optional[Union[str, SearchableString]] = None
    bioentity_name: Optional[Union[str, SearchableString]] = None
    bioentity_name_searchable: Optional[Union[str, SearchableString]] = None
    bioentity_internal_id: Optional[str] = None
    type: Optional[str] = None
    taxon: Optional[str] = None
    taxon_label: Optional[Union[str, SearchableString]] = None
    taxon_label_searchable: Optional[Union[str, SearchableString]] = None
    taxon_closure: Optional[Union[str, List[str]]] = empty_list()
    taxon_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    taxon_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    taxon_subset_closure: Optional[Union[str, List[str]]] = empty_list()
    taxon_subset_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    taxon_subset_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    isa_partof_closure: Optional[Union[str, List[str]]] = empty_list()
    isa_partof_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    isa_partof_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    regulates_closure: Optional[Union[str, List[str]]] = empty_list()
    regulates_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    regulates_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    source: Optional[str] = None
    annotation_class_list: Optional[Union[str, List[str]]] = empty_list()
    annotation_class_list_label: Optional[Union[str, List[str]]] = empty_list()
    synonym: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    synonym_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    panther_family: Optional[Union[str, SearchableString]] = None
    panther_family_searchable: Optional[Union[str, SearchableString]] = None
    panther_family_label: Optional[Union[str, SearchableString]] = None
    panther_family_label_searchable: Optional[Union[str, SearchableString]] = None
    phylo_graph_json: Optional[str] = None
    database_xref: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.document_category is not None and not isinstance(self.document_category, str):
            self.document_category = str(self.document_category)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.bioentity is not None and not isinstance(self.bioentity, str):
            self.bioentity = str(self.bioentity)

        if self.bioentity_label is not None and not isinstance(self.bioentity_label, SearchableString):
            self.bioentity_label = SearchableString(self.bioentity_label)

        if self.bioentity_label_searchable is not None and not isinstance(self.bioentity_label_searchable, SearchableString):
            self.bioentity_label_searchable = SearchableString(self.bioentity_label_searchable)

        if self.bioentity_name is not None and not isinstance(self.bioentity_name, SearchableString):
            self.bioentity_name = SearchableString(self.bioentity_name)

        if self.bioentity_name_searchable is not None and not isinstance(self.bioentity_name_searchable, SearchableString):
            self.bioentity_name_searchable = SearchableString(self.bioentity_name_searchable)

        if self.bioentity_internal_id is not None and not isinstance(self.bioentity_internal_id, str):
            self.bioentity_internal_id = str(self.bioentity_internal_id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.taxon is not None and not isinstance(self.taxon, str):
            self.taxon = str(self.taxon)

        if self.taxon_label is not None and not isinstance(self.taxon_label, SearchableString):
            self.taxon_label = SearchableString(self.taxon_label)

        if self.taxon_label_searchable is not None and not isinstance(self.taxon_label_searchable, SearchableString):
            self.taxon_label_searchable = SearchableString(self.taxon_label_searchable)

        if not isinstance(self.taxon_closure, list):
            self.taxon_closure = [self.taxon_closure] if self.taxon_closure is not None else []
        self.taxon_closure = [v if isinstance(v, str) else str(v) for v in self.taxon_closure]

        if not isinstance(self.taxon_closure_label, list):
            self.taxon_closure_label = [self.taxon_closure_label] if self.taxon_closure_label is not None else []
        self.taxon_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.taxon_closure_label]

        if not isinstance(self.taxon_closure_label_searchable, list):
            self.taxon_closure_label_searchable = [self.taxon_closure_label_searchable] if self.taxon_closure_label_searchable is not None else []
        self.taxon_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.taxon_closure_label_searchable]

        if not isinstance(self.taxon_subset_closure, list):
            self.taxon_subset_closure = [self.taxon_subset_closure] if self.taxon_subset_closure is not None else []
        self.taxon_subset_closure = [v if isinstance(v, str) else str(v) for v in self.taxon_subset_closure]

        if not isinstance(self.taxon_subset_closure_label, list):
            self.taxon_subset_closure_label = [self.taxon_subset_closure_label] if self.taxon_subset_closure_label is not None else []
        self.taxon_subset_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.taxon_subset_closure_label]

        if not isinstance(self.taxon_subset_closure_label_searchable, list):
            self.taxon_subset_closure_label_searchable = [self.taxon_subset_closure_label_searchable] if self.taxon_subset_closure_label_searchable is not None else []
        self.taxon_subset_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.taxon_subset_closure_label_searchable]

        if not isinstance(self.isa_partof_closure, list):
            self.isa_partof_closure = [self.isa_partof_closure] if self.isa_partof_closure is not None else []
        self.isa_partof_closure = [v if isinstance(v, str) else str(v) for v in self.isa_partof_closure]

        if not isinstance(self.isa_partof_closure_label, list):
            self.isa_partof_closure_label = [self.isa_partof_closure_label] if self.isa_partof_closure_label is not None else []
        self.isa_partof_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.isa_partof_closure_label]

        if not isinstance(self.isa_partof_closure_label_searchable, list):
            self.isa_partof_closure_label_searchable = [self.isa_partof_closure_label_searchable] if self.isa_partof_closure_label_searchable is not None else []
        self.isa_partof_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.isa_partof_closure_label_searchable]

        if not isinstance(self.regulates_closure, list):
            self.regulates_closure = [self.regulates_closure] if self.regulates_closure is not None else []
        self.regulates_closure = [v if isinstance(v, str) else str(v) for v in self.regulates_closure]

        if not isinstance(self.regulates_closure_label, list):
            self.regulates_closure_label = [self.regulates_closure_label] if self.regulates_closure_label is not None else []
        self.regulates_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.regulates_closure_label]

        if not isinstance(self.regulates_closure_label_searchable, list):
            self.regulates_closure_label_searchable = [self.regulates_closure_label_searchable] if self.regulates_closure_label_searchable is not None else []
        self.regulates_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.regulates_closure_label_searchable]

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if not isinstance(self.annotation_class_list, list):
            self.annotation_class_list = [self.annotation_class_list] if self.annotation_class_list is not None else []
        self.annotation_class_list = [v if isinstance(v, str) else str(v) for v in self.annotation_class_list]

        if not isinstance(self.annotation_class_list_label, list):
            self.annotation_class_list_label = [self.annotation_class_list_label] if self.annotation_class_list_label is not None else []
        self.annotation_class_list_label = [v if isinstance(v, str) else str(v) for v in self.annotation_class_list_label]

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.synonym]

        if not isinstance(self.synonym_searchable, list):
            self.synonym_searchable = [self.synonym_searchable] if self.synonym_searchable is not None else []
        self.synonym_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.synonym_searchable]

        if self.panther_family is not None and not isinstance(self.panther_family, SearchableString):
            self.panther_family = SearchableString(self.panther_family)

        if self.panther_family_searchable is not None and not isinstance(self.panther_family_searchable, SearchableString):
            self.panther_family_searchable = SearchableString(self.panther_family_searchable)

        if self.panther_family_label is not None and not isinstance(self.panther_family_label, SearchableString):
            self.panther_family_label = SearchableString(self.panther_family_label)

        if self.panther_family_label_searchable is not None and not isinstance(self.panther_family_label_searchable, SearchableString):
            self.panther_family_label_searchable = SearchableString(self.panther_family_label_searchable)

        if self.phylo_graph_json is not None and not isinstance(self.phylo_graph_json, str):
            self.phylo_graph_json = str(self.phylo_graph_json)

        if not isinstance(self.database_xref, list):
            self.database_xref = [self.database_xref] if self.database_xref is not None else []
        self.database_xref = [v if isinstance(v, str) else str(v) for v in self.database_xref]

        super().__post_init__(**kwargs)


@dataclass
class ComplexAnnotation(YAMLRoot):
    """
    An individual unit within LEGO. This is <strong>ALPHA</strong> software.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/ComplexAnnotation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "complex_annotation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/ComplexAnnotation")

    document_category: Optional[str] = None
    id: Optional[str] = None
    annotation_unit: Optional[str] = None
    annotation_unit_label: Optional[Union[str, SearchableString]] = None
    annotation_unit_label_searchable: Optional[Union[str, SearchableString]] = None
    annotation_group: Optional[str] = None
    annotation_group_label: Optional[Union[str, SearchableString]] = None
    annotation_group_label_searchable: Optional[Union[str, SearchableString]] = None
    annotation_group_url: Optional[str] = None
    enabled_by: Optional[Union[str, SearchableString]] = None
    enabled_by_searchable: Optional[Union[str, SearchableString]] = None
    enabled_by_label: Optional[Union[str, SearchableString]] = None
    enabled_by_label_searchable: Optional[Union[str, SearchableString]] = None
    panther_family: Optional[Union[str, SearchableString]] = None
    panther_family_searchable: Optional[Union[str, SearchableString]] = None
    panther_family_label: Optional[Union[str, SearchableString]] = None
    panther_family_label_searchable: Optional[Union[str, SearchableString]] = None
    taxon: Optional[str] = None
    taxon_label: Optional[Union[str, SearchableString]] = None
    taxon_label_searchable: Optional[Union[str, SearchableString]] = None
    taxon_closure: Optional[Union[str, List[str]]] = empty_list()
    taxon_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    taxon_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    function_class: Optional[str] = None
    function_class_label: Optional[Union[str, SearchableString]] = None
    function_class_label_searchable: Optional[Union[str, SearchableString]] = None
    function_class_closure: Optional[Union[str, List[str]]] = empty_list()
    function_class_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    function_class_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    process_class: Optional[str] = None
    process_class_label: Optional[Union[str, SearchableString]] = None
    process_class_label_searchable: Optional[Union[str, SearchableString]] = None
    process_class_closure: Optional[Union[str, List[str]]] = empty_list()
    process_class_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    process_class_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    location_list: Optional[Union[str, List[str]]] = empty_list()
    location_list_label: Optional[Union[str, List[str]]] = empty_list()
    location_list_closure: Optional[Union[str, List[str]]] = empty_list()
    location_list_closure_label: Optional[Union[str, List[str]]] = empty_list()
    owl_blob_json: Optional[str] = None
    topology_graph_json: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.document_category is not None and not isinstance(self.document_category, str):
            self.document_category = str(self.document_category)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.annotation_unit is not None and not isinstance(self.annotation_unit, str):
            self.annotation_unit = str(self.annotation_unit)

        if self.annotation_unit_label is not None and not isinstance(self.annotation_unit_label, SearchableString):
            self.annotation_unit_label = SearchableString(self.annotation_unit_label)

        if self.annotation_unit_label_searchable is not None and not isinstance(self.annotation_unit_label_searchable, SearchableString):
            self.annotation_unit_label_searchable = SearchableString(self.annotation_unit_label_searchable)

        if self.annotation_group is not None and not isinstance(self.annotation_group, str):
            self.annotation_group = str(self.annotation_group)

        if self.annotation_group_label is not None and not isinstance(self.annotation_group_label, SearchableString):
            self.annotation_group_label = SearchableString(self.annotation_group_label)

        if self.annotation_group_label_searchable is not None and not isinstance(self.annotation_group_label_searchable, SearchableString):
            self.annotation_group_label_searchable = SearchableString(self.annotation_group_label_searchable)

        if self.annotation_group_url is not None and not isinstance(self.annotation_group_url, str):
            self.annotation_group_url = str(self.annotation_group_url)

        if self.enabled_by is not None and not isinstance(self.enabled_by, SearchableString):
            self.enabled_by = SearchableString(self.enabled_by)

        if self.enabled_by_searchable is not None and not isinstance(self.enabled_by_searchable, SearchableString):
            self.enabled_by_searchable = SearchableString(self.enabled_by_searchable)

        if self.enabled_by_label is not None and not isinstance(self.enabled_by_label, SearchableString):
            self.enabled_by_label = SearchableString(self.enabled_by_label)

        if self.enabled_by_label_searchable is not None and not isinstance(self.enabled_by_label_searchable, SearchableString):
            self.enabled_by_label_searchable = SearchableString(self.enabled_by_label_searchable)

        if self.panther_family is not None and not isinstance(self.panther_family, SearchableString):
            self.panther_family = SearchableString(self.panther_family)

        if self.panther_family_searchable is not None and not isinstance(self.panther_family_searchable, SearchableString):
            self.panther_family_searchable = SearchableString(self.panther_family_searchable)

        if self.panther_family_label is not None and not isinstance(self.panther_family_label, SearchableString):
            self.panther_family_label = SearchableString(self.panther_family_label)

        if self.panther_family_label_searchable is not None and not isinstance(self.panther_family_label_searchable, SearchableString):
            self.panther_family_label_searchable = SearchableString(self.panther_family_label_searchable)

        if self.taxon is not None and not isinstance(self.taxon, str):
            self.taxon = str(self.taxon)

        if self.taxon_label is not None and not isinstance(self.taxon_label, SearchableString):
            self.taxon_label = SearchableString(self.taxon_label)

        if self.taxon_label_searchable is not None and not isinstance(self.taxon_label_searchable, SearchableString):
            self.taxon_label_searchable = SearchableString(self.taxon_label_searchable)

        if not isinstance(self.taxon_closure, list):
            self.taxon_closure = [self.taxon_closure] if self.taxon_closure is not None else []
        self.taxon_closure = [v if isinstance(v, str) else str(v) for v in self.taxon_closure]

        if not isinstance(self.taxon_closure_label, list):
            self.taxon_closure_label = [self.taxon_closure_label] if self.taxon_closure_label is not None else []
        self.taxon_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.taxon_closure_label]

        if not isinstance(self.taxon_closure_label_searchable, list):
            self.taxon_closure_label_searchable = [self.taxon_closure_label_searchable] if self.taxon_closure_label_searchable is not None else []
        self.taxon_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.taxon_closure_label_searchable]

        if self.function_class is not None and not isinstance(self.function_class, str):
            self.function_class = str(self.function_class)

        if self.function_class_label is not None and not isinstance(self.function_class_label, SearchableString):
            self.function_class_label = SearchableString(self.function_class_label)

        if self.function_class_label_searchable is not None and not isinstance(self.function_class_label_searchable, SearchableString):
            self.function_class_label_searchable = SearchableString(self.function_class_label_searchable)

        if not isinstance(self.function_class_closure, list):
            self.function_class_closure = [self.function_class_closure] if self.function_class_closure is not None else []
        self.function_class_closure = [v if isinstance(v, str) else str(v) for v in self.function_class_closure]

        if not isinstance(self.function_class_closure_label, list):
            self.function_class_closure_label = [self.function_class_closure_label] if self.function_class_closure_label is not None else []
        self.function_class_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.function_class_closure_label]

        if not isinstance(self.function_class_closure_label_searchable, list):
            self.function_class_closure_label_searchable = [self.function_class_closure_label_searchable] if self.function_class_closure_label_searchable is not None else []
        self.function_class_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.function_class_closure_label_searchable]

        if self.process_class is not None and not isinstance(self.process_class, str):
            self.process_class = str(self.process_class)

        if self.process_class_label is not None and not isinstance(self.process_class_label, SearchableString):
            self.process_class_label = SearchableString(self.process_class_label)

        if self.process_class_label_searchable is not None and not isinstance(self.process_class_label_searchable, SearchableString):
            self.process_class_label_searchable = SearchableString(self.process_class_label_searchable)

        if not isinstance(self.process_class_closure, list):
            self.process_class_closure = [self.process_class_closure] if self.process_class_closure is not None else []
        self.process_class_closure = [v if isinstance(v, str) else str(v) for v in self.process_class_closure]

        if not isinstance(self.process_class_closure_label, list):
            self.process_class_closure_label = [self.process_class_closure_label] if self.process_class_closure_label is not None else []
        self.process_class_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.process_class_closure_label]

        if not isinstance(self.process_class_closure_label_searchable, list):
            self.process_class_closure_label_searchable = [self.process_class_closure_label_searchable] if self.process_class_closure_label_searchable is not None else []
        self.process_class_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.process_class_closure_label_searchable]

        if not isinstance(self.location_list, list):
            self.location_list = [self.location_list] if self.location_list is not None else []
        self.location_list = [v if isinstance(v, str) else str(v) for v in self.location_list]

        if not isinstance(self.location_list_label, list):
            self.location_list_label = [self.location_list_label] if self.location_list_label is not None else []
        self.location_list_label = [v if isinstance(v, str) else str(v) for v in self.location_list_label]

        if not isinstance(self.location_list_closure, list):
            self.location_list_closure = [self.location_list_closure] if self.location_list_closure is not None else []
        self.location_list_closure = [v if isinstance(v, str) else str(v) for v in self.location_list_closure]

        if not isinstance(self.location_list_closure_label, list):
            self.location_list_closure_label = [self.location_list_closure_label] if self.location_list_closure_label is not None else []
        self.location_list_closure_label = [v if isinstance(v, str) else str(v) for v in self.location_list_closure_label]

        if self.owl_blob_json is not None and not isinstance(self.owl_blob_json, str):
            self.owl_blob_json = str(self.owl_blob_json)

        if self.topology_graph_json is not None and not isinstance(self.topology_graph_json, str):
            self.topology_graph_json = str(self.topology_graph_json)

        super().__post_init__(**kwargs)


@dataclass
class General(YAMLRoot):
    """
    A generic search document to get a general overview of everything.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/General")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "general"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/General")

    document_category: Optional[str] = None
    id: Optional[str] = None
    entity: Optional[str] = None
    entity_label: Optional[Union[str, SearchableString]] = None
    entity_label_searchable: Optional[Union[str, SearchableString]] = None
    category: Optional[str] = None
    general_blob: Optional[Union[str, SearchableString]] = None
    general_blob_searchable: Optional[Union[str, SearchableString]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.document_category is not None and not isinstance(self.document_category, str):
            self.document_category = str(self.document_category)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.entity is not None and not isinstance(self.entity, str):
            self.entity = str(self.entity)

        if self.entity_label is not None and not isinstance(self.entity_label, SearchableString):
            self.entity_label = SearchableString(self.entity_label)

        if self.entity_label_searchable is not None and not isinstance(self.entity_label_searchable, SearchableString):
            self.entity_label_searchable = SearchableString(self.entity_label_searchable)

        if self.category is not None and not isinstance(self.category, str):
            self.category = str(self.category)

        if self.general_blob is not None and not isinstance(self.general_blob, SearchableString):
            self.general_blob = SearchableString(self.general_blob)

        if self.general_blob_searchable is not None and not isinstance(self.general_blob_searchable, SearchableString):
            self.general_blob_searchable = SearchableString(self.general_blob_searchable)

        super().__post_init__(**kwargs)


@dataclass
class ModelAnnotation(YAMLRoot):
    """
    An individual unit within a GO-CAM. This is <strong>ALPHA</strong> software.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/ModelAnnotation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "model_annotation"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/ModelAnnotation")

    document_category: Optional[str] = None
    id: Optional[str] = None
    annotation_unit: Optional[str] = None
    annotation_unit_label: Optional[Union[str, SearchableString]] = None
    annotation_unit_label_searchable: Optional[Union[str, SearchableString]] = None
    model: Optional[str] = None
    model_label: Optional[Union[str, SearchableString]] = None
    model_label_searchable: Optional[Union[str, SearchableString]] = None
    model_url: Optional[str] = None
    model_state: Optional[str] = None
    annotation_value: Optional[Union[str, List[str]]] = empty_list()
    contributor: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    contributor_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    model_date: Optional[Union[str, SearchableString]] = None
    model_date_searchable: Optional[Union[str, SearchableString]] = None
    comment: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    comment_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    enabled_by: Optional[Union[str, SearchableString]] = None
    enabled_by_searchable: Optional[Union[str, SearchableString]] = None
    enabled_by_label: Optional[Union[str, SearchableString]] = None
    enabled_by_label_searchable: Optional[Union[str, SearchableString]] = None
    enabled_by_complex: Optional[Union[str, SearchableString]] = None
    enabled_by_complex_searchable: Optional[Union[str, SearchableString]] = None
    enabled_by_complex_label: Optional[Union[str, SearchableString]] = None
    enabled_by_complex_label_searchable: Optional[Union[str, SearchableString]] = None
    has_participant: Optional[Union[str, SearchableString]] = None
    has_participant_searchable: Optional[Union[str, SearchableString]] = None
    has_participant_label: Optional[Union[str, SearchableString]] = None
    has_participant_label_searchable: Optional[Union[str, SearchableString]] = None
    has_complex_participant: Optional[Union[str, SearchableString]] = None
    has_complex_participant_searchable: Optional[Union[str, SearchableString]] = None
    has_complex_participant_label: Optional[Union[str, SearchableString]] = None
    has_complex_participant_label_searchable: Optional[Union[str, SearchableString]] = None
    has_output: Optional[Union[str, SearchableString]] = None
    has_output_searchable: Optional[Union[str, SearchableString]] = None
    has_output_label: Optional[Union[str, SearchableString]] = None
    has_output_label_searchable: Optional[Union[str, SearchableString]] = None
    has_complex_output: Optional[Union[str, SearchableString]] = None
    has_complex_output_searchable: Optional[Union[str, SearchableString]] = None
    has_complex_output_label: Optional[Union[str, SearchableString]] = None
    has_complex_output_label_searchable: Optional[Union[str, SearchableString]] = None
    panther_family: Optional[Union[str, SearchableString]] = None
    panther_family_searchable: Optional[Union[str, SearchableString]] = None
    panther_family_label: Optional[Union[str, SearchableString]] = None
    panther_family_label_searchable: Optional[Union[str, SearchableString]] = None
    taxon: Optional[str] = None
    taxon_label: Optional[Union[str, SearchableString]] = None
    taxon_label_searchable: Optional[Union[str, SearchableString]] = None
    taxon_closure: Optional[Union[str, List[str]]] = empty_list()
    taxon_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    taxon_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    function_class: Optional[str] = None
    function_class_label: Optional[Union[str, SearchableString]] = None
    function_class_label_searchable: Optional[Union[str, SearchableString]] = None
    function_class_closure: Optional[Union[str, List[str]]] = empty_list()
    function_class_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    function_class_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    process_class: Optional[str] = None
    process_class_label: Optional[Union[str, SearchableString]] = None
    process_class_label_searchable: Optional[Union[str, SearchableString]] = None
    process_class_closure: Optional[Union[str, List[str]]] = empty_list()
    process_class_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    process_class_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    location_list: Optional[Union[str, List[str]]] = empty_list()
    location_list_label: Optional[Union[str, List[str]]] = empty_list()
    location_list_closure: Optional[Union[str, List[str]]] = empty_list()
    location_list_closure_label: Optional[Union[str, List[str]]] = empty_list()
    owl_blob_json: Optional[str] = None
    topology_graph_json: Optional[str] = None
    evidence_type: Optional[str] = None
    evidence_type_closure: Optional[Union[str, List[str]]] = empty_list()
    evidence_type_label: Optional[Union[str, SearchableString]] = None
    evidence_type_label_searchable: Optional[Union[str, SearchableString]] = None
    evidence_type_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    evidence_type_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    evidence_with: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    evidence_with_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    reference: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    reference_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    relationship: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    relationship_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    relationship_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    relationship_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.document_category is not None and not isinstance(self.document_category, str):
            self.document_category = str(self.document_category)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.annotation_unit is not None and not isinstance(self.annotation_unit, str):
            self.annotation_unit = str(self.annotation_unit)

        if self.annotation_unit_label is not None and not isinstance(self.annotation_unit_label, SearchableString):
            self.annotation_unit_label = SearchableString(self.annotation_unit_label)

        if self.annotation_unit_label_searchable is not None and not isinstance(self.annotation_unit_label_searchable, SearchableString):
            self.annotation_unit_label_searchable = SearchableString(self.annotation_unit_label_searchable)

        if self.model is not None and not isinstance(self.model, str):
            self.model = str(self.model)

        if self.model_label is not None and not isinstance(self.model_label, SearchableString):
            self.model_label = SearchableString(self.model_label)

        if self.model_label_searchable is not None and not isinstance(self.model_label_searchable, SearchableString):
            self.model_label_searchable = SearchableString(self.model_label_searchable)

        if self.model_url is not None and not isinstance(self.model_url, str):
            self.model_url = str(self.model_url)

        if self.model_state is not None and not isinstance(self.model_state, str):
            self.model_state = str(self.model_state)

        if not isinstance(self.annotation_value, list):
            self.annotation_value = [self.annotation_value] if self.annotation_value is not None else []
        self.annotation_value = [v if isinstance(v, str) else str(v) for v in self.annotation_value]

        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.contributor]

        if not isinstance(self.contributor_searchable, list):
            self.contributor_searchable = [self.contributor_searchable] if self.contributor_searchable is not None else []
        self.contributor_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.contributor_searchable]

        if self.model_date is not None and not isinstance(self.model_date, SearchableString):
            self.model_date = SearchableString(self.model_date)

        if self.model_date_searchable is not None and not isinstance(self.model_date_searchable, SearchableString):
            self.model_date_searchable = SearchableString(self.model_date_searchable)

        if not isinstance(self.comment, list):
            self.comment = [self.comment] if self.comment is not None else []
        self.comment = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.comment]

        if not isinstance(self.comment_searchable, list):
            self.comment_searchable = [self.comment_searchable] if self.comment_searchable is not None else []
        self.comment_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.comment_searchable]

        if self.enabled_by is not None and not isinstance(self.enabled_by, SearchableString):
            self.enabled_by = SearchableString(self.enabled_by)

        if self.enabled_by_searchable is not None and not isinstance(self.enabled_by_searchable, SearchableString):
            self.enabled_by_searchable = SearchableString(self.enabled_by_searchable)

        if self.enabled_by_label is not None and not isinstance(self.enabled_by_label, SearchableString):
            self.enabled_by_label = SearchableString(self.enabled_by_label)

        if self.enabled_by_label_searchable is not None and not isinstance(self.enabled_by_label_searchable, SearchableString):
            self.enabled_by_label_searchable = SearchableString(self.enabled_by_label_searchable)

        if self.enabled_by_complex is not None and not isinstance(self.enabled_by_complex, SearchableString):
            self.enabled_by_complex = SearchableString(self.enabled_by_complex)

        if self.enabled_by_complex_searchable is not None and not isinstance(self.enabled_by_complex_searchable, SearchableString):
            self.enabled_by_complex_searchable = SearchableString(self.enabled_by_complex_searchable)

        if self.enabled_by_complex_label is not None and not isinstance(self.enabled_by_complex_label, SearchableString):
            self.enabled_by_complex_label = SearchableString(self.enabled_by_complex_label)

        if self.enabled_by_complex_label_searchable is not None and not isinstance(self.enabled_by_complex_label_searchable, SearchableString):
            self.enabled_by_complex_label_searchable = SearchableString(self.enabled_by_complex_label_searchable)

        if self.has_participant is not None and not isinstance(self.has_participant, SearchableString):
            self.has_participant = SearchableString(self.has_participant)

        if self.has_participant_searchable is not None and not isinstance(self.has_participant_searchable, SearchableString):
            self.has_participant_searchable = SearchableString(self.has_participant_searchable)

        if self.has_participant_label is not None and not isinstance(self.has_participant_label, SearchableString):
            self.has_participant_label = SearchableString(self.has_participant_label)

        if self.has_participant_label_searchable is not None and not isinstance(self.has_participant_label_searchable, SearchableString):
            self.has_participant_label_searchable = SearchableString(self.has_participant_label_searchable)

        if self.has_complex_participant is not None and not isinstance(self.has_complex_participant, SearchableString):
            self.has_complex_participant = SearchableString(self.has_complex_participant)

        if self.has_complex_participant_searchable is not None and not isinstance(self.has_complex_participant_searchable, SearchableString):
            self.has_complex_participant_searchable = SearchableString(self.has_complex_participant_searchable)

        if self.has_complex_participant_label is not None and not isinstance(self.has_complex_participant_label, SearchableString):
            self.has_complex_participant_label = SearchableString(self.has_complex_participant_label)

        if self.has_complex_participant_label_searchable is not None and not isinstance(self.has_complex_participant_label_searchable, SearchableString):
            self.has_complex_participant_label_searchable = SearchableString(self.has_complex_participant_label_searchable)

        if self.has_output is not None and not isinstance(self.has_output, SearchableString):
            self.has_output = SearchableString(self.has_output)

        if self.has_output_searchable is not None and not isinstance(self.has_output_searchable, SearchableString):
            self.has_output_searchable = SearchableString(self.has_output_searchable)

        if self.has_output_label is not None and not isinstance(self.has_output_label, SearchableString):
            self.has_output_label = SearchableString(self.has_output_label)

        if self.has_output_label_searchable is not None and not isinstance(self.has_output_label_searchable, SearchableString):
            self.has_output_label_searchable = SearchableString(self.has_output_label_searchable)

        if self.has_complex_output is not None and not isinstance(self.has_complex_output, SearchableString):
            self.has_complex_output = SearchableString(self.has_complex_output)

        if self.has_complex_output_searchable is not None and not isinstance(self.has_complex_output_searchable, SearchableString):
            self.has_complex_output_searchable = SearchableString(self.has_complex_output_searchable)

        if self.has_complex_output_label is not None and not isinstance(self.has_complex_output_label, SearchableString):
            self.has_complex_output_label = SearchableString(self.has_complex_output_label)

        if self.has_complex_output_label_searchable is not None and not isinstance(self.has_complex_output_label_searchable, SearchableString):
            self.has_complex_output_label_searchable = SearchableString(self.has_complex_output_label_searchable)

        if self.panther_family is not None and not isinstance(self.panther_family, SearchableString):
            self.panther_family = SearchableString(self.panther_family)

        if self.panther_family_searchable is not None and not isinstance(self.panther_family_searchable, SearchableString):
            self.panther_family_searchable = SearchableString(self.panther_family_searchable)

        if self.panther_family_label is not None and not isinstance(self.panther_family_label, SearchableString):
            self.panther_family_label = SearchableString(self.panther_family_label)

        if self.panther_family_label_searchable is not None and not isinstance(self.panther_family_label_searchable, SearchableString):
            self.panther_family_label_searchable = SearchableString(self.panther_family_label_searchable)

        if self.taxon is not None and not isinstance(self.taxon, str):
            self.taxon = str(self.taxon)

        if self.taxon_label is not None and not isinstance(self.taxon_label, SearchableString):
            self.taxon_label = SearchableString(self.taxon_label)

        if self.taxon_label_searchable is not None and not isinstance(self.taxon_label_searchable, SearchableString):
            self.taxon_label_searchable = SearchableString(self.taxon_label_searchable)

        if not isinstance(self.taxon_closure, list):
            self.taxon_closure = [self.taxon_closure] if self.taxon_closure is not None else []
        self.taxon_closure = [v if isinstance(v, str) else str(v) for v in self.taxon_closure]

        if not isinstance(self.taxon_closure_label, list):
            self.taxon_closure_label = [self.taxon_closure_label] if self.taxon_closure_label is not None else []
        self.taxon_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.taxon_closure_label]

        if not isinstance(self.taxon_closure_label_searchable, list):
            self.taxon_closure_label_searchable = [self.taxon_closure_label_searchable] if self.taxon_closure_label_searchable is not None else []
        self.taxon_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.taxon_closure_label_searchable]

        if self.function_class is not None and not isinstance(self.function_class, str):
            self.function_class = str(self.function_class)

        if self.function_class_label is not None and not isinstance(self.function_class_label, SearchableString):
            self.function_class_label = SearchableString(self.function_class_label)

        if self.function_class_label_searchable is not None and not isinstance(self.function_class_label_searchable, SearchableString):
            self.function_class_label_searchable = SearchableString(self.function_class_label_searchable)

        if not isinstance(self.function_class_closure, list):
            self.function_class_closure = [self.function_class_closure] if self.function_class_closure is not None else []
        self.function_class_closure = [v if isinstance(v, str) else str(v) for v in self.function_class_closure]

        if not isinstance(self.function_class_closure_label, list):
            self.function_class_closure_label = [self.function_class_closure_label] if self.function_class_closure_label is not None else []
        self.function_class_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.function_class_closure_label]

        if not isinstance(self.function_class_closure_label_searchable, list):
            self.function_class_closure_label_searchable = [self.function_class_closure_label_searchable] if self.function_class_closure_label_searchable is not None else []
        self.function_class_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.function_class_closure_label_searchable]

        if self.process_class is not None and not isinstance(self.process_class, str):
            self.process_class = str(self.process_class)

        if self.process_class_label is not None and not isinstance(self.process_class_label, SearchableString):
            self.process_class_label = SearchableString(self.process_class_label)

        if self.process_class_label_searchable is not None and not isinstance(self.process_class_label_searchable, SearchableString):
            self.process_class_label_searchable = SearchableString(self.process_class_label_searchable)

        if not isinstance(self.process_class_closure, list):
            self.process_class_closure = [self.process_class_closure] if self.process_class_closure is not None else []
        self.process_class_closure = [v if isinstance(v, str) else str(v) for v in self.process_class_closure]

        if not isinstance(self.process_class_closure_label, list):
            self.process_class_closure_label = [self.process_class_closure_label] if self.process_class_closure_label is not None else []
        self.process_class_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.process_class_closure_label]

        if not isinstance(self.process_class_closure_label_searchable, list):
            self.process_class_closure_label_searchable = [self.process_class_closure_label_searchable] if self.process_class_closure_label_searchable is not None else []
        self.process_class_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.process_class_closure_label_searchable]

        if not isinstance(self.location_list, list):
            self.location_list = [self.location_list] if self.location_list is not None else []
        self.location_list = [v if isinstance(v, str) else str(v) for v in self.location_list]

        if not isinstance(self.location_list_label, list):
            self.location_list_label = [self.location_list_label] if self.location_list_label is not None else []
        self.location_list_label = [v if isinstance(v, str) else str(v) for v in self.location_list_label]

        if not isinstance(self.location_list_closure, list):
            self.location_list_closure = [self.location_list_closure] if self.location_list_closure is not None else []
        self.location_list_closure = [v if isinstance(v, str) else str(v) for v in self.location_list_closure]

        if not isinstance(self.location_list_closure_label, list):
            self.location_list_closure_label = [self.location_list_closure_label] if self.location_list_closure_label is not None else []
        self.location_list_closure_label = [v if isinstance(v, str) else str(v) for v in self.location_list_closure_label]

        if self.owl_blob_json is not None and not isinstance(self.owl_blob_json, str):
            self.owl_blob_json = str(self.owl_blob_json)

        if self.topology_graph_json is not None and not isinstance(self.topology_graph_json, str):
            self.topology_graph_json = str(self.topology_graph_json)

        if self.evidence_type is not None and not isinstance(self.evidence_type, str):
            self.evidence_type = str(self.evidence_type)

        if not isinstance(self.evidence_type_closure, list):
            self.evidence_type_closure = [self.evidence_type_closure] if self.evidence_type_closure is not None else []
        self.evidence_type_closure = [v if isinstance(v, str) else str(v) for v in self.evidence_type_closure]

        if self.evidence_type_label is not None and not isinstance(self.evidence_type_label, SearchableString):
            self.evidence_type_label = SearchableString(self.evidence_type_label)

        if self.evidence_type_label_searchable is not None and not isinstance(self.evidence_type_label_searchable, SearchableString):
            self.evidence_type_label_searchable = SearchableString(self.evidence_type_label_searchable)

        if not isinstance(self.evidence_type_closure_label, list):
            self.evidence_type_closure_label = [self.evidence_type_closure_label] if self.evidence_type_closure_label is not None else []
        self.evidence_type_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.evidence_type_closure_label]

        if not isinstance(self.evidence_type_closure_label_searchable, list):
            self.evidence_type_closure_label_searchable = [self.evidence_type_closure_label_searchable] if self.evidence_type_closure_label_searchable is not None else []
        self.evidence_type_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.evidence_type_closure_label_searchable]

        if not isinstance(self.evidence_with, list):
            self.evidence_with = [self.evidence_with] if self.evidence_with is not None else []
        self.evidence_with = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.evidence_with]

        if not isinstance(self.evidence_with_searchable, list):
            self.evidence_with_searchable = [self.evidence_with_searchable] if self.evidence_with_searchable is not None else []
        self.evidence_with_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.evidence_with_searchable]

        if not isinstance(self.reference, list):
            self.reference = [self.reference] if self.reference is not None else []
        self.reference = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.reference]

        if not isinstance(self.reference_searchable, list):
            self.reference_searchable = [self.reference_searchable] if self.reference_searchable is not None else []
        self.reference_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.reference_searchable]

        if not isinstance(self.relationship, list):
            self.relationship = [self.relationship] if self.relationship is not None else []
        self.relationship = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.relationship]

        if not isinstance(self.relationship_searchable, list):
            self.relationship_searchable = [self.relationship_searchable] if self.relationship_searchable is not None else []
        self.relationship_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.relationship_searchable]

        if not isinstance(self.relationship_label, list):
            self.relationship_label = [self.relationship_label] if self.relationship_label is not None else []
        self.relationship_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.relationship_label]

        if not isinstance(self.relationship_label_searchable, list):
            self.relationship_label_searchable = [self.relationship_label_searchable] if self.relationship_label_searchable is not None else []
        self.relationship_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.relationship_label_searchable]

        super().__post_init__(**kwargs)


@dataclass
class NoctuaModelMeta(YAMLRoot):
    """
    A generic capture of light Noctua metadata in realtime.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/NoctuaModelMeta")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "noctua_model_meta"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/NoctuaModelMeta")

    document_category: Optional[str] = None
    id: Optional[str] = None
    annotation_unit: Optional[str] = None
    annotation_unit_label: Optional[Union[str, SearchableString]] = None
    annotation_unit_label_searchable: Optional[Union[str, SearchableString]] = None
    contributor: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    contributor_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    model_date: Optional[Union[str, SearchableString]] = None
    model_date_searchable: Optional[Union[str, SearchableString]] = None
    model_state: Optional[str] = None
    comment: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    comment_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    owl_blob_json: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.document_category is not None and not isinstance(self.document_category, str):
            self.document_category = str(self.document_category)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.annotation_unit is not None and not isinstance(self.annotation_unit, str):
            self.annotation_unit = str(self.annotation_unit)

        if self.annotation_unit_label is not None and not isinstance(self.annotation_unit_label, SearchableString):
            self.annotation_unit_label = SearchableString(self.annotation_unit_label)

        if self.annotation_unit_label_searchable is not None and not isinstance(self.annotation_unit_label_searchable, SearchableString):
            self.annotation_unit_label_searchable = SearchableString(self.annotation_unit_label_searchable)

        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.contributor]

        if not isinstance(self.contributor_searchable, list):
            self.contributor_searchable = [self.contributor_searchable] if self.contributor_searchable is not None else []
        self.contributor_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.contributor_searchable]

        if self.model_date is not None and not isinstance(self.model_date, SearchableString):
            self.model_date = SearchableString(self.model_date)

        if self.model_date_searchable is not None and not isinstance(self.model_date_searchable, SearchableString):
            self.model_date_searchable = SearchableString(self.model_date_searchable)

        if self.model_state is not None and not isinstance(self.model_state, str):
            self.model_state = str(self.model_state)

        if not isinstance(self.comment, list):
            self.comment = [self.comment] if self.comment is not None else []
        self.comment = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.comment]

        if not isinstance(self.comment_searchable, list):
            self.comment_searchable = [self.comment_searchable] if self.comment_searchable is not None else []
        self.comment_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.comment_searchable]

        if self.owl_blob_json is not None and not isinstance(self.owl_blob_json, str):
            self.owl_blob_json = str(self.owl_blob_json)

        super().__post_init__(**kwargs)


@dataclass
class OntologyClass(YAMLRoot):
    """
    Gene Ontology Term, Synonym, or Definition.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/OntologyClass")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ontology_class"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/OntologyClass")

    document_category: Optional[str] = None
    id: Optional[str] = None
    annotation_class: Optional[str] = None
    annotation_class_label: Optional[Union[str, SearchableString]] = None
    annotation_class_label_searchable: Optional[Union[str, SearchableString]] = None
    description: Optional[Union[str, SearchableString]] = None
    description_searchable: Optional[Union[str, SearchableString]] = None
    source: Optional[str] = None
    idspace: Optional[str] = None
    is_obsolete: Optional[Union[bool, Bool]] = None
    comment: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    comment_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    synonym: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    synonym_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    alternate_id: Optional[Union[str, List[str]]] = empty_list()
    replaced_by: Optional[Union[str, List[str]]] = empty_list()
    consider: Optional[Union[str, List[str]]] = empty_list()
    subset: Optional[Union[str, List[str]]] = empty_list()
    definition_xref: Optional[Union[str, List[str]]] = empty_list()
    database_xref: Optional[Union[str, List[str]]] = empty_list()
    isa_partof_closure: Optional[Union[str, List[str]]] = empty_list()
    isa_partof_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    isa_partof_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    isa_closure: Optional[Union[str, List[str]]] = empty_list()
    isa_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    isa_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    regulates_closure: Optional[Union[str, List[str]]] = empty_list()
    regulates_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    regulates_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    topology_graph_json: Optional[str] = None
    regulates_transitivity_graph_json: Optional[str] = None
    neighborhood_graph_json: Optional[str] = None
    neighborhood_limited_graph_json: Optional[str] = None
    only_in_taxon: Optional[Union[str, SearchableString]] = None
    only_in_taxon_searchable: Optional[Union[str, SearchableString]] = None
    only_in_taxon_label: Optional[Union[str, SearchableString]] = None
    only_in_taxon_label_searchable: Optional[Union[str, SearchableString]] = None
    only_in_taxon_closure: Optional[Union[str, List[str]]] = empty_list()
    only_in_taxon_closure_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    only_in_taxon_closure_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    annotation_extension_owl_json: Optional[str] = None
    annotation_relation: Optional[str] = None
    annotation_relation_label: Optional[Union[str, SearchableString]] = None
    annotation_relation_label_searchable: Optional[Union[str, SearchableString]] = None
    equivalent_class_expressions_json: Optional[str] = None
    disjoint_class_list: Optional[Union[str, List[str]]] = empty_list()
    disjoint_class_list_label: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    disjoint_class_list_label_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.document_category is not None and not isinstance(self.document_category, str):
            self.document_category = str(self.document_category)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.annotation_class is not None and not isinstance(self.annotation_class, str):
            self.annotation_class = str(self.annotation_class)

        if self.annotation_class_label is not None and not isinstance(self.annotation_class_label, SearchableString):
            self.annotation_class_label = SearchableString(self.annotation_class_label)

        if self.annotation_class_label_searchable is not None and not isinstance(self.annotation_class_label_searchable, SearchableString):
            self.annotation_class_label_searchable = SearchableString(self.annotation_class_label_searchable)

        if self.description is not None and not isinstance(self.description, SearchableString):
            self.description = SearchableString(self.description)

        if self.description_searchable is not None and not isinstance(self.description_searchable, SearchableString):
            self.description_searchable = SearchableString(self.description_searchable)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.idspace is not None and not isinstance(self.idspace, str):
            self.idspace = str(self.idspace)

        if self.is_obsolete is not None and not isinstance(self.is_obsolete, Bool):
            self.is_obsolete = Bool(self.is_obsolete)

        if not isinstance(self.comment, list):
            self.comment = [self.comment] if self.comment is not None else []
        self.comment = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.comment]

        if not isinstance(self.comment_searchable, list):
            self.comment_searchable = [self.comment_searchable] if self.comment_searchable is not None else []
        self.comment_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.comment_searchable]

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.synonym]

        if not isinstance(self.synonym_searchable, list):
            self.synonym_searchable = [self.synonym_searchable] if self.synonym_searchable is not None else []
        self.synonym_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.synonym_searchable]

        if not isinstance(self.alternate_id, list):
            self.alternate_id = [self.alternate_id] if self.alternate_id is not None else []
        self.alternate_id = [v if isinstance(v, str) else str(v) for v in self.alternate_id]

        if not isinstance(self.replaced_by, list):
            self.replaced_by = [self.replaced_by] if self.replaced_by is not None else []
        self.replaced_by = [v if isinstance(v, str) else str(v) for v in self.replaced_by]

        if not isinstance(self.consider, list):
            self.consider = [self.consider] if self.consider is not None else []
        self.consider = [v if isinstance(v, str) else str(v) for v in self.consider]

        if not isinstance(self.subset, list):
            self.subset = [self.subset] if self.subset is not None else []
        self.subset = [v if isinstance(v, str) else str(v) for v in self.subset]

        if not isinstance(self.definition_xref, list):
            self.definition_xref = [self.definition_xref] if self.definition_xref is not None else []
        self.definition_xref = [v if isinstance(v, str) else str(v) for v in self.definition_xref]

        if not isinstance(self.database_xref, list):
            self.database_xref = [self.database_xref] if self.database_xref is not None else []
        self.database_xref = [v if isinstance(v, str) else str(v) for v in self.database_xref]

        if not isinstance(self.isa_partof_closure, list):
            self.isa_partof_closure = [self.isa_partof_closure] if self.isa_partof_closure is not None else []
        self.isa_partof_closure = [v if isinstance(v, str) else str(v) for v in self.isa_partof_closure]

        if not isinstance(self.isa_partof_closure_label, list):
            self.isa_partof_closure_label = [self.isa_partof_closure_label] if self.isa_partof_closure_label is not None else []
        self.isa_partof_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.isa_partof_closure_label]

        if not isinstance(self.isa_partof_closure_label_searchable, list):
            self.isa_partof_closure_label_searchable = [self.isa_partof_closure_label_searchable] if self.isa_partof_closure_label_searchable is not None else []
        self.isa_partof_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.isa_partof_closure_label_searchable]

        if not isinstance(self.isa_closure, list):
            self.isa_closure = [self.isa_closure] if self.isa_closure is not None else []
        self.isa_closure = [v if isinstance(v, str) else str(v) for v in self.isa_closure]

        if not isinstance(self.isa_closure_label, list):
            self.isa_closure_label = [self.isa_closure_label] if self.isa_closure_label is not None else []
        self.isa_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.isa_closure_label]

        if not isinstance(self.isa_closure_label_searchable, list):
            self.isa_closure_label_searchable = [self.isa_closure_label_searchable] if self.isa_closure_label_searchable is not None else []
        self.isa_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.isa_closure_label_searchable]

        if not isinstance(self.regulates_closure, list):
            self.regulates_closure = [self.regulates_closure] if self.regulates_closure is not None else []
        self.regulates_closure = [v if isinstance(v, str) else str(v) for v in self.regulates_closure]

        if not isinstance(self.regulates_closure_label, list):
            self.regulates_closure_label = [self.regulates_closure_label] if self.regulates_closure_label is not None else []
        self.regulates_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.regulates_closure_label]

        if not isinstance(self.regulates_closure_label_searchable, list):
            self.regulates_closure_label_searchable = [self.regulates_closure_label_searchable] if self.regulates_closure_label_searchable is not None else []
        self.regulates_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.regulates_closure_label_searchable]

        if self.topology_graph_json is not None and not isinstance(self.topology_graph_json, str):
            self.topology_graph_json = str(self.topology_graph_json)

        if self.regulates_transitivity_graph_json is not None and not isinstance(self.regulates_transitivity_graph_json, str):
            self.regulates_transitivity_graph_json = str(self.regulates_transitivity_graph_json)

        if self.neighborhood_graph_json is not None and not isinstance(self.neighborhood_graph_json, str):
            self.neighborhood_graph_json = str(self.neighborhood_graph_json)

        if self.neighborhood_limited_graph_json is not None and not isinstance(self.neighborhood_limited_graph_json, str):
            self.neighborhood_limited_graph_json = str(self.neighborhood_limited_graph_json)

        if self.only_in_taxon is not None and not isinstance(self.only_in_taxon, SearchableString):
            self.only_in_taxon = SearchableString(self.only_in_taxon)

        if self.only_in_taxon_searchable is not None and not isinstance(self.only_in_taxon_searchable, SearchableString):
            self.only_in_taxon_searchable = SearchableString(self.only_in_taxon_searchable)

        if self.only_in_taxon_label is not None and not isinstance(self.only_in_taxon_label, SearchableString):
            self.only_in_taxon_label = SearchableString(self.only_in_taxon_label)

        if self.only_in_taxon_label_searchable is not None and not isinstance(self.only_in_taxon_label_searchable, SearchableString):
            self.only_in_taxon_label_searchable = SearchableString(self.only_in_taxon_label_searchable)

        if not isinstance(self.only_in_taxon_closure, list):
            self.only_in_taxon_closure = [self.only_in_taxon_closure] if self.only_in_taxon_closure is not None else []
        self.only_in_taxon_closure = [v if isinstance(v, str) else str(v) for v in self.only_in_taxon_closure]

        if not isinstance(self.only_in_taxon_closure_label, list):
            self.only_in_taxon_closure_label = [self.only_in_taxon_closure_label] if self.only_in_taxon_closure_label is not None else []
        self.only_in_taxon_closure_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.only_in_taxon_closure_label]

        if not isinstance(self.only_in_taxon_closure_label_searchable, list):
            self.only_in_taxon_closure_label_searchable = [self.only_in_taxon_closure_label_searchable] if self.only_in_taxon_closure_label_searchable is not None else []
        self.only_in_taxon_closure_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.only_in_taxon_closure_label_searchable]

        if self.annotation_extension_owl_json is not None and not isinstance(self.annotation_extension_owl_json, str):
            self.annotation_extension_owl_json = str(self.annotation_extension_owl_json)

        if self.annotation_relation is not None and not isinstance(self.annotation_relation, str):
            self.annotation_relation = str(self.annotation_relation)

        if self.annotation_relation_label is not None and not isinstance(self.annotation_relation_label, SearchableString):
            self.annotation_relation_label = SearchableString(self.annotation_relation_label)

        if self.annotation_relation_label_searchable is not None and not isinstance(self.annotation_relation_label_searchable, SearchableString):
            self.annotation_relation_label_searchable = SearchableString(self.annotation_relation_label_searchable)

        if self.equivalent_class_expressions_json is not None and not isinstance(self.equivalent_class_expressions_json, str):
            self.equivalent_class_expressions_json = str(self.equivalent_class_expressions_json)

        if not isinstance(self.disjoint_class_list, list):
            self.disjoint_class_list = [self.disjoint_class_list] if self.disjoint_class_list is not None else []
        self.disjoint_class_list = [v if isinstance(v, str) else str(v) for v in self.disjoint_class_list]

        if not isinstance(self.disjoint_class_list_label, list):
            self.disjoint_class_list_label = [self.disjoint_class_list_label] if self.disjoint_class_list_label is not None else []
        self.disjoint_class_list_label = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.disjoint_class_list_label]

        if not isinstance(self.disjoint_class_list_label_searchable, list):
            self.disjoint_class_list_label_searchable = [self.disjoint_class_list_label_searchable] if self.disjoint_class_list_label_searchable is not None else []
        self.disjoint_class_list_label_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.disjoint_class_list_label_searchable]

        super().__post_init__(**kwargs)


@dataclass
class Family(YAMLRoot):
    """
    Information about protein (PANTHER) families.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/Family")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "family"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/Family")

    document_category: Optional[str] = None
    id: Optional[str] = None
    panther_family: Optional[Union[str, SearchableString]] = None
    panther_family_searchable: Optional[Union[str, SearchableString]] = None
    panther_family_label: Optional[Union[str, SearchableString]] = None
    panther_family_label_searchable: Optional[Union[str, SearchableString]] = None
    phylo_graph_json: Optional[str] = None
    bioentity_list: Optional[Union[str, List[str]]] = empty_list()
    bioentity_list_label: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.document_category is not None and not isinstance(self.document_category, str):
            self.document_category = str(self.document_category)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.panther_family is not None and not isinstance(self.panther_family, SearchableString):
            self.panther_family = SearchableString(self.panther_family)

        if self.panther_family_searchable is not None and not isinstance(self.panther_family_searchable, SearchableString):
            self.panther_family_searchable = SearchableString(self.panther_family_searchable)

        if self.panther_family_label is not None and not isinstance(self.panther_family_label, SearchableString):
            self.panther_family_label = SearchableString(self.panther_family_label)

        if self.panther_family_label_searchable is not None and not isinstance(self.panther_family_label_searchable, SearchableString):
            self.panther_family_label_searchable = SearchableString(self.panther_family_label_searchable)

        if self.phylo_graph_json is not None and not isinstance(self.phylo_graph_json, str):
            self.phylo_graph_json = str(self.phylo_graph_json)

        if not isinstance(self.bioentity_list, list):
            self.bioentity_list = [self.bioentity_list] if self.bioentity_list is not None else []
        self.bioentity_list = [v if isinstance(v, str) else str(v) for v in self.bioentity_list]

        if not isinstance(self.bioentity_list_label, list):
            self.bioentity_list_label = [self.bioentity_list_label] if self.bioentity_list_label is not None else []
        self.bioentity_list_label = [v if isinstance(v, str) else str(v) for v in self.bioentity_list_label]

        super().__post_init__(**kwargs)


@dataclass
class OntologyClassAc(YAMLRoot):
    """
    Easily find ontology classes in GO. For personality only - not a schema configuration.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/OntologyClassAc")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ontology_class_ac"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org//None/OntologyClassAc")

    document_category: Optional[str] = None
    id: Optional[str] = None
    annotation_class: Optional[str] = None
    annotation_class_label: Optional[Union[str, SearchableString]] = None
    annotation_class_label_searchable: Optional[Union[str, SearchableString]] = None
    synonym: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    synonym_searchable: Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]] = empty_list()
    alternate_id: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.document_category is not None and not isinstance(self.document_category, str):
            self.document_category = str(self.document_category)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.annotation_class is not None and not isinstance(self.annotation_class, str):
            self.annotation_class = str(self.annotation_class)

        if self.annotation_class_label is not None and not isinstance(self.annotation_class_label, SearchableString):
            self.annotation_class_label = SearchableString(self.annotation_class_label)

        if self.annotation_class_label_searchable is not None and not isinstance(self.annotation_class_label_searchable, SearchableString):
            self.annotation_class_label_searchable = SearchableString(self.annotation_class_label_searchable)

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.synonym]

        if not isinstance(self.synonym_searchable, list):
            self.synonym_searchable = [self.synonym_searchable] if self.synonym_searchable is not None else []
        self.synonym_searchable = [v if isinstance(v, SearchableString) else SearchableString(v) for v in self.synonym_searchable]

        if not isinstance(self.alternate_id, list):
            self.alternate_id = [self.alternate_id] if self.alternate_id is not None else []
        self.alternate_id = [v if isinstance(v, str) else str(v) for v in self.alternate_id]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.document_category = Slot(uri=DEFAULT_.document_category, name="document_category", curie=DEFAULT_.curie('document_category'),
                   model_uri=DEFAULT_.document_category, domain=None, range=Optional[str])

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=Optional[str])

slots.source = Slot(uri=DEFAULT_.source, name="source", curie=DEFAULT_.curie('source'),
                   model_uri=DEFAULT_.source, domain=None, range=Optional[str])

slots.type = Slot(uri=DEFAULT_.type, name="type", curie=DEFAULT_.curie('type'),
                   model_uri=DEFAULT_.type, domain=None, range=Optional[str])

slots.date = Slot(uri=DEFAULT_.date, name="date", curie=DEFAULT_.curie('date'),
                   model_uri=DEFAULT_.date, domain=None, range=Optional[str])

slots.assigned_by = Slot(uri=DEFAULT_.assigned_by, name="assigned_by", curie=DEFAULT_.curie('assigned_by'),
                   model_uri=DEFAULT_.assigned_by, domain=None, range=Optional[str])

slots.is_redundant_for = Slot(uri=DEFAULT_.is_redundant_for, name="is_redundant_for", curie=DEFAULT_.curie('is_redundant_for'),
                   model_uri=DEFAULT_.is_redundant_for, domain=None, range=Optional[str])

slots.taxon = Slot(uri=DEFAULT_.taxon, name="taxon", curie=DEFAULT_.curie('taxon'),
                   model_uri=DEFAULT_.taxon, domain=None, range=Optional[str])

slots.taxon_label = Slot(uri=DEFAULT_.taxon_label, name="taxon_label", curie=DEFAULT_.curie('taxon_label'),
                   model_uri=DEFAULT_.taxon_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.taxon_label_searchable = Slot(uri=DEFAULT_.taxon_label_searchable, name="taxon_label_searchable", curie=DEFAULT_.curie('taxon_label_searchable'),
                   model_uri=DEFAULT_.taxon_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.taxon_closure = Slot(uri=DEFAULT_.taxon_closure, name="taxon_closure", curie=DEFAULT_.curie('taxon_closure'),
                   model_uri=DEFAULT_.taxon_closure, domain=None, range=Optional[Union[str, List[str]]])

slots.taxon_closure_label = Slot(uri=DEFAULT_.taxon_closure_label, name="taxon_closure_label", curie=DEFAULT_.curie('taxon_closure_label'),
                   model_uri=DEFAULT_.taxon_closure_label, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.taxon_closure_label_searchable = Slot(uri=DEFAULT_.taxon_closure_label_searchable, name="taxon_closure_label_searchable", curie=DEFAULT_.curie('taxon_closure_label_searchable'),
                   model_uri=DEFAULT_.taxon_closure_label_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.taxon_subset_closure = Slot(uri=DEFAULT_.taxon_subset_closure, name="taxon_subset_closure", curie=DEFAULT_.curie('taxon_subset_closure'),
                   model_uri=DEFAULT_.taxon_subset_closure, domain=None, range=Optional[Union[str, List[str]]])

slots.taxon_subset_closure_label = Slot(uri=DEFAULT_.taxon_subset_closure_label, name="taxon_subset_closure_label", curie=DEFAULT_.curie('taxon_subset_closure_label'),
                   model_uri=DEFAULT_.taxon_subset_closure_label, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.taxon_subset_closure_label_searchable = Slot(uri=DEFAULT_.taxon_subset_closure_label_searchable, name="taxon_subset_closure_label_searchable", curie=DEFAULT_.curie('taxon_subset_closure_label_searchable'),
                   model_uri=DEFAULT_.taxon_subset_closure_label_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.secondary_taxon = Slot(uri=DEFAULT_.secondary_taxon, name="secondary_taxon", curie=DEFAULT_.curie('secondary_taxon'),
                   model_uri=DEFAULT_.secondary_taxon, domain=None, range=Optional[str])

slots.secondary_taxon_label = Slot(uri=DEFAULT_.secondary_taxon_label, name="secondary_taxon_label", curie=DEFAULT_.curie('secondary_taxon_label'),
                   model_uri=DEFAULT_.secondary_taxon_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.secondary_taxon_label_searchable = Slot(uri=DEFAULT_.secondary_taxon_label_searchable, name="secondary_taxon_label_searchable", curie=DEFAULT_.curie('secondary_taxon_label_searchable'),
                   model_uri=DEFAULT_.secondary_taxon_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.secondary_taxon_closure = Slot(uri=DEFAULT_.secondary_taxon_closure, name="secondary_taxon_closure", curie=DEFAULT_.curie('secondary_taxon_closure'),
                   model_uri=DEFAULT_.secondary_taxon_closure, domain=None, range=Optional[Union[str, List[str]]])

slots.secondary_taxon_closure_label = Slot(uri=DEFAULT_.secondary_taxon_closure_label, name="secondary_taxon_closure_label", curie=DEFAULT_.curie('secondary_taxon_closure_label'),
                   model_uri=DEFAULT_.secondary_taxon_closure_label, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.secondary_taxon_closure_label_searchable = Slot(uri=DEFAULT_.secondary_taxon_closure_label_searchable, name="secondary_taxon_closure_label_searchable", curie=DEFAULT_.curie('secondary_taxon_closure_label_searchable'),
                   model_uri=DEFAULT_.secondary_taxon_closure_label_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.isa_partof_closure = Slot(uri=DEFAULT_.isa_partof_closure, name="isa_partof_closure", curie=DEFAULT_.curie('isa_partof_closure'),
                   model_uri=DEFAULT_.isa_partof_closure, domain=None, range=Optional[Union[str, List[str]]])

slots.isa_partof_closure_label = Slot(uri=DEFAULT_.isa_partof_closure_label, name="isa_partof_closure_label", curie=DEFAULT_.curie('isa_partof_closure_label'),
                   model_uri=DEFAULT_.isa_partof_closure_label, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.isa_partof_closure_label_searchable = Slot(uri=DEFAULT_.isa_partof_closure_label_searchable, name="isa_partof_closure_label_searchable", curie=DEFAULT_.curie('isa_partof_closure_label_searchable'),
                   model_uri=DEFAULT_.isa_partof_closure_label_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.regulates_closure = Slot(uri=DEFAULT_.regulates_closure, name="regulates_closure", curie=DEFAULT_.curie('regulates_closure'),
                   model_uri=DEFAULT_.regulates_closure, domain=None, range=Optional[Union[str, List[str]]])

slots.regulates_closure_label = Slot(uri=DEFAULT_.regulates_closure_label, name="regulates_closure_label", curie=DEFAULT_.curie('regulates_closure_label'),
                   model_uri=DEFAULT_.regulates_closure_label, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.regulates_closure_label_searchable = Slot(uri=DEFAULT_.regulates_closure_label_searchable, name="regulates_closure_label_searchable", curie=DEFAULT_.curie('regulates_closure_label_searchable'),
                   model_uri=DEFAULT_.regulates_closure_label_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.has_participant_closure = Slot(uri=DEFAULT_.has_participant_closure, name="has_participant_closure", curie=DEFAULT_.curie('has_participant_closure'),
                   model_uri=DEFAULT_.has_participant_closure, domain=None, range=Optional[Union[str, List[str]]])

slots.has_participant_closure_label = Slot(uri=DEFAULT_.has_participant_closure_label, name="has_participant_closure_label", curie=DEFAULT_.curie('has_participant_closure_label'),
                   model_uri=DEFAULT_.has_participant_closure_label, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.has_participant_closure_label_searchable = Slot(uri=DEFAULT_.has_participant_closure_label_searchable, name="has_participant_closure_label_searchable", curie=DEFAULT_.curie('has_participant_closure_label_searchable'),
                   model_uri=DEFAULT_.has_participant_closure_label_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.synonym = Slot(uri=DEFAULT_.synonym, name="synonym", curie=DEFAULT_.curie('synonym'),
                   model_uri=DEFAULT_.synonym, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.synonym_searchable = Slot(uri=DEFAULT_.synonym_searchable, name="synonym_searchable", curie=DEFAULT_.curie('synonym_searchable'),
                   model_uri=DEFAULT_.synonym_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.bioentity = Slot(uri=DEFAULT_.bioentity, name="bioentity", curie=DEFAULT_.curie('bioentity'),
                   model_uri=DEFAULT_.bioentity, domain=None, range=Optional[str])

slots.bioentity_label = Slot(uri=DEFAULT_.bioentity_label, name="bioentity_label", curie=DEFAULT_.curie('bioentity_label'),
                   model_uri=DEFAULT_.bioentity_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.bioentity_label_searchable = Slot(uri=DEFAULT_.bioentity_label_searchable, name="bioentity_label_searchable", curie=DEFAULT_.curie('bioentity_label_searchable'),
                   model_uri=DEFAULT_.bioentity_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.bioentity_name = Slot(uri=DEFAULT_.bioentity_name, name="bioentity_name", curie=DEFAULT_.curie('bioentity_name'),
                   model_uri=DEFAULT_.bioentity_name, domain=None, range=Optional[Union[str, SearchableString]])

slots.bioentity_name_searchable = Slot(uri=DEFAULT_.bioentity_name_searchable, name="bioentity_name_searchable", curie=DEFAULT_.curie('bioentity_name_searchable'),
                   model_uri=DEFAULT_.bioentity_name_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.bioentity_internal_id = Slot(uri=DEFAULT_.bioentity_internal_id, name="bioentity_internal_id", curie=DEFAULT_.curie('bioentity_internal_id'),
                   model_uri=DEFAULT_.bioentity_internal_id, domain=None, range=Optional[str])

slots.qualifier = Slot(uri=DEFAULT_.qualifier, name="qualifier", curie=DEFAULT_.curie('qualifier'),
                   model_uri=DEFAULT_.qualifier, domain=None, range=Optional[Union[str, List[str]]])

slots.annotation_class = Slot(uri=DEFAULT_.annotation_class, name="annotation_class", curie=DEFAULT_.curie('annotation_class'),
                   model_uri=DEFAULT_.annotation_class, domain=None, range=Optional[str])

slots.annotation_class_label = Slot(uri=DEFAULT_.annotation_class_label, name="annotation_class_label", curie=DEFAULT_.curie('annotation_class_label'),
                   model_uri=DEFAULT_.annotation_class_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.annotation_class_label_searchable = Slot(uri=DEFAULT_.annotation_class_label_searchable, name="annotation_class_label_searchable", curie=DEFAULT_.curie('annotation_class_label_searchable'),
                   model_uri=DEFAULT_.annotation_class_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.aspect = Slot(uri=DEFAULT_.aspect, name="aspect", curie=DEFAULT_.curie('aspect'),
                   model_uri=DEFAULT_.aspect, domain=None, range=Optional[str])

slots.bioentity_isoform = Slot(uri=DEFAULT_.bioentity_isoform, name="bioentity_isoform", curie=DEFAULT_.curie('bioentity_isoform'),
                   model_uri=DEFAULT_.bioentity_isoform, domain=None, range=Optional[str])

slots.evidence_type = Slot(uri=DEFAULT_.evidence_type, name="evidence_type", curie=DEFAULT_.curie('evidence_type'),
                   model_uri=DEFAULT_.evidence_type, domain=None, range=Optional[str])

slots.evidence_type_closure = Slot(uri=DEFAULT_.evidence_type_closure, name="evidence_type_closure", curie=DEFAULT_.curie('evidence_type_closure'),
                   model_uri=DEFAULT_.evidence_type_closure, domain=None, range=Optional[Union[str, List[str]]])

slots.evidence_with = Slot(uri=DEFAULT_.evidence_with, name="evidence_with", curie=DEFAULT_.curie('evidence_with'),
                   model_uri=DEFAULT_.evidence_with, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.evidence_with_searchable = Slot(uri=DEFAULT_.evidence_with_searchable, name="evidence_with_searchable", curie=DEFAULT_.curie('evidence_with_searchable'),
                   model_uri=DEFAULT_.evidence_with_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.evidence = Slot(uri=DEFAULT_.evidence, name="evidence", curie=DEFAULT_.curie('evidence'),
                   model_uri=DEFAULT_.evidence, domain=None, range=Optional[str])

slots.evidence_label = Slot(uri=DEFAULT_.evidence_label, name="evidence_label", curie=DEFAULT_.curie('evidence_label'),
                   model_uri=DEFAULT_.evidence_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.evidence_label_searchable = Slot(uri=DEFAULT_.evidence_label_searchable, name="evidence_label_searchable", curie=DEFAULT_.curie('evidence_label_searchable'),
                   model_uri=DEFAULT_.evidence_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.evidence_closure = Slot(uri=DEFAULT_.evidence_closure, name="evidence_closure", curie=DEFAULT_.curie('evidence_closure'),
                   model_uri=DEFAULT_.evidence_closure, domain=None, range=Optional[Union[str, List[str]]])

slots.evidence_closure_label = Slot(uri=DEFAULT_.evidence_closure_label, name="evidence_closure_label", curie=DEFAULT_.curie('evidence_closure_label'),
                   model_uri=DEFAULT_.evidence_closure_label, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.evidence_closure_label_searchable = Slot(uri=DEFAULT_.evidence_closure_label_searchable, name="evidence_closure_label_searchable", curie=DEFAULT_.curie('evidence_closure_label_searchable'),
                   model_uri=DEFAULT_.evidence_closure_label_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.evidence_subset_closure = Slot(uri=DEFAULT_.evidence_subset_closure, name="evidence_subset_closure", curie=DEFAULT_.curie('evidence_subset_closure'),
                   model_uri=DEFAULT_.evidence_subset_closure, domain=None, range=Optional[Union[str, List[str]]])

slots.evidence_subset_closure_label = Slot(uri=DEFAULT_.evidence_subset_closure_label, name="evidence_subset_closure_label", curie=DEFAULT_.curie('evidence_subset_closure_label'),
                   model_uri=DEFAULT_.evidence_subset_closure_label, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.evidence_subset_closure_label_searchable = Slot(uri=DEFAULT_.evidence_subset_closure_label_searchable, name="evidence_subset_closure_label_searchable", curie=DEFAULT_.curie('evidence_subset_closure_label_searchable'),
                   model_uri=DEFAULT_.evidence_subset_closure_label_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.reference = Slot(uri=DEFAULT_.reference, name="reference", curie=DEFAULT_.curie('reference'),
                   model_uri=DEFAULT_.reference, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.reference_searchable = Slot(uri=DEFAULT_.reference_searchable, name="reference_searchable", curie=DEFAULT_.curie('reference_searchable'),
                   model_uri=DEFAULT_.reference_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.annotation_extension_class = Slot(uri=DEFAULT_.annotation_extension_class, name="annotation_extension_class", curie=DEFAULT_.curie('annotation_extension_class'),
                   model_uri=DEFAULT_.annotation_extension_class, domain=None, range=Optional[Union[str, List[str]]])

slots.annotation_extension_class_label = Slot(uri=DEFAULT_.annotation_extension_class_label, name="annotation_extension_class_label", curie=DEFAULT_.curie('annotation_extension_class_label'),
                   model_uri=DEFAULT_.annotation_extension_class_label, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.annotation_extension_class_label_searchable = Slot(uri=DEFAULT_.annotation_extension_class_label_searchable, name="annotation_extension_class_label_searchable", curie=DEFAULT_.curie('annotation_extension_class_label_searchable'),
                   model_uri=DEFAULT_.annotation_extension_class_label_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.annotation_extension_class_closure = Slot(uri=DEFAULT_.annotation_extension_class_closure, name="annotation_extension_class_closure", curie=DEFAULT_.curie('annotation_extension_class_closure'),
                   model_uri=DEFAULT_.annotation_extension_class_closure, domain=None, range=Optional[Union[str, List[str]]])

slots.annotation_extension_class_closure_label = Slot(uri=DEFAULT_.annotation_extension_class_closure_label, name="annotation_extension_class_closure_label", curie=DEFAULT_.curie('annotation_extension_class_closure_label'),
                   model_uri=DEFAULT_.annotation_extension_class_closure_label, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.annotation_extension_class_closure_label_searchable = Slot(uri=DEFAULT_.annotation_extension_class_closure_label_searchable, name="annotation_extension_class_closure_label_searchable", curie=DEFAULT_.curie('annotation_extension_class_closure_label_searchable'),
                   model_uri=DEFAULT_.annotation_extension_class_closure_label_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.annotation_extension_json = Slot(uri=DEFAULT_.annotation_extension_json, name="annotation_extension_json", curie=DEFAULT_.curie('annotation_extension_json'),
                   model_uri=DEFAULT_.annotation_extension_json, domain=None, range=Optional[Union[str, List[str]]])

slots.panther_family = Slot(uri=DEFAULT_.panther_family, name="panther_family", curie=DEFAULT_.curie('panther_family'),
                   model_uri=DEFAULT_.panther_family, domain=None, range=Optional[Union[str, SearchableString]])

slots.panther_family_searchable = Slot(uri=DEFAULT_.panther_family_searchable, name="panther_family_searchable", curie=DEFAULT_.curie('panther_family_searchable'),
                   model_uri=DEFAULT_.panther_family_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.panther_family_label = Slot(uri=DEFAULT_.panther_family_label, name="panther_family_label", curie=DEFAULT_.curie('panther_family_label'),
                   model_uri=DEFAULT_.panther_family_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.panther_family_label_searchable = Slot(uri=DEFAULT_.panther_family_label_searchable, name="panther_family_label_searchable", curie=DEFAULT_.curie('panther_family_label_searchable'),
                   model_uri=DEFAULT_.panther_family_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.geospatial_x = Slot(uri=DEFAULT_.geospatial_x, name="geospatial_x", curie=DEFAULT_.curie('geospatial_x'),
                   model_uri=DEFAULT_.geospatial_x, domain=None, range=Optional[Union[int, List[int]]])

slots.geospatial_y = Slot(uri=DEFAULT_.geospatial_y, name="geospatial_y", curie=DEFAULT_.curie('geospatial_y'),
                   model_uri=DEFAULT_.geospatial_y, domain=None, range=Optional[Union[int, List[int]]])

slots.geospatial_z = Slot(uri=DEFAULT_.geospatial_z, name="geospatial_z", curie=DEFAULT_.curie('geospatial_z'),
                   model_uri=DEFAULT_.geospatial_z, domain=None, range=Optional[Union[int, List[int]]])

slots.annotation_class_list = Slot(uri=DEFAULT_.annotation_class_list, name="annotation_class_list", curie=DEFAULT_.curie('annotation_class_list'),
                   model_uri=DEFAULT_.annotation_class_list, domain=None, range=Optional[Union[str, List[str]]])

slots.annotation_class_list_label = Slot(uri=DEFAULT_.annotation_class_list_label, name="annotation_class_list_label", curie=DEFAULT_.curie('annotation_class_list_label'),
                   model_uri=DEFAULT_.annotation_class_list_label, domain=None, range=Optional[Union[str, List[str]]])

slots.phylo_graph_json = Slot(uri=DEFAULT_.phylo_graph_json, name="phylo_graph_json", curie=DEFAULT_.curie('phylo_graph_json'),
                   model_uri=DEFAULT_.phylo_graph_json, domain=None, range=Optional[str])

slots.database_xref = Slot(uri=DEFAULT_.database_xref, name="database_xref", curie=DEFAULT_.curie('database_xref'),
                   model_uri=DEFAULT_.database_xref, domain=None, range=Optional[Union[str, List[str]]])

slots.annotation_unit = Slot(uri=DEFAULT_.annotation_unit, name="annotation_unit", curie=DEFAULT_.curie('annotation_unit'),
                   model_uri=DEFAULT_.annotation_unit, domain=None, range=Optional[str])

slots.annotation_unit_label = Slot(uri=DEFAULT_.annotation_unit_label, name="annotation_unit_label", curie=DEFAULT_.curie('annotation_unit_label'),
                   model_uri=DEFAULT_.annotation_unit_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.annotation_unit_label_searchable = Slot(uri=DEFAULT_.annotation_unit_label_searchable, name="annotation_unit_label_searchable", curie=DEFAULT_.curie('annotation_unit_label_searchable'),
                   model_uri=DEFAULT_.annotation_unit_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.annotation_group = Slot(uri=DEFAULT_.annotation_group, name="annotation_group", curie=DEFAULT_.curie('annotation_group'),
                   model_uri=DEFAULT_.annotation_group, domain=None, range=Optional[str])

slots.annotation_group_label = Slot(uri=DEFAULT_.annotation_group_label, name="annotation_group_label", curie=DEFAULT_.curie('annotation_group_label'),
                   model_uri=DEFAULT_.annotation_group_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.annotation_group_label_searchable = Slot(uri=DEFAULT_.annotation_group_label_searchable, name="annotation_group_label_searchable", curie=DEFAULT_.curie('annotation_group_label_searchable'),
                   model_uri=DEFAULT_.annotation_group_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.annotation_group_url = Slot(uri=DEFAULT_.annotation_group_url, name="annotation_group_url", curie=DEFAULT_.curie('annotation_group_url'),
                   model_uri=DEFAULT_.annotation_group_url, domain=None, range=Optional[str])

slots.enabled_by = Slot(uri=DEFAULT_.enabled_by, name="enabled_by", curie=DEFAULT_.curie('enabled_by'),
                   model_uri=DEFAULT_.enabled_by, domain=None, range=Optional[Union[str, SearchableString]])

slots.enabled_by_searchable = Slot(uri=DEFAULT_.enabled_by_searchable, name="enabled_by_searchable", curie=DEFAULT_.curie('enabled_by_searchable'),
                   model_uri=DEFAULT_.enabled_by_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.enabled_by_label = Slot(uri=DEFAULT_.enabled_by_label, name="enabled_by_label", curie=DEFAULT_.curie('enabled_by_label'),
                   model_uri=DEFAULT_.enabled_by_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.enabled_by_label_searchable = Slot(uri=DEFAULT_.enabled_by_label_searchable, name="enabled_by_label_searchable", curie=DEFAULT_.curie('enabled_by_label_searchable'),
                   model_uri=DEFAULT_.enabled_by_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.function_class = Slot(uri=DEFAULT_.function_class, name="function_class", curie=DEFAULT_.curie('function_class'),
                   model_uri=DEFAULT_.function_class, domain=None, range=Optional[str])

slots.function_class_label = Slot(uri=DEFAULT_.function_class_label, name="function_class_label", curie=DEFAULT_.curie('function_class_label'),
                   model_uri=DEFAULT_.function_class_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.function_class_label_searchable = Slot(uri=DEFAULT_.function_class_label_searchable, name="function_class_label_searchable", curie=DEFAULT_.curie('function_class_label_searchable'),
                   model_uri=DEFAULT_.function_class_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.function_class_closure = Slot(uri=DEFAULT_.function_class_closure, name="function_class_closure", curie=DEFAULT_.curie('function_class_closure'),
                   model_uri=DEFAULT_.function_class_closure, domain=None, range=Optional[Union[str, List[str]]])

slots.function_class_closure_label = Slot(uri=DEFAULT_.function_class_closure_label, name="function_class_closure_label", curie=DEFAULT_.curie('function_class_closure_label'),
                   model_uri=DEFAULT_.function_class_closure_label, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.function_class_closure_label_searchable = Slot(uri=DEFAULT_.function_class_closure_label_searchable, name="function_class_closure_label_searchable", curie=DEFAULT_.curie('function_class_closure_label_searchable'),
                   model_uri=DEFAULT_.function_class_closure_label_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.process_class = Slot(uri=DEFAULT_.process_class, name="process_class", curie=DEFAULT_.curie('process_class'),
                   model_uri=DEFAULT_.process_class, domain=None, range=Optional[str])

slots.process_class_label = Slot(uri=DEFAULT_.process_class_label, name="process_class_label", curie=DEFAULT_.curie('process_class_label'),
                   model_uri=DEFAULT_.process_class_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.process_class_label_searchable = Slot(uri=DEFAULT_.process_class_label_searchable, name="process_class_label_searchable", curie=DEFAULT_.curie('process_class_label_searchable'),
                   model_uri=DEFAULT_.process_class_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.process_class_closure = Slot(uri=DEFAULT_.process_class_closure, name="process_class_closure", curie=DEFAULT_.curie('process_class_closure'),
                   model_uri=DEFAULT_.process_class_closure, domain=None, range=Optional[Union[str, List[str]]])

slots.process_class_closure_label = Slot(uri=DEFAULT_.process_class_closure_label, name="process_class_closure_label", curie=DEFAULT_.curie('process_class_closure_label'),
                   model_uri=DEFAULT_.process_class_closure_label, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.process_class_closure_label_searchable = Slot(uri=DEFAULT_.process_class_closure_label_searchable, name="process_class_closure_label_searchable", curie=DEFAULT_.curie('process_class_closure_label_searchable'),
                   model_uri=DEFAULT_.process_class_closure_label_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.location_list = Slot(uri=DEFAULT_.location_list, name="location_list", curie=DEFAULT_.curie('location_list'),
                   model_uri=DEFAULT_.location_list, domain=None, range=Optional[Union[str, List[str]]])

slots.location_list_label = Slot(uri=DEFAULT_.location_list_label, name="location_list_label", curie=DEFAULT_.curie('location_list_label'),
                   model_uri=DEFAULT_.location_list_label, domain=None, range=Optional[Union[str, List[str]]])

slots.location_list_closure = Slot(uri=DEFAULT_.location_list_closure, name="location_list_closure", curie=DEFAULT_.curie('location_list_closure'),
                   model_uri=DEFAULT_.location_list_closure, domain=None, range=Optional[Union[str, List[str]]])

slots.location_list_closure_label = Slot(uri=DEFAULT_.location_list_closure_label, name="location_list_closure_label", curie=DEFAULT_.curie('location_list_closure_label'),
                   model_uri=DEFAULT_.location_list_closure_label, domain=None, range=Optional[Union[str, List[str]]])

slots.owl_blob_json = Slot(uri=DEFAULT_.owl_blob_json, name="owl_blob_json", curie=DEFAULT_.curie('owl_blob_json'),
                   model_uri=DEFAULT_.owl_blob_json, domain=None, range=Optional[str])

slots.topology_graph_json = Slot(uri=DEFAULT_.topology_graph_json, name="topology_graph_json", curie=DEFAULT_.curie('topology_graph_json'),
                   model_uri=DEFAULT_.topology_graph_json, domain=None, range=Optional[str])

slots.entity = Slot(uri=DEFAULT_.entity, name="entity", curie=DEFAULT_.curie('entity'),
                   model_uri=DEFAULT_.entity, domain=None, range=Optional[str])

slots.entity_label = Slot(uri=DEFAULT_.entity_label, name="entity_label", curie=DEFAULT_.curie('entity_label'),
                   model_uri=DEFAULT_.entity_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.entity_label_searchable = Slot(uri=DEFAULT_.entity_label_searchable, name="entity_label_searchable", curie=DEFAULT_.curie('entity_label_searchable'),
                   model_uri=DEFAULT_.entity_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.category = Slot(uri=DEFAULT_.category, name="category", curie=DEFAULT_.curie('category'),
                   model_uri=DEFAULT_.category, domain=None, range=Optional[str])

slots.general_blob = Slot(uri=DEFAULT_.general_blob, name="general_blob", curie=DEFAULT_.curie('general_blob'),
                   model_uri=DEFAULT_.general_blob, domain=None, range=Optional[Union[str, SearchableString]])

slots.general_blob_searchable = Slot(uri=DEFAULT_.general_blob_searchable, name="general_blob_searchable", curie=DEFAULT_.curie('general_blob_searchable'),
                   model_uri=DEFAULT_.general_blob_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.model = Slot(uri=DEFAULT_.model, name="model", curie=DEFAULT_.curie('model'),
                   model_uri=DEFAULT_.model, domain=None, range=Optional[str])

slots.model_label = Slot(uri=DEFAULT_.model_label, name="model_label", curie=DEFAULT_.curie('model_label'),
                   model_uri=DEFAULT_.model_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.model_label_searchable = Slot(uri=DEFAULT_.model_label_searchable, name="model_label_searchable", curie=DEFAULT_.curie('model_label_searchable'),
                   model_uri=DEFAULT_.model_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.model_url = Slot(uri=DEFAULT_.model_url, name="model_url", curie=DEFAULT_.curie('model_url'),
                   model_uri=DEFAULT_.model_url, domain=None, range=Optional[str])

slots.model_state = Slot(uri=DEFAULT_.model_state, name="model_state", curie=DEFAULT_.curie('model_state'),
                   model_uri=DEFAULT_.model_state, domain=None, range=Optional[str])

slots.annotation_value = Slot(uri=DEFAULT_.annotation_value, name="annotation_value", curie=DEFAULT_.curie('annotation_value'),
                   model_uri=DEFAULT_.annotation_value, domain=None, range=Optional[Union[str, List[str]]])

slots.contributor = Slot(uri=DEFAULT_.contributor, name="contributor", curie=DEFAULT_.curie('contributor'),
                   model_uri=DEFAULT_.contributor, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.contributor_searchable = Slot(uri=DEFAULT_.contributor_searchable, name="contributor_searchable", curie=DEFAULT_.curie('contributor_searchable'),
                   model_uri=DEFAULT_.contributor_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.model_date = Slot(uri=DEFAULT_.model_date, name="model_date", curie=DEFAULT_.curie('model_date'),
                   model_uri=DEFAULT_.model_date, domain=None, range=Optional[Union[str, SearchableString]])

slots.model_date_searchable = Slot(uri=DEFAULT_.model_date_searchable, name="model_date_searchable", curie=DEFAULT_.curie('model_date_searchable'),
                   model_uri=DEFAULT_.model_date_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.comment = Slot(uri=DEFAULT_.comment, name="comment", curie=DEFAULT_.curie('comment'),
                   model_uri=DEFAULT_.comment, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.comment_searchable = Slot(uri=DEFAULT_.comment_searchable, name="comment_searchable", curie=DEFAULT_.curie('comment_searchable'),
                   model_uri=DEFAULT_.comment_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.enabled_by_complex = Slot(uri=DEFAULT_.enabled_by_complex, name="enabled_by_complex", curie=DEFAULT_.curie('enabled_by_complex'),
                   model_uri=DEFAULT_.enabled_by_complex, domain=None, range=Optional[Union[str, SearchableString]])

slots.enabled_by_complex_searchable = Slot(uri=DEFAULT_.enabled_by_complex_searchable, name="enabled_by_complex_searchable", curie=DEFAULT_.curie('enabled_by_complex_searchable'),
                   model_uri=DEFAULT_.enabled_by_complex_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.enabled_by_complex_label = Slot(uri=DEFAULT_.enabled_by_complex_label, name="enabled_by_complex_label", curie=DEFAULT_.curie('enabled_by_complex_label'),
                   model_uri=DEFAULT_.enabled_by_complex_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.enabled_by_complex_label_searchable = Slot(uri=DEFAULT_.enabled_by_complex_label_searchable, name="enabled_by_complex_label_searchable", curie=DEFAULT_.curie('enabled_by_complex_label_searchable'),
                   model_uri=DEFAULT_.enabled_by_complex_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.has_participant = Slot(uri=DEFAULT_.has_participant, name="has_participant", curie=DEFAULT_.curie('has_participant'),
                   model_uri=DEFAULT_.has_participant, domain=None, range=Optional[Union[str, SearchableString]])

slots.has_participant_searchable = Slot(uri=DEFAULT_.has_participant_searchable, name="has_participant_searchable", curie=DEFAULT_.curie('has_participant_searchable'),
                   model_uri=DEFAULT_.has_participant_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.has_participant_label = Slot(uri=DEFAULT_.has_participant_label, name="has_participant_label", curie=DEFAULT_.curie('has_participant_label'),
                   model_uri=DEFAULT_.has_participant_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.has_participant_label_searchable = Slot(uri=DEFAULT_.has_participant_label_searchable, name="has_participant_label_searchable", curie=DEFAULT_.curie('has_participant_label_searchable'),
                   model_uri=DEFAULT_.has_participant_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.has_complex_participant = Slot(uri=DEFAULT_.has_complex_participant, name="has_complex_participant", curie=DEFAULT_.curie('has_complex_participant'),
                   model_uri=DEFAULT_.has_complex_participant, domain=None, range=Optional[Union[str, SearchableString]])

slots.has_complex_participant_searchable = Slot(uri=DEFAULT_.has_complex_participant_searchable, name="has_complex_participant_searchable", curie=DEFAULT_.curie('has_complex_participant_searchable'),
                   model_uri=DEFAULT_.has_complex_participant_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.has_complex_participant_label = Slot(uri=DEFAULT_.has_complex_participant_label, name="has_complex_participant_label", curie=DEFAULT_.curie('has_complex_participant_label'),
                   model_uri=DEFAULT_.has_complex_participant_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.has_complex_participant_label_searchable = Slot(uri=DEFAULT_.has_complex_participant_label_searchable, name="has_complex_participant_label_searchable", curie=DEFAULT_.curie('has_complex_participant_label_searchable'),
                   model_uri=DEFAULT_.has_complex_participant_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.has_output = Slot(uri=DEFAULT_.has_output, name="has_output", curie=DEFAULT_.curie('has_output'),
                   model_uri=DEFAULT_.has_output, domain=None, range=Optional[Union[str, SearchableString]])

slots.has_output_searchable = Slot(uri=DEFAULT_.has_output_searchable, name="has_output_searchable", curie=DEFAULT_.curie('has_output_searchable'),
                   model_uri=DEFAULT_.has_output_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.has_output_label = Slot(uri=DEFAULT_.has_output_label, name="has_output_label", curie=DEFAULT_.curie('has_output_label'),
                   model_uri=DEFAULT_.has_output_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.has_output_label_searchable = Slot(uri=DEFAULT_.has_output_label_searchable, name="has_output_label_searchable", curie=DEFAULT_.curie('has_output_label_searchable'),
                   model_uri=DEFAULT_.has_output_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.has_complex_output = Slot(uri=DEFAULT_.has_complex_output, name="has_complex_output", curie=DEFAULT_.curie('has_complex_output'),
                   model_uri=DEFAULT_.has_complex_output, domain=None, range=Optional[Union[str, SearchableString]])

slots.has_complex_output_searchable = Slot(uri=DEFAULT_.has_complex_output_searchable, name="has_complex_output_searchable", curie=DEFAULT_.curie('has_complex_output_searchable'),
                   model_uri=DEFAULT_.has_complex_output_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.has_complex_output_label = Slot(uri=DEFAULT_.has_complex_output_label, name="has_complex_output_label", curie=DEFAULT_.curie('has_complex_output_label'),
                   model_uri=DEFAULT_.has_complex_output_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.has_complex_output_label_searchable = Slot(uri=DEFAULT_.has_complex_output_label_searchable, name="has_complex_output_label_searchable", curie=DEFAULT_.curie('has_complex_output_label_searchable'),
                   model_uri=DEFAULT_.has_complex_output_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.evidence_type_label = Slot(uri=DEFAULT_.evidence_type_label, name="evidence_type_label", curie=DEFAULT_.curie('evidence_type_label'),
                   model_uri=DEFAULT_.evidence_type_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.evidence_type_label_searchable = Slot(uri=DEFAULT_.evidence_type_label_searchable, name="evidence_type_label_searchable", curie=DEFAULT_.curie('evidence_type_label_searchable'),
                   model_uri=DEFAULT_.evidence_type_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.evidence_type_closure_label = Slot(uri=DEFAULT_.evidence_type_closure_label, name="evidence_type_closure_label", curie=DEFAULT_.curie('evidence_type_closure_label'),
                   model_uri=DEFAULT_.evidence_type_closure_label, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.evidence_type_closure_label_searchable = Slot(uri=DEFAULT_.evidence_type_closure_label_searchable, name="evidence_type_closure_label_searchable", curie=DEFAULT_.curie('evidence_type_closure_label_searchable'),
                   model_uri=DEFAULT_.evidence_type_closure_label_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.relationship = Slot(uri=DEFAULT_.relationship, name="relationship", curie=DEFAULT_.curie('relationship'),
                   model_uri=DEFAULT_.relationship, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.relationship_searchable = Slot(uri=DEFAULT_.relationship_searchable, name="relationship_searchable", curie=DEFAULT_.curie('relationship_searchable'),
                   model_uri=DEFAULT_.relationship_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.relationship_label = Slot(uri=DEFAULT_.relationship_label, name="relationship_label", curie=DEFAULT_.curie('relationship_label'),
                   model_uri=DEFAULT_.relationship_label, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.relationship_label_searchable = Slot(uri=DEFAULT_.relationship_label_searchable, name="relationship_label_searchable", curie=DEFAULT_.curie('relationship_label_searchable'),
                   model_uri=DEFAULT_.relationship_label_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.description = Slot(uri=DEFAULT_.description, name="description", curie=DEFAULT_.curie('description'),
                   model_uri=DEFAULT_.description, domain=None, range=Optional[Union[str, SearchableString]])

slots.description_searchable = Slot(uri=DEFAULT_.description_searchable, name="description_searchable", curie=DEFAULT_.curie('description_searchable'),
                   model_uri=DEFAULT_.description_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.idspace = Slot(uri=DEFAULT_.idspace, name="idspace", curie=DEFAULT_.curie('idspace'),
                   model_uri=DEFAULT_.idspace, domain=None, range=Optional[str])

slots.is_obsolete = Slot(uri=DEFAULT_.is_obsolete, name="is_obsolete", curie=DEFAULT_.curie('is_obsolete'),
                   model_uri=DEFAULT_.is_obsolete, domain=None, range=Optional[Union[bool, Bool]])

slots.alternate_id = Slot(uri=DEFAULT_.alternate_id, name="alternate_id", curie=DEFAULT_.curie('alternate_id'),
                   model_uri=DEFAULT_.alternate_id, domain=None, range=Optional[Union[str, List[str]]])

slots.replaced_by = Slot(uri=DEFAULT_.replaced_by, name="replaced_by", curie=DEFAULT_.curie('replaced_by'),
                   model_uri=DEFAULT_.replaced_by, domain=None, range=Optional[Union[str, List[str]]])

slots.consider = Slot(uri=DEFAULT_.consider, name="consider", curie=DEFAULT_.curie('consider'),
                   model_uri=DEFAULT_.consider, domain=None, range=Optional[Union[str, List[str]]])

slots.subset = Slot(uri=DEFAULT_.subset, name="subset", curie=DEFAULT_.curie('subset'),
                   model_uri=DEFAULT_.subset, domain=None, range=Optional[Union[str, List[str]]])

slots.definition_xref = Slot(uri=DEFAULT_.definition_xref, name="definition_xref", curie=DEFAULT_.curie('definition_xref'),
                   model_uri=DEFAULT_.definition_xref, domain=None, range=Optional[Union[str, List[str]]])

slots.isa_closure = Slot(uri=DEFAULT_.isa_closure, name="isa_closure", curie=DEFAULT_.curie('isa_closure'),
                   model_uri=DEFAULT_.isa_closure, domain=None, range=Optional[Union[str, List[str]]])

slots.isa_closure_label = Slot(uri=DEFAULT_.isa_closure_label, name="isa_closure_label", curie=DEFAULT_.curie('isa_closure_label'),
                   model_uri=DEFAULT_.isa_closure_label, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.isa_closure_label_searchable = Slot(uri=DEFAULT_.isa_closure_label_searchable, name="isa_closure_label_searchable", curie=DEFAULT_.curie('isa_closure_label_searchable'),
                   model_uri=DEFAULT_.isa_closure_label_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.regulates_transitivity_graph_json = Slot(uri=DEFAULT_.regulates_transitivity_graph_json, name="regulates_transitivity_graph_json", curie=DEFAULT_.curie('regulates_transitivity_graph_json'),
                   model_uri=DEFAULT_.regulates_transitivity_graph_json, domain=None, range=Optional[str])

slots.neighborhood_graph_json = Slot(uri=DEFAULT_.neighborhood_graph_json, name="neighborhood_graph_json", curie=DEFAULT_.curie('neighborhood_graph_json'),
                   model_uri=DEFAULT_.neighborhood_graph_json, domain=None, range=Optional[str])

slots.neighborhood_limited_graph_json = Slot(uri=DEFAULT_.neighborhood_limited_graph_json, name="neighborhood_limited_graph_json", curie=DEFAULT_.curie('neighborhood_limited_graph_json'),
                   model_uri=DEFAULT_.neighborhood_limited_graph_json, domain=None, range=Optional[str])

slots.only_in_taxon = Slot(uri=DEFAULT_.only_in_taxon, name="only_in_taxon", curie=DEFAULT_.curie('only_in_taxon'),
                   model_uri=DEFAULT_.only_in_taxon, domain=None, range=Optional[Union[str, SearchableString]])

slots.only_in_taxon_searchable = Slot(uri=DEFAULT_.only_in_taxon_searchable, name="only_in_taxon_searchable", curie=DEFAULT_.curie('only_in_taxon_searchable'),
                   model_uri=DEFAULT_.only_in_taxon_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.only_in_taxon_label = Slot(uri=DEFAULT_.only_in_taxon_label, name="only_in_taxon_label", curie=DEFAULT_.curie('only_in_taxon_label'),
                   model_uri=DEFAULT_.only_in_taxon_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.only_in_taxon_label_searchable = Slot(uri=DEFAULT_.only_in_taxon_label_searchable, name="only_in_taxon_label_searchable", curie=DEFAULT_.curie('only_in_taxon_label_searchable'),
                   model_uri=DEFAULT_.only_in_taxon_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.only_in_taxon_closure = Slot(uri=DEFAULT_.only_in_taxon_closure, name="only_in_taxon_closure", curie=DEFAULT_.curie('only_in_taxon_closure'),
                   model_uri=DEFAULT_.only_in_taxon_closure, domain=None, range=Optional[Union[str, List[str]]])

slots.only_in_taxon_closure_label = Slot(uri=DEFAULT_.only_in_taxon_closure_label, name="only_in_taxon_closure_label", curie=DEFAULT_.curie('only_in_taxon_closure_label'),
                   model_uri=DEFAULT_.only_in_taxon_closure_label, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.only_in_taxon_closure_label_searchable = Slot(uri=DEFAULT_.only_in_taxon_closure_label_searchable, name="only_in_taxon_closure_label_searchable", curie=DEFAULT_.curie('only_in_taxon_closure_label_searchable'),
                   model_uri=DEFAULT_.only_in_taxon_closure_label_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.annotation_extension_owl_json = Slot(uri=DEFAULT_.annotation_extension_owl_json, name="annotation_extension_owl_json", curie=DEFAULT_.curie('annotation_extension_owl_json'),
                   model_uri=DEFAULT_.annotation_extension_owl_json, domain=None, range=Optional[str])

slots.annotation_relation = Slot(uri=DEFAULT_.annotation_relation, name="annotation_relation", curie=DEFAULT_.curie('annotation_relation'),
                   model_uri=DEFAULT_.annotation_relation, domain=None, range=Optional[str])

slots.annotation_relation_label = Slot(uri=DEFAULT_.annotation_relation_label, name="annotation_relation_label", curie=DEFAULT_.curie('annotation_relation_label'),
                   model_uri=DEFAULT_.annotation_relation_label, domain=None, range=Optional[Union[str, SearchableString]])

slots.annotation_relation_label_searchable = Slot(uri=DEFAULT_.annotation_relation_label_searchable, name="annotation_relation_label_searchable", curie=DEFAULT_.curie('annotation_relation_label_searchable'),
                   model_uri=DEFAULT_.annotation_relation_label_searchable, domain=None, range=Optional[Union[str, SearchableString]])

slots.equivalent_class_expressions_json = Slot(uri=DEFAULT_.equivalent_class_expressions_json, name="equivalent_class_expressions_json", curie=DEFAULT_.curie('equivalent_class_expressions_json'),
                   model_uri=DEFAULT_.equivalent_class_expressions_json, domain=None, range=Optional[str])

slots.disjoint_class_list = Slot(uri=DEFAULT_.disjoint_class_list, name="disjoint_class_list", curie=DEFAULT_.curie('disjoint_class_list'),
                   model_uri=DEFAULT_.disjoint_class_list, domain=None, range=Optional[Union[str, List[str]]])

slots.disjoint_class_list_label = Slot(uri=DEFAULT_.disjoint_class_list_label, name="disjoint_class_list_label", curie=DEFAULT_.curie('disjoint_class_list_label'),
                   model_uri=DEFAULT_.disjoint_class_list_label, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.disjoint_class_list_label_searchable = Slot(uri=DEFAULT_.disjoint_class_list_label_searchable, name="disjoint_class_list_label_searchable", curie=DEFAULT_.curie('disjoint_class_list_label_searchable'),
                   model_uri=DEFAULT_.disjoint_class_list_label_searchable, domain=None, range=Optional[Union[Union[str, SearchableString], List[Union[str, SearchableString]]]])

slots.bioentity_list = Slot(uri=DEFAULT_.bioentity_list, name="bioentity_list", curie=DEFAULT_.curie('bioentity_list'),
                   model_uri=DEFAULT_.bioentity_list, domain=None, range=Optional[Union[str, List[str]]])

slots.bioentity_list_label = Slot(uri=DEFAULT_.bioentity_list_label, name="bioentity_list_label", curie=DEFAULT_.curie('bioentity_list_label'),
                   model_uri=DEFAULT_.bioentity_list_label, domain=None, range=Optional[Union[str, List[str]]])
