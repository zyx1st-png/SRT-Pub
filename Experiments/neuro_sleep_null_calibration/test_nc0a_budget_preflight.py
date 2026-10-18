"""All policy numbers are deliberately fictional UNIT-TEST fixtures, not budgets."""
import copy
import unittest

from nc0a_budget_preflight import (
    MACOS_MEMORY_SEMANTICS, MACOS_SWAP_TELEMETRY_SEMANTICS,
    POLICY_V2_MACOS, POLICY_V3_MACOS, ResourcePolicyError, validate_policy,
)


def toy_policy():
    return {
        "purpose": "NC0A_FORMAL_SYNTHETIC_RESOURCE_POLICY_V1",
        "nc0a_protocol_decision": "CONDITIONALLY_GO_AFTER_INDEPENDENT_REVIEW",
        "target_repository_head_sha": "a" * 40,
        "runtime_dependency_lock_sha256": "b" * 64,
        "psa_evidence_report_sha256": "c" * 64,
        "host_identifier": "TOY-SYNTHETIC-HOST",
        "psa_active_time_review_url": "https://example.invalid/not-an-approval",
        "independent_methods_review_url": "https://example.invalid/review",
        "budget_approver": "TEST FIXTURE, NOT A HUMAN APPROVAL",
        "budget_approval_record_url": "https://example.invalid/budget",
        "baseline_measurement_utc": "2026-10-12T00:00:00+00:00",
        "formal_experiment_id": "9c62f2e3-72bb-4d63-b68b-89202fe4bd85",
        "authority_ledger_path": "/tmp/nc0a-ledger/ledger.jsonl",
        "authority_anchor_path": "/tmp/nc0a-anchor/tip.json",
        "memory_enforcement_backend": "CGROUP_V2_HARD",
        "host_memory_free_percent_stop": 10,
        "formal_run_completed": False,
        "case_failure_no_go": True,
        "retry_policy": "NO_SILENT_RETRY_REQUIRES_NEW_REVIEW",
        "limits": {
            "absolute_wall_seconds": 5000,
            "aggregate_cpu_seconds": 15000,
            "max_workers": 4,
            "peak_aggregate_ram_bytes": 4000000000,
            "temporary_disk_allocation_bytes": 1000000000,
            "reserved_free_disk_bytes": 1000000000,
            "measured_baseline_free_disk_bytes": 10000000000,
            "measured_physical_ram_bytes": 8000000000,
            "case_timeout_seconds": 500,
            "oracle_timeout_seconds": 300,
        },
    }


def macos_policy():
    policy = toy_policy()
    policy.update({
        "purpose": POLICY_V2_MACOS,
        "memory_enforcement_backend": "MACOS_SAMPLED_PRESSURE",
        "host_memory_free_percent_stop": 20,
        "resource_amendment_status": "INDEPENDENTLY_APPROVED",
        "resource_amendment_approver": "Independent reviewer fixture, not a human approval",
        "resource_amendment_approval_record_url": "https://example.invalid/amendment-review",
        "resource_amendment_sha256": "d" * 64,
        "memory_limit_semantics": MACOS_MEMORY_SEMANTICS,
        "macos_residual_risk_acceptance":
            "TRANSIENT_RSS_PEAK_MAY_BE_MISSED_OS_OOM_AND_APP_DISRUPTION_REMAIN",
        "macos_boot_volume_path": "/System/Volumes/Data",
        "require_ac_power": True,
        "require_thermal_normal": True,
        "require_sleep_assertion": True,
    })
    policy["limits"].update({
        "absolute_wall_seconds": 72 * 3600,
        "aggregate_cpu_seconds": 288 * 3600,
        "max_workers": 4,
        "peak_aggregate_ram_bytes": 4 * 1024**3,
        "temporary_disk_allocation_bytes": 4 * 1024**3,
        "reserved_free_disk_bytes": 30 * 1024**3,
        "measured_baseline_free_disk_bytes": 40 * 1024**3,
        "measured_physical_ram_bytes": 16 * 1024**3,
        "case_timeout_seconds": 12 * 3600,
        "oracle_timeout_seconds": 1800,
        "boot_reserve_free_disk_bytes": 30 * 1024**3,
        "minimum_boot_free_disk_bytes": 40 * 1024**3,
        "swap_growth_stop_bytes": 2 * 1024**3,
        "swap_free_stop_bytes": 1 * 1024**3,
        "minimum_swap_free_bytes": 2 * 1024**3,
    })
    return policy


