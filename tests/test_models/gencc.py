# Auto generated from gencc.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-12-23T17:43:14
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
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EXAMPLE = CurieNamespace('example', 'https://w3id.org/example')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = EXAMPLE


# Types
class HGNCIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "HGNC identifier"
    type_model_uri = EXAMPLE.HGNCIdentifier


class MONDOIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "MONDO identifier"
    type_model_uri = EXAMPLE.MONDOIdentifier


class Identifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "identifier"
    type_model_uri = EXAMPLE.Identifier


class GENCCIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "GENCC identifier"
    type_model_uri = EXAMPLE.GENCCIdentifier


class HPIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "HP identifier"
    type_model_uri = EXAMPLE.HPIdentifier


class HttpsIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "https identifier"
    type_model_uri = EXAMPLE.HttpsIdentifier


# Class references



@dataclass
class Container(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.Container
    class_class_curie: ClassVar[str] = "example:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.Container

    associations: Optional[Union[Union[dict, "GeneToDiseaseAssociation"], List[Union[dict, "GeneToDiseaseAssociation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.associations, list):
            self.associations = [self.associations] if self.associations is not None else []
        self.associations = [v if isinstance(v, GeneToDiseaseAssociation) else GeneToDiseaseAssociation(**as_dict(v)) for v in self.associations]

        super().__post_init__(**kwargs)


@dataclass
class GeneToDiseaseAssociation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.GeneToDiseaseAssociation
    class_class_curie: ClassVar[str] = "example:GeneToDiseaseAssociation"
    class_name: ClassVar[str] = "GeneToDiseaseAssociation"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.GeneToDiseaseAssociation

    uuid: Optional[str] = None
    gene_curie: Optional[Union[str, HGNCIdentifier]] = None
    gene_symbol: Optional[str] = None
    disease_curie: Optional[Union[str, MONDOIdentifier]] = None
    disease_title: Optional[str] = None
    disease_original_curie: Optional[Union[str, Identifier]] = None
    disease_original_title: Optional[str] = None
    classification_curie: Optional[Union[str, GENCCIdentifier]] = None
    classification_title: Optional[Union[str, "ClassificationTitleEnum"]] = None
    moi_curie: Optional[Union[str, HPIdentifier]] = None
    moi_title: Optional[str] = None
    submitter_curie: Optional[Union[str, GENCCIdentifier]] = None
    submitter_title: Optional[Union[str, List[str]]] = empty_list()
    submitted_as_hgnc_id: Optional[Union[str, HGNCIdentifier]] = None
    submitted_as_hgnc_symbol: Optional[str] = None
    submitted_as_disease_id: Optional[Union[str, Identifier]] = None
    submitted_as_disease_name: Optional[str] = None
    submitted_as_moi_id: Optional[Union[str, HPIdentifier]] = None
    submitted_as_moi_name: Optional[str] = None
    submitted_as_submitter_id: Optional[Union[str, GENCCIdentifier]] = None
    submitted_as_submitter_name: Optional[str] = None
    submitted_as_classification_id: Optional[Union[str, GENCCIdentifier]] = None
    submitted_as_classification_name: Optional[Union[str, "SubmittedAsClassificationNameEnum"]] = None
    submitted_as_date: Optional[str] = None
    submitted_as_public_report_url: Optional[Union[str, HttpsIdentifier]] = None
    submitted_as_notes: Optional[str] = None
    submitted_as_pmids: Optional[str] = None
    submitted_as_assertion_criteria_url: Optional[Union[str, Identifier]] = None
    submitted_as_submission_id: Optional[str] = None
    submitted_run_date: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.uuid is not None and not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.gene_curie is not None and not isinstance(self.gene_curie, HGNCIdentifier):
            self.gene_curie = HGNCIdentifier(self.gene_curie)

        if self.gene_symbol is not None and not isinstance(self.gene_symbol, str):
            self.gene_symbol = str(self.gene_symbol)

        if self.disease_curie is not None and not isinstance(self.disease_curie, MONDOIdentifier):
            self.disease_curie = MONDOIdentifier(self.disease_curie)

        if self.disease_title is not None and not isinstance(self.disease_title, str):
            self.disease_title = str(self.disease_title)

        if self.disease_original_curie is not None and not isinstance(self.disease_original_curie, Identifier):
            self.disease_original_curie = Identifier(self.disease_original_curie)

        if self.disease_original_title is not None and not isinstance(self.disease_original_title, str):
            self.disease_original_title = str(self.disease_original_title)

        if self.classification_curie is not None and not isinstance(self.classification_curie, GENCCIdentifier):
            self.classification_curie = GENCCIdentifier(self.classification_curie)

        if self.classification_title is not None and not isinstance(self.classification_title, ClassificationTitleEnum):
            self.classification_title = ClassificationTitleEnum(self.classification_title)

        if self.moi_curie is not None and not isinstance(self.moi_curie, HPIdentifier):
            self.moi_curie = HPIdentifier(self.moi_curie)

        if self.moi_title is not None and not isinstance(self.moi_title, str):
            self.moi_title = str(self.moi_title)

        if self.submitter_curie is not None and not isinstance(self.submitter_curie, GENCCIdentifier):
            self.submitter_curie = GENCCIdentifier(self.submitter_curie)

        if not isinstance(self.submitter_title, list):
            self.submitter_title = [self.submitter_title] if self.submitter_title is not None else []
        self.submitter_title = [v if isinstance(v, str) else str(v) for v in self.submitter_title]

        if self.submitted_as_hgnc_id is not None and not isinstance(self.submitted_as_hgnc_id, HGNCIdentifier):
            self.submitted_as_hgnc_id = HGNCIdentifier(self.submitted_as_hgnc_id)

        if self.submitted_as_hgnc_symbol is not None and not isinstance(self.submitted_as_hgnc_symbol, str):
            self.submitted_as_hgnc_symbol = str(self.submitted_as_hgnc_symbol)

        if self.submitted_as_disease_id is not None and not isinstance(self.submitted_as_disease_id, Identifier):
            self.submitted_as_disease_id = Identifier(self.submitted_as_disease_id)

        if self.submitted_as_disease_name is not None and not isinstance(self.submitted_as_disease_name, str):
            self.submitted_as_disease_name = str(self.submitted_as_disease_name)

        if self.submitted_as_moi_id is not None and not isinstance(self.submitted_as_moi_id, HPIdentifier):
            self.submitted_as_moi_id = HPIdentifier(self.submitted_as_moi_id)

        if self.submitted_as_moi_name is not None and not isinstance(self.submitted_as_moi_name, str):
            self.submitted_as_moi_name = str(self.submitted_as_moi_name)

        if self.submitted_as_submitter_id is not None and not isinstance(self.submitted_as_submitter_id, GENCCIdentifier):
            self.submitted_as_submitter_id = GENCCIdentifier(self.submitted_as_submitter_id)

        if self.submitted_as_submitter_name is not None and not isinstance(self.submitted_as_submitter_name, str):
            self.submitted_as_submitter_name = str(self.submitted_as_submitter_name)

        if self.submitted_as_classification_id is not None and not isinstance(self.submitted_as_classification_id, GENCCIdentifier):
            self.submitted_as_classification_id = GENCCIdentifier(self.submitted_as_classification_id)

        if self.submitted_as_classification_name is not None and not isinstance(self.submitted_as_classification_name, SubmittedAsClassificationNameEnum):
            self.submitted_as_classification_name = SubmittedAsClassificationNameEnum(self.submitted_as_classification_name)

        if self.submitted_as_date is not None and not isinstance(self.submitted_as_date, str):
            self.submitted_as_date = str(self.submitted_as_date)

        if self.submitted_as_public_report_url is not None and not isinstance(self.submitted_as_public_report_url, HttpsIdentifier):
            self.submitted_as_public_report_url = HttpsIdentifier(self.submitted_as_public_report_url)

        if self.submitted_as_notes is not None and not isinstance(self.submitted_as_notes, str):
            self.submitted_as_notes = str(self.submitted_as_notes)

        if self.submitted_as_pmids is not None and not isinstance(self.submitted_as_pmids, str):
            self.submitted_as_pmids = str(self.submitted_as_pmids)

        if self.submitted_as_assertion_criteria_url is not None and not isinstance(self.submitted_as_assertion_criteria_url, Identifier):
            self.submitted_as_assertion_criteria_url = Identifier(self.submitted_as_assertion_criteria_url)

        if self.submitted_as_submission_id is not None and not isinstance(self.submitted_as_submission_id, str):
            self.submitted_as_submission_id = str(self.submitted_as_submission_id)

        if self.submitted_run_date is not None and not isinstance(self.submitted_run_date, str):
            self.submitted_run_date = str(self.submitted_run_date)

        super().__post_init__(**kwargs)


# Enumerations
class ClassificationTitleEnum(EnumDefinitionImpl):

    Definitive = PermissibleValue(text="Definitive",
                                           description="Definitive")
    Strong = PermissibleValue(text="Strong",
                                   description="Strong")
    Limited = PermissibleValue(text="Limited",
                                     description="Limited")
    Moderate = PermissibleValue(text="Moderate",
                                       description="Moderate")

    _defn = EnumDefinition(
        name="ClassificationTitleEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Refuted Evidence",
                PermissibleValue(text="Refuted Evidence",
                                 description="Refuted Evidence") )
        setattr(cls, "No Known Disease Relationship",
                PermissibleValue(text="No Known Disease Relationship",
                                 description="No Known Disease Relationship") )
        setattr(cls, "Disputed Evidence",
                PermissibleValue(text="Disputed Evidence",
                                 description="Disputed Evidence") )

class SubmittedAsClassificationNameEnum(EnumDefinitionImpl):

    Definitive = PermissibleValue(text="Definitive",
                                           description="Definitive")
    Refuted = PermissibleValue(text="Refuted",
                                     description="Refuted")
    Strong = PermissibleValue(text="Strong",
                                   description="Strong")
    STRONG = PermissibleValue(text="STRONG",
                                   description="STRONG")
    Limited = PermissibleValue(text="Limited",
                                     description="Limited")
    Moderate = PermissibleValue(text="Moderate",
                                       description="Moderate")
    Slight = PermissibleValue(text="Slight",
                                   description="Slight")
    Disputed = PermissibleValue(text="Disputed",
                                       description="Disputed")
    LIMITED = PermissibleValue(text="LIMITED",
                                     description="LIMITED")
    Modeare = PermissibleValue(text="Modeare",
                                     description="Modeare")

    _defn = EnumDefinition(
        name="SubmittedAsClassificationNameEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Disputed evidence",
                PermissibleValue(text="Disputed evidence",
                                 description="Disputed evidence") )
        setattr(cls, "No Known Disease Relationship",
                PermissibleValue(text="No Known Disease Relationship",
                                 description="No Known Disease Relationship") )
        setattr(cls, "Refuted Evidence",
                PermissibleValue(text="Refuted Evidence",
                                 description="Refuted Evidence") )
        setattr(cls, "Disputed Evidence",
                PermissibleValue(text="Disputed Evidence",
                                 description="Disputed Evidence") )

# Slots
class slots:
    pass

slots.associations = Slot(uri=EXAMPLE.associations, name="associations", curie=EXAMPLE.curie('associations'),
                   model_uri=EXAMPLE.associations, domain=None, range=Optional[Union[Union[dict, GeneToDiseaseAssociation], List[Union[dict, GeneToDiseaseAssociation]]]])

slots.uuid = Slot(uri=EXAMPLE.uuid, name="uuid", curie=EXAMPLE.curie('uuid'),
                   model_uri=EXAMPLE.uuid, domain=None, range=Optional[str])

slots.gene_curie = Slot(uri=EXAMPLE.gene_curie, name="gene_curie", curie=EXAMPLE.curie('gene_curie'),
                   model_uri=EXAMPLE.gene_curie, domain=None, range=Optional[Union[str, HGNCIdentifier]])

slots.gene_symbol = Slot(uri=EXAMPLE.gene_symbol, name="gene_symbol", curie=EXAMPLE.curie('gene_symbol'),
                   model_uri=EXAMPLE.gene_symbol, domain=None, range=Optional[str])

slots.disease_curie = Slot(uri=EXAMPLE.disease_curie, name="disease_curie", curie=EXAMPLE.curie('disease_curie'),
                   model_uri=EXAMPLE.disease_curie, domain=None, range=Optional[Union[str, MONDOIdentifier]])

slots.disease_title = Slot(uri=EXAMPLE.disease_title, name="disease_title", curie=EXAMPLE.curie('disease_title'),
                   model_uri=EXAMPLE.disease_title, domain=None, range=Optional[str])

slots.disease_original_curie = Slot(uri=EXAMPLE.disease_original_curie, name="disease_original_curie", curie=EXAMPLE.curie('disease_original_curie'),
                   model_uri=EXAMPLE.disease_original_curie, domain=None, range=Optional[Union[str, Identifier]])

slots.disease_original_title = Slot(uri=EXAMPLE.disease_original_title, name="disease_original_title", curie=EXAMPLE.curie('disease_original_title'),
                   model_uri=EXAMPLE.disease_original_title, domain=None, range=Optional[str])

slots.classification_curie = Slot(uri=EXAMPLE.classification_curie, name="classification_curie", curie=EXAMPLE.curie('classification_curie'),
                   model_uri=EXAMPLE.classification_curie, domain=None, range=Optional[Union[str, GENCCIdentifier]])

slots.classification_title = Slot(uri=EXAMPLE.classification_title, name="classification_title", curie=EXAMPLE.curie('classification_title'),
                   model_uri=EXAMPLE.classification_title, domain=None, range=Optional[Union[str, "ClassificationTitleEnum"]])

slots.moi_curie = Slot(uri=EXAMPLE.moi_curie, name="moi_curie", curie=EXAMPLE.curie('moi_curie'),
                   model_uri=EXAMPLE.moi_curie, domain=None, range=Optional[Union[str, HPIdentifier]])

slots.moi_title = Slot(uri=EXAMPLE.moi_title, name="moi_title", curie=EXAMPLE.curie('moi_title'),
                   model_uri=EXAMPLE.moi_title, domain=None, range=Optional[str])

slots.submitter_curie = Slot(uri=EXAMPLE.submitter_curie, name="submitter_curie", curie=EXAMPLE.curie('submitter_curie'),
                   model_uri=EXAMPLE.submitter_curie, domain=None, range=Optional[Union[str, GENCCIdentifier]])

slots.submitter_title = Slot(uri=EXAMPLE.submitter_title, name="submitter_title", curie=EXAMPLE.curie('submitter_title'),
                   model_uri=EXAMPLE.submitter_title, domain=None, range=Optional[Union[str, List[str]]])

slots.submitted_as_hgnc_id = Slot(uri=EXAMPLE.submitted_as_hgnc_id, name="submitted_as_hgnc_id", curie=EXAMPLE.curie('submitted_as_hgnc_id'),
                   model_uri=EXAMPLE.submitted_as_hgnc_id, domain=None, range=Optional[Union[str, HGNCIdentifier]])

slots.submitted_as_hgnc_symbol = Slot(uri=EXAMPLE.submitted_as_hgnc_symbol, name="submitted_as_hgnc_symbol", curie=EXAMPLE.curie('submitted_as_hgnc_symbol'),
                   model_uri=EXAMPLE.submitted_as_hgnc_symbol, domain=None, range=Optional[str])

slots.submitted_as_disease_id = Slot(uri=EXAMPLE.submitted_as_disease_id, name="submitted_as_disease_id", curie=EXAMPLE.curie('submitted_as_disease_id'),
                   model_uri=EXAMPLE.submitted_as_disease_id, domain=None, range=Optional[Union[str, Identifier]])

slots.submitted_as_disease_name = Slot(uri=EXAMPLE.submitted_as_disease_name, name="submitted_as_disease_name", curie=EXAMPLE.curie('submitted_as_disease_name'),
                   model_uri=EXAMPLE.submitted_as_disease_name, domain=None, range=Optional[str])

slots.submitted_as_moi_id = Slot(uri=EXAMPLE.submitted_as_moi_id, name="submitted_as_moi_id", curie=EXAMPLE.curie('submitted_as_moi_id'),
                   model_uri=EXAMPLE.submitted_as_moi_id, domain=None, range=Optional[Union[str, HPIdentifier]])

slots.submitted_as_moi_name = Slot(uri=EXAMPLE.submitted_as_moi_name, name="submitted_as_moi_name", curie=EXAMPLE.curie('submitted_as_moi_name'),
                   model_uri=EXAMPLE.submitted_as_moi_name, domain=None, range=Optional[str])

slots.submitted_as_submitter_id = Slot(uri=EXAMPLE.submitted_as_submitter_id, name="submitted_as_submitter_id", curie=EXAMPLE.curie('submitted_as_submitter_id'),
                   model_uri=EXAMPLE.submitted_as_submitter_id, domain=None, range=Optional[Union[str, GENCCIdentifier]])

slots.submitted_as_submitter_name = Slot(uri=EXAMPLE.submitted_as_submitter_name, name="submitted_as_submitter_name", curie=EXAMPLE.curie('submitted_as_submitter_name'),
                   model_uri=EXAMPLE.submitted_as_submitter_name, domain=None, range=Optional[str])

slots.submitted_as_classification_id = Slot(uri=EXAMPLE.submitted_as_classification_id, name="submitted_as_classification_id", curie=EXAMPLE.curie('submitted_as_classification_id'),
                   model_uri=EXAMPLE.submitted_as_classification_id, domain=None, range=Optional[Union[str, GENCCIdentifier]])

slots.submitted_as_classification_name = Slot(uri=EXAMPLE.submitted_as_classification_name, name="submitted_as_classification_name", curie=EXAMPLE.curie('submitted_as_classification_name'),
                   model_uri=EXAMPLE.submitted_as_classification_name, domain=None, range=Optional[Union[str, "SubmittedAsClassificationNameEnum"]])

slots.submitted_as_date = Slot(uri=EXAMPLE.submitted_as_date, name="submitted_as_date", curie=EXAMPLE.curie('submitted_as_date'),
                   model_uri=EXAMPLE.submitted_as_date, domain=None, range=Optional[str])

slots.submitted_as_public_report_url = Slot(uri=EXAMPLE.submitted_as_public_report_url, name="submitted_as_public_report_url", curie=EXAMPLE.curie('submitted_as_public_report_url'),
                   model_uri=EXAMPLE.submitted_as_public_report_url, domain=None, range=Optional[Union[str, HttpsIdentifier]])

slots.submitted_as_notes = Slot(uri=EXAMPLE.submitted_as_notes, name="submitted_as_notes", curie=EXAMPLE.curie('submitted_as_notes'),
                   model_uri=EXAMPLE.submitted_as_notes, domain=None, range=Optional[str])

slots.submitted_as_pmids = Slot(uri=EXAMPLE.submitted_as_pmids, name="submitted_as_pmids", curie=EXAMPLE.curie('submitted_as_pmids'),
                   model_uri=EXAMPLE.submitted_as_pmids, domain=None, range=Optional[str])

slots.submitted_as_assertion_criteria_url = Slot(uri=EXAMPLE.submitted_as_assertion_criteria_url, name="submitted_as_assertion_criteria_url", curie=EXAMPLE.curie('submitted_as_assertion_criteria_url'),
                   model_uri=EXAMPLE.submitted_as_assertion_criteria_url, domain=None, range=Optional[Union[str, Identifier]])

slots.submitted_as_submission_id = Slot(uri=EXAMPLE.submitted_as_submission_id, name="submitted_as_submission_id", curie=EXAMPLE.curie('submitted_as_submission_id'),
                   model_uri=EXAMPLE.submitted_as_submission_id, domain=None, range=Optional[str])

slots.submitted_run_date = Slot(uri=EXAMPLE.submitted_run_date, name="submitted_run_date", curie=EXAMPLE.curie('submitted_run_date'),
                   model_uri=EXAMPLE.submitted_run_date, domain=None, range=Optional[str])
