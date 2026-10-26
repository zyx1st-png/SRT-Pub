"""Observed-only resource calibration, separately gated; never a G0/null launcher.

Reuses H3's host admission, Watchdog, macOS policy and durable control transport.
Inherited private filenames h3-{control,evidence,summary} are transport names;
this module's event/result schemas identify OBSERVED_CALIBRATION, not H3 replay.
"""
from __future__ import annotations

import argparse
import fcntl
import gzip
import json
import os
import shutil
import sys
import time
import uuid
from dataclasses import replace
from pathlib import Path

import h3_120_supervised_panel as h3
import h3_supervised_pilot as pilot
import riken_source_identity as identity
from g0_q_protocol import (
    build_canonical_louvain_graph,
    first_maximum_index,
    heuristic_diagnostics,
    q_vector_sha256,
    seed_vector_sha256,
)
from nc0a_watchdog import (
    HashChainLog,
    WatchdogError,
    guard_watchdog_parent,
    verify_hash_chain,
)
from observed_calibration_measurement import (
    MeasurementError,
    Phase,
    PhaseRecords,
    RawWindowCache,
    _signature,
    measure_row,
    process_counters,
)
from observed_calibration_sample import (
    HERE,
    METHOD_FILENAME,
    METHOD_SHA256,
    RESOURCE_CANDIDATE,
    SAMPLE_FILENAME,
    SOURCE_SHA256,
    canonical,
    validate_sample,
)

EXPECTED_SAMPLE_SHA256 = "f29acb99a05387b128f724bf818e3f402f7ced8a4080c12da4a936b9284d95c4"
OUTPUT_PARENT = "canonical_observed_resource_calibration_2026-10-26"
MACOS_POLICY = {key: value for key, value in pilot.H3_MACOS_RESOURCE_POLICY_CANDIDATE.items()
                if key != "status"}
EVIDENCE = "h3-evidence.jsonl"
ROW_DIR = "observed-cost-rows"


def native_thread_environment() -> dict:
    # Record/freeze existing settings without changing numerical reduction semantics.
    return {key: os.environ.get(key) for key in (
        "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
        "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")}


def bindings(head: str, run_id: str, run_dir: Path) -> dict:
    if str(uuid.UUID(run_id)) != run_id:
        raise ValueError("Canonical UUID required")
    if len(head) != 40 or any(c not in "0123456789abcdef" for c in head):
        raise ValueError("Full execution HEAD required")
    return {"head_sha": head, "run_uuid": run_id, "output_directory": str(run_dir),
            "sample_sha256": EXPECTED_SAMPLE_SHA256,
            "source_manifest_sha256": SOURCE_SHA256, "method_sha256": METHOD_SHA256,
            "runtime_lock_sha256": identity.sha256_file(HERE / "g0-runtime-macos-arm64.lock"),
            "q_protocol_sha256": identity.sha256_file(HERE / "g0_q_protocol.py"),
            "native_thread_environment": native_thread_environment(),
            "resource_limits": RESOURCE_CANDIDATE, "macos_policy": MACOS_POLICY,
            "scope": "47_FIXED_OBSERVED_GRAPHS_9400_CANONICAL_Q_NO_NULLS_NO_AUTORETRY"}


def confirmation_text(head: str, run_id: str) -> str:
    return f"I AUTHORIZE OBSERVED CALIBRATION {run_id} {EXPECTED_SAMPLE_SHA256} {head}"


def authorization_draft(head: str, run_id: str, run_dir: Path) -> dict:
    return {"schema": "SRT_OBSERVED_CALIBRATION_RESEARCHER_AUTHORIZATION_V1",
            "status": "PENDING_RESEARCHER_APPROVAL", "binding": bindings(head, run_id, run_dir),
            "researcher_confirmation": "", "researcher_identity": "", "confirmed_at_utc": "",
            "researcher_confirmed_risks": False, "no_automatic_retry": True,
            "resource_approval_record": "",
            "required_confirmation_not_yet_given": confirmation_text(head, run_id)}


def validate_authorization(path: Path, *, head: str, run_id: str,
                           run_dir: Path, confirmation: str) -> dict:
    expected = bindings(head, run_id, run_dir)
    auth = pilot._read_json(path)
    effective, method_sha = h3._method_is_effective(HERE / METHOD_FILENAME)
    if not effective or method_sha != METHOD_SHA256:
        raise ValueError("Effective canonical method identity mismatch")
    if (confirmation != confirmation_text(head, run_id) or
            auth.get("schema") != "SRT_OBSERVED_CALIBRATION_RESEARCHER_AUTHORIZATION_V1" or
            auth.get("status") != "APPROVED_FOR_SINGLE_RUN" or
            auth.get("binding") != expected or
            auth.get("researcher_confirmation") != confirmation or
            auth.get("researcher_confirmed_risks") is not True or
            auth.get("no_automatic_retry") is not True or
            not isinstance(auth.get("resource_approval_record"), str) or
            not auth["resource_approval_record"].strip() or
            not isinstance(auth.get("researcher_identity"), str) or
            not auth["researcher_identity"].strip() or
            not isinstance(auth.get("confirmed_at_utc"), str) or
            not auth["confirmed_at_utc"].strip()):
        raise ValueError("Missing researcher approval or HEAD/UUID/sample/method/runtime/output/budget mismatch")
    return {"authorization_sha256": identity.sha256_file(path), "binding": expected,
            "resource_approval_record": auth["resource_approval_record"]}


