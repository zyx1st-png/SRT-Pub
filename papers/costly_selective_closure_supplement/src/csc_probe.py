"""Common-state policy probe.

Tests whether the FROZEN policies differ on IDENTICAL observation inputs, which
rules out the possibility that the rollout cooperation gap is merely an artifact
of unequal episode lengths / computing cooperation only over surviving steps.

Design (see README, Statistical tests):
  - Headline bank: mortality_token = 0 only, and restricted to the COMMON
    support of real and resettable (energy x time-to-horizon cells reached by
    BOTH regimes at >= MIN_CELL states), with balanced 50/50 real/resettable
    contribution per cell.
  - The bank is built from SEPARATE bank-generation seeds; the evaluation-seed
    policies never contribute bank states.
  - Every evaluation policy is scored on the same global bank.
  - Two checkpoints per (regime, seed): end-of-training and end-of-withdrawal.
  - A mortality_token = 1 bank is built as an EXPLORATORY out-of-distribution
    stress test only (real has essentially no such states, so it is not common
    support and never enters the headline result).
"""
import json
import platform
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from csc_experiment import Policy, Env, train_condition  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent  # supplement/
CFG = dict(train_eps=1000, withdraw_eps=300, window=100, lr=0.04, lr_w=0.04, gamma=0.97)

EVAL_SEEDS = list(range(1, 31))
BANK_SEEDS = list(range(1001, 1011))     # disjoint from EVAL_SEEDS
BANK_RNG_SEED = 12345
MIN_CELL = 30                            # min per-regime states for a common-support cell
HELDOUT_EPS = 40                         # held-out episodes per bank-gen condition
N_BOOT = 10000
N_PERM = 20000


def p_coop(pol, x):
    return float(pol.forward(x)[1][0])   # softmax P(cooperate); action 0 = cooperate


def rollout_pairs(pols, regime, n_eps, rng):
    """Frozen-policy held-out rollout; record (obs0, obs1) at both-alive steps."""
    env = Env(regime, rng)
    pairs = []
    for _ in range(n_eps):
        env.reset()
        while True:
            both = bool(env.alive[0] and env.alive[1])
            o0, o1 = env.obs(0), env.obs(1)
            a0 = pols[0].act(o0, rng)[0]
            a1 = pols[1].act(o1, rng)[0]
            if both:
                pairs.append((o0, o1))
            _, done, _, _ = env.step(np.array([a0, a1]), bonus_active=False)
            if done:
                break
    return pairs


def _cell(pr):
    e = (pr[0][1] + pr[1][1]) / 2.0                 # mean normalized energy
    eb = "low" if e < 0.3 else ("mid" if e < 0.6 else "high")
    t = pr[0][9]                                    # time-to-horizon (shared by pair)
    tb = "early" if t > 0.66 else ("middle" if t > 0.33 else "late")
    return (eb, tb)


def _mort0(pr):
    return pr[0][10] < 0.5 and pr[1][10] < 0.5


def build_bank():
    gen_rng = np.random.default_rng(BANK_RNG_SEED)
    pools = {"real": [], "resettable": []}
    for regime in ("real", "resettable"):
        for s in BANK_SEEDS:
            _, _, ckpt_w = train_condition(regime, s, CFG, return_ckpts=True)
            pools[regime].extend(rollout_pairs(ckpt_w, regime, HELDOUT_EPS, gen_rng))

    mort1 = {r: [p for p in pools[r] if not _mort0(p)] for r in pools}
    pools = {r: [p for p in pools[r] if _mort0(p)] for r in pools}

    cellsR, cellsRe = defaultdict(list), defaultdict(list)
    for p in pools["real"]:
        cellsR[_cell(p)].append(p)
    for p in pools["resettable"]:
        cellsRe[_cell(p)].append(p)

    all_cells = sorted(set(cellsR) | set(cellsRe))
    report, valid = [], []
    for c in all_cells:
        nr, nre = len(cellsR[c]), len(cellsRe[c])
        ok = nr >= MIN_CELL and nre >= MIN_CELL
        report.append({"cell": list(c), "real_n": nr, "reset_n": nre, "valid": ok})
        if ok:
            valid.append(c)

    m = min(min(len(cellsR[c]), len(cellsRe[c])) for c in valid) if valid else 0
    brng = np.random.default_rng(BANK_RNG_SEED + 1)
    bank = []
    for c in valid:
        for pool in (cellsR[c], cellsRe[c]):
            idx = brng.choice(len(pool), m, replace=False)
            bank.extend((pool[i][0], pool[i][1]) for i in idx)
    for r in report:
        r["sampled_per_regime"] = m if tuple(r["cell"]) in valid else 0

    # exploratory OOD (mort=1); real has ~none, so use resettable's states
    ood_rng = np.random.default_rng(BANK_RNG_SEED + 2)
    ood_pool = mort1["resettable"]
    ood = []
    if len(ood_pool) > 200:
        idx = ood_rng.choice(len(ood_pool), min(len(ood_pool), 1500), replace=False)
        ood = [(ood_pool[i][0], ood_pool[i][1]) for i in idx]

    bank_meta = {
        "min_cell": MIN_CELL, "sampled_per_regime_per_cell": m,
        "n_valid_cells": len(valid), "bank_size": len(bank),
        "cells": report, "excluded_cells": [r["cell"] for r in report if not r["valid"]],
        "mort1_real_n": len(mort1["real"]), "mort1_reset_n": len(mort1["resettable"]),
        "ood_bank_size": len(ood),
    }
    return bank, ood, bank_meta


