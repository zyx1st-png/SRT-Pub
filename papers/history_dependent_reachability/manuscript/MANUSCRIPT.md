# Identifying History-Dependent Reachability: A Constructive Framework for Selection-Specific Write-Back

> Assembled from manuscript/00–07 by `assemble_manuscript.py` (mechanical
> renumbering and cross-reference unification only; no language polish).
> Numeric provenance: `RESULTS_NUMBERS.md` (read-only from frozen JSONs).
> Governed by `PAPER_CHARTER.md` and `CLAIM_LEDGER.md`.

## Abstract

Two systems can occupy the same present state and still differ in what they can
become — but only if something written by their histories survives the matching of
everything observable. We formalize this as an identification problem: after
matching the environment state, the fast values, and the initial action
distribution, can a history-formed slow memory still change a system's future
behavioral reachability, and can that change be attributed to the system's own
selection–consequence coupling rather than to generic exposure history? We
develop an identification battery — exact present-state matching, master-yoked
controls that cut the action→outcome edge, an external-action sham that
dissociates self- from external attribution, and a calibration→freeze→fresh-seed
holdout discipline with pre-registered thresholds and equivalence bounds — and run
it end to end in designed systems. A constructive double-well model first
separates three constructs that are easily conflated: persistence after support
withdrawal, general transition-rule change, and selection-specific write-back are
bidirectionally dissociable, and neither persistence nor rule change certifies
that a selection was inscribed. We then report a retained negative result: a slow
variable accumulating absolute prediction error produced durable,
future-effective history dependence that a yoked agent reproduced entirely
(0.239 vs 0.238), failing selection-specificity on a locked holdout. Replacing
accumulated surprise with action-attributable predictive information — the
log-likelihood advantage of the agent's chosen action over a fixed reference
mixture — restored it: active agents form peaked path memories while yoked
agents do not (paired difference 0.570, seed-clustered 90% CI [0.566, 0.574],
consistent with the frozen pre-holdout pooled interval [0.559, 0.581], against a
±0.15 equivalence-bounded prediction-error baseline). In a minimal MDP where only the consolidated memory
crosses the matching boundary, that memory redirected future arrival
distributions directionally — history-aligned advantage bought at the price of
perseverative cost under blocked paths and novel goals (macro total variation
0.374; 95% CI lower bound above the pre-registered 0.15; 50 fresh seeds). All
results are constructive demonstrations in designed models, audited to separate
load-bearing evidence from pipeline validation; they establish an identification
framework and its feasibility, not facts about any natural system.

---

# 1. Introduction

Two systems can behave identically now and yet not be the same system. One has
merely arrived at a state; the other has been shaped by how it arrived — and the
difference, if it exists, lives entirely in the future: in which outcomes each
system can still reach, how easily, and at what cost when the world changes. The
question this paper addresses is whether that difference can be made
experimentally real in the strictest sense: **after the observable present is
matched — same state, same fast values, same action distribution — can a system's
selection history still hide a different future reachability, carried by nothing
but a slow, history-formed memory?**

The question is easy to blur because several familiar phenomena sit next to it
without answering it. A state that persists after its support is withdrawn may
simply have fallen into a basin that was always there; persistence alone does not
show that anything was written. A transition rule that has changed may have
changed indiscriminately — noise-roughened, globally perturbed — without favoring
what the system actually selected; plasticity alone does not show that the
selection mattered. A system whose future updates are modulated by past surprise
exhibits history dependence of a real but generic kind — any passive observer of
the same event stream would carry the same trace. And a system held in place by an
external controller occupies its state without owning it. Persistence,
generic plasticity, volatility tracking, and clamped occupancy are four ways of
looking historical without being historical in the sense at issue here: none of
them requires that the system's *own selections, through their consequences*,
restructured what it can become.

There is, accordingly, an identification gap rather than a theory gap. Dynamical
systems theory quantifies stability and hysteresis; control theory quantifies the
cost of reaching and holding states; reinforcement learning and metaplasticity
describe how experience reshapes future updates; predictive-processing accounts
describe regulation under changing statistics. Each supplies constructs we use
freely in what follows. But **to our knowledge**, no existing framework packages
the specific test that the question requires: match the present completely at the
level of observables, vary only the history-formed slow memory, and determine
whether — and in which direction — the future behavioral arrival distribution
changes, under controls that differentiate selection-specific history from
generic exposure history.

This paper builds that test and runs it end to end in designed systems. The
battery has three components. *Matched present*: at test time the environment
state, the fast values, and hence the initial action distribution are reset
identically for all agents; the only quantity carried from the past is the slow
memory. *Master-yoked control*: a paired agent receives the identical reward
stream with the action→outcome coupling cut, so that anything driven by exposure
statistics alone appears equally in both arms. *External-action sham*: outcomes
are driven by an observable external action, so that controllable structure is
present in the stream but is not attributable to the agent's own choices. Around
this battery we impose a pre-registration discipline — calibration on dedicated
seeds, frozen parameters and thresholds, fresh-seed holdouts, equivalence bounds
for every claimed null — and an adversarial audit of the finished chain that
separates load-bearing evidence from pipeline validation.

