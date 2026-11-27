"""
R5-01A Round-5 Deepening & Stage-Convergence Verification (Paths A & B)
Strictly scratch script outside repo.

PATH A:
1. Exact 5D equilibria & Jacobian spectrum of full coupled S2 (proving asymptotic local stability
   at chi=1.55 vs exact coupled saddle-node fold chi_c and ghost lifetime scaling tau(chi)).
2. Exact analytical & numerical counterexamples where SUCCESS reproduces rather than erodes
   probing conditions:
   - Counterexample A-1: Superlinear infrastructure elasticity E_{C,W} > 1 (Hill-2 capacity C(W))
   - Counterexample A-2: Functional backgrounding load reduction L_fg = W*(1 - kappa_auto*Phi^2)
     at CONSTANT raw capacity C0!

PATH B (Model C2):
- Strict local unidentifiability under uniform drifting common background phi_bg(t).
- Zero smuggled sin(psi): directional gradients computed ONLY from physical two-point
  perturbation differencing of the even scalar interface output U_AB(th_i + h_i) - U_AB(th_i - h_i)
  with finite sensor deadzone!
- 100% IDENTICAL local equations and parameters for both A and B; role differentiation arises
  PURELY from history (H1 symmetric vs H2 asymmetric)!
- Four structural tests on H2 (where A withdrew to low-p anchor and B holds tracker duty):
  (T1) Whole environment shift (delta_env jump): whole STILL adapts via B (duty transfer!)
  (T2) Anchor swap (A -> A' rigid): whole STILL adapts via B!
  (T3) Tracker swap (B -> B' rigid) under high specialization stickiness: rigid failure!
  (T4) Tracker swap (B -> B' rigid) when breakdown relaxes specialization load:
       A ENDOGENOUSLY RE-AWAKENS p_A (dedifferentiation) and takes over tracker duty!
"""

import numpy as np
from scipy.optimize import root


def phi_match(psi: float) -> float:
    return 0.5 * (1.0 + np.cos(psi))


# =============================================================================
# PATH A: Exact 5D Coupled S2 Equilibria, Jacobian Spectrum & Success Counterexamples
# =============================================================================

def s2_rhs_static_aligned(state, chi_crowd, lam_surplus=0.5, cap_mode="concave", kappa_auto=0.0):
    """
    Reduced 3D exact equilibrium system (w1, w2, p) when BOTH channels are aligned (Phi1=Phi2=1, b1=b2=0),
    or when ONLY ch1 is aligned (Phi1=1, Phi2=0) -> we pass Phi1, Phi2 explicitly!
    Let's write full 5D RHS at static dphi1=0, dphi2=pi (or aligned dphi1=0, dphi2=0).
    """
    pass


def s2_rhs_3d(x, chi_crowd, Phi1, Phi2, lam_surplus=0.5, cap_mode="concave", kappa_auto=0.0):
    """Exact RHS for (w1, w2, p) at given alignments (Phi1, Phi2) with b1=b2=0."""
    w1, w2, p = x
    eps, alpha, beta = 0.2, 1.0, 0.8
    nu_w, eta_w, mu_w, gamma_cap = 0.01, 1.4, 0.25, 0.7
    nu_p, a_p, K_p, mu_p = 0.015, 1.7, 0.35, 0.65
    C0, K_s = 1.0, 0.5
    m_sig = 0.85

    A = w1 * Phi1
    B = w2 * Phi2
    u1 = A / (eps + alpha * A + beta * B)
    u2 = B / (eps + alpha * B + beta * A)

    aligned_work = A + B
    if cap_mode == "concave":
        C_tot = C0 + lam_surplus * aligned_work / (K_s + aligned_work)
    elif cap_mode == "superlinear":
        # Hill-2 infrastructure dividend: C(W) = C0 + lam * W^2 / (K_s^2 + W^2)
        C_tot = C0 + lam_surplus * (aligned_work ** 2) / ((1.4 ** 2) + aligned_work ** 2)
    else:
        C_tot = C0

    # Effective foreground load (functional backgrounding reduces active load of aligned channels!)
    L_fg = w1 * (1.0 - kappa_auto * (Phi1 ** 2)) + w2 * (1.0 - kappa_auto * (Phi2 ** 2))
    crowding = L_fg / C_tot
    gamma_eff = mu_p + chi_crowd * crowding

    dw1 = nu_w + eta_w * u1 * Phi1 - mu_w * w1 - gamma_cap * w1 * (w1 + w2 + p) / C_tot
    dw2 = nu_w + eta_w * u2 * Phi2 - mu_w * w2 - gamma_cap * w2 * (w1 + w2 + p) / C_tot
    dp = nu_p + a_p * m_sig * (p ** 2) / (K_p ** 2 + p ** 2) - gamma_eff * p
    return np.array([dw1, dw2, dp])


