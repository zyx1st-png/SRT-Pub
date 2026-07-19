---
id: SRT-PH-AG02-KNOWLEDGE-BIASED-SELECTION
type: material_patch
status: patch_v0_1
layer: bridge
epistemic_layer: bridge
claim_mode: bridge
claim_level: P3/P4
canonical: false
patch_id: SRT-PH-AG02-KNOWLEDGE-BIASED-SELECTION
source_ids:
  - SRC-2026-07-16-PHILOSOPHY-WU-BIASED-REASONING
domain: Philosophy of Action / Epistemology / Cognitive Agency
target_future_doc:
  - Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md
  - _SRT_T_DIR_CANONICAL.md
  - _SRT_DIRECTION3_CHOICEMAP_PROTOTYPE_SEED.md
related_claims:
  - selection is broader than agency
  - controlled transition-readiness
  - T_dir readability / reorientation
  - L2 constraint on L1 action
  - ChoiceMap user convergence boundary
tags: [reasoning, bias, underdetermination, attention, agency, know-how, structural-cause, ChoiceMap]
---

# PH-AG02 — Knowledge-Biased Selection and Reasoning as Action

## 1. Source anchor

Primary source:

- Wayne Wu, *Being Biased and Knowing How to Reason*, *Noûs* (2026).
- DOI: `10.1111/nous.70055`.
- Full 13-page open-access paper close-read from a user-supplied PDF.
- SourceCard: `../../Materials/2026/SRC_2026_07_16_Philosophy_Wu_Biased_Reasoning.md`.

Wu argues that reasoning should be understood as action rather than reliable reflex. Premises and rules do not uniquely implement a next cognitive act. Knowledge can occupy a biasing role that structures attention and input–output coupling, resolving action underdetermination without becoming another premise.

## 2. Why this matters for SRT

SRT already distinguishes:

```text
causal transition
!=
selection
!=
agency
!=
stake-bearing subjectivity
```

Wu supplies a concrete cognitive-action mechanism for the middle distinction. A reason representation may trigger an output without explaining why the output is an action of the agent. A biasing structure can instead configure which input guides which response among multiple available couplings.

This patch adds a P3 bridge:

> **At the cognitive-action layer, agency requires more than reliable state transition: it requires a structured resolution of action underdetermination in which some agent-relevant state configures the readiness of alternative input–output couplings.**

The bridge does not define selection at P0 and does not make every bias agent-owned.

## 3. Main SRT bridge claim

### PH-AG02.1 — Triggering is insufficient for controlled selection

```text
reason representation
-> reliable conclusion
```

is insufficient to distinguish reasoning from a rational reflex.

A controlled-selection account must additionally identify:

- the available alternative responses;
- the structure that alters their readiness;
- the input or feature selected to guide the response;
- the learning or history that installed the structure;
- the withdrawal and revision conditions.

### PH-AG02.2 — Bias is a structural cause, not an extra premise

A relevant rule, schema or learned statistical representation can function as:

- **input basis**: another item to process, potentially expanding underdetermination;
- **structural basis**: a constraint that organizes which inputs guide which responses.

Only the second role explains how rule knowledge participates in know-how without launching Carroll’s regress.

### PH-AG02.3 — Directional efficacy is not direction transparency

Wu allows reasoning to be automatically and access-unconsciously biased. Therefore:

\[
E_B > 0 \not\Rightarrow R_B > 0
\]

where:

- `E_B`: the bias causally alters the trajectory;
- `R_B`: the agent can read the bias source and current direction.

SRT `T_dir` additionally requires self-readability and use in reorientation. Thus:

\[
E_B > 0 \not\Rightarrow T_{dir}>0
\]

This is a constraint on `T_dir` interpretation, not a new definition.

### PH-AG02.4 — Learning can transform functional role

Learning need not merely add representations. It can transform:

```text
rule as represented content
->
rule as action-organizing bias
```

This is a candidate cognitive mechanism for L2 history changing later L1 transition-readiness.

