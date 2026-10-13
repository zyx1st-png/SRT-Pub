"""All policy numbers are deliberately fictional UNIT-TEST fixtures, not budgets."""
import copy
import unittest

from nc0a_budget_preflight import ResourcePolicyError, validate_policy


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


if __name__ == "__main__":
    unittest.main()