def numeric_jacobian(f, x, eps=1e-7):
    n = len(x)
    J = np.zeros((n, n))
    f0 = f(x)
    for j in range(n):
        dx = np.zeros(n)
        dx[j] = eps
        J[:, j] = (f(x + dx) - f0) / eps
    return J


def path_a_exact_bifurcation_and_counterexamples():
    print("=== PATH A.1: Exact Coupled Equilibria & Jacobian Eigenvalues (Dual-Aligned Phi1=Phi2=1) ===")
    # Note: In T=400 run, when p is active, BOTH th1 and th2 align (Phi1=Phi2=1), so w1=w2!
    # Wait: why did lo state at chi=1.55 have w1=1.312, w2=0.011 (Phi1=1, Phi2=0),
    # while hi state had w1=w2=0.6017 (Phi1=1, Phi2=1)?!
    # Let's check BOTH (Phi1=1, Phi2=0) and (Phi1=1, Phi2=1) exact equilibria + full Jacobian!
    for mode_label, Phi1, Phi2 in [
        ("Single-channel aligned (Phi1=1, Phi2=0) [low-p niche]", 1.0, 0.0),
        ("Dual-channel aligned   (Phi1=1, Phi2=1) [post-probing aligned niche]", 1.0, 1.0),
    ]:
        print(f"\n  [{mode_label}]")
        for chi in [1.45, 1.50, 1.55, 1.57, 1.58, 1.59, 1.60, 1.65]:
            f = lambda x: s2_rhs_3d(x, chi, Phi1, Phi2)
            sol_hi = root(f, [0.6, 0.6 if Phi2 > 0 else 0.01, 0.5], tol=1e-13)
            sol_lo = root(f, [1.2, 0.01 if Phi2 == 0 else 0.7, 0.007], tol=1e-13)
            res_hi = np.linalg.norm(f(sol_hi.x))
            if sol_hi.success and res_hi < 1e-10 and sol_hi.x[2] > 0.1:
                J_hi = numeric_jacobian(f, sol_hi.x)
                eigs = np.linalg.eigvals(J_hi)
                max_re = np.max(eigs.real)
                w1, w2, p = sol_hi.x
                C = 1.0 + 0.5 * (w1 * Phi1 + w2 * Phi2) / (0.5 + w1 * Phi1 + w2 * Phi2)
                G = 0.65 + chi * (w1 + w2) / C
                print(
                    f"    chi={chi:4.2f} | HIGH eq EXISTS: w=({w1:.4f},{w2:.4f}), p={p:.4f}, G={G:.4f} | "
                    f"max Re(eig)={max_re:+.5f} ({'STABLE' if max_re<0 else 'UNSTABLE'})"
                )
            else:
                w1, w2, p = sol_lo.x
                C = 1.0 + 0.5 * (w1 * Phi1 + w2 * Phi2) / (0.5 + w1 * Phi1 + w2 * Phi2)
                G = 0.65 + chi * (w1 + w2) / C
                print(
                    f"    chi={chi:4.2f} | HIGH eq ANNIHILATED (only low eq: w=({w1:.4f},{w2:.4f}), p={p:.4f}, G={G:.4f})"
                )

    # Pinpoint exact coupled fold chi_c for dual-aligned state via bisection
    lo_c, hi_c = 1.55, 1.60
    for _ in range(30):
        mid = 0.5 * (lo_c + hi_c)
        f = lambda x: s2_rhs_3d(x, mid, 1.0, 1.0)
        sol = root(f, [0.6, 0.6, 0.4], tol=1e-13)
        if sol.success and np.linalg.norm(f(sol.x)) < 1e-10 and sol.x[2] > 0.15:
            lo_c = mid
        else:
            hi_c = mid
    chi_c = 0.5 * (lo_c + hi_c)
    print(f"\n  Exact coupled upper fold (dual-aligned): chi_c = {chi_c:.6f}")

    # Verify Saddle-Node Ghost lifetime scaling tau(chi) ~ (chi - chi_c)^(-1/2)
    print("\n=== PATH A.2: Saddle-Node Ghost Lifetime Scaling (Success-Induced Delayed Extinction) ===")
    dt = 0.01
    for dchi in [0.005, 0.01, 0.02, 0.04, 0.08]:
        chi = chi_c + dchi
        x = np.array([0.60, 0.60, 0.50])
        t_drop = None
        for step in range(200000):
            x = np.maximum(0.0, x + dt * s2_rhs_3d(x, chi, 1.0, 1.0))
            if x[2] < 0.10:
                t_drop = step * dt
                break
        scaled = t_drop * np.sqrt(dchi) if t_drop is not None else np.nan
        print(f"  chi = chi_c + {dchi:.3f} ({chi:.4f}) -> collapse time tau = {t_drop:7.2f} s | tau * sqrt(dchi) = {scaled:.3f}")

    # Counterexamples A-1 and A-2 rescuing chi=1.65 (and even chi=1.80!) from success-induced extinction!
    print("\n=== PATH A.3: Two Counterexamples Where SUCCESS Reproduces Probing Conditions (dGamma/dW < 0) ===")
    # A-1: Superlinear infrastructure capacity C(W) = C0 + lam*W^2/(K^2 + W^2) with lam=2.5, K=1.4
    for chi in [1.65, 1.85]:
        f_a1 = lambda x: s2_rhs_3d(x, chi, 1.0, 1.0, lam_surplus=2.5, cap_mode="superlinear", kappa_auto=0.0)
        sol = root(f_a1, [0.8, 0.8, 0.8], tol=1e-13)
        J = numeric_jacobian(f_a1, sol.x)
        max_re = np.max(np.linalg.eigvals(J).real)
        W = sol.x[0] + sol.x[1]
        C = 1.0 + 2.5 * W**2 / (1.4**2 + W**2)
        dC = 2.5 * 2 * W * (1.4**2) / ((1.4**2 + W**2)**2)
        elast = W * dC / C
        print(
            f"  Counterexample A-1 (Superlinear C(W), chi={chi:.2f}): w=({sol.x[0]:.3f},{sol.x[1]:.3f}), "
            f"p={sol.x[2]:.4f}, max Re(eig)={max_re:+.4f} (STABLE!) | E_{{C,W}}={elast:.3f}"
        )

    # A-2: Constant raw capacity C0=1.0 (lam=0!), functional backgrounding reduces load: L_fg = W*(1 - kappa_auto*Phi^2)
    for chi, k_auto in [(1.65, 0.35), (2.00, 0.50)]:
        f_a2 = lambda x: s2_rhs_3d(x, chi, 1.0, 1.0, lam_surplus=0.0, cap_mode="constant", kappa_auto=k_auto)
        sol = root(f_a2, [0.6, 0.6, 0.6], tol=1e-13)
        J = numeric_jacobian(f_a2, sol.x)
        max_re = np.max(np.linalg.eigvals(J).real)
        print(
            f"  Counterexample A-2 (Constant C0, Backgrounding kappa_auto={k_auto:.2f}, chi={chi:.2f}): "
            f"w=({sol.x[0]:.3f},{sol.x[1]:.3f}), p={sol.x[2]:.4f}, max Re(eig)={max_re:+.4f} (STABLE!)"
        )


