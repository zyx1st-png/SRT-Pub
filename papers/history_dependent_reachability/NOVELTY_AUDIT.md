# NOVELTY AUDIT — History-Dependent Reachability

Claim-by-claim novelty review. For each load-bearing claim: what is asserted as
novel, what prior art plausibly overlaps (by topic; references to be VERIFIED in
`REFERENCE_LEDGER.md`), the residual novelty after accounting for that art, and the
risk if a reviewer supplies a specific counter-reference. **This audit does not add
citations; it identifies where the novelty claim must be defended and to what
strength.**

Overall framing (fixed by PAPER_CHARTER): the paper's novelty is an **identification
framework** demonstrated constructively in designed models — not a discovery about
natural systems, not a new learning rule per se, not a metaphysical result. Novelty
claims must be scoped to "assembling this identification test + control battery +
the retained negative result," and every exclusivity phrasing keeps "to our
knowledge."

## N1 — Construct dissociation P / W_global / W_sel (claim A1)

- **Asserted novel:** treating persistence, general rule change, and
  *selection-specific* write-back as three separately measurable constructs, with a
  counterfactual (h+ vs h−) W_sel instrument, and showing all four P×W_sel cells are
  reachable regions.
- **Overlap (verify):** hysteresis/metastability (R-01), plasticity vs. performance
  distinctions in learning. These establish that persistence and plasticity are old;
  they do **not** provide the selection-specific counterfactual functional.
- **Residual novelty:** the W_sel = Φ_M(h+) − Φ_M(h−) counterfactual construct and
  the explicit four-cell dissociation with a nonspecific-write negative control.
- **Risk / defense:** LOW–MEDIUM. Defense = the specific counterfactual instrument
  and the negative control (RoughenWrite) are not standard; keep the claim at
  "dissociable constructs + measurement instrument," not "new phenomenon."

## N2 — |PE| accumulation is history-dependent but NOT selection-specific (A2)

- **Asserted novel:** a pre-registered, frozen-holdout demonstration that a
  prediction-error metaplasticity signal fails a yoked selection-specificity test.
- **Overlap (verify):** volatility→learning-rate meta-learning (R-03); yoked-control
  methodology (R-09). Prior art shows |PE|-like signals drive adaptation; it does not
  typically subject them to a yoked selection-specificity test with this endpoint.
- **Residual novelty:** the *negative* result under a locked protocol, retained and
  used as the pivot — a methodological/curatorial novelty more than a discovery.
- **Risk / defense:** LOW. This is a self-limiting claim ("this mechanism is NOT
  selection-specific"); hard to be scooped by a positive result. Keep it framed as a
  falsification within the framework.

## N3 — Action-attributable information gates selection-specific write-back (A3)

- **Asserted novel:** using r_t = log q(o|s,a) − log Σ μ(a′)q(o|s,a′) (μ-reference
  pointwise LLR) as the write-gating signal, with data-driven active≫yoked and a
  |PE| equivalence baseline.
- **Overlap (verify, HIGHEST):** empowerment, transfer entropy / directed
  information, interventional/causal information, controllability/agency signals,
  intrinsic-control objectives (R-08, R-10). The *quantity* is related to established
  action→outcome information measures; we explicitly say we do NOT call it the
  acting-policy conditional MI.
- **Residual novelty:** not the information measure itself, but (a) its use as a
  *consolidation gate* for a path memory, and (b) the yoked+sham demonstration that
  the gate is selection-specific where |PE| is not.
- **Risk / defense:** MEDIUM–HIGH. **RESOLVED BY VERIFICATION (2026-07-17):** the
  measure is **NOT novel.** Empowerment (Klyubin et al. 2005, DOI
  10.1109/CEC.2005.1554676) is the action→outcome channel capacity; transfer entropy
  (Schreiber 2000, DOI 10.1103/PhysRevLett.85.461) is the directed-information version
  that conditions out shared history; variational empowerment (Mohamed & Rezende 2015)
  uses I(a;s′) as an RL signal. Our C_μ = I_μ(A;O|s) is a **non-capacitated action–outcome mutual information under a
  fixed reference distribution** — the same established family, but NOT an "instance of
  empowerment" (which is the capacity) and NOT a claimed exact-measure precedent. No complete precedent exists (none gates a *path memory* rather than action,
  none runs a yoked/sham selection-specificity test, none reads out directional
  behavioral reachability under a matched present).
- **Round 3 further tightening:** the "use as a *learning signal*" is ALSO precedented —
  Causal Action Influence (Seitzer et al. 2021, arXiv:2106.03443) is essentially the same
  per-state action→outcome conditional MI used as an intrinsic signal (for exploration);
  and **gated long-term consolidation** is precedented (recall-gated plasticity, Lindsey &
  Litwin-Kumar 2024, DOI 10.7554/eLife.90793), as is the neuroscience idea that
  controllability modulates consolidation. So the measure AND the generic mechanism-as-
  signal AND gated-consolidation each carry **zero** novelty weight.
- **Residual novelty (restated, narrowest):** **only the specific combination** — an
  action-attributable-information score used as a *path-memory consolidation gate* (not an
  exploration/action signal), isolated by *yoked + sham selection-specificity*, with a
  *matched-present directional-reachability* endpoint, as a **designed-model identification
  framework**. No close protocol-level precedent was identified in our search.
- **Required action (mandatory before any strengthening):** cite empowerment +
  transfer entropy + variational empowerment at the definition of r_t; state
  explicitly "not a novel measure"; keep "to our knowledge" only for the *packaging*
  (battery + endpoint), never for the measure. **APPLIED — citation-insertion round
  (2026-07):** Methods 2.4 now carries the "the measure is not novel" paragraph with
  Klyubin/Seitzer/Massey/Schreiber/Ay-Polani + Mohamed-Rezende/Gregor (signal use) +
  Lindsey-Litwin-Kumar (gated consolidation); Intro §1 and Discussion §5.2 list the
  same ingredients before the unified exclusivity sentence.

