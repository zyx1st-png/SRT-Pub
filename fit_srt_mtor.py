import math
import random
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class CircuitParams:
    lambda_base: float
    alpha: float
    theta: float
    k: float
    a: float
    b: float
    sigma_x: float


def logistic(z: float) -> float:
    return 1.0 / (1.0 + math.exp(-z))


def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


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


def simulate_dataset(
    T: float = 30.0,
    dt: float = 0.01,
    omega_true: float = 0.8,
    seed: int = 7,
) -> Tuple[List[float], List[int], List[float], CircuitParams, float]:
    """
    Return:
      x_series: mTOR state trajectory for circuit-0
      y_series: spike counts per dt for circuit-0
      U_series: utility value per dt (time-varying, known regressor)
      true_params: ground truth params for circuit-0
      omega_true
    """
    random.seed(seed)

    p = CircuitParams(
        lambda_base=5.0,
        alpha=20.0,
        theta=0.6,
        k=10.0,
        a=1.2,
        b=0.9,
        sigma_x=0.05,
    )

    x = 0.25
    steps = int(T / dt)

    x_series, y_series, U_series = [], [], []

    for t_idx in range(steps):
        t = t_idx * dt

        # mTOR drive
        s_t = 0.7 + 0.25 * math.sin(2.0 * math.pi * 0.8 * t)
        noise = p.sigma_x * math.sqrt(dt) * random.gauss(0.0, 1.0)
        x += dt * (p.a * s_t - p.b * x) + noise
        x = clamp(x, 0.0, 2.0)

        # time-varying selective utility (observable design signal)
        U_t = 0.8 + 0.2 * math.sin(2.0 * math.pi * 0.2 * t + 0.3)

        g = logistic(p.k * (x - p.theta))
        lam0 = p.lambda_base + p.alpha * g
        lam = lam0 * math.exp(omega_true * U_t)

        y = poisson_sample(lam * dt)

        x_series.append(x)
        y_series.append(y)
        U_series.append(U_t)

    return x_series, y_series, U_series, p, omega_true


def nll_poisson(y: List[int], mu: List[float]) -> float:
    # negative log-likelihood up to constant term log(y!)
    eps = 1e-12
    return sum(m - yi * math.log(m + eps) for yi, m in zip(y, mu))


def fit_grid_mle(
    x: List[float],
    y: List[int],
    U: List[float],
    dt: float,
):
    # Tight but practical grids around plausible biology + previous sim scale
    lambda_base_grid = [2.0, 3.5, 5.0, 6.5, 8.0]
    alpha_grid = [10.0, 14.0, 18.0, 22.0, 26.0]
    theta_grid = [0.45, 0.5, 0.55, 0.6, 0.65, 0.7]
    omega_grid = [i / 20 for i in range(-2, 31)]  # -0.1 .. 1.5

    k_fixed = 10.0

    best = None
    best_nll = float("inf")

    for lb in lambda_base_grid:
        for a in alpha_grid:
            for th in theta_grid:
                g_vals = [logistic(k_fixed * (xx - th)) for xx in x]
                lam0_vals = [lb + a * g for g in g_vals]

                for w in omega_grid:
                    mu = [max(1e-10, lam0 * math.exp(w * u) * dt) for lam0, u in zip(lam0_vals, U)]
                    nll = nll_poisson(y, mu)
                    if nll < best_nll:
                        best_nll = nll
                        best = (lb, a, th, w)

    return {
        "lambda_base": best[0],
        "alpha": best[1],
        "theta": best[2],
        "omega": best[3],
        "nll": best_nll,
    }


def likelihood_ratio_test_for_omega(
    x: List[float],
    y: List[int],
    U: List[float],
    dt: float,
    lambda_base: float,
    alpha: float,
    theta: float,
    omega_hat: float,
) -> Tuple[float, float, float]:
    """
    Compare H0: omega=0 vs H1: omega=omega_hat with other params fixed.
    Return (nll_h0, nll_h1, LR_stat)
    """
    k_fixed = 10.0
    g_vals = [logistic(k_fixed * (xx - theta)) for xx in x]
    lam0_vals = [lambda_base + alpha * g for g in g_vals]

    mu0 = [max(1e-10, lam0 * math.exp(0.0 * u) * dt) for lam0, u in zip(lam0_vals, U)]
    mu1 = [max(1e-10, lam0 * math.exp(omega_hat * u) * dt) for lam0, u in zip(lam0_vals, U)]

    nll0 = nll_poisson(y, mu0)
    nll1 = nll_poisson(y, mu1)

    # LR = 2*(LL1-LL0) = 2*( -nll1 - (-nll0) ) = 2*(nll0 - nll1)
    lr = 2.0 * (nll0 - nll1)
    return nll0, nll1, lr


def main():
    T, dt, omega_true = 30.0, 0.01, 0.8
    x, y, U, p_true, w_true = simulate_dataset(T=T, dt=dt, omega_true=omega_true)

    fit = fit_grid_mle(x, y, U, dt)

    nll0, nll1, lr = likelihood_ratio_test_for_omega(
        x,
        y,
        U,
        dt,
        fit["lambda_base"],
        fit["alpha"],
        fit["theta"],
        fit["omega"],
    )

    total_spikes = sum(y)
    rate_hz = total_spikes / T

    print("=== SRT-mTOR MLE Recovery (synthetic) ===")
    print(f"T={T}s, dt={dt}s, total_spikes={total_spikes}, mean_rate={rate_hz:.3f} Hz")
    print("-- True params --")
    print(
        f"lambda_base={p_true.lambda_base}, alpha={p_true.alpha}, theta={p_true.theta}, omega={w_true}"
    )
    print("-- Fitted params (grid MLE) --")
    print(
        f"lambda_base={fit['lambda_base']}, alpha={fit['alpha']}, theta={fit['theta']}, omega={fit['omega']}, nll={fit['nll']:.3f}"
    )
    print("-- Omega significance (LRT, rough) --")
    print(f"nll(omega=0)={nll0:.3f}, nll(omega=hat)={nll1:.3f}, LR={lr:.3f}")
    print("Interpretation: larger LR => stronger evidence omega != 0.")


if __name__ == "__main__":
    main()
