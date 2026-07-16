"""Sanity/identification tests for the bandit feasibility gate. Run: python3 tests/test_bandit.py"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import feasibility as F

c = F.CFG
FAILS = []
def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
    if not ok: FAILS.append(name)

# 1. reset touches Q only: z must be bit-identical before/after a Q reset.
rng = np.random.default_rng(7)
Q, z = F.run_formation("volatile", c, rng)
z_before = z.copy(); Q[:] = 0.5
check("reset changes Q only, z untouched", np.array_equal(z, z_before))

# 2. washout retains the gap by a deterministic factor (1-lambda_z)^wash, same for all.
gap0 = 1.0
factor = (1 - c["lambda_z"]) ** c["wash_steps"]
za = F.washout(np.full(3, 2.0), c, rng); zb = F.washout(np.full(3, 1.0), c, rng)
check("washout retains gap by (1-lam)^wash", abs((za.mean()-zb.mean()) - factor) < 1e-9,
      f"gap={za.mean()-zb.mean():.4f} expect={factor:.4f}")

# 3. two identical-z ensembles produce ~0 future difference (null sanity).
zc_val = 3.0
cc = F.calibrate_gate(c, 2.6, 3.7)
a, _ = F.run_future(np.full(200, zc_val), cc, np.random.default_rng(1), True)
b, _ = F.run_future(np.full(200, zc_val), cc, np.random.default_rng(2), True)
check("identical z -> ~0 future diff", abs(a.mean()-b.mean()) < 0.05, f"diff={a.mean()-b.mean():+.4f}")

# 4. monotonic gate: higher z -> higher effective learning rate.
lo = F.alpha_eff(np.array([2.0]), cc)[0]; hi = F.alpha_eff(np.array([4.0]), cc)[0]
check("alpha_eff monotone increasing in z", hi > lo, f"{lo:.3f} < {hi:.3f}")

# 5. reproducibility: same seed -> identical formed-z mean.
r1 = F.run_formation("volatile", c, np.random.default_rng(11))[1].mean()
r2 = F.run_formation("volatile", c, np.random.default_rng(11))[1].mean()
check("deterministic under fixed seed", r1 == r2, f"{r1:.6f}")

print("\n" + ("ALL TESTS PASSED" if not FAILS else f"FAILED: {FAILS}"))
sys.exit(1 if FAILS else 0)