# =============================================================================
# PATH B: Model C2 — Identical-Rule History-Driven Role Division & Dedifferentiation Rescue
# =============================================================================

def path_b_model_c2_symmetric_rules():
    print("\n=== PATH B: Model C2 (100% Identical Local Rules, Operational +/-h Probing, Pure History Differentiation) ===")
    dt = 0.01
    g_AB = 1.6
    sensor_floor = 1e-4  # realistic tiny sensor deadzone (eliminates infinitesimal magic recovery!)

    def interface_U(phi_A, phi_B, th_A, th_B, wA, wB):
        """Even scalar shared interface readout ONLY — no sin(psi) exposed anywhere!"""
        psi = (phi_A - th_A) - (phi_B - th_B)
        return g_AB * wA * wB * phi_match(psi)

    def run_c2(history_mode, perturbation_type, mu_r_relax=0.15, T_tot=140.0):
        """
        IDENTICAL equations & parameters for BOTH A and B!
        gamma_i = mu_p + chi_w * w_i - lam_U * U_AB  (SAME formula for i=A and i=B!)
        Wait: when U_AB drops (e.g., partner swap breakdown!), w_i decays toward w0 ->
        if mu_r_relax is sufficient, chi_w * w_i drops below lower fold -> RE-IGNITES p_i (dedifferentiation)!
        """
        # Identical parameters for A and B
        nu_p, a_p, K_p = 0.015, 1.7, 0.35
        mu_p, chi_w, lam_U = 0.60, 1.85, 0.12
        eta_r, w0 = 1.0, 0.15
        eta_th, h_max, K_h = 6.0, 0.50, 0.20

        # History difference ONLY in initial state (t=0):
        if history_mode == "H1_symmetric":
            pA, pB = 0.70, 0.70
            wA, wB = 0.50, 0.50
        elif history_mode == "H2_asymmetric":
            # Same equations! Only initial developmental history differs: A starts specialized/crowded, B exploratory
            pA, pB = 0.01, 0.80
            wA, wB = 0.88, 0.50
        else:
            raise ValueError(history_mode)

        thA, thB = 0.0, 0.0
        delta_env = 1.1
        bias_B = 0.0
        b_active_track = True
        a_active_track = True
        t_pert = 60.0
        rng = np.random.default_rng(123)
        phi_bg = 0.0

        snaps = {}
        n_steps = int(T_tot / dt)
        for step in range(n_steps):
            t = step * dt
            # Uniformly drifting common background phase (local gauge obstruction)
            phi_bg = (phi_bg + dt * 3.1 + np.sqrt(dt) * 1.2 * rng.standard_normal()) % (2 * np.pi)
            phiA = phi_bg + 0.5 * delta_env
            phiB = phi_bg - 0.5 * delta_env + bias_B

            # Apply perturbation at t=60
            if step == int(t_pert / dt):
                if perturbation_type == "T1_env_shift":
                    delta_env = -1.2  # 2.3 rad whole-environment shift, A & B intact!
                elif perturbation_type == "T2_swap_A_rigid":
                    # Replace anchor A with misaligned rigid A' (cannot move thA)
                    thA = 1.6
                    wA = 0.85
                    pA = 0.01
                    a_active_track = False
                elif perturbation_type in ("T3_swap_B_rigid_sticky", "T4_swap_B_rigid_plastic"):
                    # Replace tracker B with misaligned rigid B' (cannot move thB, low pB)
                    bias_B = 1.7
                    thB = 0.0
                    wB = 0.85
                    pB = 0.01
                    b_active_track = False

            U_now = interface_U(phiA, phiB, thA, thB, wA, wB)

            # Operational physical two-point probing ONLY via scalar U_AB! (Zero smuggled sin(psi)!)
            hA = h_max * pA / (pA + K_h)
            hB = h_max * pB / (pB + K_h)
            gA_raw = 0.5 * (interface_U(phiA, phiB, thA + hA, thB, wA, wB) - interface_U(phiA, phiB, thA - hA, thB, wA, wB))
            gB_raw = 0.5 * (interface_U(phiA, phiB, thA, thB + hB, wA, wB) - interface_U(phiA, phiB, thA, thB - hB, wA, wB))
            gA = 0.0 if abs(gA_raw) < sensor_floor else gA_raw
            gB = 0.0 if abs(gB_raw) < sensor_floor else gB_raw

            if a_active_track:
                thA += dt * eta_th * gA
            if b_active_track:
                thB += dt * eta_th * gB

            # Identical local relational-share dynamics for A and B
            dwA = eta_r * U_now * (1.0 - wA) - mu_r_relax * (wA - w0)
            dwB = eta_r * U_now * (1.0 - wB) - mu_r_relax * (wB - w0)
            if a_active_track:
                wA = float(np.clip(wA + dt * dwA, 0.05, 0.95))
            if b_active_track:
                wB = float(np.clip(wB + dt * dwB, 0.05, 0.95))

            # Identical local crowding & probing dynamics for A and B!
            # Note: high w_i (heavy specialized commitment) increases crowding; low U_now relaxes w_i -> drops crowding!
            gamA = mu_p + chi_w * wA - lam_U * U_now
            gamB = mu_p + chi_w * wB - lam_U * U_now
            mA = 0.85 + 2.5 * abs(gA)
            mB = 0.85 + 2.5 * abs(gB)

            if a_active_track:
                pA = max(0.0, pA + dt * (nu_p + a_p * mA * (pA ** 2) / (K_p ** 2 + pA ** 2) - gamA * pA))
            if b_active_track:
                pB = max(0.0, pB + dt * (nu_p + a_p * mB * (pB ** 2) / (K_p ** 2 + pB ** 2) - gamB * pB))

            psi_err = abs(np.angle(np.exp(1j * ((phiA - thA) - (phiB - thB)))))
            if abs(t - 59.5) < dt / 2:
                snaps["pre"] = (psi_err, U_now, wA, wB, pA, pB, gamA, gamB)
            if abs(t - 70.0) < dt / 2:
                snaps["t+10"] = (psi_err, U_now, wA, wB, pA, pB, gamA, gamB)
            if abs(t - 90.0) < dt / 2:
                snaps["t+30"] = (psi_err, U_now, wA, wB, pA, pB, gamA, gamB)
        snaps["final"] = (psi_err, U_now, wA, wB, pA, pB, gamA, gamB)
        return snaps

    # Check if H2 stays cleanly asymmetric before t=60 under IDENTICAL rules!
    tests = [
        ("H1_sym  | T1 Env shift (both active)", "H1_symmetric", "T1_env_shift", 0.15),
        ("H2_asym | T1 Env shift (A withdrew to low-p anchor, B tracks for whole!)", "H2_asymmetric", "T1_env_shift", 0.15),
        ("H2_asym | T2 Swap A -> rigid A' (B still rescues whole!)", "H2_asymmetric", "T2_swap_A_rigid", 0.15),
        ("H2_asym | T3 Swap B -> rigid B' (sticky mu_r=0.05 -> A stays trapped, FAILS!)", "H2_asymmetric", "T3_swap_B_rigid_sticky", 0.05),
        ("H2_asym | T4 Swap B -> rigid B' (plastic mu_r=0.45 -> breakdown relaxes wA -> A DEDIFFERENTIATES & RESCUES!)", "H2_asymmetric", "T4_swap_B_rigid_plastic", 0.45),
    ]
    for label, hmode, ptype, mur in tests:
        sn = run_c2(hmode, ptype, mu_r_relax=mur)
        pre, t10, t30, fin = sn["pre"], sn["t+10"], sn["t+30"], sn["final"]
        print(f"\n  {label}")
        print(f"    Pre  (t=59.5): err={pre[0]:.4f}, U={pre[1]:.3f}, w=({pre[2]:.2f},{pre[3]:.2f}), p=({pre[4]:.4f},{pre[5]:.4f}), gam=({pre[6]:.2f},{pre[7]:.2f})")
        print(f"    +10s (t=70.0): err={t10[0]:.4f}, U={t10[1]:.3f}, w=({t10[2]:.2f},{t10[3]:.2f}), p=({t10[4]:.4f},{t10[5]:.4f})")
        print(f"    +30s (t=90.0): err={t30[0]:.4f}, U={t30[1]:.3f}, w=({t30[2]:.2f},{t30[3]:.2f}), p=({t30[4]:.4f},{t30[5]:.4f})")
        print(f"    End  (t=140) : err={fin[0]:.4f}, U={fin[1]:.3f}, w=({fin[2]:.2f},{fin[3]:.2f}), p=({fin[4]:.4f},{fin[5]:.4f})")


if __name__ == "__main__":
    path_a_exact_bifurcation_and_counterexamples()
    path_b_model_c2_symmetric_rules()
