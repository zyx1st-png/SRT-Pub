from __future__ import annotations

import json
from pathlib import Path
import numpy as np


def softmax(x, temp: float):
    z = np.asarray(x, dtype=float) / temp
    z = z - np.max(z)
    e = np.exp(z)
    return e / np.sum(e)


def run_control_a(seed: int, topology: str, c: dict):
    """Matched pre-shift conditions; post-shift local burden either does or does not
    write back into the shared scaffold. Units are formed positions, not SRT Bearers.
    """
    rng = np.random.default_rng(seed)
    n = c["N"]
    k = c["K"]
    t_cal = c["calibration_steps"]
    t_post = c["post_steps"]
    q = np.zeros((n, k), dtype=float)
    scaffold = np.zeros(k, dtype=float)
    burden_positions = set(c["burden_positions"])
    pre_rewards = np.asarray(c["pre_rewards"], dtype=float)
    post_rewards = np.asarray(c["post_rewards"], dtype=float)

    agg_reward = []
    agg_cost = []
    alt_mass = []

    for t in range(t_cal + t_post):
        reward_vec = pre_rewards if t < t_cal else post_rewards
        actions, rewards, burdens = [], [], []

        for i in range(n):
            p = softmax(q[i] + scaffold, c["temperature"])
            a = int(rng.choice(k, p=p))
            r = float(reward_vec[a] + rng.normal(0.0, c["reward_noise"]))
            b = 0.0
            if t >= t_cal and i in burden_positions:
                if a == 0:
                    b = c["burden_old_best"]
                elif a == 1:
                    b = c["burden_second"]
            actions.append(a)
            rewards.append(r)
            burdens.append(b)
            q[i, a] += c["lr_policy"] * (r - q[i, a])

        reward_by = np.zeros(k)
        burden_by = np.zeros(k)
        counts = np.zeros(k)
        for a, r, b in zip(actions, rewards, burdens):
            reward_by[a] += r
            burden_by[a] += b
            counts[a] += 1

        used = counts > 0
        mean_reward = np.divide(reward_by, counts, out=np.zeros(k), where=used)
        mean_burden = np.divide(burden_by, counts, out=np.zeros(k), where=used)
        center_r = float(np.mean(mean_reward[used])) if np.any(used) else 0.0
        signal = mean_reward - center_r

        if topology == "returned_revision":
            center_b = float(np.mean(mean_burden[used])) if np.any(used) else 0.0
            signal = signal - c["burden_writeback_weight"] * (mean_burden - center_b)
        elif topology != "externalized":
            raise ValueError(f"unknown topology: {topology}")

        # Equal scaffold-update magnitude budget across conditions.
        norm = float(np.linalg.norm(signal))
        if norm > 1e-12:
            signal = signal / norm
        scaffold = np.clip(
            scaffold + c["lr_scaffold"] * signal,
            -c["scaffold_cap"],
            c["scaffold_cap"],
        )

        scaffold_p = softmax(scaffold, c["temperature"])
        agg_reward.append(float(np.mean(rewards)))
        agg_cost.append(float(np.sum(burdens)))
        alt_mass.append(float(1.0 - scaffold_p[0]))

    def wmean(xs, a, b):
        return float(np.mean(xs[a:b]))

    return {
        "seed": seed,
        "topology": topology,
        "pre_reward": wmean(agg_reward, t_cal - c["summary_window"], t_cal),
        "pre_cost": wmean(agg_cost, t_cal - c["summary_window"], t_cal),
        "pre_alt_mass": wmean(alt_mass, t_cal - c["summary_window"], t_cal),
        "post_reward_early": wmean(agg_reward, t_cal, t_cal + c["early_window"]),
        "post_reward_late": wmean(agg_reward, -c["summary_window"], None),
        "post_cost_early": wmean(agg_cost, t_cal, t_cal + c["early_window"]),
        "post_cost_late": wmean(agg_cost, -c["summary_window"], None),
        "post_alt_mass_early": wmean(alt_mass, t_cal, t_cal + c["early_window"]),
        "post_alt_mass_late": wmean(alt_mass, -c["summary_window"], None),
        "final_scaffold": scaffold.tolist(),
    }


def run_control_b(seed: int, mode: str, c: dict):
    """Calibration only: policy adaptation vs generator revision."""
    rng = np.random.default_rng(seed)
    k = c["B_K"]
    t_cal = c["B_calibration_steps"]
    t_post = c["B_post_steps"]
    q = np.zeros(k)
    generator = np.asarray(c["B_initial_generator"], dtype=float)
    pre_rewards = np.asarray(c["B_pre_rewards"], dtype=float)
    post_rewards = np.asarray(c["B_post_rewards"], dtype=float)
    perf = []

    for t in range(t_cal + t_post):
        rewards = pre_rewards if t < t_cal else post_rewards
        p = softmax(q + generator, c["B_temperature"])
        a = int(rng.choice(k, p=p))
        r = float(rewards[a] + rng.normal(0.0, c["B_reward_noise"]))

        if mode == "policy_only":
            q[a] += c["B_total_update_budget"] * (r - q[a])
        elif mode == "generator_revision":
            # Split the same total update budget between policy and generator.
            half = 0.5 * c["B_total_update_budget"]
            q[a] += half * (r - q[a])
            target = rewards - float(np.mean(rewards))
            norm = float(np.linalg.norm(target))
            if norm > 1e-12:
                target = target / norm
            generator += half * target
        else:
            raise ValueError(f"unknown B mode: {mode}")
        perf.append(r)

    return {
        "seed": seed,
        "mode": mode,
        "pre_performance": float(np.mean(perf[t_cal-c["B_summary_window"]:t_cal])),
        "post_performance_early": float(np.mean(perf[t_cal:t_cal+c["B_early_window"]])),
        "post_performance_late": float(np.mean(perf[-c["B_summary_window"]:])),
        "final_generator": generator.tolist(),
    }


def load_config(path: str | Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))