The chain includes a negative result, and we keep it in the main line of the
argument. Our first mechanism — a slow variable accumulating absolute prediction
error, the most natural reading of "history writes itself into the system" —
passed its feasibility gate and then failed the yoked control on a locked holdout:
the yoked agent, with no choice–consequence coupling at all, reproduced the future
effect. That NO-GO is retained frozen, is reported as a primary result, and is
what forced the mechanism revision at the center of the paper: replacing
accumulated surprise with *action-attributable predictive information* — how much
the agent's own chosen action improves outcome prediction over a fixed reference
mixture of the actions it could have taken.

The contributions are four, and all are deliberately limited to designed models.
First, a construct separation: persistence, general rule change, and
selection-specific write-back are shown to be bidirectionally dissociable in a
constructive system, with portable measurement instruments for each. Second, a
negative result: prediction-error accumulation yields history-dependent
metaplasticity that is not selection-specific. Third, a mechanism: action-
attributable predictive information can gate the formation of path-specific
memory, and does so selection-specifically under yoked and sham controls. Fourth,
a behavioral demonstration: with the present matched, a history-formed memory
redirects future arrival distributions directionally — history-aligned advantage
purchased at the price of perseverative cost when the old path is blocked or the
goal is new. What the paper offers, in sum, is not a discovery about any natural
system but an identification framework with a worked, falsifiable instance —
including one genuine failure that the framework itself caught.

---

# 2. Methods

## 2.1 Overview and rationale

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

## 2.2 Constructs

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

## 2.3 System S1: plastic double-well

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

## 2.4 Two-timescale agents: shared architecture

Systems S2–S4 share four separated variables (Figure 1A):

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

## 2.5 System S2: two-armed bandit (Phases 2 and 2b)

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

## 2.6 System S3: contextual bandit with controllability write-back (Phase 2c)

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
**Two reported intervals (identical conclusions).** The pre-registered, frozen
bootstrap unit is seed × volatility (80 values, two per seed) — retained as
provenance. Because that analysis treats the within-seed volatility cells as separate
resampling units, a post-audit
seed-clustered bootstrap (average the two volatility cells within each seed, then
resample the 40 seeds) is reported alongside as the preferred inferential summary;
both are given in Results (3.3). Phase 2c is treated as mechanism feasibility, with
confirmatory statistics carried by S4; neither interval changes the frozen GO.

## 2.7 System S4: tiny-MDP with behavioral reach battery (confirmatory)

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

