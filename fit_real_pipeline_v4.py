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


def load_all_rows(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            row["dt_sec"] = float(row["dt_sec"])
            row["t_sec"] = float(row["t_sec"])
            row["u_observer"] = float(row["u_observer"])
            if row["spike_count"] != "":
                row["spike_count"] = int(row["spike_count"])
            else:
                row["spike_count"] = None
            if row["x_mtor_proxy"] != "":
                row["x_mtor_proxy"] = float(row["x_mtor_proxy"])
            else:
                row["x_mtor_proxy"] = None
            rows.append(row)
    return rows


def prepare_spike_rows(rows):
    srows = [r for r in rows if r["spike_count"] is not None]

    # grouped split by circuit
    circuits = sorted({r["circuit_id"] for r in srows})
    n = len(circuits)
    n_train = max(1, int(0.7 * n))
    n_valid = max(1, int(0.15 * n))
    train_c = set(circuits[:n_train])
    valid_c = set(circuits[n_train:n_train + n_valid])

    for r in srows:
        c = r["circuit_id"]
        if c in train_c:
            r["split_v4"] = "train"
        elif c in valid_c:
            r["split_v4"] = "valid"
        else:
            r["split_v4"] = "test"

        # session block
        b = int(r["t_sec"] // 5.0)
        r["block_id"] = f"{r['session_id']}_b{b:02d}"

    # z-score U within block
    by_b = defaultdict(list)
    for r in srows:
        by_b[r["block_id"]].append(r["u_observer"])
    stats = {}
    for b, us in by_b.items():
        mu = sum(us) / len(us)
        var = sum((u - mu) ** 2 for u in us) / max(1, len(us) - 1)
        sd = math.sqrt(var) if var > 1e-12 else 1.0
        stats[b] = (mu, sd)
    for r in srows:
        mu, sd = stats[r["block_id"]]
        r["u_z"] = (r["u_observer"] - mu) / sd

    return srows


def estimate_omics_priors(rows):
    omics = [r for r in rows if r["x_mtor_proxy"] is not None and r["spike_count"] is None]
    if not omics:
        return 0.6, 0.15, 1.0, 0.5

    xs = [r["x_mtor_proxy"] for r in omics]
    mu_x = sum(xs) / len(xs)
    var_x = sum((x - mu_x) ** 2 for x in xs) / max(1, len(xs) - 1)
    sd_x = math.sqrt(max(var_x, 1e-6))

    # heuristic mapping: higher mTOR proxy -> lower threshold theta
    mu_theta = max(0.2, min(0.9, 1.0 - 0.7 * mu_x))
    sd_theta = max(0.05, min(0.25, 0.7 * sd_x))

    # alpha prior from condition contrast
    by_cond = defaultdict(list)
    for r in omics:
        by_cond[r["condition"]].append(r["x_mtor_proxy"])
    cond_means = sorted((sum(v)/len(v) for v in by_cond.values()), reverse=True)
    contrast = (cond_means[0] - cond_means[-1]) if len(cond_means) >= 2 else 0.1
    mu_alpha = max(0.2, min(2.0, 0.5 + 2.5 * contrast))
    sd_alpha = 0.4

    return mu_theta, sd_theta, mu_alpha, sd_alpha


def estimate_baseline(srows):
    per_c = defaultdict(list)
    for r in srows:
        if r["split_v4"] == "train":
            per_c[r["circuit_id"]].append(r)
    l0 = {}
    for c, rs in per_c.items():
        s = sum(x["spike_count"] for x in rs)
        t = sum(x["dt_sec"] for x in rs)
        l0[c] = max(1e-6, s / t)
    gl0 = sum(l0.values()) / max(1, len(l0))
    return l0, gl0


def nll_split(srows, split, l0, gl0, omega, theta, alpha, k=4.0):
    y, mu = [], []
    for r in srows:
        if r["split_v4"] != split:
            continue
        base = l0.get(r["circuit_id"], gl0)

        # latent mTOR proxy from normalized observer (bridge until real x(t) arrives)
        x_hat = sigmoid(0.8 * r["u_z"])  # in [0,1]
        gate = sigmoid(k * (x_hat - theta))

        # multiplicative model: SRT term + mTOR-threshold modulation
        m = base * r["dt_sec"] * math.exp(omega * r["u_z"]) * math.exp(alpha * (gate - 0.5))
        m = max(1e-10, m)

        y.append(r["spike_count"])
        mu.append(m)
    return poisson_nll(y, mu), len(y)


def fit_train(srows, l0, gl0, theta_prior, alpha_prior):
    mu_theta, sd_theta = theta_prior
    mu_alpha, sd_alpha = alpha_prior

    best = None
    best_obj = float("inf")

    omega_grid = [i / 40 for i in range(-8, 49)]   # -0.2..1.2
    theta_grid = [0.30, 0.40, 0.50, 0.60, 0.70, 0.80]
    alpha_grid = [0.0, 0.4, 0.8, 1.2, 1.6, 2.0]

    for w in omega_grid:
        for th in theta_grid:
            for a in alpha_grid:
                nll, _ = nll_split(srows, "train", l0, gl0, w, th, a)
                pen = 0.5 * ((th - mu_theta) / sd_theta) ** 2 + 0.5 * ((a - mu_alpha) / sd_alpha) ** 2
                obj = nll + pen
                if obj < best_obj:
                    best_obj = obj
                    best = (w, th, a, nll, pen)

    # null model (omega=0, alpha=0) with theta fixed to prior mean
    nll0, _ = nll_split(srows, "train", l0, gl0, 0.0, mu_theta, 0.0)
    lr = 2 * (nll0 - best[3])

    return {
        "omega_hat": best[0],
        "theta_hat": best[1],
        "alpha_hat": best[2],
        "train_nll_hat": best[3],
        "train_penalty": best[4],
        "train_nll_null": nll0,
        "train_lr": lr,
    }


def approx_p_omega_gt_0(srows, l0, gl0, theta_hat, alpha_hat):
    grid = [i / 40 for i in range(-8, 49)]
    lls = []
    for w in grid:
        nll, _ = nll_split(srows, "train", l0, gl0, w, theta_hat, alpha_hat)
        lls.append(-nll)
    m = max(lls)
    ws = [math.exp(x - m) for x in lls]
    z = sum(ws)
    ps = [w / z for w in ws]
    ppos = sum(p for g, p in zip(grid, ps) if g > 0)
    mean = sum(g * p for g, p in zip(grid, ps))
    return mean, ppos


def main():
    rows = load_all_rows(DATA_PATH)
    srows = prepare_spike_rows(rows)

    mu_theta, sd_theta, mu_alpha, sd_alpha = estimate_omics_priors(rows)
    l0, gl0 = estimate_baseline(srows)

    fit = fit_train(srows, l0, gl0, (mu_theta, sd_theta), (mu_alpha, sd_alpha))

    v_hat, n_v = nll_split(srows, "valid", l0, gl0, fit["omega_hat"], fit["theta_hat"], fit["alpha_hat"])
    t_hat, n_t = nll_split(srows, "test", l0, gl0, fit["omega_hat"], fit["theta_hat"], fit["alpha_hat"])

    v0, _ = nll_split(srows, "valid", l0, gl0, 0.0, mu_theta, 0.0)
    t0, _ = nll_split(srows, "test", l0, gl0, 0.0, mu_theta, 0.0)

    om, ppos = approx_p_omega_gt_0(srows, l0, gl0, fit["theta_hat"], fit["alpha_hat"])

    print("=== fit_real_pipeline_v4 summary ===")
    print(f"omics prior: theta~N({mu_theta:.3f},{sd_theta:.3f}), alpha~N({mu_alpha:.3f},{sd_alpha:.3f})")
    print(f"omega_hat: {fit['omega_hat']:.3f}")
    print(f"theta_hat: {fit['theta_hat']:.3f}")
    print(f"alpha_hat: {fit['alpha_hat']:.3f}")
    print(f"omega_mean≈ {om:.3f}, P(omega>0)≈ {ppos:.6f}")
    print(f"train_LR: {fit['train_lr']:.3f}")
    print(f"valid_delta_nll: {v0 - v_hat:.3f} (n={n_v})")
    print(f"test_delta_nll: {t0 - t_hat:.3f} (n={n_t})")


if __name__ == "__main__":
    main()
