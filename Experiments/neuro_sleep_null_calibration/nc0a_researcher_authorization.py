"""Schema checks for the prospective researcher-authorized NC-0a route.

This module deliberately does not provide cryptographic reviewer identity,
third-party approval, or immutable custody. Public GitHub comments provide
inspectable copies of commitments and audit tips; they are not independent
trust anchors.
"""

from __future__ import annotations

from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import uuid


PACKAGE_FORMAT = "NC0A_RESEARCHER_AUTHORIZED_EXECUTION_PACKAGE_V1"
COMMITMENT_FORMAT = "NC0A_RESEARCHER_AUTHORIZED_COMMITMENT_V1"
RESOURCE_POLICY_VERSION = "NC0A_MACOS_RESEARCHER_RESOURCE_POLICY_V1"
BACKEND = "MACOS_SAMPLED_PRESSURE"
RECOVERY_RULE = "TASK_LEVEL_FROM_ZERO_SAME_SEED_NO_OUTCOME_DEPENDENT_RETRY"
MEMORY_RISK = (
    "SAMPLED_RSS_AND_HOST_PRESSURE_ABORTS_ONLY_NOT_OS_HARD_LIMIT; "
    "TRANSIENT_RSS_PEAK_MAY_BE_MISSED_AND_OS_OOM_OR_OTHER_APP_DISRUPTION_REMAINS"
)

GIB = 1024 ** 3
MAX_WALL_SECONDS = 72 * 60 * 60
MAX_CPU_SECONDS = 288 * 60 * 60
MAX_RSS_BYTES = 4 * GIB
MAX_SWAP_GROWTH_BYTES = 2 * GIB
MIN_INTERNAL_FREE_BYTES = 40 * GIB
MIN_INTERNAL_RESERVE_BYTES = 30 * GIB
MAX_OUTPUT_BYTES = 4 * GIB
MIN_OUTPUT_RESERVE_BYTES = 30 * GIB

REQUIRED_RISK_ACKNOWLEDGEMENTS = (
    "macos_sampled_memory_is_not_a_hard_limit",
    "transient_memory_peaks_can_be_missed",
    "T_PS_A_remains_unresolved",
    "NC0a_budget_does_not_clear_G0_or_T1",
    "all_passes_retain_MIXING_UNRESOLVED",
    "prior_informal_result_exposure_is_disclosed",
    "no_outcome_dependent_seed_change_retry_or_threshold_change",
    "researcher_accepts_execution_risk_without_third_party_authorization",
    "AI_review_is_not_external_human_peer_review",
)


class ResearcherAuthorizationError(ValueError):
    """Invalid or incomplete researcher commitment; execution must stop."""


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def commitment_sha256(commitment: dict) -> str:
    return sha256(canonical_bytes(commitment)).hexdigest()


def package_sha256(package: dict) -> str:
    commitment = package.get("commitment")
    if not isinstance(commitment, dict):
        raise ResearcherAuthorizationError("Package is missing its commitment object")
    return commitment_sha256(commitment)


