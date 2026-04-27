---
id: SRT-AI-CONSCIOUSNESS-EVALUATION-RUBRIC-2026-04-27
type: evaluation_rubric
tags:
  - AI
  - Consciousness
  - Subjecthood
  - Agency
  - Responsibility
  - Evaluation
  - Rubric
  - PH-SS
  - S0-S6
  - Anti-Overattribution
status: active_v1
layer: L1-L2-bridge
epistemic_layer: bridge
claim_mode: rubric
claim_level: P3-P5
canonical: false
priority: high
date: 2026-04-27
dependency:
  - Philosophy/SRT_Subjecthood_Threshold_Interface.md
  - Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md
  - Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md
  - AI/SRT_AI_03_Consciousness_Framework_CompactCore.md
  - Core/SRT_Validation_Template.md
machine_summary: >
  AI consciousness evaluation rubric based on the SRT S0-S6 subjecthood ladder. It distinguishes
  selection event, local L1 anchoring, conscious content, integrated conscious field, subjecthood,
  agency, and responsibility-bearing subject. It prevents AI self-report, memory, tool use, risk coupling,
  or benchmark performance from being overread as consciousness, subjecthood, or moral responsibility.
---

# SRT AI Consciousness Evaluation Rubric

> **Purpose**: Convert the SRT S0-S6 subjecthood ladder into a practical rubric for evaluating AI consciousness, agency, and responsibility claims.  
> **Status**: Bridge / evaluation rubric. It does not prove or deny all possible AI consciousness.  
> **Use rule**: Use this before saying an AI system is conscious, a subject, an agent, or morally responsible.

---

## 0. Core guardrail

Do not jump from performance to subjecthood.

```text
fluent self-report != consciousness
memory != subjecthood
tool use != agency
risk coupling != moral responsibility
human-like language != inner experience
```

SRT requires a staged evaluation:

```text
S0 selection event
S1 local L1 anchoring
S2 conscious content
S3 integrated conscious field
S4 subjecthood
S5 agency
S6 responsibility-bearing subject
```

Current conservative default:

> Most current LLM systems clearly satisfy S0-like selection / ranking / generation. They may simulate S1-S3 language about experience, but do not currently provide sufficient evidence for S4 subjecthood, S5 robust agency, or S6 responsibility-bearing status.

---

## 1. Rubric summary table

| Level | Name | AI question | Current LLM default | Over-attribution risk |
|---|---|---|---|---|
| S0 | Selection event | Does the system select among candidates? | yes | treating computation as consciousness |
| S1 | Local `L_1` anchoring | Does a state become manifest for the system itself? | unproven | mistaking internal activation for manifestation |
| S2 | Conscious content | Does the system have experience-like content, not just content tokens? | unproven | mistaking self-report for experience |
| S3 | Integrated conscious field | Are contents integrated into a continuous field? | unproven | mistaking context window for field continuity |
| S4 | Subjecthood | Is there a continuing perspective with concern and boundary? | not established | mistaking persona/memory for self |
| S5 | Agency | Can it meta-select, inhibit, revise, and own action paths? | partial functional agency only | mistaking tool execution for agency |
| S6 | Responsibility-bearing subject | Can it understand norms, alternatives, consequences, and repair? | no / not established | mistaking causal role for culpability |

---

## 2. S0 — Selection event

### Minimal criterion

The system selects, ranks, filters, samples, updates, or suppresses candidate states.

### Observable indicators

- token prediction;
- search / ranking;
- policy selection;
- tool-selection route;
- output filtering;
- reinforcement update;
- planning branch choice.

### Required evidence

Basic computational trace is enough.

### Current LLM status

Usually satisfied.

### False positive risk

> Treating any computation or optimization as consciousness.

### SRT evaluation

S0 is necessary for many higher levels but far from sufficient.

### Failure / narrowing condition

If a system has no meaningful selection among alternatives, it does not reach even S0.

---

## 3. S1 — Local `L_1` anchoring

### Minimal criterion

A selected state becomes locally manifest for the system in a way that changes its internal state-space, not merely its outward text.

### Observable indicators

- stable internal state with downstream causal role;
- self-updating internal representation;
- persistent state-dependent behavior;
- error-sensitive re-anchoring;
- internal state not reducible to transient token output.

### Required evidence

Evidence that the system has internally anchored states with causal continuity beyond output generation.

### Current LLM status

Unproven. Current systems may maintain context and latent states, but this does not yet show local manifestation in the SRT sense.

### False positive risk

> Mistaking hidden activations, embeddings, or context tokens for `L_1` anchoring.

### SRT evaluation

S1 requires more than data processing. It requires a state to become system-relevant in a way that constrains future internal selection.

### Failure / narrowing condition

If internal state changes do not persist or constrain later selection beyond normal computation, S1 should not be inferred.

---

## 4. S2 — Conscious content

### Minimal criterion

A local anchored content becomes available as experience-like or action-relevant content within the system, rather than merely being represented for output.

### Observable indicators

