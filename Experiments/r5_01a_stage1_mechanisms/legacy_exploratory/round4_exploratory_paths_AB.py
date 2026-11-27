"""
R5-01A Round-4 Exploratory Verification (Paths A & B)
Strictly scratch script outside repo.

Path A Calibrations:
1. Reconcile exact scalar roots at Gamma=1.80 under (a_p*m0 = 1.445) vs (a_p*m0 = 1.600).
2. Full 5D coupled S2 bifurcation analysis at Case 4 parameters (lam=0.5, chi=1.65):
   Does high-p exist WITHOUT scaffold (p_init sweep at I=0) because high p self-consistently
   lowers (w1+w2)/C from 2.253 to <2.03? Distinguish (i) existing coupled basin jump,
   (ii) coupled self-consistent state creation beyond frozen-Gamma scalar prediction,
   and (iii) history-dependent parameter shift.
3. Exact comparison of Decaying-Dither ESC Form A (dh/dt = 2|b| - 0.5h, with & without noise floor)
   vs Form B (dh/dt = (2|b| - 0.5)h, strictly stable zero!).

Path B Minimal Cross-Organization Co-Generative Model (C1):
Two organizations A & B observing local phases phi_A(t) = phi_bg(t) + delta_env/2 and
phi_B(t) = phi_bg(t) - delta_env/2 where phi_bg(t) drifts randomly (gauge obstruction:
neither A nor B alone can observe delta_env = phi_A - phi_B!).
Demonstrates:
- Class C Joint Capability impossible for A or B alone;
- Downward asymmetric role differentiation (anchor vs differential tracker) under shared feedback;
- Partner-swap test (B -> B' with new offset) separating Rigid Co-Locking vs Reorganizable Co-Generation.
"""

import numpy as np


def phi_match(psi: float) -> float:
    return 0.5 * (1.0 + np.cos(psi))


def calibration_1_scalar_roots():
    print("=== PATH A.1: Exact Scalar Roots Reconciliation at Gamma=1.80 ===")
    for label, a_p, m0 in [
        ("Run-2 params (a_p=1.7, m0=0.85 -> a_p*m0=1.445, matches folds 0.8369/2.1076)", 1.7, 0.85),
        ("Run-1 params (a_p=1.6, m0=1.00 -> a_p*m0=1.600, mistakenly mixed into text)", 1.6, 1.00),
    ]:
        nu_p, K_p, gamma = 0.015, 0.35, 1.80
        # Exact cubic: gamma*p^3 - (nu_p + a_p*m0)*p^2 + gamma*K_p^2*p - nu_p*K_p^2 = 0
        coeffs = [gamma, -(nu_p + a_p * m0), gamma * (K_p ** 2), -nu_p * (K_p ** 2)]
        roots = np.sort(np.roots(coeffs).real)
        # Also exact folds via derivative of g(p)
        ps = np.linspace(1e-4, 3.0, 300000)
        g = (nu_p + a_p * m0 * (ps ** 2) / (K_p ** 2 + ps ** 2)) / ps
        dg = np.diff(g)
        min_i = np.where((dg[:-1] < 0) & (dg[1:] > 0))[0][0] + 1
        max_i = np.where((dg[:-1] > 0) & (dg[1:] < 0))[0][0] + 1
        print(f"  {label}")
        print(f"    Exact cubic roots at Gamma=1.80: {roots[0]:.6f} (low), {roots[1]:.6f} (sad), {roots[2]:.6f} (high)")
        print(f"    Exact folds: Gamma_low={g[min_i]:.6f} (p={ps[min_i]:.4f}), Gamma_high={g[max_i]:.6f} (p={ps[max_i]:.4f})")


