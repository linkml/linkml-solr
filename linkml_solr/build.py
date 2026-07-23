"""Runtime-agnostic, config-driven Solr index builder for LinkML-Solr.

``lsolr build --config build.yaml`` stands up Solr (Docker or Apptainer), creates
and schemas each core, loads it from DuckDB (single-writer or sharded), verifies
doc counts, and optionally tars the index — the whole build behind one command so
it runs identically on a laptop, a cloud VM, or a container-less HPC node.

The three runtime-coupled pieces are abstracted behind :class:`SolrRuntime`:

  * **start Solr** — ``docker run`` or ``apptainer run`` (bind a host solr-home);
  * **create cores** — the HTTP Cores API (works under either runtime), after the
    image's ``_default`` configset is copied into SOLR_HOME (which starts empty);
  * **tar the index** — a Docker ``--volumes-from`` sidecar or a plain ``tar`` of
    the Apptainer bind dir.

Per-core loading goes through :func:`load_core`, which either streams the whole
table into one core or hash-partitions it across N shard cores loaded in parallel
and then ``MERGEINDEXES``-collapses them into the target — the way to parallelize
past a single Lucene IndexWriter's merge ceiling on many-core / fast-disk hardware.
On a single spindle sharding is I/O-bound and does not help; keep ``shards: 1``.

Config (YAML)::

    runtime: docker            # docker | apptainer | "" (auto)
    image: solr:8
    port: 8983
    heap: 10g
    memory: 12g
    ram_buffer_mb: 512
    skip_tarball: true
    cores:
      - name: association
        linkml_schema: monarch-kg-schema.yaml
        top_class: Association
        schema_json_pre:  [text-fieldtype.json]     # POSTed to <core>/schema before create-schema
        schema_json_post: [association-copyfields.json]  # POSTed after (copy/dynamic fields)
        disable_tlog: true
        shards: 1
        source: {duckdb: monarch-kg.duckdb, table: _solr_edges}
        verify: {table: _solr_edges, id_field: id}
      - name: infores
        source: {json_docs: infores_catalog.jsonl}  # POSTed straight to <core>/update/json/docs
"""
from __future__ import annotations

import json
import os
import shlex
import shutil
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

import duckdb
import requests
import yaml

from linkml_solr.utils.solr_bulkload import bulkload_duckdb

try:
    from linkml_solr.utils.log_utils import get_logger  # optional, if present
    logger = get_logger(__name__)
except Exception:  # pragma: no cover - fall back to stdlib logging
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)


# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
@dataclass
class SourceSpec:
    duckdb: Optional[str] = None       # path to a duckdb file
    table: Optional[str] = None        # table/view name (or a parenthesized subquery)
    where: Optional[str] = None
    columns: Optional[str] = None      # comma-separated; default all
    json_docs: Optional[str] = None    # a json/jsonl file POSTed straight to update/json/docs


@dataclass
class CoreSpec:
    name: str
    linkml_schema: Optional[str] = None
    top_class: Optional[str] = None
    schema_json_pre: List[str] = field(default_factory=list)
    schema_json_post: List[str] = field(default_factory=list)
    disable_tlog: bool = True
    shards: int = 1
    source: Optional[SourceSpec] = None
    verify: Optional[dict] = None      # {table, id_field}


@dataclass
class BuildConfig:
    cores: List[CoreSpec] = field(default_factory=list)

    runtime: str = ""                  # docker | apptainer | "" (auto)
    image: str = "solr:8"
    sif: Optional[str] = None
    container: str = "my_solr"
    solrhome: str = ".solrhome"        # host dir bound to /var/solr under apptainer

    host: str = "localhost"
    port: int = 8983
    memory: str = "12g"                # docker -m
    heap: str = "10g"                  # JVM -Xms/-Xmx
    ram_buffer_mb: int = 512

    # loader tunables
    upload_workers: int = 4
    chunk_size: int = 20000
    duckdb_memory_limit: str = "4GB"   # per shard reader
    merge_threads: int = 2
    merge_timeout: int = 7200

    skip_tarball: bool = False
    tarball: str = "solr.tar.gz"
    dry_run: bool = False

    @property
    def base_url(self) -> str:
        return f"http://{self.host}:{self.port}/solr"

    @classmethod
    def from_yaml(cls, path: str) -> "BuildConfig":
        with open(path) as fh:
            raw = yaml.safe_load(fh) or {}
        cores = []
        for c in raw.pop("cores", []) or []:
            name = c.get("name", "?")
            src = c.pop("source", None)
            try:
                cores.append(CoreSpec(source=SourceSpec(**src) if src else None, **c))
            except TypeError as e:
                raise ValueError(f"invalid config for core '{name}': {e}") from e
        try:
            return cls(cores=cores, **raw)
        except TypeError as e:
            raise ValueError(f"invalid top-level build config: {e}") from e


