---
id: SRT-PHIL-PH-SS-OBJECTION-CROSSWALK-2026-04-27
type: objection_crosswalk
tags:
  - Philosophy
  - Objection-Led-Hardening
  - Soft-Spots
  - PH-SS
  - Machine-Readable
status: active_bridge_hardening
layer: L1-L2-bridge
epistemic_layer: bridge
claim_mode: guide
claim_level: P3-P5
canonical: false
priority: high
visibility: read_after_00
date: 2026-04-27
dependency:
  - SRT-PHIL-HARDENING-SOFT-SPOTS-2026-04-27
  - SRT-PHIL-OBJECTION-LEDGER
  - SRT-PHIL-HARDENING-TODO
  - SRT-CLAIM-LADDER
machine_summary: >
  Crosswalk from PH-SS-01..PH-SS-12 philosophy soft spots to objection families,
  strongest attacks, required responses, withdrawal conditions, and target files.
  Use this file when upgrading any philosophy claim or assigning hardening work.
---

# 01 — PH-SS Objection Crosswalk

> **用途**：把 `00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md` 中的 12 个软点接入 objection-led hardening。  
> **规则**：每个哲学升级都应说明它处理哪个 `PH-SS`，触发哪个 objection，失败时如何收缩。

---

## 0. Machine routing table

```yaml
philosophy_soft_spot_routing:
  PH-SS-01:
    label: "L0 ontology ambiguity"
    objection_family: ["modal realism", "hidden-world metaphysics", "mystical potentiality"]
    existing_objections: ["O-Phil-2", "O-Phil-10"]
    target_files: ["Core_Law/SRT_L0_Metaphysics.md", "Philosophy/_SRT_Phil_Axioms.md", "Philosophy/SRT_Philosophy_Foundations_CompactCore.md"]
  PH-SS-02:
    label: "selection-before-existence misread as temporal priority"
    objection_family: ["circularity", "subject-before-world", "idealism"]
    existing_objections: ["O-Phil-2"]
    target_files: ["Philosophy/SRT_Philosophy_Foundations.md", "Philosophy/_SRT_Phil_Axioms.md"]
  PH-SS-03:
    label: "L1 and reality strength"
    objection_family: ["hallucination flattening", "physicalist reduction", "truth-confusion"]
    existing_objections: ["O-Phil-1", "O-Phil-2"]
    target_files: ["Philosophy/SRT_Philosophy_Foundations_CompactCore.md", "Philosophy/SRT_Philosophy_Foundations.md"]
  PH-SS-04:
    label: "subjective idealism risk"
    objection_family: ["mind creates reality"]
    existing_objections: ["O-Phil-2"]
    target_files: ["Philosophy/README.md", "Philosophy/SRT_Philosophy_Foundations_CompactCore.md"]
  PH-SS-05:
    label: "Psi_f layer confusion"
    objection_family: ["mathematical metaphor", "conceptual equivocation"]
    existing_objections: ["O-Phil-2", "O-Phil-10"]
    target_files: ["_SRT_PSI_F_CANONICAL.md", "Philosophy/_SRT_Phil_Axioms.md", "Philosophy/SRT_Philosophy_Hardening_TODO.md"]
  PH-SS-06:
    label: "stabilization to value jump"
    objection_family: ["is-ought gap", "power legitimation"]
    existing_objections: ["O-Phil-7", "O-Phil-8"]
    target_files: ["Philosophy/SRT_Philosophy_Ethics.md", "Philosophy/SRT_Ethics_Agency.md", "Philosophy/SRT_Political_Philosophy.md"]
  PH-SS-07:
    label: "mystical teleology risk"
    objection_family: ["cosmic purpose", "unearned teleology"]
    existing_objections: ["O-Phil-7", "O-Phil-10"]
    target_files: ["Core/SRT_Core_24_Floor_Normativity_Verification.md", "Philosophy/SRT_Philosophy_Foundations.md"]
  PH-SS-08:
    label: "d-value philosophical status"
    objection_family: ["subjective preference", "affective intensity", "measurement ambiguity"]
    existing_objections: ["O-Phil-7", "O-Phil-9", "O-Phil-10"]
    target_files: ["_SRT_D_VALUE_CANONICAL.md", "Philosophy/SRT_Philosophy_Foundations_CompactCore.md"]
  PH-SS-09:
    label: "social ontology underdeveloped"
    objection_family: ["individualism", "mere social construction", "institutional reification"]
    existing_objections: ["O-Phil-7", "O-Phil-8"]
    target_files: ["Philosophy/SRT_Social_Economics_CompactCore.md", "Philosophy/SRT_Political_Philosophy.md", "Core_Law/SRT_Collective_Selection.md"]
  PH-SS-10:
    label: "consciousness threshold"
    objection_family: ["panpsychism", "combination problem", "AI over-attribution"]
    existing_objections: ["O-Phil-3", "O-Phil-9"]
    target_files: ["Philosophy/SRT_Philosophy_Foundations_CompactCore.md", "AI/SRT_AI_03_Consciousness_Framework_CompactCore.md", "Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md"]
  PH-SS-11:
    label: "non-reductive validation"
    objection_family: ["unfalsifiability", "grand synthesis", "no direct measurement"]
    existing_objections: ["O-Phil-9", "O-Phil-10"]
    target_files: ["Core/SRT_Core_24_Floor_Normativity_Verification.md", "Governance/SRT_CLAIM_LADDER.md"]
  PH-SS-12:
    label: "anti-relativism"
    objection_family: ["anything goes", "truth by power", "projection equivalence"]
    existing_objections: ["O-Phil-2", "O-Phil-7", "O-Phil-8"]
    target_files: ["Philosophy/README.md", "Philosophy/SRT_Philosophy_Foundations_CompactCore.md", "Philosophy/SRT_Political_Philosophy.md"]
```

