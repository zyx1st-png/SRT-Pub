"""
R5-01A Exploratory Refinement:
1. Exact lower & upper saddle-node fold boundaries (Gamma_low, Gamma_high) of non-absorbing Model S2.
2. Three organizational regimes of current-vs-future capacity:
   - Zero-sum trapping (Gamma > Gamma_high)
   - Bistable trapping + living-scaffold vs crutch-collapse hysteresis under TWO switches
     (Switch 1 at t=40, Scaffold on t in [45, 52], Scaffold REMOVED at t=52, Switch 2 at t=75!)
   - Surplus-release spontaneous ignition (Gamma < Gamma_low: current foreground automation
     expands total capacity C and annihilates the low-probe trap so probing self-ignites!)
3. Clean two-switch comparison against Fixed ESC, Decaying-Dither ESC, and Utility-Selective Reset.
"""

import numpy as np


def phi_match(psi: float) -> float:
    return 0.5 * (1.0 + np.cos(psi))


def find_folds(nu_p=0.015, a_p=1.7, K_p=0.35, m_sig=0.85):
    """Find exact Gamma_low and Gamma_high where saddle-node bifurcations occur.
    Equilibrium: g(p) = (nu_p + a_p*m_sig*p^2/(K_p^2+p^2)) / p = Gamma.
    Folds are local extrema of g(p) for p > 0!
    """
    ps = np.linspace(1e-4, 3.0, 300000)
    g = (nu_p + a_p * m_sig * (ps ** 2) / (K_p ** 2 + ps ** 2)) / ps
    dg = np.diff(g)
    # local minimum -> Gamma_low (annihilates low-probe trap when Gamma < Gamma_low!)
    # local maximum -> Gamma_high (annihilates high-probe state when Gamma > Gamma_high!)
    min_idx = np.where((dg[:-1] < 0) & (dg[1:] > 0))[0] + 1
    max_idx = np.where((dg[:-1] > 0) & (dg[1:] < 0))[0] + 1
    p_low_fold, gamma_low = ps[min_idx[0]], g[min_idx[0]]
    p_high_fold, gamma_high = ps[max_idx[0]], g[max_idx[0]]
    print("=== 1. Exact Saddle-Node Folds of Non-Absorbing Probing Dynamics ===")
    print(f"  Lower fold (trap annihilated if Gamma < Gamma_low):  p={p_low_fold:.4f}, Gamma_low ={gamma_low:.4f}")
    print(f"  Upper fold (active state lost if Gamma > Gamma_high): p={p_high_fold:.4f}, Gamma_high={gamma_high:.4f}")
    print(f"  Bistable hysteresis window: Gamma in ({gamma_low:.4f}, {gamma_high:.4f})")
    return gamma_low, gamma_high


def run_s2_two_switch(lambda_surplus, chi_crowd, p_init=0.01, I_ext_amp=0.0,
                      I_ext_window=(45.0, 52.0), T_tot=120.0, nu_p=0.015):
    dt = 0.01
    eps, alpha, beta = 0.2, 1.0, 0.8
    nu_w, eta_w, mu_w, gamma_cap = 0.01, 1.4, 0.25, 0.7
    a_p, K_p, mu_p = 1.7, 0.35, 0.65
    C0, K_s = 1.0, 0.5
    eta_th, h_max, K_h = 1.2, 0.7, 0.25

    w1, w2, p = 0.9, 0.05, p_init
    th1, th2 = 0.0, 0.0
    n_steps = int(T_tot / dt)

    snaps = {}
    for step in range(n_steps):
        t = step * dt
        if t < 40.0:
            # Phase 1: ch1 aligned at 0.0, ch2 unused at pi
            dphi1, dphi2 = 0.0, np.pi
        elif t < 75.0:
            # Switch 1: ch2 becomes active target at 1.2 rad
            dphi1, dphi2 = np.pi, 1.2
        else:
            # Switch 2 (AFTER scaffold removal!): ch2 jumps to -1.3 rad (large 2.5 rad shift!)
            dphi1, dphi2 = np.pi, -1.3

        A = w1 * phi_match(dphi1 - th1)
        B = w2 * phi_match(dphi2 - th2)
        u1 = A / (eps + alpha * A + beta * B)
        u2 = B / (eps + alpha * B + beta * A)

        aligned_work = w1 * phi_match(dphi1 - th1) + w2 * phi_match(dphi2 - th2)
        C_tot = C0 + lambda_surplus * aligned_work / (K_s + aligned_work)

        h = h_max * p / (p + K_h)
        b1 = -np.sin(dphi1 - th1) * np.sin(h)
        b2 = -np.sin(dphi2 - th2) * np.sin(h)

        I_ext = I_ext_amp if (I_ext_window[0] <= t <= I_ext_window[1]) else 0.0
        crowding = (w1 + w2) / C_tot
        gamma_eff = mu_p + chi_crowd * crowding
        m_sig = 0.85 + 0.6 * (abs(b1) + abs(b2))

        dw1 = nu_w + eta_w * u1 * phi_match(dphi1 - th1) - mu_w * w1 - gamma_cap * w1 * (w1 + w2 + p) / C_tot
        dw2 = nu_w + eta_w * u2 * phi_match(dphi2 - th2) - mu_w * w2 - gamma_cap * w2 * (w1 + w2 + p) / C_tot
        dp = nu_p + a_p * m_sig * (p ** 2) / (K_p ** 2 + p ** 2) + I_ext - gamma_eff * p

        w1 = max(0.0, w1 + dt * dw1)
        w2 = max(0.0, w2 + dt * dw2)
        p = max(0.0, p + dt * dp)

        th1 += dt * eta_th * (-b1)
        th2 += dt * eta_th * (-b2)

        if abs(t - 39.5) < dt / 2:
            snaps["pre_s1"] = (p, gamma_eff, C_tot)
        if abs(t - 74.5) < dt / 2:
            err2_s1 = abs(np.angle(np.exp(1j * (1.2 - th2))))
            snaps["post_s1"] = (p, gamma_eff, err2_s1)

    err2_s2 = abs(np.angle(np.exp(1j * (-1.3 - th2))))
    snaps["post_s2"] = (p, gamma_eff, err2_s2, w2)
    return snaps


