"""Deterministic accounting tests; no RIKEN source or execution/ledger writes."""
from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import observed_remediation_budget as budget

PRIOR = {"old_wall_charge_seconds": 190.68176041699851,
         "old_cpu_upper_charge_seconds": 247.79796356279473,
         "old_output_bytes": 968363}


class RemediationBudgetTests(unittest.TestCase):
    def test_old_numbers_are_charged_once_and_reserves_do_not_expand_caps(self):
        result = budget.budget_allocation(PRIOR, {"wall_seconds": 10., "cpu_seconds": 12.}, 1000)
        self.assertAlmostEqual(result["remaining_wall_seconds"],
                               14400 - PRIOR["old_wall_charge_seconds"] - 10 - 5 - 1)
        self.assertAlmostEqual(result["remaining_cpu_seconds"],
                               14400 - PRIOR["old_cpu_upper_charge_seconds"] - 12 - 40 - 8)
        self.assertEqual(result["remaining_output_bytes"], 2**30 - 968363 - 1000 - 65536)
        closed = budget.close_charge(PRIOR, {"wall_seconds": 10., "cpu_seconds": 12.}, 1000)
        self.assertAlmostEqual(closed["charged_total_wall_seconds"],
                               PRIOR["old_wall_charge_seconds"] + 10 + 5)
        self.assertAlmostEqual(closed["charged_total_cpu_seconds"],
                               PRIOR["old_cpu_upper_charge_seconds"] + 12 + 40)
        self.assertEqual(closed["charged_total_output_bytes"], 968363 + 1000 + 65536)
        self.assertEqual(closed["charged_new_wall_seconds"], 15.)
        self.assertEqual(closed["charged_new_cpu_seconds"], 52.)
        self.assertEqual(closed["extra_output_bytes"], 1000)
        self.assertTrue(closed["within_caps"])

    def test_old_auxiliary_bytes_remain_distinct_and_are_charged_once(self):
        prior = {**PRIOR, "old_auxiliary_output_bytes": 8192}
        snapshot = {"wall_seconds": 1., "cpu_seconds": 1.}
        allocation = budget.budget_allocation(prior, snapshot, 100)
        self.assertEqual(allocation["remaining_output_bytes"], 2**30 - 968363 - 8192 - 100 - 65536)
        closed = budget.close_charge(prior, snapshot, 100)
        self.assertEqual(closed["charged_total_output_bytes"], 968363 + 8192 + 100 + 65536)
        self.assertEqual(closed["old_auxiliary_output_bytes"], 8192)
        self.assertEqual(prior["old_output_bytes"], 968363)
        with self.assertRaises(budget.RemediationBudgetError):
            budget.close_charge({**prior, "old_auxiliary_output_bytes": -1}, snapshot)

    def test_invalid_or_exhausted_numbers_fail_closed(self):
        for bad in (float("nan"), float("inf"), -1, True, "1", 10**1000):
            for key in ("wall_seconds", "cpu_seconds"):
                with self.subTest(bad=bad, key=key), self.assertRaises(budget.RemediationBudgetError):
                    budget.budget_allocation(PRIOR, {"wall_seconds": 1., "cpu_seconds": 1., key: bad})
        for bad in (-1, True, 1.5):
            with self.subTest(output=bad), self.assertRaises(budget.RemediationBudgetError):
                budget.budget_allocation(PRIOR, {"wall_seconds": 1., "cpu_seconds": 1.}, bad)
        for snapshot in ({}, {"wall_seconds": 14400, "cpu_seconds": 0},
                         {"wall_seconds": 0, "cpu_seconds": 14400}):
            with self.subTest(snapshot=snapshot), self.assertRaises(budget.RemediationBudgetError):
                budget.budget_allocation(PRIOR, snapshot)
        with self.assertRaises(budget.RemediationBudgetError):
            budget.budget_allocation(PRIOR, {"wall_seconds": 0, "cpu_seconds": 0}, 2**30)
        with self.assertRaises(budget.RemediationBudgetError):
            budget.close_charge(PRIOR, {"wall_seconds": 14400, "cpu_seconds": 0})
        with self.assertRaises(budget.RemediationBudgetError):
            budget.close_charge(PRIOR, {"wall_seconds": 0, "cpu_seconds": 14400})

    def test_reaping_overlap_is_retained_as_charge_not_called_native_observation(self):
        final = {"wall_seconds": 30., "cpu_seconds": 22., "cpu_highwater_seconds": 25.,
                 "native_self_cpu_seconds": 4., "native_waited_children_cpu_seconds": 16.,
                 "native_self_plus_waited_children_cpu_seconds": 20.}
        result = budget.close_charge(PRIOR, final,
                                     highwater_snapshot={"wall_seconds": 29., "cpu_seconds": 28.})
        self.assertEqual(result["observed_new_native_cpu_seconds"], 20.)
        self.assertEqual(result["new_cpu_highwater_charge_before_closing_seconds"], 28.)
        self.assertEqual(result["charged_total_cpu_seconds"], PRIOR["old_cpu_upper_charge_seconds"] + 28 + 40)
        final["native_self_plus_waited_children_cpu_seconds"] = 19.
        with self.assertRaises(budget.RemediationBudgetError):
            budget.close_charge(PRIOR, final)

    def test_live_or_unreconciled_process_group_cannot_be_closed(self):
        for state in ("LIVE_SAMPLED", "NO_LIVE_MEMBERS_OBSERVED", "UNKNOWN"):
            with self.subTest(state=state), self.assertRaises(budget.RemediationBudgetError):
                budget.close_charge(PRIOR, {"wall_seconds": 3., "cpu_seconds": 2.,
                                            "live_group_state": state})

    def test_exact_final_caps_allowed_but_no_zero_start_allocation(self):
        snapshot = {"wall_seconds": 14400 - PRIOR["old_wall_charge_seconds"] - 5,
                    "cpu_seconds": 14400 - PRIOR["old_cpu_upper_charge_seconds"] - 40}
        output = 2**30 - PRIOR["old_output_bytes"] - 65536
        closed = budget.close_charge(PRIOR, snapshot, output)
        self.assertEqual(closed["charged_total_wall_seconds"], 14400)
        self.assertEqual(closed["charged_total_cpu_seconds"], 14400)
        self.assertEqual(closed["charged_total_output_bytes"], 2**30)
        with self.assertRaises(budget.RemediationBudgetError):
            budget.budget_allocation(PRIOR, snapshot, output)

    def test_meter_full_lifetime_startup_and_reaping_highwater(self):
        with patch.object(budget, "_process_birth_utc", return_value=100.), \
             patch.object(budget.time, "time", side_effect=[102., 103., 104.]), \
             patch.object(budget.time, "perf_counter", side_effect=[12., 13., 14.]), \
             patch.object(budget, "_native_cpu", side_effect=[(3., 2.), (4., 9.)]), \
             patch.object(budget, "_live_group_cpu", side_effect=[(10., "LIVE_SAMPLED"), (0., "TERMINAL")]):
            meter = budget.ControllerMeter()
            first = meter.snapshot()
            final = meter.snapshot()
        self.assertEqual(first["wall_seconds"], 3.)  # Includes pre-constructor process lifetime.
        self.assertEqual(first["cpu_seconds"], 15.)
        self.assertEqual(final["native_self_plus_waited_children_cpu_seconds"], 13.)
        self.assertEqual(final["cpu_seconds"], 15.)
        self.assertEqual(final["live_group_state"], "TERMINAL")

    def test_wall_jump_and_scientific_child_are_rejected(self):
        with patch.object(budget, "_process_birth_utc", return_value=100.), \
             patch.object(budget.time, "time", side_effect=[102., 110.]), \
             patch.object(budget.time, "perf_counter", side_effect=[12., 13.]), \
             patch.object(budget, "_native_cpu", return_value=(1., 0.)):
            meter = budget.ControllerMeter()
            with self.assertRaisesRegex(budget.RemediationBudgetError, "clock anomaly"):
                meter.snapshot()
        with patch.dict(os.environ, {"NC0A_WATCHDOG_PARENT_PID": "123"}), \
             patch.object(budget.subprocess, "run") as call:
            with self.assertRaisesRegex(budget.RemediationBudgetError, "scientific child"):
                budget.ControllerMeter()
            call.assert_not_called()

    def test_ps_birth_is_UTC_and_native_cpu_uses_lifetime_components(self):
        response = SimpleNamespace(stdout="Mon Oct 26 08:15:25 2026\n")
        with patch.object(budget.subprocess, "run", return_value=response) as run:
            birth = budget._process_birth_utc()
        self.assertEqual(birth, 1793002525.)
        self.assertEqual(run.call_args.kwargs["env"]["LC_ALL"], "C")
        self.assertEqual(run.call_args.kwargs["env"]["TZ"], "UTC0")
        with patch.object(budget.resource, "getrusage", side_effect=[
                SimpleNamespace(ru_utime=3., ru_stime=1.),
                SimpleNamespace(ru_utime=5., ru_stime=2.)]):
            self.assertEqual(budget._native_cpu(), (4., 7.))
        with patch.object(budget.subprocess, "run", return_value=SimpleNamespace(stdout="bad")), \
             self.assertRaises(budget.RemediationBudgetError):
            budget._process_birth_utc()

    def test_live_lease_group_and_output_identities_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve() / "synthetic-run"
            root.mkdir()
            lease = root / "h3-active-lease.json"
            self.assertEqual(budget._live_group_cpu(root), (0., "NO_LEASE"))
            doc = {"run_id": root.name, "state": "RUNNING", "runner_pid": 12345, "process_group_id": 12345}
            lease.write_text(json.dumps(doc))
            sample = SimpleNamespace(pid=12345, pgid=12345, cpu_seconds=7.)
            with patch.object(budget, "sample_process_group", return_value=[sample]):
                self.assertEqual(budget._live_group_cpu(root), (7., "LIVE_SAMPLED"))
            with patch.object(budget, "sample_process_group", return_value=[sample, sample]), \
                 self.assertRaises(budget.RemediationBudgetError):
                budget._live_group_cpu(root)
            doc["run_id"] = "wrong"
            lease.write_text(json.dumps(doc))
            with self.assertRaises(budget.RemediationBudgetError):
                budget._live_group_cpu(root)
            lease.unlink()
            lease.symlink_to(root / "missing")
            with self.assertRaises(budget.RemediationBudgetError):
                budget._live_group_cpu(root)


if __name__ == "__main__":
    unittest.main()
