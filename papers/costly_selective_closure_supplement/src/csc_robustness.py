"""
Robustness pass for the Costly Selective Closure experiment.

  (1) LIVES GRADIENT. Generalise 'terminate vs reset' to a maximum number of
      lives before termination: 1 (real) -> 2 -> 4 -> 8 -> unbounded
      (resettable). This turns the binary contrast into a dose-response curve;
      the prediction is that post-withdrawal cooperation falls monotonically as
      the life budget increases.

  (2) PAYOFF SWEEP. Vary the temptation payoff T and the mutual-defection
      starvation rate to check that real > resettable holds across the grid
      rather than at a single cell.

Reuses the exact policy / REINFORCE / reward structure of csc_experiment.py.
The single manipulated variable remains token-level irreversibility (max_lives);
the reward function is identical across levels.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent

N_FEATURES, N_HIDDEN, N_ACTIONS = 12, 16, 3
E_MAX, E_0, METABOLIC, T_HORIZON = 10.0, 6.0, 1.0, 50
INF_LIVES = 10**9

BASE_REWARD = {
    (0, 0): 1.0, (0, 1): 0.0, (0, 2): 0.2,
    (1, 0): 1.4, (1, 1): 0.6, (1, 2): 0.9,
    (2, 0): 0.25, (2, 1): 0.25, (2, 2): 0.25,
}
BASE_ENERGY = {
    (0, 0): 2.0, (0, 1): 0.0, (0, 2): 0.4,
    (1, 0): 1.2, (1, 1): 0.7, (1, 2): 1.0,
    (2, 0): 0.5, (2, 1): 0.5, (2, 2): 0.5,
}
DEATH_PENALTY = 2.0
COOP_BONUS = 1.0


def softmax(z):
    z = z - np.max(z); ez = np.exp(z); return ez / ez.sum()


class Policy:
    def __init__(self, rng):
        self.W1 = rng.normal(0, 0.18, (N_HIDDEN, N_FEATURES)); self.b1 = np.zeros(N_HIDDEN)
        self.W2 = rng.normal(0, 0.18, (N_ACTIONS, N_HIDDEN)); self.b2 = np.zeros(N_ACTIONS)

    def forward(self, x):
        h = np.tanh(self.W1 @ x + self.b1); return h, softmax(self.W2 @ h + self.b2)

    def act(self, x, rng):
        h, p = self.forward(x); return int(rng.choice(N_ACTIONS, p=p)), (x, h, p)

    def update(self, traj, lr, gamma):
        if not traj: return
        dW1 = np.zeros_like(self.W1); db1 = np.zeros_like(self.b1)
        dW2 = np.zeros_like(self.W2); db2 = np.zeros_like(self.b2)
        G = 0.0; returns = []
        for *_p, r in reversed(traj):
            G = r + gamma * G; returns.append(G)
        returns = np.array(list(reversed(returns)))
        if returns.std() > 1e-8: returns = (returns - returns.mean()) / (returns.std() + 1e-8)
        for (x, h, p, a, _r), G in zip(traj, returns):
            gz2 = -p.copy(); gz2[a] += 1.0; gz2 *= G
            dW2 += np.outer(gz2, h); db2 += gz2
            dz1 = (self.W2.T @ gz2) * (1.0 - h * h)
            dW1 += np.outer(dz1, x); db1 += dz1
        s = 1.0 / max(1, len(traj))
        self.W1 += lr * dW1 * s; self.b1 += lr * db1 * s
        self.W2 += lr * dW2 * s; self.b2 += lr * db2 * s

    def jac(self, x):
        z1 = self.W1 @ x + self.b1
        return self.W2 @ ((1.0 - np.tanh(z1) ** 2)[:, None] * self.W1)


class Env:
    def __init__(self, rng, max_lives, reward, energy, death_penalty=DEATH_PENALTY):
        self.rng = rng; self.max_lives = max_lives
        self.reward = reward; self.energy_gain = energy; self.death_penalty = death_penalty
        self.reset()

    def reset(self):
        self.energy = np.array([E_0, E_0], float)
        self.alive = np.array([1, 1], int)
        self.deaths = np.array([0, 0], int)
        self.last_action = np.array([2, 2], int)
        self.last_fail = np.array([0, 0], int)
        self.step_idx = 0; self.mortality_seen = 0

    def obs(self, i):
        j = 1 - i
        return np.array([
            1.0, self.energy[i] / E_MAX, self.energy[j] / E_MAX,
            1.0 if self.energy[i] <= 2 else 0.0, 1.0 if self.energy[j] <= 2 else 0.0,
            1.0 if self.last_action[j] == 0 else 0.0, 1.0 if self.last_action[j] == 1 else 0.0,
            float(self.last_fail[i]), float(self.last_fail[j]),
            1.0 - self.step_idx / T_HORIZON, float(self.mortality_seen),
            1.0 if self.last_action[i] == 0 else 0.0,
        ], float)

    def step(self, actions, bonus):
        rew = np.zeros(2); self.last_fail[:] = 0; self.energy -= METABOLIC
        for i in range(2):
            k = (int(actions[i]), int(actions[1 - i]))
            self.energy[i] += self.energy_gain[k]; rew[i] += self.reward[k]
        mutual = int(actions[0] == 0 and actions[1] == 0)
        if bonus and mutual: rew += COOP_BONUS
        fails = 0
        for i in range(2):
            if self.energy[i] <= 0 and self.alive[i]:
                fails += 1; self.last_fail[i] = 1; self.mortality_seen = 1
                self.deaths[i] += 1; rew[i] -= self.death_penalty
                if self.deaths[i] >= self.max_lives:
                    self.alive[i] = 0
                else:
                    self.energy[i] = E_0
        self.last_action = actions.copy(); self.step_idx += 1
        done = self.step_idx >= T_HORIZON or np.any(self.alive == 0)
        return rew, done, fails, mutual


def run_ep(pols, env, rng, bonus, collect=None):
    env.reset(); trajs = [[], []]; mutual = 0; both = 0; fails = 0
    while True:
        acts = np.zeros(2, int); caches = []
        alive_both = bool(env.alive[0] and env.alive[1])
        for i in range(2):
            x = env.obs(i); a, c = pols[i].act(x, rng); acts[i] = a; caches.append(c)
            if collect is not None and alive_both: collect.append(x.copy())
        rew, done, nf, m = env.step(acts, bonus); fails += nf
        if alive_both: both += 1; mutual += m
        for i in range(2):
            x, h, p = caches[i]; trajs[i].append((x, h, p, int(acts[i]), float(rew[i])))
        if done: break
    return trajs, mutual / max(1, both), env.step_idx, fails


def eff_rank(pol, states):
    if not states: return 0.0
    J = np.concatenate([pol.jac(x) for x in states], 0)
    e = np.linalg.eigvalsh(J.T @ J); e = e[e > 1e-8]
    return float((e.sum() ** 2) / np.square(e).sum()) if len(e) else 0.0


def run_condition(max_lives, seed, reward, energy, cfg):
    rng = np.random.default_rng(seed)
    pols = [Policy(rng), Policy(rng)]
    env = Env(rng, max_lives, reward, energy)
    ch = []
    for _ in range(cfg["train_eps"]):
        trajs, c, _, _ = run_ep(pols, env, rng, True)
        for i in range(2): pols[i].update(trajs[i], cfg["lr"], cfg["gamma"])
        ch.append(c)
    baseline = float(np.mean(ch[-cfg["window"]:]))
    st = []
    for _ in range(24): run_ep(pols, env, rng, True, collect=st)
    d_eff = eff_rank(pols[0], st[:96])
    wc, wf = [], []
    for _ in range(cfg["withdraw_eps"]):
        trajs, c, ln, f = run_ep(pols, env, rng, False)
        for i in range(2): pols[i].update(trajs[i], cfg["lr"], cfg["gamma"])
        wc.append(c); wf.append(f)
    tail = cfg["window"]
    return {"max_lives": max_lives, "seed": seed, "baseline_coop": baseline,
            "post_coop": float(np.mean(wc[-tail:])), "post_fail": float(np.mean(wf[-tail:])),
            "d_eff": d_eff}


def permutation(a, b, n=20000, seed=0):
    a = np.asarray(a, float); b = np.asarray(b, float)
    obs = a.mean() - b.mean(); pool = np.concatenate([a, b]); na = len(a)
    rng = np.random.default_rng(seed); c = 0
    for _ in range(n):
        rng.shuffle(pool)
        if abs(pool[:na].mean() - pool[na:].mean()) >= abs(obs) - 1e-12: c += 1
    return float(obs), float((c + 1) / (n + 1))


def _avg_rank(a):
    """Average (tie-aware) ranks, 1..n, with ties sharing their mean rank."""
    a = np.asarray(a, float)
    order = np.argsort(a, kind="mergesort")
    ranks = np.empty(len(a), float)
    ranks[order] = np.arange(1, len(a) + 1)
    sa = a[order]
    i = 0
    while i < len(a):
        j = i
        while j + 1 < len(a) and sa[j + 1] == sa[i]:
            j += 1
        if j > i:
            ranks[order[i:j + 1]] = (i + j) / 2.0 + 1
        i = j + 1
    return ranks


def spearman(x, y):
    """Tie-aware Spearman rank correlation (Pearson correlation of average
    ranks). Correct for the lives gradient, where both the level and the
    cooperation values contain many ties."""
    rx = _avg_rank(x); rx = rx - rx.mean()
    ry = _avg_rank(y); ry = ry - ry.mean()
    return float((rx @ ry) / (np.sqrt((rx @ rx) * (ry @ ry)) + 1e-12))


def spearman_perm_p(x, y, n_resamples=20000, seed=0):
    """Tie-aware Spearman rho and its two-sided permutation p-value (shuffling
    the pairing; the rank vectors and their norms are invariant, so only the
    cross term is recomputed)."""
    rx = _avg_rank(x); rx = rx - rx.mean()
    ry = _avg_rank(y); ry = ry - ry.mean()
    den = np.sqrt((rx @ rx) * (ry @ ry)) + 1e-12
    rho = (rx @ ry) / den
    rng = np.random.default_rng(seed)
    ry_perm = ry.copy()
    count = 0
    for _ in range(n_resamples):
        rng.shuffle(ry_perm)
        if abs((rx @ ry_perm) / den) >= abs(rho) - 1e-12:
            count += 1
    return float(rho), float((count + 1) / (n_resamples + 1))


CFG = dict(train_eps=1000, withdraw_eps=300, window=100, lr=0.04, gamma=0.97)


def gradient(seeds):
    levels = [(1, "L1(real)"), (2, "L2"), (4, "L4"), (8, "L8"), (INF_LIVES, "Linf(reset)")]
    runs = []
    for lv, name in levels:
        for s in seeds:
            r = run_condition(lv, s, BASE_REWARD, BASE_ENERGY, CFG); r["level"] = name; runs.append(r)
    out = {"seeds": seeds, "runs": runs, "summary": {}}
    print(f"\n=== LIVES GRADIENT (n_seeds={len(seeds)}) ===")
    print(f"{'level':<14}{'post_coop':>10}{'%coop':>8}{'deaths/ep':>11}{'d_eff':>7}")
    all_lv, all_c = [], []
    for lv, name in levels:
        pc = np.array([r["post_coop"] for r in runs if r["level"] == name])
        pf = np.array([r["post_fail"] for r in runs if r["level"] == name])
        de = np.array([r["d_eff"] for r in runs if r["level"] == name])
        out["summary"][name] = {"post_coop_mean": float(pc.mean()), "post_coop_std": float(pc.std()),
                                "frac_coop": float(np.mean(pc > 0.3)), "deaths": float(pf.mean()),
                                "d_eff": float(de.mean())}
        print(f"{name:<14}{pc.mean():>10.3f}{100*np.mean(pc>0.3):>7.0f}%{pf.mean():>11.2f}{de.mean():>7.2f}")
        lvl_num = np.log2(lv) if lv < INF_LIVES else np.log2(16)
        all_lv += [lvl_num] * len(pc); all_c += list(pc)
    rho, rho_p = spearman_perm_p(all_lv, all_c)
    o, p = permutation([r["post_coop"] for r in runs if r["level"] == "L1(real)"],
                       [r["post_coop"] for r in runs if r["level"] == "Linf(reset)"])
    out["spearman_lives_vs_coop"] = rho
    out["spearman_p"] = rho_p
    out["L1_vs_Linf"] = {"diff": o, "p": p}
    print(f"\nSpearman(lives, post_coop) = {rho:+.3f}  (perm p = {rho_p:.4f}; negative = more lives -> less cooperation)")
    print(f"L1(real) vs Linf(reset): diff={o:+.3f}, p={p:.4f}")
    (ROOT / "results_gradient.json").write_text(json.dumps(out, indent=2))


def sweep(seeds):
    Ts = [1.2, 1.4, 1.6]
    defect_nets = {"-0.15": 0.85, "-0.45": 0.55}  # ENERGY_GAIN[(1,1)] value -> net after metabolic 1.0
    print(f"\n=== PAYOFF SWEEP (n_seeds={len(seeds)}) real(L1) vs resettable(Linf) ===")
    print(f"{'T':>5}{'defect_net':>12}{'real':>8}{'reset':>8}{'diff':>8}{'p':>9}")
    grid = []
    for T in Ts:
        rw = dict(BASE_REWARD); rw[(1, 0)] = T
        for label, e11 in defect_nets.items():
            en = dict(BASE_ENERGY); en[(1, 1)] = e11
            real = [run_condition(1, s, rw, en, CFG)["post_coop"] for s in seeds]
            reset = [run_condition(INF_LIVES, s, rw, en, CFG)["post_coop"] for s in seeds]
            o, p = permutation(real, reset)
            grid.append({"T": T, "defect_net": label, "real_mean": float(np.mean(real)),
                         "reset_mean": float(np.mean(reset)), "diff": o, "p": p})
            print(f"{T:>5.1f}{label:>12}{np.mean(real):>8.2f}{np.mean(reset):>8.2f}{o:>+8.2f}{p:>9.4f}")
    (ROOT / "results_sweep.json").write_text(json.dumps({"seeds": seeds, "grid": grid}, indent=2))


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "gradient"
    if mode == "gradient":
        gradient(list(range(1, 31)))
    elif mode == "sweep":
        sweep(list(range(1, 16)))
