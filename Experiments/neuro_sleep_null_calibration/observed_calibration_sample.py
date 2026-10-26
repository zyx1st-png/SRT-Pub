"""Outcome-blind, deterministic observed-only cost panel; no signal/Q loading."""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

from riken_source_identity import EXPECTED_RECORDINGS, STATES, TARGETS, sha256_file

HERE = Path(__file__).resolve().parent
SOURCE_FILENAME = "G0_RIKEN_SOURCE_GRAPH_EXPECTED_MANIFEST_2026-10-21.json"
SAMPLE_FILENAME = "OBSERVED_CALIBRATION_FIXED_SAMPLE_V1_2026-10-26.json"
SOURCE_SHA256 = "6a8357ac0b815c434421a31dc6c294c292b5c144713f49c52b5344038235ece2"
METHOD_FILENAME = "G0_CANONICAL_Q_ORDER_PROSPECTIVE_AMENDMENT_DRAFT_2026-10-23.md"
METHOD_SHA256 = "c0cf7f85a18bad844e190deefbe83e8ab55f0dbe194299be0ef94e2c828e38c3"
SCHEMA = "SRT_CANONICAL_OBSERVED_COST_SAMPLE_V1"
SELECTOR = "SOURCE_WINDOW_N_ID_ONLY_SHA256_V1"
RESOURCE_CANDIDATE = {
    "wall_seconds": 4 * 3600,
    "process_tree_cpu_seconds": 4 * 3600,
    "max_compute_workers": 1,
    "sampled_aggregate_rss_bytes": 4 * 1024**3,
    "output_bytes": 1024**3,
    "memory_semantics": "SAMPLED_RSS_NOT_A_HARD_LIMIT",
    "raw_window_cache_bytes": 256 * 1024**2,
    "raw_window_cache_entries": 1,
}


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode()


def window_key(row: dict) -> tuple:
    return (row["source_file_sha256"], row["recording_id"], row["state"],
            row["window_id"], row["source_frame_indices_sha256"])


def _rank(row: dict, purpose: str) -> tuple:
    # No Q values, timing, graph features or archived optimizer outcomes enter ranking.
    digest = hashlib.sha256(canonical([SELECTOR, purpose, row["graph_id"]])).hexdigest()
    return digest, row["graph_id"]


def _public_row(row: dict) -> dict:
    # Identity references only. In particular do not copy historical Q/max/index values.
    fields = ("graph_id", "recording_id", "N", "state", "subset_repeat", "window_id",
              "source_filename", "source_file_sha256", "source_frame_indices_sha256",
              "selected_neuron_indices_sha256", "historical_job_sha256",
              "louvain_seed_vector_sha256", "historical_q_vector_sha256",
              "expected_input_identity_sha256", "expected_edge_count")
    return {key: row[key] for key in fields}


