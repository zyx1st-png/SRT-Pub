"""Synthetic-only, bounded multi-task G0 execution path.

This module exercises the registered 4E connected degree-preserving proposal
kernel, 200 seeded python-louvain trials, complete hash-chained proposal audit,
and G0ExternalStore/Watchdog integration on explicitly synthetic graphs. A
single activity freezes its task/seed inventory and schedules tasks serially;
each Louvain pool is capped at four workers. It is not a biological G0
launcher and rejects inputs outside the synthetic scope.
"""

from __future__ import annotations

from concurrent.futures import FIRST_COMPLETED, ProcessPoolExecutor, wait
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures.process import BrokenProcessPool
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass
import gzip
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path
import platform
import random
import resource
import sys
import time
import traceback
import uuid
import zlib

from connected_swap import ConnectedDegreeSwap
from g0_external_storage import G0ExternalStore, G0StorageError, RecoveryRefused
from nc0a_watchdog import WatchdogLimits


PREREG_ROOT_SEED = 20261009
PROPOSALS_PER_EDGE = 4
LOUVAIN_TRIALS = 200
SYNTHETIC_SCOPE = "SYNTHETIC_ENGINEERING_ONLY"
TARGET_MACOS_VERSION = "15.7.4"
_HEX64 = frozenset("0123456789abcdef")
_LOUVAIN_GRAPH = None
_LOUVAIN_LABELS: tuple[str | int, ...] = ()
_LOUVAIN_TEST_FAULT: str | None = None
_SYNTHETIC_TEST_FAULTS = frozenset({
    "scientific_failure", "unknown_failure", "worker_scientific_failure",
    "worker_operational_failure", "worker_abrupt_exit",
})


class G0ScientificFailure(RuntimeError):
    """A confirmed protocol, identity, graph or numerical integrity failure."""

    def __init__(self, reason_code: str, message: str):
        super().__init__(message)
        self.reason_code = reason_code

    def __reduce__(self):
        # ProcessPoolExecutor serializes worker exceptions back to the runner.
        return (type(self), (self.reason_code, str(self)))


class G0OperationalFailure(RuntimeError):
    """A known process-level failure; unknown errors are never mapped here."""

    def __init__(self, reason_code: str, message: str):
        super().__init__(message)
        self.reason_code = reason_code

    def __reduce__(self):
        return (type(self), (self.reason_code, str(self)))


class G0UnknownFailure(RuntimeError):
    """Unclassified failures; persisted fail-closed and never auto-retried."""

    def __init__(self, reason_code: str, message: str):
        super().__init__(message)
        self.reason_code = reason_code

    def __reduce__(self):
        return (type(self), (self.reason_code, str(self)))


