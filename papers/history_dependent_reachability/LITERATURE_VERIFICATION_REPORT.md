# Literature verification report — round 1 (N3, N4)

Date: 2026-07-17. Method: web verification of primary sources (DOI + venue + read of
methods/formulas for the closest N3/N4 works). **No citation inserted into
MANUSCRIPT this round; PR #675 remains Draft.** DOIs below were confirmed against
publisher/index pages this session; all *other* candidate references remain
`NEEDS-CONFIRM` and no DOI is guessed.

## 0. Stop-rule determination

The instruction was to STOP and report if a **complete precedent** for the whole
claim is found. **No complete precedent was found.** What was found is a **complete
precedent for the MEASURE** and a **partial precedent for the MECHANISM** (see §1).
Because the residual claim (consolidation-gating + yoked/sham selection-specificity +
directional reachability under a matched present) is not precedented as a whole, the
paper's contribution survives — **but N3 must be downgraded** to cite the measure
family explicitly and to scope novelty away from the measure. Proposed wording is in
§3; it is NOT applied to the manuscript this round.

## 1. N3 — action-attributable controllability score (HIGHEST RISK)

**Our quantity.** r_t = log q(o_t|s_t,a_t) − log Σ_{a'} μ(a')q(o_t|s_t,a'), a pointwise
log-likelihood ratio of the chosen action against a fixed reference-action mixture;
its structural summary C_μ(s) = Σ_a μ(a) KL(q(·|s,a) ‖ q̄_μ) is a **reference-measure
conditional mutual information** I_μ(A;O|s). We already state we do not call it the
conditional MI of the acting policy.

**Verified precedents (measure family):**

- **Empowerment** — Klyubin, Polani, Nehaniv (2005), *Proc. IEEE CEC 2005*, pp.
  128–135, DOI 10.1109/CEC.2005.1554676. VERIFIED. Formula read: empowerment is the
  **channel capacity** C = max_{p(a)} I(A^n; S′) between action sequences and the
  future sensor state. **Overlap layer: MEASURE.** Difference: empowerment *maximizes*
  over the action distribution (capacity); our score uses a *fixed* reference μ and is
  evaluated pointwise per step. Our C_μ is a fixed-reference instance of the same
  action→outcome information object → **the measure is not novel.**
- **Transfer entropy** — Schreiber (2000), *Phys. Rev. Lett.* 85(2):461–464, DOI
  10.1103/PhysRevLett.85.461. VERIFIED. Formula read: T_{X→Y} conditions transition
  probabilities to **exclude information due to common history and shared inputs**.
  **Overlap layer: MEASURE + partial CONTROL rationale** — Schreiber's motivation
  (remove shared-history information to isolate genuine directed transfer) is the
  information-theoretic analogue of what our master-yoked control does behaviorally
  (cut the action→outcome edge). Difference: transfer entropy is a *measure*, not a
  memory-gating mechanism.
- **Variational empowerment for RL** — Mohamed & Rezende (2015), *Advances in NeurIPS
  28* (proceedings.neurips.cc/paper/2015/hash/e00406144c1e7e35240afed70f34166a).
  VERIFIED (venue; NeurIPS has no DOI). Read: optimizes I(a; s′) (empowerment) as an
  **intrinsic objective** via a variational lower bound. **Overlap layer: MEASURE +
  partial MECHANISM** — action→outcome information is used as a *learning signal*.
  Difference (mechanism level): there it drives **action selection / exploration /
  skill discovery**; here z gates **memory consolidation** and explicitly does **not**
  drive the current action.

**Candidate (not web-verified this round — NEEDS-CONFIRM, no DOI guessed):**
directed information (Massey 1990; Marko 1973); causal information flow (Ay & Polani
2008, *Chaos/Adv. Complex Syst.*); Variational Intrinsic Control (Gregor, Rezende,
Wierstra 2016); "causal influence" intrinsic rewards in RL. All expected to sit at the
MEASURE (and, for VIC, partial-MECHANISM) layer.

**N3 overlap summary by layer:**
| layer | precedented? | by |
|---|---|---|
| MEASURE (action→outcome information) | **YES, fully** | empowerment; transfer entropy; variational empowerment |
| MECHANISM (use as a *gate*) | partial | empowerment used as a signal — but for action/exploration, not memory consolidation |
| MECHANISM (gate a *path memory*, not action) | **not found** | — |
| CONTROL (yoked + sham selection-specificity) | **not found (in this family)** | — |
| ENDPOINT (directional behavioral reachability, matched present) | **not found** | — |

**Effect on novelty: N3 residual novelty = consolidation-gating role + yoked/sham
selection-specificity identification + directional reachability endpoint. The measure
itself must be presented as an instance of established action→outcome information, with
citations.**

## 2. N4 — matched-present / path-dependent reachability

**Verified precedent (adjacency/reachability construct):**
- **Successor representation** — Dayan (1993), *Neural Computation* 5(4):613–624, DOI
  10.1162/neco.1993.5.4.613. VERIFIED. Read: represents a state by the discounted
  expected future occupancy of successor states — a learned **future-reachability /
  adjacency** structure. **Overlap layer: ENDPOINT vocabulary** (reachability as future
  state adjacency). Difference: the SR is a value-generalization representation; our
  endpoint is a *behavioral arrival distribution* under a matched-present identification
  protocol. No gating/identification content.

**Not found (searched):** a prior "match the observable present exactly, vary only a
slow history-carrying memory, measure whether the future behavioral distribution
changes" **identification protocol**. Path dependence (dynamical/economic) and
hidden-state/POMDP identifiability are background neighbors, not this protocol.

**Effect on novelty: N4 (the matched-present only-m identification protocol) survives;
risk MEDIUM. Frame reachability with the SR lineage as background; keep the
identification-vs-path-dependence distinction explicit (already in §1, §2.8).**

## 3. Proposed downgrade wording for N3 (NOT applied this round)

To be applied in a later, author-approved editing turn (Methods 2.4 and Discussion
5.2), after the remaining candidate refs are confirmed:

- Methods 2.4, after defining r_t: add "This action-attributable predictive-information
  quantity is an instance of the action→outcome information family (empowerment
  [Klyubin et al. 2005]; transfer entropy [Schreiber 2000]; its variational,
  reinforcement-learning use [Mohamed & Rezende 2015]); our C_μ is a fixed-reference
  conditional mutual information, not a novel measure. Our contribution is its use as a
  *consolidation gate* for a path memory — it does not drive action selection — and the
  yoked/sham test of selection-specificity."
- Discussion 5.2, replace the bare "to our knowledge no framework packages …" with the
  same, keeping "to our knowledge" only for the *packaging* (battery + endpoint), not
  for the measure.

## 4. Outputs of this round

- `REFERENCE_LEDGER.md` updated: 4 rows VERIFIED with full metadata; measure-family
  rows added; candidate rows kept NEEDS-CONFIRM.
- `NOVELTY_AUDIT.md` updated: N3 measure = precedented; residual novelty restated.
- `candidate_bibliography.bib`: verified entries + clearly separated unverified
  candidates.
- MANUSCRIPT unchanged.
