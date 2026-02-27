import math
import random
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class CircuitParams:
    lambda_base: float   # baseline firing rate (Hz)
    alpha: float         # mTOR-gated increment (Hz)
    theta: float         # mTOR threshold
    k: float             # threshold sharpness
    a: float             # mTOR input gain
    b: float             # mTOR decay
    sigma_x: float       # mTOR noise scale


def logistic(z: float) -> float:
    return 1.0 / (1.0 + math.exp(-z))


def g_mtor(x: float, theta: float, k: float) -> float:
    return logistic(k * (x - theta))


def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


def poisson_sample(mean: float) -> int:
    # Knuth method, stable for small means (we use dt small => mean usually < 1)
    if mean <= 0:
        return 0
    L = math.exp(-mean)
    p = 1.0
    k = 0
    while p > L:
        k += 1
        p *= random.random()
    return k - 1


def simulate(
    T: float = 60.0,
    dt: float = 0.005,
    omega: float = 0.0,
    n_circuits: int = 3,
    seed: int = 42,
) -> Tuple[List[int], List[float], List[float]]:
    random.seed(seed)

    # Example fixed params per circuit (can be fitted later)
    ps = [
        CircuitParams(5.0, 20.0, 0.6, 10.0, 1.2, 0.9, 0.05),
        CircuitParams(6.0, 16.0, 0.5, 9.0, 1.0, 1.1, 0.05),
        CircuitParams(4.5, 18.0, 0.55, 11.0, 1.3, 1.0, 0.05),
    ][:n_circuits]

    x = [0.2 + 0.05 * i for i in range(n_circuits)]
    spikes = [0 for _ in range(n_circuits)]

    # Pre-set selective reality target weights: circuit 0 is preferred target
    target_w = [1.0, 0.2, -0.1][:n_circuits]

    # Collect lambda histories for mean/Fano diagnostics
    rate_hist = [[] for _ in range(n_circuits)]

    steps = int(T / dt)
    for t_idx in range(steps):
        t = t_idx * dt

        # Shared upstream modulation (toy input)
        s_t = 0.7 + 0.25 * math.sin(2.0 * math.pi * 0.8 * t)

        for i, p in enumerate(ps):
            # mTOR dynamics: x_dot = a*s - b*x + noise
            noise = p.sigma_x * math.sqrt(dt) * random.gauss(0.0, 1.0)
            x[i] += dt * (p.a * s_t - p.b * x[i]) + noise
            x[i] = clamp(x[i], 0.0, 2.0)

            lam0 = p.lambda_base + p.alpha * g_mtor(x[i], p.theta, p.k)

            # U_i: selective reality utility (simplified static preference)
            U_i = target_w[i]
            lamw = lam0 * math.exp(omega * U_i)

            rate_hist[i].append(lamw)
            mean_count = lamw * dt
            spikes[i] += poisson_sample(mean_count)

    # Return spike counts + mean rates + fano proxies from binned process
    mean_rates = [sum(r) / len(r) for r in rate_hist]

    # Crude Fano proxy via 100ms bins
    bin_size = int(0.1 / dt)
    fano = []
    for i, p in enumerate(ps):
        # Re-simulate counts from stored rate for binning statistics
        bins = []
        c = 0
        k = 0
        for lam in rate_hist[i]:
            c += poisson_sample(lam * dt)
            k += 1
            if k == bin_size:
                bins.append(c)
                c = 0
                k = 0
        if len(bins) > 1:
            mu = sum(bins) / len(bins)
            var = sum((b - mu) ** 2 for b in bins) / (len(bins) - 1)
            fano.append(var / mu if mu > 1e-9 else float('nan'))
        else:
            fano.append(float('nan'))

    return spikes, mean_rates, fano


def run_sweep(omegas=(0.0, 0.4, 0.8, 1.2)):
    print("omega\tspikes(c0,c1,c2)\tmean_rate(c0,c1,c2)\tfano(c0,c1,c2)")
    for w in omegas:
        spikes, means, fano = simulate(omega=w)
        print(
            f"{w:.2f}\t{tuple(spikes)}\t"
            f"{tuple(round(m,3) for m in means)}\t"
            f"{tuple(round(f,3) for f in fano)}"
        )


if __name__ == "__main__":
    run_sweep()
