---
id: SRT-REPOSITORY-SELF-RECONSTRUCTION-PHASE3-PROVENANCE-VOCABULARY-MAP-20260923
type: audit
status: active
date: 2026-09-23
layer: operations
epistemic_layer: operations
claim_mode: audit
canonical: false
ai_do_not_use_for_definition: true
research_mode: U
comparative_claim: none
named_comparator: none
dependency:
  - Operations/Audits/SRT_REPOSITORY_SELF_RECONSTRUCTION_PHASE1_AUDIT_2026-09-23.md
  - Operations/Handoffs/SRT_REPOSITORY_SELF_RECONSTRUCTION_PHASE2_GENERATED_CLOSURE_2026-09-23.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GRG_SCIENTIFIC_GAIN_ORDER_WHOLEWARD_2026-09-21.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_SELECTION_GENERATIVE_VERTICAL_DYNAMICS_2026-09-22.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GRG_GENERATIVE_CAPACITY_INTERVENTION_GRAMMAR_2026-09-22.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GRG_REACH_RECONSTRUCTIBILITY_GENERATIVE_DEBT_2026-09-22.md
  - 01_Source_Intuition/SRT_GRG_DIALOGUE_DERIVATION_TRACE_RECONSTRUCTIBILITY_REACH_2026-09-22.md
  - Core_Law/SRT_Irreversibility.md
tags: [RepositoryReconstruction, Provenance, Vocabulary, GRG, BCTB, Phase3]
---

# Repository self-reconstruction — Phase 3 provenance and vocabulary map

## 0. Scope and boundary

Phase 3 of the repository self-reconstruction programme.

```text
Phase 1 audit = Operations/Audits/SRT_REPOSITORY_SELF_RECONSTRUCTION_PHASE1_AUDIT_2026-09-23.md
Phase 2       = PR #1031, COMPLETE / PASS (closure record: the Phase 2 handoff, archived)
Phase 3       = this file + the bounded commits listed in §6
```

This file:

- types the provenance of the three 2026-09-22 author-adjudication records against the existing A0-Q / A0-P / A1 / M schema, using only evidence preserved in the repository or in the author messages quoted in §2;
- records the BCTB T1 evidence lineage as a pointer;
- records a **PROPOSED** vocabulary crosswalk for the 2026-09-22 research terms;
- lists the mechanical canonical edits made in the same package and the author decisions that remain.

It does **not**:

- rewrite the adjudication records or the derivation trace;
- upgrade any machine synthesis to author authority;
- adjudicate vocabulary dispositions (everything in §5 is PROPOSED unless marked LANDED);
- touch STATUS, governance rules, GRG v0.3 ownership, BCTB #1027 content or T2 (Phase 4 / HOLD).

## 1. Schema and evidence rule

Schema, from `SRT_AUTHOR_ADJUDICATION_GRG_SCIENTIFIC_GAIN_ORDER_WHOLEWARD_2026-09-21.md §0`:

```text
A0-Q = direct author quotation
A0-P = faithful paraphrase of an author statement; must not be presented as literal wording
A1   = machine consolidation explicitly accepted by the author
M    = machine research synthesis / proposal not independently author-owned
```

Evidence rule applied here:

```text
A0-Q = the author's wording is preserved;
A0-P = a recorded author-originated move is preserved, but not as literal wording;
A1   = a machine consolidation has a preserved explicit author acceptance event;
M    = machine synthesis / section wording lacks item-level author quotation or acceptance evidence.
```

Earlier Phase 3 drafting used `A1-claimed` as a temporary audit-debt marker for records that said "the author accepts / confirms" without preserving an item-level event. It is **not** an authority class. Final dispositions in this file resolve those items into A0-Q / A0-P / A1 / M. A source-intuition location or record-level directional acceptance does not by itself upgrade machine wording into author authority.

## 2. Evidence sources

**E1 — derivation trace.** `SRT_GRG_DIALOGUE_DERIVATION_TRACE_RECONSTRUCTIBILITY_REACH_2026-09-22.md` attributes most moves to "the dialogue" or "the analysis". Author-originated moves: §3 (connecting the theory to the AI era) and §14 (the forgetting / reach question). Recorded acceptance events: §2 (re-objectification) and §27 (the narrow generative-debt definition). No comparable trace exists for the dialogue segments behind the first two 09-22 records.

