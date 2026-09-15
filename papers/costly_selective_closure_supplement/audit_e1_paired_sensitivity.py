"""Post-hoc paired-sensitivity audit for the historical Experiment 1 results.

The original E1 result files were produced by `src/csc_experiment.py`, whose
`permutation_test` pools the two regime samples and performs a two-sided
label-permutation test. Because the same seeds were run in both regimes, v18
also reports a paired sign-flip sensitivity analysis on per-seed differences.

This script does NOT retrain agents and does NOT replace the historical test.
It reads only committed result JSON and prints both analyses side-by-side.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"
N_RESAMPLES = 20_000
RNG_SEED = 20260915


def paired_post_coop(result_file: str):
    payload = json.loads((RESULTS / result_file).read_text(encoding="utf-8"))
    seeds = payload["seeds"]
    by = {(r["regime"], r["seed"]): float(r["post_coop"]) for r in payload["runs"]}
    terminal = np.asarray([by[("real", s)] for s in seeds], dtype=float)
    restore = np.asarray([by[("resettable", s)] for s in seeds], dtype=float)
    historical = payload["tests"]["real_vs_resettable__post_coop"]
    return seeds, terminal, restore, historical


def paired_signflip_p(diffs: np.ndarray, *, n=N_RESAMPLES, seed=RNG_SEED) -> float:
    diffs = np.asarray(diffs, dtype=float)
    obs = float(diffs.mean())
    rng = np.random.default_rng(seed)
    signs = rng.choice(np.asarray([-1.0, 1.0]), size=(n, len(diffs)))
    stats = (signs * diffs).mean(axis=1)
    return float((np.sum(np.abs(stats) >= abs(obs) - 1e-12) + 1) / (n + 1))


def audit(result_file: str) -> dict:
    seeds, terminal, restore, historical = paired_post_coop(result_file)
    diffs = terminal - restore
    return {
        "result_file": result_file,
        "n_paired_seeds": len(seeds),
        "historical_test": "two-sided two-sample label permutation",
        "historical_mean_difference": float(historical["diff"]),
        "historical_p": float(historical["p"]),
        "paired_sensitivity_test": "two-sided paired sign-flip permutation",
        "paired_mean_difference": float(diffs.mean()),
        "paired_signflip_p": paired_signflip_p(diffs),
        "positive_paired_differences": int(np.sum(diffs > 0)),
        "zero_paired_differences": int(np.sum(diffs == 0)),
        "negative_paired_differences": int(np.sum(diffs < 0)),
        "resamples": N_RESAMPLES,
        "rng_seed": RNG_SEED,
    }


def main() -> None:
    for name in ["main_results.json", "zero_penalty_results.json"]:
        out = audit(name)
        print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
