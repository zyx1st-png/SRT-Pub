---
id: SRT-PAPER-FORCING-CH-EVIDENCE-CONTROL-CASE-SELECTION-PROTOCOL
title: "Control Case Selection Protocol v0.1 — Forcing–CH Calibration"
type: evidence_protocol_candidate
status: frozen
canonical: false
layer: philosophy_bridge
epistemic_layer: evidence
claim_mode: evidence
date: 2026-08-04
version: v0_1
protocol_state: preregistered_frozen
epistemic_status: procedure_candidate
procedural_state: preregistered_frozen
freeze_scope: "selection-verdict independence principle (section 3), source scope (section 4), Control A and Control B selection criteria (sections 5-6), exclusions (section 7), enumeration and selection procedure (section 8), preregistered outcome table (section 9)"
independent_validation: none
binding_scope: forcing_ch_control_case_selection
strategy_amendment: false
binding_strategy: Philosophy/Papers/Mathematical_Reachability_and_Problem_Individuation_Strategy.md@strategy_note_v0_7
interlocks: Philosophy/Papers/Forcing_CH_Evidence/METHOD_INDIVIDUATION_PROTOCOL_v0_1.md
---

# Control Case Selection Protocol v0.1

**What this is.** A preregistered, non-canonical procedure for selecting the Control A and Control B cases that frozen `strategy_note_v0_7` §7.5–7.7 and §19(6) require, written and frozen **before any candidate case has been enumerated**.

**What this is not.** Not a strategy amendment. Not a canonical definition. Not a list of candidates. Not a verdict on any case.

## 0. Status, scope and locks

| Field | Value |
|---|---|
| Canonical | **false** — may not be cited as a definition source |
| **Epistemic status** | **procedure candidate** — untested; no selection has been carried out under it |
| **Procedural state** | **preregistered, frozen** on merge |
| **Freeze scope** | §3 independence principle, §4 source scope, §5–6 selection criteria, §7 exclusions, §8 procedure, §9 outcome table |
| Strategy amendment | **false** — `strategy_note_v0_7` remains frozen and unmodified |
| Binding scope | selection of Control A and Control B for the forcing–CH calibration |
| Retroactive force | **none** |
| Interlock | `METHOD_INDIVIDUATION_PROTOCOL_v0_1.md`, frozen for the same falsification round |

> **SCOPE LOCK**
>
> This file selects nothing and adjudicates nothing. It contains **no candidate case**, by design. It issues no C5-op, H/N/S, institutionalization, CH-regime, global update-regime, C2 or SRT verdict. `EVD-D05-0001` remains **qualified**; `EVD-D04-0002` remains **unresolved**. It modifies no strategy file, no manuscript, no canonical file, no equation and no symbol table.

## 1. Purpose

Frozen §7.7 requires a three-case calibration matrix — Control A, Control B, forcing — and §19(6) makes that triple calibration a submission condition. Frozen §7.6 adds a discipline: *"策略阶段不凭印象指定两个控制案例。必须在技术史档案完成后筛选"* — the controls may not be designated by impression, and must be selected after the technical-history archive is complete.

`METHOD_INDIVIDUATION_PROTOCOL_v0_1` is now frozen for a falsification round in which Control A and Control B are two of the four test cases. That creates a requirement §7.6 does not itself spell out: **the selection criteria must be fixed before the candidate pool is seen.** Once an auditor has looked at candidates, no later record can establish that the choice was uninfluenced by how those candidates would behave under the protocol being tested. Selection discipline is not something that can be certified retroactively.

This protocol therefore exists to be frozen early. Its content is deliberately modest; its timing is the point.

## 2. Precondition — archive adequacy

Enumeration under §8 **may not begin** until the technical-history archive required by frozen §7.6 meets the following minimum, and a dated adequacy certificate recording it exists:

