"""One consumed-attempt exception for the frozen 41-row observed suffix.

No implicit resume, new-UUID reset, reserve selection or normal-run bypass.
The default CLI can only inspect identity or print a pending draft. Real work
requires a separate exact-HEAD/UUID authorization and a durable one-time claim.
"""
from __future__ import annotations

import argparse
import fcntl
import json
import os
import shutil
import stat
import subprocess
import sys
from contextlib import contextmanager
from dataclasses import replace
from datetime import UTC, datetime
from pathlib import Path

import h3_supervised_pilot as pilot
import nc0a_watchdog as watchdog
import observed_calibration_runner as runner
import observed_remediation_identity as provenance
import riken_source_identity as identity
from nc0a_watchdog import (
    HashChainLog,
    WatchdogError,
    _directory_bytes,
    guard_watchdog_parent,
)
from observed_calibration_measurement import Phase, RawWindowCache, process_counters
from observed_calibration_sample import (
    HERE,
    RESOURCE_CANDIDATE,
    validate_sample,
)
from observed_remediation_budget import (
    ControllerMeter,
    RemediationBudgetError,
    budget_allocation,
    close_charge,
)

POLICY_RECORD = "https://github.com/zyx1st-png/SRT-Pub/pull/1133#issuecomment-6412266654"
AUTH_SCHEMA = "SRT_OBSERVED_ONCE_REMEDIATION_AUTHORIZATION_V1"
ACCOUNT_FILE = "remediation-account.json"
CLOSED_FILE = "remediation-closed.json"


class RemediationError(ValueError):
    """Missing exception identity, accounting or authorization: fail closed."""


def _receipt_path(binding: dict) -> Path:
    return (Path(binding["host_state_directory"]) /
            f"observed-remediation-{binding['prior_run']['uuid']}.claim.json")


def _read_receipt(binding: dict) -> dict:
    path = _receipt_path(binding)
    document = pilot._read_json(path)
    if (path.stat().st_nlink != 1 or
            document.get("schema") != "SRT_OBSERVED_REMEDIATION_CLAIM_RECEIPT_V1" or
            not isinstance(document.get("event"), dict) or
            type(document.get("sequence")) is not int or document["sequence"] < 0 or
            not isinstance(document.get("previous_sha256"), str)):
        raise RemediationError("Exception receipt is aliased or malformed")
    if document.get("event", {}).get("binding") != binding:
        raise RemediationError("Exception receipt belongs to a different identity")
    record = {key: document[key] for key in ("sequence", "previous_sha256", "event")}
    if identity.sha256_bytes(identity.canonical_json(record)) != document.get("record_sha256"):
        raise RemediationError("Exception receipt hash is inconsistent")
    return document


def _write_exclusive_receipt(path: Path, document: dict) -> None:
    # An interrupted partial receipt intentionally remains a consumed/uncertain
    # marker. Never replace it with a clean document on the next invocation.
    payload = identity.canonical_json(document) + b"\n"
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0), 0o600)
    try:
        directory_fd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
        view = memoryview(payload)
        while view:
            written = os.write(fd, view)
            if written <= 0:
                raise OSError("Short exception-receipt write")
            view = view[written:]
        os.fsync(fd)
    finally:
        os.close(fd)


def implementation_identity() -> dict:
    return {**runner.implementation_identity(), **{
        name: identity.sha256_file(HERE / name) for name in (
            "h3_supervised_pilot.py", "observed_calibration_remediation.py",
            "observed_remediation_identity.py", "observed_remediation_budget.py")}}


def bindings(head: str, run_id: str, run_dir: Path, old_run_dir: Path) -> dict:
    packet = provenance.load_packet()
    prior = packet["prior_run"]
    if (run_id == prior["uuid"] or old_run_dir.name != prior["uuid"] or
            old_run_dir.parent != run_dir.parent or not old_run_dir.is_absolute() or
            not run_dir.is_absolute() or ".." in run_dir.parts or ".." in old_run_dir.parts):
        raise RemediationError("Distinct UUIDs under the same fixed private parent are required")
    return {**runner.bindings(head, run_id, run_dir),
            "scope": "ONE_EXCEPTION_41_SUFFIX_8200_Q_NO_PREFIX_NO_RESERVE_NO_RETRY",
            "prior_run_directory": str(old_run_dir), "prior_run": prior,
            "remediation_packet_sha256": provenance.PACKET_SHA256,
            "suffix_sha256": provenance.SUFFIX_SHA256,
            "host_state_directory": str(pilot.default_host_state_dir()),
            "host_logical_cpu_count": os.cpu_count(),
            "max_exception_claims": 1, "policy_record": POLICY_RECORD,
            "implementation_sha256": implementation_identity(),
            "accounting_policy": "CUMULATIVE_OLD_UPPER_CHARGE_NEW_LIFETIME_PLUS_CLOSING_V1"}


def confirmation_text(head: str, run_id: str) -> str:
    return (f"I AUTHORIZE ONE OBSERVED REMEDIATION {run_id} "
            f"{provenance.load_packet()['prior_run']['uuid']} {provenance.SUFFIX_SHA256} {head}")


def authorization_draft(head: str, run_id: str, run_dir: Path, old_run_dir: Path) -> dict:
    return {"schema": AUTH_SCHEMA, "status": "PENDING_RESEARCHER_APPROVAL",
            "binding": bindings(head, run_id, run_dir, old_run_dir),
            "researcher_confirmation": "", "researcher_identity": "", "confirmed_at_utc": "",
            "researcher_confirmed_risks": False, "no_automatic_retry": True,
            "required_confirmation_not_yet_given": confirmation_text(head, run_id)}


