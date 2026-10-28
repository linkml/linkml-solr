# -*- coding: utf-8 -*-
"""Solr-free tests for ``lsolr patch`` (patch_core)."""
import os
import tempfile
import unittest
from unittest import mock

import duckdb

import linkml_solr.build as build_mod
from linkml_solr.build import BuildConfig, CoreSpec, SourceSpec, patch_core


class TestPatchCore(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.db = os.path.join(self.tmp, "kg.duckdb")
        con = duckdb.connect(self.db)
        con.execute("CREATE TABLE nodes (id VARCHAR, provided_by VARCHAR)")
        con.execute("INSERT INTO nodes VALUES ('HP:1', 'phenio'), ('DRON:1', 'medic'), ('HP:2', 'phenio')")
        con.close()
        self.spec = CoreSpec(name="entity", source=SourceSpec(duckdb=self.db, table="nodes"))
        self.cfg = BuildConfig(cores=[self.spec])

    def run_patch(self, old_ids, where="provided_by = 'medic'", loader=None, post=None):
        loaded_where = {}

        def fake_load(**kw):
            loaded_where["where"] = kw["where_clause"]
            con = duckdb.connect(self.db, read_only=True)
            rows = con.execute(f"SELECT id FROM nodes WHERE {kw['where_clause']} ORDER BY id").fetchall()
            con.close()
            loaded_where["ids"] = [r[0] for r in rows]
            return len(rows)

        with mock.patch.object(build_mod, "solr_ids", return_value=old_ids), \
                mock.patch.object(build_mod.requests, "post", side_effect=post) as post, \
                mock.patch.object(build_mod.requests, "get") as get, \
                mock.patch.object(build_mod, "bulkload_duckdb", side_effect=loader or fake_load):
            self.post, self.get = post, get
            counts = patch_core(self.cfg, self.spec, "provided_by:medic", where)
        return counts, loaded_where, post

    def posted(self):
        return [c.kwargs["json"] for c in self.post.call_args_list]

    def test_reloads_where_rows_and_surviving_old_ids(self):
        # HP:1 was medic-provided in the old index and is phenio's now; UMLS:1 is gone.
        counts, loaded, post = self.run_patch(["HP:1", "UMLS:1"])
        self.assertEqual(loaded["ids"], ["DRON:1", "HP:1"])
        self.assertEqual(counts, {"deleted": 2, "expected": 2, "loaded": 2})
        self.assertEqual(self.posted(), [{"delete": {"query": "provided_by:medic"}}])
        # committed once, by patch_core, after the load
        self.assertEqual(self.get.call_args.kwargs["params"]["commit"], "true")
        self.get.assert_called_once()

    def test_count_mismatch_rolls_back_without_commit(self):
        with self.assertRaisesRegex(RuntimeError, "loaded 1 docs, expected 2; not committed; rolled back"):
            self.run_patch(["HP:1"], loader=lambda **kw: 1)
        self.assertEqual(self.posted(), [{"delete": {"query": "provided_by:medic"}}, {"rollback": {}}])
        self.get.assert_not_called()

    def test_failed_load_rolls_back_without_commit(self):
        def boom(**kw):
            raise RuntimeError("POST failed")
        with self.assertRaisesRegex(RuntimeError, r"patch failed \(POST failed\); not committed; rolled back"):
            self.run_patch(["HP:1"], loader=boom)
        self.assertEqual(self.posted(), [{"delete": {"query": "provided_by:medic"}}, {"rollback": {}}])
        self.get.assert_not_called()

    def test_failed_rollback_says_changes_remain_pending(self):
        def post(url, json=None, **kw):
            if json == {"rollback": {}}:
                raise build_mod.requests.exceptions.ConnectionError("refused")
            return mock.Mock()
        with self.assertRaisesRegex(RuntimeError, "rollback failed .*remains pending.*autoCommit"):
            self.run_patch(["HP:1"], loader=lambda **kw: 1, post=post)
        self.get.assert_not_called()

    def test_core_source_where_still_applies(self):
        self.spec.source.where = "id <> 'DRON:1'"
        _, loaded, _ = self.run_patch(["HP:1"])
        self.assertEqual(loaded["ids"], ["HP:1"])

    def test_dry_run_changes_nothing(self):
        self.cfg.dry_run = True
        with mock.patch.object(build_mod, "solr_ids", return_value=["HP:1"]), \
                mock.patch.object(build_mod.requests, "post") as post, \
                mock.patch.object(build_mod.requests, "get") as get:
            counts = patch_core(self.cfg, self.spec, "provided_by:medic", "provided_by = 'medic'")
        post.assert_not_called()
        get.assert_not_called()
        self.assertEqual(counts, {"deleted": 1, "expected": 2, "loaded": 0})


if __name__ == "__main__":
    unittest.main()
