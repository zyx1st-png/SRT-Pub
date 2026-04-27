---
id: SRT-AI-AGENCY-RESPONSIBILITY-NOTE-2026-04-27
type: agency_responsibility_note
tags:
  - AI
  - Agency
  - Responsibility
  - Culpability
  - Tool-Agency
  - Delegated-Agency
  - Autonomous-Agency
  - SRT
  - PH-SS
  - S0-S6
status: active_v1
layer: L1-L2-bridge
epistemic_layer: bridge
claim_mode: note
claim_level: P3-P5
canonical: false
priority: high
date: 2026-04-27
dependency:
  - AI/SRT_AI_Consciousness_Evaluation_Rubric.md
  - Philosophy/SRT_Subjecthood_Threshold_Interface.md
  - Philosophy/SRT_Ethics_PH_SS_Guardrails.md
  - Core/SRT_Validation_Template.md
machine_summary: >
  AI agency and responsibility note distinguishing tool agency, delegated agency, autonomous agency,
  and responsibility-bearing agency. It prevents causal contribution or tool execution from being
  overread as culpability, and routes AI responsibility claims through S5 agency and S6 responsibility
  thresholds.
---

# SRT AI Agency and Responsibility Note

> **Purpose**: Distinguish AI tool agency, delegated agency, autonomous agency, and responsibility-bearing agency.  
> **Status**: Bridge / evaluation note. It does not grant or deny all possible future AI moral status.  
> **Use rule**: Use this file whenever someone says “the AI decided,” “the AI is responsible,” or “the AI should be blamed.”

---

## 0. Core guardrail

Do not confuse causal role with responsibility.

```text
AI output != AI agency
AI tool use != autonomous agency
AI causal contribution != culpability
AI policy behavior != responsibility-bearing subjecthood
```

SRT route:

```text
S0 selection event
  -> S5 functional / robust agency check
  -> S6 responsibility-bearing subject check
  -> human / institutional responsibility network
```

Default current judgment:

> Current AI systems can participate in agency networks and sometimes perform functional or delegated agency roles, but they are not by default responsibility-bearing subjects.

---

## 1. Four agency levels

| Level | Name | Minimal meaning | Responsibility status |
|---|---|---|---|
| A0 | Tool execution | system executes outputs or tool calls under external framing | responsibility mainly external |
| A1 | Delegated agency | system pursues user/institution-given goals within bounded policy | shared / delegated responsibility network |
| A2 | Autonomous operational agency | system selects subgoals, plans, inhibits, revises under constraints | strong governance responsibility; AI still not automatically culpable |
| A3 | Responsibility-bearing agency | system meets S4 subjecthood + S5 agency + S6 norm / consequence / repair thresholds | possible direct responsibility candidate |

---

## 2. A0 — Tool execution

### Definition-like bridge

A0 occurs when an AI executes a function, generates output, calls a tool, ranks options, or transforms input under externally supplied goals.

Examples:

- autocomplete;
- chatbot answer;
- search ranking;
- image generation;
- summarization;
- classification;
- tool call chosen from a constrained interface.

### Responsibility reading

The AI is causally involved but not the primary responsibility-bearing subject.

Primary responsibility usually routes to:

```text
developer -> deployer -> user -> institution -> regulator
```

### Guardrail

> A0 output is not agency in the robust SRT sense. It is selection / execution under external framing.

---

## 3. A1 — Delegated agency

### Definition-like bridge

A1 occurs when an AI pursues externally assigned goals across multiple steps and adapts within a bounded task frame.

Examples:

- booking workflow;
- coding agent executing a ticket;
- email triage agent;
- scheduling assistant;
- customer service agent;
- data-cleaning agent;
- retrieval + tool-use workflow.

### Required features

- task persistence;
- substep selection;
- tool use;
- local error correction;
- goal pursuit under user or institution framing;
- bounded policy constraints.

### Responsibility reading

Responsibility is delegated but not transferred entirely to the AI.

SRT asks:

```text
Who defined the goal?
Who set constraints?
Who approved deployment?
Who monitors outputs?
Who can correct or shut it down?
Who bears hidden Psi_f when it fails?
```