def test_two_switch_regimes():
    find_folds()
    print("\n=== 2. Two-Switch Test (Switch 1 at t=40, Scaffold t in [45,52], Switch 2 at t=75) ===")
    cases = [
        ("1. Surplus-Release SPONTANEOUS IGNITION (lam=5.0, chi=0.5, NO scaffold)", dict(lambda_surplus=5.0, chi_crowd=0.5, I_ext_amp=0.0, nu_p=0.08)),
        ("2. Bistable Trap, NO scaffold (lam=0.5, chi=1.65, I=0)", dict(lambda_surplus=0.5, chi_crowd=1.65, I_ext_amp=0.0)),
        ("3. Bistable Trap, SUB-THRESHOLD scaffold (lam=0.5, chi=1.65, I=0.05)", dict(lambda_surplus=0.5, chi_crowd=1.65, I_ext_amp=0.05)),
        ("4. Bistable Trap, LIVING scaffold (lam=0.5, chi=1.65, I=0.40 -> persists!)", dict(lambda_surplus=0.5, chi_crowd=1.65, I_ext_amp=0.40)),
        ("5. Over-Crowded CRUTCH (lam=0.0, chi=2.30, I=0.60 -> passes S1, FAILS S2!)", dict(lambda_surplus=0.0, chi_crowd=2.30, I_ext_amp=0.60)),
    ]
    for name, kw in cases:
        sn = run_s2_two_switch(**kw)
        s0, s1, s2 = sn["pre_s1"], sn["post_s1"], sn["post_s2"]
        print(
            f"{name}\n"
            f"  Pre-S1 (t=39.5):  p={s0[0]:.4f}, Gamma_eff={s0[1]:.3f}, C={s0[2]:.3f}\n"
            f"  Post-S1 (t=74.5): p={s1[0]:.4f}, Gamma_eff={s1[1]:.3f}, err2_S1={s1[2]:.4f} rad\n"
            f"  Post-S2 (t=120):  p={s2[0]:.4f}, Gamma_eff={s2[1]:.3f}, err2_S2={s2[2]:.4f} rad"
        )

    print("\n=== 3. Mature Baselines on Identical Two-Switch Environment (t1=40 -> 1.2, t2=75 -> -1.3) ===")
    dt = 0.01
    n_steps = int(120.0 / dt)

    # Fixed ESC
    th2 = 0.0
    cost_f = 0.0
    for step in range(n_steps):
        t = step * dt
        dphi2 = 0.0 if t < 40.0 else (1.2 if t < 75.0 else -1.3)
        h = 0.40
        b2 = -np.sin(dphi2 - th2) * np.sin(h)
        th2 += dt * 1.2 * (-b2)
        cost_f += dt * 0.5 * (1.0 - np.cos(h))
        if abs(t - 74.5) < dt / 2:
            e1_f = abs(np.angle(np.exp(1j * (1.2 - th2))))
    e2_f = abs(np.angle(np.exp(1j * (-1.3 - th2))))

    # Decaying-Dither ESC
    th2, h, cost_d = 0.0, 0.40, 0.0
    for step in range(n_steps):
        t = step * dt
        dphi2 = 0.0 if t < 40.0 else (1.2 if t < 75.0 else -1.3)
        b2 = -np.sin(dphi2 - th2) * np.sin(h)
        th2 += dt * 1.2 * (-b2)
        h = max(0.0, min(0.7, h + dt * (2.0 * abs(b2) - 0.5 * h)))
        cost_d += dt * 0.5 * (1.0 - np.cos(h))
        if abs(t - 74.5) < dt / 2:
            e1_d = abs(np.angle(np.exp(1j * (1.2 - th2))))
            h_s1 = h
    e2_d = abs(np.angle(np.exp(1j * (-1.3 - th2))))

    # Utility-Selective Reset (Dohare 2024 analogue)
    rng = np.random.default_rng(42)
    th2, util, resets = 0.0, 1.0, 0
    for step in range(n_steps):
        t = step * dt
        dphi2 = 0.0 if t < 40.0 else (1.2 if t < 75.0 else -1.3)
        perf = phi_match(dphi2 - th2)
        util = 0.99 * util + 0.01 * perf
        if util < 0.70 and (step % 150 == 0):
            th2 = rng.uniform(-np.pi, np.pi)
            resets += 1
        b2 = -np.sin(dphi2 - th2) * np.sin(0.15)
        th2 += dt * 1.2 * (-b2)
        if abs(t - 74.5) < dt / 2:
            e1_cb = abs(np.angle(np.exp(1j * (1.2 - th2))))
    e2_cb = abs(np.angle(np.exp(1j * (-1.3 - th2))))

    print(f"  Fixed-dither ESC (h=0.40):           err2_S1={e1_f:.4f}, err2_S2={e2_f:.4f} | dither_cost={cost_f:.2f}")
    print(f"  Decaying-dither ESC (PE loss):       err2_S1={e1_d:.4f} (h={h_s1:.2e}), err2_S2={e2_d:.4f} (h={h:.2e}) | cost={cost_d:.2f}")
    print(f"  Utility-selective reset (Dohare24):  err2_S1={e1_cb:.4f}, err2_S2={e2_cb:.4f} | resets={resets}")


if __name__ == "__main__":
    test_two_switch_regimes()
