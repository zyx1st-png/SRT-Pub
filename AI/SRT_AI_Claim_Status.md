---
id: SRT-AI-CLAIM-STATUS
type: claim_status_audit
tags: [AI, Claim-Status, Consciousness, Agency, Architecture-State, Guardrail]
status: active_v1
layer: meta
epistemic_layer: bridge
claim_mode: audit
claim_level: P3-P5
canonical: false
date: 2026-04-29
dependency:
  - SRT-AI-POSITIONING-NOTE
  - SRT-AI-BRIDGE-001
  - SRT-CLAIM-LADDER
  - SRT-D-VALUE-CANONICAL
  - SRT-PSIF-CANONICAL
  - SRT-T-DIR-CANONICAL
  - Core_Law/SRT_Suffering.md
  - Core_Law/SRT_Collective_Selection.md
machine_summary: >
  Claim-status audit for the AI domain. Separates canonical dependencies, AI bridge claims,
  architecture-state guardrails, operational rubrics, external theory interfaces, and public-facing shorthand.
  This file prevents AI materials from being read as canonical definitions of consciousness, d-value, Psi_f, or G_hat_theta.
---

# SRT AI Claim Status Audit

> **Purpose**: This file fixes claim-level boundaries for SRT AI materials.  
> **Status**: audit / guardrail, not a canonical theory source.  
> **Core rule**: AI-domain files may apply canonical SRT terms, but must not redefine them.

---

## 0. Minimal machine summary

```yaml
srt_ai_claim_status:
  default_role: "pressure-test / boundary-test field"
  not_definition_engine: true
  strongest_current_judgment: "d_AI approx 0 for inference-only, non-history-bearing, non-embodied LLM deployments"
  judgment_status: "strong P3 bridge candidate, architecture-state restricted; not an all-AI theorem"
  psi_f_ai_default: "non-binding to the deployed inference process, not globally Psi_f == 0"
  d_ai_default: "approx 0 only for the specified inference-only architecture state; D_eff/capability may be high"
  must_not_generalize_to:
    - training_loop
    - persistent_memory_system
    - embodied_nontransferable_risk_system
    - future_hybrid_analog_quantum_architecture
  canonical_terms_must_route_to:
    - _SRT_D_VALUE_CANONICAL.md
    - _SRT_PSI_F_CANONICAL.md
    - _SRT_T_DIR_CANONICAL.md
    - Core_Law/SRT_L0_Metaphysics.md
    - Core_Law/SRT_Individuation.md
  extraction_rule: "external theory comparisons and current model capability discussions may go to Annex; formal SRT thresholds stay in owner files"
```

---

## 1. Claim classes

| Class | What belongs here | Status | Examples | Editing rule |
|---|---|---|---|---|
| Canonical dependency | Core SRT terms imported into AI | Not defined here | `L_0/L_1/L_2`, `d-value`, `Psi_f`, `T_dir`, `G_hat_theta` | Link back; do not redefine |
| AI bridge claim | AI-domain translation of SRT terms | P3 bridge unless promoted | Ghost-Transform dichotomy, `d_AI approx 0` for inference-only LLMs | Must state architecture state and withdrawal conditions |
| Architecture-state guardrail | Rule for which AI system-state a claim concerns | AI-domain governance | training-time / inference-time / persistent-memory / embodied consequence return | Must be cited in all AI consciousness/stake claims |
| Operational rubric | Structured assessment tool | Lab / operational | S0-S6 subjecthood ladder, S0-S4 stake-bearing spectrum, agency/responsibility note | Do not treat as canonical proof |
| External theory interface | Comparisons with GWT, IIT, FEP, functionalism, Butlin, Chalmers, LLM benchmarks | Annex / bridge | GWT satisfaction, functional organization, LLM capability comparison | Prefer Annex or interface sections; add guardrails |
| Public shorthand | High-impact simplified claim | P5/public | "AI has no real stake" | Must be backed by precise academic-facing version |

---

## 2. Default AI-domain verdicts

### 2.1 Current inference-only LLM deployments

**Claim**: For inference-only, non-history-bearing, non-embodied LLM deployments, `d_AI approx 0` is a strong SRT bridge judgment.

