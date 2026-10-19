"""Small synthetic execution/recovery tests; never instantiate the formal schedule."""

from __future__ import annotations

import hashlib
import json
import multiprocessing
from pathlib import Path
import signal
import sys
import tempfile
import time
import unittest
from concurrent.futures import ProcessPoolExecutor
from unittest import mock

import nc0a_execution_engine as engine
from nc0a_execution_engine import (
    CaseSpec, ExecutionError, formal_cases, run_battery, run_case_attempt,
)
from nc0a_contract_runner import (
    NC0aContractError, OperationalExecutionFailure, ScientificIntegrityFailure, save_report_once,
    synthetic_chain,
)
from nc0a_watchdog import (
    HashChainLog, WatchdogError, WatchdogLimits, supervise, verify_hash_chain,
)
from synthetic_graphs import synthetic_seed


TOY_A = CaseSpec(20, "er-like", False)
TOY_B = CaseSpec(20, "ws-like", False)


def _spawn_raise_scientific_integrity_failure():
    raise ScientificIntegrityFailure("GRAPH_INVARIANT_FAILURE", "injected invariant failure")


def _spawn_raise_operational_execution_failure():
    raise OperationalExecutionFailure("TASK_WALL_TIMEOUT", "injected task timeout")


class NC0aExecutionEngineTests(unittest.TestCase):
    def test_spawn_workers_preserve_failure_types_and_recovery_classification(self):
        cases = (
            (_spawn_raise_scientific_integrity_failure,
             ScientificIntegrityFailure, "SCIENTIFIC_INTEGRITY_FAILURE",
             "GRAPH_INVARIANT_FAILURE", False),
            (_spawn_raise_operational_execution_failure,
             OperationalExecutionFailure, "OPERATIONAL_FAILURE",
             "TASK_WALL_TIMEOUT", True),
        )
        for target, exception_type, category, reason_code, recovery_allowed in cases:
            with self.subTest(exception=exception_type.__name__):
                context = multiprocessing.get_context("spawn")
                with ProcessPoolExecutor(max_workers=1, mp_context=context) as pool:
                    future = pool.submit(target)
                    with self.assertRaises(exception_type) as caught:
                        future.result(timeout=30)

                classification = engine._classify_attempt_failure(caught.exception)
                self.assertIs(type(caught.exception), exception_type)
                self.assertEqual(caught.exception.reason_code, reason_code)
                self.assertEqual(classification["failure_category"], category)
                self.assertEqual(classification["reason_code"], reason_code)
                self.assertIs(classification["recovery_allowed"], recovery_allowed)

    def test_direct_formal_scale_entrypoints_refuse_without_signed_launcher(self):
        import os
        from nc0a_execution_engine import _runner_entry
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ExecutionError, "cryptographically approved"):
                run_battery(tmp, cases=formal_cases(), workers=8,
                            case_seconds=1, oracle_seconds=1, formal=True)
            with self.assertRaisesRegex(ExecutionError, "signed launcher"):
                run_case_attempt(formal_cases()[0], Path(tmp) / "attempt",
                                 workers=8, case_seconds=1, oracle_seconds=1,
                                 formal=True)
        token = os.environ.pop("NC0A_WATCHDOG_LAUNCH_TOKEN", None)
        parent = os.environ.pop("NC0A_WATCHDOG_PARENT_PID", None)
        try:
            with self.assertRaisesRegex(ExecutionError, "child of the watchdog"):
                _runner_entry("", "", "", "", "", 1)
        finally:
            if token is not None:
                os.environ["NC0A_WATCHDOG_LAUNCH_TOKEN"] = token
            if parent is not None:
                os.environ["NC0A_WATCHDOG_PARENT_PID"] = parent
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ExecutionError, "sub-formal"):
                run_case_attempt(CaseSpec(100, "er-like", False),
                                 Path(tmp) / "attempt", workers=1,
                                 case_seconds=1, oracle_seconds=1)
            oversized = tuple(CaseSpec(n, family, False)
                              for n in (100, 340, 1150, 3900)
                              for family in ("er-like", "ws-like", "ba-like", "factor-mst"))
            with self.assertRaisesRegex(ExecutionError, "microtest dispatcher is capped"):
                run_battery(tmp, cases=oversized, workers=8,
                            case_seconds=1, oracle_seconds=1)

    def test_formal_launcher_fails_closed_without_external_trust_anchor(self):
        from nc0a_execution_engine import launch_formal
        import os
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            policy, approval, pubkey = root / "policy.json", root / "approval.json", root / "reviewer.pem"
            policy.write_text("{}")
            approval.write_text("{}")
            pubkey.write_text("not-a-public-key")
            with mock.patch.object(
                    engine, "_trusted_reviewer_fingerprint",
                    side_effect=ExecutionError("No administrator-provisioned reviewer trust anchor")):
                with self.assertRaisesRegex(ExecutionError, "reviewer trust anchor"):
                    launch_formal(policy, approval, pubkey, root / "run")

    def test_ed25519_approval_signature_adapter_verifies_and_rejects_tampering(self):
        import shutil
        import subprocess
        from nc0a_execution_engine import verify_ed25519_signature
        if not shutil.which("openssl"):
            self.skipTest("OpenSSL executable is required by the formal approval gate")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            private = root / "reviewer-private.pem"
            public = root / "reviewer-public.pem"
            payload = root / "payload.json"
            signature = root / "payload.sig"
            payload.write_bytes(b'{"decision":"test-only"}')
            subprocess.run(["openssl", "genpkey", "-algorithm", "ED25519",
                            "-out", str(private)], check=True,
                           capture_output=True)
            subprocess.run(["openssl", "pkey", "-in", str(private), "-pubout",
                            "-out", str(public)], check=True, capture_output=True)
            subprocess.run(["openssl", "pkeyutl", "-sign", "-inkey", str(private),
                            "-rawin", "-in", str(payload), "-out", str(signature)],
                           check=True, capture_output=True)
            self.assertTrue(verify_ed25519_signature(public, payload.read_bytes(),
                                                     signature.read_bytes()))
            self.assertFalse(verify_ed25519_signature(public, payload.read_bytes() + b"x",
                                                      signature.read_bytes()))

    def test_committed_runtime_lock_matches_the_current_apple_silicon_test_host(self):
        import platform
        import subprocess
        import sys
        from hashlib import sha256
        from nc0a_execution_engine import RUNTIME_LOCK, _host_identifier, _verify_runtime_lock
        if sys.platform != "darwin" or platform.machine() != "arm64":
            self.skipTest("runtime lock is specific to the reviewed Apple Silicon host")
        physical_ram = int(subprocess.run(
            ["/usr/sbin/sysctl", "-n", "hw.memsize"], check=True,
            capture_output=True, text=True).stdout.strip())
        policy = {"runtime_dependency_lock_sha256": sha256(RUNTIME_LOCK.read_bytes()).hexdigest(),
                  "host_identifier": _host_identifier(),
                  "limits": {"measured_physical_ram_bytes": physical_ram}}
        _verify_runtime_lock(policy)

    def test_fixed_seed_micro_chain_repeats_identically(self):
        kwargs = dict(checkpoints=(1, 2, 4, 8, 32), max_wall_seconds=20,
                      max_proposals=32 * 160)
        first = synthetic_chain(20, "er-like", 0, **kwargs)
        second = synthetic_chain(20, "er-like", 0, **kwargs)
        self.assertEqual(first["seed"], second["seed"])
        self.assertEqual(first["fixture_sha256"], second["fixture_sha256"])
        self.assertEqual(first["checkpoints"], second["checkpoints"])
        self.assertEqual(first["mixing_status"], "MIXING-UNRESOLVED")

    def test_actual_toy_dispatch_runs_eight_chains_and_independent_oracle(self):
        with tempfile.TemporaryDirectory() as tmp:
            case_dir = Path(tmp) / "attempt-01"
            case_dir.mkdir()
            report = run_case_attempt(
                TOY_A, case_dir, workers=4, case_seconds=30,
                oracle_seconds=30, formal=False)
            self.assertEqual(len(report["chains"]), 8)
            self.assertEqual(report["oracle"]["attempts"], 1000)
            self.assertEqual(report["screen"]["mixing_status"], "MIXING-UNRESOLVED")
            self.assertEqual(report["mixing_status"], "MIXING-UNRESOLVED")
            self.assertEqual(len(set(report["chain_seeds"])), 8)
            self.assertGreaterEqual(report["worker_process_cpu_seconds"], 0)

    def test_completed_case_is_verified_and_retained_across_failed_task_resume(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cases = (TOY_A, TOY_B)
            with self.assertRaisesRegex(RuntimeError, "Injected parent-runner failure"):
                run_battery(root, cases=cases, workers=4, case_seconds=30,
                            oracle_seconds=30, max_attempts_per_case=2,
                            formal=False, crash_after_start_case=TOY_B.key)
            result_a = root / "cases" / TOY_A.key / "attempt-01" / "result.json"
            original_sha = hashlib.sha256(result_a.read_bytes()).hexdigest()
            self.assertTrue(Path(str(result_a) + ".sha256").exists())
            self.assertFalse((root / "cases" / TOY_B.key / "attempt-01" / "result.json").exists())

            final = run_battery(root, cases=cases, workers=4, case_seconds=30,
                                oracle_seconds=30, max_attempts_per_case=2,
                                formal=False)
            self.assertEqual(final["completed_cases"], 2)
            self.assertEqual(final["mixing_status"], "MIXING-UNRESOLVED")
            self.assertEqual(hashlib.sha256(result_a.read_bytes()).hexdigest(), original_sha)
            result_b = root / "cases" / TOY_B.key / "attempt-02" / "result.json"
            payload = json.loads(result_b.read_text())
            self.assertEqual(payload["attempt"], 2)
            self.assertEqual(payload["chain_seeds"], [
                synthetic_seed(TOY_B.family, TOY_B.n, kind="chain",
                               chain_index=i, root=8062026)
                for i in range(8)])
            seq, _ = verify_hash_chain(root / "execution.jsonl")
            self.assertGreaterEqual(seq, 7)
            events = [json.loads(line)["event"] for line in
                      (root / "execution.jsonl").read_text().splitlines()]
            self.assertTrue(any(e["event"] == "verified_completed_case_reused" for e in events))
            self.assertTrue(any(e["event"] == "case_attempt_failed" for e in events))
            result_a.write_text(result_a.read_text() + " ")
            with self.assertRaisesRegex(ExecutionError, "SHA-256 mismatch"):
                run_battery(root, cases=cases, workers=4, case_seconds=30,
                            oracle_seconds=30, max_attempts_per_case=2,
                            formal=False)

    def test_scientific_integrity_failure_is_persisted_and_cannot_be_retried(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with mock.patch.object(engine, "_execute_case_attempt",
                                   side_effect=ScientificIntegrityFailure(
                                       "BFS_ORACLE_MISMATCH", "oracle mismatch")):
                with self.assertRaisesRegex(ScientificIntegrityFailure, "oracle mismatch"):
                    run_battery(root, cases=(TOY_A,), workers=2, case_seconds=30,
                                oracle_seconds=30, max_attempts_per_case=2,
                                formal=False)
            rows = [json.loads(line)["event"] for line in
                    (root / "execution.jsonl").read_text().splitlines()]
            failure = next(event for event in rows if event["event"] == "case_attempt_failed")
            self.assertEqual(failure["failure_category"], "SCIENTIFIC_INTEGRITY_FAILURE")
            self.assertEqual(failure["reason_code"], "BFS_ORACLE_MISMATCH")
            self.assertFalse(failure["recovery_allowed"])
            with mock.patch.object(engine, "_execute_case_attempt") as execute:
                with self.assertRaisesRegex(ScientificIntegrityFailure, "recovery is prohibited"):
                    run_battery(root, cases=(TOY_A,), workers=2, case_seconds=30,
                                oracle_seconds=30, max_attempts_per_case=2,
                                formal=False)
                execute.assert_not_called()
            self.assertFalse((root / "cases" / TOY_A.key / "attempt-02").exists())

    def test_graph_oracle_assertion_is_converted_to_scientific_integrity_failure(self):
        import connected_swap
        for route in ("chain", "oracle"):
            with self.subTest(route=route), mock.patch.object(
                    connected_swap.ConnectedDegreeSwap, "propose",
                    side_effect=AssertionError("injected graph invariant disagreement")):
                with self.assertRaises(ScientificIntegrityFailure) as caught:
                    if route == "chain":
                        synthetic_chain(20, "er-like", 0,
                                        root=8062026,
                                        checkpoints=(1,), max_wall_seconds=5,
                                        max_proposals=500)
                    else:
                        from nc0a_contract_runner import oracle_trace
                        oracle_trace(20, "er-like", root=8062026, attempts=1,
                                     max_wall_seconds=5, max_proposals=1)
                self.assertIn(caught.exception.reason_code,
                              {"GRAPH_INVARIANT_FAILURE",
                               "BFS_ORACLE_OR_GRAPH_INVARIANT_FAILURE"})

    def test_unknown_exception_is_persisted_and_blocks_automatic_recovery(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with mock.patch.object(engine, "_execute_case_attempt",
                                   side_effect=ValueError("unclassified injected fault")):
                with self.assertRaisesRegex(ValueError, "unclassified injected fault"):
                    run_battery(root, cases=(TOY_A,), workers=2, case_seconds=30,
                                oracle_seconds=30, max_attempts_per_case=2,
                                formal=False)
            rows = [json.loads(line)["event"] for line in
                    (root / "execution.jsonl").read_text().splitlines()]
            failure = next(event for event in rows if event["event"] == "case_attempt_failed")
            self.assertEqual(failure["failure_category"], "UNCLASSIFIED_REQUIRES_REVIEW")
            self.assertFalse(failure["recovery_allowed"])
            with mock.patch.object(engine, "_execute_case_attempt") as execute:
                with self.assertRaisesRegex(ExecutionError, "manual review"):
                    run_battery(root, cases=(TOY_A,), workers=2, case_seconds=30,
                                oracle_seconds=30, max_attempts_per_case=2,
                                formal=False)
                execute.assert_not_called()

    def test_report_persistence_contract_error_is_unclassified_and_blocks_recovery(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with mock.patch.object(engine, "_execute_case_attempt",
                                   return_value={"toy": True}), \
                    mock.patch.object(engine, "save_report_once",
                                      side_effect=NC0aContractError(
                                          "Existing report cannot be silently overwritten")):
                with self.assertRaisesRegex(NC0aContractError, "silently overwritten"):
                    run_battery(root, cases=(TOY_A,), workers=2, case_seconds=30,
                                oracle_seconds=30, max_attempts_per_case=2,
                                formal=False)
            rows = [json.loads(line)["event"] for line in
                    (root / "execution.jsonl").read_text().splitlines()]
            failure = next(event for event in rows if event["event"] == "case_attempt_failed")
            self.assertEqual(failure["failure_category"], "UNCLASSIFIED_REQUIRES_REVIEW")
            self.assertEqual(failure["reason_code"], "UNCLASSIFIED_EXCEPTION")
            self.assertFalse(failure["recovery_allowed"])
            with mock.patch.object(engine, "_execute_case_attempt") as execute:
                with self.assertRaisesRegex(ExecutionError, "manual review"):
                    run_battery(root, cases=(TOY_A,), workers=2, case_seconds=30,
                                oracle_seconds=30, max_attempts_per_case=2,
                                formal=False)
                execute.assert_not_called()

    def test_confirmed_watchdog_signal_exit_is_logged_and_same_seed_recovery_is_bounded(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            attempt_dir = root / "cases" / TOY_A.key / "attempt-01"
            attempt_dir.mkdir(parents=True)
            manifest = engine._new_manifest(
                root, head="TEST_ONLY", policy_hash="TEST_ONLY",
                protocol={"test_case_keys": [TOY_A.key],
                          "root_seed": engine.ENGINEERING_TEST_SEED_ROOT,
                          "recovery": engine.PROTOCOL["recovery"]}, formal=False)
            engine._write_manifest_once(root, manifest)
            (root / "active_task.json").write_text(json.dumps({
                "phase": "case", "task_id": f"{TOY_A.key}/attempt-01",
                "started_utc_epoch": time.time()}))
            as_log = HashChainLog(root / "execution.jsonl")
            try:
                as_log.append({"event": "case_attempt_started", "case": TOY_A.key,
                               "attempt": 1, "fixed_seeds": None})
            finally:
                as_log.close()
            limits = WatchdogLimits(
                wall_seconds=10, cpu_seconds=100,
                aggregate_rss_bytes=512 * 1024 * 1024, max_workers=2,
                run_disk_bytes=64 * 1024 * 1024, reserve_free_disk_bytes=1,
                case_seconds=5, oracle_seconds=5, poll_seconds=0.05,
                suspend_tolerance_seconds=1, terminate_grace_seconds=0.1)
            watched = supervise(
                [sys.executable, "-c",
                 f"import os, signal; os.kill(os.getpid(), signal.{signal.Signals(signal.SIGKILL).name})"],
                run_dir=root, limits=limits, stdout_name="runner.stdout.01.log",
                invocation_id=1)
            self.assertEqual(watched["status"], "failed")
            self.assertEqual(watched["returncode"], -signal.SIGKILL)
            self.assertTrue(engine._append_runner_signal_failure(root, 1, watched))
            engine._append_invocation_disposition(
                root, 1, status="failed", returncode=watched["returncode"],
                run_integrity="NOT_COMPLETE", result=watched, prior_event_count=1)
            rows = [json.loads(line)["event"] for line in
                    (root / "execution.jsonl").read_text().splitlines()]
            failure = next(event for event in rows if event["event"] == "case_attempt_failed")
            self.assertEqual(failure["failure_category"], "OPERATIONAL_FAILURE")
            self.assertEqual(failure["reason_code"], "RUNNER_SIGNAL_EXIT_SIGKILL")
            self.assertTrue(failure["recovery_allowed"])
            result = run_battery(root, cases=(TOY_A,), workers=2, case_seconds=30,
                                 oracle_seconds=30, max_attempts_per_case=2,
                                 formal=False)
            self.assertEqual(result["completed_cases"], 1)
            report = json.loads((root / "cases" / TOY_A.key /
                                 "attempt-02" / "result.json").read_text())
            self.assertEqual(report["attempt"], 2)
            self.assertEqual(report["chain_seeds"], [
                synthetic_seed(TOY_A.family, TOY_A.n, kind="chain",
                               chain_index=i, root=engine.ENGINEERING_TEST_SEED_ROOT)
                for i in range(8)])

    def test_watchdog_stop_after_durable_completion_reconciles_stale_active_marker(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            run_battery(root, cases=(TOY_A,), workers=2, case_seconds=30,
                        oracle_seconds=30, max_attempts_per_case=2, formal=False)
            summary = root / "test_battery_summary.json"
            summary.unlink()
            Path(str(summary) + ".sha256").unlink()
            completed_attempt = root / "cases" / TOY_A.key / "attempt-01"
            active_payload = json.dumps({
                "phase": "case", "task_id": f"{TOY_A.key}/attempt-01",
                "started_utc_epoch": 0})
            runner_code = (
                "import json,time; from pathlib import Path; active=json.loads(" +
                repr(active_payload) + "); active['started_utc_epoch']=time.time(); "
                "Path('active_task.json').write_text(json.dumps(active)); time.sleep(10)")
            limits = WatchdogLimits(
                wall_seconds=10, cpu_seconds=100,
                aggregate_rss_bytes=512 * 1024 * 1024, max_workers=2,
                run_disk_bytes=64 * 1024 * 1024, reserve_free_disk_bytes=1,
                case_seconds=0.2, oracle_seconds=5, poll_seconds=0.05,
                suspend_tolerance_seconds=1, terminate_grace_seconds=0.1)
            stopped = supervise(
                [sys.executable, "-c", runner_code],
                run_dir=root, limits=limits, stdout_name="runner.stdout.01.log",
                invocation_id=1)
            self.assertEqual(stopped["status"], "stopped")
            self.assertEqual(stopped["reason"], "CASE_WALL_LIMIT")
            engine._append_watchdog_interruption(root, 1, stopped)
            rows = [json.loads(line)["event"] for line in
                    (root / "execution.jsonl").read_text().splitlines()]
            self.assertEqual(sum(event["event"] == "case_attempt_failed" and
                                 event.get("case") == TOY_A.key for event in rows), 0)
            self.assertEqual(sum(event["event"] == "case_attempt_completed" and
                                 event.get("case") == TOY_A.key for event in rows), 1)
            result = run_battery(root, cases=(TOY_A,), workers=2, case_seconds=30,
                                 oracle_seconds=30, max_attempts_per_case=2,
                                 formal=False)
            self.assertEqual(result["completed_cases"], 1)
            self.assertTrue((completed_attempt / "result.json").is_file())
            self.assertFalse((root / "cases" / TOY_A.key / "attempt-02").exists())
            rows = [json.loads(line)["event"] for line in
                    (root / "execution.jsonl").read_text().splitlines()]
            self.assertTrue(any(event["event"] ==
                                "completed_attempt_active_marker_reconciled"
                                for event in rows))

    def test_runner_signal_after_durable_completion_preserves_completed_attempt(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            run_battery(root, cases=(TOY_A,), workers=2, case_seconds=30,
                        oracle_seconds=30, max_attempts_per_case=2, formal=False)
            summary = root / "test_battery_summary.json"
            summary.unlink()
            Path(str(summary) + ".sha256").unlink()
            (root / "active_task.json").write_text(json.dumps({
                "phase": "case", "task_id": f"{TOY_A.key}/attempt-01",
                "started_utc_epoch": time.time()}))
            limits = WatchdogLimits(
                wall_seconds=10, cpu_seconds=100,
                aggregate_rss_bytes=512 * 1024 * 1024, max_workers=2,
                run_disk_bytes=64 * 1024 * 1024, reserve_free_disk_bytes=1,
                case_seconds=5, oracle_seconds=5, poll_seconds=0.05,
                suspend_tolerance_seconds=1, terminate_grace_seconds=0.1)
            watched = supervise(
                [sys.executable, "-c",
                 f"import os, signal; os.kill(os.getpid(), signal.{signal.Signals(signal.SIGKILL).name})"],
                run_dir=root, limits=limits, stdout_name="runner.stdout.01.log",
                invocation_id=1)
            classification = engine._append_runner_signal_failure(root, 1, watched)
            self.assertEqual(classification["failure_category"], "OPERATIONAL_FAILURE")
            self.assertEqual(classification["reason_code"],
                             "RUNNER_SIGNAL_EXIT_SIGKILL_AFTER_CASE_COMPLETION")
            engine._append_invocation_disposition(
                root, 1, status="failed", returncode=watched["returncode"],
                run_integrity="NOT_COMPLETE", result=watched,
                prior_event_count=len(engine._read_execution_records(
                    root / "execution.jsonl")),
                classification_override=classification)
            rows = [json.loads(line)["event"] for line in
                    (root / "execution.jsonl").read_text().splitlines()]
            self.assertEqual(sum(event["event"] == "case_attempt_failed" and
                                 event.get("case") == TOY_A.key for event in rows), 0)
            result = run_battery(root, cases=(TOY_A,), workers=2, case_seconds=30,
                                 oracle_seconds=30, max_attempts_per_case=2,
                                 formal=False)
            self.assertEqual(result["completed_cases"], 1)
            self.assertFalse((root / "cases" / TOY_A.key / "attempt-02").exists())

    def test_positive_runner_exit_and_signal_without_valid_active_task_are_not_recoverable(self):
        self.assertFalse(engine._append_runner_signal_failure(
            Path("/not-used"), 1, {"status": "failed", "returncode": 17}))
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.assertFalse(engine._append_runner_signal_failure(
                root, 1, {"status": "failed", "returncode": -signal.SIGKILL}))

    def test_invalid_paired_statistics_are_explicit_scientific_failures(self):
        chains = []
        for index in range(8):
            metrics = {"triangles": float("nan"),
                       "assortativity": 0.0, "edge_overlap": 0.0}
            chains.append({"chain_index": index, "n": TOY_A.n,
                           "family": TOY_A.family,
                           "checkpoints": {"4": {"metrics": metrics},
                                           "32": {"metrics": metrics}}})
        with self.assertRaises(ScientificIntegrityFailure) as caught:
            engine.screen_case(chains, require_full_contract=False)
        self.assertEqual(caught.exception.reason_code, "INVALID_PAIRED_STATISTIC")

    def test_two_operational_attempts_exhaust_the_allowance(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            injected = OperationalExecutionFailure("INJECTED_RESOURCE_STOP", "bounded test stop")
            for attempt in (1, 2):
                with mock.patch.object(engine, "_execute_case_attempt", side_effect=injected):
                    with self.assertRaisesRegex(OperationalExecutionFailure, "bounded test stop"):
                        run_battery(root, cases=(TOY_A,), workers=2, case_seconds=30,
                                    oracle_seconds=30, max_attempts_per_case=2,
                                    formal=False)
                self.assertTrue((root / "cases" / TOY_A.key /
                                 f"attempt-{attempt:02d}").is_dir())
            with mock.patch.object(engine, "_execute_case_attempt") as execute:
                with self.assertRaisesRegex(ExecutionError, "exhausted its 2-attempt"):
                    run_battery(root, cases=(TOY_A,), workers=2, case_seconds=30,
                                oracle_seconds=30, max_attempts_per_case=2,
                                formal=False)
                execute.assert_not_called()

    def test_started_attempt_without_terminal_failure_record_is_not_recoverable(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with mock.patch.object(engine, "_execute_case_attempt",
                                   side_effect=OperationalExecutionFailure(
                                       "INJECTED_CRASH", "injected")):
                with self.assertRaises(OperationalExecutionFailure):
                    run_battery(root, cases=(TOY_A,), workers=2, case_seconds=30,
                                oracle_seconds=30, max_attempts_per_case=2,
                                formal=False)
            log_path = root / "execution.jsonl"
            lines = log_path.read_bytes().splitlines(keepends=True)
            failure_index = next(i for i, line in enumerate(lines)
                                 if json.loads(line)["event"]["event"] == "case_attempt_failed")
            log_path.write_bytes(b"".join(lines[:failure_index]))
            self.assertIsNotNone(verify_hash_chain(log_path))  # Valid prefix, missing terminal.
            with mock.patch.object(engine, "_execute_case_attempt") as execute:
                with self.assertRaisesRegex(ExecutionError, "incomplete or conflicting terminal"):
                    run_battery(root, cases=(TOY_A,), workers=2, case_seconds=30,
                                oracle_seconds=30, max_attempts_per_case=2,
                                formal=False)
                execute.assert_not_called()

    def test_watchdog_recovery_is_limited_to_explicit_operational_stop_reasons(self):
        recoverable = engine._classify_watchdog_stop("AGGREGATE_RSS_LIMIT")
        self.assertEqual(recoverable["failure_category"], "OPERATIONAL_FAILURE")
        self.assertTrue(recoverable["recovery_allowed"])
        unresolved = engine._classify_watchdog_stop("UNKNOWN_PROCESS_GROUP_MEMBER")
        self.assertEqual(unresolved["failure_category"], "UNCLASSIFIED_REQUIRES_REVIEW")
        self.assertFalse(unresolved["recovery_allowed"])

    def test_reason_coded_watchdog_stop_is_logged_before_same_seed_task_recovery(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "cases" / TOY_A.key / "attempt-01").mkdir(parents=True)
            manifest = engine._new_manifest(
                root, head="TEST_ONLY", policy_hash="TEST_ONLY",
                protocol={"test_case_keys": [TOY_A.key],
                          "root_seed": engine.ENGINEERING_TEST_SEED_ROOT,
                          "recovery": engine.PROTOCOL["recovery"]}, formal=False)
            engine._write_manifest_once(root, manifest)
            active = {"phase": "case", "task_id": f"{TOY_A.key}/attempt-01",
                      "started_utc_epoch": 1.0}
            (root / "active_task.json").write_text(json.dumps(active))
            as_log = HashChainLog(root / "execution.jsonl")
            try:
                as_log.append({"event": "case_attempt_started", "case": TOY_A.key,
                               "attempt": 1, "fixed_seeds": None})
            finally:
                as_log.close()
            engine._append_watchdog_interruption(
                root, 1, {"status": "stopped", "reason": "CASE_WALL_LIMIT"})
            rows = [json.loads(line)["event"] for line in
                    (root / "execution.jsonl").read_text().splitlines()]
            failure = next(event for event in rows if event["event"] == "case_attempt_failed")
            self.assertEqual(failure["failure_category"], "OPERATIONAL_FAILURE")
            self.assertEqual(failure["reason_code"], "WATCHDOG_CASE_WALL_LIMIT")
            self.assertTrue(failure["recovery_allowed"])
            result = run_battery(root, cases=(TOY_A,), workers=2, case_seconds=30,
                                 oracle_seconds=30, max_attempts_per_case=2,
                                 formal=False)
            self.assertEqual(result["completed_cases"], 1)
            report = json.loads((root / "cases" / TOY_A.key /
                                 "attempt-02" / "result.json").read_text())
            self.assertEqual(report["attempt"], 2)
            self.assertEqual(report["chain_seeds"], [
                synthetic_seed(TOY_A.family, TOY_A.n, kind="chain",
                               chain_index=i, root=8062026)
                for i in range(8)])

    def test_worker_crash_is_a_failed_task_not_a_successful_oracle_case(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with self.assertRaises(Exception):
                run_battery(root, cases=(TOY_A,), workers=4, case_seconds=30,
                            oracle_seconds=30, max_attempts_per_case=1,
                            formal=False, crash_index=0)
            attempt = root / "cases" / TOY_A.key / "attempt-01"
            self.assertFalse((attempt / "result.json").exists())
            self.assertFalse((root / "test_battery_summary.json").exists())
            rows = [json.loads(line)["event"] for line in
                    (root / "execution.jsonl").read_text().splitlines()]
            failure = next(event for event in rows if event["event"] == "case_attempt_failed")
            self.assertEqual(failure["failure_category"], "OPERATIONAL_FAILURE")
            self.assertEqual(failure["reason_code"], "COMPUTE_WORKER_PROCESS_CRASH")
            self.assertTrue(failure["recovery_allowed"])
            with self.assertRaisesRegex(ExecutionError, "exhausted"):
                run_battery(root, cases=(TOY_A,), workers=4, case_seconds=30,
                            oracle_seconds=30, max_attempts_per_case=1,
                            formal=False)

    def test_disk_write_failure_cannot_leave_a_valid_result(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "result.json"
            with mock.patch("nc0a_contract_runner.os.fsync",
                            side_effect=OSError(28, "No space left on device")):
                with self.assertRaises(OSError):
                    save_report_once(path, {"synthetic": True})
            self.assertFalse(path.exists())
            self.assertFalse(Path(str(path) + ".sha256").exists())

    def test_hash_chain_tampering_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "events.jsonl"
            log = HashChainLog(path)
            log.append({"event": "start"})
            log.close()
            path.write_text(path.read_text().replace('"start"', '"other"'))
            with self.assertRaises(WatchdogError):
                verify_hash_chain(path)


if __name__ == "__main__":
    unittest.main()
