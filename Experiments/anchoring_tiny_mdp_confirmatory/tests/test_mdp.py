"""Sanity/identification tests for the tiny-MDP confirmatory. Run: python3 tests/test_mdp.py"""
import sys, json
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import model_mdp as M

CFG = json.load(open(Path(__file__).resolve().parents[1] / "config_mdp_frozen.json"))
c = CFG["model"]
FAILS = []
def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
    if not ok: FAILS.append(name)

# 1. future reads ONLY m: same m + same seed -> identical terminal distribution.
m = np.tile([0.1, 0.8, 0.1], (c["N"], 1))
d1 = M.future_task(m, 1, -1, 42, c); d2 = M.future_task(m, 1, -1, 42, c)
check("future is a deterministic function of m (only-m carry)", np.allclose(d1, d2))

# 2. terminal distribution is a valid 4-vector (3 goals + EMPTY), sums to 1.
check("terminal dist valid (sums to 1, len 4)", abs(d1.sum() - 1.0) < 1e-9 and len(d1) == 4, str(np.round(d1, 3)))

# 3. yoked genuinely decouples: ctrl_corr ~ 0.
act = M.formation("coupled", 1, 7, c)
yok = M.formation("yoked", 1, 7, c, master_R=act["R"], act_offset=777)
check("yoked ctrl-corr ~ 0", abs(yok["ctrl_corr"]) < 0.05, f"yoked={yok['ctrl_corr']:.4f} active={act['ctrl_corr']:.4f}")

# 4. sham: self-attribution ~ 0, external-attribution > 0 (mechanism gate).
sham = M.formation("sham", 1, 7, c)
check("sham self~0 and ext>0", abs(sham["self_attr"]) < 0.05 and sham["ext_attr"] > 0.05,
      f"self={sham['self_attr']:.3f} ext={sham['ext_attr']:.3f}")

# 5. active memory peaks on history corridor; yoked memory stays diffuse.
check("active m peaks on h, yoked diffuse",
      act["m"].mean(0)[1] > 0.5 and yok["m"].mean(0).max() < 0.2,
      f"active_m={np.round(act['m'].mean(0),2)} yoked_m={np.round(yok['m'].mean(0),2)}")

# 6. TV bounds.
check("TV(identical)=0, TV in [0,1]", M.tv([0.5,0.5,0,0],[0.5,0.5,0,0]) == 0
      and 0 <= M.tv([1,0,0,0],[0,1,0,0]) <= 1)

# 7. reproducibility of formation.
z1 = M.formation("coupled", 0, 3, c)["z"].mean(); z2 = M.formation("coupled", 0, 3, c)["z"].mean()
check("formation deterministic under fixed seed", z1 == z2, f"{z1:.6f}")

# 8. holdout seeds fresh.
used = set(CFG["calibration_seeds"]) | {101} | set(range(1000,1005)) | set(range(20000,20040)) | set(range(30000,30040))
hold = set(range(CFG["holdout_seeds_start"], CFG["holdout_seeds_start"]+CFG["holdout_seeds_n"]))
check("holdout seeds fresh", len(hold & used) == 0)

print("\n" + ("ALL TESTS PASSED" if not FAILS else f"FAILED: {FAILS}"))
sys.exit(1 if FAILS else 0)
