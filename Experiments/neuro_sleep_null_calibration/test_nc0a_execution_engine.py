"""Small synthetic execution/recovery tests; never instantiate the formal schedule."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import nc0a_execution_engine as engine
from nc0a_execution_engine import (
    CaseSpec, ExecutionError, formal_cases, run_battery, run_case_attempt,
)
from nc0a_contract_runner import save_report_once, synthetic_chain
from nc0a_watchdog import HashChainLog, WatchdogError, verify_hash_chain
from synthetic_graphs import synthetic_seed


TOY_A = CaseSpec(20, "er-like", False)
TOY_B = CaseSpec(20, "ws-like", False)


class NC0aExecutionEngineTests(unittest.TestCase):
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
            with self.assertRaisesRegex(ExecutionError, "allowance is exhausted"):
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
