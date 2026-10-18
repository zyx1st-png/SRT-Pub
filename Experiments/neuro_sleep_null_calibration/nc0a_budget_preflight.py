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
import uuid

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

POLICY_V1 = "NC0A_FORMAL_SYNTHETIC_RESOURCE_POLICY_V1"
POLICY_V2_MACOS = "NC0A_FORMAL_SYNTHETIC_RESOURCE_POLICY_V2_MACOS"
POLICY_V3_MACOS = "NC0A_FORMAL_SYNTHETIC_RESOURCE_POLICY_V3_MACOS"
MACOS_MEMORY_SEMANTICS = "SAMPLED_RSS_AND_HOST_PRESSURE_ABORTS_ONLY_NOT_OS_HARD_LIMIT"
MACOS_SWAP_TELEMETRY_SEMANTICS = (
    "CURRENT_CONFIGURED_SWAP_POOL_USAGE_TELEMETRY_ONLY_NOT_FUTURE_PAGING_CAPACITY")
MIN_MACOS_BOOT_FREE_BYTES = 40 * 1024**3
MIN_MACOS_BOOT_RESERVE_BYTES = 30 * 1024**3
MIN_MACOS_SWAP_VOLUME_RESERVE_BYTES = 30 * 1024**3
MIN_MACOS_SWAP_FREE_BYTES = 2 * 1024**3
MIN_MACOS_SWAP_FREE_STOP_BYTES = 1 * 1024**3


def _positive_int(payload: dict, field: str) -> int:
    value = payload.get(field)
    if type(value) is not int or value <= 0:
        raise ResourcePolicyError(f"Missing/invalid positive integer: {field}")
    return value


