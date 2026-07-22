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
| R-05 | §5.2 | habit/perseveration as history-dependent behavior (N5 framing) | **Daw, Niv, Dayan (2005)**, Nat. Neurosci. 8(12):1704–1711. Read: model-free (habitual, inflexible) vs model-based (goal-directed) arbitration. Overlap = **ENDPOINT/background** — grounds stickiness/perseverative cost as known. Candidates: Dickinson (1985); WCST set-shifting. | **10.1038/nn1560** | **VERIFIED (background)** |
| R-06 | §2.2, §2.3 | committor / escape-barrier / Kramers functionals used as W_sel readouts | **E & Vanden-Eijnden (2010)**, Annu. Rev. Phys. Chem. 61:391–420 (committor/TPT); Kramers (1940), Physica 7:284 (escape rate). Overlap = **background methodology**. DOI resolved 2026-07 (round: citation-insertion). | **10.1146/annurev.physchem.040808.090412** | **VERIFIED** |
| R-07 | §2.3 | Euler–Maruyama integration of the SDE | Kloeden & Platen (1992), *Numerical Solution of Stochastic Differential Equations* (Springer). Overlap = **background methodology**. | — | NEEDS-CONFIRM (canonical) |
| R-08a | §2.4, §5.2 | the score belongs to the action→outcome information family; measure is NOT claimed novel | **Empowerment** — Klyubin, Polani, Nehaniv (2005), IEEE CEC, 128–135. Read: channel capacity max_p(a) I(A^n;S′). Overlap = **MEASURE** (empowerment = capacity; ours = non-capacitated fixed-μ MI I_μ(A;O|s), same family, NOT an "instance of empowerment"). Direct. **Downgrades N3 measure novelty.** | **10.1109/CEC.2005.1554676** | **VERIFIED** |
| R-08b | §2.4, §5.2 | isolating directed/attributable information from shared history | **Transfer entropy** — Schreiber (2000), Phys. Rev. Lett. 85(2):461–464. Read: conditions out common-history/shared-input info. Overlap = **MEASURE (neighboring, observational)**. NOT the information-theoretic equivalent of the yoke; interventional causal information flow (Ay & Polani) is the closer neighbor to the yoked manipulation. | **10.1103/PhysRevLett.85.461** | **VERIFIED** |
| R-08c | §2.4, §5.2 | action→outcome information used as a learning signal in RL | **Variational empowerment** — Mohamed & Rezende (2015), NeurIPS 28. Read: I(a;s′) as intrinsic objective, variational bound. Overlap = **MEASURE + mechanism-as-signal** (drives action/exploration, NOT memory consolidation). Direct (contrast). | — (NeurIPS, no DOI) | **VERIFIED** |
| R-08d | §2.4 | directed information (measure-family breadth) | **Massey (1990)**, Proc. ISITA-90, 303–305; precursor Marko (1973). Read: directed information (feedback-aware action→outcome info; bound on feedback capacity). Overlap = **MEASURE (background)**. Candidate: Lizier & Prokopenko (local transfer). | — (ISITA, no DOI) | **VERIFIED (venue)** |
| R-08g | §2.4, §5.2 | closest measure neighbor: per-state action-influence conditional MI used as a signal | **Causal Action Influence (CAI)** — Seitzer, Schölkopf, Martius (2021), NeurIPS 2021, arXiv:2106.03443. Read: situation-dependent I(A;S′|s) used as an intrinsic signal for exploration/off-policy. Overlap = **MEASURE + MECHANISM-as-signal** (drives exploration/action, NOT memory gate; uses transition dynamics, not fixed μ). **Closest single measure neighbor to C_μ.** | arXiv:2106.03443 | **VERIFIED** |
| R-08h | §2.4, §5.2 | gated long-term consolidation is not novel; gate signal differs | **Recall-gated plasticity** — Lindsey & Litwin-Kumar (2024), eLife 12:RP90793. Read: consolidation gated by recall-consistency with existing memory. Overlap = **MECHANISM (gated consolidation)**. Gate = recall-consistency, NOT action-attributable controllability. | **10.7554/eLife.90793** | **VERIFIED** |
| R-08i | §1, §5.2 (motivation) | controllability modulates what is consolidated (natural systems) | Controllability→consolidation neuroscience (escapable vs inescapable; learned-helplessness lineage, see R-09). Overlap = **background/motivation** (the phenomenon our framework provides an identification test for; NOT a designed-model precedent). | — | NEEDS-CONFIRM (background) |
| R-08e | §2.4, §5.2 | interventional causal information (closer neighbor to the yoked manipulation) | **Ay & Polani (2008)**, *Adv. Complex Syst.* 11(1):17–41. Read: interventional (do-operator) conditional MI, explicitly contrasted with observational transfer entropy. Overlap = **MEASURE (interventional) + CONTROL-rationale** (intervention ≈ yoke). Still a measure, not a mechanism/protocol. | **10.1142/S0219525908001465** | **VERIFIED** |
| R-08f | §2.4, §5.2 | action→outcome information used as a control signal + reachability of states | **Variational Intrinsic Control** — Gregor, Rezende, Wierstra (2016), arXiv:1611.07507. Read: maximizes I(options; termination states) = states reliably reachable. Overlap = **MEASURE + MECHANISM-as-signal (drives options/skills) + partial ENDPOINT (reach states)**. Closest single combination; but drives action-level option learning, no gated memory, no matched-present/yoked-sham. | arXiv:1611.07507 | **VERIFIED** |
| R-09 | §2.5, §3.2 | master-yoked control design (reinforcement decoupled from own responses) | **Seligman & Maier (1967)**, *J. Exp. Psychol.* 74(1):1–9 (yoked / learned helplessness — the master-yoked design origin). Overlap = **CONTROL methodology (background)**; also underpins the controllability→consolidation motivation (R-08i). DOI resolved 2026-07 (round: citation-insertion). | **10.1037/h0024514** | **VERIFIED (background)** |
| R-10 | §2.7 | external-action sham dissociating self- vs external attribution; sense of agency / controllability | **Sense of agency** — Haggard (2017), *Nat. Rev. Neurosci.* 18(4):196–207 (review). Read: self-attribution of control over action and its effects. Overlap = **CONTROL/self-attribution background** (supports the self-vs-external sham framing; background, not novelty-contest). Companion (candidate): Synofzik et al. (2008). | **10.1038/nrn.2017.14** | **VERIFIED (background)** |
| R-11 | §2.9, §3.3 | equivalence testing against pre-registered bounds | **Lakens (2017)**, Soc. Psychol. Personal. Sci. 8(4):355–362 (TOST primer); original Schuirmann (1987). Overlap = **background methodology**. | **10.1177/1948550617697177** | **VERIFIED** |
| R-12 | §2.9 | percentile bootstrap CIs; paired bootstrap | **Efron (1979)**, *Ann. Statist.* 7(1):1–26; Efron & Tibshirani (1993). Overlap = **background methodology**. DOI resolved 2026-07 (round: citation-insertion). | **10.1214/aos/1176344552** | **VERIFIED (background)** |
| R-13 | §1, §3.4 | "future reachability / reachable set" as a behavioral construct | **Successor representation** — Dayan (1993), Neural Computation 5(4):613–624. Read: discounted expected future-state occupancy = policy-conditioned future-occupancy structure. Overlap = **ENDPOINT/background vocabulary** only (NOT a reachable-set protocol precedent); ours is a behavioral arrival distribution under a matched-present protocol. | **10.1162/neco.1993.5.4.613** | **VERIFIED** |
| R-13b | §1, §2.8 | matched-present / only-slow-memory identification protocol | **No complete protocol precedent found (Rounds 1–2).** Path dependence and hidden-state/POMDP identifiability are background neighbors, not this protocol. | — | ROUNDS1-2: NO-COMPLETE-PRECEDENT |
| R-13c | §1, §2.8, §5.2 | closest conceptual neighbor: same percept → different appropriate response | **Perceptual aliasing** — Whitehead & Ballard (1991), *Machine Learning* 7:45–83. Read: percepts indistinguishable from immediate input require different responses. Overlap = **MATCHING (conceptual neighbor)**. **MUST cite + demarcate:** aliasing is the *agent's* inference/memory problem; ours is an *experimenter's* matched-present identification protocol with yoked/sham + reachability endpoint. Companion (candidate): Chrisman (1992), AAAI-92. | **10.1007/BF00058926** | **VERIFIED** |
| R-14 | §2.4, §5.2 | Costly Selective Closure (self) — orthogonal question | self-cite. **Repo status:** v16 after ALIFE-2026 rejection, targeting Adaptive Behavior; no confirmed Adaptive Behavior submission record in repo. State as "revised, targeting Adaptive Behavior" — NOT "submitted/under review" without author confirmation. | — (SELF) | SELF / REPO-VERIFIED; LIVE-STATUS author-to-confirm |
| R-15 | §2.2, §5.2 | Ontological friction Ψ_f (self) — NOT used as load-bearing here | self-cite. **Repo status:** Frontiers ms **1837760**, in a **revision round** (response-to-reviewers + revision checklist in repo). State as "in revision at Frontiers (ms 1837760)" — NOT "in press"/"published." | — (SELF) | SELF / REPO-VERIFIED; LIVE-STATUS author-to-confirm |
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
