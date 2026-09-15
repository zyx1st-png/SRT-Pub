"""Preregistered CSC Experiment 3: consequence-bearing recovery latency.

All conditions are non-terminal and exactly 50 environment steps long. On
energy depletion the agent is immediately rescued to E0=6 with no explicit
failure penalty. The only condition parameter is the number of subsequent
steps during which the failed agent cannot choose a normal action and is
forced through the already-existing Rest transition.

Locked design: ../EXPERIMENT3_CONSEQUENCE_RECOVERY_PREREGISTRATION.md
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

import csc_experiment as ce

ROOT = Path(__file__).resolve().parent

FAILURE_PENALTY = 0.0
RECOVERY_LATENCIES = {
    "k0": 0,
    "k2": 2,
    "k5": 5,
    "k10": 10,
}
CONDITION_ORDER = ["k0", "k2", "k5", "k10"]
N_PERMUTATIONS = 20_000
PERMUTATION_SEED = 20260917
N_BOOTSTRAP = 10_000
BOOTSTRAP_SEED = 20260918
PRACTICAL_THRESHOLD = 0.10
COMMON_BANK_SEEDS = list(range(1001, 1011))
COMMON_BANK_EPISODES_PER_SEED = 4


@dataclass
class RecoveryLatencyEnv:
    latency: int
    rng: np.random.Generator
    energy: np.ndarray = field(default_factory=lambda: np.array([ce.E_0, ce.E_0], dtype=float))
    alive: np.ndarray = field(default_factory=lambda: np.array([1, 1], dtype=int))
    last_action: np.ndarray = field(default_factory=lambda: np.array([2, 2], dtype=int))
    last_fail: np.ndarray = field(default_factory=lambda: np.array([0, 0], dtype=int))
    step_idx: int = 0
    mortality_seen: int = 0
    recovery_remaining: np.ndarray = field(default_factory=lambda: np.array([0, 0], dtype=int))
    forced_agent_steps: int = 0

    def reset(self):
        self.energy = np.array([ce.E_0, ce.E_0], dtype=float)
        self.alive = np.array([1, 1], dtype=int)
        self.last_action = np.array([2, 2], dtype=int)
        self.last_fail = np.array([0, 0], dtype=int)
        self.step_idx = 0
        self.mortality_seen = 0
        self.recovery_remaining = np.array([0, 0], dtype=int)
        self.forced_agent_steps = 0

    def obs(self, i: int):
        """Keep the Experiment 1/2 12-feature observation specification."""
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

    def active_mask(self) -> np.ndarray:
        return self.recovery_remaining == 0

    def step(self, actions: np.ndarray, active_at_start: np.ndarray, bonus_active: bool):
        rewards = np.zeros(2, dtype=float)
        self.last_fail[:] = 0

        # Every environment step has the same metabolic clock. Recovering
        # agents execute the existing Rest action, so no reward/energy table is
        # modified for Experiment 3.
        self.energy -= ce.METABOLIC
        for i in range(2):
            key = (int(actions[i]), int(actions[1 - i]))
            self.energy[i] += ce.ENERGY_GAIN[key]
            rewards[i] += ce.REWARD[key]

        eligible = bool(active_at_start[0] and active_at_start[1])
        mutual_coop = int(eligible and actions[0] == 0 and actions[1] == 0)
        if bonus_active and mutual_coop:
            rewards += ce.COOP_BONUS

        self.forced_agent_steps += int(np.sum(~active_at_start))

        # Consume one previously active recovery step before installing any
        # new timer. Thus a failure at step t creates exactly k subsequent
        # forced-Rest steps t+1..t+k.
        recovering = self.recovery_remaining > 0
        self.recovery_remaining[recovering] -= 1

        failures = 0
        for i in range(2):
            if self.energy[i] <= 0:
                if not active_at_start[i]:
                    raise AssertionError(
                        "locked k<=10 recovery should not deplete during forced Rest"
                    )
                failures += 1
                self.last_fail[i] = 1
                self.mortality_seen = 1
                # Locked: no new explicit failure reward penalty.
                rewards[i] -= FAILURE_PENALTY
                # Locked: identical immediate rescue in every condition.
                self.energy[i] = ce.E_0
                self.recovery_remaining[i] = int(self.latency)

        self.last_action = actions.copy()
        self.step_idx += 1
        done = self.step_idx >= ce.T_HORIZON
        return rewards, done, failures, mutual_coop, eligible


def _update_masked(policy: ce.Policy, trajectory: list[dict], lr: float, gamma: float):
    """REINFORCE update over genuine policy decisions only.

    Rewards on forced-recovery steps remain in the return stream so earlier
    decisions experience the correct temporal consequence. No score-function
    gradient is attributed to a forced Rest action that the policy did not
    choose.

    When every step is a decision (k0), this is algebraically the same update
    as ce.Policy.update.
    """
    if not trajectory:
        return

    returns = np.empty(len(trajectory), dtype=float)
    G = 0.0
    for idx in range(len(trajectory) - 1, -1, -1):
        G = float(trajectory[idx]["reward"]) + gamma * G
        returns[idx] = G

    decision_idx = [i for i, tr in enumerate(trajectory) if tr["decision"]]
    if not decision_idx:
        return

    decision_returns = returns[decision_idx].copy()
    if decision_returns.std() > 1e-8:
        decision_returns = (
            (decision_returns - decision_returns.mean())
            / (decision_returns.std() + 1e-8)
        )

    dW1 = np.zeros_like(policy.W1)
    db1 = np.zeros_like(policy.b1)
    dW2 = np.zeros_like(policy.W2)
    db2 = np.zeros_like(policy.b2)

    for idx, Gd in zip(decision_idx, decision_returns):
        tr = trajectory[idx]
        x, h, p = tr["cache"]
        a = int(tr["action"])
        gz2 = -p.copy()
        gz2[a] += 1.0
        gz2 *= Gd
        dW2 += np.outer(gz2, h)
        db2 += gz2
        dh = policy.W2.T @ gz2
        dz1 = dh * (1.0 - h * h)
        dW1 += np.outer(dz1, x)
        db1 += dz1

    scale = 1.0 / len(decision_idx)
    policy.W1 += lr * dW1 * scale
    policy.b1 += lr * db1 * scale
    policy.W2 += lr * dW2 * scale
    policy.b2 += lr * db2 * scale


def run_episode(
    policies,
    env: RecoveryLatencyEnv,
    rng: np.random.Generator,
    *,
    train: bool,
    bonus_active: bool,
    collect_states=None,
    collect_pairs=None,
):
    env.reset()
    trajectories = [[], []]
    eligible_mutual = 0
    eligible_steps = 0
    failures = 0

    while True:
        active = env.active_mask().copy()
        eligible = bool(active[0] and active[1])
        actions = np.full(2, 2, dtype=int)  # forced Rest unless policy decides
        caches = [None, None]

        if collect_pairs is not None and eligible:
            collect_pairs.append((env.obs(0).copy(), env.obs(1).copy()))

        for i in range(2):
            if active[i]:
                x = env.obs(i)
                a, cache = policies[i].act(x, rng)
                actions[i] = a
                caches[i] = cache
                if collect_states is not None:
                    collect_states.append(x.copy())

        rewards, done, nfail, mutual_coop, step_eligible = env.step(
            actions, active, bonus_active
        )
        failures += nfail
        if step_eligible:
            eligible_steps += 1
            eligible_mutual += mutual_coop

        for i in range(2):
            trajectories[i].append({
                "cache": caches[i],
                "action": int(actions[i]),
                "reward": float(rewards[i]),
                "decision": bool(active[i]),
            })

        if done:
            break

    eligible_coop = eligible_mutual / max(1, eligible_steps)
    forced_fraction = env.forced_agent_steps / float(2 * ce.T_HORIZON)
    eligible_fraction = eligible_steps / float(ce.T_HORIZON)
    return (
        trajectories,
        float(eligible_coop),
        env.step_idx,
        failures,
        float(forced_fraction),
        float(eligible_fraction),
    )


def train_condition(condition: str, seed: int, cfg: dict, *, return_policies: bool = False):
    if condition not in RECOVERY_LATENCIES:
        raise ValueError(f"unknown condition: {condition}")

    rng = np.random.default_rng(seed)
    policies = [ce.Policy(rng), ce.Policy(rng)]
    env = RecoveryLatencyEnv(RECOVERY_LATENCIES[condition], rng)

    coop_hist = []
    for _ep in range(cfg["train_eps"]):
        trajs, coop, length, _fail, _forced, _eligible = run_episode(
            policies, env, rng, train=True, bonus_active=True
        )
        if length != ce.T_HORIZON:
            raise AssertionError("Experiment 3 episode length drifted from fixed horizon")
        for i in range(2):
            _update_masked(policies[i], trajs[i], cfg["lr"], cfg["gamma"])
        coop_hist.append(coop)
    baseline_coop = float(np.mean(coop_hist[-cfg["window"]:]))

    # Preserve Experiment 2's pre-withdrawal measurement/RNG-consumption
    # pattern. For k0 this makes the baseline path directly comparable to E2
    # tau0 and provides a strong implementation invariant.
    states = []
    for _ in range(24):
        run_episode(
            policies, env, rng, train=False, bonus_active=True,
            collect_states=states,
        )
    d_eff = ce.effective_rank(policies[0], states[:96])

    frozen = [
        run_episode(policies, env, rng, train=False, bonus_active=False)[1]
        for _ in range(60)
    ]
    frozen_coop = float(np.mean(frozen))

    w_coop, w_len, w_fail, w_forced, w_eligible = [], [], [], [], []
    for _ep in range(cfg["withdraw_eps"]):
        trajs, coop, length, fail, forced_fraction, eligible_fraction = run_episode(
            policies, env, rng, train=True, bonus_active=False
        )
        if length != ce.T_HORIZON:
            raise AssertionError("Experiment 3 withdrawal episode terminated early")
        for i in range(2):
            _update_masked(policies[i], trajs[i], cfg["lr_w"], cfg["gamma"])
        w_coop.append(coop)
        w_len.append(length)
        w_fail.append(fail)
        w_forced.append(forced_fraction)
        w_eligible.append(eligible_fraction)

    tail = cfg["window"]
    post_coop = float(np.mean(w_coop[-tail:]))
    retention = post_coop / baseline_coop if baseline_coop > 1e-6 else 0.0
    result = {
        "condition": condition,
        "seed": seed,
        "recovery_latency": RECOVERY_LATENCIES[condition],
        "baseline_coop": baseline_coop,
        "frozen_coop": frozen_coop,
        "post_coop": post_coop,
        "retention": float(np.clip(retention, 0.0, 2.0)),
        "post_len": float(np.mean(w_len[-tail:])),
        "post_fail": float(np.mean(w_fail[-tail:])),
        "post_forced_recovery_fraction": float(np.mean(w_forced[-tail:])),
        "post_eligible_fraction": float(np.mean(w_eligible[-tail:])),
        "d_eff": d_eff,
        "coop_curve": [
            float(np.mean(w_coop[k:k + 20]))
            for k in range(0, len(w_coop), 20)
        ],
    }
    if return_policies:
        return result, (policies[0].copy(), policies[1].copy())
    return result


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
    return obs, float((count + 1) / (n + 1))


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
        "bootstrap_95_ci_mean": [
            float(np.percentile(boot, 2.5)),
            float(np.percentile(boot, 97.5)),
        ],
        "fraction_post_coop_gt_0_5": float(np.mean(vals > 0.5)),
    }


def build_common_state_bank() -> list[tuple[np.ndarray, np.ndarray]]:
    """Condition-independent decision-capable paired-state bank.

    Uses disjoint generator seeds and k0 so no bank state has an active
    recovery timer. Policies are freshly initialized and never trained.
    """
    bank: list[tuple[np.ndarray, np.ndarray]] = []
    for seed in COMMON_BANK_SEEDS:
        rng = np.random.default_rng(seed)
        policies = [ce.Policy(rng), ce.Policy(rng)]
        env = RecoveryLatencyEnv(0, rng)
        for _ in range(COMMON_BANK_EPISODES_PER_SEED):
            run_episode(
                policies, env, rng, train=False, bonus_active=False,
                collect_pairs=bank,
            )
    expected = len(COMMON_BANK_SEEDS) * COMMON_BANK_EPISODES_PER_SEED * ce.T_HORIZON
    if len(bank) != expected:
        raise AssertionError("common state bank did not remain fully decision-capable")
    return bank


def common_state_mutual_coop(policies, bank) -> float:
    vals = []
    for x0, x1 in bank:
        _h0, p0 = policies[0].forward(x0)
        _h1, p1 = policies[1].forward(x1)
        vals.append(float(p0[0] * p1[0]))
    return float(np.mean(vals))


def run_confirmatory(cfg: dict, seeds: list[int], output_path: Path):
    if seeds != list(range(1, 31)):
        raise ValueError("confirmatory run requires exactly paired seeds 1..30")

    results = []
    final_policies = {}
    for condition in CONDITION_ORDER:
        for seed in seeds:
            result, policies = train_condition(
                condition, seed, cfg, return_policies=True
            )
            results.append(result)
            final_policies[(condition, seed)] = policies

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
        and endpoint_mean_diff >= PRACTICAL_THRESHOLD
        and endpoint_ci[0] > 0.0
    )

    bank = build_common_state_bank()
    secondary_rows = []
    for condition in CONDITION_ORDER:
        for seed in seeds:
            secondary_rows.append({
                "condition": condition,
                "seed": seed,
                "expected_mutual_coop": common_state_mutual_coop(
                    final_policies[(condition, seed)], bank
                ),
            })
    secondary_matrix = np.array([
        [next(r["expected_mutual_coop"] for r in secondary_rows
              if r["seed"] == seed and r["condition"] == c)
         for c in CONDITION_ORDER]
        for seed in seeds
    ], dtype=float)
    secondary_rho = tie_aware_spearman(
        np.tile(np.arange(len(CONDITION_ORDER), dtype=float), len(seeds)),
        secondary_matrix.reshape(-1),
    )

    payload = {
        "preregistration": "EXPERIMENT3_CONSEQUENCE_RECOVERY_PREREGISTRATION.md",
        "config": cfg,
        "locked_design": {
            "failure_penalty": FAILURE_PENALTY,
            "recovery_latencies": RECOVERY_LATENCIES,
            "condition_order": CONDITION_ORDER,
            "forced_action": "Rest (existing action index 2)",
            "fixed_horizon": ce.T_HORIZON,
            "immediate_rescue_energy": ce.E_0,
            "n_seeds": len(seeds),
            "seeds": seeds,
            "permutation_resamples": N_PERMUTATIONS,
            "permutation_seed": PERMUTATION_SEED,
            "bootstrap_resamples": N_BOOTSTRAP,
            "bootstrap_seed": BOOTSTRAP_SEED,
            "practical_endpoint_threshold": PRACTICAL_THRESHOLD,
            "common_bank_seeds": COMMON_BANK_SEEDS,
            "common_bank_episodes_per_seed": COMMON_BANK_EPISODES_PER_SEED,
        },
        "primary_endpoint": "eligible mutual cooperation, final 100 withdrawal episodes",
        "primary_test": {
            "tie_aware_spearman_rho": rho,
            "blocked_by_seed_two_sided_p": p,
            "supported": primary_supported,
        },
        "endpoint_k10_minus_k0": {
            "mean_difference": endpoint_mean_diff,
            "paired_bootstrap_95_ci": endpoint_ci,
            "meets_0_10_practical_threshold": bool(
                endpoint_mean_diff >= PRACTICAL_THRESHOLD
            ),
        },
        "strong_manuscript_support": strong_supported,
        "condition_summaries": {
            c: summarize_condition(results, c) for c in CONDITION_ORDER
        },
        "diagnostics": {
            c: {
                "mean_post_len": float(np.mean([r["post_len"] for r in results if r["condition"] == c])),
                "mean_post_fail": float(np.mean([r["post_fail"] for r in results if r["condition"] == c])),
                "mean_post_forced_recovery_fraction": float(np.mean([r["post_forced_recovery_fraction"] for r in results if r["condition"] == c])),
                "mean_post_eligible_fraction": float(np.mean([r["post_eligible_fraction"] for r in results if r["condition"] == c])),
                "mean_baseline_coop": float(np.mean([r["baseline_coop"] for r in results if r["condition"] == c])),
            }
            for c in CONDITION_ORDER
        },
        "secondary_common_state_probe": {
            "bank_size": len(bank),
            "tie_aware_spearman_rho_descriptive": secondary_rho,
            "condition_means": {
                c: float(np.mean([
                    r["expected_mutual_coop"] for r in secondary_rows
                    if r["condition"] == c
                ]))
                for c in CONDITION_ORDER
            },
            "runs": secondary_rows,
        },
        "runs": results,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return payload
