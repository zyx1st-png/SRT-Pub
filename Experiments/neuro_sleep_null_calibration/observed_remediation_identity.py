"""Frozen, identity-only 41-row remedy and read-only consumed-attempt verification.

No signal reader, Louvain invocation, ledger writer or execution authorization is
provided here. An explicit packet argument is for isolated synthetic callers;
production entry points must use load_packet() and its pinned byte identity.
"""
from __future__ import annotations

import json
import math
import os
import uuid
from datetime import datetime
from pathlib import Path

import h3_supervised_pilot as pilot
import riken_source_identity as identity
from observed_calibration_sample import (
    HERE,
    METHOD_SHA256,
    SOURCE_SHA256,
    canonical,
    validate_sample,
)

PACKET_FILENAME = "OBSERVED_CALIBRATION_REMEDIATION_SUFFIX_V1_2026-10-26.json"
INCIDENT_FILENAME = "OBSERVED_CALIBRATION_FIRST_ATTEMPT_INCIDENT_EVIDENCE_2026-10-26.json"
INCIDENT_SHA256 = "003518a892f4622b61380a376cb59badb26da1279de2501f1654fb2648e0a6c6"
FULL_SAMPLE_SHA256 = "f29acb99a05387b128f724bf818e3f402f7ced8a4080c12da4a936b9284d95c4"
SUFFIX_SHA256 = "9dbb10990d0cdffa2a864e6aaec12ca42bafcf85783e05668c1b8e06b5d28808"
PACKET_SHA256 = "208121aad2f3a9d07c0b6dc98a005b5a126a4f3cc3c887c24f7cb6bbfa7639ae"
SCHEMA = "SRT_OBSERVED_CALIBRATION_REMEDIATION_SUFFIX_V1"
STATUS = "FROZEN_IDENTITY_NOT_SINGLE_RUN_AUTHORIZED"
PREPARATION_FILE_SHA256 = {
    "approved-single-run-authorization.json": "78b032b772f88195021fdacff38093c086cd226660c53dddb4afe109137b6444",
    "frozen-sample.json": FULL_SAMPLE_SHA256,
    "pending-researcher-authorization.json": "0c1621f17e279757ab143278e2f7a0a55154c74b1293df909c56325ce16238a4",
    "preflight-evidence.json": "f07f520fe180eab8260534d93e9abb5f8c2b722b15e36141376c1daa608aa369",
}


class RemediationIdentityError(ValueError):
    """Old evidence or exact suffix is not verifiable; never resume by inference."""


def _digest(document: object) -> str:
    return identity.sha256_bytes(canonical(document))


def packet_sha256(packet: dict) -> str:
    """Packet file encoding is canonical UTF-8 JSON followed by exactly one LF."""
    return identity.sha256_bytes(canonical(packet) + b"\n")


