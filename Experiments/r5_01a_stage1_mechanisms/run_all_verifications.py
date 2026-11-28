#!/usr/bin/env python3
"""
R5-01A Stage-1 Calibrated Reproducible Verification Suite
=========================================================
Non-canonical research verification package for SRT R5-01A (Stage 1 archive).
Self-contained, deterministic (fixed seeds), outputs JSON summary to
`results_calibrated.json` in the same directory.

Covers:
1. Divisive normalization exact eigenvalue & beta=alpha peak verification.
2. Model S1: Strict 2+1 replicator simplex (equation-hardcoded absorbing faces).
3. Model S2: Non-absorbing variable-capacity 2+1 system:
   - Exact scalar folds (Gamma_low, Gamma_high) & cubic roots at Gamma=1.80;
   - Exact FULL 5D equilibria & 5x5 Jacobian eigenvalues (proving single-aligned
     state is a 5D phase-saddle while dual-aligned state at chi=1.55 is strictly
     5D asymptotically stable);
   - Exact coupled upper fold chi_c_dual, critical zero eigenvalue, transversality
     (v_L^T dF/dchi != 0), and quadratic non-degeneracy (a_SN != 0);
   - Saddle-node ghost lifetime numerical trend (both wide & near-fold ranges);
   - Precision Calibration 1: Superlinear capacity A-1a (lambda=2.5 < 8*C0, level
     elevation only) vs A-1b (lambda=12.0 > 8*C0, true negative-slope dGamma/dW < 0
     at equilibrium!) vs A-2 (constant C0, functional backgrounding load-drop).
4. Mature baselines on identical two-switch protocol:
   - Fixed-dither ESC, Decaying-dither ESC (Form A noiseless, Form A + floor, Form B),
     Utility-selective reset (Dohare et al. 2024 analogue).
5. Model C2: Symmetric cross-organization co-generative capability model:
   - Strictly operational +/-h differencing of even scalar U_AB (zero smuggled sin(psi));
   - Four-way calibration: (a) different initial states, (b) IDENTICAL initial state
     experiencing different transient past histories, (c) parameter-viscosity
     sensitivity (labeled separately), (d) four-regime perturbation & partner-swap
     (T1 env shift, T2 anchor swap, T3a moderate lock-in, T3b metastabilizing
     dedifferentiation rescue, T3d antipodal void awakening);
   - Exact analytical void-awakening inequality verification.
"""

from __future__ import annotations

import json
from pathlib import Path
import numpy as np
from scipy.optimize import root


OUT_PATH = Path(__file__).resolve().parent / "results_calibrated.json"


def phi_match(psi: float) -> float:
    return float(0.5 * (1.0 + np.cos(psi)))


def numeric_jacobian(f, x: np.ndarray, eps: float = 1e-7) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    n = len(x)
    J = np.zeros((n, n), dtype=float)
    for j in range(n):
        dx = np.zeros(n, dtype=float)
        dx[j] = eps
        J[:, j] = (f(x + dx) - f(x - dx)) / (2.0 * eps)
    return J


# =============================================================================
# 1. Divisive Normalization Exact Eigenvalue Check
# =============================================================================

def verify_divisive_normalization() -> dict:
    alpha, eps, x = 1.0, 0.2, 1.0
    rows = []
    for b in [0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 3.85, 4.0]:
        D = eps + (alpha + b) * x
        lam_plus = eps / (D ** 2)
        lam_minus = (eps + 2.0 * b * x) / (D ** 2)
        dlam_minus_db = 2.0 * (x ** 2) * (alpha - b) / (D ** 3)
        rows.append({
            "beta": b,
            "lambda_plus": round(lam_plus, 6),
            "lambda_minus": round(lam_minus, 6),
            "d_lambda_minus_dbeta": round(dlam_minus_db, 6),
            "ratio_minus_over_plus": round(lam_minus / lam_plus, 4),
        })
    # Assert exact peak at beta = alpha
    peak_row = [r for r in rows if r["beta"] == 1.0][0]
    assert abs(peak_row["d_lambda_minus_dbeta"]) < 1e-12
    assert peak_row["lambda_minus"] == max(r["lambda_minus"] for r in rows)
    return {"alpha": alpha, "eps": eps, "symmetric_input_x": x, "rows": rows}


# =============================================================================
# 2. Model S1: Strict 2+1 Replicator Simplex (Equation-Hardcoded Absorbing Faces)
# =============================================================================

def verify_s1_simplex() -> dict:
    dt = 0.01
    eps, alpha, beta = 0.2, 1.0, 0.8
    g_fg, g_p, c_p = 1.5, 2.5, 0.35
    eta_th, h_max, K_h = 0.8, 0.6, 0.15

    results = {}
    for label, p0, w20 in [
        ("exact_absorbing_face", 0.0, 0.0),
        ("near_collapsed", 1e-4, 1e-4),
        ("moderate_initial_reserve", 0.2, 0.2),
    ]:
        w1, w2, p = 1.0 - w20 - p0, w20, p0
        th1, th2 = 0.2, 0.2
        n1, n2 = 4000, 4000
        for step in range(n1 + n2):
            dphi1, dphi2 = (0.0, np.pi) if step < n1 else (2.4, 0.3)
            A = w1 * phi_match(dphi1 - th1)
            B = w2 * phi_match(dphi2 - th2)
            u1 = A / (eps + alpha * A + beta * B)
            u2 = B / (eps + alpha * B + beta * A)
            h = h_max * p / (p + K_h) if p > 0 else 0.0
            b1 = -np.sin(dphi1 - th1) * np.sin(h)
            b2 = -np.sin(dphi2 - th2) * np.sin(h)
            f1, f2 = g_fg * u1, g_fg * u2
            f_p = g_p * (abs(b1) + abs(b2)) - c_p
            f_bar = w1 * f1 + w2 * f2 + p * f_p
            w1_n = w1 + dt * w1 * (f1 - f_bar)
            w2_n = w2 + dt * w2 * (f2 - f_bar)
            p_n = p + dt * p * (f_p - f_bar)
            tot = w1_n + w2_n + p_n
            w1, w2, p = w1_n / tot, w2_n / tot, p_n / tot
            th1 += dt * eta_th * (-b1)
            th2 += dt * eta_th * (-b2)
            if step == n1 - 1:
                p1_snap = {"w1": w1, "w2": w2, "p": p, "u1": u1}
        err1 = abs(np.angle(np.exp(1j * (2.4 - th1))))
        err2 = abs(np.angle(np.exp(1j * (0.3 - th2))))
        results[label] = {
            "init": {"w1": 1.0 - w20 - p0, "w2": w20, "p": p0},
            "end_phase1": p1_snap,
            "end_phase2": {"w1": w1, "w2": w2, "p": p, "err1_rad": round(float(err1), 4), "err2_rad": round(float(err2), 4)},
        }
    return results


