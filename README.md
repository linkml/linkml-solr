# linkml-sparql: ORM for SPARQL endpoints

This provides a way of querying either in-memory RDF graphs or remote SPARQL endpoints using a LinkML specified datamodel.

## Step 1: Define your datamodel and RDF bindings

As an example, a small schema for a portion of DBpedia:

```yaml
id: http://dbpedia.org/ontology/
imports:
 - linkml:types
prefixes:
  dbont: http://dbpedia.org/ontology/
  dbproperty: http://dbpedia.org/property/
  dbr: http://dbpedia.org/resource/
  linkml: https://w3id.org/linkml/
  geo: http://www.w3.org/2003/01/geo/wgs84_pos#
  wd: http://www.wikidata.org/entity/
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  
default_prefix: dbont

classes:
  Thing:
    slots:
      - id
      - label
      - comment
      - type

  Food:
    is_a: Thing
    exact_mappings:
      - wd:Q2095
    slots:
      - servingTemperature
      - servingSize
      - alias
      - cuisine
      - ingredientName
      - origin
      - region
      - distributor
      - approximateCalories
      - carbohydrate
      - fat
      - protein
```

## Step 2: Create Python dataclasses

```bash
pipenv run gen-python dbont.yaml > dbont.py
```

## Step 3: Code

```python

from dbont import Food
from linkml_sparql import QueryEngine, SparqlEndpoint



   schema = YAMLGenerator(SCHEMA).schema
   qe = QueryEngine(schema=schema,
                         endpoint=SparqlEndpoint(url='http://dbpedia.org/sparql/'),
                         lang='en')
   objs = qe.query(type=Food.class_class_curie,
                        origin='dbr:Scotland',
                        target_class=Food)
   for obj in objs:
       print(f'{obj.id} {obj.label} distributed by {obj.distributor}')
```

## More documentation

More documentation coming soon. For now, consult the tests.

## TODOs

Functionality is very incomplete

 - remote querying via DESCRIBE can be inefficient
 - ...lots more
