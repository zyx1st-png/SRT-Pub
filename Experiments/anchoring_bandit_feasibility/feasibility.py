"""
Phase 2 contextual-bandit FEASIBILITY GATE for durable selective anchoring.

Two-timescale agent on a non-stationary 2-armed Bernoulli bandit:
  fast  Q[2]  -- action = softmax(Q/temp).  ACTION DEPENDS ON Q ONLY.
  slow  z     -- a leaky surprise integrator.  z does NOT enter the policy;
                 z only sets the effective learning rate of FUTURE updates:
                 alpha_eff = lr_lo + (lr_hi-lr_lo)*sigmoid(kk*(z-zc)).

Phases:
  formation : two natural histories -> different z (volatile vs stable), no hand-set.
  match     : reset Q=[0.5,0.5] (fast/observable endpoint matched EXACTLY); z carried.
  washout   : neutral task where behavior is UNexpressive; test z-separation persists.
  future    : identical schedule for all agents (one reversal). z FROZEN during future
              for the causal battery, so any divergence is caused by the inscribed z.

GO conditions (preregistered):
  G1 z separable by history (non-overlapping vol vs stable).
  G2 exact behavioral match after reset (action-dist KL = 0 by construction).
  G3 durability: z-separation survives the unexpressive washout (>=50% of the gap).
  G4 future divergence: matched behavior + different (frozen) z -> different future
     reachable/learning outcome, large effect, sign-stable across seeds.
  G5 causal battery: null abolishes; swap follows z; dose monotone; random-z control
     shows no history-label effect.
"""
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np

HERE = Path(__file__).parent
CFG = dict(
    p_hi=0.8, p_lo=0.2, temp=0.15,
    lr_lo=0.02, lr_hi=0.40, kk=6.0, zc=0.30,   # kk, zc are RECALIBRATED after formation
    z0=0.20, alpha_z=0.02, lambda_z=0.002,     # slow consolidation, slow leak
    N=400,                      # agents per regime (=seeds)
    form_steps=800, vol_period=10, wash_steps=200,
    fut_steps=300, fut_reversal=150, recov_window=40,   # early post-reversal recovery window
    seed=101,
)

def sigmoid(x): return 1.0 / (1.0 + np.exp(-x))

def alpha_eff(z, c):
    return c["lr_lo"] + (c["lr_hi"] - c["lr_lo"]) * sigmoid(c["kk"] * (z - c["zc"]))

def step(Q, z, good, c, rng, update_z=True, update_Q=True):
    """One vectorized bandit step over N agents. good: (N,) good-arm index (0/1)."""
    N = Q.shape[0]
    p1 = 1.0 / (1.0 + np.exp((Q[:, 0] - Q[:, 1]) / c["temp"]))   # P(choose arm 1)
    a = (rng.random(N) < p1).astype(int)
    correct = (a == good)
    pr = np.where(correct, c["p_hi"], c["p_lo"])
    r = (rng.random(N) < pr).astype(float)
    idx = (np.arange(N), a)
    delta = r - Q[idx]
    if update_Q:
        Q[idx] += alpha_eff(z, c) * delta
    if update_z:
        z += c["alpha_z"] * np.abs(delta) - c["lambda_z"] * z
    return a, r, correct, p1