Future battery (Figure 4A; frozen parameters; temp_fut = 0.40, beta_fut = 0.20, 60 episodes,
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

## 2.8 Identification strategy (cross-cutting)

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

## 2.9 Statistics

Primary statistics are paired seed-level differences with percentile bootstrap CIs
(S4: unit = seed, n = 50, B = 10,000, 95% CI compared against Delta_min directly;
S3: two intervals — the frozen pre-holdout pooled analysis, unit = seed ×
volatility, n = 80, B = 2,000, 90% CI (provenance); and a post-audit seed-clustered
bootstrap, unit = seed, n = 40, B = 10,000, 90% CI (preferred inferential summary).
Both give the same conclusion; S3 is treated as feasibility). Absence claims use pre-registered equivalence bounds, not point nulls.
Direction gates are one-sided CI position checks fixed in advance. The very narrow
CIs reported for S4 reflect cross-seed reproducibility of a frozen deterministic
model (each per-seed statistic already averages N = 400 agents); they are not
construct-level confidence intervals and are never interpreted as such.

## 2.10 Reproducibility

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

---

# 3. Results

## 3.1 Persistence, rule change, and selection-specific write-back are dissociable constructs (S1)

*Source: anchoring_double_well/results_dissociation.json, results_sweep.json,
results_matched_future.json.*

Six conditions with identical external drive (J_ext = 17.3 for all except the clamp)
populate the P × W_sel plane (Table 1; Figure 2):

| condition | P_survival | W_sel(occ) | W_global KL | J_write | reading |
|---|---|---|---|---|---|
| A_transient | 0.000 | 0.000 | 0.000 | 0.00 | kick and release: nothing held, nothing written |
| PreExistingWell | 1.000 | 0.000 | 0.000 | 0.00 | persistence from a pre-given attractor; zero write |
| RoughenWrite | 0.000 | −0.000 | **7.976** | **6.70** | largest rule change of any condition, zero selection-specific write |
| LatentInscription | 0.000 | **+1.000** | 0.008 | 2.10 | write without occupancy (episode scale) |
| C_anchor | 1.000 | **+1.000** | 0.035 | 0.28 | selective anchoring: P ∧ W_sel |
| B_clamp | 1.000 held → 0.000 after withdrawal | 0.000 | 0.000 | 0.00 | occupancy rented from the controller at J_ext = 86.4 (5×) |

All four P × W_sel cells are occupied, so **neither construct implies the other**
(bidirectional dissociation; not an independence claim). The two counterfeits behave
as designed: the nonspecific control (RoughenWrite) produces the largest W_global
(KL 7.98 / JS 0.278 / TV 0.615 under the uniform reference; identical under
pre-occupancy and mixture references) with W_sel ≈ 0 — so general rule change does
not measure selection-specific write-back — and neither cost tracks W_sel (the
highest J_write, 6.70, belongs to the *non*-anchoring roughening condition; the
anchoring condition pays 0.28). LatentInscription realizes the remaining cell
(W_sel = +1.000 on all three functionals — occupancy, barrier, committor — with
P = 0.000) at the selection-episode scale; its slow variable erodes during the
off-target sojourn (z_episode = +0.74 → negative by the end of observation), which is
the state-tracking limitation that motivates the two-timescale agents of Sections 3.2–3.4.

Parameter sweeps confirm the cells are regions, not tuned points: the anchoring cell
occupies 49 and the latent cell 56 contiguous grid cells of the 9 × 7 (eta, D0)
phase diagrams.

**Matched present, different future (Figure 1B).** With the present state matched exactly
(gap = 0.0000) and identical forcing and noise, the ensemble carrying the
C_anchor-written landscape ends in reachable set {M+} with raw future
P(M+) = 1.000, while the naive ensemble ends in {M−} with P(M+) = 0.000
(future divergences: KL = 20.7, JS = 0.693, TV = 1.000). The entire difference lives
in the written slow variable.

## 3.2 A pre-registered negative result: prediction-error accumulation is history-dependent but not selection-specific (S2, Phase 2b)

*Source: anchoring_bandit_holdout/results_phase2b.json. All parameters frozen from
the Phase 2 feasibility commit; 40 fresh seeds; no retuning.*

The frozen |PE|-integrator mechanism **generalized** to new seeds: the volatile-vs-
stable z separation survived the unexpressive washout (67% retained, minimum 67%),
the frozen-z future effect was 0.241 ± 0.010 with 100% of seeds positive, the null
control abolished it (mean |diff| = 0.010), and the swap control reversed it (100%
of seeds). A cross-individual permutation (Supplementary Figure S3) confirmed the effect follows the carried z
value, not the history label (recovery~z = 0.761 vs recovery~label = 0.007).

It nevertheless **failed selection-specificity**: a master-yoked group receiving the
same reward stream with no choice→consequence coupling reproduced the future effect
essentially in full — active 0.239 vs yoked 0.238 (d = 0.05; Figure 3A); the formed z-gap ratio
was 1.20 (active 1.237 vs yoked 1.031), far short of the pre-registered ≥ 1.5
margin. (A gap Cohen's d computed on ensemble means reached 17.8 and was excluded by
design as a variance artifact.) A small genuine selection signature existed —
active stable-history z (2.661) below yoked (2.896), because choice contingency lets
the active agent learn and reduce surprise — but it did not translate into any
differential future consequence.

**Verdict (frozen): NO-GO.** Accumulated |PE| is a reward-stream volatility tracker
available to any observer, not a selection-specific write-back. Washout-length
curves (Supplementary Figure S1) (retention 1.00 / 0.90 / 0.82 / 0.67 / 0.45 / 0.20 across 0–800 steps; future
effect decaying from 0.486 at 100 steps to 0.002 at 800) show the inscription is
durable over moderate unexpressive horizons and leaky over long ones. This negative
result forced the mechanism revision of Section 3.3.

## 3.3 Action-attributable controllability yields selection-specific write-back (S3, Phase 2c)

*Source: anchoring_2c_controllability/results_2c_holdout.json. Frozen parameters;
40 fresh seeds; thresholds pre-registered. Bootstrap unit is seed × volatility
(80 values); Phase 2c is mechanism feasibility — confirmatory statistics are carried
by Section 3.4.*

With the gating signal replaced by the mu-mixture log-likelihood-ratio score r_t
(Methods 2.4), the paired active−yoked difference in content-neutral future
commitment was **0.570** — above the pre-registered Delta_min = 0.20 and consistent
across both volatility levels (d_ctrl = 0.627 high, 0.513 low). We report two
intervals for this estimate, with identical conclusions. The **frozen pre-holdout pooled analysis** (unit = seed × volatility, 80 values;
provenance) gives 90% CI
**[0.559, 0.581]**. The **post-audit seed-clustered bootstrap** — averaging the two
volatility cells within each seed and resampling the 40 seeds (10,000 resamples), the
audit-preferred inferential summary — gives 90% CI **[0.566, 0.574]** (tighter
because the within-seed between-cell variance is removed). Both lie well above zero;
the frozen GO is not modified.

Within the same framework and on the same data, the **|PE| baseline fell inside the
pre-registered ±0.15 equivalence bound: 0.087** — pooled 90% CI **[0.082, 0.091]**
(provenance) and seed-clustered 90% CI **[0.084, 0.089]** (preferred), again with
identical conclusions (d_pe = 0.067 high, 0.106 low). This is a pre-registered
equivalence test conducted within Phase 2c, distinct from the Phase 2b comparison
reported in Section 3.2; together they show the failed mechanism failing again inside the
revised framework while the controllability mechanism succeeds on identical data.

The z-formation coupling effect was sign-stable (ctrl active−yoked: +0.264 high,
+0.931 low; |PE| active−yoked: −0.070, −0.078 — the |PE| signal is, if anything,
slightly *higher* for yoked). Yoked decoupling was verified in the data
(ctrl-corr −0.000 vs active +0.270), and the structural controllability index
separated groups (C_mu 0.121 active vs 0.022 yoked). **[pipeline validation]**
Consolidation-null collapsed active commitment (0.997 → 0.000) and memory-swap
followed the memory donor (gap +0.000 vs yoked 0.427): these verify the z→m→future
plumbing and are not independent causal evidence.

## 3.4 History-formed path memory restructures behavioral reachability under a matched present (S4, tiny-MDP — main result)

*Source: anchoring_tiny_mdp_confirmatory/results_mdp_holdout.json. Thresholds locked
before calibration (Delta_min = 0.15, eps_TV = 0.05); 50 fresh seeds (40000–40049);
10,000 paired bootstrap resamples; per-seed bootstrap unit. Failures: NONE.*

With state, fast values Q, and the initial action distribution matched exactly and
**only m** carried from formation, the equal-weight macro-TV between active and
yoked goal-arrival distributions was **0.374, 95% CI [0.374, 0.375]** (Figure 5E) — the CI lower
bound directly exceeds the pre-registered Delta_min = 0.15.

The difference is directional, in all three pre-registered senses (Figure 5A–D):

- **Aligned (advantage):** active reaches the history goal more, ΔP(G_h) = +0.221,
  CI [+0.219, +0.223];
- **Blocked (stickiness cost):** with the history corridor blocked, active times out
  more, ΔP(∅) = +0.582, CI [+0.580, +0.583];
- **Novel (restriction cost):** active reaches a never-rewarded goal less,
  ΔP(G_novel) = −0.278, CI [−0.280, −0.276].

Consolidation therefore buys history-aligned advantage at the price of perseverative
stickiness — a bidirectional behavioral signature that a mere divergence magnitude
would not establish. The external-action sham behaved as the mechanism predicts (Figure 4B)
(self-attribution −0.015 ≈ 0; external-attribution +0.143 > 0): controllable
structure present in the stream but not attributable to the agent's own actions does
not gate consolidation. Yoked decoupling held (ctrl-corr −0.001).

**[pipeline validation]** (Supplementary Figure S2) memory-null = 0.044, CI [0.043, 0.045] (within ±0.05;
the residual reflects uniform-m vs near-zero-m ablation states);
same-m/different-z = 0.000 and memory-swap = 0.000 exactly, as structurally required
because the future is a deterministic function of (m, seed). These confirm that m is
the sole carrier read at test — the identification plumbing — and are not cited as
independent causal isolation.

The reported CIs measure cross-seed reproducibility of a frozen deterministic model
(each per-seed statistic averages N = 400 agents); they are not construct-level
confidence intervals.

## 3.5 Summary of the evidential structure

The load-bearing results are (i) the construct dissociation with its two behaving
counterfeits (3.1); (ii) the frozen negative result that accumulated prediction error
is not selection-specific (3.2); (iii) the data-driven selection-specificity of the
action-attributable controllability write-back, with the |PE| mechanism failing its
pre-registered equivalence test on identical data (3.3); and (iv) the directional
restructuring of behavioral reachability under a matched present carried by path
memory alone (3.4). In-framework null/swap checks are pipeline validation throughout.
All claims are bounded by the audit's final judgment: constructive results in
designed models, not empirical evidence about natural systems.

---

# 4. Audit and evidential weighting

Before drafting, the frozen chain was subjected to an adversarial internal audit
covering reproducibility, seed hygiene, information flow at test time, the
mechanical status of each control, and the correct reading of the reported
statistics. We report its findings here rather than in supplementary material,
because the paper's central claims depend on which pieces of evidence can carry
weight — and two of the controls we ourselves designed turned out to carry less
than their labels suggested. The audit re-classified all evidence into
**load-bearing** and **pipeline-validation** tiers; the claims in this paper rest
exclusively on the former.

## 4.1 Verified properties

Three properties of the chain were verified directly:

**Reproducibility.** Re-running the tiny-MDP holdout under the frozen
configuration reproduced the committed results file bit-identically
(deterministic seeding). The figures in this paper are generated by a read-only
script over the frozen results files; no number in the manuscript is produced by
re-simulation.

**Seed hygiene.** Every holdout seed set is disjoint from its own calibration set
and from all other phases' holdout sets (Phase 2b: 20000–20039; Phase 2c:
30000–30039; tiny-MDP: 40000–40049; calibration seeds 1–5 are shared between
Phase 2c and the tiny-MDP, which use different models). No holdout seed
participated in any calibration decision.

