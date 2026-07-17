"""Dissociation table: P, W_global (3 ref measures x KL/JS/TV), W_sel (h+ vs h-),
J_ext, J_write. Selection-specific write-back W_sel uses z_after_int (what the
selection EPISODE wrote), compared between h+ and its matched counterfactual h-."""
from __future__ import annotations
import hashlib, json, sys
from pathlib import Path
import numpy as np
import model as M

HERE = Path(__file__).parent

def landscape(P, cond, z_val):
    """Effective (c, D) for a condition given a slow-variable value."""
    if cond["channel"] == "roughen":
        return cond["c0"], P["D0"] * (1.0 + P["rho"] * abs(z_val))
    return cond["c0"] + P["kappa"] * z_val, P["D0"]

def ref_measures(P, c_pre):
    """Three reference measures over x for W_global: uniform, pre-occupancy, mixture."""
    xg = np.linspace(-1.6, 1.6, 41)
    uni = np.ones_like(xg)
    pre = M._stationary_pi(c_pre, P["D0"])
    prew = np.interp(xg, M._XG, pre)
    mix = 0.5 * uni / uni.sum() + 0.5 * prew / prew.sum()
    return {"uniform": (xg, uni), "pre_occupancy": (xg, prew), "mixture": (xg, mix)}

def phi_functionals(c, D):
    return {
        "occupancy": M.occupancy_Mplus(c, D),
        "escape_barrier": M.escape_barrier_Mplus(c, D),
        "committor0": M.committor_origin(c, D),
    }

def run(P):
    out = {}
    for name, cond in P["conditions"].items():
        seed_rows = []
        for s in P["seeds"]:
            rp = M.simulate(P, cond, +1, s)          # h+  (push toward M+)
            rm = M.simulate(P, cond, -1, s + 5000)   # h-  (matched counterfactual)
            # W_sel from what the EPISODE wrote (z_after_int), h+ vs h-
            c_hp, D_hp = landscape(P, cond, rp["z_after_int"])
            c_hm, D_hm = landscape(P, cond, rm["z_after_int"])
            phi_hp, phi_hm = phi_functionals(c_hp, D_hp), phi_functionals(c_hm, D_hm)
            wsel = {k: phi_hp[k] - phi_hm[k] for k in phi_hp}
            # local (M+-basin) selection-projected JS/TV between h+ and h- kernels
            xb = np.linspace(0.2, 1.4, 25); wb = np.ones_like(xb)
            loc = M.kernel_divergences(c_hm, D_hm, c_hp, D_hp, xb, wb, P["dt"])
            # W_global: h+ realized landscape vs the condition's OWN pre landscape
            c_pre, D_pre = landscape(P, cond, 0.0)
            wg = {}
            for rm_name, (xg, w) in ref_measures(P, c_pre).items():
                wg[rm_name] = M.kernel_divergences(c_pre, D_pre, c_hp, D_hp, xg, w, P["dt"])
            seed_rows.append({
                "P_survival": rp["P_survival"], "P_escape_time": rp["P_escape_time"],
                "P_after_withdraw": rp["P_after_withdraw"], "S_occ_tau": rp["S_occ_tau"],
                "J_ext": rp["J_ext"], "J_write": rp["J_write"],
                "z_after_int_hp": rp["z_after_int"], "z_after_int_hm": rm["z_after_int"],
                "z_final": rp["z_final"],
                "Wsel": wsel, "Wsel_local": loc, "Wglobal": wg,
                "phi_hp": phi_hp, "phi_hm": phi_hm,
            })
        out[name] = aggregate(seed_rows)
    return out

def aggregate(rows):
    def mean(path):
        vals = [dget(r, path) for r in rows]
        return float(np.mean(vals))
    def std(path):
        return float(np.std([dget(r, path) for r in rows]))
    agg = {
        "P_survival": mean(["P_survival"]), "P_survival_sd": std(["P_survival"]),
        "P_escape_time": mean(["P_escape_time"]), "P_after_withdraw": mean(["P_after_withdraw"]),
        "S_occ_tau": mean(["S_occ_tau"]),
        "J_ext": mean(["J_ext"]), "J_write": mean(["J_write"]),
        "z_after_int_hp": mean(["z_after_int_hp"]), "z_after_int_hm": mean(["z_after_int_hm"]),
        "Wsel": {k: mean(["Wsel", k]) for k in rows[0]["Wsel"]},
        "Wsel_sd": {k: std(["Wsel", k]) for k in rows[0]["Wsel"]},
        "Wsel_local": {k: mean(["Wsel_local", k]) for k in rows[0]["Wsel_local"]},
        "Wglobal": {rm: {d: mean(["Wglobal", rm, d]) for d in rows[0]["Wglobal"][rm]}
                    for rm in rows[0]["Wglobal"]},
        "phi_hp": {k: mean(["phi_hp", k]) for k in rows[0]["phi_hp"]},
        "phi_hm": {k: mean(["phi_hm", k]) for k in rows[0]["phi_hm"]},
    }
    return agg

def dget(d, path):
    for p in path:
        d = d[p]
    return d

def main():
    P = json.loads((HERE / "config.json").read_text())
    res = run(P)
    cfg_hash = hashlib.sha256((HERE / "config.json").read_bytes()).hexdigest()[:16]
    (HERE / "results_dissociation.json").write_text(
        json.dumps({"config_sha256": cfg_hash, "results": res}, indent=2))

    print("\n===================== DISSOCIATION (P vs W_sel vs W_global) =====================")
    hdr = (f"{'condition':<18}{'S@tau':>6}{'P_surv':>7}{'P_afwd':>7}"
           f"{'Wsel_occ':>9}{'Wg_KL(uni)':>11}{'J_ext':>7}{'J_wr':>7}  cell")
    print(hdr); print("-" * len(hdr))
    for name, r in res.items():
        print(f"{name:<18}{r['S_occ_tau']:>6.2f}{r['P_survival']:>7.3f}{r['P_after_withdraw']:>7.3f}"
              f"{r['Wsel']['occupancy']:>9.3f}{r['Wglobal']['uniform']['KL']:>11.3f}"
              f"{r['J_ext']:>7.1f}{r['J_write']:>7.2f}  {P['cells'][name]}")

    print("\n--- W_sel detail (occupancy / escape_barrier / committor0), h+ minus h- ---")
    for name, r in res.items():
        w = r["Wsel"]
        print(f"{name:<18} occ={w['occupancy']:+.3f}  barr={w['escape_barrier']:+.3f}  "
              f"comm={w['committor0']:+.3f}  | z_epi(h+)={r['z_after_int_hp']:+.2f} "
              f"z_epi(h-)={r['z_after_int_hm']:+.2f}  Wsel_sd(occ)={r['Wsel_sd']['occupancy']:.3f}")

    print("\n--- W_global robustness (KL/JS/TV x uniform/pre_occ/mixture), h+ vs own-pre ---")
    for name, r in res.items():
        g = r["Wglobal"]
        print(f"{name:<18} " + "  ".join(
            f"{rm[:3]}:KL={g[rm]['KL']:.2f}/JS={g[rm]['JS']:.3f}/TV={g[rm]['TV']:.3f}"
            for rm in ["uniform", "pre_occupancy", "mixture"]))
    print("\nwrote results_dissociation.json  (config_sha256=%s)" % cfg_hash)

if __name__ == "__main__":
    main()
