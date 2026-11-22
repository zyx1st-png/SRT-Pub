---
id: SRT-PR1137-POST-DP-METHOD-NO-GO-20261028
type: audit
status: draft
canonical: false
layer: operations
epistemic_layer: machine_analysis
claim_mode: paper_only_methodological_stop_and_research_redirection
created: 2026-10-28
updated: 2026-10-28
research_mode: U
dependency:
  - Operations/Proposals/SRT_GENERATIVE_MAINTENANCE_FULL_EXPERIMENT_DESIGN_V0_1_2026-10-28.md
  - Operations/Proposals/SRT_GENERATIVE_MAINTENANCE_REFERENCE_TRANSITIONS_V0_1_2026-10-28.md
  - Operations/Audits/SRT_GENERATIVE_MAINTENANCE_DESIGN_REVIEW_AND_IMPLEMENTATION_HANDOFF_2026-10-28.md
  - STATUS.md
tags: [MethodologicalNoGo, ExperimentAudit, CriticalReview, ArtificialLife, StopLoss]
---

# PR #1137 — post-DP methodological NO-GO (2026-10-28)

> **Disposition: METHOD NO-GO / NOT READY FOR R1 / DO NOT RUN G1 / DO NOT MERGE AS AN EXECUTABLE PROTOCOL.**
>
> The user provided an external critical review reporting exact DP on PR #1137's proposed transition profile (head `3c7003be`). This audit **preserves the review, corroborates rule-level criticisms by direct inspection, and separates externally reported numerical results from independently reproduced results**. The external script is located in a user's local Mac scratch path and was **not** retrieved or independently run here. No user-approved new theory decision, preregistration, or execution authority is inferred. The existing single CURRENT NEXT, CN-2 A, independent review/FR-ADV, and toy-execution HOLD are unchanged.

## A. What is decisively wrong without any DP

The reference transition defines R-wear rates:
- `G_closed: w(M=0)=0.50, w(M=1)=0.15, w(M=2)=0.05`.
- `G_open: w(M)=0.05` for every M.

Therefore at **identical immediate M and exogenous draw**, `w_closed(M)>=w_open(M)` identically. The local edge manipulation is **one-sided by construction** and its difference only represents a built-in protective advantage of open compared to damaged closed. A whole-system DP ordering is not logically guaranteed by that *local* inequality alone without checking state/action couplings, though the reviewer's claimed optimal-value results are consistent with it. The healthy state M=2 matching check is trivial because both mechanisms literally set 0.05.

**Decision:** reject current closed-versus-open as a substantive test of a beneficial organizational feedback mechanism; no amount of G1 seeds or PPO tuning rescues its causal claim.

## B. External numerical report (NOT independently reproduced)

The review author reports fully observed exact DP with hazard queue accessible to the planner, with survival probabilities:

| Initial condition | H=8 closed / open | H=16 closed / open |
|---|---|---|
| healthy | 1.000 / 1.000 | 0.9998 / 1.000 |
| M=0 | 0.998 / 1.000 | 0.980 / 1.000 |
| M=0,B=0 | 0.846 / 0.993 | 0.399 / 0.897 |
| C=1,M=0,B=0 | 0.479 / 0.975 | 0.121 / 0.850 |

**Provenance:** user-provided evaluation text, said to come from a local `scratchpad/dp.py` in a Mac temp worktree; that file is not in this PR. Treat the values as **reported external findings requiring independent reproducer/code-identity verification**, not as experimental results from this repository.

If validated: healthy reference values suffer ceiling effects, damaged cases show large expected open advantage; E=2 and E=6 behaving alike in tested states suggests energy is nonidentifying in that regime (do not extrapolate to all possible states).

## C. Additional rule-level and construct objections

