"""Small synthetic-only code unit tests; NOT formal NC-0a diagnostics."""
import math
import unittest

from synthetic_graphs import FAMILIES, make_synthetic_graph, metrics


def _connected(g):
    adj = [set() for _ in range(g.n)]
    for u, v in g.edges:
        adj[u].add(v)
        adj[v].add(u)
    todo, seen = [0], {0}
    while todo:
        for v in adj[todo.pop()]:
            if v not in seen:
                seen.add(v)
                todo.append(v)
    return len(seen) == g.n


class SyntheticGraphUnitTests(unittest.TestCase):
    def test_four_families_produce_connected_simple_graphs(self):
        for family in FAMILIES:
            with self.subTest(family=family):
                g = make_synthetic_graph(48, family)
                self.assertTrue(_connected(g))
                self.assertEqual(len(set(g.edges)), len(g.edges))
                self.assertTrue(all(0 <= u < v < 48 for u, v in g.edges))
                if family != "ba-like":
                    self.assertEqual(g.m, 48 * 8)

    def test_reproducible_seeds_and_edge_sets(self):
        for family in FAMILIES:
            with self.subTest(family=family):
                a = make_synthetic_graph(40, family)
                b = make_synthetic_graph(40, family)
                self.assertEqual(a.fingerprint(), b.fingerprint())
                self.assertEqual(a.edges, b.edges)

    def test_metrics_triangle_and_overlap(self):
        edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
        m = metrics(4, edges, edges)
        self.assertEqual(m["triangles"], 1)
        self.assertEqual(m["edge_overlap"], 1)
        self.assertTrue(math.isfinite(m["assortativity"]))

    def test_regular_graph_assortativity_undefined(self):
        edges = [(i, (i + 1) % 8) if i < (i + 1) % 8 else ((i + 1) % 8, i) for i in range(8)]
        m = metrics(8, edges, edges)
        self.assertTrue(math.isnan(m["assortativity"]))

    def test_invalid_family_and_n_rejected(self):
        with self.assertRaises(ValueError):
            make_synthetic_graph(10, "er-like")
        with self.assertRaises(ValueError):
            make_synthetic_graph(40, "other")


if __name__ == "__main__":
    unittest.main()
