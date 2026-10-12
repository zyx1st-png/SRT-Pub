"""Offline, metadata-only PS-A resumed-run evidence auditor.

This does NOT infer active time from calendar first/last timestamps.
It validates supplied source hashes and timestamped interval anchors,
joins explicit verified ACTIVE intervals, and reports time arithmetic.
An independent reviewer must still verify that the intervals cover all
work and are actually ACTIVE; a successful run is not NC-0a approval.

Usage: python psa_runtime_evidence.py /private/path/manifest.json
Never commit source logs, neuron metadata, or private paths to this repo.
"""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timedelta, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import sys

TIMESTAMP = re.compile(
    r"20\d{2}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}(?:\.\d+)?"
    r"(?:Z|[+-]\d{2}:?\d{2})?"
)
ACTIVE_EVIDENCE = {"scheduler_active", "verified_progress", "process_cpu_accounting"}
EXPECTED_COMPLETED_JOBS = 6006


class EvidenceError(ValueError):
    pass


def _date(text: str, naive_offset: str) -> datetime:
    value = text.replace(" ", "T").replace("Z", "+00:00")
    if re.search(r"[+-]\d{4}$", value):
        value = value[:-5] + value[-5:-2] + ":" + value[-2:]
    date = datetime.fromisoformat(value)
    if date.tzinfo is None:
        if not re.fullmatch(r"[+-](?:0\d|1[0-4]):[0-5]\d", naive_offset):
            raise EvidenceError("Local log timestamp requires explicit UTC offset")
        sign = -1 if naive_offset[0] == "-" else 1
        delta = timedelta(hours=int(naive_offset[1:3]),
                          minutes=int(naive_offset[4:]))
        date = date.replace(tzinfo=timezone(sign * delta))
    return date.astimezone(timezone.utc)


def _sha(path: Path) -> str:
    h = sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _read_source(manifest_dir: Path, item: dict) -> tuple[Path, list[str]]:
    source = Path(item["path"])
    if not source.is_absolute():
        source = manifest_dir / source
    if not source.is_file():
        raise EvidenceError(f"Missing source log: {item['id']}")
    digest = _sha(source)
    if digest != item.get("sha256"):
        raise EvidenceError(f"SHA-256 mismatch: {item['id']}")
    return source, source.read_text(encoding=item.get("encoding", "utf-8")).splitlines()


def _anchor(lines: list[str], marker: dict, offset: str) -> datetime:
    number = marker.get("line")
    if type(number) is not int or number < 1 or number > len(lines):
        raise EvidenceError("Timestamp anchor line is out of range")
    line = lines[number - 1]
    token = marker.get("unique_text")
    if not isinstance(token, str) or len(token) < 8 or token not in line:
        raise EvidenceError("Timestamp anchor text not present on claimed line")
    found = list(TIMESTAMP.finditer(line))
    if len(found) != 1:
        raise EvidenceError("Anchor needs exactly one parseable timestamp")
    return _date(found[0].group(), offset)


def _union_seconds(intervals: list[tuple[datetime, datetime]]) -> float:
    if not intervals:
        return 0.0
    ordered = sorted(intervals)
    start, end = ordered[0]
    total = 0.0
    for a, b in ordered[1:]:
        if a <= end:
            end = max(end, b)
        else:
            total += (end - start).total_seconds()
            start, end = a, b
    return total + (end - start).total_seconds()


def _job_count(root: Path, cfg: dict) -> dict:
    path = Path(cfg["path"])
    if not path.is_absolute():
        path = root / path
    if not path.is_file() or _sha(path) != cfg["sha256"]:
        raise EvidenceError("Job-coverage CSV absent or SHA mismatch")
    ids = []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if cfg["id_column"] not in (reader.fieldnames or ()) or (
            cfg["status_column"] not in (reader.fieldnames or ())
        ):
            raise EvidenceError("Job CSV missing required columns")
        for row in reader:
            if row[cfg["status_column"]] != cfg["completed_value"]:
                raise EvidenceError("Noncomplete job in completed job coverage CSV")
            value = row[cfg["id_column"]].strip()
            if not value:
                raise EvidenceError("Blank job ID")
            ids.append(value)
    if len(ids) != len(set(ids)) or len(ids) != EXPECTED_COMPLETED_JOBS:
        raise EvidenceError("Completed jobs not exactly 6006 unique identifiers")
    return {"unique_completed_jobs": len(ids), "csv_sha256": cfg["sha256"]}


