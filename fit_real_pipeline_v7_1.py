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
            rows.append({
                "spike_count": int(row["spike_count"]),
                "dt_sec": float(row["dt_sec"]),
                "t_sec": float(row["t_sec"]),
                "u_observer": float(row["u_observer"]),
                "circuit_id": row["circuit_id"],
                "session_id": row["session_id"],
            })
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
        r["block_id"] = f"{r['session_id']}_b{int(r['t_sec']//5.0):02d}"

    # zscore U within block
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
    pc = defaultdict(list)
    for r in rows:
        if r["split"] == "train":
            pc[r["circuit_id"]].append(r)
    l0 = {}
    for c, rs in pc.items():
        l0[c] = max(1e-6, sum(x["spike_count"] for x in rs) / sum(x["dt_sec"] for x in rs))
    gl0 = sum(l0.values()) / max(1, len(l0))
    return l0, gl0


def build_l2_and_psif(rows):
    # L2 rigidity proxy per block
    by_b = defaultdict(list)
    for r in rows:
        by_b[r["block_id"]].append(r["spike_count"])

    rig = {}
    for b, ys in by_b.items():
        mu = sum(ys) / len(ys)
        var = sum((y - mu) ** 2 for y in ys) / max(1, len(ys) - 1)
        rig[b] = mu / (1.0 + var)

    vals = list(rig.values())
    m = sum(vals) / len(vals)
    v = sum((x - m) ** 2 for x in vals) / max(1, len(vals) - 1)
    s = math.sqrt(v) if v > 1e-12 else 1.0
    for b in rig:
        rig[b] = (rig[b] - m) / s

    # v7.1 Ψ_f = | prediction error derivative | 
    # e_t = u_z - l2_rigidity(block),  Ψ_f(t)=|e_t-e_{t-1}| within each circuit
    by_c = defaultdict(list)
    for r in rows:
        by_c[r["circuit_id"]].append(r)
    for c in by_c:
        by_c[c].sort(key=lambda z: z["t_sec"])
        prev_e = None
        for r in by_c[c]:
            e = r["u_z"] - rig.get(r["block_id"], 0.0)
            if prev_e is None:
                r["psi_f"] = 0.0
            else:
                r["psi_f"] = abs(e - prev_e)
            prev_e = e


def nll_split(rows, split, l0, gl0, omega, alpha, theta, c_fric):
    y, mu = [], []
    for r in rows:
        if r["split"] != split:
            continue
        base = l0.get(r["circuit_id"], gl0)
        x_hat = sigmoid(0.8 * r["u_z"])
        gate = sigmoid(4.0 * (x_hat - theta))
        m = base * r["dt_sec"] * math.exp(omega * r["u_z"]) * math.exp(alpha * (gate - 0.5)) * math.exp(-c_fric * r["psi_f"])
        y.append(r["spike_count"])
        mu.append(max(1e-10, m))
    return poisson_nll(y, mu), len(y)


def fit(rows, l0, gl0):
    best, best_nll = None, float("inf")
    for w in [i / 40 for i in range(-8, 49)]:
        for a in [0.0, 0.4, 0.8, 1.2, 1.6]:
            for th in [0.4, 0.5, 0.6, 0.7]:
                for c in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
                    nll, _ = nll_split(rows, "train", l0, gl0, w, a, th, c)
                    if nll < best_nll:
                        best_nll = nll
                        best = (w, a, th, c)

    null_nll, _ = nll_split(rows, "train", l0, gl0, 0.0, 0.0, 0.6, 0.0)
    return {
        "omega": best[0],
        "alpha": best[1],
        "theta": best[2],
        "c_fric": best[3],
        "train_lr": 2 * (null_nll - best_nll),
    }


def posterior_omega(rows, l0, gl0, fit):
    grid = [i / 40 for i in range(-8, 49)]
    lls = []
    for w in grid:
        nll, _ = nll_split(rows, "train", l0, gl0, w, fit["alpha"], fit["theta"], fit["c_fric"])
        lls.append(-nll)
    m = max(lls)
    ws = [math.exp(x - m) for x in lls]
    z = sum(ws)
    ps = [w / z for w in ws]
    mean = sum(g * p for g, p in zip(grid, ps))
    ppos = sum(p for g, p in zip(grid, ps) if g > 0)
    return mean, ppos


def main():
    rows = load_rows(DATA_PATH)
    prepare(rows)
    l0, gl0 = estimate_baseline(rows)
    build_l2_and_psif(rows)

    fitp = fit(rows, l0, gl0)
    om, ppos = posterior_omega(rows, l0, gl0, fitp)

    v_hat, n_v = nll_split(rows, "valid", l0, gl0, fitp["omega"], fitp["alpha"], fitp["theta"], fitp["c_fric"])
    t_hat, n_t = nll_split(rows, "test", l0, gl0, fitp["omega"], fitp["alpha"], fitp["theta"], fitp["c_fric"])
    v0, _ = nll_split(rows, "valid", l0, gl0, 0.0, 0.0, 0.6, 0.0)
    t0, _ = nll_split(rows, "test", l0, gl0, 0.0, 0.0, 0.6, 0.0)

    print("=== fit_real_pipeline_v7.1 summary ===")
    print(f"omega_hat={fitp['omega']:.3f}, omega_mean≈{om:.3f}, P(omega>0)≈{ppos:.6f}")
    print(f"alpha_hat={fitp['alpha']:.3f}, theta_hat={fitp['theta']:.3f}")
    print(f"c_fric_hat={fitp['c_fric']:.3f}  # Ψ_f coefficient (hazard-like)")
    print(f"train_LR={fitp['train_lr']:.3f}")
    print(f"valid_delta_nll={v0 - v_hat:.3f} (n={n_v})")
    print(f"test_delta_nll={t0 - t_hat:.3f} (n={n_t})")


if __name__ == "__main__":
    main()
