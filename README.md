# linkml-solr

A simple wrapper for using Solr with [LinkML](https://linkml.io) schemas

This provides a convenience layer for working with a Solr database
whose schema is defined in LinkML. It provides bindings both from
slots in your schema to queries, and binds result objects to your
object model.

```python
from tests.test_models.books import *
from linkml_solr import SolrQueryEngine, SolrEndpoint
...
schema = YAMLGenerator(schemafile).schema
qe = SolrQueryEngine(schema=schema,
                     endpoint=SolrEndpoint(url='http://localhost:8983/solr/books'))

result = qe.search(target_class=Book, genre_s='scifi')
for book in result.items:
    print(f'Book:  {book.name} :: {book}')
```

Unlike querying with the native pysolr API, this will validate input
keys (which your IDE will be aware of), and will instantiate an
instance of your model class.

 - validate query inputs (also IDE-aware)
 - instantiate classes in your object model
 - provide mappings from abstracted domain model concepts

## Step 1: Define your datamodel

See [tests/test_models/books.yaml](tests/test_models/books.yaml) for an example schema

The Schema must be specified as a [LinkML schema](https://linkml.io/linkml/schemas/index.html). Note that LinkML is
more expressive than solr schemas, so not all constructs can be
used. However, certain inferences are performed when compiling to Solr
schemas - for example, you can use inheritance, and leaf classes will have all slots inferred.

Your schemas should be relatively "flat and wide". Use denormalization over nesting.

When designing your schema consider the two different paradigms supported:

 * one core per schema, with document records having the union of all fields
 * one core per class

Note: you can use the linkml-model-enrichment toolkit to auto-infer schemas from data

In future there will be ways to annotate your schema to give hints when making solr indexers etc.

## Step 2: Create Python dataclasses

Use the LinkML [python generator](https://linkml.io/linkml/generators/python.html)

```bash
gen-python books.yaml > books.py
```

See [tests/test_models/books.py](tests/test_models/books.py) for an example

## Step 3: Start a server

This starts a server, precreates a core "books" and loads a solr schema from a linkml schema:

```bash
lsolr start-server -C books -s books.yaml
```

This wraps a docker container. If you do not wish to use a Docker container, then start solr in the usual way

TODO: docs on how to do this

## Step 4: Bulkload (optional)

```bash
lsolr bulkload -C books -s books.yaml books1.tsv books2.tsv ...
```

## Step 5: Code against your schema

See [tests/test_query.py](tests/test_query.py) for an example

## Command Line Tools

### main command

```
lsolr --help
Usage: lsolr [OPTIONS] COMMAND [ARGS]...

  Main

  Args:

      verbose (int): Verbose.     quiet (bool): Quiet.

  Returns:

      None.

Options:
  -v, --verbose
  -q, --quiet TEXT
  --help            Show this message and exit.

Commands:
  bulkload       Convert multiple golr yaml schemas to linkml :param files:...
  create-schema
  start-server
```

### bulkload

```
lsolr bulkload --help
Usage: lsolr bulkload [OPTIONS] [FILES]...

  Convert multiple golr yaml schemas to linkml :param files: :param schema:
  :return:

Options:
  -s, --schema TEXT  Path to schema.
  -C, --core TEXT    solr core.
  -f, --format TEXT  input format.
  -u, --url TEXT     solr url.
  --help             Show this message and exit.
```

## More documentation

More documentation coming soon. For now, consult the tests.

## Appendix

### Converting from Golr schemas to LinkML

See the Makefile:

```Makefile
tests/test_models/amigo.yaml: linkml_solr/utils/golr_schema_utils.py
	pipenv run python $< tests/test_golr/*yaml > $@
```

## TODOs

Alpha code. Functionality is very incomplete

 - write
 - customizable dynamic mapping
 - automatic de-nesting/de-normalization
 - autogen of model-specific API
 - expose additional solr functionality
 - 
