"""Authorization-gated, resumable NC-0a formal dispatcher.

The historic detached-signature launcher remains available. A separate,
prospective researcher-authorized route is defined by the versioned amendment
and requires current independent review records plus a public precommit. Neither
route changes the locked scientific workload; tests cannot emit a formal PASS.
"""

from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from hashlib import sha256
import base64
import importlib.metadata
import json
import multiprocessing
import os
from pathlib import Path
import platform
import plistlib
import re
import resource
import shutil
import stat
import subprocess
import sys
import tempfile
import threading
import time
import traceback
import urllib.error
import urllib.request
import uuid
from typing import Iterable

from nc0a_budget_preflight import (
    MACOS_SWAP_TELEMETRY_SEMANTICS, POLICY_V3_MACOS, validate_policy,
)
from nc0a_contract_runner import (
    CHECKPOINTS, CHAIN_COUNT, FORMAL_N, ORACLE_PROPOSALS,
    oracle_trace, save_report_once, screen_case,
    synthetic_chain, validate_full_battery,
)
from nc0a_watchdog import (
    HashChainLog, WatchdogError, WatchdogLimits, guard_watchdog_parent,
    sample_host_memory_pressure, sample_macos_native_state, supervise, validate_hard_memory_backend,
    validate_macos_sampled_backend,
    verify_hash_chain,
)
from nc0a_authority_ledger import AuthorityLedger, AuthorityLedgerError
from nc0a_researcher_authorization import (
    BACKEND as RESEARCHER_BACKEND,
    MEMORY_RISK as RESEARCHER_MEMORY_RISK,
    PACKAGE_FORMAT as RESEARCHER_PACKAGE_FORMAT,
    REQUIRED_RISK_ACKNOWLEDGEMENTS,
    ResearcherAuthorizationError,
    canonical_bytes as _researcher_canonical_bytes,
    commitment_sha256 as _researcher_commitment_sha256,
    parse_github_comment_url,
    validate_package as _validate_researcher_package,
    validate_remote_audit_anchor,
    validate_remote_precommit,
    validate_remote_review,
)
from synthetic_graphs import FAMILIES, make_synthetic_graph, synthetic_seed


ROOT_SEED = 20261009
ENGINEERING_TEST_SEED_ROOT = 8062026
PROTOCOL = {
    "formal_cases": 16,
    "chains_per_case": 8,
    "checkpoints_E": [1, 2, 4, 8, 32],
    "long_chain_proposals": 44_937_216,
    "oracle_streams": 16,
    "proposals_per_oracle": 1_000,
    "total_oracle_proposals": 16_000,
    "comparisons": 48,
    "seed_root": ROOT_SEED,
    "recovery": "TASK_LEVEL_FROM_ZERO_SAME_SEED_NO_OUTCOME_DEPENDENT_RETRY",
}
WATCHDOG_CONTRACT = {
    "implementation": "NC0A_WATCHDOG_V5",
    "poll_seconds": 0.5,
    "wall_clock": "UTC inclusive of sleep; monotonic divergence above 5s stops",
    "cpu_accounting": "process-group ps cumulative TIME plus waited-child rusage and watchdog CPU; 8-worker termination margin",
    "rss_accounting": "CGROUP_V2_HARD enforces exact cgroup memory.max; MACOS_SAMPLED_PRESSURE is sampled telemetry and host-pressure abort only, not a hard cap and may miss transient peaks",
    "worker_accounting": "count only identified multiprocessing.spawn compute workers; sample all group members; unknown members stop",
    "disk_accounting": "run-directory bytes stop at 95% cap; free-disk stop at reserve plus 64MiB or 5% margin",
    "task_deadlines": "case/oracle UTC caps with 99% early-stop margin capped at 60s",
    "termination": "dedicated process group; SIGTERM 0.5s then SIGKILL",
    "monitor_loss": "runner-side parent-PID lease kills the entire process group if watchdog disappears",
    "audit": "fsynced append-only hash chain; no overwrite; unique runner stdout per invocation",
    "macos_controls": "AC power, caffeinate system-sleep assertion, pmset thermal status, sampled current swap-pool telemetry and used-growth abort, V2 free-swap reserve only for V2, internal Data/VM volume reserves, and output-disk reserve",
}
APPROVAL_PURPOSE = "NC0A_FORMAL_EXECUTION_APPROVAL_V1"
MACOS_APPROVAL_PURPOSE = "NC0A_FORMAL_EXECUTION_APPROVAL_V2_MACOS"
MACOS_V3_APPROVAL_PURPOSE = "NC0A_FORMAL_EXECUTION_APPROVAL_V3_MACOS"
ENGINEERING_TEST_APPROVAL_PURPOSE = "NC0A_BOUNDED_ENGINEERING_TEST_APPROVAL_V1"
MODULE_DIR = Path(__file__).resolve().parent
REPOSITORY_ROOT = MODULE_DIR.parents[1]
PREREGISTRATION = REPOSITORY_ROOT / "Experiments" / "SRT_NEURO_SLEEP_POPULATION_NULL_CALIBRATION_PREREGISTRATION_2026-10-09.md"
RUNTIME_LOCK = MODULE_DIR / "nc0a-runtime-macos-arm64.lock"
RESEARCHER_RESOURCE_AMENDMENT = MODULE_DIR / "NC0A_RESEARCHER_AUTHORIZED_EXECUTION_AMENDMENT_V1_2026-10-18.md"
REVIEWER_TRUST_ANCHOR = Path(
    "/Library/Application Support/SRT/NC0A/trusted-reviewer-key.sha256")


class ExecutionError(RuntimeError):
    pass


@dataclass(frozen=True)
class CaseSpec:
    n: int
    family: str
    formal: bool = True

    @property
    def key(self) -> str:
        return f"{self.family}-{self.n}"


def formal_cases() -> tuple[CaseSpec, ...]:
    return tuple(CaseSpec(n, family, True) for n in FORMAL_N for family in FAMILIES)


def _git_head() -> str:
    return _run_registered(["git", "rev-parse", "HEAD"], check=True,
                           capture_output=True, text=True,
                           cwd=REPOSITORY_ROOT).stdout.strip()


def _assert_clean_source_tree() -> None:
    result = _run_registered(["git", "status", "--porcelain", "--untracked-files=all"],
                             check=True, capture_output=True, text=True,
                             cwd=REPOSITORY_ROOT)
    if result.stdout.strip():
        raise ExecutionError("Formal execution requires the approved clean repository tree")


def _sysctl(name: str) -> str:
    result = _run_registered(["/usr/sbin/sysctl", "-n", name], check=True,
                             capture_output=True, text=True, timeout=5)
    return result.stdout.strip()


def _host_identifier() -> str:
    if sys.platform != "darwin" or platform.machine() != "arm64":
        raise ExecutionError("Formal execution is locked to the reviewed macOS/Apple Silicon host class")
    identity = "|".join((platform.node(), platform.machine(), _sysctl("hw.model")))
    return sha256(identity.encode("utf-8")).hexdigest()


def _trusted_reviewer_fingerprint() -> str:
    """Read an administrator-installed trust anchor outside the user's control."""
    if sys.platform != "darwin" or os.geteuid() == 0:
        raise ExecutionError("No administrator-provisioned reviewer trust anchor on the reviewed non-root macOS host")
    chain = [REVIEWER_TRUST_ANCHOR, *REVIEWER_TRUST_ANCHOR.parents]
    try:
        for path in chain:
            if path == Path("/"):
                break
            metadata = path.lstat()
            if stat.S_ISLNK(metadata.st_mode) or metadata.st_uid != 0 or \
               metadata.st_mode & 0o022:
                raise ExecutionError("Reviewer trust-anchor path is not administrator-protected")
        metadata = REVIEWER_TRUST_ANCHOR.lstat()
        if not stat.S_ISREG(metadata.st_mode):
            raise ExecutionError("Reviewer trust anchor is not a regular file")
        value = REVIEWER_TRUST_ANCHOR.read_text(encoding="ascii").strip()
    except OSError as exc:
        raise ExecutionError("No administrator-provisioned independent reviewer trust anchor") from exc
    if not re.fullmatch(r"[0-9a-f]{64}", value):
        raise ExecutionError("Administrator reviewer trust anchor must be a SHA-256 fingerprint")
    return value


def _verify_runtime_lock(policy: dict) -> None:
    lock_bytes = RUNTIME_LOCK.read_bytes()
    if sha256(lock_bytes).hexdigest() != policy.get("runtime_dependency_lock_sha256"):
        raise ExecutionError("Resource policy does not bind the committed NC-0a runtime lock")
    expected = {}
    for line in lock_bytes.decode("utf-8").splitlines():
        if line.startswith("# python=="):
            expected["python"] = line.split("==", 1)[1]
        elif line.startswith("# macOS=="):
            expected["macOS"] = line.split("==", 1)[1]
        elif line.startswith("# architecture=="):
            expected["architecture"] = line.split("==", 1)[1]
        elif "==" in line and not line.lstrip().startswith("#"):
            name, version = line.split("==", 1)
            try:
                actual = importlib.metadata.version(name)
            except importlib.metadata.PackageNotFoundError as exc:
                raise ExecutionError(f"Pinned runtime package missing: {name}") from exc
            if actual != version:
                raise ExecutionError(f"Runtime {name}={actual} differs from lock {version}")
    if sys.version.split()[0] != expected.get("python"):
        raise ExecutionError("Python version differs from the reviewed runtime lock")
    if platform.mac_ver()[0] != expected.get("macOS"):
        raise ExecutionError("macOS version differs from the reviewed runtime lock")
    if platform.machine() != expected.get("architecture"):
        raise ExecutionError("CPU architecture differs from the reviewed runtime lock")
    if int(_sysctl("hw.memsize")) != policy["limits"]["measured_physical_ram_bytes"]:
        raise ExecutionError("Host physical RAM differs from the approved measurement")
    if policy.get("host_identifier") != _host_identifier():
        raise ExecutionError("Resource policy is bound to a different host identity")


def _read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ExecutionError(f"Cannot read JSON file {path.name}") from exc
    if not isinstance(value, dict):
        raise ExecutionError(f"Expected JSON object in {path.name}")
    return value


def _canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def _protocol_hash() -> str:
    return sha256(_canonical(PROTOCOL)).hexdigest()


def _watchdog_contract_hash() -> str:
    return sha256(_canonical(WATCHDOG_CONTRACT)).hexdigest()


def _watchdog_source_hash() -> str:
    return sha256((MODULE_DIR / "nc0a_watchdog.py").read_bytes()).hexdigest()


def verify_ed25519_signature(public_key_path: Path, payload_bytes: bytes,
                             signature: bytes) -> bool:
    """Use the host OpenSSL Ed25519 implementation without shell evaluation."""
    with tempfile.TemporaryDirectory(prefix="nc0a-approval-") as tmp:
        payload = Path(tmp) / "approval.json"
        sigfile = Path(tmp) / "approval.sig"
        payload.write_bytes(payload_bytes)
        sigfile.write_bytes(signature)
        check = _run_registered([
            "openssl", "pkeyutl", "-verify", "-pubin", "-inkey",
            str(public_key_path), "-rawin", "-in", str(payload), "-sigfile", str(sigfile),
        ], capture_output=True, text=True)
        return check.returncode == 0


class ProcessRoleRegistry:
    """Atomic live PID roles for Darwin's lossy ``ps`` command rendering.

    This file is only a live identity bridge. The watchdog still samples every
    process and rejects any PID that is absent from this per-invocation,
    token-bound registry and lacks an independently recognizable command.
    """

    def __init__(self, path: Path, token: str, runner_pid: int):
        if not re.fullmatch(r"[0-9a-f]{64}", token):
            raise ExecutionError("Invalid process-role registry launch token")
        self.path = path
        self.token = token
        self.runner_pid = runner_pid
        self._roles: dict[str, str] = {}
        self._pool_worker_pids: set[str] = set()
        self._tracker_pid: str | None = None
        self._lock = threading.Lock()
        self.publish()

    def publish(self) -> None:
        document = {"format": "NC0A_PROCESS_ROLE_REGISTRY_V1",
                    "launch_token": self.token,
                    "runner_pid": self.runner_pid,
                    "roles": self._roles}
        temporary = self.path.with_name(self.path.name + f".{os.getpid()}.tmp")
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
        fd = os.open(temporary, flags, 0o600)
        try:
            raw = _canonical(document) + b"\n"
            view = memoryview(raw)
            while view:
                written = os.write(fd, view)
                if written <= 0:
                    raise ExecutionError("Short write to process-role registry")
                view = view[written:]
            os.fsync(fd)
        finally:
            os.close(fd)
        os.replace(temporary, self.path)

    def _record(self, pid: int, role: str) -> None:
        try:
            pgid = os.getpgid(pid)
        except (OSError, ProcessLookupError):
            return
        # These PIDs are obtained from Popen/ProcessPoolExecutor objects created
        # by this runner, so their direct parent identity is known at creation;
        # avoid spawning ``ps`` here, which would itself be an unregistered
        # process-group member during the watchdog's sampling window.
        if pgid != self.runner_pid:
            return
        self._roles[str(pid)] = role

    def register_helper(self, pid: int) -> None:
        with self._lock:
            self._record(pid, "runner_helper")
            self.publish()

    def unregister_helper(self, pid: int) -> None:
        with self._lock:
            self._roles.pop(str(pid), None)
            self.publish()

    def register_compute_worker(self, pid: int) -> None:
        with self._lock:
            self._record(pid, "compute_worker")
            self.publish()

    def sync_pool(self, pool: ProcessPoolExecutor) -> None:
        workers = set()
        for process in getattr(pool, "_processes", {}).values():
            pid = getattr(process, "pid", None)
            if pid is not None and process.is_alive():
                workers.add(str(pid))
        from multiprocessing import resource_tracker
        tracker = getattr(resource_tracker, "_resource_tracker", None)
        tracker_pid = getattr(tracker, "_pid", None)
        with self._lock:
            for old_pid in self._pool_worker_pids:
                self._roles.pop(old_pid, None)
            if self._tracker_pid is not None:
                self._roles.pop(self._tracker_pid, None)
            self._pool_worker_pids = set()
            self._tracker_pid = None
            for pid_text in workers:
                self._record(int(pid_text), "compute_worker")
                if pid_text in self._roles:
                    self._pool_worker_pids.add(pid_text)
            if tracker_pid is not None:
                self._record(int(tracker_pid), "resource_tracker")
                if str(tracker_pid) in self._roles:
                    self._tracker_pid = str(tracker_pid)
            self.publish()

    def clear_pool(self) -> None:
        # Python 3.11's spawn resource_tracker may otherwise outlive the runner
        # briefly and be adopted by launchd/PPID 1. The watchdog correctly
        # treats that as an orphaned group member, so reap it before the runner
        # can exit successfully. The runtime is pinned and this private API is
        # covered by end-to-end macOS spawn tests.
        from multiprocessing import resource_tracker
        tracker = getattr(resource_tracker, "_resource_tracker", None)
        if tracker is not None and getattr(tracker, "_pid", None) is not None:
            tracker._stop()
        with self._lock:
            for old_pid in self._pool_worker_pids:
                self._roles.pop(old_pid, None)
            if self._tracker_pid is not None:
                self._roles.pop(self._tracker_pid, None)
            self._pool_worker_pids = set()
            self._tracker_pid = None
            self.publish()