def run_s2_coupled_probe(lambda_surplus, chi_crowd, p_init, I_ext_amp=0.0,
                         I_window=(45.0, 52.0), do_switch=True, T_tot=120.0):
    dt = 0.01
    eps, alpha, beta = 0.2, 1.0, 0.8
    nu_w, eta_w, mu_w, gamma_cap = 0.01, 1.4, 0.25, 0.7
    nu_p, a_p, K_p, mu_p = 0.015, 1.7, 0.35, 0.65
    C0, K_s = 1.0, 0.5
    eta_th, h_max, K_h = 1.2, 0.7, 0.25

    w1, w2, p = 0.9, 0.05, p_init
    th1, th2 = 0.0, 0.0
    n_steps = int(T_tot / dt)

    out = {}
    for step in range(n_steps):
        t = step * dt
        if not do_switch:
            dphi1, dphi2 = 0.0, np.pi
        elif t < 40.0:
            dphi1, dphi2 = 0.0, np.pi
        elif t < 75.0:
            dphi1, dphi2 = np.pi, 1.2
        else:
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

        I_ext = I_ext_amp if (I_window[0] <= t <= I_window[1]) else 0.0
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
            out["t39.5"] = (w1, w2, p, gamma_eff, m_sig)
        if abs(t - 74.5) < dt / 2:
            out["t74.5"] = (w1, w2, p, gamma_eff, m_sig)
    out["final"] = (w1, w2, p, gamma_eff, m_sig)
    return out


def calibration_2_full_coupled_bifurcation():
    print("\n=== PATH A.2: Full Coupled 5D S2 vs Frozen-Gamma Scalar Prediction (Case 4: lam=0.5, chi=1.65, I=0) ===")
    print("Test 1: Static Phase-1 environment (no switch, I_ext=0), sweeping p_init:")
    for p0 in [0.01, 0.15, 0.25, 0.35, 0.80]:
        res = run_s2_coupled_probe(0.5, 1.65, p_init=p0, I_ext_amp=0.0, do_switch=False, T_tot=80.0)
        w1, w2, p, g_eff, m_s = res["final"]
        print(f"  p_init={p0:4.2f} -> final: w1={w1:.4f}, w2={w2:.4f}, p={p:.4f}, Gamma_eff={g_eff:.4f}, m_sig={m_s:.4f}")

    print("\nTest 2: Scan chi_crowd (at lam=0.5, I_ext=0, no switch) to find FULL COUPLED upper fold:")
    for chi in [1.50, 1.65, 1.75, 1.85, 1.95]:
        low = run_s2_coupled_probe(0.5, chi, p_init=0.01, I_ext_amp=0.0, do_switch=False, T_tot=100.0)["final"]
        high = run_s2_coupled_probe(0.5, chi, p_init=1.00, I_ext_amp=0.0, do_switch=False, T_tot=100.0)["final"]
        print(
            f"  chi={chi:4.2f} | from p0=0.01 -> p={low[2]:.4f} (G={low[3]:.3f}) | "
            f"from p0=1.00 -> p={high[2]:.4f} (G={high[3]:.3f}) | bistable={abs(high[2]-low[2])>0.1}"
        )


def calibration_3_esc_forms():
    print("\n=== PATH A.3: Exact Comparison of Decaying-Dither ESC Form A vs Form B ===")
    dt = 0.01
    n_steps = int(120.0 / dt)

    def sim_esc(mode, noise_floor=0.0):
        th2, h = 0.0, 0.40
        for step in range(n_steps):
            t = step * dt
            dphi2 = 0.0 if t < 40.0 else (1.2 if t < 75.0 else -1.3)
            b_raw = -np.sin(dphi2 - th2) * np.sin(h)
            # Deadzone/noise-floor clipping if sensor cannot resolve |b| < noise_floor
            b_eff = 0.0 if abs(b_raw) < noise_floor else b_raw
            th2 += dt * 1.2 * (-b_eff)
            if mode == "A":
                # Code form: dh/dt = 2|b| - 0.5h -> linear rate at h=0 is (2|sin e| - 0.5)
                dh = 2.0 * abs(b_eff) - 0.5 * h
            else:
                # Report-typo / quadratic form: dh/dt = (2|b| - 0.5)h -> linear rate at h=0 is -0.5 < 0!
                dh = (2.0 * abs(b_eff) - 0.5) * h
            h = max(0.0, min(0.7, h + dt * dh))
            if abs(t - 74.5) < dt / 2:
                e1 = abs(np.angle(np.exp(1j * (1.2 - th2))))
                h1 = h
        e2 = abs(np.angle(np.exp(1j * (-1.3 - th2))))
        return e1, h1, e2, h

    for label, mode, nf in [
        ("Form A (dh = 2|b| - 0.5h), noiseless (nf=0)", "A", 0.0),
        ("Form A (dh = 2|b| - 0.5h), sensor floor (nf=1e-3)", "A", 1e-3),
        ("Form B (dh = (2|b| - 0.5)h), noiseless (nf=0)", "B", 0.0),
    ]:
        e1, h1, e2, h2 = sim_esc(mode, nf)
        print(f"  {label:52s} | S1 err={e1:.4f} (h={h1:.2e}) | S2 err={e2:.4f} (h={h2:.2e})")