def diag(ckpt, bank):
    pcc = np.mean([p_coop(ckpt[0], o0) * p_coop(ckpt[1], o1) for o0, o1 in bank])
    pc = np.mean([(p_coop(ckpt[0], o0) + p_coop(ckpt[1], o1)) / 2 for o0, o1 in bank])
    return float(pcc), float(pc)


def evaluate(bank, ood):
    ck_names = ["end_of_training", "end_of_withdrawal"]
    out = {n: {r: {} for r in ("real", "resettable", "simulated")} for n in ck_names}
    ood_out = {r: {} for r in ("real", "resettable", "simulated")}
    anchors = []
    for regime in ("real", "resettable", "simulated"):
        for s in EVAL_SEEDS:
            res, ck_t, ck_w = train_condition(regime, s, CFG, return_ckpts=True)
            anchors.append({k: res[k] for k in
                            ("regime", "seed", "baseline_coop", "frozen_coop",
                             "post_coop", "post_len", "post_fail", "d_eff")})
            for name, ck in (("end_of_training", ck_t), ("end_of_withdrawal", ck_w)):
                pcc, pc = diag(ck, bank)
                out[name][regime][str(s)] = {"pcc": pcc, "pc": pc}
            if ood:
                pcc, _ = diag(ck_w, ood)
                ood_out[regime][str(s)] = {"pcc": pcc}
    return out, ood_out, anchors


def _bootstrap_ci(x, seed=0):
    x = np.asarray(x, float)
    rng = np.random.default_rng(seed)
    boot = rng.choice(x, size=(N_BOOT, len(x)), replace=True).mean(axis=1)
    lo, hi = np.percentile(boot, [2.5, 97.5])
    return float(x.mean()), float(lo), float(hi)


def _paired_signflip_p(diffs, seed=0):
    diffs = np.asarray(diffs, float)
    obs = diffs.mean()
    rng = np.random.default_rng(seed)
    perm = (rng.choice([-1.0, 1.0], size=(N_PERM, len(diffs))) * diffs).mean(axis=1)
    return float((np.sum(np.abs(perm) >= abs(obs) - 1e-12) + 1) / (N_PERM + 1))


def summarize(out):
    summ = {}
    for name in out:
        summ[name] = {}
        vals = {r: np.array([out[name][r][str(s)]["pcc"] for s in EVAL_SEEDS]) for r in out[name]}
        for r, v in vals.items():
            q1, med, q3 = np.percentile(v, [25, 50, 75])
            summ[name][r] = {"mean": float(v.mean()), "median": float(med),
                             "iqr": [float(q1), float(q3)], "min": float(v.min()),
                             "max": float(v.max()), "frac_gt_0.5": float(np.mean(v > 0.5))}
        d = vals["real"] - vals["resettable"]        # paired by seed
        mean_d, lo, hi = _bootstrap_ci(d)
        summ[name]["real_minus_resettable"] = {
            "mean_diff": mean_d, "median_diff": float(np.median(d)),
            "boot95": [lo, hi], "paired_signflip_p": _paired_signflip_p(d),
            "per_seed_diff": [float(x) for x in d]}
    return summ


def _git_commit():
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True).stdout.strip()
    except Exception:
        return "unknown"


def run():
    bank, ood, bank_meta = build_bank()
    out, ood_out, anchors = evaluate(bank, ood)
    summ = summarize(out)

    # cross-check retrained rollout anchors vs committed main_results
    def amean(reg, key):
        return float(np.mean([a[key] for a in anchors if a["regime"] == reg]))
    anchor_check = {reg: {k: amean(reg, k) for k in
                          ("baseline_coop", "frozen_coop", "post_coop", "post_len", "post_fail", "d_eff")}
                    for reg in ("real", "resettable", "simulated")}

    report = {
        "meta": {
            "python": platform.python_version(), "numpy": np.__version__,
            "platform": platform.platform(), "git_commit": _git_commit(),
            "eval_seeds": EVAL_SEEDS, "bank_gen_seeds": BANK_SEEDS,
            "bank_rng_seed": BANK_RNG_SEED, "n_boot": N_BOOT, "n_perm": N_PERM,
            "cfg": CFG,
        },
        "bank": bank_meta,
        "summary": summ,
        "anchor_check": anchor_check,
        "raw": {"common_state": out, "ood_mort1_exploratory": ood_out, "rollout_anchors": anchors},
    }
    (ROOT / "results" / "common_state_probe.json").write_text(json.dumps(report, indent=2))
    return report


if __name__ == "__main__":
    run()
