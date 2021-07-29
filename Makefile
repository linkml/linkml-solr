RUN = pipenv run

all: build test


build: linkml_solr/solrschema.py

test:
	pipenv run python -m unittest

test_data: tests/test_models/kitchen_sink.context.jsonld tests/test_models/kitchen_sink.py

SRC = model/schema/solrschema.yaml
linkml_solr/solrschema.py: $(SRC)
	$(RUN) gen-python --no-slots $< > $@.tmp && mv $@.tmp $@
linkml_solr/jsonschema/%.schema.json: $(SRC)
	$(RUN) gen-json-schema $< > $@.tmp && mv $@.tmp $@


TESTMODELS_SRC = tests/test_models/%.yaml
tests/test_models/%.context.jsonld: $(TESTMODELS_SRC)
	$(RUN) gen-jsonld-context $< > $@
tests/test_models/%.py: $(TESTMODELS_SRC)
	$(RUN) gen-python $< > $@
tests/test_models/%.ttl: $(TESTMODELS_SRC)
	$(RUN) gen-rdf $< > $@
tests/test_models/amigo.yaml: linkml_solr/utils/golr_schema_utils.py
	pipenv run python $< tests/test_golr/*yaml > $@

#BL = $(RUN) python linkml_solr/utils/solr_bulkload.py
BL = $(RUN) lsolr-bulkload

test-server:
	$(BL) start-server -C books -s tests/test_models/books.yaml

test-schema: 
	$(BL) create-schema -C books -s tests/test_models/books.yaml 

test-load: tests/inputs/books.tsv
	$(BL) bulkload -C books -s tests/test_models/books.yaml $<
test-load2: tests/inputs/books.json
	$(BL) bulkload -f json -C books -s tests/test_models/books.yaml $<
