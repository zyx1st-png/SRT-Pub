# Figures and captions

> Draft captions. All plotted values are read from the frozen results JSONs and
> from `../extraction_round.json` (single authorized deterministic extraction
> round) by `../make_figures.py` (read-only over `Experiments/`); rendered files
> live in `../figures/`. The previously deferred panels (Fig. 5 A–C and F;
> Supplementary S4) are now sourced from the extraction round.

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