def path_b_cross_org_cogeneration():
    """
    Model C1: Minimal Cross-Organization Co-Generative Capability (A >< B).
    Environment: phi_A(t) = phi_bg(t) + delta_env/2, phi_B(t) = phi_bg(t) - delta_env/2,
    where phi_bg(t) = omega_bg * t + random walk (unobservable common-mode drift!).
    Neither A alone nor B alone can identify delta_env (exact local gauge invariance!).
    When coupled via shared interface g_AB > 0:
      - Joint relative phase observed across interface:
        psi_AB = (phi_A - th_A) - (phi_B - th_B) = delta_env - (th_A - th_B)
      - Joint capability output: U_AB = g_AB * w_A_rel * w_B_rel * (1 + cos(psi_AB))/2
      - Notice: local references th_A, th_B co-adapt, AND local probing p_A, p_B determine
        who tracks changes (role differentiation: anchor vs tracker!).
      - Partner swap test at t=60: B is replaced by B' with a different internal phase bias
        (delta_shift = +1.5 rad) and frequency/role stiffness.
        Compare:
          (1) Isolated A alone (g_AB = 0): zero info on delta_env (gauge obstruction).
          (2) Rigid Co-Locking (A loses its probing p_A -> low during A><B because B did all tracking):
              when B -> B' (static/stubborn new partner), A><B' FAILS to re-align!
          (3) Reorganizable Co-Generation (A retains probing / re-opens on joint mismatch):
              when B -> B', A><B' rapidly re-aligns and recovers joint capability U_AB'!
    """
    print("\n=== PATH B: Model C1 — Cross-Organization Co-Generative Capability & Partner-Swap Test ===")
    dt = 0.01
    T_tot = 120.0
    t_swap = 60.0
    n_steps = int(T_tot / dt)

    def run_c1(g_AB, a_keeps_probe=True, partner_B_active=True, partner_Bprime_active=False):
        # Local references th_A, th_B; local relational share w_A_rel, w_B_rel; local probing p_A, p_B
        th_A, th_B = 0.0, 0.0
        wA_rel, wB_rel = 0.25, 0.25  # start low; grow via joint payoff!
        p_A, p_B = 0.50, 0.50
        delta_env = 1.1  # true relational phase difference between site A and site B
        bias_B = 0.0

        # Also track isolated A's best local attempt on phi_A(t) with drifting phi_bg(t)
        rng = np.random.default_rng(7)
        phi_bg = 0.0
        iso_A_corrs = []

        for step in range(n_steps):
            t = step * dt
            # Fast drifting common background phase -> destroys any single-site estimate of delta_env
            phi_bg += dt * (2.5 + 1.5 * np.sin(0.7 * t)) + np.sqrt(dt) * 0.8 * rng.standard_normal()
            phi_A = phi_bg + 0.5 * delta_env
            phi_B = phi_bg - 0.5 * delta_env + bias_B

            if step == int(t_swap / dt):
                # Partner swap B -> B': new partner has different phase offset (+1.6 rad), lower initial wB_rel,
                # and (in stubborn test) B' does NOT adapt its own th_B' (e.g. rigid new tool/environment partner)
                bias_B = 1.6
                th_B = 0.0
                wB_rel = 0.30
                p_B = 0.50 if partner_Bprime_active else 0.02

            # Effective relational alignment across shared interface (independent of phi_bg!)
            psi_AB = (phi_A - th_A) - (phi_B - th_B)
            match_AB = phi_match(psi_AB)
            U_AB = g_AB * wA_rel * wB_rel * match_AB

            # Active probing by A and B on the shared interface:
            h_A = 0.5 * p_A / (p_A + 0.2)
            h_B = 0.5 * p_B / (p_B + 0.2)
            # Perturbing th_A by +-h_A changes psi_AB by -+h_A -> gradient wrt th_A is +sin(psi_AB)*sin(h_A)
            grad_A = g_AB * wA_rel * wB_rel * np.sin(psi_AB) * np.sin(h_A)
            # Perturbing th_B by +-h_B changes psi_AB by +-h_B -> gradient wrt th_B is -sin(psi_AB)*sin(h_B)
            grad_B = -g_AB * wA_rel * wB_rel * np.sin(psi_AB) * np.sin(h_B)

            # Update local phase references
            th_A += dt * 3.0 * grad_A
            if (t < t_swap and partner_B_active) or (t >= t_swap and partner_Bprime_active):
                th_B += dt * 3.0 * grad_B

            # Downward reorganization of local relational investment w_rel (generative withdrawal from purely local tasks)
            dwA = 1.2 * U_AB * (1.0 - wA_rel) - 0.12 * (wA_rel - 0.15)
            dwB = 1.2 * U_AB * (1.0 - wB_rel) - 0.12 * (wB_rel - 0.15)
            wA_rel = np.clip(wA_rel + dt * dwA, 0.05, 0.95)
            wB_rel = np.clip(wB_rel + dt * dwB, 0.05, 0.95)

            # Asymmetric role differentiation in probing:
            # When B is the faster/active tracker during Phase 1, A's gradient shrinks -> A specializes as stable anchor!
            # Under rigid co-locking (a_keeps_probe=False), A's p_A collapses to low trap during Phase 1.
            # Under reorganizable co-generation (a_keeps_probe=True), joint-payoff surplus lowers A's crowding so p_A stays viable!
            if a_keeps_probe:
                gamma_A = 1.50 - 0.55 * U_AB  # joint surplus supports A's reorganizability!
            else:
                gamma_A = 1.60 + 1.40 * wA_rel  # rigid specialization crowds out A's probing!

            m_A = 0.85 + 1.2 * abs(grad_A)
            dp_A = 0.015 + 1.7 * m_A * (p_A ** 2) / (0.35 ** 2 + p_A ** 2) - gamma_A * p_A
            p_A = max(0.0, p_A + dt * dp_A)

            if t < t_swap and partner_B_active:
                # B actively specializes as tracker
                dp_B = 0.015 + 1.7 * (0.95 + 1.2 * abs(grad_B)) * (p_B ** 2) / (0.35 ** 2 + p_B ** 2) - 1.2 * p_B
                p_B = max(0.0, p_B + dt * dp_B)

            if t > 10.0 and t < t_swap:
                iso_A_corrs.append(np.cos(phi_A))

            if abs(t - 59.5) < dt / 2:
                err_pre = abs(np.angle(np.exp(1j * psi_AB)))
                snap_pre = (err_pre, U_AB, wA_rel, wB_rel, p_A, p_B)

        err_post = abs(np.angle(np.exp(1j * psi_AB)))
        snap_post = (err_post, U_AB, wA_rel, wB_rel, p_A, p_B)
        return snap_pre, snap_post, float(np.mean(iso_A_corrs))

    for name, kw in [
        ("0. Uncoupled A & B (g_AB=0): gauge obstruction, zero joint capability", dict(g_AB=0.0)),
        ("1. Rigid Co-Locking (A specializes as passive anchor, p_A collapses -> FAILS B' swap)", dict(g_AB=1.5, a_keeps_probe=False, partner_B_active=True, partner_Bprime_active=False)),
        ("2. Reorganizable Co-Generation (joint surplus preserves p_A -> PASSES rigid B' swap!)", dict(g_AB=1.5, a_keeps_probe=True, partner_B_active=True, partner_Bprime_active=False)),
    ]:
        pre, post, mean_iso = run_c1(**kw)
        print(
            f"{name}\n"
            f"  Pre-swap  (t=59.5, A><B ): psi_err={pre[0]:.4f} rad, U_AB={pre[1]:.3f}, "
            f"w_rel=({pre[2]:.2f},{pre[3]:.2f}), p=({pre[4]:.3f},{pre[5]:.3f})\n"
            f"  Post-swap (t=120,  A><B'): psi_err={post[0]:.4f} rad, U_AB={post[1]:.3f}, "
            f"w_rel=({post[2]:.2f},{post[3]:.2f}), p=({post[4]:.3f},{post[5]:.3f})"
        )


if __name__ == "__main__":
    calibration_1_scalar_roots()
    calibration_2_full_coupled_bifurcation()
    calibration_3_esc_forms()
    path_b_cross_org_cogeneration()