# =============================================================================
# 3. Model S2: Full 5D Coupled Analysis, Fold Non-Degeneracy & Counterexamples
# =============================================================================

S2_BASE = dict(
    eps=0.2, alpha=1.0, beta=0.8,
    nu_w=0.01, eta_w=1.4, mu_w=0.25, gamma_cap=0.7,
    nu_p=0.015, a_p=1.7, K_p=0.35, mu_p=0.65,
    C0=1.0, K_s=0.5, m0=0.85, kappa_b=0.6,
    eta_th=1.2, h_max=0.7, K_h=0.25,
)


def s2_capacity_and_deriv(W: float, lam_surplus: float, cap_mode: str, C0: float, K_s: float) -> tuple[float, float]:
    if cap_mode == "concave":
        C = C0 + lam_surplus * W / (K_s + W)
        dC = lam_surplus * K_s / ((K_s + W) ** 2)
    elif cap_mode == "superlinear":
        C = C0 + lam_surplus * (W ** 2) / (K_s ** 2 + W ** 2)
        dC = lam_surplus * 2.0 * W * (K_s ** 2) / ((K_s ** 2 + W ** 2) ** 2)
    elif cap_mode == "constant":
        C, dC = C0, 0.0
    else:
        raise ValueError(cap_mode)
    return C, dC


def s2_rhs_5d(
    state: np.ndarray,
    chi_crowd: float,
    dphi1: float,
    dphi2: float,
    lam_surplus: float = 0.5,
    cap_mode: str = "concave",
    K_s_override: float | None = None,
    kappa_auto: float = 0.0,
    smooth_mismatch: bool = True,
) -> np.ndarray:
    """
    Full 5D autonomous vector field on (w1, w2, p, th1, th2).
    smooth_mismatch=True uses m_sig = m0 + kappa_b * (b1^2 + b2^2), which is C^inf at
    aligned equilibria (b1=b2=0) and shares the EXACT same aligned equilibria as |b1|+|b2|.
    """
    w1, w2, p, th1, th2 = state
    P = S2_BASE
    K_s = P["K_s"] if K_s_override is None else K_s_override

    Phi1 = 0.5 * (1.0 + np.cos(dphi1 - th1))
    Phi2 = 0.5 * (1.0 + np.cos(dphi2 - th2))
    A, B = w1 * Phi1, w2 * Phi2
    u1 = A / (P["eps"] + P["alpha"] * A + P["beta"] * B)
    u2 = B / (P["eps"] + P["alpha"] * B + P["beta"] * A)

    aligned_work = A + B
    C_tot, _ = s2_capacity_and_deriv(aligned_work, lam_surplus, cap_mode, P["C0"], K_s)

    L_fg = w1 * (1.0 - kappa_auto * (Phi1 ** 2)) + w2 * (1.0 - kappa_auto * (Phi2 ** 2))
    gamma_eff = P["mu_p"] + chi_crowd * (L_fg / C_tot)

    h = P["h_max"] * p / (p + P["K_h"]) if p > 0 else 0.0
    b1 = -np.sin(dphi1 - th1) * np.sin(h)
    b2 = -np.sin(dphi2 - th2) * np.sin(h)
    m_sig = P["m0"] + P["kappa_b"] * ((b1 ** 2 + b2 ** 2) if smooth_mismatch else (abs(b1) + abs(b2)))

    dw1 = P["nu_w"] + P["eta_w"] * u1 * Phi1 - P["mu_w"] * w1 - P["gamma_cap"] * w1 * (w1 + w2 + p) / C_tot
    dw2 = P["nu_w"] + P["eta_w"] * u2 * Phi2 - P["mu_w"] * w2 - P["gamma_cap"] * w2 * (w1 + w2 + p) / C_tot
    dp = P["nu_p"] + P["a_p"] * m_sig * (p ** 2) / (P["K_p"] ** 2 + p ** 2) - gamma_eff * p
    dth1 = P["eta_th"] * (-b1)
    dth2 = P["eta_th"] * (-b2)
    return np.array([dw1, dw2, dp, dth1, dth2], dtype=float)


