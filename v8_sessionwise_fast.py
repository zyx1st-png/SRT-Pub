import csv
import math
from collections import defaultdict
from pathlib import Path

DATA = Path("data/unified_srt_mtor_real_multi_condid.csv")
OUT = Path("results_v8_sessionwise.md")


def poisson_nll(y, mu):
    eps = 1e-12
    return sum(m - yy * math.log(m + eps) for yy, m in zip(y, mu))


def load_rows(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            rows.append(row)
    return rows


def assign_local_split(rows):
    for r in rows:
        t = float(r["t_sec"])
        if t < 420:
            r["split_local"] = "train"
        elif t < 510:
            r["split_local"] = "valid"
        else:
            r["split_local"] = "test"


def fit_session(rows):
    # build fixed offsets from train only
    train = [r for r in rows if r["split_local"] == "train"]
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

    def nll(split, omega=0.0):
        ys, mus = [], []
        for r in rows:
            if r["split_local"] != split:
                continue
            y = int(r["spike_count"])
            dt = float(r["dt_sec"])
            u = float(r["u_observer"])
            loglam = math.log(g) + ou.get(r["circuit_id"], 0.0) + oc.get(r["condition"], 0.0) + omega * u
            mu = max(1e-10, math.exp(loglam) * dt)
            ys.append(y)
            mus.append(mu)
        return poisson_nll(ys, mus)

    best_w, best_train = None, float("inf")
    for w in [-0.2, -0.1, 0.0, 0.1, 0.2]:
        nv = nll("train", omega=w)
        if nv < best_train:
            best_train = nv
            best_w = w

    n0_tr = nll("train", omega=0.0)
    n0_v = nll("valid", omega=0.0)
    n0_t = nll("test", omega=0.0)
    n1_v = nll("valid", omega=best_w)
    n1_t = nll("test", omega=best_w)

    return {
        "omega": best_w,
        "train_lr": 2 * (n0_tr - best_train),
        "valid_dnll": n0_v - n1_v,
        "test_dnll": n0_t - n1_t,
    }


def main():
    rows = load_rows(DATA)
    by_s = defaultdict(list)
    for r in rows:
        by_s[r["session_id"]].append(r)

    lines = [
        "# v8 Session-wise Report (fast)",
        "",
        "| session_id | omega_m1 | train_LR_M1 | valid_dNLL_M1 | test_dNLL_M1 |",
        "|---:|---:|---:|---:|---:|",
    ]

    for sid in sorted(by_s.keys()):
        rs = by_s[sid]
        assign_local_split(rs)
        rep = fit_session(rs)
        lines.append(f"| {sid} | {rep['omega']:.3f} | {rep['train_lr']:.3f} | {rep['valid_dnll']:.3f} | {rep['test_dnll']:.3f} |")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == '__main__':
    main()