_ACTIVE_PROCESS_ROLE_REGISTRY: ProcessRoleRegistry | None = None
_ACTIVE_EXECUTION_ENVIRONMENT: dict | None = None


def _execution_environment(head: str) -> dict:
    """Use the launcher's frozen environment inside a supervised process group."""
    snapshot = _ACTIVE_EXECUTION_ENVIRONMENT
    if (isinstance(snapshot, dict) and
            snapshot.get("repository_head") == head):
        return snapshot
    return _environment(head)


def _run_registered(*popenargs, **kwargs):
    """subprocess.run semantics with its child PID registered while active."""
    registry = _ACTIVE_PROCESS_ROLE_REGISTRY
    if registry is None:
        return subprocess.run(*popenargs, **kwargs)
    check = kwargs.pop("check", False)
    timeout = kwargs.pop("timeout", None)
    input_data = kwargs.pop("input", None)
    capture_output = kwargs.pop("capture_output", False)
    if capture_output:
        if "stdout" in kwargs or "stderr" in kwargs:
            raise ValueError("stdout and stderr arguments may not be used with capture_output")
        kwargs["stdout"] = subprocess.PIPE
        kwargs["stderr"] = subprocess.PIPE
    if input_data is not None:
        if "stdin" in kwargs:
            raise ValueError("stdin and input arguments may not both be used")
        kwargs["stdin"] = subprocess.PIPE
    with subprocess.Popen(*popenargs, **kwargs) as process:
        registry.register_helper(process.pid)
        try:
            try:
                stdout, stderr = process.communicate(input_data, timeout=timeout)
            except subprocess.TimeoutExpired:
                process.kill()
                stdout, stderr = process.communicate()
                raise
        finally:
            registry.unregister_helper(process.pid)
        result = subprocess.CompletedProcess(process.args, process.returncode,
                                             stdout, stderr)
        if check:
            result.check_returncode()
        return result


def _verify_approval(policy_path: Path, approval_path: Path,
                     public_key_path: Path) -> tuple[dict, dict]:
    """Verify policy schema, exact HEAD/workload and detached Ed25519 approval.

    The trust fingerprint is administrator-installed outside the repository,
    user home, output directory, and run ledger. Missing or user-writable trust
    state always blocks formal execution.
    """
    policy_bytes = policy_path.read_bytes()
    approval = _read_json(approval_path)
    public_key = public_key_path.read_bytes()
    expected_fingerprint = _trusted_reviewer_fingerprint()
    actual_fingerprint = sha256(public_key).hexdigest()
    if actual_fingerprint != expected_fingerprint:
        raise ExecutionError("Reviewer signing key differs from the administrator trust anchor")
    _assert_clean_source_tree()
    raw_policy = _read_json(policy_path)
    validation_summary = validate_policy(raw_policy)
    _verify_runtime_lock(raw_policy)
    signed = dict(approval)
    signature_encoded = signed.pop("signature_ed25519_base64", None)
    if not isinstance(signature_encoded, str):
        raise ExecutionError("Detached reviewer signature is missing")
    if raw_policy.get("purpose") == POLICY_V3_MACOS:
        expected_purpose = MACOS_V3_APPROVAL_PURPOSE
    elif raw_policy.get("memory_enforcement_backend") == "MACOS_SAMPLED_PRESSURE":
        expected_purpose = MACOS_APPROVAL_PURPOSE
    else:
        expected_purpose = APPROVAL_PURPOSE
    if approval.get("purpose") != expected_purpose:
        raise ExecutionError("Wrong formal approval purpose")
    if approval.get("decision") != "APPROVED_FOR_FORMAL_NC0A":
        raise ExecutionError("Formal NC-0a approval decision is absent")
    if approval.get("policy_sha256") != sha256(policy_bytes).hexdigest():
        raise ExecutionError("Approval is not bound to this exact resource policy")
    head = _git_head()
    if approval.get("target_repository_head_sha") != head:
        raise ExecutionError("Approval is not bound to the current repository HEAD")
    if raw_policy.get("target_repository_head_sha") != head:
        raise ExecutionError("Resource policy targets a different repository HEAD")
    if validation_summary.get("review_head") != raw_policy.get("target_repository_head_sha"):
        raise ExecutionError("Resource-policy validation summary does not reproduce its target HEAD")
    if approval.get("formal_experiment_id") != raw_policy.get("formal_experiment_id"):
        raise ExecutionError("Approval is not bound to the unique formal experiment identity")
    preregistration_sha = sha256(PREREGISTRATION.read_bytes()).hexdigest()
    if approval.get("preregistration_sha256") != preregistration_sha:
        raise ExecutionError("Approval does not bind the current preregistration bytes")
    if approval.get("protocol_sha256") != _protocol_hash() or approval.get("protocol") != PROTOCOL:
        raise ExecutionError("Approval does not bind the fixed NC-0a protocol and seeds")
    if (approval.get("watchdog_contract_sha256") != _watchdog_contract_hash() or
        approval.get("watchdog_contract") != WATCHDOG_CONTRACT):
        raise ExecutionError("Approval does not bind the reviewed watchdog stop semantics")
    if approval.get("watchdog_source_sha256") != _watchdog_source_hash():
        raise ExecutionError("Approval does not bind the exact watchdog implementation bytes")
    if approval.get("resource_limits") != raw_policy.get("limits"):
        raise ExecutionError("Approved resource limits differ from the policy")
    reviewer = approval.get("independent_reviewer")
    review_url = approval.get("independent_review_url")
    if not isinstance(reviewer, str) or not reviewer.strip() or not isinstance(review_url, str) or not review_url.startswith("https://"):
        raise ExecutionError("Independent reviewer identity and review URL are required")
    if expected_purpose in (MACOS_APPROVAL_PURPOSE, MACOS_V3_APPROVAL_PURPOSE):
        bound_fields = {
            "resource_amendment_status": "INDEPENDENTLY_APPROVED",
            "resource_amendment_approver": raw_policy.get("resource_amendment_approver"),
            "resource_amendment_sha256": raw_policy.get("resource_amendment_sha256"),
            "resource_amendment_approval_record_url": raw_policy.get(
                "resource_amendment_approval_record_url"),
            "macos_memory_semantics": raw_policy.get("memory_limit_semantics"),
            "macos_residual_risk_acceptance": raw_policy.get(
                "macos_residual_risk_acceptance"),
            "reviewer_key_fingerprint_sha256": expected_fingerprint,
        }
        for field, expected_value in bound_fields.items():
            if approval.get(field) != expected_value:
                raise ExecutionError("macOS signed approval is missing/changing " + field)
        if raw_policy.get("purpose") == POLICY_V3_MACOS:
            if approval.get("macos_swap_telemetry_semantics") != \
                    raw_policy.get("macos_swap_telemetry_semantics") or \
                    approval.get("macos_swap_telemetry_semantics") != \
                    MACOS_SWAP_TELEMETRY_SEMANTICS:
                raise ExecutionError("V3 approval does not bind current-pool-only swap telemetry semantics")
    if approval.get("operational_attempts_per_case") not in (1, 2):
        raise ExecutionError("Only one or two prospectively approved operational attempts are supported")
    if approval.get("retry_rule") != PROTOCOL["recovery"]:
        raise ExecutionError("Approval permits an unfrozen or outcome-dependent retry rule")
    try:
        signature = base64.b64decode(signature_encoded, validate=True)
    except ValueError as exc:
        raise ExecutionError("Malformed Ed25519 signature") from exc
    if not verify_ed25519_signature(public_key_path, _canonical(signed), signature):
        raise ExecutionError("Independent Ed25519 approval signature did not verify")
    return raw_policy, approval


def _environment(head: str) -> dict:
    packages = {}
    for name in ("numpy", "scipy", "networkx", "python-louvain"):
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            packages[name] = "NOT_INSTALLED"
    try:
        host_identifier = _host_identifier()
    except ExecutionError:
        host_identifier = "NONPRODUCTION-" + sha256(
            f"{platform.node()}|{platform.machine()}".encode()).hexdigest()
    return {
        "repository_head": head,
        "python": sys.version,
        "python_executable": sys.executable,
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "host_identifier": host_identifier,
        "physical_ram_bytes": int(_sysctl("hw.memsize")) if sys.platform == "darwin" else None,
        "runtime_lock_sha256": sha256(RUNTIME_LOCK.read_bytes()).hexdigest(),
        "preregistration_sha256": sha256(PREREGISTRATION.read_bytes()).hexdigest(),
        "packages": packages,
        "source_sha256": {
            name: sha256((MODULE_DIR / name).read_bytes()).hexdigest()
            for name in ("nc0a_contract_runner.py", "synthetic_graphs.py",
                         "connected_swap.py", "test_anomaly_screen.py",
                         "nc0a_execution_engine.py", "nc0a_watchdog.py",
                         "nc0a_budget_preflight.py", "nc0a_authority_ledger.py",
                         "nc0a_researcher_authorization.py")
        },
    }


def _researcher_seed_manifest() -> dict:
    return {
        spec.key: {
            "fixture_seed": synthetic_seed(spec.family, spec.n, root=ROOT_SEED),
            "chain_seeds": [synthetic_seed(spec.family, spec.n, kind="chain",
                                            chain_index=i, root=ROOT_SEED)
                            for i in range(CHAIN_COUNT)],
            "bfs_seed": synthetic_seed(spec.family, spec.n,
                                       kind="bfs-identity", root=ROOT_SEED),
        }
        for spec in formal_cases()
    }


def _researcher_scientific_protocol() -> dict:
    from test_anomaly_screen import PAIRED_T_CRITICAL
    return {
        **PROTOCOL,
        "families": list(FAMILIES),
        "node_sizes": list(FORMAL_N),
        "anomaly_screen": {
            "metrics": ["triangle_count", "degree_assortativity",
                        "initial_edge_overlap"],
            "paired_chain_count": CHAIN_COUNT,
            "comparison_count": 48,
            "familywise_alpha": 0.05,
            "bonferroni_critical_t_df7": PAIRED_T_CRITICAL,
            "checkpoints_E": list(CHECKPOINTS),
            "all_48_must_pass": True,
        },
        "oracle": {"independent_streams": 16,
                   "attempts_per_stream": ORACLE_PROPOSALS,
                   "total_attempts": 16 * ORACLE_PROPOSALS},
        "mixing_interpretation": "MIXING-UNRESOLVED",
        "any_failed_screen_or_invariant": "NC0A_NO_GO_NO_OUTCOME_DEPENDENT_RERUN",
    }


def _disk_volume_identity(path: str | Path) -> dict:
    """Map a path to one of the reviewed internal Data/VM APFS volumes.

    ``diskutil info`` accepts mounted-volume paths, not arbitrary directories.
    Identify Data and VM directly, then map a result directory by its device
    number; never infer a volume identity from its spelling or parent name.
    """
    target = Path(path).expanduser().resolve(strict=False)
    probe = target
    while not probe.exists() and probe != probe.parent:
        probe = probe.parent
    if not probe.exists():
        raise ExecutionError("Output path has no existing parent volume")
    try:
        target_device = os.stat(probe).st_dev
    except OSError as exc:
        raise ExecutionError("Cannot stat the existing output-path parent") from exc
    for mount in ("/System/Volumes/Data", "/System/Volumes/VM"):
        result = subprocess.run(["/usr/sbin/diskutil", "info", "-plist", mount],
                                check=True, capture_output=True, timeout=10)
        try:
            info = plistlib.loads(result.stdout)
            mount_point = str(info["MountPoint"])
            mount_device = os.stat(mount_point).st_dev
        except (KeyError, TypeError, OSError, ValueError) as exc:
            raise ExecutionError("Cannot parse/stat internal APFS volume identity") from exc
        if target_device != mount_device:
            continue
        try:
            return {
                "mount_point": mount_point,
                "filesystem": str(info.get("FilesystemName") or info["FilesystemType"]).upper(),
                "internal": bool(info["Internal"]),
                "volume_uuid": str(info.get("VolumeUUID") or info["DiskUUID"]).upper(),
                "device_identifier": str(info["DeviceIdentifier"]),
            }
        except (KeyError, TypeError) as exc:
            raise ExecutionError("diskutil did not return a complete APFS volume identity") from exc
    raise ExecutionError("Path is not on either reviewed internal Data or VM volume")


def _resolved_non_symlink_path(path: str | Path) -> Path:
    """Resolve a run path only after rejecting symlinks in its lexical path.

    Calling ``Path.resolve`` first erases evidence that the user supplied a
    symlink. The formal run identity must be the same ordinary directory that
    was inspected and recorded in the public commitment.
    """
    lexical = Path(os.path.abspath(os.path.expanduser(os.fspath(path))))
    cursor = Path(lexical.anchor)
    for component in lexical.parts[1:]:
        cursor = cursor / component
        try:
            metadata = cursor.lstat()
        except FileNotFoundError:
            continue
        except OSError as exc:
            raise ExecutionError(f"Cannot inspect formal output path component: {cursor}") from exc
        if stat.S_ISLNK(metadata.st_mode):
            raise ExecutionError("Formal run path cannot contain a symlink component")
    return lexical.resolve(strict=False)


def _researcher_context(run_dir: str | Path) -> dict:
    """Collect current immutable identities and read-only host/output facts."""
    if sys.platform != "darwin" or platform.machine() != "arm64":
        raise ExecutionError("Researcher-authorized policy is restricted to the reviewed Apple Silicon Mac")
    head = _git_head()
    status = _run_registered(["git", "status", "--porcelain", "--untracked-files=all"],
                             check=True, capture_output=True, text=True,
                             cwd=REPOSITORY_ROOT).stdout.strip()
    env = _environment(head)
    output = _resolved_non_symlink_path(run_dir)
    if output == REPOSITORY_ROOT or REPOSITORY_ROOT in output.parents:
        raise ExecutionError("Formal output directory must be outside the repository")
    data = _disk_volume_identity("/System/Volumes/Data")
    vm = _disk_volume_identity("/System/Volumes/VM")
    output_volume = _disk_volume_identity(output)
    if data["filesystem"] != "APFS" or vm["filesystem"] != "APFS":
        raise ExecutionError("Internal Data and VM volumes must be APFS")
    return {
        "head_sha": head,
        "clean_tree": not bool(status),
        "preregistration_sha256": sha256(PREREGISTRATION.read_bytes()).hexdigest(),
        "resource_amendment_sha256": sha256(RESEARCHER_RESOURCE_AMENDMENT.read_bytes()).hexdigest(),
        "runtime_lock_sha256": sha256(RUNTIME_LOCK.read_bytes()).hexdigest(),
        "protocol_sha256": _protocol_hash(),
        "seed_manifest_sha256": sha256(_canonical(_researcher_seed_manifest())).hexdigest(),
        "watchdog_contract_sha256": _watchdog_contract_hash(),
        "watchdog_source_sha256": _watchdog_source_hash(),
        "source_sha256": env["source_sha256"],
        "environment": env,
        "data_volume": data,
        "vm_volume": vm,
        "output_volume": output_volume,
        "output_directory": str(output),
        "scientific_protocol": _researcher_scientific_protocol(),
        "current_data_free_bytes": shutil.disk_usage("/System/Volumes/Data").free,
        "current_vm_free_bytes": shutil.disk_usage("/System/Volumes/VM").free,
        "current_host_memory_pressure": sample_host_memory_pressure(),
        "current_macos_native_state": sample_macos_native_state(),
    }