**Only-m carry at test.** In the tiny-MDP, the future-task function receives only
the path memory m from formation; code inspection confirms it references no
formation-side outcome model, controllability signal, counters, or traces, and
the structural zero same-m/different-z = 0 confirms the plumbing end-to-end. This
is an implementation-level check of the identification design (Methods 2.8), not
itself causal evidence.

## 4.2 Load-bearing evidence

Two results carry the paper's claims.

**(a) Selection-specificity of the write-back is data-driven.** Active agents
develop high controllability signals and peaked path memories while their yoked
partners — receiving the same reward stream with the action→outcome edge cut —
remain near zero and diffuse. This asymmetry emerges from each agent's data, not
from the estimator: the scoring rule is identical for every arm and never sees
the group label, and the manipulation check verifies the yoke empirically
(yoked choice–reward correlation −0.001). The prediction-error baseline running
through the identical pipeline reproduces the Phase 2b failure (active ≈ yoked
within the pre-registered equivalence bound), so the asymmetry is specific to
action-attributable information, not to volatility exposure or reward statistics.

**(b) The behavioral signature is directional.** The consolidated memory does not
merely make active and yoked agents different; it makes them different in the
three pre-registered directions — history-aligned advantage (+0.221), blocked
stickiness (+0.582 non-arrival), novel-goal restriction (−0.278) — with the
primary macro-TV (0.374; 95% CI lower bound above Δ_min = 0.15). A bidirectional
signature of this shape is a non-trivial prediction: consolidation buys
history-aligned advantage at the price of perseverative cost, which no
magnitude-only divergence statistic would establish.

