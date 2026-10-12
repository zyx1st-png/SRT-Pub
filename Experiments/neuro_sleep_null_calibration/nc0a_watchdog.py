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
import os
from pathlib import Path
import re
import resource
import secrets
import shutil
import signal
import subprocess
import sys
import time
from typing import Callable, Iterable


class WatchdogError(RuntimeError):
    pass


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

    def __post_init__(self) -> None:
        for name in ("wall_seconds", "cpu_seconds", "case_seconds",
                     "oracle_seconds", "poll_seconds",
                     "suspend_tolerance_seconds", "terminate_grace_seconds"):
            value = getattr(self, name)
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError(f"{name} must be positive")
        for name in ("aggregate_rss_bytes", "max_workers", "run_disk_bytes",
                     "reserve_free_disk_bytes"):
            value = getattr(self, name)
            if type(value) is not int or value <= 0:
                raise ValueError(f"{name} must be a positive integer")
        if self.max_workers > 8:
            raise ValueError("NC-0a cannot exceed eight workers")


@dataclass(frozen=True)
class ProcessUsage:
    pid: int
    ppid: int
    pgid: int
    rss_bytes: int
    cpu_seconds: float
    state: str = ""


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
        ["/bin/ps", "-axo", "pid=,ppid=,pgid=,rss=,stat=,time="],
        check=True, capture_output=True, text=True, timeout=5)
    result = []
    for row in proc.stdout.splitlines():
        fields = row.split(None, 5)
        if len(fields) != 6:
            continue
        pid, ppid, group, rss_kib = map(int, fields[:4])
        if group == pgid:
            result.append(ProcessUsage(pid, ppid, group, rss_kib * 1024,
                                       parse_ps_time(fields[5]), fields[4]))
    return result


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
              stdout_name: str = "runner.stdout.log") -> dict:
    """Run and monitor a single scientific runner; terminate its whole group.

    ``clock`` returns (UTC epoch seconds, suspend-aware-comparison monotonic
    seconds) and is injectable for bounded tests. Wall accounting uses UTC so
    system sleep is included; any material UTC/monotonic divergence is a stop.
    """
    if not command or any(not isinstance(x, str) for x in command):
        raise ValueError("A nonempty argument-vector command is required")
    root = Path(run_dir).resolve()
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    root.chmod(0o700)
    log = HashChainLog(root / audit_name)
    output_path = root / stdout_name
    if output_path.exists() or output_path.is_symlink():
        log.close()
        raise WatchdogError("Runner output already exists; run IDs cannot be reused")
    try:
        output = output_path.open("xb", buffering=0)
        os.chmod(output_path, 0o600)
        reserve = _prepare_emergency_reserve(root, limits.run_disk_bytes)
    except BaseException as exc:
        try:
            log.append({"event": "watchdog_setup_failed", "type": type(exc).__name__,
                        "message": str(exc)[:500]})
        finally:
            log.close()
        raise
    wall_now = clock or (lambda: (time.time(), time.monotonic()))
    start_utc, start_mono = wall_now()
    monitor_cpu_start = resource.getrusage(resource.RUSAGE_SELF)
    child_cpu_start = resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu_seen: dict[tuple[int, int, int], float] = {}
    peak_rss = 0
    stop_reason: str | None = None
    last_utc, last_mono = start_utc, start_mono
    last_log = start_mono
    proc: subprocess.Popen | None = None
    try:
        child_env = os.environ.copy()
        child_env["NC0A_WATCHDOG_PARENT_PID"] = str(os.getpid())
        child_env["NC0A_WATCHDOG_LAUNCH_TOKEN"] = secrets.token_hex(32)
        proc = subprocess.Popen(command, cwd=root, stdin=subprocess.DEVNULL,
                                stdout=output, stderr=subprocess.STDOUT,
                                start_new_session=True, close_fds=True, env=child_env)
        log.append({"event": "run_started", "utc": datetime.now(timezone.utc).isoformat(),
                    "pid": proc.pid, "pgid": proc.pid, "command": command,
                    "limits": asdict(limits),
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
            elif len(samples) - (1 if any(p.pid == proc.pid for p in samples) else 0) > limits.max_workers:
                stop_reason = stop_reason or "WORKER_CONCURRENCY_LIMIT"
            elif phase == "case" and phase_elapsed is not None and phase_elapsed >= max(0.01, limits.case_seconds - case_margin):
                stop_reason = stop_reason or "CASE_WALL_LIMIT"
            elif phase == "oracle" and phase_elapsed is not None and phase_elapsed >= max(0.01, limits.oracle_seconds - oracle_margin):
                stop_reason = stop_reason or "ORACLE_WALL_LIMIT"
            if proc.poll() is not None:
                # A runner that exits while children remain is a failure, even
                # if its own status is zero; never strand an unmonitored worker.
                remaining_processes = [p for p in samples
                                       if p.pid != proc.pid and not p.state.startswith("Z")]
                if remaining_processes:
                    stop_reason = stop_reason or "ORPHANED_PROCESS_GROUP_AFTER_RUNNER_EXIT"
                elif stop_reason is None:
                    rc = proc.returncode
                    child_cpu = resource.getrusage(resource.RUSAGE_CHILDREN)
                    waited_child_cpu_seconds = ((child_cpu.ru_utime + child_cpu.ru_stime) -
                                                (child_cpu_start.ru_utime + child_cpu_start.ru_stime))
                    aggregate_cpu = max(aggregate_cpu,
                                        max(0.0, waited_child_cpu_seconds) + max(0.0, monitor_cpu_seconds))
                    usage = {"wall_seconds": wall_elapsed, "cpu_seconds": aggregate_cpu,
                             "cpu_accounting": "max_process_group_ps_and_waited_child_rusage_plus_watchdog",
                             "peak_aggregate_rss_bytes": peak_rss,
                             "run_directory_bytes": disk_bytes,
                             "free_disk_bytes": free_bytes,
                             "runner_stdout_sha256": _sha256_file(output_path)}
                    log.append({"event": "runner_exited", "returncode": rc,
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
                               "run_directory_bytes": final_disk,
                               "free_disk_bytes": final_free,
                               "runner_stdout_sha256": _sha256_file(output_path)}
                log.append({"event": "watchdog_stop", "reason": stop_reason,
                            "utc": datetime.now(timezone.utc).isoformat(),
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
                            "task_id": task_id})
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
                        "message": str(exc)[:500],
                        "usage": {"wall_seconds": max(0.0, end_utc - start_utc),
                                  "cpu_seconds": cpu_seconds,
                                  "runner_stdout_sha256": stdout_sha}})
        except Exception:
            pass
        raise
    finally:
        output.close()
        log.close()


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
