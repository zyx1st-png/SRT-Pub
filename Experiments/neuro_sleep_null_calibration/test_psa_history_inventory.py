"""Invented metadata fixtures only; never access real PS-A data."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from psa_history_inventory import inventory


class InventoryTests(unittest.TestCase):
    def fixture(self, path):
        root = path / "source"
        (root / "jobs").mkdir(parents=True)
        (root / "commands.log").write_text("2026-09-24T18:00:00+0800 python runner.py\n")
        (root / "execution.log").write_text(
            "2026-09-24 18:00:01,500 INFO checkpoint recording=r analysis=N100 window=0 repeat=10/200\n"
            "2026-09-24 18:00:01,400 INFO checkpoint recording=r analysis=N100 window=0 repeat=20/200\n"
            "2026-09-24 18:00:02,500 INFO checkpoint recording=r analysis=N100 window=0 repeat=10/200\n"
            "2026-09-24 18:10:00,000 INFO completed recording=r target=N100 subset=0 state0_window0\n"
            "2026-09-24 18:10:00,001 INFO completed job 1/1 key=r::N100::0\n")
        (root / "jobs" / "one.json").write_text(json.dumps({
            "recording_id": "r", "target_label": "N100", "subset_repeat": 0,
            "status": "complete", "windows": {"state0_window0": {"q_values": [0] * 200}}}))
        return root

    def test_inventory_preserves_unknown_gaps_repeats_and_clock_backsteps(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp); root = self.fixture(path)
            result = inventory(root, path / "report", "+08:00")
            self.assertTrue(result["job_id_sets_equal"])
            self.assertTrue(result["window_id_sets_equal"])
            self.assertEqual(result["q_value_count"], 200)
            self.assertEqual(result["checkpoint_resets"][0]["previous_repeat"], 20)
            self.assertEqual(result["timestamp_backsteps"][0]["backstep_seconds"], 0.1)
            run = result["runs_partitioned_by_recorded_command_time"][0]
            self.assertAlmostEqual(run["cadence_union_seconds_NOT_active_time"]["60"], 1.101)
            self.assertEqual(len(run["gaps_over_60s_NOT_classified_idle"]), 1)
            self.assertEqual(result["status"], "INVENTORY_ONLY_T_PSA_NOT_ESTABLISHED")

    def test_refuses_existing_output_and_reports_missing_completion_coverage(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp); root = self.fixture(path)
            (root / "execution.log").write_text("2026-09-24 18:00:01,000 INFO unknown event\n")
            result = inventory(root, path / "report", "+08:00")
            self.assertFalse(result["job_id_sets_equal"])
            self.assertEqual(result["unclassified_log_lines"], [1])
            with self.assertRaisesRegex(ValueError, "never overwritten"):
                inventory(root, path / "report", "+08:00")


if __name__ == "__main__":
    unittest.main()