def build_packet() -> dict:
    """Rebuild only public identities, never graph/Q outcomes or timings for selection."""
    sample, _ = validate_sample()
    incident_path = HERE / INCIDENT_FILENAME
    if identity.sha256_file(incident_path) != INCIDENT_SHA256:
        raise RemediationIdentityError("Frozen incident evidence identity mismatch")
    incident = json.loads(incident_path.read_text())
    rows = sample["primary_rows"]
    prefix, suffix = rows[:6], rows[6:]
    files = incident["original_run_file_sha256"]
    artifacts = []
    for row, saved in zip(prefix, incident["completed_rows"], strict=True):
        path = f"observed-cost-rows/{row['sample_order']:03d}.json"
        if (row["graph_id"] != saved["graph_id"] or
                files[path] != saved["artifact_sha256"]):
            raise RemediationIdentityError("Incident completed prefix differs from sample")
        artifacts.append({"relative_path": path, "graph_id": row["graph_id"],
                          "sample_order": row["sample_order"], "sha256": files[path]})
    return {
        "schema": SCHEMA, "status": STATUS,
        "full_sample_sha256": FULL_SAMPLE_SHA256,
        "source_manifest_sha256": SOURCE_SHA256, "method_sha256": METHOD_SHA256,
        "runtime_lock_sha256": identity.sha256_file(HERE / "g0-runtime-macos-arm64.lock"),
        "q_protocol_sha256": identity.sha256_file(HERE / "g0_q_protocol.py"),
        "incident_evidence_sha256": INCIDENT_SHA256,
        "prefix_rows": prefix, "suffix_rows": suffix,
        "suffix_sha256": _digest(suffix), "prefix_count": 6, "suffix_count": 41,
        "new_louvain_trials": 8200, "original_louvain_trials": 1200,
        "selection_rule": "exact frozen primary_rows[6:47]; no reordering, old Q or reserve execution",
        "prior_run": {
            "uuid": incident["run_uuid"], "head_sha": incident["executed_head"],
            "file_sha256": files, "hash_chain_tips": incident["verification"]["hash_chain_tips"],
            "prefix_artifacts": artifacts,
            "terminal_status": "STOPPED_BY_WATCHDOG",
            "failure_category": "OPERATIONAL_RESOURCE_STOP",
            "watchdog_reason": "UNKNOWN_PROCESS_GROUP_MEMBER",
            "reported_wall_seconds": incident["reported_usage"]["wall_seconds"],
            "reported_cpu_seconds": incident["reported_usage"]["cpu_seconds"],
            "preflight_wall_seconds": incident["original_formal_preflight"]["preflight_wall_seconds"],
            "preflight_cpu_seconds": incident["original_formal_preflight"]["preflight_process_cpu_seconds"],
            "elapsed_controller_seconds": incident["elapsed_controller_seconds"],
            "host_started_utc": incident["host_started_utc"],
            "host_finished_utc": incident["host_finished_utc"],
            "host_ledger_prefix_event_count": 6,
            "host_ledger_prefix_sha256": incident["original_host_ledger_sha256"],
            "host_ledger_prefix_tip": "f33d477aae2003002a6e5e301a72699a9fcb557070839adedca999f048e678d9",
            "accounting_cpu_count_upper_bound": 8,
            "preparation_evidence_sha256": "f07f520fe180eab8260534d93e9abb5f8c2b722b15e36141376c1daa608aa369",
            "preparation_file_sha256": dict(PREPARATION_FILE_SHA256),
        },
    }


def _validate_structure(packet: dict) -> None:
    try:
        prefix, suffix = packet["prefix_rows"], packet["suffix_rows"]
        if (packet["schema"] != SCHEMA or packet["status"] != STATUS or
                len(prefix) != 6 or len(suffix) != 41 or
                [r["sample_order"] for r in prefix + suffix] != list(range(1, 48)) or
                len({r["graph_id"] for r in prefix + suffix}) != 47 or
                packet["suffix_sha256"] != _digest(suffix) or
                packet["prefix_count"] != 6 or packet["suffix_count"] != 41 or
                packet["new_louvain_trials"] != 8200 or packet["original_louvain_trials"] != 1200):
            raise RemediationIdentityError("Remediation rows/order/hash/count mismatch")
        prior = packet["prior_run"]
        if (set(prior["preparation_file_sha256"]) != set(PREPARATION_FILE_SHA256) or
                prior["preparation_file_sha256"]["preflight-evidence.json"] !=
                prior["preparation_evidence_sha256"]):
            raise RemediationIdentityError("Original preparation file list/hash binding differs")
        if (str(uuid.UUID(prior["uuid"])) != prior["uuid"] or
                len(prior["head_sha"]) != 40 or
                any(c not in "0123456789abcdef" for c in prior["head_sha"]) or
                prior["terminal_status"] != "STOPPED_BY_WATCHDOG" or
                prior["failure_category"] != "OPERATIONAL_RESOURCE_STOP" or
                prior["watchdog_reason"] != "UNKNOWN_PROCESS_GROUP_MEMBER"):
            raise RemediationIdentityError("Only the specific consumed operational fault can be remedied")
        artifacts = prior["prefix_artifacts"]
        if len(artifacts) != 6:
            raise RemediationIdentityError("Original committed prefix must have six artifacts")
        for row, saved in zip(prefix, artifacts, strict=True):
            expected = f"observed-cost-rows/{row['sample_order']:03d}.json"
            if (saved["relative_path"] != expected or saved["graph_id"] != row["graph_id"] or
                    saved["sample_order"] != row["sample_order"] or
                    prior["file_sha256"][expected] != saved["sha256"]):
                raise RemediationIdentityError("Prefix artifact/row binding mismatch")
        for key in ("reported_wall_seconds", "reported_cpu_seconds", "preflight_wall_seconds",
                    "preflight_cpu_seconds", "elapsed_controller_seconds"):
            value = prior[key]
            if type(value) not in (int, float) or not math.isfinite(value) or value < 0:
                raise RemediationIdentityError("Invalid original resource accounting")
        if prior["elapsed_controller_seconds"] < prior["reported_wall_seconds"]:
            raise RemediationIdentityError("Controller interval is shorter than its Watchdog")
    except (KeyError, TypeError, AttributeError) as exc:
        raise RemediationIdentityError("Malformed remediation packet") from exc