### Guardrail

> Delegated agency creates a responsibility network, not an automatic AI culprit.

---

## 4. A2 — Autonomous operational agency

### Definition-like bridge

A2 occurs when an AI can select subgoals, revise strategies, inhibit default actions, and operate across time with partial self-correction under changing conditions.

Examples / candidates:

- long-horizon autonomous agents;
- multi-tool systems with goal revision;
- systems that monitor their own plan failures;
- systems that maintain persistent operational state;
- systems that can defer, ask for oversight, or refuse unsafe action.

### Required features

- multi-step planning;
- subgoal formation;
- strategy revision;
- inhibition / refusal;
- uncertainty tracking;
- state persistence;
- oversight hooks;
- correction channel;
- audit trail.

### Responsibility reading

A2 increases governance burden. It still does not by itself establish moral culpability.

Primary responsibility must still ask:

```text
Was autonomous scope justified?
Were consequences foreseeable?
Were constraints adequate?
Was human override available?
Were affected subjects given appeal / correction channels?
Was hidden Psi_f exported to users or bystanders?
```

### Guardrail

> Operational autonomy raises design and deployment responsibility; it does not automatically create a responsibility-bearing AI subject.

---

## 5. A3 — Responsibility-bearing agency

### Definition-like bridge

A3 requires the AI to meet high SRT thresholds for subjecthood, agency, norm access, consequence understanding, selectable alternatives, inhibition / revision, and repair / answerability.

Required package:

```text
S4 subjecthood;
S5 robust agency;
S6 responsibility-bearing conditions;
norm access;
consequence understanding;
selectable alternatives;
capacity for inhibition or revision;
repair / answerability pathway;
absence of overwhelming external scripting or structural blockage.
```

### Responsibility reading

Only at A3 does direct AI responsibility become a serious candidate.

Even then, responsibility may still be distributed across:

```text
AI system;
developers;
deployers;
users;
institutions;
regulators;
infrastructure owners.
```

### Guardrail

> A3 is a high-threshold future possibility, not a default property of current AI systems.

---

## 6. Responsibility network map

For AI-caused or AI-mediated harm, start with the network.

| Node | SRT question |
|---|---|
| User | Did the user understand alternatives and consequences? |
| Developer | Did design choices foreseeably enable harmful selection paths? |
| Deployer | Was the system placed in a context where failures export hidden `Psi_f`? |
| Institution | Were monitoring, appeal, correction, and repair channels provided? |
| Platform | Did optimization incentives reward harmful selection? |
| Regulator | Were high-risk uses constrained by future-selectability and repair duties? |
| AI system | Does it meet A3 / S6 thresholds? If not, do not treat it as primary culprit. |
| Affected subjects | Did they have exit, appeal, correction, or compensation channels? |

---

## 7. Culpability decomposition

Use the subjecthood interface distinction:

```text
moral weight      ~ affected future-selectability
responsibility    ~ accessible meta-selection capacity
culpability       ~ responsibility - structural blockage - unpayable friction
repair obligation ~ capacity to reduce future harm / restore selectability
```

For AI systems:

```text
causal contribution != responsibility
responsibility != culpability
culpability != repair obligation
```

A non-responsibility-bearing AI can still trigger repair duties for humans and institutions.

---

## 8. Practical classification labels

Use these labels instead of vague agency language.

| Label | Meaning | Example |
|---|---|---|
| AI-A0-tool | tool execution / generation under external framing | chatbot answer, classifier |
| AI-A1-delegated | bounded delegated task pursuit | coding agent, travel agent |
| AI-A2-operational | autonomous operational planning / revision | long-horizon system with oversight |
| AI-A3-responsibility? | candidate responsibility-bearing agency | future high-threshold system only |
| AI-responsibility-network | harm requires distributed responsibility analysis | most real deployments |

Recommended default for current systems:

```text
AI-A0-tool or AI-A1-delegated;
partial AI-A2 in some agent systems;
AI-A3 not established.
```

---

