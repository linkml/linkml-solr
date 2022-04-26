RUN = poetry run
LSOLR = $(RUN) lsolr

all: build test

clean:
	rm test-docker-env

build: linkml_solr/solrschema.py

# Running make test
# TODO: sometimes load starts before docker environment complete
test: test-docker-env test_main

test_main:
	$(RUN) python -m unittest

test_data: tests/test_models/kitchen_sink.context.jsonld tests/test_models/kitchen_sink.py

# typically this should not need to be regenerated
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
tests/test_models/%_api.py: $(TESTMODELS_SRC)
	$(RUN) gen-python-api $< > $@
tests/test_models/%.ttl: $(TESTMODELS_SRC)
	$(RUN) gen-rdf $< > $@
tests/test_models/amigo.yaml: linkml_solr/utils/golr_schema_utils.py
	pipenv run python $< tests/test_golr/*yaml > $@


test-docker-env: test-server wait-10 test-load
	touch $@

start-solr-server:
	$(LSOLR) start-server
test-server:
	$(LSOLR) start-server -C books --sleep 10 -s tests/test_models/books.yaml

add-test-core: add-core-test
add-core-%:
	$(LSOLR) add-cores $*

test-schema: 
	$(LSOLR) create-schema -C books -s tests/test_models/books.yaml 

wait-%:
	sleep $*

# uses solr_bulkload.py to load into a core
test-load: tests/inputs/books.tsv
	$(LSOLR) bulkload -C books -s tests/test_models/books.yaml $<
test-load2: tests/inputs/books.json
	$(LSOLR) bulkload -f json -C books -s tests/test_models/books.yaml $<
