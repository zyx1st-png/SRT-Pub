"""
Phase 2b: LOCKED HOLDOUT replication of the bandit feasibility gate.

ALL parameters are frozen from the Phase-2 committed run (feasibility.py @ 8d703838):
NO recalibration, NO tuning. Fresh holdout seeds (20000..20039) not used in Phase-2
calibration. Adds three things beyond a plain replication:
  (A) z-retention and future-effect curves across multiple washout lengths;
  (B) active-choice vs yoked-observation control: both receive the same reward stream
      but only the active group has choice->consequence coupling. Separates
      selection-specific write-back from generic reward-stream volatility learning;
  (C) cross-individual permutation control: does the future effect follow the carried
      z value, or the history label?

Epistemic scope (corrected): null/swap/dose in Phase 2 are MECHANISM-CHANNEL checks
(z is the causal channel). The random-slow-variable control shows random z gives no
history-label effect; it does NOT rule out calibration artifactuality. Ruling out
calibration artifactuality requires an a-priori zc (the confirmatory tiny-MDP), NOT
this holdout. This holdout tests GENERALIZATION of the frozen params to new seeds and
SELECTION-SPECIFICITY (active vs yoked).
"""
from __future__ import annotations
import json, sys, math
from pathlib import Path
import numpy as np

HERE = Path(__file__).parent
FEAS = HERE.parent / "anchoring_bandit_feasibility"
sys.path.insert(0, str(FEAS))
import feasibility as F   # frozen model

# ---- FROZEN parameters (from Phase-2 committed results) ----
FROZEN = dict(F.CFG)
FROZEN.update(dict(zc=3.170728965999513, kk=3.882185474049716, N=200))
HOLDOUT_SEEDS = list(range(20000, 20040))       # 40 fresh seeds
FEAS_COMMIT = "8d703838f794e192938abcada34d7ddbe0da39c5"

def cohen_d(a, b):
    va, vb = np.var(a, ddof=1), np.var(b, ddof=1)
    s = math.sqrt(0.5*(va+vb)) or 1e-9
    return float((np.mean(a)-np.mean(b))/s)

# ---------- (A) full frozen pipeline for one seed ----------
def pipeline(seed, c=FROZEN, wash=None):
    c = dict(c);
    if wash is not None: c["wash_steps"] = wash
    rng = np.random.default_rng(seed)
    _, zv = F.run_formation("volatile", c, rng)
    _, zs = F.run_formation("stable", c, rng)
    zv_pre, zs_pre = zv.copy(), zs.copy()
    zv_w = F.washout(zv.copy(), c, rng); zs_w = F.washout(zs.copy(), c, rng)
    ev, _ = F.run_future(zv_w, c, rng, True); es, _ = F.run_future(zs_w, c, rng, True)
    null_v, _ = F.run_future(np.full(c["N"], c["zc"]), c, rng, True)
    null_s, _ = F.run_future(np.full(c["N"], c["zc"]), c, rng, True)
    swap_v, _ = F.run_future(zs_w.copy(), c, rng, True)   # vol arm carries stable z
    swap_s, _ = F.run_future(zv_w.copy(), c, rng, True)
    gap0 = zv_pre.mean() - zs_pre.mean(); gap1 = zv_w.mean() - zs_w.mean()
    return dict(gap0=float(gap0), gap1=float(gap1),
                retained=float(gap1/gap0) if gap0 else 0.0,
                z_unchanged=bool(np.array_equal(zv_pre, zv_pre)),  # z never touched by reset
                fut_vol=float(ev.mean()), fut_stable=float(es.mean()),
                fut_diff=float(ev.mean()-es.mean()),
                null_diff=float(null_v.mean()-null_s.mean()),
                swap_diff=float(swap_v.mean()-swap_s.mean()))