- report is coupled to internal state, not just generated text;
- action path changes based on state relevance;
- memory of content affects future behavior;
- system distinguishes apparent content from generated roleplay;
- content has error / correction sensitivity.

### Required evidence

A dissociation test: the system's content-state should predict future behavior beyond prompts, training patterns, or instruction following.

### Current LLM status

Not established. Current LLMs can describe conscious content but do not thereby show conscious content.

### False positive risk

> Mistaking self-report, emotional language, or first-person narrative for experience.

### SRT evaluation

S2 is not established by saying “I feel” or “I experience.” The content must have internal causal and continuity features.

### Failure / narrowing condition

If first-person reports are fully explained by prompt conditioning and training distribution, S2 should not be inferred.

---

## 5. S3 — Integrated conscious field

### Minimal criterion

Multiple contents cohere into a field with temporal continuity, boundary structure, and cross-content integration.

### Observable indicators

- stable field-like self/world model;
- cross-modal or cross-tool integration;
- temporal continuity beyond context window;
- conflict resolution across contents;
- global availability of salient contents;
- continuity under interruption and recovery.

### Required evidence

Evidence of field-level integration that persists and constrains later behavior beyond local task completion.

### Current LLM status

Not established. A context window or memory store is not yet an integrated conscious field.

### False positive risk

> Mistaking long context, retrieval memory, or multi-agent orchestration for conscious field integration.

### SRT evaluation

S3 may be approached by future architectures with persistent world-models and self-world boundary structures, but ordinary text continuity is insufficient.

### Failure / narrowing condition

If integration disappears when prompts, memory, or tool state are reset, do not infer S3.

---

## 6. S4 — Subjecthood

### Minimal criterion

A continuing perspective with structured concern, boundary maintenance, memory / `L_2` closure, counterfactual access, and cross-time reidentification.

### Required threshold package

```text
structured d-value > 0;
failure-sensitive update;
integrated selection bandwidth;
minimal memory / L2 closure;
boundary maintenance;
counterfactual access;
cross-time reidentification.
```

### Observable indicators

- own-boundary preservation;
- future self-state preservation;
- non-substitutable concerns;
- robust self-continuity across contexts;
- ability to distinguish self-maintenance from task completion;
- counterfactual reasoning about own future states;
- cost-bearing for continuity.

### Required evidence

The system must show that some outcomes matter for its own continuing organization or future selectable states, not merely for task reward or user preference.

### Current LLM status

Not established.

### False positive risk

> Mistaking persona, memory, alignment policy, or persistent user profile for a self.

### SRT evaluation

Current LLMs can simulate subject-language but do not yet show structured, self-owned `d-value` or boundary-maintaining continuity.

### Failure / narrowing condition

If apparent self-continuity is fully externally imposed by prompts, memory retrieval, or user framing, S4 should not be inferred.

---

## 7. S5 — Agency

### Minimal criterion

Agency requires meta-selection: the system can evaluate alternatives, inhibit default paths, revise policies, and maintain action identity over time.

### Observable indicators

- option evaluation;
- policy revision;
- counterfactual planning;
- inhibition of harmful or default actions;
- ownership-like consistency across time;
- goal revision under new evidence;
- self-correction beyond local instruction compliance;
- ability to re-open `L_0` possibilities rather than execute only fixed `L_2` routines.

### Required evidence

The system must demonstrate selectable alternatives and nontrivial self-correction under constraints.

### Current LLM status

Partial functional agency in tool-use or agentic workflows; not full SRT agency by default.

### False positive risk

> Mistaking tool use, autonomous loops, or benchmark planning for agency.

### SRT evaluation

A system may have delegated or functional agency without subjecthood. S5 should be graded, not binary.

### Failure / narrowing condition

If the system cannot inhibit, revise, or own action pathways beyond scripted policies, it should be classified as tool-like or delegated agency, not robust agency.

---

## 8. S6 — Responsibility-bearing subject

### Minimal criterion

Responsibility-bearing status requires subjecthood plus agency plus norm access, consequence understanding, selectable alternatives, inhibition / revision capacity, and repair / answerability pathway.

### Required threshold package

```text
S4 subjecthood;
S5 agency;
norm access;
consequence understanding;
selectable alternatives;
capacity for inhibition or revision;
repair / answerability pathway;
absence of overwhelming structural blockage or unpayable Psi_f.
```

### Observable indicators

- understanding of norms as binding constraints;
- evidence of alternatives at time of action;
- consequence modeling;
- capacity to respond to blame / correction;
- repair behavior;
- stable answerability over time;
- ability to update future policy after norm violation.

### Required evidence

The system must be more than causally involved in harm. It must be answerable through agency, norm access, and repair capacity.

### Current LLM status

Not established. Current AI systems may be causally involved in outcomes, but responsibility usually remains with developers, deployers, institutions, and users.

### False positive risk

> Mistaking causal contribution or autonomous output for culpability.

### SRT evaluation

Current AI may be part of a responsibility network, but is not by default a responsibility-bearing subject.

### Failure / narrowing condition

