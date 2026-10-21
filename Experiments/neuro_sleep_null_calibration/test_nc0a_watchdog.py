"""Real process-group stop tests against tiny helper processes only."""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from unittest import mock

from nc0a_watchdog import (
    ProcessUsage, WatchdogLimits, classify_process_group, parse_ps_time,
    parse_macos_swap_state, parse_macos_swap_used_bytes,
    read_process_role_registry, sample_process_group, supervise,
    verify_hash_chain,
)


def limits(**overrides):
    values = dict(wall_seconds=20, cpu_seconds=1000,
                  aggregate_rss_bytes=1_000_000_000, max_workers=2,
                  run_disk_bytes=64 * 1024 * 1024,
                  reserve_free_disk_bytes=1,
                  case_seconds=10, oracle_seconds=5,
                  poll_seconds=0.05, suspend_tolerance_seconds=1,
                  terminate_grace_seconds=0.1)
    values.update(overrides)
    return WatchdogLimits(**values)


class WatchdogTests(unittest.TestCase):
    def test_darwin_collapsed_titles_require_current_process_role_registry(self):
        runner_pid = 100
        marker = ProcessUsage(
            201, runner_pid, runner_pid, 10, 0.1, "S",
            "/python -c from multiprocessing.spawn import spawn_main; "
            "spawn_main(tracker_fd=11, pipe_handle=19) --multiprocessing-fork")
        transition = ProcessUsage(201, runner_pid, runner_pid, 10, 0.1,
                                  "S", "(Python)")
        unrelated = ProcessUsage(202, runner_pid, runner_pid, 10, 0.1,
                                 "S", "(Python)")
        with mock.patch("nc0a_watchdog.sys.platform", "darwin"):
            first = classify_process_group([marker], runner_pid)
            self.assertEqual(first["worker_pids"], [201])
            self.assertEqual(first["pending_pids"], [])

            # A bare title has no role until the exact PID is published by the
            # current runner. New PIDs and changed ancestry remain unknown.
            pending = classify_process_group([transition], runner_pid)
            self.assertEqual(pending["pending_pids"], [201])
            self.assertEqual(pending["worker_pids"], [])
            registered = classify_process_group(
                [transition], runner_pid, {201: "compute_worker"})
            self.assertEqual(registered["worker_pids"], [201])
            self.assertEqual(registered["unknown_pids"], [])
            self.assertEqual(classify_process_group(
                [unrelated], runner_pid, {201: "compute_worker"}
            )["pending_pids"], [202])
            self.assertEqual(classify_process_group(
                [unrelated], runner_pid, {202: "compute_worker"}
            )["worker_pids"], [202])
            changed_parent = ProcessUsage(201, 999, runner_pid, 10, 0.1,
                                          "S", "(Python)")
            self.assertEqual(classify_process_group(
                [changed_parent], runner_pid, {201: "compute_worker"}
            )["unknown_pids"], [201])

    def test_role_registry_is_bound_to_run_token_and_runner_identity(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "roles.json"
            path.write_text(json.dumps({
                "format": "NC0A_PROCESS_ROLE_REGISTRY_V1",
                "launch_token": "a" * 64,
                "runner_pid": 100,
                "roles": {"201": "compute_worker"},
            }))
            self.assertEqual(read_process_role_registry(path, "a" * 64, 100),
                             {201: "compute_worker"})
            with self.assertRaisesRegex(Exception, "identity"):
                read_process_role_registry(path, "b" * 64, 100)

    def test_darwin_bsd_ps_time_parser(self):
        self.assertAlmostEqual(parse_ps_time("00:00.32"), 0.32)
        self.assertEqual(parse_ps_time("01:02:03"), 3723)
        self.assertEqual(parse_ps_time("2-01:02:03"), 176523)
        self.assertAlmostEqual(parse_ps_time("318:13.09"), 19093.09)

    def test_mac_swap_usage_parser(self):
        sample = "vm.swapusage: total = 12288.00M used = 11501.38M free = 786.62M (encrypted)"
        self.assertEqual(parse_macos_swap_used_bytes(sample), int(11501.38 * 1024**2))
        self.assertEqual(parse_macos_swap_state(sample), {
            "total_bytes": int(12288.00 * 1024**2),
            "used_bytes": int(11501.38 * 1024**2),
            "free_bytes": int(786.62 * 1024**2),
        })

    @unittest.skipUnless(sys.platform == "darwin", "requires real macOS native telemetry")
    def test_macos_sampled_pressure_backend_runs_protected_toy_and_records_limits(self):
        native_limits = limits(
            wall_seconds=20, cpu_seconds=120, aggregate_rss_bytes=2 * 1024**3,
            max_workers=4, reserve_free_disk_bytes=1024,
            memory_enforcement_backend="MACOS_SAMPLED_PRESSURE",
            host_memory_free_percent_stop=10,
            boot_volume_path="/System/Volumes/Data",
            boot_reserve_free_disk_bytes=10 * 1024**3,
            minimum_boot_free_disk_bytes=20 * 1024**3,
            swap_growth_stop_bytes=4 * 1024**3,
            swap_free_stop_bytes=512 * 1024,
            minimum_swap_free_bytes=1024 * 1024,
            require_ac_power=True, require_thermal_normal=True,
            require_sleep_assertion=True)
        with tempfile.TemporaryDirectory() as tmp:
            result = supervise([sys.executable, "-c", "print('bounded-macos-watchdog-ok')"],
                               run_dir=tmp, limits=native_limits)
        self.assertEqual(result["status"], "completed", result)
        usage = result["usage"]
        self.assertEqual(usage["memory_enforcement"],
                         "MACOS_SAMPLED_PRESSURE_NOT_HARD")
        self.assertEqual(usage["sleep_assertion"], "CAFFEINATE_ACTIVE")
        self.assertGreater(usage["boot_volume_free_bytes_min"], 0)
        self.assertGreater(usage["swap_used_bytes_initial"], 0)
        self.assertGreater(usage["swap_free_bytes_min_sampled"], 0)
        self.assertIn("ac_power", usage["macos_native_state"])
        self.assertTrue(usage["macos_native_state"]["thermal_normal"])

    @unittest.skipUnless(sys.platform == "darwin", "requires macOS preflight semantics")
    def test_macos_backend_rejects_low_swap_free_headroom_before_start(self):
        from nc0a_watchdog import validate_macos_sampled_backend
        native = {"swap_total_bytes": 12 * 1024**3,
                  "swap_used_bytes": 11 * 1024**3,
                  "swap_free_bytes": 256 * 1024**2,
                  "ac_power": True, "thermal_normal": True,
                  "thermal_warning_level": 0, "performance_warning_level": 0}
        values = limits(
            memory_enforcement_backend="MACOS_SAMPLED_PRESSURE",
            max_workers=4, host_memory_free_percent_stop=20,
            boot_volume_path="/System/Volumes/Data",
            boot_reserve_free_disk_bytes=10 * 1024**3,
            minimum_boot_free_disk_bytes=20 * 1024**3,
            swap_growth_stop_bytes=2 * 1024**3,
            swap_free_stop_bytes=512 * 1024**2,
            minimum_swap_free_bytes=1024**3,
            require_ac_power=True, require_thermal_normal=True,
            require_sleep_assertion=True)
        with mock.patch("nc0a_watchdog.sample_macos_native_state", return_value=native):
            with self.assertRaisesRegex(Exception, "swap free-space launch minimum"):
                validate_macos_sampled_backend(values)

    @unittest.skipUnless(sys.platform == "darwin", "requires macOS V3 preflight semantics")
    def test_macos_v3_uses_swap_growth_and_vm_volume_without_free_swap_gate(self):
        from nc0a_watchdog import validate_macos_sampled_backend
        from types import SimpleNamespace
        native = {"swap_total_bytes": 12 * 1024**3,
                  "swap_used_bytes": 11 * 1024**3,
                  "swap_free_bytes": 256 * 1024**2,
                  "ac_power": True, "thermal_normal": True,
                  "thermal_warning_level": 0, "performance_warning_level": 0}
        values = limits(
            memory_enforcement_backend="MACOS_SAMPLED_PRESSURE",
            max_workers=4, host_memory_free_percent_stop=20,
            boot_volume_path="/System/Volumes/Data",
            boot_reserve_free_disk_bytes=30 * 1024**3,
            minimum_boot_free_disk_bytes=40 * 1024**3,
            swap_volume_path="/System/Volumes/VM",
            swap_volume_reserve_free_disk_bytes=30 * 1024**3,
            minimum_swap_volume_free_disk_bytes=40 * 1024**3,
            swap_growth_stop_bytes=2 * 1024**3,
            require_ac_power=True, require_thermal_normal=True,
            require_sleep_assertion=True)
        original = shutil.disk_usage
        with mock.patch("nc0a_watchdog.sample_macos_native_state", return_value=native), \
             mock.patch("nc0a_watchdog.shutil.disk_usage",
                        side_effect=lambda path: SimpleNamespace(free=50 * 1024**3)
                        if str(path) in ("/System/Volumes/Data", "/System/Volumes/VM")
                        else original(path)):
            result = validate_macos_sampled_backend(values)
        self.assertEqual(result["swap_free_bytes"], 256 * 1024**2)
        self.assertEqual(result["swap_volume_free_bytes"], 50 * 1024**3)

    @unittest.skipUnless(sys.platform == "darwin", "requires macOS VM-volume monitoring")
    def test_macos_v3_vm_volume_reserve_breach_kills_process_group(self):
        from types import SimpleNamespace
        normal = {"swap_total_bytes": 12 * 1024**3,
                  "swap_used_bytes": 1 * 1024**3,
                  "swap_free_bytes": 11 * 1024**3,
                  "ac_power": True, "thermal_normal": True,
                  "thermal_warning_level": 0, "performance_warning_level": 0}
        native_limits = limits(
            wall_seconds=15, cpu_seconds=120, aggregate_rss_bytes=2 * 1024**3,
            max_workers=4, memory_enforcement_backend="MACOS_SAMPLED_PRESSURE",
            host_memory_free_percent_stop=10,
            boot_volume_path="/System/Volumes/Data",
            boot_reserve_free_disk_bytes=10 * 1024**3,
            minimum_boot_free_disk_bytes=20 * 1024**3,
            swap_volume_path="/System/Volumes/VM",
            swap_volume_reserve_free_disk_bytes=10 * 1024**3,
            minimum_swap_volume_free_disk_bytes=20 * 1024**3,
            swap_growth_stop_bytes=4 * 1024**3,
            require_ac_power=True, require_thermal_normal=True,
            require_sleep_assertion=True)
        original = shutil.disk_usage
        calls = {"vm": 0}

        def disk_usage(path):
            if str(path) == "/System/Volumes/Data":
                return SimpleNamespace(free=40 * 1024**3)
            if str(path) == "/System/Volumes/VM":
                calls["vm"] += 1
                free = 40 * 1024**3 if calls["vm"] <= 1 else 9 * 1024**3
                return SimpleNamespace(free=free)
            return original(path)

        with tempfile.TemporaryDirectory() as tmp, \
             mock.patch("nc0a_watchdog.sample_macos_native_state", return_value=normal), \
             mock.patch("nc0a_watchdog.shutil.disk_usage", side_effect=disk_usage):
            result = supervise([sys.executable, "-c", "import time; time.sleep(20)"],
                               run_dir=tmp, limits=native_limits)
        self.assertEqual(result["status"], "stopped")
        self.assertEqual(result["reason"], "VM_VOLUME_FREE_DISK_RESERVE_BREACH")
        self.assertGreaterEqual(calls["vm"], 2)

    @unittest.skipUnless(sys.platform == "darwin", "requires macOS Watchdog execution")
    def test_macos_swap_free_reserve_breach_kills_the_process_group(self):
        normal = {"swap_total_bytes": 12 * 1024**3,
                  "swap_used_bytes": 11 * 1024**3,
                  "swap_free_bytes": 10 * 1024**2,
                  "ac_power": True, "thermal_normal": True,
                  "thermal_warning_level": 0, "performance_warning_level": 0}
        low = {**normal, "swap_free_bytes": 256 * 1024}
        native_limits = limits(
            wall_seconds=15, cpu_seconds=120, aggregate_rss_bytes=2 * 1024**3,
            max_workers=4, memory_enforcement_backend="MACOS_SAMPLED_PRESSURE",
            host_memory_free_percent_stop=10,
            boot_volume_path="/System/Volumes/Data",
            boot_reserve_free_disk_bytes=10 * 1024**3,
            minimum_boot_free_disk_bytes=20 * 1024**3,
            swap_growth_stop_bytes=4 * 1024**3,
            swap_free_stop_bytes=512 * 1024,
            minimum_swap_free_bytes=1024 * 1024,
            require_ac_power=True, require_thermal_normal=True,
            require_sleep_assertion=True)
        with tempfile.TemporaryDirectory() as tmp, \
             mock.patch("nc0a_watchdog.sample_macos_native_state",
                        side_effect=[normal, low]):
            result = supervise([sys.executable, "-c", "import time; time.sleep(20)"],
                               run_dir=tmp, limits=native_limits)
        self.assertEqual(result["status"], "stopped")
        self.assertEqual(result["reason"], "SWAP_FREE_RESERVE_BREACH")

    def test_normal_exit_records_hash_chained_usage(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = supervise([sys.executable, "-c", "import time; time.sleep(.12)"],
                               run_dir=tmp, limits=limits())
            self.assertEqual(result["status"], "completed")
            self.assertEqual(result["returncode"], 0)
            self.assertGreaterEqual(result["usage"]["wall_seconds"], 0.08)
            self.assertTrue(result["usage"]["cpu_accounting"])
            self.assertGreater(verify_hash_chain(Path(tmp) / "watchdog.jsonl")[0], 1)

    def test_abnormal_main_exit_is_recorded_as_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = supervise([sys.executable, "-c", "raise SystemExit(17)"],
                               run_dir=tmp, limits=limits())
            self.assertEqual(result["status"], "failed")
            self.assertEqual(result["returncode"], 17)

    def test_cpu_limit_kills_entire_process_group(self):
        with tempfile.TemporaryDirectory() as tmp:
            code = "import os; open('main.pid','w').write(str(os.getpid())); x=0; " \
                   "exec('while True: x += 1')"
            result = supervise([sys.executable, "-c", code], run_dir=tmp,
                               limits=limits(cpu_seconds=0.2))
            self.assertEqual(result["status"], "stopped")
            self.assertEqual(result["reason"], "CPU_LIMIT_WITH_TERMINATION_MARGIN")
            pid = int((Path(tmp) / "main.pid").read_text())
            with self.assertRaises(ProcessLookupError):
                os.kill(pid, 0)

    def test_memory_limit_kills_process(self):
        with tempfile.TemporaryDirectory() as tmp:
            code = (
                "import os,time; x=bytearray(80*1024*1024); "
                "[x.__setitem__(i,1) for i in range(0,len(x),4096)]; "
                "open('main.pid','w').write(str(os.getpid())); time.sleep(20)"
            )
            result = supervise([sys.executable, "-c", code], run_dir=tmp,
                               limits=limits(aggregate_rss_bytes=48 * 1024 * 1024))
            self.assertEqual(result["status"], "stopped")
            self.assertEqual(result["reason"], "AGGREGATE_RSS_LIMIT")

    def test_short_lived_memory_peak_is_never_reported_as_a_hard_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            marker = root / "first-sample-complete"
            peak_file = root / "child-peak-rss.txt"
            release = root / "release-after-peak"
            code = (
                "import os,resource,sys,time; from pathlib import Path; "
                f"marker=Path({str(marker)!r}); peak=Path({str(peak_file)!r}); "
                f"release=Path({str(release)!r}); "
                "deadline=time.monotonic()+5; "
                "exec('while not marker.exists() and time.monotonic()<deadline: time.sleep(.001)'); "
                "x=bytearray(120*1024*1024); x[::4096]=b'x'*(len(x)//4096); "
                "peak.write_text(str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)); "
                "deadline=time.monotonic()+5; "
                "exec('while not release.exists() and time.monotonic()<deadline: time.sleep(.001)'); "
            )

            def first_sample_then_release(pgid):
                samples = sample_process_group(pgid)
                if any(proc.pid == pgid for proc in samples) and not marker.exists():
                    marker.write_text("sampled")
                    # Freeze this sample while the child creates a known short
                    # high-water event, then let it exit before the next sample.
                    # This removes scheduler-speed dependence from a test whose
                    # contract is only that sampled RSS is not called a hard cap.
                    deadline = time.monotonic() + 5
                    while not peak_file.exists() and time.monotonic() < deadline:
                        time.sleep(0.001)
                    if peak_file.exists():
                        release.write_text("release")
                return samples

            result = supervise([sys.executable, "-c", code], run_dir=root,
                               sampler=first_sample_then_release,
                               limits=limits(aggregate_rss_bytes=64 * 1024 * 1024))
            observed_peak = int(peak_file.read_text())
            peak_bytes = observed_peak if sys.platform == "darwin" else observed_peak * 1024
            self.assertGreater(peak_bytes, 100 * 1024 * 1024)
            self.assertEqual(result["usage"]["memory_enforcement"],
                             "SAMPLED_ONLY_NOT_HARD")
            # Sampling may miss the transient; the result must still state that
            # no OS hard limit was enforced. Depending on scheduler timing, the
            # allocation may be sampled before the short-lived child exits. In
            # that case the sampled policy must stop the group; otherwise this
            # test demonstrates the documented sampling gap. Formal policy
            # rejects this backend either way.
            sampled_peak = result["usage"]["peak_aggregate_rss_bytes"]
            if sampled_peak >= 64 * 1024 * 1024:
                self.assertEqual(result["status"], "stopped")
                self.assertEqual(result["reason"], "AGGREGATE_RSS_LIMIT")
            else:
                self.assertEqual(result["status"], "completed")

    def test_disk_allocation_limit_kills_writer_and_logs_stop(self):
        with tempfile.TemporaryDirectory() as tmp:
            code = (
                "import os,time; f=open('large.bin','wb',buffering=0); "
                "open('main.pid','w').write(str(os.getpid())); "
                "chunk=b'x'*32768; "
                "exec('while True: f.write(chunk)')"
            )
            result = supervise([sys.executable, "-c", code], run_dir=tmp,
                               limits=limits(run_disk_bytes=96 * 1024))
            self.assertEqual(result["status"], "stopped")
            self.assertEqual(result["reason"], "RUN_DISK_ALLOCATION_LIMIT")
            self.assertGreater(verify_hash_chain(Path(tmp) / "watchdog.jsonl")[0], 1)

    def test_free_disk_reserve_breach_kills_runner(self):
        from unittest import mock
        with tempfile.TemporaryDirectory() as tmp:
            real = shutil.disk_usage(tmp)
            no_free_space = type(real)(real.total, real.used, 0)
            with mock.patch("nc0a_watchdog.shutil.disk_usage", return_value=no_free_space):
                result = supervise([sys.executable, "-c", "import time; time.sleep(20)"],
                                   run_dir=tmp,
                                   limits=limits(reserve_free_disk_bytes=1024))
            self.assertEqual(result["status"], "stopped")
            self.assertEqual(result["reason"], "FREE_DISK_RESERVE_BREACH")

    def test_wall_limit_counts_elapsed_sleep_time(self):
        with tempfile.TemporaryDirectory() as tmp:
            value = [1000.0, 100.0]
            def fake_clock():
                return value[0], value[1]
            def fake_sleep(_seconds):
                value[0] += 6.0
                value[1] += 6.0
            result = supervise([sys.executable, "-c", "import time; time.sleep(20)"],
                               run_dir=tmp,
                               limits=limits(wall_seconds=5, suspend_tolerance_seconds=1),
                               clock=fake_clock, sleeper=fake_sleep)
            self.assertEqual(result["status"], "stopped")
            self.assertEqual(result["reason"], "WALL_LIMIT")

    def test_runner_exit_with_live_worker_is_killed_as_orphan(self):
        with tempfile.TemporaryDirectory() as tmp:
            code = (
                "import subprocess,sys; "
                "p=subprocess.Popen([sys.executable,'-c',"
                "'import os,time; open(\"child.pid\",\"w\").write(str(os.getpid())); time.sleep(20)']); "
                "open('worker.pid','w').write(str(p.pid))"
            )
            result = supervise([sys.executable, "-c", code], run_dir=tmp,
                               limits=limits())
            self.assertEqual(result["status"], "stopped")
            self.assertIn(result["reason"], (
                "ORPHANED_PROCESS_GROUP_AFTER_RUNNER_EXIT",
                "UNKNOWN_PROCESS_GROUP_MEMBER"))
            child_pid = int((Path(tmp) / "worker.pid").read_text())
            if result["reason"] == "UNKNOWN_PROCESS_GROUP_MEMBER":
                self.assertTrue(any(
                    row["pid"] == child_pid
                    for row in result["usage"]["unexpected_processes"]))
            try:
                os.kill(child_pid, 0)
            except ProcessLookupError:
                pass
            else:
                # Some hosts keep a killed child as a zombie briefly; it must
                # no longer be runnable even if init has not reaped it yet.
                state = subprocess.run(["/bin/ps", "-o", "stat=", "-p", str(child_pid)],
                                       capture_output=True, text=True).stdout.strip()
                self.assertTrue(not state or state.startswith("Z"), state)

    def test_watchdog_parent_loss_kills_runner_and_its_worker_group(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            supervisor = root / "supervisor.py"
            runner_pid_file = root / "runner.pid"
            worker_pid_file = root / "worker.pid"
            runner_code = (
                "import os,subprocess,time; from pathlib import Path; "
                "from nc0a_watchdog import guard_watchdog_parent; "
                "guard_watchdog_parent(os.getppid(),poll_seconds=.05,"
                "terminate_grace_seconds=.15); "
                "p=subprocess.Popen(['/bin/sleep','60']); "
                f"Path({str(worker_pid_file)!r}).write_text(str(p.pid)); "
                "time.sleep(60)"
            )
            supervisor.write_text(
                "import subprocess,sys; from pathlib import Path; "
                f"p=subprocess.Popen([sys.executable,'-c',{runner_code!r}],"
                "start_new_session=True); "
                f"Path({str(runner_pid_file)!r}).write_text(str(p.pid)); "
                "p.wait()"
            )
            env = os.environ.copy()
            module_dir = str(Path(__file__).resolve().parent)
            env["PYTHONPATH"] = module_dir + os.pathsep + env.get("PYTHONPATH", "")
            monitor = subprocess.Popen([sys.executable, str(supervisor)], env=env)
            runner_pid = worker_pid = None
            try:
                deadline = time.monotonic() + 5
                while time.monotonic() < deadline:
                    if runner_pid_file.exists() and worker_pid_file.exists():
                        runner_pid = int(runner_pid_file.read_text())
                        worker_pid = int(worker_pid_file.read_text())
                        break
                    time.sleep(0.02)
                self.assertIsNotNone(runner_pid, "runner did not start")
                self.assertIsNotNone(worker_pid, "worker did not start")
                monitor.kill()  # simulate SIGKILL of the external watchdog
                monitor.wait(timeout=2)

                def runnable(pid: int) -> bool:
                    result = subprocess.run(["/bin/ps", "-o", "stat=", "-p", str(pid)],
                                            capture_output=True, text=True)
                    state = result.stdout.strip()
                    return bool(state) and not state.startswith("Z")

                deadline = time.monotonic() + 5
                while time.monotonic() < deadline and (
                        runnable(runner_pid) or runnable(worker_pid)):
                    time.sleep(0.05)
                self.assertFalse(runnable(runner_pid), "runner survived watchdog loss")
                self.assertFalse(runnable(worker_pid), "worker survived watchdog loss")
            finally:
                if monitor.poll() is None:
                    monitor.kill()
                    monitor.wait()
                if runner_pid is not None:
                    try:
                        os.killpg(runner_pid, 9)
                    except ProcessLookupError:
                        pass

    def test_wall_clock_discontinuity_is_a_stop_and_kills_runner(self):
        with tempfile.TemporaryDirectory() as tmp:
            value = [1000.0, 100.0]
            def fake_clock():
                return value[0], value[1]
            def fake_sleep(seconds):
                value[0] += 1.0
                value[1] += 0.1
            result = supervise([sys.executable, "-c", "import time; time.sleep(20)"],
                               run_dir=tmp,
                               limits=limits(suspend_tolerance_seconds=0.2),
                               clock=fake_clock, sleeper=fake_sleep)
            self.assertEqual(result["status"], "stopped")
            self.assertEqual(result["reason"], "SUSPEND_OR_CLOCK_ANOMALY")

    def test_audit_partial_tail_cannot_be_resumed(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "watchdog.jsonl"
            path.write_text('{"partial":')
            with self.assertRaises(Exception):
                verify_hash_chain(path)


if __name__ == "__main__":
    unittest.main()
