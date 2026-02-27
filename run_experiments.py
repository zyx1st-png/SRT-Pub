import csv
import math
import random
from collections import defaultdict


def logistic(z: float) -> float:
    return 1.0 / (1.0 + math.exp(-z))


def poisson_sample(mean: float) -> int:
    if mean <= 0:
        return 0
    L = math.exp(-mean)
    p = 1.0
    k = 0
    while p > L:
        k += 1
        p *= random.random()
    return k - 1


def mutual_information_discrete(xs, ys):
    # MI(X;Y) in nats
    n = len(xs)
    px = defaultdict(int)
    py = defaultdict(int)
    pxy = defaultdict(int)
    for x, y in zip(xs, ys):
        px[x] += 1
        py[y] += 1
        pxy[(x, y)] += 1

    mi = 0.0
    for (x, y), c in pxy.items():
        pxy_v = c / n
        px_v = px[x] / n
        py_v = py[y] / n
        mi += pxy_v * math.log(pxy_v / (px_v * py_v + 1e-12) + 1e-12)
    return mi


def simulate_one(T=30.0, dt=0.01, omega=0.0, theta=0.6, sigma=0.05, seed=0):
    random.seed(seed)

    # fixed params
    lb = 5.0
    alpha = 20.0
    k = 10.0
    a = 1.2
    b = 0.9

    x = 0.25
    steps = int(T / dt)

    total_spike = 0
    y_series = []
    Ub_series = []

    for t_idx in range(steps):
        t = t_idx * dt
        s_t = 0.7 + 0.25 * math.sin(2.0 * math.pi * 0.8 * t)
        x += dt * (a * s_t - b * x) + sigma * math.sqrt(dt) * random.gauss(0.0, 1.0)
        x = max(0.0, min(2.0, x))

        U = 0.8 + 0.2 * math.sin(2.0 * math.pi * 0.2 * t + 0.3)
        Ub = 0 if U < 0.8 else 1

        lam0 = lb + alpha * logistic(k * (x - theta))
        lam = lam0 * math.exp(omega * U)
        y = poisson_sample(lam * dt)

        total_spike += y
        y_series.append(y)
        Ub_series.append(Ub)

    rate_hz = total_spike / T
    mi = mutual_information_discrete(y_series, Ub_series)
    return rate_hz, mi


def main():
    omegas = [0.0, 0.2, 0.4, 0.8, 1.2]
    thetas = [0.5, 0.6, 0.7]
    sigmas = [0.02, 0.05, 0.1]

    out_csv = "experiments_srt_mtor.csv"
    with open(out_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["omega", "theta", "sigma", "mean_rate_hz", "mi_nats", "delta_mi_vs_omega0"])

        # baseline MI map for delta
        baseline = {}
        for th in thetas:
            for sg in sigmas:
                rs = []
                mis = []
                for sd in [1, 2, 3, 4, 5]:
                    r, m = simulate_one(omega=0.0, theta=th, sigma=sg, seed=sd)
                    rs.append(r)
                    mis.append(m)
                baseline[(th, sg)] = (sum(rs) / len(rs), sum(mis) / len(mis))

        for om in omegas:
            for th in thetas:
                for sg in sigmas:
                    rs = []
                    mis = []
                    for sd in [1, 2, 3, 4, 5]:
                        r, m = simulate_one(omega=om, theta=th, sigma=sg, seed=sd)
                        rs.append(r)
                        mis.append(m)
                    r_mean = sum(rs) / len(rs)
                    mi_mean = sum(mis) / len(mis)
                    dmi = mi_mean - baseline[(th, sg)][1]
                    w.writerow([om, th, sg, round(r_mean, 6), round(mi_mean, 6), round(dmi, 6)])

    print(f"wrote {out_csv}")
    print("done: omega/theta/sigma sweep with MI diagnostics")


if __name__ == "__main__":
    main()