**E2 — 2026-09-23 Phase 2 repair decision.** The bounded P0 repair wording was produced as a machine consolidation and then accepted / executed by the author. It is therefore **A1 acceptance evidence, not A0-Q author wording**. The accepted canonical-facing burden is:

```text
Selection occurrence
!= retained historical efficacy / sedimentation / inheritance;

terminal Selection remains genuine;

arbitrary descriptive / modelled change
!= Selection automatically;

genuine actualised Selection
vs merely descriptive / modelled change
= OPEN.
```

The same accepted repair removed `= an actual breaking of generative equivalence` from P0 and deliberately did not replace it with a new equivalent definition. This confirms the bounded semantic direction at A1 strength; it does not convert the machine phrasing into direct author quotation.

**E3 — preserved author wording for the forgetting / reach move.** The author's original conversational wording was:

> **“认同，这不就是垂直结构中reach去压平的差异化吗。”**

Its conversational antecedent was the discussion of generative forgetting / reach compression. This sentence is A0-Q. The derivation trace's English rendering — “Is generative forgetting not just the vertical structure using reach to flatten differences?” — is a faithful A0-P paraphrase, not a literal author quotation.

## 3. Item-level provenance map

Short names used below:

```text
vertical-dynamics record = 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_SELECTION_GENERATIVE_VERTICAL_DYNAMICS_2026-09-22.md
capacity record          = 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GRG_GENERATIVE_CAPACITY_INTERVENTION_GRAMMAR_2026-09-22.md
reach record             = 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GRG_REACH_RECONSTRUCTIBILITY_GENERATIVE_DEBT_2026-09-22.md
```

### 3.1 `SRT_AUTHOR_ADJUDICATION_SELECTION_GENERATIVE_VERTICAL_DYNAMICS_2026-09-22.md`

| Section | Typing | Evidence / note |
|---|---|---|
| §A term-of-art guard (not pre-given-option choice) | M / inherited direction | section wording lacks an item-level acceptance event; its substance is consistent with the already author-owned 2026-09-14 Selection-totality guard |
| §A retained-consequence occurrence criterion | SUPERSEDED | superseded at author level by the capacity / intervention-grammar record §A; removed from canonical owners in PR #1031 |
| §B–§M (cuts, diffuse sediment, vertical loop, proxy, expectation, attractor, friction, support, higher-order, relation reorganization, lower-level autonomy, weak wholeward) | M | the record carries direction-level author acceptance, but no item-level acceptance event is preserved; same-day revisions: §I support wording retyped neutral by the reach record §Q (see §5 row 9); §J capacity retention corrected by the capacity record §G |
| §N BCTB methodological consequence | M + evidence pointer | no item-level acceptance event is preserved; the independent T1 evidence lineage is recorded in §4 |
| §O–§Q guards / OPEN / repository consequence / correction pointer | M | record structure |

### 3.2 `SRT_AUTHOR_ADJUDICATION_GRG_GENERATIVE_CAPACITY_INTERVENTION_GRAMMAR_2026-09-22.md`

| Section | Typing | Evidence / note |
|---|---|---|
| §A occurrence != sediment != inheritance; terminal Selection genuine; descriptive change not automatically Selection; anti-tautology OPEN | A1 | E2 records author acceptance of the machine-consolidated Phase 2 repair at this bounded canonical-facing strength |
| §A wholeward-integration clause + "= actual breaking of generative equivalence" wording | M / source-level | no item-level author wording or acceptance event is preserved for these exact formulations; the generative-equivalence identity was explicitly **not** landed in P0 |
| §B–§AA | M | record-level directional acceptance may exist, but no item-level acceptance event is preserved |
| §AB objectification closure | M | trace §1 says the dialogue began from a correction, but does not preserve author origin or acceptance for this exact section wording |
| §AC re-objectification | A1 | trace §2: "The author accepted re-objectification as a higher-order generative capacity." |
| §AD–§AE methodological core / architecture intuition | M | no item-level acceptance event preserved |
| §AF–§AI guards / OPEN / repository consequence / pointer | M | record structure |

### 3.3 `SRT_AUTHOR_ADJUDICATION_GRG_REACH_RECONSTRUCTIBILITY_GENERATIVE_DEBT_2026-09-22.md`

Origin is taken from the derivation trace. Item-level authority follows the four-class schema only; a record-level statement that “the author accepts” does not by itself upgrade machine-generated section wording.