def audit(manifest_path: str | Path) -> dict:
    source_file = Path(manifest_path).resolve()
    manifest = json.loads(source_file.read_text(encoding="utf-8"))
    if manifest.get("purpose") != "PS-A_ACTIVE_TIME_METADATA_ONLY_V1":
        raise EvidenceError("Wrong manifest type")
    offset = manifest.get("timestamp_naive_utc_offset")
    if not isinstance(offset, str):
        raise EvidenceError("Specify the log's actual local UTC offset")
    root = source_file.parent
    source_map = {}
    for entry in manifest["sources"]:
        if entry["id"] in source_map:
            raise EvidenceError("Duplicate source ID")
        source_map[entry["id"]] = _read_source(root, entry)
    if not source_map:
        raise EvidenceError("No source log")
    intervals = []
    sessions = []
    ids = set()
    machines = set()
    for interval in manifest["verified_active_intervals"]:
        key = interval["id"]
        if key in ids:
            raise EvidenceError("Duplicate interval ID")
        ids.add(key)
        if interval["activity_basis"] not in ACTIVE_EVIDENCE:
            raise EvidenceError("Activity basis requires externally verified evidence")
        if not interval.get("basis_note") or len(interval["basis_note"]) < 16:
            raise EvidenceError("Explain why entire interval was actively executing")
        if type(interval["workers"]) is not int or not 1 <= interval["workers"] <= 256:
            raise EvidenceError("Missing/implausible original worker count")
        # Archived worker configurations are observations, not new-run caps.
        # Values different from the planned <=8 workers require a separate
        # equivalence justification; do not discard historical evidence.
        machine = interval.get("machine_id", "")
        if not machine:
            raise EvidenceError("Machine identity missing")
        machines.add(machine)
        source = interval["source_id"]
        if source not in source_map:
            raise EvidenceError("Unknown interval log source")
        lines = source_map[source][1]
        start = _anchor(lines, interval["start"], offset)
        end = _anchor(lines, interval["end"], offset)
        if end <= start:
            raise EvidenceError("Non-positive active interval")
        active = (end - start).total_seconds()
        intervals.append((start, end))
        sessions.append({
            "id": key, "source_id": source,
            "machine_id": machine, "workers": interval["workers"],
            "activity_basis": interval["activity_basis"],
            "start_utc": start.isoformat(), "end_utc": end.isoformat(),
            "verified_interval_seconds": active,
            "nominal_process_worker_seconds": active * interval["workers"],
        })
    if not sessions:
        raise EvidenceError("No independently verified active intervals")
    if len(machines) != 1:
        raise EvidenceError("Multiple machines require separate comparability audit")
    if "job_coverage_csv" not in manifest:
        raise EvidenceError("Missing 6006-job completion/coverage evidence")
    job_coverage = _job_count(root, manifest["job_coverage_csv"])
    union_seconds = _union_seconds(intervals)
    process_seconds = sum(v["verified_interval_seconds"] for v in sessions)
    nominal_worker_seconds = sum(v["nominal_process_worker_seconds"] for v in sessions)
    return {
        "status": "ARITHMETIC_CHECK_ONLY_INDEPENDENT_REVIEW_REQUIRED",
        "t_psa_candidate_union_active_seconds": union_seconds,
        "verified_process_interval_seconds": process_seconds,
        "nominal_worker_seconds_not_actual_cpu_measurement": nominal_worker_seconds,
        "single_machine_id": next(iter(machines)),
        "original_worker_counts": sorted(set(s["workers"] for s in sessions)),
        "worker_profile_requires_independent_comparability_review": True,
        "segments": sessions,
        "job_coverage": job_coverage,
        "source_file_hashes": {k: _sha(v[0]) for k, v in source_map.items()},
        "manifest_sha256": _sha(source_file),
        "interpretation": (
            "Active intervals are user-supplied and source-anchored, NOT "
            "independently verified by this arithmetic program. The value is "
            "not authorized as T_PS-A until active-work/idle gaps, overlaps, "
            "resumed-job continuity and machine comparability are reviewed."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", help="Private, manually evidenced active-time manifest")
    parser.add_argument("--output", help="Optional JSON report path; does not overwrite")
    args = parser.parse_args()
    try:
        result = audit(args.manifest)
        value = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
        if args.output:
            dest = Path(args.output)
            with dest.open("x", encoding="utf-8") as file:
                file.write(value)
        else:
            print(value, end="")
        return 0
    except (EvidenceError, ValueError, KeyError, OSError) as err:
        print("EVIDENCE_NO_GO: " + str(err), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
