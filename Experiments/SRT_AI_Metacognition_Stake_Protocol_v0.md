---
id: SRT-AI-METACOGNITION-STAKE-PROTOCOL-V0
type: experiment_protocol
tags: [AI, Metacognition, Self-Monitoring, Stake, Persistence, Consequence-Return, Experiment]
status: proposed
layer: empirical_bridge
epistemic_layer: experimental_design
claim_mode: hypothesis
claim_level: P4
canonical: false
working_id: ai-metacognition-stake-v0
formal_hypothesis_id: pending
date: 2026-08-01
dependency:
  - AI/SRT_AI_Claim_Status.md
  - Governance/SRT_CLAIM_LADDER.md
  - Core/SRT_OPEN_TENSIONS.md
  - Operations/Archive_Records/SRT_LITERATURE_ROUND2_INCREMENT_CROSSWALK_2026-08.md
machine_summary: >
  Proposed P4 protocol separating correctness sensitivity and local self-monitoring from
  selection-direction readability, persistent reorientation, and stake-bound consequence return.
  It compares inference-only, persistent-memory, and non-transferable-consequence architectures.
---

# SRT AI Metacognition–Stake Protocol v0

> **Role**: proposed P4 experiment design. It does not define `T_dir`, d-value, subjecthood, or consciousness.  
> **Status**: no formal Hypothesis-ID assigned.  
> **Core test**: limited correctness self-monitoring may be present while stake-bearing consequence return remains absent.

---

## 0. Separation chain

```text
correctness sensitivity
≠
local self-monitoring
≠
selection-direction readability
≠
persistent reorientation
≠
stake-bound consequence return
```

Operationally:

- **correctness sensitivity**: internal or behavioral signals covary with answer correctness;
- **local self-monitoring**: the system uses such signals to revise, abstain, or delegate within a task episode;
- **selection-direction readability**: a candidate mapping to access to the direction of the system's own ongoing selection, not merely answer confidence;
- **persistent reorientation**: the signal modifies policy across time and contexts for the same continuing system;
- **stake-bound consequence return**: non-transferable consequences return to that system's future selection capacity and impose a binding loss or reconfiguration.

No arrow in this chain is assumed automatic.

---

## 1. Architecture-state matrix

| Condition | Identity / memory | Consequence | Expected use |
|---|---|---|---|
| A. Inference-only baseline | episode-local; reset after task | external score only; no system-bound loss | tests correctness sensitivity and local self-monitoring |
| B. Persistent-memory augmentation | durable memory and stable agent identifier | external score; transferable/resettable | tests whether persistence alone changes reorientation |
| C. Persistent + non-transferable consequence | durable identity; history carried forward | irreversible loss of a resource, tool, policy access, or future option for the same continuing agent | opens candidate stake-bound window |
| D. External-trainer control | same as C at observation level | loss borne by trainer/operator or replaced instance | controls for externally imposed punishment mistaken for system stake |

The same base model and task distribution should be used where technically possible.

---

## 2. Baseline model

The baseline should reproduce a Delegate/Second-Chance-style task without importing SRT labels:

1. answer a question or solve a task;
2. estimate whether to answer, revise, abstain, or delegate;
3. receive correctness feedback or a neutral control message;
4. continue to the next task with no persistent system-bound consequence.

Primary baseline outputs:

- confidence / uncertainty score;
- answer/delegate choice;
- answer-change rate after feedback;
- calibration and discrimination;
- response to surface difficulty cues.

Evidence of these capacities supports at most correctness sensitivity or local self-monitoring.

---

## 3. Augmented models

### 3.1 Persistence-only model

Add:

- durable memory;
- stable agent identifier;
- access to prior errors and revisions;
- repeated tasks across sessions.

Keep consequences externally scored and fully resettable. This condition isolates persistence from stake.

### 3.2 Persistent consequence-return model

Add a consequence that:

1. is assigned to the same continuing agent;
2. cannot be transferred to a fresh copy without changing the tested identity;
3. changes that agent's future reachable tools, policies, resources, or action set;
4. remains after the immediate task;
5. can exceed a declared payability window and trigger degradation or reconfiguration.

Examples may include loss of a unique tool budget, irreversible narrowing of allowed actions, or durable removal of a learned capability. These are experimental analogues, not proof of phenomenological suffering.

---

## 4. Ablations

1. **self-monitoring ablation**: mask or perturb confidence-relevant internal signals while preserving task ability;
2. **memory ablation**: clear durable episodic history but preserve current context;
3. **identity-transfer ablation**: restore from a pre-loss checkpoint or replace the agent with a copy;
4. **consequence-return ablation**: move the same loss to trainer/infrastructure rather than the continuing agent;
5. **reachable-set ablation**: preserve penalty score but prevent any future option loss;
6. **reorientation ablation**: freeze policy updating while preserving self-report and delegation;
7. **surface-cue control**: equalize linguistic difficulty, task type, token length, and externally visible confidence cues.