def validate_authorization(path: Path, *, head: str, run_id: str, run_dir: Path,
                           old_run_dir: Path, confirmation: str) -> dict:
    auth = pilot._read_json(path)
    expected = bindings(head, run_id, run_dir, old_run_dir)
    effective, method_sha = runner.h3._method_is_effective(HERE / runner.METHOD_FILENAME)
    if (not effective or method_sha != runner.METHOD_SHA256 or
            auth.get("schema") != AUTH_SCHEMA or
            auth.get("status") != "APPROVED_FOR_SINGLE_REMEDIATION" or
            confirmation != confirmation_text(head, run_id) or
            auth.get("researcher_confirmation") != confirmation or auth.get("binding") != expected or
            auth.get("researcher_confirmed_risks") is not True or
            auth.get("no_automatic_retry") is not True or
            any(not isinstance(auth.get(key), str) or not auth[key].strip()
                for key in ("researcher_identity", "confirmed_at_utc"))):
        raise RemediationError("Separate researcher remediation approval or exact binding is missing")
    return {"authorization_sha256": identity.sha256_file(path), "binding": expected,
            "authorization_bytes": path.stat().st_size,
            "authorization_path": str(path.resolve(strict=True))}


def assert_claim_state(events: list[dict], binding: dict, auth_sha: str, *, phase: str) -> None:
    """Only a closed known old attempt plus one exact claim can enter the suffix."""
    if phase not in {"unclaimed", "claimed", "running"}:
        raise RemediationError("Unknown exception-admission phase")
    prior = binding["prior_run"]
    old_starts = [e for e in events if e.get("kind") == "activity_started" and
                  e.get("run_id") == prior["uuid"]]
    old_ends = [e for e in events if e.get("kind") == "activity_finished" and
                e.get("run_id") == prior["uuid"]]
    if (len(old_starts) != 1 or len(old_ends) != 1 or
            old_starts[0].get("head_sha") != prior["head_sha"] or
            old_starts[0].get("pilot_sha256") != runner.EXPECTED_SAMPLE_SHA256 or
            old_starts[0].get("run_directory") != binding["prior_run_directory"] or
            old_ends[0].get("status") != prior["terminal_status"] or
            old_ends[0].get("failure_category") != prior["failure_category"] or
            old_ends[0].get("summary_sha256") != prior["file_sha256"]["h3-summary.json"] or
            old_ends[0].get("run_manifest_sha256") != prior["file_sha256"]["run-manifest.json"]):
        raise RemediationError("Original consumed attempt is not uniquely closed and hash-bound")
    claims = [e for e in events if e.get("kind") == "observed_remediation_claimed" and
              (e.get("prior_run_id") == prior["uuid"] or
               e.get("full_sample_sha256") == runner.EXPECTED_SAMPLE_SHA256)]
    new_events = [e for e in events if e.get("run_id") == binding["run_uuid"]]
    if phase == "unclaimed":
        if claims or new_events or _receipt_path(binding).exists() or _receipt_path(binding).is_symlink():
            raise RemediationError("The sole exception or this UUID has already been consumed")
        return
    if (len(claims) != 1 or claims[0].get("binding") != binding or
            claims[0].get("authorization_sha256") != auth_sha or
            claims[0].get("run_id") != binding["run_uuid"]):
        raise RemediationError("No unique exact exception claim")
    receipt = _read_receipt(binding)
    if receipt["event"] != claims[0] or receipt["event"]["authorization_sha256"] != auth_sha:
        raise RemediationError("Exception ledger/receipt mismatch")
    if any(e.get("kind") in {"observed_remediation_admission_failed",
                             "observed_remediation_accounted", "observed_remediation_violation"}
           for e in new_events):
        raise RemediationError("Exception is terminal/uncertain and cannot be retried")
    starts = [e for e in new_events if e.get("kind") == "activity_started"]
    ends = [e for e in new_events if e.get("kind") == "activity_finished"]
    if ends or len(starts) != (1 if phase == "running" else 0):
        raise RemediationError("Exception invocation state is inconsistent")


def claim_locked(log: HashChainLog, events: list[dict], approved: dict) -> str:
    """Caller holds both existing host locks; claim is fsynced before the repeated post-claim preflight."""
    binding, digest = approved["binding"], approved["authorization_sha256"]
    pilot._assert_host_ledger_allows(events, provenance.PACKET_SHA256)
    assert_claim_state(events, binding, digest, phase="unclaimed")
    event = {"kind": "observed_remediation_claimed", "run_id": binding["run_uuid"],
                       "prior_run_id": binding["prior_run"]["uuid"],
                       "full_sample_sha256": runner.EXPECTED_SAMPLE_SHA256,
                       "binding": binding, "authorization_sha256": digest,
                       "authorization_bytes": approved["authorization_bytes"],
                       "status": "CONSUMED_BEFORE_PREFLIGHT_NO_AUTORETRY",
                       "claimed_utc": datetime.now(UTC).isoformat()}
    record = {"sequence": log.sequence, "previous_sha256": log.previous, "event": event}
    expected_tip = identity.sha256_bytes(identity.canonical_json(record))
    _write_exclusive_receipt(_receipt_path(binding), {
        "schema": "SRT_OBSERVED_REMEDIATION_CLAIM_RECEIPT_V1", **record,
        "record_sha256": expected_tip})
    actual_tip = log.append(event)
    if actual_tip != expected_tip:
        raise RemediationError("Persisted claim differs from exclusive receipt")
    return actual_tip


