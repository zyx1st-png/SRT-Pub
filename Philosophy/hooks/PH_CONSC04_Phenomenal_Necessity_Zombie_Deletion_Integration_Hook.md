---
id: HOOK-PH-CONSC04-PHENOMENAL-NECESSITY-ZOMBIE-DELETION
type: integration_hook
status: active
record_stage: pending
integration_status: partial
canonical: false
layer: operations
epistemic_layer: bridge
claim_mode: integration_plan
updated: 2026-08-16
source_patch: Philosophy/patches/SRT_Philosophy_PH_CONSC04_Phenomenal_Necessity_Zombie_Deletion_Test_v0_1.md
source_ids:
  - SRC-2026-08-08-PHIL-LEWIS-MIND-FROM-MINDLESS-MATTER
target_documents:
  - Philosophy/SRT_HardProblem_Epistemology.md
  - Philosophy/SRT_Subjecthood_Threshold_Interface.md
  - Core/SRT_OPEN_TENSIONS.md
  - Core_Law/SRT_Individuation.md
  - AI/AI_POSITIONING_NOTE.md
landing_ledger:
  - target: "Philosophy/SRT_HardProblem_Epistemology.md"
    state: landed
    anchor: "### 3.2 承担与第一人称在场：构成性候选，而非已闭合定理"
  - target: "Philosophy/SRT_Subjecthood_Threshold_Interface.md"
    state: pending
    blocked_by: "Future subjecthood synthesis should preserve subject-position admission != phenomenal-necessity verdict and keep phenomenality separately assessed."
  - target: "Core/SRT_OPEN_TENSIONS.md"
    state: landed
    anchor: "### Status Update (2026-08-11: phenomenality and adjacent-case guards)"
  - target: "Core_Law/SRT_Individuation.md"
    state: landed
    anchor: "8. **主体位进入就证明了现象性**"
  - target: "AI/AI_POSITIONING_NOTE.md"
    state: pending
    blocked_by: "Future AI synthesis may use Z4/Z6 as complementary report/self-model versus non-transferable-bearing controls; no consciousness verdict follows automatically."
---

# PH-CONSC04 Integration Hook — Phenomenal Necessity / Zombie Deletion

## Purpose

Carry the PH-CONSC04 result into later hard-problem / subjecthood synthesis without turning a secondary source or a bridge thought experiment into canonical proof.

**2026-08-16 landing update:** the author selected **HP-B-B**. `Philosophy/SRT_HardProblem_Epistemology.md` now explicitly separates structural bearing from phenomenal bearing and keeps Z6 open. This hook remains `partial` because subjecthood and AI targets are still pending.

## Core de-materialized payload

```text
Perspective-center individuation
!=
phenomenal necessity.

SRT currently has substantial structure for the first problem and a strong constitutive proposal for the second, but the implication from structural bearing / Stable-ISP-compatible subject-position to phenomenal presence must remain open until it survives a non-circular zombie/deletion test.
```

## Target 1 — `Philosophy/SRT_HardProblem_Epistemology.md`

**Landed 2026-08-16 under HP-B-B.** The owner now:

1. splits HP-A perspective-center individuation from HP-B phenomenal necessity;
2. preserves the view-from-nowhere / re-objectification guard;
3. writes:

```text
B_s = structural bearing candidate
B_p = phenomenal bearing candidate

B_s != B_p
B_s -> B_p  ?
```

4. keeps Z6 open rather than defining phenomenality into bearing;
5. treats the qualitative-character formula as a conditional P3 structural anchor rather than a completed derivation.

Author decision record:

`Operations/SRT_PHENOMENAL_NECESSITY_AUTHOR_DECISION_PACKET_2026-08-16.md`

## Target 2 — `Philosophy/SRT_Subjecthood_Threshold_Interface.md`

Add a bounded distinction:

```text
subject-position admission
!=
phenomenal-necessity verdict
```

Use the following audit sequence:

```text
candidate unit
-> consequence-return closure
-> stake / concern
-> history writeback
-> integration / counterfactuality
-> continuity / reselection
-> subject-position candidate
-> phenomenality remains separately assessed
```

## Target 3 — `Core/SRT_OPEN_TENSIONS.md`

Recommended future open-pressure entry:

**Phenomenal necessity / SRT-zombie**

- stabilized: perspective access is not a view-from-nowhere gap; Stable ISP and individuation provide a subject-position architecture; bearing candidates can be specified without phenomenal vocabulary;
- unresolved: whether a fully individuated, non-substitutable, stake-bearing Stable-ISP-like perspective center can coherently be phenomenally empty;
- do not overstate: `bearing`, `d > 0`, same-bearer consequence return or Stable ISP are not currently canonical proofs of qualia.

This target is already landed and remains compatible with HP-B-B.

## Target 4 — `Core_Law/SRT_Individuation.md`

Preserve the two-transition architecture:

```text
subject-position entry
-> later reflective self-consciousness condensation
```

Add only a guardrail that individuation dynamics answer primarily HP-A and do not automatically close HP-B.

This target is already landed.

## Target 5 — `AI/AI_POSITIONING_NOTE.md`

Use two complementary controls:

```text
Z4: rich self-report / self-model / global access but externally borne or transferable consequence
Z6: genuine non-transferable same-bearer stake + history + Stable-ISP-like continuity, with phenomenality left open
```

This prevents both:

```text
behavior/report inflation
and
bearing inflation
```

## UAL placement

UAL should enter only as a P3/P4 bridge candidate for:

```text
history-sensitive flexible alternative evaluation
```

not as a consciousness definition.

## Forbidden integration

Do not use this hook to write:

```text
Lewis proves SRT
UAL proves consciousness
life is phenomenally subjective by boundary alone
Stable ISP = consciousness
structural bearing = phenomenal bearing by definition
SRT has solved the hard problem
```

## Exit condition

This hook can be marked fully integrated only when the remaining target surfaces preserve the HP-A / HP-B distinction and record the Z6 phenomenal-necessity pressure rather than silently closing it.