"""Validate an independently approved NC-0a resource policy, WITHOUT running it.

Pure planning/schema validation: even complete fields do NOT authorize execution.
H2 still needs the independent original PS-A active-time/host audit, and NC-0a
requires a separate signed-off formal run approval. No default resource numbers.

Usage: python nc0a_budget_preflight.py /PRIVATE/PATH/resource_policy.json
"""

from __future__ import annotations

import json
import math
from pathlib import Path
import re
import sys

from nc0a_contract_runner import FORMAL_N, CHAIN_COUNT, ORACLE_PROPOSALS
from synthetic_graphs import FAMILIES


class ResourcePolicyError(ValueError):
    pass


POSITIVE_INTEGERS = (
    "absolute_wall_seconds",
    "aggregate_cpu_seconds",
    "max_workers",
    "peak_aggregate_ram_bytes",
    "temporary_disk_allocation_bytes",
    "reserved_free_disk_bytes",
    "measured_baseline_free_disk_bytes",
    "measured_physical_ram_bytes",
    "case_timeout_seconds",
    "oracle_timeout_seconds",
)


def _positive_int(payload: dict, field: str) -> int:
    value = payload.get(field)
    if type(value) is not int or value <= 0:
        raise ResourcePolicyError(f"Missing/invalid positive integer: {field}")
    return value


def validate_policy(policy: dict) -> dict:
    if policy.get("purpose") != "NC0A_FORMAL_SYNTHETIC_RESOURCE_POLICY_V1":
        raise ResourcePolicyError("Wrong resource policy purpose")
    if policy.get("nc0a_protocol_decision") != "CONDITIONALLY_GO_AFTER_INDEPENDENT_REVIEW":
        raise ResourcePolicyError("Cannot silently claim an unconditional GO")
    for field in (
        "target_repository_head_sha",
        "host_identifier",
        "runtime_dependency_lock_sha256",
        "psa_evidence_report_sha256",
        "psa_active_time_review_url",
        "independent_methods_review_url",
        "budget_approver",
        "budget_approval_record_url",
        "baseline_measurement_utc",
    ):
        if not isinstance(policy.get(field), str) or not policy[field].strip():
            raise ResourcePolicyError("Missing approval/provenance field: " + field)
    if not re.fullmatch(r"[0-9a-f]{40}", policy["target_repository_head_sha"]):
        raise ResourcePolicyError("Target HEAD must be full SHA-1")
    for field in ("runtime_dependency_lock_sha256", "psa_evidence_report_sha256"):
        if not re.fullmatch(r"[0-9a-f]{64}", policy[field]):
            raise ResourcePolicyError("Invalid evidence SHA-256 for " + field)
    if policy.get("formal_run_completed") is not False:
        raise ResourcePolicyError("Pre-execution policy cannot claim an outcome")
    caps = policy.get("limits")
    if not isinstance(caps, dict):
        raise ResourcePolicyError("Missing aggregate resource limits")
    values = {key: _positive_int(caps, key) for key in POSITIVE_INTEGERS}
    if values["max_workers"] > 8:
        raise ResourcePolicyError("More than 8 workers prohibited")
    if values["peak_aggregate_ram_bytes"] >= 0.8 * values["measured_physical_ram_bytes"]:
        raise ResourcePolicyError("RAM limit must remain strictly below 80% of host RAM")
    if values["temporary_disk_allocation_bytes"] >= 0.7 * values["measured_baseline_free_disk_bytes"]:
        raise ResourcePolicyError("Temp disk limit must remain below 70% baseline free disk")
    if (values["temporary_disk_allocation_bytes"] + values["reserved_free_disk_bytes"]
        > values["measured_baseline_free_disk_bytes"]):
        raise ResourcePolicyError("Disk reservation exceeds measured free space")
    if values["case_timeout_seconds"] > values["absolute_wall_seconds"]:
        raise ResourcePolicyError("Per-case wall cap larger than overall wall cap")
    if values["oracle_timeout_seconds"] > values["absolute_wall_seconds"]:
        raise ResourcePolicyError("Oracle wall cap larger than overall cap")
    if not policy.get("case_failure_no_go", False):
        raise ResourcePolicyError("Fail-closed case/budget behavior is mandatory")
    if policy.get("retry_policy") != "NO_SILENT_RETRY_REQUIRES_NEW_REVIEW":
        raise ResourcePolicyError("No outcome-dependent missing-case replacement")
    sizes = tuple(FORMAL_N)
    expected_attempts = (
        sum(
            (8 * n if family != "ba-like" else (8 * n - 36)) * 32
            for n in sizes for family in FAMILIES
        ) * CHAIN_COUNT
    )
    if expected_attempts != 44_937_216:
        raise ResourcePolicyError("Synthetic workload changed unexpectedly")
    return {
        "status": "SCHEMA_VALID_ONLY_NOT_EXECUTION_AUTHORIZATION",
        "formal_cases": 16, "chains": 128,
        "long_chain_attempts": expected_attempts,
        "oracle_attempts": 16 * ORACLE_PROPOSALS,
        "limits_recorded": values,
        "review_head": policy["target_repository_head_sha"],
        "independent_approval_still_must_be_verified": True,
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python nc0a_budget_preflight.py /PRIVATE/resource_policy.json",
              file=sys.stderr)
        return 2
    try:
        policy = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        result = validate_policy(policy)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    except (ValueError, OSError, KeyError) as exc:
        print("FORMAL_NC0A_RESOURCE_NO_GO: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
