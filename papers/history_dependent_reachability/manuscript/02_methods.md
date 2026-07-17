# Methods

> Draft section for *Identifying History-Dependent Reachability: A Constructive
> Framework for Selection-Specific Write-Back*. Governed by `../PAPER_CHARTER.md` and
> `../CLAIM_LEDGER.md`. All parameter values below are read from the frozen
> configuration files under `Experiments/anchoring_*`; all result values cited in the
> Results section come exclusively from `../RESULTS_NUMBERS.md`, which is generated
> read-only from the frozen results JSONs.

## M1. Overview and rationale

We study a single identification question: after the observable present state and the
fast policy of a system are matched, can past selection–consequence history — carried
by a slow path memory — restructure the system's actually reachable future behavioral
outcomes? Answering this requires (i) constructs that separate persistence from
write-back, and selection-specific write-back from generic rule change; (ii) model
systems in which the present state and the history-carrying variable can be set or
matched independently; and (iii) an identification battery that rules out the main
counterfeit explanations (pre-existing attractors, external clamping, generic
volatility learning, calibration artifacts, seed leakage).

Four designed systems are used, in increasing order of behavioral realism: a plastic
double-well stochastic system (S1), a two-armed bandit with a slow surprise
integrator (S2), a contextual bandit with an action-attributable controllability
signal (S3), and a small Markov decision process with a behavioral reach battery
(S4). S1 provides construct separation and measurement instruments; S2–S4 provide the
mechanism chain, including one pre-registered negative result (S2, Phase 2b) that
forced the mechanism revision implemented in S3–S4.

## M2. Constructs

**Persistence (P).** A macrostate M is *persistent* if, after the initiating support
(control input) is withdrawn, the fast state remains in M. We measure survival
(fraction of trajectories never leaving M over the observation window), censored mean
first-escape time, and occupancy after a forced-withdrawal probe.

**General rule change (W_global).** Any change of the system's transition kernel,
measured at matched fast states: the divergence between the post-history and
pre-history one-step kernels, averaged over a reference measure on the fast state,

    W_global = E_{x~nu} D( K_post(.|x) || K_pre(.|x) ),

with D in {KL, JS, TV} and nu in {uniform, pre-history occupancy, mixture}. The
pre-history baseline is the *same condition's own* kernel before the episode, so
W_global counts only what this history wrote.

**Selection-specific write-back (W_sel).** The component of the write that is
specific to the *selection* content of the history, defined counterfactually: run the
actual selection history h+ (drive toward M+) and a matched counterfactual history h−
(equal magnitude and duration, opposite direction), and compare the *functional
consequences for M+* of what each episode wrote:

    W_sel = Phi_{M+}( written by h+ ) − Phi_{M+}( written by h− ),

with directional functionals Phi in {stationary occupancy of M+, escape barrier of
M+, committor at the midpoint}; basin-localized JS/TV are auxiliary. W_sel is
positive only if the write favors the selected macrostate specifically; a
nonspecific write (e.g., raising diffusion everywhere) yields large W_global but
W_sel ≈ 0.

**Anchoring criterion.** Selective anchoring is the conjunction P > 0 AND W_sel > 0.
Persistence alone (a pre-existing attractor), rule change alone (nonspecific
roughening), or cost alone (external clamping) do not qualify. P and W_sel are
claimed to be *bidirectionally dissociable / non-equivalent*, not statistically
independent.

**Costs.** Two costs are logged but are not identification criteria: J_ext (external
control effort, integral of u²) and J_write (slow-variable dissipation).

## M3. System S1: plastic double-well

Euler–Maruyama dynamics with additive noise (dt = 0.01, 4000 trajectories per
condition, five seeds 11–15):

    V(x; c)  = x^4/4 − a x^2/2 − c x,     a = 1
    x_{t+1}  = x_t − dt · V'(x_t; c(z_t)) + dt · u_t + sqrt(2 D(z_t) dt) · xi_t
    z_{t+1}  = z_t + dt · ( eta · tanh(2 x_t) − lambda · z_t )

