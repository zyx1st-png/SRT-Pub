---
id: SRT-PH-SEM01-INTEGRATION-HOOK
type: integration_hook
layer: bridge
epistemic_layer: bridge
claim_mode: integration
canonical: false
source_patch: SRT-PH-SEM01-BILATERAL-INCOMPATIBILITY-CONTEXT-REPAIR
status: active
integration_status: partial
landing_ledger:
  - target: "Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md"
    state: landed
    anchor: "Bilateral position and context repair"
  - target: "Core_Law/SRT_Occlusion_Dynamics.md"
    state: pending
    blocked_by: "尚未回写；Occlusion_Dynamics 为 draft_v0 canonical-adjacent 主文，须走 SRT_EDIT_PROTOCOL"
  - target: "90_Backstage/Incubation/_SRT_DIRECTION3_CHOICEMAP_PROTOTYPE_SEED.md"
    state: pending
    blocked_by: "目标已停驻（ChoiceMap / IRP 产品线未重启），见 _SRT_PARKED_INDEX.md §1"
  - target: "90_Backstage/Incubation/_SRT_OBJECTHOOD_AS_RESELECTABILITY_META_STANDARD.md"
    state: pending
    blocked_by: "目标已停驻（ChoiceMap / IRP 产品线未重启），见 _SRT_PARKED_INDEX.md §1"
closure_audit: Operations/Audits/Hook_Closure_Audit_2026-07-25.md
---

# PH-SEM01 Bilateral Incompatibility Integration Hook

## 1. Target: ChoiceMap

**Target:** `_SRT_DIRECTION3_CHOICEMAP_PROTOTYPE_SEED.md`

**Insert near:** S1–S4 option structure and reselection safeguards.

**Suggested bridge note:**

A ChoiceMap option should not be treated as a single label. It should separate what the option positively commits the user to, what it explicitly denies, and what it leaves open. Apparent incompatibilities should be typed as strict, defeasible, normative, identity-relative or script-generated. Before a conflict is used to close an option, the system should test whether exception information, time separation, modularity, role differentiation or boundary revision repairs the clash.

**Suggested product fields:**

```text
assertions
denials
left_open
positive_consequences
incompatibility_type
incompatibility_basis
repair_context
revision_authority
```

**Do not include:**

- `not selected = denied`;
- `semantic clash = physical impossibility`;
- automatic ranking by size of incompatibility profile;
- the claim that more context always resolves conflict.

## 2. Target: Occlusion dynamics

**Target:** `Core_Law/SRT_Occlusion_Dynamics.md`

**Insert near:** position-intrinsic versus pathological occlusion, denial mechanism or intervention window.

**Suggested bridge note:**

A possible L2 marker of pathological occlusion is the conversion of a defeasible incompatibility into an allegedly strict and persistent impossibility. The lock becomes self-sealing when exception evidence is excluded, affected parties lose standing to propose repair contexts, and the incompatibility rule itself is shielded from revision. This is a semantic-governance bridge and does not replace the canonical d-threshold dynamics.

**Do not include:**

- `I = occlusion state`;
- incompatibility profile as a d-value measure;
- the claim that all denial is pathological;
- direct import of non-persistence into physical ontology.

## 3. Target: Objecthood as reselectability

**Target:** `_SRT_OBJECTHOOD_AS_RESELECTABILITY_META_STANDARD.md`

**Insert near:** reopening / recomposition / identity-preserving repair.

**Suggested bridge note:**

Reselection need not require returning to the pre-choice state. A closure may reopen through context enrichment: a new distinction, exception, role separation or modular decomposition can permit commitments previously treated as incompatible to coexist while preserving bearer continuity. Such repair must still be audited for real cost, consequence return and whether it expands the reachable set rather than merely redescribing lock-in.

## 4. Target: Future agency / subjecthood synthesis

**Target:** `Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md`

**Suggested placement:** after PH-AG02 structural bias and PH-AG03 constitutive commitment.

**Suggested synthesis sequence:**

```text
available continuations
-> knowledge-shaped structuring bias
-> enacted commitment
-> bilateral position: assertions / denials / open remainder
-> typed incompatibilities and positive consequences
-> responsibility trace and reselection conditions
```

This sequence should preserve:

```text
semantic position
!= controlled selection
!= responsibility-bearing commitment
!= stake-bearing subjecthood
```

## 5. Integration boundary

PH-SEM01 is a P3/P4 formal-semantic bridge. It may structure decision records and diagnose false dilemmas. It must not be used to define SRT primitives or claim that inferential relations constitute all reality.
