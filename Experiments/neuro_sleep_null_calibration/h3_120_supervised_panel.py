"""Draft, fail-closed supervised runner for the fixed 120-row H3 panel.

The packet and candidate limits are engineering preparation only. Biological
execution is rejected until the prospective Q-order amendment is effective
and a current-head, UUID-bound researcher authorization is supplied.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys
import time
import uuid
from collections.abc import Callable, Iterable
from pathlib import Path
from typing import Any

import h3_supervised_pilot as pilot
from g0_q_protocol import (
    CANONICAL_ORDER_POLICY,
    build_canonical_louvain_graph,
    canonical_graph_manifest,
    canonical_graph_payload,
    canonical_louvain_q_vector,
    first_maximum_index,
    q_vector_sha256,
    seed_vector_sha256,
)
from nc0a_watchdog import HashChainLog, WatchdogError, verify_hash_chain
from riken_source_identity import (
    EXPECTED_HISTORICAL_GRAPH_FUNCTION_SHA256,
    EXPECTED_RECORDINGS,
    EXPECTED_SOURCE_CODE_HASHES,
    H3_QMAX_ATOL,
    H3_TRIAL_Q_ATOL_PROPOSED,
    LOUVAIN_TRIALS,
    STATES,
    TARGETS,
    IdentityEvidenceError,
    h3_runtime_manifest,
    hash_float64,
    hash_int64,
    reconstruct_source_graph,
    replay_louvain_q,
    sha256_bytes,
    sha256_file,
)

ROOT = pilot.ROOT
HERE = Path(__file__).resolve().parent
PACKET_FILENAME = "G0_RIKEN_H3_FIXED_120_DUAL_ORDER_PACKET_DRAFT_2026-10-24.json"
MANIFEST_FILENAME = "G0_RIKEN_SOURCE_GRAPH_EXPECTED_MANIFEST_2026-10-21.json"
METHOD_FILENAME = "G0_CANONICAL_Q_ORDER_PROSPECTIVE_AMENDMENT_DRAFT_2026-10-23.md"
EXPECTED_MANIFEST_SHA256 = "6a8357ac0b815c434421a31dc6c294c292b5c144713f49c52b5344038235ece2"
EXPECTED_IDENTITY_TOOL_SHA256 = "ba7c855c1744fcfa1f94dc3d6ffe79cf4196695af1d6d5803beffc83d9c5d73e"
EXPECTED_PACKET_SHA256 = "80b7e49a60082f9827130545f7fcb1dd0ddd6ce43278c538a686ba6b5b757dbb"
HISTORICAL_ORDER_POLICY = "HISTORICAL_GRAPH_INSERTION_ORDER_V1"
PACKET_SCHEMA = "SRT_RIKEN_H3_FIXED_120_DUAL_ORDER_PANEL_V1"
RESULT_SCHEMA = "SRT_RIKEN_H3_120_ROW_RESULT_V1"
EVIDENCE_LOG = "h3-evidence.jsonl"
ROW_DIR = "h3-120-rows"
OUTPUT_PARENT_NAME = "h3_identity_calibration_120_2026-10-24"
MINIMAL_CANDIDATE_LIMITS = {
    "wall_seconds": 8 * 60 * 60,
    "process_tree_cpu_seconds": 8 * 60 * 60,
    "max_compute_workers": 1,
    "sampled_aggregate_rss_bytes": 4 * 1024**3,
    "output_bytes": 1 * 1024**3,
    "memory_semantics": "SAMPLED_RSS_NOT_A_HARD_LIMIT",
}


class H3PanelError(RuntimeError):
    """Fail-closed error for the fixed 120-row panel workflow."""


def _canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def _read_json(path: Path) -> dict[str, Any]:
    return pilot._read_json(path)


def _write_new_json(path: Path, value: object) -> str:
    return pilot._write_new_json(path, value)


def _manifest_rows(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    source_by_id = {row["recording_id"]: row for row in manifest.get("source_data", [])}
    panel = manifest.get("h3_panel", {}).get("records")
    if not isinstance(panel, list):
        raise H3PanelError("Frozen identity manifest has no H3 panel records")
    rows = []
    for index, record in enumerate(panel, 1):
        source = source_by_id.get(record.get("recording_id"))
        if source is None or not isinstance(source.get("filename"), str):
            raise H3PanelError("Panel row does not map to a frozen source artifact")
        rows.append({"panel_order": index, "source_filename": source["filename"], **record})
    return rows


def _validate_panel_shape(rows: list[dict[str, Any]]) -> None:
    if len(rows) != 120:
        raise H3PanelError(f"Fixed H3 panel has {len(rows)} rows, expected exactly 120")
    ids = [row.get("graph_id") for row in rows]
    if len(set(ids)) != 120 or any(not isinstance(item, str) for item in ids):
        raise H3PanelError("Fixed H3 panel graph IDs are missing or duplicated")
    recording_order = list(dict.fromkeys(row["recording_id"] for row in rows))
    if tuple(recording_order) != EXPECTED_RECORDINGS:
        raise H3PanelError("H3 panel recording order differs from the frozen six-source order")
    if {row.get("N") for row in rows} != set(TARGETS):
        raise H3PanelError("H3 panel does not contain the ten frozen N values")
    if {row.get("state") for row in rows} != set(STATES):
        raise H3PanelError("H3 panel state tokens differ from the frozen Wake/NREM labels")
    for recording in EXPECTED_RECORDINGS:
        for n in TARGETS:
            for state in STATES:
                matches = [row for row in rows if row.get("recording_id") == recording
                           and row.get("N") == n and row.get("state") == state]
                if len(matches) != 1:
                    raise H3PanelError(
                        f"Panel must have one row per recording/N/state: {recording}/N{n}/{state}")
    # The frozen manifest order is source recording, ascending N, then wake/NREM.
    expected_order = sorted(
        rows,
        key=lambda row: (EXPECTED_RECORDINGS.index(row["recording_id"]),
                         TARGETS.index(row["N"]), STATES.index(row["state"])),
    )
    if rows != expected_order:
        raise H3PanelError("Panel row order differs from the frozen recording/N/state sequence")


def validate_h3_120_packet(packet_path: Path, manifest_path: Path) -> tuple[dict, dict]:
    if packet_path.is_symlink() or manifest_path.is_symlink():
        raise H3PanelError("Packet and identity manifest cannot be symlinks")
    if sha256_file(packet_path) != EXPECTED_PACKET_SHA256:
        raise H3PanelError("H3-120 packet SHA-256 differs from the fixed packet")
    if sha256_file(manifest_path) != EXPECTED_MANIFEST_SHA256:
        raise H3PanelError("H3-120 source manifest SHA-256 differs from its pin")
    packet, manifest = _read_json(packet_path), _read_json(manifest_path)
    if packet.get("schema") != PACKET_SCHEMA or packet.get("status") != \
            "PREPARED_DRAFT_NOT_AUTHORIZED":
        raise H3PanelError("H3-120 packet schema or non-authorized status changed")
    if (packet.get("source_manifest_sha256") != EXPECTED_MANIFEST_SHA256 or
            packet.get("identity_tool_sha256") != EXPECTED_IDENTITY_TOOL_SHA256 or
            manifest.get("identity_tool_sha256") != EXPECTED_IDENTITY_TOOL_SHA256):
        raise H3PanelError("H3-120 packet does not bind the frozen identity tooling")
    if (packet.get("historical_order_policy") != HISTORICAL_ORDER_POLICY or
            packet.get("canonical_order_policy") != CANONICAL_ORDER_POLICY or
            packet.get("trials_per_order_per_row") != LOUVAIN_TRIALS or
            packet.get("gross_louvain_trials") != 48_000 or
            packet.get("row_count") != 120 or
            packet.get("candidate_resource_limits_not_authorized") !=
            MINIMAL_CANDIDATE_LIMITS):
        raise H3PanelError("H3-120 protocol or candidate resource record changed")
    if packet.get("candidate_cache_credit") != {
        "maximum_historical_trials": 2000,
        "requires_complete_q_vectors_and_exact_identity_match": True,
        "legacy_sorted_edge_diagnostic_is_canonical_cache": False,
        "current_10_graph_pilot_credit": "NOT_ESTABLISHED",
    }:
        raise H3PanelError("H3-120 cache-credit rule changed")
    expected_rows = _manifest_rows(manifest)
    _validate_panel_shape(expected_rows)
    if packet.get("rows") != expected_rows:
        raise H3PanelError("H3-120 row identities/order differ from the fixed source manifest")
    if manifest.get("h3_panel", {}).get("count") != 120:
        raise H3PanelError("Source manifest's fixed H3 panel count is not 120")
    return packet, manifest


def _resource_candidate() -> dict[str, Any]:
    """Expose candidate values to review; this does not activate them."""
    return dict(MINIMAL_CANDIDATE_LIMITS)


def _method_is_effective(method_path: Path) -> tuple[bool, str]:
    if method_path.is_symlink() or not method_path.is_file():
        return False, "method amendment is missing or symlinked"
    text = method_path.read_text(encoding="utf-8")
    frontmatter = text.split("---", 2)
    if len(frontmatter) < 3 or "status: active" not in frontmatter[1]:
        return False, "canonical-Q method amendment is still DRAFT / NOT EFFECTIVE"
    if "DRAFT / NOT EFFECTIVE" in text[:3000]:
        return False, "method amendment still declares DRAFT / NOT EFFECTIVE"
    return True, sha256_file(method_path)


def validate_researcher_authorization(authorization_path: Path, *, packet_sha256: str,
                                      method_path: Path, expected_head: str,
                                      run_id: str, confirmation: str) -> dict[str, Any]:
    """Check explicit prospective approval; no test authorization is accepted."""
    effective, method_identity = _method_is_effective(method_path)
    if not effective:
        raise H3PanelError(method_identity)
    if authorization_path.is_symlink() or not authorization_path.is_file():
        raise H3PanelError("A real, current researcher authorization file is required")
    approval = _read_json(authorization_path)
    try:
        canonical_run_id = str(uuid.UUID(run_id))
    except (ValueError, TypeError, AttributeError) as exc:
        raise H3PanelError("Run identity must be a canonical UUID") from exc
    expected_confirmation = (
        f"I AUTHORIZE H3-120 {canonical_run_id} {packet_sha256} {expected_head}")
    if confirmation != expected_confirmation:
        raise H3PanelError("UUID/packet/HEAD-bound researcher confirmation is missing")
    if (approval.get("schema") != "SRT_H3_120_RESEARCHER_AUTHORIZATION_V1" or
            approval.get("status") != "APPROVED_FOR_EXECUTION" or
            approval.get("method_amendment_status") != "EFFECTIVE" or
            approval.get("method_amendment_sha256") != method_identity or
            approval.get("packet_sha256") != packet_sha256 or
            approval.get("head_sha") != expected_head or
            approval.get("run_uuid") != canonical_run_id or
            approval.get("resource_limits") != MINIMAL_CANDIDATE_LIMITS or
            approval.get("max_compute_workers") != 1 or
            approval.get("memory_semantics") != "SAMPLED_RSS_NOT_A_HARD_LIMIT"):
        raise H3PanelError("Researcher authorization does not bind this method/packet/head/run/budget")
    return {"authorization_sha256": sha256_file(authorization_path),
            "method_amendment_sha256": method_identity,
            "status": approval["status"]}


def _legacy_private_rows(packet: dict[str, Any]) -> dict[str, Any]:
    """Adapt frozen public rows to the already-tested private-root validator."""
    rows = []
    for item in packet["rows"]:
        rows.append({
            "recording_id": item["recording_id"],
            "source_filename": item["source_filename"],
            "source_mat_sha256": item["source_artifact_sha256"],
            "subset_repeat": item["subset_repeat"],
            "N": item["N"],
            "historical_job_sha256": item["historical_job_sha256"],
            "selected_neuron_indices_sha256": item["selected_neuron_indices_sha256"],
            "expected_node_order_sha256": item["expected_node_order_sha256"],
            "historical_louvain_seed_vector_sha256":
                item["historical_louvain_seed_vector_sha256"],
            "historical_q_vector_sha256": item["historical_q_vector_sha256"],
            "expected_edge_count": item["expected_edge_count"],
        })
    manifest_stub = {
        "historical_code_hashes": EXPECTED_SOURCE_CODE_HASHES,
        "source_data": [{"recording_id": row["recording_id"],
                         "filename": row["source_filename"]}
                        for row in packet["rows"]],
    }
    # Preserve one source record per recording while keeping exactly the frozen filename.
    manifest_stub["source_data"] = list({
        row["recording_id"]: {"recording_id": row["recording_id"],
                              "filename": row["source_filename"]}
        for row in packet["rows"]}.values())
    return {"historical_graph_builder_sha256":
            EXPECTED_SOURCE_CODE_HASHES["multirecording_primary.py"],
            "records": rows}, manifest_stub


def validate_h3_120_private_roots(packet: dict[str, Any], manifest: dict[str, Any],
                                  phase2_root: Path, psa_root: Path) -> tuple[Path, Path]:
    adapted, stub = _legacy_private_rows(packet)
    # The existing validator checks source/job identities, but its stub's source
    # records need the public file sizes too. Rebuild those from the pinned manifest.
    source_by_id = {row["recording_id"]: row for row in manifest["source_data"]}
    stub["source_data"] = [source_by_id[key] for key in EXPECTED_RECORDINGS]
    return pilot._validate_private_roots(phase2_root, psa_root, adapted, stub)


def _runtime_hash(runtime: dict[str, Any]) -> str:
    return sha256_bytes(_canonical(runtime))


def _implementation_hash() -> str:
    return sha256_bytes(_canonical({
        "h3_120_runner": sha256_file(Path(__file__)),
        "h3_pilot_supervisor": sha256_file(HERE / "h3_supervised_pilot.py"),
        "riken_identity": sha256_file(HERE / "riken_source_identity.py"),
        "g0_q_protocol": sha256_file(HERE / "g0_q_protocol.py"),
        "historical_graph_function": EXPECTED_HISTORICAL_GRAPH_FUNCTION_SHA256,
        "historical_builder_file": EXPECTED_SOURCE_CODE_HASHES[
            "multirecording_primary.py"],
    }))


def _graph_labeled_edges(graph, source_ids: Iterable[int]) -> list[tuple[int, int]]:
    ids = tuple(map(int, source_ids))
    if set(graph.nodes) != set(range(len(ids))) or len(ids) != len(graph):
        raise H3PanelError("Historical graph nodes do not map to the saved source-neuron vector")
    return [(ids[int(u)], ids[int(v)]) for u, v in graph.edges]


def _q_stats(values: Iterable[float]) -> dict[str, Any]:
    q = [float(value) for value in values]
    if len(q) != LOUVAIN_TRIALS or any(not math.isfinite(value) for value in q):
        raise H3PanelError("Each H3 order must produce exactly 200 finite Q values")
    first = first_maximum_index(q)
    return {"q_vector": q, "q_vector_sha256": q_vector_sha256(q),
            "q_max_200": q[first], "first_max_trial_index": first,
            "trial_count": len(q)}


def planned_louvain_trials(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Count all trials; the fixed pilot artifacts lack complete replay Q vectors."""
    _validate_panel_shape(rows)
    return {"gross_trials": 48_000, "historical_pilot_trials_credited": 0,
            "planned_new_trials": 48_000,
            "reuse_status": "NOT_ESTABLISHED_NO_COMPLETE_Q_VECTOR_ARTIFACT"}


