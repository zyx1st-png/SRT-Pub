"""
Phase 2c model: action-attributable controllability write-back.

Separation of variables (correction 1 & 2):
  Q[a] : fast POLICY value -> action via softmax(Q/temp).            (drives current action)
  q[a] : OUTCOME model P(o=1|a), SEPARATE from Q, updated AFTER the score is computed.
  z    : slow CONTROLLABILITY signal, leaky integral of the score r_t. Gates ONLY the
         consolidation STRENGTH (never the current action).
  m[a] : path-specific MEMORY (consolidated content). The future reachable set is a
         function of m only.

Score (correction 1): reference-measure pointwise log-likelihood ratio, computed with
the PRE-update q, against a FIXED reachable-action reference measure mu (uniform):
  qbar_mu(o) = sum_a mu[a] * q(o|a)
  r_t = log q(o_t|a_t) - log qbar_mu(o_t)
Also report the STRUCTURAL controllability index (a property of q, not the trajectory):
  C_mu = sum_a mu[a] * KL( Bern(q[a]) || Bern(qbar_mu1) ),  qbar_mu1 = sum_a mu[a] q[a]
This is NOT called conditional mutual information of the acting policy; it is the
mu-reference structural controllability.

Negative baseline (correction: keep |PE|): zpe = leaky integral of |o - Q[a]|, which
should again give active ~ yoked (reproduce Phase 2b).
"""
from __future__ import annotations
import numpy as np

def _bern_ll(o, p):
    p = np.clip(p, 1e-6, 1 - 1e-6)
    return o * np.log(p) + (1 - o) * np.log(1 - p)

def _bern_kl(p, r):
    p = np.clip(p, 1e-6, 1 - 1e-6); r = np.clip(r, 1e-6, 1 - 1e-6)
    return p * np.log(p / r) + (1 - p) * np.log((1 - p) / (1 - r))

def softmax_p1(Q, temp):
    return 1.0 / (1.0 + np.exp((Q[:, 0] - Q[:, 1]) / temp))

# External volatility = OUTCOME NOISE with a FIXED good arm (arm 1). Both levels are
# learnable, so the ACTIVE agent always has stable content to consolidate; only the
# reward stochasticity differs. This keeps the volatility factor orthogonal to the
# coupling factor (whether the agent's own action causes the outcome).
GOOD_ARM = 1
def reward_probs(volatility, c):
    return (c["phi_low"], c["plo_low"]) if volatility == "low" else (c["phi_high"], c["plo_high"])

def formation(coupling, volatility, z_mode, seed, c, master_R=None, action_rng_offset=0,
              null_z=False):
    """Run one formation. Returns per-agent slow states + diagnostics + reward matrix.
    coupling: 'coupled' (active) or 'decoupled' (yoked, reward replayed from master_R).
    z_mode:   'ctrl' (controllability z gates m) or 'pe' (|PE| z gates m).
    null_z:   if True, the consolidation gate uses a null z (breaks z->m during formation).
    """
    N, T = c["N"], c["form_steps"]
    rng = np.random.default_rng(seed)
    act_rng = np.random.default_rng(seed + 10_000 + action_rng_offset)  # independent action RNG
    mu = np.array([0.5, 0.5])                        # fixed reachable-action reference measure

    Q = np.full((N, 2), 0.5)        # policy value (action)
    q = np.full((N, 2), 0.5)        # outcome model (score) -- SEPARATE from Q
    z = np.zeros(N)                 # controllability z
    zpe = np.zeros(N)               # |PE| baseline
    m = np.zeros((N, 2))            # path memory content
    R = np.zeros((N, T))            # reward stream (for yoking)
    A = np.zeros((N, T), dtype=int)
    G = np.zeros((N, T), dtype=int)
    Cmu_acc = np.zeros(N)

    p_hi, p_lo = reward_probs(volatility, c)
    for t in range(T):
        p1 = softmax_p1(Q, c["temp"])
        a = (act_rng.random(N) < p1).astype(int)
        g = GOOD_ARM
        if coupling == "coupled":
            pr = np.where(a == g, p_hi, p_lo)
            o = (rng.random(N) < pr).astype(float)
        else:  # decoupled/yoked: reward replayed, NOT contingent on a
            o = master_R[:, t]
        # ---- score computed with PRE-update q ----
        qa = q[np.arange(N), a]
        qbar1 = mu[0] * q[:, 0] + mu[1] * q[:, 1]            # mu-mixture P(o=1)
        ll_a = _bern_ll(o, qa)
        ll_bar = _bern_ll(o, qbar1)
        r_t = ll_a - ll_bar
        z = z + c["alpha_z"] * r_t - c["lambda_z"] * z
        zpe = zpe + c["alpha_pe"] * np.abs(o - Q[np.arange(N), a]) - c["lambda_pe"] * zpe
        Cmu_acc += mu[0]*_bern_kl(q[:, 0], qbar1) + mu[1]*_bern_kl(q[:, 1], qbar1)
        # ---- consolidation of content into m, gated by z (strength only) ----
        zgate = (z if z_mode == "ctrl" else zpe)
        if null_z:
            zgate = np.full(N, c["null_z_value"])
        gate = np.clip(zgate, 0.0, None)
        greedy = np.stack([(Q[:, 0] >= Q[:, 1]).astype(float),
                           (Q[:, 1] > Q[:, 0]).astype(float)], axis=1)
        m += (c["alpha_m"] * gate)[:, None] * (greedy - m)
        # ---- updates AFTER scoring ----
        idx = (np.arange(N), a)
        q[idx] += c["beta_q"] * (o - q[idx])
        Q[idx] += c["beta_Q"] * (o - Q[idx])
        R[:, t] = o; A[:, t] = a; G[:, t] = g

    return dict(z=z, zpe=zpe, m=m, R=R, A=A,
                Cmu=Cmu_acc / T,
                mean_abs_pe=float(np.mean(np.abs(R - 0.5))),
                ctrl_corr=float(_ctrl_corr(A, R, G)))   # manipulation check: does choosing
                                                        # the good arm predict reward? ~0 if yoked

def _ctrl_corr(A, R, G):
    """Correlation between 'chose the good arm' and 'got reward' (context-conditioned
    controllability). High for a coupled agent, ~0 for a decoupled/yoked one."""
    chose_good = (A == G).ravel().astype(float)
    rew = (R.ravel() > 0.5).astype(float)
    if chose_good.std() < 1e-9 or rew.std() < 1e-9:
        return 0.0
    return float(np.corrcoef(chose_good, rew)[0, 1])

def future_commitment(m, c, swap_m=None):
    """CONTENT-NEUTRAL future reachable-set readout, determined by m only.

    The future policy is initialized/biased by m; commitment = how narrow the resulting
    reachable set is (how far the policy sits from uniform), REGARDLESS of which option m
    favours. This isolates the write-back STRENGTH channel (gated by z) from the CONTENT
    (which arm) -- so a |PE| baseline that consolidates any content strongly commits just
    as much as controllability-z, giving the intended active~yoked negative baseline;
    only a selection-specific z leaves the yoked memory diffuse (low commitment).
    """
    mm = m if swap_m is None else swap_m
    bias = mm - mm.mean(axis=1, keepdims=True)
    Q = 0.5 + c["rho_future"] * bias
    p1 = softmax_p1(Q, c["temp"])
    commitment = 2.0 * np.abs(p1 - 0.5)          # 0 = uniform (broad reachable set), 1 = committed
    return commitment

