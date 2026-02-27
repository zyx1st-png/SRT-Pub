import math
import random
from dataclasses import dataclass
from typing import List, Dict, Tuple


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


def simulate_condition(
    T: float,
    dt: float,
    omega_true: float,
    drive_gain: float,
    seed: int,
) -> Dict[str, List[float]]:
    random.seed(seed)

    p = CircuitParams(5.0, 20.0, 0.6, 10.0, 1.2, 0.9, 0.05)
    x = 0.25
    steps = int(T / dt)

    x_series, y_series, U_series = [], [], []

    for t_idx in range(steps):
        t = t_idx * dt
        s_t = drive_gain * (0.7 + 0.25 * math.sin(2.0 * math.pi * 0.8 * t))
        noise = p.sigma_x * math.sqrt(dt) * random.gauss(0.0, 1.0)
        x += dt * (p.a * s_t - p.b * x) + noise
        x = clamp(x, 0.0, 2.0)

        # observable selective utility regressor
        U_t = 0.8 + 0.2 * math.sin(2.0 * math.pi * 0.2 * t + 0.3)

        g = logistic(p.k * (x - p.theta))
        lam0 = p.lambda_base + p.alpha * g
        lam = lam0 * math.exp(omega_true * U_t)
        y = poisson_sample(lam * dt)

        x_series.append(x)
        y_series.append(y)
        U_series.append(U_t)

    return {"x": x_series, "y": y_series, "U": U_series}


def log_likelihood(dataset: Dict[str, List[float]], dt: float, lb: float, alpha: float, theta: float, omega: float, k: float = 10.0) -> float:
    x = dataset["x"]
    y = dataset["y"]
    U = dataset["U"]

    ll = 0.0
    eps = 1e-12
    for xx, yy, uu in zip(x, y, U):
        g = logistic(k * (xx - theta))
        lam0 = lb + alpha * g
        mu = max(eps, lam0 * math.exp(omega * uu) * dt)
        ll += yy * math.log(mu) - mu  # drop log(yy!) constant
    return ll


def log_prior(lb: float, alpha: float, theta: float, omega: float) -> float:
    # Weak priors to regularize identifiability
    # lb ~ N(5, 2^2), alpha ~ N(20, 6^2), theta ~ N(0.6, 0.1^2), omega ~ N(0.5, 0.6^2)
    def lnorm(x, m, s):
        return -0.5 * ((x - m) / s) ** 2 - math.log(s)

    return lnorm(lb, 5.0, 2.0) + lnorm(alpha, 20.0, 6.0) + lnorm(theta, 0.6, 0.1) + lnorm(omega, 0.5, 0.6)


def posterior_grid(two_cond_data: List[Dict[str, List[float]]], dt: float) -> Dict[str, float]:
    lb_grid = [2.0, 3.5, 5.0, 6.5, 8.0]
    alpha_grid = [10.0, 14.0, 18.0, 22.0, 26.0]
    theta_grid = [0.45, 0.5, 0.55, 0.6, 0.65, 0.7]
    omega_grid = [i / 20 for i in range(-2, 31)]  # -0.1 .. 1.5

    # collect log-posteriors
    items: List[Tuple[Tuple[float, float, float, float], float]] = []
    best_lp = -1e300
    best_param = None

    for lb in lb_grid:
        for alpha in alpha_grid:
            for theta in theta_grid:
                for omega in omega_grid:
                    lp = log_prior(lb, alpha, theta, omega)
                    for ds in two_cond_data:
                        lp += log_likelihood(ds, dt, lb, alpha, theta, omega)
                    items.append(((lb, alpha, theta, omega), lp))
                    if lp > best_lp:
                        best_lp = lp
                        best_param = (lb, alpha, theta, omega)

    # stabilize for normalization
    max_lp = max(lp for _, lp in items)
    ws = [(param, math.exp(lp - max_lp)) for param, lp in items]
    Z = sum(w for _, w in ws)

    # marginal posterior over omega and probability omega>0
    omega_mass = {}
    p_omega_pos = 0.0
    for (lb, alpha, theta, omega), w in ws:
        pw = w / Z
        omega_mass[omega] = omega_mass.get(omega, 0.0) + pw
        if omega > 0:
            p_omega_pos += pw

    # posterior mean omega
    omega_mean = sum(om * pm for om, pm in omega_mass.items())

    # 95% equal-tail interval from discrete marginal
    oms = sorted(omega_mass.keys())
    cdf = 0.0
    lo, hi = oms[0], oms[-1]
    for om in oms:
        cdf += omega_mass[om]
        if cdf >= 0.025:
            lo = om
            break
    cdf = 0.0
    for om in oms:
        cdf += omega_mass[om]
        if cdf >= 0.975:
            hi = om
            break

    return {
        "map_lambda_base": best_param[0],
        "map_alpha": best_param[1],
        "map_theta": best_param[2],
        "map_omega": best_param[3],
        "post_mean_omega": omega_mean,
        "ci95_lo_omega": lo,
        "ci95_hi_omega": hi,
        "p_omega_gt_0": p_omega_pos,
    }


def main():
    T, dt = 30.0, 0.01
    omega_true = 0.8

    # two intervention conditions for identifiability
    ds1 = simulate_condition(T=T, dt=dt, omega_true=omega_true, drive_gain=0.9, seed=11)
    ds2 = simulate_condition(T=T, dt=dt, omega_true=omega_true, drive_gain=1.2, seed=22)

    out = posterior_grid([ds1, ds2], dt)

    print("=== Bayesian SRT-mTOR (2-condition, grid posterior) ===")
    print(f"true omega = {omega_true}")
    print(
        "MAP: lambda_base={map_lambda_base}, alpha={map_alpha}, theta={map_theta}, omega={map_omega}".format(
            **out
        )
    )
    print(
        "Posterior omega: mean={post_mean_omega:.3f}, 95%CI=[{ci95_lo_omega:.3f}, {ci95_hi_omega:.3f}], P(omega>0)={p_omega_gt_0:.5f}".format(
            **out
        )
    )


if __name__ == "__main__":
    main()
