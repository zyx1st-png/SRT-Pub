"""B1 non-consuming admission regressions. All identities/resources are synthetic."""
from __future__ import annotations

import fcntl
import io
import json
import os
import sys
import unittest
import uuid
from contextlib import ExitStack, redirect_stdout
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import h3_supervised_pilot as pilot
import nc0a_watchdog as watchdog
import observed_calibration_remediation as remedy
import observed_calibration_runner as runner
import riken_source_identity as identity
import test_observed_calibration_remediation as fixtures


class TestReadOnlyPreflight(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.TestObservedRemediation()
        self.f.setUp()
        self.scratch_home = self.f.root / "scratch-home"
        self.scratch_home.mkdir()
        self.f.packet.update({"method_sha256": runner.METHOD_SHA256,
                              "runtime_lock_sha256": identity.sha256_file(HERE / "g0-runtime-macos-arm64.lock")})
        self.f.packet["prior_run"]["accounting_cpu_count_upper_bound"] = os.cpu_count()
        self.new_id = str(uuid.uuid4())
        self.args = {"head": self.f.head, "run_id": self.new_id,
                     "run_dir": self.f.parent / self.new_id, "old_run_dir": self.f.old_run,
                     "phase2": self.f.signal_dir, "psa": self.f.psa, "state_dir": self.f.state}
        for name in ("global.lock", pilot._HOST_LOCK):
            (self.f.state / name).touch()

    def snapshot(self):
        return {str(p.relative_to(self.f.root)): (p.read_bytes() if p.is_file() else "DIRECTORY")
                for p in self.f.root.rglob("*")}

    def admission(self, *, free_gib=48, runtime=True, method=None, head_ok=True):
        stack = ExitStack()
        stack.enter_context(self.f.patches())
        stack.enter_context(patch.object(Path, "home", return_value=self.scratch_home))
        stack.enter_context(patch.object(remedy, "_original_budget", return_value=self.f.prior_info))
        stack.enter_context(patch.object(pilot, "_git_identity", side_effect=(
            lambda head: {"head_sha": head}) if head_ok else pilot.H3PilotError("HEAD mismatch")))
        stack.enter_context(patch.object(runner.h3, "_method_is_effective", return_value=(
            True, method or runner.METHOD_SHA256)))
        stack.enter_context(patch.object(identity, "h3_runtime_manifest", return_value={
            "replay_environment_matches_recorded_versions_and_candidate_lock": runtime}))
        stack.enter_context(patch.object(remedy, "process_counters", return_value={
            "native_io_semantics": "SYNTHETIC_PREFLIGHT_SENSORS"}))
        stack.enter_context(patch.object(runner, "validate_private_identities", return_value=(
            self.f.signal_dir, self.f.psa, {"synthetic": True})))
        stack.enter_context(patch.object(runner, "validate_internal_apfs", return_value={"filesystem": "APFS"}))
        # Keep the real backend validator and 40-GiB launch thresholds; replace sensors only.
        stack.enter_context(patch.object(watchdog.sys, "platform", "darwin"))
        stack.enter_context(patch.object(watchdog.os, "uname", return_value=SimpleNamespace(machine="arm64")))
        stack.enter_context(patch.object(watchdog, "sample_macos_native_state", return_value={
            "ac_power": True, "thermal_normal": True, "swap_free_bytes": 3 << 30,
            "swap_used_bytes": 1 << 30}))
        stack.enter_context(patch.object(pilot, "sample_host_memory_pressure", return_value={"free_percent": 60}))
        stack.enter_context(patch.object(watchdog.shutil, "disk_usage", return_value=SimpleNamespace(free=free_gib << 30)))
        stack.enter_context(patch.object(remedy, "host_observation", return_value={"synthetic": True}))
        for owner, name in ((runner, "_private_process_row"), (runner, "execute_rows"), (watchdog, "supervise")):
            stack.enter_context(patch.object(owner, name, side_effect=AssertionError("preflight cannot compute")))
        return stack

    def assert_readonly(self, **changes):
        before = self.snapshot()
        with self.admission(**changes):
            report = remedy.preflight(**self.args)
        self.assertEqual(before, self.snapshot())
        self.assertFalse(self.args["run_dir"].exists())
        self.assertFalse(list(self.f.state.glob("*.claim.json")))
        return report

    def test_normal_preflight_is_readonly_and_never_authorizes(self):
        report = self.assert_readonly()
        self.assertEqual(report["status"], "PREFLIGHT PASS", report)
        self.assertTrue(all(c["status"] == "PASS" for c in report["checks"]))
        self.assertFalse(report["execution_authorized"])
        self.assertFalse(report["claim_consumed_by_preflight"])
        self.assertEqual(report["created_by_preflight"], [])
        self.assertIn("Snapshot only", report["dynamic_state"])

    def test_38_GiB_refuses_preflight_and_launch_without_consumption(self):
        limits = pilot._build_watchdog_limits(remedy.RESOURCE_CANDIDATE)
        self.assertEqual(limits.minimum_boot_free_disk_bytes, 40 << 30)
        self.assertEqual(limits.minimum_swap_volume_free_disk_bytes, 40 << 30)
        self.assertEqual(self.assert_readonly(free_gib=38)["status"], "PREFLIGHT NO-GO")
        with self.admission(free_gib=38):
            path, _, args = self.f.make_auth()
            before = self.snapshot()
            result = remedy.launch(**args, authorization=path, phase2=self.f.signal_dir,
                                   psa=self.f.psa, state_dir=self.f.state)
            self.assertEqual(result["status"], "PREFLIGHT NO-GO")
            self.assertEqual(before, self.snapshot())
            self.assertFalse(list(self.f.state.glob("*.claim.json")))

    def test_Python_HEAD_and_method_mismatch_do_not_consume(self):
        for changes in ({"runtime": False}, {"head_ok": False}, {"method": "f" * 64}):
            with self.subTest(changes=changes):
                self.assertEqual(self.assert_readonly(**changes)["status"], "PREFLIGHT NO-GO")

    def test_runtime_lock_and_original_evidence_mismatch_do_not_consume(self):
        with self.admission():
            before = self.snapshot()
            self.f.packet["runtime_lock_sha256"] = "f" * 64
            self.assertEqual(remedy.preflight(**self.args)["status"], "PREFLIGHT NO-GO")
            self.f.packet["runtime_lock_sha256"] = identity.sha256_file(HERE / "g0-runtime-macos-arm64.lock")
            with patch.object(remedy, "_original_budget", side_effect=ValueError("old evidence corrupt")):
                report = remedy.preflight(**self.args)
                self.assertEqual(report["status"], "PREFLIGHT NO-GO")
                self.assertEqual(report["checks"][1]["name"], "original_six_and_audits")
            self.assertEqual(before, self.snapshot())

    def test_already_claimed_exception_refuses_new_UUID_without_writes(self):
        with self.admission():
            path, auth, args = self.f.make_auth()
            with pilot._host_lock(self.f.state), \
                 watchdog.HashChainLog(self.f.state / pilot._HOST_LEDGER) as log:
                remedy.claim_locked(log, self.f.events(), {
                    "binding": auth["binding"], "authorization_sha256": "a" * 64,
                    "authorization_bytes": path.stat().st_size})
            before = self.snapshot()
            self.assertNotEqual(args["run_id"], self.new_id)
            result = remedy.preflight(**self.args)
            self.assertEqual(result["status"], "PREFLIGHT NO-GO")
            self.assertEqual(before, self.snapshot())

    def test_held_or_missing_lock_refuses_without_creating_lock(self):
        with self.admission():
            with (self.f.state / "global.lock").open("rb") as stream:
                fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
                before = self.snapshot()
                self.assertEqual(remedy.preflight(**self.args)["status"], "PREFLIGHT NO-GO")
                self.assertEqual(before, self.snapshot())
            (self.f.state / "global.lock").unlink()  # Synthetic fixture only.
            before = self.snapshot()
            self.assertEqual(remedy.preflight(**self.args)["status"], "PREFLIGHT NO-GO")
            self.assertEqual(before, self.snapshot())

    def test_cli_preflight_has_structured_status_and_requires_no_approval(self):
        with self.admission(), patch.dict(os.environ, {
            "SRT_PHASE2_ROOT": str(self.f.signal_dir), "SRT_PSA_ROOT": str(self.f.psa)}):
            before = self.snapshot()
            output = io.StringIO()
            with redirect_stdout(output):
                code = remedy.main(["--preflight", "--head", self.f.head, "--run-id", self.new_id,
                                    "--run-dir", str(self.args["run_dir"])])
            self.assertEqual(code, 0, output.getvalue())
            self.assertEqual(json.loads(output.getvalue())["status"], "PREFLIGHT PASS")
            self.assertEqual(before, self.snapshot())

    def test_cli_preflight_resource_refusal_exit_2_and_no_state_changes(self):
        with self.admission(free_gib=38), patch.dict(os.environ, {
            "SRT_PHASE2_ROOT": str(self.f.signal_dir), "SRT_PSA_ROOT": str(self.f.psa)}):
            before = self.snapshot()
            output = io.StringIO()
            with redirect_stdout(output):
                code = remedy.main(["--preflight", "--head", self.f.head, "--run-id", self.new_id,
                                    "--run-dir", str(self.args["run_dir"])])
            self.assertEqual(code, 2)
            self.assertEqual(json.loads(output.getvalue())["status"], "PREFLIGHT NO-GO")
            self.assertEqual(before, self.snapshot())
