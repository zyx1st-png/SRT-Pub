"""Small synthetic integration tests for the G0 executor/storage boundary."""

from __future__ import annotations

import hashlib
import json
import platform
import sys
import unittest
import uuid
from unittest import mock

from g0_external_storage import G0ExternalStore, RecoveryRefused
from g0_minimal_executor import (
    G0TaskIdentity, _audit_replay_verifier, canonical_json, g0_graph_seed,
    g0_louvain_seed, normalize_graph_input, run_synthetic_g0_activity,
    run_synthetic_g0_task,
    runtime_manifest,
)
from nc0a_watchdog import WatchdogLimits
from synthetic_graphs import make_synthetic_graph
from test_g0_external_storage import StorageFixture


ENGINEERING_ROOT = 20261021
SYNTHETIC_RUN_ID = "bbbbbbbb-cccc-4ddd-8eee-ffffffffffff"


def fixture_graph(root=ENGINEERING_ROOT, suffix=""):
    fixture = make_synthetic_graph(100, "factor-mst", root=root)
    return normalize_graph_input(
        f"SYNTHETIC_FACTOR_MST_N100_ENGINEERING_20261021{suffix}",
        tuple(range(fixture.n)), fixture.edges,
        source_artifact_sha256=fixture.fingerprint())


def fixture_identity(graph):
    return G0TaskIdentity("SYNTHETIC_ENGINEERING_RUN_20261021", graph.n,
                          0, "SYNTHETIC", 0, 0)


def small_fault_graph():
    # Dense enough for nontrivial connected swaps, but small enough that crash
    # and same-seed recovery tests exercise the real spawn boundary quickly.
    n = 12
    edges = set()
    for offset in (1, 2):
        for node in range(n):
            edges.add(tuple(sorted((node, (node + offset) % n))))
    edges.update({(0, 4), (1, 5), (3, 8), (7, 11)})
    return normalize_graph_input(
        "SYNTHETIC_SPAWN_FAILURE_N12_ENGINEERING_20261021",
        tuple(range(n)), tuple(sorted(edges)),
        source_artifact_sha256=hashlib.sha256(
            b"synthetic spawn-failure fixture 20261021").hexdigest())


def watchdog_limits(workers=4, **overrides):
    values = dict(
        wall_seconds=300, cpu_seconds=300,
        aggregate_rss_bytes=4 * 1024**3, max_workers=workers,
        run_disk_bytes=16 * 1024**2, reserve_free_disk_bytes=1024,
        case_seconds=240, oracle_seconds=240, poll_seconds=0.1,
        suspend_tolerance_seconds=3, terminate_grace_seconds=0.5,
        memory_enforcement_backend="SAMPLED_ONLY")
    values.update(overrides)
    return WatchdogLimits(**values)


