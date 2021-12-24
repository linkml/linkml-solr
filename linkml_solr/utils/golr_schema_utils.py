import click
from typing import List, Dict
import logging


import yaml

def golr_to_linkml_schema(inputs: Dict[str, dict], base_url: str = 'https://w3id.org/', schema_id: str = 'example') -> dict:
    cls_to_file = {}
    slots = {'document_category': {}}
    classes = {}
    url = f'{base_url}/{schema_id}'
    schema = {
        'id': url,
        'description': 'TODO',
        'imports': [
            'linkml:types'
        ],
        'prefixes': {
            'linkml': 'https://w3id.org/linkml/',
            schema_id: 'http://kbase.us/'
        },
        'default_prefix': schema_id,
        'classes': classes,
        'slots': slots,
        'types': {
            'SearchableString': {
                'typeof': 'string'
            }
        }
    }
    for fn, input in inputs.items():
        cslots = ['document_category']
        n = input['document_category']
        c = {'aliases': [input['display_name']],
            'description': input['description'],
            'slots': cslots}
        if n in classes:
            raise Exception(f'Duplicate class name: {n}: in {cls_to_file[n]} and {fn}')
        cls_to_file[n] = fn
        classes[n] = c
        for f in input['fields']:
            fid = f['id']

            card = f.get('cardinality', '')
            if card == 'multi':
                multivalued = True
            else:
                multivalued = False
            range = f['type']
            searchable = f.get('searchable', False)
            if searchable:
                range = 'SearchableString'
            slot = {'description': f['description'],
                    'range': range,
                    'aliases': [f['display_name']],
                    'multivalued': multivalued,
                    'comments': []}
            #for p in f.get('property', []):
            #    slot['aliases'].append(p) # TODO: xref
            if f.get('indexed', False):
                slot['comments'].append('Indexed')
            if fid in slot:
                logging.warning(f'Overwriting: {fid} in {n}')
            slots[fid] = slot
            cslots.append(fid)
            if searchable:
                sslot = slot.copy()
                sfid = f'{fid}_searchable'
                slots[sfid] = sslot
                cslots.append(sfid)
    return schema

@click.command()
@click.option('--schema', '-s',
              help='Name of schema.')
@click.argument('files', nargs=-1)
def convert(files, schema):
    """
    Convert multiple golr yaml schemas to linkml

    Note this is primarily useful for converting schemas in the
    golr format used by AmiGO/Monarch

    :param files:
    :param schema:
    :return:
    """
    inputs = {}
    for f in files:
        with open(f) as stream:
            inputs[f] = yaml.safe_load(stream)
    s = golr_to_linkml_schema(inputs, schema_id=schema)
    print(yaml.dump(s, sort_keys=False))

if __name__ == '__main__':
    convert()