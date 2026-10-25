"""Prepare a public-safe RIKEN G0 source identity inventory and H3 panel.

The CLI verifies existing artifacts and builds expected identities only. It
does not read signal samples, rebuild biological graphs, run Louvain, or make
null graphs. Library replay functions are available for a separately budgeted
and authorized H3 reconstruction.
"""

from __future__ import annotations

import argparse
import ast
import csv
import gzip
import hashlib
import json
import math
import numbers
import os
import platform
import struct
import sys
from collections.abc import Iterable

from g0_q_protocol import canonical_louvain_q_vector
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
RESULT_JSON = ROOT / "Experiments/SRT_NEURO_POPULATION_SIZE_SCALING_RESULT_2026-10-09.json"
SUMMARY_CSV = ROOT / "Experiments/SRT_NEURO_POPULATION_SIZE_SCALING_SUBSAMPLE_SUMMARY_2026-10-09.csv"
PREREG = ROOT / "Experiments/SRT_NEURO_SLEEP_POPULATION_NULL_CALIBRATION_PREREGISTRATION_2026-10-09.md"
TARGETS = (100, 150, 225, 340, 510, 765, 1150, 1725, 2600, 3900)
STATES = ("wake", "NREM")  # exact serialized tokens in the PS-A job records
WINDOW_SIZE = 1500
MEAN_DEGREE = 16
LOUVAIN_TRIALS = 200
H3_TRIAL_Q_ATOL_PROPOSED = 1e-10
H3_QMAX_ATOL = 1e-6
H3_PILOT_WALL_SECONDS = 8 * 60 * 60
H3_PILOT_CPU_SECONDS = 32 * 60 * 60
H3_PILOT_MAX_WORKERS = 4
H3_PILOT_RSS_BYTES = 4 * 1024**3
H3_PILOT_OUTPUT_BYTES = 1 * 1024**3
PSA_SEED_ROOT = 12345
PANEL_SEED_ROOT = 20261009
SUBSET_NAMESPACE = "NC_SUBSET_SELECTION_V1"
PANEL_NAMESPACE = "NC_IDENTITY_PANEL_V1"
EXPECTED_SOURCE_CODE_HASHES = {
    "population_size_scaling.py": "0e7af206456348b9eb91d5771d7cd4d18fe312ea4508b71a5772d7a47370b625",
    "multirecording_primary.py": "2421e4e21655199378aad81242aa1d0a5a02ba94a39c5cb83e0942689faa55f5",
}
EXPECTED_HISTORICAL_GRAPH_FUNCTION_SHA256 = (
    "59ed4ea1537d3b104e8ff9903ce98c51f69bb58edc09854933886f637ad90866")
EXPECTED_PREREG_SHA256 = "bf497d89e5695498451e49071007aec290d8a899b30b0fd31026f8f3faa55aaa"
EXPECTED_RESULT_SHA256 = "955e78301b9a85a05dda1cb00e20ab2445f21a64799a7b077a74f43eba29b9f3"
EXPECTED_SUMMARY_SHA256 = "eba10f8758894a91bd5c39fd8826bfc86d45cc0e05ea23cd05d20095a1c77dbe"
EXPECTED_RECORDINGS = (
    "mouse01_sleep", "mouse02_sleep", "mouse03_sleep",
    "mouse04_day1_sleep", "mouse04_day2_sleep", "mouse05_sleep",
)


class IdentityEvidenceError(ValueError):
    """An input differs from the preserved source identity evidence."""


