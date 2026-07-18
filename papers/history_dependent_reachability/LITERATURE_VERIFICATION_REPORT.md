# Literature verification report — round 1 (N3, N4)

> **CURRENT STATUS (2026-07-19).** All **three** verification rounds are complete
> (Round 1 = N3/N4 below; Round 2 = five-layer overlap map + perceptual-aliasing
> neighbor; Round 3 = measure/perseveration/methodology/self-cite). The proposed
> downgrade wording and the VERIFIED citations **have since been applied to the
> manuscript** in commit `33e97207` (Methods 2.4, Intro §1, Discussion §5.2, Results
> §3.4; `manuscript/08_references.md`). Any statement below that a change is "NOT
> applied to the manuscript this round" or that "PR #675 remains Draft" is the
> **historical record of Round 1 only** and is superseded by that commit. The live
> paper PR is now #682 (Draft); PR #675 is merged and closed.

Date: 2026-07-17. Method: web verification of primary sources (DOI + venue + read of
methods/formulas for the closest N3/N4 works). **No citation inserted into
MANUSCRIPT this round; PR #675 remains Draft.** DOIs below were confirmed against
publisher/index pages this session; all *other* candidate references remain
`NEEDS-CONFIRM` and no DOI is guessed.

## 0. Stop-rule determination

The instruction was to STOP and report if a **complete precedent** for the whole
claim is found. **No complete precedent was found.** What was found is that the information *quantity* belongs to an **established family**
(empowerment / information-control), and a **partial precedent for the MECHANISM** (see §1).
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
  over the action distribution (capacity); our C_μ = I_μ(A;O|s) is a **non-capacitated
  action–outcome mutual information under a fixed reference distribution** μ — the same
  established empowerment / information-control family, but **not** an "instance of
  empowerment" (empowerment is the capacity) and not a claimed exact-measure precedent.
  We claim only that **we do not assert the information quantity itself is new.**
- **Transfer entropy** — Schreiber (2000), *Phys. Rev. Lett.* 85(2):461–464, DOI
  10.1103/PhysRevLett.85.461. VERIFIED. Formula read: T_{X→Y} conditions transition
  probabilities to exclude information due to common history and shared inputs.
  **Overlap layer: MEASURE (neighboring, observational).** Positioned as a
  *neighboring observational directed-information measure*, **not** as the
  information-theoretic equivalent of the yoked control. The closer theoretical
  neighbor to the yoked *manipulation* is **intervention-based causal information flow**
  (Ay & Polani) — an interventional, not observational, quantity (to be verified in
  Round 2). Difference: transfer entropy is an observational *measure*, not a
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
| MEASURE (action→outcome information) | **established family** | empowerment (capacity); transfer entropy (neighboring, observational); variational empowerment |
| MECHANISM (use as a *gate*) | partial | empowerment used as a signal — but for action/exploration, not memory consolidation |
| MECHANISM (gate a *path memory*, not action) | **not found** | — |
| CONTROL (yoked + sham selection-specificity) | **not found (in this family)** | — |
| ENDPOINT (directional behavioral reachability, matched present) | **not found** | — |

**Effect on novelty: N3 residual novelty = consolidation-gating role + yoked/sham
selection-specificity identification + directional reachability endpoint. The
information quantity must be presented as belonging to the established action→outcome
information family (with citations), and the paper must not claim the quantity itself
is new.**

## 2. N4 — matched-present / path-dependent reachability

**Verified precedent (adjacency/reachability construct):**
- **Successor representation** — Dayan (1993), *Neural Computation* 5(4):613–624, DOI
  10.1162/neco.1993.5.4.613. VERIFIED. Read: represents a state by the discounted
  expected future occupancy of successor states — a learned **future-reachability /
  adjacency** structure. **Overlap layer: ENDPOINT vocabulary** (reachability as future
  state adjacency). Difference: the SR is a value-generalization representation; our
  endpoint is a *behavioral arrival distribution* under a matched-present identification
  protocol. No gating/identification content.

**No close protocol-level precedent identified in Round 1** for a "match the
observable present exactly, vary only a slow history-carrying memory, measure whether
the future behavioral distribution changes" **identification protocol**. (This is a
Round-1 search result, not a proof of non-existence; POMDP state aliasing, hidden slow
state, memory-based RL, and matched-endpoint path dependence are Round-2 targets.)
Successor representation is a **policy-conditioned future-occupancy / background**
construct, not a reachable-set *protocol* precedent.

