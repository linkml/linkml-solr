import os
from typing import Union, TextIO, Optional, Dict, Tuple

import click
import json
from linkml_runtime.linkml_model.meta import SchemaDefinition, ClassDefinition, SlotDefinition, ClassDefinitionName
from linkml_runtime.dumpers import json_dumper
from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.utils.yamlutils import YAMLRoot, as_json_object
from linkml_runtime.utils.formatutils import camelcase, be, underscore

from linkml.utils.generator import Generator, shared_arguments

from linkml_solr.solrschema import *

# Map from underlying python data type to solr equivalent
# Note: The underlying types are a union of any built-in python datatype + any type defined in
#       linkml-runtime/utils/metamodelcore.py
# Note the keys are all lower case
solr_schema_types: Dict[str, str] = {
    "int": "int",
    "integer": "int",
    "str": "string",
    "string": "string",
    "bool": "boolean",
    "boolean": "boolean",
    "float": "float",
    "double": "double",
    "decimal": "double",
    "xsddate": "date",
    "xsddatetime": "date",
    "xsdtime": "time"
}

class SolrSchemaGenerator(Generator):
    """
    Generates a Solr schema from a LinkML schema

    The output is a JSON document representing Solr operations such as AddField

    Note that this makes a flattened 'union' schema for all classes, as Solr does not have the concept
    of classes/records
    """
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.1"
    valid_formats = ["json"]
    visit_all_class_slots = True
    transaction: Transaction = None
    schemaview: SchemaView = None

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], top_class: Optional[str] = None, **kwargs) -> None:
        super().__init__(schema, **kwargs)
        #self.schema = schema
        self.transaction = Transaction()
        self.post_request = None
        self.inline = False
        self.topCls = top_class  ## SOLR object is one instance of this
        self.entryProperties = {}
        # SOLR-Schema does not have inheritance,
        # so we duplicate slots from inherited parents and mixins
        self.visit_all_slots = True
        self.schemaview = SchemaView(self.schema)

    def _transaction_json(self, transaction: Transaction) -> str:
        obj = json.loads(json_dumper.dumps(transaction))
        # TODO: linkml currently has no way to declare a slot with hyphens in the name
        obj = {k.replace('_', '-'): v for k, v in obj.items() if k != '@type'}
        self.post_request = obj
        return json.dumps(obj, indent='  ')

    def class_schema(self, class_name: Union[str, ClassDefinitionName]) -> str:
        transaction = self.get_transaction(class_name)
        return self._transaction_json(transaction)

    def end_schema(self, **_) -> None:
        transaction = self.get_transaction()
        print(self._transaction_json(transaction))

    def get_transaction(self, class_name: Union[str, ClassDefinitionName] = None) -> Transaction:
        transaction = Transaction()
        sv = self.schemaview
        field_dict = {}
        for cn, c in sv.all_classes().items():
            if class_name is None or str(cn) == str(class_name):
                for s in sv.class_induced_slots(cn):
                    field = self.get_field(s)
                    field_dict[field.name] = field
        for field in field_dict.values():
            transaction.add_field.append(field)
        return transaction

    def get_field(self, slot: SlotDefinition) -> Field:
        range = slot.range
        if range in self.schema.classes:
            range = 'string' # FK
        elif range in self.schema.enums:
            range = 'string'
        elif range in self.schema.types:
            t = self.schema.types[range]
            range = t.typeof
            if t.typeof is None:
                range = t.base
        range = str(range).lower()
        if range in solr_schema_types:
            field = Field(name=slot.name,
                          multiValued=slot.multivalued,
                          type=solr_schema_types[range])
            return field
        else:
            raise Exception(f'Unknown range: {range} for slot {slot}')


@shared_arguments(SolrSchemaGenerator)
@click.command()
def cli(yamlfile, **kwargs):
    """ Generate SOLR Schema representation of a LinkML model """
    print(SolrSchemaGenerator(yamlfile, **kwargs).serialize(**kwargs))


if __name__ == '__main__':
    cli()
