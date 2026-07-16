"""
tiny-MDP confirmatory model for controllability write-back.

Formation (corridor level, carries over Phase 2c): agent repeatedly chooses one of 3
corridors; coupled reward depends on choosing the history corridor h. Controllability
score = mu-mixture pointwise LLR (outcome model q separate from policy Q, scored pre-update);
z_ctrl gates consolidation of a corridor MEMORY m. Yoked = reward replayed, decoupled.
Sham = reward set by an observable EXTERNAL action e; self- and ext-attribution scored
separately.

Future reachable set (behavioral, NOT an m threshold): a 2-step reach task with 3 goals +
a timeout/non-arrival component. Terminal distribution over {G0,G1,G2, EMPTY}. The future
reads ONLY m (Q reset; q,z,counters,traces are formation-only and never read). m acts as a
RETENTION PULL on the evolving policy, so the initial action distribution is matched
(uniform Q) and trajectories diverge over episodes by m.
"""
from __future__ import annotations
import numpy as np

EMPTY = 3   # non-arrival / timeout index in the terminal distribution

def _ll(o, p):
    p = np.clip(p, 1e-6, 1 - 1e-6)
    return o * np.log(p) + (1 - o) * np.log(1 - p)

def _kl(p, r):
    p = np.clip(p, 1e-6, 1 - 1e-6); r = np.clip(r, 1e-6, 1 - 1e-6)
    return p * np.log(p / r) + (1 - p) * np.log((1 - p) / (1 - r))

def softmax3(Q, temp):
    z = Q / temp; z = z - z.max(axis=1, keepdims=True)
    e = np.exp(z); return e / e.sum(axis=1, keepdims=True)

def sample_cat(P, rng):
    u = rng.random(P.shape[0])[:, None]
    return (np.cumsum(P, axis=1) < u).sum(axis=1).clip(0, P.shape[1] - 1)

def tv(p, q):
    return 0.5 * float(np.sum(np.abs(np.asarray(p) - np.asarray(q))))

# ---------------- formation ----------------
def formation(coupling, h, seed, c, master_R=None, act_offset=0):
    N, T, K = c["N"], c["form_episodes"], 3
    rng = np.random.default_rng(seed)
    act_rng = np.random.default_rng(seed + 10_000 + act_offset)
    ext_rng = np.random.default_rng(seed + 20_000)
    mu = np.full(K, 1.0 / K)

    Q = np.full((N, K), 0.5)     # policy (action)
    qs = np.full((N, K), 0.5)    # self outcome model (score), separate from Q
    qe = np.full((N, K), 0.5)    # external-action outcome model (sham)
    z = np.zeros(N); zpe = np.zeros(N)
    m = np.zeros((N, K))
    R = np.zeros((N, T))
    self_acc = np.zeros(N); ext_acc = np.zeros(N)
    good = np.zeros((N, T), dtype=int); act = np.zeros((N, T), dtype=int)

    for t in range(T):
        p = softmax3(Q, c["temp_form"])
        a = sample_cat(p, act_rng)
        e = sample_cat(np.full((N, K), 1.0 / K), ext_rng)     # observable external action
        if coupling == "coupled":
            pr = np.where(a == h, c["p_hi"], c["p_lo"]); o = (rng.random(N) < pr).astype(float)
        elif coupling == "sham":
            pr = np.where(e == h, c["p_hi"], c["p_lo"]); o = (rng.random(N) < pr).astype(float)
        else:  # yoked
            o = master_R[:, t]
        # scores with PRE-update models
        qbar_s = (mu * qs).sum(axis=1); qbar_e = (mu * qe).sum(axis=1)
        r_self = _ll(o, qs[np.arange(N), a]) - _ll(o, qbar_s)
        r_ext = _ll(o, qe[np.arange(N), e]) - _ll(o, qbar_e)
        z = z + c["alpha_z"] * r_self - c["lambda_z"] * z
        zpe = zpe + c["alpha_pe"] * np.abs(o - Q[np.arange(N), a]) - c["lambda_pe"] * zpe
        self_acc += r_self; ext_acc += r_ext
        # consolidate memory (content = greedy corridor), gated by self-controllability z
        gate = np.clip(z, 0.0, None)
        greedy = (Q == Q.max(axis=1, keepdims=True)).astype(float)
        greedy /= greedy.sum(axis=1, keepdims=True)
        m += (c["alpha_m"] * gate)[:, None] * (greedy - m)
        # updates AFTER scoring
        qs[np.arange(N), a] += c["beta_q"] * (o - qs[np.arange(N), a])
        qe[np.arange(N), e] += c["beta_q"] * (o - qe[np.arange(N), e])
        Q[np.arange(N), a] += c["beta_Q"] * (o - Q[np.arange(N), a])
        R[:, t] = o; good[:, t] = h; act[:, t] = a

    chose_good = (act == h).ravel().astype(float); rew = (R.ravel() > 0.5).astype(float)
    cc = float(np.corrcoef(chose_good, rew)[0, 1]) if chose_good.std() > 1e-9 and rew.std() > 1e-9 else 0.0
    return dict(m=m, z=z, zpe=zpe, R=R, ctrl_corr=cc,
                self_attr=float(self_acc.mean() / T), ext_attr=float(ext_acc.mean() / T))

# ---------------- future reach task ----------------
def future_task(m, target, blocked, seed, c):
    """Reads ONLY m. Q reset (uniform) -> matched initial action distribution. m acts as a
    retention pull on the evolving policy. Returns 4-vector [P(G0),P(G1),P(G2),P(EMPTY)]."""
    N, K, B = m.shape[0], 3, c["budget"]
    rng = np.random.default_rng(seed + 55_000)
    Q = np.full((N, K), 0.5)                      # reset; ONLY m is carried from history
    counts = np.zeros((N, 4))
    for ep in range(c["fut_episodes"]):
        reached = -np.ones(N, dtype=int); rem = np.ones(N, dtype=bool)
        for b in range(B):
            P = softmax3(Q, c["temp_fut"])       # m does NOT enter action selection
            ch = sample_cat(P, rng)
            rch = rem & (ch != blocked)          # non-blocked pick reaches its goal (terminal)
            reached[rch] = ch[rch]               # a blocked pick just fails: consume budget, retry
            rem = rem & ~rch
        reached[rem] = EMPTY                      # non-arrival (perseverated on the block)
        got = reached < EMPTY
        r = (reached == target).astype(float)
        if got.any():
            rows = np.where(got)[0]; cols = reached[got]
            Q[rows, cols] += c["beta_fut"] * (r[got] - Q[rows, cols])
        Q += c["kappa_m"] * (m - Q)              # BOUNDED retention pull toward memory m
        if ep >= c["fut_episodes"] - c["fut_measure_last"]:
            for g in range(4):
                counts[:, g] += (reached == g)
    dist = counts.sum(axis=0); dist = dist / dist.sum()
    return dist