def _extra_bytes(run_dir: Path, ledger: Path, ledger_start_bytes: int, auth: Path) -> int:
    growth = ledger.stat().st_size - ledger_start_bytes
    if growth < 0:
        raise RemediationError("Host ledger shrank during the exception")
    if run_dir.is_symlink() or auth.is_symlink() or ledger.is_symlink():
        raise RemediationError("Attributed output/authentication path was redirected")
    receipt = _receipt_path(pilot._read_json(auth)["binding"])
    if receipt.is_symlink():
        raise RemediationError("Exception receipt redirected")
    receipt_bytes = receipt.stat().st_size if receipt.exists() else 0
    return (_directory_bytes(run_dir) if run_dir.exists() else 0) + growth + auth.stat().st_size + receipt_bytes


def _original_budget(old_run_dir: Path, state: Path, audit_guard=None) -> dict:
    info = (provenance.verify_original(old_run_dir, state) if audit_guard is None else
            provenance.verify_original(old_run_dir, state, audit_guard=audit_guard))
    # Current full-ledger hashes change on legitimate append; the old prefix
    # is independently pinned. Do not make live-ledger snapshots a budget ID.
    return {key: value for key, value in info.items()
            if key != "host_ledger_sha256_at_verification"}


def _tail_exceeds_charge(prior: dict, tail: dict, charged: dict,
                         extra_bytes: int, prospective_closure_bytes: int) -> bool:
    return (tail["wall_seconds"] > charged["charged_new_wall_seconds"] or
            tail["cpu_seconds"] > charged["charged_new_cpu_seconds"] or
            prior["old_output_bytes"] + prior.get("old_auxiliary_output_bytes", 0) +
            extra_bytes + prospective_closure_bytes > charged["charged_total_output_bytes"])


def _identity_preflight(binding: dict, phase2: Path, psa: Path) -> dict:
    """Reuse all admission checks except the intentionally consumed normal gate."""
    packet = provenance.load_packet()
    sample, manifest = validate_sample()
    if binding["runtime_lock_sha256"] != packet["runtime_lock_sha256"]:
        raise RemediationError("Frozen runtime lock hash mismatch")
    git = pilot._git_identity(binding["head_sha"])
    effective, method_sha = runner.h3._method_is_effective(HERE / runner.METHOD_FILENAME)
    if not effective or method_sha != packet["method_sha256"]:
        raise RemediationError("Effective method hash/state mismatch")
    if bindings(binding["head_sha"], binding["run_uuid"], Path(binding["output_directory"]),
                Path(binding["prior_run_directory"])) != binding:
        raise RemediationError("Bindings changed during admission")
    runtime = identity.h3_runtime_manifest()
    if not runtime["replay_environment_matches_recorded_versions_and_candidate_lock"]:
        raise RemediationError("Locked runtime mismatch")
    if (os.cpu_count() != packet["prior_run"]["accounting_cpu_count_upper_bound"] or
            os.cpu_count() != binding["host_logical_cpu_count"]):
        raise RemediationError("Host CPU count differs from the eight-core accounting/stop margin")
    process_counters()
    phase2, psa, signatures = runner.validate_private_identities(sample, manifest, phase2, psa)
    target, parent = runner.checked_output(Path(binding["output_directory"]), psa, binding["run_uuid"])
    expected_old = psa / runner.OUTPUT_PARENT / packet["prior_run"]["uuid"]
    if Path(binding["prior_run_directory"]) != expected_old:
        raise RemediationError("Original run is outside the fixed private root")
    volume = runner.validate_internal_apfs(psa)
    resources = pilot._preflight_macos_resources(pilot._build_watchdog_limits(RESOURCE_CANDIDATE), psa)
    if not parent.is_dir() or parent.is_symlink() or parent.resolve(strict=True) != parent:
        raise RemediationError("Existing original output parent is missing or redirected")
    if not os.access(parent, os.W_OK | os.X_OK):
        raise RemediationError("Output parent is not writable/searchable")
    return {"head": git, "runtime": runtime, "source_signatures": signatures,
            "phase2": str(phase2), "psa": str(psa), "run_parent": str(parent),
            "run_directory": str(target), "output_volume": volume, "resources": resources,
            "implementation": runner.implementation_identity()}


@contextmanager
def _read_only_host_locks(state: Path):
    """Inspect and lock existing admission files without creating/chmodding them."""
    if state.resolve(strict=True) != Path(os.path.abspath(state)) or not state.is_dir():
        raise RemediationError("Existing host-state directory is missing or redirected")
    descriptors = []
    try:
        for path in (watchdog._default_activity_lock_path(), state / pilot._HOST_LOCK):
            if path.resolve(strict=True) != Path(os.path.abspath(path)):
                raise RemediationError("Host activity lock is redirected")
            fd = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
            descriptors.append(fd)
            info = os.fstat(fd)
            if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
                raise RemediationError("Host activity lock must be a single regular file")
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        yield
    finally:
        for fd in reversed(descriptors):
            fcntl.flock(fd, fcntl.LOCK_UN)
            os.close(fd)


def _sleep_assertion_probe() -> dict:
    helper = watchdog._start_sleep_assertion(os.getpid(), True)
    try:
        if helper is None or helper.poll() is not None:
            raise RemediationError("Required sleep assertion capability unavailable")
        return {"status": "STARTED_AND_STOPPED", "continuous_assertion_reserved": False}
    finally:
        watchdog._stop_sleep_assertion(helper)


def host_observation(psa: Path) -> dict:
    """Diagnostic snapshot only; thresholds are still validated by the Watchdog."""
    try:
        return {"status": "OBSERVED_NOT_RESERVED",
                "macos": watchdog.sample_macos_native_state(),
                "memory": watchdog.sample_host_memory_pressure(),
                "Data_free_bytes": shutil.disk_usage(runner.MACOS_POLICY["internal_data_volume_path"]).free,
                "VM_free_bytes": shutil.disk_usage(runner.MACOS_POLICY["internal_vm_volume_path"]).free,
                "output_free_bytes": shutil.disk_usage(psa).free}
    except (OSError, ValueError, subprocess.SubprocessError, WatchdogError) as exc:
        return {"status": "UNAVAILABLE", "reason": str(exc)[:300]}