def compute_dual_order_q(*, historical_graph, source_ids: Iterable[int],
                          seeds: Iterable[int], reference_q: Iterable[float],
                          reference_qmax_first_index: int,
                          reference_qmax: float,
                          historical_replay: Callable[..., dict[str, Any]] | None = None,
                          canonical_replay: Callable[..., dict[str, Any]] | None = None
                          ) -> dict[str, Any]:
    """Replay legacy order first; a historical failure stops before canonical work."""
    seed_values = tuple(map(int, seeds))
    if len(seed_values) != LOUVAIN_TRIALS:
        raise H3PanelError("Frozen H3 seed vector must contain exactly 200 seeds")
    reference_values = [float(value) for value in reference_q]
    if len(reference_values) != LOUVAIN_TRIALS or any(
            not math.isfinite(value) for value in reference_values):
        raise H3PanelError("Historical reference Q vector is invalid")
    replay_historical = historical_replay or replay_louvain_q
    replay_canonical = canonical_replay or canonical_louvain_q_vector
    historical = replay_historical(historical_graph, seed_values, require_target=True)
    history = _q_stats(historical["q_values"])
    ref_stats = _q_stats(reference_values)
    deltas = [actual - expected for actual, expected in
              zip(history["q_vector"], reference_values, strict=True)]
    max_trial_abs = max(abs(value) for value in deltas)
    qmax_abs = abs(history["q_max_200"] - float(reference_qmax))
    if (max_trial_abs > H3_TRIAL_Q_ATOL_PROPOSED or
            qmax_abs > H3_QMAX_ATOL or
            ref_stats["q_max_200"] != float(reference_qmax) or
            ref_stats["first_max_trial_index"] != reference_qmax_first_index or
            history["first_max_trial_index"] != reference_qmax_first_index):
        raise H3PanelError("HISTORICAL_Q_INTEGRITY_FAILURE; canonical replay not started")
    edges = _graph_labeled_edges(historical_graph, source_ids)
    canonical = replay_canonical(tuple(map(int, source_ids)), edges, seed_values)
    canonical_stats = _q_stats(canonical["q_values"])
    differences = [value - old for value, old in
                   zip(canonical_stats["q_vector"], history["q_vector"], strict=True)]
    return {
        "historical_order_q_replay": "PASS",
        "historical_q_vector": history["q_vector"],
        "historical_q_vector_sha256": history["q_vector_sha256"],
        "historical_reference_q_vector": reference_values,
        "historical_reference_q_vector_sha256": ref_stats["q_vector_sha256"],
        "historical_reference_trial_abs_deltas": [abs(value) for value in deltas],
        "historical_reference_max_abs_delta": max_trial_abs,
        "historical_reference_qmax_abs_delta": qmax_abs,
        "historical_qmax": history["q_max_200"],
        "historical_first_max_trial_index": history["first_max_trial_index"],
        "canonical_order_policy": CANONICAL_ORDER_POLICY,
        "canonical_q_vector": canonical_stats["q_vector"],
        "canonical_q_vector_sha256": canonical_stats["q_vector_sha256"],
        "canonical_qmax": canonical_stats["q_max_200"],
        "canonical_first_max_trial_index": canonical_stats["first_max_trial_index"],
        "canonical_minus_historical_q_differences": differences,
        "canonical_vs_historical_max_abs_delta": max(map(abs, differences)),
        "canonical_vs_historical_status": "DIAGNOSTIC_ONLY_NO_PASS_THRESHOLD",
        "historical_first_max_index_must_match": True,
        "trial_q_absolute_tolerance": H3_TRIAL_Q_ATOL_PROPOSED,
        "trial_q_relative_tolerance": 0.0,
        "qmax_absolute_tolerance": H3_QMAX_ATOL,
    }