def validate_package(package: dict, *, context: dict, run_dir: str | Path) -> dict:
    """Validate one frozen precommit against the current repo/host and run path.

    ``context`` is collected by the execution engine from Git, the runtime lock,
    the host, and the internal Data/VM APFS volumes. This is schema and identity
    validation, not a proof that review identities are independent.
    """
    if not isinstance(package, dict) or package.get("format") != PACKAGE_FORMAT:
        raise ResearcherAuthorizationError("Wrong researcher-authorization package format")
    commitment = package.get("commitment")
    if not isinstance(commitment, dict) or commitment.get("format") != COMMITMENT_FORMAT:
        raise ResearcherAuthorizationError("Missing versioned researcher commitment")
    digest = commitment_sha256(commitment)
    if package.get("commitment_sha256") != digest:
        raise ResearcherAuthorizationError("Researcher commitment SHA-256 mismatch")
    precommit_url = package.get("precommit_comment_url")
    if not isinstance(precommit_url, str) or not precommit_url.strip():
        raise ResearcherAuthorizationError("Missing public pre-run GitHub commitment URL")

    try:
        if str(uuid.UUID(commitment["experiment_uuid"])) != commitment["experiment_uuid"]:
            raise ValueError
    except (KeyError, TypeError, ValueError, AttributeError) as exc:
        raise ResearcherAuthorizationError("experiment_uuid must be a canonical UUID") from exc

    researcher = commitment.get("researcher")
    if not isinstance(researcher, dict):
        raise ResearcherAuthorizationError("Missing researcher confirmation")
    for key in ("name", "github_login", "confirmed_at_utc"):
        if not isinstance(researcher.get(key), str) or not researcher[key].strip():
            raise ResearcherAuthorizationError(f"Missing researcher field: {key}")
    if researcher.get("decision") != "I_APPROVE_FORMAL_NC0A_AND_ACCEPT_THE_RECORDED_LIMITS_AND_RISKS":
        raise ResearcherAuthorizationError("Researcher has not explicitly accepted this execution plan")
    if researcher.get("confirmation_phrase") != (
            "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS"):
        raise ResearcherAuthorizationError("Researcher confirmation phrase is missing or incorrect")
    try:
        confirmed = datetime.fromisoformat(researcher["confirmed_at_utc"].replace("Z", "+00:00"))
        if confirmed.tzinfo is None:
            raise ValueError
    except (ValueError, TypeError) as exc:
        raise ResearcherAuthorizationError("Researcher confirmation time must include a UTC offset") from exc

    repository = commitment.get("repository")
    if not isinstance(repository, dict):
        raise ResearcherAuthorizationError("Missing frozen repository identity")
    if repository.get("head_sha") != context.get("head_sha"):
        raise ResearcherAuthorizationError("Commitment HEAD differs from the current HEAD")
    if context.get("clean_tree") is not True or repository.get("clean_tree") is not True:
        raise ResearcherAuthorizationError("Execution requires the exact clean committed tree")
    for field in ("preregistration_sha256", "resource_amendment_sha256",
                  "runtime_lock_sha256", "protocol_sha256",
                  "seed_manifest_sha256", "watchdog_contract_sha256",
                  "watchdog_source_sha256", "source_sha256"):
        if repository.get(field) != context.get(field):
            raise ResearcherAuthorizationError(f"Frozen repository identity mismatch: {field}")

    environment = commitment.get("environment")
    if not isinstance(environment, dict) or environment != context.get("environment"):
        raise ResearcherAuthorizationError("Frozen runtime/host environment differs from this host")

    resolved_run_dir = Path(run_dir).expanduser().resolve()
    output = commitment.get("resource_policy", {}).get("output_directory")
    if not isinstance(output, str) or Path(output).expanduser().resolve() != resolved_run_dir:
        raise ResearcherAuthorizationError("Run directory differs from the precommitted output path")
    if str(resolved_run_dir) != context.get("output_directory"):
        raise ResearcherAuthorizationError("Output directory is not the inspected internal-volume path")

    policy = commitment.get("resource_policy")
    if not isinstance(policy, dict) or policy.get("version") != RESOURCE_POLICY_VERSION:
        raise ResearcherAuthorizationError("Wrong prospective resource-policy version")
    if policy.get("memory_backend") != BACKEND:
        raise ResearcherAuthorizationError("Resource policy must explicitly use MACOS_SAMPLED_PRESSURE")
    if policy.get("macos_memory_semantics") != MEMORY_RISK:
        raise ResearcherAuthorizationError("Sampled macOS memory risk may not be weakened or relabeled")
    caps = policy.get("limits")
    if not isinstance(caps, dict):
        raise ResearcherAuthorizationError("Missing absolute resource limits")
    for name in ("wall_seconds", "cpu_seconds", "per_case_seconds", "oracle_seconds",
                 "sampled_rss_bytes", "host_free_percent_stop", "swap_growth_bytes",
                 "data_min_free_bytes", "data_reserve_bytes", "vm_min_free_bytes",
                 "vm_reserve_bytes", "run_output_cap_bytes", "run_output_reserve_bytes",
                 "max_workers", "max_attempts_per_case"):
        if type(caps.get(name)) is not int or caps[name] <= 0:
            raise ResearcherAuthorizationError(f"Missing positive integer resource limit: {name}")
    if caps["wall_seconds"] > MAX_WALL_SECONDS:
        raise ResearcherAuthorizationError("Wall budget exceeds the reviewed 72-hour candidate ceiling")
    if caps["cpu_seconds"] > MAX_CPU_SECONDS:
        raise ResearcherAuthorizationError("CPU budget exceeds the reviewed 288 CPU-hour candidate ceiling")
    if caps["max_workers"] != 4:
        raise ResearcherAuthorizationError("Researcher-authorized macOS policy is fixed at four workers")
    if caps["sampled_rss_bytes"] > MAX_RSS_BYTES:
        raise ResearcherAuthorizationError("Sampled RSS stop ceiling exceeds the 4 GiB candidate")
    if caps["host_free_percent_stop"] < 20 or caps["host_free_percent_stop"] > 100:
        raise ResearcherAuthorizationError("Host memory-pressure stop must be at least 20% free")
    if caps["swap_growth_bytes"] > MAX_SWAP_GROWTH_BYTES:
        raise ResearcherAuthorizationError("Sampled swap-growth stop exceeds the 2 GiB candidate")
    if caps["data_min_free_bytes"] < MIN_INTERNAL_FREE_BYTES or \
       caps["vm_min_free_bytes"] < MIN_INTERNAL_FREE_BYTES:
        raise ResearcherAuthorizationError("Internal Data and VM launch floors cannot be lowered below 40 GiB")
    if caps["data_reserve_bytes"] < MIN_INTERNAL_RESERVE_BYTES or \
       caps["vm_reserve_bytes"] < MIN_INTERNAL_RESERVE_BYTES:
        raise ResearcherAuthorizationError("Internal Data and VM reserves cannot be lowered below 30 GiB")
    if caps["run_output_cap_bytes"] > MAX_OUTPUT_BYTES:
        raise ResearcherAuthorizationError("Run-output cap exceeds the reviewed 4 GiB candidate")
    if caps["run_output_reserve_bytes"] < MIN_OUTPUT_RESERVE_BYTES:
        raise ResearcherAuthorizationError("Output-volume reserve cannot be lowered below 30 GiB")
    if caps["per_case_seconds"] > 12 * 60 * 60 or caps["oracle_seconds"] > 30 * 60:
        raise ResearcherAuthorizationError("Per-case/oracle deadline exceeds the recorded candidate")
    if caps["max_attempts_per_case"] != 2:
        raise ResearcherAuthorizationError("Only the fixed one-retry operational recovery allowance is supported")
    if policy.get("recovery_rule") != RECOVERY_RULE:
        raise ResearcherAuthorizationError("Seed-preserving task-level recovery rule changed")
    if policy.get("require_ac_power") is not True or \
       policy.get("require_normal_thermal_state") is not True or \
       policy.get("require_sleep_assertion") is not True:
        raise ResearcherAuthorizationError("AC, thermal and sleep safeguards are mandatory")
    if policy.get("output_volume") != context.get("output_volume"):
        raise ResearcherAuthorizationError("Output-volume identity differs from inspected internal APFS volume")
    expected_internal_volumes = {
        "data": context.get("data_volume"),
        "vm": context.get("vm_volume"),
    }
    if policy.get("internal_volumes") != expected_internal_volumes:
        raise ResearcherAuthorizationError("Internal Data/VM volume UUIDs differ from the commitment")
    if (not isinstance(context.get("data_volume"), dict) or
            not isinstance(context.get("vm_volume"), dict) or
            context["data_volume"].get("filesystem") != "APFS" or
            context["vm_volume"].get("filesystem") != "APFS" or
            context["data_volume"].get("internal") is not True or
            context["vm_volume"].get("internal") is not True or
            context.get("output_volume") != context.get("data_volume")):
        raise ResearcherAuthorizationError("Results must be on the reviewed internal Data APFS volume")
    if (context.get("current_data_free_bytes", 0) < caps["data_min_free_bytes"] or
            context.get("current_vm_free_bytes", 0) < caps["vm_min_free_bytes"]):
        raise ResearcherAuthorizationError("Current internal free space is below the signed launch floors")
    baseline = policy.get("baseline_measurement")
    if not isinstance(baseline, dict):
        raise ResearcherAuthorizationError("Missing explicit host/resource baseline measurement")
    for field in ("data_free_bytes", "vm_free_bytes", "host_memory_free_percent",
                  "swap_total_bytes", "swap_used_bytes", "swap_free_bytes"):
        if type(baseline.get(field)) is not int or baseline[field] < 0:
            raise ResearcherAuthorizationError(f"Invalid baseline measurement: {field}")
    if (baseline["data_free_bytes"] < caps["data_min_free_bytes"] or
            baseline["vm_free_bytes"] < caps["vm_min_free_bytes"]):
        raise ResearcherAuthorizationError("Recorded baseline does not satisfy internal storage floors")
    if baseline["host_memory_free_percent"] < caps["host_free_percent_stop"]:
        raise ResearcherAuthorizationError("Recorded baseline violates the system-wide pressure stop")
    try:
        measured_at = datetime.fromisoformat(
            str(baseline["measured_at_utc"]).replace("Z", "+00:00"))
        if measured_at.tzinfo is None:
            raise ValueError
    except (KeyError, TypeError, ValueError) as exc:
        raise ResearcherAuthorizationError("Baseline timestamp must include a UTC offset") from exc
    if (datetime.now(timezone.utc) - measured_at.astimezone(timezone.utc)).total_seconds() > 24 * 3600:
        raise ResearcherAuthorizationError("Host/resource baseline is more than 24 hours old")

    acknowledgements = commitment.get("risk_acknowledgements")
    if not isinstance(acknowledgements, dict) or any(
            acknowledgements.get(name) is not True for name in REQUIRED_RISK_ACKNOWLEDGEMENTS):
        raise ResearcherAuthorizationError("All listed scientific and execution risks must be explicitly acknowledged")

    reviews = commitment.get("independent_science_reviews")
    if not isinstance(reviews, list) or len(reviews) < 2:
        raise ResearcherAuthorizationError("At least two separately identified review records are required")
    reviewer_ids = set()
    covered = set()
    for review in reviews:
        if not isinstance(review, dict):
            raise ResearcherAuthorizationError("Malformed independent review record")
        for key in ("reviewer_id", "reviewer_type", "github_comment_url", "reviewed_head_sha",
                    "decision", "scope", "blocking_findings", "human_peer_review"):
            if key not in review:
                raise ResearcherAuthorizationError(f"Review record missing {key}")
        rid = review["reviewer_id"]
        if not isinstance(rid, str) or not rid.strip() or rid in reviewer_ids:
            raise ResearcherAuthorizationError("Reviewers must have distinct nonempty identities")
        reviewer_ids.add(rid)
        if review["reviewer_type"] not in ("AI_MODEL", "HUMAN_REVIEWER"):
            raise ResearcherAuthorizationError("Review type must distinguish AI and human reviewers")
        if review["reviewed_head_sha"] != context.get("head_sha"):
            raise ResearcherAuthorizationError("Independent review does not cover the exact frozen HEAD")
        if review["decision"] != "NO_BLOCKING_FINDINGS_FOR_NC0A_EXECUTION":
            raise ResearcherAuthorizationError("Independent review has not cleared execution blockers")
        if not isinstance(review["blocking_findings"], list) or review["blocking_findings"]:
            raise ResearcherAuthorizationError("Review contains open blocking findings")
        if not isinstance(review["scope"], list) or any(
                s not in ("methods", "statistics", "implementation") for s in review["scope"]):
            raise ResearcherAuthorizationError("Review scope must use methods/statistics/implementation")
        covered.update(review["scope"])
        if review["reviewer_type"] == "AI_MODEL" and review["human_peer_review"] is not False:
            raise ResearcherAuthorizationError("AI-assisted review cannot be labeled human peer review")
        if review["reviewer_type"] == "HUMAN_REVIEWER" and type(review["human_peer_review"]) is not bool:
            raise ResearcherAuthorizationError("Human review record must state whether it is peer review")
    if not {"methods", "statistics", "implementation"}.issubset(covered):
        raise ResearcherAuthorizationError("Reviews do not jointly cover methods, statistics and implementation")

    scientific_protocol = commitment.get("scientific_protocol")
    expected_protocol = context.get("scientific_protocol")
    if scientific_protocol != expected_protocol:
        raise ResearcherAuthorizationError("Scientific scale, fixed seeds, thresholds or protocol changed")
    if scientific_protocol.get("mixing_interpretation") != "MIXING-UNRESOLVED":
        raise ResearcherAuthorizationError("NC-0a must retain MIXING-UNRESOLVED")

    return {
        "status": "SCHEMA_AND_IDENTITY_VALID_NOT_EXECUTION_AUTHORIZATION",
        "commitment_sha256": digest,
        "experiment_uuid": commitment["experiment_uuid"],
        "review_count": len(reviews),
        "reviewer_types": sorted({r["reviewer_type"] for r in reviews}),
        "resource_limits": caps,
        "memory_enforcement": MEMORY_RISK,
        "third_party_authorization": False,
        "external_human_peer_review": any(
            r["reviewer_type"] == "HUMAN_REVIEWER" and r["human_peer_review"] is True
            for r in reviews),
    }