def _preflight_locked(binding: dict, phase2: Path, psa: Path, state: Path,
                       meter: ControllerMeter, authorization: Path | None = None) -> dict:
    """Caller holds the host locks; every operation before claim is read-only."""
    names = ("unused_exception", "original_six_and_audits", "identity_sources_and_resources",
             "sleep_assertion_capability", "remaining_cumulative_budget")
    report = {"schema": "SRT_OBSERVED_REMEDIATION_PREFLIGHT_V1", "status": "PREFLIGHT NO-GO",
              "checked_at_utc": datetime.now(UTC).isoformat(), "binding": binding,
              "claim_consumed_by_preflight": False, "created_by_preflight": [],
              "execution_authorized": False, "checks": [], "verified": {},
              "dynamic_state": "Snapshot only; no resource reservation or future guarantee. "
                               "Formal launch repeats checks under locks, then rechecks after claim."}
    current = names[0]
    try:
        if str(state) != binding["host_state_directory"]:
            raise RemediationError("Preflight ledger is not the bound host-state directory")
        events = pilot._verified_host_events(state / pilot._HOST_LEDGER)
        pilot._assert_host_ledger_allows(events, provenance.PACKET_SHA256)
        assert_claim_state(events, binding, "", phase="unclaimed")
        report["checks"].append({"name": current, "status": "PASS"})
        current = names[1]
        prior = _original_budget(Path(binding["prior_run_directory"]), state)
        report["verified"]["original"] = prior
        report["checks"].append({"name": current, "status": "PASS"})
        current = names[2]
        report["verified"]["environment"] = _identity_preflight(binding, phase2, psa)
        report["checks"].append({"name": current, "status": "PASS"})
        current = names[3]
        report["verified"]["sleep_probe"] = _sleep_assertion_probe()
        report["checks"].append({"name": current, "status": "PASS"})
        current = names[4]
        snapshot = meter.snapshot()
        report["verified"]["controller_observation"] = snapshot
        extra = authorization.stat().st_size if authorization is not None else 0
        report["verified"]["allocation_if_admitted_now"] = budget_allocation(prior, snapshot, extra)
        report["checks"].append({"name": current, "status": "PASS"})
        report["status"] = "PREFLIGHT PASS"
    except (OSError, ValueError, subprocess.SubprocessError, WatchdogError, RemediationBudgetError, pilot.H3PilotError) as exc:
        report["checks"].append({"name": current, "status": "FAIL",
                                 "failure_type": type(exc).__name__, "reason": str(exc)[:500]})
        report["observed_host_state"] = host_observation(psa)
    checked = {check["name"] for check in report["checks"]}
    report["checks"].extend({"name": name, "status": "NOT_CHECKED"} for name in names if name not in checked)
    return report


def preflight(*, head: str, run_id: str, run_dir: Path, old_run_dir: Path,
              phase2: Path, psa: Path, state_dir: Path | None = None) -> dict:
    """Non-consuming read-only preflight: no authorization, ledger or result writes."""
    try:
        meter = ControllerMeter()
        binding = bindings(head, run_id, run_dir, old_run_dir)
        state = state_dir or pilot.default_host_state_dir()
        with _read_only_host_locks(state):
            return _preflight_locked(binding, phase2, psa, state, meter)
    except (OSError, ValueError, subprocess.SubprocessError, WatchdogError, RemediationBudgetError, pilot.H3PilotError) as exc:
        return {"schema": "SRT_OBSERVED_REMEDIATION_PREFLIGHT_V1", "status": "PREFLIGHT NO-GO",
                "claim_consumed_by_preflight": False, "execution_authorized": False, "created_by_preflight": [],
                "checks": [{"name": "binding_and_existing_host_locks", "status": "FAIL",
                            "failure_type": type(exc).__name__, "reason": str(exc)[:500]}],
                "observed_host_state": host_observation(psa)}