## 4.3 Pipeline validation (downgraded)

Three controls originally framed as a causal battery were downgraded by the audit
to **pipeline validation**: they verify that the identification plumbing works,
and must not be cited as independent causal isolation.

- **memory-swap = 0 is mechanical.** As implemented, the swap comparison
  evaluates the yoked memory against itself, so zero is guaranteed by
  construction; the alternative framing (active versus active-carrying-yoked-m)
  numerically equals the main effect. Because the future task is a deterministic
  function of (m, seed), a swap cannot carry information beyond the main
  comparison.
- **memory-null = 0.044 is architecture-bound.** The residual is the difference
  between a uniform-m future and a near-zero-m (yoked) future — two slightly
  different diffuse memories under the bounded retention pull. It confirms that
  the active advantage requires its specific peaked memory, but it lives inside
  the future = f(m) architecture and is not independent causal proof. (We report
  the uniform-m ablation because it is the stricter, more principled choice;
  ablating to the yoked memory itself would give exactly zero.)
- **same-m/different-z = 0 is structural.** The future task takes no z argument,
  so this zero is tautological; its value is as a code-level confirmation of the
  only-m design.

The causal force of the paper therefore rests on the yoked and sham comparisons
during formation (where the data, not the architecture, decide the outcome), not
on post-hoc ablations inside an architecture that already fixes the answer.

## 4.4 Statistical disclosures

**Bootstrap units.** The tiny-MDP holdout resamples seeds (50 units; 10,000
paired resamples), and is the paper's confirmatory statistic. The Phase 2c
holdout pooled seed × volatility cells (80 values, two per seed), which
treats the within-seed volatility cells as separate resampling units; Phase 2c is accordingly positioned as mechanism
feasibility, its statistics are not re-used for confirmation, and the unit is
disclosed as a known limitation (Section 6).

**Confidence-interval reading.** The reported CIs are extremely narrow (e.g.,
macro-TV [0.374, 0.375]) because each per-seed statistic already averages over
N = 400 agents in a frozen, deterministic model. These intervals quantify
**cross-seed reproducibility of the frozen model**, and nothing else. They are
not construct-level confidence intervals and carry no claim about robustness to
architectural, parametric, or environmental variation.

**Provenance.** Each experiment directory is frozen with locked configuration and
seeds, results files, identification tests, and a hash manifest; the Phase 2b
negative result is retained frozen in the chain. One process defect found by the
audit (a documentation edit that outdated one manifest hash) was repaired by
superseding manifests; code, parameters, and results files were bit-unchanged
throughout.

---

# 5. Discussion

## 5.1 What the designed models establish

The chain answers one identification question: after the observable present is
matched, can a system's past selection–consequence history — carried by a slow
path memory — change its future reachable behavior? In the constructive models we
built, the answer is yes, and it decomposes into four separable facts. First,
persistence, general transition-rule change, and selection-specific write-back are
bidirectionally dissociable — neither implies the other — which means a future
that merely persists, or a rule that merely changed, is not yet evidence of a
selection-specific inscription. Second, the most obvious mechanism for such an
inscription — accumulating raw prediction error — fails the selection-specificity
test: a yoked agent receiving the identical reward stream but stripped of the
action→outcome coupling reproduces the effect. Third, replacing that signal with
action-attributable predictive information — how much the agent's own chosen action
improves outcome prediction over a reference measure — restores selection
specificity, and does so from the data rather than from the definition: the same
scoring rule returns near zero for the yoked arm, and in the sham arm — where
outcomes are driven by an observable external action — self-attribution is near
zero while external-attribution is positive, showing that controllable structure
alone does not gate consolidation unless it is attributable to the agent's own
actions. Fourth,
the resulting memory redirects future behavior in a directional way: it buys
history-aligned advantage and pays a perseverative cost when the world blocks the
old path or poses a novel goal.

The negative result in the middle of this chain is not incidental. It is the
reason the mechanism has the form it does. Had we started from action-attributable
information we could not have known it was necessary; the yoked control on the
prediction-error mechanism is what forced the revision. We therefore present the
failure as a load-bearing part of the argument rather than as discarded scaffolding.

We state the scope plainly. These are designed systems, the memory-to-future
channel is an architectural premise rather than a discovered mechanism, and the
narrow intervals report reproducibility of frozen models, not confidence in the
constructs (Sections 4 and 6). The contribution is an identification framework
and a worked demonstration that the framework discriminates — a constructive
computational result, not an empirical claim about nature.

