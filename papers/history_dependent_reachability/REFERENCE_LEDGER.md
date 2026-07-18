# REFERENCE LEDGER — History-Dependent Reachability

Systematic literature audit for the manuscript. **No citation is inserted into the
manuscript until its row here is marked VERIFIED with a real DOI/venue and its
"supports sentence" column checked against the actual source.** This file is a
worklist, not a bibliography; author verification is required for every entry.

Status legend: `NEEDS-VERIFY` = candidate identified by topic, DOI/venue not yet
confirmed by the author; `VERIFIED` = author confirmed DOI + that the source
supports the exact sentence; `SELF` = author's own manuscript (status must be
stated honestly, e.g. "submitted", not "in press", unless true).

## A. Topic areas → sentences needing support

Each row: the manuscript sentence/claim, the topic, what a citation must support,
and its effect on novelty. Candidate works are described by topic only; the author
must supply and verify the actual reference. **DOI/venue fields are intentionally
blank pending verification — do not fill with guesses.**

| # | Manuscript locus | Claim needing support | What the cite must establish | DOI / venue | Status |
|---|---|---|---|---|---|
| R-01 | §1, §5.2 | "dynamical-systems theory characterizes stability, attractors, hysteresis, bifurcation" | standard reference(s) for stability/hysteresis in stochastic bistable systems | — | NEEDS-VERIFY |
| R-02 | §1, §5.2 | "control theory quantifies the cost of reaching/holding states" | reachability/controllability + minimum-control-energy references | — | NEEDS-VERIFY |
| R-03 | §1, §3.2, §5.2 | "reinforcement learning and metaplasticity describe how experience reshapes future updates" | metaplasticity / meta-learning-rate (volatility→learning rate) references | — | NEEDS-VERIFY |
| R-04 | §1, §5.2 | "predictive-processing / FEP / active inference characterize regulation under changing statistics" | primary FEP/active-inference reference(s); the specific claim is complementarity, NOT refutation | — | NEEDS-VERIFY |
| R-05 | §5.2 | habit formation as history-dependent behavior | RL/neuro habit-formation reference | — | NEEDS-VERIFY |
| R-06 | §2.2, §2.3 | committor / escape-barrier / Kramers functionals used as W_sel readouts | committor + Kramers-rate references (transition-path theory) | — | NEEDS-VERIFY |
| R-07 | §2.3 | Euler–Maruyama integration of the SDE | standard numerical-SDE reference | — | NEEDS-VERIFY |
| R-08a | §2.4, §5.2 | the score belongs to the action→outcome information family; measure is NOT claimed novel | **Empowerment** — Klyubin, Polani, Nehaniv (2005), IEEE CEC, 128–135. Read: channel capacity max_p(a) I(A^n;S′). Overlap = **MEASURE** (empowerment = capacity; ours = non-capacitated fixed-μ MI I_μ(A;O|s), same family, NOT an "instance of empowerment"). Direct. **Downgrades N3 measure novelty.** | **10.1109/CEC.2005.1554676** | **VERIFIED** |
| R-08b | §2.4, §5.2 | isolating directed/attributable information from shared history | **Transfer entropy** — Schreiber (2000), Phys. Rev. Lett. 85(2):461–464. Read: conditions out common-history/shared-input info. Overlap = **MEASURE (neighboring, observational)**. NOT the information-theoretic equivalent of the yoke; interventional causal information flow (Ay & Polani) is the closer neighbor to the yoked manipulation. | **10.1103/PhysRevLett.85.461** | **VERIFIED** |
| R-08c | §2.4, §5.2 | action→outcome information used as a learning signal in RL | **Variational empowerment** — Mohamed & Rezende (2015), NeurIPS 28. Read: I(a;s′) as intrinsic objective, variational bound. Overlap = **MEASURE + mechanism-as-signal** (drives action/exploration, NOT memory consolidation). Direct (contrast). | — (NeurIPS, no DOI) | **VERIFIED** |
| R-08d | §2.4 | directed information / causal information flow / intrinsic control (measure family, breadth) | Massey (1990) directed information; Ay & Polani (2008) causal information flow; Gregor et al. (2016) VIC. Overlap = MEASURE (partial-mechanism for VIC). | — | NEEDS-CONFIRM |
| R-09 | §2.5, §3.2 | master-yoked control design (reinforcement decoupled from own responses) | yoked-control / learned-helplessness methodological reference | — | NEEDS-VERIFY |
| R-10 | §2.7 | external-action sham dissociating self- vs external attribution; sense of agency / controllability | agency / controllability-signal references (e.g., control-based intrinsic signals) | — | NEEDS-VERIFY |
| R-11 | §2.9, §3.3 | equivalence testing against pre-registered bounds | TOST / equivalence-testing methodological reference | — | NEEDS-VERIFY |
| R-12 | §2.9 | percentile bootstrap CIs; paired bootstrap | bootstrap methodological reference | — | NEEDS-VERIFY |
| R-13 | §1, §3.4 | "future reachability / reachable set" as a behavioral construct | **Successor representation** — Dayan (1993), Neural Computation 5(4):613–624. Read: discounted expected future-state occupancy = policy-conditioned future-occupancy structure. Overlap = **ENDPOINT/background vocabulary** only (NOT a reachable-set protocol precedent); ours is a behavioral arrival distribution under a matched-present protocol. | **10.1162/neco.1993.5.4.613** | **VERIFIED** |
| R-13b | §1, §2.8 | matched-present / only-slow-memory identification protocol | **No close protocol-level precedent identified in Round 1** (not a proof of non-existence). Path dependence and hidden-state/POMDP identifiability are background neighbors; Round-2 will search them directly. | — | ROUND1: NO-CLOSE-PRECEDENT (Round-2 targets: POMDP aliasing, hidden slow state, memory-based RL, matched-endpoint path dependence) |
| R-14 | §2.4, §5.2 | Costly Selective Closure (self) — orthogonal question | self-cite; status must be stated accurately | — (SELF: Adaptive Behavior, **submitted** — confirm current status) | SELF / NEEDS-STATUS |
| R-15 | §2.2, §5.2 | Ontological friction Ψ_f (self) — NOT used as load-bearing here | self-cite; status must be stated accurately | — (SELF: Frontiers ms 1837760, **under review** — confirm current status) | SELF / NEEDS-STATUS |
| R-16 | §5.2 (optional) | integrated information theory, IF named at review | IIT reference — currently NOT named in body; decision pending | — | OPTIONAL / not-in-body |

## B. Verification protocol (author)

For each NEEDS-VERIFY row: (1) obtain the canonical reference; (2) confirm the DOI
and current publication status; (3) read the cited passage and confirm it supports
the exact manuscript sentence (no citation inflation); (4) mark VERIFIED and only
then allow insertion. For SELF rows: state the true status; do not upgrade
"submitted"/"under review" to "in press"/"published" unless confirmed.

## C. Anti-inflation rules

- No citation may be attached to a novelty claim in `NOVELTY_AUDIT.md` unless its
  row here is VERIFIED.
- Exclusivity sentences keep the "to our knowledge" qualifier regardless of how
  many references are added.
- No secondary/review citation may stand in for a primary claim it does not itself
  make.
- Reference count is not a goal; each cite must earn a specific sentence.
