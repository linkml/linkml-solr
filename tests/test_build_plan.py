# -*- coding: utf-8 -*-
"""Solr-free tests for the config-driven build planner (``lsolr build``)."""
import os
import tempfile
import unittest
from unittest import mock

import linkml_solr.build as build_mod
from linkml_solr.build import BuildConfig, CoreSpec, SourceSpec, build, merge_indexes, _expected_count


class TestBuildConfig(unittest.TestCase):
    """BuildConfig.from_yaml parsing and dry-run planning (no Solr required)."""

    YAML = """
runtime: docker
port: 8985
heap: 4g
skip_tarball: true
cores:
  - name: entity
    linkml_schema: schema.yaml
    top_class: Entity
    schema_json_pre: [text-fieldtype.json]
    schema_json_post: [entity-copyfields.json]
    source: {duckdb: kg.duckdb, table: nodes}
    verify: {table: nodes, id_field: id}
  - name: association
    linkml_schema: schema.yaml
    top_class: Association
    shards: 3
    source: {duckdb: kg.duckdb, table: edges}
  - name: infores
    source: {json_docs: infores.jsonl}
"""

    def _cfg(self) -> BuildConfig:
        fd, path = tempfile.mkstemp(suffix=".yaml")
        with os.fdopen(fd, "w") as fh:
            fh.write(self.YAML)
        try:
            return BuildConfig.from_yaml(path)
        finally:
            os.unlink(path)

    def test_from_yaml_parses_cores(self):
        cfg = self._cfg()
        self.assertEqual(cfg.port, 8985)
        self.assertTrue(cfg.skip_tarball)
        self.assertEqual([c.name for c in cfg.cores], ["entity", "association", "infores"])

        entity = cfg.cores[0]
        self.assertEqual(entity.top_class, "Entity")
        self.assertEqual(entity.schema_json_pre, ["text-fieldtype.json"])
        self.assertEqual(entity.shards, 1)  # default
        self.assertIsInstance(entity.source, SourceSpec)
        self.assertEqual(entity.source.table, "nodes")
        self.assertEqual(entity.verify, {"table": "nodes", "id_field": "id"})

        self.assertEqual(cfg.cores[1].shards, 3)
        self.assertEqual(cfg.cores[2].source.json_docs, "infores.jsonl")

    def test_dry_run_plan_runs(self):
        """A dry run must produce a plan without touching Solr/Docker."""
        cfg = self._cfg()
        cfg.dry_run = True
        with self.assertLogs("linkml_solr.build", level="INFO") as cm:
            build(cfg)
        log = "\n".join(cm.output)
        # runtime start + configset + each core created
        self.assertIn("solr runtime: docker", log)
        self.assertIn("would install _default configset", log)
        for core in ("entity", "association", "infores"):
            self.assertIn(f"create core {core}", log)
        # sharded core plans N shard cores + a merge
        self.assertIn("association: 3 shards + MERGEINDEXES", log)
        self.assertIn("create core association_shard_0", log)
        self.assertIn("create core association_shard_2", log)
        self.assertIn("would MERGEINDEXES", log)
        # single-writer + raw-json cores
        self.assertIn("loading entity: single writer", log)
        self.assertIn("loading infores from infores.jsonl", log)

    def test_single_shard_is_not_sharded(self):
        cfg = BuildConfig(
            dry_run=True,
            cores=[CoreSpec(name="c", source=SourceSpec(duckdb="x.duckdb", table="t"), shards=1)],
        )
        with self.assertLogs("linkml_solr.build", level="INFO") as cm:
            build(cfg)
        log = "\n".join(cm.output)
        self.assertIn("loading c: single writer", log)
        self.assertNotIn("MERGEINDEXES", log)


class TestMergeAndVerifyEdges(unittest.TestCase):
    """Solr-free coverage of the risky merge/verify paths (Solr calls stubbed)."""

    def test_merge_empty_core_returns_immediately(self):
        """expected==0 (empty sharded core) must return at once, not spin to timeout."""
        cfg = BuildConfig(merge_timeout=1)  # tiny: a hang would surface as slow/raise
        with mock.patch.object(build_mod.requests, "get"), \
             mock.patch.object(build_mod, "commit"), \
             mock.patch.object(build_mod, "numfound", return_value=0):
            merge_indexes(cfg, "target", ["s0", "s1"], expected=0)  # must not raise

    def test_merge_reaches_expected(self):
        cfg = BuildConfig(merge_timeout=5)
        with mock.patch.object(build_mod.requests, "get"), \
             mock.patch.object(build_mod, "commit"), \
             mock.patch.object(build_mod, "numfound", return_value=100):
            merge_indexes(cfg, "target", ["s0"], expected=100)  # 100 >= 100 -> return

    def test_expected_count_skips_non_duckdb_source(self):
        """A verify'd json_docs/sourceless core must not crash — returns None."""
        cfg = BuildConfig()
        json_core = CoreSpec(name="infores", source=SourceSpec(json_docs="x.jsonl"),
                             verify={"table": "t", "id_field": "id"})
        self.assertIsNone(_expected_count(cfg, json_core))
        sourceless = CoreSpec(name="x", verify={"table": "t"})
        self.assertIsNone(_expected_count(cfg, sourceless))


if __name__ == "__main__":
    unittest.main()
