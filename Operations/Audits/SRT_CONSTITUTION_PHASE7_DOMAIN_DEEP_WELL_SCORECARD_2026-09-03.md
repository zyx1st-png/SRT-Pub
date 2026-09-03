---
id: SRT-CONSTITUTION-PHASE7-DOMAIN-DEEP-WELL-SCORECARD-20260903
type: audit
status: active
version: v2
date: 2026-09-03
layer: meta
epistemic_layer: governance
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
decision_state: author_choice_pending
dependency:
  - Operations/Proposals/SRT_CONSTITUTION_DOMAIN_EXECUTION_PLAN_2026-08-29.md
  - Governance/SRT_GOV_CONSTITUTION_DOMAIN_RECONSTRUCTION_2026-08-29.md
  - Core_Law/SRT_Constitution_V1.md
  - Operations/Audits/SRT_CONSTITUTION_PHASE6_IND_COLLECTIVE_CROSSSCALE_ROLE_MAP_2026-09-02.md
  - Operations/Audits/data/srt_active_theory_nodes.json
  - Experiments/AUDIT.md
  - Experiments/SRT_Experimental_Roadmap_v1.md
tags: [Constitution, Phase7, DomainResearch, DeepWell, Scorecard, AuthorChoice]
---

# Phase 7 — first domain deep-well scorecard

> **Decision state**: scoring complete；author choice pending。
>
> **Scope**: this is the Phase-7 comparison surface required by the execution plan。It does not choose a domain，start Phase 8，change a theory owner，or make a domain evidence claim。
>
> **Evidence snapshot**: repository `main` at `c70e5c4f`，2026-09-03。Version v2 includes a complete top-level `Experiments/` C4 pass。

---

## 0. Review disposition in v2

The C4 completeness objection is accepted。Version v1 did not name `Experiments/` or its independently audited locked holdout chain，even though C4 is the criterion most sensitive to the difference between plans and evidence already paid for。Version v2 therefore inventories all **22 current top-level entries** under `Experiments/`，routes each asset family to candidate domains，and recalculates C4 before retaining or changing any score。

The requested `M(t) -> T-SUFF-5` carry-over is not added because its premise is false on the evidence snapshot。The Phase-6 role map already contains，under §6：

- a named `M(t) -> T-SUFF-5` owner route；
- the declared-cut / suffering-bearer / observable-return-channel projection chain；
- the explicit rule that the relation is projection / owner routing，not identity or automatic entailment；
- the remaining MOC，coefficient，normalization and domain-identification debts；
- a priority-family coverage row marking that route explicit。

Creating a second Phase-8 carry-over would duplicate an already completed Phase-6 routing obligation。It would also blur the difference between **owner routing already complete** and **domain measurement still evidence-deferred**。

---

## 1. Candidate-set rule

The candidate set is taken from the seven domains named by the governance breadth stop rule：

```text
Physics
Biology
AI
Social
Consciousness
Neuroscience
Epistemology
```

This avoids making candidate admission itself the hidden selection step。`Consciousness` and `Neuroscience` are scored separately because their method burdens differ materially：the former includes phenomenal / first-person explanatory burdens，while the latter can be bounded by neural measurement and intervention designs。

If the author later chooses a combined Consciousness + Neuroscience well，the Phase-8 charter must state which question requires the combination and must narrow the object enough to remain one well。

---

## 2. Scoring contract

The seven criteria are copied from Phase 7 of the execution plan：

| Key | Criterion |
|---|---|
| C1 | existing repository depth |
| C2 | clarity of the traditional Given One |
| C3 | strength of the bearer / position issue |
| C4 | availability of domain-native evidence / methods |
| C5 | chance of producing a visible reorganization or new research question |
| C6 | ability to compare against strong existing frameworks |
| C7 | manageable scope |

Ordinal scale：

| Score | Meaning |
|---:|---|
| 0 | no repository-grounded basis found |
| 1 | isolated analogy or fragment only |
| 2 | weak / highly indirect preparation |
| 3 | workable，but a major burden is still open |
| 4 | strong，with a concrete bounded path |
| 5 | unusually strong and immediately usable for this criterion |

All criteria are equally weighted because the plan supplies no alternative weights。The total is a **readiness summary，not a selection algorithm**。A one-point difference cannot decide the domain for the author。

