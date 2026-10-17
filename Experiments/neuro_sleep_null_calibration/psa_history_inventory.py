"""Read-only inventory of original PS-A logs/jobs; never infer active time.

Usage: python psa_history_inventory.py PRIVATE_RUNTIME NEW_PRIVATE_OUTPUT_DIR
       --utc-offset +08:00
Outputs contain metadata only but must remain private. No MAT files are opened.
Command partitions are provisional: missing launches/concurrency require review.
"""
from __future__ import annotations

import argparse
import bisect
from collections import Counter
import csv
import json
from pathlib import Path
import re

from psa_runtime_evidence import _date, _sha, _union_seconds

LOG = re.compile(r"^(20\d\d-\d\d-\d\d \d\d:\d\d:\d\d,\d{3}) (.*)$")
JOB = re.compile(r"completed job \d+/\d+ key=(\S+)")
WINDOW = re.compile(r"completed recording=(\S+) target=(\S+) subset=(\d+) (state\d+_window\d+)")
CHECKPOINT = re.compile(r"checkpoint recording=(\S+) analysis=(\S+) window=(\d+) repeat=(\d+)/200")


def inventory(root: Path, output: Path, offset: str) -> dict:
    if output.exists():
        raise ValueError("Output directory must be new; originals are never overwritten")
    commands = (root / "commands.log").read_text().splitlines()
    starts = [_date(line.split()[0], offset) for line in commands]
    if not starts or starts != sorted(set(starts)):
        raise ValueError("Missing or unordered invocation timestamps")
    runs = [{"command_line": i + 1, "command_timestamp": t.isoformat(),
             "checkpoints": 0, "completed_jobs": 0, "completed_windows": 0}
            for i, t in enumerate(starts)]
    entries = [[] for _ in runs]
    completed, windows, resets, regressions, unknown = [], [], [], [], []
    previous = previous_cp = None
    for number, line in enumerate((root / "execution.log").open(), 1):
        match = LOG.match(line)
        if not match:
            unknown.append(number)
            continue
        t = _date(match[1], offset)
        index = bisect.bisect_right(starts, t) - 1
        if index < 0:
            raise ValueError("Activity precedes first recorded invocation")
        if previous and t < previous[0]:
            regressions.append({"lines": [previous[1], number],
                                "backstep_seconds": (previous[0] - t).total_seconds()})
        previous = (t, number)
        entries[index].append((t, number))
        job, window, cp = JOB.search(line), WINDOW.search(line), CHECKPOINT.search(line)
        if job:
            completed.append(job[1]); runs[index]["completed_jobs"] += 1
        elif window:
            windows.append("::".join(window.groups()))
            runs[index]["completed_windows"] += 1
            previous_cp = None
        elif cp:
            runs[index]["checkpoints"] += 1
            key, count = cp.groups()[:3], int(cp[4])
            if previous_cp and key == previous_cp[0] and count <= previous_cp[1]:
                resets.append({"lines": [previous_cp[2], number],
                               "previous_repeat": previous_cp[1], "next_repeat": count})
            previous_cp = (key, count, number)
        elif "all selected population-size jobs complete" not in line:
            unknown.append(number)
    for run, events in zip(runs, entries):
        if not events:
            run["no_logged_activity"] = True
            continue
        run.update(first=events[0][0].isoformat(), last=events[-1][0].isoformat(),
                   first_line=events[0][1], last_line=events[-1][1],
                   progress_envelope_seconds=(events[-1][0] - events[0][0]).total_seconds())
        pairs = list(zip(events, events[1:]))
        run["gaps_over_60s_NOT_classified_idle"] = [
            {"lines": [a[1], b[1]], "seconds": (b[0] - a[0]).total_seconds()}
            for a, b in pairs if (b[0] - a[0]).total_seconds() > 60]
        # Exploratory sensitivity, NOT an activity classifier or resource gate.
        # Union prevents double-counting overlaps caused by clock backsteps.
        run["cadence_union_seconds_NOT_active_time"] = {
            str(cap): _union_seconds([(a[0], b[0]) for a, b in pairs
                                     if 0 <= (b[0] - a[0]).total_seconds() <= cap])
            for cap in (10, 30, 60, 120, 300, 600)}
    rows, hashes, job_windows, statuses, q_count = [], [], [], Counter(), 0
    for path in sorted((root / "jobs").glob("*.json")):
        job = json.loads(path.read_text())
        key = "::".join([job["recording_id"], job["target_label"], str(job["subset_repeat"])])
        rows.append((key, job["status"]))
        hashes.append(f"{_sha(path)}  {path.name}\n")
        statuses[job["status"]] += 1
        for name, window in job["windows"].items():
            job_windows.append(key + "::" + name)
            q_count += len(window["q_values"])
    output.mkdir(parents=True, exist_ok=False)
    with (output / "completed-jobs.csv").open("x", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["job_id", "state"])
        writer.writerows(sorted(rows))
    (output / "job-file-hashes.txt").write_text("".join(hashes))
    report = {
        "status": "INVENTORY_ONLY_T_PSA_NOT_ESTABLISHED",
        "source_hashes": {p.name: _sha(p) for p in sorted(root.iterdir()) if p.is_file()},
        "runs_partitioned_by_recorded_command_time": runs,
        "job_files": len(rows), "unique_job_ids": len(set(k for k, _ in rows)),
        "job_status_counts": dict(statuses), "q_value_count": q_count,
        "logged_jobs": len(completed), "unique_logged_jobs": len(set(completed)),
        "logged_windows": len(windows), "unique_logged_windows": len(set(windows)),
        "job_id_sets_equal": set(completed) == set(k for k, _ in rows),
        "window_id_sets_equal": set(windows) == set(job_windows),
        "checkpoint_resets": resets, "timestamp_backsteps": regressions,
        "unclassified_log_lines": unknown,
        "job_csv_sha256": _sha(output / "completed-jobs.csv"),
        "job_hash_manifest_sha256": _sha(output / "job-file-hashes.txt"),
    }
    (output / "inventory.json").write_text(json.dumps(report, indent=2) + "\n")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("runtime", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--utc-offset", required=True)
    args = parser.parse_args()
    report = inventory(args.runtime, args.output, args.utc_offset)
    print(report["status"])
    print(f"Job files: {report['job_files']}; logged completions: {report['logged_jobs']}")


if __name__ == "__main__":
    main()
