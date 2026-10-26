"""Generate a public H3 closure projection; never writes into the private run.

No Louvain call exists here. Optional raw-signal inspection is limited to
constant/variance/nonfinite counts; no signal, Q vector or neuron ID is exported.
"""
from __future__ import annotations

import argparse
import json
import statistics
from collections import defaultdict
from pathlib import Path

import h3_120_supervised_panel as h3
import h3_supervised_pilot as pilot
import riken_source_identity as identity
from observed_calibration_measurement import RawWindowCache
from observed_calibration_sample import canonical

PUBLIC_FILENAME = "H3_120_PUBLIC_CLOSURE_2026-10-26.json"


def describe(values):
    return {"count": len(values), "mean": statistics.mean(values),
            "median": statistics.median(values), "minimum": min(values), "maximum": max(values),
            "positive": sum(v > 0 for v in values), "negative": sum(v < 0 for v in values),
            "zero": sum(v == 0 for v in values)}


def constant_signal_audit(packet, manifest, phase2: Path, psa: Path):
    import numpy as np

    h3.validate_h3_120_private_roots(packet, manifest, phase2, psa)
    legacy = {row["graph_id"]: {**row, "source_mat_sha256": row["source_artifact_sha256"]}
              for row in packet["rows"]}
    groups = defaultdict(list)
    for row in packet["rows"]:
        groups[(row["recording_id"], row["state"], row["window_id"],
                row["source_frame_indices_sha256"])].append(row)
    cache = RawWindowCache(256 * 1024**2)
    source_hash_cache = {}
    counts = []
    unique_pairs, affected_windows = set(), set()
    for key, group in sorted(groups.items()):
        for row in group:
            path, selected, _, _ = pilot._load_private_row(
                legacy[row["graph_id"]], manifest, phase2, psa, source_hash_cache)
            values, _ = cache.get(path, source_sha=row["source_artifact_sha256"],
                                  state=row["state"], window=row["window_id"],
                                  frame_sha=row["source_frame_indices_sha256"])
            subset = values[np.asarray(selected), :]
            zero = np.var(subset, axis=1) == 0
            const = np.all(subset == subset[:, :1], axis=1) & np.isfinite(subset[:, 0])
            nonfinite = int(np.count_nonzero(~np.isfinite(subset)))
            ids = [selected[i] for i in np.flatnonzero(zero)]
            if ids:
                affected_windows.add(key)
            unique_pairs.update((*key, node) for node in ids)
            counts.append({"graph_id": row["graph_id"], "recording_id": row["recording_id"],
                           "N": row["N"], "state": row["state"], "window_id": row["window_id"],
                           "source_frame_indices_sha256": row["source_frame_indices_sha256"],
                           "zero_variance_instances": len(ids), "constant_instances": int(sum(const)),
                           "raw_nonfinite_values": nonfinite})
    return {"method": "read-only selected-signal variance/constant audit; no corrcoef/graph/Q calculation",
            "rows": sorted(counts, key=lambda r: r["graph_id"]),
            "affected_graphs": sum(r["zero_variance_instances"] > 0 for r in counts),
            "zero_variance_graph_neuron_instances": sum(r["zero_variance_instances"] for r in counts),
            "independent_affected_source_windows": len(affected_windows),
            "unique_neuron_window_combinations": len(unique_pairs),
            "raw_nonfinite_values": sum(r["raw_nonfinite_values"] for r in counts),
            "status": "IMPACT-BOUNDED"}