**Effect on novelty: N4 (the matched-present only-m identification protocol) survives
Round 1; risk MEDIUM, pending Round-2 searches. Frame reachability with the SR lineage
as policy-conditioned future-occupancy background — not as a protocol precedent; keep
the identification-vs-path-dependence distinction explicit (already in §1, §2.8).**

## 3. Proposed downgrade wording for N3 (NOT applied this round)

To be applied in a later, author-approved editing turn (Methods 2.4 and Discussion
5.2), after the remaining candidate refs are confirmed:

- Methods 2.4, after defining r_t: add "This action-attributable predictive-information
  quantity belongs to the established action→outcome information family (empowerment
  [Klyubin et al. 2005], the action–outcome channel *capacity*; transfer entropy
  [Schreiber 2000], a neighboring observational directed-information measure; its
  variational reinforcement-learning use [Mohamed & Rezende 2015]). Our C_μ =
  I_μ(A;O|s) is a non-capacitated conditional mutual information under a fixed
  reference distribution; we do not claim the information quantity itself is new. Our
  contribution is its use as a *consolidation gate* for a path memory — it does not
  drive action selection — and the yoked/sham test of selection-specificity."
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

---

# Round 2 (N3 breadth, N4/N5 systematic) — 2026-07-17

Verified this round (DOI/venue confirmed; formula/concept read for the closest):

- **Ay & Polani (2008)**, *Adv. Complex Syst.* 11(1):17–41, DOI
  10.1142/S0219525908001465. Read: **interventional** information flow — conditional
  mutual information under the do-operator, explicitly contrasted with (observational)
  transfer entropy. **Layers: MEASURE (interventional) + CONTROL-rationale.** This is
  the closer information-theoretic neighbor to the yoked *manipulation* (an
  intervention cutting the action→outcome edge). Still a measure, not a memory-gating
  mechanism or an identification protocol.
- **Variational Intrinsic Control** — Gregor, Rezende, Wierstra (2016), arXiv:1611.07507.
  Read: maximizes I(options; termination states) = "number of states an agent can
  reliably reach." **Layers: MEASURE + MECHANISM-as-signal + partial ENDPOINT
  (reachability-of-states).** Closest single work on combining action→outcome
  information with reachability — but it drives **option/skill learning** (action), not
  a gated path memory, and has no matched-present identification or yoked/sham control.
- **Perceptual aliasing** — Whitehead & Ballard (1991), *Machine Learning* 7:45–83,
  DOI 10.1007/BF00058926. Read (concept): situations "indistinguishable from immediate
  perceptual input require different responses." **Layer: MATCHING (conceptual
  neighbor).** This is the closest neighbor to N4's intuition (same observation,
  different underlying/hidden state → different appropriate future). **Crucial
  distinction:** perceptual aliasing is the *agent's* inference/memory problem (it must
  disambiguate aliased states to act optimally); ours is an *experimenter's*
  identification protocol (match the observable present + fast state + action
  distribution, vary only the slow history-formed memory, with yoked/sham controls and
  a reachability-distribution endpoint). Not a protocol precedent, but N4 must now cite
  and demarcate it. (Companion: Chrisman 1992, AAAI-92, perceptual distinctions —
  candidate, DOI n/a.)
- **Sense of agency** — Haggard (2017), *Nat. Rev. Neurosci.* 18(4):196–207, DOI
  10.1038/nrn.2017.14 (review). Read: self-attribution of control over action and its
  effects. **Layer: CONTROL/self-attribution (background for the sham).**

Candidates identified but NOT individually web-verified this round (DOI NEEDS-CONFIRM;
no DOI guessed): Massey (1990) directed information; Lizier & Prokopenko (local
information transfer); Seitzer et al. (2021) causal-influence detection intrinsic
reward (NeurIPS); Daw et al. (2005) / Dickinson (1985) habit vs goal-directed
(perseveration, N5); learned-helplessness yoked (Seligman & Maier 1967, R-09);
equivalence testing (R-11), bootstrap (R-12), committor/TPT (R-06), Euler–Maruyama
(R-07).

## Five-layer overlap map (measure / mechanism / control / matching / endpoint)

