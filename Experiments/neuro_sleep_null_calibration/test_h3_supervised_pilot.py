from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

MODULE_DIR = Path(__file__).resolve().parent
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

from h3_supervised_pilot import (  # noqa: E402
    EXPECTED_GRAPH_IDS,
    EXPECTED_MANIFEST_SHA256,
    HERE,
    H3PilotError,
    _HOST_LEDGER,
    _synthetic_row,
    _trial_deltas,
    _verify_recovery_directory,
    launch_synthetic_test,
    validate_pilot_bundle,
)
from nc0a_watchdog import (  # noqa: E402
    HashChainLog,
    WatchdogError,
    WatchdogLimits,
    sample_process_group,
    supervise,
    verify_hash_chain,
)
from riken_source_identity import (  # noqa: E402
    H3_TRIAL_Q_ATOL_PROPOSED,
    hash_float64,
    validate_h3_replay,
)


class TestH3SupervisedPilot(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="h3-supervised-synthetic-")
        self.root = Path(self.temp.name)
        self.state = self.root / "state"
        self.runs = self.root / "runs"

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_case(self, name: str, **kwargs):
        return launch_synthetic_test(
            run_dir=self.runs / name, state_dir=self.state, **kwargs)

    def test_public_pilot_bundle_hashes_order_and_all_row_identities(self) -> None:
        pilot_path = HERE / "G0_RIKEN_H3_CALIBRATION_PILOT_2026-10-21.json"
        manifest_path = HERE / "G0_RIKEN_SOURCE_GRAPH_EXPECTED_MANIFEST_2026-10-21.json"
        with patch("h3_supervised_pilot.h3_runtime_manifest", return_value={
                "replay_environment_matches_recorded_versions_and_candidate_lock": True}):
            pilot, manifest = validate_pilot_bundle(pilot_path, manifest_path)
        self.assertEqual(len(pilot["records"]), 10)
        self.assertEqual(tuple(row["graph_id"] for row in pilot["records"]),
                         EXPECTED_GRAPH_IDS)
        self.assertEqual(pilot["source_manifest_sha256"], EXPECTED_MANIFEST_SHA256)
        self.assertEqual(len(manifest["h3_panel"]["records"]), 120)

    def test_bundle_order_or_runtime_mismatch_is_rejected_before_launch(self) -> None:
        pilot_path = HERE / "G0_RIKEN_H3_CALIBRATION_PILOT_2026-10-21.json"
        manifest_path = HERE / "G0_RIKEN_SOURCE_GRAPH_EXPECTED_MANIFEST_2026-10-21.json"
        value = json.loads(pilot_path.read_text(encoding="utf-8"))
        value["records"][0], value["records"][1] = value["records"][1], value["records"][0]
        payload = json.dumps(value, sort_keys=True, separators=(",", ":"),
                             ensure_ascii=False, allow_nan=False).encode("utf-8")
        with tempfile.TemporaryDirectory(prefix="h3-bundle-negative-") as temp:
            changed = Path(temp) / "pilot.json"
            changed.write_bytes(payload)
            changed_sha = hashlib.sha256(payload).hexdigest()
            with patch("h3_supervised_pilot.h3_runtime_manifest", return_value={
                    "replay_environment_matches_recorded_versions_and_candidate_lock": True}):
                with self.assertRaisesRegex(H3PilotError, "order or identity"):
                    validate_pilot_bundle(changed, manifest_path,
                                          expected_pilot_sha256=changed_sha)
        with patch("h3_supervised_pilot.h3_runtime_manifest", return_value={
                "replay_environment_matches_recorded_versions_and_candidate_lock": False}):
            with self.assertRaisesRegex(H3PilotError, "replay lock"):
                validate_pilot_bundle(pilot_path, manifest_path)

    def test_supervised_synthetic_rows_continue_after_first_success(self) -> None:
        result = self.run_case("ordered", rows=[{}, {}])
        self.assertEqual(result["status"], "COMPLETED", result)
        self.assertEqual(result["watchdog"]["usage"]["peak_compute_workers"], 1)
        self.assertLessEqual(result["watchdog"]["usage"]["peak_compute_workers"], 4)
        report = _verify_recovery_directory(self.runs / "ordered",
                                             host_state_dir=self.state)
        self.assertEqual(report["status"], "VERIFIED_TERMINAL")
        self.assertTrue(report["completed"])
        self.assertFalse(report["resume_allowed"])
        evidence = self.runs / "ordered" / "h3-evidence.jsonl"
        count, tip = verify_hash_chain(evidence)
        self.assertEqual(tip, result["evidence_tip_sha256"])
        events = [json.loads(line)["event"] for line in evidence.read_text().splitlines()]
        graph_rows = [event for event in events if event.get("kind") == "graph_result"]
        self.assertEqual([event["pilot_order"] for event in graph_rows], [1, 2])
        self.assertEqual([event["source_graph_identity"] for event in graph_rows],
                         ["PASS", "PASS"])
        self.assertEqual([event["historical_order_q_replay"] for event in graph_rows],
                         ["PASS", "PASS"])
        self.assertEqual(len(graph_rows[0]["historical_order_trial_q_abs_deltas"]), 200)
        self.assertEqual(len(graph_rows[0]["sorted_order_trial_q_abs_deltas"]), 200)
        self.assertGreater(count, 3)

    def test_historical_q_failure_stops_before_next_fixed_row(self) -> None:
        result = self.run_case("history-fail", rows=[{"historical_mismatch": True}, {}])
        self.assertEqual(result["status"], "STOPPED_ON_HISTORICAL_IDENTITY_FAILURE")
        self.assertEqual(result["failure_category"], "HISTORICAL_IDENTITY_FAILURE")
        evidence = self.runs / "history-fail" / "h3-evidence.jsonl"
        events = [json.loads(line)["event"] for line in evidence.read_text().splitlines()]
        graph_rows = [event for event in events if event.get("kind") == "graph_result"]
        self.assertEqual(len(graph_rows), 1)
        self.assertEqual(graph_rows[0]["historical_order_q_replay"], "NC-INVALID")
        self.assertFalse(result["resume_allowed"])

    def test_source_identity_failure_is_not_confused_with_executor_order(self) -> None:
        result = self.run_case("source-fail", rows=[{"source_mismatch": True}, {}])
        self.assertEqual(result["status"], "STOPPED_ON_HISTORICAL_IDENTITY_FAILURE")
        self.assertEqual(result["failure_category"], "HISTORICAL_IDENTITY_FAILURE")
        events = [json.loads(line)["event"] for line in
                  (self.runs / "source-fail" / "h3-evidence.jsonl").read_text().splitlines()]
        first = next(event for event in events if event.get("kind") == "graph_result")
        self.assertEqual(first["source_graph_identity"], "NC-INVALID")
        self.assertEqual(first["historical_order_q_replay"], "PASS")

    def test_executor_sorted_mismatch_is_diagnostic_and_does_not_stop(self) -> None:
        result = self.run_case("sorted-diagnostic", rows=[{"executor_mismatch": True}, {}])
        self.assertEqual(result["status"], "COMPLETED", result)
        events = [json.loads(line)["event"] for line in
                  (self.runs / "sorted-diagnostic" / "h3-evidence.jsonl").read_text().splitlines()]
        graph_rows = [event for event in events if event.get("kind") == "graph_result"]
        self.assertEqual(len(graph_rows), 2)
        self.assertEqual(graph_rows[0]["source_graph_identity"], "PASS")
        self.assertEqual(graph_rows[0]["historical_order_q_replay"], "PASS")
        self.assertEqual(graph_rows[0]["executor_sorted_order_compatibility"], "INCOMPATIBLE")

    def test_trial_q_tolerance_accepts_equal_absolute_boundary_only(self) -> None:
        fixture = _synthetic_row(0)
        replay = fixture["replay"]
        values = list(replay["historical_q_values"])
        values[0] = 0.0
        replay["historical_q_values"] = values
        fixture["expected"]["historical_q_vector_sha256"] = hash_float64(values)
        historical = list(replay["historical_builder_q_values"])
        historical[0] = H3_TRIAL_Q_ATOL_PROPOSED
        replay["historical_builder_q_values"] = historical
        self.assertEqual(_trial_deltas(historical, values)[0], H3_TRIAL_Q_ATOL_PROPOSED)
        at_boundary = validate_h3_replay(
            [fixture["expected"]], [replay], trial_q_atol=H3_TRIAL_Q_ATOL_PROPOSED)
        self.assertEqual(at_boundary["historical_order_q_replay"]["status"], "PASS")
        historical[0] = H3_TRIAL_Q_ATOL_PROPOSED + 1e-16
        replay["historical_builder_q_values"] = historical
        over_boundary = validate_h3_replay(
            [fixture["expected"]], [replay], trial_q_atol=H3_TRIAL_Q_ATOL_PROPOSED)
        self.assertEqual(over_boundary["historical_order_q_replay"]["status"],
                         "NC-INVALID")

    def test_watchdog_timeout_stops_process_tree_and_marks_attempt_terminal(self) -> None:
        result = self.run_case("timeout", scenario="sleep", test_limits={
            "wall_seconds": 0.5, "cpu_seconds": 30.0,
            "case_seconds": 0.5, "oracle_seconds": 0.5,
            "poll_seconds": 0.05,
        })
        self.assertEqual(result["status"], "STOPPED_BY_WATCHDOG")
        self.assertIn(result["watchdog"]["reason"], {"WALL_LIMIT", "CASE_WALL_LIMIT"})
        self.assertIsNotNone(result["watchdog_audit_tip_sha256"])
        self.assertFalse(result["resume_allowed"])

    def test_watchdog_cpu_limit_is_enforced(self) -> None:
        result = self.run_case("cpu", scenario="cpu", test_limits={
            "wall_seconds": 8.0, "cpu_seconds": 0.15,
            "case_seconds": 8.0, "oracle_seconds": 8.0,
            "poll_seconds": 0.05,
        })
        self.assertEqual(result["status"], "STOPPED_BY_WATCHDOG")
        self.assertIn(result["watchdog"]["reason"],
                      {"CPU_LIMIT_WITH_TERMINATION_MARGIN", "WALL_LIMIT"})

    def test_watchdog_sampled_rss_limit_stops_allocating_child(self) -> None:
        result = self.run_case("rss", scenario="memory", test_limits={
            "wall_seconds": 10.0, "cpu_seconds": 30.0,
            "aggregate_rss_bytes": 96 * 1024**2,
            "case_seconds": 10.0, "oracle_seconds": 10.0,
            "poll_seconds": 0.05,
        })
        self.assertEqual(result["status"], "STOPPED_BY_WATCHDOG")
        self.assertIn(result["watchdog"]["reason"], {"AGGREGATE_RSS_LIMIT", "CPU_LIMIT_WITH_TERMINATION_MARGIN"})
        self.assertEqual(result["memory_limit_semantics"], "4_GIB_RSS_SAMPLED_NOT_HARD")

    def test_watchdog_disk_limit_stops_streaming_child(self) -> None:
        result = self.run_case("disk", scenario="disk", test_limits={
            "wall_seconds": 10.0, "cpu_seconds": 30.0,
            "run_disk_bytes": 4 * 1024**2,
            "case_seconds": 10.0, "oracle_seconds": 10.0,
            "poll_seconds": 0.05,
        })
        self.assertEqual(result["status"], "STOPPED_BY_WATCHDOG")
        self.assertEqual(result["watchdog"]["reason"], "RUN_DISK_ALLOCATION_LIMIT")

    def test_child_process_nonzero_exit_is_operational_and_not_retried(self) -> None:
        result = self.run_case("child-exit", scenario="child_exit")
        self.assertEqual(result["status"], "FAILED_RUNNER_EXIT")
        self.assertEqual(result["failure_category"], "OPERATIONAL_FAILURE")
        with self.assertRaisesRegex(H3PilotError, "already has a recorded attempt"):
            self.run_case("child-exit-again", scenario="child_exit",
                          pilot_sha256=result["pilot_sha256"])

    def test_host_lock_rejects_concurrent_launch(self) -> None:
        from h3_supervised_pilot import _host_lock
        with _host_lock(self.state):
            with self.assertRaisesRegex(H3PilotError, "host lock"):
                self.run_case("second", rows=[{}])

    def test_other_watchdog_activity_cannot_bypass_host_worker_lock(self) -> None:
        from h3_supervised_pilot import _host_lock
        limits = WatchdogLimits(
            wall_seconds=2, cpu_seconds=2, aggregate_rss_bytes=64 * 1024**2,
            max_workers=4, run_disk_bytes=1024**2, reserve_free_disk_bytes=1,
            case_seconds=2, oracle_seconds=2, poll_seconds=0.05)
        with _host_lock(self.state):
            with self.assertRaisesRegex(WatchdogError, "host lock"):
                supervise([sys.executable, "-c", "pass"],
                          run_dir=self.root / "blocked-watchdog", limits=limits)

    def test_partial_activity_ledger_fails_closed_and_recovery_is_audit_only(self) -> None:
        self.state.mkdir(parents=True)
        with HashChainLog(self.state / _HOST_LEDGER) as ledger:
            ledger.append({"kind": "activity_started", "run_id": "prior",
                           "pilot_sha256": "f" * 64,
                           "run_directory": str(self.runs / "prior")})
        with self.assertRaisesRegex(H3PilotError, "no terminal record"):
            self.run_case("new-after-partial", rows=[{}])
        incomplete = self.runs / "recover-me"
        incomplete.mkdir(parents=True)
        with HashChainLog(incomplete / "h3-control.jsonl") as control:
            control.append({"kind": "activity_started", "run_id": "partial"})
        report = _verify_recovery_directory(incomplete, host_state_dir=self.state)
        self.assertEqual(report["status"], "INCOMPLETE_NOT_RESUMABLE")
        self.assertFalse(report["resume_allowed"])

    def test_corrupt_audit_suffix_is_rejected_during_recovery_inspection(self) -> None:
        self.run_case("tamper", rows=[{}])
        evidence = self.runs / "tamper" / "h3-evidence.jsonl"
        evidence.write_bytes(evidence.read_bytes() + b"{}\n")
        with self.assertRaises((H3PilotError, WatchdogError)):
            _verify_recovery_directory(self.runs / "tamper",
                                       host_state_dir=self.state)

    def test_valid_hash_prefix_without_last_evidence_event_is_not_terminal(self) -> None:
        self.run_case("evidence-prefix", rows=[{}])
        evidence = self.runs / "evidence-prefix" / "h3-evidence.jsonl"
        lines = evidence.read_bytes().splitlines(keepends=True)
        evidence.write_bytes(b"".join(lines[:-1]))
        with self.assertRaisesRegex(H3PilotError, "tip differs"):
            _verify_recovery_directory(self.runs / "evidence-prefix",
                                       host_state_dir=self.state)

    def test_stdout_tampering_is_rejected_even_when_watchdog_chain_is_valid(self) -> None:
        self.run_case("stdout-tamper", rows=[{}])
        stdout = self.runs / "stdout-tamper" / "runner.stdout.log"
        stdout.write_bytes(stdout.read_bytes() + b"changed after supervision")
        with self.assertRaisesRegex(H3PilotError, "stdout"):
            _verify_recovery_directory(self.runs / "stdout-tamper",
                                       host_state_dir=self.state)

    def test_control_log_suffix_loss_is_not_accepted_as_terminal(self) -> None:
        self.run_case("truncated-control", rows=[{}])
        control = self.runs / "truncated-control" / "h3-control.jsonl"
        control.write_bytes(control.read_bytes().splitlines(keepends=True)[0])
        with self.assertRaisesRegex(H3PilotError, "summary|closed"):
            _verify_recovery_directory(self.runs / "truncated-control",
                                       host_state_dir=self.state)

    def test_watchdog_parent_crash_kills_runner_and_blocks_automatic_recovery(self) -> None:
        run_dir = self.runs / "watchdog-parent-crash"
        code = (
            "import sys; from pathlib import Path; "
            "from h3_supervised_pilot import launch_synthetic_test; "
            "launch_synthetic_test(run_dir=Path(sys.argv[1]), "
            "state_dir=Path(sys.argv[2]), scenario='sleep', "
            "test_limits={'wall_seconds': 30.0, 'cpu_seconds': 30.0, "
            "'case_seconds': 30.0, 'oracle_seconds': 30.0})"
        )
        launcher = subprocess.Popen(
            [sys.executable, "-c", code, str(run_dir), str(self.state)],
            cwd=MODULE_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        lease = run_dir / "h3-active-lease.json"
        deadline = time.monotonic() + 10
        while not lease.is_file() and time.monotonic() < deadline:
            if launcher.poll() is not None:
                self.fail("Synthetic launcher exited before creating its child lease")
            time.sleep(0.05)
        self.assertTrue(lease.is_file(), "runner lease was not created")
        group_id = int(json.loads(lease.read_text())["process_group_id"])
        launcher.kill()
        launcher.wait(timeout=5)
        deadline = time.monotonic() + 5
        live_members = [object()]
        while live_members and time.monotonic() < deadline:
            try:
                members = sample_process_group(group_id)
            except (ProcessLookupError, WatchdogError, subprocess.SubprocessError):
                members = []
            live_members = [item for item in members if not item.state.startswith("Z")]
            if live_members:
                time.sleep(0.1)
        self.assertEqual(live_members, [], "runner survived watchdog-parent death")
        report = _verify_recovery_directory(run_dir, host_state_dir=self.state)
        self.assertEqual(report["status"], "INCOMPLETE_NOT_RESUMABLE")
        with self.assertRaisesRegex(H3PilotError, "no terminal record"):
            self.run_case("no-recovery-after-parent-crash", rows=[{}])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