def build_sample(manifest: dict) -> dict:
    rows = manifest["source_graphs"]
    if len(rows) != 4900 or Counter(row["N"] for row in rows) != Counter({n: 490 for n in TARGETS}):
        raise ValueError("Expected the frozen 4,900 graph population")
    h3 = manifest["h3_panel"]["records"]
    h3_ids = {row["graph_id"] for row in h3}
    h3_windows = {(row["source_artifact_sha256"], row["recording_id"], row["state"],
                   row["window_id"], row["source_frame_indices_sha256"]) for row in h3}
    windows = {window_key(row) for row in rows}
    unseen = sorted(windows - h3_windows,
                    key=lambda k: (EXPECTED_RECORDINGS.index(k[1]), STATES.index(k[2]), k[3], k[4]))
    if len(windows) != 49 or len(h3_windows) != 40 or len(unseen) != 9:
        raise ValueError("Frozen H3 window coverage changed")
    selected: dict[str, tuple[dict, str]] = {}
    for key in unseen:
        for n in (100, 765, 3900):
            row = min((r for r in rows if window_key(r) == key and r["N"] == n),
                      key=lambda r: _rank(r, "UNSEEN_WINDOW_3N"))
            selected[row["graph_id"]] = (row, "H3_UNSEEN_WINDOW_3N")
    # Exactly one Wake and one NREM supplement at each N. Rotating sources cover all six.
    for i, n in enumerate(TARGETS):
        for state_index, state in enumerate(STATES):
            recording = EXPECTED_RECORDINGS[(i + 3 * state_index) % 6]
            row = min((r for r in rows if r["N"] == n and r["state"] == state
                       and r["recording_id"] == recording
                       and r["graph_id"] not in selected and r["graph_id"] not in h3_ids),
                      key=lambda r: _rank(r, "COVERAGE_SUPPLEMENT"))
            selected[row["graph_id"]] = (row, "COVERAGE_SUPPLEMENT")
    if len(selected) != 47 or set(selected) & h3_ids:
        raise ValueError("Primary sample must be 47 unique non-H3 graphs")
    ordered = sorted(selected.values(), key=lambda item: (
        EXPECTED_RECORDINGS.index(item[0]["recording_id"]),
        STATES.index(item[0]["state"]), item[0]["window_id"],
        item[0]["source_frame_indices_sha256"], item[0]["N"], item[0]["graph_id"]))
    primary = [{"sample_order": i, "selection_role": role, **_public_row(row)}
               for i, (row, role) in enumerate(ordered, 1)]
    excluded = h3_ids | set(selected)
    reserve = []
    for n in TARGETS:
        candidates = sorted((r for r in rows if r["N"] == n and r["graph_id"] not in excluded),
                            key=lambda r: _rank(r, "SEALED_RESERVE"))
        for j, row in enumerate(candidates[:4]):
            reserve.append({"reserve_order": len(reserve) + 1,
                            "split": "TRAINING" if j < 2 else "SEALED_VALIDATION",
                            **_public_row(row)})
    return {
        "schema": SCHEMA, "status": "FROZEN_SAMPLE_NOT_EXECUTION_AUTHORIZED",
        "selector_version": SELECTOR, "source_manifest_sha256": SOURCE_SHA256,
        "method_sha256": METHOD_SHA256,
        "h3_execution_head": "147d5ca268ef0c579c41f314a6f5e5ec8cafc6d2",
        "h3_run_uuid": "e6abc8fd-831f-4076-b412-e5a7481a027b",
        "h3_rows_excluded_from_new_Q": 120, "reuse_h3_Q": False,
        "primary_rows": primary, "row_count": 47, "louvain_trials": 9400,
        "unseen_window_count": 9, "unseen_window_N": [100, 765, 3900],
        "execution_order": "recording/state/window/frame_hash/N/graph_id; cache capacity one window",
        "coverage": {
            "N": {str(n): sum(r["N"] == n for r in primary) for n in TARGETS},
            "recording": dict(sorted(Counter(r["recording_id"] for r in primary).items())),
            "state": dict(Counter(r["state"] for r in primary)),
            "unique_windows": len({window_key(r) for r in primary}),
        },
        "resource_limits_candidate_not_approved": RESOURCE_CANDIDATE,
        "inference_limit": "INITIAL_COST_MEASUREMENT_NOT_FULL_POPULATION_U95_CALIBRATION",
        "reserve_rows_not_authorized": reserve,
        "expansion_rule": {
            "automatic_expansion": False,
            "one_optional_batch_rows": 40,
            "training_rows": 20, "sealed_validation_rows": 20,
            "triggers": ["missing phase/IO measurements", "source-window or N support absent",
                         "training-only cross-validation underpredicts any held row by >25%",
                         "training-only predictive U95/median >1.5"],
            "activation": "new independent resource review and researcher UUID-bound approval; all 40 or none",
            "sealing": "validation costs not viewed until training predictor/code/hash frozen; no refit after opening",
            "failure": "integrity failure stops; no replacement, outcome-directed resampling, or automatic retry",
            "not_a_GO_rule": "Neither batch alone authorizes 4,900 baseline or G0/T1; full forecast separately reviewed",
        },
    }


def validate_sample(path: Path = HERE / SAMPLE_FILENAME) -> tuple[dict, dict]:
    source_path = HERE / SOURCE_FILENAME
    if source_path.is_symlink() or sha256_file(source_path) != SOURCE_SHA256:
        raise ValueError("Source inventory hash mismatch")
    manifest = json.loads(source_path.read_text())
    if path.is_symlink() or not path.is_file():
        raise ValueError("Sample manifest missing or symlinked")
    sample = json.loads(path.read_text())
    if sample != build_sample(manifest):
        raise ValueError("Frozen sample identities, order, scope or candidate limits changed")
    return sample, manifest


if __name__ == "__main__":
    # Deterministic generated artifact. No private file or biological Q is accessed.
    manifest = json.loads((HERE / SOURCE_FILENAME).read_text())
    target = HERE / SAMPLE_FILENAME
    target.write_bytes(canonical(build_sample(manifest)) + b"\n")
    print(sha256_file(target))