### C4 anti-inflation rule

For C4，the fact that a field has methods somewhere in the world is insufficient。The score must be supported by a repository-visible path to domain-native evidence：an executable or frozen protocol，identified data access，a completed domain case，an evidence dossier，or a concrete measurement / intervention design。

```text
general literature exists
!=
this repository is ready to pay the domain evidence burden
```

---

## 3. Score matrix

| Candidate | C1 | C2 | C3 | C4 | C5 | C6 | C7 | Total / 35 | Confidence |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Physics | 5 | 4 | 2 | 3 | 4 | 5 | 2 | **25** | medium |
| Biology | 3 | 4 | 4 | 4 | 5 | 4 | 4 | **28** | medium |
| AI | 4 | 4 | 5 | 5 | 3 | 5 | 4 | **30** | high |
| Social | 4 | 4 | 5 | 3 | 5 | 5 | 2 | **28** | medium |
| Consciousness | 5 | 5 | 5 | 3 | 5 | 5 | 2 | **30** | high |
| Neuroscience | 5 | 4 | 5 | 4 | 5 | 5 | 3 | **31** | high |
| Epistemology | 4 | 5 | 5 | 4 | 4 | 5 | 4 | **31** | medium-high |

The equal-weight result produces a **top cluster，not a winner**：Neuroscience and Epistemology score 31；AI and Consciousness score 30。Their profiles are different enough that the author decision cannot be replaced by the total。After the complete `Experiments/` pass in §4.1-4.2，all C4 values and totals remain unchanged；this is now a reviewed result rather than an omission。

---

## 4. Criterion 4 evidence/method audit

This is the discriminating criterion that most easily disappears behind repository depth。

| Candidate | Repository-visible domain-native path | C4 | Main unpaid burden |
|---|---|---:|---|
| Physics | `SRT_Physics_Claim_Status.md` fixes interpretation-specific evidence floors；`SRT_Phys_E05_Falsifiability_Program.md` and PHR-A provide discriminator / intervention requirements；no `Experiments/` asset is a physical-system experiment | 3 | no repository-owned executed physical experiment or unique empirical discriminator for the larger bridge claims |
| Biology | E. coli chemotaxis audit uses receptor perturbation，FRET，single-cell trajectory and microfluidic-gradient logic；ALIFE costly-selection pilots have executed simulations；the two AGING01 assets are parked / pre-pilot | 4 | wet-lab evidence is literature-reconstructed rather than generated here；life node remains partially active / behavior-untested |
| AI | frozen software events，correct-SHA / rejected-write controls and SEA cases are executable；`Experiments/` adds locked anchoring，ChoiceMap，selective-resynchronization and stake / future-selectability protocol families，including GO，NO-GO，design-infeasible and uninterpretable outcomes | 5 | a new deep well still needs a question not already closed as Case A / STOP or paid as an existing computational protocol |
| Social | institutional-publication cases，SEA coding manual and `M(t)` / MOC supply an audit design；no `Experiments/` asset executes a real institutional consequence-loop study | 3 | consequence-loop measurement，unit selection and counterfactual identification are unresolved in real social data |
| Consciousness | phenomenal-structure interfaces and first/third-person separation provide triangulation routes；the D-value / salience package and PHENCOMP protocol remain draft or parked and do not test phenomenal necessity | 3 | no current protocol directly adjudicates structural bearing `->?` phenomenal presence；neural or behavioral correlates cannot silently pay HP-B |
| Neuroscience | NEURAL25 / NEURAL33 / NEURAL34 protocols，NB1 execution card，data-access provenance，prediction tables and matched-state designs provide concrete experimental routes；the executed ML assets in `Experiments/` are not natural-neural data | 4 | NB1 is not formally locked / preregistered / executed，and several proxies remain P4 until validated |
| Epistemology | Forcing-CH evidence dossiers，method-individuation protocol，control-case protocol and bounded archive inventories constitute a domain-native evidence programme；generic anchoring / decision simulations do not execute this historical-method evidence design | 4 | control archive Part II remains unsigned；enumeration and control selection are still blocked |

The C4 result blocks two tempting shortcuts：

```text
large theory directory
-> high evidence readiness

published adjacent work
-> target claim already testable
```

Neither inference is licensed。