# --------------------------------------------------------------------------- #
# Runtime abstraction
# --------------------------------------------------------------------------- #
def detect_runtime(preference: str = "", *, check: bool = True) -> str:
    choice = preference or os.environ.get("LINKML_SOLR_RUNTIME", "")
    if choice:
        if check and not shutil.which(choice):
            raise RuntimeError(f"requested solr runtime '{choice}' is not on PATH")
        return choice
    for candidate in ("docker", "apptainer"):
        if shutil.which(candidate):
            return candidate
    if not check:
        return "docker"
    raise RuntimeError("no container runtime found — need `docker` or `apptainer` on PATH")


def _run(cmd: list, *, dry_run: bool, **kwargs):
    logger.info("$ " + " ".join(str(c) for c in cmd))
    if dry_run:
        return None
    kwargs.setdefault("check", True)
    return subprocess.run([str(c) for c in cmd], **kwargs)


class SolrRuntime:
    """Start/stop Solr and tar its index over either docker or apptainer."""

    def __init__(self, cfg: BuildConfig):
        self.cfg = cfg
        self.kind = detect_runtime(cfg.runtime, check=not cfg.dry_run)
        self._proc = None
        self._log = None  # apptainer: file handle for the backgrounded process's output
        logger.info(f"solr runtime: {self.kind}")

    def start(self) -> None:
        cfg = self.cfg
        env_solr = {
            "SOLR_PORT": str(cfg.port),
            "SOLR_JAVA_MEM": f"-Xms{cfg.heap} -Xmx{cfg.heap}",
            "SOLR_OPTS": f"-Dsolr.ramBufferSizeMB={cfg.ram_buffer_mb} -Dsolr.jetty.request.header.size=65535",
        }
        if self.kind == "docker":
            _run(["docker", "rm", "-f", cfg.container], dry_run=cfg.dry_run, check=False)
            cmd = ["docker", "run", "-d", "--name", cfg.container, "-p", f"{cfg.port}:{cfg.port}", "-m", cfg.memory]
            for k, v in env_solr.items():
                cmd += ["-e", f"{k}={v}"]
            cmd += [cfg.image, "solr-foreground"]
            _run(cmd, dry_run=cfg.dry_run)
        else:  # apptainer
            sif = self._ensure_sif()
            if not cfg.dry_run:
                shutil.rmtree(cfg.solrhome, ignore_errors=True)
                Path(cfg.solrhome).mkdir(parents=True, exist_ok=True)
            env = os.environ.copy()
            for k, v in env_solr.items():
                env[f"APPTAINERENV_{k}"] = v
            cmd = ["apptainer", "run", "--writable-tmpfs", "--bind", f"{cfg.solrhome}:/var/solr",
                   str(sif), "solr-foreground"]
            logger.info("$ " + " ".join(cmd) + " (backgrounded)")
            if not cfg.dry_run:
                self._log = open(Path(cfg.solrhome) / "solr.out", "wb")
                self._proc = subprocess.Popen(cmd, stdout=self._log, stderr=self._log, env=env)

    def _ensure_sif(self) -> Path:
        cfg = self.cfg
        sif = Path(cfg.sif) if cfg.sif else Path(".solr8.sif")
        if not sif.exists():
            _run(["apptainer", "pull", str(sif), f"docker://{cfg.image}"], dry_run=cfg.dry_run)
        return sif

    def _exec_sh(self, script: str) -> None:
        """Run a bash snippet against Solr's filesystem (SOLR_HOME at /var/solr)."""
        cfg = self.cfg
        if self.kind == "docker":
            subprocess.run(["docker", "exec", cfg.container, "bash", "-c", script], check=True)
        else:
            sif = self._ensure_sif()
            subprocess.run(["apptainer", "exec", "--bind", f"{cfg.solrhome}:/var/solr", str(sif),
                            "bash", "-c", script], check=True)

    def install_default_configset(self) -> None:
        """Copy the image's ``_default`` configset into SOLR_HOME (empty at start).

        Standalone Solr's Cores API ``CREATE?configSet=...`` looks under SOLR_HOME
        (/var/solr/data/configsets); the configset only ships in the install dir
        (/opt/solr/server/solr/configsets). Copy it in once as the base every
        per-core configset is cloned from.
        """
        if self.cfg.dry_run:
            logger.info("[dry-run] would install _default configset into SOLR_HOME")
            return
        self._exec_sh("mkdir -p /var/solr/data/configsets && "
                      "cp -rn /opt/solr/server/solr/configsets/_default /var/solr/data/configsets/_default")

    def clone_configset(self, name: str) -> None:
        """Clone the base ``_default`` configset to a per-core configset ``name``.

        Cores that *share* a configset also share its managed-schema, so a
        field-type/copy-field added to one core leaks into every other core on
        that configset (and re-adding it then 400s). Each core gets its own
        clone so schema edits stay isolated — the per-core copy ``solr create``
        does, done over the runtime instead.
        """
        if self.cfg.dry_run:
            logger.info(f"[dry-run] would clone configset _default -> {name}")
            return
        self._exec_sh(f"cp -rT /var/solr/data/configsets/_default /var/solr/data/configsets/{name}")

    def stop(self) -> None:
        if self.kind == "docker":
            _run(["docker", "stop", self.cfg.container], dry_run=self.cfg.dry_run, check=False)
        elif self._proc is not None:
            self._proc.terminate()
            try:
                self._proc.wait(timeout=30)
            except subprocess.TimeoutExpired:
                self._proc.kill()
        if self._log is not None:
            self._log.close()
            self._log = None

    def tar_index(self, dest: Path) -> None:
        cfg = self.cfg
        dest.parent.mkdir(parents=True, exist_ok=True)
        gz = "pigz" if shutil.which("pigz") else "gzip"
        if self.kind == "docker":
            src = f"docker run --rm --volumes-from {shlex.quote(cfg.container)} busybox tar cf - -C /var/solr data"
        else:
            src = f"tar cf - -C {shlex.quote(str(cfg.solrhome))} data"
        cmd = f"{src} | {gz} > {shlex.quote(str(dest))}"
        logger.info(f"$ {cmd}")
        if not cfg.dry_run:
            subprocess.run(cmd, shell=True, check=True)
        if self.kind == "docker":
            _run(["docker", "rm", cfg.container], dry_run=cfg.dry_run, check=False)

    def wait_ready(self, timeout: int = 180) -> None:
        if self.cfg.dry_run:
            logger.info(f"[dry-run] skipping wait for {self.cfg.base_url}")
            return
        url = f"{self.cfg.base_url}/admin/info/system"
        deadline = time.time() + timeout
        while time.time() < deadline:
            try:
                if requests.get(url, timeout=5).ok:
                    logger.info(f"Solr is ready at {self.cfg.base_url}")
                    return
            except requests.RequestException:
                pass
            time.sleep(5)
        raise RuntimeError(f"Solr did not become ready within {timeout}s")


