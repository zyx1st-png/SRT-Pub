"""Cumulative, conservative accounting for the single observed-only remedy.

Only the external controller may construct ControllerMeter. It launches a ps
identity query; the scientific child must never do so. The ps birth timestamp
is rounded down to a second, conservatively charging less than one extra second
of startup wall time. Full-lifetime self/waited CPU includes imports and helper
commands. Running-group CPU is sampled and may overlap a child being reaped;
the high-water charge deliberately retains that possible overcount.

The final closing reserve is a charge, not an observed duration. It covers the
last audit writes/fsyncs after the final snapshot without pretending a record
can contain the cost of writing itself. Missing or over-budget closure must
never be represented as a completed activity. These are sampled stopping and
accounting rules, not operating-system hard CPU or memory limits.
"""
from __future__ import annotations

import json
import math
import os
import re
import resource
import subprocess
import time
from datetime import UTC, datetime
from pathlib import Path

from nc0a_watchdog import sample_process_group

TOTAL_WALL_SECONDS = 14_400.0
TOTAL_CPU_SECONDS = 14_400.0
TOTAL_OUTPUT_BYTES = 1 << 30
CLOSING_WALL_SECONDS = 5.0
CLOSING_CPU_SECONDS = 40.0  # Five seconds on the frozen eight-logical-CPU host.
CLOSING_OUTPUT_BYTES = 64 << 10
GUARD_WALL_SECONDS = 1.0  # poll 0.5 s + termination grace 0.5 s.
GUARD_CPU_SECONDS = 8.0  # Eight native threads may run in one compute worker.
_LEASE = "h3-active-lease.json"


class RemediationBudgetError(RuntimeError):
    """Unknown, inconsistent or exhausted cumulative resources: fail closed."""


