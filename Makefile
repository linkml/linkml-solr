RUN = pipenv run

all: test

test:
	pipenv run python -m unittest

test_data: tests/test_models/kitchen_sink.context.jsonld tests/test_models/kitchen_sink.py

SRC = tests/test_models/%.yaml
tests/test_models/%.context.jsonld: $(SRC)
	$(RUN) gen-jsonld-context $< > $@
tests/test_models/%.py: $(SRC)
	$(RUN) gen-python $< > $@
tests/test_models/%.ttl: $(SRC)
	$(RUN) gen-rdf $< > $@
tests/test_models/amigo.yaml: linkml_solr/utils/golr_schema_utils.py
	pipenv run python $< tests/test_golr/*yaml > $@
