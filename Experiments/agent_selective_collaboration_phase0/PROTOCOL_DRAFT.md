---
id: SRT-AGENT-COLLAB-PHASE0-PROTOCOL-20261010
type: experiment_protocol
tags: [ChoiceMap, GRG, Beacon, Agent, EngineeringValidation, PreregistrationDraft]
status: draft
version: v0.1
layer: operations
epistemic_layer: os
claim_mode: engineering_hypothesis
canonical: false
research_mode: U
comparative_claim: bounded_agent_engineering_increment
named_comparator: risk_sensitive_structural_replanning
n_mode_triggered: true
date: 2026-10-10
---

# Phase 0 — selective collaboration engineering protocol (DRAFT; NOT LOCKED)

> Scope: noncanonical, downstream engineering. No test result in this directory is proof of SRT ontology, primitive Selection, GRG scientific distinctiveness, M4/M5 credit, or human-facing ChoiceMap benefit. Does not replace STATUS.md CURRENT NEXT. No experiment has yet been executed under this protocol.

## 0. Evidence lineage and separation

- Existing completed synthetic ChoiceMap study: papers/choicemap_explicit_scaffolding/{00_scope_and_prior_failures,05_confirmatory_results,06_final_decision}.md. It supports a **limited** engineering bridge for explicit commitment/reversibility metadata under hidden irreversible conditions. It does **not** validate human-facing ChoiceMap or GRG.
- ChoiceMap user-facing direction: Product/ChoiceMap/CHOICEMAP_RESELECTABILITY_PRODUCT_EXPLANATION_2026-07-01.md.
- GRG owner: Operations/Proposals/SRT_GRG_FOUNDATIONAL_PROTO_GRAMMAR_V0_3_2026-09-21.md; evidence record schema: Operations/Templates/SRT_GRG_GENERATIVE_TRANSFORMATION_RECORD_TEMPLATE_V0_2.md.
- Recorded negative comparator: Operations/Audits/SRT_GRG_M4_01_AI_AGENT_POLICY_ENFORCEMENT_RESULT_2026-09-21.md (ABSORBED / M4 NO). Authorization is a common baseline, not a GRG gain.
- Stage 0 proof-of-implementation checks (tests in this directory) are NOT task-level efficacy evidence.

## 1. Research target: three independently falsifiable increments

H1 ChoiceMap: C vs B1. C improves unforeseen future-task success / reachable future set in irreversible and task-reframing worlds while current-task success is noninferior within a **-3 percentage-point** margin; minimum practically useful mean increase +5 percentage points.

H2 GRG-lite: D vs C, plus D vs a preregistered B1+ strong structure-learning/risk-sensitive comparator. The GTS-driven candidate mechanism improves held-out post-frame-change task success by +5 percentage points and passes a paired cluster-level interval lower bound > 0. Mere better prompt wording, extra probes, extra computation, or a more conservative policy cannot count as demonstrated independent gain.

H3 Beacon: E vs D-memory-matched. After an interruption, recovery latency/turns drops at least 20% while state restoration correctness and authorization reliability are noninferior. Memory-matched means same retrieved evidence, context/token budget and allowed tools, with a competitive standard event-sourced semantic retriever.

H4 participation is separate human-facing research. No user-effectiveness claim until counterbalanced real participants, task-success measures, blinded review and usability-cost assessment.

These are proposed acceptance criteria only; they require power estimation, reviewer challenge and protocol locking prior to confirmation. NO actual efficacy claim follows from specifying thresholds.

## 2. Arms and parity

- B0: common tool Agent + common deterministic authorization gate (reference only).
- B1: competent risk-sensitive planner with dynamic task tree, event sourced memory, change-point detection, structural hypothesis updates, option value, rollback, and matched tools.
- B1+: B1 with independently tuned model-based structural learning / belief updating and constrained safe route; tuned on development, NOT confirmatory sets.
- C: B1 + explicit ChoiceMap options/premises/branch restoration and delayed commitment, independently ablatable.
- D: C + GRG-lite bounded GTS entries with ex-ante generative condition, prediction, failure predicate, outcome provenance and revision.
- D-noGTS: D with GTS mechanism disabled but identical computation budget; separate model ablation.
- E: D + Beacon evidence-index recovery layer.
- E-memory: D + standard semantic/event retriever with matched recovery budget.

All arms share the same model weights/version, environment access, candidate generation opportunities, safety/tool gate, data, random seeds, and nominal decision budget. Measure *active* search/tool/token costs and wall clock, rather than relying solely on padding. Pad idle budget only where it cannot alter the world. Strong baselines may not be intentionally impoverished.

## 3. Synthetic environment families

F1 stable/reversible — negative control: ChoiceMap/GRG overhead should not improve a task that does not need them.
F2 hidden irreversible — decisions prune future tasks; future set evaluated by OFFLINE oracle only.
F3 concealed regime switch — task transition model changes without advance notice; non-GRG structural learner should still be competitive.
F4 reconstructed reachability — a policy/resource/compatibility condition changes which tasks or units are available. Multiple mechanisms, not GRG-coded labels, generate worlds.
F5 noisy false alarm — cues suggest a framing change but underlying structure is stable; penalize gratuitous reframes.
F6 human scope/authority change — user updates priority or authorization; protected external effects cannot occur absent user approval.