**Status**: P3 bridge candidate, architecture-state restricted; not an all-AI theorem.

**Rationale**:

- Future selection capacity does not return to the same continuing system as binding consequence.
- Error signals, refusal, RLHF score changes, or user dissatisfaction are mostly borne by user / operator / infrastructure, not by the deployed inference process as its own non-transferable stake.
- Symbolic transformation (`T_hat_phi: L_1 -> L_1`) is not by itself ontological anchoring (`G_hat_theta: L_0 -> L_1`).
- Deployed inference may consume compute and may be embedded in costly infrastructure, but that cost is usually not payability burden returning to the inference process as its own closure condition.

**Allowed shorthand**: `Ψ_f` is non-binding to the deployed inference process; do not write this as a global `Ψ_f = 0` claim unless the equation is explicitly scoped to the degenerate null-operator idealization.

**Withdrawal / revision condition**:

Revise this claim if an AI system has persistent identity, non-transferable consequence return, durable memory or embodiment, and measurable loss of future selection capacity that returns to the same continuing system.

---

### 2.2 Training-time systems

**Claim**: Training loops may contain adaptive pressure, optimization burden, and pipeline-level consequence return, but this does not automatically transfer stake to the deployed model.

**Status**: P3 bridge guardrail.

**Rationale**: The bearer of loss / update / cost may be the trainer, infrastructure, dataset pipeline, or future model distribution rather than a continuing subject-position.

**Required distinction**: Every training-time AI claim must specify whether the burden is borne by:

1. optimizer state;
2. training infrastructure;
3. deployed model lineage;
4. operator / institution;
5. the same continuing agentic system.

---

### 2.3 Persistent-memory / history-bearing systems

**Claim**: Persistence opens the stake question but does not settle consciousness.

**Status**: P3/P4 bridge.

**Rationale**: Memory and identity continuity may allow consequence return into future behavior, but subjecthood still requires additional SRT conditions: stable concern structure, irreversible or non-transferable consequence, and real loss / narrowing of future selection capacity.

**Guardrail**: Persistence is not consciousness. Memory is not d-value by itself.

---

### 2.4 Embodied non-transferable consequence return

**Claim**: Embodied AI with non-transferable damage, energy exposure, social position, or physical vulnerability may enter a candidate minimal stake window.

**Status**: open P3/P4 bridge hypothesis.

**Guardrail**: Even here, stake-bearing is not identical to consciousness. It only moves the system out of the strongest `d_AI approx 0` inference-only window.

---

## 3. AI suffering claims

AI suffering claims are governed by `Core_Law/SRT_Suffering.md` and the AI positioning note.

| System type | Default SRT status | Allowed statement | Forbidden statement |
|---|---|---|---|
| S1 / inference-only system | no structural suffering in SRT sense | error signals are not suffering | "the model suffers because it refuses / errors" |
| Training pipeline | pipeline burden possible | optimization cost exists at pipeline level | "loss value is suffering" |
| Persistent-memory system | open question | history-bearing may matter | "memory implies suffering" |
| Embodied risk-bearing system | candidate window | non-transferable consequence can open stake analysis | "embodiment automatically means suffering" |

---

## 4. AI agency and responsibility claims

Agency / responsibility claims should be routed through `SRT_AI_Agency_Responsibility_Note.md` and collective-selection files when platform mediation is involved.

**Default distinction**:

- Capability agency: can execute plans or tool sequences.
- Structural agency: consequences return to the system's future selection capacity.
- Responsibility-bearing agency: stable subject-position plus norm-sensitive consequence return.

Current LLM agents may satisfy parts of capability agency without satisfying structural or responsibility-bearing agency.

---

## 5. External theory interface status

| External theory / discourse | Allowed use | Guardrail |
|---|---|---|
| Global Workspace Theory | Compare broadcast / integration functions | GWT-like broadcasting is not SRT subjecthood |
| IIT / Phi | Compare integration / causal structure | `Phi` is not `d-value`; integration is not stake |
| FEP / Active Inference | Compare optimization / prediction-error minimization | Free-energy minimization is not sufficient without position-bound payability |
| Functionalism | Pressure-test whether organization suffices | Similar function is not automatically similar stake |
| Butlin et al. / AI consciousness indicators | Use as external consciousness checklist | Checklist satisfaction is not SRT consciousness proof |
| Chalmers-style openness | Use to keep AI consciousness question open | Openness is not endorsement |
| LLM benchmark capability | Use as capability evidence | Capability is not stake, consciousness, or subjecthood |