def _cache_identity(row: dict[str, Any], *, labeled_edge_set_sha256: str,
                    topology_sha256: str, ordered_representation_sha256: str,
                    order_policy: str, seed_sha: str, runtime_sha: str,
                    implementation_sha: str,
                    source_frame_indices_sha256: str,
                    historical_q_vector_sha256: str) -> dict[str, Any]:
    identity = {
        "graph_id": row["graph_id"],
        "source_artifact_sha256": row["source_artifact_sha256"],
        "selected_neuron_indices_sha256": row["selected_neuron_indices_sha256"],
        "expected_node_order_sha256": row["expected_node_order_sha256"],
        "source_frame_indices_sha256": source_frame_indices_sha256,
        "historical_job_sha256": row["historical_job_sha256"],
        "historical_q_vector_sha256": historical_q_vector_sha256,
        "labeled_edge_set_sha256": labeled_edge_set_sha256,
        "topology_sha256": topology_sha256,
        "ordered_representation_sha256": ordered_representation_sha256,
        "order_policy": order_policy,
        "seed_vector_sha256": seed_sha,
        "runtime_manifest_sha256": runtime_sha,
        "implementation_sha256": implementation_sha,
    }
    return identity


def _validate_result_identity(result: dict[str, Any], row: dict[str, Any], *,
                              expected_runtime_sha256: str,
                              expected_implementation_sha256: str,
                              allow_non_target_runtime: bool = False) -> None:
    """Bind each result and both order identities to its frozen panel row/run."""
    expected_fields = {
        "panel_order": row["panel_order"],
        "graph_id": row["graph_id"],
        "recording_id": row["recording_id"],
        "N": row["N"],
        "state": row["state"],
        "subset_repeat": row["subset_repeat"],
        "window_id": row["window_id"],
        "source_artifact_sha256": row["source_artifact_sha256"],
        "selected_neuron_indices_sha256": row["selected_neuron_indices_sha256"],
        "expected_node_order_sha256": row["expected_node_order_sha256"],
        "source_frame_indices_sha256": row["source_frame_indices_sha256"],
        "historical_job_sha256": row["historical_job_sha256"],
        "seed_vector_sha256": row["historical_louvain_seed_vector_sha256"],
        "historical_reference_q_vector_sha256": row["historical_q_vector_sha256"],
    }
    if any(result.get(key) != value for key, value in expected_fields.items()):
        raise H3PanelError(
            "SOURCE_GRAPH_IDENTITY_FAILURE: result fields differ from the fixed H3 panel row")
    runtime = result.get("runtime_manifest")
    if (not isinstance(runtime, dict) or _runtime_hash(runtime) !=
            result.get("runtime_manifest_sha256") or
            result.get("runtime_manifest_sha256") != expected_runtime_sha256 or
            (not allow_non_target_runtime and not runtime.get(
                "replay_environment_matches_recorded_versions_and_candidate_lock"))):
        raise H3PanelError("Result runtime manifest differs from the supervised run identity")
    if result.get("implementation_sha256") != expected_implementation_sha256:
        raise H3PanelError("Result implementation hash differs from the supervised run identity")

    historical = result.get("historical_cache_identity")
    canonical = result.get("canonical_cache_identity")
    if not isinstance(historical, dict) or not isinstance(canonical, dict):
        raise H3PanelError("Both order-specific graph identities are required")
    for identity, policy, representation_hash in (
            (historical, HISTORICAL_ORDER_POLICY,
             result.get("historical_adjacency_iteration_sha256")),
            (canonical, CANONICAL_ORDER_POLICY,
             result.get("canonical_ordered_representation_sha256"))):
        if any(identity.get(key) != value for key, value in (
                ("graph_id", row["graph_id"]),
                ("source_artifact_sha256", row["source_artifact_sha256"]),
                ("selected_neuron_indices_sha256",
                 row["selected_neuron_indices_sha256"]),
                ("expected_node_order_sha256", row["expected_node_order_sha256"]),
                ("source_frame_indices_sha256", row["source_frame_indices_sha256"]),
                ("historical_job_sha256", row["historical_job_sha256"]),
                ("historical_q_vector_sha256", row["historical_q_vector_sha256"]),
                ("seed_vector_sha256",
                 row["historical_louvain_seed_vector_sha256"]),
                ("runtime_manifest_sha256", expected_runtime_sha256),
                ("implementation_sha256", expected_implementation_sha256),
                ("order_policy", policy),
                ("ordered_representation_sha256", representation_hash))):
            raise H3PanelError(
                "SOURCE_GRAPH_IDENTITY_FAILURE: ordered graph identity differs from fixed inputs")
    if (historical.get("labeled_edge_set_sha256") !=
            canonical.get("labeled_edge_set_sha256") or
            historical.get("topology_sha256") != canonical.get("topology_sha256")):
        raise H3PanelError(
            "SOURCE_GRAPH_IDENTITY_FAILURE: dual orders do not share one labeled topology")


