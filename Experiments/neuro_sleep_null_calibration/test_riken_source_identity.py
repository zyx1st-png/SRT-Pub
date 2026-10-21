from __future__ import annotations

import json
import math
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import numpy as np
import networkx as nx

import riken_source_identity as identity
from riken_source_identity import (
    IdentityEvidenceError,
    build_candidate_graph,
    hash_float64,
    hash_int64,
    load_h3_reference,
    read_source_abs_correlation,
    select_h3_first_by_n,
    select_g0_repeats,
    select_h3_panel,
    stable_seed,
    validate_h3_replay,
)


class TestRikenSourceIdentity(unittest.TestCase):
    def test_stable_seed_preserves_historical_target_label_realization(self) -> None:
        self.assertEqual(stable_seed(12345, "population_size_scaling_subset",
                                     "mouse01_sleep", "N100", 0), 635240748)
        self.assertEqual(stable_seed(12345, "population_size_scaling_subset",
                                     "mouse01_sleep", 100, 0), 2046770659)

    def test_g0_repeat_selection_is_deterministic_and_order_independent(self) -> None:
        self.assertEqual(select_g0_repeats("mouse01_sleep", 100, range(100)),
                         select_g0_repeats("mouse01_sleep", 100, reversed(range(100))))
        self.assertEqual(len(set(select_g0_repeats("mouse01_sleep", 100, range(100)))), 10)
        with self.assertRaises(IdentityEvidenceError):
            select_g0_repeats("mouse01_sleep", 100, range(99))

    @staticmethod
    def panel_fixture() -> list[dict]:
        recordings = ("mouse01_sleep", "mouse02_sleep", "mouse03_sleep",
                      "mouse04_day1_sleep", "mouse04_day2_sleep", "mouse05_sleep")
        rows = []
        for recording in recordings:
            for n in (100, 150, 225, 340, 510, 765, 1150, 1725, 2600, 3900):
                for repeat in select_g0_repeats(recording, n, range(100)):
                    for state in ("wake", "NREM"):
                        for window in (0, 1):
                            rows.append({
                                "graph_id": f"{recording}|N{n}|rep-{repeat:03d}|{state}|window-{window:03d}",
                                "recording_id": recording, "N": n,
                                "subset_repeat": repeat, "state": state,
                                "window_id": window,
                                "source_file_sha256": "a" * 64,
                                "selected_neuron_indices_sha256": "b" * 64,
                                "source_frame_indices_sha256": "c" * 64,
                                "expected_input_identity_sha256": "0" * 64,
                                "expected_edge_count": 8 * n,
                                "historical_job_sha256": "9" * 64,
                                "historical_q_vector_sha256": "d" * 64,
                                "louvain_seed_vector_sha256": "e" * 64,
                                "historical_q_max_first_index": 17,
                            })
        return rows

    def test_h3_panel_is_120_rows_and_does_not_use_q_values_for_selection(self) -> None:
        rows = self.panel_fixture()
        panel = select_h3_panel(rows)
        changed = [dict(row, historical_q_vector_sha256="f" * 64) for row in rows]
        changed_panel = select_h3_panel(changed)
        self.assertEqual(len(panel), 120)
        self.assertEqual([(r["graph_id"], r["identity_panel_seed"]) for r in panel],
                         [(r["graph_id"], r["identity_panel_seed"]) for r in changed_panel])
        self.assertEqual(len({row["graph_id"] for row in panel}), 120)
        self.assertTrue(all(row["edge_identity"] == "NOT_RECONSTRUCTED" for row in panel))
        pilot = select_h3_first_by_n(panel)
        self.assertEqual([row["N"] for row in pilot],
                         [100, 150, 225, 340, 510, 765, 1150, 1725, 2600, 3900])
        self.assertTrue(all(row["recording_id"] == "mouse01_sleep" for row in pilot))
        self.assertEqual([(row["graph_id"], row["pilot_order"]) for row in pilot],
                         [(row["graph_id"], index + 1)
                          for index, row in enumerate(select_h3_first_by_n(changed_panel))])

    def test_h3_replay_requires_frozen_tolerance_and_complete_identity(self) -> None:
        values = [i / 1000 for i in range(200)]
        seeds = list(range(200))
        graph_id = "mouse01_sleep|N100|rep-001|wake|window-000"
        expected = [{"graph_id": graph_id,
                     "historical_q_vector_sha256": hash_float64(values),
                     "historical_louvain_seed_vector_sha256": hash_int64(seeds),
                     "historical_q_max_first_index": 199,
                     "expected_node_order_sha256": "a" * 64,
                     "source_artifact_sha256": "f" * 64,
                     "selected_neuron_indices_sha256": "a" * 64,
                     "source_frame_indices_sha256": "c" * 64,
                     "expected_input_identity_sha256": "0" * 64,
                     "expected_edge_count": 800, "N": 100}]
        replay = [{"graph_id": graph_id,
                   "historical_edge_set_sha256": "b" * 64,
                   "candidate_edge_set_sha256": "b" * 64,
                   "historical_labeled_edge_set_sha256": "b" * 64,
                   "candidate_labeled_edge_set_sha256": "b" * 64,
                   "historical_node_order_sha256": "a" * 64,
                   "candidate_node_order_sha256": "a" * 64,
                   "source_artifact_sha256": "f" * 64,
                   "selected_neuron_indices_sha256": "a" * 64,
                   "expected_input_identity_sha256": "0" * 64,
                   "expected_source_frame_indices_sha256": "c" * 64,
                   "reconstructed_source_frame_indices_sha256": "c" * 64,
                   "historical_builder_function_sha256":
                       identity.EXPECTED_HISTORICAL_GRAPH_FUNCTION_SHA256,
                   "historical_N": 100, "candidate_N": 100,
                   "historical_E": 800, "candidate_E": 800,
                   "historical_adjacency_iteration_sha256": "f" * 64,
                   "candidate_adjacency_iteration_sha256": "f" * 64,
                   "executor_sorted_adjacency_iteration_sha256": "g" * 64,
                   "historical_candidate_adjacency_order_equal": True,
                   "historical_executor_adjacency_order_equal": False,
                   "historical_degree_sequence_sha256": "c" * 64,
                   "candidate_degree_sequence_sha256": "c" * 64,
                   "louvain_seeds": seeds, "q_values": values,
                   "historical_builder_q_values": values,
                   "historical_builder_q_max_first_index": 199,
                   "historical_q_values": values, "historical_q_max": max(values),
                   "historical_q_max_first_index": 199,
                   "q_max_first_index": 199}]
        with self.assertRaisesRegex(IdentityEvidenceError, "must equal.*1e-10"):
            validate_h3_replay(expected, replay, trial_q_atol=None)
        with self.assertRaisesRegex(IdentityEvidenceError, "must equal.*1e-10"):
            validate_h3_replay(expected, replay, trial_q_atol=1e-6)
        report = validate_h3_replay(expected, replay, trial_q_atol=1e-10)
        self.assertEqual(report["status"], "SOURCE_GRAPH_AND_HISTORICAL_Q_PASS")
        self.assertEqual(report["source_graph_identity"]["status"], "PASS")
        self.assertEqual(report["historical_order_q_replay"]["status"], "PASS")
        self.assertEqual(report["executor_sorted_order_compatibility"]["status"],
                         "RESULTS_MATCH_WITH_DIFFERENT_ADJACENCY_ORDER")
        self.assertTrue(report["executor_sorted_order_compatibility"][
            "does_not_invalidate_source_graph_or_historical_replay"])
        with self.assertRaisesRegex(IdentityEvidenceError, "missing, duplicated"):
            validate_h3_replay(expected * 2, replay, trial_q_atol=1e-10)
        changed_executor = list(values)
        changed_executor[0] += 0.01
        replay[0]["q_values"] = changed_executor
        report = validate_h3_replay(expected, replay, trial_q_atol=1e-10)
        self.assertEqual(report["source_graph_identity"]["status"], "PASS")
        self.assertEqual(report["historical_order_q_replay"]["status"], "PASS")
        self.assertEqual(report["executor_sorted_order_compatibility"]["status"],
                         "INCOMPATIBLE")
        self.assertEqual(report["status"], "SOURCE_GRAPH_AND_HISTORICAL_Q_PASS")
        replay[0]["q_values"] = values
        del replay[0]["q_values"]
        report = validate_h3_replay(expected, replay, trial_q_atol=1e-10)
        self.assertEqual(report["source_graph_identity"]["status"], "PASS")
        self.assertEqual(report["historical_order_q_replay"]["status"], "PASS")
        self.assertEqual(report["executor_sorted_order_compatibility"]["status"],
                         "INCOMPLETE_OR_INVALID")
        self.assertEqual(report["status"], "SOURCE_GRAPH_AND_HISTORICAL_Q_PASS")
        replay[0]["q_values"] = values
        replay[0]["candidate_edge_set_sha256"] = "d" * 64
        report = validate_h3_replay(expected, replay, trial_q_atol=1e-10)
        self.assertEqual(report["source_graph_identity"]["status"], "NC-INVALID")
        self.assertEqual(report["historical_order_q_replay"]["status"], "PASS")
        self.assertEqual(report["status"], "NC-INVALID_SOURCE_GRAPH_IDENTITY")
        replay[0]["candidate_edge_set_sha256"] = "b" * 64
        replay[0]["historical_builder_q_values"] = [*values]
        replay[0]["historical_builder_q_values"][0] += 0.01
        report = validate_h3_replay(expected, replay, trial_q_atol=1e-10)
        self.assertEqual(report["source_graph_identity"]["status"], "PASS")
        self.assertEqual(report["historical_order_q_replay"]["status"], "NC-INVALID")
        self.assertEqual(report["status"], "NC-INVALID_HISTORICAL_Q_REPLAY")

    def test_h3_runtime_does_not_claim_unrecorded_scipy_was_historical(self) -> None:
        runtime = identity.h3_runtime_manifest()
        self.assertFalse(runtime["historical_environment_fully_pinned"])
        self.assertEqual(runtime["historical_float_environment_exactness"],
                         "UNPROVEN_SCIPY_VERSION_NOT_RECORDED")
        self.assertIn("SciPy", runtime["historical_environment_gaps"][0])

    def test_h3_reference_loader_checks_saved_job_hash_q_and_seed_identity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            jobs = root / "jobs"
            jobs.mkdir()
            graph_id = "mouse01_sleep|N100|rep-001|wake|window-000"
            q_values = [i / 1000 for i in range(200)]
            seeds = identity._expected_louvain_seeds("mouse01_sleep", "N100", "wake", 0)
            job_path = jobs / "mouse01_sleep__N100__rep-001.json"
            job_path.write_text(json.dumps({"windows": {"state0_window0": {
                "state": "wake", "window_index": 0, "q_values": q_values,
                "q_max_first_index": 199}}}), encoding="utf-8")
            panel = {"graph_id": graph_id, "recording_id": "mouse01_sleep", "N": 100,
                     "subset_repeat": 1, "state": "wake", "window_id": 0,
                     "historical_job_sha256": identity.sha256_file(job_path),
                     "historical_q_vector_sha256": hash_float64(q_values),
                     "historical_louvain_seed_vector_sha256": hash_int64(seeds),
                     "historical_q_max_first_index": 199}
            reference = load_h3_reference(panel, root)
            self.assertEqual(reference["q_values"], q_values)
            self.assertEqual(reference["louvain_seeds"], seeds)
            job_path.write_text(job_path.read_text(encoding="utf-8").replace("0.199", "0.198"),
                                encoding="utf-8")
            with self.assertRaisesRegex(IdentityEvidenceError, "job hash differs"):
                load_h3_reference(panel, root)

    def test_candidate_graph_has_exact_edge_count_and_connectedness(self) -> None:
        from scipy.sparse.csgraph import minimum_spanning_tree

        n = 20
        matrix = np.full((n, n), 0.5, dtype=np.float64)
        np.fill_diagonal(matrix, 0.0)
        matrix[:5, :5] = 0.9
        np.fill_diagonal(matrix, 0.0)
        graph = build_candidate_graph(matrix)
        self.assertEqual(graph.number_of_edges(), 8 * n)
        self.assertTrue(nx.is_connected(graph))
        mst = minimum_spanning_tree(1.0 - matrix).tocoo()
        included = sum(graph.has_edge(int(u), int(v))
                       for u, v in zip(mst.row, mst.col, strict=True))
        self.assertEqual(included, n - 1)
        self.assertTrue(all(math.isclose(attr["weight"], 1.0)
                            for _, _, attr in graph.edges(data=True)))

    def test_historical_graph_order_difference_is_visible_to_h3(self) -> None:
        from scipy.sparse.csgraph import minimum_spanning_tree

        def historical_builder(abs_corr):
            n = abs_corr.shape[0]
            target = round(n * 16 / 2)
            cost = 1.0 - abs_corr.copy()
            np.fill_diagonal(cost, np.inf)
            mst = minimum_spanning_tree(cost).tocoo()
            mst_pairs = sorted({(min(int(i), int(j)), max(int(i), int(j)))
                                for i, j in zip(mst.row, mst.col, strict=True)})
            upper_i, upper_j = np.triu_indices(n, k=1)
            values = abs_corr[upper_i, upper_j]
            flat = np.asarray([i * (2 * n - i - 1) // 2 + j - i - 1
                               for i, j in mst_pairs])
            candidate = values.copy()
            candidate[flat] = -np.inf
            additional = target - (n - 1)
            threshold = float(np.partition(candidate, len(candidate) - additional)
                              [len(candidate) - additional])
            strict = np.flatnonzero(candidate > threshold)
            tied = np.flatnonzero(candidate == threshold)
            selected = np.concatenate((strict, tied[:additional - strict.size]))
            graph = nx.Graph()
            graph.add_nodes_from(range(n))
            graph.add_edges_from((u, v, {"weight": 1.0}) for u, v in mst_pairs)
            graph.add_edges_from((int(upper_i[k]), int(upper_j[k]), {"weight": 1.0})
                                 for k in selected)
            return graph, {}

        with mock.patch.object(identity, "_historical_connected_graph",
                               return_value=(historical_builder, "fixture")):
            matrix = np.round(np.abs(np.corrcoef(
                np.random.default_rng(20261021).normal(size=(1500, 20)).T)), 2)
            np.fill_diagonal(matrix, 0.0)
            result = identity.reconstruct_graph_pair(
                matrix, Path("synthetic-source.py"), tuple(range(100, 120)))
        self.assertEqual(result["historical_edge_set_sha256"],
                         result["candidate_edge_set_sha256"])
        self.assertEqual(result["historical_adjacency_iteration_sha256"],
                         result["candidate_adjacency_iteration_sha256"])
        self.assertFalse(result["historical_executor_adjacency_order_equal"])
        seeds = [stable_seed(20261021, "synthetic-order-probe", i) for i in range(200)]
        historical_q = identity.replay_louvain_q(
            result["historical_graph"], seeds, require_target=False)["q_values"]
        executor_q = identity.replay_louvain_q(
            identity.build_executor_order_graph(result["candidate_graph"]),
            seeds, require_target=False)["q_values"]
        self.assertTrue(any(old != new for old, new in zip(historical_q, executor_q,
                                                           strict=True)))

    def test_source_window_reader_reorders_unsorted_frame_rows_losslessly(self) -> None:
        try:
            import h5py
        except ImportError:
            self.skipTest("h5py is not part of bounded GitHub test dependencies")
        rng = np.random.default_rng(48)
        signal = rng.normal(size=(3000, 20))
        wake = np.arange(1499, -1, -1, dtype=np.int64) + 1
        nrem = np.arange(1500, 3000, dtype=np.int64) + 1
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "synthetic-source.h5"
            with h5py.File(path, "w") as handle:
                handle.create_dataset("spike_smoothed", data=signal)
                wake_ds = handle.create_dataset("wake_source_frames", data=wake)
                nrem_ds = handle.create_dataset("nrem_source_frames", data=nrem)
                handle.create_group("frame")
                used = handle.create_dataset("frame/used_frame", shape=(2,),
                                             dtype=h5py.ref_dtype)
                used[0], used[1] = wake_ds.ref, nrem_ds.ref
            observed, node_ids, frame_hash = read_source_abs_correlation(
                path, range(20), "wake", 0)
        frames = wake.astype(np.int64) - 1
        expected = np.corrcoef(signal[frames, :].T, rowvar=True)
        expected = np.nan_to_num(expected, nan=0.0, posinf=0.0, neginf=0.0)
        np.fill_diagonal(expected, 0.0)
        self.assertEqual(node_ids, tuple(range(20)))
        np.testing.assert_allclose(observed, np.abs(expected), rtol=0.0, atol=1e-13)
        self.assertEqual(frame_hash, hash_int64(frames))


if __name__ == "__main__":
    unittest.main()