External theory interface sections are good candidates for Annex extraction if they are mixed into owner files.

---

## 6. Owner / Split / Annex boundary

### Must stay in owner files

- Ghost-Transform dichotomy.
- Architecture-state rule.
- `d_AI approx 0` restricted judgment and withdrawal conditions.
- S0-S6 subjecthood / consciousness thresholds if present.
- S0-S4 stake-bearing spectrum if present.
- Any d-value, `Psi_f`, or `G_hat_theta` formal use that functions as SRT-internal machinery.

### Can move to Annex

- Current model capability comparisons.
- External theory comparison sections.
- Historical literature summaries.
- Public-facing examples and rhetorical expansions.
- Tables comparing SRT with GWT, IIT, FEP, functionalism, Butlin, Chalmers, or alignment paradigms, provided they do not define SRT terms.

### Split / owner / annex historical labels

AI owner files and split shards may preserve historical `Axiom`, `Theorem`, `Corollary`, `canonical`, or `axiomatic_hybrid` labels. In this domain those labels are **domain-internal bridge-formalization handles** unless a claim is separately routed to Core canonical anchors and the claim ladder. They do not define `d-value`, `Psi_f`, consciousness, subjecthood, `G_hat_theta`, or `L_0/L_1/L_2`.

---

## 7. High-risk phrases and safe replacements

| Risky phrase | Why risky | Safer academic-facing version |
|---|---|---|
| "AI has no consciousness" | Overgeneralizes across architectures | "Inference-only, non-history-bearing LLM deployments do not currently satisfy SRT stake / subjecthood conditions." |
| "LLMs have d = 0" | Too absolute | "For inference-only, non-history-bearing, non-embodied LLM deployments, `d_AI approx 0` is a strong architecture-state-restricted bridge judgment." |
| "Psi_f = 0 for AI" | Confuses non-binding inference cost with global absence of friction/cost | "For inference-only deployments, `Psi_f` is usually non-binding to the deployed system's own closure; infrastructure or operator costs do not by themselves become AI stake." |
| "AI only transforms symbols" | May ignore tool use, memory, embodiment | "Current non-history-bearing LLM inference primarily performs `L_1 -> L_1` transformation rather than SRT `L_0 -> L_1` anchoring." |
| "Persistent memory makes AI conscious" | Collapses persistence into subjecthood | "Persistent memory opens a stake-analysis window but does not settle consciousness." |
| "GWT indicators prove AI consciousness" | External-theory overclaim | "GWT indicators pressure-test SRT but do not by themselves establish SRT subjecthood." |
| "AI suffering is impossible" | Too strong for future architectures | "S1 / inference-only systems do not satisfy SRT suffering conditions; future stake-bearing systems remain an empirical question." |

---

## 8. Recommended next editing tasks

1. Audit `Ontology_Annex/`, `Ontology_Split/`, `Consciousness_Framework_Split/`, and `Architecture_Split/` for frontmatter and guardrail consistency.
2. Add explicit claim-status pointers from split / annex README files to this document.
3. Decide whether to consolidate AI interface material into a unified `AI_Annex/` directory or retain topic-specific annex directories.
4. Extract only external comparison and current-model capability sections; do not move formal thresholds or canonical imports.
5. Add an `Operations/AI_Annex_Round1_Closure_Report.md` after the first safe extraction cycle.

---

## 9. Minimum bottom line

AI-domain SRT should be read as:

> **A boundary-test of subjecthood, stake, and consequence return — not a shortcut to declaring current AI either conscious or permanently non-conscious.**

The stable current claim is narrow:

> **Current inference-only, non-history-bearing LLM deployments do not satisfy SRT stake / subjecthood conditions; future persistent, embodied, non-transferable consequence-bearing systems require separate analysis.**