def validate_policy(policy: dict) -> dict:
    purpose = policy.get("purpose")
    if purpose not in (POLICY_V1, POLICY_V2_MACOS, POLICY_V3_MACOS):
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
        "formal_experiment_id",
        "authority_ledger_path",
        "authority_anchor_path",
        "memory_enforcement_backend",
    ):
        if not isinstance(policy.get(field), str) or not policy[field].strip():
            raise ResourcePolicyError("Missing approval/provenance field: " + field)
    if not re.fullmatch(r"[0-9a-f]{40}", policy["target_repository_head_sha"]):
        raise ResourcePolicyError("Target HEAD must be full SHA-1")
    try:
        if str(uuid.UUID(policy["formal_experiment_id"])) != policy["formal_experiment_id"]:
            raise ValueError
    except (ValueError, AttributeError) as exc:
        raise ResourcePolicyError("formal_experiment_id must be a canonical UUID") from exc
    ledger_path = Path(policy["authority_ledger_path"])
    anchor_path = Path(policy["authority_anchor_path"])
    if (not ledger_path.is_absolute() or not anchor_path.is_absolute() or
        ledger_path == anchor_path or ledger_path.parent == anchor_path.parent):
        raise ResourcePolicyError(
            "Authority ledger and independent anchor must be absolute paths in separate directories")
    backend = policy["memory_enforcement_backend"]
    if purpose == POLICY_V1 and backend != "CGROUP_V2_HARD":
        raise ResourcePolicyError("Policy V1 is reserved for the cgroup-v2 hard-memory backend")
    if purpose in (POLICY_V2_MACOS, POLICY_V3_MACOS) and backend != "MACOS_SAMPLED_PRESSURE":
        raise ResourcePolicyError("Policy V2 is reserved for the explicit macOS sampled-pressure backend")
    if (type(policy.get("host_memory_free_percent_stop")) is not int or
        not 1 <= policy["host_memory_free_percent_stop"] <= 100):
        raise ResourcePolicyError(
            "Host memory pressure stop threshold must be an explicit integer percentage")
    for field in ("runtime_dependency_lock_sha256", "psa_evidence_report_sha256"):
        if not re.fullmatch(r"[0-9a-f]{64}", policy[field]):
            raise ResourcePolicyError("Invalid evidence SHA-256 for " + field)
    if policy.get("formal_run_completed") is not False:
        raise ResourcePolicyError("Pre-execution policy cannot claim an outcome")
    caps = policy.get("limits")
    if not isinstance(caps, dict):
        raise ResourcePolicyError("Missing aggregate resource limits")
    values = {key: _positive_int(caps, key) for key in POSITIVE_INTEGERS}
    if values["max_workers"] > (4 if backend == "MACOS_SAMPLED_PRESSURE" else 8):
        raise ResourcePolicyError("Worker cap exceeds the selected resource backend")
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
    if backend == "MACOS_SAMPLED_PRESSURE":
        for name in ("resource_amendment_approver", "resource_amendment_approval_record_url",
                     "memory_limit_semantics", "macos_residual_risk_acceptance",
                     "macos_boot_volume_path"):
            if not isinstance(policy.get(name), str) or not policy[name].strip():
                raise ResourcePolicyError("Missing macOS amendment/limitation field: " + name)
        if policy.get("resource_amendment_status") != "INDEPENDENTLY_APPROVED":
            raise ResourcePolicyError("macOS resource amendment has not received independent approval")
        if not re.fullmatch(r"[0-9a-f]{64}", policy.get("resource_amendment_sha256", "")):
            raise ResourcePolicyError("macOS resource amendment SHA-256 is required")
        if not policy["resource_amendment_approval_record_url"].startswith("https://"):
            raise ResourcePolicyError("macOS amendment approval must reference an external review record")
        if policy["memory_limit_semantics"] != MACOS_MEMORY_SEMANTICS:
            raise ResourcePolicyError("macOS RSS sampling may not be represented as a hard memory limit")
        if policy["macos_residual_risk_acceptance"] != (
                "TRANSIENT_RSS_PEAK_MAY_BE_MISSED_OS_OOM_AND_APP_DISRUPTION_REMAIN"):
            raise ResourcePolicyError("Explicit macOS transient-peak residual-risk acceptance is required")
        if policy["macos_boot_volume_path"] != "/System/Volumes/Data":
            raise ResourcePolicyError("macOS policy must monitor the internal boot/data volume")
        if policy.get("require_ac_power") is not True or \
           policy.get("require_thermal_normal") is not True or \
           policy.get("require_sleep_assertion") is not True:
            raise ResourcePolicyError("AC, thermal, and sleep safeguards must be signed on")
        if policy["host_memory_free_percent_stop"] < 20:
            raise ResourcePolicyError("macOS host-pressure stop may not be weaker than 20% free")
        for name in ("boot_reserve_free_disk_bytes", "minimum_boot_free_disk_bytes",
                     "swap_growth_stop_bytes"):
            _positive_int(caps, name)
        if caps["minimum_boot_free_disk_bytes"] < MIN_MACOS_BOOT_FREE_BYTES:
            raise ResourcePolicyError("macOS boot-volume launch minimum must be at least 40 GiB")
        if caps["boot_reserve_free_disk_bytes"] < MIN_MACOS_BOOT_RESERVE_BYTES:
            raise ResourcePolicyError("macOS boot-volume free reserve must be at least 30 GiB")
        if caps["boot_reserve_free_disk_bytes"] >= caps["minimum_boot_free_disk_bytes"]:
            raise ResourcePolicyError("macOS boot reserve must be below its launch minimum")
        if purpose == POLICY_V2_MACOS:
            # V2 remains byte-for-byte conservative until superseded by a
            # separately approved amendment. Its old free-swap gates are not
            # silently removed by the V3 proposal.
            for name in ("swap_free_stop_bytes", "minimum_swap_free_bytes"):
                _positive_int(caps, name)
            if caps["minimum_swap_free_bytes"] < MIN_MACOS_SWAP_FREE_BYTES:
                raise ResourcePolicyError("macOS launch requires at least 2 GiB free swap headroom")
            if caps["swap_free_stop_bytes"] < MIN_MACOS_SWAP_FREE_STOP_BYTES:
                raise ResourcePolicyError("macOS must stop before free swap falls below 1 GiB")
            if caps["swap_free_stop_bytes"] >= caps["minimum_swap_free_bytes"]:
                raise ResourcePolicyError("macOS swap stop reserve must be below its launch minimum")
        else:
            if policy.get("macos_swap_volume_path") != "/System/Volumes/VM":
                raise ResourcePolicyError("V3 must monitor macOS's internal VM volume")
            if policy.get("macos_swap_telemetry_semantics") != MACOS_SWAP_TELEMETRY_SEMANTICS:
                raise ResourcePolicyError("V3 must not treat vm.swapusage.free as future capacity")
            _positive_int(caps, "swap_volume_reserve_free_disk_bytes")
            _positive_int(caps, "minimum_swap_volume_free_disk_bytes")
            if caps["swap_volume_reserve_free_disk_bytes"] < MIN_MACOS_SWAP_VOLUME_RESERVE_BYTES:
                raise ResourcePolicyError("V3 VM-volume free-space reserve must be at least 30 GiB")
            if caps["minimum_swap_volume_free_disk_bytes"] < MIN_MACOS_BOOT_FREE_BYTES:
                raise ResourcePolicyError("V3 VM-volume launch minimum must be at least 40 GiB")
            if (caps["swap_volume_reserve_free_disk_bytes"] >=
                    caps["minimum_swap_volume_free_disk_bytes"]):
                raise ResourcePolicyError("V3 VM-volume reserve must be below its launch minimum")
            if "minimum_swap_free_bytes" in caps or "swap_free_stop_bytes" in caps:
                raise ResourcePolicyError("V3 may not use current free-swap values as launch/stop gates")
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
        "memory_enforcement_backend": backend,
        "resource_policy_version": purpose,
        "memory_limit_semantics": policy.get("memory_limit_semantics",
                                               "CGROUP_V2_HARD_OS_ENFORCED"),
        "swap_telemetry_semantics": policy.get("macos_swap_telemetry_semantics"),
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
