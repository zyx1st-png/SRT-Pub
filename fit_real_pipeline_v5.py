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
            row["dt_sec"] = float(row["dt_sec"])
            row["t_sec"] = float(row["t_sec"])
            row["u_observer"] = float(row["u_observer"])
            row["spike_count"] = int(row["spike_count"]) if row["spike_count"] != "" else None
            row["x_mtor_proxy"] = float(row["x_mtor_proxy"]) if row["x_mtor_proxy"] != "" else None
            rows.append(row)
    return rows


def prep_spike(rows):
    srows = [r for r in rows if r["spike_count"] is not None]

    circuits = sorted({r["circuit_id"] for r in srows})
    n = len(circuits)
    n_train = max(1, int(0.7 * n))
    n_valid = max(1, int(0.15 * n))
    train_c = set(circuits[:n_train])
    valid_c = set(circuits[n_train:n_train + n_valid])

    for r in srows:
        c = r["circuit_id"]
        if c in train_c:
            r["split"] = "train"
        elif c in valid_c:
            r["split"] = "valid"
        else:
            r["split"] = "test"
        b = int(r["t_sec"] // 5.0)
        r["block_id"] = f"{r['session_id']}_b{b:02d}"

    # zscore U within block
    bu = defaultdict(list)
    for r in srows:
        bu[r["block_id"]].append(r["u_observer"])
    bstats = {}
    for b, us in bu.items():
        m = sum(us) / len(us)
        v = sum((u - m) ** 2 for u in us) / max(1, len(us) - 1)
        s = math.sqrt(v) if v > 1e-12 else 1.0
        bstats[b] = (m, s)
    for r in srows:
        m, s = bstats[r["block_id"]]
        r["u_z"] = (r["u_observer"] - m) / s

    return srows


def estimate_omics_prior(rows):
    omics = [r for r in rows if r["spike_count"] is None and r["x_mtor_proxy"] is not None]
    if not omics:
        return (0.6, 0.12), (1.0, 0.5)
    xs = [r["x_mtor_proxy"] for r in omics]
    mx = sum(xs) / len(xs)
    vx = sum((x - mx) ** 2 for x in xs) / max(1, len(xs) - 1)
    sx = math.sqrt(max(vx, 1e-6))

    mu_theta = max(0.2, min(0.9, 1.0 - 0.7 * mx))
    sd_theta = max(0.05, min(0.25, 0.7 * sx))

    byc = defaultdict(list)
    for r in omics:
        byc[r["condition"]].append(r["x_mtor_proxy"])
    cms = sorted((sum(v) / len(v) for v in byc.values()), reverse=True)
    contrast = cms[0] - cms[-1] if len(cms) >= 2 else 0.15
    mu_alpha = max(0.2, min(2.0, 0.5 + 2.5 * contrast))
    sd_alpha = 0.4
    return (mu_theta, sd_theta), (mu_alpha, sd_alpha)


def baseline_by_circuit(srows):
    pc = defaultdict(list)
    for r in srows:
        if r["split"] == "train":
            pc[r["circuit_id"]].append(r)
    l0 = {}
    for c, rs in pc.items():
        l0[c] = max(1e-6, sum(x["spike_count"] for x in rs) / sum(x["dt_sec"] for x in rs))
    gl0 = sum(l0.values()) / max(1, len(l0))
    return l0, gl0


def intensity(r, l0c, omega_b, theta_c, alpha_c, k=4.0):
    x_hat = sigmoid(0.8 * r["u_z"])  # bridge proxy
    gate = sigmoid(k * (x_hat - theta_c))
    return max(1e-10, l0c * r["dt_sec"] * math.exp(omega_b * r["u_z"]) * math.exp(alpha_c * (gate - 0.5)))


def fit_hier_map(srows, l0, gl0, theta_prior, alpha_prior, n_iter=5):
    train = [r for r in srows if r["split"] == "train"]
    circuits = sorted({r["circuit_id"] for r in train})
    blocks = sorted({r["block_id"] for r in train})

    # init from priors
    mu_theta, sd_theta = theta_prior
    mu_alpha, sd_alpha = alpha_prior
    mu_omega, sd_omega = 0.15, 0.25

    theta_c = {c: mu_theta for c in circuits}
    alpha_c = {c: mu_alpha for c in circuits}
    omega_b = {b: mu_omega for b in blocks}

    by_c = defaultdict(list)
    by_b = defaultdict(list)
    for r in train:
        by_c[r["circuit_id"]].append(r)
        by_b[r["block_id"]].append(r)

    theta_grid = [0.30, 0.40, 0.50, 0.60, 0.70, 0.80]
    alpha_grid = [0.0, 0.4, 0.8, 1.2, 1.6, 2.0]
    omega_grid = [i / 40 for i in range(-8, 49)]  # -0.2..1.2

    for _ in range(n_iter):
        # update omega per block
        for b, rs in by_b.items():
            best_w, best_obj = omega_b[b], float("inf")
            for w in omega_grid:
                y, mu = [], []
                for r in rs:
                    c = r["circuit_id"]
                    l0c = l0.get(c, gl0)
                    mu.append(intensity(r, l0c, w, theta_c[c], alpha_c[c]))
                    y.append(r["spike_count"])
                nll = poisson_nll(y, mu)
                pen = 0.5 * ((w - mu_omega) / sd_omega) ** 2
                obj = nll + pen
                if obj < best_obj:
                    best_obj, best_w = obj, w
            omega_b[b] = best_w

        # update theta/alpha per circuit
        for c, rs in by_c.items():
            best = (theta_c[c], alpha_c[c])
            best_obj = float("inf")
            for th in theta_grid:
                for a in alpha_grid:
                    y, mu = [], []
                    for r in rs:
                        b = r["block_id"]
                        l0c = l0.get(c, gl0)
                        mu.append(intensity(r, l0c, omega_b[b], th, a))
                        y.append(r["spike_count"])
                    nll = poisson_nll(y, mu)
                    pen = 0.5 * ((th - mu_theta) / sd_theta) ** 2 + 0.5 * ((a - mu_alpha) / sd_alpha) ** 2
                    obj = nll + pen
                    if obj < best_obj:
                        best_obj = obj
                        best = (th, a)
            theta_c[c], alpha_c[c] = best

        # empirical-bayes hyper updates
        mu_omega = sum(omega_b.values()) / len(omega_b)
        sd_omega = math.sqrt(max(1e-4, sum((w - mu_omega) ** 2 for w in omega_b.values()) / max(1, len(omega_b) - 1)))
        sd_omega = max(0.08, min(0.6, sd_omega))

        mu_theta = sum(theta_c.values()) / len(theta_c)
        sd_theta = math.sqrt(max(1e-4, sum((t - mu_theta) ** 2 for t in theta_c.values()) / max(1, len(theta_c) - 1)))
        sd_theta = max(0.05, min(0.3, sd_theta))

        mu_alpha = sum(alpha_c.values()) / len(alpha_c)
        sd_alpha = math.sqrt(max(1e-4, sum((a - mu_alpha) ** 2 for a in alpha_c.values()) / max(1, len(alpha_c) - 1)))
        sd_alpha = max(0.12, min(0.8, sd_alpha))

    return {
        "theta_c": theta_c,
        "alpha_c": alpha_c,
        "omega_b": omega_b,
        "mu_omega": mu_omega,
        "sd_omega": sd_omega,
        "mu_theta": mu_theta,
        "sd_theta": sd_theta,
        "mu_alpha": mu_alpha,
        "sd_alpha": sd_alpha,
    }


def eval_delta_nll(srows, l0, gl0, pars, split):
    rs = [r for r in srows if r["split"] == split]
    y_hat, mu_hat = [], []
    y0, mu0 = [], []
    for r in rs:
        c = r["circuit_id"]
        b = r["block_id"]
        l0c = l0.get(c, gl0)

        th = pars["theta_c"].get(c, pars["mu_theta"])
        a = pars["alpha_c"].get(c, pars["mu_alpha"])
        w = pars["omega_b"].get(b, pars["mu_omega"])

        y_hat.append(r["spike_count"])
        mu_hat.append(intensity(r, l0c, w, th, a))

        # null: no SRT + no threshold modulation
        y0.append(r["spike_count"])
        mu0.append(max(1e-10, l0c * r["dt_sec"]))

    return poisson_nll(y0, mu0) - poisson_nll(y_hat, mu_hat), len(rs)


def train_lr(srows, l0, gl0, pars):
    rs = [r for r in srows if r["split"] == "train"]
    y_hat, mu_hat = [], []
    y0, mu0 = [], []
    for r in rs:
        c = r["circuit_id"]
        b = r["block_id"]
        l0c = l0.get(c, gl0)

        th = pars["theta_c"].get(c, pars["mu_theta"])
        a = pars["alpha_c"].get(c, pars["mu_alpha"])
        w = pars["omega_b"].get(b, pars["mu_omega"])

        y_hat.append(r["spike_count"])
        mu_hat.append(intensity(r, l0c, w, th, a))

        y0.append(r["spike_count"])
        mu0.append(max(1e-10, l0c * r["dt_sec"]))

    nll_hat = poisson_nll(y_hat, mu_hat)
    nll0 = poisson_nll(y0, mu0)
    return 2 * (nll0 - nll_hat)


def p_mu_omega_gt_0(mu, sd):
    z = mu / max(sd, 1e-9)
    # Phi(z)
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def main():
    rows = load_rows(DATA_PATH)
    srows = prep_spike(rows)

    theta_prior, alpha_prior = estimate_omics_prior(rows)
    l0, gl0 = baseline_by_circuit(srows)

    pars = fit_hier_map(srows, l0, gl0, theta_prior, alpha_prior, n_iter=5)

    lr = train_lr(srows, l0, gl0, pars)
    dv, nv = eval_delta_nll(srows, l0, gl0, pars, "valid")
    dt, nt = eval_delta_nll(srows, l0, gl0, pars, "test")
    ppos = p_mu_omega_gt_0(pars["mu_omega"], pars["sd_omega"])

    print("=== fit_real_pipeline_v5 summary ===")
    print(f"mu_omega={pars['mu_omega']:.3f}, sd_omega={pars['sd_omega']:.3f}, P(mu_omega>0)≈{ppos:.6f}")
    print(f"mu_theta={pars['mu_theta']:.3f}, sd_theta={pars['sd_theta']:.3f}")
    print(f"mu_alpha={pars['mu_alpha']:.3f}, sd_alpha={pars['sd_alpha']:.3f}")
    print(f"train_LR={lr:.3f}")
    print(f"valid_delta_nll={dv:.3f} (n={nv})")
    print(f"test_delta_nll={dt:.3f} (n={nt})")


if __name__ == "__main__":
    main()