The slow variable z acts through one of two channels: DEEPEN, c(z) = c0 + kappa·z
(kappa = 0.6), which deepens the currently occupied well — a selection-specific
write; or ROUGHEN, D(z) = D0 (1 + rho·|z|) (rho = 6.0), which raises diffusion
everywhere — a nonspecific write. Baseline noise D0 = 0.06; drive u = ±1.2 during the
intervention window tau = 12; observation window H = 48; forced-withdrawal probe 24.
The home landscape is monostable-left (c0 = −0.5) for the transient, roughening,
anchoring, and clamp conditions, so the target M+ = {x > 0} is not self-sustaining
and cannot be inherited from initialization.

Six conditions populate the P × W_sel plane: **A_transient** (kick, no plasticity),
**PreExistingWell** (c0 = +0.30 bistable-right, no plasticity — persistence without
write-back), **RoughenWrite** (eta = 0.35, roughen channel — the nonspecific
negative control), **LatentInscription** (eta = 0.30, deepen channel, symmetric home
c0 = 0, with the final 30% of the intervention window driving the fast state back
off-target — a write without occupancy, measured at episode scale),
**C_anchor** (eta = 0.17, deepen channel), and **B_clamp** (no plasticity, control
maintained through the observation window, then withdrawn).

W_sel is computed from z at the end of the selection episode (h+ vs h−, matched
counterfactual), because in this state-tracking architecture an off-target write
erodes during subsequent off-target sojourn; this limitation is reported and
motivates the two-timescale agents. Kernel divergences use the closed-form Gaussian
expressions of the EM kernel (verified against Monte-Carlo estimates in the frozen
test suite). Parameter sweeps over (eta, D0) grids (9 × 7) verify that each cell of
the P × W_sel plane is a contiguous region rather than a tuned point.

**Matched-present → different-future protocol.** Two ensembles are set to the
identical fast state x0 = +1 exactly (present-state gap 0 by construction) — one
carrying the landscape written by a real C_anchor history, one carrying the bare home
landscape — and receive an identical adverse probe and identical noise realizations
(paired draws). The terminal distributions over {M−, M+} define the future reachable
sets. "Matched present" here and throughout means the fast/observable state is
matched exactly; the history-carrying slow variable differs by construction — that
difference is the object of study.

## M4. Two-timescale agents: shared architecture

Systems S2–S4 share four separated variables:

- **Q** — fast policy values; actions are sampled from softmax(Q / temp). *Only Q
  drives the current action.*
- **q** — an outcome model, separate from Q, used only for scoring; scores are
  computed with the pre-update q, and q is updated after scoring.
- **z** — a slow scalar integrating a write-gating signal; z gates the *strength* of
  consolidation and never enters action selection.
- **m** — a path-specific memory holding the consolidated *content*; the future
  readout is a function of m (and, in S4, of nothing else carried from formation).

Two candidate gating signals are compared throughout:

**Prediction-error integrator (negative baseline).**

    z_pe ← z_pe + alpha_pe · | o_t − Q[a_t] | − lambda_pe · z_pe

This signal is available to any observer of the reward stream and is therefore
predicted (after Phase 2b) to be non-selection-specific.