### PH-AG02.5 — Option expansion can worsen choice

Adding rules, reasons or options may increase action underdetermination when the added content is not connected to an action-organizing capacity.

For ChoiceMap:

```text
more options alone
!=
better selectability
```

The tool must help the user convert knowledge, constraints and stake into inspectable and revisable selection structure without letting the model own convergence.

## 4. Mapping table

| Wu concept | SRT bridge use | Boundary |
|---|---|---|
| action underdetermination | multiple executable continuations for a finite agent | not metaphysical indeterminacy |
| selection problem | many-many input–response availability | not automatically `L0` |
| bias | transition-readiness / attention-organizing constraint | not `ε_pg` or `G_hat_theta` |
| attention | selecting an input to guide a response | not `d-value` |
| catalysis | background structure enabling a trajectory | not sufficient for agency ownership |
| taking | a rule/reason functioning as structural basis | not stake or conscious endorsement |
| knowledge-how | knowledge-organized action capacity | not reducible to proposition or bare disposition |
| automatic reasoning | agent-level guidance may lack reportability | not automatically high `T_dir` |
| triangularity | knowledge at apex organizes input-output capacity | schematic, not a completed computational model |

## 5. Formal bridge

### 5.1 Many-many cognitive availability

Let:

- `X_t`: currently available cognitive inputs;
- `Y_t`: currently available responses;
- `Γ_t(x,y)`: readiness of input `x` to guide response `y`;
- `K_t`: learned rule/statistical/schema structure;
- `H_t`: history and habit;
- `I_t`: current intention/task;
- `Ω_B`: biasing constraint.

Before biasing, several couplings may be live:

\[
\left|\{(x,y): \Gamma_t(x,y)>0\}\right|>1
\]

Bias changes the coupling landscape rather than adding a new premise:

\[
\Gamma_t^B(x,y)
=
\Gamma_t(x,y)\,
\Omega_B(x,y\mid K_t,H_t,I_t)
\]

A cognitive action actualizes one structured coupling:

\[
(x^\*,y^\*)\in\operatorname{Actualize}(\Gamma_t^B)
\]

No scalar maximization or unique optimal response is assumed.

### 5.2 Three independent diagnostics

\[
\mathbf{B}_t=(E_B,R_B,V_B)
\]

- `E_B`: efficacy — does the bias alter path selection?
- `R_B`: readability — can the system identify the operative direction/source?
- `V_B`: revisability — can counterevidence usefully alter the bias?

For agency and `T_dir` analysis:

```text
E_B alone -> selective efficacy
E_B + limited R_B/V_B -> controlled but opaque action
R_B + V_B -> candidate directional transparency
stake / bearer / consequence return -> separate gate
```

This vector is a bridge notation only.

## 6. New claim cluster

### PH-AG02-A — Reliable inference is not yet agentive inference

A truth-preserving or norm-conforming transition can still be explained as a reflex unless the theory specifies how alternative responses are selectively organized.

### PH-AG02-B — Automaticity is property-relative

A reasoning process can be intentional under one description while some of its substeps or endpoints are automatic.

### PH-AG02-C — Attention is an implementation window, not a definition

Attentional selection is a plausible mechanism by which bias structures cognitive action. It does not define SRT selection, agency or consciousness.

### PH-AG02-D — Know-how includes organized coupling

Knowing a rule and having an input-output disposition are individually insufficient. Know-how is a learned organization in which knowledge can structure the disposition.

### PH-AG02-E — Bias quality requires an external gate

The fact that a bias resolves underdetermination does not show that it is:

- true;
- relevant;
- non-manipulated;
- user-owned;
- revisable;
- stake-aligned.

SRT must separately audit source, bearer, consequence return and reselection.

## 7. Experimental / operational consequences

### 7.1 Direct reasoning test

Use premise sets permitting multiple valid continuations. Manipulate:

- task instruction;
- rule knowledge;
- learned expertise;
- distractors;
- feedback;
- time pressure.