def _process_private_row(row: dict[str, Any], manifest: dict[str, Any],
                         phase2_root: Path, psa_root: Path,
                         source_hash_cache: dict[str, tuple[str, tuple[int, int, int, int]]]
                         ) -> dict[str, Any]:
    compat = {
        **row,
        "source_mat_sha256": row["source_artifact_sha256"],
        "historical_louvain_seed_vector_sha256":
            row["historical_louvain_seed_vector_sha256"],
        "historical_q_vector_sha256": row["historical_q_vector_sha256"],
        "source_and_reference_status": "HASHES_AND_200_SEEDS_VERIFIED; GRAPH_NOT_REBUILT",
    }
    source_path, selected, reference, _panel_row = pilot._load_private_row(
        compat, manifest, phase2_root, psa_root, source_hash_cache)
    graph_pair = reconstruct_source_graph(
        source_path, selected, row["state"], row["window_id"],
        phase2_root / "multirecording_primary.py")
    historical_graph = graph_pair["historical_graph"]
    if (historical_graph.number_of_nodes() != row["N"] or
            historical_graph.number_of_edges() != row["expected_edge_count"] or
            graph_pair["source_frame_indices_sha256"] != row["source_frame_indices_sha256"] or
            hash_int64(selected) != row["expected_node_order_sha256"] or
            graph_pair["historical_edge_set_sha256"] !=
            graph_pair["candidate_edge_set_sha256"]):
        raise H3PanelError("SOURCE_GRAPH_IDENTITY_FAILURE")
    seeds = reference["louvain_seeds"]
    if hash_int64(seeds) != row["historical_louvain_seed_vector_sha256"]:
        raise H3PanelError("HISTORICAL_SEED_IDENTITY_FAILURE")
    if hash_float64(reference["q_values"]) != row["historical_q_vector_sha256"]:
        raise H3PanelError("HISTORICAL_Q_REFERENCE_IDENTITY_FAILURE")

    runtime = h3_runtime_manifest()
    if not runtime["replay_environment_matches_recorded_versions_and_candidate_lock"]:
        raise H3PanelError("TARGET_RUNTIME_MISMATCH")
    runtime_sha = _runtime_hash(runtime)
    implementation_sha = _implementation_hash()
    labeled_edges = _graph_labeled_edges(historical_graph, selected)
    payload = canonical_graph_payload(tuple(map(int, selected)), labeled_edges)
    topology_hash = canonical_graph_manifest(payload)["topology_sha256"]
    labeled_sha = sha256_bytes(_canonical(sorted(tuple(sorted(edge))
                                                   for edge in labeled_edges)))
    historical_identity = _cache_identity(
        row, labeled_edge_set_sha256=labeled_sha, topology_sha256=topology_hash,
        ordered_representation_sha256=graph_pair["historical_adjacency_iteration_sha256"],
        order_policy=HISTORICAL_ORDER_POLICY,
        seed_sha=seed_vector_sha256(seeds), runtime_sha=runtime_sha,
        implementation_sha=implementation_sha,
        source_frame_indices_sha256=graph_pair["source_frame_indices_sha256"],
        historical_q_vector_sha256=row["historical_q_vector_sha256"])
    hist_replay = replay_louvain_q(historical_graph, seeds, require_target=True)
    hist_replay["cache_reused"] = False
    # Validate saved historic Q before any canonical Louvain call.
    hist_stats = _q_stats(hist_replay["q_values"])
    reference_q = list(map(float, reference["q_values"]))
    history_deltas = [abs(a - b) for a, b in
                      zip(hist_stats["q_vector"], reference_q, strict=True)]
    if (max(history_deltas) > H3_TRIAL_Q_ATOL_PROPOSED or
            abs(hist_stats["q_max_200"] - float(reference["historical_q_max"])) > H3_QMAX_ATOL or
            hist_stats["first_max_trial_index"] != reference["q_max_first_index"]):
        raise H3PanelError("HISTORICAL_Q_INTEGRITY_FAILURE; canonical replay not started")

    _canonical_graph, canonical_manifest = build_canonical_louvain_graph(
        tuple(map(int, selected)), labeled_edges)
    canonical_identity = _cache_identity(
        row, labeled_edge_set_sha256=labeled_sha,
        topology_sha256=canonical_manifest["topology_sha256"],
        ordered_representation_sha256=canonical_manifest["ordered_representation_sha256"],
        order_policy=CANONICAL_ORDER_POLICY,
        seed_sha=seed_vector_sha256(seeds), runtime_sha=runtime_sha,
        implementation_sha=implementation_sha,
        source_frame_indices_sha256=graph_pair["source_frame_indices_sha256"],
        historical_q_vector_sha256=row["historical_q_vector_sha256"])
    # The ten-graph pilot's sorted-edge vector is not a canonical cache. Its
    # archived result also lacks complete Q vectors, so today's safe default is
    # to compute all 24,000 canonical trials anew.
    canonical_run = canonical_louvain_q_vector(
        tuple(map(int, selected)), labeled_edges, seeds)
    canonical_run["cache_reused"] = False
    result = compute_dual_order_q(
        historical_graph=historical_graph, source_ids=selected, seeds=seeds,
        reference_q=reference_q,
        reference_qmax_first_index=reference["q_max_first_index"],
        reference_qmax=reference["historical_q_max"],
        historical_replay=lambda *_args, **_kwargs: hist_replay,
        canonical_replay=lambda *_args, **_kwargs: canonical_run)
    result.update({
        "schema": RESULT_SCHEMA,
        "panel_order": row["panel_order"],
        "graph_id": row["graph_id"],
        "recording_id": row["recording_id"],
        "N": row["N"], "state": row["state"],
        "subset_repeat": row["subset_repeat"], "window_id": row["window_id"],
        "source_graph_identity": "PASS",
        "historical_edge_set_sha256": graph_pair["historical_labeled_edge_set_sha256"],
        "historical_adjacency_iteration_sha256":
            graph_pair["historical_adjacency_iteration_sha256"],
        "canonical_topology_sha256": canonical_manifest["topology_sha256"],
        "canonical_ordered_representation_sha256":
            canonical_manifest["ordered_representation_sha256"],
        "source_artifact_sha256": row["source_artifact_sha256"],
        "selected_neuron_indices_sha256": row["selected_neuron_indices_sha256"],
        "expected_node_order_sha256": row["expected_node_order_sha256"],
        "source_frame_indices_sha256": graph_pair["source_frame_indices_sha256"],
        "historical_job_sha256": reference["historical_job_sha256"],
        "seed_vector_sha256": hash_int64(seeds),
        "historical_reference_q_vector_sha256":
            row["historical_q_vector_sha256"],
        "labeled_edge_set_sha256": labeled_sha,
        "runtime_manifest": runtime,
        "runtime_manifest_sha256": runtime_sha,
        "implementation_sha256": implementation_sha,
        "historical_cache_reused": bool(hist_replay.get("cache_reused")),
        "canonical_cache_reused": bool(canonical_run.get("cache_reused")),
        "canonical_order_policy": CANONICAL_ORDER_POLICY,
        "elapsed_seconds": None,
    })
    result["historical_cache_identity"] = historical_identity
    result["canonical_cache_identity"] = canonical_identity
    return result


