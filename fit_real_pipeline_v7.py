import csv
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "unified_srt_mtor.csv"


def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))


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
            row["spike_count"] = int(row["spike_count"])
            row["dt_sec"] = float(row["dt_sec"])
            row["t_sec"] = float(row["t_sec"])
            row["u_observer"] = float(row["u_observer"])
            rows.append(row)
    return rows


def prepare(rows):
    circuits = sorted({r["circuit_id"] for r in rows})
    n = len(circuits)
    n_train = max(1, int(0.7 * n))
    n_valid = max(1, int(0.15 * n))
    train_c = set(circuits[:n_train])
    valid_c = set(circuits[n_train:n_train + n_valid])

    for r in rows:
        c = r["circuit_id"]
        if c in train_c:
            r["split"] = "train"
        elif c in valid_c:
            r["split"] = "valid"
        else:
            r["split"] = "test"

        bid = int(r["t_sec"] // 5.0)
        r["block_id"] = f"{r['session_id']}_b{bid:02d}"

    # U zscore within block
    by_b = defaultdict(list)
    for r in rows:
        by_b[r["block_id"]].append(r["u_observer"])
    stats = {}
    for b, us in by_b.items():
        mu = sum(us) / len(us)
        var = sum((u - mu) ** 2 for u in us) / max(1, len(us) - 1)
        sd = math.sqrt(var) if var > 1e-12 else 1.0
        stats[b] = (mu, sd)
    for r in rows:
        mu, sd = stats[r["block_id"]]
        r["u_z"] = (r["u_observer"] - mu) / sd


def estimate_baseline(rows):
    per_c = defaultdict(list)
    for r in rows:
        if r["split"] == "train":
            per_c[r["circuit_id"]].append(r)
    l0 = {}
    for c, rs in per_c.items():
        l0[c] = max(1e-6, sum(x["spike_count"] for x in rs) / sum(x["dt_sec"] for x in rs))
    gl0 = sum(l0.values()) / max(1, len(l0))
    return l0, gl0


def build_l2_state(rows):
    # L2 rigidity proxy per block: higher mean activity + lower variance => more rigid
    by_b = defaultdict(list)
    for r in rows:
        by_b[r["block_id"]].append(r["spike_count"])

    l2 = {}
    for b, ys in by_b.items():
        mu = sum(ys) / len(ys)
        var = sum((y - mu) ** 2 for y in ys) / max(1, len(ys) - 1)
        rigidity = mu / (1.0 + var)
        l2[b] = rigidity

    # zscore rigidity
    vals = list(l2.values())
    m = sum(vals) / len(vals)
    v = sum((x - m) ** 2 for x in vals) / max(1, len(vals) - 1)
    s = math.sqrt(v) if v > 1e-12 else 1.0
    for b in l2:
        l2[b] = (l2[b] - m) / s
    return l2


def psi_f(u_z, l2_rigidity):
    # explicit ontological friction proxy:
    # friction grows with mismatch between immediate selection drive (u_z) and L2 rigidity
    return abs(u_z - l2_rigidity)


def nll_for_split(rows, split, l0, gl0, omega, alpha, theta, c_fric, l2_map):
    y, mu = [], []
    for r in rows:
        if r["split"] != split:
            continue
        base = l0.get(r["circuit_id"], gl0)
        x_hat = sigmoid(0.8 * r["u_z"])
        gate = sigmoid(4.0 * (x_hat - theta))
        pf = psi_f(r["u_z"], l2_map.get(r["block_id"], 0.0))

        m = base * r["dt_sec"] * math.exp(omega * r["u_z"]) * math.exp(alpha * (gate - 0.5)) * math.exp(-c_fric * pf)
        m = max(1e-10, m)

        y.append(r["spike_count"])
        mu.append(m)

    return poisson_nll(y, mu), len(y)


def fit_train(rows, l0, gl0, l2_map):
    best = None
    best_nll = float("inf")

    omega_grid = [i / 40 for i in range(-8, 49)]
    alpha_grid = [0.0, 0.4, 0.8, 1.2, 1.6]
    theta_grid = [0.4, 0.5, 0.6, 0.7]
    c_grid = [0.0, 0.2, 0.4, 0.6, 0.8]

    for w in omega_grid:
        for a in alpha_grid:
            for th in theta_grid:
                for c in c_grid:
                    nll, _ = nll_for_split(rows, "train", l0, gl0, w, a, th, c, l2_map)
                    if nll < best_nll:
                        best_nll = nll
                        best = (w, a, th, c)

    null_nll, _ = nll_for_split(rows, "train", l0, gl0, 0.0, 0.0, 0.6, 0.0, l2_map)
    lr = 2 * (null_nll - best_nll)

    return {
        "omega": best[0],
        "alpha": best[1],
        "theta": best[2],
        "c_fric": best[3],
        "train_nll": best_nll,
        "null_nll": null_nll,
        "lr": lr,
    }


def approx_p_omega_gt_0(rows, l0, gl0, fit, l2_map):
    grid = [i / 40 for i in range(-8, 49)]
    lls = []
    for w in grid:
        nll, _ = nll_for_split(rows, "train", l0, gl0, w, fit["alpha"], fit["theta"], fit["c_fric"], l2_map)
        lls.append(-nll)
    m = max(lls)
    ws = [math.exp(x - m) for x in lls]
    z = sum(ws)
    ps = [w / z for w in ws]
    ppos = sum(p for g, p in zip(grid, ps) if g > 0)
    mean = sum(g * p for g, p in zip(grid, ps))
    return mean, ppos


def main():
    rows = load_rows(DATA_PATH)
    prepare(rows)
    l0, gl0 = estimate_baseline(rows)
    l2_map = build_l2_state(rows)

    fit = fit_train(rows, l0, gl0, l2_map)
    om, ppos = approx_p_omega_gt_0(rows, l0, gl0, fit, l2_map)

    v_hat, n_v = nll_for_split(rows, "valid", l0, gl0, fit["omega"], fit["alpha"], fit["theta"], fit["c_fric"], l2_map)
    t_hat, n_t = nll_for_split(rows, "test", l0, gl0, fit["omega"], fit["alpha"], fit["theta"], fit["c_fric"], l2_map)

    v0, _ = nll_for_split(rows, "valid", l0, gl0, 0.0, 0.0, 0.6, 0.0, l2_map)
    t0, _ = nll_for_split(rows, "test", l0, gl0, 0.0, 0.0, 0.6, 0.0, l2_map)

    print("=== fit_real_pipeline_v7 summary ===")
    print(f"omega_hat={fit['omega']:.3f}, omega_mean≈{om:.3f}, P(omega>0)≈{ppos:.6f}")
    print(f"alpha_hat={fit['alpha']:.3f}, theta_hat={fit['theta']:.3f}")
    print(f"c_fric_hat={fit['c_fric']:.3f}  # Ψ_f coefficient")
    print(f"train_LR={fit['lr']:.3f}")
    print(f"valid_delta_nll={v0 - v_hat:.3f} (n={n_v})")
    print(f"test_delta_nll={t0 - t_hat:.3f} (n={n_t})")


if __name__ == "__main__":
    main()
