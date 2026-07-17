"""Parameter phase diagrams: confirm each P x W_sel cell occupies a contiguous
REGION of parameter space, not a single tuned point. Three small sweeps, each
targeting one non-trivial cell. Classification thresholds are fixed in advance.

  P_bit    = 1 if P_survival(h+) > 0.5
  Wsel_bit = 1 if W_sel(occupancy) > 0.10   (selection-specific, h+ vs h-)
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import model as M
from run_dissociation import landscape, phi_functionals

HERE = Path(__file__).parent
P = json.load(open(HERE / "config.json"))
P = dict(P); P["n_traj"] = 800; P["H"] = 30.0; P["H_withdraw"] = 8.0   # lighter for sweeps
SEED = 21

def cell_at(cond):
    rp = M.simulate(P, cond, +1, SEED)
    rm = M.simulate(P, cond, -1, SEED + 5000)
    c_hp, D_hp = landscape(P, cond, rp["z_after_int"])
    c_hm, D_hm = landscape(P, cond, rm["z_after_int"])
    wsel = phi_functionals(c_hp, D_hp)["occupancy"] - phi_functionals(c_hm, D_hm)["occupancy"]
    p_bit = 1 if rp["P_survival"] > 0.5 else 0
    w_bit = 1 if wsel > 0.10 else 0
    return p_bit, w_bit, rp["P_survival"], wsel

def glyph(p, w):
    return {(0, 0): ".", (1, 0): "H", (0, 1): "L", (1, 1): "A"}[(p, w)]
#   . = P- Wsel- (null)   H = P+ Wsel- (pre-existing hold)
#   L = P- Wsel+ (latent) A = P+ Wsel+ (anchor)

def sweep(name, base, xkey, xs, ykey, ys):
    print(f"\n### sweep: {name}   rows={ykey} down, cols={xkey} right")
    grid = []
    for y in ys:
        row = []
        for x in xs:
            cond = dict(base); cond[xkey] = float(x); cond[ykey] = float(y)
            p, w, ps, ws = cell_at(cond)
            row.append((p, w, ps, ws))
        grid.append(row)
    # ASCII map
    print("      " + "".join(f"{x:>6.2f}" for x in xs))
    for y, row in zip(ys, grid):
        print(f"{y:>5.2f} " + "".join(f"{glyph(p,w):>6}" for (p, w, _, _) in row))
    # region check: largest 4-connected component per cell type
    from collections import deque
    def largest_region(target):
        seen = [[False]*len(xs) for _ in ys]; best = 0
        for i in range(len(ys)):
            for j in range(len(xs)):
                if seen[i][j]: continue
                p, w = grid[i][j][0], grid[i][j][1]
                if (p, w) != target: continue
                q = deque([(i, j)]); seen[i][j] = True; sz = 0
                while q:
                    a, b = q.popleft(); sz += 1
                    for da, db in ((1,0),(-1,0),(0,1),(0,-1)):
                        na, nb = a+da, b+db
                        if 0 <= na < len(ys) and 0 <= nb < len(xs) and not seen[na][nb] \
                           and (grid[na][nb][0], grid[na][nb][1]) == target:
                            seen[na][nb] = True; q.append((na, nb))
                best = max(best, sz)
        return best
    return {"grid": [[[int(p),int(w),float(ps),float(ws)] for (p,w,ps,ws) in row] for row in grid],
            "xs": list(map(float, xs)), "ys": list(map(float, ys)),
            "xkey": xkey, "ykey": ykey,
            "largest_region": {f"{p}{w}": largest_region((p, w))
                               for p in (0, 1) for w in (0, 1)}}

def main():
    results = {}
    # D0 is a global param, not per-condition, so sweeps that vary it copy P.
    def sweep_with_D0(name, base, etas, D0s, latent=False):
        print(f"\n### sweep: {name}   rows=D0 down, cols=eta right")
        grid = []
        for D0 in D0s:
            Pl = dict(P); Pl["D0"] = float(D0)
            row = []
            for eta in etas:
                cond = dict(base); cond["eta"] = float(eta)
                if latent: cond["latent"] = True
                rp = M.simulate(Pl, cond, +1, SEED)
                rm = M.simulate(Pl, cond, -1, SEED + 5000)
                c_hp, D_hp = landscape(Pl, cond, rp["z_after_int"])
                c_hm, D_hm = landscape(Pl, cond, rm["z_after_int"])
                ws = phi_functionals(c_hp, D_hp)["occupancy"] - phi_functionals(c_hm, D_hm)["occupancy"]
                p = 1 if rp["P_survival"] > 0.5 else 0
                w = 1 if ws > 0.10 else 0
                row.append((p, w, rp["P_survival"], ws))
            grid.append(row)
        print("       " + "".join(f"{e:>6.2f}" for e in etas))
        for D0, row in zip(D0s, grid):
            print(f"{D0:>5.3f} " + "".join(f"{glyph(p,w):>6}" for (p,w,_,_) in row))
        from collections import deque
        def largest(target):
            seen=[[False]*len(etas) for _ in D0s]; best=0
            for i in range(len(D0s)):
                for j in range(len(etas)):
                    if seen[i][j] or (grid[i][j][0],grid[i][j][1])!=target: continue
                    q=deque([(i,j)]); seen[i][j]=True; sz=0
                    while q:
                        a,b=q.popleft(); sz+=1
                        for da,db in((1,0),(-1,0),(0,1),(0,-1)):
                            na,nb=a+da,b+db
                            if 0<=na<len(D0s) and 0<=nb<len(etas) and not seen[na][nb] and (grid[na][nb][0],grid[na][nb][1])==target:
                                seen[na][nb]=True; q.append((na,nb))
                    best=max(best,sz)
            return best
        return {"grid":[[[int(p),int(w),float(ps),float(ws)] for (p,w,ps,ws) in row] for row in grid],
                "etas":list(map(float,etas)),"D0s":list(map(float,D0s)),
                "largest_region":{f"{p}{w}":largest((p,w)) for p in(0,1) for w in(0,1)}}

    etas = np.linspace(0.0, 0.40, 9)
    D0s = np.linspace(0.03, 0.15, 7)
    results["anchor"] = sweep_with_D0("anchor (c0=-0.5, deepen)  A=P+Wsel+",
                                      {"c0": -0.5, "lam": 0.05, "channel": "deepen", "tau": 12.0},
                                      etas, D0s)
    results["latent"] = sweep_with_D0("latent (c0=0, deepen, latent protocol)  L=P-Wsel+",
                                      {"c0": 0.0, "lam": 0.05, "channel": "deepen", "tau": 12.0},
                                      etas, D0s, latent=True)
    # Sweep 3: pre-existing hold over a range of c0 (eta=0).  expect H-region (P+ Wsel-)
    print("\n### sweep: pre-existing (eta=0, deepen)   rows=D0 down, cols=c0 right")
    c0s = np.linspace(0.10, 0.50, 9); D0s2 = np.linspace(0.03, 0.15, 7)
    grid3=[]
    for D0 in D0s2:
        Pl=dict(P); Pl["D0"]=float(D0); row=[]
        for c0 in c0s:
            cond={"c0":float(c0),"eta":0.0,"lam":0.05,"channel":"deepen","tau":12.0}
            rp=M.simulate(Pl,cond,+1,SEED)
            c_hp,D_hp=landscape(Pl,cond,rp["z_after_int"])
            ws=0.0  # eta=0 -> no written asymmetry -> Wsel=0 by construction
            p=1 if rp["P_survival"]>0.5 else 0; w=0
            row.append((p,w,rp["P_survival"],ws))
        grid3.append(row)
    print("       "+"".join(f"{c:>6.2f}" for c in c0s))
    for D0,row in zip(D0s2,grid3):
        print(f"{D0:>5.3f} "+"".join(f"{glyph(p,w):>6}" for (p,w,_,_) in row))
    results["preexisting"]={"grid":[[[int(p),int(w),float(ps),float(ws)] for (p,w,ps,ws) in row] for row in grid3],
                            "c0s":list(map(float,c0s)),"D0s":list(map(float,D0s2))}

    (HERE/"results_sweep.json").write_text(json.dumps(results,indent=2))
    print("\nlargest contiguous region per cell:")
    for k in ("anchor","latent"):
        print(f"  {k}: {results[k]['largest_region']}")
    print("wrote results_sweep.json")

if __name__ == "__main__":
    main()