# --------------------------------------------------------------------------- #
# HTTP helpers (runtime-agnostic)
# --------------------------------------------------------------------------- #
def _lsolr() -> str:
    cand = Path(sys.executable).parent / "lsolr"
    return str(cand) if cand.exists() else "lsolr"


def create_core(cfg: BuildConfig, core: str, configset: str = "_default") -> None:
    logger.info(f"create core {core} (configset {configset})")
    if cfg.dry_run:
        return
    r = requests.get(f"{cfg.base_url}/admin/cores",
                     params={"action": "CREATE", "name": core, "configSet": configset}, timeout=60)
    if not r.ok and "already exists" not in r.text:
        r.raise_for_status()


_COPYFIELD_SOURCE_MISSING = "doesn't match any explicit field or dynamicField"


def post_schema_json(cfg: BuildConfig, core: str, json_files: List[str]) -> None:
    """Apply Schema-API JSON files to ``core``, one command at a time.

    Each file is a Schema-API body: a mapping of command -> definition (or a list
    of definitions). Commands are POSTed individually and in order, so a single
    bad command doesn't roll back the whole file. One benign case is tolerated
    with a warning: an ``add-copy-field`` whose source field isn't in this core's
    schema (copy-field lists commonly over-specify across related cores). Every
    other failure raises.
    """
    for f in json_files:
        logger.info(f"  apply {f} -> {core}/schema")
        if cfg.dry_run:
            continue
        text = Path(f).read_text()
        try:
            doc = json.loads(text)
        except json.JSONDecodeError:
            # Solr's Noggit parser is lenient (e.g. trailing commas) where strict
            # json is not. Such a body can't be split per-command, so POST it whole
            # and require success.
            r = requests.post(f"{cfg.base_url}/{core}/schema", data=text.encode(),
                              headers={"Content-Type": "application/json"}, timeout=120)
            if not r.ok:
                raise RuntimeError(f"POST {f} to {core}/schema failed: {r.status_code} {r.text[:300]}")
            continue
        for command, payload in doc.items():
            for item in (payload if isinstance(payload, list) else [payload]):
                r = requests.post(f"{cfg.base_url}/{core}/schema", json={command: item},
                                  headers={"Content-Type": "application/json"}, timeout=120)
                if r.ok:
                    continue
                if command == "add-copy-field" and _COPYFIELD_SOURCE_MISSING in r.text:
                    logger.warning(f"  skip copy-field {item.get('source')} -> "
                                   f"{item.get('dest')}: source not in {core} schema")
                    continue
                raise RuntimeError(f"{command} {item} on {core}/schema failed: {r.status_code} {r.text[:300]}")