def implementation_identity() -> dict:
    names = ("observed_calibration_runner.py", "observed_calibration_measurement.py",
             "observed_calibration_sample.py", "g0_q_protocol.py", "riken_source_identity.py",
             "h3_supervised_pilot.py", "nc0a_watchdog.py")
    return {name: identity.sha256_file(HERE / name) for name in names}


def load_row_inputs(row: dict, manifest: dict, phase2: Path, psa: Path):
    full = next(item for item in manifest["source_graphs"] if item["graph_id"] == row["graph_id"])
    job_path = psa / "jobs" / (
        f"{row['recording_id']}__N{row['N']}__rep-{row['subset_repeat']:03d}.json")
    pilot._require_private_file(job_path, psa, "Historical observed job")
    if identity.sha256_file(job_path) != row["historical_job_sha256"]:
        raise identity.IdentityEvidenceError("Historical observed job identity mismatch")
    job = pilot._read_json(job_path)
    selected = job.get("selected_neuron_indices_zero_based")
    if (not isinstance(selected, list) or any(type(x) is not int for x in selected) or
            len(selected) != row["N"] or selected != sorted(set(selected)) or
            identity.hash_int64(selected) != row["selected_neuron_indices_sha256"]):
        raise identity.IdentityEvidenceError("Realized observed subset identity mismatch")
    ref = identity.load_h3_reference({**full, "historical_louvain_seed_vector_sha256":
                                     row["louvain_seed_vector_sha256"]}, psa)
    return phase2 / "data" / row["source_filename"], selected, ref["louvain_seeds"]


def validate_private_identities(sample: dict, manifest: dict, phase2: Path, psa: Path):
    """Hash/read metadata only. Does not load a signal dataset or construct a graph."""
    legacy = {"historical_graph_builder_sha256": manifest["historical_code_hashes"][
        "multirecording_primary.py"], "records": sample["primary_rows"]}
    phase2, psa = pilot._validate_private_roots(phase2, psa, legacy, manifest)
    signatures = {}
    sources = {row["source_filename"]: row for row in sample["primary_rows"]}
    for filename, row in sources.items():
        path = phase2 / "data" / filename
        before = _signature(path)
        if identity.sha256_file(path) != row["source_file_sha256"] or _signature(path) != before:
            raise identity.IdentityEvidenceError("Source MAT hash/identity changed")
        signatures[filename] = before
    ledger_path = psa / "louvain_seed_ledger.jsonl.gz"
    pilot._require_private_file(ledger_path, psa, "Historical seed ledger")
    if identity.sha256_file(ledger_path) != manifest["seed_ledger_sha256"]:
        raise identity.IdentityEvidenceError("Historical seed ledger hash mismatch")
    required = {}
    for row in sample["primary_rows"]:
        _, selected, seeds = load_row_inputs(row, manifest, phase2, psa)
        required[(row["recording_id"], f"N{row['N']}", row["subset_repeat"],
                  row["state"], row["window_id"])] = (selected, seeds)
    found = set()
    with gzip.open(ledger_path, "rt", encoding="utf-8") as stream:
        for line in stream:
            item = json.loads(line)
            key = (item["recording_id"], item["target_label"], item["subset_repeat"],
                   item["state"], item["window_index"])
            if key in required:
                selected, seeds = required[key]
                if (key in found or item["louvain_seeds"] != seeds or
                        item["selected_neuron_indices_sha256"] != identity.hash_int64(selected)):
                    raise identity.IdentityEvidenceError("Selected row/seed ledger mismatch")
                found.add(key)
    if found != set(required):
        raise identity.IdentityEvidenceError("Missing selected row in historical seed ledger")
    return phase2, psa, signatures


def checked_output(run_dir: Path, psa: Path, run_id: str) -> tuple[Path, Path]:
    root = pilot._resolve_private_root(psa, "SRT_PSA_ROOT")
    if not run_dir.is_absolute() or ".." in run_dir.parts:
        raise ValueError("Output must be absolute without traversal")
    target = Path(os.path.abspath(run_dir))
    parent = root / OUTPUT_PARENT
    if (target.parent != parent or target.name != run_id or parent.is_symlink() or
            target.exists() or target.is_symlink()):
        raise ValueError("Output must be a fresh UUID directory under the fixed private parent")
    if parent.exists() and parent.resolve(strict=True) != parent:
        raise ValueError("Output parent redirected")
    return target, parent


