import csv
import math
from collections import defaultdict
from pathlib import Path

DATA = Path("data/unified_srt_mtor_real_multi_condid.csv")
OUT = Path("results_v8_1_sessionwise.md")


def poisson_nll(y, mu):
    eps = 1e-12
    return sum(m - yy * math.log(m + eps) for yy, m in zip(y, mu))


def add_local_split(rows):
    for r in rows:
        t = float(r["t_sec"])
        if t < 420:
            r["split_local"] = "train"
        elif t < 510:
            r["split_local"] = "valid"
        else:
            r["split_local"] = "test"


def add_lag(rows):
    rows.sort(key=lambda z: float(z["t_sec"]))
    prev = 0
    for r in rows:
        r["lag1"] = prev
        prev = int(r["spike_count"])


def fit_one_session(rows):
    by_unit = defaultdict(list)
    for r in rows:
        by_unit[r["circuit_id"]].append(r)
    for k in by_unit:
        add_lag(by_unit[k])

    allr = [x for v in by_unit.values() for x in v]

    train = [r for r in allr if r["split_local"] == "train"]
    g = sum(int(r["spike_count"]) for r in train) / sum(float(r["dt_sec"]) for r in train)

    by_u = defaultdict(lambda: [0.0, 0.0])
    by_c = defaultdict(lambda: [0.0, 0.0])
    for r in train:
        y = int(r["spike_count"])
        dt = float(r["dt_sec"])
        by_u[r["circuit_id"]][0] += y
        by_u[r["circuit_id"]][1] += dt
        by_c[r["condition"]][0] += y
        by_c[r["condition"]][1] += dt
    ou = {k: math.log(max(1e-9, (yy/ee)/g)) for k, (yy, ee) in by_u.items() if ee > 0}
    oc = {k: math.log(max(1e-9, (yy/ee)/g)) for k, (yy, ee) in by_c.items() if ee > 0}

    def score(split, beta_lag, omega):
        ys, mus = [], []
        for r in allr:
            if r["split_local"] != split:
                continue
            y = int(r["spike_count"])
            dt = float(r["dt_sec"])
            u = float(r["u_observer"])
            lag = r["lag1"]
            loglam = math.log(g) + ou.get(r["circuit_id"], 0.0) + oc.get(r["condition"], 0.0)
            loglam += beta_lag * lag + omega * u
            mu = max(1e-10, math.exp(loglam) * dt)
            ys.append(y)
            mus.append(mu)
        return poisson_nll(ys, mus)

    best = None
    best_train = float("inf")
    for b in [0.0, 0.05, 0.1]:
        for w in [-0.2, -0.1, 0.0, 0.1, 0.2]:
            nt = score("train", b, w)
            if nt < best_train:
                best_train = nt
                best = (b, w)

    b, w = best
    n0_tr = score("train", b, 0.0)
    n1_tr = score("train", b, w)
    n0_v = score("valid", b, 0.0)
    n1_v = score("valid", b, w)
    n0_t = score("test", b, 0.0)
    n1_t = score("test", b, w)

    return {
        "beta": b,
        "omega": w,
        "train_lr": 2 * (n0_tr - n1_tr),
        "valid_dnll": n0_v - n1_v,
        "test_dnll": n0_t - n1_t,
    }


def main():
    by_s = defaultdict(list)
    with open(DATA, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            by_s[row["session_id"]].append(row)

    lines = [
        "# v8.1 Session-wise Report (fast)",
        "",
        "| session_id | beta_lag | omega | train_LR | valid_dNLL | test_dNLL |",
        "|---:|---:|---:|---:|---:|---:|",
    ]

    for sid in sorted(by_s.keys()):
        rs = by_s[sid]
        add_local_split(rs)
        rep = fit_one_session(rs)
        lines.append(f"| {sid} | {rep['beta']:.2f} | {rep['omega']:.2f} | {rep['train_lr']:.3f} | {rep['valid_dnll']:.3f} | {rep['test_dnll']:.3f} |")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == '__main__':
    main()
