"""Watchdog-supervised, fixed-order H3 identity pilot launcher.

The production entry point is deliberately gated by a UUID/HEAD/package-bound
researcher confirmation. Synthetic integration mode uses only generated
graphs and virtual Q references and cannot open the private RIKEN roots.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import secrets
import subprocess
import sys
import time
import uuid
from typing import Any, Iterable

from nc0a_watchdog import (
    HashChainLog,
    WatchdogError,
    WatchdogLimits,
    guard_watchdog_parent,
    supervise,
    supervised_activity_lock,
    verify_hash_chain,
)
from riken_source_identity import (
    EXPECTED_HISTORICAL_GRAPH_FUNCTION_SHA256,
    EXPECTED_SOURCE_CODE_HASHES,
    H3_PILOT_CPU_SECONDS,
    H3_PILOT_MAX_WORKERS,
    H3_PILOT_OUTPUT_BYTES,
    H3_PILOT_RSS_BYTES,
    H3_PILOT_WALL_SECONDS,
    H3_QMAX_ATOL,
    H3_TRIAL_Q_ATOL_PROPOSED,
    LOUVAIN_TRIALS,
    TARGETS,
    IdentityEvidenceError,
    hash_float64,
    hash_int64,
    h3_runtime_manifest,
    load_h3_reference,
    reconstruct_source_graph,
    run_h3_replay_for_graph,
    sha256_bytes,
    sha256_file,
    validate_h3_replay,
)


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
PILOT_FILENAME = "G0_RIKEN_H3_CALIBRATION_PILOT_2026-10-21.json"
MANIFEST_FILENAME = "G0_RIKEN_SOURCE_GRAPH_EXPECTED_MANIFEST_2026-10-21.json"
EXPECTED_PILOT_SHA256 = "286fa084f125d205463218951e3ccf2640701dc7712a9a48cec62b323a49c36b"
EXPECTED_MANIFEST_SHA256 = "6a8357ac0b815c434421a31dc6c294c292b5c144713f49c52b5344038235ece2"
EXPECTED_IDENTITY_TOOL_SHA256 = "ba7c855c1744fcfa1f94dc3d6ffe79cf4196695af1d6d5803beffc83d9c5d73e"
EXPECTED_GRAPH_IDS = (
    "mouse01_sleep|N100|rep-055|wake|window-000",
    "mouse01_sleep|N150|rep-070|wake|window-000",
    "mouse01_sleep|N225|rep-033|wake|window-000",
    "mouse01_sleep|N340|rep-083|wake|window-000",
    "mouse01_sleep|N510|rep-067|wake|window-000",
    "mouse01_sleep|N765|rep-021|wake|window-000",
    "mouse01_sleep|N1150|rep-089|wake|window-000",
    "mouse01_sleep|N1725|rep-014|wake|window-000",
    "mouse01_sleep|N2600|rep-045|wake|window-000",
    "mouse01_sleep|N3900|rep-070|wake|window-000",
)
LIMITS = {
    "wall_seconds": H3_PILOT_WALL_SECONDS,
    "process_tree_cpu_seconds": H3_PILOT_CPU_SECONDS,
    "max_compute_workers": H3_PILOT_MAX_WORKERS,
    "sampled_aggregate_rss_bytes": H3_PILOT_RSS_BYTES,
    "output_bytes": H3_PILOT_OUTPUT_BYTES,
}
_HOST_LEDGER = "h3-host-activity.jsonl"
_HOST_LOCK = "h3-host-activity.lock"
_EVIDENCE_LOG = "h3-evidence.jsonl"
_CONTROL_LOG = "h3-control.jsonl"
_WATCHDOG_LOG = "watchdog.jsonl"
_SUMMARY = "h3-summary.json"
_LEASE = "h3-active-lease.json"


class H3PilotError(RuntimeError):
    """Fail-closed error in H3 pilot preparation, execution, or recovery."""


def _canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def _read_json(path: Path) -> dict[str, Any]:
    if path.is_symlink() or not path.is_file():
        raise H3PilotError(f"Required JSON file is missing or symlinked: {path.name}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise H3PilotError(f"Cannot parse required JSON: {path.name}") from exc
    if not isinstance(value, dict):
        raise H3PilotError(f"Expected JSON object: {path.name}")
    return value


def _write_new_json(path: Path, value: object) -> str:
    if path.exists() or path.is_symlink():
        raise H3PilotError(f"Refusing to overwrite {path.name}")
    payload = _canonical(value) + b"\n"
    temp = path.with_name(path.name + ".tmp-" + secrets.token_hex(8))
    fd = os.open(temp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        view = memoryview(payload)
        while view:
            written = os.write(fd, view)
            if written <= 0:
                raise OSError("short JSON write")
            view = view[written:]
        os.fsync(fd)
    finally:
        os.close(fd)
    try:
        os.link(temp, path)
        os.chmod(path, 0o600)
        dir_fd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
    except FileExistsError as exc:
        raise H3PilotError(f"Refusing concurrent overwrite of {path.name}") from exc
    finally:
        temp.unlink(missing_ok=True)
    return hashlib.sha256(payload).hexdigest()


def _replace_json(path: Path, value: object) -> str:
    if path.is_symlink():
        raise H3PilotError(f"Refusing symlink at {path.name}")
    payload = _canonical(value) + b"\n"
    temp = path.with_name(path.name + ".tmp-" + secrets.token_hex(8))
    fd = os.open(temp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        view = memoryview(payload)
        while view:
            written = os.write(fd, view)
            if written <= 0:
                raise OSError("short JSON replacement write")
            view = view[written:]
        os.fsync(fd)
    finally:
        os.close(fd)
    os.replace(temp, path)
    dir_fd = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(dir_fd)
    finally:
        os.close(dir_fd)
    return hashlib.sha256(payload).hexdigest()


def default_host_state_dir() -> Path:
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "SRT-Pub" / "h3-state"
    state_home = Path(os.environ.get("XDG_STATE_HOME", Path.home() / ".local/state"))
    return state_home / "srt-pub" / "h3-state"


@contextmanager
def _host_lock(state_dir: Path):
    try:
        with supervised_activity_lock() as activity_lock_fd:
            state_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
            if state_dir.is_symlink() or not state_dir.is_dir():
                raise H3PilotError("Host-state directory must be a real directory")
            state_dir.chmod(0o700)
            lock_path = state_dir / _HOST_LOCK
            if lock_path.is_symlink():
                raise H3PilotError("Host activity lock cannot be a symlink")
            fd = os.open(lock_path, os.O_RDWR | os.O_CREAT |
                         getattr(os, "O_NOFOLLOW", 0), 0o600)
            try:
                if not os.path.isfile(lock_path) or os.fstat(fd).st_nlink != 1:
                    raise H3PilotError("Host activity lock must be a single regular file")
                os.fchmod(fd, 0o600)
                try:
                    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                except BlockingIOError as exc:
                    raise H3PilotError(
                        "Another H3 pilot activity holds the host-wide lock") from exc
                yield activity_lock_fd
            finally:
                try:
                    fcntl.flock(fd, fcntl.LOCK_UN)
                finally:
                    os.close(fd)
    except WatchdogError as exc:
        raise H3PilotError(str(exc)) from exc


def _verified_host_events(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    if path.is_symlink() or not path.is_file():
        raise H3PilotError("Host activity ledger is not a regular file")
    try:
        verify_hash_chain(path)
        events = []
        for line in path.read_text(encoding="utf-8").splitlines():
            item = json.loads(line)
            event = item["event"]
            if not isinstance(event, dict):
                raise ValueError("event is not an object")
            events.append(event)
        return events
    except (WatchdogError, OSError, ValueError, KeyError, TypeError) as exc:
        raise H3PilotError("Host activity ledger is damaged; manual audit required") from exc


def _assert_host_ledger_allows(events: list[dict[str, Any]], pilot_sha256: str) -> None:
    starts: dict[str, dict[str, Any]] = {}
    finished: set[str] = set()
    prior_hashes: set[str] = set()
    for event in events:
        kind, run_id = event.get("kind"), event.get("run_id")
        if kind == "activity_started" and isinstance(run_id, str):
            if run_id in starts:
                raise H3PilotError("Duplicate host-ledger activity start")
            starts[run_id] = event
            prior_hashes.add(str(event.get("pilot_sha256")))
        elif kind == "activity_finished" and isinstance(run_id, str):
            if run_id not in starts or run_id in finished:
                raise H3PilotError("Host-ledger terminal event has no unique start")
            finished.add(run_id)
    unfinished = sorted(set(starts) - finished)
    if unfinished:
        prior = starts[unfinished[0]]
        lease = Path(str(prior.get("run_directory", ""))) / _LEASE
        if lease.is_file() and not lease.is_symlink():
            try:
                doc = _read_json(lease)
                pgid = int(doc.get("process_group_id", 0))
                if pgid > 1:
                    try:
                        os.killpg(pgid, 0)
                    except ProcessLookupError:
                        pass
                    except PermissionError as exc:
                        raise H3PilotError(
                            "Prior H3 process group may still be alive; refusing launch") from exc
                    else:
                        raise H3PilotError(
                            "Prior H3 process group remains; refusing launch and recovery")
            except (OSError, ValueError, TypeError) as exc:
                raise H3PilotError("Prior H3 lease is unreadable; manual audit required") from exc
        raise H3PilotError("Prior H3 activity has no terminal record; recovery is audit-only")
    if pilot_sha256 in prior_hashes:
        raise H3PilotError("This fixed H3 pilot packet already has a recorded attempt")


def validate_pilot_bundle(pilot_path: Path, manifest_path: Path, *,
                          expected_pilot_sha256: str = EXPECTED_PILOT_SHA256,
                          expected_manifest_sha256: str = EXPECTED_MANIFEST_SHA256
                          ) -> tuple[dict[str, Any], dict[str, Any]]:
    if pilot_path.is_symlink() or manifest_path.is_symlink():
        raise H3PilotError("H3 packet or manifest cannot be a symlink")
    if sha256_file(pilot_path) != expected_pilot_sha256:
        raise H3PilotError("H3 pilot packet SHA-256 differs from the fixed packet")
    if sha256_file(manifest_path) != expected_manifest_sha256:
        raise H3PilotError("H3 identity manifest SHA-256 differs from the fixed manifest")
    pilot, manifest = _read_json(pilot_path), _read_json(manifest_path)
    if (pilot.get("schema") != "SRT_RIKEN_H3_IDENTITY_CALIBRATION_PILOT_V1" or
            pilot.get("status") != "PREPARED_NOT_APPROVED_NOT_EXECUTED"):
        raise H3PilotError("H3 pilot packet schema/status is not the fixed prepared state")
    if (pilot.get("source_manifest_sha256") != expected_manifest_sha256 or
            pilot.get("source_manifest_identity_tool_sha256") !=
            EXPECTED_IDENTITY_TOOL_SHA256 or
            pilot.get("pilot_preparation_tool_sha256") != EXPECTED_IDENTITY_TOOL_SHA256 or
            pilot.get("historical_graph_builder_function_sha256") !=
            EXPECTED_HISTORICAL_GRAPH_FUNCTION_SHA256 or
            pilot.get("historical_graph_builder_sha256") !=
            EXPECTED_SOURCE_CODE_HASHES["multirecording_primary.py"]):
        raise H3PilotError("H3 packet does not bind the reviewed manifest and historical code")
    comparison = pilot.get("scientific_comparison", {})
    if comparison != {
        "first_max_index_must_match": True,
        "historical_order_is_authoritative": True,
        "qmax_absolute_tolerance": H3_QMAX_ATOL,
        "tolerance_status": "PROPOSED_FOR_REVIEW_NOT_YET_RESEARCHER_APPROVED",
        "trial_q_absolute_tolerance_proposed": H3_TRIAL_Q_ATOL_PROPOSED,
        "trial_q_relative_tolerance": 0.0,
    }:
        raise H3PilotError("H3 comparison rule differs from the prepared fixed proposal")
    if pilot.get("candidate_limits_not_authorized") != {
        "louvain_trials_total": 4000,
        "max_compute_workers": H3_PILOT_MAX_WORKERS,
        "output_bytes": H3_PILOT_OUTPUT_BYTES,
        "process_tree_cpu_seconds": H3_PILOT_CPU_SECONDS,
        "sampled_aggregate_rss_bytes": H3_PILOT_RSS_BYTES,
        "wall_seconds": H3_PILOT_WALL_SECONDS,
    }:
        raise H3PilotError("Candidate resource ceilings differ from the fixed pilot packet")
    if (manifest.get("schema") != "SRT_RIKEN_G0_SOURCE_IDENTITY_MANIFEST_V1" or
            manifest.get("identity_tool_sha256") != EXPECTED_IDENTITY_TOOL_SHA256 or
            manifest.get("graph_builder", {}).get("historical_function_sha256") !=
            EXPECTED_HISTORICAL_GRAPH_FUNCTION_SHA256):
        raise H3PilotError("H3 identity manifest differs from the reviewed source inventory")
    records = pilot.get("records")
    panel = manifest.get("h3_panel", {}).get("records")
    if not isinstance(records, list) or len(records) != len(EXPECTED_GRAPH_IDS):
        raise H3PilotError("H3 pilot must contain exactly ten fixed rows")
    if not isinstance(panel, list):
        raise H3PilotError("Identity manifest lacks the H3 reference panel")
    panel_by_id = {row.get("graph_id"): row for row in panel}
    source_by_id = {row.get("recording_id"): row for row in manifest.get("source_data", [])}
    actual_ids = tuple(str(row.get("graph_id")) for row in records)
    if actual_ids != EXPECTED_GRAPH_IDS:
        raise H3PilotError("H3 pilot graph order or identity differs from the fixed ten-row order")
    for index, row in enumerate(records):
        if row.get("pilot_order") != index + 1 or row.get("N") != TARGETS[index]:
            raise H3PilotError("H3 pilot order or N coordinate changed")
        ref = panel_by_id.get(row["graph_id"])
        source = source_by_id.get(row.get("recording_id"))
        if ref is None or source is None:
            raise H3PilotError("H3 pilot row is absent from the frozen source manifest")
        pairs = (
            (row.get("recording_id"), ref.get("recording_id")),
            (row.get("N"), ref.get("N")),
            (row.get("subset_repeat"), ref.get("subset_repeat")),
            (row.get("state"), ref.get("state")),
            (row.get("window_id"), ref.get("window_id")),
            (row.get("source_mat_sha256"), ref.get("source_artifact_sha256")),
            (row.get("source_mat_sha256"), source.get("sha256")),
            (row.get("selected_neuron_indices_sha256"),
             ref.get("selected_neuron_indices_sha256")),
            (row.get("expected_node_order_sha256"), ref.get("expected_node_order_sha256")),
            (row.get("source_frame_indices_sha256"), ref.get("source_frame_indices_sha256")),
            (row.get("expected_edge_count"), ref.get("expected_edge_count")),
            (row.get("historical_job_sha256"), ref.get("historical_job_sha256")),
            (row.get("historical_louvain_seed_vector_sha256"),
             ref.get("historical_louvain_seed_vector_sha256")),
            (row.get("historical_q_vector_sha256"), ref.get("historical_q_vector_sha256")),
            (row.get("historical_q_max_first_index"),
             ref.get("historical_q_max_first_index")),
        )
        if any(actual != expected for actual, expected in pairs):
            raise H3PilotError(f"H3 row identity differs from frozen manifest: {row['graph_id']}")
        if row.get("source_and_reference_status") != \
                "HASHES_AND_200_SEEDS_VERIFIED; GRAPH_NOT_REBUILT":
            raise H3PilotError("H3 packet does not declare the prepared source/reference state")
    runtime = h3_runtime_manifest()
    if not runtime["replay_environment_matches_recorded_versions_and_candidate_lock"]:
        raise H3PilotError("Current Python/platform/dependencies do not match the H3 replay lock")
    return pilot, manifest


def _is_contained(path: Path, root: Path) -> bool:
    try:
        path.resolve(strict=True).relative_to(root.resolve(strict=True))
        return True
    except (OSError, ValueError):
        return False


def _load_private_row(row: dict[str, Any], manifest: dict[str, Any],
                      phase2_root: Path, psa_root: Path,
                      source_hash_cache: dict[str, tuple[str, tuple[int, int, int, int]]] | None = None
                      ) -> tuple[Path, list[int], dict, dict]:
    from riken_source_identity import sha256_file as source_sha256_file

    source_record = next((item for item in manifest["source_data"]
                          if item["recording_id"] == row["recording_id"]), None)
    if source_record is None:
        raise IdentityEvidenceError("H3 source recording is absent from the manifest")
    filename = row["source_filename"]
    if Path(filename).name != filename or filename != source_record["filename"]:
        raise IdentityEvidenceError("H3 source filename escaped or changed")
    data_dir = phase2_root / "data"
    source_path = data_dir / filename
    if (data_dir.is_symlink() or source_path.is_symlink() or not source_path.is_file() or
            not _is_contained(source_path, phase2_root)):
        raise IdentityEvidenceError("H3 source MAT is missing or symlinked")
    stat_result = source_path.stat()
    signature = (stat_result.st_dev, stat_result.st_ino, stat_result.st_size,
                 stat_result.st_mtime_ns)
    cached = source_hash_cache.get(filename) if source_hash_cache is not None else None
    if cached is None:
        actual_source_sha = source_sha256_file(source_path)
        if source_hash_cache is not None:
            source_hash_cache[filename] = (actual_source_sha, signature)
    else:
        actual_source_sha, prior_signature = cached
        if signature != prior_signature:
            raise IdentityEvidenceError("H3 source MAT changed after preflight hashing")
    if actual_source_sha != row["source_mat_sha256"]:
        raise IdentityEvidenceError("H3 source MAT SHA-256 mismatch")
    ref = next((item for item in manifest["h3_panel"]["records"]
                if item["graph_id"] == row["graph_id"]), None)
    if ref is None:
        raise IdentityEvidenceError("H3 row is absent from the frozen H3 panel")
    reference = load_h3_reference(ref, psa_root)
    job_path = psa_root / "jobs" / (
        f"{row['recording_id']}__N{row['N']}__rep-{row['subset_repeat']:03d}.json")
    if not _is_contained(job_path, psa_root):
        raise IdentityEvidenceError("H3 historical job escaped the private PS-A root")
    job = _read_json(job_path)
    selected = job.get("selected_neuron_indices_zero_based")
    if (not isinstance(selected, list) or len(selected) != row["N"] or
            any(type(value) is not int for value in selected) or
            selected != sorted(set(selected)) or
            hash_int64(selected) != row["selected_neuron_indices_sha256"] or
            hash_int64(selected) != row["expected_node_order_sha256"]):
        raise IdentityEvidenceError("H3 selected-neuron subset identity mismatch")
    if (hash_int64(reference["louvain_seeds"]) !=
            row["historical_louvain_seed_vector_sha256"] or
            hash_float64(reference["q_values"]) != row["historical_q_vector_sha256"] or
            reference["historical_job_sha256"] != row["historical_job_sha256"]):
        raise IdentityEvidenceError("H3 saved seeds/Q/job identity mismatch")
    historical_builder = phase2_root / "multirecording_primary.py"
    if (historical_builder.is_symlink() or not historical_builder.is_file() or
            not _is_contained(historical_builder, phase2_root)):
        raise IdentityEvidenceError("Historical graph builder source is missing or symlinked")
    if source_sha256_file(historical_builder) != EXPECTED_SOURCE_CODE_HASHES[
            "multirecording_primary.py"]:
        raise IdentityEvidenceError("Historical graph builder source hash mismatch")
    return source_path, selected, reference, ref


def _trial_deltas(actual: Iterable[float], expected: Iterable[float]) -> list[float]:
    a, b = list(map(float, actual)), list(map(float, expected))
    if len(a) != LOUVAIN_TRIALS or len(b) != LOUVAIN_TRIALS:
        raise H3PilotError("Expected exactly 200 trial Q values for delta evidence")
    deltas = [abs(x - y) for x, y in zip(a, b, strict=True)]
    if any(not math.isfinite(delta) for delta in deltas):
        raise H3PilotError("H3 Q difference contains a non-finite value")
    return deltas


def _set_active_task(run_dir: Path, graph_id: str) -> None:
    path = run_dir / "active_task.json"
    _replace_json(path, {"phase": "case", "started_utc_epoch": time.time(),
                         "task_id": graph_id})


def _run_real_rows(pilot: dict[str, Any], manifest: dict[str, Any],
                   phase2_root: Path, psa_root: Path, run_dir: Path) -> dict[str, Any]:
    from riken_source_identity import validate_h3_replay

    evidence_path = run_dir / _EVIDENCE_LOG
    with HashChainLog(evidence_path) as evidence:
        evidence.append({"kind": "pilot_runner_started", "run_id": os.environ["SRT_H3_RUN_ID"],
                         "pilot_sha256": EXPECTED_PILOT_SHA256,
                         "runner_sha256": sha256_file(Path(__file__)),
                         "runtime": h3_runtime_manifest()})
        outcomes = []
        source_hash_cache: dict[str, tuple[str, tuple[int, int, int, int]]] = {}
        for row in pilot["records"]:
            graph_id = row["graph_id"]
            _set_active_task(run_dir, graph_id)
            evidence.append({"kind": "graph_started", "pilot_order": row["pilot_order"],
                             "graph_id": graph_id, "N": row["N"],
                             "historical_job_sha256": row["historical_job_sha256"],
                             "selected_neuron_indices_sha256":
                                 row["selected_neuron_indices_sha256"],
                             "seed_vector_sha256":
                                 row["historical_louvain_seed_vector_sha256"],
                             "historical_q_vector_sha256": row["historical_q_vector_sha256"]})
            started = time.perf_counter()
            before = time.process_time()
            try:
                source_path, selected, reference, panel_row = _load_private_row(
                    row, manifest, phase2_root, psa_root, source_hash_cache)
                graph_pair = reconstruct_source_graph(
                    source_path, selected, row["state"], row["window_id"],
                    phase2_root / "multirecording_primary.py")
                replay = run_h3_replay_for_graph(
                    graph_pair, panel_row, reference, require_target_runtime=True)
                validation = validate_h3_replay([panel_row], [replay],
                                                trial_q_atol=H3_TRIAL_Q_ATOL_PROPOSED)
                source_status = validation["source_graph_identity"]["status"]
                historical_status = validation["historical_order_q_replay"]["status"]
                executor_status = validation[
                    "executor_sorted_order_compatibility"]["status"]
                hist_deltas = _trial_deltas(replay["historical_builder_q_values"],
                                            reference["q_values"])
                sorted_deltas = _trial_deltas(replay["q_values"], reference["q_values"])
                outcome = {
                    "pilot_order": row["pilot_order"], "graph_id": graph_id,
                    "N": row["N"], "source_graph_identity": source_status,
                    "historical_order_q_replay": historical_status,
                    "executor_sorted_order_compatibility": executor_status,
                    "historical_edge_set_sha256": replay["historical_edge_set_sha256"],
                    "candidate_edge_set_sha256": replay["candidate_edge_set_sha256"],
                    "historical_labeled_edge_set_sha256":
                        replay["historical_labeled_edge_set_sha256"],
                    "historical_node_order_sha256": replay["historical_node_order_sha256"],
                    "historical_degree_sequence_sha256":
                        replay["historical_degree_sequence_sha256"],
                    "source_mat_sha256": row["source_mat_sha256"],
                    "selected_neuron_indices_sha256":
                        row["selected_neuron_indices_sha256"],
                    "source_frame_indices_sha256":
                        replay["reconstructed_source_frame_indices_sha256"],
                    "historical_job_sha256": reference["historical_job_sha256"],
                    "expected_edge_count": row["expected_edge_count"],
                    "historical_adjacency_iteration_sha256":
                        replay["historical_adjacency_iteration_sha256"],
                    "executor_sorted_adjacency_iteration_sha256":
                        replay["executor_sorted_adjacency_iteration_sha256"],
                    "seed_vector_sha256": hash_int64(reference["louvain_seeds"]),
                    "historical_q_vector_sha256": hash_float64(reference["q_values"]),
                    "historical_order_trial_q_abs_deltas": hist_deltas,
                    "sorted_order_trial_q_abs_deltas": sorted_deltas,
                    "historical_qmax": max(reference["q_values"]),
                    "historical_qmax_first_index": reference["q_max_first_index"],
                    "historical_replay_qmax": max(replay["historical_builder_q_values"]),
                    "historical_replay_first_max_index":
                        replay["historical_builder_q_max_first_index"],
                    "sorted_replay_qmax": max(replay["q_values"]),
                    "sorted_replay_first_max_index": replay["q_max_first_index"],
                    "elapsed_seconds": time.perf_counter() - started,
                    "process_cpu_seconds": time.process_time() - before,
                    "status": "completed" if source_status == "PASS" and
                             historical_status == "PASS" else "scientific_integrity_failure",
                }
            except (IdentityEvidenceError, H3PilotError, OSError, ValueError) as exc:
                outcome = {"pilot_order": row["pilot_order"], "graph_id": graph_id,
                           "N": row["N"], "status": "identity_or_reference_failure",
                           "failure_type": type(exc).__name__,
                           "failure_reason": str(exc)[:500],
                           "elapsed_seconds": time.perf_counter() - started,
                           "process_cpu_seconds": time.process_time() - before}
            evidence.append({"kind": "graph_result", **outcome})
            outcomes.append(outcome)
            if outcome["status"] != "completed":
                terminal = {"kind": "pilot_stopped", "status": outcome["status"],
                            "failure_graph_id": graph_id, "resume_allowed": False}
                evidence.append(terminal)
                _replace_json(run_dir / "runner-terminal.json", terminal)
                return {"status": outcome["status"], "outcomes": outcomes,
                        "evidence_tip_sha256": evidence.previous}
            if outcome["executor_sorted_order_compatibility"] == "INCOMPLETE_OR_INVALID":
                terminal = {"kind": "pilot_stopped", "status": "executor_diagnostic_incomplete",
                            "failure_graph_id": graph_id, "resume_allowed": False}
                evidence.append(terminal)
                _replace_json(run_dir / "runner-terminal.json", terminal)
                return {"status": "executor_diagnostic_incomplete", "outcomes": outcomes,
                        "evidence_tip_sha256": evidence.previous}
        terminal = {"kind": "pilot_completed", "status": "completed",
                    "rows_completed": len(outcomes), "resume_allowed": False,
                    "scientific_interpretation": "HISTORICAL_OBSERVATION_Q_IDENTITY_ONLY"}
        evidence.append(terminal)
        _replace_json(run_dir / "runner-terminal.json", terminal)
        return {"status": "completed", "outcomes": outcomes,
                "evidence_tip_sha256": evidence.previous}


def _build_watchdog_limits(candidate: dict[str, Any], *, test_overrides: dict | None = None
                           ) -> WatchdogLimits:
    values = {
        "wall_seconds": float(candidate["wall_seconds"]),
        "cpu_seconds": float(candidate["process_tree_cpu_seconds"]),
        "aggregate_rss_bytes": int(candidate["sampled_aggregate_rss_bytes"]),
        "max_workers": int(candidate["max_compute_workers"]),
        "run_disk_bytes": int(candidate["output_bytes"]),
        "reserve_free_disk_bytes": 1,
        "case_seconds": float(candidate["wall_seconds"]),
        "oracle_seconds": float(candidate["wall_seconds"]),
        "memory_enforcement_backend": "SAMPLED_ONLY",
        "poll_seconds": 0.5,
    }
    if test_overrides:
        values.update(test_overrides)
    return WatchdogLimits(**values)


def _git_identity(expected_head: str) -> dict[str, str]:
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              check=True, capture_output=True, text=True).stdout.strip()
        status = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all"],
                                cwd=ROOT, check=True, capture_output=True,
                                text=True).stdout
    except (OSError, subprocess.SubprocessError) as exc:
        raise H3PilotError("Cannot verify repository execution identity") from exc
    if head != expected_head or status.strip():
        raise H3PilotError("Expected clean, locked Git HEAD does not match current checkout")
    return {"head_sha": head, "working_tree": "CLEAN"}


def _prepare_run_directory(run_dir: Path, psa_root: Path) -> None:
    if psa_root.is_symlink():
        raise H3PilotError("PS-A output root must not be a symlink")
    root = psa_root.resolve(strict=True)
    if not root.is_dir():
        raise H3PilotError("PS-A output root must be a mounted, non-symlink directory")
    target = run_dir.absolute()
    expected_parent = root / "h3_identity_calibration_2026-10-21"
    if target.parent.parent.resolve(strict=False) != expected_parent:
        raise H3PilotError("H3 run directory must be under the fixed private PSA output root")
    if target.exists() or target.is_symlink():
        raise H3PilotError("H3 output directory must be new and empty; refusing reuse")
    target.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    if target.parent.is_symlink():
        raise H3PilotError("H3 output parent cannot be a symlink")


def _load_child_result(run_dir: Path) -> dict[str, Any] | None:
    path = run_dir / "runner-terminal.json"
    if not path.exists():
        return None
    return _read_json(path)


def _launch_supervised(command: list[str], *, run_dir: Path, state_dir: Path,
                       pilot_sha256: str, run_id: str, head: dict[str, str],
                       candidate: dict[str, Any], env_extra: dict[str, str] | None = None,
                       limits: WatchdogLimits | None = None) -> dict[str, Any]:
    try:
        if str(uuid.UUID(run_id)) != run_id:
            raise ValueError("noncanonical UUID")
    except (ValueError, TypeError, AttributeError) as exc:
        raise H3PilotError("H3 pilot run identity must be a canonical UUID") from exc
    run_dir = run_dir.absolute()
    state_dir = state_dir.absolute()
    ledger_path = state_dir / _HOST_LEDGER
    token = secrets.token_hex(32)
    with _host_lock(state_dir) as activity_lock_fd:
        events = _verified_host_events(ledger_path)
        _assert_host_ledger_allows(events, pilot_sha256)
        if run_dir.exists() or run_dir.is_symlink():
            raise H3PilotError("Run directory exists; H3 pilot attempts cannot be overwritten")
        run_dir.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        run_dir.mkdir(mode=0o700)
        started = {"kind": "activity_started", "run_id": run_id,
                   "pilot_sha256": pilot_sha256, "head_sha": head["head_sha"],
                   "run_directory": str(run_dir), "started_utc":
                       datetime.now(timezone.utc).isoformat(), "lease_token": token}
        with HashChainLog(ledger_path) as host_log:
            host_log.append(started)
            with HashChainLog(run_dir / _CONTROL_LOG) as control:
                control.append({"kind": "activity_started", "run_id": run_id,
                                "pilot_sha256": pilot_sha256,
                                "head_sha": head["head_sha"],
                                "limits": candidate})
                _write_new_json(run_dir / "run-manifest.json", {
                    "schema": "SRT_RIKEN_H3_SUPERVISED_RUN_V1",
                    "status": "STARTED",
                    "run_id": run_id,
                    "pilot_sha256": pilot_sha256,
                    "head": head,
                    "runner_sha256": sha256_file(Path(__file__)),
                    "identity_tool_sha256": sha256_file(HERE / "riken_source_identity.py"),
                    "runtime": h3_runtime_manifest(),
                    "candidate_limits_not_authorized_in_packet": candidate,
                    "memory_enforcement": "SAMPLED_ONLY_NOT_HARD",
                    "created_utc": datetime.now(timezone.utc).isoformat(),
                })
                env = os.environ.copy()
                env.update({"SRT_H3_RUN_ID": run_id,
                            "SRT_H3_PILOT_SHA256": pilot_sha256,
                            "SRT_H3_LEASE_TOKEN": token,
                            "SRT_H3_LEASE_PATH": str(run_dir / _LEASE)})
                if env_extra:
                    env.update(env_extra)
                watchdog_result = None
                watchdog_exception = None
                started_clock = time.perf_counter()
                try:
                    watchdog_result = supervise(
                        command, run_dir=run_dir, limits=limits or
                        _build_watchdog_limits(candidate), audit_name=_WATCHDOG_LOG,
                        stdout_name="runner.stdout.log", invocation_id=1,
                        runner_is_compute_worker=True,
                        environment=env, _activity_lock_fd=activity_lock_fd,
                    )
                except BaseException as exc:
                    watchdog_exception = {"type": type(exc).__name__,
                                          "reason": str(exc)[:500]}
                runner_result = _load_child_result(run_dir)
                watchdog_audit_sha = None
                if (run_dir / _WATCHDOG_LOG).is_file():
                    try:
                        _, watchdog_audit_sha = verify_hash_chain(run_dir / _WATCHDOG_LOG)
                    except WatchdogError as exc:
                        watchdog_exception = {"type": "WatchdogAuditInvalid",
                                              "reason": str(exc)[:500]}
                evidence_sha = None
                evidence_tip = None
                if (run_dir / _EVIDENCE_LOG).is_file():
                    try:
                        _, evidence_tip = verify_hash_chain(run_dir / _EVIDENCE_LOG)
                        evidence_sha = sha256_file(run_dir / _EVIDENCE_LOG)
                    except WatchdogError as exc:
                        watchdog_exception = {"type": "EvidenceAuditInvalid",
                                              "reason": str(exc)[:500]}
                if watchdog_exception:
                    status = "FAILED_AUDIT_OR_WATCHDOG"
                    failure_category = "UNKNOWN_FAILURE"
                elif watchdog_result and watchdog_result["status"] == "stopped":
                    status = "STOPPED_BY_WATCHDOG"
                    failure_category = "OPERATIONAL_RESOURCE_STOP"
                elif (watchdog_result and watchdog_result["status"] == "completed" and
                      watchdog_result.get("returncode") == 0 and runner_result and
                      runner_result.get("status") == "completed"):
                    status = "COMPLETED"
                    failure_category = None
                elif runner_result and runner_result.get("status") in (
                        "scientific_integrity_failure", "identity_or_reference_failure"):
                    status = "STOPPED_ON_HISTORICAL_IDENTITY_FAILURE"
                    failure_category = "HISTORICAL_IDENTITY_FAILURE"
                elif runner_result and runner_result.get("status") == \
                        "executor_diagnostic_incomplete":
                    status = "STOPPED_ON_EXECUTOR_DIAGNOSTIC_INTEGRITY_FAILURE"
                    failure_category = "EXECUTOR_DIAGNOSTIC_INTEGRITY_FAILURE"
                elif watchdog_result and watchdog_result.get("returncode") not in (None, 0):
                    status = "FAILED_RUNNER_EXIT"
                    failure_category = "OPERATIONAL_FAILURE"
                else:
                    status = "FAILED_RUNNER_OR_OPERATION"
                    failure_category = "OPERATIONAL_OR_UNCLASSIFIED_FAILURE"
                summary = {
                    "schema": "SRT_RIKEN_H3_SUPERVISED_RUN_SUMMARY_V1",
                    "run_id": run_id, "pilot_sha256": pilot_sha256,
                    "head_sha": head["head_sha"], "status": status,
                    "failure_category": failure_category,
                    "resume_allowed": False,
                    "watchdog": watchdog_result,
                    "watchdog_exception": watchdog_exception,
                    "runner": runner_result,
                    "run_manifest_sha256": sha256_file(run_dir / "run-manifest.json"),
                    "runner_terminal_sha256": (
                        sha256_file(run_dir / "runner-terminal.json")
                        if (run_dir / "runner-terminal.json").is_file() else None),
                    "elapsed_controller_seconds": time.perf_counter() - started_clock,
                    "watchdog_audit_tip_sha256": watchdog_audit_sha,
                    "evidence_file_sha256": evidence_sha,
                    "evidence_tip_sha256": evidence_tip,
                    "memory_limit_semantics": "4_GIB_RSS_SAMPLED_NOT_HARD",
                    "created_utc": datetime.now(timezone.utc).isoformat(),
                }
                summary_sha = _write_new_json(run_dir / _SUMMARY, summary)
                control.append({"kind": "activity_finished", "run_id": run_id,
                                "status": status,
                                "failure_category": failure_category,
                                "summary_sha256": summary_sha,
                                "run_manifest_sha256": summary["run_manifest_sha256"],
                                "runner_terminal_sha256": summary["runner_terminal_sha256"],
                                "watchdog_audit_tip_sha256": watchdog_audit_sha,
                                "evidence_tip_sha256": evidence_tip})
                host_log.append({"kind": "activity_finished", "run_id": run_id,
                                 "pilot_sha256": pilot_sha256,
                                 "status": status,
                                 "failure_category": failure_category,
                                 "run_directory": str(run_dir),
                                 "summary_sha256": summary_sha,
                                 "run_manifest_sha256": summary["run_manifest_sha256"],
                                 "runner_terminal_sha256": summary["runner_terminal_sha256"],
                                 "wall_seconds": (watchdog_result or {}).get(
                                     "usage", {}).get("wall_seconds"),
                                 "cpu_seconds": (watchdog_result or {}).get(
                                     "usage", {}).get("cpu_seconds"),
                                 "watchdog_audit_tip_sha256": watchdog_audit_sha,
                                 "evidence_tip_sha256": evidence_tip,
                                 "finished_utc": datetime.now(timezone.utc).isoformat()})
                _replace_json(run_dir / _LEASE, {
                    "run_id": run_id, "pilot_sha256": pilot_sha256,
                    "lease_token": token, "state": "TERMINAL",
                    "terminal_status": status,
                    "updated_utc": datetime.now(timezone.utc).isoformat()})
                return summary


def _write_runner_lease(run_dir: Path) -> None:
    token = os.environ.get("SRT_H3_LEASE_TOKEN", "")
    run_id = os.environ.get("SRT_H3_RUN_ID", "")
    if len(token) != 64 or not run_id:
        raise H3PilotError("Watchdog lease identity is missing")
    _write_new_json(Path(os.environ["SRT_H3_LEASE_PATH"]), {
        "run_id": run_id, "pilot_sha256": os.environ.get("SRT_H3_PILOT_SHA256"),
        "lease_token": token, "state": "RUNNING", "runner_pid": os.getpid(),
        "process_group_id": os.getpgrp(),
        "started_utc": datetime.now(timezone.utc).isoformat()})


def _runner_child() -> int:
    try:
        parent_pid = int(os.environ.get("NC0A_WATCHDOG_PARENT_PID", "0"))
        guard_watchdog_parent(parent_pid)
        run_dir = Path.cwd()
        _write_runner_lease(run_dir)
        pilot_path = Path(os.environ["SRT_H3_PILOT_PATH"])
        manifest_path = Path(os.environ["SRT_H3_MANIFEST_PATH"])
        phase2_root = Path(os.environ["SRT_H3_PHASE2_ROOT"])
        psa_root = Path(os.environ["SRT_H3_PSA_ROOT"])
        pilot, manifest = validate_pilot_bundle(pilot_path, manifest_path)
        result = _run_real_rows(pilot, manifest, phase2_root, psa_root, run_dir)
        return 0 if result["status"] == "completed" else 31
    except BaseException as exc:
        try:
            run_dir = Path.cwd()
            evidence_path = run_dir / _EVIDENCE_LOG
            if evidence_path.is_file() and not evidence_path.is_symlink():
                with HashChainLog(evidence_path) as evidence:
                    evidence.append({"kind": "runner_exception",
                                     "type": type(exc).__name__,
                                     "reason": str(exc)[:500],
                                     "resume_allowed": False})
                    _replace_json(run_dir / "runner-terminal.json", {
                        "kind": "pilot_stopped", "status": "unclassified_exception",
                        "failure_type": type(exc).__name__, "resume_allowed": False,
                        "evidence_tip_sha256": evidence.previous})
        except BaseException:
            pass
        print(f"H3 runner stopped: {type(exc).__name__}: {str(exc)[:500]}",
              file=sys.stderr)
        return 32


def _verify_recovery_directory(run_dir: Path, *,
                              host_state_dir: Path | None = None) -> dict[str, Any]:
    """Audit-only recovery inspection; no H3 row is ever retried or resumed."""
    if run_dir.is_symlink() or not run_dir.is_dir():
        raise H3PilotError("Recovery directory is missing or symlinked")
    tips = {}
    for filename in (_CONTROL_LOG, _WATCHDOG_LOG, _EVIDENCE_LOG):
        path = run_dir / filename
        if path.exists():
            _, tips[filename] = verify_hash_chain(path)
    summary_path = run_dir / _SUMMARY
    summary = _read_json(summary_path) if summary_path.exists() else None
    complete = False
    if summary:
        manifest_path = run_dir / "run-manifest.json"
        terminal_path = run_dir / "runner-terminal.json"
        control_path = run_dir / _CONTROL_LOG
        run_manifest = _read_json(manifest_path) if manifest_path.exists() else None
        if (manifest_path.is_symlink() or not manifest_path.is_file() or
                run_manifest is None or
                sha256_file(manifest_path) != summary.get("run_manifest_sha256") or
                run_manifest.get("run_id") != summary.get("run_id") or
                run_manifest.get("pilot_sha256") != summary.get("pilot_sha256") or
                run_manifest.get("head", {}).get("head_sha") != summary.get("head_sha")):
            raise H3PilotError("Run manifest is missing or differs from its summary hash")
        if terminal_path.exists():
            if terminal_path.is_symlink() or sha256_file(terminal_path) != \
                    summary.get("runner_terminal_sha256"):
                raise H3PilotError("Runner terminal record differs from its summary hash")
        elif summary.get("runner_terminal_sha256") is not None:
            raise H3PilotError("Summary claims a missing runner terminal record")
        if control_path.is_symlink() or not control_path.is_file() or \
                _CONTROL_LOG not in tips:
            raise H3PilotError("Terminal run lacks a verifiable control hash chain")
        watchdog_path = run_dir / _WATCHDOG_LOG
        watchdog_events = [json.loads(line)["event"] for line in
                           watchdog_path.read_text(encoding="utf-8").splitlines()] \
            if watchdog_path.is_file() and not watchdog_path.is_symlink() else []
        stdout_path = run_dir / "runner.stdout.log"
        stdout_hashes = []
        for event in watchdog_events:
            usage = event.get("usage")
            digest = usage.get("runner_stdout_sha256") if isinstance(usage, dict) else None
            digest = digest or event.get("runner_stdout_sha256")
            if digest is not None:
                stdout_hashes.append(digest)
        if stdout_path.exists():
            if (stdout_path.is_symlink() or not stdout_path.is_file() or not stdout_hashes or
                    any(value != sha256_file(stdout_path) for value in stdout_hashes)):
                raise H3PilotError("Runner stdout is not authenticated by the Watchdog record")
        elif stdout_hashes:
            raise H3PilotError("Watchdog record references missing runner stdout")
        control_events = [json.loads(line)["event"] for line in
                          control_path.read_text(encoding="utf-8").splitlines()]
        started = [event for event in control_events
                   if event.get("kind") == "activity_started"]
        finished = [event for event in control_events
                    if event.get("kind") == "activity_finished"]
        summary_sha = sha256_file(summary_path)
        if (len(started) != 1 or len(finished) != 1 or
                started[0].get("run_id") != summary.get("run_id") or
                finished[0].get("run_id") != summary.get("run_id") or
                finished[0].get("summary_sha256") != summary_sha or
                finished[0].get("status") != summary.get("status") or
                finished[0].get("run_manifest_sha256") !=
                summary.get("run_manifest_sha256") or
                finished[0].get("runner_terminal_sha256") !=
                summary.get("runner_terminal_sha256") or
                finished[0].get("watchdog_audit_tip_sha256") !=
                summary.get("watchdog_audit_tip_sha256") or
                finished[0].get("evidence_tip_sha256") !=
                summary.get("evidence_tip_sha256")):
            raise H3PilotError("Control chain does not authenticate a unique closed summary")
        for filename, summary_key in (
                (_WATCHDOG_LOG, "watchdog_audit_tip_sha256"),
                (_EVIDENCE_LOG, "evidence_tip_sha256")):
            if tips.get(filename) != summary.get(summary_key):
                raise H3PilotError(f"{filename} tip differs from the terminal summary anchor")
        if host_state_dir is not None:
            host_events = _verified_host_events(host_state_dir / _HOST_LEDGER)
            host_started = [event for event in host_events
                            if event.get("kind") == "activity_started" and
                            event.get("run_id") == summary.get("run_id")]
            host_finished = [event for event in host_events
                             if event.get("kind") == "activity_finished" and
                             event.get("run_id") == summary.get("run_id")]
            if (len(host_started) != 1 or len(host_finished) != 1 or
                    host_started[0].get("pilot_sha256") != summary.get("pilot_sha256") or
                    host_started[0].get("head_sha") != summary.get("head_sha") or
                    Path(host_started[0].get("run_directory", "")).absolute() !=
                    run_dir.absolute() or
                    host_finished[0].get("summary_sha256") != summary_sha or
                    host_finished[0].get("status") != summary.get("status") or
                    host_finished[0].get("run_manifest_sha256") !=
                    summary.get("run_manifest_sha256") or
                    host_finished[0].get("runner_terminal_sha256") !=
                    summary.get("runner_terminal_sha256") or
                    host_finished[0].get("watchdog_audit_tip_sha256") !=
                    summary.get("watchdog_audit_tip_sha256") or
                    host_finished[0].get("evidence_tip_sha256") !=
                    summary.get("evidence_tip_sha256")):
                raise H3PilotError("Host ledger does not authenticate this run summary")
        if summary.get("status") == "COMPLETED":
            if (not terminal_path.is_file() or not summary.get("runner_terminal_sha256") or
                    tips.get(_WATCHDOG_LOG) is None or
                    tips.get(_EVIDENCE_LOG) is None or
                    tips[_WATCHDOG_LOG] != summary.get("watchdog_audit_tip_sha256") or
                    tips[_EVIDENCE_LOG] != summary.get("evidence_tip_sha256")):
                raise H3PilotError("Completed run is missing a required audit or terminal anchor")
            terminal = _read_json(terminal_path)
            evidence_events = [json.loads(line)["event"] for line in
                               (run_dir / _EVIDENCE_LOG).read_text(
                                   encoding="utf-8").splitlines()]
            graph_results = [event for event in evidence_events
                             if event.get("kind") == "graph_result"]
            terminal_events = [event for event in evidence_events
                               if event.get("kind") == "pilot_completed"]
            expected_real_ids = (
                EXPECTED_GRAPH_IDS if summary.get("pilot_sha256") ==
                EXPECTED_PILOT_SHA256 else tuple(
                    event.get("graph_id") for event in graph_results))
            if (terminal.get("kind") != "pilot_completed" or
                    terminal.get("status") != "completed" or
                    terminal.get("resume_allowed") is not False or
                    terminal.get("rows_completed") != len(graph_results) or
                    summary.get("runner") != terminal or
                    not graph_results or
                    tuple(event.get("graph_id") for event in graph_results) !=
                    expected_real_ids or
                    [event.get("pilot_order") for event in graph_results] !=
                    list(range(1, len(graph_results) + 1)) or
                    any(event.get("source_graph_identity") != "PASS" or
                        event.get("historical_order_q_replay") != "PASS"
                        for event in graph_results) or
                    not terminal_events or
                    terminal_events[-1].get("rows_completed") != len(graph_results) or
                    evidence_events[-1].get("kind") != "pilot_completed" or
                    (summary.get("pilot_sha256") == EXPECTED_PILOT_SHA256 and
                     len(graph_results) != len(EXPECTED_GRAPH_IDS))):
                raise H3PilotError("Completed evidence does not contain the full ordered H3 result")
            complete = summary.get("resume_allowed") is False
    return {"status": "VERIFIED_TERMINAL" if summary else "INCOMPLETE_NOT_RESUMABLE",
            "completed": complete, "hash_chain_tips": tips,
            "summary_sha256": sha256_file(summary_path) if summary else None,
            "resume_allowed": False}


# ---------------------------------------------------------------------------
# Synthetic-only integration helpers. They use an actual synthetic NetworkX
# graph and virtual, deterministic 200-value Q vectors; no biological loader
# or biological reference is reachable from this branch.

def _synthetic_row(index: int, *, executor_mismatch: bool = False,
                   historical_mismatch: bool = False,
                   source_mismatch: bool = False) -> dict[str, Any]:
    import networkx as nx

    n = 20
    graph = nx.cycle_graph(n)
    graph.add_edges_from((i, (i + 2) % n) for i in range(n))
    graph.add_edges_from((i, (i + 3) % n) for i in range(n))
    graph.add_edges_from((i, (i + 4) % n) for i in range(n))
    graph.add_edges_from((i, (i + 5) % n) for i in range(n))
    graph.add_edges_from((i, (i + 6) % n) for i in range(n))
    graph.add_edges_from((i, (i + 7) % n) for i in range(n))
    # Complete to E=160 without repeated edges.
    for i in range(n):
        for j in range(i + 1, n):
            if graph.number_of_edges() >= 160:
                break
            graph.add_edge(i, j)
        if graph.number_of_edges() >= 160:
            break
    if graph.number_of_edges() != 160 or not nx.is_connected(graph):
        raise AssertionError("synthetic graph must be connected with exactly 160 edges")
    edges = sorted(tuple(sorted(edge)) for edge in graph.edges)
    edge_hash = sha256_bytes(_canonical(edges))
    node_hash = hash_int64(range(n))
    adjacency = {node: list(graph.neighbors(node)) for node in graph.nodes}
    adjacency_hash = sha256_bytes(_canonical([[node, neighbors]
                                              for node, neighbors in adjacency.items()]))
    seeds = [stable for stable in range(1000 + index * LOUVAIN_TRIALS,
                                       1000 + (index + 1) * LOUVAIN_TRIALS)]
    reference_q = [0.1 + ((i * 31 + index * 7) % 137) / 1000 for i in range(LOUVAIN_TRIALS)]
    reference_q[80] = 0.9
    historical_q = list(reference_q)
    sorted_q = list(reference_q)
    if historical_mismatch:
        historical_q[0] += 0.01
    if executor_mismatch:
        sorted_q[0] += 0.01
    actual_source = "a" * 64
    expected_source = "b" * 64 if source_mismatch else actual_source
    expected = {
        "graph_id": f"SYNTHETIC_H3_N{n}_ROW{index + 1}", "N": n,
        "expected_edge_count": 160, "expected_node_order_sha256": node_hash,
        "source_artifact_sha256": expected_source,
        "selected_neuron_indices_sha256": node_hash,
        "source_frame_indices_sha256": "c" * 64,
        "expected_input_identity_sha256": "d" * 64,
        "historical_q_vector_sha256": hash_float64(reference_q),
        "historical_louvain_seed_vector_sha256": hash_int64(seeds),
        "historical_q_max_first_index": 80,
    }
    replay = {
        "graph_id": expected["graph_id"],
        "historical_edge_set_sha256": edge_hash,
        "candidate_edge_set_sha256": edge_hash,
        "historical_labeled_edge_set_sha256": edge_hash,
        "candidate_labeled_edge_set_sha256": edge_hash,
        "historical_node_order_sha256": node_hash,
        "candidate_node_order_sha256": node_hash,
        "source_artifact_sha256": actual_source,
        "selected_neuron_indices_sha256": node_hash,
        "expected_input_identity_sha256": "d" * 64,
        "expected_source_frame_indices_sha256": "c" * 64,
        "reconstructed_source_frame_indices_sha256": "c" * 64,
        "historical_builder_function_sha256": EXPECTED_HISTORICAL_GRAPH_FUNCTION_SHA256,
        "historical_N": n, "candidate_N": n,
        "historical_E": 160, "candidate_E": 160,
        "historical_adjacency_iteration_sha256": adjacency_hash,
        "candidate_adjacency_iteration_sha256": adjacency_hash,
        "executor_sorted_adjacency_iteration_sha256": "e" * 64,
        "historical_candidate_adjacency_order_equal": True,
        "historical_executor_adjacency_order_equal": False,
        "historical_degree_sequence_sha256": hash_int64(d for _, d in graph.degree()),
        "candidate_degree_sequence_sha256": hash_int64(d for _, d in graph.degree()),
        "louvain_seeds": seeds,
        "historical_builder_q_values": historical_q,
        "historical_builder_q_max_first_index": 80,
        "q_values": sorted_q,
        "historical_q_values": reference_q,
        "historical_q_max": 0.9,
        "historical_q_max_first_index": 80,
        "q_max_first_index": 80,
    }
    return {"expected": expected, "replay": replay}


def _synthetic_worker(payload_path: Path) -> int:
    parent_pid = int(os.environ.get("NC0A_WATCHDOG_PARENT_PID", "0"))
    guard_watchdog_parent(parent_pid)
    run_dir = Path.cwd()
    _write_runner_lease(run_dir)
    payload = _read_json(payload_path)
    scenario = str(payload.get("scenario", "normal"))
    if scenario in {"sleep", "cpu", "memory", "disk", "child_exit"}:
        if scenario == "sleep":
            time.sleep(float(payload.get("seconds", 5)))
            return 0
        if scenario == "cpu":
            deadline = time.monotonic() + float(payload.get("seconds", 5))
            value = 0
            while time.monotonic() < deadline:
                value = (value + 1) % 1000003
            return value % 2
        if scenario == "memory":
            blocks = []
            for _ in range(int(payload.get("blocks", 80))):
                blocks.append(bytearray(4 * 1024 * 1024))
                time.sleep(0.05)
            time.sleep(2)
            return 0
        if scenario == "disk":
            path = run_dir / "synthetic-over-cap.bin"
            with path.open("xb") as stream:
                for _ in range(int(payload.get("blocks", 128))):
                    stream.write(b"x" * 65536)
                    stream.flush()
                    os.fsync(stream.fileno())
                    time.sleep(0.02)
            return 0
        if scenario == "child_exit":
            return 17
    rows = payload.get("rows")
    if not isinstance(rows, list) or not rows:
        raise H3PilotError("Synthetic worker needs at least one generated row")
    with HashChainLog(run_dir / _EVIDENCE_LOG) as evidence:
        evidence.append({"kind": "pilot_runner_started", "synthetic_only": True,
                         "worker_count": 1,
                         "note": "generated NetworkX graph and virtual Q reference; no Louvain biology"})
        outcomes = []
        for index, flags in enumerate(rows):
            fixture = _synthetic_row(index, **flags)
            expected, replay = fixture["expected"], fixture["replay"]
            _set_active_task(run_dir, expected["graph_id"])
            started = time.perf_counter()
            report = validate_h3_replay([expected], [replay],
                                        trial_q_atol=H3_TRIAL_Q_ATOL_PROPOSED)
            source_status = report["source_graph_identity"]["status"]
            historical_status = report["historical_order_q_replay"]["status"]
            executor_status = report[
                "executor_sorted_order_compatibility"]["status"]
            reference_q = replay["historical_q_values"]
            outcome = {
                "pilot_order": index + 1, "graph_id": expected["graph_id"],
                "N": expected["N"], "source_graph_identity": source_status,
                "historical_order_q_replay": historical_status,
                "executor_sorted_order_compatibility": executor_status,
                "historical_edge_set_sha256": replay["historical_edge_set_sha256"],
                "historical_adjacency_iteration_sha256":
                    replay["historical_adjacency_iteration_sha256"],
                "executor_sorted_adjacency_iteration_sha256":
                    replay["executor_sorted_adjacency_iteration_sha256"],
                "seed_vector_sha256": hash_int64(replay["louvain_seeds"]),
                "historical_q_vector_sha256": hash_float64(reference_q),
                "historical_order_trial_q_abs_deltas": _trial_deltas(
                    replay["historical_builder_q_values"], reference_q),
                "sorted_order_trial_q_abs_deltas": _trial_deltas(
                    replay["q_values"], reference_q),
                "virtual_reference_only": True,
                "elapsed_seconds": time.perf_counter() - started,
                "process_cpu_seconds": 0.0,
                "status": "completed" if source_status == "PASS" and
                         historical_status == "PASS" else "scientific_integrity_failure",
            }
            evidence.append({"kind": "graph_result", **outcome})
            outcomes.append(outcome)
            if outcome["status"] != "completed":
                terminal = {"kind": "pilot_stopped", "status": outcome["status"],
                            "failure_graph_id": expected["graph_id"],
                            "resume_allowed": False}
                evidence.append(terminal)
                _replace_json(run_dir / "runner-terminal.json", terminal)
                return 31
            if executor_status == "INCOMPLETE_OR_INVALID":
                terminal = {"kind": "pilot_stopped",
                            "status": "executor_diagnostic_incomplete",
                            "failure_graph_id": expected["graph_id"],
                            "resume_allowed": False}
                evidence.append(terminal)
                _replace_json(run_dir / "runner-terminal.json", terminal)
                return 31
        terminal = {"kind": "pilot_completed", "status": "completed",
                    "rows_completed": len(outcomes), "resume_allowed": False}
        evidence.append(terminal)
        _replace_json(run_dir / "runner-terminal.json", terminal)
    return 0


def launch_synthetic_test(*, run_dir: Path, state_dir: Path, scenario: str = "normal",
                          rows: list[dict[str, bool]] | None = None,
                          pilot_sha256: str | None = None,
                          test_limits: dict[str, Any] | None = None) -> dict[str, Any]:
    """Exercise the same host lock + watchdog + audit path with synthetic-only inputs."""
    run_id = str(uuid.uuid4())
    payload = {"scenario": scenario, "rows": rows or [{}, {}]}
    payload_sha = sha256_bytes(_canonical(payload))
    pilot_sha = pilot_sha256 or payload_sha
    run_dir = run_dir.absolute()
    state_dir = state_dir.absolute()
    state_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
    run_dir.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    payload_path = run_dir.parent / (run_dir.name + ".synthetic-fixture.json")
    _write_new_json(payload_path, payload)
    candidate = {"wall_seconds": 60.0, "process_tree_cpu_seconds": 60.0,
                 "max_compute_workers": 4, "sampled_aggregate_rss_bytes": 512 * 1024**2,
                 "output_bytes": 1024**2}
    values = {"wall_seconds": 60.0, "cpu_seconds": 60.0,
              "aggregate_rss_bytes": 512 * 1024**2, "max_workers": 4,
              "run_disk_bytes": 1024**2, "reserve_free_disk_bytes": 1,
              "case_seconds": 60.0, "oracle_seconds": 60.0,
              "poll_seconds": 0.05, "memory_enforcement_backend": "SAMPLED_ONLY"}
    if test_limits:
        values.update(test_limits)
    limits = WatchdogLimits(**values)
    env_extra = {"SRT_H3_SYNTHETIC_PAYLOAD": str(payload_path)}
    command = [sys.executable, str(Path(__file__).resolve()), "--synthetic-worker"]
    try:
        return _launch_supervised(command, run_dir=run_dir, state_dir=state_dir,
                                  pilot_sha256=pilot_sha, run_id=run_id,
                                  head={"head_sha": "synthetic-test-head",
                                        "working_tree": "TEST_ONLY"},
                                  candidate=candidate, env_extra=env_extra, limits=limits)
    finally:
        payload_path.unlink(missing_ok=True)


def launch_real_pilot(*, pilot_path: Path, manifest_path: Path,
                      phase2_root: Path, psa_root: Path, run_dir: Path,
                      state_dir: Path, run_id: str, expected_head: str,
                      researcher_confirmation: str) -> dict[str, Any]:
    validate_pilot_bundle(pilot_path, manifest_path)
    if run_dir.name != run_id:
        raise H3PilotError("Run directory basename must equal the frozen pilot UUID")
    if state_dir.expanduser().resolve(strict=False) != \
            default_host_state_dir().expanduser().resolve(strict=False):
        raise H3PilotError("Production H3 launches must use the fixed host-wide state ledger")
    confirmation = (f"I AUTHORIZE H3 PILOT {run_id} "
                    f"{EXPECTED_PILOT_SHA256} {expected_head}")
    if researcher_confirmation != confirmation:
        raise H3PilotError("UUID/package/HEAD-bound researcher confirmation is missing")
    head = _git_identity(expected_head)
    _prepare_run_directory(run_dir, psa_root)
    env_extra = {
        "SRT_H3_PILOT_PATH": str(pilot_path.resolve(strict=True)),
        "SRT_H3_MANIFEST_PATH": str(manifest_path.resolve(strict=True)),
        "SRT_H3_PHASE2_ROOT": str(phase2_root.resolve(strict=True)),
        "SRT_H3_PSA_ROOT": str(psa_root.resolve(strict=True)),
    }
    command = [sys.executable, str(Path(__file__).resolve()), "--runner-child"]
    return _launch_supervised(
        command, run_dir=run_dir, state_dir=state_dir,
        pilot_sha256=EXPECTED_PILOT_SHA256, run_id=run_id, head=head,
        candidate=LIMITS, env_extra=env_extra,
        limits=_build_watchdog_limits(LIMITS))


def _default_paths() -> tuple[Path, Path]:
    psa = Path(os.environ.get("SRT_PSA_ROOT", ""))
    phase2 = Path(os.environ.get("SRT_PHASE2_ROOT", ""))
    if not str(psa) or not str(phase2):
        raise H3PilotError("Set private SRT_PSA_ROOT and SRT_PHASE2_ROOT first")
    return phase2, psa


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pilot", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--run-directory", type=Path)
    parser.add_argument("--run-id")
    parser.add_argument("--expected-head")
    parser.add_argument("--researcher-confirmation")
    parser.add_argument("--runner-child", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--synthetic-worker", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--inspect-recovery", type=Path)
    args = parser.parse_args(argv)
    if args.runner_child:
        return _runner_child()
    if args.synthetic_worker:
        return _synthetic_worker(Path(os.environ["SRT_H3_SYNTHETIC_PAYLOAD"]))
    if args.inspect_recovery:
        print(json.dumps(_verify_recovery_directory(
            args.inspect_recovery, host_state_dir=default_host_state_dir()), sort_keys=True))
        return 0
    required = (args.pilot, args.manifest, args.run_directory, args.run_id,
                args.expected_head, args.researcher_confirmation)
    if any(item is None for item in required):
        parser.error("production launch requires pilot, manifest, run-directory, run-id, expected-head and researcher-confirmation")
    phase2_root, psa_root = _default_paths()
    result = launch_real_pilot(
        pilot_path=args.pilot, manifest_path=args.manifest,
        phase2_root=phase2_root, psa_root=psa_root, run_dir=args.run_directory,
        state_dir=default_host_state_dir(), run_id=args.run_id,
        expected_head=args.expected_head,
        researcher_confirmation=args.researcher_confirmation)
    print(json.dumps({key: result[key] for key in
                      ("run_id", "pilot_sha256", "head_sha", "status",
                       "failure_category", "resume_allowed")}, sort_keys=True))
    return 0 if result["status"] == "COMPLETED" else 2


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