| reference | measure | mechanism | control | matching | endpoint |
|---|---|---|---|---|---|
| Empowerment (Klyubin 2005) | ✔ capacity | — | — | — | — |
| Transfer entropy (Schreiber 2000) | ✔ observational directed | — | rationale only | — | — |
| Ay & Polani (2008) | ✔ interventional | — | ✔ rationale (intervention≈yoke) | — | — |
| Mohamed & Rezende (2015) | ✔ | ✔ as signal (drives action) | — | — | — |
| VIC (Gregor 2016) | ✔ | ✔ as signal (drives options) | — | — | partial (reach states) |
| Perceptual aliasing (Whitehead 1991) | — | — | — | ✔ conceptual (agent inference) | — |
| Sense of agency (Haggard 2017) | — | — | ✔ self-attribution (background) | — | — |
| Successor representation (Dayan 1993) | — | — | — | — | ✔ future occupancy (background) |
| **This paper** | family (not novel) | **gate a path memory (not action)** | **yoked + sham selection-specificity** | **matched present, only slow memory varied** | **directional reachability distribution** |

**No single prior work occupies the mechanism+control+matching+endpoint combination.**
Each layer has a neighbor; the **identification protocol assembling all four** has no
precedent found in Rounds 1–2. STOP rule: **not triggered.**

## Effect on the novelty audit

- **N3:** unchanged from Round 1 — measure not claimed novel; interventional (Ay–Polani)
  and mechanism-as-signal (VIC, Mohamed–Rezende) neighbors now documented; residual
  novelty = gating-a-path-memory + yoked/sham + endpoint (the *combination*).
- **N4:** **risk raised MEDIUM → MEDIUM-HIGH.** Perceptual aliasing is a genuine
  conceptual neighbor and MUST be cited + demarcated (agent-inference vs
  experimenter-identification). N4 novelty survives as the *protocol*, not the intuition.
- **N5 (perseveration):** habit/goal-directed and set-shifting literature confirmed as
  the background home for the stickiness cost; N5 stays LOW–MEDIUM, framed as a
  within-model directional prediction consistent with known perseveration.

## Deliverables this round
Updated REFERENCE_LEDGER (Round-2 rows VERIFIED), NOVELTY_AUDIT (N4 demarcation
strengthened, five-layer map), candidate_bibliography.bib (4 new VERIFIED entries).
MANUSCRIPT unchanged; PR #675 Draft.

---

# Round 3 (bounded: measure breadth, perseveration, methodology, self-cite status) — 2026-07-17

Scope-limited per instruction; citation set deliberately kept small. All "no precedent"
statements are phrased **"no close protocol-level precedent was identified in our
search"** (search result, not exclusionary proof).

## Group 1 — measure breadth + the "info-as-memory-write-gate" STOP check

- **Causal Action Influence (CAI)** — Seitzer, Schölkopf, Martius (2021), *NeurIPS 2021*,
  arXiv:2106.03443. VERIFIED. Read: a situation-dependent **per-state conditional mutual
  information** of the agent's action on the next state, I(A;S′|s), used as an intrinsic
  signal to improve exploration/off-policy learning. **This is the closest measure
  neighbor to C_μ** (both are per-state action→outcome conditional MI). **Layers:
  MEASURE + MECHANISM-as-signal.** Difference: CAI modulates **exploration/action**;
  ours gates **memory consolidation** and does not drive action; CAI uses the transition
  dynamics, ours a fixed reference μ. Consequence: the measure **and** the
  "use-as-a-learning-signal" mechanism are both precedented → N3 residual novelty is
  further tightened (see below).
- **Directed information** — Massey (1990), *Proc. ISITA-90*, pp. 303–305 (no DOI);
  precursor Marko (1973, directed transinformation). VERIFIED (venue). Read: directed
  information = the feedback-aware action→outcome information; upper bound on feedback
  capacity. **Layer: MEASURE (background completeness).**
- **Recall-gated plasticity** — Lindsey & Litwin-Kumar (2024), *eLife* 12:RP90793, DOI
  10.7554/eLife.90793. VERIFIED. Read: synaptic updates are consolidated into long-term
  memory **gated** by consistency with existing (recalled) memory. **Layer: MECHANISM
  (gated consolidation).** Establishes that *gated long-term consolidation* is not novel;
  the **gate signal differs** (recall-consistency vs action-attributable controllability).
- **Controllability→consolidation (neuroscience, background):** evidence that behavioral
  controllability modulates what is consolidated (escapable vs inescapable outcomes;
  learned-helplessness lineage — see Group 3, Seligman & Maier). This is exactly the kind
  of natural-system phenomenon our framework provides an *identification test* for; it is
  **supportive context, not a defeater** (our claims are designed-model only). Cite as
  motivation, not as precedent for the framework.