def load_packet() -> dict:
    path = HERE / PACKET_FILENAME
    _regular_file(path)
    if identity.sha256_file(path) != PACKET_SHA256:
        raise RemediationIdentityError("Pinned remediation packet byte hash mismatch")
    packet = json.loads(path.read_text())
    _validate_structure(packet)
    if packet != build_packet() or packet["suffix_sha256"] != SUFFIX_SHA256:
        raise RemediationIdentityError("Remediation packet differs from original fixed identities")
    return packet


def _regular_file(path: Path) -> tuple:
    absolute = Path(os.path.abspath(path))
    if path.is_symlink() or path.resolve(strict=True) != absolute or not path.is_file():
        raise RemediationIdentityError("Original evidence is missing or redirected")
    stat = path.stat()
    if stat.st_nlink != 1:
        raise RemediationIdentityError("Original evidence has hard-link aliases")
    return stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns


def _snapshot(run_dir: Path, expected: dict, audit_guard=None) -> tuple[dict, int]:
    if (not run_dir.is_absolute() or ".." in run_dir.parts or run_dir.is_symlink() or
            run_dir.resolve(strict=True) != Path(os.path.abspath(run_dir)) or not run_dir.is_dir()):
        raise RemediationIdentityError("Original run directory is redirected or invalid")
    expected_dirs = {str(parent) for name in expected for parent in Path(name).parents
                     if str(parent) != "."}
    found, directories, signatures, size = {}, set(), {}, 0
    for path in run_dir.rglob("*"):
        relative = str(path.relative_to(run_dir))
        if path.is_symlink():
            raise RemediationIdentityError("Original evidence directory contains a symlink")
        if path.is_dir():
            directories.add(relative)
        else:
            if audit_guard is not None:
                audit_guard()
            signatures[relative] = _regular_file(path)
            if size + signatures[relative][2] > 1 << 30:
                raise RemediationIdentityError("Original files exceed their entire output ceiling")
            found[relative] = identity.sha256_file(path)
            size += signatures[relative][2]
    if found != expected or directories != expected_dirs:
        raise RemediationIdentityError("Original evidence hashes or complete directory listing differ")
    return signatures, size


def _preparation_snapshot(directory: Path, expected: dict) -> tuple[dict, int]:
    if (directory.is_symlink() or not directory.is_dir() or
            directory.resolve(strict=True) != Path(os.path.abspath(directory)) or
            {entry.name for entry in directory.iterdir()} != set(expected)):
        raise RemediationIdentityError("Original preparation directory is redirected or has unknown files")
    signatures, size = {}, 0
    for name, digest in expected.items():
        path = directory / name
        signatures[name] = _regular_file(path)
        if identity.sha256_file(path) != digest:
            raise RemediationIdentityError("Original preparation artifact hash differs")
        size += signatures[name][2]
    return signatures, size