def execute_ordered_panel(rows: list[dict[str, Any]], *, run_dir: Path,
                          process_row: Callable[[dict[str, Any]], dict[str, Any]],
                          before_row: Callable[[dict[str, Any]], None] | None = None,
                          synthetic_test_only: bool = False
                          ) -> dict[str, Any]:
    """Run rows in fixed order, persist full vectors, and fail-stop on first error."""
    _validate_panel_shape(rows)
    evidence_path = run_dir / EVIDENCE_LOG
    row_dir = run_dir / ROW_DIR
    row_dir.mkdir(mode=0o700, exist_ok=True)
    outcomes = []
    with HashChainLog(evidence_path) as evidence:
        evidence.append({"kind": "h3_120_runner_started", "packet_sha256":
                         EXPECTED_PACKET_SHA256,
                         "runner_sha256": sha256_file(Path(__file__)),
                         "runtime": h3_runtime_manifest(),
                         "runtime_manifest_sha256": _runtime_hash(h3_runtime_manifest()),
                         "implementation_sha256": _implementation_hash(),
                         "synthetic_test_only": synthetic_test_only,
                         "gross_louvain_trials": 48_000,
                         "cache_credit_rule": "COMPLETE_IDENTITY_AND_VECTOR_ONLY"})
        for row in rows:
            if before_row:
                before_row(row)
            evidence.append({"kind": "graph_started", "panel_order": row["panel_order"],
                             "graph_id": row["graph_id"], "N": row["N"],
                             "recording_id": row["recording_id"],
                             "state": row["state"],
                             "historical_job_sha256": row["historical_job_sha256"],
                             "seed_vector_sha256":
                                 row["historical_louvain_seed_vector_sha256"]})
            started_wall, started_cpu = time.perf_counter(), time.process_time()
            try:
                result = process_row(row)
                result = {**result,
                          "schema": RESULT_SCHEMA,
                          "panel_order": row["panel_order"],
                          "graph_id": row["graph_id"],
                          "elapsed_seconds": time.perf_counter() - started_wall,
                          "process_cpu_seconds": time.process_time() - started_cpu}
                required = (result.get("source_graph_identity") == "PASS" and
                            result.get("historical_order_q_replay") == "PASS" and
                            result.get("canonical_order_policy") == CANONICAL_ORDER_POLICY)
                if not required:
                    raise H3PanelError("Row did not pass source/history identity or lacks canonical Q")
                hist_q = result.get("historical_q_vector")
                canonical_q = result.get("canonical_q_vector")
                if (not isinstance(hist_q, list) or not isinstance(canonical_q, list) or
                        len(hist_q) != LOUVAIN_TRIALS or len(canonical_q) != LOUVAIN_TRIALS):
                    raise H3PanelError("Row result does not contain both complete 200-Q vectors")
                if result.get("canonical_cache_reused"):
                    raise H3PanelError("Canonical-order trials cannot be credited from the old pilot")
                if result.get("historical_cache_reused"):
                    raise H3PanelError(
                        "Legacy pilot reuse is disabled until full vectors and audit linkage exist")
                runtime_sha = _runtime_hash(h3_runtime_manifest())
                implementation_sha = _implementation_hash()
                _validate_result_identity(
                    result, row, expected_runtime_sha256=runtime_sha,
                    expected_implementation_sha256=implementation_sha,
                    allow_non_target_runtime=synthetic_test_only)
                artifact_name = f"{row['panel_order']:03d}-{hashlib.sha256(row['graph_id'].encode()).hexdigest()[:12]}.json"
                artifact_path = row_dir / artifact_name
                artifact_sha = _write_new_json(artifact_path, result)
                outcome = {
                    "kind": "graph_result", "panel_order": row["panel_order"],
                    "pilot_order": row["panel_order"],
                    "graph_id": row["graph_id"], "N": row["N"],
                    "source_graph_identity": "PASS",
                    "historical_order_q_replay": "PASS",
                    "canonical_order_policy": CANONICAL_ORDER_POLICY,
                    "runtime_manifest_sha256": result["runtime_manifest_sha256"],
                    "implementation_sha256": result["implementation_sha256"],
                    "source_artifact_sha256": row["source_artifact_sha256"],
                    "historical_job_sha256": row["historical_job_sha256"],
                    "seed_vector_sha256": row[
                        "historical_louvain_seed_vector_sha256"],
                    "historical_reference_q_vector_sha256": row[
                        "historical_q_vector_sha256"],
                    "result_artifact": f"{ROW_DIR}/{artifact_name}",
                    "result_artifact_sha256": artifact_sha,
                    "historical_q_vector_sha256": result["historical_q_vector_sha256"],
                    "canonical_q_vector_sha256": result["canonical_q_vector_sha256"],
                    "historical_cache_reused": bool(result.get("historical_cache_reused")),
                    "canonical_cache_reused": bool(result.get("canonical_cache_reused")),
                    "louvain_trials_computed": 200 * (
                        int(not result.get("historical_cache_reused")) +
                        int(not result.get("canonical_cache_reused"))),
                    "elapsed_seconds": result["elapsed_seconds"],
                    "process_cpu_seconds": result["process_cpu_seconds"],
                }
            # Any ordinary row exception is persisted and fail-stopped. This
            # intentionally includes unclassified runtime errors; BaseException
            # subclasses (KeyboardInterrupt/SystemExit) still propagate.
            except Exception as exc:  # noqa: BLE001
                message = str(exc)[:500]
                if (isinstance(exc, IdentityEvidenceError) or
                        isinstance(exc, H3PanelError) and message.startswith((
                        "SOURCE_GRAPH_IDENTITY_FAILURE",
                        "HISTORICAL_SEED_IDENTITY_FAILURE",
                        "HISTORICAL_Q_REFERENCE_IDENTITY_FAILURE",
                        "HISTORICAL_Q_INTEGRITY_FAILURE"))):
                    failure_status = "scientific_integrity_failure"
                    failure_category = "SCIENTIFIC_IDENTITY_OR_Q_FAILURE"
                else:
                    failure_status = "unclassified_exception"
                    failure_category = "UNKNOWN_FAILURE_FAIL_STOP"
                outcome = {"kind": "graph_result", "panel_order": row["panel_order"],
                           "graph_id": row["graph_id"], "N": row["N"],
                           "source_graph_identity": "FAIL_OR_UNRESOLVED",
                           "historical_order_q_replay": "FAIL_OR_NOT_RUN",
                           "canonical_order_policy": CANONICAL_ORDER_POLICY,
                           "status": "STOPPED_ON_FIRST_FAILURE",
                           "failure_type": type(exc).__name__,
                           "failure_reason": message,
                           "failure_category": failure_category,
                           "resume_allowed": False,
                           "elapsed_seconds": time.perf_counter() - started_wall,
                           "process_cpu_seconds": time.process_time() - started_cpu}
                evidence.append(outcome)
                evidence.append({"kind": "pilot_stopped", "status":
                                 failure_status, "failure_graph_id":
                                 row["graph_id"], "resume_allowed": False})
                _write_new_json(run_dir / "runner-terminal.json", {
                    "kind": "pilot_stopped", "status": failure_status,
                    "failure_graph_id": row["graph_id"], "resume_allowed": False,
                    "evidence_tip_sha256": evidence.previous})
                return {"status": failure_status, "outcomes": outcomes + [outcome],
                        "evidence_tip_sha256": evidence.previous}
            evidence.append(outcome)
            outcomes.append(outcome)
        terminal = {"kind": "pilot_completed", "status": "completed",
                    "rows_completed": 120, "resume_allowed": False,
                    "louvain_trials_gross": 48_000,
                    "synthetic_test_only": synthetic_test_only,
                    "scientific_interpretation":
                        "HISTORICAL_Q_REPLAY_PLUS_PROSPECTIVE_CANONICAL_DIAGNOSTIC"}
        evidence.append(terminal)
        _write_new_json(run_dir / "runner-terminal.json", terminal)
        return {"status": "completed", "outcomes": outcomes,
                "evidence_tip_sha256": evidence.previous}


def _prepare_output_directory(run_dir: Path, psa_root: Path, run_id: str) -> tuple[Path, Path]:
    try:
        if str(uuid.UUID(run_id)) != run_id:
            raise ValueError("noncanonical UUID")
    except (ValueError, TypeError, AttributeError) as exc:
        raise H3PanelError("Run identity must be a canonical UUID") from exc
    root = pilot._resolve_private_root(psa_root, "SRT_PSA_ROOT")
    if not run_dir.is_absolute() or ".." in run_dir.parts or run_dir.name != run_id:
        raise H3PanelError("H3-120 run directory must be absolute, traversal-free, and UUID-named")
    target = Path(os.path.abspath(run_dir.expanduser()))
    parent = root / OUTPUT_PARENT_NAME
    if target.parent != parent or parent.is_symlink():
        raise H3PanelError("H3-120 output must be in its dedicated fixed private directory")
    if target.exists() or target.is_symlink():
        raise H3PanelError("H3-120 output directory already exists; refusing overwrite/reuse")
    parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    if parent.is_symlink() or parent.resolve(strict=True) != parent:
        raise H3PanelError("H3-120 output parent changed or contains a symlink")
    return target, parent


