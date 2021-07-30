# Auto generated from books.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-07-23 21:39
# Schema: example
#
# id: https://w3id.org/example
# description: example
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
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EXAMPLE = CurieNamespace('example', 'https://w3id.org/example')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = EXAMPLE


# Types

# Class references
class BookId(extended_str):
    pass


@dataclass
class Book(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.Book
    class_class_curie: ClassVar[str] = "example:Book"
    class_name: ClassVar[str] = "book"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.Book

    id: Union[str, BookId] = None
    book_category: Optional[Union[str, List[str]]] = empty_list()
    name: Optional[str] = None
    price: Optional[str] = None
    inStock: Optional[str] = None
    author: Optional[str] = None
    series_t: Optional[str] = None
    sequence_i: Optional[int] = None
    genre_s: Optional[str] = None
    yesno: Optional[str] = None
    blah_b: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BookId):
            self.id = BookId(self.id)

        if not isinstance(self.book_category, list):
            self.book_category = [self.book_category] if self.book_category is not None else []
        self.book_category = [v if isinstance(v, str) else str(v) for v in self.book_category]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.price is not None and not isinstance(self.price, str):
            self.price = str(self.price)

        if self.inStock is not None and not isinstance(self.inStock, str):
            self.inStock = str(self.inStock)

        if self.author is not None and not isinstance(self.author, str):
            self.author = str(self.author)

        if self.series_t is not None and not isinstance(self.series_t, str):
            self.series_t = str(self.series_t)

        if self.sequence_i is not None and not isinstance(self.sequence_i, int):
            self.sequence_i = int(self.sequence_i)

        if self.genre_s is not None and not isinstance(self.genre_s, str):
            self.genre_s = str(self.genre_s)

        if self.yesno is not None and not isinstance(self.yesno, str):
            self.yesno = str(self.yesno)

        if self.blah_b is not None and not isinstance(self.blah_b, str):
            self.blah_b = str(self.blah_b)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=EXAMPLE.id, name="id", curie=EXAMPLE.curie('id'),
                   model_uri=EXAMPLE.id, domain=None, range=URIRef)

slots.book_category = Slot(uri=EXAMPLE.book_category, name="book_category", curie=EXAMPLE.curie('book_category'),
                   model_uri=EXAMPLE.book_category, domain=None, range=Optional[Union[str, List[str]]])

slots.name = Slot(uri=EXAMPLE.name, name="name", curie=EXAMPLE.curie('name'),
                   model_uri=EXAMPLE.name, domain=None, range=Optional[str])

slots.price = Slot(uri=EXAMPLE.price, name="price", curie=EXAMPLE.curie('price'),
                   model_uri=EXAMPLE.price, domain=None, range=Optional[str])

slots.inStock = Slot(uri=EXAMPLE.inStock, name="inStock", curie=EXAMPLE.curie('inStock'),
                   model_uri=EXAMPLE.inStock, domain=None, range=Optional[str])

slots.author = Slot(uri=EXAMPLE.author, name="author", curie=EXAMPLE.curie('author'),
                   model_uri=EXAMPLE.author, domain=None, range=Optional[str])

slots.series_t = Slot(uri=EXAMPLE.series_t, name="series_t", curie=EXAMPLE.curie('series_t'),
                   model_uri=EXAMPLE.series_t, domain=None, range=Optional[str])

slots.sequence_i = Slot(uri=EXAMPLE.sequence_i, name="sequence_i", curie=EXAMPLE.curie('sequence_i'),
                   model_uri=EXAMPLE.sequence_i, domain=None, range=Optional[int])

slots.genre_s = Slot(uri=EXAMPLE.genre_s, name="genre_s", curie=EXAMPLE.curie('genre_s'),
                   model_uri=EXAMPLE.genre_s, domain=None, range=Optional[str])

slots.yesno = Slot(uri=EXAMPLE.yesno, name="yesno", curie=EXAMPLE.curie('yesno'),
                   model_uri=EXAMPLE.yesno, domain=None, range=Optional[str])

slots.blah_b = Slot(uri=EXAMPLE.blah_b, name="blah_b", curie=EXAMPLE.curie('blah_b'),
                   model_uri=EXAMPLE.blah_b, domain=None, range=Optional[str])

slots._version_ = Slot(uri=EXAMPLE._version_, name="_version_", curie=EXAMPLE.curie('_version_'),
                   model_uri=EXAMPLE._version_, domain=None, range=Optional[str])