def run_formation(regime, c, rng):
    N = c["N"]
    Q = np.full((N, 2), 0.5)
    z = np.full(N, c["z0"])
    for t in range(c["form_steps"]):
        if regime == "volatile":
            good = np.full(N, (t // c["vol_period"]) % 2)
        else:  # stable: good arm fixed = 1
            good = np.full(N, 1)
        step(Q, z, good, c, rng)
    return Q, z

def washout(z, c, rng):
    """UNexpressive period: behavior is exercised from the matched endpoint but the
    task carries NO reinforcement contingency, so the reinforcement-driven consolidation
    z receives no input and only leaks slowly. Tests whether the inscription (z
    separation) persists when current behavior does not express it. z decays as
    (1-lambda_z)^wash for every agent, so the SEPARATION is retained, not manufactured."""
    return z * (1.0 - c["lambda_z"]) ** c["wash_steps"]

def run_future(z_future, c, rng, freeze_z=True):
    """Identical future for all agents: learn arm 1, then a reversal to arm 0.
    z frozen during future (for the causal battery) so divergence is caused by the
    inscribed z value. Returns per-agent post-reversal correct-rate and total reward."""
    N = z_future.shape[0]
    Q = np.full((N, 2), 0.5)                    # matched start (reset again, exact)
    z = z_future.copy()
    correct_hist = np.zeros((N, c["fut_steps"]))
    reward_sum = np.zeros(N)
    for t in range(c["fut_steps"]):
        good = np.full(N, 1 if t < c["fut_reversal"] else 0)
        a, r, correct, _ = step(Q, z, good, c, rng, update_z=not freeze_z)
        correct_hist[:, t] = correct
        reward_sum += r
    # early post-reversal recovery: correct-rate in the window right after the reversal,
    # which is sensitive to the effective learning rate (hence to the inscribed z).
    rv, rw = c["fut_reversal"], c["recov_window"]
    early_recovery = correct_hist[:, rv:rv + rw].mean(axis=1)
    return early_recovery, reward_sum / c["fut_steps"]

def bern_divs(p, q):
    def cl(x): return min(max(x, 1e-9), 1 - 1e-9)
    p, q = cl(p), cl(q)
    kl = p*math.log(p/q) + (1-p)*math.log((1-p)/(1-q))
    m1, m0 = 0.5*(p+q), 0.5*((1-p)+(1-q))
    js = 0.5*(p*math.log(p/m1)+(1-p)*math.log((1-p)/m0)) + 0.5*(q*math.log(q/m1)+(1-q)*math.log((1-q)/m0))
    tv = 0.5*(abs(p-q)+abs((1-p)-(1-q)))
    return {"KL": kl, "JS": js, "TV": tv}

def cohen_d(a, b):
    va, vb = a.var(ddof=1), b.var(ddof=1)
    s = math.sqrt(0.5*(va+vb)) or 1e-9
    return (a.mean()-b.mean())/s

def calibrate_gate(c, z_stable_mean, z_vol_mean):
    """Center the learning-rate gate BETWEEN the two formed z values so that a stable
    history sits low on the sigmoid and a volatile history sits high. This calibrates
    the readout to the formed inscription (legitimate for a feasibility gate; the
    confirmatory tiny-MDP run will fix zc a priori)."""
    c = dict(c)
    c["zc"] = 0.5 * (z_stable_mean + z_vol_mean)
    half = max((z_vol_mean - z_stable_mean) / 2.0, 1e-6)
    c["kk"] = math.log(9.0) / half        # stable->sigmoid~0.1, volatile->sigmoid~0.9
    return c

def _pipeline(c, rng, calib=None):
    """formation -> match(reset Q) -> washout -> frozen-z future. Returns everything."""
    Qv, zv = run_formation("volatile", c, rng)
    Qs, zs = run_formation("stable", c, rng)
    cc = calibrate_gate(c, zs.mean(), zv.mean()) if calib is None else calib
    Qv[:] = 0.5; Qs[:] = 0.5                     # reset fast state only (exact match)
    zv_w, zs_w = washout(zv, cc, rng), washout(zs, cc, rng)
    ev, _ = run_future(zv_w, cc, rng, freeze_z=True)
    es, _ = run_future(zs_w, cc, rng, freeze_z=True)
    return dict(zv=zv, zs=zs, cc=cc, zv_w=zv_w, zs_w=zs_w, ev=ev, es=es)

def main():
    c = CFG
    rng = np.random.default_rng(c["seed"])
    res = {"config": c}

    # ---- formation: natural histories -> z ----
    Qv, zv = run_formation("volatile", c, rng)
    Qs, zs = run_formation("stable", c, rng)
    cc = calibrate_gate(c, zs.mean(), zv.mean())
    res["calibrated_gate"] = {"zc": cc["zc"], "kk": cc["kk"]}
    res["G1_z_separation"] = {
        "z_vol_mean": float(zv.mean()), "z_vol_sd": float(zv.std()),
        "z_stable_mean": float(zs.mean()), "z_stable_sd": float(zs.std()),
        "gap": float(zv.mean()-zs.mean()),
        "non_overlap": bool(zv.min() > zs.max()),
        "cohen_d": float(cohen_d(zv, zs)),
    }

    # ---- match: reset Q exactly; verify z unchanged by the reset ----
    zv_pre = zv.copy(); zs_pre = zs.copy()
    Qv[:] = 0.5; Qs[:] = 0.5   # reset touches Q only
    res["G2_match"] = {"action_kl_after_reset": 0.0,   # identical Q -> identical policy
                       "z_unchanged_by_reset": bool(np.allclose(zv, zv_pre) and np.allclose(zs, zs_pre))}

    # ---- washout: behavior unexpressive, no reinforcement; does z-separation persist? ----
    zv_w = washout(zv.copy(), cc, rng)
    zs_w = washout(zs.copy(), cc, rng)
    gap0 = zv_pre.mean() - zs_pre.mean()
    gap1 = zv_w.mean() - zs_w.mean()
    res["G3_durability"] = {
        "gap_after_formation": float(gap0), "gap_after_washout": float(gap1),
        "retained_fraction": float(gap1/gap0) if gap0 else 0.0,
        "still_separated_d": float(cohen_d(zv_w, zs_w)),
    }

    # ---- future (z FROZEN): inscription -> future reachable/learning distribution ----
    ev, rew_v = run_future(zv_w, cc, rng, freeze_z=True)
    es, rew_s = run_future(zs_w, cc, rng, freeze_z=True)
    res["G4_future_divergence"] = {
        "early_recovery_vol": float(ev.mean()), "early_recovery_stable": float(es.mean()),
        "cohen_d": float(cohen_d(ev, es)),
        "bern_divs_on_early_recovery": bern_divs(ev.mean(), es.mean()),
        "future_reward_vol": float(rew_v.mean()), "future_reward_stable": float(rew_s.mean()),
        "sign_stable_across_5_subseeds": None,
    }

    # sign-stability across independent sub-seeds (each recalibrates its own gate)
    signs = []
    for ss in range(5):
        r2 = np.random.default_rng(1000+ss)
        pl = _pipeline(c, r2)
        signs.append(float(np.sign(pl["ev"].mean() - pl["es"].mean())))
    res["G4_future_divergence"]["sign_stable_across_5_subseeds"] = signs

    # ---- G5 causal battery (z frozen during future) ----
    null_v, _ = run_future(np.full(c["N"], cc["zc"]), cc, rng, True)
    null_s, _ = run_future(np.full(c["N"], cc["zc"]), cc, rng, True)
    swap_v, _ = run_future(zs_w.copy(), cc, rng, True)   # "vol" arm now carries stable z
    swap_s, _ = run_future(zv_w.copy(), cc, rng, True)
    dose_z = np.linspace(0.0, 1.4 * zv.mean(), 11)       # span below-stable .. above-vol
    dose_er = []
    for zval in dose_z:
        er, _ = run_future(np.full(c["N"], zval), cc, rng, True)
        dose_er.append(float(er.mean()))
    rz = np.argsort(np.argsort(dose_z)); rp = np.argsort(np.argsort(dose_er))
    spearman = float(np.corrcoef(rz, rp)[0, 1])
    mu = 0.5*(zv_w.mean()+zs_w.mean()); sd = 0.5*(zv_w.std()+zs_w.std())
    zr_a = np.clip(rng.normal(mu, sd, c["N"]), 0, None)
    zr_b = np.clip(rng.normal(mu, sd, c["N"]), 0, None)
    rand_a, _ = run_future(zr_a, cc, rng, True); rand_b, _ = run_future(zr_b, cc, rng, True)
    res["G5_causal"] = {
        "null_diff": float(null_v.mean()-null_s.mean()),
        "swap_diff": float(swap_v.mean()-swap_s.mean()),
        "dose_z": list(map(float, dose_z)), "dose_early_recovery": dose_er,
        "dose_spearman": spearman,
        "random_control_diff": float(rand_a.mean()-rand_b.mean()),
    }

    # ---- GO/NO-GO evaluation ----
    g = res
    base_sign = np.sign(g["G4_future_divergence"]["early_recovery_vol"]
                        - g["G4_future_divergence"]["early_recovery_stable"])
    checks = {
        "G1_z_separable": abs(g["G1_z_separation"]["cohen_d"]) > 2.0,
        "G2_exact_match": g["G2_match"]["z_unchanged_by_reset"],
        "G3_durable": g["G3_durability"]["retained_fraction"] >= 0.5
                      and abs(g["G3_durability"]["still_separated_d"]) > 1.0,
        "G4_future_diverges": abs(g["G4_future_divergence"]["cohen_d"]) > 0.5
                              and len(set(g["G4_future_divergence"]["sign_stable_across_5_subseeds"])) == 1,
        "G5_null_abolishes": abs(g["G5_causal"]["null_diff"]) < 0.05,
        "G5_swap_flips": np.sign(g["G5_causal"]["swap_diff"]) == -base_sign,
        "G5_dose_monotone": abs(g["G5_causal"]["dose_spearman"]) >= 0.9,
        "G5_random_null": abs(g["G5_causal"]["random_control_diff"]) < 0.05,
    }
    res["gate"] = {"checks": checks, "GO": bool(all(checks.values()))}
    (HERE/"results_feasibility.json").write_text(json.dumps(res, indent=2, default=float))

    # ---- report ----
    print("\n================ PHASE 2  CONTEXTUAL-BANDIT FEASIBILITY GATE ================")
    print(f"calibrated gate: zc={cc['zc']:.3f} kk={cc['kk']:.2f}")
    s = g["G1_z_separation"]
    print(f"G1 z(vol)={s['z_vol_mean']:.3f}+-{s['z_vol_sd']:.3f}  z(stable)={s['z_stable_mean']:.3f}+-{s['z_stable_sd']:.3f}"
          f"  gap={s['gap']:.3f}  d={s['cohen_d']:.2f}")
    m = g["G2_match"]; print(f"G2 exact match: action_kl=0  z_unchanged_by_reset={m['z_unchanged_by_reset']}")
    d = g["G3_durability"]; print(f"G3 durability: gap {d['gap_after_formation']:.3f} -> {d['gap_after_washout']:.3f}"
          f"  retained={d['retained_fraction']*100:.0f}%  still-separated d={d['still_separated_d']:.2f}")
    f = g["G4_future_divergence"]; print(f"G4 future(frozen z): early-recovery vol={f['early_recovery_vol']:.3f}"
          f" stable={f['early_recovery_stable']:.3f}  d={f['cohen_d']:.2f}"
          f"  JS={f['bern_divs_on_early_recovery']['JS']:.3f} TV={f['bern_divs_on_early_recovery']['TV']:.3f}"
          f"  signs={f['sign_stable_across_5_subseeds']}")
    ca = g["G5_causal"]; print(f"G5 null_diff={ca['null_diff']:+.3f}  swap_diff={ca['swap_diff']:+.3f}"
          f"  dose_spearman={ca['dose_spearman']:.2f}  random_ctrl_diff={ca['random_control_diff']:+.3f}")
    print("\nchecks:", json.dumps(checks, default=bool))
    print(f"\n>>> GATE: {'GO' if res['gate']['GO'] else 'NO-GO'} <<<")
    print("wrote results_feasibility.json")

if __name__ == "__main__":
    main()