---

## 1. Crosswalk table

| PH-SS | Soft point | Strongest objection | Required SRT response | Withdrawal / narrowing condition |
|---|---|---|---|---|
| **PH-SS-01** | `L_0` 的本体论地位 | `L_0` sounds like a hidden realm, modal realism, or mystical potentiality. | Define `L_0` as **modal field of selectability / condition of possible manifestation**, not an object-like world. | If `L_0` is treated as an already-populated object inventory, downgrade to metaphor or relocate to Core_Law with stricter semantics. |
| **PH-SS-02** | “选择先于存在” | The claim is circular: a selector must exist before it selects. | State that priority is **manifestational / logical / generative**, not temporal. | If readers require temporal creation language, rewrite as “determinacy requires selection” rather than “selection comes first in time.” |
| **PH-SS-03** | `L_1` 与现实强度 | SRT flattens hallucination, dream, physical object, and institution into one vague “manifest reality.” | Use **reality-strength ladder**: local manifestation, stabilized reality, cross-operator reality, canonical physical reality. | If no stability / alignment tests are supplied, restrict to E1 local manifestation only. |
| **PH-SS-04** | 主观唯心论风险 | Selection-first means mind creates reality. | Pair every selection claim with `Psi_f` resistance and `theta` as constraint-composite. | If `Psi_f` cannot be separated from subjective confidence, weaken anti-idealist claims. |
| **PH-SS-05** | `Psi_f` 混层 | `Psi_f` slides between metaphysical cost, information geometry, embodiment, and normativity. | Type it as `Psi_f^ont`, `Psi_f^inf`, `Psi_f^emb`, `Psi_f^norm`; Fisher metric is one information-geometric section. | If a file cannot specify the intended layer, rewrite the passage as provisional analogy. |
| **PH-SS-06** | 稳定化到价值/规范跳跃 | SRT commits the is-ought fallacy; stable oppression becomes “good.” | Separate descriptive norm, functional norm, and evaluative legitimacy. | If legitimacy conditions are absent, ethics must remain descriptive social ontology. |
| **PH-SS-07** | 目的论风险 | SRT smuggles in mystical cosmic purpose. | Define purpose as **high-d-value attractor / directionality in selection dynamics**, not a prewritten endpoint. | If no d-value / attractor condition is stated, downgrade “purpose” language to metaphor. |
| **PH-SS-08** | `d-value` 哲学地位 | `d-value` is just subjective preference, emotion, or utility. | Define philosophically as impact of a difference on future selectability, identity continuity, and existential stake. | If operational proxies fail, treat as bridge construct rather than measurement-ready variable. |
| **PH-SS-09** | 社会本体论不足 | Social facts are either individual psychology or arbitrary construction. | Define social reality as **collective L2 sedimentation** through recognition, repetition, enforcement, memory, and symbols. | If collective mechanisms are missing, keep claims at analogy level. |
| **PH-SS-10** | 意识阈值不清 | All selection becomes consciousness; SRT becomes panpsychism. | Require high `d-value`, counterfactual access, identity continuity, memory/L2 closure, and boundary maintenance. | If threshold cannot be operationalized, say SRT reframes, not solves, the combination problem. |
| **PH-SS-11** | 验证观不清 | SRT cannot be falsified because its primitives are hard to measure directly. | Use **non-reductive structural validation**: proxy indicators + cross-domain predictions + theory-differentiating tests. | If no risky differential predictions exist, classify the claim as metaphysical program, not empirical theory. |
| **PH-SS-12** | 相对主义风险 | If reality is selected, truth is just projection or power. | Add anti-relativism constraints: `Psi_f`, embodied limits, environmental feedback, cross-operator checks, historical path-dependence, L2 downward constraint. | If selection standards are absent, restrict claim to phenomenological relativity, not truth. |