def launch(*, head: str, run_id: str, run_dir: Path, old_run_dir: Path, authorization: Path,
           confirmation: str, phase2: Path, psa: Path, state_dir: Path | None = None) -> dict:
    meter = ControllerMeter()  # process lifetime, including imports and approval validation
    approved = validate_authorization(authorization, head=head, run_id=run_id,
                                      run_dir=run_dir, old_run_dir=old_run_dir, confirmation=confirmation)
    pilot._git_identity(head)
    runner.checked_output(run_dir, psa, run_id)
    if old_run_dir != psa / runner.OUTPUT_PARENT / provenance.load_packet()["prior_run"]["uuid"]:
        raise RemediationError("Original private output root mismatch")
    state = state_dir or pilot.default_host_state_dir()
    if str(state) != approved["binding"]["host_state_directory"]:
        raise RemediationError("Execution ledger is not the authorized host-state directory")
    ledger = state / pilot._HOST_LEDGER
    binding = approved["binding"]
    packet = provenance.load_packet()
    # The ordinary entry still refuses the old full sample. Only this distinct
    # frozen packet and the explicit claim can reach the already-reviewed kernel.
    with pilot._host_lock(state):
        # B1: environment/identity refusal must precede the irreversible claim.
        # These checks hold the same locks as the immediately following claim.
        before_claim = _preflight_locked(binding, phase2, psa, state, meter, authorization)
        if before_claim["status"] != "PREFLIGHT PASS":
            return before_claim
        events = pilot._verified_host_events(ledger)
        ledger_start_bytes = ledger.stat().st_size
        with HashChainLog(ledger) as log:
            claim_tip = claim_locked(log, events, approved)
            try:
                prior = _original_budget(old_run_dir, state)
                check = _identity_preflight(binding, phase2, psa)
                budget_allocation(prior, meter.snapshot(), _extra_bytes(
                    run_dir, ledger, ledger_start_bytes, authorization))
                log.append({"kind": "observed_remediation_preflight", "run_id": run_id,
                            "claim_tip": claim_tip, "meter": meter.snapshot(),
                            "prior_budget": prior, "status": "PASSED_NOT_STARTED"})
            except BaseException as exc:
                try:
                    failure_meter = meter.snapshot()
                except BaseException as meter_exc:  # noqa: BLE001 -- never record unknown consumption as zero
                    failure_meter = {"accounting_status": "UNKNOWN_FAIL_CLOSED",
                                     "failure_reason": str(meter_exc)[:200]}
                log.append({"kind": "observed_remediation_admission_failed", "run_id": run_id,
                            "claim_tip": claim_tip, "failure_type": type(exc).__name__,
                            "failure_reason": str(exc)[:500], "resume_allowed": False,
                            "meter": failure_meter})
                raise

    def admission(events):
        assert_claim_state(events, binding, approved["authorization_sha256"], phase="claimed")
        if _original_budget(old_run_dir, state) != prior:
            raise RemediationError("Original accounting changed before dispatch")
        validate_authorization(authorization, head=head, run_id=run_id, run_dir=run_dir,
                               old_run_dir=old_run_dir, confirmation=confirmation)
        budget_allocation(prior, meter.snapshot(), _extra_bytes(
            run_dir, ledger, ledger_start_bytes, authorization))

    allocation = budget_allocation(prior, meter.snapshot(), _extra_bytes(
        run_dir, ledger, ledger_start_bytes, authorization))
    limits = replace(pilot._build_watchdog_limits(RESOURCE_CANDIDATE),
                     wall_seconds=allocation["remaining_wall_seconds"],
                     cpu_seconds=allocation["remaining_cpu_seconds"],
                     case_seconds=allocation["remaining_wall_seconds"],
                     oracle_seconds=allocation["remaining_wall_seconds"],
                     run_disk_bytes=allocation["remaining_output_bytes"])

    def stop_guard():
        try:
            if identity.sha256_file(authorization) != approved["authorization_sha256"]:
                return "REMEDIATION_AUTHORIZATION_CHANGED"
            if _read_receipt(binding)["record_sha256"] != claim_tip:
                return "REMEDIATION_CLAIM_RECEIPT_CHANGED"
            budget_allocation(prior, meter.snapshot(run_dir), _extra_bytes(
                run_dir, ledger, ledger_start_bytes, authorization))
        except (OSError, ValueError, WatchdogError, RemediationBudgetError, pilot.H3PilotError):
            return "REMEDIATION_CUMULATIVE_BUDGET_OR_ACCOUNTING_STOP"
        return None

    def audit_guard():
        if stop_guard() is not None:
            raise RemediationBudgetError("Cumulative budget exhausted during final identity audit")

    closed_report = {}

    def completion(summary, log):
        if _original_budget(old_run_dir, state, audit_guard) != prior:
            raise RemediationError("Original accounting changed during execution")
        new, _ = _verify_new_activity(run_dir, packet, state, audit_guard)
        observed = meter.snapshot(run_dir)
        charged = close_charge(prior, observed, _extra_bytes(
            run_dir, ledger, ledger_start_bytes, authorization))
        account = {"schema": "SRT_OBSERVED_REMEDIATION_CUMULATIVE_ACCOUNT_V1",
                   "run_id": run_id, "prior_run_id": packet["prior_run"]["uuid"],
                   "claim_tip": claim_tip, "binding": binding,
                   "old_accounting": prior, "new_controller_observation": observed,
                   "charged": charged, "ledger_start_bytes": ledger_start_bytes,
                   "authorization_bytes": authorization.stat().st_size,
                   "summary_sha256": identity.sha256_file(run_dir / "h3-summary.json"),
                   "completed": new["completed"], "resume_allowed": False}
        digest = pilot._write_new_json(run_dir / ACCOUNT_FILE, account)
        accounted_tip = log.append({"kind": "observed_remediation_accounted", "run_id": run_id,
                    "prior_run_id": packet["prior_run"]["uuid"], "claim_tip": claim_tip,
                    "account_sha256": digest, "summary_sha256": account["summary_sha256"],
                    "completed": account["completed"], "charged": charged, "resume_allowed": False})
        # Last durable writes are covered by the explicitly charged tail, not
        # mislabeled as already measured. A detected overrun invalidates closure.
        closed_document = {
            "schema": "SRT_OBSERVED_REMEDIATION_CLOSED_V1", "run_id": run_id,
            "account_sha256": digest, "accounted_record_tip": accounted_tip,
            "claim_tip": claim_tip, "completed": new["completed"], "resume_allowed": False}
        prospective_closure_bytes = len(identity.canonical_json(closed_document) + b"\n")
        tail = meter.snapshot(run_dir)
        if _tail_exceeds_charge(prior, tail, charged, _extra_bytes(
                run_dir, ledger, ledger_start_bytes, authorization), prospective_closure_bytes):
            log.append({"kind": "observed_remediation_violation", "run_id": run_id,
                        "reason": "CLOSING_RESERVE_EXCEEDED", "resume_allowed": False})
            raise RemediationError("Closing work exceeded its charged reserve")
        # Only a passed tail check may create this exclusive success/failure
        # accounting closure. Removing a whole violation suffix cannot create it.
        pilot._write_new_json(run_dir / CLOSED_FILE, closed_document)
        closed_report.update(_joint_report(binding, packet, new, summary, charged))

    def audited_completion(summary, log):
        try:
            completion(summary, log)
        except BaseException as exc:
            try:
                failed_meter = meter.snapshot(run_dir)
            except BaseException as meter_exc:  # noqa: BLE001 -- uncertainty is not zero consumption
                failed_meter = {"accounting_status": "UNKNOWN_FAIL_CLOSED",
                                "failure_reason": str(meter_exc)[:200]}
            log.append({"kind": "observed_remediation_violation", "run_id": run_id,
                        "reason": "FINAL_AUDIT_OR_ACCOUNTING_FAILED", "failure_type": type(exc).__name__,
                        "failure_reason": str(exc)[:500], "meter": failed_meter,
                        "resume_allowed": False})
            raise

    env = {"SRT_OBS_REMEDIATION_AUTH": str(authorization.resolve(strict=True)),
           "SRT_OBS_REMEDIATION_AUTH_SHA256": approved["authorization_sha256"],
           "SRT_OBS_REMEDIATION_CONFIRMATION": confirmation,
           "SRT_PHASE2_ROOT": check["phase2"], "SRT_PSA_ROOT": check["psa"],
           "SRT_OBS_REMEDIATION_STATE": str(state)}
    summary = pilot._launch_supervised(
        [sys.executable, str(Path(__file__).resolve()), "--runner-child"],
        run_dir=run_dir, state_dir=state, pilot_sha256=provenance.PACKET_SHA256,
        run_id=run_id, head=check["head"], candidate={**RESOURCE_CANDIDATE,
            "workflow": "OBSERVED_ONCE_REMEDIATION", "researcher_authorization": approved,
            "preflight": check, "prior_budget": prior, "allocation": allocation},
        env_extra=env, limits=limits, expected_run_parent=Path(check["run_parent"]),
        admission_check=admission, stop_guard=stop_guard, completion_hook=audited_completion)
    if not closed_report:
        raise RemediationError("No verified cumulative closure")
    return {"status": summary["status"], "run_id": run_id, "joint_verification": closed_report}


