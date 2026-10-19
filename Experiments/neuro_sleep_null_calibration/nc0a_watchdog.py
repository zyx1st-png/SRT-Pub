"""External, fail-closed process-group watchdog for NC-0a.

The monitor is a separate process from the scientific runner. It samples the
dedicated process group, includes wall time across system sleep, records an
append-only hash chain, and kills the whole group on a stop condition. It is
not an execution authorization mechanism: the production CLI also requires a
separately signed approval record and trusted reviewer key.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import re
import resource
import secrets
import shutil
import signal
import shlex
import subprocess
import sys
import threading
import time
from typing import Callable, Iterable


class WatchdogError(RuntimeError):
    pass


def guard_watchdog_parent(expected_parent_pid: int, *, poll_seconds: float = 0.25,
                          terminate_grace_seconds: float = 0.5) -> threading.Thread:
    """Kill the scientific process group if its external watchdog disappears.

    This runner-side lease closes the gap where the monitor itself is killed:
    the runner ignores SIGTERM long enough for its guardian thread to terminate
    every process in the dedicated group, then the guardian escalates to
    SIGKILL.  The normal watchdog still owns resource-limit decisions.
    """
    if (type(expected_parent_pid) is not int or expected_parent_pid <= 1 or
            os.getppid() != expected_parent_pid):
        raise WatchdogError("Runner was not started by its expected watchdog parent")
    if (not isinstance(poll_seconds, (int, float)) or poll_seconds <= 0 or
            not isinstance(terminate_grace_seconds, (int, float)) or
            terminate_grace_seconds <= 0):
        raise ValueError("Parent-guard intervals must be positive")
    process_group = os.getpgrp()
    if process_group != os.getpid():
        raise WatchdogError("Runner must be the leader of its dedicated process group")

    # Keep this process alive through the grace period so the guardian can
    # escalate even if worker children also ignore SIGTERM.
    signal.signal(signal.SIGTERM, signal.SIG_IGN)

    def watch_parent() -> None:
        while os.getppid() == expected_parent_pid:
            time.sleep(poll_seconds)
        try:
            os.killpg(process_group, signal.SIGTERM)
        except ProcessLookupError:
            os._exit(70)
        time.sleep(terminate_grace_seconds)
        try:
            os.killpg(process_group, signal.SIGKILL)
        except ProcessLookupError:
            pass
        os._exit(70)

    thread = threading.Thread(target=watch_parent,
                              name="nc0a-watchdog-parent-guard", daemon=True)
    thread.start()
    return thread


def _canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


class HashChainLog:
    """Durable append-only JSONL audit; corruption or partial tails fail closed."""

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if self.path.is_symlink():
            raise WatchdogError("Audit log path cannot be a symlink")
        flags = os.O_WRONLY | os.O_CREAT | os.O_APPEND
        self.fd = os.open(self.path, flags, 0o600)
        try:
            fcntl.flock(self.fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            if os.fstat(self.fd).st_nlink != 1:
                raise WatchdogError("Audit log cannot have hard-link aliases")
            os.chmod(self.path, 0o600)
            self.sequence, self.previous = verify_hash_chain(self.path)
        except BaseException:
            os.close(self.fd)
            raise

    def append(self, event: dict) -> str:
        record = {"sequence": self.sequence, "previous_sha256": self.previous,
                  "event": event}
        digest = hashlib.sha256(_canonical(record)).hexdigest()
        line = _canonical({**record, "record_sha256": digest}) + b"\n"
        view = memoryview(line)
        while view:
            written = os.write(self.fd, view)
            if written <= 0:
                raise WatchdogError("Short write to audit log")
            view = view[written:]
        os.fsync(self.fd)
        self.sequence += 1
        self.previous = digest
        return digest

    def close(self) -> None:
        fcntl.flock(self.fd, fcntl.LOCK_UN)
        os.close(self.fd)


def verify_hash_chain(path: str | Path) -> tuple[int, str]:
    p = Path(path)
    if not p.exists():
        return 0, "0" * 64
    if p.is_symlink():
        raise WatchdogError("Audit log path cannot be a symlink")
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raise WatchdogError("Partial audit-log tail; manual recovery required")
    previous, sequence = "0" * 64, 0
    for line in raw.splitlines():
        try:
            item = json.loads(line)
            digest = item.pop("record_sha256")
        except (ValueError, KeyError, TypeError) as exc:
            raise WatchdogError("Malformed audit log; refusing resume") from exc
        if item.get("sequence") != sequence or item.get("previous_sha256") != previous:
            raise WatchdogError("Audit hash-chain sequence mismatch")
        expected = hashlib.sha256(_canonical(item)).hexdigest()
        if digest != expected:
            raise WatchdogError("Audit hash-chain digest mismatch")
        previous, sequence = digest, sequence + 1
    return sequence, previous


@dataclass(frozen=True)
class WatchdogLimits:
    wall_seconds: float
    cpu_seconds: float
    aggregate_rss_bytes: int
    max_workers: int
    run_disk_bytes: int
    reserve_free_disk_bytes: int
    case_seconds: float
    oracle_seconds: float
    poll_seconds: float = 0.5
    suspend_tolerance_seconds: float = 5.0
    terminate_grace_seconds: float = 0.5
    memory_enforcement_backend: str = "SAMPLED_ONLY"
    host_memory_free_percent_stop: int | None = None
    boot_volume_path: str | None = None
    boot_reserve_free_disk_bytes: int | None = None
    minimum_boot_free_disk_bytes: int | None = None
    swap_volume_path: str | None = None
    swap_volume_reserve_free_disk_bytes: int | None = None
    minimum_swap_volume_free_disk_bytes: int | None = None
    swap_growth_stop_bytes: int | None = None
    swap_free_stop_bytes: int | None = None
    minimum_swap_free_bytes: int | None = None
    require_ac_power: bool = False
    require_thermal_normal: bool = False
    require_sleep_assertion: bool = False

    def __post_init__(self) -> None:
        for name in ("wall_seconds", "cpu_seconds", "case_seconds",
                     "oracle_seconds", "poll_seconds",
                     "suspend_tolerance_seconds", "terminate_grace_seconds"):
            value = getattr(self, name)
            if not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
                raise ValueError(f"{name} must be positive")
        for name in ("aggregate_rss_bytes", "max_workers", "run_disk_bytes",
                     "reserve_free_disk_bytes"):
            value = getattr(self, name)
            if type(value) is not int or value <= 0:
                raise ValueError(f"{name} must be a positive integer")
        if self.max_workers > 8:
            raise ValueError("NC-0a cannot exceed eight workers")
        if self.memory_enforcement_backend not in (
                "SAMPLED_ONLY", "CGROUP_V2_HARD", "MACOS_SAMPLED_PRESSURE"):
            raise ValueError("Unknown memory-enforcement backend")
        if self.host_memory_free_percent_stop is not None and not (
                type(self.host_memory_free_percent_stop) is int and
                1 <= self.host_memory_free_percent_stop <= 100):
            raise ValueError("Host memory stop threshold must be an integer percentage")
        if self.memory_enforcement_backend == "MACOS_SAMPLED_PRESSURE":
            if self.max_workers > 4:
                raise ValueError("macOS sampled-pressure policy is capped at four workers")
            for name in ("boot_reserve_free_disk_bytes", "minimum_boot_free_disk_bytes",
                         "swap_growth_stop_bytes"):
                value = getattr(self, name)
                if type(value) is not int or value <= 0:
                    raise ValueError(f"{name} is required by the macOS resource policy")
            if (self.swap_free_stop_bytes is None) != (self.minimum_swap_free_bytes is None):
                raise ValueError("Legacy free-swap limits must be both present or both absent")
            if self.swap_free_stop_bytes is not None:
                if (type(self.swap_free_stop_bytes) is not int or
                        type(self.minimum_swap_free_bytes) is not int or
                        self.swap_free_stop_bytes <= 0 or self.minimum_swap_free_bytes <= 0 or
                        self.swap_free_stop_bytes >= self.minimum_swap_free_bytes):
                    raise ValueError("Invalid legacy free-swap launch/stop thresholds")
            if self.boot_volume_path != "/System/Volumes/Data":
                raise ValueError("macOS policy must monitor the internal Data/boot volume")
            vm_values = (self.swap_volume_path,
                         self.swap_volume_reserve_free_disk_bytes,
                         self.minimum_swap_volume_free_disk_bytes)
            if any(value is not None for value in vm_values) and any(
                    value is None for value in vm_values):
                raise ValueError("VM-volume path and both disk thresholds must be supplied together")
            if all(value is not None for value in vm_values):
                if (self.swap_volume_path != "/System/Volumes/VM" or
                        type(self.swap_volume_reserve_free_disk_bytes) is not int or
                        type(self.minimum_swap_volume_free_disk_bytes) is not int or
                        self.swap_volume_reserve_free_disk_bytes <= 0 or
                        self.minimum_swap_volume_free_disk_bytes <= 0 or
                        self.swap_volume_reserve_free_disk_bytes >=
                        self.minimum_swap_volume_free_disk_bytes):
                    raise ValueError("Invalid internal VM-volume launch/reserve settings")
            if self.host_memory_free_percent_stop is None:
                raise ValueError("macOS policy requires a host-memory-pressure threshold")
            if not (self.require_ac_power and self.require_thermal_normal and
                    self.require_sleep_assertion):
                raise ValueError("macOS policy must require AC, thermal telemetry, and sleep assertion")


@dataclass(frozen=True)
class ProcessUsage:
    pid: int
    ppid: int
    pgid: int
    rss_bytes: int
    cpu_seconds: float
    state: str = ""
    command: str = ""


_SECONDS_RE = re.compile(r"^(\d{1,2})(?:\.(\d+))?$")


def parse_ps_time(value: str) -> float:
    """Parse Darwin/BSD ps cumulative TIME (including day and fractional forms)."""
    value = value.strip()
    days = 0
    if "-" in value:
        day_text, value = value.split("-", 1)
        if not day_text.isdigit():
            raise WatchdogError(f"Unrecognized ps CPU time: {value!r}")
        days = int(day_text)
    parts = value.split(":")
    if len(parts) == 3:
        hours_text, minutes_text, seconds_text = parts
        if not hours_text.isdigit() or not minutes_text.isdigit():
            raise WatchdogError(f"Unrecognized ps CPU time: {value!r}")
        hours, minutes = int(hours_text), int(minutes_text)
        if minutes >= 60:
            raise WatchdogError(f"Unrecognized ps CPU time: {value!r}")
        seconds_multiplier = hours * 3600 + minutes * 60
    elif len(parts) == 2 and days == 0:
        # Darwin ps commonly prints long durations as unbounded total minutes,
        # e.g. 318:13.09; constraining this field to two digits silently breaks
        # any long-running resource monitor.
        minutes_text, seconds_text = parts
        if not minutes_text.isdigit():
            raise WatchdogError(f"Unrecognized ps CPU time: {value!r}")
        seconds_multiplier = int(minutes_text) * 60
    else:
        raise WatchdogError(f"Unrecognized ps CPU time: {value!r}")
    seconds_match = _SECONDS_RE.fullmatch(seconds_text)
    if not seconds_match:
        raise WatchdogError(f"Unrecognized ps CPU time: {value!r}")
    seconds = int(seconds_match.group(1))
    if seconds >= 60:
        raise WatchdogError(f"Unrecognized ps CPU time: {value!r}")
    fraction = float("0." + seconds_match.group(2)) if seconds_match.group(2) else 0.0
    return days * 86400 + seconds_multiplier + seconds + fraction


def sample_process_group(pgid: int) -> list[ProcessUsage]:
    """Read process-group RSS and cumulative user+system CPU using macOS ps."""
    proc = subprocess.run(
        ["/bin/ps", "-axo", "pid=,ppid=,pgid=,rss=,stat=,time=,command="],
        check=True, capture_output=True, text=True, timeout=5)
    result = []
    for row in proc.stdout.splitlines():
        fields = row.split(None, 6)
        if len(fields) != 7:
            continue
        pid, ppid, group, rss_kib = map(int, fields[:4])
        if group == pgid:
            result.append(ProcessUsage(pid, ppid, group, rss_kib * 1024,
                                       parse_ps_time(fields[5]), fields[4], fields[6]))
    return result


def _known_python_worker(process: ProcessUsage, runner_pid: int) -> bool:
    return (process.ppid == runner_pid and
            "from multiprocessing.spawn import spawn_main; spawn_main(" in process.command and
            "--multiprocessing-fork" in process.command)


def _known_resource_tracker(process: ProcessUsage, runner_pid: int) -> bool:
    return (process.ppid == runner_pid and
            "from multiprocessing.resource_tracker import main;main(" in process.command)


def _known_runner_helper(process: ProcessUsage, runner_pid: int) -> bool:
    if process.ppid != runner_pid:
        return False
    try:
        args = shlex.split(process.command)
    except ValueError:
        return False
    if not args:
        return False
    executable = Path(args[0]).name
    if executable == "git":
        return args[1:] in (["rev-parse", "HEAD"],
                            ["status", "--porcelain", "--untracked-files=all"])
    if executable == "openssl":
        return args[1:3] == ["pkeyutl", "-verify"]
    if executable == "sysctl":
        return args[1:2] == ["-n"]
    return False


def read_process_role_registry(path: Path, launch_token: str,
                               runner_pid: int) -> dict[int, str]:
    """Read the runner's atomic per-invocation PID-role bridge fail-closed."""
    if path.is_symlink():
        raise WatchdogError("Process-role registry cannot be a symlink")
    if not path.exists():
        return {}
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise WatchdogError("Process-role registry is unreadable or malformed") from exc
    if (not isinstance(document, dict) or
        document.get("format") != "NC0A_PROCESS_ROLE_REGISTRY_V1" or
        document.get("launch_token") != launch_token or
        document.get("runner_pid") != runner_pid or
        not isinstance(document.get("roles"), dict)):
        raise WatchdogError("Process-role registry identity does not match this invocation")
    roles: dict[int, str] = {}
    for raw_pid, role in document["roles"].items():
        try:
            pid = int(raw_pid)
        except (TypeError, ValueError) as exc:
            raise WatchdogError("Process-role registry contains an invalid PID") from exc
        if pid <= 1 or role not in {"compute_worker", "resource_tracker", "runner_helper"}:
            raise WatchdogError("Process-role registry contains an invalid role")
        roles[pid] = role
    return roles


