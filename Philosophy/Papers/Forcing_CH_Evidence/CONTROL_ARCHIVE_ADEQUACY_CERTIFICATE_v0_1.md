---
id: SRT-PAPER-FORCING-CH-EVIDENCE-CONTROL-ARCHIVE-ADEQUACY-CERTIFICATE
title: "Control Archive Adequacy Certificate v0.1 — Boundary Fixed, Adequacy Unattested"
type: evidence_procedure_record
status: draft
canonical: false
layer: philosophy_bridge
epistemic_layer: evidence
claim_mode: evidence
date: 2026-08-05
updated: 2026-08-11
version: v0_1
certificate_state: part_i_fixed_part_ii_unattested
boundary_state: fixed_v0_1
archive_state: assembly_in_progress
archive_corpus_work_permitted: true
enumeration_permitted: false
binding_scope: forcing_ch_control_case_selection
strategy_amendment: false
binding_strategy: Philosophy/Papers/Mathematical_Reachability_and_Problem_Individuation_Strategy.md@strategy_note_v0_7
governed_by: Philosophy/Papers/Forcing_CH_Evidence/CONTROL_CASE_SELECTION_PROTOCOL_v0_1.md
---

# Control Archive Adequacy Certificate v0.1

Step 2 of `CONTROL_CASE_SELECTION_PROTOCOL_v0_1` §8, executed as far as it can honestly be executed today.

**The certificate has two halves, and only one of them can be signed now.**

| Part | Content | State |
|---|---|---|
| **I** | The search boundary — period, discipline, subfield, exclusions | **FIXED**. This is the half that had to be committed before any reading, and it is committed here |
| **II** | The four adequacy attestations of protocol §2 | **UNATTESTED**. One local archive unit is now assembled, but corpus-wide adequacy has not been established |

**Enumeration remains blocked.** Protocol §8 step 3 may not begin until Part II is signed. Nothing in this file selects, names, or evaluates a candidate case.

**Archive-corpus assembly is permitted now.** §4 distinguishes collecting corpus material from enumerating candidates; without that distinction the certificate would deadlock, since the archive could not be built without voiding the round it serves.

> **SCOPE LOCK**
>
> No candidate case appears here. No verdict is issued. `EVD-D05-0001` remains **qualified**; `EVD-D04-0002` remains **unresolved**. `strategy_note_v0_7` remains frozen and unmodified. No source is entered into the evidence base: naming a search venue below is **not** a source citation and does not enter anything through the `SRC-*` material pipeline.

## 1. Why Part I is signed now and Part II is not

Protocol §2(1) requires the period and subfield boundary to be *"fixed in advance, not adjusted while reading."* The cleanest possible moment to fix it is before an archive exists at all — there is then nothing to adjust it toward. That is the moment this file uses.

Protocol §2(2)–(4) are attestations *about the archive corpus as a whole*: that it supplies the contemporaneous record, that it can support all six audit tests, and what its coverage limits are. A first local unit can demonstrate some of those capacities locally without discharging the corpus-wide attestations. Signing them now would still be fabrication, and it would defeat §2(4)'s entire purpose, which is to let a later "no admissible candidate" finding be distinguished from a thin archive.

So Part I is a **commitment**; Part II remains an open **work order** during corpus assembly.

## 2. PART I — the boundary, fixed

### 2.1 Period: 1938–1963

Era-matched to the D05 comparator window.

**Reason.** A control drawn from a different era would confound method-regime change with era change: publication norms, refereeing and review culture, and the evaluative vocabulary in which "important new result" and "standard technique" are expressed all shift across decades. Holding the era fixed holds those fixed, so that the difference the calibration is meant to detect is a difference in operation type rather than in period style. It also means the same review-of-record infrastructure serves all three matrix cases.

### 2.2 Discipline: mathematics

Per protocol §4.1.

### 2.3 Subfield: mathematical logic, outside the target line

Mathematical logic of the period, excluding the CH / forcing / independence line as required by protocol §4.2.

**Reason for preferring logic over a distant field.** Protocol §4.1 asks for set theory or an immediately adjacent area, so that the comparison is not carried by disciplinary distance. Set theory itself in this window is substantially the target line, so the admissible neighbourhood is the rest of period logic.

### 2.4 Exclusions

**(a) The target line — hard exclusion.** CH; forcing; independence and relative-consistency results in set theory; inner-model construction. Protocol §4.2. Nothing from the D03 or D05 record may serve as a control.

**(b) Forcing-adjacent constructions in recursion theory — exclusion pending explicit clearance.**

This is recorded as a boundary condition, before reading, because it is the trap most likely to void a control silently.