def parse_github_comment_url(url: str) -> int:
    match = re.fullmatch(
        r"https://github\.com/zyx1st-png/SRT-Pub/pull/1114#issuecomment-(\d+)",
        url or "")
    if not match:
        raise ResearcherAuthorizationError("Review/precommit must link to a PR #1114 top-level comment")
    return int(match.group(1))


def marker_payload(body: str, marker: str) -> dict:
    prefix = marker + "="
    matches = [line[len(prefix):].strip() for line in body.splitlines()
               if line.startswith(prefix)]
    if len(matches) != 1:
        raise ResearcherAuthorizationError(f"GitHub comment must contain exactly one {marker} marker")
    import base64
    try:
        value = json.loads(base64.b64decode(matches[0], validate=True))
    except (ValueError, json.JSONDecodeError) as exc:
        raise ResearcherAuthorizationError(f"Malformed {marker} payload") from exc
    if not isinstance(value, dict):
        raise ResearcherAuthorizationError(f"{marker} payload must decode to a JSON object")
    return value


def validate_remote_precommit(package: dict, comment: dict) -> None:
    """Require the actual public PR comment to contain this exact commitment."""
    commitment = package["commitment"]
    expected = commitment_sha256(commitment)
    if comment.get("user", {}).get("login") != commitment["researcher"]["github_login"]:
        raise ResearcherAuthorizationError("Precommit GitHub comment is not from the named researcher account")
    remote = marker_payload(comment.get("body", ""), "NC0A_RESEARCHER_PRECOMMIT_JSON_BASE64")
    if remote != commitment or commitment_sha256(remote) != expected:
        raise ResearcherAuthorizationError("Offsite precommit does not reproduce the exact local commitment")
    created = comment.get("created_at")
    try:
        comment_time = datetime.fromisoformat(created.replace("Z", "+00:00"))
        confirm_time = datetime.fromisoformat(
            commitment["researcher"]["confirmed_at_utc"].replace("Z", "+00:00"))
    except (AttributeError, TypeError, ValueError) as exc:
        raise ResearcherAuthorizationError("GitHub precommit/researcher timestamps are invalid") from exc
    if comment_time < confirm_time or comment_time.tzinfo is None:
        raise ResearcherAuthorizationError("GitHub precommit was not posted after researcher confirmation")


def validate_remote_review(review: dict, comment: dict) -> None:
    if review.get("github_comment_url") is None:
        raise ResearcherAuthorizationError("Review record has no public GitHub URL")
    remote = marker_payload(comment.get("body", ""), "NC0A_INDEPENDENT_REVIEW_JSON_BASE64")
    expected = {k: v for k, v in review.items() if k != "github_comment_url"}
    if remote != expected:
        raise ResearcherAuthorizationError("Public review comment differs from the commitment review record")
    if not comment.get("created_at"):
        raise ResearcherAuthorizationError("Public review comment has no timestamp")


def validate_remote_audit_anchor(summary: dict, comment: dict) -> None:
    remote = marker_payload(comment.get("body", ""), "NC0A_AUDIT_SUMMARY_JSON_BASE64")
    if remote != summary:
        raise ResearcherAuthorizationError("Resume audit anchor differs from the verified local run history")
