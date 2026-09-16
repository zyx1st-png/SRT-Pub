"""Reproduce the post-hoc E4 individual-scope latency cross-check.

This script reads only the frozen 90-row derivative preserved in
results/consequence_scope_E4_individual_latency_exploratory.json. It performs
no training and must not be used to relabel this analysis as confirmatory.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RECORD = HERE / "results" / "consequence_scope_E4_individual_latency_exploratory.json"
LATENCIES = (2, 5, 10)
SEEDS = tuple(range(101, 131))
N_PERM = 20_000


def rankdata(values: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty(len(values), dtype=float)
    i = 0
    while i < len(values):
        j = i + 1
        while j < len(values) and values[order[j]] == values[order[i]]:
            j += 1
        ranks[order[i:j]] = (i + 1 + j) / 2.0
        i = j
    return ranks


def pearson(a: np.ndarray, b: np.ndarray) -> float:
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    ac = a - a.mean()
    bc = b - b.mean()
    denom = float(np.sqrt(np.sum(ac * ac) * np.sum(bc * bc)))
    return 0.0 if denom <= 0 else float(np.sum(ac * bc) / denom)


def blocked_spearman(matrix: np.ndarray, *, permutation_seed: int) -> tuple[float, float]:
    matrix = np.asarray(matrix, dtype=float)
    if matrix.shape != (len(SEEDS), len(LATENCIES)):
        raise ValueError(f"unexpected matrix shape: {matrix.shape}")

    x = np.tile(np.arange(len(LATENCIES), dtype=float), len(SEEDS))
    x_rank = rankdata(x)
    y_rank = rankdata(matrix.reshape(-1)).reshape(len(SEEDS), len(LATENCIES))
    observed = pearson(x_rank, y_rank.reshape(-1))

    xc = x_rank - x_rank.mean()
    y_flat = y_rank.reshape(-1)
    y_mean = y_flat.mean()
    denom = float(np.sqrt(np.sum(xc * xc) * np.sum((y_flat - y_mean) ** 2)))

    rng = np.random.default_rng(permutation_seed)
    count = 0
    for _ in range(N_PERM):
        permuted = np.empty_like(y_rank)
        for s in range(len(SEEDS)):
            permuted[s] = y_rank[s, rng.permutation(len(LATENCIES))]
        stat = float(np.sum(xc * (permuted.reshape(-1) - y_mean)) / denom)
        if abs(stat) >= abs(observed) - 1e-12:
            count += 1
    return observed, float((count + 1) / (N_PERM + 1))


def matrix_from_rows(rows: list[dict], key: str) -> np.ndarray:
    lookup = {(int(r["seed"]), int(r["latency"])): float(r[key]) for r in rows}
    expected = {(seed, latency) for seed in SEEDS for latency in LATENCIES}
    if set(lookup) != expected:
        missing = sorted(expected - set(lookup))
        extra = sorted(set(lookup) - expected)
        raise RuntimeError(f"row structure mismatch; missing={missing[:5]} extra={extra[:5]}")
    return np.array([[lookup[(seed, latency)] for latency in LATENCIES] for seed in SEEDS], dtype=float)


def summarize(matrix: np.ndarray) -> dict:
    return {
        str(latency): {
            "mean": float(matrix[:, i].mean()),
            "median": float(np.median(matrix[:, i])),
            "n_gt_0_5": int(np.sum(matrix[:, i] > 0.5)),
            "n": int(matrix.shape[0]),
        }
        for i, latency in enumerate(LATENCIES)
    }


def assert_close(actual: float, expected: float, tol=1e-12) -> None:
    if abs(actual - expected) > tol:
        raise AssertionError(f"mismatch: actual={actual} expected={expected}")


def main() -> None:
    record = json.loads(RECORD.read_text(encoding="utf-8"))
    if record["confirmatory_status"] != "exploratory only; not preregistered; does not alter E4 confirmatory adjudication":
        raise RuntimeError("exploratory-status guard changed")

    rows = record["rows"]
    if len(rows) != 90:
        raise RuntimeError(f"expected 90 rows, found {len(rows)}")

    primary = matrix_from_rows(rows, "expected_mutual_coop")
    rollout = matrix_from_rows(rows, "post_coop")

    primary_summary = summarize(primary)
    rollout_summary = summarize(rollout)
    primary_rho, primary_p = blocked_spearman(primary, permutation_seed=record["primary_common_state"]["permutation_seed"])
    rollout_rho, rollout_p = blocked_spearman(rollout, permutation_seed=record["secondary_rollout"]["permutation_seed"])

    for latency in map(str, LATENCIES):
        for key in ("mean", "median"):
            assert_close(primary_summary[latency][key], record["primary_common_state"]["condition_summaries"][latency][key])
            assert_close(rollout_summary[latency][key], record["secondary_rollout"]["condition_summaries"][latency][key])
        if primary_summary[latency]["n_gt_0_5"] != record["primary_common_state"]["condition_summaries"][latency]["n_gt_0_5"]:
            raise AssertionError("primary attractor-count mismatch")
        if rollout_summary[latency]["n_gt_0_5"] != record["secondary_rollout"]["condition_summaries"][latency]["n_gt_0_5"]:
            raise AssertionError("rollout attractor-count mismatch")

    assert_close(primary_rho, record["primary_common_state"]["blocked_by_seed_tie_aware_spearman_rho"])
    assert_close(primary_p, record["primary_common_state"]["two_sided_permutation_p"])
    assert_close(rollout_rho, record["secondary_rollout"]["blocked_by_seed_tie_aware_spearman_rho"])
    assert_close(rollout_p, record["secondary_rollout"]["two_sided_permutation_p"])

    print("E4 individual-scope exploratory cross-check: PASS")
    print("primary rho/p:", primary_rho, primary_p)
    print("rollout rho/p:", rollout_rho, rollout_p)


if __name__ == "__main__":
    main()
