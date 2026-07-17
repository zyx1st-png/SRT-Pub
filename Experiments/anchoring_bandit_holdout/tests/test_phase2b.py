"""Sanity tests for the Phase 2b holdout. Run: python3 tests/test_phase2b.py"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import phase2b as P
import feasibility as F

FAILS = []
def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
    if not ok: FAILS.append(name)

# 1. frozen params really are the committed Phase-2 values (no drift).
check("frozen zc/kk match Phase-2", abs(P.FROZEN["zc"]-3.170728965999513) < 1e-12
      and abs(P.FROZEN["kk"]-3.882185474049716) < 1e-12)

# 2. local active formation matches F.run_formation exactly (identical dynamics/RNG).
rng1 = np.random.default_rng(555); z_local, _ = P.formation_record("volatile", P.FROZEN, rng1)
rng2 = np.random.default_rng(555); _, z_F = F.run_formation("volatile", P.FROZEN, rng2)
check("formation_record == F.run_formation (z)", np.allclose(z_local, z_F), f"max|d|={np.max(np.abs(z_local-z_F)):.2e}")

# 3. yoked reward is non-contingent: yoked z must differ from a matched active z
#    (if it were identical, the yoke would be trivial).
rng = np.random.default_rng(9); za, R = P.formation_record("volatile", P.FROZEN, rng)
zy = P.formation_yoked(R, P.FROZEN, np.random.default_rng(9))
check("yoked z differs from active z (decoupled)", abs(za.mean()-zy.mean()) > 1e-3,
      f"active={za.mean():.3f} yoked={zy.mean():.3f}")

# 4. reproducibility of the pipeline for a fixed seed.
a = P.pipeline(20000)["fut_diff"]; b = P.pipeline(20000)["fut_diff"]
check("pipeline deterministic under fixed seed", a == b, f"{a:.6f}")

# 5. holdout seeds are disjoint from Phase-2 calibration seeds {101, 1000..1004}.
used = {101} | set(range(1000, 1005))
check("holdout seeds are fresh", len(set(P.HOLDOUT_SEEDS) & used) == 0)

print("\n" + ("ALL TESTS PASSED" if not FAILS else f"FAILED: {FAILS}"))
sys.exit(1 if FAILS else 0)
