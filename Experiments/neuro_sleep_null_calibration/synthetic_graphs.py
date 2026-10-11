"""Draft synthetic-only graph fixtures and diagnostics for NC-0a code review.

This module DOES NOT execute the formal 16-case, 8-chain, 32E NC-0a test.
No biological or RIKEN signals may be provided to these generators.

The graph families are deterministic *procedural analogues*, not claims
that synthetic graphs accurately represent real neural networks.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from hashlib import sha256
import math
import random
from typing import Iterable


Edge = tuple[int, int]
FAMILIES = ("er-like", "ws-like", "ba-like", "factor-mst")
FACTOR_COUNT = 6
TARGET_MEAN_DEGREE = 16


def _edge(a: int, b: int) -> Edge:
    return (a, b) if a < b else (b, a)


def synthetic_seed(family: str, n: int, *, kind: str = "graph",
                   chain_index: int | None = None, root: int = 20261009) -> int:
    """Exact synthetic-only SHA-256 seed contract. NOT the biological stable_seed.

    kind=graph:        NC_SYNTH_V1|root|family|n
    kind=chain:        NC_SYNTH_V1|root|chain|family|n|chain_index
    kind=bfs-identity: NC_SYNTH_V1|root|bfs-identity|family|n

    UTF-8/ASCII payload, digest first 8 bytes, unsigned big-endian integer.
    The 0..7 chain index is required and cannot silently be omitted.
    """
    if family not in FAMILIES or type(n) is not int or n < 1:
        raise ValueError("Invalid synthetic family or node count")
    if type(root) is not int or root < 0:
        raise ValueError("Invalid synthetic seed root")
    if kind == "graph":
        if chain_index is not None:
            raise ValueError("Graph fixture seeds have no chain index")
        fields = ("NC_SYNTH_V1", str(root), family, str(n))
    elif kind == "chain":
        if type(chain_index) is not int or not 0 <= chain_index <= 7:
            raise ValueError("Synthetic chain index must be an integer in 0..7")
        fields = ("NC_SYNTH_V1", str(root), "chain", family, str(n),
                  str(chain_index))
    elif kind == "bfs-identity":
        if chain_index is not None:
            raise ValueError("BFS identity seeds have no chain index")
        fields = ("NC_SYNTH_V1", str(root), "bfs-identity", family, str(n))
    else:
        raise ValueError("Unknown synthetic seed namespace")
    payload = "|".join(fields).encode("ascii")
    return int.from_bytes(sha256(payload).digest()[:8], "big")


def _seed(family: str, n: int, root: int = 20261009) -> int:
    """Backward-compatible generator seed; preserves existing fixture hashes."""
    return synthetic_seed(family, n, root=root)


def _connected(n: int, edges: set[Edge]) -> bool:
    adjacency = [set() for _ in range(n)]
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    seen = {0}
    todo = deque([0])
    while todo:
        for nxt in adjacency[todo.popleft()]:
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return len(seen) == n


def _er_like(n: int, rng: random.Random, target: int) -> set[Edge]:
    """Connected random-tree-plus-uniform-edges analogue; not exact ER."""
    e: set[Edge] = set()
    for j in range(1, n):
        e.add(_edge(j, rng.randrange(j)))
    while len(e) < target:
        u = rng.randrange(n)
        v = rng.randrange(n - 1)
        if v >= u:
            v += 1
        e.add(_edge(u, v))
    return e


def _ws_like(n: int, rng: random.Random) -> set[Edge]:
    """Ring lattice with 10% rewiring of non-ring edges; ring never broken."""
    edges: set[Edge] = {
        _edge(i, (i + step) % n)
        for i in range(n)
        for step in range(1, 9)
    }
    # Preserve distance-one cycle: guaranteed connectivity, unlike unconditioned WS.
    for i in range(n):
        for step in range(2, 9):
            if rng.random() >= 0.10:
                continue
            old = _edge(i, (i + step) % n)
            edges.remove(old)
            # Sample from all valid alternatives, uniformly conditional on i.
            candidates = [v for v in range(n) if v != i and _edge(i, v) not in edges]
            if not candidates:
                edges.add(old)
                continue
            edges.add(_edge(i, rng.choice(candidates)))
    return edges


def _ba_like(n: int, rng: random.Random) -> set[Edge]:
    """Degree-proportional attachment with m=8, seeded by a 9-clique."""
    m = 8
    edges = {_edge(i, j) for i in range(m + 1) for j in range(i + 1, m + 1)}
    # Each existing endpoint appears as many times as its current degree.
    tickets = [v for edge in sorted(edges) for v in edge]
    for new in range(m + 1, n):
        chosen: set[int] = set()
        while len(chosen) < m:
            chosen.add(rng.choice(tickets))
        for v in sorted(chosen):
            edges.add(_edge(new, v))
        tickets.extend(sorted(chosen))
        tickets.extend([new] * m)
    return edges



def _maximum_spanning_tree(scores) -> set[Edge]:
    """Maximum spanning tree with exact canonical-edge lexicographic ties.

    Takes a symmetric dense NumPy weight matrix with -inf diagonal. For
    each Prim frontier vertex, equal-weight parent candidates also resolve
    to the lexicographically smaller canonical edge. No epsilon ties.
    """
    import numpy as np

    n = int(scores.shape[0])
    if scores.shape != (n, n) or n < 2:
        raise ValueError("Scores must be a nontrivial square matrix")
    visited = np.zeros(n, dtype=bool)
    visited[0] = True
    best_score = scores[0].copy()
    best_score[0] = -np.inf
    parent = np.zeros(n, dtype=np.int32)
    edges: set[Edge] = set()
    for _ in range(n - 1):
        top = float(np.max(best_score))
        if not np.isfinite(top):
            raise AssertionError("Synthetic MST disconnected")
        tied = np.flatnonzero(best_score == top)
        j = int(min((int(v) for v in tied),
                    key=lambda v: _edge(int(parent[v]), v)))
        edges.add(_edge(int(parent[j]), j))
        visited[j] = True
        best_score[j] = -np.inf
        # For a fixed target vertex, lower parent ID is equivalent to the
        # lexicographically smaller canonical edge pair.
        improve = (~visited) & (
            (scores[j] > best_score) |
            ((scores[j] == best_score) & (j < parent))
        )
        best_score[improve] = scores[j, improve]
        parent[improve] = j
    return edges


def _factor_mst(n: int, seed: int, target: int) -> set[Edge]:
    """Dense six-factor synthetic covariance, maximum |correlation| tree + edges.

    Uses NumPy PCG64. O(N²) dense operations; ~300 MB transient arrays at N=3900.
    Not based on real RIKEN correlation or neuron data.
    """
    import numpy as np

    rng = np.random.default_rng(np.random.PCG64(seed))
    b = rng.standard_normal((n, FACTOR_COUNT))
    norms = np.sqrt((b * b).sum(axis=1) + 1.0)
    scores = np.abs((b @ b.T) / norms[:, None] / norms[None, :])
    np.fill_diagonal(scores, -np.inf)
    # Dense Prim. Tied maximum-weight *edges*, not merely tied vertex IDs,
    # are chosen lexicographically by canonical (min(u,v), max(u,v)) pair.
    edges = _maximum_spanning_tree(scores)
    upper = np.triu_indices(n, 1)
    values = scores[upper]
    k = min(len(values), target + n)
    if k == len(values):
        candidates = np.arange(len(values))
    else:
        candidates = np.argpartition(values, -k)[-k:]
    # If exact ties at the selection cutoff appear, deterministic choice would
    # need global lexicographic ranking: stop instead of silently tie-breaking.
    if k < len(values):
        boundary = values[candidates].min()
        if np.count_nonzero(values == boundary) > 1:
            raise ValueError("Ambiguous factor-MST top-edge cutoff tie")
    for idx in sorted(candidates, key=lambda i: (-float(values[i]), int(upper[0][i]), int(upper[1][i]))):
        if len(edges) >= target:
            break
        edges.add((int(upper[0][idx]), int(upper[1][idx])))
    if len(edges) != target:
        raise AssertionError("Incomplete synthetic top-edge selection")
    return edges


@dataclass(frozen=True)
class SyntheticGraph:
    n: int
    family: str
    seed: int
    edges: tuple[Edge, ...]

    @property
    def m(self) -> int:
        return len(self.edges)

    def fingerprint(self) -> str:
        payload = f"n={self.n}|family={self.family}|seed={self.seed}\n"
        payload += "\n".join(f"{u},{v}" for u, v in self.edges)
        return sha256(payload.encode("ascii")).hexdigest()


def make_synthetic_graph(n: int, family: str, *, root: int = 20261009) -> SyntheticGraph:
    if n < 18:
        raise ValueError("Synthetic NC-0a fixtures need N>=18, so mean degree 16 is achievable")
    seed = _seed(family, n, root)
    target = min(n * (n - 1) // 2, (TARGET_MEAN_DEGREE // 2) * n)
    if family == "er-like":
        edges = _er_like(n, random.Random(seed), target)
    elif family == "ws-like":
        edges = _ws_like(n, random.Random(seed))
    elif family == "ba-like":
        edges = _ba_like(n, random.Random(seed))
    elif family == "factor-mst":
        edges = _factor_mst(n, seed, target)
    else:
        raise ValueError("Unknown synthetic family")
    if len(edges) < n - 1 or not _connected(n, edges):
        raise AssertionError("Synthetic graph is not connected")
    if family in ("er-like", "ws-like", "factor-mst") and len(edges) != target:
        raise AssertionError("Unexpected synthetic edge target")
    return SyntheticGraph(n=n, family=family, seed=seed, edges=tuple(sorted(edges)))


def metrics(n: int, edges: Iterable[Edge], initial_edges: Iterable[Edge]) -> dict[str, float]:
    """Triangle count, degree assortativity, and initial edge overlap.

    Assortativity uses the Pearson correlation of endpoint degrees with both
    undirected orientations counted; zero variance => undefined (nan).
    """
    e = tuple(edges)
    base = set(initial_edges)
    a = [set() for _ in range(n)]
    for u, v in e:
        a[u].add(v)
        a[v].add(u)
    triangles = sum(sum(1 for w in (a[u] & a[v]) if w > v) for u, v in e)
    deg = [len(x) for x in a]
    m = len(e)
    mu = sum(deg[u] + deg[v] for u, v in e) / (2 * m)
    numerator = sum(deg[u] * deg[v] for u, v in e) / m - mu * mu
    denom = sum(deg[u] ** 2 + deg[v] ** 2 for u, v in e) / (2 * m) - mu * mu
    assort = numerator / denom if denom > 1e-13 else math.nan
    overlap = len(set(e) & base) / len(base)
    return {"triangles": float(triangles), "assortativity": float(assort), "edge_overlap": float(overlap)}