def macos_v3_policy():
    policy = macos_policy()
    policy["purpose"] = POLICY_V3_MACOS
    policy["macos_swap_volume_path"] = "/System/Volumes/VM"
    policy["macos_swap_telemetry_semantics"] = MACOS_SWAP_TELEMETRY_SEMANTICS
    policy["limits"].pop("minimum_swap_free_bytes")
    policy["limits"].pop("swap_free_stop_bytes")
    policy["limits"].update({
        "swap_volume_reserve_free_disk_bytes": 30 * 1024**3,
        "minimum_swap_volume_free_disk_bytes": 40 * 1024**3,
    })
    return policy


class BudgetPreflightTests(unittest.TestCase):
    def test_toy_policy_only_passes_schema_never_authorizes(self):
        result = validate_policy(toy_policy())
        self.assertEqual(result["status"],
                         "SCHEMA_VALID_ONLY_NOT_EXECUTION_AUTHORIZATION")
        self.assertEqual(result["long_chain_attempts"], 44937216)
        self.assertEqual(result["oracle_attempts"], 16000)
        self.assertTrue(result["independent_approval_still_must_be_verified"])

    def test_missing_actual_resource_limit_fails(self):
        p = toy_policy()
        del p["limits"]["aggregate_cpu_seconds"]
        with self.assertRaises(ResourcePolicyError):
            validate_policy(p)

    def test_memory_disk_and_worker_caps_fail_closed(self):
        for key, value in (("peak_aggregate_ram_bytes", 6400000000),
                           ("temporary_disk_allocation_bytes", 7000000000),
                           ("max_workers", 9)):
            with self.subTest(key=key):
                p = toy_policy()
                p["limits"][key] = value
                with self.assertRaises(ResourcePolicyError):
                    validate_policy(p)

    def test_missing_review_provenance_fails(self):
        p = toy_policy()
        p["psa_active_time_review_url"] = ""
        with self.assertRaises(ResourcePolicyError):
            validate_policy(p)

    def test_no_silent_retry_or_prior_outcome(self):
        p = toy_policy()
        p["retry_policy"] = "RETRY_TO_PASS"
        with self.assertRaises(ResourcePolicyError):
            validate_policy(p)
        p = toy_policy()
        p["formal_run_completed"] = True
        with self.assertRaises(ResourcePolicyError):
            validate_policy(p)

    def test_macos_v2_schema_preserves_non_hard_memory_semantics(self):
        policy = macos_policy()
        result = validate_policy(policy)
        self.assertEqual(result["memory_enforcement_backend"], "MACOS_SAMPLED_PRESSURE")
        self.assertEqual(result["memory_limit_semantics"], MACOS_MEMORY_SEMANTICS)
        self.assertTrue(result["independent_approval_still_must_be_verified"])

    def test_macos_policy_rejects_unapproved_amendment_weak_limits_and_more_workers(self):
        for mutate in (
            lambda p: p.update(resource_amendment_status="DRAFT"),
            lambda p: p.update(memory_limit_semantics="HARD_MEMORY_LIMIT"),
            lambda p: p["limits"].update(max_workers=5),
            lambda p: p["limits"].update(minimum_boot_free_disk_bytes=39 * 1024**3),
            lambda p: p["limits"].update(swap_free_stop_bytes=2 * 1024**3),
            lambda p: p["limits"].update(minimum_swap_free_bytes=1536 * 1024**2),
            lambda p: p.update(require_sleep_assertion=False),
        ):
            with self.subTest(mutation=mutate), self.assertRaises(ResourcePolicyError):
                policy = macos_policy()
                mutate(policy)
                validate_policy(policy)

    def test_prospective_macos_v3_uses_swap_growth_and_vm_disk_not_free_swap_headroom(self):
        policy = macos_v3_policy()
        result = validate_policy(policy)
        self.assertEqual(result["resource_policy_version"], POLICY_V3_MACOS)
        self.assertEqual(result["swap_telemetry_semantics"], MACOS_SWAP_TELEMETRY_SEMANTICS)
        self.assertTrue(result["independent_approval_still_must_be_verified"])

    def test_macos_v3_rejects_free_swap_gates_or_missing_vm_reserve(self):
        for mutate in (
            lambda p: p["limits"].update(minimum_swap_free_bytes=2 * 1024**3),
            lambda p: p["limits"].pop("swap_volume_reserve_free_disk_bytes"),
            lambda p: p.update(macos_swap_telemetry_semantics="FUTURE_CAPACITY"),
            lambda p: p["limits"].update(minimum_swap_volume_free_disk_bytes=39 * 1024**3),
        ):
            with self.subTest(mutation=mutate), self.assertRaises(ResourcePolicyError):
                policy = macos_v3_policy()
                mutate(policy)
                validate_policy(policy)


if __name__ == "__main__":
    unittest.main()
