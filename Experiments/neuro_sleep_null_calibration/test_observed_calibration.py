"""Synthetic-only source/Q, real Watchdog and fail-closed admission regressions."""
from __future__ import annotations

import copy
import json
import os
import sys
import tempfile
import time
import unittest
import uuid
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import h3_supervised_pilot as pilot
import h5py
import nc0a_watchdog as watchdog
import networkx as nx
import numpy as np
import observed_calibration_runner as runner
import riken_source_identity as identity
from g0_q_protocol import canonical_louvain_q_vector
from observed_calibration_measurement import (
    MeasurementError,
    PhaseRecords,
    RawWindowCache,
    measure_row,
    process_counters,
)
from observed_calibration_sample import HERE as MODULE_DIR
from observed_calibration_sample import (
    SAMPLE_FILENAME,
    build_sample,
    canonical,
    validate_sample,
)
from scipy.sparse.csgraph import minimum_spanning_tree


def fixture(root: Path):
    """Engineering seed only. Never imports or points to a RIKEN data root."""
    source = root / "synthetic_signal.mat"
    values = np.random.default_rng(772026).normal(size=(3000, 32))
    values[:, 0] = 0
    with h5py.File(source, "w") as handle:
        handle.create_dataset("spike_smoothed", data=values, chunks=(50, 32), compression="gzip")
        a = handle.create_dataset("wake", data=np.arange(1, 3001))
        b = handle.create_dataset("nrem", data=np.arange(3000, 0, -1))
        handle.create_dataset("frame/used_frame", data=np.array([a.ref, b.ref], dtype=h5py.ref_dtype))
    rows, selections = [], {}
    for i, selected in enumerate((list(range(24)), list(range(4, 24))), 1):
        graph_id = f"synthetic-cost-{i}"
        rows.append({"sample_order": i, "graph_id": graph_id,
                     "N": len(selected), "expected_edge_count": 8 * len(selected),
                     "recording_id": "synthetic", "state": "wake", "window_id": 0,
                     "source_file_sha256": identity.sha256_file(source),
                     "source_frame_indices_sha256": identity.hash_int64(range(1500)),
                     "selected_neuron_indices_sha256": identity.hash_int64(selected),
                     "louvain_seed_vector_sha256": identity.hash_int64(range(700, 900))})
        selections[graph_id] = selected
    return source, rows, selections


def synthetic_builder(corr):
    """Small independent test builder; production always loads hash-pinned PS-A AST."""
    n = len(corr)
    cost = 1.0 - corr
    np.fill_diagonal(cost, np.inf)
    tree = minimum_spanning_tree(cost).tocoo()
    edges = {tuple(sorted((int(u), int(v)))) for u, v in zip(tree.row, tree.col, strict=True)}
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    graph.add_weighted_edges_from((u, v, 1.0) for u, v in sorted(edges))
    remaining = sorted(((u, v) for u in range(n) for v in range(u + 1, n) if (u, v) not in edges),
                       key=lambda edge: (-float(corr[edge]), edge))
    graph.add_weighted_edges_from((u, v, 1.0) for u, v in remaining[:8 * n - len(edges)])
    return graph, {}


def row_processor(source, selections, cache, scenario="normal"):
    def process(row, phase_sink=None):
        if scenario == "slow":
            time.sleep(3)
        if scenario == "scientific_failure":
            raise identity.IdentityEvidenceError("injected graph integrity failure")
        if scenario == "io_failure":
            raise OSError("injected write/read failure")
        return measure_row(row, source_path=source, selected=selections[row["graph_id"]],
                           seeds=list(range(700, 900)), cache=cache,
                           initial_phases=PhaseRecords(phase_sink),
                           builder_factory=lambda: (synthetic_builder, "synthetic-builder-only"))
    return process


def supervised_child(payload_path: Path) -> int:
    payload = json.loads(payload_path.read_text())
    if payload.get("schema") != "SRT_SYNTHETIC_OBSERVED_TEST_ONLY":
        raise ValueError("Synthetic payload required")
    if payload["scenario"] == "child_exit":
        os._exit(42)
    watchdog.guard_watchdog_parent(int(os.environ["NC0A_WATCHDOG_PARENT_PID"]))
    pilot._write_runner_lease(Path.cwd())
    rows = payload["rows"]
    if any(not r["graph_id"].startswith("synthetic-") for r in rows):
        raise ValueError("Biological identity cannot enter test child")
    cache = RawWindowCache(2 * 1024**2)
    result = runner.execute_rows(rows, run_dir=Path.cwd(), synthetic=True,
                                 process_row=row_processor(Path(payload["source"]), payload["selected"],
                                                           cache, payload["scenario"]))
    return 0 if result["status"] == "completed" else 31


