"""Bounded synthetic tests for the external-volume storage adapter."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import sys
import subprocess
import tempfile
import time
import unittest
import uuid
from concurrent.futures import ThreadPoolExecutor
from types import SimpleNamespace
from unittest import mock

from g0_external_storage import (
    ExternalStoragePolicy, G0ExternalStore, G0StorageError, RecoveryRefused,
    VolumeInfo,
)
from nc0a_watchdog import WatchdogLimits, verify_hash_chain


EXPECTED_UUID = "0E5DC84B-1E22-3C9B-9E3B-220EBA8607C1"
OTHER_UUID = "11111111-2222-3333-4444-555555555555"
RUN_UUID = "aaaaaaaa-bbbb-4ccc-8ddd-eeeeeeeeeeee"
SEED_FINGERPRINT = hashlib.sha256(b"engineering-only-seed").hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def write_synthetic_task_history(ledger_dir: Path, task_count: int) -> dict[str, str]:
    """Create a valid authoritative hash chain without thousands of fsyncs."""
    ledger_dir.mkdir(parents=True, exist_ok=True)
    ledger_path = ledger_dir / "storage-ledger.jsonl"
    previous = "0" * 64
    sequence = 0
    lines = []
    expected = {}
    for index in range(task_count):
        task_id = f"task-{index:05d}"
        attempt_id = str(uuid.UUID(int=index + 1))
        expected[task_id] = SEED_FINGERPRINT
        events = (
            {"event": "g0_task_started", "task_id": task_id,
             "attempt_id": attempt_id, "seed_fingerprint": SEED_FINGERPRINT,
             "result_path": f"tasks/{task_id}/attempts/{attempt_id}/result.bin"},
            {"event": "g0_task_failed", "task_id": task_id,
             "attempt_id": attempt_id, "failure_class": "OPERATIONAL",
             "reason_code": "G0_EXTERNAL_IO_FAILURE", "reason": "synthetic probe",
             "recovery_allowed": True},
        )
        for event in events:
            payload = {"run_uuid": RUN_UUID, **event}
            record = {"sequence": sequence, "previous_sha256": previous,
                      "event": payload}
            digest = hashlib.sha256(canonical(record)).hexdigest()
            lines.append(canonical({**record, "record_sha256": digest}) + b"\n")
            sequence += 1
            previous = digest
    ledger_path.write_bytes(b"".join(lines))
    anchor = {"sequence": sequence, "tip_sha256": previous, "run_uuid": RUN_UUID}
    (ledger_dir / "storage-ledger.anchor.json").write_bytes(canonical(anchor) + b"\n")
    return expected


class FakeProbe:
    def __init__(self, external: Path, internal: Path):
        self.external = external
        self.internal = internal
        self.external_uuid = EXPECTED_UUID
        self.external_available = True
        self.external_calls = 0

    def inspect(self, mount_point):
        path = Path(mount_point)
        if path == self.external:
            self.external_calls += 1
            if not self.external_available:
                raise G0StorageError("G0_EXTERNAL_MOUNT_UNAVAILABLE", "injected mount loss")
            st = path.stat()
            return VolumeInfo(str(path), self.external_uuid, "exfat", "test-ext",
                              st.st_dev, st.st_ino, 100 * 1024**3)
        if path == self.internal:
            st = path.stat()
            return VolumeInfo(str(path), OTHER_UUID, "apfs", "test-int",
                              st.st_dev, st.st_ino, 80 * 1024**3)
        raise G0StorageError("G0_EXTERNAL_MOUNT_UNAVAILABLE", "unregistered path")


class StorageFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.external = self.root / "external"
        self.internal = self.root / "internal"
        self.external.mkdir()
        self.internal.mkdir()
        self.probe = FakeProbe(self.external, self.internal)
        self.ext_free = 100 * 1024**3
        self.int_free = 80 * 1024**3
        self.policy = ExternalStoragePolicy(
            external_mount=self.external,
            internal_mount=self.internal,
            minimum_external_start_free_bytes=50 * 1024**3,
            minimum_external_reserve_free_bytes=30 * 1024**3,
            maximum_run_bytes=1024 * 1024,
            minimum_internal_start_free_bytes=40 * 1024**3,
            minimum_internal_reserve_free_bytes=30 * 1024**3,
            run_root_relative="adapter-test/runs",
        )
        self.ledger_dir = self.internal / "control" / RUN_UUID

    def tearDown(self):
        self.temp.cleanup()

    def usage(self, path):
        return SimpleNamespace(free=self.ext_free if Path(path) == self.external else self.int_free)

    def open_store(self):
        return G0ExternalStore(run_uuid=RUN_UUID, internal_ledger_dir=self.ledger_dir,
                               policy=self.policy, probe=self.probe,
                               usage_provider=self.usage)

    @staticmethod
    def attempt(n=1):
        return str(uuid.UUID(int=n))

    def test_completed_task_reopens_with_same_uuid_hash_and_is_reused(self):
        store = self.open_store()
        result = store.write_task_result(task_id="case-001", attempt_id=self.attempt(1),
                                         seed_fingerprint=SEED_FINGERPRINT,
                                         payload=b"small synthetic output")
        self.assertEqual(result["sha256"], hashlib.sha256(b"small synthetic output").hexdigest())
        cache = store.write_immutable_artifact(
            relative_path="cache/source-001/graph.bin", artifact_kind="cache",
            identity={"source_graph_sha256": hashlib.sha256(b"source").hexdigest()},
            chunks=(piece for piece in (b"graph-", b"cache", b"-bytes")))
        audit = store.write_immutable_artifact(
            relative_path="audit/case-001/events.jsonl.gz", artifact_kind="audit",
            identity={"task_id": "case-001", "compression": "gzip-test-label"},
            chunks=b"compressed-audit-placeholder")
        self.assertEqual(cache["sha256"], hashlib.sha256(b"graph-cache-bytes").hexdigest())
        self.assertEqual(audit["size_bytes"], len(b"compressed-audit-placeholder"))
        store.close()
        resumed = self.open_store()
        with self.assertRaisesRegex(RecoveryRefused, "full recovery validation"):
            resumed.begin_task(task_id="case-003", attempt_id=self.attempt(3),
                               seed_fingerprint=SEED_FINGERPRINT)
        report = resumed.verify_recovery({"case-001": SEED_FINGERPRINT,
                                          "case-002": hashlib.sha256(b"other").hexdigest()})
        self.assertEqual(report.completed_task_ids, ("case-001",))
        self.assertEqual(report.not_started_task_ids, ("case-002",))
        with self.assertRaisesRegex(RecoveryRefused, "Completed task"):
            resumed.write_task_result(task_id="case-001", attempt_id=self.attempt(2),
                                      seed_fingerprint=SEED_FINGERPRINT, payload=b"again")
        resumed.close()

    def test_artifact_namespace_is_fixed_and_stream_content_is_hashed(self):
        store = self.open_store()
        with self.assertRaisesRegex(G0StorageError, "fixed external namespace"):
            store.write_immutable_artifact(
                relative_path="cache/payload.bin", artifact_kind="audit",
                identity={}, chunks=b"blocked")
        result = store.write_immutable_artifact(
            relative_path="checkpoints/graph-001/state.bin", artifact_kind="checkpoint",
            identity={"checkpoint": "E", "seed_fingerprint": SEED_FINGERPRINT},
            chunks=iter((b"first-", b"second-", b"third")))
        self.assertEqual(result["sha256"], hashlib.sha256(b"first-second-third").hexdigest())
        store.close()
        resumed = self.open_store()
        resumed.verify_recovery({})
        artifact = Path(self.external, "adapter-test", "runs", RUN_UUID,
                        "checkpoints/graph-001/state.bin")
        artifact.write_bytes(b"tampered")
        with self.assertRaisesRegex(RecoveryRefused, "Artifact changed"):
            resumed.verify_recovery({})
        resumed.close()

    def test_four_concurrent_synthetic_workers_keep_hash_chain_and_results_valid(self):
        store = self.open_store()
        tasks = {f"parallel-{i}": SEED_FINGERPRINT for i in range(4)}

        def write(index):
            return store.write_task_result(
                task_id=f"parallel-{index}", attempt_id=self.attempt(index + 10),
                seed_fingerprint=SEED_FINGERPRINT,
                payload=(f"synthetic-worker-{index}".encode() * 128))

        with ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(write, range(4)))
        self.assertEqual(len({item["sha256"] for item in results}), 4)
        report = store.verify_recovery(tasks)
        self.assertEqual(report.completed_task_ids, tuple(sorted(tasks)))
        count, _ = verify_hash_chain(self.ledger_dir / "storage-ledger.jsonl")
        self.assertEqual(count, 9)
        store.close()

    def test_hot_paths_do_not_rescan_100_1000_or_5000_task_histories(self):
        expected = write_synthetic_task_history(self.ledger_dir, 5000)
        store = self.open_store()
        self.assertEqual(len(store._task_event_index), 5000)
        report = store.verify_recovery(expected)
        self.assertEqual(len(report.retryable_task_ids), 5000)

        lookup_count = 0
        original_task_state = store._task_state

        def counted_lookup(task_id):
            nonlocal lookup_count
            lookup_count += 1
            return original_task_state(task_id)

        with (mock.patch.object(store, "_task_events",
                                side_effect=AssertionError("hot path rescanned ledger")),
              mock.patch.object(store, "_scan_managed_tree",
                                side_effect=AssertionError("hot path walked output tree")),
              mock.patch("g0_external_storage._tree_bytes",
                         side_effect=AssertionError("hot path counted the tree")),
              mock.patch.object(store, "_task_state", side_effect=counted_lookup)):
            for task_count in (100, 1000, 5000):
                for index in range(task_count):
                    task_id = f"task-{index:05d}"
                    state = store._task_state(task_id)
                    self.assertEqual(len(state["starts"]), 1)
                    if index == 0:
                        state["starts"].clear()
                        self.assertEqual(len(store._task_state(task_id)["starts"]), 1)
                for _ in range(5):
                    self.assertGreaterEqual(store.check_health()["external_free_bytes"], 0)
            next_attempt = self.attempt(9000)
            store.begin_task(task_id="post-index-task", attempt_id=next_attempt,
                             seed_fingerprint=SEED_FINGERPRINT)
            store.complete_task_result(task_id="post-index-task", attempt_id=next_attempt,
                                       seed_fingerprint=SEED_FINGERPRINT,
                                       payload=b"indexed task result")
            store.write_immutable_artifact(
                relative_path="cache/post-index/artifact.bin", artifact_kind="cache",
                identity={"task_id": "post-index-task"}, chunks=b"indexed artifact")
            limits = WatchdogLimits(
                wall_seconds=10, cpu_seconds=30, aggregate_rss_bytes=512 * 1024**2,
                max_workers=1, run_disk_bytes=2 * 1024**2,
                reserve_free_disk_bytes=1024, case_seconds=5, oracle_seconds=5,
                poll_seconds=0.05, suspend_tolerance_seconds=2,
                terminate_grace_seconds=0.1)
            store.supervise_worker([sys.executable, "-c", "pass"], limits=limits,
                                   invocation_id=999)
        self.assertEqual(lookup_count, 6105)
        expected["post-index-task"] = SEED_FINGERPRINT
        report = store.verify_recovery(expected)
        self.assertIn("post-index-task", report.completed_task_ids)
        store.close()

    def test_streamed_file_cannot_cross_run_byte_budget_between_watchdog_samples(self):
        from dataclasses import replace

        self.policy = replace(self.policy, maximum_run_bytes=(3 * 1024 * 1024) // 2)
        store = self.open_store()
        with self.assertRaisesRegex(G0StorageError, "Bounded external write"):
            store.write_immutable_artifact(
                relative_path="audit/large/stream.bin", artifact_kind="audit",
                identity={"task_id": "large-stream"},
                chunks=(b"x" * (8 * 1024 * 1024),))
        path = Path(self.external, "adapter-test", "runs", RUN_UUID,
                    "audit/large/stream.bin")
        self.assertEqual(path.stat().st_size, 1024 * 1024)
        self.assertLessEqual(store.check_health()["external_run_bytes"],
                             self.policy.maximum_run_bytes)
        store.close()

    def test_wrong_uuid_fails_before_creating_external_or_internal_run_paths(self):
        self.probe.external_uuid = OTHER_UUID
        with self.assertRaisesRegex(G0StorageError, "UUID or mount point"):
            self.open_store()
        self.assertFalse((self.external / "adapter-test").exists())
        self.assertFalse(self.ledger_dir.exists())

    def test_internal_control_path_symlink_is_rejected(self):
        outside = self.root / "outside-control"
        outside.mkdir()
        (self.internal / "control").symlink_to(outside, target_is_directory=True)
        with self.assertRaises(OSError):
            self.open_store()
        self.assertEqual(list(outside.iterdir()), [])

    def test_path_escape_and_symlink_redirection_are_rejected(self):
        store = self.open_store()
        with self.assertRaises(G0StorageError):
            store.begin_task(task_id="../escape", attempt_id=self.attempt(1),
                             seed_fingerprint=SEED_FINGERPRINT)
        target = self.root / "outside"
        target.mkdir()
        task_root = Path(self.external, "adapter-test", "runs", RUN_UUID, "tasks")
        task_root.mkdir()
        (task_root / "linked").symlink_to(target, target_is_directory=True)
        with self.assertRaises(G0StorageError):
            store.begin_task(task_id="linked", attempt_id=self.attempt(1),
                             seed_fingerprint=SEED_FINGERPRINT)
        store.close()

    def test_external_space_is_checked_separately_from_internal_space(self):
        store = self.open_store()
        self.ext_free = 29 * 1024**3
        self.assertEqual(store.watchdog_stop_guard(), "G0_EXTERNAL_SPACE_LIMIT")
        self.ext_free = 100 * 1024**3
        self.int_free = 29 * 1024**3
        self.assertEqual(store.watchdog_stop_guard(), "G0_INTERNAL_SPACE_LIMIT")
        store.close()

    def test_uuid_change_after_mount_fails_closed(self):
        store = self.open_store()
        self.probe.external_uuid = OTHER_UUID
        self.assertEqual(store.watchdog_stop_guard(), "G0_EXTERNAL_VOLUME_IDENTITY_MISMATCH")
        with self.assertRaises(G0StorageError):
            store.write_task_result(task_id="case-001", attempt_id=self.attempt(1),
                                    seed_fingerprint=SEED_FINGERPRINT, payload=b"blocked")
        store.close()

    def test_completed_artifact_corruption_is_not_reused(self):
        store = self.open_store()
        result = store.write_task_result(task_id="case-001", attempt_id=self.attempt(1),
                                         seed_fingerprint=SEED_FINGERPRINT,
                                         payload=b"original")
        path = Path(self.external, "adapter-test", "runs", RUN_UUID,
                    result["result_path"])
        store.close()
        path.write_bytes(b"tampered")
        with self.assertRaisesRegex(RecoveryRefused, "Committed file changed"):
            self.open_store()

    def test_unknown_file_under_run_root_is_rejected(self):
        store = self.open_store()
        store.close()
        unknown = Path(self.external, "adapter-test", "runs", RUN_UUID, "untracked.bin")
        unknown.write_bytes(b"untracked")
        with self.assertRaisesRegex(RecoveryRefused, "Untracked external files"):
            self.open_store()

    def test_scientific_and_unknown_failures_are_never_retryable(self):
        store = self.open_store()
        store.begin_task(task_id="science", attempt_id=self.attempt(1),
                         seed_fingerprint=SEED_FINGERPRINT)
        store.record_task_failure(task_id="science", attempt_id=self.attempt(1),
                                  failure_class="SCIENTIFIC", reason_code="ORACLE_MISMATCH",
                                  reason="synthetic injected disagreement")
        with self.assertRaisesRegex(RecoveryRefused, "blocks recovery"):
            store.verify_recovery({"science": SEED_FINGERPRINT})
        with self.assertRaises(RecoveryRefused):
            store.begin_task(task_id="science", attempt_id=self.attempt(2),
                             seed_fingerprint=SEED_FINGERPRINT)
        store.close()

        self.temp.cleanup()
        self.setUp()
        store = self.open_store()
        store.begin_task(task_id="unknown", attempt_id=self.attempt(1),
                         seed_fingerprint=SEED_FINGERPRINT)
        store.record_task_failure(task_id="unknown", attempt_id=self.attempt(1),
                                  failure_class="UNKNOWN", reason_code="UNCLASSIFIED",
                                  reason="injected unknown exception")
        with self.assertRaises(RecoveryRefused):
            store.verify_recovery({"unknown": SEED_FINGERPRINT})
        store.close()

    def test_operational_storage_failure_allows_only_one_same_seed_retry(self):
        store = self.open_store()
        original_open = os.open

        def fail_result_open(path, flags, *args, **kwargs):
            if path == "result.bin":
                raise OSError("injected ExFAT write-open failure")
            return original_open(path, flags, *args, **kwargs)

        with mock.patch("g0_external_storage.os.open", side_effect=fail_result_open):
            with self.assertRaisesRegex(OSError, "injected ExFAT"):
                store.write_task_result(task_id="retry", attempt_id=self.attempt(1),
                                        seed_fingerprint=SEED_FINGERPRINT, payload=b"not written")
        report = store.verify_recovery({"retry": SEED_FINGERPRINT})
        self.assertEqual(report.retryable_task_ids, ("retry",))
        store.write_task_result(task_id="retry", attempt_id=self.attempt(2),
                                seed_fingerprint=SEED_FINGERPRINT, payload=b"recovered")
        report = store.verify_recovery({"retry": SEED_FINGERPRINT})
        self.assertEqual(report.completed_task_ids, ("retry",))
        store.close()

    def test_two_operational_attempts_exhaust_retry_quota(self):
        store = self.open_store()
        for attempt in (1, 2):
            store.begin_task(task_id="limited", attempt_id=self.attempt(attempt),
                             seed_fingerprint=SEED_FINGERPRINT)
            store.record_task_failure(task_id="limited", attempt_id=self.attempt(attempt),
                                      failure_class="OPERATIONAL",
                                      reason_code="G0_EXTERNAL_IO_FAILURE", reason="injected")
        report = store.verify_recovery({"limited": SEED_FINGERPRINT})
        self.assertEqual(report.exhausted_task_ids, ("limited",))
        with self.assertRaisesRegex(RecoveryRefused, "attempt limit"):
            store.begin_task(task_id="limited", attempt_id=self.attempt(3),
                             seed_fingerprint=SEED_FINGERPRINT)
        store.close()

    def test_anchor_detects_removed_audit_suffix(self):
        store = self.open_store()
        store.write_task_result(task_id="case-001", attempt_id=self.attempt(1),
                                seed_fingerprint=SEED_FINGERPRINT, payload=b"logged")
        ledger = self.ledger_dir / "storage-ledger.jsonl"
        store.close()
        raw = ledger.read_bytes()
        ledger.write_bytes(b"".join(raw.splitlines(keepends=True)[:-1]))
        with self.assertRaises(RecoveryRefused):
            self.open_store()

    def test_stale_incremental_index_rejects_external_ledger_change(self):
        store = self.open_store()
        ledger = self.ledger_dir / "storage-ledger.jsonl"
        with ledger.open("ab") as handle:
            handle.write(b"tampered-tail\n")
            handle.flush()
            os.fsync(handle.fileno())
        with self.assertRaisesRegex(RecoveryRefused, "Ledger identity, size, change metadata or tip changed"):
            store.check_health()
        store.close()

    def test_same_size_in_place_ledger_tampering_invalidates_incremental_index(self):
        store = self.open_store()
        ledger = self.ledger_dir / "storage-ledger.jsonl"
        original = ledger.read_bytes()
        old = b"g0_external_store_opened"
        new = b"g0_external_st0re_opened"
        self.assertEqual(len(old), len(new))
        self.assertIn(old, original)
        ledger.write_bytes(original.replace(old, new, 1))
        self.assertEqual(ledger.stat().st_size, len(original))
        with self.assertRaisesRegex(RecoveryRefused, "Ledger identity, size, change metadata or tip changed"):
            store._reserve_external_write(1)
        store.close()

    def test_watchdog_stop_guard_kills_supervised_process_on_mount_loss(self):
        store = self.open_store()
        marker = self.ledger_dir / "ticks.txt"
        pid_path = self.ledger_dir / "runner.pid"
        child_pid_path = self.ledger_dir / "worker.pid"
        child_code = (
            "import os,time; from pathlib import Path; "
            f"p=Path({str(marker)!r}); Path({str(child_pid_path)!r}).write_text(str(os.getpid())); "
            "exec('while True: p.open(\"a\").write(\"x\"); time.sleep(.02)')")
        command = [sys.executable, "-c", (
            "import os,subprocess,sys,time; from pathlib import Path; "
            f"p=subprocess.Popen([sys.executable,'-c',{child_code!r}]); "
            f"Path({str(pid_path)!r}).write_text(str(os.getpid())); "
            "time.sleep(60)")]
        calls = {"count": 0}
        original_guard = store.watchdog_stop_guard

        def guard():
            calls["count"] += 1
            if calls["count"] >= 1:
                deadline = time.monotonic() + 2
                while not child_pid_path.exists() and time.monotonic() < deadline:
                    time.sleep(0.01)
                self.probe.external_available = False
            return original_guard()

        store.watchdog_stop_guard = guard
        limits = WatchdogLimits(
            wall_seconds=10, cpu_seconds=100, aggregate_rss_bytes=512 * 1024**2,
            max_workers=1, run_disk_bytes=8 * 1024**2,
            reserve_free_disk_bytes=1024, case_seconds=5, oracle_seconds=5,
            poll_seconds=0.05, suspend_tolerance_seconds=2,
            terminate_grace_seconds=0.1)
        try:
            result = store.supervise_worker(command, limits=limits, invocation_id=1)
            self.assertEqual(result["status"], "stopped", result)
            self.assertEqual(result["reason"], "G0_EXTERNAL_MOUNT_UNAVAILABLE")
            pids = (int(pid_path.read_text()), int(child_pid_path.read_text()))
            for pid in pids:
                try:
                    os.kill(pid, 0)
                except ProcessLookupError:
                    continue
                state = subprocess.run(["/bin/ps", "-o", "stat=", "-p", str(pid)],
                                       capture_output=True, text=True).stdout.strip()
                self.assertTrue(not state or state.startswith("Z"), state)
            count_at_stop = len(marker.read_text())
            time.sleep(0.1)
            self.assertEqual(len(marker.read_text()), count_at_stop)
            watchdog_log = self.ledger_dir / "watchdog.g0.1.jsonl"
            self.assertGreater(verify_hash_chain(watchdog_log)[0], 1)
        finally:
            store.watchdog_stop_guard = original_guard
        self.probe.external_available = True
        report = store.verify_recovery({})
        self.assertEqual(report.completed_task_ids, ())
        store.close()


if __name__ == "__main__":
    unittest.main()