### 4.1 Complete `Experiments/` input pass

The repository currently has **22 top-level entries** under `Experiments/`。The following grouping is exhaustive at that level；nested files are interpreted through their owner README / decision record rather than counted as independent experiments。

| Top-level asset family | Count | Primary domain route | Locked / executed evidence state | C4 effect |
|---|---:|---|---|---|
| `AUDIT.md` | 1 | evidence-governance infrastructure | `final_audit_v1`，but scope is only the five `anchoring_*` directories；verifies commit chain，seed separation and bit-identical tiny-MDP rerun；retains a real Phase-2b NO-GO and downgrades mechanical controls | changes the weight of the anchoring chain，not a domain score by itself |
| `SRT_AGING01_*` | 2 | Biology | draft；roadmap marks the pair parked / pre-pilot / outside the execution queue | reinforces a biological method path but does not justify Biology C4=5 |
| `SRT_D_Value_vs_Salience_*` | 6 | cognitive / behavioral measurement，adjacent to Consciousness and Neuroscience | draft / review package；stimuli，pre-rating，dictionary and analysis plan exist，but no locked preregistration or result | no increase to Consciousness or Neuroscience C4 |
| roadmap，pilot cards，ethics note | 3 | cross-domain planning | active roadmap / cards plus draft ethics note；these organize future tests rather than execute one | no direct C4 increase |
| `SRT_PHENCOMP_Aha_Identifiability_Protocol_v0_2.md` | 1 | Consciousness / cognitive-neuroscience interface | draft，`parked_pre_pilot_v0_2`，`execution_authorized: false`；predictive discrimination only，not HP-B | no increase to Consciousness or Neuroscience C4 |
| five `anchoring_*` directories | 5 | AI / synthetic agent and cross-domain construct instrumentation | frozen chain with feasibility GO，locked holdout NO-GO，locked controllability GO and locked tiny-MDP confirmatory GO；independent audit limits the result to designed-model feasibility | strongly confirms AI C4=5；does not transfer to natural-system domains |
| `choicemap_explicit_scaffolding` | 1 | AI / synthetic decision systems | active locked confirmatory，authoritative result records GO under leakage and budget audits | confirms AI C4=5；does not raise another domain |
| two `selective_resynchronization_*` directories | 2 | AI / machine learning | locked Fashion-MNIST MVP ends NO-GO；matched-path follow-up ends design-infeasible before future-task execution | confirms that AI can pay negative-result and stop-rule costs；AI already scores 5 |
| `stake_future_selectability_mvp` | 1 | AI / reinforcement-learning agents | frozen full formal cohort；decision is `UNINTERPRETABLE PROTOCOL` after a preregistered structural gate failure | confirms protocol-lock and adverse-result capacity；does not support canonical `d` or raise another domain |

The locked negative and uninterpretable results count positively for **method availability and evidence discipline**，because C4 is not a support score。They do not count as positive evidence for the target claims。Likewise，a neural network is not a neuroscience experiment merely because it uses neural terminology，and a decision model is not an epistemology case merely because it bears on choice or inference。

### 4.2 C4 recalculation

| Candidate | v1 C4 | v2 C4 | Result after complete input pass |
|---|---:|---:|---|
| Physics | 3 | **3** | no executed physical-system evidence added |
| Biology | 4 | **4** | AGING01 is parked；existing chemotaxis / ALIFE path remains the load-bearing basis |
| AI | 5 | **5** | multiple frozen and executed computational families confirm the existing maximum |
| Social | 3 | **3** | no executed real-institution consequence-loop study added |
| Consciousness | 3 | **3** | human-facing packages are draft / parked and do not adjudicate HP-B |
| Neuroscience | 4 | **4** | executed ML protocols cannot replace an executed natural-neural protocol |
| Epistemology | 4 | **4** | anchoring simulations cannot replace the forcing-CH control archive and method-history test |

Therefore the total ranking is unchanged。This non-change is substantive：the omitted infrastructure has now been counted at its actual evidence level，while domain transfer has been refused where the repository itself forbids it。

---

## 5. Candidate profiles

### 5.1 Physics — high depth，low bearer leverage，large scope

**Repository anchors**：

