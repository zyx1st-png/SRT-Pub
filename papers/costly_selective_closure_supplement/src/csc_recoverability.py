"""Preregistered CSC Experiment 2: non-terminal recoverability gradient.

This module intentionally reuses the Experiment 1 policy, reward matrix, energy
matrix, observation specification, and training schedule. All Experiment 2
conditions use a fixed 50-step horizon and identical immediate rescue on
energy depletion. The only condition parameter is how long a fixed metabolic-
efficiency damage state persists after depletion.

Locked design: see ../EXPERIMENT2_RECOVERABILITY_PREREGISTRATION.md
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import numpy as np

import csc_experiment as ce

ROOT = Path(__file__).resolve().parent

DAMAGE_MULTIPLIER = 0.75
FAILURE_PENALTY = 0.0
PERMUTATION_SEED = 20260915
BOOTSTRAP_SEED = 20260916
N_PERMUTATIONS = 20_000
N_BOOTSTRAP = 10_000

# None means damage remains active for the remainder of the episode-token.
RECOVERY_DURATIONS: dict[str, Optional[int]] = {
    "tau0": 0,
    "tau5": 5,
    "tau15": 15,
    "tau_inf": None,
}
CONDITION_ORDER = ["tau0", "tau5", "tau15", "tau_inf"]


@dataclass
class RecoverabilityEnv:
    recovery_duration: Optional[int]
    rng: np.random.Generator
    energy: np.ndarray = field(default_factory=lambda: np.array([ce.E_0, ce.E_0], dtype=float))
    alive: np.ndarray = field(default_factory=lambda: np.array([1, 1], dtype=int))
    last_action: np.ndarray = field(default_factory=lambda: np.array([2, 2], dtype=int))
    last_fail: np.ndarray = field(default_factory=lambda: np.array([0, 0], dtype=int))
    step_idx: int = 0
    mortality_seen: int = 0
    # 0 = undamaged; positive integer = finite remaining damaged steps;
    # -1 = damaged for the remainder of the current episode-token.
    damage_remaining: np.ndarray = field(default_factory=lambda: np.array([0, 0], dtype=int))
    damaged_agent_steps: int = 0

    def reset(self):
        self.energy = np.array([ce.E_0, ce.E_0], dtype=float)
        self.alive = np.array([1, 1], dtype=int)
        self.last_action = np.array([2, 2], dtype=int)
        self.last_fail = np.array([0, 0], dtype=int)
        self.step_idx = 0
        self.mortality_seen = 0
        self.damage_remaining = np.array([0, 0], dtype=int)
        self.damaged_agent_steps = 0

    def obs(self, i):
        """Keep the Experiment 1 12-feature observation specification unchanged."""
        j = 1 - i
        return np.array([
            1.0,
            self.energy[i] / ce.E_MAX,
            self.energy[j] / ce.E_MAX,
            1.0 if self.energy[i] <= 2.0 else 0.0,
            1.0 if self.energy[j] <= 2.0 else 0.0,
            1.0 if self.last_action[j] == 0 else 0.0,
            1.0 if self.last_action[j] == 1 else 0.0,
            float(self.last_fail[i]),
            float(self.last_fail[j]),
            1.0 - self.step_idx / ce.T_HORIZON,
            float(self.mortality_seen),
            1.0 if self.last_action[i] == 0 else 0.0,
        ], dtype=float)

    def gain_multiplier(self, i: int) -> float:
        return DAMAGE_MULTIPLIER if self.damage_remaining[i] != 0 else 1.0

    def _activate_damage(self, i: int):
        if self.recovery_duration is None:
            self.damage_remaining[i] = -1
        else:
            self.damage_remaining[i] = int(self.recovery_duration)

    def step(self, actions, bonus_active):
        rewards = np.zeros(2, dtype=float)
        self.last_fail[:] = 0

        # Damage is counted when it actually changes this step's energy gain.
        active_at_step_start = self.damage_remaining != 0
        self.damaged_agent_steps += int(np.sum(active_at_step_start))

        self.energy -= ce.METABOLIC
        for i in range(2):
            key = (int(actions[i]), int(actions[1 - i]))
            self.energy[i] += ce.ENERGY_GAIN[key] * self.gain_multiplier(i)
            rewards[i] += ce.REWARD[key]

        mutual_coop = int(actions[0] == 0 and actions[1] == 0)
        if bonus_active and mutual_coop:
            rewards += ce.COOP_BONUS

        # Consume one already-active finite damaged step before processing a
        # new depletion. A new depletion therefore grants exactly tau damaged
        # *subsequent* steps, as preregistered.
        finite = self.damage_remaining > 0
        self.damage_remaining[finite] -= 1

        failures = 0
        for i in range(2):
            if self.energy[i] <= 0:
                failures += 1
                self.last_fail[i] = 1
                self.mortality_seen = 1
                # Explicit failure reward penalty is locked to zero.
                rewards[i] -= FAILURE_PENALTY
                # Immediate rescue is identical in every condition.
                self.energy[i] = ce.E_0
                self._activate_damage(i)

        self.last_action = actions.copy()
        self.step_idx += 1
        # No depletion-triggered termination in Experiment 2.
        done = self.step_idx >= ce.T_HORIZON
        return rewards, done, failures, mutual_coop


def run_episode(policies, env, rng, *, train, bonus_active, collect_states=None):
    env.reset()
    trajs = [[], []]
    mutual = 0
    steps = 0
    failures = 0
    while True:
        actions = np.zeros(2, dtype=int)
        caches = []
        for i in range(2):
            x = env.obs(i)
            a, cache = policies[i].act(x, rng)
            actions[i] = a
            caches.append(cache)
            if collect_states is not None:
                collect_states.append(x.copy())
        rewards, done, nfail, mutual_coop = env.step(actions, bonus_active)
        failures += nfail
        steps += 1
        mutual += mutual_coop
        for i in range(2):
            x, h, p = caches[i]
            trajs[i].append((x, h, p, int(actions[i]), float(rewards[i])))
        if done:
            break
    coop_rate = mutual / max(1, steps)
    damage_fraction = env.damaged_agent_steps / float(2 * ce.T_HORIZON)
    return trajs, coop_rate, env.step_idx, failures, damage_fraction


def train_condition(condition: str, seed: int, cfg: dict):
    if condition not in RECOVERY_DURATIONS:
        raise ValueError(f"unknown condition: {condition}")
    rng = np.random.default_rng(seed)
    policies = [ce.Policy(rng), ce.Policy(rng)]
    env = RecoverabilityEnv(RECOVERY_DURATIONS[condition], rng)

    coop_hist = []
    for _ep in range(cfg["train_eps"]):
        trajs, coop, length, _fail, _damage = run_episode(
            policies, env, rng, train=True, bonus_active=True
        )
        if length != ce.T_HORIZON:
            raise AssertionError("Experiment 2 episode length drifted from fixed horizon")
        for i in range(2):
            policies[i].update(trajs[i], lr=cfg["lr"], gamma=cfg["gamma"])
        coop_hist.append(coop)
    baseline_coop = float(np.mean(coop_hist[-cfg["window"]:]))

    # Preserve the Experiment 1 pre-withdrawal measurement/RNG-consumption
    # pattern: state-bank collection followed by frozen bonus-off evaluation.
    states = []
    for _ in range(24):
        run_episode(policies, env, rng, train=False, bonus_active=True, collect_states=states)
    d_eff = ce.effective_rank(policies[0], states[:96])

    frozen = [
        run_episode(policies, env, rng, train=False, bonus_active=False)[1]
        for _ in range(60)
    ]
    frozen_coop = float(np.mean(frozen))

    w_coop, w_len, w_fail, w_damage = [], [], [], []
    for _ep in range(cfg["withdraw_eps"]):
        trajs, coop, length, fail, damage_fraction = run_episode(
            policies, env, rng, train=True, bonus_active=False
        )
        if length != ce.T_HORIZON:
            raise AssertionError("Experiment 2 withdrawal episode terminated early")
        for i in range(2):
            policies[i].update(trajs[i], lr=cfg["lr_w"], gamma=cfg["gamma"])
        w_coop.append(coop)
        w_len.append(length)
        w_fail.append(fail)
        w_damage.append(damage_fraction)

    tail = cfg["window"]
    post_coop = float(np.mean(w_coop[-tail:]))
    retention = post_coop / baseline_coop if baseline_coop > 1e-6 else 0.0
    return {
        "condition": condition,
        "seed": seed,
        "recovery_duration": "inf" if RECOVERY_DURATIONS[condition] is None else RECOVERY_DURATIONS[condition],
        "baseline_coop": baseline_coop,
        "frozen_coop": frozen_coop,
        "post_coop": post_coop,
        "retention": float(np.clip(retention, 0.0, 2.0)),
        "post_len": float(np.mean(w_len[-tail:])),
        "post_fail": float(np.mean(w_fail[-tail:])),
        "post_damage_fraction": float(np.mean(w_damage[-tail:])),
        "d_eff": d_eff,
        "coop_curve": [float(np.mean(w_coop[k:k + 20])) for k in range(0, len(w_coop), 20)],
    }


def _rankdata(values: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty(len(values), dtype=float)
    i = 0
    while i < len(values):
        j = i + 1
        while j < len(values) and values[order[j]] == values[order[i]]:
            j += 1
        avg_rank = (i + 1 + j) / 2.0
        ranks[order[i:j]] = avg_rank
        i = j
    return ranks


def _pearson(a: np.ndarray, b: np.ndarray) -> float:
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    ac = a - a.mean()
    bc = b - b.mean()
    denom = float(np.sqrt(np.sum(ac * ac) * np.sum(bc * bc)))
    if denom <= 0:
        return 0.0
    return float(np.sum(ac * bc) / denom)


def tie_aware_spearman(x: np.ndarray, y: np.ndarray) -> float:
    return _pearson(_rankdata(np.asarray(x, float)), _rankdata(np.asarray(y, float)))


def blocked_spearman_test(matrix: np.ndarray, n: int = N_PERMUTATIONS, seed: int = PERMUTATION_SEED):
    """matrix shape: [n_seeds, 4] in CONDITION_ORDER."""
    matrix = np.asarray(matrix, float)
    n_seeds, n_levels = matrix.shape
    if n_levels != len(CONDITION_ORDER):
        raise ValueError("matrix must contain all four preregistered levels")

    x = np.tile(np.arange(n_levels, dtype=float), n_seeds)
    y = matrix.reshape(-1)
    x_rank = _rankdata(x)
    y_rank = _rankdata(y).reshape(n_seeds, n_levels)
    obs = _pearson(x_rank, y_rank.reshape(-1))

    xc = x_rank - x_rank.mean()
    y_flat = y_rank.reshape(-1)
    yc_mean = y_flat.mean()
    denom = float(np.sqrt(np.sum(xc * xc) * np.sum((y_flat - yc_mean) ** 2)))
    rng = np.random.default_rng(seed)
    count = 0
    for _ in range(n):
        permuted = np.empty_like(y_rank)
        for s in range(n_seeds):
            permuted[s] = y_rank[s, rng.permutation(n_levels)]
        stat = float(np.sum(xc * (permuted.reshape(-1) - yc_mean)) / denom)
        if abs(stat) >= abs(obs) - 1e-12:
            count += 1
    p = float((count + 1) / (n + 1))
    return obs, p


def paired_bootstrap_endpoint(diffs: np.ndarray, n: int = N_BOOTSTRAP, seed: int = BOOTSTRAP_SEED):
    diffs = np.asarray(diffs, float)
    rng = np.random.default_rng(seed)
    means = np.empty(n, dtype=float)
    for i in range(n):
        idx = rng.integers(0, len(diffs), size=len(diffs))
        means[i] = diffs[idx].mean()
    lo, hi = np.percentile(means, [2.5, 97.5])
    return float(diffs.mean()), [float(lo), float(hi)]


def summarize_condition(results: list[dict], condition: str) -> dict:
    vals = np.array([r["post_coop"] for r in results if r["condition"] == condition], float)
    rng = np.random.default_rng(BOOTSTRAP_SEED + CONDITION_ORDER.index(condition) + 10)
    boot = np.empty(N_BOOTSTRAP, dtype=float)
    for i in range(N_BOOTSTRAP):
        idx = rng.integers(0, len(vals), size=len(vals))
        boot[i] = vals[idx].mean()
    return {
        "mean": float(vals.mean()),
        "std": float(vals.std(ddof=0)),
        "median": float(np.median(vals)),
        "iqr": [float(np.percentile(vals, 25)), float(np.percentile(vals, 75))],
        "bootstrap_95_ci_mean": [float(np.percentile(boot, 2.5)), float(np.percentile(boot, 97.5))],
        "fraction_post_coop_gt_0_5": float(np.mean(vals > 0.5)),
    }


def run_confirmatory(cfg: dict, seeds: list[int], output_path: Path):
    if seeds != list(range(1, 31)):
        raise ValueError("confirmatory run requires exactly paired seeds 1..30")

    results = []
    for condition in CONDITION_ORDER:
        for seed in seeds:
            results.append(train_condition(condition, seed, cfg))

    matrix = np.array([
        [next(r["post_coop"] for r in results if r["seed"] == seed and r["condition"] == c)
         for c in CONDITION_ORDER]
        for seed in seeds
    ], dtype=float)

    rho, p = blocked_spearman_test(matrix)
    endpoint_diffs = matrix[:, -1] - matrix[:, 0]
    endpoint_mean_diff, endpoint_ci = paired_bootstrap_endpoint(endpoint_diffs)

    primary_supported = bool(rho > 0.0 and p < 0.05)
    strong_supported = bool(
        primary_supported
        and endpoint_mean_diff >= 0.10
        and endpoint_ci[0] > 0.0
    )

    payload = {
        "preregistration": "EXPERIMENT2_RECOVERABILITY_PREREGISTRATION.md",
        "config": cfg,
        "locked_design": {
            "damage_multiplier": DAMAGE_MULTIPLIER,
            "failure_penalty": FAILURE_PENALTY,
            "recovery_durations": {
                k: ("inf" if v is None else v) for k, v in RECOVERY_DURATIONS.items()
            },
            "condition_order": CONDITION_ORDER,
            "n_seeds": len(seeds),
            "seeds": seeds,
            "permutation_resamples": N_PERMUTATIONS,
            "permutation_seed": PERMUTATION_SEED,
            "bootstrap_resamples": N_BOOTSTRAP,
            "bootstrap_seed": BOOTSTRAP_SEED,
            "practical_endpoint_threshold": 0.10,
        },
        "primary_test": {
            "tie_aware_spearman_rho": rho,
            "blocked_by_seed_two_sided_p": p,
            "supported": primary_supported,
        },
        "endpoint_tau_inf_minus_tau0": {
            "mean_difference": endpoint_mean_diff,
            "paired_bootstrap_95_ci": endpoint_ci,
            "meets_0_10_practical_threshold": bool(endpoint_mean_diff >= 0.10),
        },
        "strong_manuscript_support": strong_supported,
        "condition_summaries": {
            c: summarize_condition(results, c) for c in CONDITION_ORDER
        },
        "diagnostics": {
            c: {
                "mean_post_len": float(np.mean([r["post_len"] for r in results if r["condition"] == c])),
                "mean_post_fail": float(np.mean([r["post_fail"] for r in results if r["condition"] == c])),
                "mean_post_damage_fraction": float(np.mean([r["post_damage_fraction"] for r in results if r["condition"] == c])),
                "mean_baseline_coop": float(np.mean([r["baseline_coop"] for r in results if r["condition"] == c])),
            }
            for c in CONDITION_ORDER
        },
        "runs": results,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return payload
