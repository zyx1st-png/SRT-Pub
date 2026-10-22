from __future__ import annotations

import hashlib
import io
import json
import os
from dataclasses import asdict
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
import unittest
from unittest.mock import patch

MODULE_DIR = Path(__file__).resolve().parent
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

from h3_supervised_pilot import (  # noqa: E402
    EXPECTED_GRAPH_IDS,
    EXPECTED_MANIFEST_SHA256,
    EXPECTED_PILOT_SHA256,
    HERE,
    H3_MACOS_RESOURCE_POLICY_CANDIDATE,
    H3PilotError,
    LIMITS,
    _HOST_LEDGER,
    _build_watchdog_limits,
    _default_paths,
    _prepare_run_directory,
    _preflight_macos_resources,
    _synthetic_row,
    _trial_deltas,
    _verify_recovery_directory,
    launch_real_pilot,
    launch_synthetic_test,
    main,
    validate_pilot_bundle,
)
from nc0a_watchdog import (  # noqa: E402
    HashChainLog,
    WatchdogError,
    WatchdogLimits,
    sample_process_group,
    supervise,
    verify_hash_chain,
)
from riken_source_identity import (  # noqa: E402
    H3_TRIAL_Q_ATOL_PROPOSED,
    hash_float64,
    validate_h3_replay,
)


