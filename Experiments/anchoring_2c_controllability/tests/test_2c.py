"""Sanity/identification tests for Phase 2c. Run: python3 tests/test_2c.py"""
import sys, json, math
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import model2c as M

CFG = json.load(open(Path(__file__).resolve().parents[1] / "config2c_frozen.json"))
c = CFG["model"]
FAILS = []
def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
    if not ok: FAILS.append(name)

# 1. mu-reference score is 0 when the outcome model is flat (q[0]==q[1]==qbar).
#    r = log q(o|a) - log qbar; with q[a]=qbar for all a, r=0 for any outcome.
q = 0.5; qbar = 0.5
r1 = M._bern_ll(1.0, q) - M._bern_ll(1.0, qbar)
r0 = M._bern_ll(0.0, q) - M._bern_ll(0.0, qbar)
check("mu-LLR score = 0 under flat outcome model", abs(r1) < 1e-12 and abs(r0) < 1e-12)

# 2. yoked genuinely decouples: ctrl-corr(chose-good, reward) ~ 0 (manipulation check).
act = M.formation("coupled", "high", "ctrl", 7, c)
yok = M.formation("decoupled", "high", "ctrl", 7, c, master_R=act["R"], action_rng_offset=777)
check("yoked ctrl-corr ~ 0 (A->O broken)", abs(yok["ctrl_corr"]) < 0.05,
      f"yoked={yok['ctrl_corr']:.4f} active={act['ctrl_corr']:.4f}")

# 3. commitment is CONTENT-NEUTRAL: mirrored memories give equal commitment.
m1 = np.tile([0.9, 0.1], (50, 1)); m2 = np.tile([0.1, 0.9], (50, 1))
ci1 = M.future_commitment(m1, c).mean(); ci2 = M.future_commitment(m2, c).mean()
check("commitment content-neutral (mirror-invariant)", abs(ci1 - ci2) < 1e-9, f"{ci1:.4f} vs {ci2:.4f}")

# 4. controllability-z is selection-specific: active z >> yoked z.
check("z_ctrl active > yoked", act["z"].mean() > yok["z"].mean() + 0.1,
      f"active={act['z'].mean():.3f} yoked={yok['z'].mean():.3f}")

# 5. |PE| baseline is NOT selection-specific: active z^PE ~ yoked z^PE.
check("z^PE active ~ yoked (not selection-specific)", abs(act["zpe"].mean() - yok["zpe"].mean()) < 0.3,
      f"active={act['zpe'].mean():.3f} yoked={yok['zpe'].mean():.3f}")

# 6. reproducibility.
z_a = M.formation("coupled", "low", "ctrl", 3, c)["z"].mean()
z_b = M.formation("coupled", "low", "ctrl", 3, c)["z"].mean()
check("deterministic under fixed seed", z_a == z_b, f"{z_a:.6f}")

# 7. holdout seeds fresh (disjoint from calibration + earlier phases).
used = set(CFG["calibration_seeds"]) | {101} | set(range(1000,1005)) | set(range(20000,20040))
hold = set(range(CFG["holdout_seeds_start"], CFG["holdout_seeds_start"]+CFG["holdout_seeds_n"]))
check("holdout seeds fresh", len(hold & used) == 0)

print("\n" + ("ALL TESTS PASSED" if not FAILS else f"FAILED: {FAILS}"))
sys.exit(1 if FAILS else 0)
