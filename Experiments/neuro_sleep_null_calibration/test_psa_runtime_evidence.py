"""Only generated timestamp/text fixtures; no actual PS-A source or biologic data."""
import csv
from hashlib import sha256
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from psa_runtime_evidence import audit, EvidenceError, _date


class RuntimeEvidenceTests(unittest.TestCase):
    def fixture(self, root: Path):
        log = root / "run.log"
        # The 10-minute overlap must be unioned; not summed twice.
        log.write_text(
            "2026-09-24 18:00:00 start run A progress\n"
            "2026-09-24 18:20:00 finish run A progress\n"
            "2026-09-24 18:10:00 start run B progress\n"
            "2026-09-24 18:30:00 finish run B progress\n",
            encoding="utf-8",
        )
        jobs = root / "jobs.csv"
        with jobs.open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["job_id", "state"])
            for i in range(6006):
                writer.writerow([f"job{i:04}", "complete"])
        def digest(p):
            return sha256(p.read_bytes()).hexdigest()
        manifest = {
            "purpose": "PS-A_ACTIVE_TIME_METADATA_ONLY_V1",
            "timestamp_naive_utc_offset": "+08:00",
            "sources": [{"id": "run", "path": "run.log", "sha256": digest(log)}],
            "job_coverage_csv": {
                "path": "jobs.csv", "sha256": digest(jobs),
                "id_column": "job_id", "status_column": "state",
                "completed_value": "complete",
            },
            "verified_active_intervals": [
                {
                    "id": "A", "source_id": "run", "machine_id": "host-1",
                    "workers": 8, "activity_basis": "scheduler_active",
                    "basis_note": "Test scheduler active continuous interval",
                    "start": {"line": 1, "unique_text": "start run A progress"},
                    "end": {"line": 2, "unique_text": "finish run A progress"},
                },
                {
                    "id": "B", "source_id": "run", "machine_id": "host-1",
                    "workers": 4, "activity_basis": "verified_progress",
                    "basis_note": "Test verified continuous progress interval",
                    "start": {"line": 3, "unique_text": "start run B progress"},
                    "end": {"line": 4, "unique_text": "finish run B progress"},
                },
            ],
        }
        config = root / "manifest.json"
        config.write_text(json.dumps(manifest), encoding="utf-8")
        return config, manifest

    def test_source_anchored_active_union_not_calendar_or_process_sum(self):
        with TemporaryDirectory() as tmp:
            path, manifest = self.fixture(Path(tmp))
            result = audit(path)
            self.assertEqual(result["t_psa_candidate_union_active_seconds"], 1800)
            self.assertEqual(result["verified_process_interval_seconds"], 2400)
            self.assertEqual(result["nominal_worker_seconds_not_actual_cpu_measurement"],
                             20 * 60 * 8 + 20 * 60 * 4)
            self.assertEqual(result["job_coverage"]["unique_completed_jobs"], 6006)
            self.assertIn("REVIEW_REQUIRED", result["status"])

    def test_source_sha_change_fails_closed(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            path, _ = self.fixture(root)
            (root / "run.log").write_text("edited\n", encoding="utf-8")
            with self.assertRaisesRegex(EvidenceError, "SHA-256 mismatch"):
                audit(path)

    def test_missing_job_coverage_fails_closed(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            path, manifest = self.fixture(root)
            del manifest["job_coverage_csv"]
            path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(EvidenceError, "6006-job"):
                audit(path)

    def test_bad_anchor_or_unverified_active_time_fails_closed(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            path, manifest = self.fixture(root)
            manifest["verified_active_intervals"][0]["start"]["line"] = 4
            path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(EvidenceError, "anchor text"):
                audit(path)
            manifest["verified_active_intervals"][0]["start"]["line"] = 1
            manifest["verified_active_intervals"][0]["activity_basis"] = "calendar_span"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(EvidenceError, "verified evidence"):
                audit(path)

    def test_naive_offset_and_timezone_normalization(self):
        d = _date("2026-09-24 18:00:00", "+08:00")
        self.assertEqual(d.isoformat(), "2026-09-24T10:00:00+00:00")
        with self.assertRaises(EvidenceError):
            _date("2026-09-24 18:00:00", "UNKNOWN")

    def test_interleaved_log_offsets_are_not_inferred_as_active(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            path, manifest = self.fixture(root)
            # A giant calendar gap is not included unless the user supplies
            # an explicitly verified active interval spanning it.
            data = (root / "run.log").read_text(encoding="utf-8")
            data += "2026-10-09 16:30:00 final unrelated entry\n"
            (root / "run.log").write_text(data, encoding="utf-8")
            manifest["sources"][0]["sha256"] = sha256(
                (root / "run.log").read_bytes()).hexdigest()
            path.write_text(json.dumps(manifest), encoding="utf-8")
            self.assertEqual(audit(path)["t_psa_candidate_union_active_seconds"], 1800)


if __name__ == "__main__":
    unittest.main()
