---
hook_id: HOOK-PHIL-PH-CONSC03-SUBJECTIVITY-DECOMPOSITION
patch_id: PATCH-PHIL-PH-CONSC03-SUBJECTIVITY-DECOMPOSITION
domain: philosophy_of_mind
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: integration_hook
id: HOOK-PHIL-PH-CONSC03-SUBJECTIVITY-DECOMPOSITION
status: active
integration_status: pending
landing_ledger:
  - target: "Philosophy/SRT_HardProblem_Epistemology.md"
    state: pending
    blocked_by: "需要在现有 hard-problem dissolution 后加入四问题拆分，并保持 phenomenality residual open；属于 B 类哲学接口编辑"
  - target: "Philosophy/SRT_Subjecthood_Threshold_Interface.md"
    state: pending
    blocked_by: "需要在 unit-binding gate 后加入 Selector / Bearer / Concern Domain / Experiencer 角色分离；属于 B 类接口编辑"
  - target: "Philosophy/SRT_Consciousness_Conditions.md"
    state: pending
    blocked_by: "需要修正 legacy 'd = alignment depth' 表述并澄清 bearing 不自动推出 phenomenality；不得改 canonical d"
---

# Integration Hook: PH-CONSC03 Subjectivity Decomposition

## Target 1 — hard-problem epistemology

```text
Philosophy/SRT_HardProblem_Epistemology.md
```

Suggested landing after the current perspectival-gap / dissolution chain:

```text
Hard problem -> four separable problems:
A. Perspective
B. Bearer
C. Ownership / feeling
D. Qualitative character
```

Required guard:

```text
Rovelli strongly pressures A;
A's dissolution does not close B-D.
```

Suggested native paragraph:

> The first/third-person contrast should not be treated as one homogeneous explanatory gap. A perspectival difference can be naturalized without yet explaining what makes a perspective bearer-centered, what produces ownership or feeling, or why a phenomenal state has one qualitative character rather than another. SRT should therefore treat the hard problem as a decomposition problem rather than claim a single completed dissolution.

## Target 2 — subjecthood threshold interface

```text
Philosophy/SRT_Subjecthood_Threshold_Interface.md
```

Suggested insertion immediately after the unit-binding gate:

```text
Selector != Bearer != Concern Domain != Experiencer
```

Suggested table columns:

```text
role | diagnostic question | failure mode
```

Required sub-guard:

```text
B != C_B
```

where `B` is the candidate bearer closure and `C_B` is the concern domain whose irreversible changes enter stake-coupled evaluation.

## Target 3 — consciousness conditions compatibility repair

```text
Philosophy/SRT_Consciousness_Conditions.md
```

Required repair only:

1. defer every `d = alignment depth` reading to `_SRT_D_VALUE_CANONICAL.md`;
2. do not treat `d >= d_min` as a phenomenality proof;
3. do not treat bearing as an automatic synonym for experiencer status;
4. preserve the file's own `strongest candidate window` epistemic caution.

## Do not include

- Do not promote PH-CONSC03 into a canonical consciousness definition.
- Do not rewrite `_SRT_D_VALUE_CANONICAL.md`.
- Do not claim enactivism lacks stake, vulnerability, or intrinsic normativity.
- Do not claim Damasio is merely a biological implementation of an already-complete SRT theory.
- Do not convert future-selectability rewrite into a consciousness scalar.
- Do not treat cells as conscious merely because they satisfy a bearer test.

## Future empirical pressure

A useful later discrimination study should attempt to match systems for autonomy, viability regulation, adaptive feedback, and information-processing capacity while varying:

```text
same-bearer consequence return
non-outsourcing
history-bearing writeback
future-selectability rewrite
```

If these variables fail to add independent discrimination, the SRT vocabulary should be translated downward rather than protected by definition.