class G0MinimalExecutorTests(StorageFixture):
    def open_store_for(self, run_id):
        return G0ExternalStore(
            run_uuid=run_id,
            internal_ledger_dir=self.internal / "control" / run_id,
            policy=self.policy, probe=self.probe, usage_provider=self.usage)

    def execute(self, store, *, attempt=1, invocation=1, fault=None, graph=None,
                workers=4, limits=None):
        graph = graph or fixture_graph()
        return run_synthetic_g0_task(
            store=store, graph=graph, identity=fixture_identity(graph),
            attempt_id=str(uuid.UUID(int=attempt)), invocation_id=invocation,
            limits=limits or watchdog_limits(workers=workers), workers=workers,
            require_target_runtime=False, _test_fault=fault)

    def test_target_runtime_matches_historical_versions_on_local_mac(self):
        if (sys.platform != "darwin" or platform.machine() != "arm64" or
                sys.version_info[:3] != (3, 14, 0)):
            self.skipTest("Exact G0 target-runtime verification requires the dedicated "
                          "macOS arm64 Python 3.14.0 environment")
        manifest = runtime_manifest(require_target=True)
        self.assertEqual(manifest["python"], "3.14.0")
        self.assertEqual(manifest["machine"], "arm64")
        self.assertEqual(manifest["macos_version"], "15.7.4")
        self.assertEqual(manifest["packages"]["python-louvain"], "0.16")
        self.assertEqual(manifest["packages"]["networkx"], "3.6.1")
        self.assertEqual(manifest["packages"]["numpy"], "2.5.3")
        self.assertEqual(manifest["packages"]["scipy"], "1.18.1")
        self.assertEqual(manifest["packages"]["h5py"], "3.16.0")

    def test_g0_seed_serialization_matches_fixed_dummy_identity_vectors(self):
        graph = fixture_graph()
        identity = fixture_identity(graph)
        self.assertEqual(g0_graph_seed(identity), 1126166200)
        self.assertEqual(g0_louvain_seed(identity, 0), 1635419549)
        self.assertEqual(g0_louvain_seed(identity, 199), 2045046386)

    def test_normalized_graph_rejects_identity_and_topology_corruption(self):
        with self.assertRaisesRegex(ValueError, "Duplicate node"):
            normalize_graph_input("SYNTHETIC_DUP", [0, 1, 1, 3],
                                  [(0, 1), (1, 3), (3, 0)])
        with self.assertRaisesRegex(ValueError, "Duplicate or reversed"):
            normalize_graph_input("SYNTHETIC_DUP_EDGE", [0, 1, 2, 3],
                                  [(0, 1), (1, 0), (1, 2), (2, 3)])
        with self.assertRaisesRegex(ValueError, "connected simple graph"):
            normalize_graph_input("SYNTHETIC_DISCONNECTED", [0, 1, 2, 3],
                                  [(0, 1), (2, 3)])
        with self.assertRaisesRegex(ValueError, "visibly synthetic"):
            graph = fixture_graph()
            store = self.open_store()
            try:
                run_synthetic_g0_task(
                    store=store, graph=graph,
                    identity=G0TaskIdentity("mouse01_sleep", 100, 0, "Wake", 0, 0),
                    attempt_id=str(uuid.uuid4()), invocation_id=1,
                    limits=watchdog_limits(), workers=4)
            finally:
                store.close()

    def test_synthetic_task_requires_source_artifact_hash(self):
        fixture = small_fault_graph()
        graph = normalize_graph_input(
            "SYNTHETIC_MISSING_SOURCE_HASH", fixture.nodes, fixture.edges)
        store = self.open_store()
        try:
            with self.assertRaisesRegex(ValueError, "source-artifact SHA-256"):
                self.execute(store, graph=graph)
        finally:
            store.close()

    def test_four_worker_end_to_end_4e_200_louvain_audit_and_reuse(self):
        graph = fixture_graph()
        store = self.open_store()
        report = self.execute(store)
        self.assertEqual(report["status"], "completed", report)
        result = report["result"]
        self.assertEqual(result["swap"]["attempts"], 4 * graph.m)
        self.assertGreater(result["swap"]["accepted"], 0)
        self.assertEqual(tuple(result["topology"]["degree_sequence"]),
                         graph.degree_sequence)
        self.assertEqual(result["swap"]["proposal_audit_records"], 4 * graph.m)
        self.assertEqual(result["swap"]["attempts"],
                         result["swap"]["accepted"] + result["swap"]["rejected_overlap"] +
                         result["swap"]["rejected_duplicate"] +
                         result["swap"]["rejected_disconnect"])
        self.assertEqual(result["louvain"]["trial_count"], 200)
        self.assertEqual(len(result["louvain"]["q_values"]), 200)
        self.assertEqual(report["watchdog"]["status"], "completed")
        self.assertEqual(report["watchdog"]["usage"]["peak_compute_workers"], 4)
        self.assertEqual(report["recovery_report"].completed_task_ids,
                         (report["task_id"],))

        audit_rel = result["artifacts"]["proposal_audit"]["relative_path"]
        audit_file = (self.external / self.policy.run_root_relative / store.run_uuid /
                      audit_rel)
        compressed = audit_file.read_bytes()
        replay = _audit_replay_verifier(
            graph, result["seed_manifest"]["graph_seed"], compressed,
            result["null_graph_sha256"])
        self.assertEqual(replay["proposal_count"], 4 * graph.m)
        self.assertEqual(replay["accepted"], result["swap"]["accepted"])
        self.assertEqual(replay["audit_tip_sha256"],
                         result["swap"]["proposal_audit_tip_sha256"])
        self.assertEqual(hashlib.sha256(compressed).hexdigest(),
                         result["artifacts"]["proposal_audit"]["sha256"])
        self.assertEqual(result["artifacts"]["proposal_audit"]["stream_metadata"][
            "stream_format"], "G0_GZIP_CANONICAL_JSONL_AUDIT_V1")
        stdout_path = store.control_dir / "runner.g0.1.stdout.log"
        stdout = stdout_path.read_bytes()
        self.assertNotIn(b"AUDIT\t", stdout)
        self.assertNotIn(b"final_edges", stdout)
        self.assertNotIn(b"best_partition", stdout)
        self.assertIn(b"RESULT_REF\t", stdout)
        self.assertLess(len(stdout), 1024 * 1024)
        self.assertFalse(any(self.internal.rglob("proposals.jsonl.gz")))

        reused = self.execute(store, attempt=2, invocation=2)
        self.assertEqual(reused["status"], "reused_verified_completion")
        saved = json.loads(reused["result_payload"])
        self.assertEqual(saved["task_identity_sha256"], result["task_identity_sha256"])
        self.assertEqual(store._watchdog_invocation_ids, {1})
        store.close()

    def test_multi_task_activity_freezes_inventory_streams_audits_and_reuses(self):
        graphs = [fixture_graph(), fixture_graph(ENGINEERING_ROOT + 1, "_SECOND")]
        identities = [
            G0TaskIdentity("SYNTHETIC_ACTIVITY_20261021", 100, 0,
                           "SYNTHETIC", index, 0)
            for index in range(2)
        ]
        tasks = list(zip(graphs, identities, strict=True))
        factory_calls = []

        def task_source():
            factory_calls.append("called")
            return iter(tasks)

        store = self.open_store_for("11111111-2222-4333-8444-555555555555")
        original_verify = store.verify_recovery
        with mock.patch.object(store, "verify_recovery", wraps=original_verify) as verify:
            first = run_synthetic_g0_activity(
                store=store, tasks=task_source, limits=watchdog_limits(), workers=4)
            self.assertEqual(verify.call_count, 1,
                             "full ledger/file verification must occur once at activity start")
            self.assertEqual(first["status"], "completed", first)
            self.assertEqual(first["task_count"], 2)
            self.assertEqual(first["schedule"], "serial_tasks")
            self.assertEqual(first["global_compute_worker_cap"], 4)
            self.assertEqual(first["recovery_report"].completed_task_ids,
                             tuple(sorted(first_outcome["task_id"]
                                          for first_outcome in first["outcomes"])))
            self.assertEqual(first["resource_accounting"]["peak_compute_workers"], 4)
            self.assertEqual(first["resource_accounting"]["watchdog_invocation_count"], 2)
            self.assertTrue(first["resource_accounting"]["resource_accounting_complete"])
            self.assertTrue(all("result" not in item and "result_payload" not in item
                                for item in first["outcomes"]))
            self.assertTrue(all("sha256" in item["result_record"]
                                for item in first["outcomes"]))
            self.assertEqual(store._active_task_ids, set())
            # The frozen manifest contains the whole inventory and its seed
            # fingerprint map, not just the currently running task.
            self.assertEqual(len(store.activity_task_seeds), 2)

            second = run_synthetic_g0_activity(
                store=store, tasks=task_source, limits=watchdog_limits(), workers=4)
            self.assertEqual(verify.call_count, 1,
                             "normal task reuse must use the verified incremental index")
            self.assertEqual([item["status"] for item in second["outcomes"]],
                             ["reused_verified_completion"] * 2)
            self.assertTrue(all("result_payload" not in item and "result" not in item
                                for item in second["outcomes"]))
            self.assertTrue(all("sha256" in item["result_record"]
                                for item in second["outcomes"]))
            self.assertEqual(second["recovery_report"].completed_task_ids,
                             first["recovery_report"].completed_task_ids)
            self.assertEqual(second["resource_accounting"]["watchdog_invocation_count"], 2)
            self.assertEqual(second["resource_accounting"]["accounted_invocation_count"], 2)
            self.assertEqual(second["resource_accounting"]["summed_watchdog_cpu_seconds"],
                             first["resource_accounting"]["summed_watchdog_cpu_seconds"])
            self.assertEqual(len(factory_calls), 4,
                             "replayable task factories are streamed twice per activity call")
        with self.assertRaisesRegex(RecoveryRefused, "inventory are immutable"):
            run_synthetic_g0_activity(
                store=store, tasks=tasks[:1], limits=watchdog_limits(), workers=4)
        with self.assertRaisesRegex(RecoveryRefused, "inventory are immutable"):
            run_synthetic_g0_activity(
                store=store, tasks=list(reversed(tasks)),
                limits=watchdog_limits(), workers=4)
        store.close()
        resumed = self.open_store_for("11111111-2222-4333-8444-555555555555")
        with mock.patch.object(resumed, "verify_recovery",
                               wraps=resumed.verify_recovery) as full_verify:
            restored = run_synthetic_g0_activity(
                store=resumed, tasks=tasks, limits=watchdog_limits(), workers=4)
            self.assertEqual(full_verify.call_count, 1,
                             "new process must fully verify ledger and archived audit streams")
            self.assertEqual([item["status"] for item in restored["outcomes"]],
                             ["reused_verified_completion"] * 2)
        resumed.close()

    def test_active_task_guard_prevents_a_second_concurrent_task(self):
        graph_a = fixture_graph()
        graph_b = fixture_graph(ENGINEERING_ROOT + 2, "_THIRD")
        identity_a = G0TaskIdentity("SYNTHETIC_CONCURRENCY", 100, 0,
                                    "SYNTHETIC", 0, 0)
        identity_b = G0TaskIdentity("SYNTHETIC_CONCURRENCY", 100, 0,
                                    "SYNTHETIC", 1, 0)
        from g0_minimal_executor import _synthetic_task_plan
        environment = runtime_manifest(require_target=False)
        plans = [_synthetic_task_plan(graph_a, identity_a, environment),
                 _synthetic_task_plan(graph_b, identity_b, environment)]
        inventory = {str(plan["task_id"]): str(plan["seed_fingerprint"])
                     for plan in plans}
        store = self.open_store_for("22222222-3333-4444-8555-666666666666")
        store.prepare_activity(activity_id=store.run_uuid, expected_tasks=inventory)
        first = plans[0]
        attempt = str(uuid.UUID(int=901))
        store.begin_task(task_id=str(first["task_id"]), attempt_id=attempt,
                         seed_fingerprint=str(first["seed_fingerprint"]),
                         invocation_id=1)
        with self.assertRaisesRegex(RecoveryRefused, "one active task"):
            store.begin_task(task_id=str(plans[1]["task_id"]),
                             attempt_id=str(uuid.UUID(int=902)),
                             seed_fingerprint=str(plans[1]["seed_fingerprint"]),
                             invocation_id=2)
        store.record_task_failure(task_id=str(first["task_id"]), attempt_id=attempt,
                                  failure_class="UNKNOWN",
                                  reason_code="G0_TEST_INTERRUPTION",
                                  reason="Guard-only test cleanup")
        store.close()

    def test_activity_recovery_reuses_prior_success_and_retries_only_failed_task(self):
        graphs = [fixture_graph(), fixture_graph(ENGINEERING_ROOT + 3, "_RECOVERY")]
        tasks = [
            (graphs[0], G0TaskIdentity("SYNTHETIC_ACTIVITY_RECOVERY", 100, 0,
                                       "SYNTHETIC", 0, 0)),
            (graphs[1], G0TaskIdentity("SYNTHETIC_ACTIVITY_RECOVERY", 100, 0,
                                       "SYNTHETIC", 1, 0)),
        ]
        run_id = "44444444-5555-4666-8777-888888888888"
        from g0_minimal_executor import _synthetic_task_plan
        operational_task_id = _synthetic_task_plan(
            graphs[1], tasks[1][1], runtime_manifest(require_target=False))["task_id"]
        store = self.open_store_for(run_id)
        first = run_synthetic_g0_activity(
            store=store, tasks=tasks, limits=watchdog_limits(), workers=4,
            _test_faults={
                # The second task fails after its complete proposal trace, with
                # a typed operational worker error eligible for one recovery.
                operational_task_id: "worker_operational_failure"
            })
        self.assertEqual(first["status"], "stopped_after_task_failure", first)
        self.assertEqual(first["resource_accounting"]["watchdog_invocation_count"], 2)
        self.assertEqual(first["resource_accounting"]["accounted_invocation_count"], 2)
        self.assertEqual([item["status"] for item in first["outcomes"]],
                         ["completed", "operational_failure"])
        failed_task = first["outcomes"][1]["task_id"]
        self.assertEqual(first["recovery_state"], "retryable")
        self.assertEqual(len(store._task_state(failed_task)["starts"]), 1)
        store.close()

        resumed = self.open_store_for(run_id)
        second = run_synthetic_g0_activity(
            store=resumed, tasks=tasks, limits=watchdog_limits(), workers=4)
        self.assertEqual(second["status"], "completed", second)
        self.assertEqual(second["resource_accounting"]["watchdog_invocation_count"], 3)
        self.assertEqual(second["resource_accounting"]["accounted_invocation_count"], 3)
        self.assertEqual([item["status"] for item in second["outcomes"]],
                         ["reused_verified_completion", "completed"])
        self.assertTrue(all("result_payload" not in item and "result" not in item
                            for item in second["outcomes"]))
        self.assertTrue(all("sha256" in item["result_record"]
                            for item in second["outcomes"]))
        self.assertEqual(len(resumed._task_state(failed_task)["starts"]), 2)
        self.assertEqual(resumed._task_state(failed_task)["starts"][0]["seed_fingerprint"],
                         resumed._task_state(failed_task)["starts"][1]["seed_fingerprint"])
        watchdog_usage = [record["finished"]["result"]["usage"]
                          for record in resumed._watchdog_invocations.values()]
        self.assertAlmostEqual(
            second["resource_accounting"]["summed_watchdog_cpu_seconds"],
            sum(item["cpu_seconds"] for item in watchdog_usage))
        resumed.close()

    def test_activity_scheduler_lock_rejects_concurrent_entry_before_writes(self):
        graph = fixture_graph()
        tasks = [(graph, fixture_identity(graph))]
        store = self.open_store_for("55555555-6666-4777-8888-999999999999")
        with store.activity_execution():
            with self.assertRaisesRegex(RecoveryRefused, "Another scheduler"):
                run_synthetic_g0_activity(
                    store=store, tasks=tasks, limits=watchdog_limits(), workers=4)
        self.assertFalse(store._has_prior_work)
        store.close()

    def test_replayable_task_source_drift_is_rejected_before_scientific_work(self):
        graphs = [fixture_graph(), fixture_graph(ENGINEERING_ROOT + 4, "_DRIFT")]
        tasks = [
            (graphs[0], G0TaskIdentity("SYNTHETIC_SOURCE_DRIFT", 100, 0,
                                       "SYNTHETIC", 0, 0)),
            (graphs[1], G0TaskIdentity("SYNTHETIC_SOURCE_DRIFT", 100, 0,
                                       "SYNTHETIC", 1, 0)),
        ]
        calls = []

        def changing_source():
            calls.append(len(calls))
            return iter(tasks if len(calls) == 1 else list(reversed(tasks)))

        store = self.open_store_for("66666666-7777-4888-8999-000000000000")
        with self.assertRaisesRegex(RecoveryRefused, "after inventory freeze"):
            run_synthetic_g0_activity(
                store=store, tasks=changing_source,
                limits=watchdog_limits(), workers=4)
        self.assertEqual(len(calls), 2)
        self.assertEqual(store._task_event_index, {})
        store.close()

    def test_audit_stream_write_failure_stops_and_fails_closed_for_recovery(self):
        # Enough bounded engineering records to fill the OS pipe if its
        # external consumer fails before task completion.
        graph = fixture_graph()
        identity = fixture_identity(graph)
        store = self.open_store_for("33333333-4444-4555-8666-777777777777")
        original_write = store.write_immutable_artifact

        def injected_write_failure(*, relative_path, artifact_kind,
                                   identity, chunks, stream_metadata=None):
            if artifact_kind != "audit":
                return original_write(relative_path=relative_path,
                                      artifact_kind=artifact_kind,
                                      identity=identity, chunks=chunks,
                                      stream_metadata=stream_metadata)

            def broken_stream():
                for index, block in enumerate(chunks):
                    if index == 1:
                        raise OSError("injected external SSD write interruption")
                    yield block

            return original_write(relative_path=relative_path,
                                  artifact_kind=artifact_kind,
                                  identity=identity, chunks=broken_stream(),
                                  stream_metadata=stream_metadata)

        with mock.patch.object(store, "write_immutable_artifact",
                               side_effect=injected_write_failure):
            with self.assertRaises(Exception):
                self.execute(store, graph=graph, workers=1,
                             limits=watchdog_limits(workers=1))
        task_plan = __import__("g0_minimal_executor")._synthetic_task_plan(
            graph, identity, runtime_manifest(require_target=False))
        state = store._task_state(str(task_plan["task_id"]))
        self.assertEqual(state["failures"][-1]["failure_class"], "UNKNOWN")
        self.assertEqual(state["failures"][-1]["reason_code"],
                         "G0_AUDIT_STREAM_WRITE_FAILED")
        watchdog_terminals = [event for event in store._task_events()
                              if event.get("event") ==
                              "g0_watchdog_invocation_finished"]
        self.assertEqual(len(watchdog_terminals), 1)
        self.assertEqual(watchdog_terminals[0]["status"], "stopped")
        self.assertEqual(watchdog_terminals[0]["result"]["reason"],
                         "G0_EXTERNAL_IO_FAILURE")
        with self.assertRaises(RecoveryRefused):
            store.verify_recovery({str(task_plan["task_id"]):
                                   str(task_plan["seed_fingerprint"])})
        store.close()

    def test_fixed_seed_rerun_reproduces_graph_q_vector_and_best_partition(self):
        first_store = self.open_store_for(SYNTHETIC_RUN_ID)
        second_run = "cccccccc-dddd-4eee-8fff-000000000001"
        second_store = self.open_store_for(second_run)
        first = self.execute(first_store, attempt=1, invocation=1)
        second = self.execute(second_store, attempt=2, invocation=1)
        self.assertEqual(first["status"], "completed", first)
        self.assertEqual(second["status"], "completed", second)
        left, right = first["result"], second["result"]
        self.assertEqual(left["task_identity_sha256"], right["task_identity_sha256"])
        self.assertEqual(left["null_graph_sha256"], right["null_graph_sha256"])
        self.assertEqual(left["seed_manifest"], right["seed_manifest"])
        self.assertEqual(left["louvain"]["q_values"], right["louvain"]["q_values"])
        self.assertEqual(left["louvain"]["max_q"], right["louvain"]["max_q"])
        self.assertEqual(left["louvain"]["best_partition"],
                         right["louvain"]["best_partition"])
        first_store.close()
        second_store.close()

    def test_scientific_and_unknown_failures_do_not_become_retries(self):
        for run_id, fault, expected_class in (
                ("dddddddd-eeee-4fff-8000-000000000001", "scientific_failure", "SCIENTIFIC"),
                ("dddddddd-eeee-4fff-8000-000000000002", "unknown_failure", "UNKNOWN")):
            store = self.open_store_for(run_id)
            result = self.execute(store, fault=fault)
            self.assertEqual(result["status"],
                             "scientific_failure" if expected_class == "SCIENTIFIC"
                             else "unknown_failure")
            with self.assertRaises(RecoveryRefused):
                store.verify_recovery({result["task_id"]:
                                       result["seed_fingerprint"]})
            state = store._task_state(result["task_id"])
            self.assertEqual(state["failures"][-1]["failure_class"], expected_class)
            self.assertFalse(state["failures"][-1]["recovery_allowed"])
            store.close()

    def test_spawn_worker_scientific_and_operational_failures_keep_classification(self):
        graph = small_fault_graph()
        for run_id, fault, expected_status, failure_class in (
                ("eeeeeeee-ffff-4000-8000-000000000001",
                 "worker_scientific_failure", "scientific_failure", "SCIENTIFIC"),
                ("eeeeeeee-ffff-4000-8000-000000000002",
                 "worker_operational_failure", "operational_failure", "OPERATIONAL")):
            store = self.open_store_for(run_id)
            first = self.execute(store, fault=fault, graph=graph)
            self.assertEqual(first["status"], expected_status, first)
            identity = fixture_identity(graph)
            seed_fingerprint = hashlib.sha256(canonical_json({
                "graph_seed": g0_graph_seed(identity),
                "louvain_seeds": [g0_louvain_seed(identity, i) for i in range(200)],
            })).hexdigest()
            state = store._task_state(first["task_id"])
            self.assertEqual(state["failures"][-1]["failure_class"], failure_class)
            if failure_class == "SCIENTIFIC":
                self.assertFalse(state["failures"][-1]["recovery_allowed"])
                with self.assertRaises(RecoveryRefused):
                    store.verify_recovery({first["task_id"]: seed_fingerprint})
            else:
                self.assertTrue(state["failures"][-1]["recovery_allowed"])
                report = store.verify_recovery({first["task_id"]: seed_fingerprint})
                self.assertEqual(report.retryable_task_ids, (first["task_id"],))
                recovered = self.execute(store, attempt=2, invocation=2, graph=graph)
                self.assertEqual(recovered["status"], "completed", recovered)
                self.assertEqual(recovered["result"]["task_id"], first["task_id"])
                self.assertEqual(recovered["result"]["seed_manifest"]["graph_seed"],
                                 g0_graph_seed(identity))
            store.close()

    def test_abrupt_spawn_worker_exit_is_unknown_and_cannot_be_retried(self):
        graph = small_fault_graph()
        store = self.open_store_for("eeeeeeee-ffff-4000-8000-000000000003")
        result = self.execute(
            store, fault="worker_abrupt_exit", graph=graph, workers=1,
            limits=watchdog_limits(workers=1, wall_seconds=45,
                                   cpu_seconds=45, case_seconds=20))
        self.assertEqual(result["status"], "unknown_failure", result)
        self.assertEqual(result["reason_code"], "G0_WORKER_EXIT_UNCLASSIFIED")
        state = store._task_state(result["task_id"])
        self.assertEqual(state["failures"][-1]["failure_class"], "UNKNOWN")
        self.assertFalse(state["failures"][-1]["recovery_allowed"])
        identity = fixture_identity(graph)
        seed_fingerprint = hashlib.sha256(canonical_json({
            "graph_seed": g0_graph_seed(identity),
            "louvain_seeds": [g0_louvain_seed(identity, i) for i in range(200)],
        })).hexdigest()
        with self.assertRaises(RecoveryRefused):
            store.verify_recovery({result["task_id"]: seed_fingerprint})
        store.close()


if __name__ == "__main__":
    unittest.main()