def create_linkml_schema(cfg: BuildConfig, core: str, top_class: str, schema: str) -> None:
    _run([_lsolr(), "create-schema", "-C", core, "-s", str(schema), "-u", cfg.base_url, "-t", top_class],
         dry_run=cfg.dry_run)


def disable_tlog_and_reload(cfg: BuildConfig, core: str) -> None:
    if cfg.dry_run:
        return
    requests.post(f"{cfg.base_url}/{core}/config",
                  json={"set-property": {"updateLog.numRecordsToKeep": 0}}, timeout=60)
    requests.get(f"{cfg.base_url}/admin/cores", params={"action": "RELOAD", "core": core}, timeout=180)


def commit(cfg: BuildConfig, core: str) -> None:
    if cfg.dry_run:
        return
    requests.get(f"{cfg.base_url}/{core}/update",
                 params={"commit": "true", "waitSearcher": "true"}, timeout=600)


def unload_core(cfg: BuildConfig, core: str) -> None:
    if cfg.dry_run:
        return
    requests.get(f"{cfg.base_url}/admin/cores",
                 params={"action": "UNLOAD", "core": core, "deleteIndex": "true",
                         "deleteDataDir": "true", "deleteInstanceDir": "true"}, timeout=180)


def numfound(cfg: BuildConfig, core: str) -> int:
    r = requests.get(f"{cfg.base_url}/{core}/select", params={"q": "*:*", "rows": 0}, timeout=120)
    return r.json()["response"]["numFound"]


# --------------------------------------------------------------------------- #
# Loading (single-writer or sharded) + merge
# --------------------------------------------------------------------------- #
def _shard_worker(a: tuple) -> tuple:
    """Load one (optionally hash-partitioned) slice into ``core``. Picklable.

    Streams directly from the read-only duckdb (no snapshot), memory-capped, and
    commits the core at the end. Returns (core, docs, seconds).
    """
    db_path, base_url, core, table, where, mem, chunk, workers = a
    t0 = time.time()
    loaded = bulkload_duckdb(
        db_path=db_path, table_name=table, base_url=base_url, core=core, schema=None,
        chunk_size=chunk, max_workers=workers, where_clause=where,
        snapshot=False, drop_nulls=True, memory_limit=mem,
    )
    requests.get(f"{base_url}/{core}/update", params={"commit": "true", "waitSearcher": "true"}, timeout=600)
    return core, loaded, round(time.time() - t0, 1)


