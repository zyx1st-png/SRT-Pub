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
| R-08 | §2.4 | the score r_t as action-attributable predictive information; distinction from conditional mutual information of the acting policy | information-theoretic references (pointwise LLR / directed or transfer information / interventional information); must support that we do NOT claim policy-CMI | — | NEEDS-VERIFY |
| R-09 | §2.5, §3.2 | master-yoked control design (reinforcement decoupled from own responses) | yoked-control / learned-helplessness methodological reference | — | NEEDS-VERIFY |
| R-10 | §2.7 | external-action sham dissociating self- vs external attribution; sense of agency / controllability | agency / controllability-signal references (e.g., control-based intrinsic signals) | — | NEEDS-VERIFY |
| R-11 | §2.9, §3.3 | equivalence testing against pre-registered bounds | TOST / equivalence-testing methodological reference | — | NEEDS-VERIFY |
| R-12 | §2.9 | percentile bootstrap CIs; paired bootstrap | bootstrap methodological reference | — | NEEDS-VERIFY |
| R-13 | §1, §3.4 | "future reachability / reachable set" as a behavioral construct | reachable-set / reachability references (control or RL successor-representation adjacency) | — | NEEDS-VERIFY |
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