## 5.2 Relation to existing frameworks

The question here is deliberately narrow, and this narrowness is what separates it
from adjacent accounts. Dynamical-systems theory characterizes stability,
attractors, hysteresis, and bifurcation; control theory characterizes the cost of
reaching or holding a target; reinforcement-learning accounts of habit and
metaplasticity characterize how experience reshapes future updates; the
free-energy principle and active inference characterize adaptive regulation under
a boundary. Each of these covers part of the target. What they do not, **to our
knowledge**, package together is the specific identification test at the center of
this paper: hold the present state, fast values, and initial action distribution
fixed; vary only the history-formed slow memory; and ask whether the future
behavioral arrival distribution changes, with yoked and sham controls that
differentiate selection-specific from generic history dependence. We make no claim that these
frameworks are wrong or superseded — several of our own constructs are standard
instances of them — only that the identification question and its control battery
appear not to have been assembled in this form. Prediction-error metaplasticity in
particular is real in our models (Phase 2b); our point is precisely that it is not,
by itself, selection-specific, which is a statement about what that mechanism does
not distinguish, not a refutation of it.

Two of the closest neighbors are our own. **Costly selective closure** asks what
makes an artificial system life-like and isolates token-level irreversibility
through post-withdrawal cooperation; its central operation is persistence after
support is withdrawn. The present paper asks an orthogonal question —
identification under a matched present — and treats persistence-after-withdrawal
not as the target but as one dissociable component (P) that we show is neither
necessary nor sufficient for selection-specific write-back. The two papers share a
vocabulary of selection and history but answer different questions with different
endpoints. **Ontological friction (Ψ_f)** models a latent cross-modal control-cost
factor for executive breakdown. This paper does not use anchoring friction or any
Ψ_A as a load-bearing construct; cost enters only as the two side-measurements
J_ext and J_write in Phase 1, with the explicit finding that neither tracks
selection-specific write-back — the highest write dissipation belongs to the
nonspecific control. A reader familiar with that line of work should read the
present contribution as concerning identification of history-dependent
reachability, not as a cost theory.

## 5.3 An operational bridge to selective-reality constructs

The constructs in this paper were chosen so that they could, in principle, serve as
operational counterparts to elements of a broader selection-first account of
reality: the accessible alternatives from which an outcome is selected; the
selection-specific write-back by which a manifest state deposits a durable
constraint; and the resulting change in what the system can subsequently reach. In
that vocabulary, the tiny-MDP result reads as a worked instance of a manifest
selection (L1) depositing a slow constraint (L2) that reshapes the accessible
future (L0′), under a matched present. We offer this mapping strictly as an
**operational bridge**, not as an ontological proof. Nothing here shows that any
natural system realizes these constructs, that a modal field of selectability
exists in general, that selection precedes existence, or that value or subjecthood
follows; those remain outside the evidence this paper can carry (Section 6). What
the bridge does provide is a concrete, falsifiable template — matched present,
varied history, controlled selection specificity, behavioral reachability readout —
against which such larger claims could later be tested in systems we do not design.
The value of a real negative result inside this chain is exactly that it shows the
template can fail; that is the property a bridge to empirical work must have.

---

# 6. Limitations

**1. Everything shown is a designed model.** All five systems were constructed to
make the constructs separable and the identification clean. The results are
constructive existence and identification results: they show that persistence,
nonspecific rule change, and selection-specific write-back *can* be dissociated,
that a selection-contingent consolidation mechanism *can* be built and detected
under yoked and sham controls, and that a written path memory *can* redirect
future reachability under a matched present. They do not show that any natural
system — biological, neural, or social — implements this architecture, and no
claim in this paper should be read as empirical evidence about natural systems.

**2. The m → future channel is part of the architecture, not a discovery.** In
the tiny-MDP, the consolidated memory shapes the future through a bounded
retention pull that we defined. What the experiments establish is conditional:
*given* such a channel, action-attributable gating plus consolidated content
produce directional reachability restructuring that survives the identification
battery. The existence of the channel itself is an architectural premise —
demonstrated to be buildable, not discovered in any target system. The same
holds for the double-well system, where the plasticity channel z was likewise
defined into the dynamics.

**3. Phase 2c's frozen pre-holdout analysis treats within-seed volatility cells as separate resampling units.**
The frozen Phase 2c holdout pooled seed × volatility cells (80 values from 40 seeds)
rather than resampling seeds. We retain that frozen pre-holdout interval as provenance
and additionally report a post-audit seed-clustered bootstrap (average the two
volatility cells per seed, then resample the 40 seeds) as the preferred inferential
summary; the two agree in direction and conclusion (Results 3.3), and the frozen GO
is unchanged. Regardless, Phase 2c is positioned as mechanism feasibility only; the
confirmatory statistics of this paper come exclusively from the tiny-MDP holdout,
whose bootstrap unit is the seed (50 units, 10,000 paired resamples).

**4. The narrow confidence intervals measure model reproducibility, not
construct confidence.** Intervals such as macro-TV [0.374, 0.375] arise because
each per-seed statistic averages N = 400 agents of a frozen deterministic model.
They quantify cross-seed reproducibility of that model and must not be read as
high confidence in the constructs, nor as robustness to architectural,
parametric, or environmental variation. Construct-level uncertainty is not
estimated anywhere in this paper.