---

## 2. Objection families to add or extend in `SRT_Philosophy_Objection_Ledger.md`

The existing ledger already covers many of these objections. Future edits should either add these as new `O-Phil` entries or cross-link them explicitly.

| Proposed ID | Name | Covers |
|---|---|---|
| `O-Phil-11` | L0 hidden-world objection | PH-SS-01 |
| `O-Phil-12` | temporal priority objection | PH-SS-02 |
| `O-Phil-13` | reality-strength flattening objection | PH-SS-03 |
| `O-Phil-14` | Psi_f equivocation objection | PH-SS-05 |
| `O-Phil-15` | mystical teleology objection | PH-SS-07 |
| `O-Phil-16` | d-value preference-reduction objection | PH-SS-08 |
| `O-Phil-17` | social construction / institutional reification objection | PH-SS-09 |
| `O-Phil-18` | consciousness over-attribution objection | PH-SS-10 |
| `O-Phil-19` | non-reductive verification objection | PH-SS-11 |
| `O-Phil-20` | selected-reality relativism objection | PH-SS-12 |

---

## 3. Default response pattern

When adding a philosophy paragraph, use this compact template:

```text
Claim:
PH-SS addressed:
Objection triggered:
Layer: L0 / L1 / L2 / bridge / social L2 / phenomenological
Claim level: P2 / P3 / P4 / P5
Cost / resistance term:
Threshold or stabilization test:
Anti-misreading guardrail:
Withdrawal / narrowing condition:
Target owner file:
```

---

## 4. High-risk phrase linter

| Phrase to flag | Why risky | Safer rewrite |
|---|---|---|
| “consciousness chooses reality” | idealism + panpsychism | “manifest reality is constrained by operator-relative selection under friction” |
| “L0 contains all possible things” | hidden-world / modal realism | “L0 is the modal field of selectability / condition of possible manifestation” |
| “selection comes before existence” | temporal circularity | “selection is manifestationally prior to determinate existence” |
| “value is stabilized selection” | is-ought gap | “some values emerge through stabilized high-d-value selection; legitimacy requires further tests” |
| “purpose is built into the universe” | mystical teleology | “purpose is directionality generated by high-d-value attractor structure” |
| “truth is selected” | relativism | “truth is stabilized alignment under resistance, intervention, and cross-operator correction” |
| “Psi_f is Fisher metric” | layer collapse | “Fisher metric is one information-geometric expression of Psi_f, not the whole concept” |

---

## 5. Compact conclusion

The Philosophy section should now route through three files:

```text
00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md
  -> 01_PH_SS_Objection_Crosswalk.md
    -> 02_PH_SS_Hardening_Execution_Plan.md
```

This creates a readable path for humans and a stable routing path for agents.