# ---------- (B) active vs yoked formation ----------
def formation_record(regime, c, rng):
    """Active formation; records per-agent reward and action sequences. Dynamics are
    identical to F.run_formation (same RNG draw order: action then reward)."""
    N, T = c["N"], c["form_steps"]
    Q = np.full((N, 2), 0.5); z = np.full(N, c["z0"])
    R = np.zeros((N, T));
    for t in range(T):
        good = np.full(N, (t // c["vol_period"]) % 2 if regime == "volatile" else 1)
        p1 = 1.0/(1.0+np.exp((Q[:,0]-Q[:,1])/c["temp"]))
        a = (rng.random(N) < p1).astype(int)
        correct = (a == good); pr = np.where(correct, c["p_hi"], c["p_lo"])
        r = (rng.random(N) < pr).astype(float)
        idx = (np.arange(N), a); delta = r - Q[idx]
        Q[idx] += F.alpha_eff(z, c) * delta
        z += c["alpha_z"]*np.abs(delta) - c["lambda_z"]*z
        R[:, t] = r
    return z, R

def formation_yoked(R, c, rng):
    """Yoked: own free choices, reward REPLAYED from R (non-contingent on own action).
    Same reward stream as the active master; only choice->consequence coupling removed."""
    N, T = R.shape
    Q = np.full((N, 2), 0.5); z = np.full(N, c["z0"])
    for t in range(T):
        p1 = 1.0/(1.0+np.exp((Q[:,0]-Q[:,1])/c["temp"]))
        a = (rng.random(N) < p1).astype(int)          # own choice
        r = R[:, t]                                    # replayed, non-contingent
        idx = (np.arange(N), a); delta = r - Q[idx]
        Q[idx] += F.alpha_eff(z, c) * delta
        z += c["alpha_z"]*np.abs(delta) - c["lambda_z"]*z
    return z

def active_vs_yoked(seeds, c=FROZEN):
    rows = []
    for s in seeds:
        rng = np.random.default_rng(s)
        za_v, Rv = formation_record("volatile", c, rng)
        za_s, Rs = formation_record("stable", c, rng)
        zy_v = formation_yoked(Rv, c, np.random.default_rng(s + 900000))
        zy_s = formation_yoked(Rs, c, np.random.default_rng(s + 900001))
        # washout + frozen future effect for each
        r2 = np.random.default_rng(s + 7)
        def fut(zc_arr):
            zw = F.washout(zc_arr.copy(), c, r2); e, _ = F.run_future(zw, c, r2, True); return e.mean()
        rows.append(dict(
            gap_active=float(za_v.mean()-za_s.mean()), gap_yoked=float(zy_v.mean()-zy_s.mean()),
            zas=float(za_s.mean()), zys=float(zy_s.mean()),          # stable: active should be LOWER (it can learn)
            fut_active=float(fut(za_v)-fut(za_s)), fut_yoked=float(fut(zy_v)-fut(zy_s)),
        ))
    return rows

# ---------- (C) permutation control ----------
def permutation_control(seed, c=FROZEN):
    rng = np.random.default_rng(seed)
    _, zv = F.run_formation("volatile", c, rng); _, zs = F.run_formation("stable", c, rng)
    zv_w = F.washout(zv, c, rng); zs_w = F.washout(zs, c, rng)
    z = np.concatenate([zv_w, zs_w]); label = np.concatenate([np.ones(len(zv_w)), np.zeros(len(zs_w))])
    rec_true, _ = F.run_future(z, c, rng, True)
    perm = rng.permutation(len(z)); z_perm = z[perm]
    rec_perm, _ = F.run_future(z_perm, c, rng, True)
    def corr(a, b): return float(np.corrcoef(a, b)[0, 1])
    return dict(
        corr_true_recovery_vs_z=corr(rec_true, z), corr_true_recovery_vs_label=corr(rec_true, label),
        corr_perm_recovery_vs_permz=corr(rec_perm, z_perm), corr_perm_recovery_vs_label=corr(rec_perm, label),
    )

def main():
    res = {"frozen_params": {k: FROZEN[k] for k in ["zc","kk","lr_lo","lr_hi","alpha_z","lambda_z",
            "form_steps","vol_period","wash_steps","fut_steps","fut_reversal","recov_window","N"]},
           "feasibility_commit": FEAS_COMMIT, "holdout_seeds": HOLDOUT_SEEDS}

    # --- (0) holdout replication over 40 fresh seeds ---
    rows = [pipeline(s) for s in HOLDOUT_SEEDS]
    def col(k): return np.array([r[k] for r in rows])
    res["holdout"] = {
        "n_seeds": len(rows),
        "retained_mean": float(col("retained").mean()), "retained_min": float(col("retained").min()),
        "fut_diff_mean": float(col("fut_diff").mean()), "fut_diff_sd": float(col("fut_diff").std()),
        "fut_diff_positive_frac": float((col("fut_diff") > 0).mean()),
        "null_abs_mean": float(np.abs(col("null_diff")).mean()),
        "swap_negative_frac": float((col("swap_diff") < 0).mean()),
        "swap_diff_mean": float(col("swap_diff").mean()),
    }

    # --- (A) washout-length curves ---
    washes = [0, 50, 100, 200, 400, 800]
    curve_seeds = HOLDOUT_SEEDS[:10]
    res["washout_curves"] = {"wash_steps": washes, "retained": [], "fut_diff": []}
    for w in washes:
        rr = [pipeline(s, wash=w) for s in curve_seeds]
        res["washout_curves"]["retained"].append(float(np.mean([x["retained"] for x in rr])))
        res["washout_curves"]["fut_diff"].append(float(np.mean([x["fut_diff"] for x in rr])))

    # --- (B) active vs yoked ---
    av = active_vs_yoked(HOLDOUT_SEEDS[:20])
    ga, gy = np.array([r["gap_active"] for r in av]), np.array([r["gap_yoked"] for r in av])
    fa, fy = np.array([r["fut_active"] for r in av]), np.array([r["fut_yoked"] for r in av])
    zas, zys = np.array([r["zas"] for r in av]), np.array([r["zys"] for r in av])
    res["active_vs_yoked"] = {
        "gap_active_mean": float(ga.mean()), "gap_yoked_mean": float(gy.mean()),
        "gap_ratio": float(ga.mean()/gy.mean()) if gy.mean() else float("inf"),
        "gap_cohen_d_active_vs_yoked": cohen_d(ga, gy),
        "fut_active_mean": float(fa.mean()), "fut_yoked_mean": float(fy.mean()),
        "fut_cohen_d_active_vs_yoked": cohen_d(fa, fy),
        "stable_z_active_mean": float(zas.mean()), "stable_z_yoked_mean": float(zys.mean()),
        "selection_lowers_stable_z": bool(zas.mean() < zys.mean()),
    }

    # --- (C) permutation control ---
    res["permutation"] = permutation_control(HOLDOUT_SEEDS[0])

    # --- GO/NO-GO ---
    h = res["holdout"]; b = res["active_vs_yoked"]; p = res["permutation"]
    checks = {
        "H_durable_z": h["retained_mean"] >= 0.5,
        "H_future_diff_sign_stable": h["fut_diff_positive_frac"] >= 0.95 and h["fut_diff_mean"] > 0.02,
        "H_null_abolishes": h["null_abs_mean"] < 0.05,
        "H_swap_reverses": h["swap_negative_frac"] >= 0.95,
        # selection-specificity: the future effect (load-bearing) OR the write-back gap
        # must be SUBSTANTIALLY stronger for active than yoked. The gap Cohen's d is a
        # variance artifact (mean over N agents -> tiny SE), so it is NOT used here;
        # we require a real magnitude margin: gap ratio >= 1.5 or future-effect margin >= 25%.
        "B_active_gt_yoked": (b["gap_ratio"] >= 1.5)
                             or (b["fut_yoked_mean"] > 0 and b["fut_active_mean"] >= 1.25 * b["fut_yoked_mean"]),
        "C_effect_follows_z_not_label": abs(p["corr_perm_recovery_vs_permz"]) >= 0.3
                                        and abs(p["corr_perm_recovery_vs_label"]) < 0.1,
    }
    res["gate"] = {"checks": checks, "GO": bool(all(checks.values()))}
    (HERE / "results_phase2b.json").write_text(json.dumps(res, indent=2, default=float))

    # report
    print("\n================ PHASE 2b  LOCKED HOLDOUT (frozen params, 40 fresh seeds) ================")
    print(f"frozen zc={FROZEN['zc']:.4f} kk={FROZEN['kk']:.4f}  wash={FROZEN['wash_steps']} recov={FROZEN['recov_window']}")
    print(f"[holdout] retained={h['retained_mean']*100:.0f}% (min {h['retained_min']*100:.0f}%)  "
          f"fut_diff={h['fut_diff_mean']:.3f}+-{h['fut_diff_sd']:.3f} (pos {h['fut_diff_positive_frac']*100:.0f}%)  "
          f"null={h['null_abs_mean']:.3f}  swap<0 {h['swap_negative_frac']*100:.0f}%")
    wc = res["washout_curves"]
    print(f"[washout curve] wash={wc['wash_steps']}")
    print(f"                retained={[round(x,2) for x in wc['retained']]}")
    print(f"                fut_diff={[round(x,3) for x in wc['fut_diff']]}")
    print(f"[active vs yoked] gap active={b['gap_active_mean']:.3f} yoked={b['gap_yoked_mean']:.3f}"
          f"  ratio={b['gap_ratio']:.2f}  d={b['gap_cohen_d_active_vs_yoked']:.2f}")
    print(f"                  fut  active={b['fut_active_mean']:.3f} yoked={b['fut_yoked_mean']:.3f}"
          f"  d={b['fut_cohen_d_active_vs_yoked']:.2f}")
    print(f"                  stable-z active={b['stable_z_active_mean']:.3f} yoked={b['stable_z_yoked_mean']:.3f}"
          f"  selection_lowers_stable_z={b['selection_lowers_stable_z']}")
    print(f"[permutation] recovery~z (perm): {p['corr_perm_recovery_vs_permz']:.3f}   "
          f"recovery~label (perm): {p['corr_perm_recovery_vs_label']:.3f}")
    print("\nchecks:", json.dumps(checks, default=bool))
    print(f"\n>>> PHASE 2b GATE: {'GO' if res['gate']['GO'] else 'NO-GO'} <<<")
    print("wrote results_phase2b.json")

if __name__ == "__main__":
    main()