def _fetch_pr_comment(url: str) -> dict:
    comment_id = parse_github_comment_url(url)
    api_url = f"https://api.github.com/repos/zyx1st-png/SRT-Pub/issues/comments/{comment_id}"
    request = urllib.request.Request(
        api_url,
        headers={"Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28",
                 "User-Agent": "SRT-Pub-NC0a-Researcher-Authorization"},
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            payload = json.loads(response.read())
    except (urllib.error.URLError, TimeoutError, ValueError, OSError) as exc:
        raise ExecutionError("Cannot verify public PR #1114 commitment/review comment") from exc
    if (payload.get("html_url") != url or
            not str(payload.get("issue_url", "")).endswith("/issues/1114")):
        raise ExecutionError("GitHub record is not a top-level comment on PR #1114")
    return payload


def _fetch_pr_head() -> dict:
    request = urllib.request.Request(
        "https://api.github.com/repos/zyx1st-png/SRT-Pub/pulls/1114",
        headers={"Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28",
                 "User-Agent": "SRT-Pub-NC0a-Researcher-Authorization"},
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            payload = json.loads(response.read())
    except (urllib.error.URLError, TimeoutError, ValueError, OSError) as exc:
        raise ExecutionError("Cannot verify the live PR #1114 head") from exc
    if not isinstance(payload, dict) or not isinstance(payload.get("head"), dict):
        raise ExecutionError("GitHub PR #1114 response lacks a head identity")
    return payload


def _verify_current_remote_pr_head(expected_head: str, fetcher=None) -> None:
    payload = (fetcher or _fetch_pr_head)()
    if payload.get("head", {}).get("sha") != expected_head:
        raise ExecutionError("Current GitHub PR #1114 HEAD differs from the frozen commitment")


def _list_pr_comments() -> list[dict]:
    """Fetch the visible top-level PR comments used as public audit copies.

    This is a replay-detection aid only. GitHub comments remain editable by
    repository administrators and are not an immutable or independent ledger.
    """
    comments = []
    for page in range(1, 21):
        api_url = ("https://api.github.com/repos/zyx1st-png/SRT-Pub/issues/1114/comments"
                   f"?per_page=100&page={page}")
        request = urllib.request.Request(
            api_url,
            headers={"Accept": "application/vnd.github+json",
                     "X-GitHub-Api-Version": "2022-11-28",
                     "User-Agent": "SRT-Pub-NC0a-Researcher-Authorization"},
        )
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                batch = json.loads(response.read())
        except (urllib.error.URLError, TimeoutError, ValueError, OSError) as exc:
            raise ExecutionError("Cannot inspect public PR #1114 audit history") from exc
        if not isinstance(batch, list):
            raise ExecutionError("GitHub PR comment listing returned an invalid payload")
        for comment in batch:
            if not str(comment.get("issue_url", "")).endswith("/issues/1114"):
                raise ExecutionError("GitHub returned a comment outside PR #1114")
        comments.extend(batch)
        if len(batch) < 100:
            return comments
    raise ExecutionError("PR #1114 comment history exceeds the checked audit-history page limit")


def _verify_remote_audit_history(package: dict, finished: list[dict],
                                 resume_anchor_url: str | None,
                                 comment_lister=None) -> None:
    """Prevent ordinary local-log deletion from looking like a first run."""
    comments = (comment_lister or _list_pr_comments)()
    commitment = package["commitment"]
    experiment_uuid = commitment["experiment_uuid"]
    commitment_sha = package["commitment_sha256"]
    matched = []
    for comment in comments:
        body = comment.get("body", "")
        if "NC0A_AUDIT_SUMMARY_JSON_BASE64=" not in body:
            continue
        try:
            summary = validate_remote_audit_anchor_payload(body)
        except ResearcherAuthorizationError as exc:
            raise ExecutionError(
                "A malformed public NC-0a audit anchor prevents safe replay classification") from exc
        if (summary.get("experiment_uuid") == experiment_uuid and
                summary.get("commitment_sha256") == commitment_sha):
            matched.append((str(comment.get("created_at", "")),
                            comment.get("html_url"), summary))
    if not matched:
        if finished:
            raise ExecutionError("Local invocations exist without their public audit-summary copies")
        return
    if not finished:
        raise ExecutionError(
            "A public audit summary exists for this experiment but local invocation logs do not; "
            "possible log loss/replay requires manual audit")
    matched.sort(key=lambda item: item[0])
    if len(finished) != len(matched):
        raise ExecutionError("Local invocation count differs from visible public audit summaries")
    expected_invocations = list(range(1, len(finished) + 1))
    if [item[2].get("invocation_count") for item in matched] != expected_invocations:
        raise ExecutionError("Public audit summaries do not form the expected invocation sequence")
    if not resume_anchor_url or matched[-1][1] != resume_anchor_url:
        raise ExecutionError("Resume must use the latest public summary for this experiment")


def validate_remote_audit_anchor_payload(body: str) -> dict:
    """Decode one summary marker without accepting an absent or duplicate marker."""
    from nc0a_researcher_authorization import marker_payload
    return marker_payload(body, "NC0A_AUDIT_SUMMARY_JSON_BASE64")


def _researcher_limits(commitment: dict) -> WatchdogLimits:
    policy = commitment["resource_policy"]
    caps = policy["limits"]
    return WatchdogLimits(
        wall_seconds=caps["wall_seconds"],
        cpu_seconds=caps["cpu_seconds"],
        aggregate_rss_bytes=caps["sampled_rss_bytes"],
        max_workers=caps["max_workers"],
        run_disk_bytes=caps["run_output_cap_bytes"],
        reserve_free_disk_bytes=caps["run_output_reserve_bytes"],
        case_seconds=caps["per_case_seconds"],
        oracle_seconds=caps["oracle_seconds"],
        memory_enforcement_backend=RESEARCHER_BACKEND,
        host_memory_free_percent_stop=caps["host_free_percent_stop"],
        boot_volume_path="/System/Volumes/Data",
        boot_reserve_free_disk_bytes=caps["data_reserve_bytes"],
        minimum_boot_free_disk_bytes=caps["data_min_free_bytes"],
        swap_volume_path="/System/Volumes/VM",
        swap_volume_reserve_free_disk_bytes=caps["vm_reserve_bytes"],
        minimum_swap_volume_free_disk_bytes=caps["vm_min_free_bytes"],
        swap_growth_stop_bytes=caps["swap_growth_bytes"],
        require_ac_power=policy["require_ac_power"],
        require_thermal_normal=policy["require_normal_thermal_state"],
        require_sleep_assertion=policy["require_sleep_assertion"],
    )


def _researcher_runner_entry(run_dir: str, snapshot_path: str,
                             commitment_sha: str, max_attempts: int) -> int:
    global _ACTIVE_PROCESS_ROLE_REGISTRY, _ACTIVE_EXECUTION_ENVIRONMENT
    token = os.environ.get("NC0A_WATCHDOG_LAUNCH_TOKEN", "")
    parent = os.environ.get("NC0A_WATCHDOG_PARENT_PID", "")
    if not re.fullmatch(r"[0-9a-f]{64}", token) or parent != str(os.getppid()):
        raise ExecutionError("Researcher runner must be a child of the active watchdog")
    root = Path(run_dir).resolve()
    role_path = Path(os.environ.get("NC0A_PROCESS_ROLE_REGISTRY", ""))
    if role_path.parent.resolve() != root:
        raise ExecutionError("Process-role registry is outside the researcher run directory")
    snapshot = _read_json(Path(snapshot_path))
    commitment = snapshot.get("commitment")
    if (snapshot.get("format") != RESEARCHER_PACKAGE_FORMAT or
            _researcher_commitment_sha(commitment) != commitment_sha or
            snapshot.get("commitment_sha256") != commitment_sha or
            Path(commitment["resource_policy"]["output_directory"]).resolve() != root):
        raise ExecutionError("Researcher commitment snapshot is invalid or belongs to another run")
    if max_attempts != commitment["resource_policy"]["limits"]["max_attempts_per_case"]:
        raise ExecutionError("Retry count differs from the frozen researcher commitment")
    if _git_head() != commitment["repository"]["head_sha"]:
        raise ExecutionError("Repository HEAD changed after researcher precommit")
    _assert_clean_source_tree()
    _ACTIVE_PROCESS_ROLE_REGISTRY = ProcessRoleRegistry(role_path, token, os.getpid())
    _ACTIVE_EXECUTION_ENVIRONMENT = commitment["environment"]
    guard_watchdog_parent(int(parent))
    limits = _researcher_limits(commitment)
    result = _run_battery_core(
        root, cases=formal_cases(), workers=limits.max_workers,
        case_seconds=limits.case_seconds, oracle_seconds=limits.oracle_seconds,
        max_attempts_per_case=max_attempts, formal=True,
        policy_hash=commitment_sha, head=commitment["repository"]["head_sha"],
        process_role_registry=_ACTIVE_PROCESS_ROLE_REGISTRY)
    print(json.dumps(result, sort_keys=True))
    return 0


def _read_chain_rows(path: Path) -> tuple[list[dict], str]:
    if not path.exists():
        return [], "0" * 64
    verify_hash_chain(path)
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
    return rows, rows[-1]["record_sha256"] if rows else "0" * 64


def _researcher_invocation_history(root: Path) -> tuple[list[dict], str]:
    path = root / "researcher_authorization.jsonl"
    rows, tip = _read_chain_rows(path)
    active = None
    finished = []
    for row in rows:
        event = row.get("event", {})
        if event.get("event") == "invocation_started":
            if active is not None:
                raise ExecutionError("Overlapping researcher invocations; manual audit required")
            active = event
        elif event.get("event") == "invocation_finished":
            if active is None or event.get("invocation") != active.get("invocation"):
                raise ExecutionError("Researcher invocation ledger has an unmatched terminal event")
            if not isinstance(event.get("usage"), dict):
                raise ExecutionError("Invocation terminal lacks resource usage")
            finished.append(event)
            active = None
    if active is not None:
        raise ExecutionError(
            "An invocation has no durable terminal record; cost is unknown and resume is blocked")
    return finished, tip


def _watchdog_invocation_history(root: Path) -> tuple[int, int, str]:
    rows, tip = _read_chain_rows(root / "watchdog.jsonl")
    active = False
    starts = terminals = 0
    for row in rows:
        event = row.get("event", {}).get("event")
        if event == "run_started":
            if active:
                raise ExecutionError("Watchdog audit contains overlapping process groups")
            starts += 1
            active = True
        elif event in ("runner_exited", "watchdog_stop", "watchdog_exception"):
            if event == "watchdog_exception" and not active:
                # Exceptions before process creation are charged in the
                # researcher invocation log, but have no process-group start.
                continue
            if not active:
                raise ExecutionError("Watchdog terminal event has no matching run start")
            if not isinstance(row.get("event", {}).get("usage"), dict):
                raise ExecutionError("Watchdog terminal event lacks resource accounting")
            terminals += 1
            active = False
    if active or starts != terminals:
        raise ExecutionError(
            "Watchdog start/terminal events do not pair; unknown cost blocks automatic resume")
    return starts, terminals, tip


def _verify_researcher_stdout_history(root: Path,
                                     finished: list[dict]) -> set[str]:
    """Admit only Watchdog stdout files bound to a finished invocation.

    Current Watchdog records carry the researcher invocation number directly.
    Logs written before that field was added are supported by pairing their
    ordered stdout digests with the ordered watchdog_started records.
    Every output must be present, a regular non-symlink file, canonically
    numbered, and byte-for-byte consistent with the Watchdog hash record.
    """
    auth_by_invocation = {}
    for expected_number, event in enumerate(finished, start=1):
        invocation = event.get("invocation")
        if type(invocation) is not int or invocation != expected_number:
            raise ExecutionError("Researcher invocation numbering is not contiguous")
        auth_by_invocation[invocation] = event
    rows, _ = _read_chain_rows(root / "watchdog.jsonl")
    output_events: list[tuple[int | None, str]] = []
    for row in rows:
        event = row.get("event", {})
        name = event.get("event")
        if name not in ("runner_exited", "watchdog_stop", "watchdog_exception",
                        "watchdog_setup_failed"):
            continue
        usage = event.get("usage", {})
        digest = event.get("runner_stdout_sha256")
        if digest is None and isinstance(usage, dict):
            digest = usage.get("runner_stdout_sha256")
        if digest is None:
            if name in ("runner_exited", "watchdog_stop"):
                raise ExecutionError("Watchdog terminal record lacks its stdout digest")
            continue
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ExecutionError("Watchdog stdout digest is malformed")
        invocation = event.get("invocation")
        if invocation is not None and (type(invocation) is not int or invocation < 1):
            raise ExecutionError("Watchdog stdout invocation number is invalid")
        output_events.append((invocation, digest))

    expected: dict[int, str] = {}
    legacy_digests = []
    for invocation, digest in output_events:
        if invocation is None:
            legacy_digests.append(digest)
            continue
        if invocation not in auth_by_invocation:
            raise ExecutionError("Watchdog stdout refers to an unknown researcher invocation")
        if invocation in expected:
            raise ExecutionError("Watchdog recorded more than one stdout digest for an invocation")
        expected[invocation] = digest

    legacy_invocations = [
        invocation for invocation, event in sorted(auth_by_invocation.items())
        if event.get("watchdog_started") and invocation not in expected
    ]
    if len(legacy_invocations) != len(legacy_digests):
        raise ExecutionError("Legacy Watchdog stdout history cannot be paired with invocation records")
    expected.update(zip(legacy_invocations, legacy_digests))

    for invocation, event in auth_by_invocation.items():
        if event.get("watchdog_started") and invocation not in expected:
            raise ExecutionError("A started Watchdog invocation has no stdout digest record")

    actual: dict[int, Path] = {}
    for entry in root.iterdir():
        if not entry.name.startswith("runner.stdout"):
            continue
        match = re.fullmatch(r"runner\.stdout\.(\d{2,})\.log", entry.name)
        if not match:
            raise ExecutionError("Run directory contains an invalid Watchdog stdout filename")
        invocation = int(match.group(1))
        if invocation < 1 or entry.name != f"runner.stdout.{invocation:02d}.log":
            raise ExecutionError("Watchdog stdout invocation number is not canonical")
        if entry.is_symlink() or not entry.is_file():
            raise ExecutionError("Watchdog stdout must be a regular non-symlink file")
        if invocation in actual:
            raise ExecutionError("Duplicate Watchdog stdout invocation number")
        actual[invocation] = entry

    if set(actual) != set(expected):
        raise ExecutionError("Watchdog stdout files do not match the recorded invocation history")
    for invocation, path in actual.items():
        digest = sha256()
        with path.open("rb") as handle:
            for block in iter(lambda: handle.read(1 << 20), b""):
                digest.update(block)
        if digest.hexdigest() != expected[invocation]:
            raise ExecutionError("Watchdog stdout hash differs from its chained audit record")
    return {path.name for path in actual.values()}


def _first_invocation_epoch(root: Path) -> float | None:
    rows, _ = _read_chain_rows(root / "researcher_authorization.jsonl")
    for row in rows:
        event = row.get("event", {})
        if event.get("event") == "invocation_started":
            return float(event["started_utc_epoch"])
    return None


def _researcher_audit_summary(root: Path, package: dict,
                              as_of_epoch: float | None = None) -> dict:
    finished, authorization_tip = _researcher_invocation_history(root)
    starts, terminals, watchdog_tip = _watchdog_invocation_history(root)
    if sum(bool(row.get("watchdog_started")) for row in finished) != starts:
        raise ExecutionError("Researcher and watchdog invocation counts differ")
    execution_path = root / "execution.jsonl"
    if execution_path.exists():
        _, execution_tip = _read_chain_rows(execution_path)
    else:
        execution_tip = "0" * 64
    cumulative_wall = sum(float(row["usage"].get("wall_seconds", 0)) for row in finished)
    cumulative_cpu = sum(float(row["usage"].get("cpu_seconds", 0)) for row in finished)
    manifest_path = root / "run_manifest.json"
    manifest_sha = sha256(manifest_path.read_bytes()).hexdigest() if manifest_path.is_file() else None
    result_hashes = {}
    for result_path in sorted(root.glob("cases/*/attempt-*/result.json")):
        result_hashes[str(result_path.relative_to(root))] = sha256(result_path.read_bytes()).hexdigest()
    final_path = root / "formal_battery_summary.json"
    formal_summary = None
    if final_path.is_file():
        formal_summary = json.loads(final_path.read_text(encoding="utf-8"))
    first_epoch = _first_invocation_epoch(root)
    summary_epoch = time.time() if as_of_epoch is None else as_of_epoch
    return {
        "format": "NC0A_RESEARCHER_AUTHORIZED_AUDIT_SUMMARY_V1",
        "experiment_uuid": package["commitment"]["experiment_uuid"],
        "commitment_sha256": package["commitment_sha256"],
        "repository_head_sha": package["commitment"]["repository"]["head_sha"],
        "invocation_count": len(finished),
        "watchdog_start_count": starts,
        "watchdog_terminal_count": terminals,
        "cumulative_accounted_wall_seconds": cumulative_wall,
        "cumulative_accounted_cpu_seconds": cumulative_cpu,
        "elapsed_wall_seconds_from_first_invocation_at_summary": (
            max(0.0, summary_epoch - first_epoch) if first_epoch is not None else 0.0),
        "summary_created_at_epoch": summary_epoch,
        "authorization_log_tip_sha256": authorization_tip,
        "watchdog_log_tip_sha256": watchdog_tip,
        "execution_log_tip_sha256": execution_tip,
        "run_manifest_sha256": manifest_sha,
        "case_result_sha256": result_hashes,
        "formal_battery_summary": formal_summary,
        "mixing_interpretation": "MIXING-UNRESOLVED",
        "third_party_authorization": False,
        "local_hash_chain_is_not_immutable_custody": True,
    }


def _verify_completed_researcher_battery(root: Path, commitment: dict) -> dict:
    """Recompute the full-battery decision before the launcher reports success."""
    manifest_path = root / "run_manifest.json"
    manifest_side = root / "run_manifest.json.sha256"
    if not manifest_path.is_file() or not manifest_side.is_file():
        raise ExecutionError("Runner exited zero without a complete run manifest")
    manifest_digest = sha256(manifest_path.read_bytes()).hexdigest()
    if manifest_side.read_text(encoding="ascii").split()[0] != manifest_digest:
        raise ExecutionError("Formal run manifest SHA-256 mismatch")
    manifest = _read_json(manifest_path)
    if (manifest.get("formal_contract") is not True or
            manifest.get("repository_head") != commitment["repository"]["head_sha"] or
            manifest.get("resource_policy_sha256") != commitment_sha256_for_run(commitment) or
            manifest.get("protocol") != PROTOCOL or
            manifest.get("seed_manifest") != _researcher_seed_manifest()):
        raise ExecutionError("Formal manifest differs from the frozen commitment or protocol")
    execution_rows = _read_execution_records(root / "execution.jsonl")
    completed_events = [row["event"] for row in execution_rows
                        if row.get("event", {}).get("event") == "case_attempt_completed"]
    wanted = {spec.key: spec for spec in formal_cases()}
    if (len(completed_events) != len(wanted) or
            {e.get("case") for e in completed_events} != set(wanted)):
        raise ExecutionError("Runner exited zero without exactly one completed event per fixed case")
    reports = []
    oracle_reports = []
    for event in completed_events:
        spec = wanted[event["case"]]
        report_path = (root / "cases" / spec.key /
                       f"attempt-{int(event['attempt']):02d}" / "result.json")
        try:
            report = json.loads(report_path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            raise ExecutionError(f"Completed case result is missing/corrupt: {spec.key}") from exc
        digest = _verify_case_report(report_path, spec, report)
        if digest != event.get("report_sha256"):
            raise ExecutionError("Execution event does not anchor the completed case result")
        reports.append({"n": report["n"], "family": report["family"],
                        "metrics": report["screen"]["metrics"],
                        "anomaly_screen_pass": report["screen"]["anomaly_screen_pass"]})
        oracle = report["oracle"]
        oracle_reports.append({"n": report["n"], "family": report["family"],
                              "attempts": oracle["attempts"],
                              "oracle_mismatches": oracle["oracle_mismatches"],
                              "accepted_local_audits": oracle["accepted_local_audits"],
                              "accepted": oracle["accepted"]})
    summary = validate_full_battery(reports, oracle_reports)
    summary_path = root / "formal_battery_summary.json"
    summary_side = Path(str(summary_path) + ".sha256")
    if not summary_path.is_file() or not summary_side.is_file():
        raise ExecutionError("Formal summary or checksum is missing")
    summary_digest = sha256(summary_path.read_bytes()).hexdigest()
    if summary_side.read_text(encoding="ascii").split()[0] != summary_digest:
        raise ExecutionError("Formal summary SHA-256 mismatch")
    stored = _read_json(summary_path)
    if stored != summary:
        raise ExecutionError("Formal summary does not reproduce from all 16 case/oracle reports")
    return stored


def commitment_sha256_for_run(commitment: dict) -> str:
    """Local import avoids coupling the report verifier to package parsing."""
    return _researcher_commitment_sha256(commitment)


def _write_once_bytes(path: Path, raw: bytes) -> str:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        view = memoryview(raw)
        while view:
            written = os.write(fd, view)
            if written <= 0:
                raise ExecutionError("Short write while saving immutable run evidence")
            view = view[written:]
        os.fsync(fd)
    finally:
        os.close(fd)
    return sha256(raw).hexdigest()


def _save_researcher_audit_summary(root: Path, package: dict,
                                   invocation: int) -> dict:
    summary = _researcher_audit_summary(root, package)
    payload = (_researcher_canonical_bytes(summary) + b"\n")
    digest = _write_once_bytes(
        root / "audit-summaries" / f"invocation-{invocation:02d}.json", payload)
    return {"summary": summary, "summary_sha256": digest,
            "github_anchor_body": (
                "NC0A_AUDIT_SUMMARY_SHA256=" + digest + "\n" +
                "NC0A_AUDIT_SUMMARY_JSON_BASE64=" +
                base64.b64encode(_researcher_canonical_bytes(summary)).decode("ascii"))}


def _verify_resume_anchor(root: Path, package: dict, url: str,
                          comment_fetcher=None) -> None:
    finished, _ = _researcher_invocation_history(root)
    if not finished:
        if url:
            raise ExecutionError("A first invocation must not use a resume audit anchor")
        return
    if not url:
        raise ExecutionError("Resume requires a public GitHub audit-summary anchor from the prior invocation")
    comment_id = parse_github_comment_url(url)
    del comment_id
    fetch = comment_fetcher or _fetch_pr_comment
    comment = fetch(url)
    if comment.get("user", {}).get("login") != package["commitment"]["researcher"]["github_login"]:
        raise ExecutionError("Resume audit anchor was not posted by the named researcher account")
    latest_index = len(finished)
    summary_path = root / "audit-summaries" / f"invocation-{latest_index:02d}.json"
    if summary_path.is_symlink() or not summary_path.is_file():
        raise ExecutionError("Prior invocation has no saved audit-summary artifact")
    saved = json.loads(summary_path.read_text(encoding="utf-8"))
    if _researcher_canonical_bytes(saved) != _researcher_canonical_bytes(
            _researcher_audit_summary(
                root, package, as_of_epoch=float(saved["summary_created_at_epoch"]))):
        raise ExecutionError("Prior audit summary no longer matches local chained records")
    remote = comment.get("body", "")
    expected_digest = sha256(summary_path.read_bytes()).hexdigest()
    digest_lines = [line.partition("=")[2].strip() for line in remote.splitlines()
                    if line.startswith("NC0A_AUDIT_SUMMARY_SHA256=")]
    if digest_lines != [expected_digest]:
        raise ExecutionError("GitHub resume anchor does not include the exact prior summary hash")
    validate_remote_audit_anchor(saved, comment)


def _write_manifest_once(run_dir: Path, manifest: dict) -> str:
    path = run_dir / "run_manifest.json"
    payload = (json.dumps(manifest, sort_keys=True, indent=2, allow_nan=False) + "\n").encode()
    digest = sha256(payload).hexdigest()
    if path.exists():
        side = run_dir / "run_manifest.json.sha256"
        if (path.is_symlink() or side.is_symlink() or
            path.read_bytes() != payload):
            raise ExecutionError("Existing run manifest differs; refusing to resume")
        if side.read_text().strip().split()[0] != digest:
            raise ExecutionError("Existing run manifest hash mismatch")
        return digest
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "wb") as handle:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())
    side = run_dir / "run_manifest.json.sha256"
    sfd = os.open(side, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(sfd, "w", encoding="ascii") as handle:
        handle.write(digest + "  run_manifest.json\n")
        handle.flush()
        os.fsync(handle.fileno())
    dir_fd = os.open(run_dir, os.O_RDONLY)
    try:
        os.fsync(dir_fd)
    finally:
        os.close(dir_fd)
    return digest


_WORKER_SPEC: tuple | None = None
_WORKER_FIXTURE: tuple | None = None


def _worker_init(n: int, family: str, root: int, edges: tuple,
                 checkpoints: tuple, case_seconds: float,
                 max_proposals: int, test_worker_hold_seconds: float = 0.0) -> None:
    global _WORKER_SPEC, _WORKER_FIXTURE
    _WORKER_SPEC = (n, family, root, checkpoints, case_seconds, max_proposals,
                    test_worker_hold_seconds)
    _WORKER_FIXTURE = (n, family, synthetic_seed(family, n, root=root), edges)


def _chain_worker(chain_index: int, crash_index: int | None = None) -> dict:
    if crash_index == chain_index:
        os._exit(71)  # Integration-test fault injection; formal calls never set it.
    if _WORKER_SPEC is None or _WORKER_FIXTURE is None:
        raise ExecutionError("Worker fixture initializer was not run")
    n, family, root, checkpoints, case_seconds, max_proposals, hold_seconds = _WORKER_SPEC
    fn, ff, fseed, edges = _WORKER_FIXTURE
    if (fn, ff) != (n, family):
        raise ExecutionError("Worker received a mismatched immutable fixture")
    class SharedFixture:
        pass
    fixture = SharedFixture()
    fixture.n, fixture.family, fixture.seed, fixture.edges = n, family, fseed, edges
    fixture.m = len(edges)
    from hashlib import sha256 as _sha
    def fingerprint() -> str:
        payload = f"n={n}|family={family}|seed={fseed}\n" + "\n".join(
            f"{u},{v}" for u, v in edges)
        return _sha(payload.encode("ascii")).hexdigest()
    fixture.fingerprint = fingerprint
    result = synthetic_chain(n, family, chain_index, root=root,
                             checkpoints=checkpoints,
                             max_wall_seconds=case_seconds,
                             max_proposals=max_proposals, fixture=fixture)
    if hold_seconds:
        time.sleep(hold_seconds)  # Signed engineering-test only; never formal.
    return result


def _verify_case_report(path: Path, spec: CaseSpec, report: dict) -> str:
    checksum = Path(str(path) + ".sha256")
    if (path.is_symlink() or checksum.is_symlink() or
        any(parent.is_symlink() for parent in path.parents) or
        not path.is_file() or not checksum.is_file()):
        raise ExecutionError("Case result or checksum is missing/unsafe")
    expected = checksum.read_text(encoding="ascii").split()[0]
    actual = sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise ExecutionError("Case report SHA-256 mismatch")
    if report.get("n") != spec.n or report.get("family") != spec.family:
        raise ExecutionError("Case report identity mismatch")
    chains = report.get("chains")
    if not isinstance(chains, list) or len(chains) != CHAIN_COUNT:
        raise ExecutionError("Cannot resume a case without all eight chains")
    expected_root = ROOT_SEED if spec.formal else ENGINEERING_TEST_SEED_ROOT
    expected_seeds = {synthetic_seed(spec.family, spec.n, kind="chain",
                                      chain_index=i, root=expected_root)
                      for i in range(CHAIN_COUNT)}
    if {c.get("seed") for c in chains} != expected_seeds:
        raise ExecutionError("Completed case has changed/missing chain seeds")
    if set(c.get("chain_index") for c in chains) != set(range(CHAIN_COUNT)):
        raise ExecutionError("Completed case has missing/duplicate chain indices")
    if (report.get("seed_root") != expected_root or
        report.get("fixture_seed") != synthetic_seed(spec.family, spec.n,
                                                       root=expected_root)):
        raise ExecutionError("Completed case has a changed fixture seed")
    fixture_hash = report.get("fixture_sha256")
    if not isinstance(fixture_hash, str) or len(fixture_hash) != 64:
        raise ExecutionError("Completed case lacks a fixture SHA-256")
    for chain in chains:
        if chain.get("fixture_sha256") != fixture_hash or chain.get("fixture_seed") != report["fixture_seed"]:
            raise ExecutionError("Chain fixture identity differs from its case")
        if set(chain.get("checkpoints", {})) != set(map(str, CHECKPOINTS)):
            raise ExecutionError("Completed chain is missing a locked checkpoint")
        if chain.get("mixing_status") != "MIXING-UNRESOLVED":
            raise ExecutionError("A chain may not claim certified mixing")
        for multiplier in CHECKPOINTS:
            snapshot = chain["checkpoints"][str(multiplier)]
            if snapshot.get("attempts") != multiplier * report.get("edge_count", 0):
                raise ExecutionError("Completed chain checkpoint proposal count mismatch")
            if snapshot.get("accepted") != snapshot.get("audited_accepted_swaps"):
                raise ExecutionError("Completed chain contains unaudited accepted swaps")
    oracle = report.get("oracle", {})
    if (oracle.get("attempts") != ORACLE_PROPOSALS or
        oracle.get("seed") != synthetic_seed(spec.family, spec.n, kind="bfs-identity",
                                               root=expected_root) or
        oracle.get("fixture_sha256") != fixture_hash or
        oracle.get("oracle_mismatches") != 0):
        raise ExecutionError("Completed case lacks its fixed 1,000-proposal oracle")
    if report.get("mixing_status") != "MIXING-UNRESOLVED":
        raise ExecutionError("Formal screening may never be reported as convergence")
    recalculated = screen_case(chains, require_full_contract=spec.formal)
    if recalculated != report.get("screen"):
        raise ExecutionError("Stored statistical screen does not reproduce from chain data")
    if report.get("screen", {}).get("mixing_status") != "MIXING-UNRESOLVED":
        raise ExecutionError("A result may not claim a mixing certificate")
    return actual


def _read_execution_records(path: Path) -> list[dict]:
    if not path.exists():
        return []
    # HashChainLog initialization already validates the whole file. Keep the
    # event payloads for report-hash anchoring during deterministic recovery.
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def _execute_case_attempt(spec: CaseSpec, attempt_dir: Path, *, workers: int,
                          case_seconds: float, oracle_seconds: float,
                          formal: bool, crash_index: int | None = None,
                          crash_after_start: bool = False,
                          phase_callback=None,
                          test_worker_hold_seconds: float = 0.0,
                          process_role_registry: ProcessRoleRegistry | None = None,
                          head: str | None = None) -> dict:
    """Run one immutable task attempt. Toy specs exist only for engineering tests."""
    if formal != spec.formal:
        raise ExecutionError("Formal/test mode and case identity disagree")
    if formal and spec not in formal_cases():
        raise ExecutionError("Non-preregistered case supplied to formal dispatcher")
    if not formal and (spec.n >= min(FORMAL_N) or spec.family not in FAMILIES):
        raise ExecutionError("Test dispatcher is limited to sub-formal synthetic graph sizes")
    if workers < 1 or workers > 8:
        raise ExecutionError("Worker count must be 1..8")
    if not (case_seconds > 0 and oracle_seconds > 0):
        raise ExecutionError("Positive case and oracle deadlines required")
    seed_root = ROOT_SEED if formal else ENGINEERING_TEST_SEED_ROOT
    fixture = make_synthetic_graph(spec.n, spec.family, root=seed_root)
    if crash_after_start:
        raise RuntimeError("Injected parent-runner failure")
    max_proposals = 32 * fixture.m
    context = multiprocessing.get_context("spawn")
    chains: list[dict] = []
    child_before = resource.getrusage(resource.RUSAGE_CHILDREN)
    try:
        with ProcessPoolExecutor(
            max_workers=workers, mp_context=context,
            initializer=_worker_init,
            initargs=(spec.n, spec.family, seed_root, fixture.edges,
                      CHECKPOINTS, case_seconds, max_proposals,
                      test_worker_hold_seconds),
        ) as pool:
            futures = {}
            for i in range(CHAIN_COUNT):
                futures[pool.submit(_chain_worker, i, crash_index)] = i
                if process_role_registry is not None:
                    process_role_registry.sync_pool(pool)
            for future in as_completed(futures):
                chains.append(future.result())
                if process_role_registry is not None:
                    process_role_registry.sync_pool(pool)
    except BaseException:
        # ProcessPoolExecutor.shutdown waits for workers. On abnormal worker
        # death, terminate the executor's remaining workers promptly; the
        # outer watchdog remains the final process-group kill authority.
        raise
    finally:
        if process_role_registry is not None:
            process_role_registry.clear_pool()
    child_after = resource.getrusage(resource.RUSAGE_CHILDREN)
    worker_cpu_seconds = ((child_after.ru_utime + child_after.ru_stime) -
                          (child_before.ru_utime + child_before.ru_stime))
    chains.sort(key=lambda c: c["chain_index"])
    screen = screen_case(chains, require_full_contract=formal)
    if phase_callback is not None:
        phase_callback("oracle")
    oracle = oracle_trace(spec.n, spec.family,
                          root=seed_root, attempts=ORACLE_PROPOSALS,
                          max_wall_seconds=oracle_seconds,
                          max_proposals=ORACLE_PROPOSALS)
    return {
        "format": "NC0A_CASE_RESULT_V1",
        "n": spec.n, "family": spec.family,
        "formal_contract": formal,
        "seed_root": seed_root,
        "fixture_seed": fixture.seed,
        "fixture_sha256": fixture.fingerprint(),
        "edge_count": fixture.m,
        "worker_process_cpu_seconds": worker_cpu_seconds,
        "chain_seeds": [c["seed"] for c in chains],
        "bfs_seed": oracle["seed"],
        "chains": chains,
        "screen": screen,
        "oracle": oracle,
        "execution_environment": _execution_environment(head or _git_head()),
        "mixing_status": "MIXING-UNRESOLVED",
    }


def run_case_attempt(spec: CaseSpec, attempt_dir: Path, *, workers: int,
                     case_seconds: float, oracle_seconds: float,
                     formal: bool = False, **test_faults) -> dict:
    """Public microtest route only; formal cases require the signed launcher."""
    if formal or spec.formal:
        raise ExecutionError("Formal case execution is available only through the signed launcher")
    if spec.n >= min(FORMAL_N) or workers > 4:
        raise ExecutionError("Public case microtests are capped below sub-formal graph and worker scale")
    return _execute_case_attempt(spec, attempt_dir, workers=workers,
                                 case_seconds=case_seconds,
                                 oracle_seconds=oracle_seconds, formal=False,
                                 **test_faults)


def _new_manifest(run_dir: Path, *, head: str, policy_hash: str,
                  protocol: dict, formal: bool) -> dict:
    return {
        "format": "NC0A_RUN_MANIFEST_V1",
        "formal_contract": formal,
        "repository_head": head,
        "resource_policy_sha256": policy_hash,
        "protocol": protocol,
        "watchdog_contract": WATCHDOG_CONTRACT,
        "environment": _execution_environment(head),
        "seed_manifest": {
            spec.key: {
                "fixture_seed": synthetic_seed(spec.family, spec.n, root=ROOT_SEED),
                "chain_seeds": [synthetic_seed(spec.family, spec.n, kind="chain",
                                                chain_index=i, root=ROOT_SEED)
                                for i in range(CHAIN_COUNT)],
                "bfs_seed": synthetic_seed(spec.family, spec.n,
                                           kind="bfs-identity", root=ROOT_SEED),
            } for spec in (formal_cases() if formal else ())
        },
    }


def _run_battery_core(run_dir: str | Path, *, cases: Iterable[CaseSpec], workers: int,
                      case_seconds: float, oracle_seconds: float,
                      max_attempts_per_case: int = 1,
                      formal: bool, policy_hash: str = "TEST_ONLY",
                      head: str = "TEST_ONLY",
                      crash_index: int | None = None,
                      crash_after_start: bool = False,
                      crash_after_start_case: str | None = None,
                      test_worker_hold_seconds: float = 0.0,
                      process_role_registry: ProcessRoleRegistry | None = None) -> dict:
    """Fixed-order task recovery; completed SHA-verified cases are never replaced."""
    root = Path(run_dir).resolve()
    if root == REPOSITORY_ROOT or REPOSITORY_ROOT in root.parents:
        raise ExecutionError("Private run directory must be outside the repository checkout")
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    root.chmod(0o700)
    ordered = tuple(cases)
    if formal and ordered != formal_cases():
        raise ExecutionError("Formal run must use all 16 locked cases in order")
    if not ordered or len({c.key for c in ordered}) != len(ordered):
        raise ExecutionError("Empty or duplicate case schedule")
    if not 1 <= max_attempts_per_case <= 2:
        raise ExecutionError("At most two approved operational attempts are supported")
    manifest = _new_manifest(root, head=head, policy_hash=policy_hash,
                             protocol=PROTOCOL if formal else {
                                 "test_case_keys": [c.key for c in ordered],
                                 "root_seed": ENGINEERING_TEST_SEED_ROOT,
                                 "recovery": PROTOCOL["recovery"]}, formal=formal)
    manifest_sha = _write_manifest_once(root, manifest)
    events = HashChainLog(root / "execution.jsonl")
    prior_events = _read_execution_records(root / "execution.jsonl")
    active_file = root / "active_task.json"
    if active_file.exists():
        if active_file.is_symlink():
            events.close()
            raise ExecutionError("Active-task marker cannot be a symlink")
        try:
            prior_active = _read_json(active_file)
        except ExecutionError:
            events.close()
            raise
        events.append({"event": "prior_attempt_interrupted_at_restart",
                       "active_task": prior_active,
                       "utc": datetime.now(timezone.utc).isoformat()})
        active_file.unlink()
    reports = []
    try:
        for spec in ordered:
            case_dir = root / "cases" / spec.key
            if case_dir.is_symlink():
                raise ExecutionError("Case directory cannot be a symlink")
            case_dir.mkdir(parents=True, exist_ok=True)
            # Completion requires both a valid immutable report and its durable
            # completion-event hash anchor; an unanchored file is quarantined.
            valid = []
            quarantined = []
            for result_path in sorted(case_dir.glob("attempt-*/result.json")):
                try:
                    report = json.loads(result_path.read_text(encoding="utf-8"))
                    digest = _verify_case_report(result_path, spec, report)
                except (ValueError, OSError, ExecutionError) as exc:
                    raise ExecutionError(f"Invalid existing case result {result_path}: {exc}") from exc
                attempt_num = int(result_path.parent.name.split("-")[-1])
                if report.get("attempt") != attempt_num:
                    raise ExecutionError("Result attempt number differs from its immutable path")
                if report.get("run_manifest_sha256") != manifest_sha:
                    raise ExecutionError("Existing result belongs to a different run manifest")
                anchored = any(
                    row.get("event", {}).get("event") == "case_attempt_completed" and
                    row.get("event", {}).get("case") == spec.key and
                    row.get("event", {}).get("attempt") == attempt_num and
                    row.get("event", {}).get("report_sha256") == digest
                    for row in prior_events)
                if anchored:
                    valid.append((result_path, report, digest))
                else:
                    quarantined.append((result_path, digest, attempt_num))
            if len(valid) > 1:
                raise ExecutionError("Multiple completed results for one fixed case")
            for result_path, digest, attempt_num in quarantined:
                already_logged = any(
                    row.get("event", {}).get("event") == "unanchored_result_quarantined" and
                    row.get("event", {}).get("case") == spec.key and
                    row.get("event", {}).get("attempt") == attempt_num and
                    row.get("event", {}).get("report_sha256") == digest
                    for row in prior_events)
                if not already_logged:
                    event = {"event": "unanchored_result_quarantined",
                             "case": spec.key, "attempt": attempt_num,
                             "path": str(result_path.relative_to(root)),
                             "report_sha256": digest}
                    events.append(event)
                    prior_events.append({"event": event})
            if valid:
                report = valid[0][1]
                reports.append(report)
                events.append({"event": "verified_completed_case_reused",
                               "case": spec.key, "report_sha256": valid[0][2]})
                prior_events.append({"event": {"event": "verified_completed_case_reused",
                                                 "case": spec.key,
                                                 "report_sha256": valid[0][2]}})
                continue
            attempts = sorted(case_dir.glob("attempt-*"))
            if any(path.is_symlink() or not path.is_dir() for path in attempts):
                raise ExecutionError("Attempt paths must be ordinary directories")
            if len(attempts) >= max_attempts_per_case:
                raise ExecutionError(
                    f"Case {spec.key} has {len(attempts)} failed/interrupted attempt(s); "
                    "approved retry allowance is exhausted")
            attempt_num = len(attempts) + 1
            attempt_dir = case_dir / f"attempt-{attempt_num:02d}"
            attempt_dir.mkdir(mode=0o700)
            task_started = time.time()
            active = {"phase": "case", "task_id": f"{spec.key}/attempt-{attempt_num:02d}",
                      "started_utc_epoch": task_started}
            tmp = active_file.with_suffix(".tmp")
            tmp.write_text(json.dumps(active, sort_keys=True), encoding="utf-8")
            os.replace(tmp, active_file)
            events.append({"event": "case_attempt_started", "case": spec.key,
                           "attempt": attempt_num, "fixed_seeds": manifest["seed_manifest"].get(spec.key),
                           "utc": datetime.now(timezone.utc).isoformat()})
            try:
                def set_phase(phase: str) -> None:
                    active.update({"phase": phase,
                                   "task_id": f"{spec.key}/attempt-{attempt_num:02d}/{phase}",
                                   "started_utc_epoch": time.time()})
                    tmp.write_text(json.dumps(active, sort_keys=True), encoding="utf-8")
                    os.replace(tmp, active_file)

                report = _execute_case_attempt(
                    spec, attempt_dir, workers=workers, case_seconds=case_seconds,
                    oracle_seconds=oracle_seconds, formal=formal,
                    crash_index=crash_index,
                    crash_after_start=(crash_after_start or
                                       spec.key == crash_after_start_case),
                    phase_callback=set_phase,
                    test_worker_hold_seconds=(test_worker_hold_seconds if not formal else 0.0),
                    process_role_registry=process_role_registry,
                    head=head)
                report["attempt"] = attempt_num
                report["run_manifest_sha256"] = manifest_sha
                report["resource_policy_sha256"] = policy_hash
                report["fixed_seeds"] = manifest["seed_manifest"].get(spec.key)
                # Watchdog enforces the oracle cap from this durable phase marker.
                digest = save_report_once(attempt_dir / "result.json", report)
                _verify_case_report(attempt_dir / "result.json", spec, report)
                reports.append(report)
                events.append({"event": "case_attempt_completed", "case": spec.key,
                               "attempt": attempt_num, "report_sha256": digest,
                               "anomaly_screen_pass": report["screen"]["anomaly_screen_pass"],
                               "mixing_status": "MIXING-UNRESOLVED"})
                active_file.unlink(missing_ok=True)
            except BaseException as exc:
                events.append({"event": "case_attempt_failed", "case": spec.key,
                               "attempt": attempt_num, "exception_type": type(exc).__name__,
                               "message": str(exc)[:500],
                               "traceback": traceback.format_exc(limit=8)[-3000:]})
                active_file.unlink(missing_ok=True)
                raise
        final = None
        if formal:
            cases_report = [{"n": r["n"], "family": r["family"],
                             "metrics": r["screen"]["metrics"],
                             "anomaly_screen_pass": r["screen"]["anomaly_screen_pass"]}
                            for r in reports]
            oracles = [{"n": r["n"], "family": r["family"],
                        "attempts": r["oracle"]["attempts"],
                        "oracle_mismatches": r["oracle"]["oracle_mismatches"],
                        "accepted_local_audits": r["oracle"]["accepted_local_audits"],
                        "accepted": r["oracle"]["accepted"]} for r in reports]
            final = validate_full_battery(cases_report, oracles)
        else:
            final = {"status": "TEST_ONLY_NOT_FORMAL_NC0A",
                     "completed_cases": len(reports), "mixing_status": "MIXING-UNRESOLVED"}
        final_path = root / ("formal_battery_summary.json" if formal else "test_battery_summary.json")
        final_sha = save_report_once(final_path, final)
        events.append({"event": "battery_finished", "summary_sha256": final_sha,
                       "formal": formal, "summary": final})
        active_file.unlink(missing_ok=True)
        return final
    finally:
        events.close()


def run_battery(run_dir: str | Path, *, cases: Iterable[CaseSpec], workers: int,
                case_seconds: float, oracle_seconds: float,
                max_attempts_per_case: int = 1, formal: bool = False,
                **test_faults) -> dict:
    """Public test-only battery route; it cannot launch the formal 16-case run."""
    ordered = tuple(cases)
    if formal or any(spec.formal for spec in ordered):
        raise ExecutionError("Formal NC-0a requires a cryptographically approved watchdog launch")
    if (len(ordered) > 2 or any(spec.n >= min(FORMAL_N) or spec.family not in FAMILIES
                                for spec in ordered) or workers > 4):
        raise ExecutionError("Public microtest dispatcher is capped below the formal battery scale")
    return _run_battery_core(run_dir, cases=ordered, workers=workers,
                             case_seconds=case_seconds,
                             oracle_seconds=oracle_seconds,
                             max_attempts_per_case=max_attempts_per_case,
                             formal=False, **test_faults)


def _limits_from_policy(policy: dict) -> WatchdogLimits:
    caps = policy["limits"]
    macos = policy["memory_enforcement_backend"] == "MACOS_SAMPLED_PRESSURE"
    return WatchdogLimits(
        wall_seconds=caps["absolute_wall_seconds"],
        cpu_seconds=caps["aggregate_cpu_seconds"],
        aggregate_rss_bytes=caps["peak_aggregate_ram_bytes"],
        max_workers=caps["max_workers"],
        run_disk_bytes=caps["temporary_disk_allocation_bytes"],
        reserve_free_disk_bytes=caps["reserved_free_disk_bytes"],
        case_seconds=caps["case_timeout_seconds"],
        oracle_seconds=caps["oracle_timeout_seconds"],
        memory_enforcement_backend=policy["memory_enforcement_backend"],
        host_memory_free_percent_stop=policy["host_memory_free_percent_stop"],
        boot_volume_path=policy.get("macos_boot_volume_path") if macos else None,
        boot_reserve_free_disk_bytes=caps.get("boot_reserve_free_disk_bytes") if macos else None,
        minimum_boot_free_disk_bytes=caps.get("minimum_boot_free_disk_bytes") if macos else None,
        swap_volume_path=policy.get("macos_swap_volume_path") if macos else None,
        swap_volume_reserve_free_disk_bytes=caps.get(
            "swap_volume_reserve_free_disk_bytes") if macos else None,
        minimum_swap_volume_free_disk_bytes=caps.get(
            "minimum_swap_volume_free_disk_bytes") if macos else None,
        swap_growth_stop_bytes=caps.get("swap_growth_stop_bytes") if macos else None,
        swap_free_stop_bytes=caps.get("swap_free_stop_bytes") if macos else None,
        minimum_swap_free_bytes=caps.get("minimum_swap_free_bytes") if macos else None,
        require_ac_power=policy.get("require_ac_power", False) if macos else False,
        require_thermal_normal=policy.get("require_thermal_normal", False) if macos else False,
        require_sleep_assertion=policy.get("require_sleep_assertion", False) if macos else False,
    )


def _assert_authority_store_outside_run(policy: dict, root: Path) -> tuple[Path, Path]:
    ledger = Path(policy["authority_ledger_path"]).resolve()
    anchor = Path(policy["authority_anchor_path"]).resolve()
    for path in (ledger, anchor):
        if path == root or path in root.parents or root in path.parents:
            raise ExecutionError("Authority ledger and anchor must be outside the result directory tree")
        if path == REPOSITORY_ROOT or REPOSITORY_ROOT in path.parents:
            raise ExecutionError("Authority ledger and anchor must remain outside the repository")
    if ledger == anchor or ledger.parent == anchor.parent:
        raise ExecutionError("Authority ledger and anchor must use separate directories")
    return ledger, anchor


def _verify_watchdog_ledger_anchors(ledger: AuthorityLedger, experiment_id: str,
                                    root: Path, is_resume: bool) -> None:
    log_path = root / "watchdog.jsonl"
    anchors = ledger.audit_anchors(experiment_id)
    if not is_resume:
        if any(root.iterdir()):
            raise ExecutionError("A new authorization cannot adopt an existing run directory")
        return
    if not anchors or not log_path.is_file():
        raise ExecutionError("Resumed authorization lacks its externally anchored watchdog log")
    verify_hash_chain(log_path)
    rows = [json.loads(line) for line in log_path.read_text(encoding="utf-8").splitlines()]
    recorded = {row.get("record_sha256"): row.get("event", {}).get("event") for row in rows}
    expected_terminals = {"runner_exited", "watchdog_stop"}
    for anchor in anchors:
        if anchor not in recorded or recorded[anchor] not in expected_terminals:
            raise ExecutionError("Watchdog log is truncated or differs from the external authority anchor")
    starts = sum(row.get("event", {}).get("event") == "run_started" for row in rows)
    terminals = sum(recorded.get(anchor) in expected_terminals for anchor in anchors)
    if starts != terminals or starts != len(anchors):
        raise ExecutionError("Watchdog invocation starts and externally anchored terminals do not pair")


def _runner_entry(run_dir: str, policy_path: str, policy_sha: str,
                  approval_path: str, public_key_path: str,
                  max_attempts: int) -> int:
    global _ACTIVE_PROCESS_ROLE_REGISTRY
    token = os.environ.get("NC0A_WATCHDOG_LAUNCH_TOKEN", "")
    parent = os.environ.get("NC0A_WATCHDOG_PARENT_PID", "")
    if not re.fullmatch(r"[0-9a-f]{64}", token) or parent != str(os.getppid()):
        raise ExecutionError("Internal runner must be an authenticated child of the watchdog launcher")
    role_path = Path(os.environ.get("NC0A_PROCESS_ROLE_REGISTRY", ""))
    if role_path.parent.resolve() != Path(run_dir).resolve():
        raise ExecutionError("Process-role registry must be in this invocation's run directory")
    _ACTIVE_PROCESS_ROLE_REGISTRY = ProcessRoleRegistry(role_path, token, os.getpid())
    guard_watchdog_parent(int(parent))
    policy, approval = _verify_approval(Path(policy_path), Path(approval_path),
                                        Path(public_key_path))
    policy_bytes = Path(policy_path).read_bytes()
    if sha256(policy_bytes).hexdigest() != policy_sha:
        raise ExecutionError("Resource policy changed after watchdog authorization")
    if approval["operational_attempts_per_case"] != max_attempts:
        raise ExecutionError("Operational retry allowance changed after launcher approval")
    result = _run_battery_core(
        run_dir, cases=formal_cases(), workers=policy["limits"]["max_workers"],
        case_seconds=policy["limits"]["case_timeout_seconds"],
        oracle_seconds=policy["limits"]["oracle_timeout_seconds"],
        max_attempts_per_case=max_attempts, formal=True,
        policy_hash=policy_sha, head=_git_head(),
        process_role_registry=_ACTIVE_PROCESS_ROLE_REGISTRY)
    print(json.dumps(result, sort_keys=True))
    return 0


def _test_source_hashes() -> dict:
    names = ("nc0a_execution_engine.py", "nc0a_watchdog.py",
             "nc0a_authority_ledger.py", "nc0a_contract_runner.py",
             "synthetic_graphs.py", "connected_swap.py", "test_anomaly_screen.py")
    return {name: sha256((MODULE_DIR / name).read_bytes()).hexdigest()
            for name in names}


def _validate_engineering_test_policy(policy: dict) -> tuple[tuple[CaseSpec, ...], int]:
    if policy.get("purpose") != ENGINEERING_TEST_APPROVAL_PURPOSE:
        raise ExecutionError("Wrong bounded engineering-test policy purpose")
    try:
        import uuid
        if str(uuid.UUID(policy["test_experiment_id"])) != policy["test_experiment_id"]:
            raise ValueError
    except (ValueError, KeyError, TypeError, AttributeError) as exc:
        raise ExecutionError("Test experiment identity must be a canonical UUID") from exc
    rows = policy.get("cases")
    if not isinstance(rows, list) or not 1 <= len(rows) <= 2:
        raise ExecutionError("Engineering tests are limited to one or two toy cases")
    cases = []
    for row in rows:
        if not isinstance(row, dict) or type(row.get("n")) is not int or not 2 <= row["n"] <= 50:
            raise ExecutionError("Engineering test graph size must remain strictly sub-formal")
        family = row.get("family")
        if family not in FAMILIES:
            raise ExecutionError("Unknown synthetic test family")
        cases.append(CaseSpec(row["n"], family, False))
    if len({case.key for case in cases}) != len(cases):
        raise ExecutionError("Engineering test case identities must be unique")
    workers = policy.get("max_workers")
    if type(workers) is not int or not 1 <= workers <= 8:
        raise ExecutionError("Engineering test worker count must be 1..8")
    if policy.get("memory_enforcement_backend") != "SAMPLED_ONLY":
        raise ExecutionError("Test-only authorization cannot claim a production hard-memory backend")
    threshold = policy.get("host_memory_free_percent_stop")
    if type(threshold) is not int or not 1 <= threshold <= 100:
        raise ExecutionError("Engineering test requires an explicit host-pressure stop threshold")
    if type(policy.get("max_invocations")) is not int or policy["max_invocations"] not in (1, 2):
        raise ExecutionError("Engineering test may authorize at most two same-run invocations")
    hold = policy.get("worker_hold_seconds", 0.0)
    if type(hold) not in (int, float) or not 0 <= hold <= 1:
        raise ExecutionError("Test worker hold must be bounded to at most one second")
    fault = policy.get("fault_first_invocation")
    if fault is not None and fault not in ({case.key for case in cases} |
                                           {"worker_crash", "extra_compute_worker"}):
        raise ExecutionError("Test fault injection must name a signed toy case")
    caps = policy.get("limits")
    if not isinstance(caps, dict):
        raise ExecutionError("Missing bounded engineering-test resource caps")
    for name in ("absolute_wall_seconds", "aggregate_cpu_seconds", "peak_aggregate_ram_bytes",
                 "temporary_disk_allocation_bytes", "reserved_free_disk_bytes",
                 "case_timeout_seconds", "oracle_timeout_seconds"):
        if type(caps.get(name)) is not int or caps[name] <= 0:
            raise ExecutionError("Invalid engineering-test resource cap: " + name)
    if caps.get("max_workers", workers) != workers:
        raise ExecutionError("Engineering-test worker caps disagree with the signed schedule")
    if (caps["absolute_wall_seconds"] > 300 or caps["aggregate_cpu_seconds"] > 1800 or
        caps["peak_aggregate_ram_bytes"] > 2 * 1024**3 or
        caps["temporary_disk_allocation_bytes"] > 256 * 1024**2):
        raise ExecutionError("Engineering-test authorization exceeds fixed toy-run bounds")
    if caps["case_timeout_seconds"] > caps["absolute_wall_seconds"] or caps["oracle_timeout_seconds"] > caps["absolute_wall_seconds"]:
        raise ExecutionError("Engineering-test task deadline exceeds its total wall cap")
    for key in ("authority_ledger_path", "authority_anchor_path"):
        if not isinstance(policy.get(key), str) or not Path(policy[key]).is_absolute():
            raise ExecutionError("Engineering-test authority store paths must be absolute")
    if Path(policy["authority_ledger_path"]).parent == Path(policy["authority_anchor_path"]).parent:
        raise ExecutionError("Engineering-test ledger and anchor must be separately located")
    return tuple(cases), workers


def _verify_engineering_test_approval(policy_path: Path, approval_path: Path,
                                      public_key_path: Path, *,
                                      verify_current_environment: bool = True) -> tuple[dict, dict]:
    policy_bytes = policy_path.read_bytes()
    policy = _read_json(policy_path)
    approval = _read_json(approval_path)
    cases, workers = _validate_engineering_test_policy(policy)
    key_bytes = public_key_path.read_bytes()
    trusted = os.environ.get("NC0A_TEST_TRUSTED_PUBKEY_SHA256", "")
    if not trusted or sha256(key_bytes).hexdigest() != trusted:
        raise ExecutionError("No matching test-only trust anchor; formal trust is not accepted here")
    signed = dict(approval)
    encoded = signed.pop("signature_ed25519_base64", None)
    if (approval.get("purpose") != ENGINEERING_TEST_APPROVAL_PURPOSE or
        approval.get("decision") != "APPROVED_FOR_BOUNDED_ENGINEERING_TEST_ONLY"):
        raise ExecutionError("Formal or unsigned authorization cannot enter test-only mode")
    if approval.get("test_experiment_id") != policy.get("test_experiment_id"):
        raise ExecutionError("Test approval identity differs from its policy")
    if approval.get("policy_sha256") != sha256(policy_bytes).hexdigest():
        raise ExecutionError("Test approval does not bind the exact resource policy")
    head = _git_head()
    if approval.get("target_repository_head_sha") != head:
        raise ExecutionError("Test approval is not bound to the current repository HEAD")
    if policy.get("target_repository_head_sha") != head:
        raise ExecutionError("Test resource policy targets a different repository HEAD")
    if (approval.get("cases") != policy["cases"] or
        approval.get("max_workers") != workers or
        approval.get("seed_root") != ENGINEERING_TEST_SEED_ROOT or
        approval.get("recovery_rule") != PROTOCOL["recovery"]):
        raise ExecutionError("Test approval differs from its bounded workload or fixed seeds")
    if approval.get("test_source_sha256") != _test_source_hashes():
        raise ExecutionError("Test approval does not bind the exact execution and watchdog code")
    execution_environment = policy.get("execution_environment")
    if not isinstance(execution_environment, dict):
        raise ExecutionError("Test policy must freeze the pre-launch runtime environment")
    if (approval.get("test_environment_sha256") !=
            sha256(_canonical(execution_environment)).hexdigest()):
        raise ExecutionError("Test approval does not bind its frozen runtime environment")
    if verify_current_environment and execution_environment != _environment(head):
        raise ExecutionError("Test policy runtime environment differs from the launch host")
    if not isinstance(encoded, str):
        raise ExecutionError("Detached test authorization signature is missing")
    try:
        signature = base64.b64decode(encoded, validate=True)
    except ValueError as exc:
        raise ExecutionError("Malformed bounded test signature") from exc
    if not verify_ed25519_signature(public_key_path, _canonical(signed), signature):
        raise ExecutionError("Bounded engineering-test signature did not verify")
    return policy, approval


def _runner_test_entry(run_dir: str, policy_path: str, policy_sha: str,
                       approval_path: str, public_key_path: str,
                       invocation: int) -> int:
    global _ACTIVE_PROCESS_ROLE_REGISTRY, _ACTIVE_EXECUTION_ENVIRONMENT
    token = os.environ.get("NC0A_WATCHDOG_LAUNCH_TOKEN", "")
    parent = os.environ.get("NC0A_WATCHDOG_PARENT_PID", "")
    if not re.fullmatch(r"[0-9a-f]{64}", token) or parent != str(os.getppid()):
        raise ExecutionError("Test runner must be an authenticated child of the watchdog launcher")
    role_path = Path(os.environ.get("NC0A_PROCESS_ROLE_REGISTRY", ""))
    if role_path.parent.resolve() != Path(run_dir).resolve():
        raise ExecutionError("Test process-role registry must be in this invocation's run directory")
    _ACTIVE_PROCESS_ROLE_REGISTRY = ProcessRoleRegistry(role_path, token, os.getpid())
    guard_watchdog_parent(int(parent))
    policy, _ = _verify_engineering_test_approval(
        Path(policy_path), Path(approval_path), Path(public_key_path),
        verify_current_environment=False)
    if sha256(Path(policy_path).read_bytes()).hexdigest() != policy_sha:
        raise ExecutionError("Test resource policy changed after watchdog authorization")
    _ACTIVE_EXECUTION_ENVIRONMENT = policy["execution_environment"]
    cases, workers = _validate_engineering_test_policy(policy)
    root = Path(run_dir)
    fault_case = policy.get("fault_first_invocation") if invocation == 1 else None
    crash_index = 0 if fault_case == "worker_crash" else None
    crash_after_case = fault_case if fault_case in {case.key for case in cases} else None
    extra_worker = None
    if fault_case == "extra_compute_worker":
        extra_worker = multiprocessing.get_context("spawn").Process(target=_test_extra_worker)
        extra_worker.start()
        if _ACTIVE_PROCESS_ROLE_REGISTRY is not None:
            _ACTIVE_PROCESS_ROLE_REGISTRY.register_compute_worker(extra_worker.pid)
        time.sleep(0.25)
    result = _run_battery_core(
        root, cases=cases, workers=workers,
        case_seconds=policy["limits"]["case_timeout_seconds"],
        oracle_seconds=policy["limits"]["oracle_timeout_seconds"],
        max_attempts_per_case=2, formal=False,
        policy_hash=policy_sha, head=policy["target_repository_head_sha"],
        crash_index=crash_index, crash_after_start_case=crash_after_case,
        test_worker_hold_seconds=policy.get("worker_hold_seconds", 0.0),
        process_role_registry=_ACTIVE_PROCESS_ROLE_REGISTRY)
    if extra_worker is not None:
        extra_worker.terminate()
        extra_worker.join(timeout=2)
    print(json.dumps(result, sort_keys=True))
    return 0


def _test_extra_worker() -> None:
    time.sleep(30)


def _prepare_authorized_invocation(policy: dict, approval: dict, run_dir: str | Path,
                                   ledger: AuthorityLedger, approval_path: Path,
                                   policy_sha: str, max_invocations: int) -> tuple[Path, dict]:
    root = Path(run_dir).resolve()
    if root == REPOSITORY_ROOT or REPOSITORY_ROOT in root.parents:
        raise ExecutionError("Private run directory must be outside the repository checkout")
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    root.chmod(0o700)
    _assert_authority_store_outside_run(policy, root)
    begin = ledger.begin(
        experiment_id=policy.get("formal_experiment_id", policy.get("test_experiment_id")),
        run_dir=root, policy_sha256=policy_sha,
        approval_sha256=sha256(approval_path.read_bytes()).hexdigest(),
        wall_budget_seconds=policy["limits"]["absolute_wall_seconds"],
        cpu_budget_seconds=policy["limits"]["aggregate_cpu_seconds"],
        max_invocations=max_invocations,
        pre_start_check=lambda is_resume: _verify_watchdog_ledger_anchors(
            ledger, policy.get("formal_experiment_id", policy.get("test_experiment_id")),
            root, is_resume))
    return root, begin


def launch_formal(policy_path: str | Path, approval_path: str | Path,
                  public_key_path: str | Path, run_dir: str | Path) -> dict:
    """Check external approval then launch the formal runner under watchdog."""
    policy_path, approval_path, public_key_path = map(Path,
        (policy_path, approval_path, public_key_path))
    policy, approval = _verify_approval(policy_path, approval_path, public_key_path)
    policy_sha = sha256(policy_path.read_bytes()).hexdigest()
    limits = _limits_from_policy(policy)
    if policy["memory_enforcement_backend"] == "MACOS_SAMPLED_PRESSURE":
        try:
            validate_macos_sampled_backend(limits)
        except WatchdogError as exc:
            raise ExecutionError(str(exc)) from exc
    elif policy["memory_enforcement_backend"] == "CGROUP_V2_HARD":
        cgroup = validate_hard_memory_backend(
            policy["memory_enforcement_backend"], limits.aggregate_rss_bytes)
        if cgroup is None:
            raise ExecutionError("Formal execution requires verified hard cgroup-v2 memory enforcement")
    else:
        raise ExecutionError("Formal execution requires an approved hard or macOS sampled-pressure backend")
    ledger_path, anchor_path = _assert_authority_store_outside_run(policy, Path(run_dir).resolve())
    with AuthorityLedger(ledger_path, anchor_path) as ledger:
        root, begin = _prepare_authorized_invocation(
            policy, approval, run_dir, ledger, approval_path, policy_sha,
            approval["operational_attempts_per_case"])
        limits = WatchdogLimits(**{**asdict(limits),
                                   "wall_seconds": limits.wall_seconds - begin["wall_seconds"],
                                   "cpu_seconds": limits.cpu_seconds - begin["cpu_seconds"]})
        runner_command = _formal_runner_command(
            root, policy_path, policy_sha, approval_path, public_key_path,
            approval["operational_attempts_per_case"])
        result = _supervise_named(runner_command, root, limits, begin["invocation"])
        ledger.finish(experiment_id=policy["formal_experiment_id"],
                      invocation=begin["invocation"], status=result["status"],
                      usage=result["usage"], audit_sha256=result["audit_sha256"],
                      completed=result["status"] == "completed")
        return {"watchdog": result, "prior_usage": {
                    "wall_seconds": begin["wall_seconds"],
                    "cpu_seconds": begin["cpu_seconds"]},
                "invocation": begin["invocation"],
                "authorization": {"approval_sha256": sha256(approval_path.read_bytes()).hexdigest(),
                                  "policy_sha256": policy_sha,
                                  "reviewer": approval["independent_reviewer"]}}


def _formal_runner_command(root: Path, policy_path: Path, policy_sha: str,
                           approval_path: Path, public_key_path: Path,
                           max_attempts: int) -> list[str]:
    """Production science runner; tests may replace only this executor seam."""
    return [sys.executable, str(Path(__file__).resolve()),
            "--runner-internal", str(root), str(policy_path.resolve()),
            policy_sha, str(approval_path.resolve()), str(public_key_path.resolve()),
            str(max_attempts)]


def launch_test_only(policy_path: str | Path, approval_path: str | Path,
                     public_key_path: str | Path, run_dir: str | Path) -> dict:
    """Signed bounded toy-test mode; its key and policy cannot authorize formal NC-0a."""
    policy_path, approval_path, public_key_path = map(Path,
        (policy_path, approval_path, public_key_path))
    policy, approval = _verify_engineering_test_approval(
        policy_path, approval_path, public_key_path)
    policy_sha = sha256(policy_path.read_bytes()).hexdigest()
    limits = _limits_from_policy(policy)
    if limits.memory_enforcement_backend != "SAMPLED_ONLY":
        raise ExecutionError("Bounded toy tests must label memory as sampled telemetry only")
    ledger_path, anchor_path = _assert_authority_store_outside_run(policy, Path(run_dir).resolve())
    with AuthorityLedger(ledger_path, anchor_path) as ledger:
        root, begin = _prepare_authorized_invocation(
            policy, approval, run_dir, ledger, approval_path, policy_sha,
            policy["max_invocations"])
        limits = WatchdogLimits(**{**asdict(limits),
                                   "wall_seconds": limits.wall_seconds - begin["wall_seconds"],
                                   "cpu_seconds": limits.cpu_seconds - begin["cpu_seconds"]})
        command = [sys.executable, str(Path(__file__).resolve()),
                   "--runner-test-internal", str(root), str(policy_path.resolve()),
                   policy_sha, str(approval_path.resolve()),
                   str(public_key_path.resolve()), str(begin["invocation"])]
        result = _supervise_named(command, root, limits, begin["invocation"])
        ledger.finish(experiment_id=policy["test_experiment_id"],
                      invocation=begin["invocation"], status=result["status"],
                      usage=result["usage"], audit_sha256=result["audit_sha256"],
                      completed=result["status"] == "completed")
        return {"watchdog": result, "prior_usage": {
                    "wall_seconds": begin["wall_seconds"],
                    "cpu_seconds": begin["cpu_seconds"]},
                "invocation": begin["invocation"], "test_only": True,
                "authorization": {"approval_sha256": sha256(approval_path.read_bytes()).hexdigest(),
                                  "policy_sha256": policy_sha,
                                  "identity": policy["test_experiment_id"]}}


def _researcher_runner_command(root: Path, snapshot_path: Path,
                               commitment_sha: str, max_attempts: int) -> list[str]:
    return [sys.executable, str(Path(__file__).resolve()),
            "--researcher-runner-internal", str(root), str(snapshot_path),
            commitment_sha, str(max_attempts)]


def _researcher_terminal_usage(root: Path) -> tuple[int, dict | None]:
    rows, _ = _read_chain_rows(root / "watchdog.jsonl")
    terminals = [row["event"] for row in rows
                 if row.get("event", {}).get("event") in
                 ("runner_exited", "watchdog_stop", "watchdog_exception") and
                 isinstance(row.get("event", {}).get("usage"), dict)]
    starts, terminal_count, _ = _watchdog_invocation_history(root)
    if starts != terminal_count:
        raise ExecutionError("Watchdog run is incomplete; no recoverable terminal resource record")
    return terminal_count, terminals[-1] if terminals else None


def _load_researcher_package(path: str | Path) -> dict:
    package = _read_json(Path(path))
    if package.get("format") != RESEARCHER_PACKAGE_FORMAT:
        raise ExecutionError("Researcher authorization package format is not recognized")
    return package


def researcher_execution_inventory(run_dir: str | Path) -> dict:
    """Read-only inventory for creating a later researcher commitment."""
    _assert_clean_source_tree()
    context = _researcher_context(run_dir)
    return {
        "status": "INVENTORY_ONLY_NOT_AUTHORIZATION",
        "format": RESEARCHER_PACKAGE_FORMAT,
        "context": context,
        "candidate_resource_limits_not_approved": {
            "max_workers": 4,
            "wall_seconds": 72 * 3600,
            "cpu_seconds": 288 * 3600,
            "per_case_seconds": 12 * 3600,
            "oracle_seconds": 30 * 60,
            "sampled_rss_bytes": 4 * 1024**3,
            "swap_growth_bytes": 2 * 1024**3,
            "data_vm_minimum_free_bytes": 40 * 1024**3,
            "data_vm_reserve_bytes": 30 * 1024**3,
            "run_output_cap_bytes": 4 * 1024**3,
        },
        "risk_acknowledgements_required": list(REQUIRED_RISK_ACKNOWLEDGEMENTS),
        "scientific_protocol": context["scientific_protocol"],
        "third_party_signature_or_custodian": "NOT_REQUIRED_BY_THIS_PROSPECTIVE_MODE",
        "external_review_identity_assurance": "NOT_CRYPTOGRAPHICALLY_PROVEN",
    }


def _verify_researcher_remote_records(package: dict, fetcher=None) -> None:
    fetch = fetcher or _fetch_pr_comment
    commitment = package["commitment"]
    precommit = fetch(package["precommit_comment_url"])
    from nc0a_researcher_authorization import validate_remote_precommit
    validate_remote_precommit(package, precommit)
    precommit_time = datetime.fromisoformat(precommit["created_at"].replace("Z", "+00:00"))
    researcher_login = commitment["researcher"]["github_login"]
    for review in commitment["independent_science_reviews"]:
        comment_id = parse_github_comment_url(review["github_comment_url"])
        del comment_id
        comment = fetch(review["github_comment_url"])
        validate_remote_review(review, comment)
        comment_time = datetime.fromisoformat(comment["created_at"].replace("Z", "+00:00"))
        if comment_time > precommit_time:
            raise ExecutionError("Independent review was not publicly recorded before researcher precommit")
        if (review["reviewer_type"] == "HUMAN_REVIEWER" and
                comment.get("user", {}).get("login") == researcher_login):
            raise ExecutionError("A researcher cannot present their own GitHub comment as an independent human review")


def launch_researcher_authorized(package_path: str | Path, run_dir: str | Path,
                                 confirmation: str, *, resume_anchor_url: str | None = None,
                                 comment_fetcher=None, comment_lister=None) -> dict:
    """Formal NC-0a entry under explicit researcher responsibility.

    This does not require third-party signatures or an external custodian. It
    does require the exact public precommit, two current-head public review
    records, the fixed scientific contract, matching local environment and
    resource checks. GitHub comments and local hash chains remain editable by
    sufficiently privileged parties; this is disclosed, not misrepresented.
    """
    package = _load_researcher_package(package_path)
    commitment = package["commitment"]
    expected_confirmation = (
        "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
        commitment.get("experiment_uuid", "INVALID-UUID"))
    if confirmation != expected_confirmation:
        raise ExecutionError("Typed researcher confirmation did not match this experiment UUID")
    _assert_clean_source_tree()
    context = _researcher_context(run_dir)
    try:
        validation = _validate_researcher_package(package, context=context, run_dir=run_dir)
    except ResearcherAuthorizationError as exc:
        raise ExecutionError(str(exc)) from exc
    policy = commitment["resource_policy"]
    environment = commitment["environment"]
    lock_policy = {
        "runtime_dependency_lock_sha256": commitment["repository"]["runtime_lock_sha256"],
        "host_identifier": environment["host_identifier"],
        "limits": {"measured_physical_ram_bytes": environment["physical_ram_bytes"]},
    }
    _verify_runtime_lock(lock_policy)
    _verify_current_remote_pr_head(commitment["repository"]["head_sha"])
    _verify_researcher_remote_records(package, comment_fetcher)
    limits = _researcher_limits(commitment)
    try:
        validate_macos_sampled_backend(limits)
        host_pressure = sample_host_memory_pressure()
    except WatchdogError as exc:
        raise ExecutionError(str(exc)) from exc
    if (not host_pressure or
            host_pressure.get("free_percent", -1) < limits.host_memory_free_percent_stop):
        raise ExecutionError("Current system-wide memory pressure is below the committed launch threshold")

    root = _resolved_non_symlink_path(run_dir)
    if root == REPOSITORY_ROOT or REPOSITORY_ROOT in root.parents:
        raise ExecutionError("Formal run directory must remain outside the repository")
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    root.chmod(0o700)
    auth_path = root / "researcher_authorization.jsonl"
    snapshot_path = root / "researcher_authorization.json"
    package_bytes = (_researcher_canonical_bytes(package) + b"\n")
    commitment_sha = package["commitment_sha256"]
    allowed_before = {"researcher_authorization.jsonl", "researcher_authorization.json",
                      "watchdog.jsonl", "execution.jsonl", "run_manifest.json",
                      "run_manifest.json.sha256", "active_task.json", "cases",
                      "formal_battery_summary.json", "audit-summaries"}
    existing_entries = list(root.iterdir())
    if any(entry.is_symlink() for entry in existing_entries):
        raise ExecutionError("Run-directory entries cannot be symlinks")
    stdout_entries = {entry.name for entry in existing_entries
                      if entry.name.startswith("runner.stdout")}
    unrecognized = sorted(entry.name for entry in existing_entries
                          if entry.name not in allowed_before and
                          entry.name not in stdout_entries)
    if unrecognized:
        raise ExecutionError(
            "Run directory contains unrecognized files; refusing adoption: " +
            ", ".join(unrecognized[:8]))
    prior_finished, _ = _researcher_invocation_history(root)
    verified_stdout = _verify_researcher_stdout_history(root, prior_finished)
    if stdout_entries != verified_stdout:
        raise ExecutionError("Run directory contains unverified Watchdog stdout files")
    _verify_remote_audit_history(
        package, prior_finished, resume_anchor_url,
        comment_lister=comment_lister)
    events = HashChainLog(auth_path)
    try:
        if snapshot_path.exists():
            existing = snapshot_path.read_bytes()
            if existing != package_bytes:
                raise ExecutionError("Run directory is already bound to a different commitment")
        else:
            if any(p.name != auth_path.name for p in root.iterdir()):
                raise ExecutionError("New experiment UUID requires an empty, unique run directory")
            _write_once_bytes(snapshot_path, package_bytes)
            events.append({"event": "researcher_precommit_verified",
                           "experiment_uuid": commitment["experiment_uuid"],
                           "commitment_sha256": commitment_sha,
                           "precommit_comment_url": package["precommit_comment_url"],
                           "verified_head_sha": commitment["repository"]["head_sha"],
                           "utc": datetime.now(timezone.utc).isoformat()})
            events.append({"event": "researcher_confirmation_recorded",
                           "decision": commitment["researcher"]["decision"],
                           "researcher_name": commitment["researcher"]["name"],
                           "risk_acknowledgements": commitment["risk_acknowledgements"],
                           "utc": datetime.now(timezone.utc).isoformat()})

        if (root / "formal_battery_summary.json").exists():
            raise ExecutionError("Formal battery already has a terminal summary; rerun is prohibited")
        finished, _ = _researcher_invocation_history(root)
        watchdog_starts, _, _ = _watchdog_invocation_history(root)
        if sum(bool(item.get("watchdog_started")) for item in finished) != watchdog_starts:
            raise ExecutionError("Authorization and watchdog histories disagree; manual audit required")
        if finished:
            _verify_resume_anchor(root, package, resume_anchor_url or "", comment_fetcher)
        elif resume_anchor_url:
            raise ExecutionError("First invocation must use the precommit only; no resume anchor is valid")

        current_events, _ = _read_chain_rows(auth_path)
        starts = [row["event"] for row in current_events
                  if row.get("event", {}).get("event") == "invocation_started"]
        if len(starts) != len(finished):
            raise ExecutionError("Invocation start/finish records do not pair")
        cumulative_wall = sum(float(item["usage"].get("wall_seconds", 0)) for item in finished)
        cumulative_cpu = sum(float(item["usage"].get("cpu_seconds", 0)) for item in finished)
        first_start = float(starts[0]["started_utc_epoch"]) if starts else time.time()
        elapsed_wall = max(cumulative_wall, time.time() - first_start)
        caps = policy["limits"]
        remaining_wall = caps["wall_seconds"] - elapsed_wall
        remaining_cpu = caps["cpu_seconds"] - cumulative_cpu
        if remaining_wall <= 60 or remaining_cpu <= max(60, caps["max_workers"] * 2):
            raise ExecutionError("Cumulative absolute resource budget is exhausted or within watchdog stop margin")
        if finished and Path(package["commitment"]["resource_policy"][
                "output_directory"]).resolve() != root:
            raise ExecutionError("Resume directory differs from the fixed experiment identity")
        invocation = len(finished) + 1
        limits = WatchdogLimits(**{**asdict(limits),
                                   "wall_seconds": remaining_wall,
                                   "cpu_seconds": remaining_cpu})
        started_epoch = time.time()
        events.append({"event": "invocation_started", "invocation": invocation,
                       "started_utc_epoch": started_epoch,
                       "remaining_wall_seconds": remaining_wall,
                       "remaining_cpu_seconds": remaining_cpu,
                       "experiment_uuid": commitment["experiment_uuid"],
                       "commitment_sha256": commitment_sha,
                       "utc": datetime.now(timezone.utc).isoformat()})
        before_watchdog_starts, _, _ = _watchdog_invocation_history(root)
        runner_command = _researcher_runner_command(
            root, snapshot_path, commitment_sha, caps["max_attempts_per_case"])
        local_cpu_before = resource.getrusage(resource.RUSAGE_SELF)
        call_start = time.monotonic()
        try:
            result = _supervise_named(runner_command, root, limits, invocation)
        except BaseException as exc:
            after_starts, after_terminals, _ = _watchdog_invocation_history(root)
            if after_starts > before_watchdog_starts:
                if after_terminals != after_starts:
                    raise ExecutionError(
                        "Watchdog failed without a paired terminal record; unknown cost blocks resume") from exc
                _, terminal = _researcher_terminal_usage(root)
                usage = terminal["usage"]
                status = "watchdog_exception"
                returncode = None
                watchdog_started = True
                result = {"status": status, "usage": usage,
                          "exception": f"{type(exc).__name__}: {exc}"}
            else:
                local_cpu_after = resource.getrusage(resource.RUSAGE_SELF)
                usage = {
                    "wall_seconds": max(0.0, time.monotonic() - call_start),
                    "cpu_seconds": max(0.0,
                        local_cpu_after.ru_utime + local_cpu_after.ru_stime -
                        local_cpu_before.ru_utime - local_cpu_before.ru_stime),
                    "resource_source": "launcher_only_pre_runner_failure",
                }
                status = "watchdog_setup_failed"
                returncode = None
                watchdog_started = False
                result = {"status": status, "usage": usage,
                          "exception": f"{type(exc).__name__}: {exc}"}
        else:
            after_starts, after_terminals, _ = _watchdog_invocation_history(root)
            watchdog_started = after_starts == before_watchdog_starts + 1
            if not watchdog_started:
                raise ExecutionError("Supervisor returned without creating a new watchdog process group")
            if after_terminals != after_starts:
                raise ExecutionError("Watchdog did not write a paired terminal event")
            usage = result["usage"]
            returncode = result.get("returncode")
            status = result.get("status", "unknown")
        run_integrity = "NOT_COMPLETE"
        if status == "completed" and returncode == 0:
            try:
                result["formal_summary"] = _verify_completed_researcher_battery(
                    root, commitment)
                run_integrity = "VERIFIED_COMPLETE"
            except (ExecutionError, ValueError, OSError, KeyError) as exc:
                status = "COMPLETED_PROCESS_BUT_RESULT_INVALID"
                result["result_integrity_error"] = f"{type(exc).__name__}: {exc}"
        local_cpu_after = resource.getrusage(resource.RUSAGE_SELF)
        launcher_cpu = max(0.0, local_cpu_after.ru_utime + local_cpu_after.ru_stime -
                           local_cpu_before.ru_utime - local_cpu_before.ru_stime)
        usage = dict(usage)
        usage["wall_seconds"] = max(float(usage.get("wall_seconds", 0)),
                                    time.monotonic() - call_start)
        usage["cpu_seconds"] = max(float(usage.get("cpu_seconds", 0)), launcher_cpu)
        events.append({"event": "invocation_finished", "invocation": invocation,
                       "status": status, "returncode": returncode,
                       "watchdog_started": watchdog_started,
                       "run_integrity": run_integrity,
                       "usage": usage,
                       "watchdog_audit_tip_sha256": _watchdog_invocation_history(root)[2],
                       "utc": datetime.now(timezone.utc).isoformat()})
    finally:
        events.close()

    summary_output = _save_researcher_audit_summary(root, package, invocation)
    summary_path = root / "audit-summaries" / f"invocation-{invocation:02d}.json"
    return {
        "watchdog": result,
        "run_integrity": run_integrity,
        "commitment": validation,
        "experiment_uuid": commitment["experiment_uuid"],
        "invocation": invocation,
        "audit_summary_path": str(summary_path),
        "audit_summary_sha256": summary_output["summary_sha256"],
        "github_anchor_body": summary_output["github_anchor_body"],
        "cumulative_wall_seconds": summary_output["summary"]["cumulative_accounted_wall_seconds"],
        "cumulative_cpu_seconds": summary_output["summary"]["cumulative_accounted_cpu_seconds"],
        "third_party_authorization": False,
    }


def _supervise_named(command: list[str], root: Path, limits: WatchdogLimits,
                     invocation: int) -> dict:
    """Monitor the actual run directory and keep stdout unique per invocation."""
    return supervise(command, run_dir=root, limits=limits,
                     audit_name="watchdog.jsonl",
                     stdout_name=f"runner.stdout.{invocation:02d}.log",
                     invocation_id=invocation)


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "--researcher-runner-internal":
        if len(argv) != 5:
            return 2
        try:
            return _researcher_runner_entry(argv[1], argv[2], argv[3], int(argv[4]))
        except BaseException as exc:
            print(f"RESEARCHER_NC0A_RUN_FAILED: {type(exc).__name__}: {exc}", file=sys.stderr)
            return 2
    if argv and argv[0] == "--runner-internal":
        if len(argv) != 7:
            return 2
        try:
            return _runner_entry(argv[1], argv[2], argv[3], argv[4],
                                 argv[5], int(argv[6]))
        except BaseException as exc:
            print(f"FORMAL_NC0A_RUN_FAILED: {type(exc).__name__}: {exc}", file=sys.stderr)
            return 2
    if argv and argv[0] == "--runner-test-internal":
        if len(argv) != 7:
            return 2
        try:
            return _runner_test_entry(argv[1], argv[2], argv[3], argv[4],
                                      argv[5], int(argv[6]))
        except BaseException as exc:
            print(f"NC0A_TEST_RUN_FAILED: {type(exc).__name__}: {exc}", file=sys.stderr)
            return 2
    if argv and argv[0] == "--test-only":
        if len(argv) != 5:
            return 2
        try:
            result = launch_test_only(argv[1], argv[2], argv[3], argv[4])
            print(json.dumps(result, indent=2, sort_keys=True))
            return 0 if result["watchdog"]["status"] == "completed" else 2
        except (ExecutionError, ValueError, OSError, WatchdogError,
                AuthorityLedgerError) as exc:
            print(f"NC0A_ENGINEERING_TEST_FAILED: {exc}", file=sys.stderr)
            return 2
    if argv and argv[0] == "--researcher-inventory":
        if len(argv) != 2:
            return 2
        try:
            print(json.dumps(researcher_execution_inventory(argv[1]), indent=2,
                             sort_keys=True))
            return 0
        except (ExecutionError, ValueError, OSError, WatchdogError) as exc:
            print(f"NC0A_RESEARCHER_INVENTORY_FAILED: {exc}", file=sys.stderr)
            return 2
    if argv and argv[0] == "--researcher-audit-summary":
        if len(argv) != 2:
            return 2
        try:
            root = Path(argv[1]).expanduser().resolve()
            package = _load_researcher_package(root / "researcher_authorization.json")
            summary = _researcher_audit_summary(root, package)
            raw = _researcher_canonical_bytes(summary) + b"\n"
            digest = sha256(raw).hexdigest()
            print(json.dumps({"summary": summary,
                              "summary_sha256": digest,
                              "github_anchor_body": (
                                  "NC0A_AUDIT_SUMMARY_SHA256=" + digest + "\n" +
                                  "NC0A_AUDIT_SUMMARY_JSON_BASE64=" +
                                  base64.b64encode(_researcher_canonical_bytes(summary)).decode("ascii"))},
                             indent=2, sort_keys=True))
            return 0
        except (ExecutionError, ResearcherAuthorizationError, ValueError, OSError,
                WatchdogError) as exc:
            print(f"NC0A_RESEARCHER_AUDIT_SUMMARY_FAILED: {exc}", file=sys.stderr)
            return 2
    if argv and argv[0] == "--researcher-authorized":
        if len(argv) not in (3, 5) or (len(argv) == 5 and argv[3] != "--resume-anchor"):
            print("Usage: nc0a_execution_engine.py --researcher-authorized PACKAGE.json RUN_DIR [--resume-anchor GITHUB_COMMENT_URL]",
                  file=sys.stderr)
            return 2
        try:
            package = _load_researcher_package(argv[1])
            experiment_uuid = package["commitment"]["experiment_uuid"]
            print("FORMAL NC-0a researcher-authorized route: 16 fixed cases, 128 chains, 32E, 16 oracle streams.")
            print("macOS sampled-memory monitoring is not a hard limit. No G0/T1 authorization is implied.")
            expected = (
                "I ACCEPT NC-0a RESEARCHER-AUTHORIZED EXECUTION AND RECORDED RISKS " +
                experiment_uuid)
            print("Type exactly to continue: " + expected)
            typed = input().strip()
            anchor = argv[4] if len(argv) == 5 else None
            result = launch_researcher_authorized(
                argv[1], argv[2], typed, resume_anchor_url=anchor)
            print(json.dumps(result, indent=2, sort_keys=True))
            return (0 if result["watchdog"]["status"] == "completed" and
                    result["run_integrity"] == "VERIFIED_COMPLETE" else 2)
        except (ExecutionError, ResearcherAuthorizationError, ValueError, OSError,
                WatchdogError, AuthorityLedgerError, KeyError) as exc:
            print(f"FORMAL_NC0A_RESEARCHER_GATE_NO_GO: {exc}", file=sys.stderr)
            return 2
    if len(argv) != 4:
        print("Usage: nc0a_execution_engine.py RESOURCE_POLICY APPROVAL_JSON REVIEWER_PUBLIC_KEY RUN_DIR",
              file=sys.stderr)
        return 2
    try:
        result = launch_formal(*argv)
        print(json.dumps(result, indent=2, sort_keys=True))
        if result["watchdog"]["status"] != "completed":
            return 2
        return 0
    except (ExecutionError, ValueError, OSError, WatchdogError,
            AuthorityLedgerError) as exc:
        print(f"FORMAL_NC0A_RESOURCE_NO_GO: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