1. the archive covers a stated period and subfield boundary, fixed in advance, not adjusted while reading;
2. for each candidate it can supply the *contemporaneous* record — the author's own characterization, and period review or survey literature — not only later textbook treatment;
3. it is sufficient to run all six audit tests of `METHOD_INDIVIDUATION_PROTOCOL_v0_1` §4 on any candidate it admits;
4. its coverage limits are stated, so that "no admissible candidate" can be distinguished from "no candidate found in a thin archive."

An archive that cannot meet (2) cannot support this protocol at all, because §5 and §6 rest on contemporaneous testimony rather than hindsight.

## 3. The selection-verdict independence principle

This is the load-bearing rule of the file.

> **Selection criteria must be independent of the individuation verdict they will be used to test.**
>
> A case may be selected as Control A or Control B **only** on grounds that do not presuppose, invoke, or anticipate the verdict of `METHOD_INDIVIDUATION_PROTOCOL_v0_1`.

The problem this addresses is concrete. Frozen §7.5 requires Control A to have "没有新操作类型" — no new operation type. That is exactly the question the individuation protocol adjudicates. If a case is selected as Control A *because the protocol says it introduces no new operation*, then running the protocol on it afterwards tests nothing: the expected answer was built into the selection.

The resolution is a division of labour, and every step of §8 depends on it:

| Step | Established by | May **not** be established by |
|---|---|---|
| Selection | historical and evaluative indicators from the contemporaneous record (§5, §6) | the individuation protocol's verdict |
| Verdict | the individuation protocol's six tests (§4 of that file) | the selection indicators |
| Test outcome | comparison of the two, against §9 | anything decided after the comparison |

The indicators in §5 and §6 are therefore stated as **defeasible presumptions from testimony**, never as individuation findings. A period source saying "the proof uses standard techniques" is evidence about how practitioners described the work. It is not a determination that the generative resource was unchanged — and if the protocol later disagrees with the testimony, that disagreement is the test result, not an error to be corrected in the selection.

## 4. Source scope and admissible domain

Fixed in advance:

1. **Discipline.** Candidates come from mathematics, and preferentially from set theory or an immediately adjacent area, so that the comparison with forcing is not carried by disciplinary distance.
2. **Exclusion of the target line.** No candidate may be drawn from the CH / forcing / independence line itself, nor from work whose admissibility turns on the Gödel-stage or Cohen-event record already adjudicated in D03 and D05. Controls must be uncontaminated by the case they calibrate.
3. **Period.** A stated window, fixed in the adequacy certificate before enumeration, chosen for archive quality rather than for the cases it is expected to contain.
4. **Record depth.** Only candidates for which the contemporaneous record — author's characterization plus period review or survey literature — is actually available. Absence of that record is a ground for exclusion, not for inference (`METHOD_INDIVIDUATION_PROTOCOL_v0_1` exclusion 7).

## 5. Control A — selection criteria

Control A is a **result innovation**: an important new result inside a mature, stable method regime. Frozen §7.5 states five requirements. Each is mapped below to an indicator drawn from the contemporaneous record, never from the individuation protocol.

| Frozen §7.5 requirement | Admissible selection indicator |
|---|---|
| 1. inside a mature, stable method regime | at the time of the result, the subfield had settled monograph or textbook treatment and a recognized standard method canon, with no live dispute in the period literature about which methods were admissible |
| 2. an important new result | contemporaneous evaluative standing: named in period survey or review literature as a major advance, or resolving a long-standing named problem. Later textbook prominence alone does not qualify — that is hindsight, and it measures influence |
| 3. no new operation type | **testimony only.** The author does not claim a new method, and period reviewers describe the proof as applying known or standard techniques. Recorded as a defeasible presumption. **This indicator may not be established by the individuation protocol**, and its later contradiction by that protocol is a test outcome under §9, not a selection error |
| 4. response-role structure unchanged | the kinds of answer that counted as answers to the problem, and their standing, are the same in the period record before and after |
| 5. update regime unchanged | no new axiom, principle or mode of legitimation was admitted to the field on the strength of the result |