- `Physics/README.md` and `Physics/SRT_Physics_Claim_Status.md`；
- measurement / representation owners and PHR-A evidence floor；
- quantum-instrument，reference-frame，thermodynamics and relational-time bridges；
- `NODE-PHYSICS-MEASUREMENT = active_complete / observed`。

**Why the scores are high**：the repository is deep，the traditional Given One is visible in state space，measurement outcome，observer frame，law and object identity，and rival frameworks are unusually strong。

**Why it is not currently top-ranked**：bearer / consequence position is not load-bearing in every physics question；the domain is broad enough to invite interpretation drift，cross-scale analogy and a return to universal formalism before one empirical discriminator is fixed。

**Minimum viable well**：one interpretation-plural measurement / record-formation question with one declared physical system，event unit and discriminator。

### 5.2 Biology — less depth，good experimental form，high potential increment

**Repository anchors**：

- `03_Bridges/SRT_Dissipative_Structures_and_Selection_Structures_Bridge_2026-08-04.md`；
- `Operations/SRT_LIFE_BOUNDARY_CASE_ECOLI_CHEMOTAXIS_UNIFIED_AUDIT_2026-08-05.md`；
- ALIFE 2026 manuscript family and executed costly-selection simulation pilots；
- `NODE-LIFE-DISSIPATIVE = partially_active / untested`。

**Why the profile is attractive**：organism，cell，lineage and environment cuts make the Given One and bearer question concrete；FRET，microfluidics，knockouts，single-cell trajectories and intervention logic can expose whether SRT reorganizes evidence rather than renaming adaptation。

**Main weakness**：there is no dedicated Biology owner directory comparable to Physics / Neuroscience，and the existing life work has not yet demonstrated behavioral availability as a coherent domain node。

**Minimum viable well**：the already-bounded E. coli chemotaxis case，extended only to the same-event consequence-bearing measurement that the negative audit identified as missing。

### 5.3 AI — easiest execution，strong bearer contrast，increment risk

**Repository anchors**：

- `AI/AI_POSITIONING_NOTE.md`，`AI/SRT_AI_Claim_Status.md` and architecture-state distinctions；
- AI consciousness / agency rubrics；
- SEA correct-SHA，rejected-write and disconnected-write cases；
- `NODE-AI-REASONING = active_complete / robustly_observed`。

**Why C3/C4 are maximal**：model，tool，pipeline，operator and institution can be experimentally separated；software state and consequence return can be logged，reset and intervened on cheaply。

**Why C5 is only 3**：the AI layer is a dormant，touch-repair library；the existing AI cluster and retrieval probes already produced Case A / STOP results。A Phase-8 well that only repeats capability / persistence / stake separations would be translation or validation，not a visible new reorganization。

**Minimum viable well**：a matched persistent-agent experiment where memory continuity and non-transferable consequence return vary independently，with no consciousness verdict built into the outcome。

### 5.4 Social — strongest consequence-attribution use case，weakest scope control

**Repository anchors**：

- `Core_Law/SRT_Collective_Selection.md` and Def-C-2 `M(t)`；
- `Philosophy/SRT_Soc_03_Institutions.md` and social / political compacts；
- SEA institutional-publication cases and coding manual；
- `NODE-SOCIAL-L2 = partially_active / untested`。

**Why C3/C5 are high**：institution，group，member，decision，beneficiary and consequence bearer are routinely mis-collapsed；re-cutting them can visibly reorganize claims about collective choice and externalization。

**Main weakness**：real social systems create severe unit，boundary，grain，timescale，confounding and measurement burdens。`M(t)` remains a P2 diagnostic object with unresolved concrete measurability，so a broad institutions / politics well would be unmanageable。

**Minimum viable well**：one bounded institutional event with a frozen actor-role map and measurable consequence / recourse channels；no society-wide `M(t)` claim。

### 5.5 Consciousness — clearest constitutional pressure，method gap at HP-B

**Repository anchors**：

- `Philosophy/SRT_HardProblem_Epistemology.md`；
- `Philosophy/SRT_Phenomenal_Structure_Interface.md` and `SRT_Consciousness_Conditions.md`；
- consciousness mechanism owners and existing published neural work；
- `NODE-CONSCIOUSNESS = active_complete / robustly_observed`。

**Why C2/C3/C5 are maximal**：the pre-given subject，experience，report and third-person object are exactly the sort of Ones the Constitution is intended to re-cut。`still this / from here / for me` and structural-vs-phenomenal bearing expose a nontrivial unresolved problem。

