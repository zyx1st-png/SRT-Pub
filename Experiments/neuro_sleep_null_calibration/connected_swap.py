"""Proposed G0 connected degree-preserving swap kernel (draft, synthetic tests only).

No real RIKEN inputs or experiment execution are implemented here.
The sampler is *procedure-defined* and is not asserted to sample uniformly
from connected graphs with the supplied degree sequence.

Spec owner: Experiments/SRT_NEURO_SLEEP_POPULATION_NULL_CALIBRATION_PREREGISTRATION_2026-10-09.md
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from hashlib import sha256
import random
from typing import Iterable, Sequence


Edge = tuple[int, int]


def normalize_edge(u: int, v: int) -> Edge:
    if u == v:
        raise ValueError("Self loops are not allowed")
    return (u, v) if u < v else (v, u)


@dataclass(frozen=True)
class SwapStats:
    attempts: int
    accepted: int
    rejected_overlap: int
    rejected_duplicate: int
    rejected_disconnect: int
    proposal_seed: int

    @property
    def rejection_count(self) -> int:
        return self.rejected_overlap + self.rejected_duplicate + self.rejected_disconnect


class ConnectedDegreeSwap:
    """Mutable simple labeled graph with a deterministic proposal-index stream.

    Nodes are the consecutive integers 0..n-1; this constraint is explicit,
    because label normalization would change the intended neural-ID map.
    Each proposal samples two distinct edge *slots* uniformly and a 1-bit
    cross-pairing choice uniformly, then either accepts or stays in place.
    """

    def __init__(self, n: int, edges: Iterable[Edge]) -> None:
        if n < 4:
            raise ValueError("At least four nodes are required")
        normalized: list[Edge] = []
        for u, v in edges:
            if type(u) is not int or type(v) is not int or not (0 <= u < n and 0 <= v < n):
                raise ValueError("Node IDs must be ordinary integers in [0,n)")
            normalized.append(normalize_edge(u, v))
        if len(set(normalized)) != len(normalized):
            raise ValueError("Duplicate edges are not allowed")
        if len(normalized) < n - 1:
            raise ValueError("Too few edges to connect all nodes")
        # Canonical edge-slot order is part of the deterministic implementation.
        self.edges = sorted(normalized)
        self.n = n
        self.adj = [set() for _ in range(n)]
        for u, v in self.edges:
            self.adj[u].add(v)
            self.adj[v].add(u)
        if not self.full_connected():
            raise ValueError("Input graph must be connected")
        self.initial_degrees = tuple(map(len, self.adj))
        self.attempts = self.accepted = 0
        self.rejected_overlap = self.rejected_duplicate = self.rejected_disconnect = 0

    @property
    def m(self) -> int:
        return len(self.edges)

    def full_connected(self) -> bool:
        seen = {0}
        q = deque([0])
        while q:
            u = q.popleft()
            for v in self.adj[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        return len(seen) == self.n

    def endpoints_connected(self, four: Sequence[int]) -> bool:
        """Equivalent to full connectivity after a valid 2-edge swap.

        Precondition: prior graph connected, the only changes are two removed
        edges and two added edges, and all four endpoints distinct.
        Every possible new component must contain at least one endpoint.
        """
        a, b, c, d = four
        targets = {b, c, d}
        seen = {a}
        q = deque([a])
        while q and targets:
            u = q.popleft()
            for v in self.adj[u]:
                if v not in seen:
                    seen.add(v)
                    targets.discard(v)
                    if not targets:
                        return True
                    q.append(v)
        return not targets

    def _erase(self, e: Edge) -> None:
        u, v = e
        self.adj[u].remove(v)
        self.adj[v].remove(u)

    def _insert(self, e: Edge) -> None:
        u, v = e
        self.adj[u].add(v)
        self.adj[v].add(u)

    def assert_accepted_swap_local(self, old1: Edge, old2: Edge,
                                   new1: Edge, new2: Edge,
                                   slots: tuple[int, int]) -> None:
        """O(local touched-degree) audit for one just-accepted two-edge switch.

        Induction: if the input graph was simple, undirected and had the
        original degree sequence, the only four vertices and two edge slots
        modified by a legal swap suffice to check the same invariants afterward.
        Full-graph *connectivity* still gets checked at fixed checkpoints.
        """
        i, j = slots
        if i == j or new1 == new2 or old1 == old2:
            raise AssertionError("Invalid two-edge swap slots")
        if self.edges[i] != new1 or self.edges[j] != new2:
            raise AssertionError("Accepted edge slots do not match proposal")
        touched = {x for e in (old1, old2) for x in e}
        if len(touched) != 4 or set(new1 + new2) != touched:
            raise AssertionError("Accepted swap did not preserve endpoints")
        if self.m < self.n - 1:
            raise AssertionError("Accepted graph edge count invalid")
        for u in touched:
            if len(self.adj[u]) != self.initial_degrees[u]:
                raise AssertionError("Accepted swap changed degree")
        for u, v in (old1, old2):
            if v in self.adj[u] or u in self.adj[v]:
                raise AssertionError("Old accepted edge still present")
        for u, v in (new1, new2):
            if u >= v or v not in self.adj[u] or u not in self.adj[v]:
                raise AssertionError("New accepted edge missing or asymmetric")

    def propose(self, rng: random.Random, *, oracle: bool = False,
                audit_local: bool = False) -> bool:
        """Try one move. Rejection counts as one chain step (stay put).

        When oracle=True, verify the short BFS decision with full connectivity
        on each tentative graph; intended for small synthetic unit tests only.
        """
        self.attempts += 1
        i = rng.randrange(self.m)
        j = rng.randrange(self.m - 1)
        if j >= i:
            j += 1
        a, b = self.edges[i]
        c, d = self.edges[j]
        orientation = rng.randrange(2)
        if len({a, b, c, d}) < 4:
            self.rejected_overlap += 1
            return False
        if orientation == 0:
            e1, e2 = normalize_edge(a, c), normalize_edge(b, d)
        else:
            e1, e2 = normalize_edge(a, d), normalize_edge(b, c)
        if e1[1] in self.adj[e1[0]] or e2[1] in self.adj[e2[0]]:
            self.rejected_duplicate += 1
            return False

        orig1, orig2 = self.edges[i], self.edges[j]
        self._erase(orig1)
        self._erase(orig2)
        self._insert(e1)
        self._insert(e2)
        local_ok = self.endpoints_connected((a, b, c, d))
        if oracle and local_ok != self.full_connected():
            raise AssertionError("Endpoint BFS and full graph connectivity disagree")
        if local_ok:
            self.edges[i] = e1
            self.edges[j] = e2
            self.accepted += 1
            if audit_local:
                self.assert_accepted_swap_local(orig1, orig2, e1, e2, (i, j))
            return True
        self._erase(e1)
        self._erase(e2)
        self._insert(orig1)
        self._insert(orig2)
        self.rejected_disconnect += 1
        return False

    def fingerprint(self) -> str:
        payload = "\n".join(f"{u},{v}" for u, v in sorted(self.edges))
        return sha256((f"n={self.n}\n" + payload + "\n").encode("utf-8")).hexdigest()

    def assert_invariants(self) -> None:
        if len(self.edges) != len(set(self.edges)) or any(u >= v for u, v in self.edges):
            raise AssertionError("Edge list is not simple and canonical")
        if tuple(map(len, self.adj)) != self.initial_degrees:
            raise AssertionError("Degree sequence changed")
        for u, v in self.edges:
            if u not in self.adj[v] or v not in self.adj[u]:
                raise AssertionError("Adjacency/edge-list mismatch")
        if sum(map(len, self.adj)) != 2 * len(self.edges):
            raise AssertionError("Edge count changed")
        if not self.full_connected():
            raise AssertionError("Connectivity was lost")

    def stats(self, seed: int) -> SwapStats:
        return SwapStats(
            attempts=self.attempts, accepted=self.accepted,
            rejected_overlap=self.rejected_overlap,
            rejected_duplicate=self.rejected_duplicate,
            rejected_disconnect=self.rejected_disconnect,
            proposal_seed=seed,
        )


def run_chain(n: int, edges: Iterable[Edge], seed: int, attempts: int,
              checkpoints: Sequence[int] = (), *, oracle: bool = False
              ) -> tuple[ConnectedDegreeSwap, dict[int, dict[str, object]]]:
    """Run fixed attempted proposals, saving only preselected audit snapshots.

    Must not be called on biological data before NC-0 freeze. The optional
    oracle flag is strictly for synthetic tests and adds a full BFS per proposal.
    """
    if attempts < 0:
        raise ValueError("attempts must be nonnegative")
    if any(t < 1 or t > attempts for t in checkpoints):
        raise ValueError("checkpoints must fall within (0, attempts]")
    graph = ConnectedDegreeSwap(n, edges)
    rng = random.Random(seed)
    selected = set(checkpoints)
    snapshots: dict[int, dict[str, object]] = {}
    for t in range(1, attempts + 1):
        graph.propose(rng, oracle=oracle)
        if t in selected:
            graph.assert_invariants()
            snapshots[t] = {"graph_sha256": graph.fingerprint(),
                            "attempts": t, "accepted": graph.accepted,
                            "rejection_count": t - graph.accepted}
    graph.assert_invariants()
    if graph.attempts != graph.accepted + graph.rejected_overlap + graph.rejected_duplicate + graph.rejected_disconnect:
        raise AssertionError("Attempt accounting broken")
    return graph, snapshots
