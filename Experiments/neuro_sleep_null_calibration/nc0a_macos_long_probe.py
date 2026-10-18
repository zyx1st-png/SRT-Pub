"""Run one fixed, nonformal four-worker 32E factor-MST probe under watchdog.

This is a bounded engineering measurement, not a formal NC-0a test. It uses a
separate fixed seed, one maximum-size synthetic fixture, four chains, and
strict local limits. It cannot run the 16-case/128-chain formal battery.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import platform
import sys

from nc0a_macos_feasibility_probe import R11_LONG_PROBE_ROOT
from nc0a_watchdog import WatchdogLimits, supervise


MODULE_DIR = Path(__file__).resolve().parent
PROBE_SCRIPT = MODULE_DIR / "nc0a_macos_feasibility_probe.py"
MAX_WALL_SECONDS = 20 * 60
MAX_CPU_SECONDS = 60 * 60
MAX_RSS_BYTES = 2 * 1024**3
MAX_RUN_DISK_BYTES = 64 * 1024**2


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_directory", type=Path)
    args = parser.parse_args(argv)
    if sys.platform != "darwin" or platform.machine() != "arm64":
        parser.error("The R11 long probe requires native Apple Silicon macOS")
    root = args.run_directory.resolve()
    repository_root = MODULE_DIR.parents[1].resolve()
    if root == repository_root or repository_root in root.parents:
        parser.error("Probe output must remain outside the repository checkout")
    if root.exists() and any(root.iterdir()):
        parser.error("Probe run directory must be new or empty; outputs are never overwritten")
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    report_dir = root / "reports"
    command = [sys.executable, str(PROBE_SCRIPT), "long-chain",
               "--family", "factor-mst", "--workers", "4",
               "--report-dir", str(report_dir)]
    limits = WatchdogLimits(
        wall_seconds=MAX_WALL_SECONDS,
        cpu_seconds=MAX_CPU_SECONDS,
        aggregate_rss_bytes=MAX_RSS_BYTES,
        max_workers=4,
        run_disk_bytes=MAX_RUN_DISK_BYTES,
        reserve_free_disk_bytes=4 * 1024**3,
        case_seconds=MAX_WALL_SECONDS,
        oracle_seconds=10 * 60,
        memory_enforcement_backend="MACOS_SAMPLED_PRESSURE",
        host_memory_free_percent_stop=20,
        boot_volume_path="/System/Volumes/Data",
        boot_reserve_free_disk_bytes=20 * 1024**3,
        minimum_boot_free_disk_bytes=25 * 1024**3,
        swap_volume_path="/System/Volumes/VM",
        swap_volume_reserve_free_disk_bytes=20 * 1024**3,
        minimum_swap_volume_free_disk_bytes=25 * 1024**3,
        swap_growth_stop_bytes=1024**3,
        require_ac_power=True,
        require_thermal_normal=True,
        require_sleep_assertion=True,
    )
    result = supervise(command, run_dir=root, limits=limits,
                       audit_name="r11-long-probe-watchdog.jsonl",
                       stdout_name="r11-long-probe.stdout.log")
    print(json.dumps({
        "status": "NONFORMAL_ENGINEERING_PROBE",
        "seed_root": R11_LONG_PROBE_ROOT,
        "scheduled_work": "N=3900 factor-mst; 4 independent chains; 32E each",
        "resource_limits": {
            "wall_seconds": MAX_WALL_SECONDS,
            "aggregate_cpu_seconds": MAX_CPU_SECONDS,
            "sampled_process_group_rss_bytes": MAX_RSS_BYTES,
            "run_directory_bytes": MAX_RUN_DISK_BYTES,
            "actual_workers": 4,
            "boot_and_vm_volume_reserve_bytes": 20 * 1024**3,
            "swap_used_growth_bytes": 1024**3,
        },
        "watchdog": result,
        "report_files": sorted(p.name for p in report_dir.glob("*.json"))
            if report_dir.exists() else [],
    }, sort_keys=True, indent=2), flush=True)
    return 0 if result["status"] == "completed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