def validate_internal_apfs(psa: Path) -> dict:
    import plistlib
    import subprocess

    # diskutil accepts a volume mount point, not an arbitrary private subdirectory.
    data_volume = Path(MACOS_POLICY["internal_data_volume_path"])
    if psa.stat().st_dev != data_volume.stat().st_dev:
        raise ValueError("Observed output is not on the internal Data volume")
    disk = plistlib.loads(subprocess.run(
        ["diskutil", "info", "-plist", str(data_volume)], check=True, capture_output=True).stdout)
    if disk.get("FilesystemType") != "apfs" or disk.get("Internal") is not True:
        raise ValueError("Observed calibration output requires internal APFS")
    return {"filesystem": "apfs", "internal": True, "same_Data_volume_device": True}


def preflight(*, head: str, phase2: Path, psa: Path, run_dir: Path,
              run_id: str) -> dict:
    started, cpu = time.perf_counter(), time.process_time()
    bindings(head, run_id, run_dir)
    sample, manifest = validate_sample()
    if identity.sha256_file(HERE / SAMPLE_FILENAME) != EXPECTED_SAMPLE_SHA256:
        raise ValueError("Pinned sample file hash mismatch")
    effective, method_sha = h3._method_is_effective(HERE / METHOD_FILENAME)
    if not effective or method_sha != METHOD_SHA256:
        raise ValueError("Effective method identity mismatch")
    git = pilot._git_identity(head)
    runtime = identity.h3_runtime_manifest()
    if not runtime["replay_environment_matches_recorded_versions_and_candidate_lock"]:
        raise ValueError("Target macOS arm64 / Python 3.14.0 runtime mismatch")
    process_counters()  # refuse unavailable native byte counters, no surrogate units
    phase2, psa, signatures = validate_private_identities(sample, manifest, phase2, psa)
    target, parent = checked_output(run_dir, psa, run_id)
    output_volume = validate_internal_apfs(psa)
    limits = pilot._build_watchdog_limits(RESOURCE_CANDIDATE)
    resources = pilot._preflight_macos_resources(limits, psa)
    state = pilot.default_host_state_dir()
    events = pilot._verified_host_events(state / pilot._HOST_LEDGER)
    pilot._assert_host_ledger_allows(events, EXPECTED_SAMPLE_SHA256)
    if any(event.get("run_id") == run_id for event in events):
        raise ValueError("UUID already appears in host activity ledger")
    from nc0a_watchdog import _default_activity_lock_path
    for lock_path in (_default_activity_lock_path(), state / pilot._HOST_LOCK):
        if lock_path.is_symlink():
            raise ValueError("Host lock is redirected")
        if lock_path.exists():
            fd = os.open(lock_path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                fcntl.flock(fd, fcntl.LOCK_UN)
            finally:
                os.close(fd)
    writable_parent = parent if parent.exists() else psa
    if not os.access(writable_parent, os.W_OK | os.X_OK):
        raise ValueError("Output parent is not writable/searchable")
    # Admission later acquires both existing host locks and rechecks ledger atomically.
    return {"status": "PREFLIGHT_PASSED_NOT_AUTHORIZED", "head": git, "runtime": runtime,
            "source_signatures": signatures, "phase2": str(phase2), "psa": str(psa),
            "run_directory": str(target), "run_parent": str(parent),
            "resources": resources, "implementation": implementation_identity(),
            "output_volume": output_volume,
            "preflight_wall_seconds": time.perf_counter() - started,
            "preflight_process_cpu_seconds": time.process_time() - cpu}


def _validate_result(result: dict, row: dict) -> None:
    if result.get("input_identity") != row or result.get("graph_id") != row["graph_id"]:
        raise identity.IdentityEvidenceError("Observed result input identity mismatch")
    nodes, edges, seeds = (result["original_neuron_ids"], result["labeled_edges"],
                            result["louvain_seeds"])
    _, graph_manifest = build_canonical_louvain_graph(nodes, edges)
    q = result["canonical"]
    if (identity.hash_int64(nodes) != row["selected_neuron_indices_sha256"] or
            seed_vector_sha256(seeds) != row["louvain_seed_vector_sha256"] or
            len(seeds) != 200 or len(q["q_values"]) != 200 or
            q.get("seed_count") != 200 or q.get("resolution") != 1.0 or
            q.get("python_louvain_version") != "0.16" or
            q.get("algorithm") != "community.community_louvain.best_partition" or
            q.get("q_function") != "community.community_louvain.modularity" or
            len(q["partition_sha256"]) != 200 or
            q["q_vector_sha256"] != q_vector_sha256(q["q_values"]) or
            q["q_max_200"] != max(q["q_values"]) or
            q["first_max_trial_index"] != first_maximum_index(q["q_values"]) or
            q["seed_vector_sha256"] != row["louvain_seed_vector_sha256"] or
            q["heuristic_diagnostics"] != heuristic_diagnostics(q["q_values"], q["partition_sha256"]) or
            any(q.get(k) != v for k, v in graph_manifest.items()) or
            graph_manifest["node_count"] != row["N"] or
            graph_manifest["edge_count"] != row["expected_edge_count"] or
            result["source_graph_identity"].get("status") != "PASS" or
            result["source_graph_identity"].get("N") != row["N"] or
            result["source_graph_identity"].get("E") != row["expected_edge_count"] or
            result["source_graph_identity"].get("node_order_sha256") != row["selected_neuron_indices_sha256"] or
            result["source_graph_identity"].get("labeled_edge_set_sha256") !=
            identity.sha256_bytes(canonical(edges))):
        raise identity.IdentityEvidenceError("Canonical result graph, seed, Q or diagnostic integrity failure")
    required_phases = {"source_hdf5_and_raw_window", "correlation_and_zero_variance_diagnostics",
                       "historical_graph_builder_inclusive", "mst", "edge_selection_graph_residual",
                       "independent_graph_identity_and_canonical_representation",
                       "canonical_200_Q_including_shared_representation"}
    if not required_phases <= set(result["phases"]):
        raise MeasurementError("Required phase resource measurements are missing")
    diag = result["zero_variance"]
    for field in ("zero_variance_neuron_ids", "constant_neuron_ids"):
        ids = diag[field]
        if ids != sorted(set(ids)) or not set(ids) <= set(nodes):
            raise identity.IdentityEvidenceError("Invalid original-neuron window diagnostic identity")
    for phase in result["phases"].values():
        if phase.get("aborted") or any(not isinstance(phase.get(k), (int, float)) or
                                       not 0 <= phase[k] < float("inf")
                                       for k in ("wall_seconds", "process_cpu_seconds")):
            raise MeasurementError("Incomplete or nonfinite phase resource accounting")


def validate_result(result: dict, row: dict) -> None:
    try:
        _validate_result(result, row)
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        raise identity.IdentityEvidenceError("Malformed/nonfinite canonical result: " + str(exc)[:200]) from exc


def write_result_payload(path: Path, payload: bytes) -> str:
    """H3's exclusive-temp/link/fsync persistence, using already measured JSON bytes."""
    if path.exists() or path.is_symlink() or path.parent.is_symlink():
        raise OSError("Refusing result overwrite or redirected directory")
    temp = path.with_name(path.name + ".tmp-" + uuid.uuid4().hex)
    fd = os.open(temp, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0), 0o600)
    try:
        view = memoryview(payload)
        while view:
            count = os.write(fd, view)
            if count <= 0:
                raise OSError("Short result write")
            view = view[count:]
        os.fsync(fd)
    finally:
        os.close(fd)
    # A partial temp on failure remains evidence; an existing target is never replaced.
    os.link(temp, path)
    temp.unlink()
    parent_fd = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(parent_fd)
    finally:
        os.close(parent_fd)
    return identity.sha256_bytes(payload)