**5. The ablation battery is pipeline validation, not causal isolation.**
memory-swap is mechanical (zero by construction), memory-null is
architecture-bound (a residual between two diffuse memories inside the
future = f(m) design), and same-m/different-z is structural (the future task
takes no z argument). They verify the only-m plumbing and nothing more
(Section 4.3). The causal weight of the paper rests on the formation-side
active/yoked/sham comparisons, where the data decide the outcome.

**6. No validation beyond designed systems.** The mechanism has not been tested
in end-to-end trained networks, in biological preparations, or in humans. Our
earlier attempt to run a matched-endpoint history test in an end-to-end
image classifier (Fashion-MNIST) ended in an identification NO-GO: no valid
matched groups existed because history and endpoint live in the same weight
vector. That result is a failure of *that protocol under that architecture* —
it must not be read as evidence that history-dependent reachability is absent
or unidentifiable in end-to-end systems in general. Identifying architectures
in which fast state can be matched while slow history varies remains open
outside designed models.

**7. Scale and scope of the environments.** The systems are deliberately
minimal: one-dimensional dynamics, two- and three-armed bandits, a two-step MDP
with three goals. Role counterbalancing, interior (non-saturated) operating
points, and pre-registered thresholds mitigate — but do not remove — the risk
that the effect sizes are idiosyncratic to small state spaces. The
pre-registered thresholds (Δ_min, equivalence bounds) are themselves
model-relative conventions, not theoretically derived quantities.

**8. Deferred components.** The external-action sham was added only at the
tiny-MDP stage (Phase 2c v1 omitted it rather than duplicate a hidden yoked
control); the latent-inscription condition is established at selection-episode
scale only, and its durable form was obtained only after replacing the
state-tracking slow variable with the two-timescale architecture. The per-class
four-bar arrival distributions and the latent erosion were completed by the
authorized extraction round; the latter is reported only as a **two-point erosion
comparison** (episode-end vs end-of-observation z), because a per-step record is not
extractable without editing frozen code.

**9. What this paper does not claim.** Per the claim ledger fixed before
drafting: no claim that natural systems exhibit historicity write-back; no claim
about the general ontology of possibility spaces; no claim that selection
precedes existence; no claims about value, subjecthood, or consciousness; no
claim of superiority over the free-energy principle, integrated information
theory, or reinforcement-learning accounts of habit — the relation to these
frameworks is complementarity of question, addressed in Section 5; and no
reading of the reported intervals as construct-level confidence.

---

# Figures and captions (back matter)

## Figure 1 — The identification problem and formal framework

**(A)** Framework: a selection–consequence history is scored by the
action-attributable log-likelihood-ratio signal r_t, which drives the slow gate z
(write *strength*); consolidation writes path content into the memory m, and the
future reachable outcome set Γ'_H is a function of m alone. Core statement: with the
present state matched (x_A = x_B) but histories differing (m_A ≠ m_B), future
outcome distributions differ. **(B)** Constructive instance from the double-well
system (S1): two ensembles at the identical present state (present-state gap
0.0000), one carrying an anchoring history and one naive, end in maximally
separated, non-overlapping finite-horizon outcome distributions under the specified
adverse probe — raw future P(M+) = 1.000 (anchored) vs 0.000 (naive); TV = 1.000,
JS = 0.693. *Source: results_matched_future.json.*

## Figure 2 — Constructive dissociation of P, W_global, and W_sel (S1)

**(A)** The P × W_sel plane with all six conditions. Co-located conditions are drawn
as ring + filled marker: at (0, 0) A_transient (ring) with RoughenWrite (diamond);
at (0, 1) PreExistingWell (ring) with B_clamp while held (cross). All four cells are
occupied — persistence does not imply selection-specific write-back
(PreExistingWell), and write-back does not imply persistence (LatentInscription, at
selection-episode scale) — a bidirectional dissociation, not an independence claim.
The clamp collapses to P = 0.00 on withdrawal (arrow). RoughenWrite carries the
largest general rule change of any condition (W_global KL = 7.98) with W_sel ≈ 0:
general rule change does not measure selection-specific write-back. **(B)** Neither
cost tracks W_sel: external effort J_ext is identical (17.3) for all non-clamp
conditions (clamp: 86.4), and the largest write dissipation J_write (6.70) belongs
to the *nonspecific* control, while the anchoring condition pays 0.28. **(C, D)**
Phase diagrams over (η, D0): each cell class occupies a contiguous region (anchor
cell 49, latent cell 56 of 63 grid cells), not a tuned point.
*Sources: results_dissociation.json, results_sweep.json.*

## Figure 3 — The failed mechanism and its revision (pivot figure)

