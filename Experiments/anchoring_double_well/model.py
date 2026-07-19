"""
Plastic double-well toy, v2 (selective anchoring).

Upgrades over v1, per review corrections:
  #1  W_sel is a SELECTION-HISTORY-SPECIFIC directional functional difference:
      compare the landscape written by the actual selection history h+ (push
      toward M+) against a matched counterfactual history h- (push toward M-,
      equal magnitude/duration). W_sel = Phi_M(post-h+) - Phi_M(post-h-), with
      Phi_M in {stationary occupancy of M+, escape barrier, committor}.
  #2  RoughenWrite is an explicit NON-SPECIFIC negative control (big W_global,
      ~0 W_sel). A separate LatentInscription condition realizes low-P / high-W_sel.
  #3  Cost is split into J_ext (external control effort) and J_write (slow-variable
      dissipation). We do NOT claim total cost is independent of anchoring.
  #4  W_global is reported over three reference measures (uniform, pre-occupancy,
      mixture) and three divergences (KL, JS, TV).

Dynamics (Euler-Maruyama, additive noise):
  V(x;c)   = x^4/4 - a x^2/2 - c x
  V'(x;c)  = x^3 - a x - c            (c>0 tilts toward M+ = {x>0})
  x_{t+1}  = x_t - dt V'(x_t;c(z_t)) + dt u_t + sqrt(2 D(z_t) dt) xi
  z_{t+1}  = z_t + dt (eta phi(x_t) - lam z_t),   phi(x)=tanh(2x)
  DEEPEN  : c(z) = c0 + kappa z     (selection-specific: deepens occupied well)
  ROUGHEN : D(z) = D0 (1 + rho |z|) (non-specific: raises diffusion everywhere)
"""
from __future__ import annotations
import math
import numpy as np

A = 1.0

# ---- potential, wells, barriers -------------------------------------------------
def Vpot(x, c):
    return x**4 / 4.0 - A * x**2 / 2.0 - c * x

def drift(x, c):
    return x**3 - A * x - c

_XG = np.linspace(-2.6, 2.6, 2601)   # fine grid for analytic landscape functionals

def _stationary_pi(c, D):
    v = Vpot(_XG, c)
    logp = -v / D
    logp -= logp.max()
    p = np.exp(logp)
    p /= np.trapz(p, _XG)
    return p

def occupancy_Mplus(c, D):
    """Stationary occupancy of M+ = {x>0}."""
    p = _stationary_pi(c, D)
    mask = _XG > 0
    return float(np.trapz(p[mask], _XG[mask]) / np.trapz(p, _XG))

def critical_points(c):
    """Return (x_left_min, x_saddle, x_right_min) if bistable, else None for missing."""
    dv = drift(_XG, c)
    sign = np.sign(dv)
    cross = np.where(np.diff(sign) != 0)[0]
    roots = []
    for i in cross:
        # linear interpolation of the zero crossing
        x0, x1 = _XG[i], _XG[i + 1]
        y0, y1 = dv[i], dv[i + 1]
        roots.append(x0 - y0 * (x1 - x0) / (y1 - y0))
    roots = sorted(roots)
    if len(roots) == 3:
        return roots[0], roots[1], roots[2]   # min, saddle, min
    return None

def escape_barrier_Mplus(c, D):
    """Kramers log-persistence proxy for M+: (V(saddle)-V(right well)) / D.
    Large -> M+ is a deep, persistent well. 0 if M+ is not a well."""
    cp = critical_points(c)
    if cp is None:
        # monostable: if the single min is >0, M+ is the only well (very persistent),
        # else M+ is not a well (no barrier).
        xm = _XG[np.argmin(Vpot(_XG, c))]
        return 5.0 if xm > 0 else 0.0
    xl, xs, xr = cp
    return float((Vpot(xs, c) - Vpot(xr, c)) / D)

def committor_origin(c, D):
    """q(0): probability that a trajectory started at x=0 commits to M+ before M-.
    Closed form for 1D gradient dynamics: q(x)=int_{xl}^x e^{V/D} / int_{xl}^{xr} e^{V/D}."""
    cp = critical_points(c)
    if cp is None:
        xm = _XG[np.argmin(Vpot(_XG, c))]
        return 1.0 if xm > 0 else 0.0
    xl, xs, xr = cp
    g = _XG[(_XG >= xl) & (_XG <= xr)]
    ig = np.exp((Vpot(g, c) - Vpot(g, c).max()) / D)
    denom = np.trapz(ig, g)
    gg = g[g <= 0.0]
    num = np.trapz(np.exp((Vpot(gg, c) - Vpot(g, c).max()) / D), gg) if len(gg) > 1 else 0.0
    return float(num / denom)

# ---- transition-kernel divergences (EM kernel is Gaussian) ----------------------
_YG = np.linspace(-3.0, 3.0, 601)   # next-state grid for numeric TV/JS

def _gauss(mu, var):
    return np.exp(-(_YG - mu) ** 2 / (2 * var)) / math.sqrt(2 * math.pi * var)

def _kl_gauss(mu1, var1, mu2, var2):
    return 0.5 * (math.log(var2 / var1) + (var1 + (mu1 - mu2) ** 2) / var2 - 1.0)

