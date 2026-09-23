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
A0-Q       requires the author's wording to be preserved;
A0-P       requires a recorded author-originated move whose wording is not preserved;
A1         requires a recorded acceptance event for that consolidation;
A1-claimed = the record says "the author accepts / confirms", but neither an acceptance
             event nor author wording for that item is preserved in the repository.
```

`A1-claimed` is not a demotion. It marks items whose acceptance granularity cannot currently be reconstructed. The author may confirm them (-> A1) or reclassify them (-> M with direction-level acceptance). A source-intuition location does not by itself upgrade M content into author authority.

## 2. Evidence sources

**E1 — derivation trace.** `SRT_GRG_DIALOGUE_DERIVATION_TRACE_RECONSTRUCTIBILITY_REACH_2026-09-22.md` attributes most moves to "the dialogue" or "the analysis". Author-originated moves: §3 (connecting the theory to the AI era) and §14 (the forgetting / reach question). Recorded acceptance events: §2 (re-objectification) and §27 (the narrow generative-debt definition). No comparable trace exists for the dialogue segments behind the first two 09-22 records.

**E2 — author messages of 2026-09-23** (Claude Code session executing the Phase 2 closure of PR #1031), quoted verbatim.

[A0-Q] Instruction authorizing the P0 boundary repair:

```text
删除 Core/SRT_Core_21_Minimal_Axioms.md 中
“= an actual breaking of generative equivalence.”

P0 保留：
Selection = genuine actualised non-neutral differentiation.