def execute_rows(rows: list[dict], *, run_dir: Path, process_row,
                 synthetic: bool = False, admission_phases: dict | None = None,
                 remediation_identity: dict | None = None) -> dict:
    """No retries, skipped failures or output replacement; durable ordered prefix."""
    row_dir = run_dir / ROW_DIR
    row_dir.mkdir(mode=0o700)  # existing directory is never silently reused
    results, zero_pairs, zero_windows = [], set(), set()
    with HashChainLog(run_dir / EVIDENCE) as log:
        log.append({"kind": "observed_calibration_started", "sample_sha256": EXPECTED_SAMPLE_SHA256,
                    "remediation_identity": remediation_identity,
                    "synthetic_test_only": synthetic, "rows": rows,
                    "implementation": implementation_identity(),
                    "supervised_admission_phases": admission_phases or {},
                    "native_thread_environment": native_thread_environment(),
                    "runtime": identity.h3_runtime_manifest(), "resume_allowed": False})
        for row in rows:
            pilot._set_active_task(run_dir, row["graph_id"])
            started_ns = time.time_ns()
            log.append({"kind": "graph_started", "sample_order": row["sample_order"],
                        "graph_id": row["graph_id"], "started_utc_ns": started_ns})
            try:
                phase_audit = {"wall_seconds": 0.0, "process_cpu_seconds": 0.0}

                def phase_sink(name, metrics, graph_id=row["graph_id"], audit_cost=phase_audit):
                    wall, cpu = time.perf_counter(), time.process_time()
                    log.append({"kind": "phase_measured", "graph_id": graph_id,
                                "phase": name, "metrics": metrics})
                    audit_cost["wall_seconds"] += time.perf_counter() - wall
                    audit_cost["process_cpu_seconds"] += time.process_time() - cpu

                result = process_row(row, phase_sink=phase_sink)
                validate_result(result, row)
                result.update({"started_utc_ns": started_ns, "finished_compute_utc_ns": time.time_ns(),
                               "runtime": identity.h3_runtime_manifest(),
                               "native_thread_environment": native_thread_environment(),
                               "implementation": implementation_identity(),
                               "synthetic_test_only": synthetic})
                cost = {"phase_audit_append_fsync_total": phase_audit}
                with Phase(cost, "result_serialization"):
                    payload = canonical(result) + b"\n"
                relative = Path(ROW_DIR) / f"{row['sample_order']:03d}.json"
                # Bound each persisted artifact before attempting a write, independently of polling.
                if len(payload) > 32 * 1024**2:
                    raise MeasurementError("One result exceeds the fixed 32-MiB artifact cap")
                with Phase(cost, "result_write_fsync"):
                    digest = write_result_payload(run_dir / relative, payload)
                with Phase(cost, "result_audit_append_fsync"):
                    log.append({"kind": "graph_result", "graph_id": row["graph_id"],
                                "sample_order": row["sample_order"], "artifact": str(relative),
                                "artifact_sha256": digest, "artifact_bytes": len(payload),
                                "q_vector_sha256": result["canonical"]["q_vector_sha256"],
                                "started_utc_ns": started_ns, "finished_utc_ns": time.time_ns()})
                log.append({"kind": "artifact_cost", "graph_id": row["graph_id"],
                            "artifact_sha256": digest, "cost": cost,
                            "caveat": "cost-event self-write excluded; included in end-to-end Watchdog"})
                diag = result["zero_variance"]
                frame = (row["source_file_sha256"], row["state"], row["source_frame_indices_sha256"])
                if diag["zero_variance_neuron_ids"]:
                    zero_windows.add(frame)
                zero_pairs.update((*frame, node) for node in diag["zero_variance_neuron_ids"])
                results.append({"graph_id": row["graph_id"], "artifact_sha256": digest,
                                "cache_hit": result["cache"]["hit"],
                                "has_zero_variance": bool(diag["zero_variance_neuron_ids"])})
            except Exception as exc:  # noqa: BLE001 -- persist unknown failures, never retry
                category = ("SCIENTIFIC_INTEGRITY" if isinstance(exc, identity.IdentityEvidenceError)
                            else "OPERATIONAL_IO" if isinstance(exc, OSError)
                            else "UNKNOWN_FAIL_STOP")
                log.append({"kind": "calibration_failed", "graph_id": row["graph_id"],
                            "failure_category": category, "failure_type": type(exc).__name__,
                            "failure_reason": str(exc)[:500],
                            "resume_allowed": False, "rows_completed": len(results)})
                terminal = {"kind": "calibration_failed", "status": "failed",
                            "failure_category": category, "resume_allowed": False,
                            "rows_completed": len(results), "synthetic_test_only": synthetic,
                            "evidence_tip_sha256": log.previous}
                pilot._write_new_json(run_dir / "runner-terminal.json", terminal)
                return terminal
        terminal = {"kind": "calibration_completed", "status": "completed",
                    "rows_completed": len(rows), "louvain_trials": 200 * len(rows),
                    "resume_allowed": False, "synthetic_test_only": synthetic,
                    "zero_variance_summary": {"affected_graphs": sum(r["has_zero_variance"] for r in results),
                                              "independent_source_windows": len(zero_windows),
                                              "unique_neuron_window_combinations": len(zero_pairs)},
                    "artifact_index_sha256": identity.sha256_bytes(canonical(results))}
        log.append(terminal)
        terminal["evidence_tip_sha256"] = log.previous
        pilot._write_new_json(run_dir / "runner-terminal.json", terminal)
        return terminal


