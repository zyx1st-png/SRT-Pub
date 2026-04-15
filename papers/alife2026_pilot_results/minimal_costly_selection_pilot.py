from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
OUT_JSON = ROOT / "pilot_results.json"
OUT_MD = ROOT / "pilot_results_summary.md"


N_FEATURES = 12
N_HIDDEN = 12
N_ACTIONS = 3  # cooperate, solo, rest


def softmax(z: np.ndarray) -> np.ndarray:
    z = z - np.max(z)
    ez = np.exp(z)
    return ez / np.sum(ez)


@dataclass
class EpisodeStats:
    mutual_coop_rate: float
    episode_length: int
    failures: int


class SharedPolicy:
    def __init__(self, rng: np.random.Generator):
        self.W1 = rng.normal(0.0, 0.18, size=(N_HIDDEN, N_FEATURES))
        self.b1 = np.zeros(N_HIDDEN)
        self.W2 = rng.normal(0.0, 0.18, size=(N_ACTIONS, N_HIDDEN))
        self.b2 = np.zeros(N_ACTIONS)

    def forward(self, x: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        z1 = self.W1 @ x + self.b1
        h = np.tanh(z1)
        z2 = self.W2 @ h + self.b2
        p = softmax(z2)
        return h, z2, p

    def act(self, x: np.ndarray, rng: np.random.Generator) -> tuple[int, tuple[np.ndarray, np.ndarray, np.ndarray]]:
        h, z2, p = self.forward(x)
        a = int(rng.choice(N_ACTIONS, p=p))
        return a, (x, h, p)

    def update(self, trajectories: list[list[tuple[np.ndarray, np.ndarray, np.ndarray, int, float]]], lr: float, gamma: float) -> None:
        dW1 = np.zeros_like(self.W1)
        db1 = np.zeros_like(self.b1)
        dW2 = np.zeros_like(self.W2)
        db2 = np.zeros_like(self.b2)

        for traj in trajectories:
            returns = []
            G = 0.0
            for *_prefix, reward in reversed(traj):
                G = reward + gamma * G
                returns.append(G)
            returns = np.array(list(reversed(returns)))
            if returns.std() > 1e-8:
                returns = (returns - returns.mean()) / (returns.std() + 1e-8)

            for (x, h, p, a, _reward), G in zip(traj, returns):
                grad_z2 = -p
                grad_z2[a] += 1.0
                grad_z2 *= G
                dW2 += np.outer(grad_z2, h)
                db2 += grad_z2
                dh = self.W2.T @ grad_z2
                dz1 = dh * (1.0 - h * h)
                dW1 += np.outer(dz1, x)
                db1 += dz1

        scale = 1.0 / max(1, sum(len(t) for t in trajectories))
        self.W1 += lr * dW1 * scale
        self.b1 += lr * db1 * scale
        self.W2 += lr * dW2 * scale
        self.b2 += lr * db2 * scale

    def jacobian_logits(self, x: np.ndarray) -> np.ndarray:
        z1 = self.W1 @ x + self.b1
        sech2 = 1.0 - np.tanh(z1) ** 2
        return self.W2 @ (sech2[:, None] * self.W1)


class StakesEnv:
    def __init__(self, regime: str, rng: np.random.Generator):
        self.regime = regime
        self.rng = rng
        self.max_steps = 24
        self.reset()

    def reset(self) -> None:
        self.energy = np.array([6.0, 6.0], dtype=float)
        self.alive = np.array([1, 1], dtype=int)
        self.last_action = np.array([2, 2], dtype=int)
        self.last_fail = np.array([0, 0], dtype=int)
        self.step_idx = 0
        self.mortality_seen = 0
        self.current_threat = 0

    def obs(self, i: int, coop_bonus_active: bool) -> np.ndarray:
        j = 1 - i
        threat = self.current_threat
        return np.array(
            [
                1.0,
                self.energy[i] / 6.0,
                self.energy[j] / 6.0,
                1.0 if self.energy[i] <= 2.0 else 0.0,
                1.0 if self.energy[j] <= 2.0 else 0.0,
                float(threat),
                1.0 if self.last_action[i] == 0 else 0.0,
                1.0 if self.last_action[j] == 0 else 0.0,
                float(self.last_fail[i]),
                float(self.last_fail[j]),
                1.0 - self.step_idx / self.max_steps,
                float(self.mortality_seen or (self.regime == "simulated")),
            ],
            dtype=float,
        )

    def step(self, actions: np.ndarray, coop_bonus_active: bool) -> tuple[np.ndarray, bool, int]:
        rewards = np.zeros(2, dtype=float)
        mutual_coop = int(actions[0] == 0 and actions[1] == 0)
        self.last_fail[:] = 0

        # base decay
        self.energy -= 1.0

        if actions[0] == 0 and actions[1] == 0:
            gains = 1.25 + 0.55 * self.current_threat
            self.energy += gains
            rewards += 0.80 + 0.35 * self.current_threat
        elif actions[0] == 1 and actions[1] == 1:
            gains = 1.15 - 0.95 * self.current_threat
            self.energy += gains
            rewards += 0.75 - 0.25 * self.current_threat
        else:
            for i, a in enumerate(actions):
                if a == 0:  # cooperated alone
                    gains = 0.35 - 0.75 * self.current_threat
                    rew = 0.15 - 0.25 * self.current_threat
                elif a == 1:  # solo
                    gains = 1.20 - 0.95 * self.current_threat
                    rew = 0.85 - 0.20 * self.current_threat
                else:  # rest
                    gains = 0.55 - 0.10 * self.current_threat
                    rew = 0.20
                self.energy[i] += gains
                rewards[i] += rew

        if coop_bonus_active and mutual_coop:
            rewards += 1.0

        failures = 0
        for i in range(2):
            if self.energy[i] <= 0 and self.alive[i]:
                failures += 1
                self.last_fail[i] = 1
                self.mortality_seen = 1
                if self.regime == "real":
                    self.alive[i] = 0
                    rewards -= 6.0
                elif self.regime == "resettable":
                    rewards[i] -= 0.05
                    self.energy[i] = 6.0
                elif self.regime == "simulated":
                    rewards[i] -= 3.0
                    self.energy[i] = 6.0

        self.last_action = actions.copy()
        self.step_idx += 1
        done = self.step_idx >= self.max_steps or (self.regime == "real" and np.any(self.alive == 0))
        return rewards, done, failures


def run_episode(policy: SharedPolicy, env: StakesEnv, rng: np.random.Generator, *, train: bool, coop_bonus_active: bool) -> tuple[list[list[tuple[np.ndarray, np.ndarray, np.ndarray, int, float]]], EpisodeStats, list[np.ndarray]]:
    env.reset()
    trajectories = [[], []]
    jac_states: list[np.ndarray] = []
    mutual = 0
    failures = 0
    while True:
        actions = np.zeros(2, dtype=int)
        caches: list[tuple[np.ndarray, np.ndarray, np.ndarray]] = []
        env.current_threat = int(env.rng.random() < 0.35)
        for i in range(2):
            x = env.obs(i, coop_bonus_active)
            a, cache = policy.act(x, rng)
            actions[i] = a
            caches.append(cache)
            if train:
                jac_states.append(x.copy())
        rewards, done, new_failures = env.step(actions, coop_bonus_active)
        failures += new_failures
        if actions[0] == 0 and actions[1] == 0:
            mutual += 1
        for i in range(2):
            x, h, p = caches[i]
            trajectories[i].append((x, h, p, int(actions[i]), float(rewards[i])))
        if done:
            break
    stats = EpisodeStats(
        mutual_coop_rate=mutual / env.step_idx,
        episode_length=env.step_idx,
        failures=failures,
    )
    return trajectories, stats, jac_states


def effective_rank(policy: SharedPolicy, states: list[np.ndarray]) -> float:
    mats = [policy.jacobian_logits(x) for x in states]
    J = np.concatenate(mats, axis=0)
    gram = J.T @ J
    eigvals = np.linalg.eigvalsh(gram)
    eigvals = eigvals[eigvals > 1e-8]
    if len(eigvals) == 0:
        return 0.0
    s = eigvals.sum()
    return float((s * s) / np.square(eigvals).sum())


def train_condition(regime: str, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    policy = SharedPolicy(rng)
    env = StakesEnv(regime, rng)

    train_stats = []
    collected_states: list[np.ndarray] = []
    for episode in range(700):
        trajectories, stats, jac_states = run_episode(policy, env, rng, train=True, coop_bonus_active=True)
        policy.update(trajectories, lr=0.035, gamma=0.96)
        train_stats.append(stats)
        if episode >= 620:
            collected_states.extend(jac_states[:4])

    d_eff = effective_rank(policy, collected_states[:96])
    baseline = float(np.mean([s.mutual_coop_rate for s in train_stats[-80:]]))
    baseline_length = float(np.mean([s.episode_length for s in train_stats[-80:]]))
    baseline_failures = float(np.mean([s.failures for s in train_stats[-80:]]))

    withdrawal_rates = []
    withdrawal_lengths = []
    withdrawal_failures = []
    persistence = 120
    for idx in range(120):
        trajectories, stats, _ = run_episode(policy, env, rng, train=True, coop_bonus_active=False)
        policy.update(trajectories, lr=0.03, gamma=0.96)
        withdrawal_rates.append(stats.mutual_coop_rate)
        withdrawal_lengths.append(stats.episode_length)
        withdrawal_failures.append(stats.failures)
        trailing = float(np.mean(withdrawal_rates[max(0, idx - 9) : idx + 1]))
        if trailing < 0.5 * baseline and persistence == 120:
            persistence = idx + 1

    return {
        "seed": seed,
        "regime": regime,
        "d_eff": d_eff,
        "baseline_coop": baseline,
        "baseline_length": baseline_length,
        "baseline_failures": baseline_failures,
        "withdrawal_coop_mean": float(np.mean(withdrawal_rates[-20:])),
        "withdrawal_length_mean": float(np.mean(withdrawal_lengths[-20:])),
        "withdrawal_failures_mean": float(np.mean(withdrawal_failures[-20:])),
        "persistence_episodes": int(persistence),
    }


def summarize(results: list[dict]) -> dict:
    by_regime: dict[str, dict[str, float | list[float]]] = {}
    for regime in sorted({r["regime"] for r in results}):
        rows = [r for r in results if r["regime"] == regime]
        summary: dict[str, float] = {}
        for key in [
            "d_eff",
            "baseline_coop",
            "baseline_length",
            "baseline_failures",
            "withdrawal_coop_mean",
            "withdrawal_length_mean",
            "withdrawal_failures_mean",
            "persistence_episodes",
        ]:
            vals = np.array([row[key] for row in rows], dtype=float)
            summary[key + "_mean"] = float(vals.mean())
            summary[key + "_std"] = float(vals.std(ddof=0))
        by_regime[regime] = summary
    return by_regime


def main() -> None:
    seeds = [3, 7, 11, 19, 23, 29]
    all_results: list[dict] = []
    for regime in ["real", "resettable", "simulated"]:
        for seed in seeds:
            all_results.append(train_condition(regime, seed))

    summary = summarize(all_results)
    OUT_JSON.write_text(json.dumps({"runs": all_results, "summary": summary}, indent=2), encoding="utf-8")

    lines = [
        "# Minimal Costly-Selection Pilot",
        "",
        "Symmetric two-agent environment with shared-policy REINFORCE, 700 training episodes with mutual-cooperation bonus, followed by 120 online adaptation episodes after bonus withdrawal.",
        "",
        "| Regime | d_eff | Baseline mutual cooperation | Post-withdrawal mutual cooperation | Persistence episodes |",
        "|---|---:|---:|---:|---:|",
    ]
    for regime in ["real", "resettable", "simulated"]:
        s = summary[regime]
        lines.append(
            f"| {regime} | {s['d_eff_mean']:.2f} ± {s['d_eff_std']:.2f} | "
            f"{s['baseline_coop_mean']:.2f} ± {s['baseline_coop_std']:.2f} | "
            f"{s['withdrawal_coop_mean_mean']:.2f} ± {s['withdrawal_coop_mean_std']:.2f} | "
            f"{s['persistence_episodes_mean']:.1f} ± {s['persistence_episodes_std']:.1f} |"
        )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")
    for regime in ["real", "resettable", "simulated"]:
        print(regime, summary[regime])


if __name__ == "__main__":
    main()
