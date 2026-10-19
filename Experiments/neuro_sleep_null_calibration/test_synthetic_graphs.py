"""Small synthetic-only code unit tests; NOT formal NC-0a diagnostics."""
import math
import unittest

from synthetic_graphs import (FAMILIES, make_synthetic_graph, metrics,
                              synthetic_seed, _maximum_spanning_tree)


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

    def test_seed_namespaces_and_replay(self):
        from hashlib import sha256
        graph = "NC_SYNTH_V1|20261009|factor-mst|100"
        chain = "NC_SYNTH_V1|20261009|chain|factor-mst|100|0"
        bfs = "NC_SYNTH_V1|20261009|bfs-identity|factor-mst|100"
        expect = lambda payload: int.from_bytes(
            sha256(payload.encode("ascii")).digest()[:8], "big")
        self.assertEqual(synthetic_seed("factor-mst", 100), expect(graph))
        self.assertEqual(
            synthetic_seed("factor-mst", 100, kind="chain", chain_index=0),
            expect(chain))
        self.assertEqual(
            synthetic_seed("factor-mst", 100, kind="bfs-identity"),
            expect(bfs))
        self.assertEqual(len({
            synthetic_seed("factor-mst", 100, kind="chain", chain_index=j)
            for j in range(8)}), 8)
        self.assertNotEqual(expect(graph), expect(bfs))

    def test_seed_invalid_index_cannot_be_silently_reused(self):
        for index in (-1, 8, 1.5, None):
            with self.subTest(index=index), self.assertRaises(ValueError):
                synthetic_seed("factor-mst", 100, kind="chain",
                               chain_index=index)
        with self.assertRaises(ValueError):
            synthetic_seed("factor-mst", 100, kind="graph", chain_index=0)

    def test_prim_global_lexicographic_edge_tie(self):
        import numpy as np
        # This fixture distinguishes canonical edge tie-breaking from
        # choosing the smallest frontier vertex on equal scores.
        matrix = np.array([
            [-np.inf, 2, 1, 1, 3],
            [2, -np.inf, 2, 3, 2],
            [1, 2, -np.inf, 1, 2],
            [1, 3, 1, -np.inf, 2],
            [3, 2, 2, 2, -np.inf],
        ], dtype=float)
        expected = {(0, 1), (0, 4), (1, 2), (1, 3)}
        self.assertEqual(_maximum_spanning_tree(matrix), expected)

    def test_invalid_family_and_n_rejected(self):
        with self.assertRaises(ValueError):
            make_synthetic_graph(10, "er-like")
        with self.assertRaises(ValueError):
            make_synthetic_graph(40, "other")


if __name__ == "__main__":
    unittest.main()
