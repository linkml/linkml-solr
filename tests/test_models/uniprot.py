# Auto generated from uniprot.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-07-20 00:45
# Schema: uniprot-core
#
# id: http://purl.uniprot.org/core/
# description: uniprot ontology schema
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
from linkml_runtime.linkml_model.types import Boolean, Date, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool, XSDDate

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
UNIPROT = CurieNamespace('uniprot', 'http://purl.uniprot.org/uniprot/')
UPCORE = CurieNamespace('upcore', 'http://purl.uniprot.org/core/')
UPKEYWORDS = CurieNamespace('upkeywords', 'http://purl.uniprot.org/keywords/')
UPTAXON = CurieNamespace('uptaxon', 'http://purl.uniprot.org/taxon/')
DEFAULT_ = UPCORE


# Types

# Class references



class Thing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Thing
    class_class_curie: ClassVar[str] = "upcore:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = UPCORE.Thing


class SubcellularLocation(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Subcellular_Location
    class_class_curie: ClassVar[str] = "upcore:Subcellular_Location"
    class_name: ClassVar[str] = "Subcellular_Location"
    class_model_uri: ClassVar[URIRef] = UPCORE.SubcellularLocation


class Disease(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Disease
    class_class_curie: ClassVar[str] = "upcore:Disease"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = UPCORE.Disease


class ProteinExistence(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Protein_Existence
    class_class_curie: ClassVar[str] = "upcore:Protein_Existence"
    class_name: ClassVar[str] = "Protein_Existence"
    class_model_uri: ClassVar[URIRef] = UPCORE.ProteinExistence


class Organelle(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Organelle
    class_class_curie: ClassVar[str] = "upcore:Organelle"
    class_name: ClassVar[str] = "Organelle"
    class_model_uri: ClassVar[URIRef] = UPCORE.Organelle


class FamilyMembershipStatement(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Family_Membership_Statement
    class_class_curie: ClassVar[str] = "upcore:Family_Membership_Statement"
    class_name: ClassVar[str] = "Family_Membership_Statement"
    class_model_uri: ClassVar[URIRef] = UPCORE.FamilyMembershipStatement


class Class(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Class
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "Class"
    class_model_uri: ClassVar[URIRef] = UPCORE.Class


class Statement(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF.Statement
    class_class_curie: ClassVar[str] = "rdf:Statement"
    class_name: ClassVar[str] = "Statement"
    class_model_uri: ClassVar[URIRef] = UPCORE.Statement


class Enzyme(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Enzyme
    class_class_curie: ClassVar[str] = "upcore:Enzyme"
    class_name: ClassVar[str] = "Enzyme"
    class_model_uri: ClassVar[URIRef] = UPCORE.Enzyme


class Protein(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Protein
    class_class_curie: ClassVar[str] = "upcore:Protein"
    class_name: ClassVar[str] = "Protein"
    class_model_uri: ClassVar[URIRef] = UPCORE.Protein


class Taxon(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Taxon
    class_class_curie: ClassVar[str] = "upcore:Taxon"
    class_name: ClassVar[str] = "Taxon"
    class_model_uri: ClassVar[URIRef] = UPCORE.Taxon


class Citation(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Citation
    class_class_curie: ClassVar[str] = "upcore:Citation"
    class_name: ClassVar[str] = "Citation"
    class_model_uri: ClassVar[URIRef] = UPCORE.Citation


class CatalyticActivity(YAMLRoot):
    """
    The catalytic activity of an enzyme.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Catalytic_Activity
    class_class_curie: ClassVar[str] = "upcore:Catalytic_Activity"
    class_name: ClassVar[str] = "Catalytic_Activity"
    class_model_uri: ClassVar[URIRef] = UPCORE.CatalyticActivity


class Molecule(YAMLRoot):
    """
    A biological molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Molecule
    class_class_curie: ClassVar[str] = "upcore:Molecule"
    class_name: ClassVar[str] = "Molecule"
    class_model_uri: ClassVar[URIRef] = UPCORE.Molecule


class Tissue(YAMLRoot):
    """
    A tissue such as lung or heart.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Tissue
    class_class_curie: ClassVar[str] = "upcore:Tissue"
    class_name: ClassVar[str] = "Tissue"
    class_model_uri: ClassVar[URIRef] = UPCORE.Tissue


class Sequence(YAMLRoot):
    """
    An amino acid sequence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Sequence
    class_class_curie: ClassVar[str] = "upcore:Sequence"
    class_name: ClassVar[str] = "Sequence"
    class_model_uri: ClassVar[URIRef] = UPCORE.Sequence


class Participant(YAMLRoot):
    """
    A participant in a protein-protein interaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Participant
    class_class_curie: ClassVar[str] = "upcore:Participant"
    class_name: ClassVar[str] = "Participant"
    class_model_uri: ClassVar[URIRef] = UPCORE.Participant


class NotObsolete(YAMLRoot):
    """
    A class introduced to group all records that are currently in the database.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Not_Obsolete
    class_class_curie: ClassVar[str] = "upcore:Not_Obsolete"
    class_name: ClassVar[str] = "Not_Obsolete"
    class_model_uri: ClassVar[URIRef] = UPCORE.NotObsolete


class StructuredName(YAMLRoot):
    """
    A resource that holds a set of the known names for this protein together.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Structured_Name
    class_class_curie: ClassVar[str] = "upcore:Structured_Name"
    class_name: ClassVar[str] = "Structured_Name"
    class_model_uri: ClassVar[URIRef] = UPCORE.StructuredName


class Status(YAMLRoot):
    """
    Indicator for the reliability of a piece of information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Status
    class_class_curie: ClassVar[str] = "upcore:Status"
    class_name: ClassVar[str] = "Status"
    class_model_uri: ClassVar[URIRef] = UPCORE.Status


class Method(YAMLRoot):
    """
    An experimental method.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Method
    class_class_curie: ClassVar[str] = "upcore:Method"
    class_name: ClassVar[str] = "Method"
    class_model_uri: ClassVar[URIRef] = UPCORE.Method


class Plasmid(YAMLRoot):
    """
    Description of a Plasmid
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Plasmid
    class_class_curie: ClassVar[str] = "upcore:Plasmid"
    class_name: ClassVar[str] = "Plasmid"
    class_model_uri: ClassVar[URIRef] = UPCORE.Plasmid


class Resource(YAMLRoot):
    """
    A life science resource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Resource
    class_class_curie: ClassVar[str] = "upcore:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = UPCORE.Resource


class Annotation(YAMLRoot):
    """
    Description of a resource on a specific topic.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Annotation
    class_class_curie: ClassVar[str] = "upcore:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.Annotation


class Reviewed(YAMLRoot):
    """
    The class of all reviewed records in the database (i.e. records that where looked at by a curator for integration
    into the database).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Reviewed
    class_class_curie: ClassVar[str] = "upcore:Reviewed"
    class_name: ClassVar[str] = "Reviewed"
    class_model_uri: ClassVar[URIRef] = UPCORE.Reviewed


class Interaction(YAMLRoot):
    """
    Description of a protein-protein interaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Interaction
    class_class_curie: ClassVar[str] = "upcore:Interaction"
    class_name: ClassVar[str] = "Interaction"
    class_model_uri: ClassVar[URIRef] = UPCORE.Interaction


class Transposon(YAMLRoot):
    """
    A transposon
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Transposon
    class_class_curie: ClassVar[str] = "upcore:Transposon"
    class_name: ClassVar[str] = "Transposon"
    class_model_uri: ClassVar[URIRef] = UPCORE.Transposon


class Pathway(YAMLRoot):
    """
    A hierarchical discription of a metabolic pathway.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Pathway
    class_class_curie: ClassVar[str] = "upcore:Pathway"
    class_name: ClassVar[str] = "Pathway"
    class_model_uri: ClassVar[URIRef] = UPCORE.Pathway


class Attribution(YAMLRoot):
    """
    Entity used to attach evidence or provenance to a rdf statement via reification.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Attribution
    class_class_curie: ClassVar[str] = "upcore:Attribution"
    class_name: ClassVar[str] = "Attribution"
    class_model_uri: ClassVar[URIRef] = UPCORE.Attribution


class Strain(YAMLRoot):
    """
    A strain of a species.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Strain
    class_class_curie: ClassVar[str] = "upcore:Strain"
    class_name: ClassVar[str] = "Strain"
    class_model_uri: ClassVar[URIRef] = UPCORE.Strain


class Rank(YAMLRoot):
    """
    A rank of a taxon.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Rank
    class_class_curie: ClassVar[str] = "upcore:Rank"
    class_name: ClassVar[str] = "Rank"
    class_model_uri: ClassVar[URIRef] = UPCORE.Rank


class Obsolete(YAMLRoot):
    """
    The class of all obsolete records in the database (i.e. records that where once published but are now removed).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Obsolete
    class_class_curie: ClassVar[str] = "upcore:Obsolete"
    class_name: ClassVar[str] = "Obsolete"
    class_model_uri: ClassVar[URIRef] = UPCORE.Obsolete


class EnzymeRegulationAnnotation(YAMLRoot):
    """
    The use of this class has been replaced by Activity_Regulation_Annotation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Enzyme_Regulation_Annotation
    class_class_curie: ClassVar[str] = "upcore:Enzyme_Regulation_Annotation"
    class_name: ClassVar[str] = "Enzyme_Regulation_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.EnzymeRegulationAnnotation


class Proteome(YAMLRoot):
    """
    Description of a proteome.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Proteome
    class_class_curie: ClassVar[str] = "upcore:Proteome"
    class_name: ClassVar[str] = "Proteome"
    class_model_uri: ClassVar[URIRef] = UPCORE.Proteome


class DomainAssignmentStatement(Statement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Domain_Assignment_Statement
    class_class_curie: ClassVar[str] = "upcore:Domain_Assignment_Statement"
    class_name: ClassVar[str] = "Domain_Assignment_Statement"
    class_model_uri: ClassVar[URIRef] = UPCORE.DomainAssignmentStatement


class UnpublishedCitation(Citation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Unpublished_Citation
    class_class_curie: ClassVar[str] = "upcore:Unpublished_Citation"
    class_name: ClassVar[str] = "Unpublished_Citation"
    class_model_uri: ClassVar[URIRef] = UPCORE.UnpublishedCitation


class ActivityRegulationAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Activity_Regulation_Annotation
    class_class_curie: ClassVar[str] = "upcore:Activity_Regulation_Annotation"
    class_name: ClassVar[str] = "Activity_Regulation_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.ActivityRegulationAnnotation


class Orientation(SubcellularLocation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Orientation
    class_class_curie: ClassVar[str] = "upcore:Orientation"
    class_name: ClassVar[str] = "Orientation"
    class_model_uri: ClassVar[URIRef] = UPCORE.Orientation


class ReferenceProteome(Proteome):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Reference_Proteome
    class_class_curie: ClassVar[str] = "upcore:Reference_Proteome"
    class_name: ClassVar[str] = "Reference_Proteome"
    class_model_uri: ClassVar[URIRef] = UPCORE.ReferenceProteome


class InductionAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Induction_Annotation
    class_class_curie: ClassVar[str] = "upcore:Induction_Annotation"
    class_name: ClassVar[str] = "Induction_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.InductionAnnotation


class SequenceCautionAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Sequence_Caution_Annotation
    class_class_curie: ClassVar[str] = "upcore:Sequence_Caution_Annotation"
    class_name: ClassVar[str] = "Sequence_Caution_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.SequenceCautionAnnotation


class ErroneousTerminationAnnotation(SequenceCautionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Erroneous_Termination_Annotation
    class_class_curie: ClassVar[str] = "upcore:Erroneous_Termination_Annotation"
    class_name: ClassVar[str] = "Erroneous_Termination_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.ErroneousTerminationAnnotation


class SequenceAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Sequence_Annotation
    class_class_curie: ClassVar[str] = "upcore:Sequence_Annotation"
    class_name: ClassVar[str] = "Sequence_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.SequenceAnnotation


class NaturalVariationAnnotation(SequenceAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Natural_Variation_Annotation
    class_class_curie: ClassVar[str] = "upcore:Natural_Variation_Annotation"
    class_name: ClassVar[str] = "Natural_Variation_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.NaturalVariationAnnotation


class CautionAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Caution_Annotation
    class_class_curie: ClassVar[str] = "upcore:Caution_Annotation"
    class_name: ClassVar[str] = "Caution_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.CautionAnnotation


class ExperimentalInformationAnnotation(SequenceAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Experimental_Information_Annotation
    class_class_curie: ClassVar[str] = "upcore:Experimental_Information_Annotation"
    class_name: ClassVar[str] = "Experimental_Information_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.ExperimentalInformationAnnotation


class NotObsoleteTaxon(Taxon):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Not_Obsolete_Taxon
    class_class_curie: ClassVar[str] = "upcore:Not_Obsolete_Taxon"
    class_name: ClassVar[str] = "Not_Obsolete_Taxon"
    class_model_uri: ClassVar[URIRef] = UPCORE.NotObsoleteTaxon


class SequenceConflictAnnotation(ExperimentalInformationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Sequence_Conflict_Annotation
    class_class_curie: ClassVar[str] = "upcore:Sequence_Conflict_Annotation"
    class_name: ClassVar[str] = "Sequence_Conflict_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.SequenceConflictAnnotation


class ObservationCitation(UnpublishedCitation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Observation_Citation
    class_class_curie: ClassVar[str] = "upcore:Observation_Citation"
    class_name: ClassVar[str] = "Observation_Citation"
    class_model_uri: ClassVar[URIRef] = UPCORE.ObservationCitation


class DNA(Molecule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.DNA
    class_class_curie: ClassVar[str] = "upcore:DNA"
    class_name: ClassVar[str] = "DNA"
    class_model_uri: ClassVar[URIRef] = UPCORE.DNA


class GenomicDNA(DNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Genomic_DNA
    class_class_curie: ClassVar[str] = "upcore:Genomic_DNA"
    class_name: ClassVar[str] = "Genomic_DNA"
    class_model_uri: ClassVar[URIRef] = UPCORE.GenomicDNA


class CitationStatement(Statement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Citation_Statement
    class_class_curie: ClassVar[str] = "upcore:Citation_Statement"
    class_name: ClassVar[str] = "Citation_Statement"
    class_model_uri: ClassVar[URIRef] = UPCORE.CitationStatement


class RNAEditingAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.RNA_Editing_Annotation
    class_class_curie: ClassVar[str] = "upcore:RNA_Editing_Annotation"
    class_name: ClassVar[str] = "RNA_Editing_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.RNAEditingAnnotation


class Part(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Part
    class_class_curie: ClassVar[str] = "upcore:Part"
    class_name: ClassVar[str] = "Part"
    class_model_uri: ClassVar[URIRef] = UPCORE.Part


class UnassignedDNA(DNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Unassigned_DNA
    class_class_curie: ClassVar[str] = "upcore:Unassigned_DNA"
    class_name: ClassVar[str] = "Unassigned_DNA"
    class_model_uri: ClassVar[URIRef] = UPCORE.UnassignedDNA


class ReviewedProtein(Reviewed):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Reviewed_Protein
    class_class_curie: ClassVar[str] = "upcore:Reviewed_Protein"
    class_name: ClassVar[str] = "Reviewed_Protein"
    class_model_uri: ClassVar[URIRef] = UPCORE.ReviewedProtein


class MassMeasurementMethod(Method):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Mass_Measurement_Method
    class_class_curie: ClassVar[str] = "upcore:Mass_Measurement_Method"
    class_name: ClassVar[str] = "Mass_Measurement_Method"
    class_model_uri: ClassVar[URIRef] = UPCORE.MassMeasurementMethod


class NucleotideResource(Resource):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Nucleotide_Resource
    class_class_curie: ClassVar[str] = "upcore:Nucleotide_Resource"
    class_name: ClassVar[str] = "Nucleotide_Resource"
    class_model_uri: ClassVar[URIRef] = UPCORE.NucleotideResource


class PTMAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.PTM_Annotation
    class_class_curie: ClassVar[str] = "upcore:PTM_Annotation"
    class_name: ClassVar[str] = "PTM_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.PTMAnnotation


class CofactorAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Cofactor_Annotation
    class_class_curie: ClassVar[str] = "upcore:Cofactor_Annotation"
    class_name: ClassVar[str] = "Cofactor_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.CofactorAnnotation


class FrameshiftAnnotation(SequenceCautionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Frameshift_Annotation
    class_class_curie: ClassVar[str] = "upcore:Frameshift_Annotation"
    class_name: ClassVar[str] = "Frameshift_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.FrameshiftAnnotation


class PathwayAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Pathway_Annotation
    class_class_curie: ClassVar[str] = "upcore:Pathway_Annotation"
    class_name: ClassVar[str] = "Pathway_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.PathwayAnnotation


class PolymorphismAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Polymorphism_Annotation
    class_class_curie: ClassVar[str] = "upcore:Polymorphism_Annotation"
    class_name: ClassVar[str] = "Polymorphism_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.PolymorphismAnnotation


class NonTerminalResidueAnnotation(ExperimentalInformationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE["Non-terminal_Residue_Annotation"]
    class_class_curie: ClassVar[str] = "upcore:Non-terminal_Residue_Annotation"
    class_name: ClassVar[str] = "Non_terminal_Residue_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.NonTerminalResidueAnnotation


class ErroneousGeneModelPredictionAnnotation(SequenceCautionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Erroneous_Gene_Model_Prediction_Annotation
    class_class_curie: ClassVar[str] = "upcore:Erroneous_Gene_Model_Prediction_Annotation"
    class_name: ClassVar[str] = "Erroneous_Gene_Model_Prediction_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.ErroneousGeneModelPredictionAnnotation


class MoleculeProcessingAnnotation(SequenceAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Molecule_Processing_Annotation
    class_class_curie: ClassVar[str] = "upcore:Molecule_Processing_Annotation"
    class_name: ClassVar[str] = "Molecule_Processing_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.MoleculeProcessingAnnotation


class TransitPeptideAnnotation(MoleculeProcessingAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Transit_Peptide_Annotation
    class_class_curie: ClassVar[str] = "upcore:Transit_Peptide_Annotation"
    class_name: ClassVar[str] = "Transit_Peptide_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.TransitPeptideAnnotation


class SignalPeptideAnnotation(MoleculeProcessingAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Signal_Peptide_Annotation
    class_class_curie: ClassVar[str] = "upcore:Signal_Peptide_Annotation"
    class_name: ClassVar[str] = "Signal_Peptide_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.SignalPeptideAnnotation


class SubunitAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Subunit_Annotation
    class_class_curie: ClassVar[str] = "upcore:Subunit_Annotation"
    class_name: ClassVar[str] = "Subunit_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.SubunitAnnotation


class PeptideAnnotation(MoleculeProcessingAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Peptide_Annotation
    class_class_curie: ClassVar[str] = "upcore:Peptide_Annotation"
    class_name: ClassVar[str] = "Peptide_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.PeptideAnnotation


class ErroneousInitiationAnnotation(SequenceCautionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Erroneous_Initiation_Annotation
    class_class_curie: ClassVar[str] = "upcore:Erroneous_Initiation_Annotation"
    class_name: ClassVar[str] = "Erroneous_Initiation_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.ErroneousInitiationAnnotation


class BiotechnologyAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Biotechnology_Annotation
    class_class_curie: ClassVar[str] = "upcore:Biotechnology_Annotation"
    class_name: ClassVar[str] = "Biotechnology_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.BiotechnologyAnnotation


class RegionAnnotation(SequenceAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Region_Annotation
    class_class_curie: ClassVar[str] = "upcore:Region_Annotation"
    class_name: ClassVar[str] = "Region_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.RegionAnnotation


class IntramembraneAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Intramembrane_Annotation
    class_class_curie: ClassVar[str] = "upcore:Intramembrane_Annotation"
    class_name: ClassVar[str] = "Intramembrane_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.IntramembraneAnnotation


class CompositionalBiasAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Compositional_Bias_Annotation
    class_class_curie: ClassVar[str] = "upcore:Compositional_Bias_Annotation"
    class_name: ClassVar[str] = "Compositional_Bias_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.CompositionalBiasAnnotation


class TransmembraneAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Transmembrane_Annotation
    class_class_curie: ClassVar[str] = "upcore:Transmembrane_Annotation"
    class_name: ClassVar[str] = "Transmembrane_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.TransmembraneAnnotation


class CalciumBindingAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Calcium_Binding_Annotation
    class_class_curie: ClassVar[str] = "upcore:Calcium_Binding_Annotation"
    class_name: ClassVar[str] = "Calcium_Binding_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.CalciumBindingAnnotation


class ZincFingerAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Zinc_Finger_Annotation
    class_class_curie: ClassVar[str] = "upcore:Zinc_Finger_Annotation"
    class_name: ClassVar[str] = "Zinc_Finger_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.ZincFingerAnnotation


class CoiledCoilAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Coiled_Coil_Annotation
    class_class_curie: ClassVar[str] = "upcore:Coiled_Coil_Annotation"
    class_name: ClassVar[str] = "Coiled_Coil_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.CoiledCoilAnnotation


class RepeatAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Repeat_Annotation
    class_class_curie: ClassVar[str] = "upcore:Repeat_Annotation"
    class_name: ClassVar[str] = "Repeat_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.RepeatAnnotation


class NotObsoleteProtein(Protein):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Not_Obsolete_Protein
    class_class_curie: ClassVar[str] = "upcore:Not_Obsolete_Protein"
    class_name: ClassVar[str] = "Not_Obsolete_Protein"
    class_model_uri: ClassVar[URIRef] = UPCORE.NotObsoleteProtein


class CatalyticActivityAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Catalytic_Activity_Annotation
    class_class_curie: ClassVar[str] = "upcore:Catalytic_Activity_Annotation"
    class_name: ClassVar[str] = "Catalytic_Activity_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.CatalyticActivityAnnotation


class NonSelfInteraction(Interaction):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Non_Self_Interaction
    class_class_curie: ClassVar[str] = "upcore:Non_Self_Interaction"
    class_name: ClassVar[str] = "Non_Self_Interaction"
    class_model_uri: ClassVar[URIRef] = UPCORE.NonSelfInteraction


class KnownSequence(Sequence):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Known_Sequence
    class_class_curie: ClassVar[str] = "upcore:Known_Sequence"
    class_name: ClassVar[str] = "Known_Sequence"
    class_model_uri: ClassVar[URIRef] = UPCORE.KnownSequence


class ExternalSequence(KnownSequence):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.External_Sequence
    class_class_curie: ClassVar[str] = "upcore:External_Sequence"
    class_name: ClassVar[str] = "External_Sequence"
    class_model_uri: ClassVar[URIRef] = UPCORE.ExternalSequence


class ErroneousTranslationAnnotation(SequenceCautionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Erroneous_Translation_Annotation
    class_class_curie: ClassVar[str] = "upcore:Erroneous_Translation_Annotation"
    class_name: ClassVar[str] = "Erroneous_Translation_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.ErroneousTranslationAnnotation


class StructureMappingStatement(Statement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Structure_Mapping_Statement
    class_class_curie: ClassVar[str] = "upcore:Structure_Mapping_Statement"
    class_name: ClassVar[str] = "Structure_Mapping_Statement"
    class_model_uri: ClassVar[URIRef] = UPCORE.StructureMappingStatement


class DevelopmentalStageAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Developmental_Stage_Annotation
    class_class_curie: ClassVar[str] = "upcore:Developmental_Stage_Annotation"
    class_name: ClassVar[str] = "Developmental_Stage_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.DevelopmentalStageAnnotation


class SiteAnnotation(SequenceAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Site_Annotation
    class_class_curie: ClassVar[str] = "upcore:Site_Annotation"
    class_name: ClassVar[str] = "Site_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.SiteAnnotation


class MetalBindingAnnotation(SiteAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Metal_Binding_Annotation
    class_class_curie: ClassVar[str] = "upcore:Metal_Binding_Annotation"
    class_name: ClassVar[str] = "Metal_Binding_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.MetalBindingAnnotation


class BindingSiteAnnotation(SiteAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Binding_Site_Annotation
    class_class_curie: ClassVar[str] = "upcore:Binding_Site_Annotation"
    class_name: ClassVar[str] = "Binding_Site_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.BindingSiteAnnotation


class ToxicDoseAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Toxic_Dose_Annotation
    class_class_curie: ClassVar[str] = "upcore:Toxic_Dose_Annotation"
    class_name: ClassVar[str] = "Toxic_Dose_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.ToxicDoseAnnotation


class NucleotideBindingAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Nucleotide_Binding_Annotation
    class_class_curie: ClassVar[str] = "upcore:Nucleotide_Binding_Annotation"
    class_name: ClassVar[str] = "Nucleotide_Binding_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.NucleotideBindingAnnotation


class ObsoleteTaxon(Taxon):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Obsolete_Taxon
    class_class_curie: ClassVar[str] = "upcore:Obsolete_Taxon"
    class_name: ClassVar[str] = "Obsolete_Taxon"
    class_model_uri: ClassVar[URIRef] = UPCORE.ObsoleteTaxon


class SecondaryStructureAnnotation(SequenceAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Secondary_Structure_Annotation
    class_class_curie: ClassVar[str] = "upcore:Secondary_Structure_Annotation"
    class_name: ClassVar[str] = "Secondary_Structure_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.SecondaryStructureAnnotation


class BetaStrandAnnotation(SecondaryStructureAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Beta_Strand_Annotation
    class_class_curie: ClassVar[str] = "upcore:Beta_Strand_Annotation"
    class_name: ClassVar[str] = "Beta_Strand_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.BetaStrandAnnotation


class MutagenesisAnnotation(ExperimentalInformationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Mutagenesis_Annotation
    class_class_curie: ClassVar[str] = "upcore:Mutagenesis_Annotation"
    class_name: ClassVar[str] = "Mutagenesis_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.MutagenesisAnnotation


class PharmaceuticalAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Pharmaceutical_Annotation
    class_class_curie: ClassVar[str] = "upcore:Pharmaceutical_Annotation"
    class_name: ClassVar[str] = "Pharmaceutical_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.PharmaceuticalAnnotation


class RepresentativeProteome(Proteome):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Representative_Proteome
    class_class_curie: ClassVar[str] = "upcore:Representative_Proteome"
    class_name: ClassVar[str] = "Representative_Proteome"
    class_model_uri: ClassVar[URIRef] = UPCORE.RepresentativeProteome


class NonAdjacentResiduesAnnotation(ExperimentalInformationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE["Non-adjacent_Residues_Annotation"]
    class_class_curie: ClassVar[str] = "upcore:Non-adjacent_Residues_Annotation"
    class_name: ClassVar[str] = "Non_adjacent_Residues_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.NonAdjacentResiduesAnnotation


class Concept(Class):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Concept
    class_class_curie: ClassVar[str] = "upcore:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = UPCORE.Concept


class Topology(SubcellularLocation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Topology
    class_class_curie: ClassVar[str] = "upcore:Topology"
    class_name: ClassVar[str] = "Topology"
    class_model_uri: ClassVar[URIRef] = UPCORE.Topology


class ObsoleteProtein(Protein):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Obsolete_Protein
    class_class_curie: ClassVar[str] = "upcore:Obsolete_Protein"
    class_name: ClassVar[str] = "Obsolete_Protein"
    class_model_uri: ClassVar[URIRef] = UPCORE.ObsoleteProtein


class MemberOfRedudantProteome(ObsoleteProtein):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Member_Of_Redudant_Proteome
    class_class_curie: ClassVar[str] = "upcore:Member_Of_Redudant_Proteome"
    class_name: ClassVar[str] = "Member_Of_Redudant_Proteome"
    class_model_uri: ClassVar[URIRef] = UPCORE.MemberOfRedudantProteome


class SimpleSequence(KnownSequence):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Simple_Sequence
    class_class_curie: ClassVar[str] = "upcore:Simple_Sequence"
    class_name: ClassVar[str] = "Simple_Sequence"
    class_model_uri: ClassVar[URIRef] = UPCORE.SimpleSequence


class Journal(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Journal
    class_class_curie: ClassVar[str] = "upcore:Journal"
    class_name: ClassVar[str] = "Journal"
    class_model_uri: ClassVar[URIRef] = UPCORE.Journal


class PublishedCitation(Citation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Published_Citation
    class_class_curie: ClassVar[str] = "upcore:Published_Citation"
    class_name: ClassVar[str] = "Published_Citation"
    class_model_uri: ClassVar[URIRef] = UPCORE.PublishedCitation


class SubmissionCitation(PublishedCitation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Submission_Citation
    class_class_curie: ClassVar[str] = "upcore:Submission_Citation"
    class_name: ClassVar[str] = "Submission_Citation"
    class_model_uri: ClassVar[URIRef] = UPCORE.SubmissionCitation


class JournalCitation(PublishedCitation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Journal_Citation
    class_class_curie: ClassVar[str] = "upcore:Journal_Citation"
    class_name: ClassVar[str] = "Journal_Citation"
    class_model_uri: ClassVar[URIRef] = UPCORE.JournalCitation


class PatentCitation(PublishedCitation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Patent_Citation
    class_class_curie: ClassVar[str] = "upcore:Patent_Citation"
    class_name: ClassVar[str] = "Patent_Citation"
    class_model_uri: ClassVar[URIRef] = UPCORE.PatentCitation


class MassSpectrometryAnnotation(ExperimentalInformationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Mass_Spectrometry_Annotation
    class_class_curie: ClassVar[str] = "upcore:Mass_Spectrometry_Annotation"
    class_name: ClassVar[str] = "Mass_Spectrometry_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.MassSpectrometryAnnotation


class BookCitation(PublishedCitation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Book_Citation
    class_class_curie: ClassVar[str] = "upcore:Book_Citation"
    class_name: ClassVar[str] = "Book_Citation"
    class_model_uri: ClassVar[URIRef] = UPCORE.BookCitation


class CellularComponent(SubcellularLocation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Cellular_Component
    class_class_curie: ClassVar[str] = "upcore:Cellular_Component"
    class_name: ClassVar[str] = "Cellular_Component"
    class_model_uri: ClassVar[URIRef] = UPCORE.CellularComponent


class NaturalVariantAnnotation(NaturalVariationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Natural_Variant_Annotation
    class_class_curie: ClassVar[str] = "upcore:Natural_Variant_Annotation"
    class_name: ClassVar[str] = "Natural_Variant_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.NaturalVariantAnnotation


class StructureResource(Resource):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Structure_Resource
    class_class_curie: ClassVar[str] = "upcore:Structure_Resource"
    class_name: ClassVar[str] = "Structure_Resource"
    class_model_uri: ClassVar[URIRef] = UPCORE.StructureResource


class UnknownSequence(Sequence):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Unknown_Sequence
    class_class_curie: ClassVar[str] = "upcore:Unknown_Sequence"
    class_name: ClassVar[str] = "Unknown_Sequence"
    class_model_uri: ClassVar[URIRef] = UPCORE.UnknownSequence


class AlternativeSequenceAnnotation(NaturalVariationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Alternative_Sequence_Annotation
    class_class_curie: ClassVar[str] = "upcore:Alternative_Sequence_Annotation"
    class_name: ClassVar[str] = "Alternative_Sequence_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.AlternativeSequenceAnnotation


class ActiveSiteAnnotation(SiteAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Active_Site_Annotation
    class_class_curie: ClassVar[str] = "upcore:Active_Site_Annotation"
    class_name: ClassVar[str] = "Active_Site_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.ActiveSiteAnnotation


class NucleotideMappingStatement(Statement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Nucleotide_Mapping_Statement
    class_class_curie: ClassVar[str] = "upcore:Nucleotide_Mapping_Statement"
    class_name: ClassVar[str] = "Nucleotide_Mapping_Statement"
    class_model_uri: ClassVar[URIRef] = UPCORE.NucleotideMappingStatement


class ModificationAnnotation(SequenceAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Modification_Annotation
    class_class_curie: ClassVar[str] = "upcore:Modification_Annotation"
    class_name: ClassVar[str] = "Modification_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.ModificationAnnotation


class LipidationAnnotation(ModificationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Lipidation_Annotation
    class_class_curie: ClassVar[str] = "upcore:Lipidation_Annotation"
    class_name: ClassVar[str] = "Lipidation_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.LipidationAnnotation


class ModifiedResidueAnnotation(ModificationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Modified_Residue_Annotation
    class_class_curie: ClassVar[str] = "upcore:Modified_Residue_Annotation"
    class_name: ClassVar[str] = "Modified_Residue_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.ModifiedResidueAnnotation


class GlycosylationAnnotation(ModificationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Glycosylation_Annotation
    class_class_curie: ClassVar[str] = "upcore:Glycosylation_Annotation"
    class_name: ClassVar[str] = "Glycosylation_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.GlycosylationAnnotation


class InitiatorMethionineAnnotation(MoleculeProcessingAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Initiator_Methionine_Annotation
    class_class_curie: ClassVar[str] = "upcore:Initiator_Methionine_Annotation"
    class_name: ClassVar[str] = "Initiator_Methionine_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.InitiatorMethionineAnnotation


class MotifAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Motif_Annotation
    class_class_curie: ClassVar[str] = "upcore:Motif_Annotation"
    class_name: ClassVar[str] = "Motif_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.MotifAnnotation


class SimilarityAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Similarity_Annotation
    class_class_curie: ClassVar[str] = "upcore:Similarity_Annotation"
    class_name: ClassVar[str] = "Similarity_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.SimilarityAnnotation


class Database(Class):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Database
    class_class_curie: ClassVar[str] = "upcore:Database"
    class_name: ClassVar[str] = "Database"
    class_model_uri: ClassVar[URIRef] = UPCORE.Database


class NPBindingAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.NP_Binding_Annotation
    class_class_curie: ClassVar[str] = "upcore:NP_Binding_Annotation"
    class_name: ClassVar[str] = "NP_Binding_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.NPBindingAnnotation


class TopologicalDomainAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Topological_Domain_Annotation
    class_class_curie: ClassVar[str] = "upcore:Topological_Domain_Annotation"
    class_name: ClassVar[str] = "Topological_Domain_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.TopologicalDomainAnnotation


class TissueSpecificityAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Tissue_Specificity_Annotation
    class_class_curie: ClassVar[str] = "upcore:Tissue_Specificity_Annotation"
    class_name: ClassVar[str] = "Tissue_Specificity_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.TissueSpecificityAnnotation


class TranscriptResource(Resource):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Transcript_Resource
    class_class_curie: ClassVar[str] = "upcore:Transcript_Resource"
    class_name: ClassVar[str] = "Transcript_Resource"
    class_model_uri: ClassVar[URIRef] = UPCORE.TranscriptResource


class FunctionAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Function_Annotation
    class_class_curie: ClassVar[str] = "upcore:Function_Annotation"
    class_name: ClassVar[str] = "Function_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.FunctionAnnotation


class EndpointStatement(Statement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Endpoint_Statement
    class_class_curie: ClassVar[str] = "upcore:Endpoint_Statement"
    class_name: ClassVar[str] = "Endpoint_Statement"
    class_model_uri: ClassVar[URIRef] = UPCORE.EndpointStatement


class ProteomeComponent(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Proteome_Component
    class_class_curie: ClassVar[str] = "upcore:Proteome_Component"
    class_name: ClassVar[str] = "Proteome_Component"
    class_model_uri: ClassVar[URIRef] = UPCORE.ProteomeComponent


class CrossLinkAnnotation(ModificationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE["Cross-link_Annotation"]
    class_class_curie: ClassVar[str] = "upcore:Cross-link_Annotation"
    class_name: ClassVar[str] = "Cross_link_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.CrossLinkAnnotation


class StructureDeterminationMethod(Method):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Structure_Determination_Method
    class_class_curie: ClassVar[str] = "upcore:Structure_Determination_Method"
    class_name: ClassVar[str] = "Structure_Determination_Method"
    class_model_uri: ClassVar[URIRef] = UPCORE.StructureDeterminationMethod


class DisulfideBondAnnotation(ModificationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Disulfide_Bond_Annotation
    class_class_curie: ClassVar[str] = "upcore:Disulfide_Bond_Annotation"
    class_name: ClassVar[str] = "Disulfide_Bond_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.DisulfideBondAnnotation


class BiophysicochemicalAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Biophysicochemical_Annotation
    class_class_curie: ClassVar[str] = "upcore:Biophysicochemical_Annotation"
    class_name: ClassVar[str] = "Biophysicochemical_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.BiophysicochemicalAnnotation


class TemperatureDependenceAnnotation(BiophysicochemicalAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Temperature_Dependence_Annotation
    class_class_curie: ClassVar[str] = "upcore:Temperature_Dependence_Annotation"
    class_name: ClassVar[str] = "Temperature_Dependence_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.TemperatureDependenceAnnotation


class RedoxPotentialAnnotation(BiophysicochemicalAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Redox_Potential_Annotation
    class_class_curie: ClassVar[str] = "upcore:Redox_Potential_Annotation"
    class_name: ClassVar[str] = "Redox_Potential_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.RedoxPotentialAnnotation


class PHDependenceAnnotation(BiophysicochemicalAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.PH_Dependence_Annotation
    class_class_curie: ClassVar[str] = "upcore:PH_Dependence_Annotation"
    class_name: ClassVar[str] = "PH_Dependence_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.PHDependenceAnnotation


class KineticsAnnotation(BiophysicochemicalAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Kinetics_Annotation
    class_class_curie: ClassVar[str] = "upcore:Kinetics_Annotation"
    class_name: ClassVar[str] = "Kinetics_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.KineticsAnnotation


class DomainExtentAnnotation(RegionAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Domain_Extent_Annotation
    class_class_curie: ClassVar[str] = "upcore:Domain_Extent_Annotation"
    class_name: ClassVar[str] = "Domain_Extent_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.DomainExtentAnnotation


class SequenceUncertaintyAnnotation(ExperimentalInformationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Sequence_Uncertainty_Annotation
    class_class_curie: ClassVar[str] = "upcore:Sequence_Uncertainty_Annotation"
    class_name: ClassVar[str] = "Sequence_Uncertainty_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.SequenceUncertaintyAnnotation


class DiseaseAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Disease_Annotation
    class_class_curie: ClassVar[str] = "upcore:Disease_Annotation"
    class_name: ClassVar[str] = "Disease_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.DiseaseAnnotation


class ElectronicCitation(PublishedCitation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Electronic_Citation
    class_class_curie: ClassVar[str] = "upcore:Electronic_Citation"
    class_name: ClassVar[str] = "Electronic_Citation"
    class_model_uri: ClassVar[URIRef] = UPCORE.ElectronicCitation


class TurnAnnotation(SecondaryStructureAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Turn_Annotation
    class_class_curie: ClassVar[str] = "upcore:Turn_Annotation"
    class_name: ClassVar[str] = "Turn_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.TurnAnnotation


class SelfInteraction(Interaction):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Self_Interaction
    class_class_curie: ClassVar[str] = "upcore:Self_Interaction"
    class_name: ClassVar[str] = "Self_Interaction"
    class_model_uri: ClassVar[URIRef] = UPCORE.SelfInteraction


class DomainAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Domain_Annotation
    class_class_curie: ClassVar[str] = "upcore:Domain_Annotation"
    class_name: ClassVar[str] = "Domain_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.DomainAnnotation


class ChainAnnotation(MoleculeProcessingAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Chain_Annotation
    class_class_curie: ClassVar[str] = "upcore:Chain_Annotation"
    class_name: ClassVar[str] = "Chain_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.ChainAnnotation


class SubcellularLocationAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Subcellular_Location_Annotation
    class_class_curie: ClassVar[str] = "upcore:Subcellular_Location_Annotation"
    class_name: ClassVar[str] = "Subcellular_Location_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.SubcellularLocationAnnotation


class DisruptionPhenotypeAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Disruption_Phenotype_Annotation
    class_class_curie: ClassVar[str] = "upcore:Disruption_Phenotype_Annotation"
    class_name: ClassVar[str] = "Disruption_Phenotype_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.DisruptionPhenotypeAnnotation


class ThesisCitation(PublishedCitation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Thesis_Citation
    class_class_curie: ClassVar[str] = "upcore:Thesis_Citation"
    class_name: ClassVar[str] = "Thesis_Citation"
    class_model_uri: ClassVar[URIRef] = UPCORE.ThesisCitation


class Cluster(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Cluster
    class_class_curie: ClassVar[str] = "upcore:Cluster"
    class_name: ClassVar[str] = "Cluster"
    class_model_uri: ClassVar[URIRef] = UPCORE.Cluster


class RNA(Molecule):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.RNA
    class_class_curie: ClassVar[str] = "upcore:RNA"
    class_name: ClassVar[str] = "RNA"
    class_model_uri: ClassVar[URIRef] = UPCORE.RNA


class OtherRNA(RNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Other_RNA
    class_class_curie: ClassVar[str] = "upcore:Other_RNA"
    class_name: ClassVar[str] = "Other_RNA"
    class_model_uri: ClassVar[URIRef] = UPCORE.OtherRNA


class UnassignedRNA(RNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Unassigned_RNA
    class_class_curie: ClassVar[str] = "upcore:Unassigned_RNA"
    class_name: ClassVar[str] = "Unassigned_RNA"
    class_model_uri: ClassVar[URIRef] = UPCORE.UnassignedRNA


class ViralCRNA(RNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Viral_cRNA
    class_class_curie: ClassVar[str] = "upcore:Viral_cRNA"
    class_name: ClassVar[str] = "Viral_cRNA"
    class_model_uri: ClassVar[URIRef] = UPCORE.ViralCRNA


class GenomicRNA(RNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Genomic_RNA
    class_class_curie: ClassVar[str] = "upcore:Genomic_RNA"
    class_name: ClassVar[str] = "Genomic_RNA"
    class_model_uri: ClassVar[URIRef] = UPCORE.GenomicRNA


class TranscribedRNA(RNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Transcribed_RNA
    class_class_curie: ClassVar[str] = "upcore:Transcribed_RNA"
    class_name: ClassVar[str] = "Transcribed_RNA"
    class_model_uri: ClassVar[URIRef] = UPCORE.TranscribedRNA


class MRNA(RNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.MRNA
    class_class_curie: ClassVar[str] = "upcore:MRNA"
    class_name: ClassVar[str] = "MRNA"
    class_model_uri: ClassVar[URIRef] = UPCORE.MRNA


class AbsorptionAnnotation(BiophysicochemicalAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Absorption_Annotation
    class_class_curie: ClassVar[str] = "upcore:Absorption_Annotation"
    class_name: ClassVar[str] = "Absorption_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.AbsorptionAnnotation


class OtherDNA(DNA):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Other_DNA
    class_class_curie: ClassVar[str] = "upcore:Other_DNA"
    class_name: ClassVar[str] = "Other_DNA"
    class_model_uri: ClassVar[URIRef] = UPCORE.OtherDNA


class ModifiedSequence(KnownSequence):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Modified_Sequence
    class_class_curie: ClassVar[str] = "upcore:Modified_Sequence"
    class_name: ClassVar[str] = "Modified_Sequence"
    class_model_uri: ClassVar[URIRef] = UPCORE.ModifiedSequence


class AllergenAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Allergen_Annotation
    class_class_curie: ClassVar[str] = "upcore:Allergen_Annotation"
    class_name: ClassVar[str] = "Allergen_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.AllergenAnnotation


class NonStandardResidueAnnotation(ModificationAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE["Non-standard_Residue_Annotation"]
    class_class_curie: ClassVar[str] = "upcore:Non-standard_Residue_Annotation"
    class_name: ClassVar[str] = "Non_standard_Residue_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.NonStandardResidueAnnotation


class PropeptideAnnotation(MoleculeProcessingAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Propeptide_Annotation
    class_class_curie: ClassVar[str] = "upcore:Propeptide_Annotation"
    class_name: ClassVar[str] = "Propeptide_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.PropeptideAnnotation


class Gene(Concept):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Gene
    class_class_curie: ClassVar[str] = "upcore:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = UPCORE.Gene


class HelixAnnotation(SecondaryStructureAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Helix_Annotation
    class_class_curie: ClassVar[str] = "upcore:Helix_Annotation"
    class_name: ClassVar[str] = "Helix_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.HelixAnnotation


class AlternativeProductsAnnotation(Annotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Alternative_Products_Annotation
    class_class_curie: ClassVar[str] = "upcore:Alternative_Products_Annotation"
    class_name: ClassVar[str] = "Alternative_Products_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.AlternativeProductsAnnotation


class AlternativePromoterUsageAnnotation(AlternativeProductsAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Alternative_Promoter_Usage_Annotation
    class_class_curie: ClassVar[str] = "upcore:Alternative_Promoter_Usage_Annotation"
    class_name: ClassVar[str] = "Alternative_Promoter_Usage_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.AlternativePromoterUsageAnnotation


class RibosomalFrameshifting(AlternativeProductsAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Ribosomal_Frameshifting
    class_class_curie: ClassVar[str] = "upcore:Ribosomal_Frameshifting"
    class_name: ClassVar[str] = "Ribosomal_Frameshifting"
    class_model_uri: ClassVar[URIRef] = UPCORE.RibosomalFrameshifting


class AlternativeSplicingAnnotation(AlternativeProductsAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Alternative_Splicing_Annotation
    class_class_curie: ClassVar[str] = "upcore:Alternative_Splicing_Annotation"
    class_name: ClassVar[str] = "Alternative_Splicing_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.AlternativeSplicingAnnotation


class AlternativeInitiationAnnotation(AlternativeProductsAnnotation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UPCORE.Alternative_Initiation_Annotation
    class_class_curie: ClassVar[str] = "upcore:Alternative_Initiation_Annotation"
    class_name: ClassVar[str] = "Alternative_Initiation_Annotation"
    class_model_uri: ClassVar[URIRef] = UPCORE.AlternativeInitiationAnnotation


# Enumerations


# Slots
class slots:
    pass

slots.objectProperty = Slot(uri=UPCORE.objectProperty, name="objectProperty", curie=UPCORE.curie('objectProperty'),
                   model_uri=UPCORE.objectProperty, domain=None, range=Optional[str])

slots.catalyticActivity = Slot(uri=UPCORE.catalyticActivity, name="catalyticActivity", curie=UPCORE.curie('catalyticActivity'),
                   model_uri=UPCORE.catalyticActivity, domain=None, range=Optional[Union[dict, CatalyticActivity]])

slots.mappedAnnotation = Slot(uri=UPCORE.mappedAnnotation, name="mappedAnnotation", curie=UPCORE.curie('mappedAnnotation'),
                   model_uri=UPCORE.mappedAnnotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.structuredName = Slot(uri=UPCORE.structuredName, name="structuredName", curie=UPCORE.curie('structuredName'),
                   model_uri=UPCORE.structuredName, domain=None, range=Optional[Union[dict, StructuredName]])

slots.mappedCitation = Slot(uri=UPCORE.mappedCitation, name="mappedCitation", curie=UPCORE.curie('mappedCitation'),
                   model_uri=UPCORE.mappedCitation, domain=None, range=Optional[Union[dict, Citation]])

slots.topology = Slot(uri=UPCORE.topology, name="topology", curie=UPCORE.curie('topology'),
                   model_uri=UPCORE.topology, domain=None, range=Optional[Union[dict, Topology]])

slots.classifiedWith = Slot(uri=UPCORE.classifiedWith, name="classifiedWith", curie=UPCORE.curie('classifiedWith'),
                   model_uri=UPCORE.classifiedWith, domain=None, range=Optional[Union[dict, Concept]])

slots.encodedIn = Slot(uri=UPCORE.encodedIn, name="encodedIn", curie=UPCORE.curie('encodedIn'),
                   model_uri=UPCORE.encodedIn, domain=None, range=Optional[Union[dict, SubcellularLocation]])

slots.potentialSequence = Slot(uri=UPCORE.potentialSequence, name="potentialSequence", curie=UPCORE.curie('potentialSequence'),
                   model_uri=UPCORE.potentialSequence, domain=None, range=Optional[Union[dict, Sequence]])

slots.domain = Slot(uri=UPCORE.domain, name="domain", curie=UPCORE.curie('domain'),
                   model_uri=UPCORE.domain, domain=None, range=Optional[Union[dict, Part]])

slots.enzymeClass = Slot(uri=UPCORE.enzymeClass, name="enzymeClass", curie=UPCORE.curie('enzymeClass'),
                   model_uri=UPCORE.enzymeClass, domain=None, range=Optional[Union[dict, Enzyme]])

slots.publishedIn = Slot(uri=UPCORE.publishedIn, name="publishedIn", curie=UPCORE.curie('publishedIn'),
                   model_uri=UPCORE.publishedIn, domain=None, range=Optional[Union[dict, Journal]])

slots.translatedFrom = Slot(uri=UPCORE.translatedFrom, name="translatedFrom", curie=UPCORE.curie('translatedFrom'),
                   model_uri=UPCORE.translatedFrom, domain=None, range=Optional[Union[dict, NucleotideResource]])

slots.erratumFor = Slot(uri=UPCORE.erratumFor, name="erratumFor", curie=UPCORE.curie('erratumFor'),
                   model_uri=UPCORE.erratumFor, domain=None, range=Optional[Union[dict, PublishedCitation]])

slots.member = Slot(uri=UPCORE.member, name="member", curie=UPCORE.curie('member'),
                   model_uri=UPCORE.member, domain=None, range=Optional[Union[dict, Sequence]])

slots.interaction = Slot(uri=UPCORE.interaction, name="interaction", curie=UPCORE.curie('interaction'),
                   model_uri=UPCORE.interaction, domain=None, range=Optional[Union[dict, Interaction]])

slots.attribution = Slot(uri=UPCORE.attribution, name="attribution", curie=UPCORE.curie('attribution'),
                   model_uri=UPCORE.attribution, domain=None, range=Optional[Union[dict, Attribution]])

slots.erratum = Slot(uri=UPCORE.erratum, name="erratum", curie=UPCORE.curie('erratum'),
                   model_uri=UPCORE.erratum, domain=None, range=Optional[Union[dict, PublishedCitation]])

slots.strain = Slot(uri=UPCORE.strain, name="strain", curie=UPCORE.curie('strain'),
                   model_uri=UPCORE.strain, domain=None, range=Optional[Union[dict, Strain]])

slots.basedOn = Slot(uri=UPCORE.basedOn, name="basedOn", curie=UPCORE.curie('basedOn'),
                   model_uri=UPCORE.basedOn, domain=None, range=Optional[Union[dict, SimpleSequence]])

slots.alternativeName = Slot(uri=UPCORE.alternativeName, name="alternativeName", curie=UPCORE.curie('alternativeName'),
                   model_uri=UPCORE.alternativeName, domain=None, range=Optional[Union[dict, StructuredName]])

slots.orientation = Slot(uri=UPCORE.orientation, name="orientation", curie=UPCORE.curie('orientation'),
                   model_uri=UPCORE.orientation, domain=None, range=Optional[Union[dict, Orientation]])

slots.database = Slot(uri=UPCORE.database, name="database", curie=UPCORE.curie('database'),
                   model_uri=UPCORE.database, domain=None, range=Optional[Union[dict, Database]])

slots.host = Slot(uri=UPCORE.host, name="host", curie=UPCORE.curie('host'),
                   model_uri=UPCORE.host, domain=None, range=Optional[Union[dict, Taxon]])

slots.enzyme = Slot(uri=UPCORE.enzyme, name="enzyme", curie=UPCORE.curie('enzyme'),
                   model_uri=UPCORE.enzyme, domain=None, range=Optional[Union[dict, Enzyme]])

slots.modification = Slot(uri=UPCORE.modification, name="modification", curie=UPCORE.curie('modification'),
                   model_uri=UPCORE.modification, domain=None, range=Optional[Union[dict, AlternativeSequenceAnnotation]])

slots.partOf = Slot(uri=UPCORE.partOf, name="partOf", curie=UPCORE.curie('partOf'),
                   model_uri=UPCORE.partOf, domain=None, range=Optional[Union[dict, SubcellularLocation]])

slots.rank = Slot(uri=UPCORE.rank, name="rank", curie=UPCORE.curie('rank'),
                   model_uri=UPCORE.rank, domain=None, range=Optional[Union[dict, Rank]])

slots.participant = Slot(uri=UPCORE.participant, name="participant", curie=UPCORE.curie('participant'),
                   model_uri=UPCORE.participant, domain=None, range=Optional[Union[dict, Participant]])

slots.activity = Slot(uri=UPCORE.activity, name="activity", curie=UPCORE.curie('activity'),
                   model_uri=UPCORE.activity, domain=None, range=Optional[Union[dict, CatalyticActivity]])

slots.organism = Slot(uri=UPCORE.organism, name="organism", curie=UPCORE.curie('organism'),
                   model_uri=UPCORE.organism, domain=None, range=Optional[Union[dict, Taxon]])

slots.conflictingSequence = Slot(uri=UPCORE.conflictingSequence, name="conflictingSequence", curie=UPCORE.curie('conflictingSequence'),
                   model_uri=UPCORE.conflictingSequence, domain=None, range=Optional[Union[dict, ExternalSequence]])

slots.citation = Slot(uri=UPCORE.citation, name="citation", curie=UPCORE.curie('citation'),
                   model_uri=UPCORE.citation, domain=None, range=Optional[Union[dict, Citation]])

slots.seedFor = Slot(uri=UPCORE.seedFor, name="seedFor", curie=UPCORE.curie('seedFor'),
                   model_uri=UPCORE.seedFor, domain=None, range=Optional[Union[dict, Cluster]])

slots.representativeFor = Slot(uri=UPCORE.representativeFor, name="representativeFor", curie=UPCORE.curie('representativeFor'),
                   model_uri=UPCORE.representativeFor, domain=None, range=Optional[Union[dict, Cluster]])

slots.relatedLocation = Slot(uri=UPCORE.relatedLocation, name="relatedLocation", curie=UPCORE.curie('relatedLocation'),
                   model_uri=UPCORE.relatedLocation, domain=None, range=Optional[Union[dict, SubcellularLocation]])

slots.isolatedFrom = Slot(uri=UPCORE.isolatedFrom, name="isolatedFrom", curie=UPCORE.curie('isolatedFrom'),
                   model_uri=UPCORE.isolatedFrom, domain=None, range=Optional[Union[dict, Tissue]])

slots.component = Slot(uri=UPCORE.component, name="component", curie=UPCORE.curie('component'),
                   model_uri=UPCORE.component, domain=None, range=Optional[Union[dict, Part]])

slots.annotation = Slot(uri=UPCORE.annotation, name="annotation", curie=UPCORE.curie('annotation'),
                   model_uri=UPCORE.annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.commonTaxon = Slot(uri=UPCORE.commonTaxon, name="commonTaxon", curie=UPCORE.curie('commonTaxon'),
                   model_uri=UPCORE.commonTaxon, domain=None, range=Optional[Union[dict, Taxon]])

slots.encodedBy = Slot(uri=UPCORE.encodedBy, name="encodedBy", curie=UPCORE.curie('encodedBy'),
                   model_uri=UPCORE.encodedBy, domain=None, range=Optional[Union[dict, Gene]])

slots.disease = Slot(uri=UPCORE.disease, name="disease", curie=UPCORE.curie('disease'),
                   model_uri=UPCORE.disease, domain=None, range=Optional[Union[dict, Disease]])

slots.sequence = Slot(uri=UPCORE.sequence, name="sequence", curie=UPCORE.curie('sequence'),
                   model_uri=UPCORE.sequence, domain=None, range=Optional[Union[dict, Sequence]])

slots.part = Slot(uri=UPCORE.part, name="part", curie=UPCORE.curie('part'),
                   model_uri=UPCORE.part, domain=None, range=Optional[Union[dict, Part]])

slots.submittedName = Slot(uri=UPCORE.submittedName, name="submittedName", curie=UPCORE.curie('submittedName'),
                   model_uri=UPCORE.submittedName, domain=None, range=Optional[Union[dict, StructuredName]])

slots.redundantTo = Slot(uri=UPCORE.redundantTo, name="redundantTo", curie=UPCORE.curie('redundantTo'),
                   model_uri=UPCORE.redundantTo, domain=None, range=Optional[Union[dict, Proteome]])

slots.locatedOn = Slot(uri=UPCORE.locatedOn, name="locatedOn", curie=UPCORE.curie('locatedOn'),
                   model_uri=UPCORE.locatedOn, domain=None, range=Optional[Union[dict, Molecule]])

slots.recommendedName = Slot(uri=UPCORE.recommendedName, name="recommendedName", curie=UPCORE.curie('recommendedName'),
                   model_uri=UPCORE.recommendedName, domain=None, range=Optional[Union[dict, StructuredName]])

slots.cellularComponent = Slot(uri=UPCORE.cellularComponent, name="cellularComponent", curie=UPCORE.curie('cellularComponent'),
                   model_uri=UPCORE.cellularComponent, domain=None, range=Optional[Union[dict, CellularComponent]])

slots.memberOf = Slot(uri=UPCORE.memberOf, name="memberOf", curie=UPCORE.curie('memberOf'),
                   model_uri=UPCORE.memberOf, domain=None, range=Optional[Union[dict, Cluster]])

slots.panproteome = Slot(uri=UPCORE.panproteome, name="panproteome", curie=UPCORE.curie('panproteome'),
                   model_uri=UPCORE.panproteome, domain=None, range=Optional[Union[dict, Proteome]])

slots.nucleotideSequenceMappingIssue = Slot(uri=UPCORE.nucleotideSequenceMappingIssue, name="nucleotideSequenceMappingIssue", curie=UPCORE.curie('nucleotideSequenceMappingIssue'),
                   model_uri=UPCORE.nucleotideSequenceMappingIssue, domain=None, range=Optional[Union[dict, NucleotideResource]])

slots.method = Slot(uri=UPCORE.method, name="method", curie=UPCORE.curie('method'),
                   model_uri=UPCORE.method, domain=None, range=Optional[Union[dict, Method]])

slots.datatypeProperty = Slot(uri=UPCORE.datatypeProperty, name="datatypeProperty", curie=UPCORE.curie('datatypeProperty'),
                   model_uri=UPCORE.datatypeProperty, domain=None, range=Optional[str])

slots.title = Slot(uri=UPCORE.title, name="title", curie=UPCORE.curie('title'),
                   model_uri=UPCORE.title, domain=None, range=Optional[str])

slots.height = Slot(uri=UPCORE.height, name="height", curie=UPCORE.curie('height'),
                   model_uri=UPCORE.height, domain=None, range=Optional[int])

slots.cofactorLabel = Slot(uri=UPCORE.cofactorLabel, name="cofactorLabel", curie=UPCORE.curie('cofactorLabel'),
                   model_uri=UPCORE.cofactorLabel, domain=None, range=Optional[str])

slots.precursor = Slot(uri=UPCORE.precursor, name="precursor", curie=UPCORE.curie('precursor'),
                   model_uri=UPCORE.precursor, domain=None, range=Optional[Union[bool, Bool]])

slots.created = Slot(uri=UPCORE.created, name="created", curie=UPCORE.curie('created'),
                   model_uri=UPCORE.created, domain=None, range=Optional[Union[str, XSDDate]])

slots.linkIsExplicit = Slot(uri=UPCORE.linkIsExplicit, name="linkIsExplicit", curie=UPCORE.curie('linkIsExplicit'),
                   model_uri=UPCORE.linkIsExplicit, domain=None, range=Optional[Union[bool, Bool]])

slots.length = Slot(uri=UPCORE.length, name="length", curie=UPCORE.curie('length'),
                   model_uri=UPCORE.length, domain=None, range=Optional[int])

slots.partOfLineage = Slot(uri=UPCORE.partOfLineage, name="partOfLineage", curie=UPCORE.curie('partOfLineage'),
                   model_uri=UPCORE.partOfLineage, domain=None, range=Optional[Union[bool, Bool]])

slots.measuredActivity = Slot(uri=UPCORE.measuredActivity, name="measuredActivity", curie=UPCORE.curie('measuredActivity'),
                   model_uri=UPCORE.measuredActivity, domain=None, range=Optional[str])

slots.curated = Slot(uri=UPCORE.curated, name="curated", curie=UPCORE.curie('curated'),
                   model_uri=UPCORE.curated, domain=None, range=Optional[Union[bool, Bool]])

slots.otherName = Slot(uri=UPCORE.otherName, name="otherName", curie=UPCORE.curie('otherName'),
                   model_uri=UPCORE.otherName, domain=None, range=Optional[str])

slots.experiments = Slot(uri=UPCORE.experiments, name="experiments", curie=UPCORE.curie('experiments'),
                   model_uri=UPCORE.experiments, domain=None, range=Optional[int])

slots.reviewed = Slot(uri=UPCORE.reviewed, name="reviewed", curie=UPCORE.curie('reviewed'),
                   model_uri=UPCORE.reviewed, domain=None, range=Optional[Union[bool, Bool]])

slots.modified = Slot(uri=UPCORE.modified, name="modified", curie=UPCORE.curie('modified'),
                   model_uri=UPCORE.modified, domain=None, range=Optional[Union[str, XSDDate]])

slots.institution = Slot(uri=UPCORE.institution, name="institution", curie=UPCORE.curie('institution'),
                   model_uri=UPCORE.institution, domain=None, range=Optional[str])

slots.authorsIncomplete = Slot(uri=UPCORE.authorsIncomplete, name="authorsIncomplete", curie=UPCORE.curie('authorsIncomplete'),
                   model_uri=UPCORE.authorsIncomplete, domain=None, range=Optional[Union[bool, Bool]])

slots.abstract = Slot(uri=UPCORE.abstract, name="abstract", curie=UPCORE.curie('abstract'),
                   model_uri=UPCORE.abstract, domain=None, range=Optional[Union[bool, Bool]])

slots.groupcore = Slot(uri=UPCORE.group, name="groupcore", curie=UPCORE.curie('group'),
                   model_uri=UPCORE.groupcore, domain=None, range=Optional[str])

slots.orfName = Slot(uri=UPCORE.orfName, name="orfName", curie=UPCORE.curie('orfName'),
                   model_uri=UPCORE.orfName, domain=None, range=Optional[str])

slots.width = Slot(uri=UPCORE.width, name="width", curie=UPCORE.curie('width'),
                   model_uri=UPCORE.width, domain=None, range=Optional[int])

slots.place = Slot(uri=UPCORE.place, name="place", curie=UPCORE.curie('place'),
                   model_uri=UPCORE.place, domain=None, range=Optional[str])

slots.name = Slot(uri=UPCORE.name, name="name", curie=UPCORE.curie('name'),
                   model_uri=UPCORE.name, domain=None, range=Optional[str])

slots.md5Checksum = Slot(uri=UPCORE.md5Checksum, name="md5Checksum", curie=UPCORE.curie('md5Checksum'),
                   model_uri=UPCORE.md5Checksum, domain=None, range=Optional[str])

slots.mnemonic = Slot(uri=UPCORE.mnemonic, name="mnemonic", curie=UPCORE.curie('mnemonic'),
                   model_uri=UPCORE.mnemonic, domain=None, range=Optional[str])

slots.frameshift = Slot(uri=UPCORE.frameshift, name="frameshift", curie=UPCORE.curie('frameshift'),
                   model_uri=UPCORE.frameshift, domain=None, range=Optional[Union[bool, Bool]])

slots.oldMnemonic = Slot(uri=UPCORE.oldMnemonic, name="oldMnemonic", curie=UPCORE.curie('oldMnemonic'),
                   model_uri=UPCORE.oldMnemonic, domain=None, range=Optional[str])

slots.chain = Slot(uri=UPCORE.chain, name="chain", curie=UPCORE.curie('chain'),
                   model_uri=UPCORE.chain, domain=None, range=Optional[str])

slots.pages = Slot(uri=UPCORE.pages, name="pages", curie=UPCORE.curie('pages'),
                   model_uri=UPCORE.pages, domain=None, range=Optional[str])

slots.pattern = Slot(uri=UPCORE.pattern, name="pattern", curie=UPCORE.curie('pattern'),
                   model_uri=UPCORE.pattern, domain=None, range=Optional[str])

slots.substitution = Slot(uri=UPCORE.substitution, name="substitution", curie=UPCORE.curie('substitution'),
                   model_uri=UPCORE.substitution, domain=None, range=Optional[str])

slots.version = Slot(uri=UPCORE.version, name="version", curie=UPCORE.curie('version'),
                   model_uri=UPCORE.version, domain=None, range=Optional[int])

slots.implicit = Slot(uri=UPCORE.implicit, name="implicit", curie=UPCORE.curie('implicit'),
                   model_uri=UPCORE.implicit, domain=None, range=Optional[Union[bool, Bool]])

slots.measuredAffinity = Slot(uri=UPCORE.measuredAffinity, name="measuredAffinity", curie=UPCORE.curie('measuredAffinity'),
                   model_uri=UPCORE.measuredAffinity, domain=None, range=Optional[str])

slots.obsolete = Slot(uri=UPCORE.obsolete, name="obsolete", curie=UPCORE.curie('obsolete'),
                   model_uri=UPCORE.obsolete, domain=None, range=Optional[Union[bool, Bool]])

slots.locator = Slot(uri=UPCORE.locator, name="locator", curie=UPCORE.curie('locator'),
                   model_uri=UPCORE.locator, domain=None, range=Optional[str])

slots.mass = Slot(uri=UPCORE.mass, name="mass", curie=UPCORE.curie('mass'),
                   model_uri=UPCORE.mass, domain=None, range=Optional[int])

slots.uriTemplate = Slot(uri=UPCORE.uriTemplate, name="uriTemplate", curie=UPCORE.curie('uriTemplate'),
                   model_uri=UPCORE.uriTemplate, domain=None, range=Optional[str])

slots.scientificName = Slot(uri=UPCORE.scientificName, name="scientificName", curie=UPCORE.curie('scientificName'),
                   model_uri=UPCORE.scientificName, domain=None, range=Optional[str])

slots.alias = Slot(uri=UPCORE.alias, name="alias", curie=UPCORE.curie('alias'),
                   model_uri=UPCORE.alias, domain=None, range=Optional[str])

slots.exclusionReason = Slot(uri=UPCORE.exclusionReason, name="exclusionReason", curie=UPCORE.curie('exclusionReason'),
                   model_uri=UPCORE.exclusionReason, domain=None, range=Optional[str])

slots.measuredError = Slot(uri=UPCORE.measuredError, name="measuredError", curie=UPCORE.curie('measuredError'),
                   model_uri=UPCORE.measuredError, domain=None, range=Optional[float])

slots.publisher = Slot(uri=UPCORE.publisher, name="publisher", curie=UPCORE.curie('publisher'),
                   model_uri=UPCORE.publisher, domain=None, range=Optional[str])

slots.maximum = Slot(uri=UPCORE.maximum, name="maximum", curie=UPCORE.curie('maximum'),
                   model_uri=UPCORE.maximum, domain=None, range=Optional[float])

slots.structuredNameType = Slot(uri=UPCORE.structuredNameType, name="structuredNameType", curie=UPCORE.curie('structuredNameType'),
                   model_uri=UPCORE.structuredNameType, domain=None, range=Optional[str])

slots.editor = Slot(uri=UPCORE.editor, name="editor", curie=UPCORE.curie('editor'),
                   model_uri=UPCORE.editor, domain=None, range=Optional[str])

slots.author = Slot(uri=UPCORE.author, name="author", curie=UPCORE.curie('author'),
                   model_uri=UPCORE.author, domain=None, range=Optional[str])

slots.measuredValue = Slot(uri=UPCORE.measuredValue, name="measuredValue", curie=UPCORE.curie('measuredValue'),
                   model_uri=UPCORE.measuredValue, domain=None, range=Optional[float])

slots.negative = Slot(uri=UPCORE.negative, name="negative", curie=UPCORE.curie('negative'),
                   model_uri=UPCORE.negative, domain=None, range=Optional[Union[bool, Bool]])

slots.shortCoden = Slot(uri=UPCORE.shortCoden, name="shortCoden", curie=UPCORE.curie('shortCoden'),
                   model_uri=UPCORE.shortCoden, domain=None, range=Optional[str])

slots.xeno = Slot(uri=UPCORE.xeno, name="xeno", curie=UPCORE.curie('xeno'),
                   model_uri=UPCORE.xeno, domain=None, range=Optional[Union[bool, Bool]])

slots.synonym = Slot(uri=UPCORE.synonym, name="synonym", curie=UPCORE.curie('synonym'),
                   model_uri=UPCORE.synonym, domain=None, range=Optional[str])

slots.scope = Slot(uri=UPCORE.scope, name="scope", curie=UPCORE.curie('scope'),
                   model_uri=UPCORE.scope, domain=None, range=Optional[str])

slots.urlTemplate = Slot(uri=UPCORE.urlTemplate, name="urlTemplate", curie=UPCORE.curie('urlTemplate'),
                   model_uri=UPCORE.urlTemplate, domain=None, range=Optional[str])

slots.resolution = Slot(uri=UPCORE.resolution, name="resolution", curie=UPCORE.curie('resolution'),
                   model_uri=UPCORE.resolution, domain=None, range=Optional[float])

slots.manual = Slot(uri=UPCORE.manual, name="manual", curie=UPCORE.curie('manual'),
                   model_uri=UPCORE.manual, domain=None, range=Optional[Union[bool, Bool]])

slots.certain = Slot(uri=UPCORE.certain, name="certain", curie=UPCORE.curie('certain'),
                   model_uri=UPCORE.certain, domain=None, range=Optional[Union[bool, Bool]])

slots.complete = Slot(uri=UPCORE.complete, name="complete", curie=UPCORE.curie('complete'),
                   model_uri=UPCORE.complete, domain=None, range=Optional[Union[bool, Bool]])