- **C=0,R=0 is not spontaneously repairable under the current action preconditions.** Calibration of C requires R>=1, repair of R requires C>=1; without other input the model has no autonomous way back. The two-step failed-function counter cannot genuinely identify ordinary recovery across this state. The possible value of a 2-step grace counter in other configurations is a different question.
- **J effects are preprogrammed twice**, both traverse success (0.9/0.1) and U/V damage probabilities (0.75/0.15). They are manipulation checks, not evidence of new affordance grammar or endogenous generation.
- **Full-state G0 DP reads queued true hazards that G1 agents cannot.** It is an oracle upper bound, not a lawful information-matched learning benchmark. A belief-state POMDP benchmark would be needed, with explicit observation history, calibration and accuracy/error bounds. Filtering some hidden variables may factorize under assumptions; **computing the optimal policy over the continuous belief space is not automatically trivial** even when the finite physical state space is modest.
- **Cross-world raw log-loss is not a fair causal algorithm comparison**, because targets and base event probabilities can differ. Where an appropriate Bayes comparator exists, evaluate within-world out-of-sample proper-loss regret `loss(model,g)-loss(Bayes lawful,g)`, then compare regrets, using the same legal information and calibration. For control compare `V^*_lawful,g - V^π_g` or analogous regret, not ratios near V*=0 or unobserved oracle DP values. Keep world-specific absolute outcomes for descriptive causal analysis.
- **Sham is mechanically the same as closed**, making it a unit test or A/A diagnostic, not an independent quarter of the large confirmatory model budget.
- **Paired train seeds alone do not ensure material variance reduction**: cross-world trajectories/policies diverge; estimate paired covariance from an independent calibration/pilot if ever authorized, otherwise use conservative unpaired power.
- **State equivalence/controlled predictive partition is source-owned**, related to MDP bisimulation, predictive state representations, computational mechanics and task-limited action-conditional abstraction. Related sources: Givan, Dean & Greig (2003), DOI 10.1016/S0004-3702(02)00376-4; Ferns, Panangaden & Precup (2004), *Metrics for Finite Markov Decision Processes*; Zhang et al. (ICLR 2021), *Learning Invariant Representations for Reinforcement Learning without Reconstruction*. The particular §5.2 definition is **task-/horizon-limited predictive equivalence**, not necessarily the full reward-and-transition recursive bisimulation relation. This distinction avoids both claiming novelty and overidentifying nonidentical mathematical definitions.
- **Two specification sources conflict** (7 vs 8 actions/observe; transient vs persistent L; fail-traverse damage; open g(M?) vs constant), so the candidate is not yet a frozen implementation contract. The companion reference file resolves some variants by priority, but having contradictory general formulas is a review liability.
- **Construct mismatch:** the organism is a designer-specified fixed M/C/R slot graph with two predetermined J constructions. Testing agents' control of this graph does **not** investigate the emergence of a maintenance-constituted individual, new component relations, or coarse-graining before individuated boundaries. The original question was maintaining a *continuously generated structure*, not holding fixed physiological slots.

## D. Yoked protection is a design candidate, not a sufficient fix

The review proposes replaying protective inputs from actual closed trajectories into open; this is better motivated than fixed 0.05, but must not be automatically labeled “clean causal identification”.

1. **Within-tape same-trajectory yoked replay** can carry correlations between `z_t` and exogenous shocks, policy response and past M; the causal quantity may still include shock alignment or history selection. Simply matching the marginal input histogram is insufficient.
2. **Independent-cross-trajectory, phase-shifted, or conditional-lawful-history replay** each tests a *different* hypothesis. For each specify what information is withheld, and what distribution of protection amount, timing, history and energy flow is matched.
3. Exogenous input playback can change dynamic resource/energy availability; preserving downstream state exactly would block the hypothesized mediation. Define a total effect versus a deliberately controlled direct effect rather than calling all differences "feedback".
4. **Even an ideal yoked contrast is a feedback-control question**, already in classical control theory. A successful result cannot by itself answer the user's stronger question about endogenous genesis of an organization's own relevant distinctions.

**Stop loss:** do not retrofit the current design with yoked replay and immediately approve 57.6M steps. First state an outcome which would materially alter the research decision.

## E. The missing value-of-information decision (the main failure)

Three cases exhaust the existing primary claim for the proposed small fixed-body POMDP:
- G0 succeeds: an explicitly coded feedback world has its explicitly coded dynamics; not a new observation about spontaneous generative organization.
- G1 strong RL succeeds: mature world-model/HRL sufficiency is confirmed locally, but the target is already known to be explainable in these frameworks.
- G1 fails: finite train-budget/task difficulty is inconclusive about autonomous generation.

**There is no predeclared discriminating result that moves the central claim forward.** This is more fundamental than optimizer, seed count or DP implementation. The main experiment must remain **NO-GO** until a user-meaningful, non-tautological success/failure predicate exists.

## F. CI provenance (verified separately)

GitHub Actions workflow run `40626046699`, job `122611094705`, for PR head `3c7003be` ended FAILURE. Its log reported `context bundle freshness` failed for `SRT_CONTEXT_BUNDLE_SPINE.md`; workflow attribution reported `failure_scope=base_main`, `base_main_health=failure`, while changed frontmatter reported `errors=0,warnings=0`. This is **a real red CI**, but the evidence does *not* establish that the three added experiment documents caused it. Resolve via scoped repository maintenance when appropriate, not via changing simulation hyperparameters or claiming CI passes.

## G. Decision and research redirection

**Proposed PR disposition:** keep the record available as a rejected method candidate, mark prominently `METHOD NO-GO`; do not proceed to R1, G0 implementation or G1 model training; do not merge this protocol as executable design.

For any successor exploratory concept, first answer:
1. **What exactly remains unspecified at t0?** An agent boundary? maintenance network topology? component identity? mapping from environmental differences to endogenous significance? If all of them are specified, do not call later repair “endogenous genesis”.
2. **Which precise counterfactual result changes the next action?** E.g. if a minimal chemical/graph organization self-constitutes under a neutral dynamics family more often than matched no-reciprocity controls **without fitness labels to the learner**, what would that establish, what mature chemistry/automata result already covers it, and what outcome would stop the route? Do not assert such a result yet.
3. **Can the strongest mature models already fully simulate it?** That may still be interesting for mechanistic sufficiency, but without a novel identified question it does not warrant a large empirical budget.
4. **What is the smallest paper-only discriminating environment with nontrivial negatives?** If it cannot be described without selecting the desired result by construction, stop before code.

**No successor experiment chosen or authorized by this audit.** Existing one CURRENT NEXT / CN-2 A and all canonical / FR-ADV / toy HOLD remain unchanged.
