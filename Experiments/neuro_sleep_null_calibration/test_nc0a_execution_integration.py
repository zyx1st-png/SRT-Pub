"""End-to-end signed toy-only launch tests; never authorizes a formal workload."""

from __future__ import annotations

import base64
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from unittest import mock
import uuid

import nc0a_execution_engine as engine
from nc0a_authority_ledger import (
    AuthorityLedger, AuthorityLedgerError, initialize_authority_store,
)
from nc0a_execution_engine import ExecutionError, launch_test_only
from nc0a_watchdog import WatchdogError


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


class SignedToyLauncherTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.key_root = tempfile.TemporaryDirectory(prefix="nc0a-r8-signing-key-")
        root = Path(cls.key_root.name)
        cls.private_key = root / "test-only-private.pem"
        cls.public_key = root / "test-only-public.pem"
        subprocess.run(["openssl", "genpkey", "-algorithm", "ED25519",
                        "-out", str(cls.private_key)], check=True,
                       capture_output=True)
        subprocess.run(["openssl", "pkey", "-in", str(cls.private_key),
                        "-pubout", "-out", str(cls.public_key)], check=True,
                       capture_output=True)
        cls.fingerprint = hashlib.sha256(cls.public_key.read_bytes()).hexdigest()

    @classmethod
    def tearDownClass(cls):
        cls.key_root.cleanup()

    @contextmanager
    def trusted_test_key(self):
        with mock.patch.dict(os.environ,
                             {"NC0A_TEST_TRUSTED_PUBKEY_SHA256": self.fingerprint}):
            yield

    def make_authorization(self, root: Path, *, workers: int = 4,
                           fault: str | None = None) -> tuple[Path, Path, Path, Path]:
        root.mkdir(parents=True, exist_ok=True)
        store_root = root / "external-authority"
        ledger_path = store_root / "ledger" / "authority.jsonl"
        anchor_path = store_root / "anchor" / "tip.json"
        initialize_authority_store(ledger_path, anchor_path)
        policy = {
            "purpose": engine.ENGINEERING_TEST_APPROVAL_PURPOSE,
            "test_experiment_id": str(uuid.uuid4()),
            "target_repository_head_sha": engine._git_head(),
            "execution_environment": engine._environment(engine._git_head()),
            "authority_ledger_path": str(ledger_path),
            "authority_anchor_path": str(anchor_path),
            "memory_enforcement_backend": "SAMPLED_ONLY",
            "host_memory_free_percent_stop": 1,
            "max_workers": workers,
            "max_invocations": 2 if fault else 1,
            "worker_hold_seconds": 0.9,
            "fault_first_invocation": fault,
            "cases": [{"n": 20, "family": "er-like"}],
            "limits": {
                "absolute_wall_seconds": 120,
                "aggregate_cpu_seconds": 600,
                "max_workers": workers,
                "peak_aggregate_ram_bytes": 2 * 1024**3,
                "temporary_disk_allocation_bytes": 64 * 1024**2,
                "reserved_free_disk_bytes": 1,
                "case_timeout_seconds": 60,
                "oracle_timeout_seconds": 30,
            },
        }
        policy_path = root / "test-resource-policy.json"
        policy_path.write_bytes(canonical(policy) + b"\n")
        approval = {
            "purpose": engine.ENGINEERING_TEST_APPROVAL_PURPOSE,
            "decision": "APPROVED_FOR_BOUNDED_ENGINEERING_TEST_ONLY",
            "test_experiment_id": policy["test_experiment_id"],
            "target_repository_head_sha": engine._git_head(),
            "policy_sha256": hashlib.sha256(policy_path.read_bytes()).hexdigest(),
            "cases": policy["cases"],
            "max_workers": workers,
            "seed_root": engine.ENGINEERING_TEST_SEED_ROOT,
            "recovery_rule": engine.PROTOCOL["recovery"],
            "test_source_sha256": engine._test_source_hashes(),
            "test_environment_sha256": hashlib.sha256(
                canonical(policy["execution_environment"])).hexdigest(),
        }
        unsigned = canonical(approval)
        payload = root / "approval.payload"
        signature = root / "approval.signature"
        payload.write_bytes(unsigned)
        subprocess.run(["openssl", "pkeyutl", "-sign", "-inkey",
                        str(self.private_key), "-rawin", "-in", str(payload),
                        "-out", str(signature)], check=True, capture_output=True)
        approval["signature_ed25519_base64"] = base64.b64encode(
            signature.read_bytes()).decode("ascii")
        approval_path = root / "test-approval.json"
        approval_path.write_bytes(canonical(approval) + b"\n")
        return policy_path, approval_path, self.public_key, root / "run-one"

    def make_formal_v2_test_authorization(self, root: Path, *,
                                          wall_seconds: int = 300,
                                          cpu_seconds: int = 600,
                                          attempts: int = 2):
        """Create a temporary test-key signature for the real V2 launcher path.

        The test trust fingerprint is injected only inside a mocked test scope;
        this fixture is not a production reviewer approval and cannot be used
        by the production CLI or administrator-installed trust anchor.
        """
        from test_nc0a_budget_preflight import macos_policy

        root.mkdir(parents=True, exist_ok=True)
        ledger_path = root / "external-ledger" / "authority.jsonl"
        anchor_path = root / "external-tip" / "tip.json"
        initialize_authority_store(ledger_path, anchor_path)
        policy = macos_policy()
        policy.update({
            "formal_experiment_id": str(uuid.uuid4()),
            "target_repository_head_sha": engine._git_head(),
            "runtime_dependency_lock_sha256": hashlib.sha256(
                engine.RUNTIME_LOCK.read_bytes()).hexdigest(),
            "host_identifier": engine._host_identifier(),
            "authority_ledger_path": str(ledger_path),
            "authority_anchor_path": str(anchor_path),
        })
        policy["limits"]["absolute_wall_seconds"] = wall_seconds
        policy["limits"]["aggregate_cpu_seconds"] = cpu_seconds
        policy["limits"]["case_timeout_seconds"] = min(60, wall_seconds)
        policy["limits"]["oracle_timeout_seconds"] = min(30, wall_seconds)
        policy_path = root / "resource-policy.json"
        policy_path.write_bytes(canonical(policy) + b"\n")
        approval = {
            "purpose": engine.MACOS_APPROVAL_PURPOSE,
            "decision": "APPROVED_FOR_FORMAL_NC0A",
            "policy_sha256": hashlib.sha256(policy_path.read_bytes()).hexdigest(),
            "target_repository_head_sha": engine._git_head(),
            "formal_experiment_id": policy["formal_experiment_id"],
            "preregistration_sha256": hashlib.sha256(
                engine.PREREGISTRATION.read_bytes()).hexdigest(),
            "protocol_sha256": engine._protocol_hash(),
            "protocol": engine.PROTOCOL,
            "watchdog_contract_sha256": engine._watchdog_contract_hash(),
            "watchdog_contract": engine.WATCHDOG_CONTRACT,
            "watchdog_source_sha256": engine._watchdog_source_hash(),
            "resource_limits": policy["limits"],
            "independent_reviewer": "TEMPORARY TEST SIGNER; NOT A REAL APPROVAL",
            "independent_review_url": "https://example.invalid/test-only-not-an-approval",
            "operational_attempts_per_case": attempts,
            "retry_rule": engine.PROTOCOL["recovery"],
            "resource_amendment_status": policy["resource_amendment_status"],
            "resource_amendment_approver": policy["resource_amendment_approver"],
            "resource_amendment_sha256": policy["resource_amendment_sha256"],
            "resource_amendment_approval_record_url":
                policy["resource_amendment_approval_record_url"],
            "macos_memory_semantics": policy["memory_limit_semantics"],
            "macos_residual_risk_acceptance":
                policy["macos_residual_risk_acceptance"],
            "reviewer_key_fingerprint_sha256": self.fingerprint,
        }
        payload_path = root / "approval.payload"
        signature_path = root / "approval.signature"
        approval_path = root / "approval.json"
        payload_path.write_bytes(canonical(approval))
        subprocess.run(["openssl", "pkeyutl", "-sign", "-inkey",
                        str(self.private_key), "-rawin", "-in", str(payload_path),
                        "-out", str(signature_path)], check=True, capture_output=True)
        approval["signature_ed25519_base64"] = base64.b64encode(
            signature_path.read_bytes()).decode("ascii")
        approval_path.write_bytes(canonical(approval) + b"\n")
        return policy_path, approval_path, self.public_key, root / "private-run", policy

    def make_formal_v3_test_authorization(self, root: Path, *,
                                          wall_seconds: int = 300,
                                          cpu_seconds: int = 600):
        """Test-only V3 signature fixture; independent approval fields are fake."""
        from test_nc0a_budget_preflight import macos_v3_policy
        from nc0a_budget_preflight import MACOS_SWAP_TELEMETRY_SEMANTICS

        root.mkdir(parents=True, exist_ok=True)
        ledger_path = root / "external-ledger" / "authority.jsonl"
        anchor_path = root / "external-tip" / "tip.json"
        initialize_authority_store(ledger_path, anchor_path)
        policy = macos_v3_policy()
        policy.update({
            "formal_experiment_id": str(uuid.uuid4()),
            "target_repository_head_sha": engine._git_head(),
            "runtime_dependency_lock_sha256": hashlib.sha256(
                engine.RUNTIME_LOCK.read_bytes()).hexdigest(),
            "host_identifier": engine._host_identifier(),
            "authority_ledger_path": str(ledger_path),
            "authority_anchor_path": str(anchor_path),
        })
        policy["limits"]["absolute_wall_seconds"] = wall_seconds
        policy["limits"]["aggregate_cpu_seconds"] = cpu_seconds
        policy["limits"]["case_timeout_seconds"] = min(60, wall_seconds)
        policy["limits"]["oracle_timeout_seconds"] = min(30, wall_seconds)
        policy_path = root / "resource-policy-v3.json"
        policy_path.write_bytes(canonical(policy) + b"\n")
        approval = {
            "purpose": engine.MACOS_V3_APPROVAL_PURPOSE,
            "decision": "APPROVED_FOR_FORMAL_NC0A",
            "policy_sha256": hashlib.sha256(policy_path.read_bytes()).hexdigest(),
            "target_repository_head_sha": engine._git_head(),
            "formal_experiment_id": policy["formal_experiment_id"],
            "preregistration_sha256": hashlib.sha256(
                engine.PREREGISTRATION.read_bytes()).hexdigest(),
            "protocol_sha256": engine._protocol_hash(),
            "protocol": engine.PROTOCOL,
            "watchdog_contract_sha256": engine._watchdog_contract_hash(),
            "watchdog_contract": engine.WATCHDOG_CONTRACT,
            "watchdog_source_sha256": engine._watchdog_source_hash(),
            "resource_limits": policy["limits"],
            "independent_reviewer": "TEMPORARY TEST SIGNER; NOT A REAL APPROVAL",
            "independent_review_url": "https://example.invalid/test-only-not-an-approval",
            "operational_attempts_per_case": 1,
            "retry_rule": engine.PROTOCOL["recovery"],
            "resource_amendment_status": policy["resource_amendment_status"],
            "resource_amendment_approver": policy["resource_amendment_approver"],
            "resource_amendment_sha256": policy["resource_amendment_sha256"],
            "resource_amendment_approval_record_url":
                policy["resource_amendment_approval_record_url"],
            "macos_memory_semantics": policy["memory_limit_semantics"],
            "macos_residual_risk_acceptance":
                policy["macos_residual_risk_acceptance"],
            "macos_swap_telemetry_semantics": MACOS_SWAP_TELEMETRY_SEMANTICS,
            "reviewer_key_fingerprint_sha256": self.fingerprint,
        }
        payload_path = root / "approval-v3.payload"
        signature_path = root / "approval-v3.signature"
        approval_path = root / "approval-v3.json"
        payload_path.write_bytes(canonical(approval))
        subprocess.run(["openssl", "pkeyutl", "-sign", "-inkey",
                        str(self.private_key), "-rawin", "-in", str(payload_path),
                        "-out", str(signature_path)], check=True, capture_output=True)
        approval["signature_ed25519_base64"] = base64.b64encode(
            signature_path.read_bytes()).decode("ascii")
        approval_path.write_bytes(canonical(approval) + b"\n")
        return policy_path, approval_path, self.public_key, root / "private-run", policy

    def make_science_stub(self, root: Path) -> Path:
        """Runner substitute still calls the real task scheduler on a toy case."""
        script = root / "nonformal-science-stub.py"
        source = """
            from pathlib import Path
            import os, sys, time

            def main():
                module_dir, run_dir, action = sys.argv[1], Path(sys.argv[2]), sys.argv[3]
                sys.path.insert(0, module_dir)
                import nc0a_execution_engine as e
                from nc0a_execution_engine import CaseSpec
                from nc0a_watchdog import guard_watchdog_parent
                token = os.environ['NC0A_WATCHDOG_LAUNCH_TOKEN']
                parent = int(os.environ['NC0A_WATCHDOG_PARENT_PID'])
                role_path = Path(os.environ['NC0A_PROCESS_ROLE_REGISTRY'])
                if parent != os.getppid() or role_path.parent.resolve() != run_dir.resolve():
                    raise SystemExit(91)
                e._ACTIVE_PROCESS_ROLE_REGISTRY = e.ProcessRoleRegistry(
                    role_path, token, os.getpid())
                guard_watchdog_parent(parent)
                if action == 'wall-overrun':
                    time.sleep(30)
                    raise SystemExit(0)
                faults = {'crash_index': 0} if action == 'worker-crash' else {}
                result = e.run_battery(
                    run_dir, cases=(CaseSpec(20, 'er-like', False),), workers=2,
                    case_seconds=60, oracle_seconds=30, max_attempts_per_case=2,
                    process_role_registry=e._ACTIVE_PROCESS_ROLE_REGISTRY, **faults)
                print(result, flush=True)

            if __name__ == '__main__':
                main()
        """
        script.write_text(textwrap.dedent(source), encoding="utf-8")
        return script

    @contextmanager
    def formal_v2_test_runtime(self, runner_factory, *, native_state=None):
        """Mock only hardware telemetry/trust; run real approval/ledger/watchdog."""
        from types import SimpleNamespace
        import nc0a_watchdog as watchdog

        real_disk_usage = shutil.disk_usage
        native = native_state or {
            "swap_total_bytes": 8 * 1024**3,
            "swap_used_bytes": 2 * 1024**3,
            "swap_free_bytes": 6 * 1024**3,
            "ac_power": True, "thermal_normal": True,
            "thermal_warning_level": 0, "performance_warning_level": 0}

        def disk_usage(path):
            if str(path) in ("/System/Volumes/Data", "/System/Volumes/VM"):
                return SimpleNamespace(free=60 * 1024**3)
            return real_disk_usage(path)

        with mock.patch.object(engine, "_trusted_reviewer_fingerprint",
                               return_value=self.fingerprint), \
             mock.patch.object(engine, "_formal_runner_command",
                               side_effect=runner_factory), \
             mock.patch.object(watchdog, "sample_macos_native_state",
                               return_value=native), \
             mock.patch.object(watchdog.shutil, "disk_usage", side_effect=disk_usage):
            yield

    def _formal_stub_factory(self, root: Path, script: Path, action: str):
        def factory(run_dir, policy_path, policy_sha, approval_path,
                    public_key_path, max_attempts):
            return [sys.executable, str(script), str(engine.MODULE_DIR),
                    str(run_dir), action]
        return factory

    @unittest.skipUnless(sys.platform == "darwin" and platform.machine() == "arm64",
                         "formal macOS V2 launch rehearsal requires Apple Silicon")
    def test_v2_formal_launcher_end_to_end_with_nonformal_scheduler_result_and_ledger(self):
        with tempfile.TemporaryDirectory(prefix="nc0a-v2-launch-e2e-") as tmp:
            root = Path(tmp)
            policy, approval, public_key, run_dir, signed_policy = \
                self.make_formal_v2_test_authorization(root)
            script = self.make_science_stub(root)
            factory = self._formal_stub_factory(root, script, "success")
            with self.formal_v2_test_runtime(factory):
                result = engine.launch_formal(policy, approval, public_key, run_dir)
            self.assertEqual(result["watchdog"]["status"], "completed")
            summary = json.loads((run_dir / "test_battery_summary.json").read_text())
            self.assertEqual(summary["status"], "TEST_ONLY_NOT_FORMAL_NC0A")
            self.assertEqual(summary["mixing_status"], "MIXING-UNRESOLVED")
            case_path = run_dir / "cases/er-like-20/attempt-01/result.json"
            report_bytes = case_path.read_bytes()
            report = json.loads(report_bytes)
            self.assertEqual(report["seed_root"], engine.ENGINEERING_TEST_SEED_ROOT)
            self.assertEqual(report["mixing_status"], "MIXING-UNRESOLVED")
            self.assertEqual(Path(str(case_path) + ".sha256").read_text().split()[0],
                             hashlib.sha256(report_bytes).hexdigest())
            audit_path = run_dir / "watchdog.jsonl"
            _, tip = engine.verify_hash_chain(audit_path)
            with AuthorityLedger(
                    root / "external-ledger/authority.jsonl",
                    root / "external-tip/tip.json") as ledger:
                self.assertEqual(ledger.audit_anchors(signed_policy["formal_experiment_id"]),
                                 [tip])
                events = [row["event"] for row in ledger.records]
            audit_events = [json.loads(line)["event"]["event"]
                            for line in audit_path.read_text().splitlines()]
            self.assertEqual(audit_events[0], "run_started")
            self.assertEqual(audit_events[-1], "runner_exited")
            self.assertTrue(any(e.get("event") == "run_completed" for e in events))
            self.assertGreater(result["watchdog"]["usage"]["wall_seconds"], 0)

    @unittest.skipUnless(sys.platform == "darwin" and platform.machine() == "arm64",
                         "formal macOS V3 launch rehearsal requires Apple Silicon")
    def test_v3_formal_launcher_uses_signed_swap_telemetry_and_vm_reserve(self):
        with tempfile.TemporaryDirectory(prefix="nc0a-v3-launch-e2e-") as tmp:
            root = Path(tmp)
            policy, approval, public_key, run_dir, signed_policy = \
                self.make_formal_v3_test_authorization(root)
            script = self.make_science_stub(root)
            factory = self._formal_stub_factory(root, script, "success")
            # The low current-pool `free` value proves V3 does not retain the
            # obsolete V2 gate. This is mocked telemetry under a test key only.
            low_free_swap = {"swap_total_bytes": 8 * 1024**3,
                             "swap_used_bytes": 8 * 1024**3 - 256 * 1024**2,
                             "swap_free_bytes": 256 * 1024**2,
                             "ac_power": True, "thermal_normal": True,
                             "thermal_warning_level": 0, "performance_warning_level": 0}
            with self.formal_v2_test_runtime(factory, native_state=low_free_swap):
                result = engine.launch_formal(policy, approval, public_key, run_dir)
            self.assertEqual(result["watchdog"]["status"], "completed")
            self.assertEqual(result["watchdog"]["usage"]["memory_enforcement"],
                             "MACOS_SAMPLED_PRESSURE_NOT_HARD")
            summary = json.loads((run_dir / "test_battery_summary.json").read_text())
            self.assertEqual(summary["status"], "TEST_ONLY_NOT_FORMAL_NC0A")
            self.assertEqual(summary["mixing_status"], "MIXING-UNRESOLVED")
            case_path = run_dir / "cases/er-like-20/attempt-01/result.json"
            report = json.loads(case_path.read_text())
            self.assertEqual(report["seed_root"], engine.ENGINEERING_TEST_SEED_ROOT)
            self.assertTrue(Path(str(case_path) + ".sha256").is_file())
            _, tip = engine.verify_hash_chain(run_dir / "watchdog.jsonl")
            with AuthorityLedger(
                    root / "external-ledger/authority.jsonl",
                    root / "external-tip/tip.json") as ledger:
                self.assertEqual(ledger.audit_anchors(signed_policy["formal_experiment_id"]),
                                 [tip])
                self.assertTrue(any(
                    row["event"].get("event") == "run_completed"
                    for row in ledger.records))

    @unittest.skipUnless(sys.platform == "darwin" and platform.machine() == "arm64",
                         "formal macOS V2 launch rehearsal requires Apple Silicon")
    def test_v2_formal_launcher_accounts_worker_crash_and_recovers_same_signed_run(self):
        with tempfile.TemporaryDirectory(prefix="nc0a-v2-recovery-e2e-") as tmp:
            root = Path(tmp)
            policy, approval, public_key, run_dir, signed_policy = \
                self.make_formal_v2_test_authorization(root)
            script = self.make_science_stub(root)
            calls = 0

            def factory(run, policy_path, policy_sha, approval_path, key_path, attempts):
                nonlocal calls
                calls += 1
                action = "worker-crash" if calls == 1 else "success"
                return [sys.executable, str(script), str(engine.MODULE_DIR),
                        str(run), action]

            with self.formal_v2_test_runtime(factory):
                first = engine.launch_formal(policy, approval, public_key, run_dir)
                second = engine.launch_formal(policy, approval, public_key, run_dir)
            self.assertEqual(first["watchdog"]["status"], "failed")
            self.assertGreater(first["watchdog"]["usage"]["cpu_seconds"], 0)
            self.assertEqual(second["invocation"], 2)
            self.assertEqual(second["watchdog"]["status"], "completed")
            recovered = json.loads((run_dir / "cases/er-like-20/attempt-02/result.json").read_text())
            self.assertEqual(recovered["attempt"], 2)
            self.assertEqual(recovered["seed_root"], engine.ENGINEERING_TEST_SEED_ROOT)
            self.assertEqual(recovered["mixing_status"], "MIXING-UNRESOLVED")
            self.assertTrue((run_dir / "cases/er-like-20/attempt-01").is_dir())
            _, tip = engine.verify_hash_chain(run_dir / "watchdog.jsonl")
            with AuthorityLedger(
                    root / "external-ledger/authority.jsonl",
                    root / "external-tip/tip.json") as ledger:
                self.assertEqual(ledger.audit_anchors(signed_policy["formal_experiment_id"])[-1], tip)
                finishes = [row["event"] for row in ledger.records
                            if row["event"].get("event") == "invocation_finished"]
            self.assertEqual([row["status"] for row in finishes], ["failed", "completed"])
            self.assertGreater(sum(row["usage"]["wall_seconds"] for row in finishes),
                               first["watchdog"]["usage"]["wall_seconds"])

    @unittest.skipUnless(sys.platform == "darwin" and platform.machine() == "arm64",
                         "formal macOS V2 launch rehearsal requires Apple Silicon")
    def test_v2_formal_launcher_enforces_wall_budget_and_records_nonzero_cost(self):
        with tempfile.TemporaryDirectory(prefix="nc0a-v2-budget-e2e-") as tmp:
            root = Path(tmp)
            policy, approval, public_key, run_dir, signed_policy = \
                self.make_formal_v2_test_authorization(
                    root, wall_seconds=5, cpu_seconds=600, attempts=1)
            script = self.make_science_stub(root)
            factory = self._formal_stub_factory(root, script, "wall-overrun")
            with self.formal_v2_test_runtime(factory):
                result = engine.launch_formal(policy, approval, public_key, run_dir)
            self.assertEqual(result["watchdog"]["status"], "stopped")
            self.assertEqual(result["watchdog"]["reason"], "WALL_LIMIT")
            self.assertGreater(result["watchdog"]["usage"]["wall_seconds"], 0)
            with AuthorityLedger(
                    root / "external-ledger/authority.jsonl",
                    root / "external-tip/tip.json") as ledger:
                finish = [row["event"] for row in ledger.records
                          if row["event"].get("event") == "invocation_finished"]
            self.assertEqual(len(finish), 1)
            self.assertEqual(finish[0]["status"], "stopped")
            self.assertGreater(finish[0]["usage"]["wall_seconds"], 0)

    @unittest.skipUnless(sys.platform == "darwin" and platform.machine() == "arm64",
                         "formal macOS V2 launch rehearsal requires Apple Silicon")
    def test_v2_formal_launcher_rejects_bad_test_signature_before_ledger_start(self):
        with tempfile.TemporaryDirectory(prefix="nc0a-v2-signature-e2e-") as tmp:
            root = Path(tmp)
            policy, approval, public_key, run_dir, signed_policy = \
                self.make_formal_v2_test_authorization(root)
            payload = json.loads(approval.read_text())
            payload["signature_ed25519_base64"] = base64.b64encode(b"not-a-signature").decode()
            approval.write_bytes(canonical(payload) + b"\n")
            script = self.make_science_stub(root)
            factory = self._formal_stub_factory(root, script, "success")
            with self.formal_v2_test_runtime(factory), self.assertRaisesRegex(
                    ExecutionError, "signature did not verify"):
                engine.launch_formal(policy, approval, public_key, run_dir)
            with AuthorityLedger(
                    root / "external-ledger/authority.jsonl",
                    root / "external-tip/tip.json") as ledger:
                self.assertEqual(ledger.records, [])
            self.assertFalse((run_dir / "watchdog.jsonl").exists())

    def test_signed_test_only_launch_repeats_2_4_8_spawn_workers_under_watchdog(self):
        for workers in (2, 4, 8):
            for repetition in range(3):
                with self.subTest(workers=workers, repetition=repetition), \
                     tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    policy, approval, public_key, run_dir = self.make_authorization(
                        root, workers=workers)
                    with self.trusted_test_key():
                        result = launch_test_only(policy, approval, public_key, run_dir)
                    watchdog = result["watchdog"]
                    self.assertEqual(watchdog["status"], "completed", watchdog)
                    usage = watchdog["usage"]
                    self.assertEqual(usage["peak_compute_workers"], workers)
                    self.assertGreaterEqual(usage["peak_resource_trackers"], 1)
                    self.assertGreater(usage["peak_process_group_members"], workers + 1)
                    self.assertEqual(usage["memory_enforcement"], "SAMPLED_ONLY_NOT_HARD")
                    summary = json.loads((run_dir / "test_battery_summary.json").read_text())
                    case_path = run_dir / "cases/er-like-20/attempt-01/result.json"
                    case_bytes = case_path.read_bytes()
                    case = json.loads(case_bytes)
                    self.assertEqual(summary["status"], "TEST_ONLY_NOT_FORMAL_NC0A")
                    self.assertEqual(case["attempt"], 1)
                    self.assertEqual(case["oracle"]["attempts"], 1000)
                    self.assertEqual(len(case["chains"]), 8)
                    self.assertEqual(case["seed_root"], engine.ENGINEERING_TEST_SEED_ROOT)
                    self.assertEqual(case["mixing_status"], "MIXING-UNRESOLVED")
                    self.assertEqual(case["screen"]["mixing_status"], "MIXING-UNRESOLVED")
                    self.assertEqual(
                        Path(str(case_path) + ".sha256").read_text().split()[0],
                        hashlib.sha256(case_bytes).hexdigest())
                    with self.assertRaisesRegex(AuthorityLedgerError, "already complete"):
                        with AuthorityLedger(
                            root / "external-authority/ledger/authority.jsonl",
                            root / "external-authority/anchor/tip.json") as ledger:
                            ledger.begin(
                                experiment_id=json.loads(policy.read_text())["test_experiment_id"],
                                run_dir=run_dir,
                                policy_sha256=hashlib.sha256(policy.read_bytes()).hexdigest(),
                                approval_sha256=hashlib.sha256(approval.read_bytes()).hexdigest(),
                                wall_budget_seconds=120, cpu_budget_seconds=600,
                                max_invocations=1)
                    # The same signature cannot create a second result directory.
                    with self.trusted_test_key(), self.assertRaisesRegex(
                            AuthorityLedgerError, "another run"):
                        launch_test_only(policy, approval, public_key, root / "run-two")

    def test_worker_crash_is_accounted_then_same_run_recovers_with_fixed_seeds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            policy, approval, public_key, run_dir = self.make_authorization(
                root, workers=4, fault="worker_crash")
            with self.trusted_test_key():
                first = launch_test_only(policy, approval, public_key, run_dir)
            self.assertEqual(first["invocation"], 1)
            self.assertIn(first["watchdog"]["status"], ("failed", "stopped"))
            self.assertGreaterEqual(first["watchdog"]["usage"]["cpu_seconds"], 0)
            self.assertFalse((run_dir / "test_battery_summary.json").exists())
            self.assertFalse((run_dir / "cases/er-like-20/attempt-01/result.json").exists())
            with self.trusted_test_key():
                second = launch_test_only(policy, approval, public_key, run_dir)
            self.assertEqual(second["invocation"], 2)
            self.assertEqual(second["prior_usage"]["wall_seconds"],
                             first["watchdog"]["usage"]["wall_seconds"])
            self.assertEqual(second["watchdog"]["status"], "completed", second["watchdog"])
            result = json.loads((run_dir / "cases/er-like-20/attempt-02/result.json").read_text())
            self.assertEqual(result["attempt"], 2)
            self.assertEqual(result["seed_root"], engine.ENGINEERING_TEST_SEED_ROOT)
            self.assertEqual(result["mixing_status"], "MIXING-UNRESOLVED")

    def test_signed_extra_compute_worker_is_really_killed_above_cap(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            policy, approval, public_key, run_dir = self.make_authorization(
                root, workers=4, fault="extra_compute_worker")
            with self.trusted_test_key():
                result = launch_test_only(policy, approval, public_key, run_dir)
            self.assertEqual(result["watchdog"]["status"], "stopped")
            self.assertEqual(result["watchdog"]["reason"], "WORKER_CONCURRENCY_LIMIT")
            self.assertGreater(result["watchdog"]["usage"]["peak_compute_workers"], 4)

    def test_invalid_signature_wrong_head_tampered_budget_and_missing_anchor_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            policy_path, approval_path, public_key, run_dir = self.make_authorization(root)
            with self.trusted_test_key():
                approval = json.loads(approval_path.read_text())
                approval["signature_ed25519_base64"] = base64.b64encode(b"bad-signature").decode()
                approval_path.write_bytes(canonical(approval) + b"\n")
                with self.assertRaisesRegex(ExecutionError, "signature did not verify"):
                    launch_test_only(policy_path, approval_path, public_key, run_dir)

                policy_path, approval_path, public_key, run_dir = self.make_authorization(root / "head")
                approval = json.loads(approval_path.read_text())
                approval["target_repository_head_sha"] = "f" * 40
                approval_path.write_bytes(canonical(approval) + b"\n")
                with self.assertRaisesRegex(ExecutionError, "current repository HEAD"):
                    launch_test_only(policy_path, approval_path, public_key, run_dir)

                policy_path, approval_path, public_key, run_dir = self.make_authorization(root / "budget")
                policy = json.loads(policy_path.read_text())
                policy["limits"]["absolute_wall_seconds"] = 121
                policy_path.write_bytes(canonical(policy) + b"\n")
                with self.assertRaisesRegex(ExecutionError, "exact resource policy"):
                    launch_test_only(policy_path, approval_path, public_key, run_dir)

                policy_path, approval_path, public_key, run_dir = self.make_authorization(root / "trust")
                with mock.patch.dict(os.environ, {}, clear=True):
                    with self.assertRaisesRegex(ExecutionError, "test-only trust anchor"):
                        launch_test_only(policy_path, approval_path, public_key, run_dir)

    def test_formal_signature_verifier_returns_raw_policy_not_validation_summary(self):
        from test_nc0a_budget_preflight import toy_policy
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            policy = toy_policy()
            policy["target_repository_head_sha"] = engine._git_head()
            policy["runtime_dependency_lock_sha256"] = hashlib.sha256(
                engine.RUNTIME_LOCK.read_bytes()).hexdigest()
            policy_path = root / "formal-policy.json"
            policy_path.write_bytes(canonical(policy) + b"\n")
            approval = {
                "purpose": engine.APPROVAL_PURPOSE,
                "decision": "APPROVED_FOR_FORMAL_NC0A",
                "policy_sha256": hashlib.sha256(policy_path.read_bytes()).hexdigest(),
                "target_repository_head_sha": engine._git_head(),
                "formal_experiment_id": policy["formal_experiment_id"],
                "preregistration_sha256": hashlib.sha256(
                    engine.PREREGISTRATION.read_bytes()).hexdigest(),
                "protocol_sha256": engine._protocol_hash(),
                "protocol": engine.PROTOCOL,
                "watchdog_contract_sha256": engine._watchdog_contract_hash(),
                "watchdog_contract": engine.WATCHDOG_CONTRACT,
                "watchdog_source_sha256": engine._watchdog_source_hash(),
                "resource_limits": policy["limits"],
                "independent_reviewer": "Temporary test signer; not a real approval",
                "independent_review_url": "https://example.invalid/test-only",
                "operational_attempts_per_case": 1,
                "retry_rule": engine.PROTOCOL["recovery"],
            }
            payload = root / "formal-approval.payload"
            signature = root / "formal-approval.signature"
            approval_path = root / "formal-approval.json"
            payload.write_bytes(canonical(approval))
            subprocess.run(["openssl", "pkeyutl", "-sign", "-inkey",
                            str(self.private_key), "-rawin", "-in", str(payload),
                            "-out", str(signature)], check=True, capture_output=True)
            approval["signature_ed25519_base64"] = base64.b64encode(
                signature.read_bytes()).decode("ascii")
            approval_path.write_bytes(canonical(approval) + b"\n")
            with mock.patch.object(engine, "_trusted_reviewer_fingerprint",
                                   return_value=self.fingerprint), \
                 mock.patch.object(engine, "_assert_clean_source_tree"), \
                 mock.patch.object(engine, "_verify_runtime_lock"), \
                 mock.patch.object(engine, "_git_head", return_value=policy["target_repository_head_sha"]):
                returned_policy, returned_approval = engine._verify_approval(
                    policy_path, approval_path, self.public_key)
            self.assertEqual(returned_policy, policy)
            self.assertEqual(returned_policy["limits"], policy["limits"])
            self.assertEqual(returned_approval["resource_limits"], policy["limits"])
            self.assertNotIn("limits_recorded", returned_policy)

    def test_macos_v2_signature_binds_amendment_and_non_hard_memory_semantics(self):
        from test_nc0a_budget_preflight import macos_policy
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            policy = macos_policy()
            head = engine._git_head()
            policy["target_repository_head_sha"] = head
            policy["runtime_dependency_lock_sha256"] = hashlib.sha256(
                engine.RUNTIME_LOCK.read_bytes()).hexdigest()
            policy_path = root / "macos-policy.json"
            policy_path.write_bytes(canonical(policy) + b"\n")
            approval = {
                "purpose": engine.MACOS_APPROVAL_PURPOSE,
                "decision": "APPROVED_FOR_FORMAL_NC0A",
                "policy_sha256": hashlib.sha256(policy_path.read_bytes()).hexdigest(),
                "target_repository_head_sha": head,
                "formal_experiment_id": policy["formal_experiment_id"],
                "preregistration_sha256": hashlib.sha256(
                    engine.PREREGISTRATION.read_bytes()).hexdigest(),
                "protocol_sha256": engine._protocol_hash(),
                "protocol": engine.PROTOCOL,
                "watchdog_contract_sha256": engine._watchdog_contract_hash(),
                "watchdog_contract": engine.WATCHDOG_CONTRACT,
                "watchdog_source_sha256": engine._watchdog_source_hash(),
                "resource_limits": policy["limits"],
                "independent_reviewer": "Temporary test signer; not a real approval",
                "independent_review_url": "https://example.invalid/test-only",
                "operational_attempts_per_case": 1,
                "retry_rule": engine.PROTOCOL["recovery"],
                "resource_amendment_status": policy["resource_amendment_status"],
                "resource_amendment_approver": policy["resource_amendment_approver"],
                "resource_amendment_sha256": policy["resource_amendment_sha256"],
                "resource_amendment_approval_record_url":
                    policy["resource_amendment_approval_record_url"],
                "macos_memory_semantics": policy["memory_limit_semantics"],
                "macos_residual_risk_acceptance":
                    policy["macos_residual_risk_acceptance"],
                "reviewer_key_fingerprint_sha256": self.fingerprint,
            }
            payload = root / "macos-approval.payload"
            signature = root / "macos-approval.signature"
            approval_path = root / "macos-approval.json"
            payload.write_bytes(canonical(approval))
            subprocess.run(["openssl", "pkeyutl", "-sign", "-inkey",
                            str(self.private_key), "-rawin", "-in", str(payload),
                            "-out", str(signature)], check=True, capture_output=True)
            approval["signature_ed25519_base64"] = base64.b64encode(
                signature.read_bytes()).decode("ascii")
            approval_path.write_bytes(canonical(approval) + b"\n")
            with mock.patch.object(engine, "_trusted_reviewer_fingerprint",
                                   return_value=self.fingerprint), \
                 mock.patch.object(engine, "_assert_clean_source_tree"), \
                 mock.patch.object(engine, "_verify_runtime_lock"), \
                 mock.patch.object(engine, "_git_head", return_value=head):
                returned_policy, returned_approval = engine._verify_approval(
                    policy_path, approval_path, self.public_key)
            self.assertEqual(returned_policy["memory_enforcement_backend"],
                             "MACOS_SAMPLED_PRESSURE")
            self.assertEqual(returned_approval["macos_memory_semantics"],
                             "SAMPLED_RSS_AND_HOST_PRESSURE_ABORTS_ONLY_NOT_OS_HARD_LIMIT")
            self.assertEqual(returned_approval["reviewer_key_fingerprint_sha256"],
                             self.fingerprint)

    def test_macos_v3_signature_binds_current_swap_pool_semantics(self):
        from test_nc0a_budget_preflight import macos_v3_policy
        from nc0a_budget_preflight import MACOS_SWAP_TELEMETRY_SEMANTICS
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            policy = macos_v3_policy()
            head = engine._git_head()
            policy["target_repository_head_sha"] = head
            policy["runtime_dependency_lock_sha256"] = hashlib.sha256(
                engine.RUNTIME_LOCK.read_bytes()).hexdigest()
            policy_path = root / "macos-v3-policy.json"
            policy_path.write_bytes(canonical(policy) + b"\n")
            approval = {
                "purpose": engine.MACOS_V3_APPROVAL_PURPOSE,
                "decision": "APPROVED_FOR_FORMAL_NC0A",
                "policy_sha256": hashlib.sha256(policy_path.read_bytes()).hexdigest(),
                "target_repository_head_sha": head,
                "formal_experiment_id": policy["formal_experiment_id"],
                "preregistration_sha256": hashlib.sha256(
                    engine.PREREGISTRATION.read_bytes()).hexdigest(),
                "protocol_sha256": engine._protocol_hash(),
                "protocol": engine.PROTOCOL,
                "watchdog_contract_sha256": engine._watchdog_contract_hash(),
                "watchdog_contract": engine.WATCHDOG_CONTRACT,
                "watchdog_source_sha256": engine._watchdog_source_hash(),
                "resource_limits": policy["limits"],
                "independent_reviewer": "Temporary test signer; not a real approval",
                "independent_review_url": "https://example.invalid/test-only",
                "operational_attempts_per_case": 1,
                "retry_rule": engine.PROTOCOL["recovery"],
                "resource_amendment_status": policy["resource_amendment_status"],
                "resource_amendment_approver": policy["resource_amendment_approver"],
                "resource_amendment_sha256": policy["resource_amendment_sha256"],
                "resource_amendment_approval_record_url":
                    policy["resource_amendment_approval_record_url"],
                "macos_memory_semantics": policy["memory_limit_semantics"],
                "macos_residual_risk_acceptance":
                    policy["macos_residual_risk_acceptance"],
                "reviewer_key_fingerprint_sha256": self.fingerprint,
                "macos_swap_telemetry_semantics": MACOS_SWAP_TELEMETRY_SEMANTICS,
            }
            payload = root / "macos-v3.payload"
            signature = root / "macos-v3.signature"
            approval_path = root / "macos-v3-approval.json"
            payload.write_bytes(canonical(approval))
            subprocess.run(["openssl", "pkeyutl", "-sign", "-inkey",
                            str(self.private_key), "-rawin", "-in", str(payload),
                            "-out", str(signature)], check=True, capture_output=True)
            approval["signature_ed25519_base64"] = base64.b64encode(
                signature.read_bytes()).decode("ascii")
            approval_path.write_bytes(canonical(approval) + b"\n")
            with mock.patch.object(engine, "_trusted_reviewer_fingerprint",
                                   return_value=self.fingerprint), \
                 mock.patch.object(engine, "_assert_clean_source_tree"), \
                 mock.patch.object(engine, "_verify_runtime_lock"), \
                 mock.patch.object(engine, "_git_head", return_value=head):
                returned, signed = engine._verify_approval(
                    policy_path, approval_path, self.public_key)
            self.assertEqual(returned["purpose"], "NC0A_FORMAL_SYNTHETIC_RESOURCE_POLICY_V3_MACOS")
            self.assertEqual(signed["macos_swap_telemetry_semantics"],
                             MACOS_SWAP_TELEMETRY_SEMANTICS)
            signed["macos_swap_telemetry_semantics"] = "FUTURE_PAGING_CAPACITY"
            approval_path.write_bytes(canonical(signed) + b"\n")
            with mock.patch.object(engine, "_trusted_reviewer_fingerprint",
                                   return_value=self.fingerprint), \
                 mock.patch.object(engine, "_assert_clean_source_tree"), \
                 mock.patch.object(engine, "_verify_runtime_lock"), \
                 mock.patch.object(engine, "_git_head", return_value=head), \
                 self.assertRaisesRegex(ExecutionError, "current-pool-only swap telemetry"):
                engine._verify_approval(policy_path, approval_path, self.public_key)

    def test_valid_hash_chain_with_deleted_terminal_is_rejected_by_external_anchor(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            policy, approval, public_key, run_dir = self.make_authorization(
                root, workers=4, fault="worker_crash")
            with self.trusted_test_key():
                result = launch_test_only(policy, approval, public_key, run_dir)
            self.assertIn(result["watchdog"]["status"], ("failed", "stopped"))
            audit = run_dir / "watchdog.jsonl"
            rows = audit.read_bytes().splitlines(keepends=True)
            self.assertGreaterEqual(len(rows), 2)
            audit.write_bytes(b"".join(rows[:-1]))  # valid complete-line prefix, but unanchored
            with self.trusted_test_key(), self.assertRaisesRegex(
                    ExecutionError, "truncated or differs from the external authority anchor"):
                launch_test_only(policy, approval, public_key, run_dir)

    def test_macOS_cannot_claim_hard_cgroup_memory_enforcement(self):
        if sys.platform != "darwin":
            self.skipTest("native cgroup-v2 refusal is macOS-specific")
        from nc0a_watchdog import validate_hard_memory_backend
        with self.assertRaisesRegex(WatchdogError, "requires Linux cgroup v2"):
            validate_hard_memory_backend("CGROUP_V2_HARD", 1024**3)


if __name__ == "__main__":
    unittest.main()
