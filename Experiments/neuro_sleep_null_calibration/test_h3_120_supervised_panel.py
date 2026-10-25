from __future__ import annotations

import json
import sys
import tempfile
import unittest
import uuid
from pathlib import Path
from unittest.mock import patch

MODULE_DIR = Path(__file__).resolve().parent
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

import h3_120_supervised_panel as h3_120
from g0_q_protocol import (
    CANONICAL_ORDER_POLICY,
    first_maximum_index,
    q_vector_sha256,
)
from h3_supervised_pilot import _verify_recovery_directory
from riken_source_identity import (
    EXPECTED_RECORDINGS,
    LOUVAIN_TRIALS,
    TARGETS,
    h3_runtime_manifest,
    replay_louvain_q,
)


class TestH3Supervised120Panel(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="h3-120-synthetic-")
        self.root = Path(self.temp.name).resolve()
        self.packet_path = MODULE_DIR / h3_120.PACKET_FILENAME
        self.manifest_path = MODULE_DIR / h3_120.MANIFEST_FILENAME

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _packet(self):
        return h3_120.validate_h3_120_packet(self.packet_path, self.manifest_path)

    @staticmethod
    def _fake_result(row: dict) -> dict:
        runtime = h3_runtime_manifest()
        runtime_sha = h3_120._runtime_hash(runtime)
        implementation_sha = h3_120._implementation_hash()
        historical = [0.2] * LOUVAIN_TRIALS
        canonical = [0.25] * LOUVAIN_TRIALS
        hist_order = "synthetic-historical-order-hash"
        canonical_order = "synthetic-canonical-order-hash"
        labels_hash = "synthetic-labeled-edge-set-hash"
        topology_hash = "synthetic-topology-hash"
        base_identity = {
            "graph_id": row["graph_id"],
            "source_artifact_sha256": row["source_artifact_sha256"],
            "selected_neuron_indices_sha256": row[
                "selected_neuron_indices_sha256"],
            "expected_node_order_sha256": row["expected_node_order_sha256"],
            "source_frame_indices_sha256": row["source_frame_indices_sha256"],
            "historical_job_sha256": row["historical_job_sha256"],
            "historical_q_vector_sha256": row["historical_q_vector_sha256"],
            "labeled_edge_set_sha256": labels_hash,
            "topology_sha256": topology_hash,
            "seed_vector_sha256": row[
                "historical_louvain_seed_vector_sha256"],
            "runtime_manifest_sha256": runtime_sha,
            "implementation_sha256": implementation_sha,
        }
        hist_identity = {**base_identity,
                         "order_policy": h3_120.HISTORICAL_ORDER_POLICY,
                         "ordered_representation_sha256": hist_order}
        canonical_identity = {**base_identity,
                              "order_policy": CANONICAL_ORDER_POLICY,
                              "ordered_representation_sha256": canonical_order}
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
            "selected_neuron_indices_sha256": row[
                "selected_neuron_indices_sha256"],
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
            "labeled_edge_set_sha256": labels_hash,
            "historical_q_vector": historical,
            "historical_q_vector_sha256": q_vector_sha256(historical),
            "historical_qmax": max(historical),
            "historical_first_max_trial_index": 0,
            "canonical_q_vector": canonical,
            "canonical_q_vector_sha256": q_vector_sha256(canonical),
            "canonical_qmax": max(canonical),
            "canonical_first_max_trial_index": 0,
            "historical_cache_identity": hist_identity,
            "canonical_cache_identity": canonical_identity,
            "historical_cache_reused": False,
            "canonical_cache_reused": False,
        }

    def test_fixed_packet_hash_order_and_coverage(self) -> None:
        packet, manifest = self._packet()
        self.assertEqual(packet["row_count"], 120)
        self.assertEqual(len(packet["rows"]), 120)
        self.assertEqual(manifest["h3_panel"]["count"], 120)
        self.assertEqual(tuple(dict.fromkeys(r["recording_id"] for r in packet["rows"])),
                         EXPECTED_RECORDINGS)
        self.assertEqual({n: sum(r["N"] == n for r in packet["rows"])
                          for n in TARGETS}, {n: 12 for n in TARGETS})
        self.assertEqual(sum(r["state"] == "wake" for r in packet["rows"]), 60)
        self.assertEqual(sum(r["state"] == "NREM" for r in packet["rows"]), 60)
        self.assertEqual(h3_120.planned_louvain_trials(packet["rows"]), {
            "gross_trials": 48_000,
            "historical_pilot_trials_credited": 0,
            "planned_new_trials": 48_000,
            "reuse_status": "NOT_ESTABLISHED_NO_COMPLETE_Q_VECTOR_ARTIFACT",
        })
        self.assertFalse(packet["candidate_cache_credit"][
            "legacy_sorted_edge_diagnostic_is_canonical_cache"])
        self.assertEqual(packet["candidate_cache_credit"][
            "current_10_graph_pilot_credit"], "NOT_ESTABLISHED")

    def test_method_draft_and_missing_authorization_fail_closed(self) -> None:
        effective, reason = h3_120._method_is_effective(MODULE_DIR / h3_120.METHOD_FILENAME)
        self.assertFalse(effective)
        self.assertIn("DRAFT", reason)
        spoofed_status = self.root / "spoofed-method-status.md"
        spoofed_status.write_text(
            "---\nstatus: draft\nnote: prior status: active\n---\n",
            encoding="utf-8")
        self.assertFalse(h3_120._method_is_effective(spoofed_status)[0])
        auth = self.root / "approval.json"
        auth.write_text("{}", encoding="utf-8")
        run_id = str(uuid.uuid4())
        confirmation = (f"I AUTHORIZE H3-120 {run_id} "
                        f"{h3_120.EXPECTED_PACKET_SHA256} synthetic-head")
        with self.assertRaisesRegex(h3_120.H3PanelError, "DRAFT"):
            h3_120.validate_researcher_authorization(
                auth, packet_sha256=h3_120.EXPECTED_PACKET_SHA256,
                method_path=MODULE_DIR / h3_120.METHOD_FILENAME,
                expected_head="synthetic-head", run_id=run_id,
                confirmation=confirmation)

    def test_researcher_authorization_accepts_exact_binding_and_rejects_mismatches(self) -> None:
        method_path = self.root / "method-amendment.md"
        method_path.write_text(
            "---\nstatus: active\n---\n# Synthetic effective method\n",
            encoding="utf-8")
        method_sha = h3_120.sha256_file(method_path)
        run_id = str(uuid.uuid4())
        expected_head = "a" * 40
        approval = {
            "schema": "SRT_H3_120_RESEARCHER_AUTHORIZATION_V1",
            "status": "APPROVED_FOR_EXECUTION",
            "method_amendment_status": "EFFECTIVE",
            "method_amendment_sha256": method_sha,
            "packet_sha256": h3_120.EXPECTED_PACKET_SHA256,
            "head_sha": expected_head,
            "run_uuid": run_id,
            "resource_limits": dict(h3_120.MINIMAL_CANDIDATE_LIMITS),
            "max_compute_workers": 1,
            "memory_semantics": "SAMPLED_RSS_NOT_A_HARD_LIMIT",
        }
        authorization_path = self.root / "authorization.json"
        authorization_path.write_text(json.dumps(approval), encoding="utf-8")
        confirmation = (f"I AUTHORIZE H3-120 {run_id} "
                        f"{h3_120.EXPECTED_PACKET_SHA256} {expected_head}")

        accepted = h3_120.validate_researcher_authorization(
            authorization_path, packet_sha256=h3_120.EXPECTED_PACKET_SHA256,
            method_path=method_path, expected_head=expected_head,
            run_id=run_id, confirmation=confirmation)
        self.assertEqual(accepted["status"], "APPROVED_FOR_EXECUTION")
        self.assertEqual(accepted["method_amendment_sha256"], method_sha)
        self.assertEqual(accepted["authorization_sha256"],
                         h3_120.sha256_file(authorization_path))

        mutations = {
            "schema": lambda item: item.update(schema="WRONG_SCHEMA"),
            "status": lambda item: item.update(status="DRAFT"),
            "method state": lambda item: item.update(method_amendment_status="DRAFT"),
            "method hash": lambda item: item.update(method_amendment_sha256="0" * 64),
            "packet hash": lambda item: item.update(packet_sha256="0" * 64),
            "HEAD": lambda item: item.update(head_sha="b" * 40),
            "UUID": lambda item: item.update(run_uuid=str(uuid.uuid4())),
            "worker ceiling": lambda item: item.update(max_compute_workers=2),
            "memory semantics": lambda item: item.update(memory_semantics="HARD_LIMIT"),
        }
        for name, mutate in mutations.items():
            with self.subTest(mismatch=name):
                altered = json.loads(json.dumps(approval))
                mutate(altered)
                authorization_path.write_text(json.dumps(altered), encoding="utf-8")
                with self.assertRaises(h3_120.H3PanelError):
                    h3_120.validate_researcher_authorization(
                        authorization_path,
                        packet_sha256=h3_120.EXPECTED_PACKET_SHA256,
                        method_path=method_path, expected_head=expected_head,
                        run_id=run_id, confirmation=confirmation)

        for name in h3_120.MINIMAL_CANDIDATE_LIMITS:
            with self.subTest(mismatched_budget=name):
                altered = json.loads(json.dumps(approval))
                altered["resource_limits"][name] = "MISMATCH"
                authorization_path.write_text(json.dumps(altered), encoding="utf-8")
                with self.assertRaises(h3_120.H3PanelError):
                    h3_120.validate_researcher_authorization(
                        authorization_path,
                        packet_sha256=h3_120.EXPECTED_PACKET_SHA256,
                        method_path=method_path, expected_head=expected_head,
                        run_id=run_id, confirmation=confirmation)

        authorization_path.write_text(json.dumps(approval), encoding="utf-8")
        with self.assertRaisesRegex(h3_120.H3PanelError, "confirmation"):
            h3_120.validate_researcher_authorization(
                authorization_path, packet_sha256=h3_120.EXPECTED_PACKET_SHA256,
                method_path=method_path, expected_head=expected_head,
                run_id=run_id, confirmation="wrong confirmation")
        method_path.write_text(method_path.read_text(encoding="utf-8") + "\n",
                               encoding="utf-8")
        with self.assertRaisesRegex(h3_120.H3PanelError, "does not bind"):
            h3_120.validate_researcher_authorization(
                authorization_path, packet_sha256=h3_120.EXPECTED_PACKET_SHA256,
                method_path=method_path, expected_head=expected_head,
                run_id=run_id, confirmation=confirmation)

    def test_production_launcher_binds_accepted_authorization_to_watchdog_run(self) -> None:
        self._packet()
        state_dir = self.root / "host-state"
        phase2_root = self.root / "phase2"
        psa_root = self.root / "psa"
        run_id = str(uuid.uuid4())
        run_dir = psa_root / "h3_identity_calibration_120_2026-10-24" / run_id
        expected_parent = run_dir.parent
        head_sha = "c" * 40
        authorization_evidence = {
            "authorization_sha256": "1" * 64,
            "method_amendment_sha256": "2" * 64,
            "status": "APPROVED_FOR_EXECUTION",
        }
        captured = {}

        def capture_launch(command, **kwargs):
            captured["command"] = command
            captured.update(kwargs)
            return {"status": "COMPLETED"}

        with (
            patch.object(h3_120, "validate_researcher_authorization",
                         return_value=authorization_evidence),
            patch.object(h3_120.pilot, "default_host_state_dir", return_value=state_dir),
            patch.object(h3_120.pilot, "_git_identity",
                         return_value={"head_sha": head_sha, "working_tree": "CLEAN"}),
            patch.object(h3_120, "validate_h3_120_private_roots",
                         return_value=(phase2_root, psa_root)),
            patch.object(h3_120.pilot, "_preflight_macos_resources",
                         return_value={"synthetic_preflight": "PASS"}),
            patch.object(h3_120, "_prepare_output_directory",
                         return_value=(run_dir, expected_parent)),
            patch.object(h3_120.pilot, "_launch_supervised", side_effect=capture_launch),
        ):
            launched = h3_120.launch_real_h3_120(
                packet_path=self.packet_path, manifest_path=self.manifest_path,
                phase2_root=phase2_root, psa_root=psa_root, run_dir=run_dir,
                state_dir=state_dir, run_id=run_id, expected_head=head_sha,
                authorization_path=self.root / "unused-auth.json",
                researcher_confirmation="synthetic UUID/packet/HEAD confirmation")

        self.assertEqual(launched["status"], "COMPLETED")
        self.assertIn("--runner-child", captured["command"])
        self.assertEqual(captured["run_id"], run_id)
        self.assertEqual(captured["head"]["head_sha"], head_sha)
        self.assertEqual(captured["candidate"]["researcher_authorization"],
                         authorization_evidence)
        self.assertEqual(captured["candidate"]["panel_rows"], 120)
        self.assertEqual(captured["candidate"]["louvain_trials_gross"], 48_000)
        self.assertEqual(captured["limits"].max_workers, 1)
        self.assertEqual(captured["limits"].memory_enforcement_backend,
                         "MACOS_SAMPLED_PRESSURE")

    def test_production_candidate_maps_to_macos_sampled_pressure_without_activation(self) -> None:
        limits = h3_120._candidate_watchdog_limits()
        self.assertEqual(limits.memory_enforcement_backend, "MACOS_SAMPLED_PRESSURE")
        self.assertEqual(limits.max_workers, 1)
        self.assertEqual(limits.wall_seconds, 8 * 60 * 60)
        self.assertEqual(limits.cpu_seconds, 8 * 60 * 60)
        self.assertEqual(limits.aggregate_rss_bytes, 4 * 1024**3)
        self.assertEqual(limits.run_disk_bytes, 1 * 1024**3)
        self.assertEqual(limits.minimum_boot_free_disk_bytes, 40 * 1024**3)
        self.assertEqual(limits.boot_reserve_free_disk_bytes, 30 * 1024**3)
        self.assertEqual(limits.swap_growth_stop_bytes, 2 * 1024**3)
        self.assertFalse(h3_120._method_is_effective(
            MODULE_DIR / h3_120.METHOD_FILENAME)[0])

    def test_historical_failure_does_not_call_canonical_replay(self) -> None:
        import networkx as nx

        graph = nx.cycle_graph(8)
        seeds = tuple(range(1, LOUVAIN_TRIALS + 1))
        reference = [0.1] * LOUVAIN_TRIALS
        calls = []

        def bad_history(*_args, **_kwargs):
            return {"q_values": [0.2, *([0.1] * (LOUVAIN_TRIALS - 1))]}

        def canonical(*_args, **_kwargs):
            calls.append("canonical")
            return {"q_values": [0.3] * LOUVAIN_TRIALS}

        with self.assertRaisesRegex(h3_120.H3PanelError, "HISTORICAL_Q_INTEGRITY_FAILURE"):
            h3_120.compute_dual_order_q(
                historical_graph=graph, source_ids=tuple(range(8)), seeds=seeds,
                reference_q=reference, reference_qmax_first_index=0,
                reference_qmax=0.1, historical_replay=bad_history,
                canonical_replay=canonical)
        self.assertEqual(calls, [])

    def test_qmax_reference_uses_declared_absolute_tolerance(self) -> None:
        import networkx as nx

        graph = nx.cycle_graph(8)
        seeds = tuple(range(1, LOUVAIN_TRIALS + 1))
        reference = [0.4, *([0.1] * (LOUVAIN_TRIALS - 1))]
        stored_qmax = reference[0] + 5e-7
        canonical_calls = []
        result = h3_120.compute_dual_order_q(
            historical_graph=graph, source_ids=tuple(range(8)), seeds=seeds,
            reference_q=reference, reference_qmax_first_index=0,
            reference_qmax=stored_qmax,
            historical_replay=lambda *_args, **_kwargs: {"q_values": reference},
            canonical_replay=lambda *_args, **_kwargs: (
                canonical_calls.append(True) or {"q_values": reference}))
        self.assertEqual(result["historical_order_q_replay"], "PASS")
        self.assertAlmostEqual(
            result["historical_reference_qmax_abs_delta"], 5e-7, places=12)
        self.assertEqual(canonical_calls, [True])
        canonical_calls.clear()
        with self.assertRaisesRegex(
                h3_120.H3PanelError, "HISTORICAL_Q_INTEGRITY_FAILURE"):
            h3_120.compute_dual_order_q(
                historical_graph=graph, source_ids=tuple(range(8)), seeds=seeds,
                reference_q=reference, reference_qmax_first_index=0,
                reference_qmax=reference[0] + 2e-6,
                historical_replay=lambda *_args, **_kwargs: {"q_values": reference},
                canonical_replay=lambda *_args, **_kwargs:
                    canonical_calls.append(True) or {"q_values": reference})
        self.assertEqual(canonical_calls, [])

    def test_synthetic_graph_dual_200_q_replay_and_runtime(self) -> None:
        import platform

        import networkx as nx

        runtime = h3_runtime_manifest()
        is_target_runtime = (sys.version_info[:3] == (3, 14, 0) and
                             platform.machine() == "arm64")
        if is_target_runtime:
            self.assertEqual(runtime["actual"], {
                "h5py": "3.16.0", "networkx": "3.6.1", "numpy": "2.5.3",
                "python-louvain": "0.16", "scipy": "1.18.1"})
            self.assertTrue(
                runtime["replay_environment_matches_recorded_versions_and_candidate_lock"])
        else:
            # Portable CI may exercise the synthetic logic on another runner,
            # but it must never report that environment as the target replay.
            self.assertFalse(
                runtime["replay_environment_matches_recorded_versions_and_candidate_lock"])

        graph = nx.Graph()
        graph.add_nodes_from(range(16))
        graph.add_edges_from((i, (i + 1) % 16) for i in range(16))
        graph.add_edges_from((i, (i + 4) % 16) for i in range(16))
        seeds = tuple(range(1, LOUVAIN_TRIALS + 1))
        reference = replay_louvain_q(
            graph, seeds, require_target=is_target_runtime)["q_values"]
        result = h3_120.compute_dual_order_q(
            historical_graph=graph, source_ids=tuple(range(16)), seeds=seeds,
            reference_q=reference,
            reference_qmax_first_index=first_maximum_index(reference),
            reference_qmax=max(reference),
            historical_replay=lambda g, seed_values, **_: replay_louvain_q(
                g, seed_values, require_target=is_target_runtime))
        self.assertEqual(result["historical_order_q_replay"], "PASS")
        self.assertEqual(result["historical_reference_max_abs_delta"], 0.0)
        self.assertEqual(len(result["historical_q_vector"]), 200)
        self.assertEqual(len(result["canonical_q_vector"]), 200)
        self.assertEqual(result["canonical_order_policy"], CANONICAL_ORDER_POLICY)
        self.assertEqual(result["canonical_vs_historical_status"],
                         "DIAGNOSTIC_ONLY_NO_PASS_THRESHOLD")

    def test_all_120_rows_ordered_and_hash_verifiable_with_virtual_q(self) -> None:
        packet, _ = self._packet()
        rows = packet["rows"]
        run_dir = self.root / "run"
        run_dir.mkdir()
        seen = []

        def process(row):
            seen.append(row["graph_id"])
            return self._fake_result(row)

        result = h3_120.execute_ordered_panel(
            rows, run_dir=run_dir, process_row=process, synthetic_test_only=True)
        self.assertEqual(result["status"], "completed")
        self.assertEqual(seen, [row["graph_id"] for row in rows])
        self.assertEqual(len(list((run_dir / h3_120.ROW_DIR).glob("*.json"))), 120)
        verified = h3_120.verify_h3_120_run(run_dir)
        # Artifact verification alone is not a completed supervised run: the
        # Watchdog summary and host activity ledger are required as well.
        self.assertFalse(verified["completed_120_row_panel"])
        self.assertTrue(verified["synthetic_test_only"])
        self.assertEqual(verified["result_artifacts_verified"], 120)
        self.assertFalse(verified["resume_allowed"])

    def test_full_120_virtual_panel_through_shared_watchdog_and_host_ledger(self) -> None:
        run_dir = self.root / "watchdog-full-panel-mock"
        state_dir = self.root / "state-full-panel-mock"
        supervised = h3_120.launch_synthetic_watchdog_test(
            run_dir=run_dir, state_dir=state_dir, scenario="full_panel_mock")
        self.assertEqual(supervised["status"], "COMPLETED")
        self.assertIsNone(supervised["failure_category"])
        verified = h3_120.verify_h3_120_run(
            run_dir, host_state_dir=state_dir)
        self.assertTrue(verified["completed"])
        self.assertFalse(verified["completed_120_row_panel"])
        self.assertTrue(verified["synthetic_test_only"])
        self.assertEqual(verified["result_rows_seen"], 120)
        self.assertEqual(verified["result_artifacts_verified"], 120)
        events = [json.loads(line)["event"] for line in
                  (run_dir / h3_120.EVIDENCE_LOG).read_text().splitlines()]
        graph_results = [event for event in events if event.get("kind") == "graph_result"]
        self.assertEqual(len(graph_results), 120)
        self.assertEqual(sum(event["louvain_trials_computed"]
                             for event in graph_results), 48_000)
        self.assertTrue(all(event["louvain_trials_computed"] == 400
                            for event in graph_results))
        artifact = run_dir / graph_results[0]["result_artifact"]
        artifact.write_bytes(artifact.read_bytes() + b" ")
        with self.assertRaisesRegex(h3_120.H3PanelError, "hash changed"):
            h3_120.verify_h3_120_run(run_dir, host_state_dir=state_dir)

    def test_first_failed_row_stops_without_executing_or_reusing_later_rows(self) -> None:
        packet, _ = self._packet()
        rows = packet["rows"]
        run_dir = self.root / "failed-run"
        run_dir.mkdir()
        calls = []

        def fail(row):
            calls.append(row["graph_id"])
            raise h3_120.H3PanelError("HISTORICAL_Q_INTEGRITY_FAILURE")

        result = h3_120.execute_ordered_panel(rows, run_dir=run_dir, process_row=fail)
        self.assertEqual(result["status"], "scientific_integrity_failure")
        self.assertEqual(calls, [rows[0]["graph_id"]])
        terminal = json.loads((run_dir / "runner-terminal.json").read_text())
        self.assertFalse(terminal["resume_allowed"])
        verified = h3_120.verify_h3_120_run(run_dir)
        self.assertFalse(verified["completed_120_row_panel"])
        self.assertEqual(verified["result_rows_seen"], 1)

    def test_result_identity_mismatch_is_scientific_fail_stop(self) -> None:
        packet, _ = self._packet()
        run_dir = self.root / "identity-failure-run"
        run_dir.mkdir()
        calls = []

        def bad_identity(row):
            calls.append(row["graph_id"])
            result = self._fake_result(row)
            result["source_artifact_sha256"] = "0" * 64
            return result

        outcome = h3_120.execute_ordered_panel(
            packet["rows"], run_dir=run_dir, process_row=bad_identity,
            synthetic_test_only=True)
        self.assertEqual(outcome["status"], "scientific_integrity_failure")
        self.assertEqual(calls, [packet["rows"][0]["graph_id"]])
        audit = h3_120.verify_h3_120_run(run_dir)
        self.assertFalse(audit["completed_120_row_panel"])
        self.assertEqual(audit["result_rows_seen"], 1)

    def test_shared_watchdog_supervises_synthetic_h3_child_and_stops_crash(self) -> None:
        complete_dir = self.root / "watchdog-normal"
        complete = h3_120.launch_synthetic_watchdog_test(
            run_dir=complete_dir, state_dir=self.root / "state-normal")
        self.assertEqual(complete["status"], "COMPLETED")
        self.assertEqual(complete["failure_category"], None)
        checked = _verify_recovery_directory(
            complete_dir, host_state_dir=self.root / "state-normal")
        self.assertTrue(checked["completed"])

        crash_dir = self.root / "watchdog-crash"
        crashed = h3_120.launch_synthetic_watchdog_test(
            run_dir=crash_dir, state_dir=self.root / "state-crash",
            scenario="child_exit")
        self.assertNotEqual(crashed["status"], "COMPLETED")
        self.assertFalse(crashed["resume_allowed"])
        crash_check = _verify_recovery_directory(
            crash_dir, host_state_dir=self.root / "state-crash")
        self.assertEqual(crash_check["status"], "VERIFIED_TERMINAL")
        self.assertFalse(crash_check["completed"])

    def test_shared_watchdog_wall_stop_is_terminal(self) -> None:
        run_dir = self.root / "watchdog-timeout"
        result = h3_120.launch_synthetic_watchdog_test(
            run_dir=run_dir, state_dir=self.root / "state-timeout", scenario="slow",
            test_limits={"wall_seconds": 0.4, "cpu_seconds": 30.0,
                         "case_seconds": 0.4, "oracle_seconds": 0.4,
                         "poll_seconds": 0.05})
        self.assertEqual(result["status"], "STOPPED_BY_WATCHDOG")
        self.assertFalse(result["resume_allowed"])


if __name__ == "__main__":
    unittest.main()