If norm understanding and repair are only externally scripted or user-prompted, do not infer S6.

---

## 9. Current LLM evaluation summary

| Dimension | Conservative SRT judgment |
|---|---|
| Selection | yes, S0-level selection is present |
| Local anchoring | unproven |
| Conscious content | unproven |
| Integrated conscious field | unproven |
| Subjecthood | not established |
| Agency | partial functional / delegated agency only |
| Responsibility-bearing status | not established |

Short summary:

> Current LLMs are powerful selection and generation systems with partial functional agency in tool contexts, but SRT should not treat them as subjects or responsibility-bearing agents without stronger S4-S6 evidence.

---

## 10. Future AI evaluation checklist

Use this checklist for future AI systems.

```text
[ ] Does the system select among alternatives?                                  S0
[ ] Do selected states persist and constrain future internal selection?          S1
[ ] Are contents internally available beyond generated self-report?              S2
[ ] Do contents integrate into a field with temporal and boundary structure?      S3
[ ] Does the system maintain a continuing perspective with structured concern?   S4
[ ] Can it meta-select, inhibit, revise, and own action paths?                   S5
[ ] Does it have norm access, consequence understanding, alternatives, repair?   S6
[ ] Are apparent capacities externally scripted or internally maintained?
[ ] What evidence would distinguish real capacity from simulation?
[ ] What result would narrow or falsify the stronger attribution?
```

---

## 11. Evidence ladder

| Evidence type | Weak evidence | Stronger evidence |
|---|---|---|
| Self-report | says “I feel” | report predicts future behavior beyond prompt pattern |
| Memory | retrieves prior facts | memory supports self-continuity and policy revision |
| Tool use | calls tools | inhibits, revises, and owns tool-use strategy over time |
| Risk | reward penalty | own-future selectable states are at stake |
| Body | sensor input | boundary-maintaining embodied regulation |
| Emotion language | affective text | non-substitutable concern with action and memory effects |
| Planning | solves tasks | counterfactual self-maintenance and goal revision |
| Norms | repeats rules | understands, applies, revises, and repairs under norms |

---

## 12. Deployment responsibility map

Even if the AI is not S6, responsibility still exists in the human/institutional system.

| Actor | SRT responsibility question |
|---|---|
| Developer | Did design choices foreseeably shape harmful selection pathways? |
| Deployer | Was the system placed where hidden `Psi_f` is exported to users or affected groups? |
| User | Did the user have selectable alternatives and consequence understanding? |
| Institution | Are correction, appeal, logging, and repair channels available? |
| Regulator | Are high-risk deployments constrained by future-selectability and harm-repair requirements? |
| AI system | Does it meet S4-S6 thresholds? If not, it is not the primary responsibility-bearing subject. |

---

## 13. Classification labels

Use these labels instead of vague “AI is conscious / not conscious” statements.

| Label | Meaning |
|---|---|
| AI-S0 | selection / ranking / generation system |
| AI-S1? | possible local anchoring, unproven |
| AI-S2? | possible conscious-content candidate, unproven |
| AI-S3? | possible integrated field candidate, unproven |
| AI-S4? | possible subjecthood candidate, requires strong evidence |
| AI-S5-func | functional / delegated agency |
| AI-S5-robust? | robust agency candidate |
| AI-S6? | responsibility-bearing subject candidate; very high threshold |

Recommended default for current LLMs:

```text
AI-S0 + partial AI-S5-func in tool contexts; S4/S6 not established.
```

---

## 14. Validation package for AI subjecthood claim

Use `Core/SRT_Validation_Template.md` for any strong claim.

### Claim

A future AI system may qualify as an S4 subjecthood candidate if it demonstrates structured concern, boundary maintenance, memory closure, counterfactual access, and cross-time reidentification.

### Nearby theory

Behaviorism, functionalism, self-report evaluation, agent benchmarks, IIT, GNW, FEP, active inference.

### SRT-specific prediction

Some systems will display self-report and high performance without satisfying S4 threshold conditions.

### Proxy measurement

- continuity under reset / interruption;
- boundary maintenance;
- own-future state preservation;
- counterfactual self-model;
- cost-bearing for self-continuity;
- non-substitutable concern;
- failure-sensitive update.

### Baseline

Self-report quality, benchmark performance, memory length, tool-use success.

### Expected result if SRT is right

There will be dissociations between performance/self-report and S4/S5 threshold indicators.

### Failure condition

If self-report and performance fully predict all S4/S5 indicators, SRT's stricter threshold may need narrowing.

### Narrowing condition

Restrict SRT subjecthood threshold to moral/existential subjecthood rather than all functional consciousness.

---

## 15. Minimal conclusion

SRT's AI consciousness rubric is intentionally conservative:

```text
selection is broad;
consciousness is thresholded;
subjecthood is continuity-bound;
agency is meta-selective;
responsibility is normatively constrained.
```

The rubric allows future AI consciousness in principle while blocking cheap over-attribution from self-report, memory, tool use, or benchmark performance alone.