def classify_process_group(samples: list[ProcessUsage], runner_pid: int,
                           registered_roles: dict[int, str] | None = None) -> dict:
    """Classify known workers/helpers and leave unresolved titles fail-closed.

    Darwin sometimes replaces a process's command with ``(Python)`` or
    ``(git)``. Those titles are only pending identities: the exact PID must
    appear in the current token-bound runner registry before the resolution
    grace expires. The executable title alone never grants a role.
    """
    registered_roles = registered_roles or {}
    active = [p for p in samples if not p.state.startswith("Z")]
    runners = [p for p in active if p.pid == runner_pid]
    workers = [p for p in active if (
        _known_python_worker(p, runner_pid) or
        (registered_roles.get(p.pid) == "compute_worker" and p.ppid == runner_pid and
         p.pgid == runner_pid))]
    trackers = [p for p in active if (
        _known_resource_tracker(p, runner_pid) or
        (registered_roles.get(p.pid) == "resource_tracker" and p.ppid == runner_pid and
         p.pgid == runner_pid))]
    helpers = [p for p in active if (
        _known_runner_helper(p, runner_pid) or
        (registered_roles.get(p.pid) == "runner_helper" and p.ppid == runner_pid and
         p.pgid == runner_pid))]
    known = {p.pid for p in runners + workers + trackers + helpers}
    pending = [p for p in active if p.pid not in known and p.ppid == runner_pid and
               sys.platform == "darwin" and p.command.strip() in {"(Python)", "(git)"}]
    pending_pids = {p.pid for p in pending}
    unknown = [p for p in active if p.pid not in known and p.pid not in pending_pids]
    return {"runner_pids": [p.pid for p in runners],
            "worker_pids": sorted(p.pid for p in workers),
            "resource_tracker_pids": sorted(p.pid for p in trackers),
            "helper_pids": sorted(p.pid for p in helpers),
            "pending_pids": sorted(p.pid for p in pending),
            "unknown_pids": sorted(p.pid for p in unknown)}


