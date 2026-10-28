import json
import os
import tempfile
import unittest
from unittest import mock

import duckdb

import linkml_solr.utils.solr_bulkload as bulkload_mod
from linkml_solr.utils.solr_bulkload import _solr_value


class SolrValueTestCase(unittest.TestCase):
    """Nested records are serialized to JSON strings for Solr (no service needed)."""

    def test_record_becomes_json_string(self):
        assert json.loads(_solr_value({"resource_id": "infores:x", "urls": ["u"]})) == {
            "resource_id": "infores:x",
            "urls": ["u"],
        }

    def test_list_of_records_becomes_list_of_json_strings(self):
        value = _solr_value([{"resource_id": "infores:x"}, {"resource_id": "infores:y"}])
        assert [json.loads(v)["resource_id"] for v in value] == ["infores:x", "infores:y"]

    def test_scalars_and_scalar_lists_pass_through(self):
        assert _solr_value("MONDO:1") == "MONDO:1"
        assert _solr_value(["PMID:1", "PMID:2"]) == ["PMID:1", "PMID:2"]
        assert _solr_value(None) is None
        assert _solr_value(3) == 3


class BulkloadDuckdbJsonFieldsTestCase(unittest.TestCase):
    """bulkload_duckdb serializes nested records before posting (Solr mocked out)."""

    def _posted_docs(self, drop_nulls: bool) -> list:
        with tempfile.TemporaryDirectory() as tmp:
            db = os.path.join(tmp, "src.duckdb")
            conn = duckdb.connect(db)
            conn.execute("""
                CREATE TABLE assoc AS SELECT * FROM (VALUES
                  ('a1', [{'resource_id': 'infores:x', 'urls': ['u']}], NULL),
                  ('a2', [{'resource_id': 'infores:y', 'urls': []}], 'PMID:1')
                ) t(id, sources, publication)
            """)
            conn.close()
            posted = []

            def fake_upload(docs, *args, **kwargs):
                posted.extend(docs)
                return len(docs)

            with mock.patch.object(bulkload_mod, "_upload_docs_to_solr", side_effect=fake_upload):
                loaded = bulkload_mod.bulkload_duckdb(
                    db, "assoc", "http://solr.invalid", "core", schema=None,
                    max_workers=1, snapshot=False, drop_nulls=drop_nulls,
                )
            assert loaded == 2
            return sorted(posted, key=lambda d: d["id"])

    def _assert_sources_are_json_strings(self, docs):
        for doc in docs:
            assert all(isinstance(v, str) for v in doc["sources"])
        assert json.loads(docs[0]["sources"][0]) == {"resource_id": "infores:x", "urls": ["u"]}

    def test_drop_nulls_path_serializes_records(self):
        # `lsolr build` (_shard_worker) loads with drop_nulls=True
        docs = self._posted_docs(drop_nulls=True)
        self._assert_sources_are_json_strings(docs)
        assert "publication" not in docs[0]
        assert docs[1]["publication"] == "PMID:1"

    def test_keep_nulls_path_serializes_records(self):
        docs = self._posted_docs(drop_nulls=False)
        self._assert_sources_are_json_strings(docs)
        assert docs[0]["publication"] is None


if __name__ == '__main__':
    unittest.main()