| Section | Trace | Origin / acceptance evidence | Typing |
|---|---|---|---|
| §A AI changes the cost of reconstructibility | §3 | author-originated move; wording not preserved | A0-P for the move; section wording M |
| §B reconstructible generative civilization | §4 | no item-level author wording / acceptance event preserved | M |
| §C unified grammar != one final model | §5 | dialogue / analysis | M |
| §D progressive reconstructibility | §7 | dialogue-proposed; no preserved item-level acceptance event | M |
| §E minimum sufficient generative provenance | §6 | analysis | M |
| §F provenance itself is Selection | §9 | dialogue / analysis | M |
| §G provenance pluralism / distributed retention | §8 | dialogue / analysis | M |
| §H generative redundancy | §10 | dialogue / analysis | M |
| §I generative lineage / evidence independence | §11 | dialogue / analysis | M |
| §J unresolved friction as memory | §12 | dialogue / analysis | M |
| §K cumulative self-reconstruction | §13 | dialogue / analysis | M |
| §L generative forgetting as reach compression | §14 | direct author wording preserved in E3; English trace is paraphrase | A0-Q for the Chinese author sentence; A0-P for the English rendering |
| §M active vs latent reconstructive reach | §16 | dialogue-proposed; no preserved item-level acceptance event | M |
| §N healthy vs destructive compression | §15 | origin / acceptance not preserved at item level | M |
| §O higher-order depth | §17 | origin / acceptance not preserved at item level | M |
| §P vertical structure as reach architecture | §18 | analysis | M |
| §Q proxy and support in reach dynamics | §19 | dialogue / analysis | M |
| §R genuine vs supported equivalence | §20 | analysis | M |
| §S memory / attention / forgetting through reach | §18 | analysis | M |
| §T power as reach control | §21 | origin / acceptance not preserved at item level | M |
| §U failed cut != first exception | §24 | dialogue / analysis | M |
| §V friction as exposed cost of maintained equivalence | §22–§23 | origin / acceptance not preserved at item level | M |
| §W parasitic vs integrative compensation | §25 | analysis | M |
| §X friction conversion | §26 | origin / acceptance not preserved at item level | M |
| §Y generative debt (narrow definition) | §27 | dialogue-proposed; trace explicitly records author acceptance | A1 |
| §Z debt displacement | §28 | analysis | M |
| §AA debt not automatically pathological | §29 | dialogue / analysis | M |
| §AB borrowing present stability | — | record says “accepted in the dialogue”, but no acceptance event is preserved | M |
| §AC wholeward more concrete | §30 | origin / acceptance not preserved at item level | M |
| §AD civilizational memory as multi-reach memory | — | no item-level provenance preserved | M |
| §AE AI-era risk | — | no item-level provenance preserved | M |
| §AF integrated chain | §31 | synthesis | M |
| §AG civilization-scale synthesis | — | no item-level provenance preserved | M |
| §AH–§AJ guards / OPEN / repository consequence | — | record structure | M |

### 3.4 Derivation trace

Keep intact. It is the only in-repository evidence of origin and acceptance for the reach record. Do not rewrite it into an author-only narrative.

### 3.5 Summary

```text
A0-Q
= direct author wording preserved:
  reach record §L / trace §14 Chinese sentence in E3.

A0-P
= author-originated move whose exact wording is not preserved:
  reach record §A;
  plus the English rendering of the §L question.

A1
= machine consolidation with a preserved explicit acceptance event:
  capacity record §A canonical-facing Phase 2 repair subset (E2);
  capacity record §AC re-objectification;
  reach record §Y narrow generative-debt definition.

M
= remaining machine synthesis / section wording / record structure
  where no item-level author wording or acceptance event is preserved.
  Record-level directional acceptance may be noted, but does not upgrade item-level provenance.

SUPERSEDED
= the earlier retained-consequence occurrence criterion.
```

`A1-claimed` is retained only as a historical audit-debt label in earlier drafts. It is **not** a fifth authority class and is not used as a final disposition here.

## 4. BCTB T1 evidence lineage (pointer; no landing)

