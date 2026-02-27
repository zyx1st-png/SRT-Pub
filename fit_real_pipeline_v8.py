import csv
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "unified_srt_mtor_real_multi_condid.csv"


def poisson_nll(y, mu):
    eps = 1e-12
    return sum(m - yy * math.log(m + eps) for yy, m in zip(y, mu))


def load_rows(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            if row["spike_count"] == "":
                continue
            rows.append({
                "session_id": row["session_id"],
                "circuit_id": row["circuit_id"],
                "condition": row["condition"],
                "split": row["split"],
                "dt": float(row["dt_sec"]),
                "y": int(row["spike_count"]),
                "u": float(row["u_observer"]),
                "t": float(row["t_sec"]),
            })
    return rows


def prepare_psif(rows):
    # hazard-like friction proxy by unit sequence: |Δe| where e=u - cond_mean_u(train)
    cond_mu = defaultdict(list)
    for r in rows:
        if r["split"] == "train":
            cond_mu[r["condition"]].append(r["u"])
    cond_mu = {k: sum(v)/len(v) for k,v in cond_mu.items()}

    by_unit = defaultdict(list)
    for r in rows:
        by_unit[(r["session_id"], r["circuit_id"])].append(r)
    for k in by_unit:
        by_unit[k].sort(key=lambda z: z["t"])
        prev = None
        for r in by_unit[k]:
            e = r["u"] - cond_mu.get(r["condition"], 0.0)
            r["psi_f"] = 0.0 if prev is None else abs(e - prev)
            prev = e


def fit_offsets(rows, use_omega=False, omega=0.0, use_fric=False, c_fric=0.0):
    # Estimate additive log-rate offsets per unit/session/condition from train by ratio-to-global
    train = [r for r in rows if r["split"] == "train"]
    global_rate = sum(r["y"] for r in train) / max(1e-9, sum(r["dt"] for r in train))

    def adj_weight(r):
        w = math.exp(omega * r["u"]) if use_omega else 1.0
        if use_fric:
            w *= math.exp(-c_fric * r["psi_f"])
        return w

    # effective exposure adjustment
    by_u = defaultdict(lambda: [0.0, 0.0])
    by_s = defaultdict(lambda: [0.0, 0.0])
    by_c = defaultdict(lambda: [0.0, 0.0])

    for r in train:
        w = adj_weight(r)
        by_u[r["circuit_id"]][0] += r["y"]
        by_u[r["circuit_id"]][1] += r["dt"] * w

        by_s[r["session_id"]][0] += r["y"]
        by_s[r["session_id"]][1] += r["dt"] * w

        by_c[r["condition"]][0] += r["y"]
        by_c[r["condition"]][1] += r["dt"] * w

    def to_offset(tab):
        out = {}
        for k,(yy,ee) in tab.items():
            rate = yy / max(1e-9, ee)
            out[k] = math.log(max(1e-12, rate / global_rate))
        return out

    return global_rate, to_offset(by_u), to_offset(by_s), to_offset(by_c)


def nll(rows, global_rate, ou, os, oc, omega=0.0, c_fric=0.0, use_omega=False, use_fric=False, split="train"):
    ys, mus = [], []
    for r in rows:
        if r["split"] != split:
            continue
        loglam = math.log(global_rate)
        loglam += ou.get(r["circuit_id"], 0.0)
        loglam += os.get(r["session_id"], 0.0)
        loglam += oc.get(r["condition"], 0.0)
        if use_omega:
            loglam += omega * r["u"]
        if use_fric:
            loglam += -c_fric * r["psi_f"]
        mu = max(1e-10, math.exp(loglam) * r["dt"])
        ys.append(r["y"])
        mus.append(mu)
    return poisson_nll(ys, mus), len(ys)


def fit_v8(rows):
    # M0: no omega no friction
    g0, ou0, os0, oc0 = fit_offsets(rows, use_omega=False, use_fric=False)
    nll0_train, _ = nll(rows, g0, ou0, os0, oc0, split="train")

    # M1: omega
    best1 = (None, float("inf"), None)
    for w in [i/200 for i in range(-40, 41)]:  # -0.2..0.2 finer grid
        g, ou, os, oc = fit_offsets(rows, use_omega=True, omega=w, use_fric=False)
        v, _ = nll(rows, g, ou, os, oc, omega=w, use_omega=True, split="train")
        if v < best1[1]:
            best1 = (w, v, (g, ou, os, oc))

    # M2: omega + friction
    best2 = (None, None, float("inf"), None)
    for w in [i/200 for i in range(-40, 41)]:
        for c in [i/20 for i in range(0, 21)]:  # 0..1
            g, ou, os, oc = fit_offsets(rows, use_omega=True, omega=w, use_fric=True, c_fric=c)
            v, _ = nll(rows, g, ou, os, oc, omega=w, c_fric=c, use_omega=True, use_fric=True, split="train")
            if v < best2[2]:
                best2 = (w, c, v, (g, ou, os, oc))

    return nll0_train, best1, best2


def eval_models(rows, nll0_train, best1, best2):
    w1, nll1_train, p1 = best1
    w2, c2, nll2_train, p2 = best2

    g0, ou0, os0, oc0 = fit_offsets(rows, use_omega=False, use_fric=False)

    out = {}
    for sp in ["valid", "test"]:
        n0, n_sp = nll(rows, g0, ou0, os0, oc0, split=sp)
        n1, _ = nll(rows, *p1, omega=w1, use_omega=True, split=sp)
        n2, _ = nll(rows, *p2, omega=w2, c_fric=c2, use_omega=True, use_fric=True, split=sp)
        out[sp] = {
            "n": n_sp,
            "dNLL_M1": n0 - n1,
            "dNLL_M2": n0 - n2,
            "dNLL_M2vsM1": n1 - n2,
        }

    return {
        "omega_m1": w1,
        "omega_m2": w2,
        "c_fric_m2": c2,
        "train_LR_M1": 2*(nll0_train - nll1_train),
        "train_LR_M2": 2*(nll0_train - nll2_train),
        "train_LR_M2vsM1": 2*(nll1_train - nll2_train),
        "eval": out,
    }


def main():
    rows = load_rows(DATA_PATH)
    prepare_psif(rows)
    nll0_train, best1, best2 = fit_v8(rows)
    rep = eval_models(rows, nll0_train, best1, best2)

    print("=== fit_real_pipeline_v8 summary ===")
    print(f"omega_m1={rep['omega_m1']:.4f}")
    print(f"omega_m2={rep['omega_m2']:.4f}, c_fric_m2={rep['c_fric_m2']:.3f}")
    print(f"train_LR_M1={rep['train_LR_M1']:.3f}")
    print(f"train_LR_M2={rep['train_LR_M2']:.3f}")
    print(f"train_LR_M2vsM1={rep['train_LR_M2vsM1']:.3f}")
    for sp in ["valid","test"]:
        e = rep['eval'][sp]
        print(f"{sp}: n={e['n']}, dNLL_M1={e['dNLL_M1']:.3f}, dNLL_M2={e['dNLL_M2']:.3f}, dNLL_M2vsM1={e['dNLL_M2vsM1']:.3f}")


if __name__ == "__main__":
    main()