def canonical_json(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def hash_int64(values: Iterable[int]) -> str:
    packed = b"".join(struct.pack("<q", int(value)) for value in values)
    return sha256_bytes(packed)


def hash_float64(values: Iterable[float]) -> str:
    packed = b"".join(struct.pack("<d", float(value)) for value in values)
    return sha256_bytes(packed)


def stable_seed(root: int, *parts: object) -> int:
    payload = "|".join([str(root), *(str(part) for part in parts)]).encode("utf-8")
    value = int.from_bytes(hashlib.blake2b(payload, digest_size=8).digest(), "little")
    return int(value % (2**31 - 1)) or 1


def select_g0_repeats(recording_id: str, n: int,
                      repeat_ids: Iterable[int]) -> tuple[int, ...]:
    ranked = sorted(
        ((stable_seed(PANEL_SEED_ROOT, SUBSET_NAMESPACE, recording_id,
                      f"N{n}", int(repeat)), int(repeat)) for repeat in repeat_ids),
        key=lambda item: (item[0], item[1]),
    )
    if len(ranked) != 100 or len({item[1] for item in ranked}) != 100:
        raise IdentityEvidenceError(f"Expected 100 unique repeat IDs for {recording_id}/N{n}")
    return tuple(item[1] for item in ranked[:10])


def select_h3_panel(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Select one ID per recording × N × state without reading any Q value."""
    panel = []
    for recording_id in dict.fromkeys(row["recording_id"] for row in records):
        for n in TARGETS:
            rows = [row for row in records
                    if row["recording_id"] == recording_id and row["N"] == n]
            repeats = {int(row["subset_repeat"]) for row in rows}
            if len(repeats) != 10:
                raise IdentityEvidenceError(f"Expected 10 preselected repeats for {recording_id}/N{n}")
            for state in STATES:
                candidates = [row for row in rows
                              if row["subset_repeat"] in repeats and row["state"] == state]
                if not candidates:
                    raise IdentityEvidenceError(f"Missing H3 candidates: {recording_id}/N{n}/{state}")
                choice = min(candidates, key=lambda row: (
                    stable_seed(PANEL_SEED_ROOT, PANEL_NAMESPACE, recording_id,
                                f"N{n}", state, row["subset_repeat"], row["window_id"]),
                    row["subset_repeat"], row["window_id"],
                ))
                panel.append({
                    "graph_id": choice["graph_id"], "recording_id": recording_id,
                    "N": n, "subset_repeat": choice["subset_repeat"],
                    "state": state, "window_id": choice["window_id"],
                    "identity_panel_seed": stable_seed(
                        PANEL_SEED_ROOT, PANEL_NAMESPACE, recording_id, f"N{n}",
                        state, choice["subset_repeat"], choice["window_id"]),
                    "source_artifact_sha256": choice["source_file_sha256"],
                    "selected_neuron_indices_sha256": choice["selected_neuron_indices_sha256"],
                    "source_frame_indices_sha256": choice["source_frame_indices_sha256"],
                    "expected_input_identity_sha256":
                        choice["expected_input_identity_sha256"],
                    "expected_node_order_sha256": choice["selected_neuron_indices_sha256"],
                    "expected_edge_count": choice["expected_edge_count"],
                    "historical_job_sha256": choice["historical_job_sha256"],
                    "historical_q_vector_sha256": choice["historical_q_vector_sha256"],
                    "historical_louvain_seed_vector_sha256": choice["louvain_seed_vector_sha256"],
                    "historical_q_max_first_index": choice["historical_q_max_first_index"],
                    "historical_q_reference": "PRESENT_IN_PRIVATE_PS_A_JOB_JSON; values not copied",
                    "historical_partition": "NOT_ARCHIVED; no historical partition comparator",
                    "edge_identity": "NOT_RECONSTRUCTED", "q_replay": "NOT_RUN",
                })
    if len(panel) != 120:
        raise IdentityEvidenceError(f"H3 panel has {len(panel)} records, expected 120")
    return panel


def select_h3_first_by_n(panel: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Select the first frozen H3 panel identity per N, without consulting Q."""
    ids = [row.get("graph_id") for row in panel]
    if len(ids) != len(set(ids)) or len(panel) != 120:
        raise IdentityEvidenceError("Expected the unique, complete frozen 120-row H3 panel")
    selected = []
    for n in TARGETS:
        candidates = [row for row in panel if int(row["N"]) == n]
        if len(candidates) != len(EXPECTED_RECORDINGS) * len(STATES):
            raise IdentityEvidenceError(f"Incomplete H3 panel stratum N{n}")
        first = min(candidates, key=lambda row: (
            EXPECTED_RECORDINGS.index(str(row["recording_id"])),
            STATES.index(str(row["state"])), int(row["subset_repeat"]),
            int(row["window_id"]),
        ))
        selected.append({**first, "pilot_order": len(selected) + 1,
                         "pilot_selection": "FIRST_FROZEN_PANEL_ID_PER_ASCENDING_N"})
    if len({row["graph_id"] for row in selected}) != len(TARGETS):
        raise IdentityEvidenceError("H3 calibration pilot identities are not unique")
    return selected


def _h5_frames(path: Path, expected_shape: str,
               expected_frame_counts: dict[str, int]
               ) -> dict[str, dict[int, dict[str, Any]]]:
    import h5py
    import numpy as np

    def dataset(handle, suffix: str):
        names: list[str] = []
        handle.visit(names.append)
        suffix = suffix.strip("/").lower()
        exact = [name for name in names if name.strip("/").lower() == suffix]
        matches = exact or [name for name in names
                            if name.strip("/").lower().endswith("/" + suffix)]
        if not matches or not isinstance(handle[matches[0]], h5py.Dataset):
            raise IdentityEvidenceError(f"HDF5 dataset missing: {suffix}")
        return handle[matches[0]]

    output: dict[str, dict[int, dict[str, Any]]] = {state: {} for state in STATES}
    with h5py.File(path, "r") as handle:
        signal = dataset(handle, "spike_smoothed")
        if f"{signal.shape[0]}x{signal.shape[1]}" != expected_shape:
            raise IdentityEvidenceError("spike_smoothed shape differs from public inventory")
        refs = np.asarray(dataset(handle, "frame/used_frame")[()]).reshape(-1)
        if len(refs) != 2:
            raise IdentityEvidenceError("Expected exactly two used-frame state arrays")
        for state_index, ref in enumerate(refs):
            values = np.asarray(handle[ref][()]).reshape(-1).astype(np.int64) - 1
            state = STATES[state_index]
            if values.size != expected_frame_counts[state]:
                raise IdentityEvidenceError(f"Source frame count mismatch: {state}")
            if (values.size == 0 or np.any(values < 0) or
                    np.any(values >= int(signal.shape[0]))):
                raise IdentityEvidenceError("Invalid source used-frame indices")
            for window_id in range(values.size // WINDOW_SIZE):
                block = values[window_id * WINDOW_SIZE:(window_id + 1) * WINDOW_SIZE]
                output[state][window_id] = {
                    "source_frame_start_one_based": int(block[0]) + 1,
                    "source_frame_end_one_based": int(block[-1]) + 1,
                    "source_frame_indices_sha256": sha256_bytes(
                        np.asarray(block, dtype="<i8").tobytes()),
                }
    return output


def read_source_abs_correlation(path: Path, selected_neuron_indices: Iterable[int],
                                state: str, window_id: int):
    """Reproduce the PS-A HDF5 row order and abs(corr) input for one window."""
    import h5py
    import numpy as np

    if state not in STATES or type(window_id) is not int or window_id < 0:
        raise IdentityEvidenceError("Invalid source state/window")
    selected = np.asarray(tuple(selected_neuron_indices), dtype=np.int64)
    if selected.size < 2 or np.any(selected < 0) or np.unique(selected).size != selected.size:
        raise IdentityEvidenceError("Invalid selected neuron indices")
    with h5py.File(path, "r") as handle:
        names: list[str] = []
        handle.visit(names.append)

        def dataset(suffix: str):
            suffix = suffix.strip("/").lower()
            exact = [name for name in names if name.strip("/").lower() == suffix]
            matches = exact or [name for name in names
                                if name.strip("/").lower().endswith("/" + suffix)]
            if not matches or not isinstance(handle[matches[0]], h5py.Dataset):
                raise IdentityEvidenceError(f"HDF5 dataset missing: {suffix}")
            return handle[matches[0]]

        signal = dataset("spike_smoothed")
        refs = np.asarray(dataset("frame/used_frame")[()]).reshape(-1)
        state_index = STATES.index(state)
        if len(refs) != 2:
            raise IdentityEvidenceError("Expected two used-frame state arrays")
        all_frames = np.asarray(handle[refs[state_index]][()]).reshape(-1).astype(np.int64) - 1
        begin, end = window_id * WINDOW_SIZE, (window_id + 1) * WINDOW_SIZE
        if end > len(all_frames) or np.any(all_frames < 0) or np.any(all_frames >= signal.shape[0]):
            raise IdentityEvidenceError("Requested source window is invalid or unavailable")
        frame_indices = all_frames[begin:end]
        if np.all(np.diff(frame_indices) >= 0):
            window_data = np.asarray(signal[frame_indices.tolist(), :], dtype=np.float64).T
        else:
            order = np.argsort(frame_indices, kind="stable")
            sorted_data = np.asarray(signal[frame_indices[order].tolist(), :], dtype=np.float64).T
            window_data = np.empty_like(sorted_data)
            window_data[:, order] = sorted_data
        if np.any(selected >= window_data.shape[0]):
            raise IdentityEvidenceError("Selected neuron index exceeds source signal width")
        correlation = np.corrcoef(window_data[selected, :], rowvar=True)
        correlation = np.nan_to_num(correlation, nan=0.0, posinf=0.0, neginf=0.0)
        np.fill_diagonal(correlation, 0.0)
        return (np.abs(correlation), tuple(map(int, selected)),
                sha256_bytes(np.asarray(frame_indices, dtype="<i8").tobytes()))


def reconstruct_source_graph(source_path: Path,
                             selected_neuron_indices: Iterable[int],
                             state: str, window_id: int,
                             historical_builder_path: Path) -> dict[str, Any]:
    """Rebuild and compare one observed graph without running Louvain/nulls."""
    correlation, neuron_ids, frame_sha = read_source_abs_correlation(
        source_path, selected_neuron_indices, state, window_id)
    pair = reconstruct_graph_pair(correlation, historical_builder_path, neuron_ids)
    return {**pair, "source_frame_indices_sha256": frame_sha,
            "source_neuron_order_sha256": hash_int64(neuron_ids)}


def _seed_ledger(path: Path) -> dict[tuple[str, str, int, str, int], dict[str, Any]]:
    result = {}
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        for number, line in enumerate(stream, 1):
            row = json.loads(line)
            key = (row["recording_id"], row["target_label"], int(row["subset_repeat"]),
                   row["state"], int(row["window_index"]))
            if key in result:
                raise IdentityEvidenceError(f"Duplicate seed-ledger key at line {number}")
            result[key] = row
    return result


def _expected_louvain_seeds(recording: str, target: str,
                            state: str, window: int) -> list[int]:
    encoded = STATES.index(state) * 1000 + window
    return [stable_seed(PSA_SEED_ROOT, recording, "sleep", "S3", "C1",
                        target, encoded, trial) for trial in range(LOUVAIN_TRIALS)]


def build_inventory(*, repo_root: Path, phase2_root: Path,
                    psa_root: Path) -> dict[str, Any]:
    result_path = repo_root / RESULT_JSON.relative_to(ROOT)
    summary_path = repo_root / SUMMARY_CSV.relative_to(ROOT)
    prereg_path = repo_root / PREREG.relative_to(ROOT)
    result = json.loads(result_path.read_text(encoding="utf-8"))
    inventory = {row["recording_id"]: row for row in result["data_inventory"]}
    if tuple(inventory) != EXPECTED_RECORDINGS:
        raise IdentityEvidenceError("Published source recording identity/order changed")
    prereg_sha = sha256_file(prereg_path)
    result_sha = sha256_file(result_path)
    summary_sha = sha256_file(summary_path)
    if (prereg_sha != EXPECTED_PREREG_SHA256 or
            result_sha != EXPECTED_RESULT_SHA256 or
            summary_sha != EXPECTED_SUMMARY_SHA256):
        raise IdentityEvidenceError("Frozen preregistration or public PS-A evidence hash changed")
    source_hashes = result["source_data_sha256_by_filename"]
    code_hashes = result["runtime_code_sha256"]
    if code_hashes != EXPECTED_SOURCE_CODE_HASHES:
        raise IdentityEvidenceError("Published PS-A runtime hashes differ from the frozen values")
    local_code_hashes = {
        "population_size_scaling.py": sha256_file(psa_root / "population_size_scaling.py"),
        "multirecording_primary.py": sha256_file(phase2_root / "multirecording_primary.py"),
    }
    if local_code_hashes != code_hashes:
        raise IdentityEvidenceError("Local PS-A source code does not match its public result hashes")

    frames = {}
    source_records = []
    for recording, item in inventory.items():
        path = phase2_root / "data" / item["filename"]
        if not path.is_file() or path.is_symlink():
            raise IdentityEvidenceError(f"Source file missing or symlinked: {item['filename']}")
        digest = sha256_file(path)
        if digest != source_hashes.get(item["filename"]) or digest != item["sha256"]:
            raise IdentityEvidenceError(f"Source SHA-256 mismatch: {item['filename']}")
        if path.stat().st_size != int(item["bytes"]):
            raise IdentityEvidenceError(f"Source size mismatch: {item['filename']}")
        frames[recording] = _h5_frames(
            path, item["signal_shape"],
            {"wake": int(item["wake_frames"]), "NREM": int(item["nrem_frames"])})
        for state in STATES:
            count = int(item["wake_frames"] if state == "wake" else item["nrem_frames"])
            if len(frames[recording][state]) != count // WINDOW_SIZE:
                raise IdentityEvidenceError(f"Window count mismatch: {recording}/{state}")
        source_records.append({"recording_id": recording, "filename": item["filename"],
                               "animal_id": item["animal_id"],
                               "session_label": next(
                                   (part for part in recording.split("_")
                                    if part in {"day1", "day2"}), None),
                               "session_label_source": (
                                   "recording_id_token" if any(
                                       part in {"day1", "day2"}
                                       for part in recording.split("_")) else
                                   "not_separately_encoded_in_inventory"),
                               "bytes": int(item["bytes"]), "sha256": digest,
                               "signal_shape": item["signal_shape"],
                               "accepted_neurons": int(item["accepted_neurons"]),
                               "wake_frames": int(item["wake_frames"]),
                               "nrem_frames": int(item["nrem_frames"])})

    summaries = {}
    with summary_path.open(newline="", encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            key = (row["recording_id"], row["target_label"], int(row["subset_repeat"]))
            if key in summaries:
                raise IdentityEvidenceError(f"Duplicate public summary row: {key}")
            summaries[key] = row
    jobs = {}
    for path in sorted((psa_root / "jobs").glob("*.json")):
        if path.is_symlink():
            raise IdentityEvidenceError(f"PS-A job is a symlink: {path.name}")
        job = json.loads(path.read_text(encoding="utf-8"))
        key = (job["recording_id"], job["target_label"], int(job["subset_repeat"]))
        if key in jobs:
            raise IdentityEvidenceError(f"Duplicate PS-A job: {key}")
        jobs[key] = (job, sha256_file(path))
    expected_keys = {(recording, f"N{n}", repeat)
                     for recording in inventory for n in TARGETS for repeat in range(100)}
    expected_keys.update((recording, "FULL", 0) for recording in inventory)
    if set(jobs) != expected_keys or set(summaries) != expected_keys:
        raise IdentityEvidenceError(
            f"PS-A job and public summary coverage mismatch: {len(jobs)}/{len(summaries)}")

    for (recording, target, repeat), (job, _) in jobs.items():
        item = inventory[recording]
        n = None if target == "FULL" else int(target[1:])
        indices = job.get("selected_neuron_indices_zero_based")
        expected_index_count = n or int(item["accepted_neurons"])
        if (not isinstance(indices, list) or len(indices) != expected_index_count or
                indices != sorted(set(indices)) or any(type(i) is not int or i < 0 or
                i >= int(item["accepted_neurons"]) for i in indices)):
            raise IdentityEvidenceError(f"Subset node list invalid: {recording}/{target}/{repeat}")
        index_hash = hash_int64(indices)
        if index_hash != job.get("selected_neuron_indices_sha256"):
            raise IdentityEvidenceError(f"Subset index SHA mismatch: {recording}/{target}/{repeat}")
        actual_seed = (None if n is None else stable_seed(
            PSA_SEED_ROOT, "population_size_scaling_subset", recording, target, repeat))
        if job.get("subset_seed") != actual_seed:
            raise IdentityEvidenceError(f"Realized subset seed mismatch: {recording}/{target}/{repeat}")
        summary = summaries[(recording, target, repeat)]
        if (summary["selected_neuron_indices_sha256"] != index_hash or
                summary["subset_seed"] != ("" if actual_seed is None else str(actual_seed)) or
                int(summary["accepted_neurons"]) != int(item["accepted_neurons"]) or
                job.get("status") != "complete" or job.get("active_window") is not None or
                job.get("target_n") != n or job.get("repeats_per_graph") != LOUVAIN_TRIALS):
            raise IdentityEvidenceError(f"PS-A job/public summary mismatch: {recording}/{target}/{repeat}")
        if (job.get("protocol") != "RIKEN_SLEEP_POPULATION_SIZE_SCALING_2026-09-24" or
                job.get("animal_id") != item["animal_id"] or
                job.get("filename") != item["filename"] or
                job.get("condition") != "sleep" or job.get("signal") != "S3" or
                job.get("inclusion") != "C1"):
            raise IdentityEvidenceError(f"PS-A protocol identity mismatch: {recording}/{target}/{repeat}")
        expected_window_keys = {
            f"state{si}_window{wi}" for si, state in enumerate(STATES)
            for wi in frames[recording][state]
        }
        if set(job.get("windows", {})) != expected_window_keys:
            raise IdentityEvidenceError(f"State/window set mismatch: {recording}/{target}/{repeat}")
        if (int(summary["wake_window_count"]) != len(frames[recording]["wake"]) or
                int(summary["nrem_window_count"]) != len(frames[recording]["NREM"]) or
                int(summary["repeats_per_graph"]) != LOUVAIN_TRIALS):
            raise IdentityEvidenceError(f"Public PS-A window summary mismatch: {recording}/{target}/{repeat}")

    ledger_path = psa_root / "louvain_seed_ledger.jsonl.gz"
    ledger = _seed_ledger(ledger_path)
    expected_ledger_keys = {
        (recording, target, repeat, state, window_id)
        for (recording, target, repeat), (_job, _) in jobs.items()
        for state in STATES
        for window_id in frames[recording][state]
    }
    if set(ledger) != expected_ledger_keys:
        raise IdentityEvidenceError(
            f"Complete seed-ledger key coverage mismatch: {len(ledger)}/"
            f"{len(expected_ledger_keys)}")
    for recording, target, repeat, state, window_id in sorted(
            expected_ledger_keys, key=lambda key: (
                EXPECTED_RECORDINGS.index(key[0]),
                (TARGETS.index(int(key[1][1:])) if key[1].startswith("N")
                 else len(TARGETS)),
                key[2], STATES.index(key[3]), key[4])):
        job = jobs[(recording, target, repeat)][0]
        saved = job["windows"][f"state{STATES.index(state)}_window{window_id}"]
        q_values = saved.get("q_values")
        seed_row = ledger[(recording, target, repeat, state, window_id)]
        qmax = (max(map(float, q_values))
                if isinstance(q_values, list) and q_values else math.nan)
        first_max = (next((i for i, value in enumerate(q_values)
                           if float(value) == qmax), -1)
                     if isinstance(q_values, list) else -1)
        seeds = _expected_louvain_seeds(recording, target, state, window_id)
        if (not isinstance(q_values, list) or len(q_values) != LOUVAIN_TRIALS or
                any(not math.isfinite(float(value)) for value in q_values) or
                float(saved.get("q_max", math.nan)) != qmax or
                int(saved.get("q_max_first_index", -1)) != first_max or
                saved.get("state") != state or
                int(saved.get("window_index", -1)) != window_id or
                seed_row.get("louvain_seeds") != seeds or
                float(seed_row.get("q_max", math.nan)) != qmax or
                seed_row.get("selected_neuron_indices_sha256") !=
                job["selected_neuron_indices_sha256"]):
            raise IdentityEvidenceError(
                f"Seed ledger does not match its complete historical job: "
                f"{recording}/{target}/{repeat}/{state}/{window_id}")
    selected_records = []
    selected_ledger_keys = set()
    repeat_map = {(recording, f"N{n}"): set(select_g0_repeats(
        recording, n, range(100))) for recording in inventory for n in TARGETS}
    for recording, item in inventory.items():
        for n in TARGETS:
            target = f"N{n}"
            for repeat in sorted(repeat_map[(recording, target)]):
                job, job_sha = jobs[(recording, target, repeat)]
                for state in STATES:
                    state_index = STATES.index(state)
                    for window_id, frame in sorted(frames[recording][state].items()):
                        key = (recording, target, repeat, state, window_id)
                        job_key = f"state{state_index}_window{window_id}"
                        saved = job["windows"][job_key]
                        q_values = saved.get("q_values")
                        if (not isinstance(q_values, list) or len(q_values) != LOUVAIN_TRIALS or
                                any(not math.isfinite(float(q)) for q in q_values)):
                            raise IdentityEvidenceError(f"Invalid historical Q vector: {key}")
                        qmax = max(map(float, q_values))
                        first_max = next(i for i, value in enumerate(q_values)
                                         if float(value) == qmax)
                        if (float(saved.get("q_max")) != qmax or
                                int(saved.get("q_max_first_index", -1)) != first_max or
                                int(saved.get("source_frame_start_one_based", -1)) !=
                                int(frame["source_frame_start_one_based"]) or
                                int(saved.get("source_frame_end_one_based", -1)) !=
                                int(frame["source_frame_end_one_based"]) or
                                saved.get("state") != state or
                                int(saved.get("window_index", -1)) != window_id):
                            raise IdentityEvidenceError(f"Historical window/Q summary mismatch: {key}")
                        seed_row = ledger.get(key)
                        expected_seeds = _expected_louvain_seeds(recording, target, state, window_id)
                        if (seed_row is None or seed_row.get("louvain_seeds") != expected_seeds or
                                float(seed_row.get("q_max")) != qmax or
                                seed_row.get("selected_neuron_indices_sha256") !=
                                job["selected_neuron_indices_sha256"]):
                            raise IdentityEvidenceError(f"Historical seed ledger mismatch: {key}")
                        selected_ledger_keys.add(key)
                        edge_count = round(n * MEAN_DEGREE / 2)
                        graph_id = f"{recording}|N{n}|rep-{repeat:03d}|{state}|window-{window_id:03d}"
                        identity = {
                            "schema": "SRT_RIKEN_EXPECTED_SOURCE_GRAPH_IDENTITY_V1",
                            "graph_id": graph_id,
                            "source_artifact_sha256": source_hashes[item["filename"]],
                            "selected_neuron_indices_sha256": job["selected_neuron_indices_sha256"],
                            "source_frame_indices_sha256": frame["source_frame_indices_sha256"],
                            "recording_id": recording, "N": n,
                            "animal_id": item["animal_id"],
                            "session_label": next(
                                (part for part in recording.split("_")
                                 if part in {"day1", "day2"}), None),
                            "subset_repeat": repeat, "state": state,
                            "state_index": state_index,
                            "window_id": window_id,
                            "node_order": "ascending saved zero-based original neuron IDs",
                            "graph_rule": "abs(corr(spike_smoothed S3/C1)); nonfinite->0; diagonal=0; SciPy MST(cost=1-abs_corr); strongest non-MST abs-correlation edges to round(N*16/2); binary unweighted",
                        }
                        selected_records.append({
                            **identity,
                            "expected_input_identity_sha256": sha256_bytes(canonical_json(identity)),
                            "source_filename": item["filename"],
                            "source_file_sha256": source_hashes[item["filename"]],
                            "subset_seed": job["subset_seed"],
                            "subset_seed_deviation": "realized target label string Nxx preserved; prereg numeric-N seed recipe differs",
                            "accepted_neuron_count": int(item["accepted_neurons"]),
                            "source_frame_start_one_based": frame["source_frame_start_one_based"],
                            "source_frame_end_one_based": frame["source_frame_end_one_based"],
                            "expected_edge_count": edge_count,
                            "expected_mean_degree": float(2 * edge_count / n),
                            "louvain_trials": LOUVAIN_TRIALS,
                            "louvain_seed_vector_sha256": hash_int64(expected_seeds),
                            "historical_q_vector_sha256": hash_float64(q_values),
                            "historical_q_max_first_index": first_max,
                            "historical_job_sha256": job_sha,
                            "historical_q_reference": "PRESENT_IN_PRIVATE_JOB_JSON; values not copied",
                            "historical_partition": "NOT_ARCHIVED",
                            "labeled_edge_set_sha256": None,
                            "identity_status": "SOURCE_SUBSET_WINDOW_AND_Q_REFERENCE_VERIFIED; EDGE_SET_NOT_RECONSTRUCTED",
                        })
    expected_selected_ledger = {
        key for key in ledger if key[1].startswith("N") and
        key[2] in repeat_map[(key[0], key[1])]
    }
    if selected_ledger_keys != expected_selected_ledger:
        raise IdentityEvidenceError("Selected graph seed ledger coverage is incomplete")
    if len(selected_records) != 4900 or len(ledger) != 49049:
        raise IdentityEvidenceError(
            f"Expected 4,900 selected graphs / 49,049 ledger rows; got "
            f"{len(selected_records)} / {len(ledger)}")
    selected_records.sort(key=lambda row: (
        EXPECTED_RECORDINGS.index(row["recording_id"]), TARGETS.index(row["N"]),
        row["subset_repeat"], STATES.index(row["state"]), row["window_id"]))
    panel = select_h3_panel(selected_records)
    return {
        "schema": "SRT_RIKEN_G0_SOURCE_IDENTITY_MANIFEST_V1",
        "status": "EXPECTED_IDENTITIES_VERIFIED; EDGE_IDENTITIES_PENDING_RECONSTRUCTION",
        "identity_tool_sha256": sha256_file(Path(__file__)),
        "verification_runtime": h3_runtime_manifest(),
        "preregistration_sha256": prereg_sha,
        "result_json_sha256": result_sha,
        "subsample_summary_sha256": summary_sha,
        "historical_code_hashes": local_code_hashes,
        "seed_ledger_sha256": sha256_file(ledger_path),
        "seed_ledger_rows": len(ledger), "historical_job_count": len(jobs),
        "public_summary_rows": len(summaries),
        "historical_finite_source_graphs": 49000,
        "g0_source_graph_count": len(selected_records),
        "g0_historical_q_trial_references": len(selected_records) * LOUVAIN_TRIALS,
        "source_data": source_records,
        "graph_builder": {
            "source_sha256": local_code_hashes["multirecording_primary.py"],
            "historical_function_sha256": EXPECTED_HISTORICAL_GRAPH_FUNCTION_SHA256,
            "signal": "spike_smoothed, S3/C1, 1,500-frame source windows",
            "correlation": "numpy.corrcoef by selected-neuron rows; nonfinite values to zero; diagonal zero; absolute value",
            "mst": "scipy.sparse.csgraph.minimum_spanning_tree on 1-abs(correlation), diagonal infinity",
            "edge_addition": "rank remaining abs-correlation values; threshold ties resolved by upper-triangle row-major source order",
            "mst_tie_semantics": (
                "candidate reconstruction uses SciPy 1.18.1; historical PS-A SciPy version "
                "was not recorded, so historical MST tie semantics are empirically unverified"),
            "edge_insertion": "sorted MST edges; strict-above-threshold edges in row-major order; boundary ties in row-major order",
            "historical_edge_lists": "NOT ARCHIVED; only source-code/data/subset reconstruction anchors exist",
        },
        "selection": {"subset_pool": 100, "selected_per_recording_N": 10,
                      "namespace": SUBSET_NAMESPACE, "root_seed": PANEL_SEED_ROOT,
                      "ranking": "ascending stable_seed; tie by repeat ID; no Q used"},
        "h3_panel": {"count": 120, "state_tokens": list(STATES),
                     "selection_is_Q_independent": True,
                     "partition_reference": "historical maximizing partitions are absent; no partition comparison is possible",
                     "records": panel},
        "source_graphs": selected_records,
    }


def _historical_connected_graph(source_path: Path):
    """Load the exact historical builder function without its module side effects."""
    expected = EXPECTED_SOURCE_CODE_HASHES["multirecording_primary.py"]
    if sha256_file(source_path) != expected:
        raise IdentityEvidenceError("Historical builder code hash mismatch")
    import networkx as nx
    import numpy as np
    from scipy.sparse.csgraph import minimum_spanning_tree

    source = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(source_path))
    wanted = {"upper_flat_index", "connected_graph"}
    functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)
                 and node.name in wanted]
    if {node.name for node in functions} != wanted:
        raise IdentityEvidenceError("Historical builder source functions are incomplete")
    namespace = {"Any": Any, "TARGET_MEAN_DEGREE": MEAN_DEGREE,
                 "nx": nx, "np": np,
                 "minimum_spanning_tree": minimum_spanning_tree}
    # This is intentionally limited to the two AST-verified functions from
    # the exact hash-pinned historical source; importing its module runs jobs.
    exec(compile(ast.Module(body=functions, type_ignores=[]), str(source_path), "exec"),  # noqa: S102
         namespace)
    function_source = "\n".join(ast.get_source_segment(source, node) or "" for node in functions)
    return namespace["connected_graph"], sha256_bytes(function_source.encode("utf-8"))


def build_candidate_graph(abs_corr):
    """Independent graph build with exact threshold-tie and insertion ordering."""
    import networkx as nx
    import numpy as np
    from scipy.sparse.csgraph import minimum_spanning_tree

    if (abs_corr.ndim != 2 or abs_corr.shape[0] != abs_corr.shape[1] or
            abs_corr.shape[0] < 2 or not np.isfinite(abs_corr).all() or
            not np.allclose(abs_corr, abs_corr.T, rtol=0.0, atol=1e-12) or
            not np.allclose(np.diag(abs_corr), 0.0, rtol=0.0, atol=1e-12) or
            np.any(abs_corr < 0) or np.any(abs_corr > 1 + 1e-12)):
        raise IdentityEvidenceError("Expected a finite symmetric absolute-correlation matrix")
    n = int(abs_corr.shape[0])
    possible = n * (n - 1) // 2
    target_edges = round(n * MEAN_DEGREE / 2.0)
    if target_edges < n - 1 or target_edges > possible:
        raise IdentityEvidenceError("Target mean degree is infeasible")
    cost = 1.0 - np.asarray(abs_corr, dtype=np.float64)
    np.fill_diagonal(cost, np.inf)
    mst = minimum_spanning_tree(cost).tocoo()
    mst_pairs = sorted({(min(int(i), int(j)), max(int(i), int(j)))
                        for i, j in zip(mst.row, mst.col, strict=True)})
    if len(mst_pairs) != n - 1:
        raise IdentityEvidenceError("Historical SciPy MST did not span all nodes")
    upper_i, upper_j = np.triu_indices(n, k=1)
    values = np.asarray(abs_corr[upper_i, upper_j], dtype=np.float64)
    mst_flat = {i * (2 * n - i - 1) // 2 + j - i - 1 for i, j in mst_pairs}
    candidates = [idx for idx in range(possible) if idx not in mst_flat]
    additional = target_edges - (n - 1)
    if additional:
        ranked = sorted(candidates, key=lambda idx: (-float(values[idx]), idx))
        threshold = float(values[ranked[additional - 1]])
        strict = [idx for idx in candidates if float(values[idx]) > threshold]
        tied = [idx for idx in candidates if float(values[idx]) == threshold]
        selected = strict + tied[:additional - len(strict)]
    else:
        selected = []
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    graph.add_edges_from((u, v, {"weight": 1.0}) for u, v in mst_pairs)
    # Historical code inserts strict-above-threshold edges first, then the
    # row-major boundary ties. Preserve that adjacency order: Louvain's seeded
    # tie behavior can depend on NetworkX neighbor iteration order.
    graph.add_edges_from((int(upper_i[k]), int(upper_j[k]), {"weight": 1.0})
                         for k in selected)
    if graph.number_of_edges() != target_edges or not nx.is_connected(graph):
        raise IdentityEvidenceError("Candidate graph failed connectedness/edge-count validation")
    return graph


def build_executor_order_graph(graph):
    """Rebuild the same labeled edges using PR #1126's normalized sorted order."""
    import networkx as nx

    executor_graph = nx.Graph()
    executor_graph.add_nodes_from(graph.nodes)
    executor_graph.add_weighted_edges_from(
        (int(u), int(v), 1.0) for u, v in sorted(
            (tuple(sorted((int(u), int(v)))) for u, v in graph.edges)))
    return executor_graph


def reconstruct_graph_pair(abs_corr, historical_source: Path,
                           source_node_ids: Iterable[int]):
    historical_builder, function_sha = _historical_connected_graph(historical_source)
    historical, _ = historical_builder(abs_corr)
    candidate = build_candidate_graph(abs_corr)
    node_ids = tuple(map(int, source_node_ids))
    if tuple(historical.nodes) != tuple(candidate.nodes) or len(node_ids) != len(historical):
        raise IdentityEvidenceError("Historical/candidate node order differs")
    def edge_set(graph):
        return {tuple(sorted((int(u), int(v)))) for u, v in graph.edges}

    old_edges, new_edges = edge_set(historical), edge_set(candidate)
    if old_edges != new_edges:
        raise IdentityEvidenceError("Historical/candidate labeled edge sets differ")
    old_adjacency = {u: tuple(historical.neighbors(u)) for u in historical.nodes}
    new_adjacency = {u: tuple(candidate.neighbors(u)) for u in candidate.nodes}
    executor_graph = build_executor_order_graph(candidate)
    executor_adjacency = {u: tuple(executor_graph.neighbors(u))
                          for u in executor_graph.nodes}
    labeled = {(min(node_ids[u], node_ids[v]), max(node_ids[u], node_ids[v]))
               for u, v in old_edges}
    return {
        "historical_graph": historical, "candidate_graph": candidate,
        "historical_edge_set_sha256": sha256_bytes(canonical_json(sorted(old_edges))),
        "candidate_edge_set_sha256": sha256_bytes(canonical_json(sorted(new_edges))),
        "historical_labeled_edge_set_sha256": sha256_bytes(canonical_json(sorted(labeled))),
        "candidate_labeled_edge_set_sha256": sha256_bytes(canonical_json(sorted(labeled))),
        "node_order_sha256": hash_int64(node_ids),
        "historical_adjacency_iteration_sha256": sha256_bytes(canonical_json(
            [[u, list(v)] for u, v in old_adjacency.items()])),
        "candidate_adjacency_iteration_sha256": sha256_bytes(canonical_json(
            [[u, list(v)] for u, v in new_adjacency.items()])),
        "adjacency_iteration_order_equal": old_adjacency == new_adjacency,
        "executor_sorted_adjacency_iteration_sha256": sha256_bytes(canonical_json(
            [[u, list(v)] for u, v in executor_adjacency.items()])),
        "historical_executor_adjacency_order_equal": old_adjacency == executor_adjacency,
        "historical_builder_function_sha256": function_sha,
    }


def h3_runtime_manifest() -> dict[str, Any]:
    from importlib import metadata
    candidate_lock = {"h5py": "3.16.0", "networkx": "3.6.1", "numpy": "2.5.3",
                      "python-louvain": "0.16", "scipy": "1.18.1"}
    actual = {}
    for package in candidate_lock:
        try:
            actual[package] = metadata.version(package)
        except metadata.PackageNotFoundError:
            actual[package] = None
    historical_record = {
        "python": "3.14.0", "platform": "macOS 15.7.4 arm64",
        "numpy": "2.5.3", "networkx": "3.6.1", "python-louvain": "0.16",
    }
    recorded_checks = {
        "python": platform.python_version() == historical_record["python"],
        "macos_arm64_and_patch": (
            sys.platform == "darwin" and platform.machine() == "arm64" and
            platform.mac_ver()[0] == "15.7.4"),
        "numpy": actual["numpy"] == historical_record["numpy"],
        "networkx": actual["networkx"] == historical_record["networkx"],
        "python_louvain_distribution": actual["python-louvain"] ==
        historical_record["python-louvain"],
    }
    candidate_lock_match = actual == candidate_lock
    return {
        "historical_environment_record": historical_record,
        "historical_recorded_checks": recorded_checks,
        "matches_historical_recorded_versions": all(recorded_checks.values()),
        "historical_environment_gaps": [
            "PS-A environment.txt does not record the SciPy version used by its MST builder",
            "PS-A environment.txt does not record h5py or the HDF5 library version",
        ],
        "historical_environment_fully_pinned": False,
        "candidate_replay_lock": candidate_lock,
        "actual": actual,
        "matches_candidate_replay_lock": candidate_lock_match,
        "replay_environment_matches_recorded_versions_and_candidate_lock":
            all(recorded_checks.values()) and candidate_lock_match,
        "historical_float_environment_exactness": "UNPROVEN_SCIPY_VERSION_NOT_RECORDED",
    }


def replay_louvain_q(graph, seeds: Iterable[int], *, require_target: bool = True):
    if (require_target and not h3_runtime_manifest()[
            "replay_environment_matches_recorded_versions_and_candidate_lock"]):
        raise IdentityEvidenceError(
            "H3 runtime does not match recorded PS-A versions and candidate replay lock")
    from community import community_louvain
    seed_list = list(map(int, seeds))
    if len(seed_list) != LOUVAIN_TRIALS:
        raise IdentityEvidenceError("Expected exactly 200 historical Louvain seeds")
    values, partitions = [], []
    for seed in seed_list:
        partition = community_louvain.best_partition(
            graph, weight="weight", resolution=1.0, random_state=seed)
        q = float(community_louvain.modularity(partition, graph, weight="weight"))
        if not math.isfinite(q):
            raise IdentityEvidenceError("Louvain produced a nonfinite Q")
        values.append(q)
        partitions.append(partition)
    best = max(range(len(values)), key=values.__getitem__)
    communities: dict[Any, list[int]] = {}
    for index, node in enumerate(graph.nodes):
        communities.setdefault(partitions[best][node], []).append(index)
    canonical_partition = [0] * len(graph)
    for group, indices in enumerate(sorted(communities.values(), key=min)):
        for index in indices:
            canonical_partition[index] = group
    return {"q_values": values, "q_max": values[best], "q_max_first_index": best,
            "best_partition_sha256": sha256_bytes(canonical_json(canonical_partition)),
            "partition_comparison": "NO_ARCHIVED_HISTORICAL_PARTITION"}


def replay_canonical_louvain_q(graph, source_neuron_indices: Iterable[int],
                                seeds: Iterable[int], *,
                                require_target: bool = True) -> dict[str, Any]:
    """Run the candidate common Q contract using stable source neuron IDs.

    The historical replay function above remains authoritative for legacy
    comparison. This separate entry point requires the prospective amendment
    and must not be interpreted as activating it.
    """
    if (require_target and not h3_runtime_manifest()[
            "replay_environment_matches_recorded_versions_and_candidate_lock"]):
        raise IdentityEvidenceError(
            "Canonical replay runtime does not match recorded PS-A versions and candidate lock")
    raw_source_ids = tuple(source_neuron_indices)
    if any(isinstance(value, bool) or not isinstance(value, numbers.Integral) or value < 0
           for value in raw_source_ids):
        raise IdentityEvidenceError(
            "Canonical replay requires nonnegative integer source-neuron indices")
    source_ids = tuple(int(value) for value in raw_source_ids)
    expected_local_nodes = set(range(len(source_ids)))
    if set(graph.nodes) != expected_local_nodes or len(source_ids) != len(graph):
        raise IdentityEvidenceError(
            "Historical graph nodes do not map one-to-one to the source neuron ID vector")
    labeled_edges = tuple((source_ids[int(u)], source_ids[int(v)])
                          for u, v in graph.edges)
    try:
        return canonical_louvain_q_vector(source_ids, labeled_edges, seeds)
    except (TypeError, ValueError) as exc:
        raise IdentityEvidenceError(
            f"Canonical Louvain Q replay input failed validation: {exc}") from exc


def load_h3_reference(panel_record: dict[str, Any], psa_root: Path) -> dict[str, Any]:
    """Load one saved H3 Q-vector and seeds, verifying the job-file identity."""
    recording = str(panel_record["recording_id"])
    n = int(panel_record["N"])
    repeat = int(panel_record["subset_repeat"])
    state = str(panel_record["state"])
    window = int(panel_record["window_id"])
    state_index = STATES.index(state)
    job_path = psa_root / "jobs" / f"{recording}__N{n}__rep-{repeat:03d}.json"
    if job_path.is_symlink() or not job_path.is_file():
        raise IdentityEvidenceError("H3 historical job is missing or symlinked")
    if sha256_file(job_path) != panel_record["historical_job_sha256"]:
        raise IdentityEvidenceError("H3 historical job hash differs from frozen manifest")
    job = json.loads(job_path.read_text(encoding="utf-8"))
    saved = job["windows"][f"state{state_index}_window{window}"]
    q_values = [float(value) for value in saved["q_values"]]
    seeds = _expected_louvain_seeds(recording, f"N{n}", state, window)
    if (saved.get("state") != state or int(saved.get("window_index", -1)) != window or
            hash_float64(q_values) != panel_record["historical_q_vector_sha256"] or
            hash_int64(seeds) != panel_record["historical_louvain_seed_vector_sha256"] or
            int(saved.get("q_max_first_index", -1)) !=
            int(panel_record["historical_q_max_first_index"])):
        raise IdentityEvidenceError("H3 saved Q-vector, seed, or coordinate identity mismatch")
    return {"graph_id": panel_record["graph_id"], "q_values": q_values,
            "louvain_seeds": seeds, "historical_q_max": max(q_values),
            "q_max_first_index": int(saved["q_max_first_index"]),
            "historical_job_sha256": panel_record["historical_job_sha256"]}


def prepare_h3_pilot_manifest(manifest: dict[str, Any], manifest_path: Path,
                              phase2_root: Path, psa_root: Path) -> dict[str, Any]:
    """Freeze and verify the first preselected H3 identity at each N; no graph/Q replay."""
    panel = manifest.get("h3_panel", {}).get("records")
    if not isinstance(panel, list):
        raise IdentityEvidenceError("Source manifest has no H3 panel records")
    chosen = select_h3_first_by_n(panel)
    source_by_recording = {row["recording_id"]: row
                           for row in manifest.get("source_data", [])}
    historical_builder = phase2_root / "multirecording_primary.py"
    if historical_builder.is_symlink() or not historical_builder.is_file():
        raise IdentityEvidenceError("Historical graph builder source is missing or symlinked")
    if sha256_file(historical_builder) != EXPECTED_SOURCE_CODE_HASHES[
            "multirecording_primary.py"]:
        raise IdentityEvidenceError("Historical graph builder source hash differs")

    source_hashes_checked: dict[str, str] = {}
    records = []
    for row in chosen:
        recording = str(row["recording_id"])
        source = source_by_recording.get(recording)
        if source is None:
            raise IdentityEvidenceError(f"Source file identity is missing for {recording}")
        filename = str(source["filename"])
        source_path = phase2_root / "data" / filename
        if source_path.is_symlink() or not source_path.is_file():
            raise IdentityEvidenceError(f"Source MAT is missing or symlinked: {filename}")
        if filename not in source_hashes_checked:
            source_hashes_checked[filename] = sha256_file(source_path)
        source_sha = source_hashes_checked[filename]
        if source_sha != source["sha256"] or source_sha != row["source_artifact_sha256"]:
            raise IdentityEvidenceError(f"Source MAT hash mismatch for {recording}")
        reference = load_h3_reference(row, psa_root)
        q_values = reference["q_values"]
        seeds = reference["louvain_seeds"]
        if (len(q_values) != LOUVAIN_TRIALS or len(seeds) != LOUVAIN_TRIALS or
                any(not math.isfinite(value) for value in q_values) or
                max(q_values) != reference["historical_q_max"] or
                reference["q_max_first_index"] != row["historical_q_max_first_index"]):
            raise IdentityEvidenceError(
                f"H3 reference completeness check failed: {row['graph_id']}")
        records.append({
            "pilot_order": int(row["pilot_order"]), "N": int(row["N"]),
            "graph_id": row["graph_id"], "recording_id": recording,
            "source_filename": filename, "source_mat_sha256": source_sha,
            "state": row["state"], "window_id": int(row["window_id"]),
            "subset_repeat": int(row["subset_repeat"]),
            "selected_neuron_indices_sha256": row["selected_neuron_indices_sha256"],
            "expected_node_order_sha256": row["expected_node_order_sha256"],
            "source_frame_indices_sha256": row["source_frame_indices_sha256"],
            "expected_edge_count": int(row["expected_edge_count"]),
            "historical_job_sha256": reference["historical_job_sha256"],
            "historical_louvain_seed_vector_sha256": hash_int64(seeds),
            "historical_q_vector_sha256": hash_float64(q_values),
            "historical_q_max": reference["historical_q_max"],
            "historical_q_max_first_index": reference["q_max_first_index"],
            "source_and_reference_status": "HASHES_AND_200_SEEDS_VERIFIED; GRAPH_NOT_REBUILT",
        })
    return {
        "schema": "SRT_RIKEN_H3_IDENTITY_CALIBRATION_PILOT_V1",
        "status": "PREPARED_NOT_APPROVED_NOT_EXECUTED",
        "source_manifest_sha256": sha256_file(manifest_path),
        "source_manifest_identity_tool_sha256": manifest.get("identity_tool_sha256"),
        "pilot_preparation_tool_sha256": sha256_file(Path(__file__)),
        "historical_graph_builder_sha256": EXPECTED_SOURCE_CODE_HASHES[
            "multirecording_primary.py"],
        "historical_graph_builder_function_sha256":
            EXPECTED_HISTORICAL_GRAPH_FUNCTION_SHA256,
        "selection_rule": (
            "First row in the Q-independent frozen 120-row H3 panel for each ascending N; "
            "tie order is registered recording order then wake before NREM"),
        "scientific_comparison": {
            "historical_order_is_authoritative": True,
            "trial_q_absolute_tolerance_proposed": H3_TRIAL_Q_ATOL_PROPOSED,
            "trial_q_relative_tolerance": 0.0,
            "qmax_absolute_tolerance": H3_QMAX_ATOL,
            "first_max_index_must_match": True,
            "tolerance_status": "PROPOSED_FOR_REVIEW_NOT_YET_RESEARCHER_APPROVED",
        },
        "candidate_limits_not_authorized": {
            "wall_seconds": H3_PILOT_WALL_SECONDS,
            "process_tree_cpu_seconds": H3_PILOT_CPU_SECONDS,
            "max_compute_workers": H3_PILOT_MAX_WORKERS,
            "sampled_aggregate_rss_bytes": H3_PILOT_RSS_BYTES,
            "output_bytes": H3_PILOT_OUTPUT_BYTES,
            "louvain_trials_total": len(records) * LOUVAIN_TRIALS * 2,
        },
        "stop_rule": (
            "Stop immediately on source identity, graph construction, historical-order Q-vector, "
            "Qmax, or first-max integrity failure; sorted-executor mismatch is a separate "
            "compatibility diagnostic and does not invalidate a passing historical graph/Q"),
        "source_hashes_checked": source_hashes_checked,
        "pilot_count": len(records), "records": records,
    }


def run_h3_replay_for_graph(graph_pair: dict[str, Any], panel_record: dict[str, Any],
                            reference: dict[str, Any], *,
                            require_target_runtime: bool = True) -> dict[str, Any]:
    """Replay saved seeds on authoritative historical and diagnostic sorted orders."""
    if reference.get("graph_id") != panel_record.get("graph_id"):
        raise IdentityEvidenceError("H3 Q reference does not match the panel graph ID")
    historical_graph = graph_pair["historical_graph"]
    executor_graph = build_executor_order_graph(graph_pair["candidate_graph"])
    seeds = list(map(int, reference["louvain_seeds"]))
    historical_replay = replay_louvain_q(
        historical_graph, seeds, require_target=require_target_runtime)
    executor_replay = replay_louvain_q(
        executor_graph, seeds, require_target=require_target_runtime)

    def degree_hash(graph):
        return hash_int64(degree for _, degree in graph.degree())

    return {
        "graph_id": panel_record["graph_id"],
        "historical_edge_set_sha256": graph_pair["historical_edge_set_sha256"],
        "candidate_edge_set_sha256": graph_pair["candidate_edge_set_sha256"],
        "historical_labeled_edge_set_sha256":
            graph_pair["historical_labeled_edge_set_sha256"],
        "candidate_labeled_edge_set_sha256":
            graph_pair["candidate_labeled_edge_set_sha256"],
        "historical_node_order_sha256": graph_pair["node_order_sha256"],
        "candidate_node_order_sha256": graph_pair["node_order_sha256"],
        "source_artifact_sha256": panel_record["source_artifact_sha256"],
        "selected_neuron_indices_sha256":
            panel_record["selected_neuron_indices_sha256"],
        "expected_input_identity_sha256":
            panel_record.get("expected_input_identity_sha256"),
        "expected_source_frame_indices_sha256":
            panel_record["source_frame_indices_sha256"],
        "reconstructed_source_frame_indices_sha256":
            graph_pair["source_frame_indices_sha256"],
        "historical_builder_function_sha256":
            graph_pair["historical_builder_function_sha256"],
        "historical_N": historical_graph.number_of_nodes(),
        "candidate_N": executor_graph.number_of_nodes(),
        "historical_E": historical_graph.number_of_edges(),
        "candidate_E": executor_graph.number_of_edges(),
        "historical_adjacency_iteration_sha256":
            graph_pair["historical_adjacency_iteration_sha256"],
        "candidate_adjacency_iteration_sha256":
            graph_pair["candidate_adjacency_iteration_sha256"],
        "executor_sorted_adjacency_iteration_sha256":
            graph_pair["executor_sorted_adjacency_iteration_sha256"],
        "historical_candidate_adjacency_order_equal":
            graph_pair["adjacency_iteration_order_equal"],
        "historical_executor_adjacency_order_equal":
            graph_pair["historical_executor_adjacency_order_equal"],
        "historical_degree_sequence_sha256": degree_hash(historical_graph),
        "candidate_degree_sequence_sha256": degree_hash(executor_graph),
        "louvain_seeds": seeds,
        "historical_builder_q_values": historical_replay["q_values"],
        "historical_builder_q_max_first_index":
            historical_replay["q_max_first_index"],
        "q_values": executor_replay["q_values"],
        "historical_q_values": reference["q_values"],
        "historical_q_max": reference["historical_q_max"],
        "historical_q_max_first_index": reference["q_max_first_index"],
        "q_max_first_index": executor_replay["q_max_first_index"],
        "historical_builder_partition_sha256":
            historical_replay["best_partition_sha256"],
        "executor_partition_sha256": executor_replay["best_partition_sha256"],
        "partition_comparison": "HISTORICAL_PARTITION_NOT_ARCHIVED",
    }


def validate_h3_replay(expected_panel: list[dict[str, Any]],
                       replay_rows: list[dict[str, Any]], *,
                       trial_q_atol: float | None) -> dict[str, Any]:
    if (trial_q_atol is None or not math.isfinite(trial_q_atol) or
            float(trial_q_atol) != H3_TRIAL_Q_ATOL_PROPOSED):
        raise IdentityEvidenceError(
            "Trial-Q tolerance must equal the proposed pre-run 1e-10 absolute threshold")
    expected = {row["graph_id"]: row for row in expected_panel}
    actual = {row.get("graph_id"): row for row in replay_rows}
    if (len(expected) != len(expected_panel) or len(actual) != len(replay_rows) or
            set(actual) != set(expected)):
        raise IdentityEvidenceError("H3 replay IDs are missing, duplicated, or unexpected")

    source_failures: list[str] = []
    graph_failures: list[str] = []
    historical_qvector_failures: list[str] = []
    historical_qmax_failures: list[str] = []
    executor_qvector_failures: list[str] = []
    executor_qmax_failures: list[str] = []
    executor_input_failures: list[str] = []
    graph_summaries, q_summaries, executor_summaries = [], [], []

    def q_comparison(left: list, right: list) -> tuple[float, int]:
        differences = [abs(float(a) - float(b))
                       for a, b in zip(left, right, strict=True)]
        return max(differences, default=0.0), sum(value > trial_q_atol
                                                  for value in differences)

    def finite_q_vector(values: Any) -> bool:
        return (isinstance(values, list) and len(values) == LOUVAIN_TRIALS and
                all(type(value) in (int, float) and math.isfinite(value)
                    for value in values))

    for graph_id, ref in expected.items():
        row = actual[graph_id]
        source_equal = (
            row.get("source_artifact_sha256") == ref.get("source_artifact_sha256") and
            row.get("selected_neuron_indices_sha256") ==
            ref.get("selected_neuron_indices_sha256") and
            row.get("expected_source_frame_indices_sha256") ==
            ref.get("source_frame_indices_sha256") and
            row.get("reconstructed_source_frame_indices_sha256") ==
            ref.get("source_frame_indices_sha256") and
            row.get("historical_builder_function_sha256") ==
            EXPECTED_HISTORICAL_GRAPH_FUNCTION_SHA256 and
            row.get("expected_input_identity_sha256") ==
            ref.get("expected_input_identity_sha256"))
        if not source_equal:
            source_failures.append(graph_id)
        graph_equal = (
            row.get("historical_edge_set_sha256") == row.get("candidate_edge_set_sha256") and
            row.get("historical_edge_set_sha256") is not None and
            row.get("historical_labeled_edge_set_sha256") ==
            row.get("candidate_labeled_edge_set_sha256") and
            row.get("historical_node_order_sha256") == ref["expected_node_order_sha256"] and
            row.get("candidate_node_order_sha256") == ref["expected_node_order_sha256"] and
            int(row.get("historical_N", -1)) == ref["N"] and
            int(row.get("candidate_N", -1)) == ref["N"] and
            int(row.get("historical_E", -1)) == ref["expected_edge_count"] and
            int(row.get("candidate_E", -1)) == ref["expected_edge_count"] and
            row.get("historical_adjacency_iteration_sha256") ==
            row.get("candidate_adjacency_iteration_sha256") and
            row.get("historical_candidate_adjacency_order_equal") is True and
            row.get("historical_degree_sequence_sha256") ==
            row.get("candidate_degree_sequence_sha256"))
        if not graph_equal:
            graph_failures.append(graph_id)
        graph_summaries.append({
            "graph_id": graph_id,
            "source_input_identity": "PASS" if source_equal else "NC-INVALID",
            "historical_builder_consistency": "PASS" if graph_equal else "NC-INVALID",
        })

        seeds = row.get("louvain_seeds")
        executor_q = row.get("q_values")
        old_q = row.get("historical_q_values")
        historical_q = row.get("historical_builder_q_values")
        try:
            seeds_valid = (
                isinstance(seeds, list) and len(seeds) == LOUVAIN_TRIALS and
                hash_int64(seeds) == ref["historical_louvain_seed_vector_sha256"])
        except (TypeError, ValueError, OverflowError):
            seeds_valid = False
        try:
            archived_qmax = float(row.get("historical_q_max"))
            reference_q_hash_matches = (
                finite_q_vector(old_q) and hash_float64(old_q) ==
                ref["historical_q_vector_sha256"])
        except (TypeError, ValueError, OverflowError):
            archived_qmax = math.nan
            reference_q_hash_matches = False
        reference_q_valid = (
            reference_q_hash_matches and math.isfinite(archived_qmax) and
            max(old_q) == archived_qmax and
            row.get("historical_q_max_first_index") ==
            ref["historical_q_max_first_index"])
        historical_q_valid = (
            finite_q_vector(historical_q))
        if not seeds_valid or not reference_q_valid or not historical_q_valid:
            historical_qvector_failures.append(graph_id)
        else:
            hist_max_delta, hist_exceed = q_comparison(historical_q, old_q)
            if hist_exceed:
                historical_qvector_failures.append(graph_id)
            if (abs(max(map(float, historical_q)) - float(row.get("historical_q_max"))) >
                    H3_QMAX_ATOL or
                    row.get("historical_builder_q_max_first_index") !=
                    ref["historical_q_max_first_index"]):
                historical_qmax_failures.append(graph_id)
            q_summaries.append({
                "graph_id": graph_id,
                "historical_order_max_abs_trial_q_delta": hist_max_delta,
                "historical_order_trials_over_atol": hist_exceed,
            })

        executor_q_valid = (
            seeds_valid and finite_q_vector(executor_q))
        if not executor_q_valid:
            executor_input_failures.append(graph_id)
        elif reference_q_valid:
            executor_max_delta, executor_exceed = q_comparison(executor_q, old_q)
            if executor_exceed:
                executor_qvector_failures.append(graph_id)
            if (abs(max(map(float, executor_q)) - float(row.get("historical_q_max"))) >
                    H3_QMAX_ATOL or
                    row.get("q_max_first_index") != ref["historical_q_max_first_index"]):
                executor_qmax_failures.append(graph_id)
            executor_summaries.append({
                "graph_id": graph_id,
                "sorted_path_adjacency_order_equal":
                    row.get("historical_executor_adjacency_order_equal") is True,
                "sorted_path_max_abs_trial_q_delta": executor_max_delta,
                "sorted_path_trials_over_atol": executor_exceed,
            })
        else:
            executor_input_failures.append(graph_id)

    source_failures = sorted(set(source_failures))
    graph_failures = sorted(set(graph_failures))
    historical_qvector_failures = sorted(set(historical_qvector_failures))
    historical_qmax_failures = sorted(set(historical_qmax_failures))
    executor_qvector_failures = sorted(set(executor_qvector_failures))
    executor_qmax_failures = sorted(set(executor_qmax_failures))
    executor_input_failures = sorted(set(executor_input_failures))
    source_status = "PASS" if not (source_failures or graph_failures) else "NC-INVALID"
    historical_status = "PASS" if not (
        historical_qvector_failures or historical_qmax_failures) else "NC-INVALID"
    executor_problem = bool(executor_qvector_failures or executor_qmax_failures)
    executor_order_differs = any(
        not row["sorted_path_adjacency_order_equal"] for row in executor_summaries)
    executor_status = (
        "INCOMPLETE_OR_INVALID" if executor_input_failures else
        "INCOMPATIBLE" if executor_problem else
        "RESULTS_MATCH_WITH_DIFFERENT_ADJACENCY_ORDER" if executor_order_differs else
        "COMPATIBLE")
    overall = (
        "NC-INVALID_SOURCE_GRAPH_IDENTITY" if source_status != "PASS" else
        "NC-INVALID_HISTORICAL_Q_REPLAY" if historical_status != "PASS" else
        "SOURCE_GRAPH_AND_HISTORICAL_Q_PASS")
    return {
        "panel_count": len(expected_panel),
        "trial_q_tolerance": {"absolute": H3_TRIAL_Q_ATOL_PROPOSED,
                               "relative": 0.0, "qmax_absolute": H3_QMAX_ATOL,
                               "first_max_index_exact": True},
        "source_graph_identity": {
            "status": source_status,
            "source_input_failures": source_failures,
            "historical_vs_faithful_builder_failures": graph_failures,
            "per_graph": graph_summaries,
        },
        "historical_order_q_replay": {
            "status": historical_status,
            "trial_q_failures": historical_qvector_failures,
            "qmax_or_first_index_failures": historical_qmax_failures,
            "per_graph": q_summaries,
        },
        "executor_sorted_order_compatibility": {
            "status": executor_status,
            "incomplete_or_invalid_inputs": executor_input_failures,
            "trial_q_failures": executor_qvector_failures,
            "qmax_or_first_index_failures": executor_qmax_failures,
            "per_graph": executor_summaries,
            "does_not_invalidate_source_graph_or_historical_replay": True,
        },
        "status": overall,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase2-root", type=Path, required=True,
                        help="Private local Phase-2 root containing data/ and source code")
    parser.add_argument("--psa-root", type=Path, required=True,
                        help="Private local PS-A runtime root containing jobs/ and seed ledger")
    parser.add_argument("--output", type=Path, required=True,
                        help="Public-safe manifest or pilot-inventory output path")
    parser.add_argument("--prepare-h3-pilot", action="store_true",
                        help="Verify and freeze the first fixed H3 identity at each N only")
    parser.add_argument("--manifest", type=Path,
                        help="Existing public-safe source-identity manifest for H3 preparation")
    args = parser.parse_args(argv)
    if args.prepare_h3_pilot:
        if args.manifest is None:
            parser.error("--prepare-h3-pilot requires --manifest")
        if args.output.exists() or args.output.is_symlink():
            parser.error("Pilot manifest output already exists; refusing to overwrite")
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
        prepared = prepare_h3_pilot_manifest(
            manifest, args.manifest, args.phase2_root, args.psa_root)
        summary = {"status": prepared["status"],
                   "pilot_count": prepared["pilot_count"],
                   "louvain_trials_total": prepared["candidate_limits_not_authorized"][
                       "louvain_trials_total"]}
    else:
        if args.manifest is not None:
            parser.error("--manifest is only valid with --prepare-h3-pilot")
        prepared = build_inventory(repo_root=ROOT, phase2_root=args.phase2_root,
                                   psa_root=args.psa_root)
        summary = {"status": prepared["status"],
                   "source_graphs": prepared["g0_source_graph_count"],
                   "h3_panel": prepared["h3_panel"]["count"]}
    payload = canonical_json(prepared) + b"\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_name(args.output.name + ".tmp")
    if temporary.exists() or temporary.is_symlink():
        parser.error("Output temporary path already exists; refusing to overwrite")
    with temporary.open("wb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    if args.prepare_h3_pilot:
        try:
            os.link(temporary, args.output)
        except FileExistsError:
            temporary.unlink(missing_ok=True)
            parser.error("Pilot output appeared concurrently; refusing to overwrite")
        temporary.unlink()
    else:
        os.replace(temporary, args.output)
    print(json.dumps({**summary, "manifest_sha256": sha256_bytes(payload),
                      "bytes": len(payload)}, sort_keys=True))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