Certain period recursion-theoretic constructions — those proceeding by finite extension, by requirement enumeration, or by producing an object generic with respect to a family of conditions — stand in a close structural relation to the Cohen construction's characteristic apparatus. A control drawn from that family could turn out to belong to the *same method family* as forcing under `METHOD_INDIVIDUATION_PROTOCOL_v0_1` exclusion 6. Such a case would not be a control at all: it would be a second forcing case wearing a control's label, and it would corrupt the calibration in the direction that flatters the paper's thesis.

Therefore: any candidate whose construction proceeds by finite extension, requirement enumeration, or genericity over a family of conditions is **inadmissible unless explicitly cleared**, and clearance must be recorded as a positive finding — that the candidate's characteristic generative resource is *not* in the forcing family — rather than assumed by default.

**(c) Contested novelty status; thin record.** Protocol §7.4 and §7.5, restated here so the boundary is self-contained.

### 2.5 Anticipated failure of the boundary — and why it is not a licence

It is possible that period logic outside the target line will prove either too thin to instantiate a mature stable method regime, or too entangled with (b) to yield a clean Control A.

That outcome is **anticipated but not pre-authorized as a widening.** If it occurs, it is reported under protocol §10 as a boundary failure, and the response is a **v0.2 of this boundary**, preregistered before re-enumeration, naming the widened scope and the archive grounds for widening.

What is prohibited: reading within this boundary, finding nothing convenient, and quietly moving to a field where a comfortable candidate is known to exist. That is the tuning protocol §7.2 forbids, executed at the boundary rather than at the candidate.

### 2.6 Boundary lock

Part I is fixed as of this file's merge. It may not be adjusted while reading. Adjustment requires a versioned successor with its own preregistration, disclosing what had already been seen at the time of adjustment.

## 3. PART II — adequacy attestations, all UNATTESTED

Each attestation below is required by protocol §2 before enumeration. Each is recorded with what would discharge it. **None is signed.**

| § | Attestation required | State | What would discharge it |
|---|---|---|---|
| 2(1) | Stated period and subfield boundary, fixed in advance | **DISCHARGED** by Part I | — |
| 2(2) | The archive can supply, for each candidate, the *contemporaneous* record: the author's own characterization plus period review or survey literature — not only later textbook treatment | **UNATTESTED** | An assembled archive with, per candidate, the original publication and at least one period review or survey notice, both located and page-verified |
| 2(3) | The archive is sufficient to run all six audit tests of `METHOD_INDIVIDUATION_PROTOCOL_v0_1` §4 on any candidate it admits | **UNATTESTED** | A worked demonstration that the six tests are runnable on the archive's record depth — in particular that the load-bearing removal/replacement test (§4.3) has enough construction detail to distinguish destruction from degradation |
| 2(4) | Coverage limits stated, so that "no admissible candidate" is distinguishable from "no candidate found in a thin archive" | **UNATTESTED** | An explicit statement of what was swept exhaustively, what was sampled, and what was not reached at all |

**Reading of the "for each candidate" quantifier.** In §2(2)–(3) it ranges over **future members of the admission pool**, not over any presently identified work. These attestations are capacity claims about the corpus — that *for whatever the corpus admits*, the contemporaneous record can be supplied and the six tests can be run. No work is identified, and signing Part II identifies none. See §4.6.

### 3.1 First-unit capacity audit — 2026-08-11, no signature

The first assembled record is `CONTROL_ARCHIVE_UNIT_SHEN_STANLEY_MULLER_MONTAGUE.md`, backed by the source manifest and coverage log indexed in the evidence README.

- `§2(2) demonstrated for this archive unit`: two complete primary publications, one period joint review, and one period technical reconstruction are page-verified.
- §2(3) remains **UNATTESTED**: the local record marks load-bearing removal/replacement **insufficient**, so the six-test capacity requirement is not discharged even locally.
- §2(4) remains **UNATTESTED globally**: the reached material is an opportunistic JSL 1953–1955 paradox/intuitive-set-theory unit, not a systematic sweep and not full-period or full-subfield coverage.

This entry records progress in archive assembly only. It signs no Part II attestation and authorizes no enumeration or later protocol step.

### 3.2 Proposed search venues — to be verified at assembly

Recorded as a work order for whoever assembles the archive. **These are venue proposals, not sources**, and none is entered into the evidence base by being named here. Each must be verified to exist, to cover the stated period, and to be reachable before it is relied on.

- the review-of-record serials for mathematics and for symbolic logic covering 1938–1963, as the primary instrument for §2(2)'s "period review literature";
- period survey and address literature in logic, as the instrument for the Control A indicator "named in period survey or review literature as a major advance";
- original publication venues for candidates surfaced by the above.

