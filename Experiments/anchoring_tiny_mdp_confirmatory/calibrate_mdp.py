"""Calibration (env/mechanism only; thresholds Delta_min=0.15, eps_TV=0.05 are LOCKED).
Goal: keep behavior interior (avoid saturation), verify direction structure + z separation."""
import numpy as np
import model_mdp as M

CFG = dict(
    N=400, p_hi=0.8, p_lo=0.2,
    temp_form=0.20, temp_fut=0.40,
    beta_Q=0.15, beta_q=0.10, beta_fut=0.20,
    alpha_z=0.05, lambda_z=0.01, alpha_pe=0.05, lambda_pe=0.01, alpha_m=0.05,
    form_episodes=400, kappa_m=0.10, budget=2, fut_episodes=60, fut_measure_last=20,
)
CAL = [1, 2, 3, 4, 5]

def roles(seed):
    h = seed % 3; other = (seed + 1) % 3; novel = (seed + 2) % 3
    return h, other, novel

def battery(m, h, other, novel, seed):
    return {
        "aligned":  M.future_task(m, target=h,     blocked=-1, seed=seed, c=CFG),
        "blocked":  M.future_task(m, target=other, blocked=h,  seed=seed, c=CFG),
        "novel":    M.future_task(m, target=novel, blocked=-1, seed=seed, c=CFG),
    }

for s in CAL:
    h, other, novel = roles(s)
    act = M.formation("coupled", h, s, CFG)
    yok = M.formation("yoked", h, s, CFG, master_R=act["R"], act_offset=777)
    sham = M.formation("sham", h, s, CFG)
    ba = battery(act["m"], h, other, novel, s)
    by = battery(yok["m"], h, other, novel, s)
    tvs = {k: M.tv(ba[k], by[k]) for k in ba}
    macro = np.mean(list(tvs.values()))
    print(f"\nseed {s} (h={h},other={other},novel={novel})  z_a={act['z'].mean():.2f} z_y={yok['z'].mean():.2f} "
          f"| ctrl_corr a={act['ctrl_corr']:.2f} y={yok['ctrl_corr']:.2f} | sham self={sham['self_attr']:.3f} ext={sham['ext_attr']:.3f}")
    print(f"  aligned  active={np.round(ba['aligned'],2)} yoked={np.round(by['aligned'],2)} TV={tvs['aligned']:.3f}  "
          f"[adv: a.P(Gh)={ba['aligned'][h]:.2f} vs y={by['aligned'][h]:.2f}]")
    print(f"  blocked  active={np.round(ba['blocked'],2)} yoked={np.round(by['blocked'],2)} TV={tvs['blocked']:.3f}  "
          f"[stick: a.P(EMPTY)={ba['blocked'][3]:.2f} vs y={by['blocked'][3]:.2f}]")
    print(f"  novel    active={np.round(ba['novel'],2)} yoked={np.round(by['novel'],2)} TV={tvs['novel']:.3f}  "
          f"[stick: a.P(Gnovel)={ba['novel'][novel]:.2f} vs y={by['novel'][novel]:.2f}]")
    print(f"  macro-TV={macro:.3f}")