**Preregistered expectation** (from frozen §7.5): C1, C2 and C5-op all preserved; under the individuation protocol, **not a distinct operation candidate**.

## 6. Control B — selection criteria

Control B is a **local technical innovation**: a genuinely new technique that nonetheless fails to become infrastructure. Frozen §7.6 states five requirements.

| Frozen §7.6 requirement | Admissible selection indicator |
|---|---|
| 1. a new technique with no conservative preimage in the earlier repertoire | **testimony only.** The author claims a new technique or device, and period reviewers describe it as new and not reducible to prior methods. Defeasible presumption; **not** an individuation finding |
| 2. C5-op nominally fails | nominal failure on the face of the record, i.e. entailed by indicator 1 as the period record presents it — not a protocol verdict |
| 3. serves only a local problem or short-term task | the documented application record is confined to the originating problem or a narrow cluster |
| 4. no cross-problem inheritance | no documented reuse across distinct problems, model families or proof tasks by other researchers |
| 5. no training, textbook or scaffold formation | absent from subsequent textbooks, training material, standard terminology and tooling |

Indicators 3–5 are uptake facts. They are established from the reception record and are legitimately independent of the individuation protocol; they are also what makes Control B a control rather than a second forcing case.

**Preregistered expectation** (from frozen §7.6): `¬C5_op(m*) ∧ ¬Inst(m*)` — under the individuation protocol, **a distinct operation candidate**; and, on independent H/N/S evidence, **institutionalization fails**.

## 7. Exclusions

A candidate is inadmissible if any of the following holds. Each is a prohibition on selection, not a judgement about the mathematics.

1. **Protocol-derived selection.** It was identified, preferred or retained because of how it behaves under `METHOD_INDIVIDUATION_PROTOCOL_v0_1`.
2. **Matrix-fit selection.** It was selected, or a rival rejected, because the choice makes the three-case matrix come out as frozen §7.7 predicts. This is the prohibition that `METHOD_INDIVIDUATION_PROTOCOL_v0_1` §6.1 imposes, applied at the selection stage.
3. **Contaminated domain.** It falls inside the CH / forcing / independence line (§4.2).
4. **Contested novelty status.** The period record itself disputes whether the work introduced a new technique. Such a case may be historically interesting but cannot carry a clean preregistered expectation.
5. **Thin record.** The contemporaneous record cannot support §5 or §6, or the archive cannot support all six audit tests.
6. **Post-hoc entry.** It was first considered after any protocol verdict in the current round had been rendered.
7. **Motivating resemblance.** It was chosen because it resembles the D05 case that motivated the individuation protocol. Controls exist to test that protocol outside the case that produced it.

## 8. Enumeration and selection procedure

The steps are ordered, and the order is part of the freeze. **No step may be re-run after a later step has begun.** If a step must be redone, the entire round restarts with a new dated record, and the restart — including what was already seen — is disclosed in that record.

1. **Freeze.** This protocol is frozen on merge. Enumeration before that point is void.
2. **Certify the archive.** Produce the dated adequacy certificate required by §2, including the stated period, subfield boundary and coverage limits.
3. **Enumerate mechanically.** Apply §4 to the archive and record the **full** resulting pool — every candidate considered, including every rejection with its §7 ground. A pool recorded only as its survivors is not a pool.
4. **Score and rank.** Score each pool member against the §5 or §6 indicators only. Record each score with its source citation. Rank by the number of indicators met, then by record depth.
5. **Select and lock.** Select the highest-ranked admissible candidate for each control. Record the reasons, the runners-up, and why each runner-up ranked lower. Lock the selection in a dated record before proceeding.
6. **Run the individuation protocol.** Only now apply the six audit tests of `METHOD_INDIVIDUATION_PROTOCOL_v0_1` §4 to each selected case, recording every test outcome including those that do not decide.
7. **Assess Control B's institutionalization separately.** `¬Inst` must be established from H/N/S evidence, not from the individuation verdict.
8. **Compare against §9** and record the outcome. The comparison is the test; it is not an opportunity to revisit steps 3–5.

