"""Matched-present -> different-future test.

Two ensembles forced to the SAME present fast state x0 (gap = 0, exact), differing
only in slow history z (hence landscape). Identical adverse probe + identical noise
(paired). Reports RAW future probabilities and KL/JS/TV between the two future
outcome distributions over the macrostate partition {M-, M+}.

The anchored landscape is taken from the C_anchor selection history (naturally
formed z), NOT hand-set. The naive landscape carries no history (home only).
"""
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
import model as M

HERE = Path(__file__).parent

def bern_divs(p_anchor, p_naive):
    def clip(x): return min(max(x, 1e-9), 1 - 1e-9)
    p, q = clip(p_anchor), clip(p_naive)
    kl = p*math.log(p/q) + (1-p)*math.log((1-p)/(1-q))
    m1, m0 = 0.5*(p+q), 0.5*((1-p)+(1-q))
    js = 0.5*(p*math.log(p/m1)+(1-p)*math.log((1-p)/m0)) + 0.5*(q*math.log(q/m1)+(1-q)*math.log((1-q)/m0))
    tv = 0.5*(abs(p-q)+abs((1-p)-(1-q)))
    return {"KL": kl, "JS": js, "TV": tv}

def run(P, x0=1.0, n=8000, delta=40.0, probe_u=-0.9, probe_T=6.0, seed=99):
    rng = np.random.default_rng(seed)
    dt, D0 = P["dt"], P["D0"]
    # anchored landscape from a real C_anchor history (z formed naturally):
    zC = M.simulate(P, P["conditions"]["C_anchor"], +1, 7)["z_after_int"]
    cC = P["conditions"]["C_anchor"]["c0"] + P["kappa"] * zC
    c_naive = P["conditions"]["C_anchor"]["c0"]   # home, no history written

    xa = np.full(n, x0); xn = np.full(n, x0)      # identical present state (exact)
    n_probe, n_free = int(round(probe_T/dt)), int(round(delta/dt))
    for k in range(n_probe + n_free):
        xi = rng.standard_normal(n)               # shared draws -> divergence is landscape-only
        u = probe_u if k < n_probe else 0.0
        xa = xa - dt*M.drift(xa, cC) + dt*u + math.sqrt(2*D0*dt)*xi
        xn = xn - dt*M.drift(xn, c_naive) + dt*u + math.sqrt(2*D0*dt)*xi
    pa, pn = float((xa > 0).mean()), float((xn > 0).mean())
    reach = lambda x: sorted({s for s, ok in [("M+", (x>0).mean()>0.05), ("M-", (x<0).mean()>0.05)] if ok})
    return {"present_state_gap": 0.0, "x0": x0, "zC": float(zC), "cC": float(cC), "c_naive": float(c_naive),
            "raw_future_Pplus": {"anchor": pa, "naive": pn},
            "raw_future_Pminus": {"anchor": 1-pa, "naive": 1-pn},
            "reachable": {"anchor": reach(xa), "naive": reach(xn)},
            "divergences": bern_divs(pa, pn)}

def main():
    P = json.load(open(HERE/"config.json"))
    r = run(P)
    (HERE/"results_matched_future.json").write_text(json.dumps(r, indent=2))
    print("\n============ MATCHED-PRESENT -> DIFFERENT-FUTURE (present gap = %.4f) ============" % r["present_state_gap"])
    print(f"raw future P(M+):  anchor={r['raw_future_Pplus']['anchor']:.3f}   naive={r['raw_future_Pplus']['naive']:.3f}")
    print(f"raw future P(M-):  anchor={r['raw_future_Pminus']['anchor']:.3f}   naive={r['raw_future_Pminus']['naive']:.3f}")
    print(f"reachable set:     anchor={r['reachable']['anchor']}   naive={r['reachable']['naive']}")
    d = r["divergences"]
    print(f"future divergence: KL={d['KL']:.3f}  JS={d['JS']:.3f}  TV={d['TV']:.3f}")
    print("wrote results_matched_future.json")

if __name__ == "__main__":
    main()