def build_closure(run_dir: Path, *, phase2: Path, psa: Path) -> dict:
    verified = h3.verify_h3_120_run(run_dir, host_state_dir=pilot.default_host_state_dir())
    if not verified["completed_120_row_panel"]:
        raise ValueError("Only a verified complete real H3 run can be closed")
    summary = pilot._read_json(run_dir / "h3-summary.json")
    packet, manifest = h3.validate_h3_120_packet(h3.HERE / h3.PACKET_FILENAME,
                                               h3.HERE / h3.MANIFEST_FILENAME)
    files = sorted((run_dir / h3.ROW_DIR).glob("*.json"))
    rows = [pilot._read_json(path) for path in files]
    deltas = [r["canonical_qmax"] - r["historical_qmax"] for r in rows]
    trial_deltas = [v for r in rows for v in r["canonical_minus_historical_q_differences"]]
    groups = {}
    for field in ("N", "state", "recording_id"):
        groups[field] = {str(value): describe([r["canonical_qmax"] - r["historical_qmax"]
                                               for r in rows if r[field] == value])
                         for value in sorted({r[field] for r in rows})}
    cost = {str(n): {"rows": len(rr),
                     "dual_order_wall_seconds": describe([r["elapsed_seconds"] for r in rr]),
                     "dual_order_cpu_seconds": describe([r["process_cpu_seconds"] for r in rr])}
            for n in identity.TARGETS if (rr := [r for r in rows if r["N"] == n])}
    watch = [json.loads(line)["event"] for line in (run_dir / "watchdog.jsonl").read_text().splitlines()]
    samples = [e for e in watch if e.get("event") == "resource_sample"]
    usage = summary["watchdog"]["usage"]
    # Whitelist counters; never project private run paths/authorization JSON.
    resource = {key: usage.get(key) for key in (
        "wall_seconds", "cpu_seconds", "peak_aggregate_rss_bytes", "peak_compute_workers",
        "peak_process_group_members", "run_directory_bytes")}
    resource["row_artifact_bytes"] = sum(p.stat().st_size for p in files)
    resource["terminal_all_file_bytes"] = sum(p.stat().st_size for p in run_dir.rglob("*") if p.is_file())
    resource["storage_semantics"] = ("run_directory_bytes is Watchdog exit sample including its emergency scratch reserve; "
                                     "terminal_all_file_bytes is the closed-directory file-byte sum after reserve cleanup")
    resource["samples"] = len(samples)
    resource["memory_semantics"] = "sampled RSS, not process-group true peak or hard limit"
    return {"schema": "SRT_H3_120_PUBLIC_SCIENTIFIC_CLOSURE_V1",
            "run_uuid": summary["run_id"], "execution_head_sha": summary["head_sha"],
            "closure": "PASS", "verification": verified,
            "h3_packet_sha256": h3.EXPECTED_PACKET_SHA256,
            "source_manifest_sha256": h3.EXPECTED_MANIFEST_SHA256,
            "artifact_sha256": {name: identity.sha256_file(run_dir / name) for name in
                                 ("h3-summary.json", "run-manifest.json", "runner-terminal.json",
                                  "h3-evidence.jsonl", "h3-control.jsonl", "watchdog.jsonl", "runner.stdout.log")},
            "row_artifact_hashes": [{"graph_id": row["graph_id"], "sha256": identity.sha256_file(path)}
                                    for row, path in zip(rows, files, strict=True)],
            "source_identity_pass": sum(r["source_graph_identity"] == "PASS" for r in rows),
            "historical_q_replay_pass": sum(r["historical_order_q_replay"] == "PASS" for r in rows),
            "historical_trial_max_abs_delta": max(r["historical_reference_max_abs_delta"] for r in rows),
            "canonical_minus_historical_qmax": describe(deltas), "qmax_groups": groups,
            "canonical_first_max_matches_history": sum(r["canonical_first_max_trial_index"] ==
                                                        r["historical_first_max_trial_index"] for r in rows),
            "paired_trial_nonzero_differences": sum(v != 0 for v in trial_deltas),
            "paired_trial_absolute_difference": describe([abs(v) for v in trial_deltas]),
            "canonical_comparison": "DESCRIPTIVE_ONLY_NO_PASS_THRESHOLD_NO_ADDITIONAL_TESTS",
            "dual_order_row_cost_by_N": cost, "resource": resource,
            "runtime": rows[0]["runtime_manifest"],
            "constant_signal_audit": constant_signal_audit(packet, manifest, phase2, psa),
            "limitations": ["fixed 120-row panel, no population effect inference",
                            "historical SciPy/h5py/HDF5 versions incompletely archived",
                            "no independent Louvain recalculation in closure audit",
                            "no phase-separated H3 timing or source-read byte telemetry",
                            "zero correlations for undefined corrcoef are inherited modeling choices",
                            "MIXING-UNRESOLVED unchanged; G0/T1 RESOURCE NO-GO"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--phase2-root", type=Path, required=True)
    parser.add_argument("--psa-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists() or args.output.is_symlink() or args.run_dir.resolve() in args.output.resolve().parents:
        parser.error("Output must be new and outside the private run directory")
    closure = build_closure(args.run_dir, phase2=args.phase2_root, psa=args.psa_root)
    args.output.write_bytes(canonical(closure) + b"\n")
    print(json.dumps({"closure": closure["closure"], "sha256": identity.sha256_file(args.output),
                      "constant_signal_audit": {k: v for k, v in closure["constant_signal_audit"].items() if k != "rows"}}))