## 9. Preregistered outcome table

Fixed now, before any candidate is known.

| Case | Preregistered expectation | Outcome that **confirms** | Outcome that **falsifies or qualifies** |
|---|---|---|---|
| **Control A** | C5-op preserved; not a distinct operation candidate | the protocol returns **not a distinct operation candidate** | the protocol returns **distinct operation candidate** → the individuation is **too fine**; the fineness bound of `METHOD_INDIVIDUATION_PROTOCOL_v0_1` §4.6 is breached |
| **Control B** | `¬C5_op ∧ ¬Inst` | the protocol returns **distinct operation candidate**, *and* H/N/S evidence independently shows `¬Inst` | the protocol returns **not a distinct operation candidate** → the individuation is **too coarse**. If instead `Inst` holds, the case was **mis-selected** under §6 indicators 3–5; that is a selection failure, not a protocol result, and it voids the case rather than the protocol |
| **Both together** | A and B fall on opposite sides of C5-op | opposite sides | same side → the criterion does not discriminate result innovation from local technical innovation, and frozen §12 / §19 *两个控制案例无法区分：停止并重构判据* applies |

If Control A returns *distinct* **and** Control B returns *not distinct*, both bounds are breached in opposite directions and the individuation protocol is falsified outright.

**Response to falsification is fixed in advance.** Per `METHOD_INDIVIDUATION_PROTOCOL_v0_1` §8, that file may not be edited in response to these outcomes. A falsifying result is recorded, and any replacement rule is issued as a separately versioned **v0.2** with its own preregistration and freeze. This protocol is likewise not to be amended in response to what the controls turn out to be; a defect in the selection procedure is answered by a versioned successor, disclosed as such.

## 10. If no admissible control exists

A recorded, reportable outcome — not a reason to relax §5–§7.

If enumeration yields no admissible candidate for either control, the finding is that the stated source scope contains no clean control. Frozen §7.7 then applies directly: *"没有两个控制案例，不进入投稿稿阶段"* — without two controls, the work does not proceed to the submission draft.

The permitted response is a **new version of this protocol** widening the source scope, with the widening justified on archive grounds and preregistered before re-enumeration. The prohibited responses are loosening the criteria in place, weakening an exclusion to admit a known candidate, or proceeding with one control.

## 11. Interlock with the individuation protocol

Both files are frozen for the same round and neither may be repaired using the other's outputs.

- `METHOD_INDIVIDUATION_PROTOCOL_v0_1` supplies the **verdict** (its §4 tests) and the prohibition on outcome-driven revision (its §8).
- This file supplies the **selection**, and guarantees that selection did not anticipate the verdict (§3).
- Its §6.1 prohibition on treating calibration success as evidence for the individuation is reinforced here at the selection stage by §7.2.
- Neither file's freeze is lifted by the other's outcome.

**No D06 institutionalization verdict may be finalized** before the controls are selected under this protocol and the calibration outcome recorded — frozen §19(6) makes triple calibration a submission condition, and Control B's `¬Inst` finding shares the H/N/S evidence base D06 will use.

## 12. Freeze status

**This protocol is frozen on merge**, covering the scope listed in §0. The freeze takes effect **before enumeration**, which is the entire point: a selection procedure written after the candidates are known cannot demonstrate that it did not follow them.

Editorial corrections that do not touch the frozen scope require a dated **non-substantive erratum record** stating what changed and why the frozen scope is untouched. An unrecorded edit to a frozen file is a violation regardless of size.

Freezing is procedural. It fixes the procedure against outcome-driven revision; it does not make the procedure correct, and it is not independent validation. The epistemic status remains **procedure candidate**.

Nothing in this file establishes that forcing was novel, important, inheritable, non-local, scaffold-forming or institutionalized, and nothing in it selects a case. It fixes only how the two control cases must be found.
