"""End-to-end signed toy-only launch tests; never authorizes a formal workload."""

from __future__ import annotations

import base64
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
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
                canonical(engine._environment(engine._git_head()))).hexdigest(),
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
