---
id: SRT-AI-README
type: directory_entry
tags: [AI, Consciousness, Agency, Boundary-Test, Navigation]
status: active_v1
layer: meta
epistemic_layer: bridge
claim_mode: navigation
canonical: false
dependency:
  - SRT-AI-POSITIONING-NOTE
  - SRT-AI-BRIDGE-001
  - SRT-AI-CLAIM-STATUS
  - SRT-D-VALUE-CANONICAL
  - SRT-PSIF-CANONICAL
  - SRT-CLAIM-LADDER
---

# AI

This directory contains SRT's AI-facing bridge, consciousness, agency, architecture, and operational evaluation materials.

AI is a **pressure-test / boundary-test field** for SRT, not the theory's definition engine. AI-domain files must not redefine `L_0/L_1/L_2`, `d-value`, `Psi_f`, `T_dir`, or `G_hat_theta`; they route those terms back to canonical anchors.

## Read order

1. [`AI_POSITIONING_NOTE.md`](AI_POSITIONING_NOTE.md)  
   Architecture-state guardrail for all AI claims. Use this first when evaluating `d_AI`, AI stake, AI suffering, or AI subjecthood.

2. [`SRT_AI_Claim_Status.md`](SRT_AI_Claim_Status.md)  
   Claim-status audit for AI-domain materials. Use this to distinguish canonical dependencies, AI bridge claims, operational rubrics, external theory interfaces, and public-facing shorthand.

3. [`_SRT_AI_Bridge.md`](_SRT_AI_Bridge.md)  
   Main AI bridge layer. Contains the Ghost-Transform dichotomy, Pour-El/Richards boundary note, and AI-domain formal translation claims. Treat Axiom/Theorem labels here as bridge-formalization devices unless separately promoted.

4. [`SRT_AI_01_Ontology_CompactCore.md`](SRT_AI_01_Ontology_CompactCore.md)  
   Compact AI ontology entry.

5. [`SRT_AI_03_Consciousness_Framework_CompactCore.md`](SRT_AI_03_Consciousness_Framework_CompactCore.md)  
   Compact AI consciousness framework. Use with `AI_POSITIONING_NOTE.md` and the claim-status audit before making AI consciousness claims.

6. [`SRT_AI_Consciousness_Evaluation_Rubric.md`](SRT_AI_Consciousness_Evaluation_Rubric.md)  
   Operational evaluation rubric. It is a structured assessment tool, not a canonical consciousness definition source.

7. [`SRT_AI_Agency_Responsibility_Note.md`](SRT_AI_Agency_Responsibility_Note.md)  
   Operational agency / responsibility note. Use for responsibility gradients and governance-facing distinctions.

## Status distinction

- `AI_POSITIONING_NOTE.md`: AI-domain guardrail and architecture-state rule. It governs usage but does not settle AI consciousness.
- `_SRT_AI_Bridge.md`: bridge-layer foundation for AI. It should not be split into Annex unless a separate adjudication decides otherwise.
- CompactCore files: concise current summaries, not replacements for canonical anchors.
- Full owner files (`SRT_AI_01_Ontology.md`, `SRT_AI_03_Consciousness_Framework.md`, `SRT_AI_Architecture.md`) preserve long-form arguments and should be edited cautiously.
- Split directories (`Ontology_Split/`, `Consciousness_Framework_Split/`, `Architecture_Split/`) are long-form reading aids; they do not create new authority layers.
- Annex directories (`Ontology_Annex/` and any future `AI_Annex/`) are interface / comparison layers; they are `canonical: false` unless explicitly promoted through governance.

## Architecture-state rule

Any sentence about AI `d-value`, AI burden, AI subjectivity, AI suffering, or AI friction must state which architecture state is being discussed:

| State | Minimal meaning | Default caution |
|---|---|---|
| training-time | loss, gradients, optimizer updates, trainer / infrastructure loop | feedback may belong to the pipeline rather than the deployed model |
| inference-time | bounded prompt / response or tool-use run under fixed weights | `d_AI approx 0` is strongest here when no binding consequence returns to the system |
| persistent-memory / history-bearing deployment | future behavior depends on retained memory, identity state, or account / body history | opens the stake question but does not by itself imply consciousness |
| embodied non-transferable consequence return | damage, energy, exposure, spatial or social position returns to the same continuing system | candidate minimal stake window; still not a consciousness verdict |

## Guardrails

- Do not collapse competence into stake.
- Do not collapse persistence into consciousness.
- Do not collapse tool use into `G_hat_theta` anchoring.
- Do not treat current LLM capability comparisons as SRT endorsement of AI consciousness.
- Do not treat `d_AI approx 0` as a species-level verdict across all possible AI architectures; it is strongest for inference-only / non-history-bearing deployments.
- Do not move S0-S6 subjecthood thresholds, d-value definitions, or `Psi_f` definitions into Annex files.

## Current restructuring status

The AI directory already has partial split / annex structure:

- [`Ontology_Annex/`](Ontology_Annex/) — historical interface batches for AI ontology; claim status must be read through `AI_POSITIONING_NOTE.md` and `SRT_AI_Claim_Status.md`.
- [`Ontology_Split/`](Ontology_Split/) — long-form split of `SRT_AI_01_Ontology.md`; reading aid only.
- [`Consciousness_Framework_Split/`](Consciousness_Framework_Split/) — long-form split of `SRT_AI_03_Consciousness_Framework.md`; reading aid only.
- [`Architecture_Split/`](Architecture_Split/) — long-form split of `SRT_AI_Architecture.md`; reading aid only.

Before any new AI extraction PR, run an audit of these existing split / annex directories to avoid duplicate interface files and to verify frontmatter / guardrails.

## Recommended next cycle

1. Audit existing AI split / annex directories.
2. Normalize frontmatter and guardrails in split / annex indexes.
3. Decide whether to create a unified `AI_Annex/` or keep topic-specific Annex directories.
4. Extract only external theory comparisons and LLM capability comparisons; keep SRT formal thresholds and architecture-state claims in owner files.
5. Close the cycle with an `Operations/AI_Annex_Round1_Closure_Report.md`.