def _private_process_row(row, manifest, phase2, psa, signatures, cache, phase_sink):
    phases = PhaseRecords(phase_sink)
    with Phase(phases, "private_job_subset_seed_identity"):
        source, selected, seeds = load_row_inputs(row, manifest, phase2, psa)
        if _signature(source) != tuple(signatures[row["source_filename"]]):
            raise identity.IdentityEvidenceError("Source changed after admission")
    with Phase(phases, "resource_snapshot_before"):
        # Host telemetry belongs to the external Watchdog. Its command-line
        # helpers would inherit this scientific process group and correctly
        # trigger UNKNOWN_PROCESS_GROUP_MEMBER if launched here.
        before = {"process": process_counters(),
                  "output_free_bytes": shutil.disk_usage(psa).free}
    def historical_factory():
        function, digest = identity._historical_connected_graph(phase2 / "multirecording_primary.py")
        if digest != identity.EXPECTED_HISTORICAL_GRAPH_FUNCTION_SHA256:
            raise identity.IdentityEvidenceError("Historical graph-function identity mismatch")
        return function, digest

    result = measure_row(row, source_path=source, selected=selected, seeds=seeds,
                         cache=cache, initial_phases=phases, builder_factory=historical_factory)
    with Phase(result["phases"], "resource_snapshot_after"):
        after = {"process": process_counters(),
                 "output_free_bytes": shutil.disk_usage(psa).free}
    result["resource_endpoints"] = {
        "before": before, "after": after,
        "host_telemetry": {"artifact": "watchdog.jsonl", "task_id": row["graph_id"],
                           "semantics": "external periodic task-ID samples may lag row boundaries, "
                                        "not exact row endpoints; "
                                        "no matching sample means unknown, not zero"},
    }
    return result


