"""
Costly Selective Closure -- controlled two-agent experiment.

Question under test:
    Does token-level irreversibility (real-stake) preserve costly cooperation
    better than a cheaply-resettable regime, AFTER an explicit cooperation
    bonus is withdrawn?

Design principles:
  1. Genuine social dilemma (Prisoner's-Dilemma-style immediate reward:
     T=1.4 > R=1.0 > P=0.6 > S=0.0). Unilateral defection is tempting, so
     withdrawing the bonus creates real decay pressure.
  2. Tight energy economy: only mutual cooperation thrives; mutual defection
     slowly starves. This ties survival to cooperation, so death actually
     happens and the terminate-vs-reset manipulation has an effect.
  3. Independent learners (two separate policies) so defection can genuinely
     emerge, rather than a single shared policy that moves in lockstep.
  4. Real and Resettable share an IDENTICAL reward function. The ONLY
     difference is what happens at energy<=0: terminate (real) vs reset
     (resettable). This is a clean single-variable manipulation of
     token-level irreversibility.
  5. Non-saturating continuous metric: post-withdrawal mutual cooperation,
     reported with a permutation test.

The experiment is designed so the prediction CAN show up, but is not guaranteed
to: if survival pressure is too weak, real-stake will unravel into defection
just like resettable, which would be evidence against the claim.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent

N_FEATURES = 12
N_HIDDEN = 16
N_ACTIONS = 3  # 0=Cooperate, 1=Solo/Defect, 2=Rest

E_MAX = 10.0
E_0 = 6.0
METABOLIC = 1.0
T_HORIZON = 50

# --- immediate reward (PD-style) and energy gain, indexed [own_action][partner_action]
# ordering guarantees Temptation(1.4) > Reward(1.0) > Punishment(0.6) > Sucker(0.0)
REWARD = {
    # own = Cooperate
    (0, 0): 1.0, (0, 1): 0.0, (0, 2): 0.2,
    # own = Solo
    (1, 0): 1.4, (1, 1): 0.6, (1, 2): 0.9,
    # own = Rest
    (2, 0): 0.25, (2, 1): 0.25, (2, 2): 0.25,
}
ENERGY_GAIN = {
    (0, 0): 2.0, (0, 1): 0.0, (0, 2): 0.4,
    (1, 0): 1.2, (1, 1): 0.7, (1, 2): 1.0,
    (2, 0): 0.5, (2, 1): 0.5, (2, 2): 0.5,
}

DEATH_PENALTY = 2.0        # applied in ALL regimes (matched)
SIM_DANGER_PENALTY = 1.5   # simulated regime only: extra "represented danger"
COOP_BONUS = 1.0           # training only; withdrawn in phase 2


def softmax(z: np.ndarray) -> np.ndarray:
    z = z - np.max(z)
    ez = np.exp(z)
    return ez / np.sum(ez)


class Policy:
    def __init__(self, rng: np.random.Generator):
        self.W1 = rng.normal(0.0, 0.18, size=(N_HIDDEN, N_FEATURES))
        self.b1 = np.zeros(N_HIDDEN)
        self.W2 = rng.normal(0.0, 0.18, size=(N_ACTIONS, N_HIDDEN))
        self.b2 = np.zeros(N_ACTIONS)

    def forward(self, x):
        z1 = self.W1 @ x + self.b1
        h = np.tanh(z1)
        z2 = self.W2 @ h + self.b2
        return h, softmax(z2)

    def act(self, x, rng):
        h, p = self.forward(x)
        a = int(rng.choice(N_ACTIONS, p=p))
        return a, (x, h, p)

    def update(self, traj, lr, gamma):
        if not traj:
            return
        dW1 = np.zeros_like(self.W1); db1 = np.zeros_like(self.b1)
        dW2 = np.zeros_like(self.W2); db2 = np.zeros_like(self.b2)
        returns = []
        G = 0.0
        for *_p, reward in reversed(traj):
            G = reward + gamma * G
            returns.append(G)
        returns = np.array(list(reversed(returns)))
        if returns.std() > 1e-8:
            returns = (returns - returns.mean()) / (returns.std() + 1e-8)
        for (x, h, p, a, _r), G in zip(traj, returns):
            gz2 = -p.copy(); gz2[a] += 1.0; gz2 *= G
            dW2 += np.outer(gz2, h); db2 += gz2
            dh = self.W2.T @ gz2
            dz1 = dh * (1.0 - h * h)
            dW1 += np.outer(dz1, x); db1 += dz1
        scale = 1.0 / max(1, len(traj))
        self.W1 += lr * dW1 * scale; self.b1 += lr * db1 * scale
        self.W2 += lr * dW2 * scale; self.b2 += lr * db2 * scale

    def jacobian_logits(self, x):
        z1 = self.W1 @ x + self.b1
        sech2 = 1.0 - np.tanh(z1) ** 2
        return self.W2 @ (sech2[:, None] * self.W1)


@dataclass
class Env:
    regime: str
    rng: np.random.Generator
    death_penalty: float = DEATH_PENALTY
    sim_danger_penalty: float = SIM_DANGER_PENALTY
    energy: np.ndarray = field(default_factory=lambda: np.array([E_0, E_0]))
    alive: np.ndarray = field(default_factory=lambda: np.array([1, 1]))
    last_action: np.ndarray = field(default_factory=lambda: np.array([2, 2]))
    last_fail: np.ndarray = field(default_factory=lambda: np.array([0, 0]))
    step_idx: int = 0
    mortality_seen: int = 0

    def reset(self):
        self.energy = np.array([E_0, E_0], dtype=float)
        self.alive = np.array([1, 1], dtype=int)
        self.last_action = np.array([2, 2], dtype=int)
        self.last_fail = np.array([0, 0], dtype=int)
        self.step_idx = 0
        self.mortality_seen = 0

    def obs(self, i):
        j = 1 - i
        return np.array([
            1.0,
            self.energy[i] / E_MAX,
            self.energy[j] / E_MAX,
            1.0 if self.energy[i] <= 2.0 else 0.0,
            1.0 if self.energy[j] <= 2.0 else 0.0,
            1.0 if self.last_action[j] == 0 else 0.0,
            1.0 if self.last_action[j] == 1 else 0.0,
            float(self.last_fail[i]),
            float(self.last_fail[j]),
            1.0 - self.step_idx / T_HORIZON,
            float(self.mortality_seen or (self.regime == "simulated")),
            1.0 if self.last_action[i] == 0 else 0.0,
        ], dtype=float)

    def step(self, actions, bonus_active):
        rewards = np.zeros(2, dtype=float)
        self.last_fail[:] = 0
        self.energy -= METABOLIC
        for i in range(2):
            key = (int(actions[i]), int(actions[1 - i]))
            self.energy[i] += ENERGY_GAIN[key]
            rewards[i] += REWARD[key]
        mutual_coop = int(actions[0] == 0 and actions[1] == 0)
        if bonus_active and mutual_coop:
            rewards += COOP_BONUS

        failures = 0
        for i in range(2):
            if self.energy[i] <= 0 and self.alive[i]:
                failures += 1
                self.last_fail[i] = 1
                self.mortality_seen = 1
                rewards[i] -= self.death_penalty     # matched across regimes
                if self.regime == "real":
                    self.alive[i] = 0
                else:
                    if self.regime == "simulated":
                        rewards[i] -= self.sim_danger_penalty
                    self.energy[i] = E_0             # cheap restore

        self.last_action = actions.copy()
        self.step_idx += 1
        done = self.step_idx >= T_HORIZON or (self.regime == "real" and np.any(self.alive == 0))
        return rewards, done, failures, mutual_coop


def run_episode(policies, env, rng, *, train, bonus_active, collect_states=None):
    env.reset()
    trajs = [[], []]
    mutual = 0
    steps_both_alive = 0
    failures = 0
    while True:
        actions = np.zeros(2, dtype=int)
        caches = []
        both_alive = bool(env.alive[0] and env.alive[1])
        for i in range(2):
            x = env.obs(i)
            a, cache = policies[i].act(x, rng)
            actions[i] = a
            caches.append(cache)
            if collect_states is not None and both_alive:
                collect_states.append(x.copy())
        rewards, done, nfail, mutual_coop = env.step(actions, bonus_active)
        failures += nfail
        if both_alive:
            steps_both_alive += 1
            mutual += mutual_coop
        for i in range(2):
            x, h, p = caches[i]
            trajs[i].append((x, h, p, int(actions[i]), float(rewards[i])))
        if done:
            break
    coop_rate = mutual / max(1, steps_both_alive)
    return trajs, coop_rate, env.step_idx, failures


def effective_rank(policy, states):
    if not states:
        return 0.0
    J = np.concatenate([policy.jacobian_logits(x) for x in states], axis=0)
    eig = np.linalg.eigvalsh(J.T @ J)
    eig = eig[eig > 1e-8]
    if len(eig) == 0:
        return 0.0
    s = eig.sum()
    return float((s * s) / np.square(eig).sum())


def train_condition(regime, seed, cfg):
    rng = np.random.default_rng(seed)
    policies = [Policy(rng), Policy(rng)]
    env = Env(regime, rng,
              death_penalty=cfg.get("death_penalty", DEATH_PENALTY),
              sim_danger_penalty=cfg.get("sim_danger_penalty", SIM_DANGER_PENALTY))

    coop_hist = []
    for ep in range(cfg["train_eps"]):
        trajs, coop, _, _ = run_episode(policies, env, rng, train=True, bonus_active=True)
        for i in range(2):
            policies[i].update(trajs[i], lr=cfg["lr"], gamma=cfg["gamma"])
        coop_hist.append(coop)
    baseline_coop = float(np.mean(coop_hist[-cfg["window"]:]))

    # d_eff on end-of-training policy (agent 0)
    states = []
    for _ in range(24):
        run_episode(policies, env, rng, train=False, bonus_active=True, collect_states=states)
    d_eff = effective_rank(policies[0], states[:96])

    # frozen evaluation: bonus OFF, no learning -> "commitment learned under the regime"
    frozen = [run_episode(policies, env, rng, train=False, bonus_active=False)[1] for _ in range(60)]
    frozen_coop = float(np.mean(frozen))

    # withdrawal phase: bonus off, online learning continues
    w_coop, w_len, w_fail = [], [], []
    for ep in range(cfg["withdraw_eps"]):
        trajs, coop, length, fail = run_episode(policies, env, rng, train=True, bonus_active=False)
        for i in range(2):
            policies[i].update(trajs[i], lr=cfg["lr_w"], gamma=cfg["gamma"])
        w_coop.append(coop); w_len.append(length); w_fail.append(fail)

    tail = cfg["window"]
    post_coop = float(np.mean(w_coop[-tail:]))
    retention = post_coop / baseline_coop if baseline_coop > 1e-6 else 0.0
    return {
        "regime": regime, "seed": seed,
        "baseline_coop": baseline_coop,
        "frozen_coop": frozen_coop,
        "post_coop": post_coop,
        "retention": float(np.clip(retention, 0.0, 2.0)),
        "post_len": float(np.mean(w_len[-tail:])),
        "post_fail": float(np.mean(w_fail[-tail:])),
        "d_eff": d_eff,
        "coop_curve": [float(np.mean(w_coop[k:k + 20])) for k in range(0, len(w_coop), 20)],
    }


def permutation_test(a, b, n=20000, seed=0):
    a = np.asarray(a, float); b = np.asarray(b, float)
    obs = a.mean() - b.mean()
    pool = np.concatenate([a, b]); na = len(a)
    rng = np.random.default_rng(seed)
    count = 0
    for _ in range(n):
        rng.shuffle(pool)
        if abs(pool[:na].mean() - pool[na:].mean()) >= abs(obs) - 1e-12:
            count += 1
    return float(obs), float((count + 1) / (n + 1))


def summarize(results, key):
    out = {}
    for reg in ["real", "resettable", "simulated"]:
        v = np.array([r[key] for r in results if r["regime"] == reg], float)
        out[reg] = (float(v.mean()), float(v.std(ddof=0)))
    return out


def main(cfg, seeds, out_prefix):
    results = []
    for regime in ["real", "resettable", "simulated"]:
        for seed in seeds:
            results.append(train_condition(regime, seed, cfg))

    def col(reg, key):
        return [r[key] for r in results if r["regime"] == reg]

    report = {"config": cfg, "n_seeds": len(seeds), "seeds": seeds}
    for key in ["baseline_coop", "frozen_coop", "post_coop", "retention", "post_len", "post_fail", "d_eff"]:
        report[key] = summarize(results, key)

    tests = {}
    for key in ["frozen_coop", "retention", "post_coop", "post_len"]:
        obs, p = permutation_test(col("real", key), col("resettable", key))
        tests[f"real_vs_resettable__{key}"] = {"diff": obs, "p": p}
        obs2, p2 = permutation_test(col("real", key), col("simulated", key))
        tests[f"real_vs_simulated__{key}"] = {"diff": obs2, "p": p2}
    report["tests"] = tests
    report["runs"] = results

    (ROOT / f"{out_prefix}.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"\n=== {out_prefix}  (n_seeds={len(seeds)}) ===")
    print(f"{'regime':<12} {'base_coop':>10} {'frozen':>9} {'post_coop':>10} {'post_len':>9} {'post_fail':>9} {'d_eff':>7}")
    for reg in ["real", "resettable", "simulated"]:
        def m(k): return summarize(results, k)[reg]
        print(f"{reg:<12} {m('baseline_coop')[0]:>10.3f} {m('frozen_coop')[0]:>9.3f} {m('post_coop')[0]:>10.3f} "
              f"{m('post_len')[0]:>9.1f} {m('post_fail')[0]:>9.2f} {m('d_eff')[0]:>7.2f}")
    print("\npermutation tests (real vs X):")
    for k, v in tests.items():
        print(f"  {k:<40} diff={v['diff']:+.3f}  p={v['p']:.4f}")
    return report


if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "smoke"
    base_cfg = dict(train_eps=1000, withdraw_eps=300, window=100,
                    lr=0.04, lr_w=0.04, gamma=0.97)
    if mode == "smoke":
        main(base_cfg, seeds=[1, 2, 3, 4, 5], out_prefix="smoke")
    elif mode == "full":
        main(base_cfg, seeds=list(range(1, 31)), out_prefix="results_full")
    elif mode == "ablate_nopenalty":
        cfg = dict(base_cfg, death_penalty=0.0, sim_danger_penalty=1.5)
        main(cfg, seeds=list(range(1, 31)), out_prefix="results_nopenalty")