def verify_s2_full_5d_and_calibrations() -> dict:
    P = S2_BASE
    # 3.1 Exact scalar folds & Gamma=1.80 cubic roots
    gamma = 1.80
    a_m0 = P["a_p"] * P["m0"]  # 1.445
    coeffs = [gamma, -(P["nu_p"] + a_m0), gamma * (P["K_p"] ** 2), -P["nu_p"] * (P["K_p"] ** 2)]
    roots_180 = np.sort(np.roots(coeffs).real)
    ps = np.linspace(1e-4, 3.0, 300000)
    g_curve = (P["nu_p"] + a_m0 * (ps ** 2) / (P["K_p"] ** 2 + ps ** 2)) / ps
    dg = np.diff(g_curve)
    min_i = np.where((dg[:-1] < 0) & (dg[1:] > 0))[0][0] + 1
    max_i = np.where((dg[:-1] > 0) & (dg[1:] < 0))[0][0] + 1
    scalar_summary = {
        "a_p_times_m0": round(a_m0, 6),
        "gamma_low": round(float(g_curve[min_i]), 6),
        "p_low_fold": round(float(ps[min_i]), 6),
        "gamma_high": round(float(g_curve[max_i]), 6),
        "p_high_fold": round(float(ps[max_i]), 6),
        "roots_at_gamma_1_80": [round(float(r), 6) for r in roots_180],
    }
    assert abs(roots_180[0] - 0.008846) < 1e-5
    assert abs(roots_180[1] - 0.187816) < 1e-5
    assert abs(roots_180[2] - 0.614450) < 1e-5

    # 3.2 Full 5D equilibria & Jacobian spectrum (Calibration 2!)
    # Environment: dphi1=0, dphi2=pi
    # Single-aligned: th1=0, th2=0 (antipodal on ch2 -> Phi1=1, Phi2=0)
    # Dual-aligned:   th1=0, th2=pi (both aligned -> Phi1=1, Phi2=1)
    single_5d = {}
    dual_5d = {}
    for chi in [1.45, 1.55, 1.58, 1.59, 1.65]:
        # Single-aligned 5D equilibrium (fix th1=0, th2=0; solve (w1,w2,p) then evaluate FULL 5x5 Jacobian!)
        f_full = lambda s: s2_rhs_5d(s, chi, 0.0, np.pi)
        sol_s = root(f_full, [1.1, 0.01, 0.5, 0.0, 0.0], tol=1e-13)
        if sol_s.success and np.linalg.norm(f_full(sol_s.x)) < 1e-10 and sol_s.x[2] > 0.1:
            J5 = numeric_jacobian(f_full, sol_s.x)
            eigs5 = np.sort(np.linalg.eigvals(J5).real)
            eigs3 = np.sort(np.linalg.eigvals(J5[:3, :3]).real)
            single_5d[f"{chi:.2f}"] = {
                "state": [round(float(v), 6) for v in sol_s.x],
                "subspace_3d_eigs_real": [round(float(e), 6) for e in eigs3],
                "full_5d_eigs_real": [round(float(e), 6) for e in eigs5],
                "stable_3d_subspace": bool(np.max(eigs3) < 0),
                "stable_full_5d": bool(np.max(eigs5) < 0),
                "positive_phase_eigenvalue": round(float(np.max(eigs5)), 6),
            }

        # Dual-aligned 5D equilibrium (th1=0, th2=pi)
        sol_d = root(f_full, [0.6, 0.6, 0.45, 0.0, np.pi], tol=1e-13)
        if sol_d.success and np.linalg.norm(f_full(sol_d.x)) < 1e-10 and sol_d.x[2] > 0.1:
            J5 = numeric_jacobian(f_full, sol_d.x)
            eigs5 = np.sort(np.linalg.eigvals(J5).real)
            w1, w2, p, _, _ = sol_d.x
            C, _ = s2_capacity_and_deriv(w1 + w2, 0.5, "concave", P["C0"], P["K_s"])
            G = P["mu_p"] + chi * (w1 + w2) / C
            dual_5d[f"{chi:.2f}"] = {
                "exists": True,
                "state_w1_w2_p": [round(float(w1), 6), round(float(w2), 6), round(float(p), 6)],
                "gamma_eff": round(float(G), 6),
                "full_5d_eigs_real": [round(float(e), 6) for e in eigs5],
                "stable_full_5d": bool(np.max(eigs5) < 0),
            }
        else:
            sol_lo = root(f_full, [0.7, 0.7, 0.007, 0.0, np.pi], tol=1e-13)
            J5_lo = numeric_jacobian(f_full, sol_lo.x)
            eigs5_lo = np.sort(np.linalg.eigvals(J5_lo).real)
            dual_5d[f"{chi:.2f}"] = {
                "exists": False,
                "low_eq_w1_w2_p": [round(float(v), 6) for v in sol_lo.x[:3]],
                "low_eq_full_5d_eigs_real": [round(float(e), 6) for e in eigs5_lo],
                "low_eq_stable_full_5d": bool(np.max(eigs5_lo) < 0),
            }

    assert single_5d["1.65"]["stable_3d_subspace"] is True
    assert single_5d["1.65"]["stable_full_5d"] is False  # Phase saddle!
    assert dual_5d["1.55"]["stable_full_5d"] is True     # Strictly 5D stable!
    assert dual_5d["1.65"]["exists"] is False            # Annihilated!

    # 3.3 Exact Coupled Upper Fold chi_c_dual via Augmented Saddle-Node System {F=0, det(J_3x3)=0}
    def fold_aug_sys(z: np.ndarray) -> np.ndarray:
        w, p, chi = z
        s = np.array([w, w, p, 0.0, np.pi], dtype=float)
        f5 = s2_rhs_5d(s, chi, 0.0, np.pi)
        J3 = numeric_jacobian(lambda u: s2_rhs_5d(np.array([u[0], u[1], u[2], 0.0, np.pi]), chi, 0.0, np.pi)[:3],
                              np.array([w, w, p], dtype=float))
        return np.array([f5[0], f5[2], np.linalg.det(J3)], dtype=float)

    sol_fold = root(fold_aug_sys, [0.618, 0.35, 1.5888], tol=1e-13)
    assert sol_fold.success and np.linalg.norm(fold_aug_sys(sol_fold.x)) < 1e-10
    w_c, p_c, chi_c = [float(v) for v in sol_fold.x]
    x_c = np.array([w_c, w_c, p_c, 0.0, np.pi], dtype=float)
    J_c = numeric_jacobian(lambda s: s2_rhs_5d(s, chi_c, 0.0, np.pi), x_c)
    evals, evecs_R = np.linalg.eig(J_c)
    idx_zero = int(np.argmin(np.abs(evals)))
    lam_crit = float(evals[idx_zero].real)
    v_R = evecs_R[:, idx_zero].real
    v_R = v_R / np.linalg.norm(v_R)
    evals_L, evecs_L = np.linalg.eig(J_c.T)
    idx_zero_L = int(np.argmin(np.abs(evals_L)))
    v_L = evecs_L[:, idx_zero_L].real
    v_L = v_L / float(np.dot(v_L, v_R))  # bi-orthonormal: v_L^T v_R = 1

    # Transversality: v_L^T (dF/dchi)
    eps_chi = 1e-6
    dF_dchi = (s2_rhs_5d(x_c, chi_c + eps_chi, 0.0, np.pi) - s2_rhs_5d(x_c, chi_c - eps_chi, 0.0, np.pi)) / (2.0 * eps_chi)
    transversality = float(np.dot(v_L, dF_dchi))

    # Quadratic non-degeneracy: a_SN = 0.5 * v_L^T D^2 F[v_R, v_R]
    eps_q = 1e-4
    f_c = s2_rhs_5d(x_c, chi_c, 0.0, np.pi)
    f_plus = s2_rhs_5d(x_c + eps_q * v_R, chi_c, 0.0, np.pi)
    f_minus = s2_rhs_5d(x_c - eps_q * v_R, chi_c, 0.0, np.pi)
    d2F_vRvR = (f_plus - 2.0 * f_c + f_minus) / (eps_q ** 2)
    a_SN = 0.5 * float(np.dot(v_L, d2F_vRvR))

    other_eigs = sorted([float(evals[i].real) for i in range(5) if i != idx_zero])
    fold_cert = {
        "chi_c_dual": round(float(chi_c), 8),
        "x_c_w1_w2_p": [round(float(v), 6) for v in x_c[:3]],
        "critical_eigenvalue": float(f"{lam_crit:.3e}"),
        "remaining_4_eigs_real": [round(e, 6) for e in other_eigs],
        "transversality_vL_dFdchi": round(transversality, 6),
        "quadratic_nondegeneracy_aSN": round(a_SN, 6),
        "nondegenerate_saddle_node_certified": bool(
            abs(lam_crit) < 1e-7 and max(other_eigs) < -0.05 and abs(transversality) > 0.01 and abs(a_SN) > 0.05
        ),
    }
    assert fold_cert["nondegenerate_saddle_node_certified"] is True

    # 3.4 Ghost lifetime numerical trend (near-fold asymptotic + wide range)
    def ghost_time(dchi: float) -> float:
        dt = 0.01
        s = np.array([0.61, 0.61, 0.50, 0.0, np.pi], dtype=float)
        for step in range(400000):
            s = s + dt * s2_rhs_5d(s, chi_c + dchi, 0.0, np.pi)
            s[:3] = np.maximum(0.0, s[:3])
            if s[2] < 0.10:
                return step * dt
        return float("nan")

    near_dchis = [0.0002, 0.0005, 0.001, 0.002, 0.005]
    wide_dchis = [0.005, 0.01, 0.02, 0.04, 0.08]
    near_taus = [ghost_time(dc) for dc in near_dchis]
    wide_taus = [ghost_time(dc) for dc in wide_dchis]
    slope_near = float(np.polyfit(np.log(near_dchis), np.log(near_taus), 1)[0])
    slope_wide = float(np.polyfit(np.log(wide_dchis), np.log(wide_taus), 1)[0])
    ghost_trend = {
        "near_fold": [
            {"dchi": dc, "tau": round(t, 2), "tau_sqrt_dchi": round(t * np.sqrt(dc), 4)}
            for dc, t in zip(near_dchis, near_taus)
        ],
        "loglog_slope_near_fold": round(slope_near, 4),
        "wide_range": [
            {"dchi": dc, "tau": round(t, 2), "tau_sqrt_dchi": round(t * np.sqrt(dc), 4)}
            for dc, t in zip(wide_dchis, wide_taus)
        ],
        "loglog_slope_wide_range": round(slope_wide, 4),
    }

    # 3.5 Precision Calibration 1: A-1a (lambda=2.5 < 8 C0) vs A-1b (lambda=12.0 > 8 C0) vs A-2 (backgrounding)
    # Verify exact analytical threshold lambda > 8 C0
    xs = np.linspace(0.0, 1.0, 100001)
    q_vals = xs * (1.0 - xs) / ((1.0 + xs) ** 2)
    q_max = float(np.max(q_vals))
    x_argmax = float(xs[int(np.argmax(q_vals))])
    assert abs(q_max - 0.125) < 1e-9
    assert abs(x_argmax - 1.0 / 3.0) < 1e-5

    def eval_counterexample(label, chi, lam, cap_mode, K_s_ov, k_auto):
        f_ce = lambda s: s2_rhs_5d(s, chi, 0.0, np.pi, lam_surplus=lam, cap_mode=cap_mode,
                                   K_s_override=K_s_ov, kappa_auto=k_auto)
        sol = root(f_ce, [0.7, 0.7, 0.7, 0.0, np.pi], tol=1e-13)
        assert sol.success and np.linalg.norm(f_ce(sol.x)) < 1e-10
        J5 = numeric_jacobian(f_ce, sol.x)
        eigs5 = np.sort(np.linalg.eigvals(J5).real)
        W = float(sol.x[0] + sol.x[1])
        C, dC = s2_capacity_and_deriv(W, lam, cap_mode, P["C0"], K_s_ov)
        elast = float(W * dC / C)
        dGamma_dW = float(chi * (1.0 - k_auto) * (C - W * dC) / (C ** 2))
        return {
            "label": label,
            "chi": chi, "lambda": lam, "K_s": K_s_ov, "kappa_auto": k_auto,
            "W_star": round(W, 6), "p_star": round(float(sol.x[2]), 6),
            "C_star": round(C, 6), "elasticity_E_CW": round(elast, 6),
            "dGamma_dW_at_eq": round(dGamma_dW, 6),
            "max_Re_eig_5d": round(float(np.max(eigs5)), 6),
            "stable_full_5d": bool(np.max(eigs5) < 0),
        }

    counterexamples = {
        "analytical_threshold_lambda_over_C0": 8.0,
        "q_max_verified": round(q_max, 8),
        "x_argmax_verified": round(x_argmax, 8),
        "A1a_level_elevation_only": eval_counterexample(
            "A-1a: lambda=2.5 < 8*C0 (level elevation ONLY, dGamma/dW > 0 everywhere!)",
            chi=1.65, lam=2.5, cap_mode="superlinear", K_s_ov=1.4, k_auto=0.0,
        ),
        "A1b_true_negative_slope_chi165": eval_counterexample(
            "A-1b: lambda=12.0 > 8*C0, K=4.0 (TRUE E_{C,W} > 1 & dGamma/dW < 0 at coupled eq!)",
            chi=1.65, lam=12.0, cap_mode="superlinear", K_s_ov=4.0, k_auto=0.0,
        ),
        "A1b_true_negative_slope_chi210": eval_counterexample(
            "A-1b: lambda=12.0 > 8*C0, K=4.0, chi=2.10 (TRUE E_{C,W} > 1 & dGamma/dW < 0 at coupled eq!)",
            chi=2.10, lam=12.0, cap_mode="superlinear", K_s_ov=4.0, k_auto=0.0,
        ),
        "A2_constant_C0_backgrounding_chi165": eval_counterexample(
            "A-2: constant C0=1, lambda=0, backgrounding kappa_auto=0.35, chi=1.65",
            chi=1.65, lam=0.0, cap_mode="constant", K_s_ov=0.5, k_auto=0.35,
        ),
        "A2_constant_C0_backgrounding_chi200": eval_counterexample(
            "A-2: constant C0=1, lambda=0, backgrounding kappa_auto=0.50, chi=2.00",
            chi=2.00, lam=0.0, cap_mode="constant", K_s_ov=0.5, k_auto=0.50,
        ),
    }
    assert counterexamples["A1a_level_elevation_only"]["dGamma_dW_at_eq"] > 0
    assert counterexamples["A1b_true_negative_slope_chi165"]["dGamma_dW_at_eq"] < 0
    assert counterexamples["A1b_true_negative_slope_chi165"]["elasticity_E_CW"] > 1.0
    assert counterexamples["A1b_true_negative_slope_chi165"]["stable_full_5d"] is True
    assert counterexamples["A2_constant_C0_backgrounding_chi200"]["stable_full_5d"] is True

    # 3.6 P1-02: Explicit Two-Switch Phase-Perturbation Control at chi=1.65 (Case 4)
    # Separates (a) saddle-escape waiting time from the exact antipodal invariant subspace
    # (sin(pi)=0) vs (b) post-alignment saddle-node ghost extinction time after dual alignment.
    def run_s2_two_switch_control(mode: str, pert_rad: float = 0.0, T_tot: float = 400.0) -> dict:
        dt = 0.01
        lam_s, chi = 0.5, 1.65
        w1, w2, p = 0.9, 0.05, 0.01
        th1, th2 = 0.0, 0.0
        snaps = {}
        t_align_dual = None
        t_extinct = None
        for step in range(int(T_tot / dt)):
            t = step * dt
            if t < 40.0:
                dphi1, dphi2 = 0.0, np.pi
            elif t < 75.0:
                dphi1, dphi2 = np.pi, 1.2
            else:
                dphi1, dphi2 = np.pi, -1.3

            # Explicit small phase perturbation off exact antipodal saddle at Switch 1 (t=40)
            if mode == "explicit_perturbation" and step == 4000:
                th1 += pert_rad

            Phi1 = 0.5 * (1.0 + np.cos(dphi1 - th1))
            Phi2 = 0.5 * (1.0 + np.cos(dphi2 - th2))
            A, B = w1 * Phi1, w2 * Phi2
            u1 = A / (P["eps"] + P["alpha"] * A + P["beta"] * B)
            u2 = B / (P["eps"] + P["alpha"] * B + P["beta"] * A)
            C_tot = P["C0"] + lam_s * (A + B) / (P["K_s"] + A + B)
            h = P["h_max"] * p / (p + P["K_h"]) if p > 0 else 0.0

            # In strict_antipodal_clamp, enforce exact mathematical sin(pi) = 0 on ch1 once at antipodal
            if mode == "strict_antipodal_clamp" and t >= 40.0 and abs(abs(np.angle(np.exp(1j * (dphi1 - th1)))) - np.pi) < 1e-12:
                b1 = 0.0
            else:
                b1 = -np.sin(dphi1 - th1) * np.sin(h)
            b2 = -np.sin(dphi2 - th2) * np.sin(h)

            I_ext = 0.40 if (45.0 <= t <= 52.0) else 0.0
            gamma_eff = P["mu_p"] + chi * (w1 + w2) / C_tot
            m_sig = P["m0"] + P["kappa_b"] * (abs(b1) + abs(b2))

            dw1 = P["nu_w"] + P["eta_w"] * u1 * Phi1 - P["mu_w"] * w1 - P["gamma_cap"] * w1 * (w1 + w2 + p) / C_tot
            dw2 = P["nu_w"] + P["eta_w"] * u2 * Phi2 - P["mu_w"] * w2 - P["gamma_cap"] * w2 * (w1 + w2 + p) / C_tot
            dp = P["nu_p"] + P["a_p"] * m_sig * (p ** 2) / (P["K_p"] ** 2 + p ** 2) + I_ext - gamma_eff * p

            w1 = max(0.0, w1 + dt * dw1)
            w2 = max(0.0, w2 + dt * dw2)
            p = max(0.0, p + dt * dp)
            th1 += dt * P["eta_th"] * (-b1)
            th2 += dt * P["eta_th"] * (-b2)

            err1 = abs(np.angle(np.exp(1j * (dphi1 - th1))))
            err2 = abs(np.angle(np.exp(1j * (dphi2 - th2))))
            if t >= 75.0 and t_align_dual is None and err1 < 0.2 and err2 < 0.2:
                t_align_dual = round(t, 2)
            if t >= 52.0 and t_extinct is None and p < 0.10:
                t_extinct = round(t, 2)

            if step == 7450:
                snaps["t74_5"] = {"w1": round(w1, 5), "w2": round(w2, 5), "p": round(p, 5), "err1": round(err1, 4), "err2": round(err2, 4)}
            if step == 12000:
                snaps["t120"] = {"w1": round(w1, 5), "w2": round(w2, 5), "p": round(p, 5), "err1": round(err1, 4), "err2": round(err2, 4)}
        snaps["t400"] = {"w1": round(w1, 5), "w2": round(w2, 5), "p": round(p, 5), "err1": round(err1, 4), "err2": round(err2, 4)}
        snaps["t_dual_aligned"] = t_align_dual
        snaps["t_extinct_p_below_0_10"] = t_extinct
        return snaps

    two_switch_perturbation_control = {
        "chi": 1.65,
        "lam_surplus": 0.5,
        "scaffold_pulse": {"I_ext": 0.40, "window": [45.0, 52.0]},
        "strict_antipodal_clamp": run_s2_two_switch_control("strict_antipodal_clamp"),
        "standard_float_roundoff": run_s2_two_switch_control("standard_float_roundoff"),
        "explicit_perturbation_1e-3_rad": run_s2_two_switch_control("explicit_perturbation", pert_rad=1e-3),
    }
    # Assert exact structural separation:
    # 1. Strict antipodal clamp stays permanently on single-aligned 3D saddle (p ~ 0.4516 at t=400)
    assert two_switch_perturbation_control["strict_antipodal_clamp"]["t400"]["p"] > 0.40
    # 2. Standard float roundoff escapes late -> still high at t=120, extinct by t=400
    assert two_switch_perturbation_control["standard_float_roundoff"]["t120"]["p"] > 0.40
    assert two_switch_perturbation_control["standard_float_roundoff"]["t400"]["p"] < 0.02
    # 3. Explicit 1e-3 rad perturbation escapes promptly -> already extinct by t=120 & t=400
    assert two_switch_perturbation_control["explicit_perturbation_1e-3_rad"]["t120"]["p"] < 0.02
    assert two_switch_perturbation_control["explicit_perturbation_1e-3_rad"]["t400"]["p"] < 0.02

    return {
        "scalar_reduction": scalar_summary,
        "single_aligned_5d": single_5d,
        "dual_aligned_5d": dual_5d,
        "coupled_fold_certificate": fold_cert,
        "ghost_lifetime_trend": ghost_trend,
        "success_reproduction_counterexamples": counterexamples,
        "two_switch_phase_perturbation_control": two_switch_perturbation_control,
    }