不要用新的等价定义替代它。
继续明确：
genuine actualised Selection
vs merely descriptive / modelled change
= OPEN。
```

[A0-Q] Phase 2 closure instruction, restating the accepted criteria:

```text
1. Selection occurrence 不再绑定 retained historical efficacy / sedimentation / inheritance；
2. terminal Selection remains genuine；
3. arbitrary descriptive / modelled change 不自动成为 Selection；
4. anti-tautology distinction 保持 OPEN；
```

**E3 — Phase 1 execution report, relayed by the author on 2026-09-23.** It gives candidate original wording for the trace §14 question: “forgetting 是否就是垂直结构中 reach 去压平差异化”. The original dialogue is not in the repository, so this is an A0-Q candidate pending author confirmation.

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
| §A term-of-art guard (not pre-given-option choice) | A1-claimed | consistent with pre-existing canonical P0-01 ("does not specify a prior chooser / a completed option set") and the 2026-09-14 Selection-totality calibration |
| §A retained-consequence occurrence criterion | SUPERSEDED | superseded at author level by the capacity / intervention-grammar record §A; removed from canonical owners in PR #1031 |
| §B–§M (cuts, diffuse sediment, vertical loop, proxy, expectation, attractor, friction, support, higher-order, relation reorganization, lower-level autonomy, weak wholeward) | A1-claimed | no derivation trace for this segment; same-day revisions: §I support wording retyped neutral by the reach record §Q (see §5 row 9); §J capacity retention corrected by the capacity record §G |
| §N BCTB methodological consequence | A1-claimed | the record itself keeps it "weaker than an author cancellation decision"; evidence lineage in §4 |
| §O–§Q guards / OPEN / repository consequence / correction pointer | M | record structure |

### 3.2 `SRT_AUTHOR_ADJUDICATION_GRG_GENERATIVE_CAPACITY_INTERVENTION_GRAMMAR_2026-09-22.md`

| Section | Typing | Evidence / note |
|---|---|---|
| §A occurrence != sediment != inheritance; terminal Selection genuine; descriptive change not automatically Selection; anti-tautology OPEN | A0-Q-confirmed (2026-09-23) | E2. Its wholeward-integration clause remains A1-claimed. Its identity "= actual breaking of generative equivalence" was explicitly **not** landed in P0 (E2) and stays source-level wording |
| §B–§AA | A1-claimed | no trace for this segment |
| §AB objectification closure | A1-claimed | trace §1 ("the dialogue began from a correction"); origin not stated |
| §AC re-objectification | A1 | trace §2: "The author accepted re-objectification as a higher-order generative capacity." |
| §AD–§AE methodological core / architecture intuition | A1-claimed | |
| §AF–§AI guards / OPEN / repository consequence / pointer | M | record structure |

### 3.3 `SRT_AUTHOR_ADJUDICATION_GRG_REACH_RECONSTRUCTIBILITY_GENERATIVE_DEBT_2026-09-22.md`

Origin is taken from the trace wording: "author", "dialogue / analysis" (explicitly non-author), or "unstated".

| Section | Trace | Origin | Acceptance evidence | Typing |
|---|---|---|---|---|
| §A AI changes the cost of reconstructibility | §3 | author | — | move A0-P; section wording A1-claimed |
| §B reconstructible generative civilization | §4 | unstated | claimed only | A1-claimed |
| §C unified grammar != one final model | §5 | dialogue | claimed only | A1-claimed |
| §D progressive reconstructibility | §7 | dialogue | claimed only | A1-claimed |
| §E minimum sufficient generative provenance | §6 | analysis | claimed only | A1-claimed |
| §F provenance itself is Selection | §9 | dialogue | claimed only | A1-claimed |
| §G provenance pluralism / distributed retention | §8 | dialogue | claimed only | A1-claimed |
| §H generative redundancy | §10 | dialogue | claimed only | A1-claimed |
| §I generative lineage / evidence independence | §11 | dialogue | claimed only | A1-claimed |
| §J unresolved friction as memory | §12 | dialogue | claimed only | A1-claimed |
| §K cumulative self-reconstruction | §13 | dialogue | claimed only | A1-claimed |
| §L generative forgetting as reach compression | §14 | author | — | A0-P (trace English rendering); A0-Q candidate via E3 |
| §M active vs latent reconstructive reach | §16 | dialogue | claimed only | A1-claimed |
| §N healthy vs destructive compression | §15 | unstated | claimed only | A1-claimed |
| §O higher-order depth | §17 | unstated | claimed only | A1-claimed |
| §P vertical structure as reach architecture | §18 | analysis | claimed only | A1-claimed |
| §Q proxy and support in reach dynamics | §19 | dialogue | claimed only | A1-claimed |
| §R genuine vs supported equivalence | §20 | analysis | claimed only | A1-claimed |
| §S memory / attention / forgetting through reach | §18 | analysis | claimed only | A1-claimed |
| §T power as reach control | §21 | unstated | claimed only | A1-claimed |
| §U failed cut != first exception | §24 | dialogue | claimed only | A1-claimed |
| §V friction as exposed cost of maintained equivalence | §22–§23 | unstated | claimed only | A1-claimed |
| §W parasitic vs integrative compensation | §25 | analysis | claimed only | A1-claimed |
| §X friction conversion | §26 | unstated | claimed only | A1-claimed |
| §Y generative debt (narrow definition) | §27 | dialogue-proposed | recorded: "The author accepted the narrow definition" | A1 |
| §Z debt displacement | §28 | analysis | claimed only | A1-claimed |
| §AA debt not automatically pathological | §29 | dialogue | claimed only | A1-claimed |
| §AB borrowing present stability | — | "accepted in the dialogue" | claimed only | A1-claimed |
| §AC wholeward more concrete | §30 | unstated | claimed only | A1-claimed |
| §AD civilizational memory as multi-reach memory | — | — | claimed only | A1-claimed |
| §AE AI-era risk | — | — | claimed only | A1-claimed |
| §AF integrated chain | §31 | synthesis | — | M |
| §AG civilization-scale synthesis | — | — | claimed only | A1-claimed |
| §AH–§AJ guards / OPEN / repository consequence | — | record structure | — | M |

### 3.4 Derivation trace

Keep intact. It is the only in-repository evidence of origin and acceptance for the reach record. Do not rewrite it into an author-only narrative.

### 3.5 Summary

```text
A0-Q-confirmed : capacity record §A (canonical-facing content), via E2
A1 (recorded)  : capacity record §AC; reach record §Y
A0-P           : reach record §A (move), §L (question; A0-Q candidate via E3)
A1-claimed     : 71 sections (vertical-dynamics record 13, capacity record 29, reach record 29),
                 plus the wording of reach record §A and the wholeward clause of capacity record §A