def _candidate_watchdog_limits():
    candidate = {
        "wall_seconds": MINIMAL_CANDIDATE_LIMITS["wall_seconds"],
        "process_tree_cpu_seconds": MINIMAL_CANDIDATE_LIMITS["process_tree_cpu_seconds"],
        "max_compute_workers": MINIMAL_CANDIDATE_LIMITS["max_compute_workers"],
        "sampled_aggregate_rss_bytes":
            MINIMAL_CANDIDATE_LIMITS["sampled_aggregate_rss_bytes"],
        "output_bytes": MINIMAL_CANDIDATE_LIMITS["output_bytes"],
    }
    return pilot._build_watchdog_limits(candidate)


def _runner_child() -> int:
    run_dir = Path.cwd()
    try:
        from nc0a_watchdog import guard_watchdog_parent
        parent_pid = int(os.environ.get("NC0A_WATCHDOG_PARENT_PID", "0"))
        guard_watchdog_parent(parent_pid)
        pilot._write_runner_lease(run_dir)
        packet_path = Path(os.environ["SRT_H3_120_PACKET_PATH"])
        manifest_path = Path(os.environ["SRT_H3_120_MANIFEST_PATH"])
        phase2_root = Path(os.environ["SRT_H3_PHASE2_ROOT"])
        psa_root = Path(os.environ["SRT_H3_PSA_ROOT"])
        packet, manifest = validate_h3_120_packet(packet_path, manifest_path)
        # Revalidate all private file identities inside the supervised child.
        validate_h3_120_private_roots(packet, manifest, phase2_root, psa_root)
        evidence_path = run_dir / EVIDENCE_LOG
        with HashChainLog(evidence_path) as evidence:
            evidence.append({"kind": "h3_120_private_runner_started",
                             "packet_sha256": EXPECTED_PACKET_SHA256,
                             "runner_sha256": sha256_file(Path(__file__)),
                             "identity_tool_sha256": sha256_file(
                                 HERE / "riken_source_identity.py"),
                             "q_protocol_sha256": sha256_file(HERE / "g0_q_protocol.py"),
                             "runtime": h3_runtime_manifest(),
                             "compute_workers": 1,
                             "louvain_trials_gross": 48_000})
        # execute_ordered_panel opens/appends the same chain. The initial record
        # above is written in a separate close; it remains hash chained.
        source_hash_cache: dict[str, tuple[str, tuple[int, int, int, int]]] = {}
        result = execute_ordered_panel(
            packet["rows"], run_dir=run_dir,
            process_row=lambda row: _process_private_row(
                row, manifest, phase2_root, psa_root, source_hash_cache))
        return 0 if result["status"] == "completed" else 31
    # Preserve evidence for any ordinary child failure, including unexpected
    # dependency/runtime errors; process-control BaseException subclasses escape.
    except Exception as exc:  # noqa: BLE001
        try:
            evidence_path = run_dir / EVIDENCE_LOG
            if evidence_path.is_file() and not evidence_path.is_symlink():
                with HashChainLog(evidence_path) as evidence:
                    evidence.append({"kind": "runner_exception",
                                     "type": type(exc).__name__,
                                     "reason": str(exc)[:500],
                                     "resume_allowed": False})
                    pilot._write_new_json(run_dir / "runner-terminal.json", {
                        "kind": "pilot_stopped", "status": "unclassified_exception",
                        "failure_type": type(exc).__name__, "resume_allowed": False,
                        "evidence_tip_sha256": evidence.previous})
        except (OSError, WatchdogError, ValueError) as audit_exc:
            print(f"H3-120 failure audit could not be completed: {audit_exc}",
                  file=sys.stderr)
        print(f"H3-120 runner stopped: {type(exc).__name__}: {str(exc)[:500]}",
              file=sys.stderr)
        return 32


def verify_h3_120_run(run_dir: Path, *, expected_packet_sha256: str = EXPECTED_PACKET_SHA256,
                      host_state_dir: Path | None = None) -> dict[str, Any]:
    base = pilot._verify_recovery_directory(run_dir, host_state_dir=host_state_dir)
    if run_dir.is_symlink() or not run_dir.is_dir():
        raise H3PanelError("H3-120 run directory is missing or symlinked")
    evidence_path = run_dir / EVIDENCE_LOG
    verify_hash_chain(evidence_path)
    events = [json.loads(line)["event"] for line in
              evidence_path.read_text(encoding="utf-8").splitlines()]
    starts = [item for item in events if item.get("kind") == "h3_120_runner_started"]
    rows = [item for item in events if item.get("kind") == "graph_result"]
    if len(starts) != 1 or starts[0].get("packet_sha256") != expected_packet_sha256:
        raise H3PanelError("H3-120 evidence start record does not bind the fixed packet")
    packet, _ = validate_h3_120_packet(HERE / PACKET_FILENAME,
                                       HERE / MANIFEST_FILENAME)
    expected = packet["rows"]
    if len(rows) > 120 or [event.get("graph_id") for event in rows] != [
            row["graph_id"] for row in expected[:len(rows)]]:
        raise H3PanelError("H3-120 result events are missing, duplicated, or out of order")
    terminal_path = run_dir / "runner-terminal.json"
    terminal = _read_json(terminal_path) if terminal_path.is_file() else {}
    verified_artifacts = 0
    expected_artifact_names: set[str] = set()
    for event in rows:
        if event.get("status") == "STOPPED_ON_FIRST_FAILURE":
            if (event.get("resume_allowed") is not False or
                    event.get("failure_category") not in (
                        "SCIENTIFIC_IDENTITY_OR_Q_FAILURE", "UNKNOWN_FAILURE_FAIL_STOP") or
                    event.get("result_artifact") is not None):
                raise H3PanelError("H3-120 failure event is not an authenticated fail-stop record")
            continue
        relative = Path(event.get("result_artifact", ""))
        if (relative.is_absolute() or ".." in relative.parts or
                relative.parts[:1] != (ROW_DIR,)):
            raise H3PanelError("H3-120 result artifact path is invalid")
        path = run_dir / relative
        expected_artifact_names.add(path.name)
        if path.is_symlink() or not path.is_file() or sha256_file(path) != \
                event.get("result_artifact_sha256"):
            raise H3PanelError("H3-120 result artifact is missing or its hash changed")
        artifact = _read_json(path)
        panel_order = event.get("panel_order")
        if type(panel_order) is not int or not 1 <= panel_order <= 120:
            raise H3PanelError("H3-120 result event has an invalid panel position")
        expected_row = expected[panel_order - 1]
        if (event.get("graph_id") != expected_row["graph_id"] or
                artifact.get("schema") != RESULT_SCHEMA or
                artifact.get("graph_id") != event.get("graph_id") or
                artifact.get("source_graph_identity") != "PASS" or
                artifact.get("historical_order_q_replay") != "PASS" or
                artifact.get("canonical_order_policy") != CANONICAL_ORDER_POLICY or
                artifact.get("historical_q_vector_sha256") != event.get(
                    "historical_q_vector_sha256") or
                artifact.get("canonical_q_vector_sha256") != event.get(
                    "canonical_q_vector_sha256")):
            raise H3PanelError("H3-120 artifact identity/status differs from its evidence event")
        _validate_result_identity(
            artifact, expected_row,
            expected_runtime_sha256=starts[0].get("runtime_manifest_sha256", ""),
            expected_implementation_sha256=starts[0].get("implementation_sha256", ""),
            allow_non_target_runtime=terminal.get("synthetic_test_only") is True)
        if (event.get("runtime_manifest_sha256") !=
                artifact.get("runtime_manifest_sha256") or
                event.get("implementation_sha256") != artifact.get("implementation_sha256") or
                event.get("source_artifact_sha256") != expected_row["source_artifact_sha256"] or
                event.get("historical_job_sha256") != expected_row["historical_job_sha256"] or
                event.get("seed_vector_sha256") !=
                expected_row["historical_louvain_seed_vector_sha256"] or
                event.get("historical_reference_q_vector_sha256") !=
                expected_row["historical_q_vector_sha256"]):
            raise H3PanelError("H3-120 evidence event does not bind source and runtime identity")
        hist = _q_stats(artifact.get("historical_q_vector", []))
        canonical = _q_stats(artifact.get("canonical_q_vector", []))
        if (hist["q_vector_sha256"] != event.get("historical_q_vector_sha256") or
                canonical["q_vector_sha256"] != event.get("canonical_q_vector_sha256") or
                artifact.get("historical_qmax") != hist["q_max_200"] or
                artifact.get("historical_first_max_trial_index") !=
                hist["first_max_trial_index"] or
                artifact.get("canonical_qmax") != canonical["q_max_200"] or
                artifact.get("canonical_first_max_trial_index") !=
                canonical["first_max_trial_index"] or
                artifact.get("historical_cache_identity", {}).get("order_policy") !=
                HISTORICAL_ORDER_POLICY or
                artifact.get("canonical_cache_identity", {}).get("order_policy") !=
                CANONICAL_ORDER_POLICY):
            raise H3PanelError("H3-120 full Q vectors or order-bound hashes do not verify")
        verified_artifacts += 1
    row_dir = run_dir / ROW_DIR
    if row_dir.exists():
        if row_dir.is_symlink() or not row_dir.is_dir():
            raise H3PanelError("H3-120 row-artifact directory is symlinked or not a directory")
        actual_names = set()
        for child in row_dir.iterdir():
            if child.is_symlink() or not child.is_file():
                raise H3PanelError("H3-120 row-artifact directory contains an unsafe entry")
            actual_names.add(child.name)
        if actual_names != expected_artifact_names:
            raise H3PanelError("H3-120 row artifacts include missing or unlogged files")
    elif expected_artifact_names:
        raise H3PanelError("H3-120 row-artifact directory is missing")
    completed = (base.get("completed") is True and
                 terminal.get("kind") == "pilot_completed" and
                 terminal.get("synthetic_test_only") is not True and
                 terminal.get("rows_completed") == 120 and len(rows) == 120 and
                 all(event.get("source_graph_identity") == "PASS" and
                     event.get("historical_order_q_replay") == "PASS"
                     and event.get("louvain_trials_computed") == 400 and
                     not event.get("historical_cache_reused") and
                     not event.get("canonical_cache_reused")
                     for event in rows) and
                 sum(event.get("louvain_trials_computed", 0) for event in rows) == 48_000)
    return {**base, "completed_120_row_panel": completed,
            "result_rows_seen": len(rows), "result_artifacts_verified": verified_artifacts,
            "synthetic_test_only": terminal.get("synthetic_test_only") is True,
            "packet_sha256": expected_packet_sha256, "resume_allowed": False}


