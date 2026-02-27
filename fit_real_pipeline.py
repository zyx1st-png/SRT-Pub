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
            # keep only rows with spike_count for firing model fit
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


def fit_omega_only(rows):
    # Baseline lambda per circuit from train split only
    per_circuit = defaultdict(list)
    for row in rows:
        if row["split"] == "train":
            per_circuit[row["circuit_id"]].append(row)

    lambda0 = {}
    for cid, rs in per_circuit.items():
        total_spikes = sum(r["spike_count"] for r in rs)
        total_t = sum(r["dt_sec"] for r in rs)
        lambda0[cid] = max(1e-6, total_spikes / total_t)

    # Optimize omega globally on train split
    y_train = []
    u_train = []
    l0_train = []
    for row in rows:
        if row["split"] != "train":
            continue
        cid = row["circuit_id"]
        if cid not in lambda0:
            continue
        y_train.append(row["spike_count"])
        u_train.append(row["u_observer"])
        l0_train.append(lambda0[cid] * row["dt_sec"])

    best_omega = None
    best_nll = float("inf")
    grid = [i / 20 for i in range(-4, 41)]  # -0.2..2.0
    for w in grid:
        mu = [max(1e-10, l0 * math.exp(w * u)) for l0, u in zip(l0_train, u_train)]
        nll = poisson_nll(y_train, mu)
        if nll < best_nll:
            best_nll = nll
            best_omega = w

    # Null model omega=0
    mu0 = [max(1e-10, l0 * math.exp(0.0 * u)) for l0, u in zip(l0_train, u_train)]
    nll0 = poisson_nll(y_train, mu0)
    lr = 2 * (nll0 - best_nll)

    return lambda0, best_omega, best_nll, nll0, lr


def eval_split(rows, lambda0, omega, split="test"):
    y = []
    mu = []
    for row in rows:
        if row["split"] != split:
            continue
        cid = row["circuit_id"]
        if cid not in lambda0:
            continue
        l0 = lambda0[cid] * row["dt_sec"]
        m = max(1e-10, l0 * math.exp(omega * row["u_observer"]))
        y.append(row["spike_count"])
        mu.append(m)
    return poisson_nll(y, mu), len(y)


def permutation_test(rows, lambda0, omega_hat, n_perm=100, seed=0):
    random.seed(seed)

    train_rows = [r for r in rows if r["split"] == "train" and r["circuit_id"] in lambda0]
    us = [r["u_observer"] for r in train_rows]
    ys = [r["spike_count"] for r in train_rows]
    l0s = [lambda0[r["circuit_id"]] * r["dt_sec"] for r in train_rows]

    def best_nll_for_u(u_vals):
        best = float("inf")
        for w in [i / 20 for i in range(-4, 41)]:
            mu = [max(1e-10, l0 * math.exp(w * u)) for l0, u in zip(l0s, u_vals)]
            nll = poisson_nll(ys, mu)
            if nll < best:
                best = nll
        return best

    obs_best = best_nll_for_u(us)
    null_better = 0
    for _ in range(n_perm):
        up = us[:]
        random.shuffle(up)
        nll_p = best_nll_for_u(up)
        if nll_p <= obs_best:
            null_better += 1

    pval = (null_better + 1) / (n_perm + 1)
    return obs_best, pval


def approx_p_omega_gt_0(rows, lambda0):
    # Approx posterior over omega with flat prior on grid
    train_rows = [r for r in rows if r["split"] == "train" and r["circuit_id"] in lambda0]
    ys = [r["spike_count"] for r in train_rows]
    us = [r["u_observer"] for r in train_rows]
    l0s = [lambda0[r["circuit_id"]] * r["dt_sec"] for r in train_rows]

    grid = [i / 40 for i in range(-8, 81)]  # -0.2..2.0, step 0.025
    lls = []
    for w in grid:
        mu = [max(1e-10, l0 * math.exp(w * u)) for l0, u in zip(l0s, us)]
        ll = -poisson_nll(ys, mu)
        lls.append(ll)

    m = max(lls)
    ws = [math.exp(ll - m) for ll in lls]
    z = sum(ws)
    probs = [w / z for w in ws]

    ppos = sum(p for w, p in zip(grid, probs) if w > 0)
    mean = sum(w * p for w, p in zip(grid, probs))

    return mean, ppos


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"missing {DATA_PATH}")

    rows = load_rows(DATA_PATH)
    lambda0, omega_hat, nll_hat, nll0, lr = fit_omega_only(rows)

    nll_valid, n_valid = eval_split(rows, lambda0, omega_hat, split="valid")
    nll_test, n_test = eval_split(rows, lambda0, omega_hat, split="test")
    nll_valid_null, _ = eval_split(rows, lambda0, 0.0, split="valid")
    nll_test_null, _ = eval_split(rows, lambda0, 0.0, split="test")

    obs_nll, p_perm = permutation_test(rows, lambda0, omega_hat, n_perm=80)
    omega_mean, p_omega_pos = approx_p_omega_gt_0(rows, lambda0)

    print("=== fit_real_pipeline summary ===")
    print(f"train rows: {sum(1 for r in rows if r['split']=='train')}")
    print(f"valid rows: {n_valid}, test rows: {n_test}")
    print(f"omega_hat={omega_hat:.3f}, omega_mean≈{omega_mean:.3f}, P(omega>0)≈{p_omega_pos:.5f}")
    print(f"train NLL(omega=0)={nll0:.3f}, train NLL(omega=hat)={nll_hat:.3f}, LR={lr:.3f}")
    print(f"valid ΔNLL(null-hat)={nll_valid_null - nll_valid:.3f}")
    print(f"test  ΔNLL(null-hat)={nll_test_null - nll_test:.3f}")
    print(f"permutation p-value≈{p_perm:.5f} (smaller is better)")


if __name__ == "__main__":
    main()