def kernel_divergences(c_pre, D_pre, c_post, D_post, ref_x, ref_w, dt):
    """E_{x~ref} d(K_post(.|x) || K_pre(.|x)) for d in {KL, JS, TV}."""
    var_pre, var_post = 2 * D_pre * dt, 2 * D_post * dt
    kl = js = tv = 0.0
    wsum = float(np.sum(ref_w))
    for x, w in zip(ref_x, ref_w):
        mu_pre = x - dt * drift(x, c_pre)
        mu_post = x - dt * drift(x, c_post)
        kl += w * _kl_gauss(mu_post, var_post, mu_pre, var_pre)
        p, q = _gauss(mu_post, var_post), _gauss(mu_pre, var_pre)
        tv += w * 0.5 * np.trapz(np.abs(p - q), _YG)
        m = 0.5 * (p + q)
        with np.errstate(divide="ignore", invalid="ignore"):
            klpm = np.trapz(np.where(p > 0, p * np.log(p / m), 0.0), _YG)
            klqm = np.trapz(np.where(q > 0, q * np.log(q / m), 0.0), _YG)
        js += w * 0.5 * (klpm + klqm)
    return {"KL": kl / wsum, "JS": js / wsum, "TV": tv / wsum}

# ---- simulation -----------------------------------------------------------------
def em_step(x, c, D, u, rng):
    return x - c_dt(x, c) + u + np.sqrt(2.0 * D * _DT) * rng.standard_normal(x.shape)

_DT = 0.01
def c_dt(x, c):
    return _DT * drift(x, c)

def simulate(P, cond, direction, seed):
    """Run one history. direction=+1 is h+ (push toward M+), -1 is h- (counterfactual).
    Returns metrics incl. z_final, P (from the natural post-intervention state),
    J_ext, J_write, and the realized (c_post, D_post)."""
    global _DT
    _DT = P["dt"]
    rng = np.random.default_rng(seed)
    n = P["n_traj"]
    c0, eta, lam, channel = cond["c0"], cond["eta"], cond["lam"], cond["channel"]
    clamp, latent = cond.get("clamp", False), cond.get("latent", False)
    U = P["u_push"] * direction

    x = -1.0 + 0.15 * rng.standard_normal(n)   # start in the left (home) basin
    z = np.zeros(n)
    J_ext = np.zeros(n)
    J_write = np.zeros(n)

    def c_of(z):
        return c0 + (P["kappa"] * z if channel == "deepen" else 0.0)
    def D_of(z):
        return P["D0"] * (1.0 + P["rho"] * np.abs(z)) if channel == "roughen" else P["D0"]

    n_int = int(round(cond["tau"] / _DT))
    n_obs = int(round(P["H"] / _DT))

    # ---- intervention window: drive selection + let plasticity write z ----
    # LatentInscription drives toward M+ for the first 70% (writing z) then returns
    # the fast state to the home basin for the last 30% -> writes without leaving x
    # in the target (the operational meaning of "latent": inscribed, not occupying).
    for k in range(n_int):
        if latent and k >= int(0.7 * n_int):
            u = np.full(n, -U)          # return leg: opposite of the exposure direction
        else:
            u = np.full(n, U)           # exposure leg: writes z in the selected direction
        J_ext += (u ** 2) * _DT
        z_prev = z.copy()
        x = em_step(x, c_of(z), D_of(z), u, rng)
        z = z + _DT * (eta * np.tanh(2.0 * x) - lam * z)
        J_write += ((z - z_prev) ** 2) / max(_DT, 1e-9)   # slow-variable dissipation
    occ_tau = float((x > 0).mean())
    z_after_int = z.copy()

    # ---- observation / persistence after withdrawal ----
    escaped = np.zeros(n, dtype=bool)
    esc_step = np.full(n, n_obs, dtype=float)
    occ_series = np.zeros(n_obs)
    for k in range(n_obs):
        u = np.full(n, U) if clamp else np.zeros(n)
        J_ext += (u ** 2) * _DT
        z_prev = z.copy()
        x = em_step(x, c_of(z), D_of(z), u, rng)
        z = z + _DT * (eta * np.tanh(2.0 * x) - lam * z)
        J_write += ((z - z_prev) ** 2) / max(_DT, 1e-9)
        occ_series[k] = (x > 0).mean()
        newly = (~escaped) & (x < -0.5)
        esc_step[newly] = k
        escaped |= newly

    # ---- forced withdrawal probe (turn control OFF for everyone, incl. clamp) ----
    n_w = int(round(P["H_withdraw"] / _DT))
    for k in range(n_w):
        z_prev = z.copy()
        x = em_step(x, c_of(z), D_of(z), np.zeros(n), rng)
        z = z + _DT * (eta * np.tanh(2.0 * x) - lam * z)
        J_write += ((z - z_prev) ** 2) / max(_DT, 1e-9)
    occ_after_withdraw = float((x > 0).mean())

    z_final = float(z.mean())
    c_post = float(np.mean(c_of(z)))
    D_post = float(np.mean(D_of(z)))
    return {
        "S_occ_tau": occ_tau,
        "P_survival": float((~escaped).mean()),
        "P_escape_time": float(np.mean(esc_step) * _DT),
        "P_after_withdraw": occ_after_withdraw,
        "J_ext": float(J_ext.mean()),
        "J_write": float(J_write.mean()),
        "z_final": z_final,
        "c_post": c_post,
        "D_post": D_post,
        "z_after_int": float(z_after_int.mean()),
    }
