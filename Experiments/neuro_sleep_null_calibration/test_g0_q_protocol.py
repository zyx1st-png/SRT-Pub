"""Synthetic tests for the prospective common observed/null Q interface."""

from __future__ import annotations

import random
import unittest

import networkx as nx

from g0_q_protocol import (
    CANONICAL_ORDER_POLICY,
    build_canonical_louvain_graph,
    canonical_graph_payload,
    canonical_louvain_q_vector,
    first_maximum_index,
)
from riken_source_identity import replay_canonical_louvain_q


def synthetic_fixture():
    # Deterministic, connected, tie-rich topology. Original neuron IDs are
    # intentionally nonconsecutive so the test catches accidental use of
    # temporary local positions as canonical scientific labels.
    nodes = (91, 7, 44, 13, 62, 2, 80, 31, 55, 19, 73, 5, 38, 100, 26, 67)
    edges = set()
    for offset in (1, 2, 5):
        for index, node in enumerate(nodes):
            other = nodes[(index + offset) % len(nodes)]
            edges.add((min(node, other), max(node, other)))
    edges.update({(2, 44), (7, 62), (13, 80), (19, 91)})
    return nodes, tuple(sorted(edges))


def seeds():
    return [100_000 + index * 17 for index in range(200)]


class CanonicalQProtocolTests(unittest.TestCase):
    def test_first_maximum_tie_uses_lowest_fixed_seed_index(self):
        self.assertEqual(first_maximum_index([0.3, 0.8, 0.8, 0.2]), 1)
        with self.assertRaisesRegex(ValueError, "nonempty and finite"):
            first_maximum_index([0.2, float("nan")])

    def test_edge_and_node_input_order_do_not_change_canonical_q_vector(self):
        nodes, edges = synthetic_fixture()
        reference = canonical_louvain_q_vector(nodes, edges, seeds())
        shuffled_nodes = list(nodes)
        shuffled_edges = list(edges)
        random.Random(81273).shuffle(shuffled_nodes)
        random.Random(9927).shuffle(shuffled_edges)
        shuffled = canonical_louvain_q_vector(
            shuffled_nodes, shuffled_edges, seeds())
        self.assertEqual(reference["order_policy"], CANONICAL_ORDER_POLICY)
        self.assertEqual(reference["topology_sha256"], shuffled["topology_sha256"])
        self.assertEqual(reference["ordered_representation_sha256"],
                         shuffled["ordered_representation_sha256"])
        self.assertEqual(reference["seed_vector_sha256"],
                         shuffled["seed_vector_sha256"])
        self.assertEqual(reference["q_values"], shuffled["q_values"])
        self.assertEqual(reference["q_vector_sha256"], shuffled["q_vector_sha256"])
        self.assertEqual(reference["q_max_200"], shuffled["q_max_200"])
        self.assertEqual(reference["first_max_trial_index"],
                         shuffled["first_max_trial_index"])
        self.assertEqual(reference["heuristic_diagnostics"]["prefix_max_q"]["200"],
                         reference["q_max_200"])
        self.assertEqual(len(reference["partition_sha256"]), 200)

    def test_original_id_permutation_must_be_explicitly_mapped_back(self):
        nodes, edges = synthetic_fixture()
        reference = canonical_louvain_q_vector(nodes, edges, seeds())
        permutation = {node: 1000 + ((index * 7) % len(nodes))
                       for index, node in enumerate(nodes)}
        relabeled_nodes = tuple(permutation[node] for node in nodes)
        relabeled_edges = tuple((permutation[u], permutation[v]) for u, v in edges)
        relabeled = canonical_louvain_q_vector(
            relabeled_nodes, relabeled_edges, seeds())
        self.assertNotEqual(reference["topology_sha256"],
                            relabeled["topology_sha256"])
        self.assertNotEqual(reference["ordered_representation_sha256"],
                            relabeled["ordered_representation_sha256"])
        inverse = {new: old for old, new in permutation.items()}
        restored_nodes = tuple(inverse[node] for node in relabeled_nodes)
        restored_edges = tuple((inverse[u], inverse[v])
                               for u, v in relabeled_edges)
        restored = canonical_louvain_q_vector(
            restored_nodes, restored_edges, seeds())
        self.assertEqual(reference["q_values"], restored["q_values"])
        self.assertEqual(reference["ordered_representation_sha256"],
                         restored["ordered_representation_sha256"])

    def test_observed_and_null_entry_points_share_one_q_contract(self):
        nodes, edges = synthetic_fixture()
        expected = canonical_louvain_q_vector(nodes, edges, seeds())
        historical_local_graph = nx.Graph()
        historical_local_graph.add_nodes_from(range(len(nodes)))
        historical_local_graph.add_edges_from(
            (nodes.index(u), nodes.index(v)) for u, v in reversed(edges))
        observed = replay_canonical_louvain_q(
            historical_local_graph, nodes, seeds(), require_target=False)
        self.assertEqual(expected["ordered_representation_sha256"],
                         observed["ordered_representation_sha256"])
        self.assertEqual(expected["q_values"], observed["q_values"])
        self.assertEqual(expected["q_max_200"], observed["q_max_200"])
        self.assertEqual(expected["first_max_trial_index"],
                         observed["first_max_trial_index"])

    def test_canonical_payload_rejects_ambiguous_or_corrupt_edges(self):
        nodes, edges = synthetic_fixture()
        payload = canonical_graph_payload(list(reversed(nodes)), edges)
        self.assertEqual(payload["nodes"], tuple(sorted(nodes)))
        self.assertEqual(payload["edges"], tuple(sorted(
            (min(u, v), max(u, v)) for u, v in edges)))
        with self.assertRaisesRegex(ValueError, "duplicate edges"):
            canonical_graph_payload(nodes, [*edges, tuple(reversed(edges[0]))])
        with self.assertRaisesRegex(ValueError, "original integer indices"):
            canonical_graph_payload([0, "1", 2], [(0, 2)])

    def test_builder_records_unit_weights_and_connected_graph(self):
        nodes, edges = synthetic_fixture()
        graph, manifest = build_canonical_louvain_graph(
            list(reversed(nodes)), list(reversed(edges)))
        self.assertEqual(tuple(graph.nodes), tuple(sorted(nodes)))
        self.assertEqual(manifest["order_policy"], CANONICAL_ORDER_POLICY)
        self.assertTrue(nx.is_connected(graph))
        self.assertTrue(all(data["weight"] == 1.0
                            for _, _, data in graph.edges(data=True)))


if __name__ == "__main__":
    unittest.main()