## N4 — Matched-present → different future reachability carried by memory alone (A4)

- **Asserted novel:** matching current state, fast values, and initial action
  distribution, carrying *only* the slow memory, and measuring a behavioral
  reachability change.
- **Overlap (verify):** path dependence generally; reachable-set/successor
  representations (R-13); metaplasticity carryover. Path dependence is old; the
  **identification move** (match everything observable, vary only the slow carrier,
  code-verify only-m carry) is the novel part.
- **Residual novelty:** the exact matched-present identification protocol with the
  only-m guarantee, applied to a behavioral reachability readout.
- **Risk / defense:** **MEDIUM → MEDIUM-HIGH (Round 2).** **VERIFICATION:** successor
  representation (Dayan 1993, DOI 10.1162/neco.1993.5.4.613) is policy-conditioned
  future-occupancy background. **Round 2 found the close conceptual neighbor:
  perceptual aliasing** (Whitehead & Ballard 1991, DOI 10.1007/BF00058926; companion
  Chrisman 1992) — "indistinguishable percepts require different responses," i.e.
  same-observation / different-hidden-state → different appropriate future. **Mandatory
  defense:** cite and demarcate — perceptual aliasing is the *agent's* inference/memory
  problem (disambiguate aliased states to act optimally); ours is an *experimenter's*
  identification protocol (match observable present + fast state + action distribution,
  vary only the slow history-formed memory, with yoked/sham controls and a reachability-
  distribution endpoint). **No complete protocol precedent found (Rounds 1–2).** N4
  novelty survives as the *protocol*, not the intuition; the reviewer's most likely
  counter is now anticipated.

## N5 — Directional signature: aligned advantage vs blocked/novel stickiness (A5)

- **Asserted novel:** a bidirectional behavioral prediction (benefit + perseverative
  cost) from consolidation, not merely a divergence magnitude.
- **Overlap (verify):** perseveration / cognitive-rigidity / set-shifting literature;
  habit vs goal-directed control (R-05). Perseveration costs are well documented in
  behavior; the novelty is that they emerge here from the *same* selection-specific
  memory that yields the aligned advantage, under matched present.
- **Residual novelty:** the joint advantage+cost signature as a discriminating
  prediction of the write-back account within this identification design.
- **Risk / defense:** LOW–MEDIUM. **VERIFIED (Round 3):** habit/goal-directed arbitration
  (Daw, Niv, Dayan 2005, DOI 10.1038/nn1560) is the background home for perseverative
  (habitual, inflexible) cost. Defense = frame the aligned-advantage-plus-change-cost as a
  *within-model joint directional prediction consistent with known perseveration*, not a
  new behavioral discovery.

## N6 — Self-demarcation (own prior work)

- **CSC (R-14):** must be cited and distinguished (orthogonal identification vs
  life-likeness question); risk is a reviewer seeing overlap in "selection/history."
  Defense already drafted in §5.2.
- **Ψ_f (R-15):** must be cited and explicitly NOT load-bearing here; risk is a
  reviewer thinking the paper smuggles a cost theory. Defense already in §5.2 + the
  J_ext/J_write null finding.

## Summary of novelty risk

| claim | novelty locus | risk | required action |
|---|---|---|---|
| N1 | counterfactual W_sel + 4-cell dissociation | LOW–MED | verify R-01/R-06; keep "instrument" framing |
| N2 | pre-registered negative (yoked) result | LOW | verify R-03/R-09; keep as falsification |
| N3 | info-measure as *gate* + selection-specificity | **MED–HIGH → resolved (tightened R3)** | **VERIFIED: measure not novel (CAI is the direct neighbor; empowerment/TE/VIC); mechanism-as-signal not novel (CAI/VIC); gated consolidation not novel (recall-gated plasticity).** Residual = the *combination* (path-memory gate + yoked/sham + reachability endpoint). Cite; no complete precedent found. |
| N4 | matched-present only-m identification | **MED-HIGH (R2)** | **Perceptual aliasing (Whitehead & Ballard 1991) is the close conceptual neighbor — cite + demarcate (agent-inference vs experimenter-identification).** SR = future-occupancy background. No complete protocol precedent (R1–R2). |
| N5 | joint advantage+cost signature | LOW–MED | verify R-05; within-model framing |
| N6 | demarcation from CSC / Ψ_f | MED | verify R-14/R-15 status; keep §5.2 demarcation |

**Highest-priority verification: N3 (R-08, R-10).** The paper's most contestable
novelty is the controllability score; the reference ledger must resolve the closest
prior information measures before any strengthening of the N3 wording, and the
current hedges ("to our knowledge"; "not the conditional mutual information of the
acting policy") must remain until then.

**Status (citation-insertion round, 2026-07):** N3 resolution APPLIED to the
manuscript (measure explicitly disavowed as novel; ingredient citations inserted at
Methods 2.4 / Intro §1 / Discussion §5.2). N4 perceptual-aliasing demarcation and N5
habit/goal-directed framing APPLIED (Discussion §5.2, Results §3.4). All exclusivity
sentences unified to "to our knowledge, no close protocol-level precedent combining
these elements was identified in our search." Residual novelty for every N-row is
unchanged — narrowed to the *combination*, not strengthened. Self-cites (N6) carry
"unpublished manuscript" + author-to-confirm status notes; CSC not marked
"submitted," Ψ_f not marked "published/in press."