class TestH3SupervisedPilot(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="h3-supervised-synthetic-")
        self.root = Path(self.temp.name).resolve()
        self.state = self.root / "state"
        self.runs = self.root / "runs"

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_case(self, name: str, **kwargs):
        return launch_synthetic_test(
            run_dir=self.runs / name, state_dir=self.state, **kwargs)

    def _private_root_fixture(self):
        phase2 = self.root / "phase2"
        psa = self.root / "psa"
        (phase2 / "data").mkdir(parents=True)
        (psa / "jobs").mkdir(parents=True)
        builder = phase2 / "multirecording_primary.py"
        population = psa / "population_size_scaling.py"
        source = phase2 / "data" / "synthetic-source.mat"
        builder.write_bytes(b"synthetic historical graph builder")
        population.write_bytes(b"synthetic historical population runner")
        source_bytes = b"synthetic placeholder; never parsed as signal data"
        source.write_bytes(source_bytes)
        job = psa / "jobs" / "recording-synthetic__N100__rep-001.json"
        job_bytes = b'{"synthetic_fixture":true}\n'
        job.write_bytes(job_bytes)
        builder_sha = hashlib.sha256(builder.read_bytes()).hexdigest()
        population_sha = hashlib.sha256(population.read_bytes()).hexdigest()
        job_sha = hashlib.sha256(job_bytes).hexdigest()
        pilot = {
            "historical_graph_builder_sha256": builder_sha,
            "records": [{
                "recording_id": "recording-synthetic",
                "source_filename": source.name,
                "subset_repeat": 1,
                "N": 100,
                "historical_job_sha256": job_sha,
            }],
        }
        manifest = {
            "historical_code_hashes": {
                "multirecording_primary.py": builder_sha,
                "population_size_scaling.py": population_sha,
            },
            "source_data": [{
                "recording_id": "recording-synthetic",
                "filename": source.name,
                "bytes": len(source_bytes),
            }],
        }
        pilot_path = self.root / "synthetic-pilot.json"
        manifest_path = self.root / "synthetic-manifest.json"
        pilot_path.write_text("{}", encoding="utf-8")
        manifest_path.write_text("{}", encoding="utf-8")
        return phase2, psa, pilot_path, manifest_path, pilot, manifest

    def test_run_directory_requires_exact_fixed_parent_and_refuses_symlinks(self) -> None:
        psa = self.root / "psa"
        psa.mkdir()
        run_id = str(uuid.uuid4())
        expected_parent = psa / "h3_identity_calibration_2026-10-21"
        target = expected_parent / run_id
        prepared = _prepare_run_directory(target, psa)
        self.assertEqual(prepared, target)
        self.assertTrue(expected_parent.is_dir())
        self.assertFalse(target.exists())

        with self.assertRaisesRegex(H3PilotError, "fixed private PSA output root"):
            _prepare_run_directory(psa / "other" / run_id, psa)
        with self.assertRaisesRegex(H3PilotError, "path traversal"):
            _prepare_run_directory(expected_parent / ".." / run_id, psa)
        target.mkdir()
        with self.assertRaisesRegex(H3PilotError, "new and empty"):
            _prepare_run_directory(target, psa)

        link_parent = psa / "h3_identity_calibration_2026-10-21"
        target.rmdir()
        link_parent.rmdir()
        real_parent = self.root / "redirected-parent"
        real_parent.mkdir()
        link_parent.symlink_to(real_parent, target_is_directory=True)
        with self.assertRaisesRegex(H3PilotError, "cannot be a symlink"):
            _prepare_run_directory(link_parent / str(uuid.uuid4()), psa)

        alias_root_parent = self.root / "psa-parent-alias"
        alias_root_parent.symlink_to(self.root, target_is_directory=True)
        aliased_psa = alias_root_parent / "psa"
        with self.assertRaisesRegex(H3PilotError, "symlink path components"):
            _prepare_run_directory(
                expected_parent / str(uuid.uuid4()), aliased_psa)

    def test_default_paths_reject_missing_empty_relative_and_symlink_roots(self) -> None:
        valid_phase2 = self.root / "valid-phase2"
        valid_psa = self.root / "valid-psa"
        valid_phase2.mkdir()
        valid_psa.mkdir()
        for phase2_value, psa_value in (
                (None, str(valid_psa)), ("", str(valid_psa)),
                ("   ", str(valid_psa)), ("relative", str(valid_psa)),
                (str(valid_phase2), None), (str(valid_phase2), ""),
                (str(valid_phase2), "relative")):
            env = {}
            if phase2_value is not None:
                env["SRT_PHASE2_ROOT"] = phase2_value
            if psa_value is not None:
                env["SRT_PSA_ROOT"] = psa_value
            with self.subTest(phase2=phase2_value, psa=psa_value):
                with patch.dict(os.environ, env, clear=True):
                    with self.assertRaises(H3PilotError):
                        _default_paths()
        link = self.root / "phase2-link"
        link.symlink_to(valid_phase2, target_is_directory=True)
        with patch.dict(os.environ, {
                "SRT_PHASE2_ROOT": str(link), "SRT_PSA_ROOT": str(valid_psa)},
                clear=True):
            with self.assertRaisesRegex(H3PilotError, "symlink"):
                _default_paths()

    def test_cli_rejects_empty_environment_before_any_production_write(self) -> None:
        run_id = str(uuid.uuid4())
        run_dir = self.root / "psa" / "h3_identity_calibration_2026-10-21" / run_id
        state = self.root / "must-not-be-created"
        args = [
            "--pilot", str(self.root / "unused-pilot.json"),
            "--manifest", str(self.root / "unused-manifest.json"),
            "--run-directory", str(run_dir), "--run-id", run_id,
            "--expected-head", "3" * 40,
            "--researcher-confirmation", "test-only",
        ]
        with (
            patch.dict(os.environ, {"SRT_PSA_ROOT": "  ", "SRT_PHASE2_ROOT": ""},
                       clear=True),
            patch("h3_supervised_pilot.default_host_state_dir", return_value=state),
            patch("h3_supervised_pilot.launch_real_pilot",
                  side_effect=AssertionError("launch must not be entered")),
            patch("sys.stderr", new=io.StringIO()),
        ):
            with self.assertRaises(SystemExit):
                main(args)
        self.assertFalse(run_dir.parent.exists())
        self.assertFalse(state.exists())

    def test_production_run_path_mismatch_is_rejected_before_activity_ledger(self) -> None:
        phase2, psa, pilot_path, manifest_path, pilot, manifest = \
            self._private_root_fixture()
        run_id = str(uuid.uuid4())
        wrong_run_dir = psa / "wrong-parent" / run_id
        state = self.root / "must-not-be-created-for-path-mismatch"
        head_sha = "4" * 40
        confirmation = (f"I AUTHORIZE H3 PILOT {run_id} "
                        f"{EXPECTED_PILOT_SHA256} {head_sha}")
        with (
            patch("h3_supervised_pilot.validate_pilot_bundle",
                  return_value=(pilot, manifest)),
            patch("h3_supervised_pilot.default_host_state_dir", return_value=state),
            patch("h3_supervised_pilot._git_identity", return_value={
                "head_sha": head_sha, "working_tree": "CLEAN"}),
            patch("h3_supervised_pilot._preflight_macos_resources", return_value={
                "synthetic_preflight": True}),
        ):
            with self.assertRaisesRegex(H3PilotError, "fixed private PSA output root"):
                launch_real_pilot(
                    pilot_path=pilot_path, manifest_path=manifest_path,
                    phase2_root=phase2, psa_root=psa, run_dir=wrong_run_dir,
                    state_dir=state, run_id=run_id, expected_head=head_sha,
                    researcher_confirmation=confirmation)
        self.assertFalse(wrong_run_dir.parent.exists())
        self.assertFalse(state.exists())

    def test_production_launch_preflights_roots_then_reaches_watchdog_without_science(self) -> None:
        phase2, psa, pilot_path, manifest_path, pilot, manifest = \
            self._private_root_fixture()
        run_id = str(uuid.uuid4())
        run_dir = psa / "h3_identity_calibration_2026-10-21" / run_id
        state = self.root / "host-state"
        head_sha = "1" * 40
        calls = []

        def stop_after_admission(command, *, run_dir, limits, audit_name,
                                 stdout_name, **_kwargs):
            # Exercise launch_real_pilot's real production route into supervise,
            # while never starting the real runner-child scientific computation.
            self.assertEqual(command[-1], "--runner-child")
            self.assertEqual(limits.memory_enforcement_backend,
                             "MACOS_SAMPLED_PRESSURE")
            self.assertEqual(limits.max_workers, 4)
            calls.append((command, limits))
            (run_dir / stdout_name).write_bytes(b"synthetic preflight-only watchdog stub\n")
            stdout_sha = hashlib.sha256((run_dir / stdout_name).read_bytes()).hexdigest()
            with HashChainLog(run_dir / audit_name) as audit:
                audit.append({"event": "test_stopped_after_admission",
                              "runner_stdout_sha256": stdout_sha})
            return {"status": "stopped", "reason": "TEST_STOP_AFTER_ADMISSION",
                    "returncode": None,
                    "usage": {"wall_seconds": 0.01, "cpu_seconds": 0.0}}

        confirmation = (f"I AUTHORIZE H3 PILOT {run_id} "
                        f"{EXPECTED_PILOT_SHA256} {head_sha}")
        with (
            patch("h3_supervised_pilot.validate_pilot_bundle",
                  return_value=(pilot, manifest)),
            patch("h3_supervised_pilot.default_host_state_dir", return_value=state),
            patch("h3_supervised_pilot._git_identity", return_value={
                "head_sha": head_sha, "working_tree": "CLEAN"}),
            patch("h3_supervised_pilot._preflight_macos_resources", return_value={
                "memory_enforcement": "MACOS_SAMPLED_PRESSURE_NOT_HARD",
                "synthetic_preflight": True}),
            patch("h3_supervised_pilot.supervise", side_effect=stop_after_admission),
            patch("h3_supervised_pilot.reconstruct_source_graph",
                  side_effect=AssertionError("real source graph must not be reconstructed")),
            patch("h3_supervised_pilot.run_h3_replay_for_graph",
                  side_effect=AssertionError("Louvain must not run in this test")),
        ):
            result = launch_real_pilot(
                pilot_path=pilot_path, manifest_path=manifest_path,
                phase2_root=phase2, psa_root=psa, run_dir=run_dir,
                state_dir=state, run_id=run_id, expected_head=head_sha,
                researcher_confirmation=confirmation)

        self.assertEqual(result["status"], "STOPPED_BY_WATCHDOG")
        self.assertEqual(len(calls), 1)
        self.assertTrue(run_dir.is_dir())
        self.assertTrue((state / _HOST_LEDGER).is_file())
        report = _verify_recovery_directory(run_dir, host_state_dir=state)
        self.assertEqual(report["status"], "VERIFIED_TERMINAL")
        self.assertFalse(report["resume_allowed"])

    def test_wrong_private_root_rejected_before_output_or_activity_ledger(self) -> None:
        _phase2, psa, pilot_path, manifest_path, pilot, manifest = \
            self._private_root_fixture()
        wrong_phase2 = self.root / "wrong-phase2"
        wrong_phase2.mkdir()
        run_id = str(uuid.uuid4())
        run_dir = psa / "h3_identity_calibration_2026-10-21" / run_id
        state = self.root / "must-not-be-created"
        head_sha = "2" * 40
        confirmation = (f"I AUTHORIZE H3 PILOT {run_id} "
                        f"{EXPECTED_PILOT_SHA256} {head_sha}")
        with (
            patch("h3_supervised_pilot.validate_pilot_bundle",
                  return_value=(pilot, manifest)),
            patch("h3_supervised_pilot.default_host_state_dir", return_value=state),
            patch("h3_supervised_pilot._git_identity", return_value={
                "head_sha": head_sha, "working_tree": "CLEAN"}),
        ):
            with self.assertRaisesRegex(H3PilotError, "expected private data root"):
                launch_real_pilot(
                    pilot_path=pilot_path, manifest_path=manifest_path,
                    phase2_root=wrong_phase2, psa_root=psa, run_dir=run_dir,
                    state_dir=state, run_id=run_id, expected_head=head_sha,
                    researcher_confirmation=confirmation)
        self.assertFalse(run_dir.parent.exists())
        self.assertFalse(state.exists())

    def test_mac_resource_candidate_maps_to_full_sampled_pressure_policy(self) -> None:
        limits = _build_watchdog_limits(LIMITS)
        policy = H3_MACOS_RESOURCE_POLICY_CANDIDATE
        self.assertEqual(limits.memory_enforcement_backend, "MACOS_SAMPLED_PRESSURE")
        self.assertEqual(limits.max_workers, 4)
        self.assertEqual(limits.wall_seconds, 8 * 60 * 60)
        self.assertEqual(limits.cpu_seconds, 32 * 60 * 60)
        self.assertEqual(limits.aggregate_rss_bytes, 4 * 1024**3)
        self.assertEqual(limits.run_disk_bytes, 1 * 1024**3)
        self.assertEqual(limits.reserve_free_disk_bytes, 30 * 1024**3)
        self.assertEqual(limits.boot_volume_path, "/System/Volumes/Data")
        self.assertEqual(limits.minimum_boot_free_disk_bytes, 40 * 1024**3)
        self.assertEqual(limits.boot_reserve_free_disk_bytes, 30 * 1024**3)
        self.assertEqual(limits.swap_volume_path, "/System/Volumes/VM")
        self.assertEqual(limits.minimum_swap_volume_free_disk_bytes, 40 * 1024**3)
        self.assertEqual(limits.swap_volume_reserve_free_disk_bytes, 30 * 1024**3)
        self.assertEqual(limits.swap_growth_stop_bytes, 2 * 1024**3)
        self.assertEqual(limits.host_memory_free_percent_stop, 20)
        self.assertEqual(policy["reserve_breach_margin_fraction"], 0.05)
        self.assertEqual(policy["minimum_reserve_breach_margin_bytes"], 64 * 1024**2)
        self.assertTrue(limits.require_ac_power)
        self.assertTrue(limits.require_thermal_normal)
        self.assertTrue(limits.require_sleep_assertion)
        self.assertIn("NOT_RESEARCHER_APPROVED", policy["status"])
        self.assertIn("NOT_HARD", policy["memory_limit_semantics"])

    def test_mac_resource_preflight_requires_telemetry_pressure_and_space(self) -> None:
        limits = _build_watchdog_limits(LIMITS)
        disk = shutil._ntuple_diskusage(100 * 1024**3, 60 * 1024**3, 40 * 1024**3)
        with (
            patch("h3_supervised_pilot.validate_macos_sampled_backend",
                  return_value={"ac_power": True, "thermal_normal": True}),
            patch("h3_supervised_pilot.sample_host_memory_pressure",
                  return_value={"free_percent": 30, "estimated_available_bytes": 5}),
            patch("h3_supervised_pilot.shutil.disk_usage", return_value=disk),
        ):
            evidence = _preflight_macos_resources(limits, self.root)
        self.assertEqual(evidence["memory_enforcement"],
                         "MACOS_SAMPLED_PRESSURE_NOT_HARD")
        self.assertEqual(evidence["output_volume_start_minimum_bytes_exclusive"],
                         65 * 1024**3 // 2)

        with patch("h3_supervised_pilot.validate_macos_sampled_backend",
                   side_effect=WatchdogError("native state unavailable")):
            with self.assertRaisesRegex(H3PilotError, "unavailable"):
                _preflight_macos_resources(limits, self.root)
        with (
            patch("h3_supervised_pilot.validate_macos_sampled_backend", return_value={}),
            patch("h3_supervised_pilot.sample_host_memory_pressure",
                  return_value={"free_percent": 19}),
        ):
            with self.assertRaisesRegex(H3PilotError, "memory pressure"):
                _preflight_macos_resources(limits, self.root)
        low_disk = shutil._ntuple_diskusage(100 * 1024**3, 68 * 1024**3,
                                            32 * 1024**3)
        with (
            patch("h3_supervised_pilot.validate_macos_sampled_backend", return_value={}),
            patch("h3_supervised_pilot.sample_host_memory_pressure",
                  return_value={"free_percent": 50}),
            patch("h3_supervised_pilot.shutil.disk_usage", return_value=low_disk),
        ):
            with self.assertRaisesRegex(
                    H3PilotError, "preserve its reserve and full run allocation"):
                _preflight_macos_resources(limits, self.root)

    def test_mac_watchdog_stops_worker_when_pressure_telemetry_fails(self) -> None:
        limits = _build_watchdog_limits(LIMITS, test_overrides={
            "wall_seconds": 8.0, "cpu_seconds": 30.0,
            "case_seconds": 8.0, "oracle_seconds": 8.0,
            "poll_seconds": 0.05, "terminate_grace_seconds": 0.1,
        })
        state = {"swap_used_bytes": 1024, "swap_total_bytes": 4096,
                 "swap_free_bytes": 3072, "ac_power": True,
                 "thermal_normal": True, "boot_volume_free_bytes": 80 * 1024**3,
                 "swap_volume_free_bytes": 80 * 1024**3}
        actual_disk_usage = shutil.disk_usage

        def disk_usage(path):
            if str(path) in {"/System/Volumes/Data", "/System/Volumes/VM"}:
                return shutil._ntuple_diskusage(100 * 1024**3,
                                                80 * 1024**3,
                                                20 * 1024**3)
            return actual_disk_usage(path)

        with (
            patch("nc0a_watchdog.validate_macos_sampled_backend", return_value=state),
            patch("nc0a_watchdog.sample_host_memory_pressure",
                  side_effect=WatchdogError("injected host-pressure telemetry loss")),
            patch("nc0a_watchdog._start_sleep_assertion", return_value=None),
            patch("nc0a_watchdog.shutil.disk_usage", side_effect=disk_usage),
        ):
            result = self.run_case("mac-pressure-telemetry-loss", scenario="sleep",
                                   test_limits=asdict(limits))
        self.assertEqual(result["status"], "STOPPED_BY_WATCHDOG")
        self.assertEqual(result["watchdog"]["reason"],
                         "HOST_MEMORY_PRESSURE_UNAVAILABLE")

    def test_mac_watchdog_sleep_assertion_failure_kills_started_worker_group(self) -> None:
        limits = _build_watchdog_limits(LIMITS, test_overrides={
            "wall_seconds": 8.0, "cpu_seconds": 30.0,
            "case_seconds": 8.0, "oracle_seconds": 8.0,
            "poll_seconds": 0.05, "terminate_grace_seconds": 0.1,
        })
        state = {"swap_used_bytes": 1024, "swap_total_bytes": 4096,
                 "swap_free_bytes": 3072, "ac_power": True,
                 "thermal_normal": True, "boot_volume_free_bytes": 80 * 1024**3,
                 "swap_volume_free_bytes": 80 * 1024**3}
        run_dir = self.runs / "mac-sleep-assertion-failure"
        actual_disk_usage = shutil.disk_usage
        real_popen = subprocess.Popen
        captured = {}

        def disk_usage(path):
            if str(path) in {"/System/Volumes/Data", "/System/Volumes/VM"}:
                return shutil._ntuple_diskusage(100 * 1024**3,
                                                80 * 1024**3,
                                                20 * 1024**3)
            return actual_disk_usage(path)

        def fail_after_runner_is_live(_watchdog_pid, required):
            self.assertTrue(required)
            lease = run_dir / "h3-active-lease.json"
            deadline = time.monotonic() + 3
            while not lease.is_file() and time.monotonic() < deadline:
                time.sleep(0.01)
            self.assertTrue(lease.is_file(), "synthetic runner did not start")
            raise WatchdogError("injected caffeinate startup failure")

        def capture_popen(*args, **kwargs):
            proc = real_popen(*args, **kwargs)
            captured["pid"] = proc.pid
            return proc

        with (
            patch("nc0a_watchdog.validate_macos_sampled_backend", return_value=state),
            patch("nc0a_watchdog.sample_host_memory_pressure",
                  return_value={"free_percent": 50, "estimated_available_bytes": 8}),
            patch("nc0a_watchdog._start_sleep_assertion",
                  side_effect=fail_after_runner_is_live),
            patch("nc0a_watchdog.shutil.disk_usage", side_effect=disk_usage),
            patch("nc0a_watchdog.subprocess.Popen", side_effect=capture_popen),
        ):
            result = self.run_case("mac-sleep-assertion-failure", scenario="sleep",
                                   test_limits=asdict(limits))
        self.assertEqual(result["status"], "FAILED_AUDIT_OR_WATCHDOG")
        self.assertEqual(result["watchdog_exception"]["type"], "WatchdogError")
        self.assertIn("pid", captured)
        deadline = time.monotonic() + 3
        live_members = [object()]
        while live_members and time.monotonic() < deadline:
            try:
                members = sample_process_group(captured["pid"])
            except (ProcessLookupError, WatchdogError, subprocess.SubprocessError):
                members = []
            live_members = [member for member in members
                            if not member.state.startswith("Z")]
            if live_members:
                time.sleep(0.05)
        self.assertEqual(live_members, [], "worker survived sleep-assertion failure")

    def test_public_pilot_bundle_hashes_order_and_all_row_identities(self) -> None:
        pilot_path = HERE / "G0_RIKEN_H3_CALIBRATION_PILOT_2026-10-21.json"
        manifest_path = HERE / "G0_RIKEN_SOURCE_GRAPH_EXPECTED_MANIFEST_2026-10-21.json"
        with patch("h3_supervised_pilot.h3_runtime_manifest", return_value={
                "replay_environment_matches_recorded_versions_and_candidate_lock": True}):
            pilot, manifest = validate_pilot_bundle(pilot_path, manifest_path)
        self.assertEqual(len(pilot["records"]), 10)
        self.assertEqual(tuple(row["graph_id"] for row in pilot["records"]),
                         EXPECTED_GRAPH_IDS)
        self.assertEqual(pilot["source_manifest_sha256"], EXPECTED_MANIFEST_SHA256)
        self.assertEqual(len(manifest["h3_panel"]["records"]), 120)

    def test_bundle_order_or_runtime_mismatch_is_rejected_before_launch(self) -> None:
        pilot_path = HERE / "G0_RIKEN_H3_CALIBRATION_PILOT_2026-10-21.json"
        manifest_path = HERE / "G0_RIKEN_SOURCE_GRAPH_EXPECTED_MANIFEST_2026-10-21.json"
        value = json.loads(pilot_path.read_text(encoding="utf-8"))
        value["records"][0], value["records"][1] = value["records"][1], value["records"][0]
        payload = json.dumps(value, sort_keys=True, separators=(",", ":"),
                             ensure_ascii=False, allow_nan=False).encode("utf-8")
        with tempfile.TemporaryDirectory(prefix="h3-bundle-negative-") as temp:
            changed = Path(temp) / "pilot.json"
            changed.write_bytes(payload)
            changed_sha = hashlib.sha256(payload).hexdigest()
            with patch("h3_supervised_pilot.h3_runtime_manifest", return_value={
                    "replay_environment_matches_recorded_versions_and_candidate_lock": True}):
                with self.assertRaisesRegex(H3PilotError, "order or identity"):
                    validate_pilot_bundle(changed, manifest_path,
                                          expected_pilot_sha256=changed_sha)
        with patch("h3_supervised_pilot.h3_runtime_manifest", return_value={
                "replay_environment_matches_recorded_versions_and_candidate_lock": False}):
            with self.assertRaisesRegex(H3PilotError, "replay lock"):
                validate_pilot_bundle(pilot_path, manifest_path)

    def test_supervised_synthetic_rows_continue_after_first_success(self) -> None:
        result = self.run_case("ordered", rows=[{}, {}])
        self.assertEqual(result["status"], "COMPLETED", result)
        self.assertEqual(result["watchdog"]["usage"]["peak_compute_workers"], 1)
        self.assertLessEqual(result["watchdog"]["usage"]["peak_compute_workers"], 4)
        report = _verify_recovery_directory(self.runs / "ordered",
                                             host_state_dir=self.state)
        self.assertEqual(report["status"], "VERIFIED_TERMINAL")
        self.assertTrue(report["completed"])
        self.assertFalse(report["resume_allowed"])
        evidence = self.runs / "ordered" / "h3-evidence.jsonl"
        count, tip = verify_hash_chain(evidence)
        self.assertEqual(tip, result["evidence_tip_sha256"])
        events = [json.loads(line)["event"] for line in evidence.read_text().splitlines()]
        graph_rows = [event for event in events if event.get("kind") == "graph_result"]
        self.assertEqual([event["pilot_order"] for event in graph_rows], [1, 2])
        self.assertEqual([event["source_graph_identity"] for event in graph_rows],
                         ["PASS", "PASS"])
        self.assertEqual([event["historical_order_q_replay"] for event in graph_rows],
                         ["PASS", "PASS"])
        self.assertEqual(len(graph_rows[0]["historical_order_trial_q_abs_deltas"]), 200)
        self.assertEqual(len(graph_rows[0]["sorted_order_trial_q_abs_deltas"]), 200)
        self.assertGreater(count, 3)

    def test_historical_q_failure_stops_before_next_fixed_row(self) -> None:
        result = self.run_case("history-fail", rows=[{"historical_mismatch": True}, {}])
        self.assertEqual(result["status"], "STOPPED_ON_HISTORICAL_IDENTITY_FAILURE")
        self.assertEqual(result["failure_category"], "HISTORICAL_IDENTITY_FAILURE")
        evidence = self.runs / "history-fail" / "h3-evidence.jsonl"
        events = [json.loads(line)["event"] for line in evidence.read_text().splitlines()]
        graph_rows = [event for event in events if event.get("kind") == "graph_result"]
        self.assertEqual(len(graph_rows), 1)
        self.assertEqual(graph_rows[0]["historical_order_q_replay"], "NC-INVALID")
        self.assertFalse(result["resume_allowed"])

    def test_source_identity_failure_is_not_confused_with_executor_order(self) -> None:
        result = self.run_case("source-fail", rows=[{"source_mismatch": True}, {}])
        self.assertEqual(result["status"], "STOPPED_ON_HISTORICAL_IDENTITY_FAILURE")
        self.assertEqual(result["failure_category"], "HISTORICAL_IDENTITY_FAILURE")
        events = [json.loads(line)["event"] for line in
                  (self.runs / "source-fail" / "h3-evidence.jsonl").read_text().splitlines()]
        first = next(event for event in events if event.get("kind") == "graph_result")
        self.assertEqual(first["source_graph_identity"], "NC-INVALID")
        self.assertEqual(first["historical_order_q_replay"], "PASS")

    def test_executor_sorted_mismatch_is_diagnostic_and_does_not_stop(self) -> None:
        result = self.run_case("sorted-diagnostic", rows=[{"executor_mismatch": True}, {}])
        self.assertEqual(result["status"], "COMPLETED", result)
        events = [json.loads(line)["event"] for line in
                  (self.runs / "sorted-diagnostic" / "h3-evidence.jsonl").read_text().splitlines()]
        graph_rows = [event for event in events if event.get("kind") == "graph_result"]
        self.assertEqual(len(graph_rows), 2)
        self.assertEqual(graph_rows[0]["source_graph_identity"], "PASS")
        self.assertEqual(graph_rows[0]["historical_order_q_replay"], "PASS")
        self.assertEqual(graph_rows[0]["executor_sorted_order_compatibility"], "INCOMPATIBLE")

    def test_trial_q_tolerance_accepts_equal_absolute_boundary_only(self) -> None:
        fixture = _synthetic_row(0)
        replay = fixture["replay"]
        values = list(replay["historical_q_values"])
        values[0] = 0.0
        replay["historical_q_values"] = values
        fixture["expected"]["historical_q_vector_sha256"] = hash_float64(values)
        historical = list(replay["historical_builder_q_values"])
        historical[0] = H3_TRIAL_Q_ATOL_PROPOSED
        replay["historical_builder_q_values"] = historical
        self.assertEqual(_trial_deltas(historical, values)[0], H3_TRIAL_Q_ATOL_PROPOSED)
        at_boundary = validate_h3_replay(
            [fixture["expected"]], [replay], trial_q_atol=H3_TRIAL_Q_ATOL_PROPOSED)
        self.assertEqual(at_boundary["historical_order_q_replay"]["status"], "PASS")
        historical[0] = H3_TRIAL_Q_ATOL_PROPOSED + 1e-16
        replay["historical_builder_q_values"] = historical
        over_boundary = validate_h3_replay(
            [fixture["expected"]], [replay], trial_q_atol=H3_TRIAL_Q_ATOL_PROPOSED)
        self.assertEqual(over_boundary["historical_order_q_replay"]["status"],
                         "NC-INVALID")

    def test_watchdog_timeout_stops_process_tree_and_marks_attempt_terminal(self) -> None:
        result = self.run_case("timeout", scenario="sleep", test_limits={
            "wall_seconds": 0.5, "cpu_seconds": 30.0,
            "case_seconds": 0.5, "oracle_seconds": 0.5,
            "poll_seconds": 0.05,
        })
        self.assertEqual(result["status"], "STOPPED_BY_WATCHDOG")
        self.assertIn(result["watchdog"]["reason"], {"WALL_LIMIT", "CASE_WALL_LIMIT"})
        self.assertIsNotNone(result["watchdog_audit_tip_sha256"])
        self.assertFalse(result["resume_allowed"])

    def test_watchdog_cpu_limit_is_enforced(self) -> None:
        result = self.run_case("cpu", scenario="cpu", test_limits={
            "wall_seconds": 8.0, "cpu_seconds": 0.15,
            "case_seconds": 8.0, "oracle_seconds": 8.0,
            "poll_seconds": 0.05,
        })
        self.assertEqual(result["status"], "STOPPED_BY_WATCHDOG")
        self.assertIn(result["watchdog"]["reason"],
                      {"CPU_LIMIT_WITH_TERMINATION_MARGIN", "WALL_LIMIT"})

    def test_watchdog_sampled_rss_limit_stops_allocating_child(self) -> None:
        result = self.run_case("rss", scenario="memory", test_limits={
            "wall_seconds": 10.0, "cpu_seconds": 30.0,
            "aggregate_rss_bytes": 96 * 1024**2,
            "case_seconds": 10.0, "oracle_seconds": 10.0,
            "poll_seconds": 0.05,
        })
        self.assertEqual(result["status"], "STOPPED_BY_WATCHDOG")
        self.assertIn(result["watchdog"]["reason"], {"AGGREGATE_RSS_LIMIT", "CPU_LIMIT_WITH_TERMINATION_MARGIN"})
        self.assertEqual(result["memory_limit_semantics"], "4_GIB_RSS_SAMPLED_NOT_HARD")

    def test_watchdog_disk_limit_stops_streaming_child(self) -> None:
        result = self.run_case("disk", scenario="disk", test_limits={
            "wall_seconds": 10.0, "cpu_seconds": 30.0,
            "run_disk_bytes": 4 * 1024**2,
            "case_seconds": 10.0, "oracle_seconds": 10.0,
            "poll_seconds": 0.05,
        })
        self.assertEqual(result["status"], "STOPPED_BY_WATCHDOG")
        self.assertEqual(result["watchdog"]["reason"], "RUN_DISK_ALLOCATION_LIMIT")

    def test_child_process_nonzero_exit_is_operational_and_not_retried(self) -> None:
        result = self.run_case("child-exit", scenario="child_exit")
        self.assertEqual(result["status"], "FAILED_RUNNER_EXIT")
        self.assertEqual(result["failure_category"], "OPERATIONAL_FAILURE")
        with self.assertRaisesRegex(H3PilotError, "already has a recorded attempt"):
            self.run_case("child-exit-again", scenario="child_exit",
                          pilot_sha256=result["pilot_sha256"])

    def test_host_lock_rejects_concurrent_launch(self) -> None:
        from h3_supervised_pilot import _host_lock
        with _host_lock(self.state):
            with self.assertRaisesRegex(H3PilotError, "host lock"):
                self.run_case("second", rows=[{}])

    def test_other_watchdog_activity_cannot_bypass_host_worker_lock(self) -> None:
        from h3_supervised_pilot import _host_lock
        limits = WatchdogLimits(
            wall_seconds=2, cpu_seconds=2, aggregate_rss_bytes=64 * 1024**2,
            max_workers=4, run_disk_bytes=1024**2, reserve_free_disk_bytes=1,
            case_seconds=2, oracle_seconds=2, poll_seconds=0.05)
        with _host_lock(self.state):
            with self.assertRaisesRegex(WatchdogError, "host lock"):
                supervise([sys.executable, "-c", "pass"],
                          run_dir=self.root / "blocked-watchdog", limits=limits)

    def test_partial_activity_ledger_fails_closed_and_recovery_is_audit_only(self) -> None:
        self.state.mkdir(parents=True)
        with HashChainLog(self.state / _HOST_LEDGER) as ledger:
            ledger.append({"kind": "activity_started", "run_id": "prior",
                           "pilot_sha256": "f" * 64,
                           "run_directory": str(self.runs / "prior")})
        with self.assertRaisesRegex(H3PilotError, "no terminal record"):
            self.run_case("new-after-partial", rows=[{}])
        incomplete = self.runs / "recover-me"
        incomplete.mkdir(parents=True)
        with HashChainLog(incomplete / "h3-control.jsonl") as control:
            control.append({"kind": "activity_started", "run_id": "partial"})
        report = _verify_recovery_directory(incomplete, host_state_dir=self.state)
        self.assertEqual(report["status"], "INCOMPLETE_NOT_RESUMABLE")
        self.assertFalse(report["resume_allowed"])

    def test_corrupt_audit_suffix_is_rejected_during_recovery_inspection(self) -> None:
        self.run_case("tamper", rows=[{}])
        evidence = self.runs / "tamper" / "h3-evidence.jsonl"
        evidence.write_bytes(evidence.read_bytes() + b"{}\n")
        with self.assertRaises((H3PilotError, WatchdogError)):
            _verify_recovery_directory(self.runs / "tamper",
                                       host_state_dir=self.state)

    def test_valid_hash_prefix_without_last_evidence_event_is_not_terminal(self) -> None:
        self.run_case("evidence-prefix", rows=[{}])
        evidence = self.runs / "evidence-prefix" / "h3-evidence.jsonl"
        lines = evidence.read_bytes().splitlines(keepends=True)
        evidence.write_bytes(b"".join(lines[:-1]))
        with self.assertRaisesRegex(H3PilotError, "tip differs"):
            _verify_recovery_directory(self.runs / "evidence-prefix",
                                       host_state_dir=self.state)

    def test_stdout_tampering_is_rejected_even_when_watchdog_chain_is_valid(self) -> None:
        self.run_case("stdout-tamper", rows=[{}])
        stdout = self.runs / "stdout-tamper" / "runner.stdout.log"
        stdout.write_bytes(stdout.read_bytes() + b"changed after supervision")
        with self.assertRaisesRegex(H3PilotError, "stdout"):
            _verify_recovery_directory(self.runs / "stdout-tamper",
                                       host_state_dir=self.state)

    def test_control_log_suffix_loss_is_not_accepted_as_terminal(self) -> None:
        self.run_case("truncated-control", rows=[{}])
        control = self.runs / "truncated-control" / "h3-control.jsonl"
        control.write_bytes(control.read_bytes().splitlines(keepends=True)[0])
        with self.assertRaisesRegex(H3PilotError, "summary|closed"):
            _verify_recovery_directory(self.runs / "truncated-control",
                                       host_state_dir=self.state)

    def test_watchdog_parent_crash_kills_runner_and_blocks_automatic_recovery(self) -> None:
        run_dir = self.runs / "watchdog-parent-crash"
        code = (
            "import sys; from pathlib import Path; "
            "from h3_supervised_pilot import launch_synthetic_test; "
            "launch_synthetic_test(run_dir=Path(sys.argv[1]), "
            "state_dir=Path(sys.argv[2]), scenario='sleep', "
            "test_limits={'wall_seconds': 30.0, 'cpu_seconds': 30.0, "
            "'case_seconds': 30.0, 'oracle_seconds': 30.0})"
        )
        launcher = subprocess.Popen(
            [sys.executable, "-c", code, str(run_dir), str(self.state)],
            cwd=MODULE_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        lease = run_dir / "h3-active-lease.json"
        deadline = time.monotonic() + 10
        while not lease.is_file() and time.monotonic() < deadline:
            if launcher.poll() is not None:
                self.fail("Synthetic launcher exited before creating its child lease")
            time.sleep(0.05)
        self.assertTrue(lease.is_file(), "runner lease was not created")
        group_id = int(json.loads(lease.read_text())["process_group_id"])
        launcher.kill()
        launcher.wait(timeout=5)
        deadline = time.monotonic() + 5
        live_members = [object()]
        while live_members and time.monotonic() < deadline:
            try:
                members = sample_process_group(group_id)
            except (ProcessLookupError, WatchdogError, subprocess.SubprocessError):
                members = []
            live_members = [item for item in members if not item.state.startswith("Z")]
            if live_members:
                time.sleep(0.1)
        self.assertEqual(live_members, [], "runner survived watchdog-parent death")
        report = _verify_recovery_directory(run_dir, host_state_dir=self.state)
        self.assertEqual(report["status"], "INCOMPLETE_NOT_RESUMABLE")
        with self.assertRaisesRegex(H3PilotError, "no terminal record"):
            self.run_case("no-recovery-after-parent-crash", rows=[{}])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