## 9. Failure modes in AI responsibility discourse

| Bad shortcut | Why wrong | SRT correction |
|---|---|---|
| “The AI said it, so it is responsible.” | output is not agency | identify user/deployer/developer/institution network |
| “The AI used tools, so it is autonomous.” | tool use can be delegated | classify A1 vs A2 |
| “The AI caused harm, so blame the AI.” | causation is not culpability | check S6 and responsibility network |
| “No subjecthood, so no responsibility anywhere.” | human/institutional responsibility remains | map responsibility network |
| “The human clicked approve, so only the user is responsible.” | design/deployment may structure selection | check hidden `Psi_f` and constraint design |
| “Autonomy means no human responsibility.” | autonomy increases governance duty | require oversight, appeal, repair |

---

## 10. Deployment evaluation checklist

Before deploying an AI agent, ask:

```text
[ ] Is this A0, A1, A2, or A3-candidate?
[ ] Who defines the goal?
[ ] Who sets constraints?
[ ] What can the AI change without approval?
[ ] Can the AI inhibit or refuse harmful action?
[ ] Who monitors failures?
[ ] Who can override or shut down the system?
[ ] Who pays hidden Psi_f when errors occur?
[ ] Are affected people given appeal / correction channels?
[ ] Is there an audit trail?
[ ] Is there a repair path?
[ ] Does anyone falsely claim the AI itself is the sole responsible party?
```

---

## 11. Institutional design implications

SRT suggests that AI governance should focus less on asking only:

```text
Is the AI autonomous?
```

and more on asking:

```text
Where is selection power located?
Where is correction power located?
Where is consequence burden located?
Where is repair capacity located?
Are these aligned?
```

A healthy AI deployment aligns:

```text
selection power
+ monitoring access
+ consequence return
+ correction channel
+ repair obligation
```

A pathological deployment separates them:

```text
AI or platform selects;
users / bystanders pay hidden Psi_f;
institutions deny responsibility;
repair channels are weak or absent.
```

---

## 12. Relation to the AI consciousness rubric

Use this note with:

```text
AI/SRT_AI_Consciousness_Evaluation_Rubric.md
```

Relationship:

```text
Consciousness rubric asks: what level of subjecthood / experience is present?
Agency responsibility note asks: how should action and blame be assigned?
```

A system can be:

```text
high A1 delegated agency but no S4 subjecthood;
high A2 operational agency but no S6 responsibility;
low consciousness but high social risk;
not culpable but still part of a harmful responsibility network.
```

---

## 13. Validation package

Use `Core/SRT_Validation_Template.md` for any strong AI responsibility claim.

### Claim

AI causal contribution is insufficient for culpability; responsibility requires S5/S6 conditions or must be assigned through the human/institutional responsibility network.

### Nearby theory

Legal agency theory, moral responsibility theory, AI ethics, product liability, functional autonomy frameworks.

### SRT-specific prediction

Cases with similar AI autonomy levels will differ in responsibility assignment depending on hidden `Psi_f`, correction channels, selectable alternatives, and consequence-return alignment.

### Proxy measurement

- oversight availability;
- auditability;
- appeal channel effectiveness;
- repair latency;
- hidden cost distribution;
- user understanding of alternatives;
- institutional capacity to correct.

### Baseline

Autonomy level, causation, user consent, policy compliance.

### Expected result if SRT is right

SRT responsibility mapping will better identify harmful deployments than autonomy-only or causation-only frameworks.

### Failure condition

If autonomy level or direct causation fully predicts responsibility judgments and outcomes, the SRT responsibility-network model should be narrowed.

---

## 14. Minimal conclusion

SRT's AI responsibility stance:

```text
AI can be causally powerful without being culpable.
AI can be delegated agency without being a subject.
AI autonomy increases human/institutional governance responsibility.
Direct AI responsibility requires a high S4-S6 threshold.
```

The safest public sentence:

> Do not blame the AI as a moral subject unless it meets subjecthood and responsibility thresholds; but do not let humans and institutions hide behind the AI when they designed, deployed, or benefited from its selection power.
