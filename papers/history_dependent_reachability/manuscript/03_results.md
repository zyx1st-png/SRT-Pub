# Results

> Draft section. Every number below is taken from `../RESULTS_NUMBERS.md` (generated
> read-only from the frozen results JSONs); source files are named per subsection.
> Items marked **[pipeline validation]** verify the identification plumbing and are
> not cited as independent causal evidence (see `../CLAIM_LEDGER.md`).

## R1. Persistence, rule change, and selection-specific write-back are dissociable constructs (S1)

*Source: anchoring_double_well/results_dissociation.json, results_sweep.json,
results_matched_future.json.*

Six conditions with identical external drive (J_ext = 17.3 for all except the clamp)
populate the P × W_sel plane (Table 1):

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
the state-tracking limitation that motivates the two-timescale agents of R2–R4.

Parameter sweeps confirm the cells are regions, not tuned points: the anchoring cell
occupies 49 and the latent cell 56 contiguous grid cells of the 9 × 7 (eta, D0)
phase diagrams.

**Matched present, different future.** With the present state matched exactly
(gap = 0.0000) and identical forcing and noise, the ensemble carrying the
C_anchor-written landscape ends in reachable set {M+} with raw future
P(M+) = 1.000, while the naive ensemble ends in {M−} with P(M+) = 0.000
(future divergences: KL = 20.7, JS = 0.693, TV = 1.000). The entire difference lives
in the written slow variable.

## R2. A pre-registered negative result: prediction-error accumulation is history-dependent but not selection-specific (S2, Phase 2b)

*Source: anchoring_bandit_holdout/results_phase2b.json. All parameters frozen from
the Phase 2 feasibility commit; 40 fresh seeds; no retuning.*

The frozen |PE|-integrator mechanism **generalized** to new seeds: the volatile-vs-
stable z separation survived the unexpressive washout (67% retained, minimum 67%),
the frozen-z future effect was 0.241 ± 0.010 with 100% of seeds positive, the null
control abolished it (mean |diff| = 0.010), and the swap control reversed it (100%
of seeds). A cross-individual permutation confirmed the effect follows the carried z
value, not the history label (recovery~z = 0.761 vs recovery~label = 0.007).

It nevertheless **failed selection-specificity**: a master-yoked group receiving the
same reward stream with no choice→consequence coupling reproduced the future effect
essentially in full — active 0.239 vs yoked 0.238 (d = 0.05); the formed z-gap ratio
was 1.20 (active 1.237 vs yoked 1.031), far short of the pre-registered ≥ 1.5
margin. (A gap Cohen's d computed on ensemble means reached 17.8 and was excluded by
design as a variance artifact.) A small genuine selection signature existed —
active stable-history z (2.661) below yoked (2.896), because choice contingency lets
the active agent learn and reduce surprise — but it did not translate into any
differential future consequence.

**Verdict (frozen): NO-GO.** Accumulated |PE| is a reward-stream volatility tracker
available to any observer, not a selection-specific write-back. Washout-length
curves (retention 1.00 / 0.90 / 0.82 / 0.67 / 0.45 / 0.20 across 0–800 steps; future
effect decaying from 0.486 at 100 steps to 0.002 at 800) show the inscription is
durable over moderate unexpressive horizons and leaky over long ones. This negative
result forced the mechanism revision of R3.

## R3. Action-attributable controllability yields selection-specific write-back (S3, Phase 2c)

*Source: anchoring_2c_controllability/results_2c_holdout.json. Frozen parameters;
40 fresh seeds; thresholds pre-registered. Bootstrap unit is seed × volatility
(80 values); Phase 2c is mechanism feasibility — confirmatory statistics are carried
by R4.*

With the gating signal replaced by the mu-mixture log-likelihood-ratio score r_t
(Methods M4), the paired active−yoked difference in content-neutral future
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
reported in R2; together they show the failed mechanism failing again inside the
revised framework while the controllability mechanism succeeds on identical data.

The z-formation coupling effect was sign-stable (ctrl active−yoked: +0.264 high,
+0.931 low; |PE| active−yoked: −0.070, −0.078 — the |PE| signal is, if anything,
slightly *higher* for yoked). Yoked decoupling was verified in the data
(ctrl-corr −0.000 vs active +0.270), and the structural controllability index
separated groups (C_mu 0.121 active vs 0.022 yoked). **[pipeline validation]**
Consolidation-null collapsed active commitment (0.997 → 0.000) and memory-swap
followed the memory donor (gap +0.000 vs yoked 0.427): these verify the z→m→future
plumbing and are not independent causal evidence.

## R4. History-formed path memory restructures behavioral reachability under a matched present (S4, tiny-MDP — main result)

*Source: anchoring_tiny_mdp_confirmatory/results_mdp_holdout.json. Thresholds locked
before calibration (Delta_min = 0.15, eps_TV = 0.05); 50 fresh seeds (40000–40049);
10,000 paired bootstrap resamples; per-seed bootstrap unit. Failures: NONE.*

With state, fast values Q, and the initial action distribution matched exactly and
**only m** carried from formation, the equal-weight macro-TV between active and
yoked goal-arrival distributions was **0.374, 95% CI [0.374, 0.375]** — the CI lower
bound directly exceeds the pre-registered Delta_min = 0.15.

The difference is directional, in all three pre-registered senses:

- **Aligned (advantage):** active reaches the history goal more, ΔP(G_h) = +0.221,
  CI [+0.219, +0.223];
- **Blocked (stickiness cost):** with the history corridor blocked, active times out
  more, ΔP(∅) = +0.582, CI [+0.580, +0.583];
- **Novel (restriction cost):** active reaches a never-rewarded goal less,
  ΔP(G_novel) = −0.278, CI [−0.280, −0.276].

Consolidation therefore buys history-aligned advantage at the price of perseverative
stickiness — a bidirectional behavioral signature that a mere divergence magnitude
would not establish. The external-action sham behaved as the mechanism predicts
(self-attribution −0.015 ≈ 0; external-attribution +0.143 > 0): controllable
structure present in the stream but not attributable to the agent's own actions does
not gate consolidation. Yoked decoupling held (ctrl-corr −0.001).

**[pipeline validation]** memory-null = 0.044, CI [0.043, 0.045] (within ±0.05;
the residual reflects uniform-m vs near-zero-m ablation states);
same-m/different-z = 0.000 and memory-swap = 0.000 exactly, as structurally required
because the future is a deterministic function of (m, seed). These confirm that m is
the sole carrier read at test — the identification plumbing — and are not cited as
independent causal isolation.

The reported CIs measure cross-seed reproducibility of a frozen deterministic model
(each per-seed statistic averages N = 400 agents); they are not construct-level
confidence intervals.

## R5. Summary of the evidential structure

The load-bearing results are (i) the construct dissociation with its two behaving
counterfeits (R1); (ii) the frozen negative result that accumulated prediction error
is not selection-specific (R2); (iii) the data-driven selection-specificity of the
action-attributable controllability write-back, with the |PE| mechanism failing its
pre-registered equivalence test on identical data (R3); and (iv) the directional
restructuring of behavioral reachability under a matched present carried by path
memory alone (R4). In-framework null/swap checks are pipeline validation throughout.
All claims are bounded by the audit's final judgment: constructive results in
designed models, not empirical evidence about natural systems.