**Action-attributable controllability score.** With a fixed reference measure mu over
the reachable actions (uniform here), the pointwise log-likelihood ratio

    r_t = log q(o_t | s_t, a_t) − log Σ_{a'} mu(a' | s_t) · q(o_t | s_t, a')

compares the explanatory power of the agent's own chosen action against the
mu-mixture over reachable alternatives, using the pre-update q. Its expectation is
nonnegative and positive only where the agent's own action carries outcome
information (an A→O edge exists in the data). The slow variable is

    z ← z + alpha_z · r_t − lambda_z · z.

We also report the structural controllability index C_mu(s) = Σ_a mu(a|s) ·
KL[ q(·|s,a) || q̄_mu ], a property of the outcome model rather than of the
trajectory. We do not refer to either quantity as the conditional mutual information
of the acting policy. The estimator is identical for every experimental group and
never receives the group label; active-versus-yoked differences in z can therefore
arise only from each agent's own data.

## M5. System S2: two-armed bandit (Phases 2 and 2b)

Bernoulli two-armed bandit (p_hi = 0.8, p_lo = 0.2, temp = 0.15). The slow variable
(the |PE| integrator; alpha_z = 0.02, lambda_z = 0.002) sets the effective learning
rate of future updates through a sigmoid gate: alpha_eff = lr_lo + (lr_hi − lr_lo) ·
sigmoid( kk (z − zc) ), lr_lo = 0.02, lr_hi = 0.40. Two natural formation histories
(800 steps) create different z: *volatile* (good arm alternates every 10 steps) and
*stable* (good arm fixed). Matching resets Q to 0.5 exactly (the reset touches Q
only; z is verified bit-unchanged). A washout phase (200 steps) exercises behavior
with no reinforcement contingency. The future phase (300 steps, reversal at 150) is
identical for all agents with z frozen; the outcome is the early post-reversal
recovery rate (window 40).

Phase 2 (N = 400 per regime, seed 101) established feasibility with the gate
parameters (zc, kk) calibrated post-formation — a disclosed limitation. **Phase 2b**
is the locked holdout: all parameters frozen at the Phase 2 values (zc = 3.1707,
kk = 3.8822), 40 fresh seeds (20000–20039, disjoint from all calibration), N = 200,
no retuning. Phase 2b adds (i) washout-length curves (0–800 steps); (ii) an
**active vs master-yoked** contrast — each yoked agent receives the recorded reward
sequence of its active master, decoupled from its own actions, with an independent
action RNG; the decoupling is verified by the correlation between "chose the good
arm" and "received reward" (≈ 0 under yoking); and (iii) a cross-individual
permutation control testing whether the future effect follows the carried z value or
the history label. Pre-registered pass criteria included a substantive
selection-specificity margin (gap ratio ≥ 1.5 or future-effect margin ≥ 25%); a
variance-artifact Cohen's d on ensemble means was explicitly excluded as a criterion.
The Phase 2b outcome (NO-GO) is retained frozen as a formal result.

## M6. System S3: contextual bandit with controllability write-back (Phase 2c)

Two-armed Bernoulli bandit with a fixed good arm; *external volatility* is
operationalized as outcome noise (low: 0.85/0.15; high: 0.65/0.35), so the active
agent always has stable content to consolidate and the volatility factor stays
orthogonal to the coupling factor. Design: 2 × 2, volatility × action–consequence
coupling (active vs master-yoked, independent action RNG, offset 777). N = 300,
400 formation steps; beta_Q = 0.15, beta_q = 0.10; controllability z (alpha_z = 0.05,
lambda_z = 0.01) and |PE| baseline z_pe (alpha_pe = 0.05, lambda_pe = 0.01) are
computed in parallel on identical data.

Consolidation writes the greedy content of Q into m at a rate gated by z:
m ← m + alpha_m · relu(z_gate) · (greedy(Q) − m), alpha_m = 0.05. The future readout
is **content-neutral commitment**: with the future policy initialized as Q = 0.5 +
rho_future · (m − mean(m)) (rho_future = 1.5), commitment = 2 |p1 − 0.5| measures how
narrow the m-biased policy is regardless of which option m favors. Content
neutrality is required so that a strongly consolidating baseline (the |PE| gate,
which is high for active *and* yoked) commits both groups equally — making
active ≈ yoked the correct negative-baseline prediction — while a selection-specific
gate leaves the yoked memory diffuse.

Pre-registered thresholds (locked before the holdout): primary GO if the paired
active−yoked commitment difference under the controllability gate exceeds
Delta_min = 0.20 with a 90% bootstrap CI lower bound above zero; the |PE| baseline
must fall within a ±0.15 equivalence bound; yoked decoupling within ±0.05;
consolidation-null (z replaced by 0 during formation) must collapse the active
commitment; memory-swap must follow the memory donor. Calibration used seeds 1–5;
the locked holdout used 40 fresh seeds (30000–30039) with 2000 bootstrap resamples.
**Disclosed limitation:** the 2c bootstrap unit is seed × volatility (80 values, two
per seed); Phase 2c is therefore treated as mechanism feasibility, with confirmatory
statistics carried by S4.

## M7. System S4: tiny-MDP with behavioral reach battery (confirmatory)

Environment: from a start state, the agent picks one of three corridors leading to
three goals; a *blocked* corridor fails (consuming budget) and forces re-selection;
exceeding the move budget (2) ends the episode in a non-arrival state ∅. Terminal
distributions are four-vectors [P(G0), P(G1), P(G2), P(∅)].

Formation (400 episodes, N = 400): corridor-level bandit identical in structure to
S3 (temp_form = 0.20; p_hi = 0.8 / p_lo = 0.2), with three groups — active,
master-yoked (reward replayed, independent action RNG), and **external-action sham**:
the outcome is determined by an observable external action e_t drawn uniformly,
not by the agent's own action; separate outcome models q_self(o|a) and q_ext(o|e)
yield separate self-attribution and external-attribution scores. The self score
gates consolidation. The sham is a mechanism gate (predicted: self ≈ 0, ext > 0),
not GO-deciding.

Future battery (frozen parameters; temp_fut = 0.40, beta_fut = 0.20, 60 episodes,
measured over the last 20): three task classes with goal/blocked roles
counterbalanced across seeds — **aligned** (target = history corridor's goal),
**blocked** (history corridor blocked; target elsewhere), **novel** (target never
rewarded in formation). The future resets the environment state and Q (uniform;
initial action distribution matched exactly) and reads **only m**: formation q, z,
counters, and traces are never read (code-verified; also implied by
same-m/different-z = 0). m acts as a bounded retention pull on the evolving policy,
Q ← Q + kappa_m (m − Q) per episode (kappa_m = 0.10), so trajectories diverge across
episodes by m alone. Reward magnitudes and temperatures were calibrated (seeds 1–5)
solely to keep arrival probabilities interior (no arm at 1.0).

Pre-registered, locked before calibration: primary GO iff the 95% paired-bootstrap
CI lower bound of the equal-weight macro-TV across the three task classes *directly
exceeds* Delta_min = 0.15; mandatory direction gates (aligned: active advantage;
blocked and novel: active stickiness, CIs on the pre-registered side); null-type
controls (memory-null, same-m/different-z) with 95% CIs entirely within
±eps_TV = 0.05; memory-swap following the memory donor. Holdout: 50 fresh seeds
(40000–40049), 10,000 paired bootstrap resamples.

## M8. Identification strategy (cross-cutting)

1. **Counterfeit ledger.** Each qualifying construct has a designed counterfeit that
   must fail the criterion: pre-existing attractor (P without W_sel), nonspecific
   roughening (W_global without W_sel), external clamp (occupancy without P after
   withdrawal, at 5× external cost), |PE| integrator (history dependence without
   selection specificity), calibration artifact (random-slow-variable and permutation
   controls), content confound (content-neutral commitment in S3; content-
   counterbalanced battery in S4).
2. **Matched present.** All future comparisons match the observable present exactly:
   the fast state in S1; state, Q, and initial action distribution in S4. Only the
   history-carrying slow structure differs.
3. **Calibration → freeze → holdout.** Every confirmatory claim is evaluated on
   fresh seeds under parameters frozen before those seeds were run, with thresholds
   pre-registered (in S4, locked before calibration). Holdout seed sets are disjoint
   from calibration and from each other across phases (verified in the audit).
4. **Retention of negative results.** The Phase 2b NO-GO is frozen and reported as a
   formal result; the mechanism revision it forced (from |PE| to action-attributable
   controllability) is the paper's central theoretical move.

## M9. Statistics

Primary statistics are paired seed-level differences with percentile bootstrap CIs
(S4: unit = seed, n = 50, B = 10,000, 95% CI compared against Delta_min directly;
S3: unit = seed × volatility, n = 80, B = 2,000, 90% CI — disclosed and treated as
feasibility). Absence claims use pre-registered equivalence bounds, not point nulls.
Direction gates are one-sided CI position checks fixed in advance. The very narrow
CIs reported for S4 reflect cross-seed reproducibility of a frozen deterministic
model (each per-seed statistic already averages N = 400 agents); they are not
construct-level confidence intervals and are never interpreted as such.

## M10. Reproducibility

Each experiment directory is frozen with a locked configuration (all parameters and
seeds), results JSON, a test suite (identification and sanity tests, all passing),
and a sha256 freeze manifest (v2 manifests supersede v1 where documentation was
corrected post-audit; code, parameters, and results are byte-identical to the
originals). An independent audit verified bit-identical re-runs of the confirmatory
holdout, seed-set disjointness, and the only-m-read property, and re-classified two
in-framework checks (memory-null, memory-swap) as pipeline validation rather than
independent causal evidence. Evidence coordinates (commits on the
`research/selective-anchoring` lineage and the sealed archive tag) are listed in the
charter; numeric provenance for every figure and table is
`papers/history_dependent_reachability/RESULTS_NUMBERS.md`, generated read-only from
the frozen JSONs.
