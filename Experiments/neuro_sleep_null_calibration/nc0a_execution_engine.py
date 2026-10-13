"""Authorization-gated, resumable NC-0a formal dispatcher.

The only runnable formal entrypoint is the signed-approval launcher at the
bottom of this module. Unit tests use explicitly nonformal 8-chain toy cases;
they cannot emit a formal battery PASS or change the locked production scale.
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
import re
import resource
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
from typing import Iterable

from nc0a_budget_preflight import validate_policy
from nc0a_contract_runner import (
    CHECKPOINTS, CHAIN_COUNT, FORMAL_N, ORACLE_PROPOSALS,
    oracle_trace, save_report_once, screen_case,
    synthetic_chain, validate_full_battery,
)
from nc0a_watchdog import (
    HashChainLog, WatchdogError, WatchdogLimits, guard_watchdog_parent,
    supervise, validate_hard_memory_backend, verify_hash_chain,
)
from nc0a_authority_ledger import AuthorityLedger, AuthorityLedgerError
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
    "implementation": "NC0A_WATCHDOG_V3",
    "poll_seconds": 0.5,
    "wall_clock": "UTC inclusive of sleep; monotonic divergence above 5s stops",
    "cpu_accounting": "process-group ps cumulative TIME plus waited-child rusage and watchdog CPU; 8-worker termination margin",
    "rss_accounting": "sampled process-group RSS is telemetry only; formal memory enforcement requires exact cgroup-v2 memory.max",
    "worker_accounting": "count only identified multiprocessing.spawn compute workers; sample all group members; unknown members stop",
    "disk_accounting": "run-directory bytes stop at 95% cap; free-disk stop at reserve plus 64MiB or 5% margin",
    "task_deadlines": "case/oracle UTC caps with 99% early-stop margin capped at 60s",
    "termination": "dedicated process group; SIGTERM 0.5s then SIGKILL",
    "monitor_loss": "runner-side parent-PID lease kills the entire process group if watchdog disappears",
    "audit": "fsynced append-only hash chain; no overwrite; unique runner stdout per invocation",
}
APPROVAL_PURPOSE = "NC0A_FORMAL_EXECUTION_APPROVAL_V1"
ENGINEERING_TEST_APPROVAL_PURPOSE = "NC0A_BOUNDED_ENGINEERING_TEST_APPROVAL_V1"
MODULE_DIR = Path(__file__).resolve().parent
REPOSITORY_ROOT = MODULE_DIR.parents[1]
PREREGISTRATION = REPOSITORY_ROOT / "Experiments" / "SRT_NEURO_SLEEP_POPULATION_NULL_CALIBRATION_PREREGISTRATION_2026-10-09.md"
RUNTIME_LOCK = MODULE_DIR / "nc0a-runtime-macos-arm64.lock"


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
    return subprocess.run(["git", "rev-parse", "HEAD"], check=True,
                          capture_output=True, text=True,
                          cwd=REPOSITORY_ROOT).stdout.strip()


def _assert_clean_source_tree() -> None:
    result = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all"],
                            check=True, capture_output=True, text=True,
                            cwd=REPOSITORY_ROOT)
    if result.stdout.strip():
        raise ExecutionError("Formal execution requires the approved clean repository tree")


def _sysctl(name: str) -> str:
    result = subprocess.run(["/usr/sbin/sysctl", "-n", name], check=True,
                            capture_output=True, text=True, timeout=5)
    return result.stdout.strip()


def _host_identifier() -> str:
    if sys.platform != "darwin" or platform.machine() != "arm64":
        raise ExecutionError("Formal execution is locked to the reviewed macOS/Apple Silicon host class")
    identity = "|".join((platform.node(), platform.machine(), _sysctl("hw.model")))
    return sha256(identity.encode("utf-8")).hexdigest()


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
        check = subprocess.run([
            "openssl", "pkeyutl", "-verify", "-pubin", "-inkey",
            str(public_key_path), "-rawin", "-in", str(payload), "-sigfile", str(sigfile),
        ], capture_output=True, text=True)
        return check.returncode == 0


def _verify_approval(policy_path: Path, approval_path: Path,
                     public_key_path: Path) -> tuple[dict, dict]:
    """Verify policy schema, exact HEAD/workload and detached Ed25519 approval.

    The trusted public-key fingerprint is injected by the execution host, not
    stored in this PR. An empty/missing trust anchor always blocks formal runs.
    """
    policy_bytes = policy_path.read_bytes()
    approval = _read_json(approval_path)
    public_key = public_key_path.read_bytes()
    expected_fingerprint = os.environ.get("NC0A_TRUSTED_REVIEWER_PUBKEY_SHA256", "")
    actual_fingerprint = sha256(public_key).hexdigest()
    if not expected_fingerprint or actual_fingerprint != expected_fingerprint:
        raise ExecutionError("No matching externally provisioned reviewer trust anchor")
    _assert_clean_source_tree()
    raw_policy = _read_json(policy_path)
    validation_summary = validate_policy(raw_policy)
    _verify_runtime_lock(raw_policy)
    signed = dict(approval)
    signature_encoded = signed.pop("signature_ed25519_base64", None)
    if not isinstance(signature_encoded, str):
        raise ExecutionError("Detached reviewer signature is missing")
    if approval.get("purpose") != APPROVAL_PURPOSE:
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
        "runtime_lock_sha256": sha256(RUNTIME_LOCK.read_bytes()).hexdigest(),
        "preregistration_sha256": sha256(PREREGISTRATION.read_bytes()).hexdigest(),
        "packages": packages,
        "source_sha256": {
            name: sha256((MODULE_DIR / name).read_bytes()).hexdigest()
            for name in ("nc0a_contract_runner.py", "synthetic_graphs.py",
                         "connected_swap.py", "test_anomaly_screen.py",
                         "nc0a_execution_engine.py", "nc0a_watchdog.py",
                         "nc0a_budget_preflight.py", "nc0a_authority_ledger.py")
        },
    }


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
                          test_worker_hold_seconds: float = 0.0) -> dict:
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
            futures = {pool.submit(_chain_worker, i, crash_index): i
                       for i in range(CHAIN_COUNT)}
            for future in as_completed(futures):
                chains.append(future.result())
    except BaseException:
        # ProcessPoolExecutor.shutdown waits for workers. On abnormal worker
        # death, terminate the executor's remaining workers promptly; the
        # outer watchdog remains the final process-group kill authority.
        raise
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
        "execution_environment": _environment(_git_head()),
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
        "environment": _environment(head),
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
                      test_worker_hold_seconds: float = 0.0) -> dict:
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
                    test_worker_hold_seconds=(test_worker_hold_seconds if not formal else 0.0))
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
    token = os.environ.get("NC0A_WATCHDOG_LAUNCH_TOKEN", "")
    parent = os.environ.get("NC0A_WATCHDOG_PARENT_PID", "")
    if not re.fullmatch(r"[0-9a-f]{64}", token) or parent != str(os.getppid()):
        raise ExecutionError("Internal runner must be an authenticated child of the watchdog launcher")
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
        policy_hash=policy_sha, head=_git_head())
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
                                      public_key_path: Path) -> tuple[dict, dict]:
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
    if approval.get("test_environment_sha256") != sha256(_canonical(_environment(head))).hexdigest():
        raise ExecutionError("Test approval does not bind the current runtime environment")
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
    token = os.environ.get("NC0A_WATCHDOG_LAUNCH_TOKEN", "")
    parent = os.environ.get("NC0A_WATCHDOG_PARENT_PID", "")
    if not re.fullmatch(r"[0-9a-f]{64}", token) or parent != str(os.getppid()):
        raise ExecutionError("Test runner must be an authenticated child of the watchdog launcher")
    guard_watchdog_parent(int(parent))
    policy, _ = _verify_engineering_test_approval(
        Path(policy_path), Path(approval_path), Path(public_key_path))
    if sha256(Path(policy_path).read_bytes()).hexdigest() != policy_sha:
        raise ExecutionError("Test resource policy changed after watchdog authorization")
    cases, workers = _validate_engineering_test_policy(policy)
    root = Path(run_dir)
    fault_case = policy.get("fault_first_invocation") if invocation == 1 else None
    crash_index = 0 if fault_case == "worker_crash" else None
    crash_after_case = fault_case if fault_case in {case.key for case in cases} else None
    extra_worker = None
    if fault_case == "extra_compute_worker":
        extra_worker = multiprocessing.get_context("spawn").Process(target=_test_extra_worker)
        extra_worker.start()
        time.sleep(0.25)
    result = _run_battery_core(
        root, cases=cases, workers=workers,
        case_seconds=policy["limits"]["case_timeout_seconds"],
        oracle_seconds=policy["limits"]["oracle_timeout_seconds"],
        max_attempts_per_case=2, formal=False,
        policy_hash=policy_sha, head=_git_head(),
        crash_index=crash_index, crash_after_start_case=crash_after_case,
        test_worker_hold_seconds=policy.get("worker_hold_seconds", 0.0))
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
    cgroup = validate_hard_memory_backend(
        policy["memory_enforcement_backend"], limits.aggregate_rss_bytes)
    if cgroup is None:
        raise ExecutionError("Formal execution requires verified hard cgroup-v2 memory enforcement")
    ledger_path, anchor_path = _assert_authority_store_outside_run(policy, Path(run_dir).resolve())
    with AuthorityLedger(ledger_path, anchor_path) as ledger:
        root, begin = _prepare_authorized_invocation(
            policy, approval, run_dir, ledger, approval_path, policy_sha,
            approval["operational_attempts_per_case"])
        limits = WatchdogLimits(**{**asdict(limits),
                                   "wall_seconds": limits.wall_seconds - begin["wall_seconds"],
                                   "cpu_seconds": limits.cpu_seconds - begin["cpu_seconds"]})
        runner_command = [sys.executable, str(Path(__file__).resolve()),
                          "--runner-internal", str(root), str(policy_path.resolve()),
                          policy_sha, str(approval_path.resolve()),
                          str(public_key_path.resolve()),
                          str(approval["operational_attempts_per_case"])]
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


def _supervise_named(command: list[str], root: Path, limits: WatchdogLimits,
                     invocation: int) -> dict:
    """Monitor the actual run directory and keep stdout unique per invocation."""
    return supervise(command, run_dir=root, limits=limits,
                     audit_name="watchdog.jsonl",
                     stdout_name=f"runner.stdout.{invocation:02d}.log")


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
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
