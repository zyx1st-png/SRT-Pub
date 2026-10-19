"""Synthetic-only unit tests. Not NC-0a mixing/feasibility execution."""

import random
import unittest

from connected_swap import ConnectedDegreeSwap, run_chain


def toy_graph(n=14):
    edges = {(min(i, (i + 1) % n), max(i, (i + 1) % n)) for i in range(n)}
    for i in range(n):
        j = (i + 3) % n
        edges.add((min(i, j), max(i, j)))
    return sorted(edges)


class SwapTests(unittest.TestCase):
    def test_non_simple_inputs_rejected(self):
        edges = toy_graph()
        with self.assertRaises(ValueError):
            ConnectedDegreeSwap(14, edges + [edges[0]])
        with self.assertRaises(ValueError):
            ConnectedDegreeSwap(14, [(0, 1), (1, 2)])
        with self.assertRaises(ValueError):
            ConnectedDegreeSwap(14, [(0, 0)] + edges)

    def test_deterministic_proposal_stream_and_invariants(self):
        a, ss_a = run_chain(14, toy_graph(), 17, 500, (1, 100, 500), oracle=True)
        b, ss_b = run_chain(14, list(reversed(toy_graph())), 17, 500, (1, 100, 500), oracle=True)
        self.assertEqual(a.fingerprint(), b.fingerprint())
        self.assertEqual(ss_a, ss_b)
        self.assertGreater(a.accepted, 0)
        self.assertEqual(a.attempts, 500)
        a.assert_invariants()

    def test_connected_bridge_cases(self):
        # Simple path (a tree with bridges); every accepted proposal remains connected.
        edges = [(i, i + 1) for i in range(13)]
        graph, _ = run_chain(14, edges, 200, 500, (20, 100, 500), oracle=True)
        graph.assert_invariants()
        self.assertGreater(graph.rejected_disconnect, 0)

    def test_proposal_and_reject_counts(self):
        graph = ConnectedDegreeSwap(14, toy_graph())
        rng = random.Random(3)
        for _ in range(400):
            graph.propose(rng, oracle=True)
        stats = graph.stats(3)
        self.assertEqual(stats.rejection_count + stats.accepted, stats.attempts)
        self.assertEqual(stats.attempts, 400)
        graph.assert_invariants()

    def test_snapshot_errors(self):
        with self.assertRaises(ValueError):
            run_chain(14, toy_graph(), 1, 3, (4,))


if __name__ == "__main__":
    unittest.main()