def canonical_json(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _is_sha256(value: object) -> bool:
    return (isinstance(value, str) and len(value) == 64 and
            set(value) <= _HEX64)


def _node_key(value: object) -> tuple[str, object]:
    # bool is an int subclass but is not a valid graph label in this contract.
    if type(value) is int:
        return ("int", value)
    if isinstance(value, str) and value:
        return ("str", value)
    raise ValueError("Node labels must be nonempty strings or ordinary integers")


def _node_record(value: str | int) -> dict[str, object]:
    return {"type": "int", "value": value} if type(value) is int else {
        "type": "str", "value": value}


@dataclass(frozen=True)
class NormalizedGraph:
    """Canonical labeled graph payload; node order remains part of identity."""

    source_id: str
    nodes: tuple[str | int, ...]
    edges: tuple[tuple[int, int], ...]
    graph_sha256: str
    source_artifact_sha256: str | None

    @property
    def n(self) -> int:
        return len(self.nodes)

    @property
    def m(self) -> int:
        return len(self.edges)

    @property
    def degree_sequence(self) -> tuple[int, ...]:
        degrees = [0] * self.n
        for u, v in self.edges:
            degrees[u] += 1
            degrees[v] += 1
        return tuple(degrees)

    def payload(self) -> dict[str, object]:
        return {"format": "G0_NORMALIZED_GRAPH_V1", "source_id": self.source_id,
                "nodes": [_node_record(node) for node in self.nodes],
                "edges": [list(edge) for edge in self.edges],
                "graph_sha256": self.graph_sha256,
                "source_artifact_sha256": self.source_artifact_sha256}


def normalize_graph_input(source_id: str, nodes, edges, *,
                          source_artifact_sha256: str | None = None) -> NormalizedGraph:
    """Validate and hash the exact node order and canonical labeled edge set.

    This is a graph identity interface, not the historical signal/correlation
    reconstruction. External node identifiers are retained in order and
    edges are normalized to their zero-based canonical positions.
    """
    if (not isinstance(source_id, str) or not source_id or len(source_id) > 120 or
            "/" in source_id or "\\" in source_id or ".." in source_id):
        raise ValueError("source_id is malformed")
    if source_artifact_sha256 is not None and not _is_sha256(source_artifact_sha256):
        raise ValueError("source_artifact_sha256 must be SHA-256 hex")
    node_list = tuple(nodes)
    if len(node_list) < 4:
        raise ValueError("G0 input graphs require at least four nodes")
    positions: dict[tuple[str, object], int] = {}
    for index, node in enumerate(node_list):
        key = _node_key(node)
        if key in positions:
            raise ValueError("Duplicate node label")
        positions[key] = index
    normalized: set[tuple[int, int]] = set()
    for edge in edges:
        if not isinstance(edge, (tuple, list)) or len(edge) != 2:
            raise ValueError("Every edge must contain exactly two labels")
        left, right = _node_key(edge[0]), _node_key(edge[1])
        if left not in positions or right not in positions:
            raise ValueError("Edge references a node outside the declared identity map")
        u, v = positions[left], positions[right]
        if u == v:
            raise ValueError("Self-loops are prohibited")
        pair = (u, v) if u < v else (v, u)
        if pair in normalized:
            raise ValueError("Duplicate or reversed duplicate edge")
        normalized.add(pair)
    edge_list = tuple(sorted(normalized))
    try:
        ConnectedDegreeSwap(len(node_list), edge_list)
    except (ValueError, AssertionError) as exc:
        raise ValueError(f"Input graph is not a valid connected simple graph: {exc}") from exc
    identity = {"format": "G0_NORMALIZED_GRAPH_V1", "source_id": source_id,
                "nodes": [_node_record(node) for node in node_list],
                "edges": [list(edge) for edge in edge_list],
                "source_artifact_sha256": source_artifact_sha256}
    return NormalizedGraph(source_id, node_list, edge_list,
                           sha256_bytes(canonical_json(identity)),
                           source_artifact_sha256)


@dataclass(frozen=True)
class G0TaskIdentity:
    """Preregistered source/window coordinates for one null replicate."""

    recording_id: str
    n: int
    repeat_id: int
    state: str
    window_id: int
    null_repeat: int

    def validate(self, graph: NormalizedGraph) -> None:
        if (not isinstance(self.recording_id, str) or not self.recording_id or
                type(self.n) is not int or self.n != graph.n or
                type(self.repeat_id) is not int or self.repeat_id < 0 or
                not isinstance(self.state, str) or not self.state or
                type(self.window_id) is not int or self.window_id < 0 or
                type(self.null_repeat) is not int or not 0 <= self.null_repeat <= 9):
            raise ValueError("G0 task coordinates do not match the normalized graph")

    def as_dict(self) -> dict[str, object]:
        return {"recording_id": self.recording_id, "N": self.n,
                "repeat_id": self.repeat_id, "state": self.state,
                "window_id": self.window_id, "null_repeat": self.null_repeat}


def preregistered_stable_seed(root: int, *parts: object) -> int:
    """Match Phase-2 stable_seed: BLAKE2b-64 little-endian then mod 2^31-1."""
    payload = "|".join([str(root), *(str(part) for part in parts)]).encode("utf-8")
    value = int.from_bytes(hashlib.blake2b(payload, digest_size=8).digest(), "little")
    return int(value % (2**31 - 1)) or 1


def g0_graph_seed(identity: G0TaskIdentity) -> int:
    return preregistered_stable_seed(
        PREREG_ROOT_SEED, "NC_G0_GRAPH_V1", identity.recording_id,
        f"N{identity.n}", identity.repeat_id, identity.state,
        identity.window_id, identity.null_repeat)


def g0_louvain_seed(identity: G0TaskIdentity, louvain_repeat: int) -> int:
    if type(louvain_repeat) is not int or not 0 <= louvain_repeat < LOUVAIN_TRIALS:
        raise ValueError("louvain_repeat must be in 0..199")
    return preregistered_stable_seed(
        PREREG_ROOT_SEED, "NC_G0_LOUVAIN_V1", identity.recording_id,
        f"N{identity.n}", identity.repeat_id, identity.state,
        identity.window_id, identity.null_repeat, louvain_repeat)


def runtime_manifest(*, require_target: bool = False) -> dict[str, object]:
    lock_path = Path(__file__).with_name("g0-runtime-macos-arm64.lock")
    lock_bytes = lock_path.read_bytes()
    expected = {"h5py": "3.16.0", "networkx": "3.6.1", "numpy": "2.5.3",
                "python-louvain": "0.16", "scipy": "1.18.1"}
    actual = {}
    for name in expected:
        try:
            actual[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            actual[name] = None
    python = platform.python_version()
    machine = platform.machine()
    macos_version = platform.mac_ver()[0] or None
    if require_target and actual != expected:
        raise RuntimeError(f"G0 dependency lock mismatch: expected={expected}, actual={actual}")
    if require_target and (python != "3.14.0" or sys.platform != "darwin" or machine != "arm64"):
        raise RuntimeError("Target G0 engineering runtime requires Python 3.14.0 on macOS arm64")
    if require_target and macos_version != TARGET_MACOS_VERSION:
        raise RuntimeError(f"Target G0 engineering runtime requires macOS {TARGET_MACOS_VERSION}")
    source_hashes = {}
    for name in ("g0_minimal_executor.py", "connected_swap.py", "g0_external_storage.py",
                 "nc0a_watchdog.py", "nc0a_execution_engine.py"):
        source_hashes[name] = sha256_bytes(Path(__file__).with_name(name).read_bytes())
    return {"python": python, "executable": sys.executable,
            "platform": sys.platform, "machine": machine,
            "macos_version": macos_version,
            "packages": actual, "locked_packages": expected,
            "runtime_lock_sha256": sha256_bytes(lock_bytes),
            "source_sha256": source_hashes}


def _partition_encoding(labels: tuple[str | int, ...], partition: dict) -> list[int]:
    groups: dict[object, list[int]] = {}
    for index, label in enumerate(labels):
        groups.setdefault(partition[label], []).append(index)
    ordered_groups = sorted(groups.values(), key=lambda members: min(members))
    encoded = [0] * len(labels)
    for community_id, members in enumerate(ordered_groups):
        for index in members:
            encoded[index] = community_id
    return encoded


def _louvain_worker_init(n: int, labels: tuple[str | int, ...],
                         edges: tuple[tuple[int, int], ...],
                         test_fault: str | None) -> None:
    global _LOUVAIN_GRAPH, _LOUVAIN_LABELS, _LOUVAIN_TEST_FAULT
    import networkx as nx

    graph = nx.Graph()
    graph.add_nodes_from(labels)
    graph.add_weighted_edges_from(
        (labels[u], labels[v], 1.0) for u, v in edges)
    if graph.number_of_nodes() != n or not nx.is_connected(graph):
        raise G0ScientificFailure("G0_LOUVAIN_INPUT_GRAPH_INVALID",
                                  "Louvain worker received a nonconnected graph")
    _LOUVAIN_GRAPH = graph
    _LOUVAIN_LABELS = labels
    _LOUVAIN_TEST_FAULT = test_fault


def _louvain_trial(trial_index: int, seed: int) -> dict[str, object]:
    if _LOUVAIN_GRAPH is None:
        raise RuntimeError("Louvain worker graph was not initialized")
    if _LOUVAIN_TEST_FAULT == "worker_scientific_failure" and trial_index == 0:
        raise G0ScientificFailure("G0_INJECTED_WORKER_SCIENTIFIC_FAILURE",
                                  "Synthetic-only spawn scientific failure injection")
    if _LOUVAIN_TEST_FAULT == "worker_abrupt_exit" and trial_index == 0:
        # Test-only process death validates fail-closed classification across
        # the real spawn / BrokenProcessPool boundary.
        os._exit(73)
    if _LOUVAIN_TEST_FAULT == "worker_operational_failure" and trial_index == 0:
        raise G0OperationalFailure("G0_WORKER_PROCESS_EXIT",
                                   "Synthetic-only spawn operational failure injection")
    from community import community_louvain

    partition = community_louvain.best_partition(
        _LOUVAIN_GRAPH, weight="weight", resolution=1.0, random_state=seed)
    q_value = float(community_louvain.modularity(
        partition, _LOUVAIN_GRAPH, weight="weight"))
    if not math.isfinite(q_value):
        raise G0ScientificFailure("G0_LOUVAIN_Q_NONFINITE",
                                  f"Trial {trial_index} returned a nonfinite modularity")
    encoded_partition = _partition_encoding(_LOUVAIN_LABELS, partition)
    return {"trial_index": trial_index, "seed": seed, "modularity": q_value,
            "partition_sha256": sha256_bytes(canonical_json(encoded_partition)),
            "partition": encoded_partition,
            "community_count": max(encoded_partition, default=-1) + 1}


def _terminate_louvain_pool(pool: ProcessPoolExecutor,
                            processes: tuple[object, ...]) -> None:
    """Stop every sibling after one worker exits before pending work completes."""
    terminate_workers = getattr(pool, "terminate_workers", None)
    if callable(terminate_workers):
        # Python 3.14's public API closes the executor and joins its workers.
        terminate_workers()
        return
    # CI still exercises the fallback on Python 3.11. The process objects came
    # directly from this executor; terminating only that snapshot cannot reach
    # unrelated process-group members.
    for process in processes:
        try:
            if process.is_alive():
                process.terminate()
        except (OSError, ValueError):
            continue
    for process in processes:
        try:
            process.join(timeout=5)
        except (OSError, ValueError):
            continue
    pool.shutdown(wait=True, cancel_futures=True)


def _graph_metrics(labels: tuple[str | int, ...], edges: tuple[tuple[int, int], ...],
                   initial_edges: tuple[tuple[int, int], ...]) -> dict[str, object]:
    import networkx as nx

    graph = nx.Graph()
    graph.add_nodes_from(labels)
    graph.add_edges_from((labels[u], labels[v]) for u, v in edges)
    if not nx.is_connected(graph):
        raise G0ScientificFailure("G0_GRAPH_DISCONNECTED", "Final null graph is disconnected")
    try:
        assortativity = float(nx.degree_assortativity_coefficient(graph))
    except (ArithmeticError, ValueError, ZeroDivisionError):
        assortativity = math.nan
    if not math.isfinite(assortativity):
        raise G0ScientificFailure("G0_GRAPH_ASSORTATIVITY_INVALID",
                                  "Final graph degree assortativity is undefined")
    triangle_count = sum(nx.triangles(graph).values()) // 3
    overlap = len(set(edges).intersection(initial_edges)) / len(initial_edges)
    return {"node_count": graph.number_of_nodes(), "edge_count": graph.number_of_edges(),
            "component_count": nx.number_connected_components(graph),
            "triangle_count": triangle_count,
            "degree_assortativity": assortativity,
            "initial_edge_overlap": overlap,
            "degree_sequence": [degree for _, degree in graph.degree()],
            "degree_sequence_sha256": sha256_bytes(canonical_json(
                [degree for _, degree in graph.degree()]))}


def _hash_audit_record(sequence: int, previous: str,
                       event: dict[str, object]) -> dict[str, object]:
    body = {"sequence": sequence, "previous_sha256": previous, "event": event}
    digest = sha256_bytes(canonical_json(body))
    return {**body, "record_sha256": digest}


def _emit(tag: str, payload: dict[str, object]) -> None:
    sys.stdout.buffer.write(tag.encode("ascii") + b"\t" + canonical_json(payload) + b"\n")


def _write_phase(path: Path, task_id: str, phase: str) -> None:
    value = {"task_id": task_id, "phase": phase, "started_utc_epoch": time.time()}
    temporary = path.with_name(path.name + f".{os.getpid()}.tmp")
    fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        raw = canonical_json(value) + b"\n"
        view = memoryview(raw)
        while view:
            written = os.write(fd, view)
            if written <= 0:
                raise OSError("short active-task marker write")
            view = view[written:]
        os.fsync(fd)
    finally:
        os.close(fd)
    os.replace(temporary, path)


def _write_fd_all(fd: int, payload: bytes) -> None:
    view = memoryview(payload)
    while view:
        written = os.write(fd, view)
        if written <= 0:
            raise OSError("short write to supervised audit pipe")
        view = view[written:]


def _close_fd(fd: int) -> None:
    if fd >= 0:
        try:
            os.close(fd)
        except OSError:
            pass


def _worker_entry(config_path: Path, expected_sha256: str,
                  control_dir: Path, stderr_path: Path,
                  audit_fd: int, result_fd: int) -> int:
    """Watchdog child entry; control frames go to stdout, trace goes to audit_fd."""
    from nc0a_execution_engine import ProcessRoleRegistry
    from nc0a_watchdog import guard_watchdog_parent

    expected_parent = int(os.environ["NC0A_WATCHDOG_PARENT_PID"])
    guard_watchdog_parent(expected_parent)
    # Watchdog merges the supervised runner's stderr into stdout. Keep the
    # machine-readable protocol stream clean while preserving child tracebacks
    # in a separate, checksummed diagnostic artifact.
    stderr_fd = os.open(stderr_path, os.O_WRONLY | os.O_APPEND)
    try:
        os.dup2(stderr_fd, 2)
    finally:
        os.close(stderr_fd)
    role_path = Path(os.environ["NC0A_PROCESS_ROLE_REGISTRY"])
    token = os.environ["NC0A_WATCHDOG_LAUNCH_TOKEN"]
    roles = ProcessRoleRegistry(role_path, token, os.getpid())
    try:
        config_bytes = config_path.read_bytes()
        if sha256_bytes(config_bytes) != expected_sha256:
            raise G0ScientificFailure("G0_WORKER_CONFIG_HASH_MISMATCH",
                                      "Worker configuration hash changed after launch")
        config = json.loads(config_bytes)
        if config.get("scope") != SYNTHETIC_SCOPE:
            raise G0ScientificFailure("G0_NON_SYNTHETIC_INPUT_REJECTED",
                                      "This executor only permits synthetic engineering inputs")
        task_id = str(config["task_id"])
        graph_payload = config["graph"]
        labels = tuple(item["value"] for item in graph_payload["nodes"])
        edges = tuple(tuple(edge) for edge in graph_payload["edges"])
        n = len(labels)
        graph = ConnectedDegreeSwap(n, edges)
        if graph.fingerprint() != config["kernel_graph_sha256"]:
            raise G0ScientificFailure("G0_KERNEL_GRAPH_HASH_MISMATCH",
                                      "Normalized graph does not match the configured kernel graph")
        identity = config["task_coordinates"]
        if identity.get("recording_id", "").startswith("SYNTHETIC_") is False:
            raise G0ScientificFailure("G0_NON_SYNTHETIC_TASK_ID_REJECTED",
                                      "Synthetic task coordinates must be visibly labeled")
        graph_seed = int(config["graph_seed"])
        louvain_seeds = [int(value) for value in config["louvain_seeds"]]
        if len(louvain_seeds) != LOUVAIN_TRIALS:
            raise G0ScientificFailure("G0_LOUVAIN_SEED_COUNT_INVALID",
                                      "Exactly 200 Louvain seeds are required")
        if config.get("test_fault") == "scientific_failure":
            raise G0ScientificFailure("G0_INJECTED_SCIENTIFIC_INTEGRITY_FAILURE",
                                      "Synthetic-only scientific failure injection")
        if config.get("test_fault") == "unknown_failure":
            raise ValueError("Synthetic-only unknown failure injection")

        attempts = PROPOSALS_PER_EDGE * graph.m
        os.fstat(audit_fd)
        os.fstat(result_fd)
        _emit("HEADER", {"format": "G0_WORKER_HEADER_V1", "task_id": task_id,
                         "task_identity_sha256": config["task_identity_sha256"],
                         "graph_sha256": config["graph_sha256"],
                         "source_artifact_sha256": config["source_artifact_sha256"],
                         "proposal_attempts": attempts})
        sys.stdout.flush()
        _write_phase(control_dir / "active_task.json", task_id, "case")
        began_swap = time.perf_counter()
        rng = random.Random(graph_seed)
        previous = "0" * 64
        audit_sequence = 0
        for _ in range(attempts):
            accepted, event = graph.propose_audited(rng, audit_local=True)
            record = _hash_audit_record(audit_sequence, previous, event)
            _write_fd_all(audit_fd, canonical_json(record) + b"\n")
            previous = str(record["record_sha256"])
            audit_sequence += 1
            if accepted and graph.attempts != graph.accepted + graph.rejected_overlap + graph.rejected_duplicate + graph.rejected_disconnect:
                raise G0ScientificFailure("G0_PROPOSAL_ACCOUNTING_INVALID",
                                          "Attempt counters do not reconcile")
        _close_fd(audit_fd)
        audit_fd = -1
        os.fstat(result_fd)
        sys.stdout.flush()
        graph.assert_invariants()
        if graph.attempts != attempts or graph.attempts != (
                graph.accepted + graph.rejected_overlap + graph.rejected_duplicate +
                graph.rejected_disconnect):
            raise G0ScientificFailure("G0_PROPOSAL_COUNT_INVALID",
                                      "4E attempt or rejection accounting is incomplete")
        swap_seconds = time.perf_counter() - began_swap
        final_edges = tuple(sorted(graph.edges))
        final_graph_hash = graph.fingerprint()
        metrics = _graph_metrics(labels, final_edges, tuple(edges))

        _write_phase(control_dir / "active_task.json", task_id, "case")
        before_children = resource.getrusage(resource.RUSAGE_CHILDREN)
        began_louvain = time.perf_counter()
        trials: list[dict[str, object]] = []
        try:
            with ProcessPoolExecutor(
                    max_workers=int(config["workers"]),
                    mp_context=__import__("multiprocessing").get_context("spawn"),
                    initializer=_louvain_worker_init,
                    initargs=(n, labels, final_edges, config.get("test_fault"))) as pool:
                futures = {pool.submit(_louvain_trial, index, seed): index
                           for index, seed in enumerate(louvain_seeds)}
                roles.sync_pool(pool)
                pending = set(futures)
                # Do not rely only on as_completed(): on macOS spawn a worker
                # that exits via os._exit can leave pending futures unresolved
                # on some supported Python builds. Poll both futures and the
                # exact Process objects created by this executor so an abrupt
                # child exit becomes a typed operational failure promptly.
                pool_processes = tuple(getattr(pool, "_processes", {}).values())
                while pending:
                    done, pending = wait(pending, timeout=0.25,
                                         return_when=FIRST_COMPLETED)
                    for future in done:
                        try:
                            trials.append(future.result())
                        except G0ScientificFailure:
                            _terminate_louvain_pool(pool, pool_processes)
                            raise
                        except G0OperationalFailure:
                            _terminate_louvain_pool(pool, pool_processes)
                            raise
                        except BrokenProcessPool as exc:
                            exit_codes = sorted({process.exitcode for process in pool_processes
                                                 if process.exitcode is not None})
                            _terminate_louvain_pool(pool, pool_processes)
                            raise G0UnknownFailure(
                                "G0_WORKER_EXIT_UNCLASSIFIED",
                                "A Louvain spawn worker exited without a typed operational cause "
                                f"(exit codes: {exit_codes})") from exc
                    if pending:
                        exited = [process for process in pool_processes
                                  if process.exitcode is not None]
                        if exited:
                            codes = sorted({process.exitcode for process in exited})
                            _terminate_louvain_pool(pool, pool_processes)
                            raise G0UnknownFailure(
                                "G0_WORKER_EXIT_UNCLASSIFIED",
                                "A Louvain spawn worker exited without a typed operational cause "
                                f"(exit codes: {codes})")
                    roles.sync_pool(pool)
        finally:
            roles.clear_pool()
        os.fstat(result_fd)
        after_children = resource.getrusage(resource.RUSAGE_CHILDREN)
        louvain_cpu_seconds = ((after_children.ru_utime + after_children.ru_stime) -
                               (before_children.ru_utime + before_children.ru_stime))
        louvain_seconds = time.perf_counter() - began_louvain
        trials.sort(key=lambda item: int(item["trial_index"]))
        if [item["trial_index"] for item in trials] != list(range(LOUVAIN_TRIALS)):
            raise G0ScientificFailure("G0_LOUVAIN_TRIAL_COVERAGE_INVALID",
                                      "Louvain trial indices are missing or duplicated")
        q_values = [float(item["modularity"]) for item in trials]
        if any(not math.isfinite(value) for value in q_values):
            raise G0ScientificFailure("G0_LOUVAIN_Q_NONFINITE",
                                      "At least one Louvain modularity is nonfinite")
        best_index = max(range(len(q_values)), key=q_values.__getitem__)
        best_partition = list(trials[best_index]["partition"])
        for item in trials:
            item.pop("partition", None)
        result = {
            "format": "G0_SYNTHETIC_NULL_RESULT_V1",
            "scope": SYNTHETIC_SCOPE,
            "task_id": task_id,
            "task_identity_sha256": config["task_identity_sha256"],
            "task_coordinates": identity,
            "input_graph_sha256": config["graph_sha256"],
            "source_artifact_sha256": config["source_artifact_sha256"],
            "kernel_input_sha256": config["kernel_graph_sha256"],
            "null_graph_sha256": final_graph_hash,
            "degree_sequence_sha256": metrics["degree_sequence_sha256"],
            "seed_manifest": {"graph_seed": graph_seed,
                              "louvain_seeds": louvain_seeds},
            "swap": {"attempts": graph.attempts, "accepted": graph.accepted,
                     "rejected_overlap": graph.rejected_overlap,
                     "rejected_duplicate": graph.rejected_duplicate,
                     "rejected_disconnect": graph.rejected_disconnect,
                     "acceptance_rate": graph.accepted / graph.attempts,
                     "proposal_audit_records": audit_sequence,
                     "proposal_audit_tip_sha256": previous,
                     "swap_seconds": swap_seconds},
            "topology": metrics,
            "louvain": {"algorithm": "community.community_louvain.best_partition",
                        "q_function": "community.community_louvain.modularity",
                        "resolution": 1.0, "weight": "weight", "trials": trials,
                        "trial_count": len(trials), "q_values": q_values,
                        "max_q": q_values[best_index],
                        "first_max_trial_index": best_index,
                        "best_partition": best_partition,
                        "wall_seconds": louvain_seconds,
                        "child_cpu_seconds": max(0.0, louvain_cpu_seconds)},
        }
        _emit("GRAPH", {"graph_sha256": final_graph_hash,
                         "edge_count": len(final_edges),
                         "node_count": graph.n})
        result_bundle = canonical_json({
            "format": "G0_TASK_OUTPUT_BUNDLE_V1",
            "result": result,
            "final_edges": [list(edge) for edge in final_edges],
        })
        _write_fd_all(result_fd, result_bundle)
        _close_fd(result_fd)
        result_fd = -1
        _emit("RESULT_REF", {"sha256": sha256_bytes(result_bundle),
                              "size_bytes": len(result_bundle),
                              "audit_tip_sha256": previous})
        sys.stdout.flush()
        (control_dir / "active_task.json").unlink(missing_ok=True)
        return 0
    except G0ScientificFailure as exc:
        _close_fd(audit_fd)
        _close_fd(result_fd)
        _emit("FAIL", {"failure_class": "SCIENTIFIC", "reason_code": exc.reason_code,
                        "reason": str(exc)[:500]})
        sys.stdout.flush()
        return 65
    except G0OperationalFailure as exc:
        _close_fd(audit_fd)
        _close_fd(result_fd)
        _emit("FAIL", {"failure_class": "OPERATIONAL", "reason_code": exc.reason_code,
                        "reason": str(exc)[:500]})
        sys.stdout.flush()
        return 75
    except G0UnknownFailure as exc:
        _close_fd(audit_fd)
        _close_fd(result_fd)
        _emit("FAIL", {"failure_class": "UNKNOWN", "reason_code": exc.reason_code,
                        "reason": str(exc)[:500]})
        sys.stdout.flush()
        return 70
    except BaseException as exc:
        _close_fd(audit_fd)
        _close_fd(result_fd)
        _emit("FAIL", {"failure_class": "UNKNOWN",
                        "reason_code": "G0_UNCLASSIFIED_EXCEPTION",
                        "reason": (f"{type(exc).__name__}: {exc}; "
                                   f"{traceback.format_exc()[-300:]}")[:500]})
        sys.stdout.flush()
        return 70


def _write_once(path: Path, payload: bytes) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        view = memoryview(payload)
        while view:
            written = os.write(fd, view)
            if written <= 0:
                raise OSError("short write to worker configuration")
            view = view[written:]
        os.fsync(fd)
    finally:
        os.close(fd)
    return sha256_bytes(payload)


def _parse_worker_stdout(path: Path, *, expected_attempts: int,
                         expected_identity_sha256: str,
                         expected_graph_sha256: str,
                         expected_degree_sequence: tuple[int, ...],
                         expected_seed_manifest: dict[str, object],
                         result_bundle: bytes
                         ) -> tuple[dict, str, tuple[tuple[int, int], ...]]:
    header = None
    final_graph = None
    result_ref = None
    failure = None
    with path.open("rb") as handle:
        for line_number, raw in enumerate(handle, start=1):
            if not raw.endswith(b"\n"):
                raise G0ScientificFailure("G0_WORKER_STDOUT_TRUNCATED",
                                          f"Worker stdout has a partial record at line {line_number}")
            tag, separator, payload = raw.partition(b"\t")
            if not separator:
                raise G0ScientificFailure("G0_WORKER_STDOUT_FRAME_INVALID",
                                          f"Worker stdout has an invalid frame at line {line_number}")
            try:
                value = json.loads(payload)
            except (ValueError, UnicodeDecodeError) as exc:
                raise G0ScientificFailure("G0_WORKER_STDOUT_JSON_INVALID",
                                          f"Worker stdout JSON invalid at line {line_number}") from exc
            if tag == b"HEADER":
                if header is not None or result_ref is not None:
                    raise G0ScientificFailure("G0_WORKER_HEADER_DUPLICATE",
                                              "Worker header is duplicated or out of order")
                header = value
            elif tag == b"RESULT":
                raise G0ScientificFailure("G0_WORKER_RESULT_INLINE_FORBIDDEN",
                                          "Large scientific results must use the bounded result pipe")
            elif tag == b"GRAPH":
                if header is None or final_graph is not None or result_ref is not None or failure is not None:
                    raise G0ScientificFailure("G0_WORKER_GRAPH_FRAME_INVALID",
                                              "Worker graph frame is duplicated or out of order")
                final_graph = value
            elif tag == b"RESULT_REF":
                if (header is None or final_graph is None or result_ref is not None or
                        failure is not None):
                    raise G0ScientificFailure("G0_WORKER_RESULT_REFERENCE_INVALID",
                                              "Worker result reference is duplicated or out of order")
                result_ref = value
            elif tag == b"FAIL":
                if failure is not None or result_ref is not None:
                    raise G0ScientificFailure("G0_WORKER_FAILURE_FRAME_INVALID",
                                              "Worker failure frame is duplicated or follows a result")
                failure = value
            else:
                raise G0ScientificFailure("G0_WORKER_STDOUT_TAG_INVALID",
                                          f"Unrecognized worker output frame at line {line_number}")
    if failure is not None:
        raise _failure_from_worker(failure)
    if (header is None or final_graph is None or result_ref is None or
            not isinstance(result_bundle, bytes) or
            result_ref.get("size_bytes") != len(result_bundle) or
            result_ref.get("sha256") != sha256_bytes(result_bundle) or
            len(result_bundle) > _MAX_RESULT_BUNDLE_BYTES or
            header.get("proposal_attempts") != expected_attempts or
            header.get("task_identity_sha256") != expected_identity_sha256 or
            header.get("graph_sha256") != expected_graph_sha256):
        raise G0ScientificFailure("G0_WORKER_RESULT_INCOMPLETE",
                                  "Worker result, identity or proposal audit does not reconcile")
    try:
        bundle = json.loads(result_bundle)
    except (ValueError, UnicodeDecodeError) as exc:
        raise G0ScientificFailure("G0_WORKER_RESULT_BUNDLE_INVALID",
                                  "Worker result bundle is not valid JSON") from exc
    if (canonical_json(bundle) != result_bundle or
            not isinstance(bundle, dict) or
            set(bundle) != {"format", "result", "final_edges"} or
            bundle.get("format") != "G0_TASK_OUTPUT_BUNDLE_V1" or
            not isinstance(bundle.get("result"), dict) or
            not isinstance(bundle.get("final_edges"), list)):
        raise G0ScientificFailure("G0_WORKER_RESULT_BUNDLE_INVALID",
                                  "Worker result bundle is noncanonical or incomplete")
    result = bundle["result"]
    final_edges = tuple(tuple(edge) for edge in bundle["final_edges"])
    if (final_graph.get("edge_count") != len(final_edges) or
            final_graph.get("node_count") != len(expected_degree_sequence) or
            final_graph.get("graph_sha256") != result.get("null_graph_sha256") or
            result_ref.get("audit_tip_sha256") !=
            result.get("swap", {}).get("proposal_audit_tip_sha256") or
            result.get("task_identity_sha256") != expected_identity_sha256 or
            result.get("input_graph_sha256") != expected_graph_sha256 or
            result.get("seed_manifest") != expected_seed_manifest or
            result.get("swap", {}).get("proposal_audit_records") != expected_attempts or
            not _is_sha256(result.get("swap", {}).get("proposal_audit_tip_sha256"))):
        raise G0ScientificFailure("G0_WORKER_RESULT_BUNDLE_IDENTITY_INVALID",
                                  "Result bundle identities do not match the control frames")
    if final_edges != tuple(sorted(final_edges)):
        raise G0ScientificFailure("G0_WORKER_GRAPH_FRAME_ORDER_INVALID",
                                  "Final graph edge list is not canonical")
    checked_graph = ConnectedDegreeSwap(
        len(expected_degree_sequence), final_edges)
    checked_graph.assert_invariants()
    if (checked_graph.fingerprint() != final_graph.get("graph_sha256") or
            checked_graph.fingerprint() != result.get("null_graph_sha256") or
            checked_graph.initial_degrees != expected_degree_sequence or
            tuple(result.get("topology", {}).get("degree_sequence", [])) !=
            expected_degree_sequence):
        raise G0ScientificFailure("G0_WORKER_GRAPH_FRAME_HASH_INVALID",
                                  "Worker graph frame does not match the validated task result")
    _validate_result(result, expected_attempts)
    return result, result["swap"]["proposal_audit_tip_sha256"], final_edges


def _failure_from_worker(value: dict) -> BaseException:
    if not isinstance(value, dict):
        return G0ScientificFailure("G0_WORKER_FAILURE_FRAME_INVALID",
                                   "Worker failure frame is not an object")
    category, code, reason = (value.get("failure_class"), value.get("reason_code"),
                              value.get("reason"))
    if not all(isinstance(item, str) and item for item in (category, code, reason)):
        return G0ScientificFailure("G0_WORKER_FAILURE_FRAME_INVALID",
                                   "Worker failure frame lacks classification fields")
    if category == "SCIENTIFIC":
        return G0ScientificFailure(code, reason)
    if category == "OPERATIONAL":
        return G0OperationalFailure(code, reason)
    if category == "UNKNOWN":
        return G0UnknownFailure(code, reason)
    return RuntimeError(reason)


def _validate_result(result: dict, expected_attempts: int) -> None:
    swap = result.get("swap", {})
    if (swap.get("attempts") != expected_attempts or
            swap.get("proposal_audit_records") != expected_attempts or
            swap.get("attempts") != swap.get("accepted", -1) +
            swap.get("rejected_overlap", -1) + swap.get("rejected_duplicate", -1) +
            swap.get("rejected_disconnect", -1)):
        raise G0ScientificFailure("G0_PROPOSAL_ACCOUNTING_INVALID",
                                  "Proposal outcomes do not total the exact 4E schedule")
    louvain = result.get("louvain", {})
    trials = louvain.get("trials")
    if (louvain.get("trial_count") != LOUVAIN_TRIALS or
            not isinstance(trials, list) or len(trials) != LOUVAIN_TRIALS or
            [item.get("trial_index") for item in trials] != list(range(LOUVAIN_TRIALS))):
        raise G0ScientificFailure("G0_LOUVAIN_TRIAL_COVERAGE_INVALID",
                                  "Expected exactly 200 ordered Louvain trial records")
    q_values = [float(item["modularity"]) for item in trials]
    if any(not math.isfinite(value) for value in q_values):
        raise G0ScientificFailure("G0_LOUVAIN_Q_NONFINITE", "Nonfinite Louvain Q in result")
    first_max = max(range(len(q_values)), key=q_values.__getitem__)
    if (louvain.get("q_values") != q_values or
            louvain.get("max_q") != q_values[first_max] or
            louvain.get("first_max_trial_index") != first_max or
            len(louvain.get("best_partition", [])) != result.get("topology", {}).get("node_count")):
        raise G0ScientificFailure("G0_LOUVAIN_MAXIMUM_INVALID",
                                  "Saved Q vector or first-maximum definition is inconsistent")


_MAX_AUDIT_RECORD_BYTES = 64 * 1024
_MAX_RESULT_BUNDLE_BYTES = 32 * 1024 * 1024
_AUDIT_STREAM_FORMAT = "G0_GZIP_CANONICAL_JSONL_AUDIT_V1"


def _read_bounded_result_pipe(read_fd: int, stream_metadata: dict,
                              close_reader=None) -> bytes:
    """Collect only the bounded final result/checkpoint bundle, never proposal logs."""
    payload = bytearray()
    try:
        while True:
            block = os.read(read_fd, 64 * 1024)
            if not block:
                break
            payload.extend(block)
            if len(payload) > _MAX_RESULT_BUNDLE_BYTES:
                raise G0UnknownFailure(
                    "G0_RESULT_BUNDLE_TOO_LARGE",
                    "Final scientific result bundle exceeds the 32 MiB internal bound")
        stream_metadata["size_bytes"] = len(payload)
        stream_metadata["sha256"] = sha256_bytes(payload)
        return bytes(payload)
    finally:
        if close_reader is None:
            os.close(read_fd)
        else:
            close_reader()


def _compressed_audit_pipe_chunks(read_fd: int, *, expected_records: int,
                                  stream_metadata: dict,
                                  close_reader=None):
    """Validate and gzip a bounded audit-pipe stream as the adapter writes it.

    Complete records are checked for canonical encoding, sequence, previous
    digest, record digest and proposal ordinal. A short clean EOF is sealed as
    an explicitly incomplete evidence artifact; a malformed record raises and
    leaves the storage layer fail-closed.
    """
    compressor = zlib.compressobj(level=6, wbits=16 + zlib.MAX_WBITS)
    pending = bytearray()
    previous = "0" * 64
    count = 0
    trailing_partial_bytes = 0
    try:
        while True:
            block = os.read(read_fd, 64 * 1024)
            if not block:
                break
            pending.extend(block)
            while True:
                newline = pending.find(b"\n")
                if newline < 0:
                    if len(pending) > _MAX_AUDIT_RECORD_BYTES:
                        raise G0ScientificFailure(
                            "G0_AUDIT_RECORD_TOO_LARGE",
                            "Audit pipe record exceeds the frozen record-size guard")
                    break
                raw = bytes(pending[:newline + 1])
                del pending[:newline + 1]
                payload = raw[:-1]
                try:
                    record = json.loads(payload)
                    if (len(payload) > _MAX_AUDIT_RECORD_BYTES or
                            canonical_json(record) != payload):
                        raise ValueError("record is oversized or not canonical JSON")
                    digest = record.pop("record_sha256")
                    body = {"sequence": record.get("sequence"),
                            "previous_sha256": record.get("previous_sha256"),
                            "event": record.get("event")}
                    if (set(record) != {"sequence", "previous_sha256", "event"} or
                            body["sequence"] != count or
                            body["previous_sha256"] != previous or
                            not _is_sha256(digest) or
                            sha256_bytes(canonical_json(body)) != digest or
                            not isinstance(body["event"], dict) or
                            body["event"].get("attempt") != count + 1):
                        raise ValueError("audit hash chain or proposal ordinal mismatch")
                except (ValueError, KeyError, TypeError, UnicodeDecodeError) as exc:
                    raise G0ScientificFailure(
                        "G0_PROPOSAL_AUDIT_HASH_INVALID",
                        f"Streamed proposal audit is invalid at record {count}: {exc}") from exc
                if count >= expected_records:
                    raise G0ScientificFailure("G0_PROPOSAL_COUNT_INVALID",
                                              "Audit stream contains more than the registered proposals")
                previous = digest
                count += 1
                compressed = compressor.compress(raw)
                if compressed:
                    yield compressed
        if pending:
            if count >= expected_records:
                raise G0ScientificFailure("G0_AUDIT_TRAILING_BYTES",
                                          "Unexpected bytes followed the final registered audit record")
            trailing_partial_bytes = len(pending)
            compressed = compressor.compress(bytes(pending))
            if compressed:
                yield compressed
        tail = compressor.flush()
        if tail:
            yield tail
        stream_metadata.update({
            "stream_format": _AUDIT_STREAM_FORMAT,
            "record_count": count,
            "chain_tip_sha256": previous,
            "complete": count == expected_records and trailing_partial_bytes == 0,
            "trailing_partial_bytes": trailing_partial_bytes,
        })
    finally:
        if close_reader is None:
            os.close(read_fd)
        else:
            close_reader()


def _synthetic_task_plan(graph: NormalizedGraph, identity: G0TaskIdentity,
                         environment: dict) -> dict[str, object]:
    if (not graph.source_id.startswith("SYNTHETIC_") or
            not identity.recording_id.startswith("SYNTHETIC_")):
        raise ValueError("run_synthetic_g0_task accepts only visibly synthetic identities")
    if graph.source_artifact_sha256 is None:
        raise ValueError("Synthetic task input requires a source-artifact SHA-256 identity")
    identity.validate(graph)
    graph_seed = g0_graph_seed(identity)
    louvain_seeds = [g0_louvain_seed(identity, index)
                     for index in range(LOUVAIN_TRIALS)]
    seed_manifest = {"graph_seed": graph_seed, "louvain_seeds": louvain_seeds}
    seed_fingerprint = sha256_bytes(canonical_json(seed_manifest))
    protocol_identity = {
        "protocol": "NC_G0_CONNECTED_DOUBLE_EDGE_SWAP_V1",
        "attempts": PROPOSALS_PER_EDGE * graph.m,
        "louvain_trials": LOUVAIN_TRIALS,
        "task_coordinates": identity.as_dict(),
        "graph_sha256": graph.graph_sha256,
        "seed_fingerprint": seed_fingerprint,
        "environment": environment,
    }
    task_identity_sha256 = sha256_bytes(canonical_json(protocol_identity))
    task_id = f"g0synth-{task_identity_sha256[:48]}"
    return {"graph": graph, "identity": identity, "environment": environment,
            "graph_seed": graph_seed, "louvain_seeds": louvain_seeds,
            "seed_manifest": seed_manifest,
            "seed_fingerprint": seed_fingerprint,
            "task_identity_sha256": task_identity_sha256, "task_id": task_id}


def _activity_outcome_summary(outcome: dict[str, object]) -> dict[str, object]:
    """Keep activity reports bounded; task payloads already live in external storage."""
    summary_keys = ("status", "task_id", "attempt_id", "seed_fingerprint",
                    "task_identity_sha256", "reason_code", "reason")
    summary = {key: outcome[key] for key in summary_keys if key in outcome}
    for record_key in ("result_record", "audit_record", "stderr_record"):
        record = outcome.get(record_key)
        if isinstance(record, dict):
            ref_keys = ("task_id", "attempt_id", "result_path", "relative_path",
                        "artifact_kind", "size_bytes", "sha256")
            summary[record_key] = {key: record[key] for key in ref_keys if key in record}
    watchdog = outcome.get("watchdog")
    if isinstance(watchdog, dict):
        watchdog_keys = ("status", "returncode", "invocation_id",
                         "control_ledger_tip_sha256", "usage")
        summary["watchdog"] = {key: watchdog[key] for key in watchdog_keys
                                if key in watchdog}
    return summary


def _audit_replay_verifier(graph: NormalizedGraph, seed: int,
                           compressed_audit: bytes,
                           expected_final_hash: str) -> dict[str, object]:
    """Independently replay an archived proposal trace (intended for tests)."""
    inflater = gzip.decompress(compressed_audit)
    graph_state = ConnectedDegreeSwap(graph.n, graph.edges)
    rng = random.Random(seed)
    previous = "0" * 64
    records = inflater.splitlines()
    for sequence, raw in enumerate(records):
        try:
            record = json.loads(raw)
        except (ValueError, UnicodeDecodeError) as exc:
            raise G0ScientificFailure("G0_AUDIT_REPLAY_JSON_INVALID",
                                      f"Cannot parse proposal audit {sequence}") from exc
        digest = record.pop("record_sha256", None)
        body = {"sequence": record.get("sequence"),
                "previous_sha256": record.get("previous_sha256"),
                "event": record.get("event")}
        accepted, event = graph_state.propose_audited(rng, audit_local=True)
        expected = _hash_audit_record(sequence, previous, event)
        if (set(record) != {"sequence", "previous_sha256", "event"} or
                record != {key: expected[key] for key in ("sequence", "previous_sha256", "event")} or
                digest != expected["record_sha256"]):
            raise G0ScientificFailure("G0_AUDIT_REPLAY_MISMATCH",
                                      f"Recorded proposal {sequence} differs from fixed-seed replay")
        previous = str(digest)
    graph_state.assert_invariants()
    if graph_state.fingerprint() != expected_final_hash:
        raise G0ScientificFailure("G0_AUDIT_FINAL_GRAPH_MISMATCH",
                                  "Replayed proposal trace does not produce the committed graph")
    return {"proposal_count": len(records), "accepted": graph_state.accepted,
            "final_graph_sha256": graph_state.fingerprint(),
            "audit_tip_sha256": previous}


def run_synthetic_g0_task(*, store: G0ExternalStore, graph: NormalizedGraph,
                          identity: G0TaskIdentity, attempt_id: str,
                          invocation_id: int, limits: WatchdogLimits,
                          workers: int = 4, require_target_runtime: bool = False,
                          _test_fault: str | None = None) -> dict[str, object]:
    """Run one synthetic-only G0 null task through store -> watchdog -> result.

    This creates exactly 4E proposals and 200 independent, fixed-seed Louvain
    trials. Synthetic identity prefixes are caller declarations, not source
    provenance authentication; this module has no biological loader or
    full-battery launcher.
    """
    if not 1 <= workers <= 4 or limits.max_workers != workers:
        raise ValueError("Worker count must be 1..4 and match the Watchdog limit")
    if _test_fault not in (None, *_SYNTHETIC_TEST_FAULTS):
        raise ValueError("Unrecognized synthetic-only fault injection")
    environment = runtime_manifest(require_target=require_target_runtime)
    plan = _synthetic_task_plan(graph, identity, environment)
    task_id = str(plan["task_id"])
    seed_fingerprint = str(plan["seed_fingerprint"])
    expected = {task_id: seed_fingerprint}
    store.prepare_activity(activity_id=store.run_uuid, expected_tasks=expected)
    return _execute_synthetic_g0_plan(
        store=store, plan=plan, attempt_id=attempt_id,
        invocation_id=invocation_id, limits=limits, workers=workers,
        test_fault=_test_fault, expected_tasks=expected, final_report=True)


def run_synthetic_g0_activity(*, store: G0ExternalStore,
                               tasks: (Sequence[tuple[NormalizedGraph, G0TaskIdentity]] |
                                       Callable[[], Iterable[tuple[NormalizedGraph, G0TaskIdentity]]]),
                               limits: WatchdogLimits, workers: int = 4,
                               activity_id: str | None = None,
                               require_target_runtime: bool = False,
                               _test_faults: dict[str, str] | None = None) -> dict[str, object]:
    with store.activity_execution():
        return _run_synthetic_g0_activity_locked(
            store=store, tasks=tasks, limits=limits, workers=workers,
            activity_id=activity_id,
            require_target_runtime=require_target_runtime,
            _test_faults=_test_faults)


def _run_synthetic_g0_activity_locked(*, store: G0ExternalStore,
                                      tasks: (Sequence[tuple[NormalizedGraph, G0TaskIdentity]] |
                                              Callable[[], Iterable[tuple[NormalizedGraph, G0TaskIdentity]]]),
                                      limits: WatchdogLimits, workers: int = 4,
                                      activity_id: str | None = None,
                                      require_target_runtime: bool = False,
                                      _test_faults: dict[str, str] | None = None
                                      ) -> dict[str, object]:
    """Run a frozen synthetic task inventory sequentially with per-task watchdogs.

    Serial scheduling is intentional: at no time can concurrent task pools
    multiply the per-task worker cap. Each invocation has its own Watchdog
    limits; cumulative supervised CPU and worker-wall usage is reconstructed
    from the activity's append-only control ledger. A failed task stops the
    activity; resume revalidates the full frozen inventory, then uses indexed
    per-task state.
    """
    if not callable(tasks) and not isinstance(tasks, Sequence):
        raise TypeError("tasks must be a replayable Sequence or a zero-argument iterator factory")
    if not 1 <= workers <= 4 or limits.max_workers != workers:
        raise ValueError("Worker count must be 1..4 and match the Watchdog limit")
    environment = runtime_manifest(require_target=require_target_runtime)
    task_seeds: dict[str, str] = {}
    task_order: list[str] = []
    first_pass = tasks() if callable(tasks) else iter(tasks)
    for graph, identity in first_pass:
        plan = _synthetic_task_plan(graph, identity, environment)
        task_id = str(plan["task_id"])
        if task_id in task_seeds:
            raise ValueError("Activity contains duplicate task identities")
        task_seeds[task_id] = str(plan["seed_fingerprint"])
        task_order.append(task_id)
    task_count = len(task_order)
    if not task_count:
        raise ValueError("A G0 activity requires at least one task")
    test_faults = dict(_test_faults or {})
    if (set(test_faults) - set(task_seeds) or
            any(fault not in _SYNTHETIC_TEST_FAULTS for fault in test_faults.values())):
        raise ValueError("Activity fault injection must use known synthetic tasks and faults")
    frozen_activity_id = activity_id or store.run_uuid
    activity_started = time.perf_counter()
    store.prepare_activity(activity_id=frozen_activity_id,
                           expected_tasks=task_seeds)
    outcomes = []
    second_pass = tasks() if callable(tasks) else iter(tasks)
    processed = 0
    for graph, identity in second_pass:
        # Keep the all-task manifest small. In particular, do not retain the
        # 200-seed array and full plan object for every task while executing a
        # large activity; reconstruct only the current task's plan.
        plan = _synthetic_task_plan(graph, identity, environment)
        task_id = str(plan["task_id"])
        seed_fingerprint = str(plan["seed_fingerprint"])
        if (processed >= task_count or task_id != task_order[processed] or
                task_seeds.get(task_id) != seed_fingerprint):
            raise RecoveryRefused("G0_ACTIVITY_PLAN_CHANGED",
                                  "Task identity or seed changed after inventory freeze")
        processed += 1
        state = store.task_recovery_state(task_id=task_id,
                                          seed_fingerprint=seed_fingerprint)
        if state == "completed":
            # prepare_activity() already fully verified the ledger and every
            # referenced file for this process. Reuse the verified completion
            # index instead of loading the potentially large result payload.
            completion = store._task_state(task_id)["completions"][0]
            outcomes.append({"status": "reused_verified_completion",
                             "task_id": task_id,
                             "seed_fingerprint": seed_fingerprint,
                             "result_record": {
                                 "task_id": task_id,
                                 "attempt_id": completion["attempt_id"],
                                 "result_path": completion["result_path"],
                                 "size_bytes": completion["size_bytes"],
                                 "sha256": completion["sha256"]}})
            continue
        if state == "attempts_exhausted":
            raise RecoveryRefused("G0_TASK_ATTEMPT_LIMIT",
                                  f"Task recovery quota is exhausted: {task_id}")
        if state not in ("not_started", "retryable"):
            raise RecoveryRefused("G0_TASK_RECOVERY_NOT_AUTHORIZED",
                                  f"Prior task state is not eligible: {task_id}")
        outcome = _execute_synthetic_g0_plan(
            store=store, plan=plan, attempt_id=str(uuid.uuid4()),
            invocation_id=store.next_watchdog_invocation_id(),
            limits=limits, workers=workers, test_fault=test_faults.get(task_id),
            expected_tasks=task_seeds, final_report=False)
        outcomes.append(_activity_outcome_summary(outcome))
        if outcome.get("status") != "completed":
            return {"status": "stopped_after_task_failure",
                    "activity_id": frozen_activity_id, "outcomes": outcomes,
                    "recovery_state": store.task_recovery_state(
                        task_id=task_id, seed_fingerprint=seed_fingerprint),
                    "resource_accounting": {
                        **store.activity_resource_accounting(frozen_activity_id),
                        "process_session_wall_seconds": time.perf_counter() - activity_started}}
    if processed != task_count:
        raise RecoveryRefused("G0_ACTIVITY_PLAN_CHANGED",
                              "Task source ended before the frozen activity inventory")
    report = store._incremental_recovery_report(task_seeds)
    return {"status": "completed", "activity_id": frozen_activity_id,
            "outcomes": outcomes, "recovery_report": report,
            "task_count": task_count, "global_compute_worker_cap": workers,
            "schedule": "serial_tasks",
            "resource_accounting": {
                **store.activity_resource_accounting(frozen_activity_id),
                "process_session_wall_seconds": time.perf_counter() - activity_started}}


def _execute_synthetic_g0_plan(*, store: G0ExternalStore, plan: dict[str, object],
                               attempt_id: str, invocation_id: int,
                               limits: WatchdogLimits, workers: int,
                               test_fault: str | None,
                               expected_tasks: dict[str, str],
                               final_report: bool) -> dict[str, object]:
    graph = plan["graph"]
    identity = plan["identity"]
    environment = plan["environment"]
    graph_seed = plan["graph_seed"]
    louvain_seeds = plan["louvain_seeds"]
    seed_manifest = plan["seed_manifest"]
    seed_fingerprint = str(plan["seed_fingerprint"])
    task_identity_sha256 = str(plan["task_identity_sha256"])
    task_id = str(plan["task_id"])
    if not isinstance(graph, NormalizedGraph) or not isinstance(identity, G0TaskIdentity):
        raise TypeError("Invalid planned G0 task")
    store.assert_activity_task(task_id=task_id, seed_fingerprint=seed_fingerprint)
    state = store.task_recovery_state(task_id=task_id,
                                      seed_fingerprint=seed_fingerprint)
    if state == "completed":
        payload = store.read_completed_task_result(task_id=task_id,
                                                   seed_fingerprint=seed_fingerprint)
        return {"status": "reused_verified_completion", "task_id": task_id,
                "seed_fingerprint": seed_fingerprint,
                "result_payload": payload,
                "task_identity_sha256": task_identity_sha256}
    if state == "attempts_exhausted":
        raise RecoveryRefused("G0_TASK_ATTEMPT_LIMIT", "Synthetic task recovery quota is exhausted")
    if state not in ("retryable", "not_started"):
        raise RecoveryRefused("G0_TASK_RECOVERY_NOT_AUTHORIZED",
                              "Prior attempt is not eligible under the verified task ledger")

    attempt_uuid = str(uuid.UUID(attempt_id))
    source_path = f"source-graphs/{task_id}/{attempt_uuid}/input.json.gz"
    source_payload = gzip.compress(canonical_json(graph.payload()), mtime=0)
    source_record = store.write_immutable_artifact(
        relative_path=source_path, artifact_kind="source_graph",
        identity={"task_id": task_id, "attempt_id": attempt_uuid,
                  "graph_sha256": graph.graph_sha256,
                  "source_artifact_sha256": graph.source_artifact_sha256,
                  "scope": SYNTHETIC_SCOPE}, chunks=source_payload)
    store.begin_task(task_id=task_id, attempt_id=attempt_uuid,
                     seed_fingerprint=seed_fingerprint,
                     invocation_id=invocation_id)
    kernel_graph = ConnectedDegreeSwap(graph.n, graph.edges)
    config = {"scope": SYNTHETIC_SCOPE, "task_id": task_id,
              "task_identity_sha256": task_identity_sha256,
              "task_coordinates": identity.as_dict(),
              "graph": {"nodes": [_node_record(node) for node in graph.nodes],
                        "edges": [list(edge) for edge in graph.edges]},
              "graph_sha256": graph.graph_sha256,
              "kernel_graph_sha256": kernel_graph.fingerprint(),
              "source_artifact_sha256": source_record["sha256"],
              "graph_seed": graph_seed, "louvain_seeds": louvain_seeds,
              "workers": workers, "test_fault": test_fault}
    config_bytes = canonical_json(config)
    config_path = store.control_dir / f"g0-worker-config.{invocation_id}.json"
    config_sha256 = _write_once(config_path, config_bytes)
    stderr_path = store.control_dir / f"runner.g0.{invocation_id}.stderr.log"
    _write_once(stderr_path, b"")
    worker_script = Path(__file__).resolve()
    expected_proposals = PROPOSALS_PER_EDGE * graph.m
    audit_identity = {
        "task_id": task_id, "attempt_id": attempt_uuid,
        "graph_sha256": graph.graph_sha256,
        "seed_fingerprint": seed_fingerprint,
        "stream_format": _AUDIT_STREAM_FORMAT,
        "expected_record_count": expected_proposals,
        "invocation_id": invocation_id,
    }
    stream_metadata: dict[str, object] = {}
    audit_read_fd, audit_write_fd = os.pipe()
    audit_reader_state = {"open": True}

    def close_audit_reader() -> None:
        if audit_reader_state["open"]:
            _close_fd(audit_read_fd)
            audit_reader_state["open"] = False

    audit_chunks = _compressed_audit_pipe_chunks(
        audit_read_fd, expected_records=expected_proposals,
        stream_metadata=stream_metadata, close_reader=close_audit_reader)
    audit_writer = ThreadPoolExecutor(
        max_workers=2, thread_name_prefix="g0-artifact-stream-reader")
    audit_future = audit_writer.submit(
        store.write_immutable_artifact,
        relative_path=f"audit/{task_id}/{attempt_uuid}/proposals.jsonl.gz",
        artifact_kind="audit", identity=audit_identity,
        chunks=audit_chunks, stream_metadata=stream_metadata)
    result_read_fd, result_write_fd = os.pipe()
    result_stream_metadata: dict[str, object] = {}
    result_reader_state = {"open": True}

    def close_result_reader() -> None:
        if result_reader_state["open"]:
            _close_fd(result_read_fd)
            result_reader_state["open"] = False

    result_future = audit_writer.submit(
        _read_bounded_result_pipe, result_read_fd, result_stream_metadata,
        close_result_reader)
    command = [sys.executable, str(worker_script), "--worker",
               str(config_path), config_sha256, str(store.control_dir),
               str(stderr_path), str(audit_write_fd), str(result_write_fd)]
    before_cpu = time.process_time()
    began = time.perf_counter()
    watchdog: dict | None = None
    watchdog_error: BaseException | None = None

    def audit_writer_guard() -> str | None:
        if audit_future.done():
            try:
                audit_future.result()
            except BaseException as exc:
                close_audit_reader()
                code = getattr(exc, "code", "G0_EXTERNAL_IO_FAILURE")
                if code not in {
                        "G0_EXTERNAL_MOUNT_UNAVAILABLE",
                        "G0_EXTERNAL_VOLUME_IDENTITY_MISMATCH",
                        "G0_EXTERNAL_SPACE_LIMIT", "G0_INTERNAL_SPACE_LIMIT",
                        "G0_EXTERNAL_IO_FAILURE", "G0_EXTERNAL_POSTWRITE_IDENTITY_FAILURE"}:
                    code = "G0_EXTERNAL_IO_FAILURE"
                return code
        if result_future.done():
            try:
                result_future.result()
            except BaseException:
                close_result_reader()
                return "G0_RESULT_PIPE_FAILED"
        return None

    try:
        try:
            watchdog = store.supervise_worker(
                command, limits=limits, invocation_id=invocation_id,
                task_id=task_id, attempt_id=attempt_uuid,
                activity_id=str(store.activity_id),
                inherited_fds=(audit_write_fd, result_write_fd),
                additional_stop_guard=audit_writer_guard)
        except BaseException as exc:
            watchdog_error = exc
        finally:
            _close_fd(audit_write_fd)
            _close_fd(result_write_fd)
            audit_write_fd = -1
            result_write_fd = -1
        try:
            audit_record = audit_future.result()
        except BaseException as exc:
            state = store._task_state(task_id)
            if state["starts"] and not state["completions"] and not state["failures"]:
                store.record_task_failure(
                    task_id=task_id, attempt_id=attempt_uuid,
                    # Loss or uncertain persistence of the proposal trace is
                    # not automatically retryable: the missing evidence cannot
                    # be repaired by re-running the same stochastic task.
                    failure_class="UNKNOWN",
                    reason_code="G0_AUDIT_STREAM_WRITE_FAILED",
                    reason=f"External audit stream failed: {type(exc).__name__}: {exc}")
            raise
        finally:
            audit_writer.shutdown(wait=True)
        try:
            result_bundle = result_future.result()
        except BaseException as exc:
            state = store._task_state(task_id)
            if state["starts"] and not state["completions"] and not state["failures"]:
                store.record_task_failure(
                    task_id=task_id, attempt_id=attempt_uuid,
                    failure_class="UNKNOWN",
                    reason_code="G0_RESULT_BUNDLE_READ_FAILED",
                    reason=f"Result pipe failed: {type(exc).__name__}: {exc}")
            raise
        if watchdog_error is not None:
            raise watchdog_error
        assert watchdog is not None
        stdout_path = store.control_dir / f"runner.g0.{invocation_id}.stdout.log"
        stdout_hash = sha256_bytes(stdout_path.read_bytes())
        if watchdog.get("usage", {}).get("runner_stdout_sha256") != stdout_hash:
            raise G0ScientificFailure("G0_WATCHDOG_STDOUT_HASH_MISMATCH",
                                      "Watchdog stdout hash differs from the persisted log")
        stderr_record = store.write_immutable_artifact(
            relative_path=(f"diagnostic-logs/{task_id}/{attempt_uuid}/"
                           f"invocation-{invocation_id}.log"),
            artifact_kind="diagnostic_log",
            identity={"task_id": task_id, "attempt_id": attempt_uuid,
                      "invocation_id": invocation_id,
                      "source_artifact_sha256": graph.source_artifact_sha256},
            chunks=stderr_path.read_bytes())
        if watchdog.get("status") == "stopped":
            reason = str(watchdog.get("reason", "unspecified watchdog stop"))
            operational_reasons = {
                "WALL_LIMIT", "CPU_LIMIT_WITH_TERMINATION_MARGIN",
                "AGGREGATE_RSS_LIMIT", "RUN_DISK_ALLOCATION_LIMIT",
                "FREE_DISK_RESERVE_BREACH", "CASE_WALL_LIMIT", "ORACLE_WALL_LIMIT",
                "HOST_MEMORY_PRESSURE_LIMIT", "SWAP_GROWTH_LIMIT",
                "SWAP_FREE_RESERVE_BREACH", "BOOT_VOLUME_FREE_DISK_RESERVE_BREACH",
                "VM_VOLUME_FREE_DISK_RESERVE_BREACH", "SLEEP_ASSERTION_LOST",
                "AC_POWER_LOST", "THERMAL_WARNING", "G0_EXTERNAL_MOUNT_UNAVAILABLE",
                "G0_EXTERNAL_VOLUME_IDENTITY_MISMATCH", "G0_EXTERNAL_SPACE_LIMIT",
                "G0_INTERNAL_SPACE_LIMIT", "G0_EXTERNAL_IO_FAILURE",
                "G0_EXTERNAL_POSTWRITE_IDENTITY_FAILURE",
            }
            retryable_stop = reason in operational_reasons
            store.record_task_failure(
                task_id=task_id, attempt_id=attempt_uuid,
                failure_class="OPERATIONAL" if retryable_stop else "UNKNOWN",
                reason_code=reason if retryable_stop else "G0_WATCHDOG_STOP_UNCLASSIFIED",
                reason=reason)
            return {"status": "stopped" if retryable_stop else "unknown_failure",
                    "task_id": task_id,
                    "attempt_id": attempt_uuid, "seed_fingerprint": seed_fingerprint,
                    "watchdog": watchdog, "stderr_record": stderr_record}
        if (watchdog.get("status") == "failed" and
                watchdog.get("returncode") not in (0, None)):
            fail_frame_present = any(
                line.startswith(b"FAIL\t") for line in stdout_path.read_bytes().splitlines())
            if not fail_frame_present:
                store.record_task_failure(
                    task_id=task_id, attempt_id=attempt_uuid,
                    failure_class="UNKNOWN",
                    reason_code="G0_WORKER_EXIT_UNCLASSIFIED",
                    reason=f"Watchdog runner exited {watchdog.get('returncode')} without a typed failure")
                return {"status": "unknown_failure", "task_id": task_id,
                        "attempt_id": attempt_uuid,
                        "seed_fingerprint": seed_fingerprint, "watchdog": watchdog,
                        "stderr_record": stderr_record}
        try:
            result, audit_tip, final_edges = _parse_worker_stdout(
                stdout_path, expected_attempts=4 * graph.m,
                expected_identity_sha256=task_identity_sha256,
                expected_graph_sha256=graph.graph_sha256,
                expected_degree_sequence=graph.degree_sequence,
                expected_seed_manifest=seed_manifest,
                result_bundle=result_bundle)
        except G0OperationalFailure as exc:
            store.record_task_failure(task_id=task_id, attempt_id=attempt_uuid,
                                      failure_class="OPERATIONAL",
                                      reason_code=exc.reason_code, reason=str(exc))
            return {"status": "operational_failure", "task_id": task_id,
                    "attempt_id": attempt_uuid, "reason_code": exc.reason_code,
                    "seed_fingerprint": seed_fingerprint,
                    "watchdog": watchdog, "stderr_record": stderr_record}
        except G0ScientificFailure as exc:
            store.record_task_failure(task_id=task_id, attempt_id=attempt_uuid,
                                      failure_class="SCIENTIFIC",
                                      reason_code=exc.reason_code, reason=str(exc))
            return {"status": "scientific_failure", "task_id": task_id,
                    "attempt_id": attempt_uuid, "reason_code": exc.reason_code,
                    "seed_fingerprint": seed_fingerprint,
                    "watchdog": watchdog, "stderr_record": stderr_record}
        except G0UnknownFailure as exc:
            store.record_task_failure(task_id=task_id, attempt_id=attempt_uuid,
                                      failure_class="UNKNOWN",
                                      reason_code=exc.reason_code, reason=str(exc))
            return {"status": "unknown_failure", "task_id": task_id,
                    "attempt_id": attempt_uuid, "reason_code": exc.reason_code,
                    "reason": str(exc),
                    "seed_fingerprint": seed_fingerprint,
                    "watchdog": watchdog, "stderr_record": stderr_record}
        except RuntimeError as exc:
            store.record_task_failure(task_id=task_id, attempt_id=attempt_uuid,
                                      failure_class="UNKNOWN",
                                      reason_code="G0_UNCLASSIFIED_EXCEPTION",
                                      reason=str(exc))
            return {"status": "unknown_failure", "task_id": task_id,
                    "attempt_id": attempt_uuid, "seed_fingerprint": seed_fingerprint,
                    "watchdog": watchdog, "stderr_record": stderr_record}
        if watchdog.get("status") != "completed" or watchdog.get("returncode") != 0:
            store.record_task_failure(task_id=task_id, attempt_id=attempt_uuid,
                                      failure_class="UNKNOWN",
                                      reason_code="G0_WATCHDOG_TERMINAL_MISMATCH",
                                      reason="Worker result exists without a completed watchdog exit")
            return {"status": "unknown_failure", "task_id": task_id,
                    "attempt_id": attempt_uuid, "watchdog": watchdog,
                    "stderr_record": stderr_record}

        expected_stream_metadata = {
            "stream_format": _AUDIT_STREAM_FORMAT,
            "record_count": 4 * graph.m,
            "chain_tip_sha256": audit_tip,
            "complete": True,
            "trailing_partial_bytes": 0,
        }
        if stream_metadata != expected_stream_metadata:
            store.record_task_failure(
                task_id=task_id, attempt_id=attempt_uuid,
                failure_class="SCIENTIFIC",
                reason_code="G0_PROPOSAL_AUDIT_STREAM_INCOMPLETE",
                reason="External proposal trace differs from the worker's complete count/tip")
            return {"status": "scientific_failure", "task_id": task_id,
                    "attempt_id": attempt_uuid,
                    "reason_code": "G0_PROPOSAL_AUDIT_STREAM_INCOMPLETE",
                    "seed_fingerprint": seed_fingerprint,
                    "watchdog": watchdog, "stderr_record": stderr_record,
                    "audit_record": audit_record}
        final_graph_payload = {"format": "G0_NULL_GRAPH_V1",
                               "nodes": [_node_record(node) for node in graph.nodes],
                               "edges": [list(edge) for edge in final_edges]}
        final_graph_bytes = gzip.compress(canonical_json(final_graph_payload), mtime=0)
        checkpoint_path = f"checkpoints/{task_id}/{attempt_uuid}/4E-graph.json.gz"
        checkpoint_record = store.write_immutable_artifact(
            relative_path=checkpoint_path, artifact_kind="checkpoint",
            identity={"task_id": task_id, "attempt_id": attempt_uuid,
                      "graph_sha256": result["null_graph_sha256"],
                      "checkpoint": "4E", "seed_fingerprint": seed_fingerprint},
            chunks=final_graph_bytes)
        result["environment"] = environment
        result["runtime_accounting"] = {
            "watchdog": watchdog.get("usage"),
            "watchdog_invocation_id": invocation_id,
            "executor_parent_wall_seconds": time.perf_counter() - began,
            "executor_parent_process_cpu_seconds": max(0.0, time.process_time() - before_cpu),
            "watchdog_control_ledger_tip_sha256": watchdog.get("control_ledger_tip_sha256"),
        }
        result["artifacts"] = {"source_graph": source_record,
                               "proposal_audit": audit_record,
                               "null_graph_checkpoint": checkpoint_record,
                               "runner_stderr": stderr_record,
                               "worker_config_sha256": config_sha256,
                               "watchdog_stdout_sha256": stdout_hash,
                               "proposal_audit_tip_sha256": audit_tip}
        result_bytes = canonical_json(result)
        completion = store.complete_task_result(
            task_id=task_id, attempt_id=attempt_uuid,
            seed_fingerprint=seed_fingerprint, payload=result_bytes)
        if store.task_recovery_state(task_id=task_id,
                                     seed_fingerprint=seed_fingerprint) != "completed":
            raise G0ScientificFailure("G0_TASK_COMPLETION_NOT_VERIFIED",
                                      "Incremental task index does not accept committed completion")
        report = (store._incremental_recovery_report(expected_tasks)
                  if final_report else None)
        return {"status": "completed", "task_id": task_id,
                "attempt_id": attempt_uuid, "task_identity_sha256": task_identity_sha256,
                "result": result, "result_record": completion,
                "recovery_report": report, "watchdog": watchdog,
                "audit_record": audit_record}
    except (G0StorageError, RecoveryRefused):
        raise
    except BaseException as exc:
        # Exceptions not explicitly classified remain UNKNOWN. The storage
        # ledger must record them before a caller can inspect recovery state.
        try:
            state = store._task_state(task_id)
            if state["starts"] and not state["completions"] and not state["failures"]:
                store.record_task_failure(
                    task_id=task_id, attempt_id=attempt_uuid,
                    failure_class="UNKNOWN", reason_code="G0_UNCLASSIFIED_EXCEPTION",
                    reason=f"{type(exc).__name__}: {exc}")
        except BaseException:
            pass
        raise


def main(argv: list[str] | None = None) -> int:
    if len(sys.argv if argv is None else argv) == 8 and (sys.argv if argv is None else argv)[1] == "--worker":
        args = sys.argv if argv is None else argv
        return _worker_entry(Path(args[2]), args[3], Path(args[4]), Path(args[5]),
                             int(args[6]), int(args[7]))
    print("This module exposes only the synthetic task API; no biological G0 CLI exists.",
          file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
