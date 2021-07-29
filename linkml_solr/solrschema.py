# Auto generated from solrschema.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-07-25 18:10
# Schema: solr-schema
#
# id: https://w3id.org/linkml/solr
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
BOOLEAN = CurieNamespace('boolean', 'http://example.org/UNKNOWN/boolean/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SOLR = CurieNamespace('solr', 'https://w3id.org/linkml/solr/')
DEFAULT_ = SOLR


# Types

# Class references
class FieldName(extended_str):
    pass


class DynamicFieldName(extended_str):
    pass


class FieldTypeName(extended_str):
    pass


@dataclass
class Field(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOLR.Field
    class_class_curie: ClassVar[str] = "solr:Field"
    class_name: ClassVar[str] = "Field"
    class_model_uri: ClassVar[URIRef] = SOLR.Field

    name: Union[str, FieldName] = None
    type: Optional[str] = None
    stored: Optional[str] = None
    indexed: Optional[str] = None
    multiValued: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, FieldName):
            self.name = FieldName(self.name)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.stored is not None and not isinstance(self.stored, str):
            self.stored = str(self.stored)

        if self.indexed is not None and not isinstance(self.indexed, str):
            self.indexed = str(self.indexed)

        if self.multiValued is not None and not isinstance(self.multiValued, Bool):
            self.multiValued = Bool(self.multiValued)

        super().__post_init__(**kwargs)


@dataclass
class DynamicField(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOLR.DynamicField
    class_class_curie: ClassVar[str] = "solr:DynamicField"
    class_name: ClassVar[str] = "DynamicField"
    class_model_uri: ClassVar[URIRef] = SOLR.DynamicField

    name: Union[str, DynamicFieldName] = None
    type: Optional[str] = None
    stored: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DynamicFieldName):
            self.name = DynamicFieldName(self.name)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.stored is not None and not isinstance(self.stored, str):
            self.stored = str(self.stored)

        super().__post_init__(**kwargs)


@dataclass
class CopyField(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOLR.CopyField
    class_class_curie: ClassVar[str] = "solr:CopyField"
    class_name: ClassVar[str] = "CopyField"
    class_model_uri: ClassVar[URIRef] = SOLR.CopyField

    source: str = None
    dest: Union[str, List[str]] = None
    maxChars: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self._is_empty(self.dest):
            self.MissingRequiredField("dest")
        if not isinstance(self.dest, list):
            self.dest = [self.dest] if self.dest is not None else []
        self.dest = [v if isinstance(v, str) else str(v) for v in self.dest]

        if self.maxChars is not None and not isinstance(self.maxChars, int):
            self.maxChars = int(self.maxChars)

        super().__post_init__(**kwargs)


@dataclass
class FieldType(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOLR.FieldType
    class_class_curie: ClassVar[str] = "solr:FieldType"
    class_name: ClassVar[str] = "FieldType"
    class_model_uri: ClassVar[URIRef] = SOLR.FieldType

    name: Union[str, FieldTypeName] = None
    _class: Optional[str] = None
    positionIncrementGap: Optional[str] = None
    analyzer: Optional[Union[dict, "Analyzer"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, FieldTypeName):
            self.name = FieldTypeName(self.name)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        if self.positionIncrementGap is not None and not isinstance(self.positionIncrementGap, str):
            self.positionIncrementGap = str(self.positionIncrementGap)

        if self.analyzer is not None and not isinstance(self.analyzer, Analyzer):
            self.analyzer = Analyzer(**as_dict(self.analyzer))

        super().__post_init__(**kwargs)


@dataclass
class Analyzer(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOLR.Analyzer
    class_class_curie: ClassVar[str] = "solr:Analyzer"
    class_name: ClassVar[str] = "Analyzer"
    class_model_uri: ClassVar[URIRef] = SOLR.Analyzer

    charFilters: Optional[Union[str, List[str]]] = empty_list()
    tokenizer: Optional[Union[dict, "Tokenizer"]] = None
    filters: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.charFilters, list):
            self.charFilters = [self.charFilters] if self.charFilters is not None else []
        self.charFilters = [v if isinstance(v, str) else str(v) for v in self.charFilters]

        if self.tokenizer is not None and not isinstance(self.tokenizer, Tokenizer):
            self.tokenizer = Tokenizer(**as_dict(self.tokenizer))

        if not isinstance(self.filters, list):
            self.filters = [self.filters] if self.filters is not None else []
        self.filters = [v if isinstance(v, str) else str(v) for v in self.filters]

        super().__post_init__(**kwargs)


@dataclass
class Tokenizer(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOLR.Tokenizer
    class_class_curie: ClassVar[str] = "solr:Tokenizer"
    class_name: ClassVar[str] = "Tokenizer"
    class_model_uri: ClassVar[URIRef] = SOLR.Tokenizer

    _class: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        super().__post_init__(**kwargs)


@dataclass
class CharFilter(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOLR.CharFilter
    class_class_curie: ClassVar[str] = "solr:CharFilter"
    class_name: ClassVar[str] = "CharFilter"
    class_model_uri: ClassVar[URIRef] = SOLR.CharFilter

    _class: Optional[str] = None
    replacement: Optional[str] = None
    pattern: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        if self.replacement is not None and not isinstance(self.replacement, str):
            self.replacement = str(self.replacement)

        if self.pattern is not None and not isinstance(self.pattern, str):
            self.pattern = str(self.pattern)

        super().__post_init__(**kwargs)


@dataclass
class Filter(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOLR.Filter
    class_class_curie: ClassVar[str] = "solr:Filter"
    class_name: ClassVar[str] = "Filter"
    class_model_uri: ClassVar[URIRef] = SOLR.Filter

    _class: Optional[str] = None
    preserveOriginal: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        if self.preserveOriginal is not None and not isinstance(self.preserveOriginal, str):
            self.preserveOriginal = str(self.preserveOriginal)

        super().__post_init__(**kwargs)


@dataclass
class Transaction(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOLR.Transaction
    class_class_curie: ClassVar[str] = "solr:Transaction"
    class_name: ClassVar[str] = "transaction"
    class_model_uri: ClassVar[URIRef] = SOLR.Transaction

    add_field: Optional[Union[Dict[Union[str, FieldName], Union[dict, Field]], List[Union[dict, Field]]]] = empty_dict()
    delete_field: Optional[Union[Union[str, FieldName], List[Union[str, FieldName]]]] = empty_list()
    replace_field: Optional[Union[Union[str, FieldName], List[Union[str, FieldName]]]] = empty_list()
    add_field_type: Optional[Union[Dict[Union[str, FieldTypeName], Union[dict, FieldType]], List[Union[dict, FieldType]]]] = empty_dict()
    delete_field_type: Optional[Union[Union[str, FieldTypeName], List[Union[str, FieldTypeName]]]] = empty_list()
    replace_field_type: Optional[Union[Union[str, FieldTypeName], List[Union[str, FieldTypeName]]]] = empty_list()
    add_dynamic_field: Optional[Union[Dict[Union[str, DynamicFieldName], Union[dict, DynamicField]], List[Union[dict, DynamicField]]]] = empty_dict()
    delete_dynamic_field: Optional[Union[Union[str, DynamicFieldName], List[Union[str, DynamicFieldName]]]] = empty_list()
    replace_dynamic_field: Optional[Union[Union[str, DynamicFieldName], List[Union[str, DynamicFieldName]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="add_field", slot_type=Field, key_name="name", keyed=True)

        if not isinstance(self.delete_field, list):
            self.delete_field = [self.delete_field] if self.delete_field is not None else []
        self.delete_field = [v if isinstance(v, FieldName) else FieldName(v) for v in self.delete_field]

        if not isinstance(self.replace_field, list):
            self.replace_field = [self.replace_field] if self.replace_field is not None else []
        self.replace_field = [v if isinstance(v, FieldName) else FieldName(v) for v in self.replace_field]

        self._normalize_inlined_as_list(slot_name="add_field_type", slot_type=FieldType, key_name="name", keyed=True)

        if not isinstance(self.delete_field_type, list):
            self.delete_field_type = [self.delete_field_type] if self.delete_field_type is not None else []
        self.delete_field_type = [v if isinstance(v, FieldTypeName) else FieldTypeName(v) for v in self.delete_field_type]

        if not isinstance(self.replace_field_type, list):
            self.replace_field_type = [self.replace_field_type] if self.replace_field_type is not None else []
        self.replace_field_type = [v if isinstance(v, FieldTypeName) else FieldTypeName(v) for v in self.replace_field_type]

        self._normalize_inlined_as_list(slot_name="add_dynamic_field", slot_type=DynamicField, key_name="name", keyed=True)

        if not isinstance(self.delete_dynamic_field, list):
            self.delete_dynamic_field = [self.delete_dynamic_field] if self.delete_dynamic_field is not None else []
        self.delete_dynamic_field = [v if isinstance(v, DynamicFieldName) else DynamicFieldName(v) for v in self.delete_dynamic_field]

        if not isinstance(self.replace_dynamic_field, list):
            self.replace_dynamic_field = [self.replace_dynamic_field] if self.replace_dynamic_field is not None else []
        self.replace_dynamic_field = [v if isinstance(v, DynamicFieldName) else DynamicFieldName(v) for v in self.replace_dynamic_field]

        super().__post_init__(**kwargs)


# Enumerations


# Slots

