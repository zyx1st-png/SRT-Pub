# PAPER CHARTER — History-Dependent Reachability

**Status:** paper constitution, locked before manuscript drafting. Changes to this file
require explicit author decision, not drafting convenience.
**Branch discipline:** evidence source of truth = tag `archive/anchoring-audit-2026-07-17`
and the six frozen commits on `research/selective-anchoring`. This paper branch adds only:
charter files, figure plan, result-extraction scripts/tables, manuscript, supplementary.
**No new experiments. No modification of frozen code, params, or results JSON.**

> **Author status-sync decision (2026-08-18):** bibliographic status may be updated
> without reopening the scientific charter. `Costly Selective Closure` is now recorded
> as submitted to *Adaptive Behavior*. The former Frontiers manuscript `1837760` is now
> the published article Zhang (2026), DOI `10.3389/fnins.2026.1837760`.

## The single question of this paper

> After the observable present state and the fast policy are matched, can past
> selection-consequence history — carried by a slow path memory — restructure the
> system's actually reachable future behavioral outcomes?

## Paper type

**Constructive computational theory / methods paper.** It establishes construct
separability, an identification strategy, and a mechanism existence proof in designed
models. It is NOT an empirical paper about natural systems, NOT a proof of SRT ontology,
NOT a consciousness/value/life paper.

## What this paper is NOT about (do not let these back in)

Ontological friction as a load-bearing construct; the full SRT system; consciousness;
value / d-value; definitions of life. These appear only in the final Discussion
subsection as a research-program bridge, explicitly labeled an **operational bridge,
not an ontological proof**.

## Title (decided)

**Identifying History-Dependent Reachability: A Constructive Framework for
Selection-Specific Write-Back**

Decisions bound to this title:
- The framework-identifying framing (not "Reshapes...") matches the evidence level:
  what is shown is constructibility + identifiability in designed models.
- **Terminology unified to "selection-specific"** (matches frozen READMEs/AUDIT.md and
  the `W_sel` notation). "Selection-contingent" is NOT used. If a venue prefers it, the
  equivalence must be declared at first definition — but default is selection-specific
  everywhere.

## Self-demarcation (mandatory, Intro + Related Work)

Two paragraphs distinguishing this paper from the author's own prior work — this is the
first attack a reviewer familiar with the program will make:
- **Costly Selective Closure (CSC / Adaptive Behavior submission):** asks "what counts
  as life-like" and isolates token-level irreversibility (V) via post-withdrawal
  cooperation. This paper asks an orthogonal **identification** question: matched
  present, different history → different future reachability. Persistence-after-
  withdrawal appears here only as one construct (P) among three, and the flagship
  result is about W_sel and reachability, not stake or life-likeness.
- **Executive-friction / ontological-friction line (Zhang 2026, Frontiers in Neuroscience
  20:1837760; DOI `10.3389/fnins.2026.1837760`):** a published cross-modal
  control-cost framework for executive breakdown. This paper does **not** use `Psi_f` /
  anchoring friction as a load-bearing construct; cost appears only as J_ext/J_write
  side-measurements in Phase 1, with the explicit finding that neither tracks W_sel.
- Also position against: path dependence, metaplasticity, RL habit formation, control
  theory, FEP/active inference. The claim is not that these are wrong, but that — **to
  our knowledge** — none of them provides the S/P/W_sel identification battery under
  matched present states. All exclusivity claims in Related Work MUST carry the
  "to our knowledge" qualifier; no bare universal negatives.

## Section structure (locked)

1. Introduction — the identification problem: same current behavior ≠ same future structure.
2. Construct Definitions — P, W_global, W_sel; r_t (mu-mixture LLR); r_t → z → m
   (z = write strength, m = path content).
3. Identification Strategy — active / master-yoked / external-action sham; matched
   state/Q/action-distribution; formation→calibration→freeze→holdout; why the Phase 2b
   NO-GO is retained as a formal result.
4. Constructive Dissociation (Phase 1) — P/W_global/W_sel separation; matched fast
   state, different slow constraint; measurement instruments.
5. Failed Mechanism: Prediction-Error Accumulation (Phase 2b) — |PE| write-back is
   history-dependent but NOT selection-specific (yoked reproduces the future effect
   within the pre-registered equivalence bound). **The theoretical pivot of the paper.**
6. Selection-Specific Consolidation (Phase 2c) — action-attributable predictive
   information; active-yoked separation; |PE| negative baseline; z/m split.
   Statistical role: mechanism feasibility (bootstrap unit = seed x volatility,
   disclosed in Methods AND Limitations; NOT the main confirmatory statistic).
7. Behavioral Reachability in the tiny-MDP — MAIN RESULT: macro-TV; aligned advantage;
   blocked stickiness; novel-goal restriction; timeout component; matching protocol.
   Pure per-seed bootstrap carries the confirmatory weight.
8. Audit and Evidential Weighting (short main-text section, not supplementary) —
   reproducibility (bit-identical re-run), seed hygiene, only-m-read verification,
   swap mechanical, null weak, correct CI interpretation.
9. Discussion — three layers: (i) direct results in designed models; (ii) relation to
   existing theory INCLUDING self-demarcation from CSC and `Psi_f`; (iii) SRT bridge
   L1→L2→L0' as operational bridge only.
10. Limitations — designed systems; m's future role is architecture-defined; mechanism
    existence + behavioral consequence only; not yet in end-to-end networks / biology /
    humans; null/swap are not independent causal evidence; FMNIST 0/5 is an
    identification NO-GO under that protocol, not a general impossibility.

## Writing order (locked)

Methods → Results → Figures+captions → Audit/Limitations → Discussion → Introduction →
Abstract → Title-final-check. Rationale: prevent narrative from outrunning results.

## Statistics policy

- No new statistics before drafting. Figures/tables read the frozen JSONs directly.
- Phase 2c seed×volatility bootstrap: disclose transparently; do not promote 2c to
  confirmatory status.
- Pre-submission only: one "statistical extraction re-check" (per-seed summary table,
  unified stats script, figure pipeline reading frozen JSON). This is packaging, not a
  new experiment.

## Evidence coordinates (research/selective-anchoring)

| Phase | Dir under Experiments/ | Commit |
|---|---|---|
| 1 double-well | anchoring_double_well | f267cfbd |
| 2 feasibility | anchoring_bandit_feasibility | c758cfe4 |
| 2b NO-GO | anchoring_bandit_holdout | b55313ae |
| 2c controllability | anchoring_2c_controllability | 28508e74 |
| tiny-MDP confirmatory | anchoring_tiny_mdp_confirmatory | 766637b9 |
| audit repair | Experiments/AUDIT.md + manifest v2 | 96d7fbbd |

Sealed originals: tag `archive/anchoring-audit-2026-07-17` (7d6fd039 / 8d703838 /
6d5f80d4 / c653b170 / 104baf9b / e19388f8).
