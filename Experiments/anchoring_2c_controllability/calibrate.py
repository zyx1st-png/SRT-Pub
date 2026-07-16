"""Calibration sanity: does controllability-z dissociate active vs yoked where |PE| does not?
Run on a few CALIBRATION seeds only (not the holdout set)."""
import numpy as np, json
import model2c as M

CFG = dict(
    N=300, temp=0.15,
    phi_low=0.85, plo_low=0.15, phi_high=0.65, plo_high=0.35,   # volatility = outcome noise
    beta_Q=0.15, beta_q=0.10,
    alpha_z=0.05, lambda_z=0.01, alpha_pe=0.05, lambda_pe=0.01,
    form_steps=400,
    alpha_m=0.05, null_z_value=0.0, rho_future=1.5,
)
CAL_SEEDS = [1, 2, 3, 4, 5]

def one(seed, vol, z_mode, null_z=False):
    act = M.formation("coupled", vol, z_mode, seed, CFG, null_z=null_z)
    # yoked: INDEPENDENT action RNG (offset) so its actions are decoupled from the
    # reward-generating actions; reward replayed from the active master.
    yok = M.formation("decoupled", vol, z_mode, seed, CFG, master_R=act["R"],
                      action_rng_offset=777, null_z=null_z)
    fa = M.future_commitment(act["m"], CFG).mean()
    fy = M.future_commitment(yok["m"], CFG).mean()
    return dict(z_a=float(act["z"].mean()), z_y=float(yok["z"].mean()),
                zpe_a=float(act["zpe"].mean()), zpe_y=float(yok["zpe"].mean()),
                Cmu_a=float(act["Cmu"].mean()), Cmu_y=float(yok["Cmu"].mean()),
                fut_a=float(fa), fut_y=float(fy), fut_diff=float(fa - fy),
                cc_y=float(yok["ctrl_corr"]), cc_a=float(act["ctrl_corr"]))

for vol in ["high", "low"]:
    print(f"\n===== volatility={vol} =====")
    for z_mode in ["ctrl", "pe"]:
        rows = [one(s, vol, z_mode) for s in CAL_SEEDS]
        def mean(k): return np.mean([r[k] for r in rows])
        print(f"[{z_mode:4}] z: active={mean('z_a') if z_mode=='ctrl' else mean('zpe_a'):.3f} "
              f"yoked={mean('z_y') if z_mode=='ctrl' else mean('zpe_y'):.3f}  "
              f"| future: active={mean('fut_a'):.3f} yoked={mean('fut_y'):.3f} "
              f"diff={mean('fut_diff'):+.3f}  | Cmu a/y={mean('Cmu_a'):.3f}/{mean('Cmu_y'):.3f}")
    ccs = [one(s, vol, 'ctrl') for s in CAL_SEEDS]
    print(f"       ctrl-corr(chose-good, reward): active={np.mean([r['cc_a'] for r in ccs]):.3f} "
          f"yoked={np.mean([r['cc_y'] for r in ccs]):.3f}  (yoked should be ~0)")

# null-z and swap-m checks (high vol, ctrl)
print("\n===== causal (high vol, ctrl) =====")
s = 1
act = M.formation("coupled", "high", "ctrl", s, CFG)
yok = M.formation("decoupled", "high", "ctrl", s, CFG, master_R=act["R"], action_rng_offset=777)
act_null = M.formation("coupled", "high", "ctrl", s, CFG, null_z=True)
print(f"commit active={M.future_commitment(act['m'],CFG).mean():.3f}  yoked={M.future_commitment(yok['m'],CFG).mean():.3f}")
print(f"null-z active commit={M.future_commitment(act_null['m'],CFG).mean():.3f}  (should drop toward yoked)")
print(f"swap-m: active-with-yoked-m commit={M.future_commitment(act['m'],CFG,swap_m=yok['m']).mean():.3f}  (should follow m)")