The §2(2) requirement is the binding constraint on the whole exercise: a candidate for which the *contemporaneous* characterization cannot be recovered is inadmissible under protocol §7.5, however well documented it is in later textbooks.

### 3.3 Known risk to §2(3)

Record depth for the load-bearing test is the likeliest point of failure. Period papers frequently compress construction detail in ways that make it hard to establish whether removing a component destroys or merely degrades a result. If §2(3) cannot be attested for the boundary in Part I, that is a §10 boundary failure and follows §2.5 — not a reason to relax the test.

## 4. Archive work versus candidate enumeration

### 4.1 The ambiguity being resolved

Read one way, this certificate's requirements deadlock. Part II must be signed before any candidate pool is enumerated; the archive must be assembled before Part II can be attested; and contact with a candidate before Part II is signed forces a restart. If merely *reading a paper or a review notice during assembly* counted as contact with a candidate, the archive could never be assembled without voiding the round it exists to serve.

The deadlock is an artifact of this record's own earlier wording, not of the governing protocol. `CONTROL_CASE_SELECTION_PROTOCOL_v0_1` nowhere equates archive contact with candidate enumeration: its §8 step 3 speaks of enumerating and recording a *pool*, and its §7.6 excludes works first *considered* after a verdict has been rendered in the round. Neither reaches the act of collecting corpus material. The clarification below is therefore recorded here, in a `draft` procedure record, and **amends nothing in the frozen protocol**.

**No boundary or criterion is changed.** The 1938–1963 period, the mathematical-logic scope, the target-line exclusion, the forcing-adjacent recursion-theoretic exclusion, and every Control A and Control B indicator stand exactly as registered.

### 4.2 Archive-corpus work — permitted before Part II

The following is corpus assembly, not candidate enumeration, and is permitted now:

- mechanical collection of **titles, bibliographic records, review and abstract entries, and full texts**, by sweeping the fixed period, subfield, serial and index scope registered in Part I;
- verification that the venues proposed in §3.2 exist, cover the period, and are reachable;
- recording of what was swept, sampled, or not reached, toward the §2(4) coverage statement.

Collection is driven by the **scope**, not by the work. Sweeping a serial's 1938–1963 run and recording what is in it is a bibliographic act. It carries no judgement about any item's admissibility, and it is exactly the labour Part II must certify.

### 4.3 When a work becomes a candidate

A work in the corpus becomes a **candidate** in the sense of protocol §8 step 3 at the first of these moments:

1. it is **entered into the candidate pool**; or
2. an **admission, exclusion, scoring, ranking, or individuation judgement** under protocol §§5–7 begins to be formed about it.

Until then it is corpus material, however thoroughly it has been read. The line is between *having the record* and *judging the record*.

### 4.4 Logging obligation

All archive contact before Part II is signed enters the **source and coverage log**: what was swept, in what order, what was retrieved, and what was not reached. The log is what makes §2(4)'s distinction between "no admissible candidate" and "thin archive" checkable afterwards, and it is what makes the §4.3 line auditable rather than self-certified.

### 4.5 What still triggers a restart

Restart under protocol §8 is triggered by **candidate-directed** work performed before Part II is signed:

- searching *for* a candidate rather than *within* the scope;
- screening corpus items for admissibility under §§5–7;
- scoring, ranking, or selecting;
- running any individuation audit on a control candidate.

Any of these before Part II is signed must be disclosed and the round restarted with that disclosure on the record. Corpus assembly under §4.2 does not trigger it.

### 4.6 What Part II certifies

Part II certifies the **evidentiary capacity of the archive corpus to support future members of the admission pool**: that for a work the corpus admits, the contemporaneous record can be supplied, the six audit tests can be run, and the coverage limits are known.

It is **not** advance certification of an already-chosen candidate. No work has been selected, and Part II's signature will not select one.

## 5. Remaining prohibitions until Part II is signed

- enumeration of any candidate pool (protocol §8 step 3);
- scoring, ranking or selection (steps 4–5);
- application of the individuation protocol to any control candidate (step 6).

## 6. A note on procedure-to-evidence ratio

This is the third procedural artifact in this line and the last one that should precede evidence work. Three specifications and no new historical evidence would be a failure mode in its own right — a project can be talked into perfect method and no findings.

Each of the three was written because a specific circularity or fitting risk was live and would have been unrecoverable if discovered later: the `M_t` granularity gap, the selection-verdict circularity, and the boundary-adjustment loophole. None of them was written to postpone the archive work. **The next work in this line is continued archive assembly and, only when every attestation is discharged, a signed Part II — not another protocol.**

Nothing in this file establishes any historical claim, selects any case, or licenses any verdict.
