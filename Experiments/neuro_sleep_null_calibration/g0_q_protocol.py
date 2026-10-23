"""Prospective common Louvain-Q contract for observed and G0 null graphs.

CANONICAL_SORTED_EDGE_V1 is a candidate method amendment, not an execution
authorization. Biological node labels must be the stable original neuron
indices, not temporary positions in an input list.
"""

from __future__ import annotations

import hashlib
import importlib.metadata
import json
import math
import struct
from collections.abc import Iterable, Sequence
from typing import Any

CANONICAL_ORDER_POLICY = "CANONICAL_SORTED_EDGE_V1"
LOUVAIN_TRIALS = 200


def _canonical_json(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_graph_payload(nodes: Sequence[int],
                            edges: Iterable[tuple[int, int]]) -> dict[str, Any]:
    """Return the policy's validated, identity-bound node/edge insertion plan."""
    node_values = tuple(nodes)
    if len(node_values) < 2 or any(type(node) is not int or node < 0
                                  for node in node_values):
        raise ValueError("Canonical source nodes must be nonnegative original integer indices")
    if len(set(node_values)) != len(node_values):
        raise ValueError("Canonical source node indices must be unique")
    ordered_nodes = tuple(sorted(node_values))
    node_set = set(ordered_nodes)
    edge_values: set[tuple[int, int]] = set()
    for edge in edges:
        if not isinstance(edge, (tuple, list)) or len(edge) != 2:
            raise ValueError("Each canonical edge must contain exactly two node indices")
        u, v = edge
        if type(u) is not int or type(v) is not int or u not in node_set or v not in node_set:
            raise ValueError("Canonical edge endpoint is not a declared original node index")
        if u == v:
            raise ValueError("Canonical Louvain graph cannot contain self loops")
        pair = (u, v) if u < v else (v, u)
        if pair in edge_values:
            raise ValueError("Canonical Louvain graph cannot contain duplicate edges")
        edge_values.add(pair)
    ordered_edges = tuple(sorted(edge_values))
    if not ordered_edges:
        raise ValueError("Canonical Louvain graph requires at least one edge")
    return {
        "policy": CANONICAL_ORDER_POLICY,
        "nodes": ordered_nodes,
        "edges": ordered_edges,
        "weight": 1.0,
    }


def build_canonical_louvain_graph(nodes: Sequence[int],
                                  edges: Iterable[tuple[int, int]]):
    """Build NetworkX graph: original IDs ascending, then normalized edges lexicographic."""
    import networkx as nx

    payload = canonical_graph_payload(nodes, edges)
    graph = nx.Graph()
    graph.add_nodes_from(payload["nodes"])
    graph.add_weighted_edges_from(
        (u, v, 1.0) for u, v in payload["edges"])
    if graph.number_of_nodes() != len(payload["nodes"]):
        raise ValueError("Canonical graph node count changed during construction")
    if graph.number_of_edges() != len(payload["edges"]):
        raise ValueError("Canonical graph edge count changed during construction")
    if not nx.is_connected(graph):
        raise ValueError("Canonical Louvain graph must be connected")
    return graph, canonical_graph_manifest(payload, graph)


def canonical_graph_manifest(payload: dict[str, Any], graph=None) -> dict[str, Any]:
    """Hash topology and the exact ordered representation separately."""
    ordered_nodes = tuple(payload["nodes"])
    ordered_edges = tuple(payload["edges"])
    adjacency = {node: [] for node in ordered_nodes}
    for u, v in ordered_edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    expected_adjacency = [[node, adjacency[node]] for node in ordered_nodes]
    if graph is not None:
        actual_adjacency = [[node, list(graph.neighbors(node))]
                            for node in graph.nodes]
        if tuple(graph.nodes) != ordered_nodes or actual_adjacency != expected_adjacency:
            raise ValueError("NetworkX insertion order differs from canonical payload")
    topology = {
        "nodes": list(ordered_nodes),
        "edges": [list(edge) for edge in ordered_edges],
        "weight": 1.0,
    }
    ordered = {
        "policy": CANONICAL_ORDER_POLICY,
        "nodes_in_insertion_order": list(ordered_nodes),
        "edges_in_insertion_order": [list(edge) for edge in ordered_edges],
        "weight": 1.0,
        "adjacency_iteration": expected_adjacency,
    }
    return {
        "order_policy": CANONICAL_ORDER_POLICY,
        "node_count": len(ordered_nodes),
        "edge_count": len(ordered_edges),
        "weight": 1.0,
        "topology_sha256": _sha256(_canonical_json(topology)),
        "ordered_representation_sha256": _sha256(_canonical_json(ordered)),
    }




def seed_vector_sha256(seeds: Iterable[int]) -> str:
    values = tuple(seeds)
    if any(type(seed) is not int or not 0 <= seed <= (2**63 - 1)
           for seed in values):
        raise ValueError("Canonical Louvain seeds must be signed-int64 nonnegative values")
    return _sha256(b"".join(struct.pack("<q", seed) for seed in values))


def q_vector_sha256(q_values: Iterable[float]) -> str:
    values = tuple(float(value) for value in q_values)
    if any(not math.isfinite(value) for value in values):
        raise ValueError("Canonical Q vector must contain only finite values")
    return _sha256(b"".join(struct.pack("<d", value) for value in values))


def first_maximum_index(q_values: Sequence[float]) -> int:
    """Return the first index attaining the maximum of a finite nonempty vector."""
    values = tuple(float(value) for value in q_values)
    if not values or any(not math.isfinite(value) for value in values):
        raise ValueError("Q vector must be nonempty and finite")
    return max(range(len(values)), key=values.__getitem__)


def validate_louvain_runtime() -> None:
    try:
        version = importlib.metadata.version("python-louvain")
    except importlib.metadata.PackageNotFoundError as exc:
        raise RuntimeError("python-louvain is not installed") from exc
    if version != "0.16":
        raise RuntimeError(f"CANONICAL_SORTED_EDGE_V1 requires python-louvain 0.16, got {version}")


def louvain_partition_q_for_seed(graph, seed: int):
    if type(seed) is not int or seed < 0:
        raise ValueError("Louvain seeds must be nonnegative integers")
    from community import community_louvain

    partition = community_louvain.best_partition(
        graph, weight="weight", resolution=1.0, random_state=seed)
    q_value = float(community_louvain.modularity(
        partition, graph, weight="weight"))
    if not math.isfinite(q_value):
        raise ValueError("Louvain returned nonfinite modularity")
    return partition, q_value


def canonical_partition_encoding(nodes: Sequence[int], partition: dict) -> list[int]:
    """Encode a partition by canonical node position, independent of community labels."""
    groups: dict[object, list[int]] = {}
    node_set = set(nodes)
    for index, node in enumerate(nodes):
        if node not in partition:
            raise ValueError("Louvain partition omits a canonical graph node")
        groups.setdefault(partition[node], []).append(index)
    if any(node not in node_set for node in partition):
        raise ValueError("Louvain partition contains an unknown graph node")
    ordered_groups = sorted(groups.values(), key=lambda members: min(members))
    encoded = [0] * len(nodes)
    for community_id, members in enumerate(ordered_groups):
        for index in members:
            encoded[index] = community_id
    return encoded


def heuristic_diagnostics(q_values: Sequence[float],
                          partition_sha256: Sequence[str]) -> dict[str, Any]:
    """Descriptive finite-restart diagnostics; none alter the Qmax endpoint."""
    if len(q_values) != LOUVAIN_TRIALS or len(partition_sha256) != LOUVAIN_TRIALS:
        raise ValueError("Heuristic diagnostics require exactly 200 aligned trials")
    prefixes = (50, 100, 150, 200)
    return {
        "prefix_max_q": {str(size): max(q_values[:size]) for size in prefixes},
        "distinct_partition_count": len(set(partition_sha256)),
    }


def louvain_q_for_seed(graph, seed: int) -> float:
    return louvain_partition_q_for_seed(graph, seed)[1]


def canonical_louvain_q_vector(nodes: Sequence[int],
                               edges: Iterable[tuple[int, int]],
                               seeds: Iterable[int]) -> dict[str, Any]:
    """Run the fixed 200-seed Q vector on the canonical graph representation."""
    seed_values = tuple(seeds)
    if len(seed_values) != LOUVAIN_TRIALS:
        raise ValueError("The canonical primary Q statistic requires exactly 200 seeds")
    if any(type(seed) is not int or not 0 <= seed <= (2**63 - 1)
           for seed in seed_values):
        raise ValueError("Canonical Louvain seeds must be signed-int64 nonnegative values")
    validate_louvain_runtime()
    graph, manifest = build_canonical_louvain_graph(nodes, edges)
    q_values = []
    partition_hashes = []
    canonical_nodes = tuple(graph.nodes)
    for seed in seed_values:
        partition, q_value = louvain_partition_q_for_seed(graph, seed)
        q_values.append(q_value)
        encoded = canonical_partition_encoding(canonical_nodes, partition)
        partition_hashes.append(_sha256(_canonical_json(encoded)))
    first_max_index = first_maximum_index(q_values)
    return {
        **manifest,
        "algorithm": "community.community_louvain.best_partition",
        "q_function": "community.community_louvain.modularity",
        "python_louvain_version": "0.16",
        "resolution": 1.0,
        "seed_count": LOUVAIN_TRIALS,
        "seed_vector_sha256": seed_vector_sha256(seed_values),
        "q_values": q_values,
        "q_vector_sha256": q_vector_sha256(q_values),
        "partition_sha256": partition_hashes,
        "heuristic_diagnostics": heuristic_diagnostics(q_values, partition_hashes),
        "q_max_200": q_values[first_max_index],
        "first_max_trial_index": first_max_index,
    }
