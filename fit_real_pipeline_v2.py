import csv
import math
import random
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "unified_srt_mtor.csv"


def load_rows(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            if row["spike_count"] == "":
                continue
            row["spike_count"] = int(row["spike_count"])
            row["dt_sec"] = float(row["dt_sec"])
            row["u_observer"] = float(row["u_observer"])
            rows.append(row)
    return rows


def poisson_nll(y, mu):
    eps = 1e-12
    return sum(m - yy * math.log(m + eps) for yy, m in zip(y, mu))


def assign_group_split(rows):
    # grouped split by (session, circuit) to reduce temporal leakage
    groups = sorted({(r["session_id"], r["circuit_id"]) for r in rows})
    random.seed(123)
    random.shuffle(groups)

    n = len(groups)
    n_train = max(1, int(0.7 * n))
    n_valid = max(1, int(0.15 * n))

    train_g = set(groups[:n_train])
    valid_g = set(groups[n_train:n_train + n_valid])
    test_g = set(groups[n_train + n_valid:])

    for r in rows:
        g = (r["session_id"], r["circuit_id"])
        if g in train_g:
            r["split_v2"] = "train"
        elif g in valid_g:
            r["split_v2"] = "valid"
        elif g in test_g:
            r["split_v2"] = "test"
        else:
            r["split_v2"] = "test"


def estimate_baselines(rows):
    # circuit random effect proxy: baseline per circuit from train split_v2
    per_circuit = defaultdict(list)
    for r in rows:
        if r["split_v2"] == "train":
            per_circuit[r["circuit_id"]].append(r)

    lambda0 = {}
    for cid, rs in per_circuit.items():
        s = sum(x["spike_count"] for x in rs)
        t = sum(x["dt_sec"] for x in rs)
        lambda0[cid] = max(1e-6, s / t)

    global_base = sum(lambda0.values()) / max(1, len(lambda0))
    return lambda0, global_base


def nll_for_split(rows, split, omega, lambda0, global_base):
    y, mu = [], []
    for r in rows:
        if r["split_v2"] != split:
            continue
        lbase = lambda0.get(r["circuit_id"], global_base)
        m = max(1e-10, lbase * r["dt_sec"] * math.exp(omega * r["u_observer"]))
        y.append(r["spike_count"])
        mu.append(m)
    return poisson_nll(y, mu), len(y)


def fit_omega(rows, lambda0, global_base):
    best_w, best_nll = None, float("inf")
    for w in [i / 20 for i in range(-4, 41)]:
        nll, _ = nll_for_split(rows, "train", w, lambda0, global_base)
        if nll < best_nll:
            best_nll = nll
            best_w = w

    null_nll, _ = nll_for_split(rows, "train", 0.0, lambda0, global_base)
    lr = 2 * (null_nll - best_nll)
    return best_w, best_nll, null_nll, lr


def approx_posterior_w(rows, lambda0, global_base):
    grid = [i / 40 for i in range(-8, 81)]
    lls = []
    for w in grid:
        nll, _ = nll_for_split(rows, "train", w, lambda0, global_base)
        lls.append(-nll)
    m = max(lls)
    ws = [math.exp(ll - m) for ll in lls]
    z = sum(ws)
    probs = [w / z for w in ws]
    p_pos = sum(p for w, p in zip(grid, probs) if w > 0)
    mean = sum(w * p for w, p in zip(grid, probs))
    return mean, p_pos


def permutation_test(rows, lambda0, global_base, n_perm=100):
    train_rows = [r for r in rows if r["split_v2"] == "train"]
    us = [r["u_observer"] for r in train_rows]

    def best_nll_with_u(uvals):
        best = float("inf")
        for w in [i / 20 for i in range(-4, 41)]:
            y, mu = [], []
            for r, u in zip(train_rows, uvals):
                lbase = lambda0.get(r["circuit_id"], global_base)
                m = max(1e-10, lbase * r["dt_sec"] * math.exp(w * u))
                y.append(r["spike_count"])
                mu.append(m)
            nll = poisson_nll(y, mu)
            if nll < best:
                best = nll
        return best

    obs = best_nll_with_u(us)
    better = 0
    random.seed(999)
    for _ in range(n_perm):
        up = us[:]
        random.shuffle(up)
        pnll = best_nll_with_u(up)
        if pnll <= obs:
            better += 1
    p = (better + 1) / (n_perm + 1)
    return p


def main():
    rows = load_rows(DATA_PATH)
    assign_group_split(rows)
    lambda0, global_base = estimate_baselines(rows)
    w_hat, nll_hat, nll0, lr = fit_omega(rows, lambda0, global_base)
    w_mean, p_pos = approx_posterior_w(rows, lambda0, global_base)
    p_perm = permutation_test(rows, lambda0, global_base, n_perm=80)

    v_hat, n_v = nll_for_split(rows, "valid", w_hat, lambda0, global_base)
    v_0, _ = nll_for_split(rows, "valid", 0.0, lambda0, global_base)
    t_hat, n_t = nll_for_split(rows, "test", w_hat, lambda0, global_base)
    t_0, _ = nll_for_split(rows, "test", 0.0, lambda0, global_base)

    out = {
        "omega_hat": w_hat,
        "omega_mean": w_mean,
        "p_omega_gt_0": p_pos,
        "train_lr": lr,
        "valid_delta_nll": v_0 - v_hat,
        "test_delta_nll": t_0 - t_hat,
        "perm_p": p_perm,
        "n_train": sum(1 for r in rows if r["split_v2"] == "train"),
        "n_valid": n_v,
        "n_test": n_t,
    }

    print("=== fit_real_pipeline_v2 summary ===")
    for k, v in out.items():
        if isinstance(v, float):
            print(f"{k}: {v:.6f}")
        else:
            print(f"{k}: {v}")


if __name__ == "__main__":
    main()