**Why C4 is only 3 and C7 only 2**：the active owner explicitly leaves `Structural Bearing ->? Phenomenal Presence` open。First-person reports，neural measures and structural criteria can constrain the problem，but no current method directly establishes phenomenal necessity。Without a narrow subproblem，the hard problem expands beyond one well。

**Minimum viable well**：one dissociation question among experience，memory closure，report and same-bearer attribution；not “solve consciousness”。

### 5.6 Neuroscience — strongest evidence-ready Constitution test

**Repository anchors**：

- `Neuroscience/SRT_Neural_Mechanisms.md` and both mechanism CompactCores；
- `SRT_NEURAL25_EXPERIMENT_PROTOCOL_v0_1.md`；
- `SRT_NEURAL33_EXPERIMENT_PROTOCOL_v0_1.md`；
- `SRT_NEURAL34_MATCHED_STATE_RELATIONAL_HISTORY_PROTOCOL_v0_1.md`；
- NB1 execution card and W0 data-access provenance；
- `NODE-NEURAL-DECODABILITY = active_complete / observed`。

**Why it scores 31**：the repository already contains neural implementations of re-identification，history，state transition，embodied position and report dissociations；the field supplies intervention，decoding，matched-state，physiology and behavioral methods，plus strong rivals such as GWT，IIT，FEP / predictive processing and recurrent-processing approaches。

**Why it is not automatically selected**：the folder is deep partly because it contains many patches，hooks and staging documents；its README says NB1 remains unregistered and unexecuted。Proxy inflation (`d = PCI / Phi / salience` or `Psi_f = free energy / prediction error`) remains a live risk。

**Minimum viable well**：NEURAL34-style matched neural state with relational-history perturbation，or another single protocol that separates current state identity from history-conditioned future efficacy。

### 5.7 Epistemology — cleanest bounded method family，less direct empirical bearer

**Repository anchors**：

- `Philosophy/SRT_HardProblem_Epistemology.md` and philosophy foundations；
- Forcing-CH evidence dossiers；
- frozen method-individuation and control-case selection protocols；
- bounded archive inventories and evidence-obligation ledger。

**Why C2/C3/C6 are high**：object，proof method，research regime，observer position，evidence and historical availability can all be re-cut；strong rival accounts and historical records are available without needing SRT vocabulary。

**Why confidence is below the neuro / AI cases**：the candidate can quietly become internal philosophy or historiography instead of testing a domain increment。The control archive also remains incomplete，so the clean method programme is not yet fully executable。

**Minimum viable well**：complete one preregistered independent control case under the existing forcing-CH method-individuation protocol，then test whether the Constitution changes the object / method cut in a way the baseline does not already supply。

---

## 6. Decision surface for the author

The totals do not select the domain。They expose three materially different leading profiles：

| If the first well should prioritize... | Candidate with the strongest current profile | What is being accepted |
|---|---|---|
| domain-native measurement and intervention | Neuroscience | higher protocol readiness，with proxy and execution debt |
| bounded method / historical evidence discipline | Epistemology | cleaner object/method audit，with weaker direct empirical bearer pressure |
| direct attack on the Constitution's hardest bearer question | Consciousness | maximum conceptual pressure，with the largest C4 / scope debt |

AI remains the fastest executable control-like option，but its lower C5 score means the Phase-8 charter would need to name a genuine unresolved increment before selection。Biology is the strongest developmental alternative because it has a concrete same-event measurement gap。Physics and Social should be selected only with a sharply narrower subproblem than their directory-level labels。

No row in this section is an author decision。

---

## 7. Phase-8 entry gate after author choice

Whichever domain is chosen，Phase 8 must not start until one bounded charter records：

1. the exact domain object and the traditional Given One being re-cut；
2. the mandatory Bearer-Objectification Declaration；
3. one matched system / contrast or equivalent domain-native baseline；
4. the strongest existing rival frameworks；
5. measurable outcome and evidence-access path；
6. falsifier / withdrawal condition；
7. why this is one deep well rather than a parallel domain programme。

The author decision should be recorded separately from this scorecard。Until then：

```text
Phase 7 scoring = complete
author choice = pending
Phase 8 = not started
```