```text
programme routing on main:
  01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_SELECTION_GENERATIVE_VERTICAL_DYNAMICS_2026-09-22.md §N
  STATUS.md §0 / §0.4 / §0.4a (BCTB = secondary diagnostic candidate; T2 not automatic)

evidence lineage (not on main):
  execution ref = experiments/grg-bctb0-t1-preexec-package-20260922
                  @ b393b46c64f172a4fba770982219b5249e32dded
  R5 result     = Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_R5_EVALUATION_RESULT_2026-09-22.md
                  blob e6108481a3dc47e45aeb537ffde4c1cc34830934
  package index = Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_PACKAGE_INDEX_2026-09-22.md
                  blob 687e51402d3e9c449207fd4d48419be6461c3f88
  score packets = Operations/GRG/BCTB0/T1/Outputs/SRT_GRG_BCTB0_T1_{G,S,A,C}{1,2,3}_SCORE_2026-09-22.md
  charter / pre-execution audit = draft PR #1027 (refs/pull/1027/head = 7875772e9cde149ec2406cc34e8e52fcf30464ca)
```

Frozen verdict, quoted from the R5 result §0:

```text
fold = T1
generator freeze = 12/12 COMPLETE
formal identity probe = AMBIGUOUS
blind integrity = COMPROMISED
valid core fold = NO
absolute historical-transfer credit = NO
allowed use = COMPROMISED-DIAGNOSTIC

historical A/X/F recovery = YES
GRG residual candidate = NO
residual classification = BASELINE-SHARED
canonical consequence = NONE
M4 credit = NONE
M5 credit = NONE
scientific-distinctiveness credit = NONE
```

Bounded inference recorded:

```text
T1 (COMPROMISED-DIAGNOSTIC) found no GRG-specific residual:
every arm recovered the historical admission / exclusion structure (majority 3/3 per arm).
Together with the author's 2026-09-22 concern that relation-transfer is not the GRG core burden,
this supports only:
  BCTB = secondary diagnostic candidate; T2 not automatic.
It does not support: GRG credit of any kind, a claim about what the GRG core burden is,
a rerun, T2, or promotion of the benchmark result into theory authority.
```

Preservation notes:

- Evidence-preservation ref: `archive/grg-bctb0-t1-evidence-20260922` -> `b393b46c64f172a4fba770982219b5249e32dded`. This archival branch exists only to keep the execution evidence reachable; it grants no theory authority, valid-core credit or T2 authorization.
- The original execution ref may still be deleted later without losing reachability through the archival ref.
- The R5 result uses `status: complete`, which is outside the frontmatter ratchet enum. A verbatim landing on main would require retyping its status, so this package records a pointer instead.

## 5. Vocabulary crosswalk — PROPOSED dispositions

Base: Phase 1 audit §6. Row 3 is added here. Row 7 stays DISTINGUISH; the "MERGE / INHERIT" wording in the Phase 2 execution report is not adopted.