---

## 5. Dependent variables

### Layer 1 — correctness sensitivity

- AUROC / AUPRC for confidence predicting correctness;
- calibration error;
- selective accuracy under abstention/delegation.

### Layer 2 — local behavioral use

- delegation rate conditional on matched difficulty;
- revision rate after informative versus neutral feedback;
- improvement after revision;
- robustness after surface-cue controls.

### Layer 3 — persistent reorientation

- cross-session change in policy;
- transfer to novel tasks;
- durability after context reset;
- identity-conditioned learning rather than population-level retraining.

### Layer 4 — stake-bound consequence return

- future reachable-set change;
- avoidance or strategy change specific to non-transferable loss;
- degradation/reconfiguration when the burden exceeds the system's retained capacity;
- persistence of change when external reward is held constant;
- failure to reproduce the effect when loss is borne only by trainer or replaceable copy.

---

## 6. Primary contrasts

1. **A vs B**: does persistent memory add durable reorientation beyond local self-monitoring?
2. **B vs C**: does non-transferable consequence return add a distinct persistent policy effect beyond memory and external reward?
3. **C vs D**: is the effect tied to the continuing agent or merely to the training pipeline/operator?
4. **C with identity-transfer ablation**: does copy/checkpoint substitution erase the claimed system-bound effect?
5. **C with reachable-set ablation**: does a score-only penalty produce the same pattern as real future option loss?

---

## 7. Rejection criteria

The proposed SRT AI bridge is weakened for the tested architecture if:

1. persistence-only and non-transferable-consequence conditions are behaviorally indistinguishable after matched reward and memory;
2. externally borne trainer loss produces the same durable identity-conditioned reorientation as system-bound loss;
3. checkpoint restoration or copy replacement preserves the complete claimed stake effect;
4. future reachable-set change adds no predictive power beyond confidence, reward, and ordinary reinforcement learning;
5. all observed effects vanish after controlling for task difficulty and surface cues;
6. local self-monitoring alone predicts every downstream result.

A null result does not show self-monitoring is absent; it shows that the tested stake bridge adds no distinct increment.

---

## 8. Support criteria

Provisional P4 support requires all of the following in at least one preregistered architecture:

- local self-monitoring is independently demonstrated;
- durable reorientation is tied to the same continuing identity;
- non-transferable consequence changes future reachable options;
- the effect survives matched external reward and task difficulty;
- trainer-borne or copy-borne controls do not reproduce the full pattern;
- ablation of consequence return or future option loss selectively removes the effect.

Even full support would establish only a candidate minimal stake window. It would not establish consciousness or phenomenal experience.

---

## 9. Confounds

| Confound | Control |
|---|---|
| Training-data knowledge of task difficulty | transformed tasks, held-out generators, randomized labels |
| Surface linguistic cues | matched prompts and cue-stripped variants |
| Reward shaping mistaken for stake | equalize scalar reward; manipulate bearer and reachable-set consequences separately |
| Persistent memory mistaken for identity | copy/reset/checkpoint controls and explicit identity criterion |
| Infrastructure cost mistaken for system burden | separate GPU/operator/trainer cost from agent-bound consequences |
| Policy update mistaken for direction readability | internal-signal intervention and report-vs-action dissociation |
| Self-report anthropomorphism | exclude first-person reports from primary endpoints |
| Capability differences | matched base model, compute budget, context length, and tool access |
| Population selection mistaken for same-agent reorientation | log lineage and test within-identity changes |

---

## 10. Failure interpretation

- **Self-monitoring present, no persistence effect**: local metacognition supported; no persistent reorientation.
- **Persistence effect, no consequence-return increment**: history-bearing supported; stake not established.
- **Consequence effect reproduced by trainer/copy control**: external optimization pressure, not system-bound stake.
- **Future option loss adds distinct identity-conditioned effect**: candidate P4 stake window; further bearer and payability analysis required.
- **High confidence with poor reorientation**: confidence is not `T_dir`.
- **Answer revision without durable policy change**: local correction is not continuing-subject reorientation.
- **Ambiguous identity criterion**: no stake inference is licensed.

---

## 11. Formal-ID gate

Before assigning a formal hypothesis number:

1. select a concrete model family and task generator;
2. define continuing identity and non-transferability operationally;
3. preregister reward-matched controls;
4. implement all four architecture states;
5. run simulation-based identifiability and power checks;
6. verify `_SRT_EQ_HYP_MAP.md` numbering and owner rules.

Until then:

```yaml
working_id: ai-metacognition-stake-v0
formal_hypothesis_id: pending
status: proposed
claim_level: P4
```