def _unexpected_process_diagnostics(samples: list[ProcessUsage],
                                    unknown_pids: Iterable[int]) -> list[dict]:
    """Record safe identifiers for fail-closed process-group stops.

    Keep arguments out of the audit because process command lines may contain
    sensitive values. The executable basename and process ancestry are enough
    to distinguish a transient helper from an unapproved compute process.
    """
    wanted = set(unknown_pids)
    diagnostics = []
    for process in samples:
        if process.pid not in wanted:
            continue
        try:
            fields = shlex.split(process.command)
        except ValueError:
            fields = []
        executable = Path(fields[0]).name if fields else "unknown"
        diagnostics.append({"pid": process.pid, "ppid": process.ppid,
                            "pgid": process.pgid, "state": process.state,
                            "executable": executable,
                            "command_sha256": hashlib.sha256(
                                process.command.encode("utf-8", errors="replace")
                            ).hexdigest()})
    return diagnostics


def sample_host_memory_pressure() -> dict:
    """Return host pressure telemetry; this is not a per-process memory limit."""
    if sys.platform == "darwin":
        result = subprocess.run(["/usr/bin/memory_pressure", "-Q"],
                                check=True, capture_output=True, text=True, timeout=5)
        match = re.search(r"System-wide memory free percentage:\s*(\d+)%", result.stdout)
        if not match:
            raise WatchdogError("Cannot parse macOS memory_pressure output")
        total_match = re.search(r"The system has\s+(\d+)\s*\(", result.stdout)
        page_match = re.search(r"page size is\s+(\d+)", result.stdout)
        total = int(total_match.group(1)) * (int(page_match.group(1)) if page_match else 1)
        percent = int(match.group(1))
        return {"source": "macOS memory_pressure -Q",
                "free_percent": percent,
                "estimated_available_bytes": total * percent // 100}
    if sys.platform.startswith("linux"):
        values = {}
        for line in Path("/proc/meminfo").read_text().splitlines():
            match = re.match(r"^(MemTotal|MemAvailable):\s+(\d+)\s+kB$", line)
            if match:
                values[match.group(1)] = int(match.group(2)) * 1024
        if set(values) != {"MemTotal", "MemAvailable"}:
            raise WatchdogError("Cannot parse Linux host memory telemetry")
        return {"source": "/proc/meminfo", "free_percent":
                min(100, values["MemAvailable"] * 100 // values["MemTotal"]),
                "estimated_available_bytes": values["MemAvailable"]}
    raise WatchdogError("Host memory-pressure telemetry is unsupported on this platform")


_SWAP_FIELD_RE = re.compile(
    r"\b(total|used|free)\s*=\s*([0-9]+(?:\.[0-9]+)?)\s*([KMGTP])\b", re.I)


def parse_macos_swap_state(output: str) -> dict[str, int]:
    values = {}
    exponents = {"K": 1, "M": 2, "G": 3, "T": 4, "P": 5}
    for label, quantity, unit in _SWAP_FIELD_RE.findall(output):
        values[label.lower() + "_bytes"] = int(
            float(quantity) * 1024 ** exponents[unit.upper()])
    if set(values) != {"total_bytes", "used_bytes", "free_bytes"}:
        raise WatchdogError("Cannot parse complete macOS vm.swapusage state")
    return values


def parse_macos_swap_used_bytes(output: str) -> int:
    return parse_macos_swap_state(output)["used_bytes"]


def sample_macos_native_state() -> dict:
    """Sample current swap-pool telemetry, power and thermal state.

    ``vm.swapusage.free`` is current availability in the configured pool; it
    does not promise future swap capacity. None of these samples is a hard RAM
    cap or an OS-enforced memory limit.
    """
    if sys.platform != "darwin":
        raise WatchdogError("macOS native resource telemetry is unavailable")
    swap = subprocess.run(["/usr/sbin/sysctl", "vm.swapusage"], check=True,
                          capture_output=True, text=True, timeout=5).stdout
    battery = subprocess.run(["/usr/bin/pmset", "-g", "batt"], check=True,
                             capture_output=True, text=True, timeout=5).stdout
    thermal = subprocess.run(["/usr/bin/pmset", "-g", "therm"], check=True,
                             capture_output=True, text=True, timeout=5).stdout
    lowered = thermal.lower()
    warning_levels = []
    for label in ("thermal", "performance"):
        if f"no {label} warning level" in lowered:
            warning_levels.append(0)
            continue
        match = re.search(label + r" warning level\s*[:=]\s*(\d+)\b", lowered)
        if not match:
            raise WatchdogError("macOS thermal/performance status is unparseable")
        warning_levels.append(int(match.group(1)))
    swap_state = parse_macos_swap_state(swap)
    return {"swap_total_bytes": swap_state["total_bytes"],
            "swap_used_bytes": swap_state["used_bytes"],
            "swap_free_bytes": swap_state["free_bytes"],
            "ac_power": "Now drawing from 'AC Power'" in battery,
            "thermal_normal": all(level == 0 for level in warning_levels),
            "thermal_warning_level": warning_levels[0],
            "performance_warning_level": warning_levels[1]}


def validate_macos_sampled_backend(limits: WatchdogLimits) -> dict:
    """Fail-closed preflight for the prospective, explicitly non-hard backend."""
    if limits.memory_enforcement_backend != "MACOS_SAMPLED_PRESSURE":
        raise WatchdogError("Expected the explicitly named macOS sampled-pressure backend")
    if sys.platform != "darwin" or os.uname().machine != "arm64":
        raise WatchdogError("MACOS_SAMPLED_PRESSURE is locked to Apple Silicon macOS")
    state = sample_macos_native_state()
    if (limits.minimum_swap_free_bytes is not None and
            state["swap_free_bytes"] < limits.minimum_swap_free_bytes):
        raise WatchdogError("macOS swap free-space launch minimum is not met")
    if not state["ac_power"]:
        raise WatchdogError("macOS run requires AC power")
    if not state["thermal_normal"]:
        raise WatchdogError("macOS run requires normal thermal/performance status")
    boot_free = shutil.disk_usage(limits.boot_volume_path).free
    if boot_free < limits.minimum_boot_free_disk_bytes:
        raise WatchdogError("Internal boot-volume free space is below the signed launch minimum")
    if boot_free < limits.boot_reserve_free_disk_bytes:
        raise WatchdogError("Internal boot-volume reserve is already breached")
    result = {**state, "boot_volume_free_bytes": boot_free}
    if limits.swap_volume_path is not None:
        swap_volume_free = shutil.disk_usage(limits.swap_volume_path).free
        if swap_volume_free < limits.minimum_swap_volume_free_disk_bytes:
            raise WatchdogError("Internal VM-volume launch free-space minimum is not met")
        if swap_volume_free < limits.swap_volume_reserve_free_disk_bytes:
            raise WatchdogError("Internal VM-volume free-space reserve is already breached")
        result["swap_volume_free_bytes"] = swap_volume_free
    return result


def _start_sleep_assertion(watchdog_pid: int, required: bool) -> subprocess.Popen | None:
    if not required:
        return None
    if sys.platform != "darwin":
        raise WatchdogError("macOS sleep assertion requested on another platform")
    # Tie the assertion to the watchdog process, so a watchdog crash releases
    # it even if the supervised runner's parent guard is still terminating.
    helper = subprocess.Popen(["/usr/bin/caffeinate", "-is", "-w", str(watchdog_pid)],
                              stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL, start_new_session=True,
                              close_fds=True)
    time.sleep(0.05)
    if helper.poll() is not None:
        raise WatchdogError("macOS caffeinate sleep assertion failed to start")
    return helper


def _stop_sleep_assertion(helper: subprocess.Popen | None) -> None:
    if helper is None:
        return
    if helper.poll() is None:
        helper.terminate()
        try:
            helper.wait(timeout=1)
        except subprocess.TimeoutExpired:
            helper.kill()
            helper.wait()


def _memory_backend_label(limits: WatchdogLimits, cgroup_path: Path | None) -> str:
    if cgroup_path is not None:
        return "CGROUP_V2_HARD"
    if limits.memory_enforcement_backend == "MACOS_SAMPLED_PRESSURE":
        return "MACOS_SAMPLED_PRESSURE_NOT_HARD"
    return "SAMPLED_ONLY_NOT_HARD"


def current_cgroup_v2_path() -> Path:
    if not sys.platform.startswith("linux"):
        raise WatchdogError("Hard aggregate memory enforcement requires Linux cgroup v2")
    entries = Path("/proc/self/cgroup").read_text(encoding="ascii").splitlines()
    unified = [row[3:] for row in entries if row.startswith("0::")]
    if len(unified) != 1:
        raise WatchdogError("Process is not in a unified cgroup v2 hierarchy")
    root = Path("/sys/fs/cgroup").resolve()
    path = (root / unified[0].lstrip("/")).resolve()
    if path != root and root not in path.parents:
        raise WatchdogError("Resolved cgroup escaped the unified hierarchy")
    required = ("memory.max", "memory.current", "memory.peak", "memory.events")
    if any(not (path / name).is_file() for name in required):
        raise WatchdogError("Delegated cgroup lacks required memory-controller files")
    return path


def validate_hard_memory_backend(backend: str, memory_cap_bytes: int) -> Path | None:
    if backend == "SAMPLED_ONLY":
        return None
    if backend != "CGROUP_V2_HARD":
        raise WatchdogError("Unknown memory enforcement backend")
    path = current_cgroup_v2_path()
    try:
        configured = int((path / "memory.max").read_text().strip())
    except (ValueError, OSError) as exc:
        raise WatchdogError("Cannot read cgroup v2 memory.max") from exc
    if configured != memory_cap_bytes:
        raise WatchdogError("Current cgroup memory.max differs from signed aggregate cap")
    members = {int(row) for row in (path / "cgroup.procs").read_text().splitlines()
               if row.strip()}
    if members != {os.getpid()}:
        raise WatchdogError("Hard memory cgroup must be an isolated scope containing only its watchdog")
    return path


def _cgroup_memory_snapshot(path: Path) -> dict:
    try:
        current = int((path / "memory.current").read_text().strip())
        peak = int((path / "memory.peak").read_text().strip())
        events = {}
        for line in (path / "memory.events").read_text().splitlines():
            key, value = line.split()
            events[key] = int(value)
    except (OSError, ValueError) as exc:
        raise WatchdogError("Cannot sample hard cgroup-v2 memory accounting") from exc
    return {"current_bytes": current, "peak_bytes": peak, "events": events}


def _directory_bytes(root: Path) -> int:
    total = 0
    for item in root.rglob("*"):
        if item.is_symlink():
            raise WatchdogError("Run directory may not contain symlinks")
        if item.is_file():
            total += item.stat().st_size
    return total


def _prepare_emergency_reserve(root: Path, allocation_cap: int) -> Path:
    """Preallocate a small same-volume reserve so stop records survive ENOSPC."""
    reserve = root / ".watchdog-emergency.reserve"
    if reserve.exists():
        if reserve.is_symlink() or not reserve.is_file():
            raise WatchdogError("Unsafe emergency reserve path")
        return reserve
    size = min(1 << 20, max(4096, allocation_cap // 100))
    fd = os.open(reserve, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        if hasattr(os, "posix_fallocate"):
            try:
                os.posix_fallocate(fd, 0, size)
            except OSError:
                os.ftruncate(fd, 0)
                os.lseek(fd, 0, os.SEEK_SET)
                _write_zeros(fd, size)
        else:
            _write_zeros(fd, size)
        os.fsync(fd)
    finally:
        os.close(fd)
    return reserve


def _write_zeros(fd: int, size: int) -> None:
    chunk = b"\0" * min(size, 65536)
    remaining = size
    while remaining:
        block = chunk[:min(remaining, len(chunk))]
        os.write(fd, block)
        remaining -= len(block)


def _phase(path: Path, now_utc: float,
           invocation_start_utc: float) -> tuple[str | None, float | None, str | None]:
    if not path.exists():
        return None, None, None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        name, started, task_id = (payload["phase"], float(payload["started_utc_epoch"]),
                                  str(payload["task_id"]))
        if name not in ("case", "oracle") or started > now_utc + 1:
            raise ValueError
        if started < invocation_start_utc:
            return None, None, task_id
        return name, now_utc - started, task_id
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise WatchdogError("Malformed active-task heartbeat") from exc


def _terminate_group(proc: subprocess.Popen, grace: float) -> None:
    try:
        os.killpg(proc.pid, signal.SIGTERM)
    except ProcessLookupError:
        return
    deadline = time.monotonic() + grace
    while time.monotonic() < deadline:
        try:
            live = [p for p in sample_process_group(proc.pid)
                    if not p.state.startswith("Z")]
        except (ProcessLookupError, subprocess.SubprocessError, WatchdogError):
            break
        if not live:
            return
        time.sleep(min(0.05, max(0.0, deadline - time.monotonic())))
    try:
        os.killpg(proc.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass


def supervise(command: list[str], *, run_dir: str | Path,
              limits: WatchdogLimits,
              sampler: Callable[[int], list[ProcessUsage]] = sample_process_group,
              sleeper: Callable[[float], None] = time.sleep,
              clock: Callable[[], tuple[float, float]] | None = None,
              audit_name: str = "watchdog.jsonl",
              stdout_name: str = "runner.stdout.log",
              invocation_id: int | None = None) -> dict:
    """Run and monitor a single scientific runner; terminate its whole group.

    ``clock`` returns (UTC epoch seconds, suspend-aware-comparison monotonic
    seconds) and is injectable for bounded tests. Wall accounting uses UTC so
    system sleep is included; any material UTC/monotonic divergence is a stop.
    """
    if not command or any(not isinstance(x, str) for x in command):
        raise ValueError("A nonempty argument-vector command is required")
    if invocation_id is not None and (type(invocation_id) is not int or invocation_id < 1):
        raise ValueError("Watchdog invocation_id must be a positive integer")
    macos_initial = None
    if limits.memory_enforcement_backend == "MACOS_SAMPLED_PRESSURE":
        macos_initial = validate_macos_sampled_backend(limits)
        cgroup_path = None
    else:
        cgroup_path = validate_hard_memory_backend(
            limits.memory_enforcement_backend, limits.aggregate_rss_bytes)
    cgroup_initial = _cgroup_memory_snapshot(cgroup_path) if cgroup_path else None
    root = Path(run_dir).resolve()
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    root.chmod(0o700)
    log = HashChainLog(root / audit_name)
    output_path = root / stdout_name
    reserve: Path | None = None
    if output_path.exists() or output_path.is_symlink():
        log.close()
        raise WatchdogError("Runner output already exists; run IDs cannot be reused")
    try:
        output = output_path.open("xb", buffering=0)
        os.chmod(output_path, 0o600)
        reserve = _prepare_emergency_reserve(root, limits.run_disk_bytes)
    except BaseException as exc:
        try:
            stdout_digest = (_sha256_file(output_path)
                             if output_path.is_file() and not output_path.is_symlink()
                             else None)
            log.append({"event": "watchdog_setup_failed", "type": type(exc).__name__,
                        "message": str(exc)[:500], "invocation": invocation_id,
                        "runner_stdout_sha256": stdout_digest})
        finally:
            log.close()
        raise
    wall_now = clock or (lambda: (time.time(), time.monotonic()))
    start_utc, start_mono = wall_now()
    boot_free = macos_initial["boot_volume_free_bytes"] if macos_initial else None
    boot_free_min = boot_free
    swap_volume_free_min = (macos_initial.get("swap_volume_free_bytes")
                            if macos_initial else None)
    swap_initial = macos_initial["swap_used_bytes"] if macos_initial else None
    swap_peak = swap_initial
    swap_total_initial = macos_initial["swap_total_bytes"] if macos_initial else None
    swap_total_peak = swap_total_initial
    swap_free_initial = macos_initial["swap_free_bytes"] if macos_initial else None
    swap_free_min = macos_initial["swap_free_bytes"] if macos_initial else None
    latest_macos_state = macos_initial
    last_native_sample = start_mono
    sleep_assertion: subprocess.Popen | None = None
    host_pressure_min = 100
    cgroup_peak = cgroup_initial["peak_bytes"] if cgroup_initial else None
    cgroup_events_initial = dict(cgroup_initial["events"]) if cgroup_initial else {}
    monitor_cpu_start = resource.getrusage(resource.RUSAGE_SELF)
    child_cpu_start = resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu_seen: dict[tuple[int, int, int], float] = {}
    peak_rss = 0
    peak_workers = 0
    peak_resource_trackers = 0
    peak_process_members = 0
    stop_reason: str | None = None
    unexpected_processes: list[dict] = []
    pending_process_first_seen: dict[tuple[int, int, int, str], float] = {}
    pending_process_resolution_grace = max(2.0, 4 * limits.poll_seconds)
    last_utc, last_mono = start_utc, start_mono
    last_log = start_mono
    proc: subprocess.Popen | None = None
    role_registry_path: Path | None = None
    try:
        child_env = os.environ.copy()
        child_env["NC0A_WATCHDOG_PARENT_PID"] = str(os.getpid())
        launch_token = secrets.token_hex(32)
        child_env["NC0A_WATCHDOG_LAUNCH_TOKEN"] = launch_token
        role_registry_path = root / f".nc0a-process-roles-{launch_token}.json"
        child_env["NC0A_PROCESS_ROLE_REGISTRY"] = str(role_registry_path)
        proc = subprocess.Popen(command, cwd=root, stdin=subprocess.DEVNULL,
                                stdout=output, stderr=subprocess.STDOUT,
                                start_new_session=True, close_fds=True, env=child_env)
        if limits.memory_enforcement_backend == "MACOS_SAMPLED_PRESSURE":
            sleep_assertion = _start_sleep_assertion(
                os.getpid(), limits.require_sleep_assertion)
        log.append({"event": "run_started", "utc": datetime.now(timezone.utc).isoformat(),
                    "invocation": invocation_id,
                    "pid": proc.pid, "pgid": proc.pid, "command": command,
                    "limits": asdict(limits),
                    "macos_initial_state": macos_initial,
                    "stop_thresholds": {
                        "wall_seconds": max(0.01, limits.wall_seconds -
                                             max(2 * limits.poll_seconds,
                                                 min(60.0, limits.wall_seconds * 0.01))),
                        "cpu_seconds": max(0.01, limits.cpu_seconds -
                                           max(1.0, limits.max_workers *
                                               (limits.poll_seconds + limits.terminate_grace_seconds))),
                        "aggregate_rss_bytes": max(1, int(limits.aggregate_rss_bytes * 0.90)),
                        "run_disk_bytes": max(1, int(limits.run_disk_bytes * 0.95)),
                        "free_disk_bytes": limits.reserve_free_disk_bytes +
                                           max(64 * 1024 * 1024,
                                               int(limits.reserve_free_disk_bytes * 0.05)),
                        "case_seconds": max(0.01, limits.case_seconds -
                                             max(2 * limits.poll_seconds,
                                                 min(60.0, limits.case_seconds * 0.01))),
                        "oracle_seconds": max(0.01, limits.oracle_seconds -
                                               max(2 * limits.poll_seconds,
                                                   min(60.0, limits.oracle_seconds * 0.01))),
                    }})
        while True:
            now_utc, now_mono = wall_now()
            wall_elapsed = now_utc - start_utc
            divergence = (now_utc - last_utc) - (now_mono - last_mono)
            if abs(divergence) > limits.suspend_tolerance_seconds:
                stop_reason = "SUSPEND_OR_CLOCK_ANOMALY"
            last_utc, last_mono = now_utc, now_mono
            samples = sampler(proc.pid)
            if not samples and proc.poll() is None:
                stop_reason = stop_reason or "WATCHDOG_CANNOT_OBSERVE_PROCESS_GROUP"
            try:
                registered_roles = read_process_role_registry(
                    role_registry_path, launch_token, proc.pid)
            except WatchdogError:
                registered_roles = {}
                stop_reason = stop_reason or "PROCESS_ROLE_REGISTRY_INVALID"
            process_classes = classify_process_group(samples, proc.pid, registered_roles)
            pending = [p for p in samples if p.pid in process_classes["pending_pids"]]
            current_pending_keys = {(p.pid, p.ppid, p.pgid, p.command) for p in pending}
            pending_process_first_seen = {
                key: value for key, value in pending_process_first_seen.items()
                if key in current_pending_keys}
            unresolved_expired = []
            for process in pending:
                key = (process.pid, process.ppid, process.pgid, process.command)
                first_seen = pending_process_first_seen.setdefault(key, now_mono)
                if now_mono - first_seen >= pending_process_resolution_grace:
                    unresolved_expired.append(process.pid)
            unresolved_pids = sorted(set(process_classes["unknown_pids"] + unresolved_expired))
            if unresolved_pids:
                unexpected_processes = _unexpected_process_diagnostics(
                    samples, unresolved_pids)
            peak_workers = max(peak_workers, len(process_classes["worker_pids"]))
            peak_resource_trackers = max(
                peak_resource_trackers, len(process_classes["resource_tracker_pids"]))
            peak_process_members = max(peak_process_members, len(samples))
            try:
                host_pressure = sample_host_memory_pressure()
                host_pressure_min = min(host_pressure_min, host_pressure["free_percent"])
            except (OSError, subprocess.SubprocessError, WatchdogError):
                host_pressure = None
                stop_reason = stop_reason or "HOST_MEMORY_PRESSURE_UNAVAILABLE"
            cgroup_snapshot = _cgroup_memory_snapshot(cgroup_path) if cgroup_path else None
            if cgroup_snapshot:
                cgroup_peak = max(cgroup_peak or 0, cgroup_snapshot["peak_bytes"])
                if cgroup_snapshot["current_bytes"] > limits.aggregate_rss_bytes:
                    stop_reason = stop_reason or "CGROUP_MEMORY_CURRENT_EXCEEDS_SIGNED_LIMIT"
                if any(cgroup_snapshot["events"].get(key, 0) > cgroup_events_initial.get(key, 0)
                       for key in ("max", "oom", "oom_kill")):
                    stop_reason = stop_reason or "CGROUP_MEMORY_LIMIT_EVENT"
            if (host_pressure is not None and
                limits.host_memory_free_percent_stop is not None and
                host_pressure["free_percent"] < limits.host_memory_free_percent_stop):
                stop_reason = stop_reason or "HOST_MEMORY_PRESSURE_LIMIT"
            if limits.memory_enforcement_backend == "MACOS_SAMPLED_PRESSURE":
                try:
                    boot_free = shutil.disk_usage(limits.boot_volume_path).free
                    boot_free_min = min(boot_free_min or boot_free, boot_free)
                    if now_mono - last_native_sample >= 2.0:
                        latest_macos_state = sample_macos_native_state()
                        last_native_sample = now_mono
                        swap_peak = max(swap_peak or 0,
                                        latest_macos_state["swap_used_bytes"])
                        swap_total_peak = max(swap_total_peak or 0,
                                              latest_macos_state["swap_total_bytes"])
                        swap_free_min = min(swap_free_min or latest_macos_state[
                            "swap_free_bytes"], latest_macos_state["swap_free_bytes"])
                    if limits.swap_volume_path is not None:
                        swap_volume_free = shutil.disk_usage(limits.swap_volume_path).free
                        swap_volume_free_min = min(
                            swap_volume_free_min or swap_volume_free, swap_volume_free)
                        swap_volume_stop = limits.swap_volume_reserve_free_disk_bytes + max(
                            64 * 1024 * 1024,
                            int(limits.swap_volume_reserve_free_disk_bytes * 0.05))
                        if swap_volume_free <= swap_volume_stop:
                            stop_reason = stop_reason or "VM_VOLUME_FREE_DISK_RESERVE_BREACH"
                    if sleep_assertion is None or sleep_assertion.poll() is not None:
                        stop_reason = stop_reason or "SLEEP_ASSERTION_LOST"
                    if not latest_macos_state["ac_power"]:
                        stop_reason = stop_reason or "AC_POWER_LOST"
                    if not latest_macos_state["thermal_normal"]:
                        stop_reason = stop_reason or "THERMAL_WARNING"
                    if (swap_initial is not None and swap_peak is not None and
                        swap_peak - swap_initial > limits.swap_growth_stop_bytes):
                        stop_reason = stop_reason or "SWAP_GROWTH_LIMIT"
                    if (limits.swap_free_stop_bytes is not None and
                            latest_macos_state["swap_free_bytes"] <= limits.swap_free_stop_bytes):
                        stop_reason = stop_reason or "SWAP_FREE_RESERVE_BREACH"
                    boot_free_stop = limits.boot_reserve_free_disk_bytes + max(
                        64 * 1024 * 1024,
                        int(limits.boot_reserve_free_disk_bytes * 0.05))
                    if boot_free <= boot_free_stop:
                        stop_reason = stop_reason or "BOOT_VOLUME_FREE_DISK_RESERVE_BREACH"
                except (OSError, subprocess.SubprocessError, WatchdogError):
                    stop_reason = stop_reason or "MACOS_NATIVE_RESOURCE_TELEMETRY_UNAVAILABLE"
            current_rss = sum(p.rss_bytes for p in samples)  # conservative: shared pages may count twice
            peak_rss = max(peak_rss, current_rss)
            for p in samples:
                key = (p.pid, p.ppid, p.pgid)
                cpu_seen[key] = max(cpu_seen.get(key, 0.0), p.cpu_seconds)
            monitor_cpu = resource.getrusage(resource.RUSAGE_SELF)
            monitor_cpu_seconds = ((monitor_cpu.ru_utime + monitor_cpu.ru_stime) -
                                   (monitor_cpu_start.ru_utime + monitor_cpu_start.ru_stime))
            child_cpu = resource.getrusage(resource.RUSAGE_CHILDREN)
            waited_child_cpu_seconds = ((child_cpu.ru_utime + child_cpu.ru_stime) -
                                        (child_cpu_start.ru_utime + child_cpu_start.ru_stime))
            aggregate_cpu = max(sum(cpu_seen.values()), max(0.0, waited_child_cpu_seconds)) + max(0.0, monitor_cpu_seconds)
            disk_bytes = _directory_bytes(root)
            free_bytes = shutil.disk_usage(root).free
            phase, phase_elapsed, task_id = _phase(root / "active_task.json", now_utc,
                                                   start_utc)
            # Leave a sampling/termination allowance so the measured cap is not
            # deliberately consumed before the group can be killed.
            cpu_margin = max(1.0, limits.max_workers *
                             (limits.poll_seconds + limits.terminate_grace_seconds))
            cpu_stop = max(0.01, limits.cpu_seconds - cpu_margin)
            wall_margin = max(2 * limits.poll_seconds,
                              min(60.0, limits.wall_seconds * 0.01))
            rss_stop = max(1, int(limits.aggregate_rss_bytes * 0.90))
            disk_stop = max(1, int(limits.run_disk_bytes * 0.95))
            free_stop = limits.reserve_free_disk_bytes + max(
                64 * 1024 * 1024, int(limits.reserve_free_disk_bytes * 0.05))
            case_margin = max(2 * limits.poll_seconds,
                              min(60.0, limits.case_seconds * 0.01))
            oracle_margin = max(2 * limits.poll_seconds,
                                min(60.0, limits.oracle_seconds * 0.01))
            if wall_elapsed >= max(0.01, limits.wall_seconds - wall_margin):
                stop_reason = stop_reason or "WALL_LIMIT"
            elif aggregate_cpu >= cpu_stop:
                stop_reason = stop_reason or "CPU_LIMIT_WITH_TERMINATION_MARGIN"
            elif current_rss >= rss_stop:
                stop_reason = stop_reason or "AGGREGATE_RSS_LIMIT"
            elif disk_bytes >= disk_stop:
                stop_reason = stop_reason or "RUN_DISK_ALLOCATION_LIMIT"
            elif free_bytes <= free_stop:
                stop_reason = stop_reason or "FREE_DISK_RESERVE_BREACH"
            elif unresolved_pids:
                stop_reason = stop_reason or "UNKNOWN_PROCESS_GROUP_MEMBER"
            elif len(process_classes["worker_pids"]) > limits.max_workers:
                stop_reason = stop_reason or "WORKER_CONCURRENCY_LIMIT"
            elif phase == "case" and phase_elapsed is not None and phase_elapsed >= max(0.01, limits.case_seconds - case_margin):
                stop_reason = stop_reason or "CASE_WALL_LIMIT"
            elif phase == "oracle" and phase_elapsed is not None and phase_elapsed >= max(0.01, limits.oracle_seconds - oracle_margin):
                stop_reason = stop_reason or "ORACLE_WALL_LIMIT"
            if proc.poll() is not None:
                # The first sample can race with a fast runner exit and miss a
                # child just forked before exit. Require repeated post-exit
                # observations of an empty process group before success.
                for _ in range(3):
                    try:
                        after_exit = sampler(proc.pid)
                    except (ProcessLookupError, subprocess.SubprocessError, WatchdogError):
                        after_exit = None
                    if after_exit is None:
                        stop_reason = stop_reason or "WATCHDOG_CANNOT_OBSERVE_PROCESS_GROUP"
                        break
                    lingering = [p for p in after_exit
                                 if p.pid != proc.pid and not p.state.startswith("Z")]
                    if lingering:
                        stop_reason = stop_reason or "ORPHANED_PROCESS_GROUP_AFTER_RUNNER_EXIT"
                        break
                    peak_process_members = max(peak_process_members, len(after_exit))
                    sleeper(min(0.05, limits.poll_seconds))
                confirmed_utc, _ = wall_now()
                wall_elapsed = max(wall_elapsed, confirmed_utc - start_utc)
                if stop_reason is None:
                    rc = proc.returncode
                    monitor_cpu = resource.getrusage(resource.RUSAGE_SELF)
                    monitor_cpu_seconds = ((monitor_cpu.ru_utime + monitor_cpu.ru_stime) -
                                           (monitor_cpu_start.ru_utime + monitor_cpu_start.ru_stime))
                    child_cpu = resource.getrusage(resource.RUSAGE_CHILDREN)
                    waited_child_cpu_seconds = ((child_cpu.ru_utime + child_cpu.ru_stime) -
                                                (child_cpu_start.ru_utime + child_cpu_start.ru_stime))
                    aggregate_cpu = max(aggregate_cpu,
                                        max(0.0, waited_child_cpu_seconds) + max(0.0, monitor_cpu_seconds))
                    if wall_elapsed >= max(0.01, limits.wall_seconds - wall_margin):
                        stop_reason = "WALL_LIMIT"
                    elif aggregate_cpu >= cpu_stop:
                        stop_reason = "CPU_LIMIT_WITH_TERMINATION_MARGIN"
                    if stop_reason is not None:
                        # Fall through to the stop record; a completed runner
                        # does not exempt the invocation from its budget cap.
                        pass
                    else:
                        usage = {"wall_seconds": wall_elapsed, "cpu_seconds": aggregate_cpu,
                                 "cpu_accounting": "max_process_group_ps_and_waited_child_rusage_plus_watchdog",
                                 "peak_aggregate_rss_bytes": peak_rss,
                                 "memory_enforcement": _memory_backend_label(limits, cgroup_path),
                                 "host_memory_free_percent_min": host_pressure_min,
                                 "boot_volume_free_bytes_min": boot_free_min,
                                 "swap_used_bytes_initial": swap_initial,
                                 "swap_used_bytes_peak_sampled": swap_peak,
                                 "swap_total_bytes_initial": swap_total_initial,
                                 "swap_total_bytes_peak_sampled": swap_total_peak,
                                 "swap_free_bytes_initial": swap_free_initial,
                                 "swap_free_bytes_min_sampled": swap_free_min,
                                 "vm_volume_free_bytes_min": swap_volume_free_min,
                                 "sleep_assertion": "CAFFEINATE_ACTIVE" if sleep_assertion else "NOT_REQUESTED",
                                 "macos_native_state": latest_macos_state,
                                 "cgroup_memory_peak_bytes": cgroup_peak,
                                 "peak_compute_workers": peak_workers,
                                 "peak_resource_trackers": peak_resource_trackers,
                                 "peak_process_group_members": peak_process_members,
                                 "run_directory_bytes": disk_bytes,
                                 "free_disk_bytes": free_bytes,
                                 "runner_stdout_sha256": _sha256_file(output_path)}
                        log.append({"event": "runner_exited", "returncode": rc,
                                    "invocation": invocation_id,
                                    "usage": usage})
                        return {"status": "completed" if rc == 0 else "failed",
                                "returncode": rc, "usage": usage,
                                "audit_sha256": log.previous}
            if stop_reason:
                # Free the preallocated same-volume reserve before persisting
                # the stop record. The audit remains append-only; the reserve
                # is operational scratch and is released only on a stop.
                reserve.unlink(missing_ok=True)
                log.append({"event": "watchdog_stop_requested", "reason": stop_reason,
                            "utc": datetime.now(timezone.utc).isoformat(),
                            "task_id": task_id, "phase": phase,
                            "unexpected_processes": unexpected_processes,
                            "wall_seconds": wall_elapsed,
                            "sampled_cpu_seconds": aggregate_cpu})
                _terminate_group(proc, limits.terminate_grace_seconds)
                try:
                    proc.wait(timeout=max(1.0, limits.terminate_grace_seconds + 1))
                except subprocess.TimeoutExpired:
                    proc.kill()
                    proc.wait()
                final_utc, _ = wall_now()
                final_samples = sampler(proc.pid)
                for p in final_samples:
                    key = (p.pid, p.ppid, p.pgid)
                    cpu_seen[key] = max(cpu_seen.get(key, 0.0), p.cpu_seconds)
                monitor_cpu = resource.getrusage(resource.RUSAGE_SELF)
                monitor_cpu_seconds = ((monitor_cpu.ru_utime + monitor_cpu.ru_stime) -
                                       (monitor_cpu_start.ru_utime + monitor_cpu_start.ru_stime))
                child_cpu = resource.getrusage(resource.RUSAGE_CHILDREN)
                waited_child_cpu_seconds = ((child_cpu.ru_utime + child_cpu.ru_stime) -
                                            (child_cpu_start.ru_utime + child_cpu_start.ru_stime))
                final_cpu = max(sum(cpu_seen.values()),
                                max(0.0, waited_child_cpu_seconds)) + max(0.0, monitor_cpu_seconds)
                final_wall = max(0.0, final_utc - start_utc)
                final_rss = sum(p.rss_bytes for p in final_samples)
                final_disk = _directory_bytes(root)
                final_free = shutil.disk_usage(root).free
                final_usage = {"wall_seconds": final_wall,
                               "cpu_seconds": final_cpu,
                               "cpu_accounting": "max_process_group_ps_and_waited_child_rusage_plus_watchdog",
                               "aggregate_rss_bytes": final_rss,
                               "peak_aggregate_rss_bytes": max(peak_rss, final_rss),
                               "memory_enforcement": _memory_backend_label(limits, cgroup_path),
                               "host_memory_free_percent_min": host_pressure_min,
                               "boot_volume_free_bytes_min": boot_free_min,
                               "swap_used_bytes_initial": swap_initial,
                               "swap_used_bytes_peak_sampled": swap_peak,
                               "swap_total_bytes_initial": swap_total_initial,
                               "swap_total_bytes_peak_sampled": swap_total_peak,
                               "swap_free_bytes_initial": swap_free_initial,
                               "swap_free_bytes_min_sampled": swap_free_min,
                               "vm_volume_free_bytes_min": swap_volume_free_min,
                               "sleep_assertion": "CAFFEINATE_ACTIVE" if sleep_assertion else "NOT_REQUESTED",
                               "macos_native_state": latest_macos_state,
                               "cgroup_memory_peak_bytes": cgroup_peak,
                               "peak_compute_workers": peak_workers,
                               "peak_resource_trackers": peak_resource_trackers,
                               "peak_process_group_members": peak_process_members,
                               "unexpected_processes": unexpected_processes,
                               "run_directory_bytes": final_disk,
                               "free_disk_bytes": final_free,
                               "runner_stdout_sha256": _sha256_file(output_path)}
                log.append({"event": "watchdog_stop", "reason": stop_reason,
                            "utc": datetime.now(timezone.utc).isoformat(),
                            "invocation": invocation_id,
                            "task_id": task_id, "phase": phase,
                            "usage": final_usage})
                return {"status": "stopped", "reason": stop_reason,
                        "returncode": proc.returncode,
                        "usage": final_usage,
                        "audit_sha256": log.previous}
            if now_mono - last_log >= min(5.0, limits.poll_seconds * 10):
                log.append({"event": "resource_sample", "utc": datetime.now(timezone.utc).isoformat(),
                            "usage": {"wall_seconds": wall_elapsed,
                                      "cpu_seconds": aggregate_cpu,
                                      "aggregate_rss_bytes": current_rss,
                                      "peak_aggregate_rss_bytes": peak_rss,
                                      "run_directory_bytes": disk_bytes,
                                      "free_disk_bytes": free_bytes},
                            "process_count": len(samples), "phase": phase,
                            "task_id": task_id,
                            "process_classes": process_classes,
                            "host_memory_pressure": host_pressure,
                            "macos_native_state": latest_macos_state,
                            "boot_volume_free_bytes": boot_free,
                            "cgroup_memory": cgroup_snapshot})
                last_log = now_mono
            sleeper(limits.poll_seconds)
    except BaseException as exc:
        if proc is not None and proc.poll() is None:
            _terminate_group(proc, limits.terminate_grace_seconds)
            proc.wait()
        try:
            reserve.unlink(missing_ok=True)
            end_utc, _ = wall_now()
            try:
                samples = sampler(proc.pid) if proc is not None else []
            except Exception:
                samples = []
            for p in samples:
                key = (p.pid, p.ppid, p.pgid)
                cpu_seen[key] = max(cpu_seen.get(key, 0.0), p.cpu_seconds)
            monitor_cpu = resource.getrusage(resource.RUSAGE_SELF)
            child_cpu = resource.getrusage(resource.RUSAGE_CHILDREN)
            monitor_cpu_seconds = ((monitor_cpu.ru_utime + monitor_cpu.ru_stime) -
                                   (monitor_cpu_start.ru_utime + monitor_cpu_start.ru_stime))
            waited_child_cpu_seconds = ((child_cpu.ru_utime + child_cpu.ru_stime) -
                                        (child_cpu_start.ru_utime + child_cpu_start.ru_stime))
            cpu_seconds = max(sum(cpu_seen.values()), max(0.0, waited_child_cpu_seconds)) + max(0.0, monitor_cpu_seconds)
            try:
                stdout_sha = _sha256_file(output_path)
            except OSError:
                stdout_sha = None
            log.append({"event": "watchdog_exception", "type": type(exc).__name__,
                        "invocation": invocation_id,
                        "message": str(exc)[:500],
                            "usage": {"wall_seconds": max(0.0, end_utc - start_utc),
                                      "cpu_seconds": cpu_seconds,
                                      "memory_enforcement": _memory_backend_label(limits, cgroup_path),
                                      "boot_volume_free_bytes_min": boot_free_min,
                                      "swap_used_bytes_initial": swap_initial,
                                      "swap_used_bytes_peak_sampled": swap_peak,
                                      "swap_free_bytes_min_sampled": swap_free_min,
                                      "host_memory_free_percent_min": host_pressure_min,
                                      "cgroup_memory_peak_bytes": cgroup_peak,
                                      "peak_compute_workers": peak_workers,
                                      "peak_resource_trackers": peak_resource_trackers,
                                      "peak_process_group_members": peak_process_members,
                                 "runner_stdout_sha256": stdout_sha}})
        except Exception:
            pass
        raise
    finally:
        _stop_sleep_assertion(sleep_assertion)
        cleanup_error = None
        if reserve is not None:
            try:
                reserve.unlink(missing_ok=True)
            except OSError as exc:
                cleanup_error = ("Cannot remove the invocation's emergency reserve", exc)
        if role_registry_path is not None:
            try:
                role_registry_path.unlink(missing_ok=True)
            except OSError as exc:
                if cleanup_error is None:
                    cleanup_error = (
                        "Cannot remove the invocation's process-role registry", exc)
        output.close()
        log.close()
        if cleanup_error is not None:
            message, cause = cleanup_error
            raise WatchdogError(message) from cause


def main(argv: list[str] | None = None) -> int:
    # Deliberately no generic shell command interface here. The production
    # authorization wrapper is added in nc0a_execution_engine.py.
    if argv is None:
        argv = sys.argv[1:]
    print("Watchdog library only; use the authorization-gated NC-0a launcher.",
          file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