class TestObservedCalibration(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="srt-observed-synthetic-")
        self.root = Path(self.temp.name).resolve()
        self.source, self.rows, self.selected = fixture(self.root)

    def tearDown(self):
        self.temp.cleanup()

    def run_supervised(self, scenario="normal", **overrides):
        run_dir = self.root / "runs" / str(uuid.uuid4())
        state = self.root / "state" / run_dir.name
        payload = self.root / f"payload-{uuid.uuid4()}.json"
        payload.write_text(json.dumps({"schema": "SRT_SYNTHETIC_OBSERVED_TEST_ONLY", "scenario": scenario,
                                       "rows": self.rows, "source": str(self.source), "selected": self.selected}))
        limits = pilot._build_watchdog_limits(runner.RESOURCE_CANDIDATE, test_overrides={
            "wall_seconds": 30, "cpu_seconds": 30, "aggregate_rss_bytes": 512 * 1024**2,
            "run_disk_bytes": 32 * 1024**2, "reserve_free_disk_bytes": 1,
            "case_seconds": 30, "oracle_seconds": 30, "poll_seconds": 0.05,
            "memory_enforcement_backend": "SAMPLED_ONLY", "host_memory_free_percent_stop": None,
            "boot_volume_path": None, "boot_reserve_free_disk_bytes": None,
            "minimum_boot_free_disk_bytes": None, "swap_volume_path": None,
            "swap_volume_reserve_free_disk_bytes": None, "minimum_swap_volume_free_disk_bytes": None,
            "swap_growth_stop_bytes": None, "require_ac_power": False,
            "require_thermal_normal": False, "require_sleep_assertion": False, **overrides})
        with patch.object(watchdog, "_default_activity_lock_path", return_value=state / "global.lock"):
            summary = pilot._launch_supervised(
                [sys.executable, str(Path(__file__)), "--synthetic-worker", str(payload)],
                run_dir=run_dir, state_dir=state, run_id=run_dir.name,
                pilot_sha256=identity.sha256_file(payload), head={"head_sha": "synthetic-test"},
                candidate={"workflow": "SYNTHETIC_TEST_ONLY"}, limits=limits)
        return run_dir, state, summary

    def test_sample_is_deterministic_outcome_blind_and_complete(self):
        sample, manifest = validate_sample()
        self.assertEqual(identity.sha256_file(MODULE_DIR / SAMPLE_FILENAME), runner.EXPECTED_SAMPLE_SHA256)
        changed = copy.deepcopy(manifest)
        for row in changed["source_graphs"]:
            row["historical_q_max_first_index"] = 999  # never a selection input
        self.assertEqual(build_sample(changed), sample)
        h3 = {r["graph_id"] for r in manifest["h3_panel"]["records"]}
        self.assertFalse(h3 & {r["graph_id"] for r in sample["primary_rows"]})
        self.assertEqual(sample["row_count"], 47)
        self.assertEqual(sample["louvain_trials"], 9400)
        self.assertEqual(len(sample["reserve_rows_not_authorized"]), 40)
        self.assertFalse(sample["expansion_rule"]["automatic_expansion"])

    def test_cache_hit_subset_isolation_and_Q_exact_legacy_parity(self):
        cache = RawWindowCache(2 * 1024**2)
        first = row_processor(self.source, self.selected, cache)(self.rows[0])
        second = row_processor(self.source, self.selected, cache)(self.rows[1])
        self.assertFalse(first["cache"]["hit"])
        self.assertTrue(second["cache"]["hit"])
        self.assertLessEqual(cache.retained_bytes, cache.max_bytes)
        self.assertFalse(cache.entry[2].flags.writeable)
        self.assertEqual(first["zero_variance"]["zero_variance_neuron_ids"], [0])
        self.assertEqual(second["zero_variance"]["zero_variance_neuron_ids"], [])
        for row, result in zip(self.rows, (first, second), strict=True):
            selected = self.selected[row["graph_id"]]
            with np.errstate(invalid="ignore", divide="ignore"):
                correlation, _, _ = identity.read_source_abs_correlation(self.source, selected, "wake", 0)
            graph = identity.build_candidate_graph(correlation)
            edges = sorted(tuple(sorted((selected[u], selected[v]))) for u, v in graph.edges)
            reference = canonical_louvain_q_vector(selected, edges, list(range(700, 900)))
            self.assertEqual(result["canonical"], reference)
            runner.validate_result(result, row)
            self.assertTrue(all(v["wall_seconds"] >= 0 for v in result["phases"].values()))
        self.assertEqual(first["zero_variance"]["raw_nonfinite_values"], 0)

    def test_cache_state_frame_source_invalidation_and_cap(self):
        cache = RawWindowCache(2 * 1024**2)
        args = {"source_sha": self.rows[0]["source_file_sha256"], "state": "wake", "window": 0,
                "frame_sha": self.rows[0]["source_frame_indices_sha256"]}
        cache.get(self.source, **args)
        cache.get(self.source, **{**args, "window": 1, "frame_sha": identity.hash_int64(range(1500, 3000))})
        self.assertEqual(cache.evictions, 1)
        _, status = cache.get(self.source, **{**args, "state": "NREM",
                                              "frame_sha": identity.hash_int64(range(2999, 1499, -1))})
        self.assertFalse(status["hit"])
        with self.assertRaisesRegex(identity.IdentityEvidenceError, "frame identity"):
            cache.get(self.source, **{**args, "frame_sha": "0" * 64})
        with self.assertRaisesRegex(MeasurementError, "byte cap"):
            RawWindowCache(16).get(self.source, **args)
        cache.get(self.source, **args)
        with self.source.open("ab") as handle:
            handle.write(b"test-source-mutation")
        with self.assertRaisesRegex(identity.IdentityEvidenceError, "Source changed"):
            cache.get(self.source, **args)
        link = self.root / "alias.mat"
        link.symlink_to(self.source)
        with self.assertRaises(identity.IdentityEvidenceError):
            cache.get(link, **args)

    def make_auth(self, head=None, run_id=None):
        head = head or "a" * 40
        run_id = run_id or str(uuid.uuid4())
        run_dir = self.root / "production-parent" / run_id
        line = runner.confirmation_text(head, run_id)
        auth = {"schema": "SRT_OBSERVED_CALIBRATION_RESEARCHER_AUTHORIZATION_V1",
                "status": "APPROVED_FOR_SINGLE_RUN", "binding": runner.bindings(head, run_id, run_dir),
                "researcher_confirmation": line, "researcher_confirmed_risks": True,
                "no_automatic_retry": True, "resource_approval_record": "SYNTHETIC_TEST_ONLY_NEVER_A_REAL_APPROVAL",
                "researcher_identity": "synthetic-test", "confirmed_at_utc": "2026-10-26T00:00:00Z"}
        path = self.root / "synthetic-authorization.json"
        path.write_bytes(canonical(auth))
        return path, auth, {"head": head, "run_id": run_id, "run_dir": run_dir, "confirmation": line}

    def test_authorization_positive_and_all_bindings_negative(self):
        path, _auth, args = self.make_auth()
        auth = _auth
        runner.validate_authorization(path, **args)
        for field in auth["binding"]:
            broken = copy.deepcopy(auth)
            broken["binding"][field] = "tampered"
            path.write_bytes(canonical(broken))
            with self.subTest(field=field), self.assertRaises(ValueError):
                runner.validate_authorization(path, **args)
        for field, value in auth["binding"]["resource_limits"].items():
            broken = copy.deepcopy(auth)
            broken["binding"]["resource_limits"][field] = value + 1 if type(value) is int else value + "-changed"
            path.write_bytes(canonical(broken))
            with self.subTest(resource=field), self.assertRaises(ValueError):
                runner.validate_authorization(path, **args)
        path.write_bytes(canonical({**auth, "status": "PENDING_RESEARCHER_APPROVAL"}))
        with self.assertRaises(ValueError):
            runner.validate_authorization(path, **args)
        with self.assertRaises((OSError, pilot.H3PilotError)):
            runner.validate_authorization(self.root / "missing.json", **args)
        path.write_bytes(canonical(runner.authorization_draft(args["head"], args["run_id"], args["run_dir"])))
        with self.assertRaises(ValueError):
            runner.validate_authorization(path, **args)

    def test_output_is_new_and_cannot_escape_or_follow_symlinks(self):
        psa = self.root / "psa"
        psa.mkdir()
        run_id = str(uuid.uuid4())
        target = psa / runner.OUTPUT_PARENT / run_id
        self.assertEqual(runner.checked_output(target, psa, run_id)[0], target)
        self.assertFalse(target.parent.exists())
        for wrong in (psa / "other" / run_id, psa / runner.OUTPUT_PARENT / ".." / run_id):
            with self.assertRaises(ValueError):
                runner.checked_output(wrong, psa, run_id)
        target.parent.symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(ValueError):
            runner.checked_output(target, psa, run_id)

    def test_production_preflight_positive_and_resource_refusal_create_no_run(self):
        phase2, psa, state = (self.root / name for name in ("phase2", "psa", "state"))
        phase2.mkdir()
        psa.mkdir()
        run_id = str(uuid.uuid4())
        target = psa / runner.OUTPUT_PARENT / run_id
        with patch.object(pilot, "_git_identity", return_value={"head_sha": "a" * 40, "working_tree": "CLEAN"}), \
             patch.object(identity, "h3_runtime_manifest", return_value={"replay_environment_matches_recorded_versions_and_candidate_lock": True}), \
             patch.object(runner, "validate_private_identities", return_value=(phase2, psa, {})), \
             patch.object(runner, "validate_internal_apfs", return_value={"filesystem": "apfs"}), \
             patch.object(pilot, "default_host_state_dir", return_value=state), \
             patch.object(watchdog, "_default_activity_lock_path", return_value=state / "global.lock"), \
             patch.object(pilot, "_preflight_macos_resources", return_value={"checked": True}) as live:
            kwargs = {"head": "a" * 40, "run_id": run_id, "run_dir": target, "phase2": phase2, "psa": psa}
            self.assertEqual(runner.preflight(**kwargs)["status"], "PREFLIGHT_PASSED_NOT_AUTHORIZED")
            limits = live.call_args.args[0]
            self.assertEqual(limits.memory_enforcement_backend, "MACOS_SAMPLED_PRESSURE")
            self.assertTrue(limits.require_sleep_assertion)
            self.assertEqual(limits.max_workers, 1)
            live.side_effect = pilot.H3PilotError("injected Data/VM/Swap/thermal refusal")
            with self.assertRaises(pilot.H3PilotError):
                runner.preflight(**kwargs)
        self.assertFalse(target.parent.exists())
        self.assertFalse(state.exists())

    @unittest.skipUnless(sys.platform == "darwin", "native internal APFS path check")
    def test_actual_mac_Data_volume_check_uses_mount_point_not_private_directory(self):
        self.assertTrue(runner.validate_internal_apfs(self.root)["same_Data_volume_device"])

    def test_complete_Q_vector_and_graph_metadata_tampering_is_scientific_failure(self):
        row = self.rows[0]
        result = row_processor(self.source, self.selected, RawWindowCache(2 * 1024**2))(row)
        for mutate in (lambda r: r["canonical"]["q_values"].__setitem__(0, float("nan")),
                       lambda r: r["source_graph_identity"].__setitem__("E", 3),
                       lambda r: r["louvain_seeds"].__setitem__(0, 1)):
            altered = copy.deepcopy(result)
            mutate(altered)
            with self.assertRaises(identity.IdentityEvidenceError):
                runner.validate_result(altered, row)

    def test_public_closure_contains_counts_and_hashes_not_private_signal_or_Q(self):
        path = MODULE_DIR / "H3_120_PUBLIC_CLOSURE_2026-10-26.json"
        text = path.read_text()
        self.assertNotIn("/Users/", text)
        self.assertNotIn('"q_values"', text)
        self.assertNotIn('"original_neuron_ids"', text)
        data = json.loads(text)
        self.assertEqual(data["source_identity_pass"], 120)
        self.assertEqual(data["historical_trial_max_abs_delta"], 0)
        self.assertEqual(data["constant_signal_audit"]["unique_neuron_window_combinations"], 859)
        self.assertEqual(len(data["row_artifact_hashes"]), 120)

    @unittest.skipUnless(os.environ.get("SRT_TEST_HISTORICAL_BUILDER"), "optional hash-pinned historical code; no private signals")
    def test_actual_historical_builder_timing_wrapper_on_synthetic_data(self):
        path = Path(os.environ["SRT_TEST_HISTORICAL_BUILDER"])
        row = self.rows[0]
        measured = measure_row(row, source_path=self.source, selected=self.selected[row["graph_id"]],
                               seeds=list(range(700, 900)), cache=RawWindowCache(2 * 1024**2),
                               builder_factory=lambda: identity._historical_connected_graph(path))
        self.assertEqual(measured["source_graph_identity"]["historical_function_sha256"],
                         identity.EXPECTED_HISTORICAL_GRAPH_FUNCTION_SHA256)
        reference = row_processor(self.source, self.selected, RawWindowCache(2 * 1024**2))(row)
        self.assertEqual(measured["canonical"], reference["canonical"])

    def test_production_launch_interface_and_child_identity_dispatch(self):
        path, _auth, args = self.make_auth()
        check = {"preflight_wall_seconds": 1., "preflight_process_cpu_seconds": 0.1,
                 "run_parent": str(args["run_dir"].parent), "phase2": str(self.root),
                 "psa": str(self.root), "head": {"head_sha": args["head"]}}
        with patch.object(runner, "preflight", return_value=check), \
             patch.object(pilot, "_launch_supervised", return_value={"dispatched": True}) as launch:
            self.assertTrue(runner.launch(**args, authorization=path, phase2=self.root, psa=self.root)["dispatched"])
        kwargs = launch.call_args.kwargs
        self.assertEqual(kwargs["limits"].max_workers, 1)
        self.assertEqual(kwargs["limits"].wall_seconds, runner.RESOURCE_CANDIDATE["wall_seconds"] - 1)
        self.assertEqual(kwargs["env_extra"]["SRT_OBS_AUTH_PATH"], str(path))
        with patch.object(Path, "cwd", return_value=args["run_dir"]), \
             patch.dict(os.environ, {"NC0A_WATCHDOG_PARENT_PID": "123", "SRT_OBS_AUTH_PATH": str(path),
                                     "SRT_OBS_AUTH_SHA256": identity.sha256_file(path),
                                     "SRT_OBS_CONFIRMATION": args["confirmation"],
                                     "SRT_PHASE2_ROOT": str(self.root), "SRT_PSA_ROOT": str(self.root)}), \
             patch.object(runner, "guard_watchdog_parent"), patch.object(pilot, "_write_runner_lease"), \
             patch.object(pilot, "_git_identity"), patch.object(runner, "validate_sample", return_value=({"primary_rows": self.rows}, {})), \
             patch.object(runner, "validate_private_identities", return_value=(self.root, self.root, {})), \
             patch.object(identity, "h3_runtime_manifest", return_value={"replay_environment_matches_recorded_versions_and_candidate_lock": True}), \
             patch.object(runner, "execute_rows", return_value={"status": "completed"}) as dispatch:
            self.assertEqual(runner._runner_child(), 0)
        self.assertEqual(dispatch.call_args.args[0], self.rows)
        # No signal processing is reachable from the mocked dispatch/admission test.
        self.assertFalse(args["run_dir"].exists())

    def test_real_watchdog_success_then_verified_and_no_overwrite(self):
        run, state, summary = self.run_supervised()
        self.assertEqual(summary["status"], "COMPLETED")
        audit = runner.verify_run(run, state_dir=state)
        self.assertTrue(audit["completed"])
        self.assertTrue(audit["synthetic_test_only"])
        self.assertEqual(audit["rows_verified"], 2)
        self.assertFalse(audit["resume_allowed"])
        with self.assertRaisesRegex(pilot.H3PilotError, "recorded attempt"):
            pilot._assert_host_ledger_allows(pilot._verified_host_events(state / pilot._HOST_LEDGER),
                                             summary["pilot_sha256"])
        with self.assertRaises(FileExistsError):
            runner.execute_rows(self.rows, run_dir=run, process_row=lambda r: {})
        artifact = run / runner.ROW_DIR / "001.json"
        artifact.write_bytes(artifact.read_bytes() + b" ")
        with self.assertRaisesRegex(ValueError, "artifact"):
            runner.verify_run(run, state_dir=state)

    def test_failures_never_retry_or_succeed_and_preserve_accounting(self):
        for scenario, category in (("scientific_failure", "SCIENTIFIC_INTEGRITY"), ("io_failure", "OPERATIONAL_IO")):
            with self.subTest(scenario=scenario):
                run, state, summary = self.run_supervised(scenario)
                self.assertNotEqual(summary["status"], "COMPLETED")
                self.assertEqual(summary["runner"]["failure_category"], category)
                self.assertEqual(summary["runner"]["rows_completed"], 0)
                self.assertGreater(summary["watchdog"]["usage"]["cpu_seconds"], 0)
                self.assertFalse(runner.verify_run(run, state_dir=state)["resume_allowed"])

    def test_watchdog_wall_cpu_rss_and_output_stops(self):
        for override in ({"wall_seconds": 0.25}, {"cpu_seconds": 0.02},
                         {"aggregate_rss_bytes": 65536}, {"run_disk_bytes": 8192}):
            with self.subTest(override=override):
                run, _, summary = self.run_supervised("slow", **override)
                self.assertEqual(summary["status"], "STOPPED_BY_WATCHDOG")
                self.assertFalse(summary["resume_allowed"])
                lease = pilot._read_json(run / pilot._LEASE)
                self.assertEqual(lease["state"], "TERMINAL")

    def test_child_exit_and_audit_suffix_loss_fail_closed(self):
        run, state, summary = self.run_supervised("child_exit")
        self.assertNotEqual(summary["status"], "COMPLETED")
        with self.assertRaises((OSError, ValueError, watchdog.WatchdogError)):
            runner.verify_run(run, state_dir=state)
        run, state, _ = self.run_supervised()
        evidence = run / runner.EVIDENCE
        lines = evidence.read_bytes().splitlines(keepends=True)
        evidence.write_bytes(b"".join(lines[:-1]))
        with self.assertRaisesRegex(ValueError, "suffix|anchor"):
            runner.verify_run(run, state_dir=state)

    def test_unknown_failure_and_held_host_lock_refuse_automatic_recovery(self):
        run = self.root / "unknown-run"
        run.mkdir()
        def unknown(_row, **_kwargs):
            raise RuntimeError("unknown injected failure")
        terminal = runner.execute_rows(self.rows, run_dir=run, process_row=unknown, synthetic=True)
        self.assertEqual(terminal["failure_category"], "UNKNOWN_FAIL_STOP")
        self.assertFalse(terminal["resume_allowed"])
        state = self.root / "locked-state"
        with patch.object(watchdog, "_default_activity_lock_path", return_value=state / "global.lock"), \
             watchdog.supervised_activity_lock(), self.assertRaisesRegex(pilot.H3PilotError, "host lock"), \
             pilot._host_lock(state):
            self.fail("second activity admitted")

    def test_result_writer_failure_is_persisted_without_success_or_replacement(self):
        run = self.root / "writer-fault"
        run.mkdir()
        with patch.object(runner, "write_result_payload", side_effect=OSError("injected fsync/write error")):
            terminal = runner.execute_rows(self.rows, run_dir=run, synthetic=True,
                                           process_row=row_processor(self.source, self.selected, RawWindowCache(2 * 1024**2)))
        self.assertEqual(terminal["failure_category"], "OPERATIONAL_IO")
        self.assertEqual(terminal["rows_completed"], 0)
        self.assertFalse(terminal["resume_allowed"])
        events = [json.loads(line)["event"] for line in (run / runner.EVIDENCE).read_text().splitlines()]
        self.assertEqual(events[-1]["kind"], "calibration_failed")
        self.assertTrue(any(e["kind"] == "phase_measured" for e in events))
        self.assertFalse(any(e["kind"] == "graph_result" for e in events))

    def test_native_counters_are_bytes_not_block_operation_aliases(self):
        result = process_counters()
        self.assertIn("process-attributed bytes", result["native_io_semantics"])
        self.assertGreater(result["current_process_rss_bytes"], 0)
        self.assertGreaterEqual(result["read_bytes"], 0)


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--synthetic-worker":
        raise SystemExit(supervised_child(Path(sys.argv[2])))
    unittest.main()