def merge_indexes(cfg: BuildConfig, target: str, sources: List[str], expected: Optional[int] = None) -> None:
    """MERGEINDEXES the source cores into ``target`` (segment copy, no re-analysis).

    A large merge runs server-side on the Lucene writer and can outlive the HTTP
    request (Jetty may close a long-blocked request that sends no bytes), so fire
    the request, tolerate a disconnect, and *poll* the target count until it lands
    — never blindly retry the merge (addIndexes is not idempotent; it duplicates
    ids). The poll calls are themselves wrapped: a transient reset while Solr is
    busy merging must not abort the build.
    """
    if cfg.dry_run:
        logger.info(f"[dry-run] would MERGEINDEXES {sources} -> {target}")
        return
    src = "".join(f"&srcCore={s}" for s in sources)
    url = f"{cfg.base_url}/admin/cores?action=mergeindexes&core={target}{src}"
    logger.info(f"MERGEINDEXES {len(sources)} shards -> {target} (polling for completion)")
    try:
        requests.get(url, timeout=(30, cfg.merge_timeout))
    except requests.exceptions.RequestException as e:
        logger.warning(f"mergeindexes connection dropped ({e}); merge continues server-side, polling")

    deadline = time.time() + cfg.merge_timeout
    got = last = -1  # `got` must be bound even if every poll raises (else the timeout msg NameErrors)
    while time.time() < deadline:
        try:
            commit(cfg, target)
            got = numfound(cfg, target)
        except requests.exceptions.RequestException as e:
            # Solr is busy with the merge (or briefly unreachable). Do NOT abort —
            # that was the bug that turned a survivable disconnect into a failure.
            logger.warning(f"poll failed while merge in progress ({e}); retrying")
            time.sleep(30)
            continue
        logger.info(f"  merged {got:,}" + (f"/{expected:,}" if expected is not None else ""))
        if expected is not None and got >= expected:
            return  # includes expected == 0 (empty core): done immediately, no hang
        # Fallback when the caller can't supply an expected count: stop once two
        # consecutive polls agree AND the merge request has returned. `load_core`
        # always passes an expected, so this branch is only for direct callers.
        if expected is None and got == last:
            return
        last = got
        time.sleep(30)
    raise RuntimeError(f"MERGEINDEXES did not complete within {cfg.merge_timeout}s (target has {got})")


def load_core(cfg: BuildConfig, spec: CoreSpec, runtime: "SolrRuntime") -> None:
    """Load one core from its source: single-writer, sharded+merge, or raw json docs."""
    src = spec.source
    if src is None:
        return
    if src.json_docs:
        logger.info(f"loading {spec.name} from {src.json_docs}")
        if not cfg.dry_run:
            r = requests.post(f"{cfg.base_url}/{spec.name}/update/json/docs", params={"commit": "true"},
                              data=Path(src.json_docs).read_bytes(),
                              headers={"Content-Type": "application/json"}, timeout=300)
            r.raise_for_status()
        return

    n = max(1, spec.shards)
    if n == 1:
        logger.info(f"loading {spec.name}: single writer")
        if cfg.dry_run:
            return
        core, loaded, secs = _shard_worker(
            (src.duckdb, cfg.base_url, spec.name, src.table, src.where,
             cfg.duckdb_memory_limit, cfg.chunk_size, cfg.upload_workers))
        logger.info(f"  {core}: {loaded:,} docs in {secs}s")
        return

    # sharded: N shard cores loaded in parallel, then MERGEINDEXES -> target.
    shards = [f"{spec.name}_shard_{j}" for j in range(n)]
    logger.info(f"loading {spec.name}: {n} shards + MERGEINDEXES")
    for shard in shards:
        _setup_core_schema(cfg, CoreSpec(name=shard, linkml_schema=spec.linkml_schema,
                                         top_class=spec.top_class, schema_json_pre=spec.schema_json_pre,
                                         schema_json_post=spec.schema_json_post, disable_tlog=spec.disable_tlog),
                           runtime)
    if cfg.dry_run:
        logger.info(f"[dry-run] would parallel-load {n} shards of {spec.name}")
        merge_indexes(cfg, spec.name, shards, expected=None)
        for shard in shards:
            unload_core(cfg, shard)
        return

    base_where = f"({src.where}) AND " if src.where else ""
    # Partition by hash(id). hash(NULL) is NULL and matches no shard, so route
    # null-id rows to shard 0 — otherwise they'd be silently dropped from every
    # shard (the single-writer path keeps them, so the two paths must agree).
    args = [(src.duckdb, cfg.base_url, shard, src.table,
             f"{base_where}(hash(id) % {n} = {j}" + (f" OR id IS NULL)" if j == 0 else ")"),
             cfg.duckdb_memory_limit, cfg.chunk_size, cfg.upload_workers)
            for j, shard in enumerate(shards)]
    with ProcessPoolExecutor(max_workers=n) as ex:
        for core, loaded, secs in sorted(ex.map(_shard_worker, args)):
            logger.info(f"  {core}: {loaded:,} docs in {secs}s")

    # Always give the merge a concrete target count (distinct ids across the whole
    # source slice) so an empty or no-`verify` sharded core doesn't spin to the
    # merge timeout, and a paused merge can't be mistaken for a finished one.
    expected = _shard_source_count(src.duckdb, src.table, src.where)
    merge_indexes(cfg, spec.name, shards, expected=expected)
    for shard in shards:
        unload_core(cfg, shard)