# =============================================================================
# 4. Mature Baselines (Two-Switch Comparison: Fixed ESC, Form A/B ESC, Dohare 2024)
# =============================================================================

def verify_mature_baselines() -> dict:
    dt = 0.01
    n_steps = 12000

    # Fixed ESC
    th2, cost_f = 0.0, 0.0
    for step in range(n_steps):
        t = step * dt
        dphi2 = 0.0 if t < 40.0 else (1.2 if t < 75.0 else -1.3)
        h = 0.40
        b2 = -np.sin(dphi2 - th2) * np.sin(h)
        th2 += dt * 1.2 * (-b2)
        cost_f += dt * 0.5 * (1.0 - np.cos(h))
        if step == 7450:
            e1_f = abs(np.angle(np.exp(1j * (1.2 - th2))))
    e2_f = abs(np.angle(np.exp(1j * (-1.3 - th2))))

    def run_decay_esc(mode: str, noise_floor: float):
        th2, h, cost = 0.0, 0.40, 0.0
        for step in range(n_steps):
            t = step * dt
            dphi2 = 0.0 if t < 40.0 else (1.2 if t < 75.0 else -1.3)
            b_raw = -np.sin(dphi2 - th2) * np.sin(h)
            b_eff = 0.0 if abs(b_raw) < noise_floor else b_raw
            th2 += dt * 1.2 * (-b_eff)
            dh = (2.0 * abs(b_eff) - 0.5 * h) if mode == "A" else ((2.0 * abs(b_eff) - 0.5) * h)
            h = max(0.0, min(0.7, h + dt * dh))
            cost += dt * 0.5 * (1.0 - np.cos(h))
            if step == 7450:
                e1 = abs(np.angle(np.exp(1j * (1.2 - th2))))
                h1 = h
        e2 = abs(np.angle(np.exp(1j * (-1.3 - th2))))
        return {"err_S1": round(float(e1), 4), "h_S1": h1, "err_S2": round(float(e2), 4), "h_S2": h, "cost": round(cost, 3)}

    # Utility-selective reset (Dohare 2024 analogue)
    rng = np.random.default_rng(42)
    th2, util, resets = 0.0, 1.0, 0
    for step in range(n_steps):
        t = step * dt
        dphi2 = 0.0 if t < 40.0 else (1.2 if t < 75.0 else -1.3)
        perf = phi_match(dphi2 - th2)
        util = 0.99 * util + 0.01 * perf
        if util < 0.70 and (step % 150 == 0):
            th2 = float(rng.uniform(-np.pi, np.pi))
            resets += 1
        b2 = -np.sin(dphi2 - th2) * np.sin(0.15)
        th2 += dt * 1.2 * (-b2)
        if step == 7450:
            e1_cb = abs(np.angle(np.exp(1j * (1.2 - th2))))
    e2_cb = abs(np.angle(np.exp(1j * (-1.3 - th2))))

    return {
        "fixed_dither_ESC": {"err_S1": round(float(e1_f), 4), "err_S2": round(float(e2_f), 4), "dither_cost": round(cost_f, 3)},
        "decay_ESC_FormA_noiseless": run_decay_esc("A", 0.0),
        "decay_ESC_FormA_floor_1e-3": run_decay_esc("A", 1e-3),
        "decay_ESC_FormB_quadratic_noiseless": run_decay_esc("B", 0.0),
        "utility_selective_reset_Dohare24_analogue": {
            "err_S1": round(float(e1_cb), 4), "err_S2": round(float(e2_cb), 4), "resets": resets, "seed": 42,
        },
    }