| # | 2026-09-22 term | 09-22 source | Existing owner / vocabulary | Disposition | Note |
|---|---|---|---|---|---|
| 1 | Selection occurrence | capacity record §A | P0-03; Irreversibility A | INHERIT — LANDED (PR #1031) | |
| 2 | sedimentation | capacity record §A; vertical-dynamics record §C | Irreversibility B (retained historical efficacy); L0 history; L₂ | INHERIT / RETYPE | research shorthand under retained historical efficacy where later efficacy is established; do not create a second canonical owner |
| 3 | generative retention | L0 permanent-distinction block (wording from the vertical-dynamics landing) | retained historical efficacy | INHERIT — LANDED in this package (§6.2) | |
| 4 | generative asymmetry | capacity record §B | O0 non-maximal indifference + S0 actualising differentiation (L0 Quick Reference; 2026-09-14 O0 adjudication) | RETYPE: analytic face, not a second primitive | the source already says so |
| 5 | friction: constitutive / boundary | vertical-dynamics record §H; capacity record §M; reach record §V | `Psi_f` ontological friction (`_SRT_PSI_F_CANONICAL.md`, Freeze-A) | DISTINGUISH | both are GRG research terms; neither is automatically `Psi_f` or `Delta Psi_f`. Any mapping to canonical `Psi_f` requires an explicitly declared bridge and its own burden |
| 6 | expectation | vertical-dynamics record §F | 2026-09-20 generative-expectation typing B + C0/C1; `E_G` in GRG v0.3 | ALIGN / INHERIT FROM B+C0/C1; DISTINGUISH FROM `E_G` | 09-22 structural / operative expectation may reshape reachability, but it is not automatically `E_G`. Reserve `E_G` for typed transformation expectation / classification relative to an admitted Generative Order; use projected `E_G` only under the separately typed Projected Order route |
| 7 | generative inheritance | capacity record §A | X4c inherited reconstructed condition + carrier architecture | DISTINGUISH (no merge) | X4c is a carrier-explicit specialization requiring carrier + successor cohort + changed later possibility structure |
| 8 | proxy | vertical-dynamics record §E; capacity record §Q | measurement / operational proxy vocabulary in the symbol table and canonical owners (`d`, `T_dir`, domain projections) | RENAME + DISTINGUISH | prefer `generative proxy` / `GRG proxy` when ambiguity exists; GRG proxy = operative generative partition / mediation, not a measurement proxy |
| 9 | support | vertical-dynamics record §I vs reach record §Q, §W | — | RETYPE to the neutral reach-record §Q definition; integrative vs parasitic as outcome classes | removes the "parasitic support" contradiction created by the success-defined wording |
| 10 | generative reach | capacity record §R; reach record §M, §P | reachability; accessibility (`T_dir` accessibility index); propagation | KEEP AS RESEARCH TERM | representation OPEN (reach record §AI) |
| 11 | reconstructibility | reach record §A–§K | provenance / retrieval mechanics (bounded retrieval protocol) plus earlier domain-specific reconstructibility usages | DISTINGUISH / QUALIFY | prefer `generative reconstructibility` where theory meaning could be confused with repository / data / empirical reconstructibility; the GRG research term remains broader than retrieval |
| 12 | generative debt | reach record §Y | repository "debt" usages (reconciliation debt, canonical repair debt, GOV-SUB01 residuals) | DISTINGUISH | GRG research burden != repository work debt |

## 6. Canonical edits made in this package

Each is a separate commit, so any of them can be dropped.

1. **L0 terminal-guard provenance.** The L0 sentence that attributed `terminal Selection remains genuine` to the 2026-09-22 correction now names its origin: the 2026-09-14 author hard guards (O0 primitive generativity §G / §L; Selection-totality §L), reconfirmed on 2026-09-22. No semantic change.
2. **L0 permanent distinction.** `generative retention` -> `retained historical efficacy`, the canonical name of Irreversibility B. No semantic change intended.
3. **Owner versions.** L0 v4 -> v5, Core_21 Minimal v3 -> v4, Spine v3 -> v4, plus the Registry Spine entry. PR #1031 changed owner content after the 2026-09-22 bumps, so each distinct content now has a distinct version.
4. **Context Bundles** regenerated by the generator only.

Not done (optional, author choice): a Spine §2.1 backlink "(typed owner: `Core_Law/SRT_Irreversibility.md` A / B)".

## 7. Author decisions applied in this corrective

- **D1 provenance**: do **not** bulk-upgrade the 71 former `A1-claimed` items. Final authority remains the four-class A0-Q / A0-P / A1 / M schema. Without a preserved item-level author wording or explicit acceptance event, machine section wording is M; record-level directional acceptance may be noted without upgrading item-level authority.
- **D2 forgetting / reach**: the direct author quotation is `认同，这不就是垂直结构中reach去压平的差异化吗。` The English trace remains A0-P.
- **D3 vocabulary**: rows 1–12 are adopted with the dispositions shown in §5 after the Phase 3 corrective. In particular, expectation is aligned to the 2026-09-20 B+C0/C1 typing but distinguished from `E_G`; generative inheritance remains broader than X4c; proxy is renamed / distinguished where ambiguous.
- **D4 T1 evidence**: preserved through archival ref `archive/grg-bctb0-t1-evidence-20260922` at `b393b46c64f172a4fba770982219b5249e32dded`. Evidence preservation does not authorize T2 or confer theory credit.
- **D5 canonical commits**: keep the L0 terminal-guard provenance correction, `generative retention -> retained historical efficacy` vocabulary correction and owner-version / Registry sync.

## 8. Constraint

The SPINE Context Bundle is close to its load budget (about 153.8K of 155,000 estimated tokens after this package). Any later text added to SPINE inputs (L0, Spine, Core_21, Registry, SRT_AI_START and other registered inputs) must be offset.

## 9. Phase 4 carry-forward (not executed)

- STATUS §0.4 / §0.4a compression; one current next; mark §0.5 and the 2026-09-21 Immediate routing as superseded.
- GRG v0.3 synchronization boundary (Phase 1 audit §11, Option C).
- Governance gaps (Phase 1 audit §12): unresolved same-day dialogue -> no direct Freeze-A semantic landing; C-class canonical semantic edit -> independent content review before merge.
- Recommended rule for future author-adjudication records: tag A0-Q / A0-P / A1 / M per item; A1 requires a recorded acceptance event.

BCTB T2 remains HOLD.
