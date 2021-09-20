import os
from typing import Union, TextIO, Optional, Dict, Tuple

import click
import json
from linkml_runtime.linkml_model.meta import SchemaDefinition, ClassDefinition, SlotDefinition
from linkml_runtime.dumpers import json_dumper
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
    generatorname = os.path.basename(__file__)
    generatorversion = "0.0.1"
    valid_formats = ["json"]
    visit_all_class_slots = True
    transaction: Transaction = None

    def __init__(self, schema: Union[str, TextIO, SchemaDefinition], top_class: Optional[str] = None, **kwargs) -> None:
        super().__init__(schema, **kwargs)
        self.transaction = Transaction()
        self.post_request = None
        self.inline = False
        self.topCls = top_class  ## SOLR object is one instance of this
        self.entryProperties = {}
        # SOLR-Schema does not have inheritance,
        # so we duplicate slots from inherited parents and mixins
        self.visit_all_slots = True

    def end_schema(self, **_) -> None:
        obj = json.loads(json_dumper.dumps(self.transaction))
        # TODO: linkml currently has no way to declare a slot with hyphens in the name
        obj = {k.replace('_', '-'): v for k, v in obj.items() if k != '@type'}
        self.post_request = obj
        print(json.dumps(obj, indent='  '))

    def visit_slot(self, aliased_slot_name: str, slot: SlotDefinition) -> None:
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
            field = Field(name=aliased_slot_name,
                          multiValued=slot.multivalued,
                          type=solr_schema_types[range])
            self.transaction.add_field.append(field)
        else:
            raise Exception(f'Unknown range: {range} for slot {slot}')




# TODO: move to linkml
@shared_arguments(SolrSchemaGenerator)
@click.command()
def cli(yamlfile, **kwargs):
    """ Generate SOLR Schema representation of a biolink model """
    print(SolrSchemaGenerator(yamlfile, **kwargs).serialize(**kwargs))


if __name__ == '__main__':
    cli()