- **Candidate (NEEDS-CONFIRM):** Lizier & Prokopenko (local/pointwise transfer entropy).

## Group 2 — perseveration / habit (N5 framing)

- **Daw, Niv, Dayan (2005)**, *Nat. Neurosci.* 8(12):1704–1711, DOI 10.1038/nn1560.
  VERIFIED. Read: uncertainty-based arbitration between model-free (habitual, inflexible)
  and model-based (goal-directed, flexible) control. **Layer: ENDPOINT/background.**
  Grounds the "stickiness / perseverative cost" as a known behavioral phenomenon (habit
  inflexibility). **Effect on N5:** the aligned-advantage-plus-change-cost pattern is a
  **within-model joint directional prediction consistent with known perseveration**, not
  a new behavioral discovery. N5 stays LOW–MEDIUM.
- **Candidates (NEEDS-CONFIRM):** Dickinson (1985) actions vs habits; set-shifting /
  cognitive-flexibility (WCST perseveration).

## Group 3 — methodology primary sources

- **Equivalence testing (TOST):** Lakens (2017), *Soc. Psychol. Personal. Sci.*
  8(4):355–362, DOI 10.1177/1948550617697177 (accessible primer). VERIFIED. Original:
  Schuirmann (1987), *J. Pharmacokinet. Biopharm.* (candidate DOI NEEDS-CONFIRM). Supports
  the pre-registered ±ε equivalence bounds.
- **Committor / transition-path theory:** E & Vanden-Eijnden (2010), *Annu. Rev. Phys.
  Chem.* 61:391–420. VERIFIED (venue); DOI NEEDS-CONFIRM. Supports the committor W_sel
  functional.
- **Canonical primaries (well-known; DOIs NEEDS-CONFIRM, not fetched this round; no DOI
  guessed):** master-yoked / learned helplessness — Seligman & Maier (1967), *J. Exp.
  Psychol.*; bootstrap — Efron (1979), *Ann. Statist.* 7(1):1–26; Kramers escape rate —
  Kramers (1940), *Physica* 7:284; Euler–Maruyama — Kloeden & Platen (1992), *Numerical
  Solution of Stochastic Differential Equations* (Springer).

## Group 4 — self-citation status (repo records; live status = author to confirm)

Verified against **repository records** only (external submission portals not accessible):

- **Ontological friction (Ψ_f):** Frontiers **manuscript ID 1837760**, in a **revision
  round** (repo contains `frontiers_response_to_reviewers.md` and a revision-round
  submission checklist). Honest status: **"in revision at Frontiers (ms 1837760)."** Do
  not write "in press" or "published." Author to confirm current live decision.
- **Costly Selective Closure (CSC):** repo shows **v16** following an **ALIFE-2026
  rejection**, targeting **Adaptive Behavior** (per project records/memory). No confirmed
  Adaptive Behavior submission record in the repo. Honest status: **"revised (v16) after
  ALIFE-2026 rejection; targeting Adaptive Behavior; submission status to be confirmed."**
  Do not upgrade to "submitted/under review at Adaptive Behavior" without author
  confirmation.

## Updated N3 residual (after Round 3)

The information **quantity** (CAI, empowerment, transfer entropy, directed information,
Ay–Polani) and its **use as a learning signal** (CAI, VIC, Mohamed–Rezende) are both
established; **gated long-term consolidation** is established (recall-gated plasticity);
**controllability-modulated consolidation** is a known neuroscience idea. **Residual N3
novelty is therefore only the specific combination:** an action-attributable-information
score used as a *path-memory consolidation gate*, isolated by *yoked + sham
selection-specificity*, with a *matched-present directional-reachability* endpoint, as a
**designed-model identification framework**. The measure and the generic
mechanism-as-signal carry **zero** novelty weight.

## STOP determination (Round 3)
**No close protocol-level precedent was identified in our search** for the full
identification protocol (matched present + only-slow-memory + yoked/sham + reachability
distribution with a controllability memory-gate). STOP **not** triggered.

## Deliverables (Round 3)
Updated REFERENCE_LEDGER (Round-3 VERIFIED rows + self-cite status), NOVELTY_AUDIT (N3
residual tightened; N5 grounded), candidate_bibliography.bib (verified additions).
MANUSCRIPT unchanged; PR #675 Draft. Citation set kept bounded (not a review).
