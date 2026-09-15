"""Preregistered Experiment 4: consequence scope under non-terminal recovery.

Locked design: ../EXPERIMENT4_CONSEQUENCE_SCOPE_PREREGISTRATION.md
Primary factors: scope in {individual, shared}, latency k in {2,5,10}.
Confirmatory seeds 101..130 must not be used before invariant checks pass.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import numpy as np

import csc_experiment as ce

ROOT = Path(__file__).resolve().parent
SCOPES = ("individual", "shared")
LATENCIES = (2, 5, 10)
FAILURE_PENALTY = 0.0
CONFIRMATORY_SEEDS = list(range(101, 131))
COMMON_BANK_SEEDS = list(range(2001, 2011))
COMMON_BANK_EPISODES_PER_SEED = 4
N_SIGNFLIP = 20_000
SIGNFLIP_SEED = 20260919
N_BOOTSTRAP = 10_000
BOOTSTRAP_SEED = 20260920
PRACTICAL_THRESHOLD = 0.10


def _failure_category(actions: np.ndarray, failed_i: int) -> str:
    own = int(actions[failed_i])
    partner = int(actions[1 - failed_i])
    if own == 0 and partner == 1:
        return "failed_C_vs_partner_Solo"
    if own == 1 and partner == 0:
        return "failed_Solo_vs_partner_C"
    if own == 0 and partner == 0:
        return "mutual_C"
    if own == 1 and partner == 1:
        return "mutual_Solo"
    if own == 2 or partner == 2:
        return "involving_Rest"
    return "other"


@dataclass
class ConsequenceScopeEnv:
    scope: str
    latency: int
    rng: np.random.Generator
    energy: np.ndarray = field(default_factory=lambda: np.array([ce.E_0, ce.E_0], dtype=float))
    last_action: np.ndarray = field(default_factory=lambda: np.array([2, 2], dtype=int))
    last_fail: np.ndarray = field(default_factory=lambda: np.array([0, 0], dtype=int))
    recovery_remaining: np.ndarray = field(default_factory=lambda: np.array([0, 0], dtype=int))
    step_idx: int = 0
    mortality_seen: int = 0

    def __post_init__(self):
        if self.scope not in SCOPES:
            raise ValueError(f"unknown scope {self.scope}")
        if self.latency < 0:
            raise ValueError("latency must be non-negative")

    def reset(self):
        self.energy = np.array([ce.E_0, ce.E_0], dtype=float)
        self.last_action = np.array([2, 2], dtype=int)
        self.last_fail = np.array([0, 0], dtype=int)
        self.recovery_remaining = np.array([0, 0], dtype=int)
        self.step_idx = 0
        self.mortality_seen = 0

    def active_mask(self) -> np.ndarray:
        return self.recovery_remaining == 0

    def obs(self, i: int) -> np.ndarray:
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

    def step(self, actions: np.ndarray, active_at_start: np.ndarray, bonus_active: bool):
        rewards = np.zeros(2, dtype=float)
        self.last_fail[:] = 0

        self.energy -= ce.METABOLIC
        for i in range(2):
            key = (int(actions[i]), int(actions[1 - i]))
            self.energy[i] += ce.ENERGY_GAIN[key]
            rewards[i] += ce.REWARD[key]

        eligible = bool(active_at_start[0] and active_at_start[1])
        mutual_coop = int(eligible and actions[0] == 0 and actions[1] == 0)
        if bonus_active and mutual_coop:
            rewards += ce.COOP_BONUS

        # Consume one already-active recovery step. Newly triggered recovery
        # is installed afterwards, so latency k means exactly k subsequent steps.
        recovering = self.recovery_remaining > 0
        self.recovery_remaining[recovering] -= 1

        failed = np.where(self.energy <= 0)[0].tolist()
        failure_categories = []
        if failed:
            self.mortality_seen = 1
            for i in failed:
                self.last_fail[i] = 1
                rewards[i] -= FAILURE_PENALTY
                self.energy[i] = ce.E_0
                failure_categories.append(_failure_category(actions, i))

            if self.scope == "individual":
                for i in failed:
                    self.recovery_remaining[i] = int(self.latency)
            else:
                self.recovery_remaining[:] = int(self.latency)

        self.last_action = actions.copy()
        self.step_idx += 1
        done = self.step_idx >= ce.T_HORIZON
        return rewards, done, failed, failure_categories, mutual_coop, eligible


def _update_fixed_horizon(policy: ce.Policy, trajectory: list[dict], lr: float, gamma: float):
    """REINFORCE with full-horizon return normalization and fixed /T scaling."""
    if len(trajectory) != ce.T_HORIZON:
        raise AssertionError("E4 update requires exactly the locked 50-step trajectory")

    returns = np.empty(len(trajectory), dtype=float)
    G = 0.0
    for idx in range(len(trajectory) - 1, -1, -1):
        G = float(trajectory[idx]["reward"]) + gamma * G
        returns[idx] = G

    norm_returns = returns.copy()
    if norm_returns.std() > 1e-8:
        norm_returns = (norm_returns - norm_returns.mean()) / (norm_returns.std() + 1e-8)

    dW1 = np.zeros_like(policy.W1)
    db1 = np.zeros_like(policy.b1)
    dW2 = np.zeros_like(policy.W2)
    db2 = np.zeros_like(policy.b2)

    for idx, tr in enumerate(trajectory):
        if not tr["decision"]:
            continue
        x, h, p = tr["cache"]
        a = int(tr["action"])
        gz2 = -p.copy()
        gz2[a] += 1.0
        gz2 *= norm_returns[idx]
        dW2 += np.outer(gz2, h)
        db2 += gz2
        dh = policy.W2.T @ gz2
        dz1 = dh * (1.0 - h * h)
        dW1 += np.outer(dz1, x)
        db1 += dz1

    scale = 1.0 / ce.T_HORIZON
    policy.W1 += lr * dW1 * scale
    policy.b1 += lr * db1 * scale
    policy.W2 += lr * dW2 * scale
    policy.b2 += lr * db2 * scale


def run_episode(
    policies,
    env: ConsequenceScopeEnv,
    rng: np.random.Generator,
    *,
    bonus_active: bool,
    collect_pairs: Optional[list] = None,
):
    env.reset()
    trajectories = [[], []]
    eligible_steps = 0
    eligible_mutual = 0
    forced_agent_steps = 0
    both_forced_steps = 0
    exactly_one_forced_steps = 0
    genuine_decisions = np.zeros(2, dtype=int)
    failures = 0
    failure_categories = Counter()
    first_failure_categories = Counter()
    first_failure_seen = False
    partner_actions_during_individual_recovery = Counter()

    while True:
        active = env.active_mask().copy()
        inactive_count = int(np.sum(~active))
        forced_agent_steps += inactive_count
        both_forced_steps += int(inactive_count == 2)
        exactly_one_forced_steps += int(inactive_count == 1)

        eligible = bool(active[0] and active[1])
        if collect_pairs is not None and eligible:
            collect_pairs.append((env.obs(0).copy(), env.obs(1).copy()))

        actions = np.full(2, 2, dtype=int)
        caches = [None, None]
        for i in range(2):
            if active[i]:
                x = env.obs(i)
                a, cache = policies[i].act(x, rng)
                actions[i] = a
                caches[i] = cache
                genuine_decisions[i] += 1

        if env.scope == "individual" and inactive_count == 1:
            active_i = int(np.where(active)[0][0])
            partner_actions_during_individual_recovery[int(actions[active_i])] += 1

        rewards, done, failed, cats, mutual_coop, step_eligible = env.step(
            actions, active, bonus_active
        )
        failures += len(failed)
        for cat in cats:
            failure_categories[cat] += 1
        if cats and not first_failure_seen:
            for cat in cats:
                first_failure_categories[cat] += 1
            first_failure_seen = True

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

    if env.step_idx != ce.T_HORIZON:
        raise AssertionError("E4 episode length drifted from fixed horizon")

    diag = {
        "failures": failures,
        "forced_agent_fraction": forced_agent_steps / float(2 * ce.T_HORIZON),
        "both_forced_fraction": both_forced_steps / float(ce.T_HORIZON),
        "exactly_one_forced_fraction": exactly_one_forced_steps / float(ce.T_HORIZON),
        "eligible_fraction": eligible_steps / float(ce.T_HORIZON),
        "genuine_decisions_agent0": int(genuine_decisions[0]),
        "genuine_decisions_agent1": int(genuine_decisions[1]),
        "failure_categories": dict(failure_categories),
        "first_failure_categories": dict(first_failure_categories),
        "partner_actions_during_individual_recovery": dict(partner_actions_during_individual_recovery),
    }
    coop = eligible_mutual / max(1, eligible_steps)
    return trajectories, float(coop), diag


def train_condition(scope: str, latency: int, seed: int, cfg: dict, *, return_policies=False):
    if scope not in SCOPES or latency not in LATENCIES:
        raise ValueError("invalid E4 confirmatory cell")
    rng = np.random.default_rng(seed)
    policies = [ce.Policy(rng), ce.Policy(rng)]
    env = ConsequenceScopeEnv(scope, latency, rng)

    train_coop = []
    for _ in range(cfg["train_eps"]):
        trajs, coop, _diag = run_episode(policies, env, rng, bonus_active=True)
        for i in range(2):
            _update_fixed_horizon(policies[i], trajs[i], cfg["lr"], cfg["gamma"])
        train_coop.append(coop)

    withdrawal_coop = []
    withdrawal_diags = []
    for _ in range(cfg["withdraw_eps"]):
        trajs, coop, diag = run_episode(policies, env, rng, bonus_active=False)
        for i in range(2):
            _update_fixed_horizon(policies[i], trajs[i], cfg["lr_w"], cfg["gamma"])
        withdrawal_coop.append(coop)
        withdrawal_diags.append(diag)

    tail = cfg["window"]
    result = {
        "scope": scope,
        "latency": latency,
        "seed": seed,
        "baseline_coop": float(np.mean(train_coop[-tail:])),
        "post_coop": float(np.mean(withdrawal_coop[-tail:])),
        "post_diags": withdrawal_diags[-tail:],
    }
    if return_policies:
        return result, (policies[0].copy(), policies[1].copy())
    return result


def build_common_state_bank() -> list[tuple[np.ndarray, np.ndarray]]:
    bank = []
    for seed in COMMON_BANK_SEEDS:
        rng = np.random.default_rng(seed)
        policies = [ce.Policy(rng), ce.Policy(rng)]
        env = ConsequenceScopeEnv("individual", 0, rng)
        for _ in range(COMMON_BANK_EPISODES_PER_SEED):
            run_episode(policies, env, rng, bonus_active=False, collect_pairs=bank)
    expected = len(COMMON_BANK_SEEDS) * COMMON_BANK_EPISODES_PER_SEED * ce.T_HORIZON
    if len(bank) != expected:
        raise AssertionError("E4 common bank must contain exactly 2000 decision-capable state pairs")
    return bank


def common_state_mutual_coop(policies, bank) -> float:
    vals = []
    for x0, x1 in bank:
        _h0, p0 = policies[0].forward(x0)
        _h1, p1 = policies[1].forward(x1)
        vals.append(float(p0[0] * p1[0]))
    return float(np.mean(vals))


def signflip_test(diffs: np.ndarray, n=N_SIGNFLIP, seed=SIGNFLIP_SEED):
    diffs = np.asarray(diffs, float)
    obs = float(diffs.mean())
    rng = np.random.default_rng(seed)
    count = 0
    for _ in range(n):
        signs = rng.choice(np.array([-1.0, 1.0]), size=len(diffs))
        stat = float(np.mean(diffs * signs))
        if abs(stat) >= abs(obs) - 1e-12:
            count += 1
    return obs, float((count + 1) / (n + 1))


def paired_bootstrap(diffs: np.ndarray, n=N_BOOTSTRAP, seed=BOOTSTRAP_SEED):
    diffs = np.asarray(diffs, float)
    rng = np.random.default_rng(seed)
    means = np.empty(n, dtype=float)
    for i in range(n):
        idx = rng.integers(0, len(diffs), size=len(diffs))
        means[i] = diffs[idx].mean()
    lo, hi = np.percentile(means, [2.5, 97.5])
    return [float(lo), float(hi)]


def _merge_counts(diags: list[dict], key: str) -> dict:
    c = Counter()
    for d in diags:
        c.update(d[key])
    return dict(c)


def summarize_diag(rows: list[dict]) -> dict:
    diags = [d for r in rows for d in r["post_diags"]]
    return {
        "mean_failures": float(np.mean([d["failures"] for d in diags])),
        "mean_forced_agent_fraction": float(np.mean([d["forced_agent_fraction"] for d in diags])),
        "mean_both_forced_fraction": float(np.mean([d["both_forced_fraction"] for d in diags])),
        "mean_exactly_one_forced_fraction": float(np.mean([d["exactly_one_forced_fraction"] for d in diags])),
        "mean_eligible_fraction": float(np.mean([d["eligible_fraction"] for d in diags])),
        "mean_genuine_decisions_per_agent": float(np.mean([
            (d["genuine_decisions_agent0"] + d["genuine_decisions_agent1"]) / 2.0
            for d in diags
        ])),
        "failure_categories": _merge_counts(diags, "failure_categories"),
        "first_failure_categories": _merge_counts(diags, "first_failure_categories"),
        "partner_actions_during_individual_recovery": _merge_counts(diags, "partner_actions_during_individual_recovery"),
    }


def run_confirmatory(cfg: dict, seeds: list[int], output_path: Path):
    import json

    if seeds != CONFIRMATORY_SEEDS:
        raise ValueError("E4 confirmatory seeds must be exactly 101..130")

    results = []
    final_policies = {}
    for scope in SCOPES:
        for k in LATENCIES:
            for seed in seeds:
                row, policies = train_condition(scope, k, seed, cfg, return_policies=True)
                results.append(row)
                final_policies[(scope, k, seed)] = policies

    bank = build_common_state_bank()
    primary_rows = []
    for scope in SCOPES:
        for k in LATENCIES:
            for seed in seeds:
                primary_rows.append({
                    "scope": scope,
                    "latency": k,
                    "seed": seed,
                    "expected_mutual_coop": common_state_mutual_coop(
                        final_policies[(scope, k, seed)], bank
                    ),
                })

    def pv(scope, k, seed):
        return next(r["expected_mutual_coop"] for r in primary_rows
                    if r["scope"] == scope and r["latency"] == k and r["seed"] == seed)

    per_seed_scope = []
    by_latency = {}
    for k in LATENCIES:
        diffs = np.array([pv("shared", k, s) - pv("individual", k, s) for s in seeds], float)
        by_latency[str(k)] = {
            "mean_difference": float(diffs.mean()),
            "median_difference": float(np.median(diffs)),
            "paired_bootstrap_95_ci": paired_bootstrap(diffs, seed=BOOTSTRAP_SEED + k),
            "n_positive": int(np.sum(diffs > 0)),
            "n_zero": int(np.sum(diffs == 0)),
            "n_negative": int(np.sum(diffs < 0)),
        }
    for s in seeds:
        ds = [pv("shared", k, s) - pv("individual", k, s) for k in LATENCIES]
        per_seed_scope.append(float(np.mean(ds)))
    per_seed_scope = np.array(per_seed_scope, float)
    primary_mean, primary_p = signflip_test(per_seed_scope)
    primary_ci = paired_bootstrap(per_seed_scope)
    supported = bool(primary_mean > 0 and primary_p < 0.05)
    strong = bool(supported and primary_mean >= PRACTICAL_THRESHOLD and primary_ci[0] > 0)

    def rollout(scope, k, seed):
        return next(r["post_coop"] for r in results
                    if r["scope"] == scope and r["latency"] == k and r["seed"] == seed)
    rollout_seed_diffs = np.array([
        np.mean([rollout("shared", k, s) - rollout("individual", k, s) for k in LATENCIES])
        for s in seeds
    ], float)

    diagnostics = {}
    for scope in SCOPES:
        for k in LATENCIES:
            rows = [r for r in results if r["scope"] == scope and r["latency"] == k]
            diagnostics[f"{scope}_k{k}"] = summarize_diag(rows)

    payload = {
        "preregistration": "EXPERIMENT4_CONSEQUENCE_SCOPE_PREREGISTRATION.md",
        "config": cfg,
        "locked_design": {
            "scopes": list(SCOPES),
            "latencies": list(LATENCIES),
            "confirmatory_seeds": seeds,
            "fixed_horizon": ce.T_HORIZON,
            "failure_penalty": FAILURE_PENALTY,
            "immediate_rescue_energy": ce.E_0,
            "common_bank_seeds": COMMON_BANK_SEEDS,
            "common_bank_size": len(bank),
            "signflip_resamples": N_SIGNFLIP,
            "signflip_seed": SIGNFLIP_SEED,
            "bootstrap_resamples": N_BOOTSTRAP,
            "bootstrap_seed": BOOTSTRAP_SEED,
            "practical_threshold": PRACTICAL_THRESHOLD,
        },
        "primary_endpoint": "common-state expected mutual cooperation after withdrawal",
        "primary_scope_test": {
            "mean_shared_minus_individual_collapsed_over_latency": primary_mean,
            "paired_signflip_two_sided_p": primary_p,
            "paired_bootstrap_95_ci": primary_ci,
            "supported": supported,
            "strong_support": strong,
            "per_seed_collapsed_differences": per_seed_scope.tolist(),
        },
        "latency_level_primary_contrasts": by_latency,
        "secondary_rollout_scope_contrast": {
            "mean_shared_minus_individual_collapsed_over_latency": float(rollout_seed_diffs.mean()),
            "paired_bootstrap_95_ci": paired_bootstrap(rollout_seed_diffs, seed=BOOTSTRAP_SEED + 100),
            "per_seed_collapsed_differences": rollout_seed_diffs.tolist(),
        },
        "primary_rows": primary_rows,
        "results": results,
        "diagnostics": diagnostics,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return payload