Three panels; the data of Phases 2b and 2c are strictly separated. **(A)** Phase 2b
(locked holdout, frozen parameters, 40 fresh seeds): with the prediction-error
integrator |PE| → z, the master-yoked group — same reward stream, no
choice→consequence coupling — reproduces the future effect of the active group
(0.239 vs 0.238; d = 0.05). History-dependent, but not selection-specific: NO-GO.
*Source: results_phase2b.json.* **(B)** Phase 2c, pre-registered equivalence test of
the |PE| baseline *within the revised framework*: paired active−yoked commitment
0.087, 90% CI [0.082, 0.091], entirely inside the ±0.15 equivalence bound (shaded).
This is a distinct experiment and statistic from panel A. *Source:
results_2c_holdout.json.* **(C)** Phase 2c primary (same source): replacing the gate
with the action-attributable controllability score r_t yields paired active−yoked
commitment 0.570, 90% CI [0.559, 0.581], above the pre-registered Δ_min = 0.20. The
frozen negative result in (A) forced the mechanism revision confirmed in (C); (B)
shows the failed mechanism failing again on identical data inside the revised
framework.

## Figure 4 — tiny-MDP protocol and sham mechanism gate (S4)

**(A)** Protocol: formation under active / master-yoked / external-action-sham
coupling; exact matching of environment state, fast values Q, and initial action
distribution; **only the path memory m is carried** into a frozen-parameter task
battery (aligned / blocked / novel; goal and blocked roles counterbalanced across
seeds). Terminal outcomes are four-vectors [P(G0), P(G1), P(G2), P(∅)] including a
timeout/non-arrival component. Formation q, z, counters, and traces are never read
at test (code-verified; the structural zero same-m/different-z = 0 is an
implementation-level pipeline check confirming only-m carry — it is not independent
causal evidence). **(B)** Sham mechanism gate:
outcomes driven by an observable external action produce near-zero self-attribution
(−0.015) but clearly positive external-attribution (+0.143) — controllable structure
that is not attributable to the agent's own actions does not gate consolidation.
*Source: results_mdp_holdout.json.*

## Figure 5 — Directional behavioral reachability under a matched present (main result)

**(A–C)** Role-aligned mean arrival distributions [P(G_hist), P(G_other),
P(G_novel), P(∅)] for active vs yoked in each battery class (50-seed means from the
authorized extraction round). Aligned: active concentrates on the history goal
(0.86 vs 0.64). Blocked: active perseverates into non-arrival (P(∅) = 0.61 vs 0.03)
while yoked reaches the alternative goal (0.77). Novel: active is drawn back to the
history goal (0.50) and reaches the novel goal less (0.36 vs 0.64). **(D)** Paired
active−yoked differences with 95% CIs, all three pre-registered direction gates
passing: aligned advantage ΔP(G_h) = +0.221 [+0.219, +0.223]; blocked stickiness
ΔP(∅) = +0.582 [+0.580, +0.583]; novel restriction ΔP(G_novel) = −0.278
[−0.280, −0.276]. Consolidation buys history-aligned advantage at the price of
perseverative stickiness. **(E)** Primary endpoint: equal-weight macro-TV between
active and yoked arrival distributions = 0.374, 95% CI [0.374, 0.375], with the CI
lower bound directly above the pre-registered Δ_min = 0.15 (50 fresh seeds; 10,000
paired bootstrap resamples). **(F)** Per-seed macro-TV distribution (extraction
round; axis zoomed to the data range — all 50 seeds lie far above Δ_min). The
narrow CIs reflect cross-seed reproducibility of a frozen deterministic model (each
per-seed statistic averages N = 400 agents); they are not construct-level
confidence intervals. *Sources: results_mdp_holdout.json (D, E);
extraction_round.json (A–C, F).*

## Supplementary figures

**S1 — Washout-length curves (Phase 2b).** Retention of the volatile-vs-stable z gap
(1.00 / 0.90 / 0.82 / 0.67 / 0.45 / 0.20 across 0–800 unexpressive steps) and the
corresponding frozen-z future effect (peaking 0.486 at 100 steps, decaying to 0.002
at 800): the inscription is durable over moderate unexpressive horizons and leaky
over long ones. *Source: results_phase2b.json.*

**S2 — Pipeline validation (tiny-MDP), labeled as such.** memory-null macro-TV
0.044 [0.043, 0.045]; memory-swap 0.000; same-m/different-z 0.000; all within the
±0.05 equivalence bound. These verify the only-m plumbing (m is the sole carrier
read at test) and are **not** independent causal evidence: the swap comparison is
mechanical, the null residual is architecture-bound, and same-m/different-z is
structural. *Source: results_mdp_holdout.json.*

**S3 — Permutation control (Phase 2b).** After cross-individual permutation of the
carried z, future recovery follows the carried value (r = 0.761), not the history
label (r = 0.007). *Source: results_phase2b.json.*

**S4 — State-tracking erosion of an off-target write (two-point).** Ensemble-mean
slow variable z at the end of the selection episode vs the end of the observation
window, frozen seeds 11–15, from the authorized extraction round:
LatentInscription +0.742 ± 0.000 → −5.543 ± 0.033 (the off-target write erodes as
the state-tracking z follows the fast state back to the home basin), while
C_anchor +1.534 ± 0.000 → +3.322 ± 0.000 (the expressed write self-consolidates).
This is a **two-point erosion comparison**, not a trajectory or time course: a
per-step record is not extractable without editing frozen code, so only the two
endpoints are reported. *Source: extraction_round.json.*