# =============================================================================
# 5. Model C2: Symmetric Cross-Org Co-Generation + Four-Way History Calibration
# =============================================================================

def verify_c2_cross_org() -> dict:
    dt = 0.01
    g_AB = 1.6
    sensor_floor = 0.012
    nu_p, a_p, K_p = 0.015, 1.7, 0.35
    mu_p, chi_w, lam_U, w0 = 0.55, 1.85, 0.10, 0.12
    eta_th, h_max, K_h = 6.0, 0.50, 0.20

    def U_fn(phiA, phiB, tA, tB, wA, wB):
        return g_AB * wA * wB * phi_match((phiA - tA) - (phiB - tB))

    def run_c2(
        init_p=(0.50, 0.50),
        init_w=(0.60, 0.60),
        early_shock_A: tuple[float, float, float] | None = None,
        pert_type: str = "none",
        swap_psi: float = 2.55,
        mu_r: float = 0.45,
        eta_r: float = 1.0,
        T_tot: float = 160.0,
    ) -> dict:
        pA, pB = init_p
        wA, wB = init_w
        thA, thB = 0.0, 0.0
        delta_env, bias_B = 1.1, 0.0
        a_active, b_active = True, True
        rng = np.random.default_rng(123)
        # Note (P2-01): Theoretical local unidentifiability assumes stationary Uniform(S^1)
        # background phase independent of delta_env; the simulation initializes phi_bg=0.0
        # for deterministic comparability because phi_bg cancels identically in psi_AB.
        phi_bg = 0.0
        snaps = {}

        for step in range(int(T_tot / dt)):
            t = step * dt
            # Drifting common background phase (cancels identically in shared interface psi_AB)
            phi_bg = float((phi_bg + dt * 3.1 + np.sqrt(dt) * 1.2 * rng.standard_normal()) % (2.0 * np.pi))
            phiA = phi_bg + 0.5 * delta_env
            phiB = phi_bg - 0.5 * delta_env + bias_B

            if step == 6000:
                if pert_type == "T1_env_shift":
                    delta_env = -1.2
                elif pert_type == "T2_swap_A":
                    thA = thA + 2.2
                    pA = 0.01
                    a_active = False
                elif pert_type == "T3_swap_B":
                    bias_B = delta_env - thA - swap_psi
                    thB = 0.0
                    wB = 0.68
                    pB = 0.01
                    b_active = False

            U_now = U_fn(phiA, phiB, thA, thB, wA, wB)
            hA = h_max * pA / (pA + K_h)
            hB = h_max * pB / (pB + K_h)
            # Operational physical two-point perturbation differencing ONLY via even scalar U_AB!
            gA_raw = 0.5 * (U_fn(phiA, phiB, thA + hA, thB, wA, wB) - U_fn(phiA, phiB, thA - hA, thB, wA, wB))
            gB_raw = 0.5 * (U_fn(phiA, phiB, thA, thB + hB, wA, wB) - U_fn(phiA, phiB, thA, thB - hB, wA, wB))
            gA = 0.0 if abs(gA_raw) < sensor_floor else gA_raw
            gB = 0.0 if abs(gB_raw) < sensor_floor else gB_raw

            if a_active:
                thA += dt * eta_th * gA
            if b_active:
                thB += dt * eta_th * gB

            if a_active:
                wA = float(np.clip(wA + dt * (eta_r * U_now * (1.0 - wA) - mu_r * (wA - w0)), 0.05, 0.95))
            if b_active:
                wB = float(np.clip(wB + dt * (eta_r * U_now * (1.0 - wB) - mu_r * (wB - w0)), 0.05, 0.95))

            shock_A = 0.0
            if early_shock_A is not None and early_shock_A[0] <= t <= early_shock_A[1]:
                shock_A = early_shock_A[2]

            gamA = mu_p + chi_w * wA - lam_U * U_now + shock_A
            gamB = mu_p + chi_w * wB - lam_U * U_now
            if a_active:
                pA = max(0.0, pA + dt * (nu_p + a_p * (0.85 + 2.5 * abs(gA)) * (pA ** 2) / (K_p ** 2 + pA ** 2) - gamA * pA))
            if b_active:
                pB = max(0.0, pB + dt * (nu_p + a_p * (0.85 + 2.5 * abs(gB)) * (pB ** 2) / (K_p ** 2 + pB ** 2) - gamB * pB))

            psi_err = float(abs(np.angle(np.exp(1j * ((phiA - thA) - (phiB - thB))))))
            for ck_step, ck_name in [(5950, "pre_t59_5"), (16000, "t160"), (20000, "t200"), (40000, "t400")]:
                if step == ck_step:
                    snaps[ck_name] = {
                        "err": round(psi_err, 4), "U": round(U_now, 4),
                        "wA": round(wA, 4), "wB": round(wB, 4),
                        "pA": round(pA, 4), "pB": round(pB, 4),
                        "gamA": round(gamA, 4), "gamB": round(gamB, 4),
                    }
        # Analytical maximum achievable gradient signal ceiling at end state (state-conditional, P2-02)
        K_AB = g_AB * wA * wB
        S_max = 0.5 * K_AB * abs(np.sin(psi_err)) * np.sin(h_max)
        end_key = f"end_t{int(T_tot)}"
        snaps[end_key] = {
            "err": round(psi_err, 4), "U": round(U_now, 4),
            "wA": round(wA, 4), "wB": round(wB, 4),
            "pA": round(pA, 4), "pB": round(pB, 4),
            "gamA": round(gamA, 4), "gamB": round(gamB, 4),
            "signal_ceiling_S_max": round(float(S_max), 5),
            "below_sensor_floor": bool(S_max <= sensor_floor),
        }
        return snaps

    # Calibration 3b: IDENTICAL INITIAL STATE (0.50, 0.50) experiencing two different transient histories!
    same_init_sym = run_c2(init_p=(0.50, 0.50), init_w=(0.60, 0.60), early_shock_A=None, pert_type="T1_env_shift")
    same_init_asym_T1 = run_c2(init_p=(0.50, 0.50), init_w=(0.60, 0.60), early_shock_A=(5.0, 12.0, 1.5), pert_type="T1_env_shift")
    same_init_asym_T2 = run_c2(init_p=(0.50, 0.50), init_w=(0.60, 0.60), early_shock_A=(5.0, 12.0, 1.5), pert_type="T2_swap_A")
    same_init_asym_T3a = run_c2(init_p=(0.50, 0.50), init_w=(0.60, 0.60), early_shock_A=(5.0, 12.0, 1.5), pert_type="T3_swap_B", swap_psi=1.40)
    same_init_asym_T3b = run_c2(init_p=(0.50, 0.50), init_w=(0.60, 0.60), early_shock_A=(5.0, 12.0, 1.5), pert_type="T3_swap_B", swap_psi=2.55)
    same_init_asym_T3d = run_c2(init_p=(0.50, 0.50), init_w=(0.60, 0.60), early_shock_A=(5.0, 12.0, 1.5), pert_type="T3_swap_B", swap_psi=2.95)
    # P1-01 Calibration: Extend sticky parameter-viscosity control (T3c) to T=1000!
    # Reveals historical viscosity causes RECONFIGURATION DELAY (recovers after t~180), NOT permanent failure!
    param_sticky_T3c_T1000 = run_c2(
        init_p=(0.01, 0.70), init_w=(0.65, 0.65), early_shock_A=None,
        pert_type="T3_swap_B", swap_psi=2.55, mu_r=0.05, eta_r=0.11, T_tot=1000.0,
    )

    # Assert identical-initial-state history bifurcation actually worked!
    assert same_init_sym["pre_t59_5"]["pA"] > 0.60 and same_init_sym["pre_t59_5"]["pB"] > 0.60
    assert same_init_asym_T1["pre_t59_5"]["pA"] < 0.02 and same_init_asym_T1["pre_t59_5"]["pB"] > 0.60
    assert abs(same_init_sym["pre_t59_5"]["U"] - same_init_asym_T1["pre_t59_5"]["U"]) < 0.01
    # Assert T1 & T2 recovery despite withdrawn pA
    assert same_init_asym_T1["end_t160"]["err"] < 0.12
    assert same_init_asym_T2["end_t160"]["err"] < 0.12
    # Assert T3a degraded lock-in, T3b dedifferentiation rescue, T3d void awakening!
    assert same_init_asym_T3a["end_t160"]["err"] > 1.30 and same_init_asym_T3a["end_t160"]["pA"] < 0.02
    assert same_init_asym_T3b["end_t160"]["err"] < 0.12 and same_init_asym_T3b["end_t160"]["pA"] > 0.50
    assert same_init_asym_T3d["end_t160"]["err"] > 2.90 and same_init_asym_T3d["end_t160"]["pA"] > 1.50
    assert same_init_asym_T3d["end_t160"]["below_sensor_floor"] is True
    # Assert P1-01: sticky T3c still unrecovered at t=160, recovers by t=400 and stays recovered at t=1000!
    assert param_sticky_T3c_T1000["t160"]["err"] > 2.40 and param_sticky_T3c_T1000["t160"]["pA"] < 0.05
    assert param_sticky_T3c_T1000["t400"]["err"] < 0.12 and param_sticky_T3c_T1000["t400"]["pA"] > 0.50
    assert param_sticky_T3c_T1000["end_t1000"]["err"] < 0.12 and param_sticky_T3c_T1000["end_t1000"]["pA"] > 0.50

    return {
        "parameters": {
            "g_AB": g_AB, "sensor_floor": sensor_floor, "h_max": h_max, "K_h": K_h,
            "nu_p": nu_p, "a_p": a_p, "K_p": K_p, "mu_p": mu_p, "chi_w": chi_w,
            "lam_U": lam_U, "w0": w0, "eta_r": 1.0, "mu_r": 0.45, "seed": 123,
        },
        "same_initial_state_H_sym_T1": same_init_sym,
        "same_initial_state_H_asym_T1_env_shift": same_init_asym_T1,
        "same_initial_state_H_asym_T2_anchor_swap": same_init_asym_T2,
        "same_initial_state_H_asym_T3a_moderate_lockin": same_init_asym_T3a,
        "same_initial_state_H_asym_T3b_dediff_rescue": same_init_asym_T3b,
        "same_initial_state_H_asym_T3d_void_awakening": same_init_asym_T3d,
        "parameter_viscosity_delay_T3c_T1000": param_sticky_T3c_T1000,
    }


