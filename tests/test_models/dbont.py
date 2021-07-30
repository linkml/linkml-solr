# Auto generated from dbont.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-07-19 17:38
# Schema: dbpedia-ontology
#
# id: http://dbpedia.org/ontology/
# description: dbpedia ontology schema
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
from linkml_runtime.linkml_model.types import Date, Double, Integer, String
from linkml_runtime.utils.metamodelcore import XSDDate

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DBONT = CurieNamespace('dbont', 'http://dbpedia.org/ontology/')
DBPROPERTY = CurieNamespace('dbproperty', 'http://dbpedia.org/property/')
DBR = CurieNamespace('dbr', 'http://dbpedia.org/resource/')
DCE = CurieNamespace('dce', 'http://purl.org/dc/elements/1.1/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
GEO = CurieNamespace('geo', 'http://www.w3.org/2003/01/geo/wgs84_pos#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
DEFAULT_ = DBONT


# Types

# Class references
class ThingId(extended_str):
    pass


class ClassId(ThingId):
    pass


class FoodId(ThingId):
    pass


class SpeciesId(ThingId):
    pass


class ActivityId(ThingId):
    pass


class PlaceId(ThingId):
    pass


class PopulatedPlaceId(PlaceId):
    pass


class CountryId(PopulatedPlaceId):
    pass


class LanguageId(ThingId):
    pass


class TopicalConceptId(ThingId):
    pass


class MedicalSpecialtyId(ThingId):
    pass


class AgentId(ThingId):
    pass


class PersonId(AgentId):
    pass


class OrganisationId(AgentId):
    pass


class BiomoleculeId(ThingId):
    pass


class ChemicalSubstanceId(ThingId):
    pass


class IdentifierId(ThingId):
    pass


class WorkId(ThingId):
    pass


class AwardId(ThingId):
    pass


class DiseaseId(ThingId):
    pass


class EthnicGroupId(ThingId):
    pass


class EventId(ThingId):
    pass


class AnatomicalStructureId(ThingId):
    pass


class AlgorithmId(ThingId):
    pass


class AltitudeId(ThingId):
    pass


class FlagId(ThingId):
    pass


class MediaId(ThingId):
    pass


class MedicineId(ThingId):
    pass


class PopulationId(ThingId):
    pass


class PublicServiceId(ThingId):
    pass


class StatisticId(ThingId):
    pass


@dataclass
class Thing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Thing
    class_class_curie: ClassVar[str] = "dbont:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = DBONT.Thing

    id: Union[str, ThingId] = None
    label: Optional[str] = None
    comment: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThingId):
            self.id = ThingId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class Class(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Class
    class_class_curie: ClassVar[str] = "dbont:Class"
    class_name: ClassVar[str] = "Class"
    class_model_uri: ClassVar[URIRef] = DBONT.Class

    id: Union[str, ClassId] = None
    subClassOf: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClassId):
            self.id = ClassId(self.id)

        if self.subClassOf is not None and not isinstance(self.subClassOf, str):
            self.subClassOf = str(self.subClassOf)

        super().__post_init__(**kwargs)


@dataclass
class Food(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Food
    class_class_curie: ClassVar[str] = "dbont:Food"
    class_name: ClassVar[str] = "Food"
    class_model_uri: ClassVar[URIRef] = DBONT.Food

    id: Union[str, FoodId] = None
    differentFrom: Optional[Union[str, ThingId]] = None
    thumbnail: Optional[str] = None
    wikiPageID: Optional[int] = None
    wikiPageRevisionID: Optional[int] = None
    sameAs: Optional[str] = None
    servingTemperature: Optional[str] = None
    abstract: Optional[str] = None
    servingSize: Optional[float] = None
    alias: Optional[str] = None
    cuisine: Optional[str] = None
    ingredientName: Optional[str] = None
    country: Optional[Union[str, CountryId]] = None
    manufacturer: Optional[Union[str, OrganisationId]] = None
    origin: Optional[Union[str, PopulatedPlaceId]] = None
    region: Optional[Union[str, PlaceId]] = None
    creatorOfDish: Optional[Union[str, PersonId]] = None
    wikiPageLength: Optional[int] = None
    notes: Optional[str] = None
    distributor: Optional[Union[str, OrganisationId]] = None
    approximateCalories: Optional[float] = None
    carbohydrate: Optional[float] = None
    fat: Optional[float] = None
    protein: Optional[float] = None
    introduced: Optional[Union[str, XSDDate]] = None
    species: Optional[Union[str, SpeciesId]] = None
    glycemicIndex: Optional[int] = None
    maxTime: Optional[float] = None
    minTime: Optional[float] = None
    complexity: Optional[str] = None
    discontinued: Optional[Union[str, XSDDate]] = None
    imdbId: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FoodId):
            self.id = FoodId(self.id)

        if self.differentFrom is not None and not isinstance(self.differentFrom, ThingId):
            self.differentFrom = ThingId(self.differentFrom)

        if self.thumbnail is not None and not isinstance(self.thumbnail, str):
            self.thumbnail = str(self.thumbnail)

        if self.wikiPageID is not None and not isinstance(self.wikiPageID, int):
            self.wikiPageID = int(self.wikiPageID)

        if self.wikiPageRevisionID is not None and not isinstance(self.wikiPageRevisionID, int):
            self.wikiPageRevisionID = int(self.wikiPageRevisionID)

        if self.sameAs is not None and not isinstance(self.sameAs, str):
            self.sameAs = str(self.sameAs)

        if self.servingTemperature is not None and not isinstance(self.servingTemperature, str):
            self.servingTemperature = str(self.servingTemperature)

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.servingSize is not None and not isinstance(self.servingSize, float):
            self.servingSize = float(self.servingSize)

        if self.alias is not None and not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self.cuisine is not None and not isinstance(self.cuisine, str):
            self.cuisine = str(self.cuisine)

        if self.ingredientName is not None and not isinstance(self.ingredientName, str):
            self.ingredientName = str(self.ingredientName)

        if self.country is not None and not isinstance(self.country, CountryId):
            self.country = CountryId(self.country)

        if self.manufacturer is not None and not isinstance(self.manufacturer, OrganisationId):
            self.manufacturer = OrganisationId(self.manufacturer)

        if self.origin is not None and not isinstance(self.origin, PopulatedPlaceId):
            self.origin = PopulatedPlaceId(self.origin)

        if self.region is not None and not isinstance(self.region, PlaceId):
            self.region = PlaceId(self.region)

        if self.creatorOfDish is not None and not isinstance(self.creatorOfDish, PersonId):
            self.creatorOfDish = PersonId(self.creatorOfDish)

        if self.wikiPageLength is not None and not isinstance(self.wikiPageLength, int):
            self.wikiPageLength = int(self.wikiPageLength)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.distributor is not None and not isinstance(self.distributor, OrganisationId):
            self.distributor = OrganisationId(self.distributor)

        if self.approximateCalories is not None and not isinstance(self.approximateCalories, float):
            self.approximateCalories = float(self.approximateCalories)

        if self.carbohydrate is not None and not isinstance(self.carbohydrate, float):
            self.carbohydrate = float(self.carbohydrate)

        if self.fat is not None and not isinstance(self.fat, float):
            self.fat = float(self.fat)

        if self.protein is not None and not isinstance(self.protein, float):
            self.protein = float(self.protein)

        if self.introduced is not None and not isinstance(self.introduced, XSDDate):
            self.introduced = XSDDate(self.introduced)

        if self.species is not None and not isinstance(self.species, SpeciesId):
            self.species = SpeciesId(self.species)

        if self.glycemicIndex is not None and not isinstance(self.glycemicIndex, int):
            self.glycemicIndex = int(self.glycemicIndex)

        if self.maxTime is not None and not isinstance(self.maxTime, float):
            self.maxTime = float(self.maxTime)

        if self.minTime is not None and not isinstance(self.minTime, float):
            self.minTime = float(self.minTime)

        if self.complexity is not None and not isinstance(self.complexity, str):
            self.complexity = str(self.complexity)

        if self.discontinued is not None and not isinstance(self.discontinued, XSDDate):
            self.discontinued = XSDDate(self.discontinued)

        if self.imdbId is not None and not isinstance(self.imdbId, str):
            self.imdbId = str(self.imdbId)

        super().__post_init__(**kwargs)


@dataclass
class Species(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Species
    class_class_curie: ClassVar[str] = "dbont:Species"
    class_name: ClassVar[str] = "Species"
    class_model_uri: ClassVar[URIRef] = DBONT.Species

    id: Union[str, SpeciesId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpeciesId):
            self.id = SpeciesId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Activity(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Activity
    class_class_curie: ClassVar[str] = "dbont:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = DBONT.Activity

    id: Union[str, ActivityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityId):
            self.id = ActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Place(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Place
    class_class_curie: ClassVar[str] = "dbont:Place"
    class_name: ClassVar[str] = "Place"
    class_model_uri: ClassVar[URIRef] = DBONT.Place

    id: Union[str, PlaceId] = None
    lat: Optional[str] = None
    long: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlaceId):
            self.id = PlaceId(self.id)

        if self.lat is not None and not isinstance(self.lat, str):
            self.lat = str(self.lat)

        if self.long is not None and not isinstance(self.long, str):
            self.long = str(self.long)

        super().__post_init__(**kwargs)


@dataclass
class PopulatedPlace(Place):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.PopulatedPlace
    class_class_curie: ClassVar[str] = "dbont:PopulatedPlace"
    class_name: ClassVar[str] = "PopulatedPlace"
    class_model_uri: ClassVar[URIRef] = DBONT.PopulatedPlace

    id: Union[str, PopulatedPlaceId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PopulatedPlaceId):
            self.id = PopulatedPlaceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Country(PopulatedPlace):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Country
    class_class_curie: ClassVar[str] = "dbont:Country"
    class_name: ClassVar[str] = "Country"
    class_model_uri: ClassVar[URIRef] = DBONT.Country

    id: Union[str, CountryId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CountryId):
            self.id = CountryId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Language(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Language
    class_class_curie: ClassVar[str] = "dbont:Language"
    class_name: ClassVar[str] = "Language"
    class_model_uri: ClassVar[URIRef] = DBONT.Language

    id: Union[str, LanguageId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LanguageId):
            self.id = LanguageId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class TopicalConcept(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.TopicalConcept
    class_class_curie: ClassVar[str] = "dbont:TopicalConcept"
    class_name: ClassVar[str] = "TopicalConcept"
    class_model_uri: ClassVar[URIRef] = DBONT.TopicalConcept

    id: Union[str, TopicalConceptId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TopicalConceptId):
            self.id = TopicalConceptId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MedicalSpecialty(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.MedicalSpecialty
    class_class_curie: ClassVar[str] = "dbont:MedicalSpecialty"
    class_name: ClassVar[str] = "MedicalSpecialty"
    class_model_uri: ClassVar[URIRef] = DBONT.MedicalSpecialty

    id: Union[str, MedicalSpecialtyId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MedicalSpecialtyId):
            self.id = MedicalSpecialtyId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Agent(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Agent
    class_class_curie: ClassVar[str] = "dbont:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = DBONT.Agent

    id: Union[str, AgentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AgentId):
            self.id = AgentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Person(Agent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Person
    class_class_curie: ClassVar[str] = "dbont:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = DBONT.Person

    id: Union[str, PersonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Organisation(Agent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Organisation
    class_class_curie: ClassVar[str] = "dbont:Organisation"
    class_name: ClassVar[str] = "Organisation"
    class_model_uri: ClassVar[URIRef] = DBONT.Organisation

    id: Union[str, OrganisationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganisationId):
            self.id = OrganisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Biomolecule(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Biomolecule
    class_class_curie: ClassVar[str] = "dbont:Biomolecule"
    class_name: ClassVar[str] = "Biomolecule"
    class_model_uri: ClassVar[URIRef] = DBONT.Biomolecule

    id: Union[str, BiomoleculeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiomoleculeId):
            self.id = BiomoleculeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalSubstance(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.ChemicalSubstance
    class_class_curie: ClassVar[str] = "dbont:ChemicalSubstance"
    class_name: ClassVar[str] = "ChemicalSubstance"
    class_model_uri: ClassVar[URIRef] = DBONT.ChemicalSubstance

    id: Union[str, ChemicalSubstanceId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalSubstanceId):
            self.id = ChemicalSubstanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Identifier(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Identifier
    class_class_curie: ClassVar[str] = "dbont:Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = DBONT.Identifier

    id: Union[str, IdentifierId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdentifierId):
            self.id = IdentifierId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Work(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Work
    class_class_curie: ClassVar[str] = "dbont:Work"
    class_name: ClassVar[str] = "Work"
    class_model_uri: ClassVar[URIRef] = DBONT.Work

    id: Union[str, WorkId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkId):
            self.id = WorkId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Award(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Award
    class_class_curie: ClassVar[str] = "dbont:Award"
    class_name: ClassVar[str] = "Award"
    class_model_uri: ClassVar[URIRef] = DBONT.Award

    id: Union[str, AwardId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AwardId):
            self.id = AwardId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Disease(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Disease
    class_class_curie: ClassVar[str] = "dbont:Disease"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = DBONT.Disease

    id: Union[str, DiseaseId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EthnicGroup(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.EthnicGroup
    class_class_curie: ClassVar[str] = "dbont:EthnicGroup"
    class_name: ClassVar[str] = "EthnicGroup"
    class_model_uri: ClassVar[URIRef] = DBONT.EthnicGroup

    id: Union[str, EthnicGroupId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EthnicGroupId):
            self.id = EthnicGroupId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Event(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Event
    class_class_curie: ClassVar[str] = "dbont:Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = DBONT.Event

    id: Union[str, EventId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventId):
            self.id = EventId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalStructure(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.AnatomicalStructure
    class_class_curie: ClassVar[str] = "dbont:AnatomicalStructure"
    class_name: ClassVar[str] = "AnatomicalStructure"
    class_model_uri: ClassVar[URIRef] = DBONT.AnatomicalStructure

    id: Union[str, AnatomicalStructureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalStructureId):
            self.id = AnatomicalStructureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Algorithm(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Algorithm
    class_class_curie: ClassVar[str] = "dbont:Algorithm"
    class_name: ClassVar[str] = "Algorithm"
    class_model_uri: ClassVar[URIRef] = DBONT.Algorithm

    id: Union[str, AlgorithmId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlgorithmId):
            self.id = AlgorithmId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Altitude(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Altitude
    class_class_curie: ClassVar[str] = "dbont:Altitude"
    class_name: ClassVar[str] = "Altitude"
    class_model_uri: ClassVar[URIRef] = DBONT.Altitude

    id: Union[str, AltitudeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AltitudeId):
            self.id = AltitudeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Flag(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Flag
    class_class_curie: ClassVar[str] = "dbont:Flag"
    class_name: ClassVar[str] = "Flag"
    class_model_uri: ClassVar[URIRef] = DBONT.Flag

    id: Union[str, FlagId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FlagId):
            self.id = FlagId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Media(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Media
    class_class_curie: ClassVar[str] = "dbont:Media"
    class_name: ClassVar[str] = "Media"
    class_model_uri: ClassVar[URIRef] = DBONT.Media

    id: Union[str, MediaId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MediaId):
            self.id = MediaId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Medicine(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Medicine
    class_class_curie: ClassVar[str] = "dbont:Medicine"
    class_name: ClassVar[str] = "Medicine"
    class_model_uri: ClassVar[URIRef] = DBONT.Medicine

    id: Union[str, MedicineId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MedicineId):
            self.id = MedicineId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Population(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Population
    class_class_curie: ClassVar[str] = "dbont:Population"
    class_name: ClassVar[str] = "Population"
    class_model_uri: ClassVar[URIRef] = DBONT.Population

    id: Union[str, PopulationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PopulationId):
            self.id = PopulationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PublicService(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.PublicService
    class_class_curie: ClassVar[str] = "dbont:PublicService"
    class_name: ClassVar[str] = "PublicService"
    class_model_uri: ClassVar[URIRef] = DBONT.PublicService

    id: Union[str, PublicServiceId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicServiceId):
            self.id = PublicServiceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Statistic(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBONT.Statistic
    class_class_curie: ClassVar[str] = "dbont:Statistic"
    class_name: ClassVar[str] = "Statistic"
    class_model_uri: ClassVar[URIRef] = DBONT.Statistic

    id: Union[str, StatisticId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StatisticId):
            self.id = StatisticId(self.id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=DBONT.id, name="id", curie=DBONT.curie('id'),
                   model_uri=DBONT.id, domain=None, range=URIRef)

slots.label = Slot(uri=RDFS.label, name="label", curie=RDFS.curie('label'),
                   model_uri=DBONT.label, domain=None, range=Optional[str])

slots.comment = Slot(uri=RDFS.comment, name="comment", curie=RDFS.curie('comment'),
                   model_uri=DBONT.comment, domain=None, range=Optional[str])

slots.subClassOf = Slot(uri=RDFS.subClassOf, name="subClassOf", curie=RDFS.curie('subClassOf'),
                   model_uri=DBONT.subClassOf, domain=None, range=Optional[str])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=DBONT.type, domain=None, range=Optional[str])

slots.sameAs = Slot(uri=OWL.sameAs, name="sameAs", curie=OWL.curie('sameAs'),
                   model_uri=DBONT.sameAs, domain=None, range=Optional[str])

slots.lat = Slot(uri=GEO.lat, name="lat", curie=GEO.curie('lat'),
                   model_uri=DBONT.lat, domain=None, range=Optional[str])

slots.long = Slot(uri=GEO.long, name="long", curie=GEO.curie('long'),
                   model_uri=DBONT.long, domain=None, range=Optional[str])

slots.servingSize = Slot(uri=DBONT.servingSize, name="servingSize", curie=DBONT.curie('servingSize'),
                   model_uri=DBONT.servingSize, domain=None, range=Optional[float])

slots.wikiPageRevisionID = Slot(uri=DBONT.wikiPageRevisionID, name="wikiPageRevisionID", curie=DBONT.curie('wikiPageRevisionID'),
                   model_uri=DBONT.wikiPageRevisionID, domain=None, range=Optional[int])

slots.wikiPageLength = Slot(uri=DBONT.wikiPageLength, name="wikiPageLength", curie=DBONT.curie('wikiPageLength'),
                   model_uri=DBONT.wikiPageLength, domain=None, range=Optional[int])

slots.approximateCalories = Slot(uri=DBONT.approximateCalories, name="approximateCalories", curie=DBONT.curie('approximateCalories'),
                   model_uri=DBONT.approximateCalories, domain=None, range=Optional[float])

slots.complexity = Slot(uri=DBONT.complexity, name="complexity", curie=DBONT.curie('complexity'),
                   model_uri=DBONT.complexity, domain=None, range=Optional[str])

slots.thumbnail = Slot(uri=DBONT.thumbnail, name="thumbnail", curie=DBONT.curie('thumbnail'),
                   model_uri=DBONT.thumbnail, domain=None, range=Optional[str])

slots.differentFrom = Slot(uri=OWL.differentFrom, name="differentFrom", curie=OWL.curie('differentFrom'),
                   model_uri=DBONT.differentFrom, domain=None, range=Optional[Union[str, ThingId]])

slots.creatorOfDish = Slot(uri=DBONT.creatorOfDish, name="creatorOfDish", curie=DBONT.curie('creatorOfDish'),
                   model_uri=DBONT.creatorOfDish, domain=None, range=Optional[Union[str, PersonId]])

slots.distributor = Slot(uri=DBONT.distributor, name="distributor", curie=DBONT.curie('distributor'),
                   model_uri=DBONT.distributor, domain=None, range=Optional[Union[str, OrganisationId]])

slots.introduced = Slot(uri=DBONT.introduced, name="introduced", curie=DBONT.curie('introduced'),
                   model_uri=DBONT.introduced, domain=None, range=Optional[Union[str, XSDDate]])

slots.ingredientName = Slot(uri=DBONT.ingredientName, name="ingredientName", curie=DBONT.curie('ingredientName'),
                   model_uri=DBONT.ingredientName, domain=None, range=Optional[str])

slots.wikiPageID = Slot(uri=DBONT.wikiPageID, name="wikiPageID", curie=DBONT.curie('wikiPageID'),
                   model_uri=DBONT.wikiPageID, domain=None, range=Optional[int])

slots.carbohydrate = Slot(uri=DBONT.carbohydrate, name="carbohydrate", curie=DBONT.curie('carbohydrate'),
                   model_uri=DBONT.carbohydrate, domain=None, range=Optional[float])

slots.discontinued = Slot(uri=DBONT.discontinued, name="discontinued", curie=DBONT.curie('discontinued'),
                   model_uri=DBONT.discontinued, domain=None, range=Optional[Union[str, XSDDate]])

slots.maxTime = Slot(uri=DBONT.maxTime, name="maxTime", curie=DBONT.curie('maxTime'),
                   model_uri=DBONT.maxTime, domain=None, range=Optional[float])

slots.origin = Slot(uri=DBONT.origin, name="origin", curie=DBONT.curie('origin'),
                   model_uri=DBONT.origin, domain=None, range=Optional[Union[str, PopulatedPlaceId]])

slots.manufacturer = Slot(uri=DBONT.manufacturer, name="manufacturer", curie=DBONT.curie('manufacturer'),
                   model_uri=DBONT.manufacturer, domain=None, range=Optional[Union[str, OrganisationId]])

slots.fat = Slot(uri=DBONT.fat, name="fat", curie=DBONT.curie('fat'),
                   model_uri=DBONT.fat, domain=None, range=Optional[float])

slots.imdbId = Slot(uri=DBONT.imdbId, name="imdbId", curie=DBONT.curie('imdbId'),
                   model_uri=DBONT.imdbId, domain=None, range=Optional[str])

slots.region = Slot(uri=DBONT.region, name="region", curie=DBONT.curie('region'),
                   model_uri=DBONT.region, domain=None, range=Optional[Union[str, PlaceId]])

slots.glycemicIndex = Slot(uri=DBONT.glycemicIndex, name="glycemicIndex", curie=DBONT.curie('glycemicIndex'),
                   model_uri=DBONT.glycemicIndex, domain=None, range=Optional[int])

slots.protein = Slot(uri=DBONT.protein, name="protein", curie=DBONT.curie('protein'),
                   model_uri=DBONT.protein, domain=None, range=Optional[float])

slots.cuisine = Slot(uri=DBONT.cuisine, name="cuisine", curie=DBONT.curie('cuisine'),
                   model_uri=DBONT.cuisine, domain=None, range=Optional[str])

slots.abstract = Slot(uri=DBONT.abstract, name="abstract", curie=DBONT.curie('abstract'),
                   model_uri=DBONT.abstract, domain=None, range=Optional[str])

slots.notes = Slot(uri=DBONT.notes, name="notes", curie=DBONT.curie('notes'),
                   model_uri=DBONT.notes, domain=None, range=Optional[str])

slots.servingTemperature = Slot(uri=DBONT.servingTemperature, name="servingTemperature", curie=DBONT.curie('servingTemperature'),
                   model_uri=DBONT.servingTemperature, domain=None, range=Optional[str])

slots.species = Slot(uri=DBONT.species, name="species", curie=DBONT.curie('species'),
                   model_uri=DBONT.species, domain=None, range=Optional[Union[str, SpeciesId]])

slots.country = Slot(uri=DBONT.country, name="country", curie=DBONT.curie('country'),
                   model_uri=DBONT.country, domain=None, range=Optional[Union[str, CountryId]])

slots.minTime = Slot(uri=DBONT.minTime, name="minTime", curie=DBONT.curie('minTime'),
                   model_uri=DBONT.minTime, domain=None, range=Optional[float])

slots.alias = Slot(uri=DBONT.alias, name="alias", curie=DBONT.curie('alias'),
                   model_uri=DBONT.alias, domain=None, range=Optional[str])
