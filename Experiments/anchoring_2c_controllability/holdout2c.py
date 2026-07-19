"""
Phase 2c LOCKED HOLDOUT. Frozen params (config2c_frozen.json), 40 fresh seeds.
Primary GO metric (correction 5): paired active-yoked future COMMITMENT under
controllability-z exceeds pre-registered Delta_min AND the paired CI lower bound > 0.
NO Cohen's d / relative-margin OR conditions. Mediation is auxiliary; the primary
causal evidence is consolidation-null (null-z) and memory-swap (swap-m). All "no
effect" claims use pre-registered equivalence bounds.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).parent))
import model2c as M

HERE = Path(__file__).parent
CFG = json.load(open(HERE / "config2c_frozen.json"))
c = CFG["model"]
PRE = CFG["preregistered"]
OFF = CFG["yoked_action_rng_offset"]
SEEDS = list(range(CFG["holdout_seeds_start"], CFG["holdout_seeds_start"] + CFG["holdout_seeds_n"]))

def pair(seed, vol, z_mode, null_z=False):
    act = M.formation("coupled", vol, z_mode, seed, c, null_z=null_z)
    yok = M.formation("decoupled", vol, z_mode, seed, c, master_R=act["R"],
                      action_rng_offset=OFF, null_z=null_z)
    return act, yok

def commit(d): return M.future_commitment(d["m"], c).mean()

def boot_ci(x, level, B):
    x = np.asarray(x); rng = np.random.default_rng(12345)
    means = np.array([rng.choice(x, len(x), replace=True).mean() for _ in range(B)])
    lo = np.percentile(means, 100 * (1 - level) / 2)
    hi = np.percentile(means, 100 * (1 - (1 - level) / 2))
    return float(x.mean()), float(lo), float(hi)

def main():
    rows = {"high": [], "low": []}
    zsep = {"high": {"ctrl": [], "pe": []}, "low": {"ctrl": [], "pe": []}}
    ccorr_yoked, ccorr_active = [], []
    causal = {"null_active": [], "yoked": [], "swap_active_to_yoked": []}
    Cmu = {"active": [], "yoked": []}

    for s in SEEDS:
        for vol in ("high", "low"):
            a_c, y_c = pair(s, vol, "ctrl")
            a_p, y_p = pair(s, vol, "pe")
            d_ctrl = commit(a_c) - commit(y_c)
            d_pe = commit(a_p) - commit(y_p)
            rows[vol].append({"d_ctrl": float(d_ctrl), "d_pe": float(d_pe),
                              "commit_a_ctrl": float(commit(a_c)), "commit_y_ctrl": float(commit(y_c))})
            zsep[vol]["ctrl"].append(float(a_c["z"].mean() - y_c["z"].mean()))
            zsep[vol]["pe"].append(float(a_p["zpe"].mean() - y_p["zpe"].mean()))
            ccorr_yoked.append(float(y_c["ctrl_corr"])); ccorr_active.append(float(a_c["ctrl_corr"]))
            Cmu["active"].append(float(a_c["Cmu"].mean())); Cmu["yoked"].append(float(y_c["Cmu"].mean()))
            # causal battery on ctrl (high & low pooled)
            a_null, _ = pair(s, vol, "ctrl", null_z=True)
            causal["null_active"].append(float(M.future_commitment(a_null["m"], c).mean()))
            causal["yoked"].append(float(commit(y_c)))
            causal["swap_active_to_yoked"].append(
                float(M.future_commitment(a_c["m"], c, swap_m=y_c["m"]).mean()))

    pooled_ctrl = [r["d_ctrl"] for v in rows for r in rows[v]]
    pooled_pe = [r["d_pe"] for v in rows for r in rows[v]]
    m_ctrl, lo_ctrl, hi_ctrl = boot_ci(pooled_ctrl, PRE["ci_level"], PRE["bootstrap_resamples"])
    m_pe, lo_pe, hi_pe = boot_ci(pooled_pe, PRE["ci_level"], PRE["bootstrap_resamples"])

    # causal contrasts:
    #   null-z should COLLAPSE the active commitment to the no-write floor (necessity of z).
    #   swap-m should make active-with-yoked-m match yoked (memory carries the reachable set).
    active_normal_commit = float(np.mean([r["commit_a_ctrl"] for v in rows for r in rows[v]]))
    null_active_commit = float(np.mean(causal["null_active"]))
    null_drop = active_normal_commit - null_active_commit
    swap_gap = np.mean(causal["swap_active_to_yoked"]) - np.mean(causal["yoked"])

    checks = {
        # P2 primary GO
        "P2_ctrl_gt_Deltamin": m_ctrl > PRE["Delta_min"] and lo_ctrl > 0,
        # N1 negative baseline: |PE| effect within equivalence bound
        "N1_pe_within_equiv": (lo_pe >= -PRE["eps_equiv_commit"]) and (hi_pe <= PRE["eps_equiv_commit"]),
        # P1 z-formation coupling effect: ctrl selection-specific, sign-stable
        "P1_zctrl_sign_stable": float(np.mean([d > 0 for v in zsep for d in zsep[v]["ctrl"]])) >= 0.95,
        # manipulation check: yoked I(A;O) proxy ~ 0
        "manip_yoked_ctrlcorr_equiv": abs(np.mean(ccorr_yoked)) < PRE["eps_equiv_ctrlcorr"],
        # causal: null-z collapses active commitment to the no-write floor (z necessary)
        "causal_null_collapses": (null_drop > PRE["Delta_min"]) and (null_active_commit < PRE["Delta_min"]),
        # causal: swap-m follows m (active-with-yoked-m ~ yoked)
        "causal_swap_follows_m": abs(swap_gap) < PRE["eps_equiv_commit"],
    }
    checks = {k: bool(v) for k, v in checks.items()}
    GO = bool(all(checks.values()))

    res = {
        "seeds": SEEDS,
        "primary_ctrl": {"mean": m_ctrl, "ci_lo": lo_ctrl, "ci_hi": hi_ctrl, "Delta_min": PRE["Delta_min"]},
        "negative_pe": {"mean": m_pe, "ci_lo": lo_pe, "ci_hi": hi_pe, "eps": PRE["eps_equiv_commit"]},
        "per_vol": {v: {"d_ctrl": float(np.mean([r["d_ctrl"] for r in rows[v]])),
                        "d_pe": float(np.mean([r["d_pe"] for r in rows[v]]))} for v in rows},
        "z_formation": {v: {"ctrl_active_minus_yoked": float(np.mean(zsep[v]["ctrl"])),
                            "pe_active_minus_yoked": float(np.mean(zsep[v]["pe"]))} for v in zsep},
        "manip": {"ctrl_corr_yoked": float(np.mean(ccorr_yoked)),
                  "ctrl_corr_active": float(np.mean(ccorr_active))},
        "Cmu": {"active": float(np.mean(Cmu["active"])), "yoked": float(np.mean(Cmu["yoked"]))},
        "causal": {"active_normal_commit": active_normal_commit,
                   "null_active_commit": null_active_commit,
                   "yoked_commit": float(np.mean(causal["yoked"])),
                   "swap_active_to_yoked_commit": float(np.mean(causal["swap_active_to_yoked"])),
                   "null_drop": float(null_drop), "swap_gap": float(swap_gap)},
        "checks": checks, "GO": GO,
    }
    (HERE / "results_2c_holdout.json").write_text(json.dumps(res, indent=2))

    print("\n================ PHASE 2c LOCKED HOLDOUT (frozen, 40 fresh seeds) ================")
    print(f"[P2 primary] paired active-yoked commitment (ctrl): mean={m_ctrl:.3f} "
          f"90%CI=[{lo_ctrl:.3f},{hi_ctrl:.3f}]  (need >Delta_min={PRE['Delta_min']} & lo>0)")
    print(f"[N1 negbase] paired active-yoked commitment (|PE|): mean={m_pe:.3f} "
          f"90%CI=[{lo_pe:.3f},{hi_pe:.3f}]  (need within +-{PRE['eps_equiv_commit']})")
    for v in ("high", "low"):
        print(f"   vol={v}: d_ctrl={res['per_vol'][v]['d_ctrl']:.3f}  d_pe={res['per_vol'][v]['d_pe']:.3f}  "
              f"| z_form ctrl(a-y)={res['z_formation'][v]['ctrl_active_minus_yoked']:.3f} "
              f"pe(a-y)={res['z_formation'][v]['pe_active_minus_yoked']:.3f}")
    print(f"[manip] yoked ctrl-corr={res['manip']['ctrl_corr_yoked']:+.3f} (active {res['manip']['ctrl_corr_active']:+.3f})")
    print(f"[Cmu structural] active={res['Cmu']['active']:.3f} yoked={res['Cmu']['yoked']:.3f}")
    print(f"[causal] null-z: active commit {active_normal_commit:.3f} -> {null_active_commit:.3f} (drop {null_drop:+.3f}; z necessary)")
    print(f"[causal] swap active->yoked-m commit={res['causal']['swap_active_to_yoked_commit']:.3f} vs yoked={res['causal']['yoked_commit']:.3f} (gap {swap_gap:+.3f})")
    print("\nchecks:", json.dumps(checks, default=bool))
    print(f"\n>>> PHASE 2c GATE: {'GO' if GO else 'NO-GO'} <<<")
    print("wrote results_2c_holdout.json")

if __name__ == "__main__":
    main()