def main() -> None:
    results = {
        "suite": "SRT R5-01A Stage-1 Calibrated Reproducible Verification",
        "divisive_normalization": verify_divisive_normalization(),
        "model_s1_simplex": verify_s1_simplex(),
        "model_s2_full_5d": verify_s2_full_5d_and_calibrations(),
        "mature_baselines_two_switch": verify_mature_baselines(),
        "model_c2_cross_org": verify_c2_cross_org(),
    }
    OUT_PATH.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"[PASS] All assertions passed. Calibrated results written to {OUT_PATH}")
    print("\n--- Key Verified Highlights ---")
    s2 = results["model_s2_full_5d"]
    print("S2 scalar folds:", s2["scalar_reduction"])
    print("S2 fold cert   :", s2["coupled_fold_certificate"])
    print("S2 ghost slopes:", s2["ghost_lifetime_trend"]["loglog_slope_near_fold"], "(near),",
          s2["ghost_lifetime_trend"]["loglog_slope_wide_range"], "(wide)")
    ce = s2["success_reproduction_counterexamples"]
    print("A-1a (lam=2.5) :", ce["A1a_level_elevation_only"]["elasticity_E_CW"], ce["A1a_level_elevation_only"]["dGamma_dW_at_eq"])
    print("A-1b (lam=12.0):", ce["A1b_true_negative_slope_chi165"]["elasticity_E_CW"], ce["A1b_true_negative_slope_chi165"]["dGamma_dW_at_eq"])
    print("A-2  (bg k=0.5):", ce["A2_constant_C0_backgrounding_chi200"]["p_star"], ce["A2_constant_C0_backgrounding_chi200"]["max_Re_eig_5d"])
    c2 = results["model_c2_cross_org"]
    print("C2 same-init H_sym pre :", c2["same_initial_state_H_sym_T1"]["pre_t59_5"])
    print("C2 same-init H_asym pre:", c2["same_initial_state_H_asym_T1_env_shift"]["pre_t59_5"])
    print("C2 T3a moderate lock-in:", c2["same_initial_state_H_asym_T3a_moderate_lockin"]["end_t160"])
    print("C2 T3b dediff rescue   :", c2["same_initial_state_H_asym_T3b_dediff_rescue"]["end_t160"])
    print("C2 T3d void awakening  :", c2["same_initial_state_H_asym_T3d_void_awakening"]["end_t160"])
    print("C2 T3c sticky delay    :", {k: c2["parameter_viscosity_delay_T3c_T1000"][k] for k in ["t160", "t200", "t400", "end_t1000"]})
    p102 = s2["two_switch_phase_perturbation_control"]
    print("S2 P1-02 antipodal     :", p102["strict_antipodal_clamp"]["t120"]["p"], "->", p102["strict_antipodal_clamp"]["t400"]["p"])
    print("S2 P1-02 float roundoff:", p102["standard_float_roundoff"]["t120"]["p"], "->", p102["standard_float_roundoff"]["t400"]["p"], "t_ext=", p102["standard_float_roundoff"]["t_extinct_p_below_0_10"])
    print("S2 P1-02 explicit 1e-3 :", p102["explicit_perturbation_1e-3_rad"]["t120"]["p"], "->", p102["explicit_perturbation_1e-3_rad"]["t400"]["p"], "t_ext=", p102["explicit_perturbation_1e-3_rad"]["t_extinct_p_below_0_10"])


if __name__ == "__main__":
    main()
