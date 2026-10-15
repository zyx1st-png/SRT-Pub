"""Real process-group stop tests against tiny helper processes only."""

from __future__ import annotations

import json
import os
from pathlib import Path
import resource
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

from nc0a_watchdog import (
    WatchdogLimits, parse_ps_time, sample_process_group, supervise, verify_hash_chain,
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
    def test_darwin_bsd_ps_time_parser(self):
        self.assertAlmostEqual(parse_ps_time("00:00.32"), 0.32)
        self.assertEqual(parse_ps_time("01:02:03"), 3723)
        self.assertEqual(parse_ps_time("2-01:02:03"), 176523)
        self.assertAlmostEqual(parse_ps_time("318:13.09"), 19093.09)

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
            code = (
                "import os,resource,sys,time; from pathlib import Path; "
                f"marker=Path({str(marker)!r}); peak=Path({str(peak_file)!r}); "
                "deadline=time.monotonic()+5; "
                "exec('while not marker.exists() and time.monotonic()<deadline: time.sleep(.001)'); "
                "x=bytearray(120*1024*1024); x[::4096]=b'x'*(len(x)//4096); "
                "peak.write_text(str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)); "
            )

            def first_sample_then_release(pgid):
                samples = sample_process_group(pgid)
                if any(proc.pid == pgid for proc in samples):
                    marker.write_text("sampled")
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
            # no OS hard limit was enforced. Formal policy rejects this backend.
            self.assertLess(result["usage"]["peak_aggregate_rss_bytes"],
                            64 * 1024 * 1024)

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
