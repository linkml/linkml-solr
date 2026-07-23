# -*- coding: utf-8 -*-
"""Docker-backed integration tests for ``lsolr build``.

Spins up its own Solr container (distinct name/port so it never touches a Solr a
developer already has running) and exercises both load paths end-to-end against
the repo's ``books`` model: single-writer, and sharded + MERGEINDEXES. Skipped
automatically when Docker is unavailable.
"""
import os
import shutil
import tempfile
import unittest

import duckdb
import requests

from linkml_solr.build import BuildConfig, CoreSpec, SourceSpec, SolrRuntime, build, numfound
from tests import INPUT_DIR, MODEL_DIR

CONTAINER = "lsolr_build_test"
PORT = 8985  # off the default 8983 so we don't clobber a dev Solr
BOOKS_TSV = os.path.join(INPUT_DIR, "books.tsv")
BOOKS_SCHEMA = os.path.join(MODEL_DIR, "books.yaml")
# A custom field type + copy fields (incl. one with a missing source) so the
# build exercises per-core configset isolation and copy-field tolerance across
# every core it creates (target + shards).
FIELDTYPE_JSON = os.path.join(INPUT_DIR, "books_fieldtype.json")
COPYFIELDS_JSON = os.path.join(INPUT_DIR, "books_copyfields.json")


@unittest.skipIf(shutil.which("docker") is None, "docker not available")
class TestBuildIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(prefix="lsolr_build_test_")
        cls.duckdb = os.path.join(cls.tmp, "books.duckdb")
        con = duckdb.connect(cls.duckdb)
        con.execute(
            f"CREATE TABLE books AS SELECT * FROM "
            f"read_csv_auto('{BOOKS_TSV}', delim='\t', header=true, all_varchar=true)"
        )
        cls.nrows = con.execute("SELECT count(DISTINCT id) FROM books").fetchone()[0]
        con.close()

    @classmethod
    def tearDownClass(cls):
        import subprocess
        subprocess.run(["docker", "rm", "-f", CONTAINER], capture_output=True)
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def _base_cfg(self, **kw) -> BuildConfig:
        return BuildConfig(
            runtime="docker", container=CONTAINER, port=PORT,
            heap="2g", memory="3g", skip_tarball=True,
            cores=[CoreSpec(
                name="books", linkml_schema=BOOKS_SCHEMA, top_class="book",
                schema_json_pre=[FIELDTYPE_JSON], schema_json_post=[COPYFIELDS_JSON],
                source=SourceSpec(duckdb=self.duckdb, table="books"),
                verify={"table": "books", "id_field": "id"}, **kw,
            )],
        )

    def _teardown_solr(self, cfg):
        SolrRuntime(cfg).stop()
        import subprocess
        subprocess.run(["docker", "rm", "-f", CONTAINER], capture_output=True)

    def test_single_writer_build(self):
        cfg = self._base_cfg()
        try:
            build(cfg)
            self.assertEqual(numfound(cfg, "books"), self.nrows)
        finally:
            self._teardown_solr(cfg)

    def test_sharded_build_and_merge(self):
        cfg = self._base_cfg(shards=2)
        try:
            build(cfg)
            # merged target holds every row exactly once...
            self.assertEqual(numfound(cfg, "books"), self.nrows)
            # ...and the intermediate shard cores were unloaded.
            for shard in ("books_shard_0", "books_shard_1"):
                r = requests.get(f"{cfg.base_url}/{shard}/select", params={"q": "*:*"})
                self.assertNotEqual(r.status_code, 200, f"{shard} should have been unloaded")
        finally:
            self._teardown_solr(cfg)


if __name__ == "__main__":
    unittest.main()