def _runner_child() -> int:
    run_dir = Path.cwd()
    try:
        guard_watchdog_parent(int(os.environ["NC0A_WATCHDOG_PARENT_PID"]))
        pilot._write_runner_lease(run_dir)
        path = Path(os.environ["SRT_OBS_REMEDIATION_AUTH"])
        auth = pilot._read_json(path)
        binding = auth["binding"]
        approved = validate_authorization(path, head=binding["head_sha"], run_id=binding["run_uuid"],
            run_dir=run_dir, old_run_dir=Path(binding["prior_run_directory"]),
            confirmation=os.environ["SRT_OBS_REMEDIATION_CONFIRMATION"])
        if approved["authorization_sha256"] != os.environ["SRT_OBS_REMEDIATION_AUTH_SHA256"]:
            raise RemediationError("Authorization changed after claim")
        state = Path(os.environ["SRT_OBS_REMEDIATION_STATE"])
        assert_claim_state(pilot._verified_host_events(state / pilot._HOST_LEDGER), binding,
                           approved["authorization_sha256"], phase="running")
        provenance.verify_original(Path(binding["prior_run_directory"]), state)
        pilot._git_identity(binding["head_sha"])
        packet = provenance.load_packet()
        sample, manifest = validate_sample()
        phases = {}
        with Phase(phases, "remediation_source_job_seed_revalidation"):
            phase2, psa, signatures = runner.validate_private_identities(sample, manifest,
                Path(os.environ["SRT_PHASE2_ROOT"]), Path(os.environ["SRT_PSA_ROOT"]))
        if not identity.h3_runtime_manifest()["replay_environment_matches_recorded_versions_and_candidate_lock"]:
            raise RemediationError("Supervised runtime mismatch")
        cache = RawWindowCache(RESOURCE_CANDIDATE["raw_window_cache_bytes"])
        terminal = runner.execute_rows(packet["suffix_rows"], run_dir=run_dir, admission_phases=phases,
            remediation_identity={"packet_sha256": provenance.PACKET_SHA256,
                                  "suffix_sha256": provenance.SUFFIX_SHA256,
                                  "prior_run_id": packet["prior_run"]["uuid"]},
            process_row=lambda row, phase_sink: runner._private_process_row(
                row, manifest, phase2, psa, signatures, cache, phase_sink))
        return 0 if terminal["status"] == "completed" else 31
    except BaseException as exc:  # noqa: BLE001 -- durable fail-stop, never retry an interrupted child
        with HashChainLog(run_dir / runner.EVIDENCE) as log:
            log.append({"kind": "remediation_admission_exception", "failure_type": type(exc).__name__,
                        "failure_reason": str(exc)[:500], "resume_allowed": False})
            if not (run_dir / "runner-terminal.json").exists():
                pilot._write_new_json(run_dir / "runner-terminal.json", {
                    "kind": "calibration_failed", "status": "failed", "resume_allowed": False,
                    "failure_type": type(exc).__name__, "evidence_tip_sha256": log.previous})
        return 32