def verify_original(run_dir: Path, state_dir: Path, *, packet: dict | None = None,
                    audit_guard=None) -> dict:
    """Read-only official terminal verification plus fixed old-run/hash/accounting ties.

    This verifies result identities and saved Q integrity, never recomputes Q.
    Any explicit packet is an in-memory injection for isolated synthetic tests;
    a production caller must first load the fixed packet and offer no CLI override.
    """
    import observed_calibration_runner as runner

    packet = load_packet() if packet is None else packet
    _validate_structure(packet)
    prior = packet["prior_run"]
    if run_dir.name != prior["uuid"]:
        raise RemediationIdentityError("Original run UUID/path mismatch")
    signatures, output_bytes = _snapshot(run_dir, prior["file_sha256"], audit_guard)
    ledger = state_dir / pilot._HOST_LEDGER
    _regular_file(ledger)
    ledger_sha = identity.sha256_file(ledger)
    ledger_lines = ledger.read_bytes().splitlines(keepends=True)
    prefix_count = prior["host_ledger_prefix_event_count"]
    if (type(prefix_count) is not int or prefix_count < 1 or len(ledger_lines) < prefix_count or
            identity.sha256_bytes(b"".join(ledger_lines[:prefix_count])) != prior["host_ledger_prefix_sha256"] or
            json.loads(ledger_lines[prefix_count - 1])["record_sha256"] != prior["host_ledger_prefix_tip"]):
        raise RemediationIdentityError("Original host-ledger prefix differs or is truncated")
    preparation = (run_dir.parent.parent / "canonical_observed_authorization_preparation_2026-10-26" /
                   prior["uuid"] / "preflight-evidence.json")
    preparation_signatures, preparation_bytes = _preparation_snapshot(
        preparation.parent, prior["preparation_file_sha256"])
    prep_signature = _regular_file(preparation)
    if identity.sha256_file(preparation) != prior["preparation_evidence_sha256"]:
        raise RemediationIdentityError("Original CPU-count preparation evidence differs")
    prepared = pilot._read_json(preparation)
    cpu_count = prior["accounting_cpu_count_upper_bound"]
    if (type(cpu_count) is not int or cpu_count <= 0 or
            prepared["component_checks"]["cpu_count"] != cpu_count or
            prepared["head_sha"] != prior["head_sha"] or prepared["run_uuid"] != prior["uuid"]):
        raise RemediationIdentityError("Original CPU-count bound is not evidenced")
    verification = (runner.verify_run(run_dir, state_dir=state_dir) if audit_guard is None else
                    runner.verify_run(run_dir, state_dir=state_dir, _audit_guard=audit_guard))
    if (verification["status"] != "VERIFIED_TERMINAL" or verification["completed"] is not False or
            verification["resume_allowed"] is not False or verification["rows_verified"] != 6 or
            verification["hash_chain_tips"] != prior["hash_chain_tips"]):
        raise RemediationIdentityError("Original run is not the fixed consumed six-row terminal")
    summary = pilot._read_json(run_dir / "h3-summary.json")
    manifest = pilot._read_json(run_dir / "run-manifest.json")
    usage = summary["watchdog"]["usage"]
    preflight = manifest["candidate_limits_not_authorized_in_packet"]["preflight"]
    approved_path = preparation.parent / "approved-single-run-authorization.json"
    approved = pilot._read_json(approved_path)
    approved_sha = manifest["candidate_limits_not_authorized_in_packet"][
        "researcher_authorization"]["authorization_sha256"]
    if (identity.sha256_file(approved_path) != approved_sha or
            approved["preparation_evidence_sha256"] != prior["preparation_evidence_sha256"] or
            approved["status"] != "APPROVED_FOR_SINGLE_RUN" or
            approved["binding"]["head_sha"] != prior["head_sha"] or
            approved["binding"]["run_uuid"] != prior["uuid"] or
            approved["binding"]["sample_sha256"] != packet["full_sample_sha256"] or
            approved["binding"]["output_directory"] != str(run_dir)):
        raise RemediationIdentityError("Original approval does not authenticate CPU-count preparation evidence")
    if (summary["run_id"] != prior["uuid"] or summary["head_sha"] != prior["head_sha"] or
            summary["pilot_sha256"] != packet["full_sample_sha256"] or
            summary["status"] != prior["terminal_status"] or
            summary["failure_category"] != prior["failure_category"] or
            summary["resume_allowed"] is not False or summary["runner"] is not None or
            summary["runner_terminal_sha256"] is not None or
            summary["watchdog"]["reason"] != prior["watchdog_reason"] or
            usage["wall_seconds"] != prior["reported_wall_seconds"] or
            usage["cpu_seconds"] != prior["reported_cpu_seconds"] or
            usage["cpu_accounting"] != "max_process_group_ps_and_waited_child_rusage_plus_watchdog" or
            preflight["preflight_wall_seconds"] != prior["preflight_wall_seconds"] or
            preflight["preflight_process_cpu_seconds"] != prior["preflight_cpu_seconds"] or
            summary["elapsed_controller_seconds"] != prior["elapsed_controller_seconds"]):
        raise RemediationIdentityError("Original terminal cause or resource accounting differs")
    for row, saved in zip(packet["prefix_rows"], prior["prefix_artifacts"], strict=True):
        result = pilot._read_json(run_dir / saved["relative_path"])
        if (result["input_identity"] != row or result["graph_id"] != row["graph_id"] or
                len(result["louvain_seeds"]) != 200 or len(result["canonical"]["q_values"]) != 200):
            raise RemediationIdentityError("Original six-row prefix identity or Q count differs")
    events = pilot._verified_host_events(ledger)
    starts = [e for e in events if e.get("run_id") == prior["uuid"] and e.get("kind") == "activity_started"]
    finishes = [e for e in events if e.get("run_id") == prior["uuid"] and e.get("kind") == "activity_finished"]
    if len(starts) != 1 or len(finishes) != 1:
        raise RemediationIdentityError("Original host claim is not uniquely closed")
    start, finish = starts[0], finishes[0]
    old_host_record_bytes = sum(len(line) for line in ledger_lines
                               if json.loads(line)["event"].get("run_id") == prior["uuid"] and
                               json.loads(line)["event"].get("kind") in
                               {"activity_started", "activity_finished"})
    if (start["head_sha"] != prior["head_sha"] or
            start["pilot_sha256"] != packet["full_sample_sha256"] or
            start["run_directory"] != str(run_dir) or start["started_utc"] != prior["host_started_utc"] or
            finish["pilot_sha256"] != packet["full_sample_sha256"] or
            finish["run_directory"] != str(run_dir) or finish["finished_utc"] != prior["host_finished_utc"] or
            finish["status"] != prior["terminal_status"] or
            finish["failure_category"] != prior["failure_category"] or
            finish["summary_sha256"] != prior["file_sha256"]["h3-summary.json"] or
            finish["run_manifest_sha256"] != prior["file_sha256"]["run-manifest.json"] or
            finish["runner_terminal_sha256"] is not None or
            finish["wall_seconds"] != prior["reported_wall_seconds"] or
            finish["cpu_seconds"] != prior["reported_cpu_seconds"] or
            finish["watchdog_audit_tip_sha256"] != prior["hash_chain_tips"]["watchdog.jsonl"] or
            finish["evidence_tip_sha256"] != prior["hash_chain_tips"]["h3-evidence.jsonl"]):
        raise RemediationIdentityError("Original host terminal/identity/accounting mismatch")
    after, after_bytes = _snapshot(run_dir, prior["file_sha256"], audit_guard)
    preparation_after, preparation_after_bytes = _preparation_snapshot(
        preparation.parent, prior["preparation_file_sha256"])
    if (after != signatures or after_bytes != output_bytes or identity.sha256_file(ledger) != ledger_sha or
            preparation_after != preparation_signatures or preparation_after_bytes != preparation_bytes or
            _regular_file(preparation) != prep_signature or
            identity.sha256_file(preparation) != prior["preparation_evidence_sha256"]):
        raise RemediationIdentityError("Original evidence changed during read-only verification")
    host_wall = (datetime.fromisoformat(prior["host_finished_utc"]) -
                 datetime.fromisoformat(prior["host_started_utc"])).total_seconds()
    if not math.isfinite(host_wall) or host_wall < prior["reported_wall_seconds"]:
        raise RemediationIdentityError("Original host interval cannot contain Watchdog interval")
    # The approved object is byte-bound by the old manifest. Its confirmation
    # timestamp precedes launch's authorization/import work, which the formal
    # preflight stopwatch did not cover. Charge this wider elapsed window once,
    # never add the already-contained preflight/Watchdog intervals a second time.
    confirmed = datetime.fromisoformat(approved["confirmed_at_utc"])
    host_started = datetime.fromisoformat(prior["host_started_utc"])
    host_finished = datetime.fromisoformat(prior["host_finished_utc"])
    if (confirmed.tzinfo is None or host_started.tzinfo is None or host_finished.tzinfo is None or
            (host_started - confirmed).total_seconds() < prior["preflight_wall_seconds"]):
        raise RemediationIdentityError("Original approved confirmation cannot contain launch/preflight")
    authorization_wall = (host_finished - confirmed).total_seconds()
    if not math.isfinite(authorization_wall) or authorization_wall < host_wall:
        raise RemediationIdentityError("Original authorization window is not a conservative elapsed bound")
    # This is a disclosed CPU upper charge, not an invented historical CPU
    # measurement: eight evidenced cores can consume at most this extra CPU
    # time outside the already-accounted Watchdog interval.
    old_cpu_upper = max(
        prior["reported_cpu_seconds"] + prior["preflight_cpu_seconds"],
        prior["reported_cpu_seconds"] +
        (authorization_wall - prior["reported_wall_seconds"]) * cpu_count)
    return {
        "verification": verification, "old_output_bytes": output_bytes,
        "old_auxiliary_output_bytes": preparation_bytes + old_host_record_bytes,
        "old_preparation_output_bytes": preparation_bytes,
        "old_host_ledger_record_bytes": old_host_record_bytes,
        "old_wall_seconds": prior["reported_wall_seconds"],
        "old_cpu_seconds": prior["reported_cpu_seconds"],
        "old_preflight_wall_seconds": prior["preflight_wall_seconds"],
        "old_preflight_cpu_seconds": prior["preflight_cpu_seconds"],
        "elapsed_controller_seconds": prior["elapsed_controller_seconds"],
        "old_host_wall_seconds": host_wall,
        "old_authorization_window_wall_seconds": authorization_wall,
        "old_authorization_confirmed_at_utc": approved["confirmed_at_utc"],
        "old_segmented_measured_wall_seconds": host_wall + prior["preflight_wall_seconds"],
        "old_wall_charge_seconds": authorization_wall,
        "old_cpu_upper_charge_seconds": old_cpu_upper,
        "controller_wall_difference_seconds": prior["elapsed_controller_seconds"] - prior["reported_wall_seconds"],
        "packet_sha256": packet_sha256(packet), "suffix_sha256": packet["suffix_sha256"],
        "summary_sha256": prior["file_sha256"]["h3-summary.json"],
        "manifest_sha256": prior["file_sha256"]["run-manifest.json"],
        "hash_chain_tips": prior["hash_chain_tips"],
        "host_ledger_sha256_at_verification": ledger_sha,
    }