def launch_real_h3_120(*, packet_path: Path, manifest_path: Path,
                       phase2_root: Path, psa_root: Path, run_dir: Path,
                       state_dir: Path, run_id: str, expected_head: str,
                       authorization_path: Path,
                       researcher_confirmation: str) -> dict[str, Any]:
    packet, manifest = validate_h3_120_packet(packet_path, manifest_path)
    validate_researcher_authorization(
        authorization_path, packet_sha256=EXPECTED_PACKET_SHA256,
        method_path=HERE / METHOD_FILENAME, expected_head=expected_head,
        run_id=run_id, confirmation=researcher_confirmation)
    if state_dir.expanduser().resolve(strict=False) != \
            pilot.default_host_state_dir().expanduser().resolve(strict=False):
        raise H3PanelError("Production H3-120 must use the fixed host-wide activity ledger")
    head = pilot._git_identity(expected_head)
    phase2_root, psa_root = validate_h3_120_private_roots(
        packet, manifest, phase2_root, psa_root)
    limits = _candidate_watchdog_limits()
    resource_preflight = pilot._preflight_macos_resources(limits, psa_root)
    run_dir, expected_parent = _prepare_output_directory(run_dir, psa_root, run_id)
    env_extra = {
        "SRT_H3_120_PACKET_PATH": str(packet_path.resolve(strict=True)),
        "SRT_H3_120_MANIFEST_PATH": str(manifest_path.resolve(strict=True)),
        "SRT_H3_PHASE2_ROOT": str(phase2_root),
        "SRT_H3_PSA_ROOT": str(psa_root),
        "SRT_H3_120_PACKET_SHA256": EXPECTED_PACKET_SHA256,
    }
    command = [sys.executable, str(Path(__file__).resolve()), "--runner-child"]
    return pilot._launch_supervised(
        command, run_dir=run_dir, state_dir=state_dir,
        pilot_sha256=EXPECTED_PACKET_SHA256, run_id=run_id, head=head,
        candidate={**_resource_candidate(),
                  "macos_resource_policy_candidate_not_authorized":
                      pilot.H3_MACOS_RESOURCE_POLICY_CANDIDATE,
                  "preflight_sample": resource_preflight,
                  "packet_sha256": EXPECTED_PACKET_SHA256,
                  "panel_rows": 120, "louvain_trials_gross": 48_000},
        env_extra=env_extra, limits=limits, expected_run_parent=expected_parent)