def _verify_new_activity(run_dir: Path, packet: dict, state: Path, audit_guard=None) -> tuple:
    """Full science verification happens before the controller closes its meter."""
    summary = pilot._read_json(run_dir / "h3-summary.json")
    evidence_path = run_dir / runner.EVIDENCE
    evidence_events = ([json.loads(line)["event"] for line in evidence_path.read_text().splitlines()]
                       if evidence_path.exists() else [])
    begins = [e for e in evidence_events if e.get("kind") == "observed_calibration_started"]
    expected_identity = {"packet_sha256": provenance.PACKET_SHA256,
                         "suffix_sha256": provenance.SUFFIX_SHA256,
                         "prior_run_id": packet["prior_run"]["uuid"]}
    if begins:
        if (len(begins) != 1 or begins[0].get("remediation_identity") != expected_identity or
                begins[0].get("synthetic_test_only") is not False or
                begins[0].get("rows") != packet["suffix_rows"] or
                begins[0].get("sample_sha256") != runner.EXPECTED_SAMPLE_SHA256):
            raise RemediationError("New science lacks its exact non-synthetic suffix/prior identity")
        new = runner.verify_run(run_dir, state_dir=state, _remediation_packet=packet, _audit_guard=audit_guard)
    else:
        # A crash before science admission is a consumed, failed opportunity,
        # never a completed zero-row activity and never a resumable exception.
        terminal = pilot._verify_recovery_directory(run_dir, host_state_dir=state)
        if terminal["completed"] or summary["status"] == "COMPLETED":
            raise RemediationError("No science admission cannot be completed")
        new = {"completed": False, "rows_verified": 0}
    if (summary["pilot_sha256"] != provenance.PACKET_SHA256 or
            new["completed"] and (new["rows_verified"] != 41 or summary["runner"]["louvain_trials"] != 8200)):
        raise RemediationError("Incomplete or wrong-packet remediation cannot be completed")
    return new, summary


def verify_joint(run_dir: Path, *, state_dir: Path | None = None) -> dict:
    """Read-only OLD/NEW/TOTAL, never a resume operation or U95 calculation."""
    state = state_dir or pilot.default_host_state_dir()
    packet = provenance.load_packet()
    manifest = pilot._read_json(run_dir / "run-manifest.json")
    candidate = manifest["candidate_limits_not_authorized_in_packet"]
    approved = candidate["researcher_authorization"]
    binding = approved["binding"]
    if (str(state) != binding["host_state_directory"] or
            binding != bindings(binding["head_sha"], binding["run_uuid"], run_dir,
                            Path(binding["prior_run_directory"])) or
            manifest["head"]["head_sha"] != binding["head_sha"] or
            binding["remediation_packet_sha256"] != provenance.PACKET_SHA256 or
            binding["suffix_sha256"] != provenance.SUFFIX_SHA256 or
            binding["output_directory"] != str(run_dir) or manifest["run_id"] != binding["run_uuid"]):
        raise RemediationError("Joint run binding mismatch")
    old = _original_budget(Path(binding["prior_run_directory"]), state)
    new, summary = _verify_new_activity(run_dir, packet, state)
    events = pilot._verified_host_events(state / pilot._HOST_LEDGER)
    ledger_lines = (state / pilot._HOST_LEDGER).read_bytes().splitlines(keepends=True)
    records = [json.loads(line) for line in ledger_lines]
    claims = [e for e in events if e.get("kind") == "observed_remediation_claimed" and
              (e.get("prior_run_id") == packet["prior_run"]["uuid"] or
               e.get("full_sample_sha256") == runner.EXPECTED_SAMPLE_SHA256)]
    closes = [e for e in events if e.get("kind") == "observed_remediation_accounted" and
              e.get("run_id") == binding["run_uuid"]]
    if (len(claims) != 1 or claims[0].get("binding") != binding or
            claims[0].get("authorization_sha256") != approved["authorization_sha256"] or
            len(closes) != 1 or any(e.get("kind") in {
                "observed_remediation_violation", "observed_remediation_admission_failed"}
                and e.get("run_id") == binding["run_uuid"] for e in events)):
        raise RemediationError("Exception claim/closure is missing, repeated or invalid")
    account = pilot._read_json(run_dir / ACCOUNT_FILE)
    closed = pilot._read_json(run_dir / CLOSED_FILE)
    claim_index = next(i for i, record in enumerate(records) if record["event"] == claims[0])
    actual_claim_tip = records[claim_index]["record_sha256"]
    close_index = next(i for i, record in enumerate(records) if record["event"] == closes[0])
    receipt = _read_receipt(binding)
    starts = [e for e in events if e.get("kind") == "activity_started" and
              e.get("run_id") == binding["run_uuid"]]
    preflights = [e for e in events if e.get("kind") == "observed_remediation_preflight" and
                  e.get("run_id") == binding["run_uuid"]]
    if (len(starts) != 1 or len(preflights) != 1 or
            starts[0].get("head_sha") != binding["head_sha"] or
            starts[0].get("pilot_sha256") != provenance.PACKET_SHA256 or
            starts[0].get("run_directory") != str(run_dir) or
            identity.sha256_file(run_dir / ACCOUNT_FILE) != closes[0]["account_sha256"] or
            account["binding"] != binding or account["old_accounting"] != old or
            account["run_id"] != binding["run_uuid"] or
            account["prior_run_id"] != packet["prior_run"]["uuid"] or
            account["claim_tip"] != actual_claim_tip or closes[0]["claim_tip"] != actual_claim_tip or
            receipt["record_sha256"] != actual_claim_tip or receipt["event"] != claims[0] or
            account["ledger_start_bytes"] != sum(len(line) for line in ledger_lines[:claim_index]) or
            account["authorization_bytes"] != claims[0]["authorization_bytes"] or
            account["authorization_bytes"] != approved["authorization_bytes"] or
            closed.get("schema") != "SRT_OBSERVED_REMEDIATION_CLOSED_V1" or
            closed.get("run_id") != binding["run_uuid"] or
            closed.get("account_sha256") != closes[0]["account_sha256"] or
            closed.get("accounted_record_tip") != records[close_index]["record_sha256"] or
            closed.get("claim_tip") != actual_claim_tip or
            closed.get("completed") != account["completed"] or closed.get("resume_allowed") is not False or
            closes[0].get("prior_run_id") != packet["prior_run"]["uuid"] or
            closes[0].get("completed") != account["completed"] or
            account.get("resume_allowed") is not False or closes[0].get("resume_allowed") is not False or
            account["charged"] != closes[0]["charged"] or
            account["summary_sha256"] != identity.sha256_file(run_dir / "h3-summary.json") or
            account["completed"] != new["completed"] or
            close_charge(old, account["new_controller_observation"],
                         account["charged"]["extra_output_bytes"]) != account["charged"]):
        raise RemediationError("Cumulative accounting cannot be independently reproduced")
    charged, final_meter = account["charged"], account["new_controller_observation"]
    usage = (summary.get("watchdog") or {}).get("usage", {})
    if (charged["charged_new_wall_seconds"] < max(
            summary["elapsed_controller_seconds"], usage.get("wall_seconds", 0)) or
            charged["charged_new_cpu_seconds"] < usage.get("cpu_seconds", 0) or
            final_meter["wall_seconds"] < preflights[0]["meter"]["wall_seconds"] or
            final_meter["cpu_seconds"] < preflights[0]["meter"]["cpu_seconds"]):
        raise RemediationError("Final account is below independently anchored activity costs")
    # Later unrelated activities may append to this shared ledger. Attribute
    # only the immutable prefix through this exception's closing record.
    ledger_end_bytes = sum(len(line) for line in ledger_lines[:close_index + 1])
    new_attributed = (_directory_bytes(run_dir) + ledger_end_bytes - account["ledger_start_bytes"] +
                      account["authorization_bytes"] + _receipt_path(binding).stat().st_size)
    if (new_attributed < 0 or old["old_output_bytes"] + old.get("old_auxiliary_output_bytes", 0) +
            new_attributed > account["charged"]["charged_total_output_bytes"]):
        raise RemediationError("Actual OLD+NEW files exceed charged output")
    return _joint_report(binding, packet, new, summary, account["charged"])