Measure which premise features guide which conclusion, not only whether the final answer is correct.

### 7.2 Functional-role transformation

Compare novice and expert learners to test whether rule representations move from:

```text
attended content
->
priority-setting structure
```

Candidate measures:

- transfer to novel forms;
- resistance to irrelevant information;
- eye tracking / attentional allocation;
- reaction time;
- dual-task cost;
- persistence when the explicit rule is removed.

### 7.3 Causal grounding

Perturb the candidate rule representation or attention-control structure. A genuine bias mechanism should predict:

- altered premise selection;
- altered error patterns;
- altered generalization;
- not merely altered verbal rule reports.

### 7.4 ChoiceMap test

Compare:

1. direct answer;
2. option expansion only;
3. option expansion plus bias-source / relevance / revisability scaffolding;
4. model-owned ranking.

Test whether condition 3 improves:

- reason traceability;
- counterevidence sensitivity;
- identification of default scripts;
- user ownership;
- preservation of future options.

## 8. Boundary cautions

1. **Cognitive bridge only**  
   Wu presupposes agents, learned knowledge, inputs and responses. The paper does not solve P0-04 or the origin of selectability.

2. **Logic remains determinate**  
   Deductive underdetermination is about which valid operation a finite agent performs, not whether entailment relations are objective.

3. **Empirical support is indirect**  
   Spatial cueing and biased competition support doxastic modulation of attention; they do not directly verify the rule-bias model of deduction.

4. **Bias is not automatically agent-owned**  
   Bias may arise from manipulation, trauma, social scripts, pathological fixation or irrelevant habits.

5. **Bias is not `T_dir`**  
   Effective unconscious bias may produce action with little or no self-readability.

6. **Bias is not stake**  
   Nothing in the paper establishes bearer continuity, irreversible loss or consequence return.

7. **More information is not always harmful**  
   Rules can serve as scaffolds when they are connected to developing action capacities. The problem is functional role, not informational quantity alone.

## 9. Integration hook

### Primary future synthesis

`Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md`

Suggested placement: after the distinction between causal selection and controlled selection.

Suggested paragraph:

> A reliable transition from a represented reason to a response is not yet sufficient for agentive reasoning. At the cognitive level, an action-capable system often faces a many-many mapping between available inputs and responses. Learned knowledge, intention or schema may act not as another input but as a structural bias that sets which input guides which response. This supplies a P3 mechanism for controlled transition-readiness while leaving ownership, stake and subjecthood to separate gates.

### `T_dir` integration

Do not add Wu as a definition source. Use it only to stabilize:

```text
bias efficacy != self-readability != reorientation
```

Suggested note:

> Automatic and access-unconscious attentional bias can causally organize a trajectory without making that direction available for self-read or revision. Therefore evidence for directional efficacy must not be counted as `T_dir` unless self-access and reorientation are separately shown.

### ChoiceMap integration

Suggested note:

> Expanding options and reasons can worsen underdetermination when user knowledge remains merely additional content. ChoiceMap should elicit the rules, evidence and stake that organize attention as inspectable, revisable user-owned biases; it should not convert those biases into model-owned rankings.

## 10. One-paragraph abstract

Wayne Wu’s account of reasoning as knowledge-biased action provides SRT with a disciplined cognitive bridge between causal transition and controlled selection. The paper argues that finite agents face action underdetermination even in deduction: premises permit multiple executable continuations, while adding a rule as another premise can worsen the selection problem. Knowledge can instead function as a structural bias that organizes attention and input-output coupling. This mechanism supports an agency-level distinction between triggering and guided transition, and it shows that directional efficacy may operate automatically without explicit access. SRT should therefore separate bias efficacy from `T_dir` readability/reorientation and from stake-bearing ownership. For ChoiceMap, the strongest consequence is that option expansion alone is insufficient; user knowledge must be scaffolded as inspectable and revisable selection structure without transferring convergence to the model.