def _shard_source_count(duckdb_path: str, table: str, where: Optional[str]) -> int:
    con = duckdb.connect(duckdb_path, read_only=True)
    try:
        w = f" WHERE {where}" if where else ""
        return con.execute(f"SELECT count(DISTINCT id) FROM {table}{w}").fetchone()[0]
    finally:
        con.close()


def _expected_count(cfg: BuildConfig, spec: CoreSpec) -> Optional[int]:
    if cfg.dry_run or not spec.verify:
        return None
    if not spec.source or not spec.source.duckdb:
        # verify counts distinct ids in a duckdb table; a json_docs (or sourceless)
        # core has no such table, so there's nothing to count against.
        logger.warning(f"  {spec.name}: verify set but source is not a duckdb table; skipping count check")
        return None
    con = duckdb.connect(spec.source.duckdb, read_only=True)
    try:
        idf = spec.verify.get("id_field", "id")
        return con.execute(f"SELECT count(DISTINCT {idf}) FROM {spec.verify['table']}").fetchone()[0]
    finally:
        con.close()


# --------------------------------------------------------------------------- #
# Orchestration
# --------------------------------------------------------------------------- #
def _setup_core_schema(cfg: BuildConfig, spec: CoreSpec, runtime: "SolrRuntime") -> None:
    # Each core gets its own configset clone so schema edits don't leak across cores.
    configset = f"{spec.name}_cs"
    runtime.clone_configset(configset)
    create_core(cfg, spec.name, configset)
    post_schema_json(cfg, spec.name, spec.schema_json_pre)
    if spec.linkml_schema and spec.top_class:
        create_linkml_schema(cfg, spec.name, spec.top_class, spec.linkml_schema)
    if spec.disable_tlog:
        disable_tlog_and_reload(cfg, spec.name)
    post_schema_json(cfg, spec.name, spec.schema_json_post)


def verify_counts(cfg: BuildConfig) -> None:
    if cfg.dry_run:
        logger.info("[dry-run] skipping doc-count verification")
        return
    failures = []
    for spec in cfg.cores:
        if not spec.verify:
            continue
        expected = _expected_count(cfg, spec)
        if expected is None:  # not countable (e.g. non-duckdb source); already warned
            continue
        got = numfound(cfg, spec.name)
        status = "OK" if got == expected else "MISMATCH"
        logger.info(f"  {spec.name}: numDocs={got:,} expected={expected:,} ({status})")
        if got != expected:
            failures.append(f"{spec.name}: {got} != {expected} ({spec.verify['table']})")
    if failures:
        raise RuntimeError("Solr load incomplete:\n  - " + "\n  - ".join(failures))


def build(cfg: BuildConfig) -> None:
    """Build all cores per ``cfg``: start Solr, create+schema+load each, verify, tar."""
    runtime = SolrRuntime(cfg)
    runtime.start()
    try:
        runtime.wait_ready()
        runtime.install_default_configset()

        # set up every non-shard core's schema first (shards are set up inside load_core)
        for spec in cfg.cores:
            _setup_core_schema(cfg, spec, runtime)

        for spec in cfg.cores:
            load_core(cfg, spec, runtime)

        for spec in cfg.cores:
            commit(cfg, spec.name)

        logger.info("verifying core doc counts against source tables")
        verify_counts(cfg)
    except Exception:
        # Don't leave an orphan Solr container/process on a failed build.
        logger.error("build failed — stopping Solr")
        runtime.stop()
        raise

    if cfg.skip_tarball:
        logger.info(f"skip_tarball set — leaving Solr running, not producing {cfg.tarball}")
        return
    logger.info("committing + stopping Solr, then tarring the index")
    runtime.stop()
    time.sleep(3)
    runtime.tar_index(Path(cfg.tarball))
    logger.info(f"wrote {cfg.tarball}")
