"""Sanity/identification tests for the anchoring toy. Run: python3 tests/test_toy.py"""
import json, math, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import model as M

P = json.load(open(Path(__file__).resolve().parents[1] / "config.json"))
FAILS = []
def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
    if not ok: FAILS.append(name)

# 1. Kernel divergence is zero when post == pre (matched state, no rule change).
xg = np.linspace(-1.5, 1.5, 21); w = np.ones_like(xg)
d0 = M.kernel_divergences(-0.5, 0.06, -0.5, 0.06, xg, w, 0.01)
check("kernel div zero on identical kernels", all(abs(v) < 1e-9 for v in d0.values()), str(d0))

# 2. Closed-form KL matches a Monte-Carlo estimate for a shifted-mean Gaussian pair.
rng = np.random.default_rng(0); dt = 0.01
c_pre, c_post, D = -0.5, 0.3, 0.06
var = 2*D*dt; x = 0.4
mu_pre = x - dt*M.drift(x, c_pre); mu_post = x - dt*M.drift(x, c_post)
kl_cf = M._kl_gauss(mu_post, var, mu_pre, var)
s = rng.normal(mu_post, math.sqrt(var), 400000)
kl_mc = np.mean(-((s-mu_post)**2)/(2*var) + ((s-mu_pre)**2)/(2*var))
check("closed-form KL ~ Monte-Carlo KL", abs(kl_cf - kl_mc) < 0.02, f"cf={kl_cf:.4f} mc={kl_mc:.4f}")

# 3. W_global is invariant to reference measure here (additive drift/D shifts).
from run_dissociation import ref_measures
cond = P["conditions"]["C_anchor"]
c_pre, D_pre = cond["c0"], P["D0"]
c_post, D_post = cond["c0"] + P["kappa"]*1.5, P["D0"]
vals = [M.kernel_divergences(c_pre, D_pre, c_post, D_post, xg2, w2, P["dt"])["KL"]
        for xg2, w2 in ref_measures(P, c_pre).values()]
check("W_global ~ invariant across ref measures", max(vals)-min(vals) < 1e-6, str([round(v,4) for v in vals]))

# 4. h+/h- symmetry: for a NO-write condition (eta=0), W_sel occupancy == 0.
from run_dissociation import landscape, phi_functionals
a = P["conditions"]["A_transient"]
rp = M.simulate(P, a, +1, 3); rm = M.simulate(P, a, -1, 5003)
wsel = phi_functionals(*landscape(P, a, rp["z_after_int"]))["occupancy"] \
     - phi_functionals(*landscape(P, a, rm["z_after_int"]))["occupancy"]
check("W_sel == 0 for eta=0 condition", abs(wsel) < 1e-6, f"Wsel={wsel:.6f}")

# 5. occupancy monotone in c (more positive tilt -> more M+ occupancy).
occs = [M.occupancy_Mplus(c, 0.06) for c in (-0.4, -0.1, 0.0, 0.1, 0.4)]
check("occupancy monotone increasing in c", all(occs[i] <= occs[i+1]+1e-9 for i in range(len(occs)-1)), str([round(o,3) for o in occs]))

# 6. reproducibility: same seed -> identical P_survival.
r1 = M.simulate(P, P["conditions"]["C_anchor"], +1, 11)["P_survival"]
r2 = M.simulate(P, P["conditions"]["C_anchor"], +1, 11)["P_survival"]
check("deterministic under fixed seed", r1 == r2, f"{r1} == {r2}")

print("\n" + ("ALL TESTS PASSED" if not FAILS else f"FAILED: {FAILS}"))
sys.exit(1 if FAILS else 0)
