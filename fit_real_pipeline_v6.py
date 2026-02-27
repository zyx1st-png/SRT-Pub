import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "unified_srt_mtor.csv"


def load_train_rows(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            if row["spike_count"] == "":
                continue
            y = int(row["spike_count"])
            dt = float(row["dt_sec"])
            u = float(row["u_observer"])
            rows.append((y, dt, u))
    return rows


def aggregate(rows):
    # aggregate to speed MCMC
    ys = [y for y, _, _ in rows]
    dts = [dt for _, dt, _ in rows]
    us = [u for _, _, u in rows]
    # normalize u
    mu_u = sum(us) / len(us)
    var_u = sum((u - mu_u) ** 2 for u in us) / max(1, len(us) - 1)
    sd_u = math.sqrt(var_u) if var_u > 1e-12 else 1.0
    uz = [(u - mu_u) / sd_u for u in us]
    return ys, dts, uz


def logpost(omega, ys, dts, uz, lam0):
    # prior omega ~ N(0, 0.5^2)
    lp = -0.5 * (omega / 0.5) ** 2
    for y, dt, u in zip(ys, dts, uz):
        mu = max(1e-12, lam0 * dt * math.exp(omega * u))
        lp += y * math.log(mu) - mu
    return lp


def rw_mh(ys, dts, uz, lam0, n=24000, burn=6000, step=0.09):
    import random
    w = 0.0
    lp = logpost(w, ys, dts, uz, lam0)
    out = []
    acc = 0
    for i in range(n):
        wp = random.gauss(w, step)
        lpp = logpost(wp, ys, dts, uz, lam0)
        if math.log(random.random()) < (lpp - lp):
            w, lp = wp, lpp
            acc += 1
        if i >= burn:
            out.append(w)
    return out, acc / n


def summary(samples):
    n = len(samples)
    mean = sum(samples) / n
    xs = sorted(samples)
    lo = xs[int(0.025 * n)]
    hi = xs[int(0.975 * n)]
    ppos = sum(1 for x in samples if x > 0) / n
    # ESS rough via lag-1 autocorr on chain order
    m = mean
    v = sum((x - m) ** 2 for x in samples) / (n - 1)
    if v <= 1e-12:
        ess = float(n)
    else:
        c1 = sum((samples[i] - m) * (samples[i + 1] - m) for i in range(n - 1)) / (n - 1)
        rho1 = c1 / v
        ess = n * (1 - rho1) / (1 + rho1) if (1 + rho1) > 1e-8 else float(n)
        ess = max(1.0, min(float(n), ess))
    return mean, lo, hi, ppos, ess


def main():
    rows = load_train_rows(DATA_PATH)
    ys, dts, uz = aggregate(rows)
    lam0 = sum(ys) / max(1e-9, sum(dts))

    samples, acc = rw_mh(ys, dts, uz, lam0)
    mean, lo, hi, ppos, ess = summary(samples)

    print("=== fit_real_pipeline_v6 (MCMC fallback) ===")
    print(f"n_obs={len(ys)}, lambda0={lam0:.4f}")
    print(f"omega mean={mean:.4f}, 95%CI=[{lo:.4f},{hi:.4f}], P(omega>0)={ppos:.4f}")
    print(f"acceptance={acc:.3f}, ESS~{ess:.1f}")


if __name__ == '__main__':
    main()