def _runner_child() -> int:
    run_dir = Path.cwd()
    admission_phases = {}
    try:
        guard_watchdog_parent(int(os.environ["NC0A_WATCHDOG_PARENT_PID"]))
        pilot._write_runner_lease(run_dir)
        auth = pilot._read_json(Path(os.environ["SRT_OBS_AUTH_PATH"]))
        binding = auth["binding"]
        validate_authorization(Path(os.environ["SRT_OBS_AUTH_PATH"]), head=binding["head_sha"],
                               run_id=binding["run_uuid"], run_dir=run_dir,
                               confirmation=os.environ["SRT_OBS_CONFIRMATION"])
        if identity.sha256_file(Path(os.environ["SRT_OBS_AUTH_PATH"])) != os.environ["SRT_OBS_AUTH_SHA256"]:
            raise ValueError("Authorization changed between admission and supervised child")
        pilot._git_identity(binding["head_sha"])
        sample, manifest = validate_sample()
        if identity.sha256_file(HERE / SAMPLE_FILENAME) != EXPECTED_SAMPLE_SHA256:
            raise ValueError("Supervised child sample byte identity mismatch")
        with Phase(admission_phases, "supervised_source_job_seed_revalidation"):
            phase2, psa, signatures = validate_private_identities(
                sample, manifest, Path(os.environ["SRT_PHASE2_ROOT"]), Path(os.environ["SRT_PSA_ROOT"]))
        if not identity.h3_runtime_manifest()["replay_environment_matches_recorded_versions_and_candidate_lock"]:
            raise ValueError("Supervised child target runtime mismatch")
        cache = RawWindowCache(RESOURCE_CANDIDATE["raw_window_cache_bytes"])
        terminal = execute_rows(sample["primary_rows"], run_dir=run_dir,
                                admission_phases=admission_phases,
                                process_row=lambda row, phase_sink: _private_process_row(
                                    row, manifest, phase2, psa, signatures, cache, phase_sink))
        return 0 if terminal["status"] == "completed" else 31
    except Exception as exc:  # noqa: BLE001 -- fail closed with an auditable terminal record
        with HashChainLog(run_dir / EVIDENCE) as log:
            log.append({"kind": "admission_or_runner_exception", "failure_type": type(exc).__name__,
                        "failure_reason": str(exc)[:500],
                        "admission_phases": admission_phases,
                        "failure_category": "UNKNOWN_FAIL_STOP", "resume_allowed": False})
            if not (run_dir / "runner-terminal.json").exists():
                pilot._write_new_json(run_dir / "runner-terminal.json", {
                    "kind": "calibration_failed", "status": "failed", "resume_allowed": False,
                    "failure_type": type(exc).__name__, "evidence_tip_sha256": log.previous})
        return 32


def launch(*, head: str, run_id: str, run_dir: Path, authorization: Path,
           confirmation: str, phase2: Path, psa: Path) -> dict:
    approved = validate_authorization(authorization, head=head, run_id=run_id,
                                      run_dir=run_dir, confirmation=confirmation)
    check = preflight(head=head, phase2=phase2, psa=psa, run_dir=run_dir, run_id=run_id)
    remaining_wall = RESOURCE_CANDIDATE["wall_seconds"] - check["preflight_wall_seconds"]
    remaining_cpu = RESOURCE_CANDIDATE["process_tree_cpu_seconds"] - check["preflight_process_cpu_seconds"]
    if min(remaining_wall, remaining_cpu) <= 0:
        raise MeasurementError("Identity preflight exhausted the single-run resource allocation")
    limits = replace(pilot._build_watchdog_limits(RESOURCE_CANDIDATE),
                     wall_seconds=remaining_wall, cpu_seconds=remaining_cpu)
    parent = Path(check["run_parent"])
    parent.mkdir(mode=0o700, exist_ok=True)
    env = {"SRT_OBS_AUTH_PATH": str(authorization.resolve(strict=True)),
           "SRT_OBS_AUTH_SHA256": approved["authorization_sha256"],
           "SRT_OBS_CONFIRMATION": confirmation, "SRT_PHASE2_ROOT": check["phase2"],
           "SRT_PSA_ROOT": check["psa"]}
    return pilot._launch_supervised(
        [sys.executable, str(Path(__file__).resolve()), "--runner-child"],
        run_dir=run_dir, state_dir=pilot.default_host_state_dir(),
        pilot_sha256=EXPECTED_SAMPLE_SHA256, run_id=run_id, head=check["head"],
        candidate={**RESOURCE_CANDIDATE, "workflow": "OBSERVED_ONLY_CALIBRATION",
                   "researcher_authorization": approved, "preflight": check},
        env_extra=env, limits=limits, expected_run_parent=parent)


