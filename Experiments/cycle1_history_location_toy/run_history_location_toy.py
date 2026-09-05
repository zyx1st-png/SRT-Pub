"""Cycle 1 history-location toy model.

Purpose
-------
Demonstrate logical / causal separability of two historical carriers after one
shared training history:

    H_M : field / multiplicity-side retained consequence
    H_1 : candidate-One-side retained adaptive state

This is a toy coherence test. It is NOT empirical evidence for SRT ontology and
it does not define Bearer identity.

The same trained agent/field pair is forked into four test conditions:

    00  reset field history, reset agent history
    10  preserve field history, reset agent history
    01  reset field history, preserve agent history
    11  preserve field history, preserve agent history

The useful prediction is a temporal crossing:

    01 starts history-conditioned immediately but can recover after field reset;
    10 starts like a fresh agent but becomes history-conditioned after
       re-contact with the historically changed field.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent

TRAIN_STEPS = 250
TEST_STEPS = 160
EARLY_WINDOW = 20
LATE_WINDOW = 40
ALPHA = 0.12
TEMPERATURE = 0.25
FIELD_INCREMENT = 0.012
NOISE_SD = 0.08
BASE_REWARD_A = 1.25
BASE_REWARD_B = 1.00
FIELD_PENALTY_SCALE = 1.25
SEEDS = list(range(1, 31))
N_SIGNFLIP = 20_000
SIGNFLIP_SEED = 20260905

CONDITIONS = {
    "00": (False, False),  # preserve H_M?, preserve H_1?
    "10": (True, False),
    "01": (False, True),
    "11": (True, True),
}


def softmax(q: np.ndarray) -> np.ndarray:
    z = np.asarray(q, dtype=float) / TEMPERATURE
    z = z - np.max(z)
    ez = np.exp(z)
    return ez / ez.sum()


def train_shared_history(seed: int) -> tuple[np.ndarray, float]:
    """Create both an external field trace and an internal adaptive trace.

    Action A is initially better than B, but choosing A progressively scars the
    external field. The same consequences also update the agent's Q values.

    External field scar = toy H_M carrier.
    Learned Q vector      = toy H_1 carrier.
    """
    rng = np.random.default_rng(seed)
    q = np.array([0.0, 0.0], dtype=float)
    field_hazard = 0.0

    for _ in range(TRAIN_STEPS):
        p = softmax(q)
        action = int(rng.choice(2, p=p))

        if action == 0:
            # The Selection itself alters the future field: a toy form of
            # multiplicity-side sedimentation.
            field_hazard = min(1.0, field_hazard + FIELD_INCREMENT)
            reward = (
                BASE_REWARD_A
                - FIELD_PENALTY_SCALE * field_hazard
                + rng.normal(0.0, NOISE_SD)
            )
        else:
            reward = BASE_REWARD_B + rng.normal(0.0, NOISE_SD)

        q[action] += ALPHA * (reward - q[action])

    return q.copy(), float(field_hazard)


def probe(
    q0: np.ndarray,
    field_hazard: float,
    seed: int,
) -> dict[str, float]:
    """Probe a fork while allowing ordinary within-test learning.

    The retained field hazard is held fixed during the probe. This isolates the
    effect of the historical field carrier rather than adding further H_M write.
    """
    rng = np.random.default_rng(seed)
    q = q0.copy()

    initial_p_a = float(softmax(q)[0])
    p_a_trace: list[float] = []
    action_trace: list[int] = []
    reward_trace: list[float] = []

    for _ in range(TEST_STEPS):
        p = softmax(q)
        p_a_trace.append(float(p[0]))
        action = int(rng.choice(2, p=p))
        action_trace.append(action)

        if action == 0:
            reward = (
                BASE_REWARD_A
                - FIELD_PENALTY_SCALE * field_hazard
                + rng.normal(0.0, NOISE_SD)
            )
        else:
            reward = BASE_REWARD_B + rng.normal(0.0, NOISE_SD)

        reward_trace.append(float(reward))
        q[action] += ALPHA * (reward - q[action])

    actions = np.asarray(action_trace)
    return {
        "initial_pA": initial_p_a,
        "early_pA": float(np.mean(p_a_trace[:EARLY_WINDOW])),
        "late_pA": float(np.mean(p_a_trace[-LATE_WINDOW:])),
        "early_A_rate": float(np.mean(actions[:EARLY_WINDOW] == 0)),
        "late_A_rate": float(np.mean(actions[-LATE_WINDOW:] == 0)),
        "mean_reward": float(np.mean(reward_trace)),
    }


def paired_signflip_p(diffs: np.ndarray) -> float:
    diffs = np.asarray(diffs, dtype=float)
    obs = float(np.mean(diffs))
    if np.allclose(diffs, 0.0):
        return 1.0
    rng = np.random.default_rng(SIGNFLIP_SEED)
    signs = rng.choice([-1.0, 1.0], size=(N_SIGNFLIP, len(diffs)))
    null = np.mean(signs * diffs, axis=1)
    return float((np.sum(np.abs(null) >= abs(obs) - 1e-12) + 1) / (N_SIGNFLIP + 1))


def run() -> dict:
    rows: list[dict] = []

    for seed in SEEDS:
        trained_q, trained_field = train_shared_history(seed)

        for condition, (keep_m, keep_one) in CONDITIONS.items():
            q0 = trained_q.copy() if keep_one else np.array([0.0, 0.0])
            field0 = trained_field if keep_m else 0.0
            result = probe(q0, field0, seed=10_000 + seed)
            rows.append(
                {
                    "seed": seed,
                    "condition": condition,
                    "train_field": trained_field,
                    "train_qA": float(trained_q[0]),
                    "train_qB": float(trained_q[1]),
                    **result,
                }
            )

    metrics = ["initial_pA", "early_pA", "late_pA", "mean_reward"]
    summary: dict[str, dict] = {}

    for condition in CONDITIONS:
        rs = [r for r in rows if r["condition"] == condition]
        summary[condition] = {
            metric: float(np.mean([r[metric] for r in rs]))
            for metric in metrics
        }
        summary[condition]["mean_train_field"] = float(
            np.mean([r["train_field"] for r in rs])
        )

    paired: dict[str, dict] = {}
    for left, right in [
        ("01", "00"),
        ("10", "00"),
        ("11", "10"),
        ("11", "01"),
        ("10", "01"),
    ]:
        key = f"{left}-{right}"
        paired[key] = {}
        lrows = sorted(
            [r for r in rows if r["condition"] == left], key=lambda x: x["seed"]
        )
        rrows = sorted(
            [r for r in rows if r["condition"] == right], key=lambda x: x["seed"]
        )
        for metric in metrics:
            diffs = np.array(
                [a[metric] - b[metric] for a, b in zip(lrows, rrows)], dtype=float
            )
            paired[key][metric] = {
                "mean_diff": float(np.mean(diffs)),
                "paired_signflip_p": paired_signflip_p(diffs),
            }

    report = {
        "status": "toy_coherence_result_not_empirical_support",
        "parameters": {
            "train_steps": TRAIN_STEPS,
            "test_steps": TEST_STEPS,
            "early_window": EARLY_WINDOW,
            "late_window": LATE_WINDOW,
            "alpha": ALPHA,
            "temperature": TEMPERATURE,
            "field_increment": FIELD_INCREMENT,
            "noise_sd": NOISE_SD,
            "base_reward_A": BASE_REWARD_A,
            "base_reward_B": BASE_REWARD_B,
            "field_penalty_scale": FIELD_PENALTY_SCALE,
            "seeds": SEEDS,
            "n_signflip": N_SIGNFLIP,
            "signflip_seed": SIGNFLIP_SEED,
        },
        "condition_key": {
            "00": "reset H_M; reset H_1",
            "10": "preserve H_M; reset H_1",
            "01": "reset H_M; preserve H_1",
            "11": "preserve H_M; preserve H_1",
        },
        "summary": summary,
        "paired": paired,
        "raw": rows,
    }

    out = ROOT / "results_summary.json"
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


if __name__ == "__main__":
    run()
