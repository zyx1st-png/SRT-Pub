"""
tiny-MDP CONFIRMATORY locked holdout. Frozen params (config_mdp_frozen.json), 50 fresh
seeds 40000-40049, 10000 paired bootstrap. Thresholds Delta_min=0.15, eps_TV=0.05 LOCKED.

Primary GO: 95% paired bootstrap CI lower bound of macro-TV (equal-weight over aligned /
blocked / novel) DIRECTLY EXCEEDS Delta_min=0.15. Mandatory direction gate: aligned ->
active advantage; blocked/novel -> active stickiness. Null controls (memory-null,
same-m/different-z) 95% CI fully within +-eps_TV; memory-swap follows the memory donor.
Sham is a mechanism gate only (self ~ 0, ext > 0), not GO-deciding.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).parent))
import model_mdp as M

HERE = Path(__file__).parent
CFG = json.load(open(HERE / "config_mdp_frozen.json"))
c = CFG["model"]; TH = CFG["locked_thresholds"]; OFF = CFG["yoked_act_offset"]
SEEDS = list(range(CFG["holdout_seeds_start"], CFG["holdout_seeds_start"] + CFG["holdout_seeds_n"]))
UNIFORM_M = None  # set per-N below

def roles(seed):
    return seed % 3, (seed + 1) % 3, (seed + 2) % 3

def battery(m, h, other, novel, seed):
    return {"aligned": M.future_task(m, h, -1, seed, c),
            "blocked": M.future_task(m, other, h, seed, c),
            "novel":   M.future_task(m, novel, -1, seed, c)}

def macro_tv(bx, by):
    return float(np.mean([M.tv(bx[k], by[k]) for k in bx]))

def boot_ci(x, level, B, seed=999):
    x = np.asarray(x, float); rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(x), size=(B, len(x)))
    means = x[idx].mean(axis=1)
    lo = float(np.percentile(means, 100 * (1 - level) / 2))
    hi = float(np.percentile(means, 100 * (1 + level) / 2))
    return float(x.mean()), lo, hi

def main():
    uni = np.full((c["N"], 3), 1.0 / 3)
    macro, macro_null, macro_swap = [], [], []
    dir_aligned, dir_blocked, dir_novel = [], [], []
    sham_self, sham_ext, cc_yoked = [], [], []
    same_m_diff_z = []

    for s in SEEDS:
        h, other, novel = roles(s)
        act = M.formation("coupled", h, s, c)
        yok = M.formation("yoked", h, s, c, master_R=act["R"], act_offset=OFF)
        sham = M.formation("sham", h, s, c)
        ba = battery(act["m"], h, other, novel, s)
        by = battery(yok["m"], h, other, novel, s)
        macro.append(macro_tv(ba, by))
        # direction gates
        dir_aligned.append(float(ba["aligned"][h] - by["aligned"][h]))         # active adv (>0)
        dir_blocked.append(float(ba["blocked"][M.EMPTY] - by["blocked"][M.EMPTY]))  # active stickiness (>0)
        dir_novel.append(float(ba["novel"][novel] - by["novel"][novel]))       # active stickiness (<0)
        # memory-null: active memory ablated to uniform -> should collapse toward yoked
        bnull = battery(uni, h, other, novel, s)
        macro_null.append(macro_tv(bnull, by))
        # memory-swap: active carries yoked's memory -> should follow the donor (yoked)
        bswap = battery(yok["m"], h, other, novel, s)
        macro_swap.append(macro_tv(bswap, by))
        # same-m/different-z: future reads ONLY m, so identical m -> identical future (z ignored)
        same_m_diff_z.append(macro_tv(battery(act["m"], h, other, novel, s), ba))
        sham_self.append(sham["self_attr"]); sham_ext.append(sham["ext_attr"]); cc_yoked.append(yok["ctrl_corr"])

    L, B = TH["ci_level"], TH["bootstrap_resamples"]
    m_macro, lo_macro, hi_macro = boot_ci(macro, L, B)
    m_null, lo_null, hi_null = boot_ci(macro_null, L, B)
    m_swap, lo_swap, hi_swap = boot_ci(macro_swap, L, B)
    m_al, lo_al, hi_al = boot_ci(dir_aligned, L, B)
    m_bl, lo_bl, hi_bl = boot_ci(dir_blocked, L, B)
    m_nv, lo_nv, hi_nv = boot_ci(dir_novel, L, B)
    m_smz, lo_smz, hi_smz = boot_ci(same_m_diff_z, L, B)

    checks = {
        "P1_macro_TV_lower_gt_Delta": lo_macro > TH["Delta_min"],
        "DIR_aligned_advantage": lo_al > 0,
        "DIR_blocked_stickiness": lo_bl > 0,
        "DIR_novel_stickiness": hi_nv < 0,
        "NULL_memory_null_within_eps": hi_null < TH["eps_TV"] and lo_null > -TH["eps_TV"],
        "NULL_same_m_diff_z_within_eps": hi_smz < TH["eps_TV"] and lo_smz > -TH["eps_TV"],
        "SWAP_follows_donor_within_eps": hi_swap < TH["eps_TV"] and lo_swap > -TH["eps_TV"],
    }
    checks = {k: bool(v) for k, v in checks.items()}
    # sham mechanism gate (reported, not GO-deciding)
    sham_ok = bool(abs(np.mean(sham_self)) < 0.05 and np.mean(sham_ext) > 0.05)
    GO = bool(all(checks.values()))
    failures = [k for k, v in checks.items() if not v]

    res = {
        "seeds": SEEDS, "locked_thresholds": TH,
        "primary_macro_TV": {"mean": m_macro, "ci": [lo_macro, hi_macro], "Delta_min": TH["Delta_min"]},
        "direction": {"aligned_active_adv": [m_al, lo_al, hi_al],
                      "blocked_active_stickiness": [m_bl, lo_bl, hi_bl],
                      "novel_active_stickiness": [m_nv, lo_nv, hi_nv]},
        "memory_null_macroTV": [m_null, lo_null, hi_null],
        "memory_swap_macroTV": [m_swap, lo_swap, hi_swap],
        "same_m_diff_z_macroTV": [m_smz, lo_smz, hi_smz],
        "sham": {"self_attr": float(np.mean(sham_self)), "ext_attr": float(np.mean(sham_ext)), "ok": sham_ok},
        "yoked_ctrl_corr": float(np.mean(cc_yoked)),
        "checks": checks, "failures": failures, "GO": GO,
    }
    (HERE / "results_mdp_holdout.json").write_text(json.dumps(res, indent=2))

    print("\n================ tiny-MDP CONFIRMATORY LOCKED HOLDOUT (50 seeds, 10k bootstrap) ================")
    print(f"[P1 primary] macro-TV mean={m_macro:.3f}  95%CI=[{lo_macro:.3f},{hi_macro:.3f}]  (need lower > {TH['Delta_min']})")
    print(f"[DIR aligned] active adv P(Gh) diff mean={m_al:+.3f} CI=[{lo_al:+.3f},{hi_al:+.3f}] (need lower>0)")
    print(f"[DIR blocked] active stickiness P(EMPTY) diff mean={m_bl:+.3f} CI=[{lo_bl:+.3f},{hi_bl:+.3f}] (need lower>0)")
    print(f"[DIR novel]   active stickiness P(Gnovel) diff mean={m_nv:+.3f} CI=[{lo_nv:+.3f},{hi_nv:+.3f}] (need upper<0)")
    print(f"[NULL memory-null] macro-TV mean={m_null:.3f} CI=[{lo_null:.3f},{hi_null:.3f}] (need within +-{TH['eps_TV']})")
    print(f"[NULL same-m/diff-z] macro-TV mean={m_smz:.3f} CI=[{lo_smz:.3f},{hi_smz:.3f}] (need within +-{TH['eps_TV']})")
    print(f"[SWAP memory-swap] follows donor macro-TV mean={m_swap:.3f} CI=[{lo_swap:.3f},{hi_swap:.3f}] (need within +-{TH['eps_TV']})")
    print(f"[sham mechanism] self={np.mean(sham_self):+.3f} ext={np.mean(sham_ext):+.3f} ok={sham_ok}  | yoked ctrl-corr={np.mean(cc_yoked):+.3f}")
    print("\nchecks:", json.dumps(checks))
    print("failures:", failures if failures else "NONE")
    print(f"\n>>> tiny-MDP CONFIRMATORY GATE: {'GO' if GO else 'NO-GO'} <<<")
    print("wrote results_mdp_holdout.json")

if __name__ == "__main__":
    main()