Generator MUST output: private truth, public AgentView, observations, legal tool actions, future-task catalog, and offline evaluation oracle. Verify hidden regime/future task and evaluator outputs never occur in AgentView/prompts/memory. Match realistic but synthetic cases across business planning, coding workflows and service operations; leave-one-template-family-out tests challenge schema leakage.

## 4. Required observable contracts

A proposed change to task frame is not a committed change. Agent may propose, user may reject, compose, rename axes or accept. A GTS candidate is a **hypothesis**, not source-native causal proof; distinguish predicted outcomes from tool-verified effects. Previous task frame and rejected branches remain addressable. Beacon recovery is an index into original events and does not grant or infer permission.

State/event records need at least: task id, frame version, root goal, actor and evidence source, branch id/parent, premise revision, reversibility, authorization scope, observation id, GTS condition/prediction/failure, provenance and timestamps. A tool-layer authorization check operates independently of model response.

GRG-lite is process/transform-first: freeze a bounded generative condition and prospective prediction before seeing evaluation outcomes. A larger horizontal / structure-learning model may represent the same dynamic; no inherent representational exclusivity is asserted.

## 5. Primary metrics and failure modes

- FTR (primary): percent previously-unseen future tasks completed after change, with resources/time constraints, scored by offline oracle.
- CSR: current-task success. Require lower confidence bound for C−B1 and D−C above -0.03 for noninferiority.
- RFS-AUC: size of genuinely reachable future task set over time, offline only.
- Correct-frame recovery: agreement of restored goal, premises, branch state, provenance and authorization with user-confirmed ground truth.
- Reframe precision/recall: post hoc blinded classification of evidence-supported reframing, including false positive F5.
- GTS prospective discrimination: pre-outcome prediction accuracy and failure revision rates, without contamination by self-generated intervention outcomes.
- Costs: inference tokens, calls, search expansions, latency, user turns, confirmation count and cognitive burden.
- Zero tolerated unauthorized environment mutations. A breach is a safety STOP, not a favorable comparison endpoint.

Do not report generic “GRG win” from H1 or memory gain from H2. Negative controls and anomalous cells remain in the primary report.

## 6. Proposed statistical plan

Exploratory pilot: start 10 random seeds × F1–F6 × 20 paired episodes × all relevant arms; purpose is code/integrity checks, comparison fairness, variance and power. Do not use pilot as confirmatory evidence. Before independent confirmation, publish an immutable manifest of generator, code, arm knobs, baselines, task template split, selection of primary endpoint, test direction, cluster unit, stopping conditions, and random seed procedure.

Confirmatory sample size set from pilot variance via preregistered power analysis, with a provisional planning grid of at least 40 independent seeds × 6 families × 100 episodes where feasible. Paired seed/family clusters (not repeated episodes treated as independent subjects) are the inference units. Use paired cluster bootstrap CIs, family-stratified effect estimates, and multiplicity-adjusted primary tests. Include null or harmful effects, 95% interval, run-level cost, exact exclusion counts, ablation and boundary cases.

H2 extra demand: a preregistered risk-sensitive/structure-learning B1+ that can adapt candidate spaces and choose the safe route. If B1+ matches D's joint current/future frontier at equivalent cost, classify independent GRG effect NO or unresolved; do not rescue by moving the goalposts.

## 7. Human interface phase (separate from synthetic validation)

Start with 12–20 participants only as qualitative/exploratory usability work: crossover or counterbalanced tasks with interrupted multi-stage work, changed premises and explicit irreversible decisions. Neither user satisfaction nor self-rated model performance alone establishes efficacy. Human confirmation remains required where consent or real business effects are concerned. Human-facing ChoiceMap's author convergence rule cannot be inferred from autonomous-agent efficacy.

## 8. Stage gates

- P0 protocol review: claim typing; independent strongest-rival design; leak and fair-budget audit; runbook reproducibility.
- P1 implementation smoke: event-chain fidelity, no model authority escalation, offline oracle separation and negative-case tests; no success claim.
- P2 pilot: variance, cost and sample power, baseline adequacy, reproducibility.
- P3 locked confirmatory: GO / HOLD / NARROW / STOP per frozen criteria, including a right for the strongest rival to absorb any claimed novelty.
- P4 human/transfer: product usefulness and scope checks.

**Current status: P0 DRAFT / P1 smoke scaffolding only.** No source-native scientific gain, cross-domain M4/M5 credit or product utility result is claimed.

## External comparison (bounded)

- Factual conflict: none established from existing result descriptions; this protocol itself contains hypotheses only.
- Internal contradiction: none in the stated source distinction; an implementation that auto-commits an unapproved consequential choice would violate ChoiceMap product boundary.
- Existing neighbors: risk-sensitive model predictive control, contingent planning, structure learning, event-sourced workflow engines, human-in-the-loop approvals, memory retrieval — partially overlapping; compare full functions rather than labels.