def _number(value, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise RemediationBudgetError(f"{label} must be finite and nonnegative")
    try:
        number = float(value)
    except OverflowError as exc:
        raise RemediationBudgetError(f"{label} is outside finite telemetry range") from exc
    if not math.isfinite(number) or number < 0:
        raise RemediationBudgetError(f"{label} must be finite and nonnegative")
    return number


def _bytes(value, label: str) -> int:
    if type(value) is not int or value < 0:
        raise RemediationBudgetError(f"{label} must be a nonnegative integer")
    return value


def _prior(prior: dict) -> tuple[float, float, int, int]:
    try:
        return (_number(prior["old_wall_charge_seconds"], "Old wall charge"),
                _number(prior["old_cpu_upper_charge_seconds"], "Old CPU charge"),
                _bytes(prior["old_output_bytes"], "Old output"),
                _bytes(prior.get("old_auxiliary_output_bytes", 0), "Old auxiliary output"))
    except (KeyError, TypeError) as exc:
        raise RemediationBudgetError("Missing old resource charges") from exc


def _snapshot(snapshot: dict) -> tuple[float, float]:
    try:
        wall = _number(snapshot["wall_seconds"], "Controller wall")
        cpu = _number(snapshot["cpu_seconds"], "Controller CPU")
    except (KeyError, TypeError) as exc:
        raise RemediationBudgetError("Missing controller resource snapshot") from exc
    native_keys = ("native_self_cpu_seconds", "native_waited_children_cpu_seconds",
                   "native_self_plus_waited_children_cpu_seconds")
    if any(key in snapshot for key in native_keys):
        if not all(key in snapshot for key in native_keys):
            raise RemediationBudgetError("Incomplete native CPU components")
        own, waited, native = (_number(snapshot[key], key) for key in native_keys)
        if not math.isclose(own + waited, native, rel_tol=0.0, abs_tol=1e-6):
            raise RemediationBudgetError("Native CPU components do not reconcile")
        cpu = max(cpu, native)
    if "cpu_highwater_seconds" in snapshot:
        cpu = max(cpu, _number(snapshot["cpu_highwater_seconds"], "CPU high-water"))
    return wall, cpu


def _process_birth_utc() -> float:
    env = os.environ.copy()
    env.update({"LC_ALL": "C", "TZ": "UTC0"})
    try:
        result = subprocess.run(["ps", "-p", str(os.getpid()), "-o", "lstart="],
                                check=True, capture_output=True, text=True, timeout=5,
                                env=env)
        text = result.stdout.strip()
        match = re.fullmatch(
            r"[A-Za-z]{3}\s+([A-Za-z]{3})\s+(\d{1,2})\s+"
            r"(\d{2}):(\d{2}):(\d{2})\s+(\d{4})", text)
        if match is None:
            raise ValueError("Unparseable ps process birth")
        month, day, hour, minute, second, year = match.groups()
        months = {name: index for index, name in enumerate(
            ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"), 1)}
        return datetime(int(year), months[month], int(day), int(hour), int(minute),
                        int(second), tzinfo=UTC).timestamp()
    except (OSError, subprocess.SubprocessError, KeyError, ValueError) as exc:
        raise RemediationBudgetError("Controller process birth telemetry unavailable") from exc


def _native_cpu() -> tuple[float, float]:
    try:
        own = resource.getrusage(resource.RUSAGE_SELF)
        waited = resource.getrusage(resource.RUSAGE_CHILDREN)
    except OSError as exc:
        raise RemediationBudgetError("Native controller CPU accounting unavailable") from exc
    return (_number(own.ru_utime + own.ru_stime, "Native self CPU"),
            _number(waited.ru_utime + waited.ru_stime, "Native waited-child CPU"))


def _live_group_cpu(run_dir: Path | None) -> tuple[float, str]:
    if run_dir is None:
        return 0.0, "NOT_STARTED"
    run_dir = Path(run_dir)
    if run_dir.is_symlink():
        raise RemediationBudgetError("Controller resource path is redirected")
    lease = run_dir / _LEASE
    if lease.is_symlink():
        raise RemediationBudgetError("Controller resource lease is redirected")
    if not lease.exists():
        return 0.0, "NO_LEASE"
    if (run_dir.resolve(strict=True) != Path(os.path.abspath(run_dir)) or
            not lease.is_file()):
        raise RemediationBudgetError("Controller resource lease is not regular")
    try:
        document = json.loads(lease.read_text())
        if document["run_id"] != run_dir.name:
            raise ValueError("Lease run identity mismatch")
        if document["state"] == "TERMINAL":
            return 0.0, "TERMINAL"
        if document["state"] != "RUNNING":
            raise ValueError("Unknown lease state")
        pid = document["runner_pid"]
        if (type(pid) is not int or pid <= 1 or pid == os.getpid() or
                document["process_group_id"] != pid):
            raise ValueError("Invalid scientific process-group identity")
        samples = sample_process_group(pid)
        if len({sample.pid for sample in samples}) != len(samples):
            raise ValueError("Duplicate sampled process identity")
        if any(sample.pgid != pid for sample in samples):
            raise ValueError("Sampled process escaped declared group")
        return (sum(_number(sample.cpu_seconds, "Live group CPU") for sample in samples),
                "LIVE_SAMPLED" if samples else "NO_LIVE_MEMBERS_OBSERVED")
    except (KeyError, TypeError, ValueError, OSError, RuntimeError) as exc:
        raise RemediationBudgetError("Controller process-group accounting unavailable") from exc


class ControllerMeter:
    """One external-controller lifetime; no test or scientific-worker CLI mode."""
    def __init__(self):
        if os.environ.get("NC0A_WATCHDOG_PARENT_PID"):
            raise RemediationBudgetError("ControllerMeter is forbidden in the scientific child")
        self.pid = os.getpid()
        self.birth = _process_birth_utc()
        self.last_utc, self.last_mono = time.time(), time.perf_counter()
        if self.last_utc < self.birth:
            raise RemediationBudgetError("Controller birth is in the future")
        self.cpu_highwater = 0.0

    def snapshot(self, run_dir: Path | None = None) -> dict:
        if os.getpid() != self.pid or os.environ.get("NC0A_WATCHDOG_PARENT_PID"):
            raise RemediationBudgetError("ControllerMeter cannot be inherited by a scientific child")
        live_cpu, group_state = _live_group_cpu(run_dir)
        # Read native totals after the sampler so its external ps helper is
        # accounted. Reaping across this boundary may conservatively count
        # scientific CPU twice; high-water keeps that charge instead of hiding it.
        own, waited = _native_cpu()
        utc, mono = time.time(), time.perf_counter()
        divergence = (utc - self.last_utc) - (mono - self.last_mono)
        if abs(divergence) > 2.0 or utc < self.last_utc or mono < self.last_mono:
            raise RemediationBudgetError("Controller suspend or wall-clock anomaly")
        self.last_utc, self.last_mono = utc, mono
        wall = _number(utc - self.birth, "Controller lifetime wall")
        self.cpu_highwater = max(self.cpu_highwater, own + waited + live_cpu)
        return {"wall_seconds": wall, "cpu_seconds": self.cpu_highwater,
                "native_self_cpu_seconds": own,
                "native_waited_children_cpu_seconds": waited,
                "native_self_plus_waited_children_cpu_seconds": own + waited,
                "live_group_cpu_seconds": live_cpu, "live_group_state": group_state,
                "cpu_highwater_seconds": self.cpu_highwater,
                "process_birth_utc_seconds_floor": self.birth,
                "wall_semantics": "UTC process-birth floor; conservatively includes <1s startup rounding",
                "cpu_semantics": "high-water self + waited children + sampled live group; "
                                 "possible conservative overlap at reaping"}


def budget_allocation(prior: dict, meter_snapshot: dict, extra_output_bytes: int = 0) -> dict:
    """Return a strictly positive allocation after old/new cost and stop reserves."""
    old_wall, old_cpu, old_output, old_auxiliary = _prior(prior)
    wall, cpu = _snapshot(meter_snapshot)
    output = _bytes(extra_output_bytes, "New attributed output")
    remaining = {
        "remaining_wall_seconds": TOTAL_WALL_SECONDS - old_wall - wall - CLOSING_WALL_SECONDS - GUARD_WALL_SECONDS,
        "remaining_cpu_seconds": TOTAL_CPU_SECONDS - old_cpu - cpu - CLOSING_CPU_SECONDS - GUARD_CPU_SECONDS,
        "remaining_output_bytes": TOTAL_OUTPUT_BYTES - old_output - old_auxiliary - output - CLOSING_OUTPUT_BYTES,
    }
    if any(value <= 0 for value in remaining.values()):
        raise RemediationBudgetError("Cumulative budget exhausted including stopping/closing reserves")
    return {**remaining,
            "closing_reserve": {"wall_seconds": CLOSING_WALL_SECONDS,
                                "cpu_seconds": CLOSING_CPU_SECONDS,
                                "output_bytes": CLOSING_OUTPUT_BYTES},
            "stopping_margin": {"wall_seconds": GUARD_WALL_SECONDS,
                                "cpu_seconds": GUARD_CPU_SECONDS},
            "total_caps": {"wall_seconds": TOTAL_WALL_SECONDS,
                           "cpu_seconds": TOTAL_CPU_SECONDS, "output_bytes": TOTAL_OUTPUT_BYTES}}


def close_charge(prior: dict, actual_snapshot: dict, extra_output_bytes: int = 0,
                 highwater_snapshot: dict | None = None) -> dict:
    """Charge the final observed high-water plus a fixed, explicitly unmeasured tail.

    The caller must persist this closure within the reserved tail. A missing,
    damaged or over-reserve closure is incomplete and cannot permit another run.
    Stopping margin is not charged twice; actual termination cost is already in
    the final controller lifetime. The separate closing reserve is fully charged.
    """
    old_wall, old_cpu, old_output, old_auxiliary = _prior(prior)
    if not isinstance(actual_snapshot, dict):
        raise RemediationBudgetError("Missing final controller resource snapshot")
    if actual_snapshot.get("live_group_state") not in (None, "NOT_STARTED", "NO_LEASE", "TERMINAL"):
        raise RemediationBudgetError("Cannot close accounting before supervised group termination")
    wall, cpu = _snapshot(actual_snapshot)
    if highwater_snapshot is not None:
        high_wall, high_cpu = _snapshot(highwater_snapshot)
        wall, cpu = max(wall, high_wall), max(cpu, high_cpu)
    output = _bytes(extra_output_bytes, "New attributed output")
    total_wall = old_wall + wall + CLOSING_WALL_SECONDS
    total_cpu = old_cpu + cpu + CLOSING_CPU_SECONDS
    total_output = old_output + old_auxiliary + output + CLOSING_OUTPUT_BYTES
    if (total_wall > TOTAL_WALL_SECONDS or total_cpu > TOTAL_CPU_SECONDS or
            total_output > TOTAL_OUTPUT_BYTES):
        raise RemediationBudgetError("Final cumulative charge exceeds approved caps")
    return {"observed_new_wall_seconds": actual_snapshot["wall_seconds"],
            "observed_new_native_cpu_seconds": actual_snapshot.get(
                "native_self_plus_waited_children_cpu_seconds", actual_snapshot["cpu_seconds"]),
            "new_wall_charge_before_closing_seconds": wall,
            "new_cpu_highwater_charge_before_closing_seconds": cpu,
            "new_output_bytes_before_closing": output,
            "charged_new_wall_seconds": wall + CLOSING_WALL_SECONDS,
            "charged_new_cpu_seconds": cpu + CLOSING_CPU_SECONDS,
            "extra_output_bytes": output,
            "old_auxiliary_output_bytes": old_auxiliary,
            "charged_total_wall_seconds": total_wall,
            "charged_total_cpu_seconds": total_cpu,
            "charged_total_output_bytes": total_output,
            "closing_reserve": {"wall_seconds": CLOSING_WALL_SECONDS,
                                "cpu_seconds": CLOSING_CPU_SECONDS,
                                "output_bytes": CLOSING_OUTPUT_BYTES},
            "within_caps": True,
            "closure_semantics": "fixed tail allowance is charged, not measured; "
                                 "missing/over-reserve closure must fail closed"}