def _synthetic_supervised_child() -> int:
    """Test-only real Watchdog child: small generated graph, never private data."""
    run_dir = Path.cwd()
    payload_path = Path(os.environ["SRT_H3_120_SYNTHETIC_PAYLOAD"])
    payload = _read_json(payload_path)
    scenario = payload.get("scenario")
    if scenario == "child_exit":
        os._exit(42)  # exercise process-group failure handling without cleanup paths
    if scenario == "full_panel_mock":
        packet, _ = validate_h3_120_packet(HERE / PACKET_FILENAME,
                                           HERE / MANIFEST_FILENAME)

        def virtual_row(row):
            runtime = h3_runtime_manifest()
            runtime_sha = _runtime_hash(runtime)
            implementation_sha = _implementation_hash()
            historical = [0.2] * LOUVAIN_TRIALS
            canonical = [0.25] * LOUVAIN_TRIALS
            hist_order = "synthetic-historical-order-hash"
            canonical_order = "synthetic-canonical-order-hash"
            labels_hash = "synthetic-labeled-edge-set-hash"
            topology_hash = "synthetic-topology-hash"
            base_identity = {
                "graph_id": row["graph_id"],
                "source_artifact_sha256": row["source_artifact_sha256"],
                "selected_neuron_indices_sha256":
                    row["selected_neuron_indices_sha256"],
                "expected_node_order_sha256": row["expected_node_order_sha256"],
                "source_frame_indices_sha256": row["source_frame_indices_sha256"],
                "historical_job_sha256": row["historical_job_sha256"],
                "historical_q_vector_sha256": row["historical_q_vector_sha256"],
                "labeled_edge_set_sha256": labels_hash,
                "topology_sha256": topology_hash,
                "seed_vector_sha256":
                    row["historical_louvain_seed_vector_sha256"],
                "runtime_manifest_sha256": runtime_sha,
                "implementation_sha256": implementation_sha,
            }
            return {
                "source_graph_identity": "PASS",
                "historical_order_q_replay": "PASS",
                "canonical_order_policy": CANONICAL_ORDER_POLICY,
                "recording_id": row["recording_id"],
                "N": row["N"],
                "state": row["state"],
                "subset_repeat": row["subset_repeat"],
                "window_id": row["window_id"],
                "source_artifact_sha256": row["source_artifact_sha256"],
                "selected_neuron_indices_sha256":
                    row["selected_neuron_indices_sha256"],
                "expected_node_order_sha256": row["expected_node_order_sha256"],
                "source_frame_indices_sha256": row["source_frame_indices_sha256"],
                "historical_job_sha256": row["historical_job_sha256"],
                "seed_vector_sha256": row[
                    "historical_louvain_seed_vector_sha256"],
                "historical_reference_q_vector_sha256":
                    row["historical_q_vector_sha256"],
                "historical_adjacency_iteration_sha256": hist_order,
                "canonical_ordered_representation_sha256": canonical_order,
                "runtime_manifest": runtime,
                "runtime_manifest_sha256": runtime_sha,
                "implementation_sha256": implementation_sha,
                "historical_cache_identity": {
                    **base_identity,
                    "order_policy": HISTORICAL_ORDER_POLICY,
                    "ordered_representation_sha256": hist_order},
                "canonical_cache_identity": {
                    **base_identity,
                    "order_policy": CANONICAL_ORDER_POLICY,
                    "ordered_representation_sha256": canonical_order},
                "labeled_edge_set_sha256": labels_hash,
                "historical_q_vector": historical,
                "historical_q_vector_sha256": q_vector_sha256(historical),
                "historical_qmax": 0.2,
                "historical_first_max_trial_index": 0,
                "canonical_q_vector": canonical,
                "canonical_q_vector_sha256": q_vector_sha256(canonical),
                "canonical_qmax": 0.25,
                "canonical_first_max_trial_index": 0,
                "historical_cache_reused": False,
                "canonical_cache_reused": False,
            }

        result = execute_ordered_panel(packet["rows"], run_dir=run_dir,
                                       process_row=virtual_row,
                                       synthetic_test_only=True)
        return 0 if result["status"] == "completed" else 31
    if scenario == "slow":
        time.sleep(2.0)
    import networkx as nx
    from community import community_louvain

    graph = nx.Graph()
    graph.add_nodes_from(range(16))
    graph.add_edges_from((i, (i + 1) % 16) for i in range(16))
    graph.add_edges_from((i, (i + 4) % 16) for i in range(16))
    seeds = tuple(range(1, LOUVAIN_TRIALS + 1))

    def replay(g, seed_values):
        values = []
        for seed in seed_values:
            part = community_louvain.best_partition(
                g, weight="weight", resolution=1.0, random_state=seed)
            values.append(float(community_louvain.modularity(
                part, g, weight="weight")))
        return {"q_values": values}

    historical = nx.Graph()
    historical.add_nodes_from(graph.nodes)
    historical.add_weighted_edges_from((u, v, 1.0) for u, v in graph.edges)
    virtual_reference = replay(historical, seeds)["q_values"]
    result = compute_dual_order_q(
        historical_graph=historical, source_ids=tuple(range(16)), seeds=seeds,
        reference_q=virtual_reference,
        reference_qmax_first_index=first_maximum_index(virtual_reference),
        reference_qmax=max(virtual_reference),
        historical_replay=lambda g, seed_values, **_: replay(g, seed_values),
        canonical_replay=lambda nodes, edges, seed_values:
            canonical_louvain_q_vector(nodes, edges, seed_values))
    evidence_path = run_dir / EVIDENCE_LOG
    with HashChainLog(evidence_path) as evidence:
        evidence.append({"kind": "h3_120_synthetic_runner_started",
                         "scenario": scenario,
                         "graph_nodes": 16,
                         "trials_per_order": LOUVAIN_TRIALS,
                         "source_data_access": "NONE"})
        artifact_dir = run_dir / ROW_DIR
        artifact_dir.mkdir(mode=0o700)
        artifact_path = artifact_dir / "001-synthetic.json"
        artifact_sha = _write_new_json(artifact_path, {
            "schema": "SRT_H3_120_SYNTHETIC_TEST_RESULT_V1",
            "historical_q_vector_sha256": result["historical_q_vector_sha256"],
            "canonical_q_vector_sha256": result["canonical_q_vector_sha256"],
            "historical_order_q_replay": "PASS",
            "source_graph_identity": "PASS_SYNTHETIC_ONLY",
            "q_values_historical": result["historical_q_vector"],
            "q_values_canonical": result["canonical_q_vector"],
        })
        evidence.append({"kind": "graph_result", "pilot_order": 1,
                         "graph_id": "SYNTHETIC_H3_WATCHDOG_GRAPH",
                         "source_graph_identity": "PASS",
                         "historical_order_q_replay": "PASS",
                         "result_artifact": f"{ROW_DIR}/{artifact_path.name}",
                         "result_artifact_sha256": artifact_sha,
                         "historical_q_vector_sha256":
                             result["historical_q_vector_sha256"],
                         "canonical_q_vector_sha256":
                             result["canonical_q_vector_sha256"]})
        terminal = {"kind": "pilot_completed", "status": "completed",
                    "rows_completed": 1, "resume_allowed": False,
                    "source_data_access": "NONE"}
        evidence.append(terminal)
        _write_new_json(run_dir / "runner-terminal.json", terminal)
    return 0


def launch_synthetic_watchdog_test(*, run_dir: Path, state_dir: Path,
                                   scenario: str = "normal",
                                   test_limits: dict[str, Any] | None = None) -> dict[str, Any]:
    """Exercise the exact shared Watchdog/host-ledger boundary without RIKEN data."""
    run_id = str(uuid.uuid4())
    payload = {"run_id": run_id, "scenario": scenario}
    payload_sha = sha256_bytes(_canonical(payload))
    run_dir, state_dir = run_dir.absolute(), state_dir.absolute()
    state_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
    run_dir.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    payload_path = run_dir.parent / f"{run_dir.name}.synthetic-payload.json"
    _write_new_json(payload_path, payload)
    candidate = {"wall_seconds": 30.0, "process_tree_cpu_seconds": 30.0,
                 "max_compute_workers": 1, "sampled_aggregate_rss_bytes": 512 * 1024**2,
                 "output_bytes": 16 * 1024**2}
    limits_values = {"wall_seconds": 30.0, "cpu_seconds": 30.0,
                     "aggregate_rss_bytes": 512 * 1024**2, "max_workers": 1,
                     "run_disk_bytes": 16 * 1024**2, "reserve_free_disk_bytes": 1,
                     "case_seconds": 30.0, "oracle_seconds": 30.0,
                     "poll_seconds": 0.05, "memory_enforcement_backend": "SAMPLED_ONLY"}
    if test_limits:
        limits_values.update(test_limits)
    from nc0a_watchdog import WatchdogLimits
    limits = WatchdogLimits(**limits_values)
    try:
        return pilot._launch_supervised(
            [sys.executable, str(Path(__file__).resolve()), "--synthetic-child"],
            run_dir=run_dir, state_dir=state_dir, pilot_sha256=payload_sha,
            run_id=run_id, head={"head_sha": "synthetic-test-head",
                                 "working_tree": "TEST_ONLY"},
            candidate=candidate,
            env_extra={"SRT_H3_120_SYNTHETIC_PAYLOAD": str(payload_path)},
            limits=limits)
    finally:
        payload_path.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", type=Path, default=HERE / PACKET_FILENAME)
    parser.add_argument("--manifest", type=Path, default=HERE / MANIFEST_FILENAME)
    parser.add_argument("--run-directory", type=Path)
    parser.add_argument("--run-id")
    parser.add_argument("--expected-head")
    parser.add_argument("--authorization", type=Path)
    parser.add_argument("--researcher-confirmation")
    parser.add_argument("--runner-child", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--synthetic-child", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args(argv)
    if args.runner_child:
        return _runner_child()
    if args.synthetic_child:
        return _synthetic_supervised_child()
    if args.verify:
        print(json.dumps(verify_h3_120_run(
            args.verify, host_state_dir=pilot.default_host_state_dir()), sort_keys=True))
        return 0
    try:
        _packet, _manifest = validate_h3_120_packet(args.packet, args.manifest)
        # This check intentionally stops today: the amendment remains draft.
        effective, detail = _method_is_effective(HERE / METHOD_FILENAME)
        if not effective:
            raise H3PanelError(detail)
        if any(value is None for value in (args.run_directory, args.run_id,
                                           args.expected_head, args.authorization,
                                           args.researcher_confirmation)):
            raise H3PanelError("A complete researcher authorization and run identity are required")
        phase2_root, psa_root = pilot._default_paths()
        state_dir = pilot.default_host_state_dir()
        result = launch_real_h3_120(
            packet_path=args.packet, manifest_path=args.manifest,
            phase2_root=phase2_root, psa_root=psa_root,
            run_dir=args.run_directory, state_dir=state_dir,
            run_id=args.run_id, expected_head=args.expected_head,
            authorization_path=args.authorization,
            researcher_confirmation=args.researcher_confirmation)
        print(json.dumps({key: result.get(key) for key in
                          ("run_id", "pilot_sha256", "head_sha", "status",
                           "failure_category", "resume_allowed")}, sort_keys=True))
        return 0 if result.get("status") == "COMPLETED" else 2
    except (H3PanelError, pilot.H3PilotError, IdentityEvidenceError, WatchdogError) as exc:
        parser.error(str(exc))
    return 2


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
