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

    def run_patch(self, old_ids, where="provided_by = 'medic'"):
        loaded_where = {}

        def fake_worker(a):
            loaded_where["where"] = a[4]
            con = duckdb.connect(self.db, read_only=True)
            rows = con.execute(f"SELECT id FROM nodes WHERE {a[4]} ORDER BY id").fetchall()
            con.close()
            loaded_where["ids"] = [r[0] for r in rows]
            return a[2], len(rows), 0.0

        with mock.patch.object(build_mod, "solr_ids", return_value=old_ids), \
                mock.patch.object(build_mod.requests, "post") as post, \
                mock.patch.object(build_mod, "_shard_worker", side_effect=fake_worker):
            counts = patch_core(self.cfg, self.spec, "provided_by:medic", where)
        return counts, loaded_where, post

    def test_reloads_where_rows_and_surviving_old_ids(self):
        # HP:1 was medic-provided in the old index and is phenio's now; UMLS:1 is gone.
        counts, loaded, post = self.run_patch(["HP:1", "UMLS:1"])
        self.assertEqual(loaded["ids"], ["DRON:1", "HP:1"])
        self.assertEqual(counts, {"deleted": 2, "expected": 2, "loaded": 2})
        self.assertEqual(post.call_args.kwargs["json"], {"delete": {"query": "provided_by:medic"}})

    def test_core_source_where_still_applies(self):
        self.spec.source.where = "id <> 'DRON:1'"
        _, loaded, _ = self.run_patch(["HP:1"])
        self.assertEqual(loaded["ids"], ["HP:1"])

    def test_dry_run_changes_nothing(self):
        self.cfg.dry_run = True
        with mock.patch.object(build_mod, "solr_ids", return_value=["HP:1"]), \
                mock.patch.object(build_mod.requests, "post") as post:
            counts = patch_core(self.cfg, self.spec, "provided_by:medic", "provided_by = 'medic'")
        post.assert_not_called()
        self.assertEqual(counts, {"deleted": 1, "expected": 2, "loaded": 0})


if __name__ == "__main__":
    unittest.main()
