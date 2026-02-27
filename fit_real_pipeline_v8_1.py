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


def add_lag_feature(rows):
    by_uc = defaultdict(list)
    for r in rows:
        by_uc[(r["session_id"], r["circuit_id"])].append(r)
    for k in by_uc:
        by_uc[k].sort(key=lambda z: z["t"])
        prev = 0
        for r in by_uc[k]:
            r["lag1"] = prev
            prev = r["y"]


def fit_offsets(rows, beta_lag=0.0, omega=0.0, use_omega=False):
    train = [r for r in rows if r["split"] == "train"]
    g = sum(r["y"] for r in train) / max(1e-9, sum(r["dt"] for r in train))

    by_u = defaultdict(lambda: [0.0, 0.0])
    by_s = defaultdict(lambda: [0.0, 0.0])
    by_c = defaultdict(lambda: [0.0, 0.0])

    for r in train:
        w = math.exp(beta_lag * r["lag1"]) * (math.exp(omega * r["u"]) if use_omega else 1.0)
        by_u[r["circuit_id"]][0] += r["y"]
        by_u[r["circuit_id"]][1] += r["dt"] * w
        by_s[r["session_id"]][0] += r["y"]
        by_s[r["session_id"]][1] += r["dt"] * w
        by_c[r["condition"]][0] += r["y"]
        by_c[r["condition"]][1] += r["dt"] * w

    def to_off(tab):
        out = {}
        for k, (yy, ee) in tab.items():
            rate = yy / max(1e-9, ee)
            out[k] = math.log(max(1e-12, rate / g))
        return out

    return g, to_off(by_u), to_off(by_s), to_off(by_c)


def nll(rows, g, ou, os, oc, beta_lag=0.0, omega=0.0, use_omega=False, split="train"):
    ys, mus = [], []
    for r in rows:
        if r["split"] != split:
            continue
        loglam = math.log(g) + ou.get(r["circuit_id"], 0.0) + os.get(r["session_id"], 0.0) + oc.get(r["condition"], 0.0)
        loglam += beta_lag * r["lag1"]
        if use_omega:
            loglam += omega * r["u"]
        mu = max(1e-10, math.exp(loglam) * r["dt"])
        ys.append(r["y"])
        mus.append(mu)
    return poisson_nll(ys, mus), len(ys)


def main():
    rows = load_rows(DATA_PATH)
    add_lag_feature(rows)

    # M0': baseline + lag
    best0 = (None, float("inf"), None)
    for b in [i / 200 for i in range(0, 21)]:  # 0..0.1
        g, ou, os, oc = fit_offsets(rows, beta_lag=b, use_omega=False)
        v, _ = nll(rows, g, ou, os, oc, beta_lag=b, use_omega=False, split="train")
        if v < best0[1]:
            best0 = (b, v, (g, ou, os, oc))

    # M1': baseline + lag + omega
    best1 = (None, None, float("inf"), None)
    for b in [i / 200 for i in range(0, 21)]:
        for w in [i / 200 for i in range(-40, 41)]:
            g, ou, os, oc = fit_offsets(rows, beta_lag=b, omega=w, use_omega=True)
            v, _ = nll(rows, g, ou, os, oc, beta_lag=b, omega=w, use_omega=True, split="train")
            if v < best1[2]:
                best1 = (b, w, v, (g, ou, os, oc))

    b0, n0, p0 = best0
    b1, w1, n1, p1 = best1

    print("=== fit_real_pipeline_v8.1 summary ===")
    print(f"beta_lag_m0={b0:.4f}")
    print(f"beta_lag_m1={b1:.4f}, omega_m1={w1:.4f}")
    print(f"train_LR_M1vsM0={2*(n0-n1):.3f}")

    for sp in ["valid", "test"]:
        n0s, ns = nll(rows, *p0, beta_lag=b0, use_omega=False, split=sp)
        n1s, _ = nll(rows, *p1, beta_lag=b1, omega=w1, use_omega=True, split=sp)
        print(f"{sp}: n={ns}, dNLL_M1vsM0={n0s - n1s:.3f}")


if __name__ == "__main__":
    main()
