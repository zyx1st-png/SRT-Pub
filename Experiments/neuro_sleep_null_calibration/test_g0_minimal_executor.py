"""Small synthetic integration tests for the G0 executor/storage boundary."""

from __future__ import annotations

import hashlib
import json
import platform
import sys
import unittest
import uuid

from g0_external_storage import G0ExternalStore, RecoveryRefused
from g0_minimal_executor import (
    G0TaskIdentity, _audit_replay_verifier, canonical_json, g0_graph_seed,
    g0_louvain_seed, normalize_graph_input, run_synthetic_g0_task,
    runtime_manifest,
)
from nc0a_watchdog import WatchdogLimits
from synthetic_graphs import make_synthetic_graph
from test_g0_external_storage import StorageFixture


ENGINEERING_ROOT = 20261021
SYNTHETIC_RUN_ID = "bbbbbbbb-cccc-4ddd-8eee-ffffffffffff"


def fixture_graph():
    fixture = make_synthetic_graph(100, "factor-mst", root=ENGINEERING_ROOT)
    return normalize_graph_input(
        "SYNTHETIC_FACTOR_MST_N100_ENGINEERING_20261021",
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


def watchdog_limits(workers=4):
    return WatchdogLimits(
        wall_seconds=300, cpu_seconds=300,
        aggregate_rss_bytes=4 * 1024**3, max_workers=workers,
        run_disk_bytes=16 * 1024**2, reserve_free_disk_bytes=1024,
        case_seconds=240, oracle_seconds=240, poll_seconds=0.1,
        suspend_tolerance_seconds=3, terminate_grace_seconds=0.5,
        memory_enforcement_backend="SAMPLED_ONLY")


class G0MinimalExecutorTests(StorageFixture):
    def open_store_for(self, run_id):
        return G0ExternalStore(
            run_uuid=run_id,
            internal_ledger_dir=self.internal / "control" / run_id,
            policy=self.policy, probe=self.probe, usage_provider=self.usage)

    def execute(self, store, *, attempt=1, invocation=1, fault=None, graph=None):
        graph = graph or fixture_graph()
        return run_synthetic_g0_task(
            store=store, graph=graph, identity=fixture_identity(graph),
            attempt_id=str(uuid.UUID(int=attempt)), invocation_id=invocation,
            limits=watchdog_limits(), workers=4,
            require_target_runtime=False, _test_fault=fault)

    def test_target_runtime_matches_historical_versions_on_local_mac(self):
        if (sys.platform != "darwin" or platform.machine() != "arm64" or
                sys.version_info[:3] != (3, 14, 0)):
            self.skipTest("Exact G0 target-runtime verification requires the dedicated "
                          "macOS arm64 Python 3.14.0 environment")
        manifest = runtime_manifest(require_target=True)
        self.assertEqual(manifest["python"], "3.14.0")
        self.assertEqual(manifest["machine"], "arm64")
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

        reused = self.execute(store, attempt=2, invocation=2)
        self.assertEqual(reused["status"], "reused_verified_completion")
        saved = json.loads(reused["result_payload"])
        self.assertEqual(saved["task_identity_sha256"], result["task_identity_sha256"])
        self.assertEqual(store._watchdog_invocation_ids, {1})
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


if __name__ == "__main__":
    unittest.main()