def verify_run(run_dir: Path, *, state_dir: Path | None = None,
               _remediation_packet: dict | None = None, _audit_guard=None) -> dict:
    """Audit-only: verify ordered results and anchors. Never resume/retry a row."""
    if run_dir.is_symlink() or run_dir.resolve(strict=True) != Path(os.path.abspath(run_dir)):
        raise ValueError("Run directory redirected")
    if _audit_guard is not None:
        _audit_guard()
    summary = pilot._read_json(run_dir / "h3-summary.json")
    allowed = {"h3-summary.json", "h3-control.jsonl", EVIDENCE, "watchdog.jsonl", "run-manifest.json",
               "runner-terminal.json", "runner.stdout.log", "active_task.json", pilot._LEASE, ROW_DIR}
    if _remediation_packet is not None:
        from observed_remediation_identity import PACKET_SHA256, load_packet
        if _remediation_packet != load_packet():
            raise ValueError("Remediation verifier requires the exact frozen packet")
        allowed.update({"remediation-account.json", "remediation-closed.json"})
    if any(p.name not in allowed or p.is_symlink() for p in run_dir.iterdir()):
        raise ValueError("Unknown or redirected run artifact")
    control_events = []
    tips = {}
    for name in ("h3-control.jsonl", "watchdog.jsonl", EVIDENCE):
        _, tips[name] = verify_hash_chain(run_dir / name)
    for name, key in (("watchdog.jsonl", "watchdog_audit_tip_sha256"),
                      (EVIDENCE, "evidence_tip_sha256")):
        if tips[name] != summary[key]:
            raise ValueError("Audit suffix removed or anchor mismatch")
    control_events = [json.loads(line)["event"] for line in
                      (run_dir / "h3-control.jsonl").read_text().splitlines()]
    starts = [e for e in control_events if e["kind"] == "activity_started"]
    finishes = [e for e in control_events if e["kind"] == "activity_finished"]
    manifest = pilot._read_json(run_dir / "run-manifest.json")
    if (len(starts) != 1 or len(finishes) != 1 or finishes[0] != control_events[-1] or
            starts[0]["run_id"] != summary["run_id"] or finishes[0]["run_id"] != summary["run_id"] or
            starts[0]["head_sha"] != summary["head_sha"] or
            starts[0]["pilot_sha256"] != summary["pilot_sha256"] or
            finishes[0]["summary_sha256"] != identity.sha256_file(run_dir / "h3-summary.json") or
            identity.sha256_file(run_dir / "run-manifest.json") != summary["run_manifest_sha256"] or
            manifest["run_id"] != summary["run_id"] or
            manifest["head"]["head_sha"] != summary["head_sha"]):
        raise ValueError("Unique start/finish/manifest/summary anchor failed")
    for key in ("status", "failure_category", "run_manifest_sha256", "runner_terminal_sha256",
                "watchdog_audit_tip_sha256", "evidence_tip_sha256"):
        if finishes[0][key] != summary[key]:
            raise ValueError("Control terminal differs from summary")
    terminal_path = run_dir / "runner-terminal.json"
    if summary["runner_terminal_sha256"] is not None and (
            terminal_path.is_symlink() or identity.sha256_file(terminal_path) != summary["runner_terminal_sha256"]):
        raise ValueError("Terminal artifact changed")
    if terminal_path.exists() and summary["runner"] != pilot._read_json(terminal_path):
        raise ValueError("Summary runner differs from terminal artifact")
    watchdog = [json.loads(line)["event"] for line in (run_dir / "watchdog.jsonl").read_text().splitlines()]
    hashes = [e.get("usage", {}).get("runner_stdout_sha256") or e.get("runner_stdout_sha256")
              for e in watchdog]
    hashes = [value for value in hashes if value]
    if (not hashes or any(value != identity.sha256_file(run_dir / "runner.stdout.log") for value in hashes)):
        raise ValueError("Unauthenticated stdout")
    events = [json.loads(line)["event"] for line in (run_dir / EVIDENCE).read_text().splitlines()]
    begins = [e for e in events if e["kind"] == "observed_calibration_started"]
    if len(begins) != 1:
        raise ValueError("No unique calibration start; incomplete admission is not resumable")
    begin = begins[0]
    rows = begin["rows"]
    if begin["synthetic_test_only"] is not True:
        sample, _ = validate_sample()
        expected_rows = (sample["primary_rows"] if _remediation_packet is None else
                         _remediation_packet["suffix_rows"])
        expected_packet = EXPECTED_SAMPLE_SHA256 if _remediation_packet is None else PACKET_SHA256
        if rows != expected_rows or begin["sample_sha256"] != EXPECTED_SAMPLE_SHA256:
            raise ValueError("Run row identities differ from fixed sample")
        if summary["pilot_sha256"] != expected_packet:
            raise ValueError("Run summary does not bind observed sample")
        check = manifest["candidate_limits_not_authorized_in_packet"]["preflight"]
        if (begin["implementation"] != check["implementation"] or begin["runtime"] != check["runtime"] or
                not begin["runtime"]["replay_environment_matches_recorded_versions_and_candidate_lock"]):
            raise ValueError("Run implementation/runtime differs from admitted environment")
    result_events = [e for e in events if e["kind"] == "graph_result"]
    if [e["graph_id"] for e in result_events] != [r["graph_id"] for r in rows[:len(result_events)]]:
        raise ValueError("Missing/duplicate/out-of-order result")
    costs = [e for e in events if e["kind"] == "artifact_cost"]
    if len(costs) != len(result_events):
        raise ValueError("Incomplete or duplicate artifact resource accounting")
    files = set()
    for row, event in zip(rows, result_events, strict=False):
        if _audit_guard is not None:
            _audit_guard()
        relative = Path(ROW_DIR) / f"{row['sample_order']:03d}.json"
        path = run_dir / relative
        if str(relative) != event["artifact"] or path.is_symlink() or identity.sha256_file(path) != event["artifact_sha256"]:
            raise ValueError("Row artifact missing or changed")
        data = pilot._read_json(path)
        validate_result(data, row)
        phase_events = [e for e in events if e["kind"] == "phase_measured" and e["graph_id"] == row["graph_id"]]
        if (len(phase_events) != len(data["phases"]) or
                {e["phase"]: e["metrics"] for e in phase_events} != data["phases"]):
            raise ValueError("Phase meters missing or differ from durable phase evidence")
        if (data["implementation"] != begin["implementation"] or data["runtime"] != begin["runtime"] or
                data["native_thread_environment"] != begin["native_thread_environment"] or
                data["synthetic_test_only"] != begin["synthetic_test_only"] or
                len([e for e in costs if e["artifact_sha256"] == event["artifact_sha256"]]) != 1):
            raise ValueError("Row runtime/implementation/resource-cost record mismatch")
        files.add(path.name)
        if _audit_guard is not None:
            _audit_guard()
    if (run_dir / ROW_DIR).is_symlink() or {p.name for p in (run_dir / ROW_DIR).iterdir()} != files:
        raise ValueError("Unlogged row artifact")
    if state_dir is not None:
        host = pilot._verified_host_events(state_dir / pilot._HOST_LEDGER)
        begun = [e for e in host if e.get("run_id") == summary["run_id"] and e["kind"] == "activity_started"]
        ended = [e for e in host if e.get("run_id") == summary["run_id"] and e["kind"] == "activity_finished"]
        if (len(begun) != 1 or len(ended) != 1 or
                begun[0]["head_sha"] != summary["head_sha"] or
                begun[0]["pilot_sha256"] != summary["pilot_sha256"] or
                ended[0]["summary_sha256"] != identity.sha256_file(run_dir / "h3-summary.json")):
            raise ValueError("Host ledger does not anchor run summary")
    completed = summary["status"] == "COMPLETED"
    if completed and (len(result_events) != len(rows) or not events or
                      events[-1]["kind"] != "calibration_completed" or
                      summary["runner"]["louvain_trials"] != len(rows) * 200):
        raise ValueError("Incomplete result cannot be completed")
    if completed:
        terminal = {key: value for key, value in summary["runner"].items() if key != "evidence_tip_sha256"}
        if terminal != events[-1] or summary["runner"]["evidence_tip_sha256"] != tips[EVIDENCE]:
            raise ValueError("Runner terminal does not close the evidence chain")
    samples = [e for e in watchdog if e.get("event") == "resource_sample"]
    row_rss = {r["graph_id"]: [e["usage"]["aggregate_rss_bytes"] for e in samples
                               if e.get("task_id") == r["graph_id"]] for r in rows}
    return {"status": "VERIFIED_TERMINAL", "completed": completed,
            "rows_verified": len(result_events), "resume_allowed": False,
            "synthetic_test_only": begin["synthetic_test_only"], "hash_chain_tips": tips,
            "row_watchdog_rss": {key: {"sample_count": len(value),
                                       "sampled_max_bytes": max(value) if value else None}
                                 for key, value in row_rss.items()},
            "rss_note": "zero samples means unknown row peak, never zero memory use"}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--validate-sample", action="store_true")
    mode.add_argument("--preflight", action="store_true")
    mode.add_argument("--authorization-draft", action="store_true")
    mode.add_argument("--run", action="store_true")
    mode.add_argument("--verify", type=Path)
    mode.add_argument("--runner-child", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--head")
    parser.add_argument("--run-id")
    parser.add_argument("--run-dir", type=Path)
    parser.add_argument("--authorization", type=Path)
    parser.add_argument("--researcher-confirmation")
    args = parser.parse_args(argv)
    if args.runner_child:
        return _runner_child()
    if args.validate_sample:
        sample, _ = validate_sample()
        print(json.dumps({"status": "FROZEN_NOT_AUTHORIZED", "sha256": EXPECTED_SAMPLE_SHA256,
                          "coverage": sample["coverage"], "rows": sample["row_count"]}))
        return 0
    if args.verify:
        print(json.dumps(verify_run(args.verify, state_dir=pilot.default_host_state_dir())))
        return 0
    if not all((args.head, args.run_id, args.run_dir)):
        parser.error("preflight/run require --head, --run-id and --run-dir")
    roots = [os.environ.get(name, "").strip() for name in ("SRT_PHASE2_ROOT", "SRT_PSA_ROOT")]
    if not all(roots):
        parser.error("Both private root variables must be explicitly nonempty")
    kwargs = {"head": args.head, "run_id": args.run_id, "run_dir": args.run_dir,
              "phase2": Path(roots[0]), "psa": Path(roots[1])}
    if args.preflight or args.authorization_draft:
        check = preflight(**kwargs)
        print(json.dumps({"preflight": check, "pending_authorization": authorization_draft(
            args.head, args.run_id, args.run_dir)} if args.authorization_draft else check))
    else:
        if not args.authorization or not args.researcher_confirmation:
            parser.error("No run without an approved JSON and exact researcher confirmation")
        print(json.dumps(launch(**kwargs, authorization=args.authorization,
                                confirmation=args.researcher_confirmation)))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, WatchdogError, MeasurementError) as exc:
        print(f"OBSERVED CALIBRATION REFUSED: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
