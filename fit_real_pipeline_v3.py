import csv
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "unified_srt_mtor.csv"


def load_spike_rows(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            if row["spike_count"] == "":
                continue
            row["spike_count"] = int(row["spike_count"])
            row["dt_sec"] = float(row["dt_sec"])
            row["u_observer"] = float(row["u_observer"])
            row["t_sec"] = float(row["t_sec"])
            rows.append(row)
    return rows


def grouped_split(rows):
    # deterministic grouped split by circuit_id
    circuits = sorted({r["circuit_id"] for r in rows})
    n = len(circuits)
    n_train = max(1, int(0.7 * n))
    n_valid = max(1, int(0.15 * n))
    train = set(circuits[:n_train])
    valid = set(circuits[n_train:n_train + n_valid])

    for r in rows:
        c = r["circuit_id"]
        if c in train:
            r["split_v3"] = "train"
        elif c in valid:
            r["split_v3"] = "valid"
        else:
            r["split_v3"] = "test"


def add_block_id(rows, block_sec=5.0):
    for r in rows:
        bid = int(r["t_sec"] // block_sec)
        r["block_id"] = f"{r['session_id']}_b{bid:02d}"


def zscore_u_within_block(rows):
    by_block = defaultdict(list)
    for r in rows:
        by_block[r["block_id"]].append(r["u_observer"])

    stats = {}
    for b, us in by_block.items():
        mu = sum(us) / len(us)
        var = sum((u - mu) ** 2 for u in us) / max(1, len(us) - 1)
        sd = math.sqrt(var) if var > 1e-12 else 1.0
        stats[b] = (mu, sd)

    for r in rows:
        mu, sd = stats[r["block_id"]]
        r["u_z"] = (r["u_observer"] - mu) / sd


def poisson_nll(y, mu):
    eps = 1e-12
    return sum(m - yy * math.log(m + eps) for yy, m in zip(y, mu))


def estimate_baseline(rows):
    # circuit-specific baseline from train
    per_c = defaultdict(list)
    for r in rows:
        if r["split_v3"] == "train":
            per_c[r["circuit_id"]].append(r)

    l0 = {}
    for c, rs in per_c.items():
        s = sum(x["spike_count"] for x in rs)
        t = sum(x["dt_sec"] for x in rs)
        l0[c] = max(1e-6, s / t)

    global_l0 = sum(l0.values()) / max(1, len(l0))
    return l0, global_l0


def objective_train(rows, l0_map, l0_global, mu_omega, delta_map, sigma_delta):
    y, mu = [], []
    for r in rows:
        if r["split_v3"] != "train":
            continue
        l0 = l0_map.get(r["circuit_id"], l0_global)
        b = r["block_id"]
        w = mu_omega + delta_map.get(b, 0.0)
        m = max(1e-10, l0 * r["dt_sec"] * math.exp(w * r["u_z"]))
        y.append(r["spike_count"])
        mu.append(m)

    nll = poisson_nll(y, mu)
    # gaussian prior penalty for block deviations (hierarchical shrinkage)
    pen = 0.5 * sum((d / sigma_delta) ** 2 for d in delta_map.values())
    return nll + pen


def fit_hierarchical(rows, l0_map, l0_global, sigma_delta=0.25, iters=4):
    blocks = sorted({r["block_id"] for r in rows if r["split_v3"] == "train"})
    delta = {b: 0.0 for b in blocks}

    mu_grid = [i / 40 for i in range(-8, 49)]  # -0.2..1.2
    d_grid = [i / 40 for i in range(-20, 21)]  # -0.5..0.5

    mu_hat = 0.0
    for _ in range(iters):
        # update global mu
        best_mu, best_obj = None, float("inf")
        for mu in mu_grid:
            obj = objective_train(rows, l0_map, l0_global, mu, delta, sigma_delta)
            if obj < best_obj:
                best_obj, best_mu = obj, mu
        mu_hat = best_mu

        # update each block delta with others fixed
        for b in blocks:
            best_d, best_obj_d = None, float("inf")
            old = delta[b]
            for d in d_grid:
                delta[b] = d
                obj = objective_train(rows, l0_map, l0_global, mu_hat, delta, sigma_delta)
                if obj < best_obj_d:
                    best_obj_d, best_d = obj, d
            delta[b] = best_d if best_d is not None else old

    obj_hat = objective_train(rows, l0_map, l0_global, mu_hat, delta, sigma_delta)
    # null: mu=0 and all delta=0
    delta0 = {b: 0.0 for b in blocks}
    obj_null = objective_train(rows, l0_map, l0_global, 0.0, delta0, sigma_delta)
    lr = 2 * (obj_null - obj_hat)

    return mu_hat, delta, obj_hat, obj_null, lr


def eval_split(rows, l0_map, l0_global, mu_hat, delta_map, split):
    y, mu = [], []
    for r in rows:
        if r["split_v3"] != split:
            continue
        l0 = l0_map.get(r["circuit_id"], l0_global)
        w = mu_hat + delta_map.get(r["block_id"], 0.0)
        m = max(1e-10, l0 * r["dt_sec"] * math.exp(w * r["u_z"]))
        y.append(r["spike_count"])
        mu.append(m)

    nll_hat = poisson_nll(y, mu)
    mu0 = [max(1e-10, l0_map.get(r["circuit_id"], l0_global) * r["dt_sec"]) for r in rows if r["split_v3"] == split]
    y0 = [r["spike_count"] for r in rows if r["split_v3"] == split]
    nll0 = poisson_nll(y0, mu0)
    return nll0 - nll_hat, len(y)


def approx_p_mu_gt_0(rows, l0_map, l0_global, sigma_delta=0.25):
    # integrate only over mu with delta fixed at 0 (fast approximation)
    grid = [i / 40 for i in range(-8, 49)]
    lls = []
    for mu in grid:
        obj = objective_train(rows, l0_map, l0_global, mu, {}, sigma_delta)
        lls.append(-obj)

    m = max(lls)
    ws = [math.exp(ll - m) for ll in lls]
    z = sum(ws)
    ps = [w / z for w in ws]
    p_pos = sum(p for g, p in zip(grid, ps) if g > 0)
    mean = sum(g * p for g, p in zip(grid, ps))
    return mean, p_pos


def main():
    rows = load_spike_rows(DATA_PATH)
    grouped_split(rows)
    add_block_id(rows, block_sec=5.0)
    zscore_u_within_block(rows)

    l0_map, l0_global = estimate_baseline(rows)
    mu_hat, delta_map, obj_hat, obj0, lr = fit_hierarchical(rows, l0_map, l0_global, sigma_delta=0.25, iters=4)

    d_valid, n_valid = eval_split(rows, l0_map, l0_global, mu_hat, delta_map, "valid")
    d_test, n_test = eval_split(rows, l0_map, l0_global, mu_hat, delta_map, "test")
    mu_mean, p_mu_pos = approx_p_mu_gt_0(rows, l0_map, l0_global)

    print("=== fit_real_pipeline_v3 summary ===")
    print(f"mu_omega_hat: {mu_hat:.6f}")
    print(f"mu_omega_mean≈ {mu_mean:.6f}")
    print(f"P(mu_omega>0)≈ {p_mu_pos:.6f}")
    print(f"train_LR: {lr:.6f}")
    print(f"valid_delta_nll: {d_valid:.6f} (n={n_valid})")
    print(f"test_delta_nll: {d_test:.6f} (n={n_test})")
    print(f"n_train: {sum(1 for r in rows if r['split_v3']=='train')}")
    print(f"n_blocks_train: {len({r['block_id'] for r in rows if r['split_v3']=='train'})}")


if __name__ == "__main__":
    main()