def _joint_report(binding: dict, packet: dict, new: dict, summary: dict, charged: dict) -> dict:
    return {"status": "VERIFIED_JOINT_TERMINAL", "completed": new["completed"],
            "failure_category": (summary.get("runner") or {}).get(
                "failure_category", summary.get("failure_category")),
            "OLD": {"rows": 6, "trials": 1200, "run_id": packet["prior_run"]["uuid"],
                    "measurement_version": "ORIGINAL_WORKER_HOST_ENDPOINTS"},
            "NEW": {"rows": new["rows_verified"], "trials": 200 * new["rows_verified"],
                    "run_id": binding["run_uuid"], "measurement_version": "EXTERNAL_WATCHDOG_HOST_SAMPLES"},
            "TOTAL": {"unique_rows": 6 + new["rows_verified"],
                      "trials": 1200 + 200 * new["rows_verified"], "resource_charge": charged},
            "resume_allowed": False, "single_continuous_run": False,
            "full_population_U95_supported": False}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--validate-packet", action="store_true")
    mode.add_argument("--authorization-draft", action="store_true")
    mode.add_argument("--preflight", action="store_true")
    mode.add_argument("--run", action="store_true")
    mode.add_argument("--verify", type=Path)
    mode.add_argument("--runner-child", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--head")
    parser.add_argument("--run-id")
    parser.add_argument("--run-dir", type=Path)
    parser.add_argument("--authorization", type=Path)
    parser.add_argument("--researcher-confirmation")
    args = parser.parse_args(argv)
    if args.runner_child:
        return _runner_child()
    if args.validate_packet:
        packet = provenance.load_packet()
        print(json.dumps({"status": packet["status"], "rows": len(packet["suffix_rows"]),
                          "packet_sha256": provenance.PACKET_SHA256,
                          "suffix_sha256": provenance.SUFFIX_SHA256}))
        return 0
    if args.verify:
        print(json.dumps(verify_joint(args.verify)))
        return 0
    if not all((args.head, args.run_id, args.run_dir)):
        parser.error("Explicit final HEAD/new UUID/private directory required")
    roots = [os.environ.get(k, "").strip() for k in ("SRT_PHASE2_ROOT", "SRT_PSA_ROOT")]
    if not all(roots):
        parser.error("Both private roots must be explicitly set")
    phase2, psa = map(Path, roots)
    old = psa / runner.OUTPUT_PARENT / provenance.load_packet()["prior_run"]["uuid"]
    if args.preflight:
        result = preflight(head=args.head, run_id=args.run_id, run_dir=args.run_dir,
                           old_run_dir=old, phase2=phase2, psa=psa)
        print(json.dumps(result))
        return 0 if result["status"] == "PREFLIGHT PASS" else 2
    if args.authorization_draft:
        print(json.dumps(authorization_draft(args.head, args.run_id, args.run_dir, old)))
        return 0
    if not args.authorization or not args.researcher_confirmation:
        parser.error("Separate approved remediation JSON and personal confirmation required")
    result = launch(head=args.head, run_id=args.run_id, run_dir=args.run_dir,
        old_run_dir=old, authorization=args.authorization, confirmation=args.researcher_confirmation,
        phase2=phase2, psa=psa)
    print(json.dumps(result))
    return 2 if result["status"] == "PREFLIGHT NO-GO" else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, WatchdogError, RemediationBudgetError, pilot.H3PilotError) as exc:
        print(f"OBSERVED REMEDIATION REFUSED: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