M              : record-structure sections
```

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

- The execution ref is a branch without a PR ref. If it is deleted, the evidence commits can become unreachable. See D4.
- The R5 result uses `status: complete`, which is outside the frontmatter ratchet enum. A verbatim landing on main would require retyping its status, so this package records a pointer instead.

## 5. Vocabulary crosswalk — PROPOSED dispositions

Base: Phase 1 audit §6. Row 3 is added here. Row 7 stays DISTINGUISH; the "MERGE / INHERIT" wording in the Phase 2 execution report is not adopted.

| # | 2026-09-22 term | 09-22 source | Existing owner / vocabulary | Disposition | Note |
|---|---|---|---|---|---|
| 1 | Selection occurrence | capacity record §A | P0-03; Irreversibility A | INHERIT — LANDED (PR #1031) | |
| 2 | sedimentation | capacity record §A; vertical-dynamics record §C | Irreversibility B (retained historical efficacy); L0 history; L₂ | INHERIT | canonical already writes "retained historical efficacy / sedimentation / L2-side history"; no new canonical term |
| 3 | generative retention | L0 permanent-distinction block (wording from the vertical-dynamics landing) | retained historical efficacy | INHERIT — LANDED in this package (§6.2) | |
| 4 | generative asymmetry | capacity record §B | O0 non-maximal indifference + S0 actualising differentiation (L0 Quick Reference; 2026-09-14 O0 adjudication) | RETYPE: analytic face, not a second primitive | the source already says so |
| 5 | friction: constitutive / boundary | vertical-dynamics record §H; capacity record §M; reach record §V | `Psi_f` ontological friction (`_SRT_PSI_F_CANONICAL.md`, Freeze-A) | DISTINGUISH | constitutive friction overlaps the `Psi_f` payability burden; boundary friction (the cost of maintaining an equivalence against returning mismatch) is a GRG research term, not canonical `Psi_f` and not automatically `Delta Psi_f` |
| 6 | expectation | vertical-dynamics record §F | `E_G` (GRG v0.3); 2026-09-20 generative-expectation typing (B / C) | INHERIT | "reshapes reachability" stays research-level |
| 7 | generative inheritance | capacity record §A | X4c inherited reconstructed condition + carrier architecture | DISTINGUISH (no merge) | X4c is a carrier-explicit specialization requiring carrier + successor cohort + changed later possibility structure |
| 8 | proxy | vertical-dynamics record §E; capacity record §Q | measurement proxy in the symbol table (`d`, `T_dir`) | DISTINGUISH | GRG proxy = operative generative partition / mediation |
| 9 | support | vertical-dynamics record §I vs reach record §Q, §W | — | RETYPE to the neutral reach-record §Q definition; integrative vs parasitic as outcome classes | removes the "parasitic support" contradiction created by the success-defined wording |
| 10 | generative reach | capacity record §R; reach record §M, §P | reachability; accessibility (`T_dir` accessibility index); propagation | KEEP AS RESEARCH TERM | representation OPEN (reach record §AI) |
| 11 | reconstructibility | reach record §A–§K | provenance / retrieval mechanics (bounded retrieval protocol) | DISTINGUISH | the theory term is broader than retrieval |
| 12 | generative debt | reach record §Y | repository "debt" usages (reconciliation debt, canonical repair debt, GOV-SUB01 residuals) | DISTINGUISH | GRG research burden != repository work debt |

## 6. Canonical edits made in this package

Each is a separate commit, so any of them can be dropped.

1. **L0 terminal-guard provenance.** The L0 sentence that attributed `terminal Selection remains genuine` to the 2026-09-22 correction now names its origin: the 2026-09-14 author hard guards (O0 primitive generativity §G / §L; Selection-totality §L), reconfirmed on 2026-09-22. No semantic change.
2. **L0 permanent distinction.** `generative retention` -> `retained historical efficacy`, the canonical name of Irreversibility B. No semantic change intended.
3. **Owner versions.** L0 v4 -> v5, Core_21 Minimal v3 -> v4, Spine v3 -> v4, plus the Registry Spine entry. PR #1031 changed owner content after the 2026-09-22 bumps, so each distinct content now has a distinct version.
4. **Context Bundles** regenerated by the generator only.

Not done (optional, author choice): a Spine §2.1 backlink "(typed owner: `Core_Law/SRT_Irreversibility.md` A / B)".

## 7. Author decisions requested

- **D1** Provenance of the 71 A1-claimed sections: confirm as A1 in bulk, per record, or reclassify as M with direction-level acceptance.
- **D2** Confirm the E3 wording as the A0-Q for reach record §L / trace §14.
- **D3** Vocabulary dispositions 1–12: accept, amend or reject.
- **D4** T1 evidence preservation: protect the execution ref (for example a tag at `b393b46c`), or land a retyped copy of the R5 result later together with the #1027 disposition.
- **D5** Keep or drop the canonical commits in §6.1–§6.3.

## 8. Constraint

The SPINE Context Bundle is close to its load budget (about 153.8K of 155,000 estimated tokens after this package). Any later text added to SPINE inputs (L0, Spine, Core_21, Registry, SRT_AI_START and other registered inputs) must be offset.

## 9. Phase 4 carry-forward (not executed)

- STATUS §0.4 / §0.4a compression; one current next; mark §0.5 and the 2026-09-21 Immediate routing as superseded.
- GRG v0.3 synchronization boundary (Phase 1 audit §11, Option C).
- Governance gaps (Phase 1 audit §12): unresolved same-day dialogue -> no direct Freeze-A semantic landing; C-class canonical semantic edit -> independent content review before merge.
- Recommended rule for future author-adjudication records: tag A0-Q / A0-P / A1 / M per item; A1 requires a recorded acceptance event.

BCTB T2 remains HOLD.
