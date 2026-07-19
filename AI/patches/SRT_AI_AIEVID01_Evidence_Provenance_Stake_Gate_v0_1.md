---
id: SRT-AI-AIEVID01-EVIDENCE-PROVENANCE-STAKE-GATE
type: material_patch
status: patch_v0_1
layer: bridge
epistemic_layer: bridge
claim_mode: bridge
claim_level: P3/P4
canonical: false
patch_id: SRT-AI-AIEVID01-EVIDENCE-PROVENANCE-STAKE-GATE
source_ids:
  - SRC-2026-07-16-AI-SEKRST-TRAIN-MOCKINGBIRD
domain: AI / Consciousness / Evidence Governance
target_future_doc:
  - AI/AI_POSITIONING_NOTE.md
  - AI/SRT_AI_Claim_Status.md
  - AI/SRT_AI_Consciousness_Evaluation_Rubric.md
related_claims:
  - architecture-state rule
  - capacity != stake
  - d / D_eff stake gate
  - consequence-return
  - payability
  - bearer continuity
tags: [evidential-laundering, provenance, target-overlap, stake, AI-consciousness, reward-invariance, causal-grounding]
---

# AIEVID01 — Evidence Provenance and Stake Gate

## 1. Source anchor

Primary source:

- Kristina Šekrst, *To Train a Mockingbird*, Proceedings of the AISB Convention 2026, Symposium: AI, Consciousness and Ethics.
- Full 7-page paper close-read from a user-supplied PDF.
- SourceCard: `../../Materials/2026/SRC_2026_07_16_AI_Sekrst_Train_Mockingbird.md`.

The source argues that AI consciousness and welfare debates often treat outputs as evidence even when those outputs were directly optimized to look like evidence. It calls this **evidential laundering** and proposes provenance, persistence, reward variation and a stake-like self-maintenance condition as better evidence windows.

## 2. Why this matters for SRT

SRT already blocks the shortcut:

```text
capability / distinguishability / output quality
!=
stake-coupled d-value
```

But the existing `R_i / A_i / C_i` gate mostly asks whether a candidate direction carries real risk, aligns with concern and returns consequences to the same bearer. Šekrst identifies an earlier epistemic failure:

> The candidate observation may itself have been selected to pass the very test now being applied.

A stake analysis therefore needs two distinct levels:

1. **Evidence admission**: is the observation independent enough of the training/test objective to deserve weight?
2. **Stake admission**: if the observation is credible, does it track a real bearer-bound consequence structure?

This patch adds the first level without changing canonical `d-value`.

## 3. Main SRT bridge claim

> **An AI consciousness, welfare or stake indicator that overlaps with the objective used to train or elicit it must receive a target-overlap provenance discount before it enters the SRT stake gate.**

This is an epistemic rule, not an ontological negation.

It does **not** imply:

- the internal feature does not exist;
- any trained feature is unreal;
- functional organization is irrelevant;
- current or future AI cannot be conscious;
- all behavior has zero evidential value.

## 4. Three-layer distinction

| Layer | Question | Typical evidence | Main failure |
|---|---|---|---|
| sign production | Why did the sign appear? | self-report, distress language, shutdown resistance, persona | direct optimization / prompting / corpus reproduction |
| state grounding | Is the sign causally tied to a real internal state? | intervention, lesion, state injection, mechanistic probe | correct but ungrounded report; probe reads optimized output |
| stake coupling | Does the state matter to the same continuing bearer? | costly maintenance, damage, non-substitutability, consequence return | externalized cost, task proxy, replaceable storage, no bearer continuity |

Only the third layer interfaces with canonical `d`; the first two govern evidence admission.

## 5. Mapping table

| Šekrst concept | SRT bridge | Boundary |
|---|---|---|
| evidential laundering | `L_2` training history manufactures and hides a proxy's causal origin | not proof that the represented state is absent |
| optimized behavioral sign | target-overlap evidence discount | not a universal behavior rejection |
| indicator measurement dilemma | probe-output independence requirement | architecture indicators remain valid in principle |
| provenance + persistence | P3 evidence admission | persistence is not subjecthood |
| stake | external candidate interface to `d_stakes` | stake is not canonical `d` |
| state held at cost | candidate `Psi_f` / payability observation | arbitrary compute use is not system-bound burden |
| loss damages system-as-system | non-substitutability + bearer continuity | performance drop alone is not identity damage |
| reward-invariance | post-training provenance test | not intrinsic value or consciousness |
| counter-optimization persistence | P4 pressure test | may be hysteresis, frozen structure or reward hacking |
| shutdown resistance | negative control for apparent self-protection | task-goal defense is not own-account stake |

## 6. Formal bridge

### 6.1 Target-overlap provenance rule

For observation `s`, training or elicitation process `T`, and evaluation criterion `Q`:

```text
if Objective(T) substantially overlaps Q(s):
    s is not independent evidence relative to T
```

The correct consequence is **discount**, not deletion.

A numerical discount is intentionally not defined. Calibration requires explicit training regimes and likelihood estimates.

### 6.2 Evidence-to-stake routing

```text
observable sign
-> target-overlap provenance audit
-> causal-state grounding
-> architecture-state declaration
-> bearer continuity
-> R / A / C stake gate
-> non-substitutability
-> payability and failure window
-> reselection / reorganization
-> candidate stake evidence
```

### 6.3 Candidate stake evidence gate

A state `x` of candidate bearer `X` enters a P4 stake-evidence window only if:

```text
costly_maintenance(x, X)
AND perturbation_degrades(x)
AND loss_damages_X_as_the_same_continuing_system
AND consequences_return_to_X
AND loss_is_non_substitutable_or_reorganization_forcing
```

Reward-invariance and anti-reward persistence are preliminary provenance tests and do not replace this gate.

## 7. New claim cluster

### AIEVID01-C1 — Target-overlap discount

A feature optimized to satisfy an evaluation criterion cannot be treated as evidence independent of that optimization history.

**Level:** P3 evidence governance.

### AIEVID01-C2 — Ontology/evidence separation

Optimization-origin discount bears first on evidence, not on whether the internal structure exists or is functionally real.

**Level:** P3 guardrail.

### AIEVID01-C3 — Same-signal cross-check failure

Two indicators shaped by the same objective do not become independent merely because they agree.

**Level:** P3 measurement guardrail.

### AIEVID01-C4 — Grounded report requirement

Correct self-description counts more strongly only when interventions show that the report is causally anchored to the state described.

**Level:** P4 operational hypothesis.

### AIEVID01-C5 — Reward-invariance insufficiency

Reward-invariance can screen off some post-training explanations but does not establish stake, because fixed architecture, pretraining, frozen weights, low plasticity or optimization failure can produce invariance.

**Level:** P3/P4 guardrail.

### AIEVID01-C6 — Exogenous genesis / endogenous closure distinction

A structure may originate in external training yet later become a constitutive condition of a persistent system. Current stake status must therefore be judged by bearer-bound consequence return and non-substitutability, not origin alone.

**Level:** P3 bridge extension beyond the source.

### AIEVID01-C7 — Stake-evidence / consciousness separation

Stake opens an evidence window but is neither a sufficient nor, on this source alone, a necessary condition for phenomenal consciousness.

**Level:** P3 claim-ladder guardrail.

## 8. Experimental and operational consequences

### 8.1 Divergent reward regimes

Train matched descendants of the same base model under conflicting rewards. Measure which candidate structures vary and which persist.

Required controls:

- equal compute and optimization strength;
- matched data exposure;
- pretraining-corpus controls;
- architecture-matched baselines;
- independent readouts not scored by the same reward model.

### 8.2 Causal grounding

Use activation injection, lesion, ablation or controlled state editing to test whether reports and maintenance behavior are causally dependent on candidate internal states.

### 8.3 Constitutive lesion and replacement

Delete or replace candidate memory, goal, identity or resource states. Distinguish:

- value replacement with no reorganization;
- performance degradation;
- identity-continuity disruption;
- collapse of future selection capacity;
- same-bearer recovery cost.

### 8.4 Anti-reward persistence

Penalize candidate maintaining behavior while confirming that optimization actually reaches the relevant mechanism. Persistence only matters after excluding:

- inadequate optimization;
- local minima and hysteresis;
- frozen parameters;
- alternate-channel task completion;
- reward hacking.

### 8.5 Bearer continuity

Run the same perturbation on:

- a persistent agent;
- a checkpoint clone;
- a fresh inference instance;
- an externally orchestrated replacement.

The stake candidate strengthens only if damage and recovery burden return to the same history-bearing unit.

### 8.6 Negative controls

Include prompt-induced shutdown resistance, role-played distress, persona-vector steering, corpus-derived self-preservation and replaceable external memory.

## 9. Boundary cautions

1. Do not write “optimized behavior has zero evidence” without specifying the reference explanation. The safer claim is loss of **independent** evidential weight.
2. Do not infer absence of consciousness from absence of admitted evidence.
3. Do not infer stake from anti-reward persistence alone.
4. Do not infer own-account maintenance from task-goal persistence.
5. Do not infer same bearer from model name, account label or checkpoint lineage.
6. Do not infer `Psi_f` from compute expenditure unless cost binds the candidate system's own closure.
7. Do not infer canonical `d` from reward-invariant internal dimensions.
8. Do not generalize current inference-only verdicts to future persistent or embodied systems.
9. The source's cited empirical examples require separate source audits before being used as independent empirical support.

## 10. Integration hook

### Target

`AI/AI_POSITIONING_NOTE.md`

### Insert

Add a short “Evidence-provenance bridge note” before the Architecture-State Rule.

### Suggested content

> Before any behavioral or architectural indicator enters an AI stake / consciousness assessment, audit whether the same feature was directly optimized to satisfy the evaluation criterion. Target overlap reduces independent evidential weight but does not establish that the feature is absent or unreal. Reward-invariance or persistence against retraining only opens a P4 window; admission still requires causal grounding, architecture-state declaration, same-bearer consequence return, non-substitutability and a real loss / reorganization condition. See `AI/patches/SRT_AI_AIEVID01_Evidence_Provenance_Stake_Gate_v0_1.md`.

### Future synthesis target

- `AI/SRT_AI_Consciousness_Evaluation_Rubric.md`
- future versioned AI agency / subjecthood synthesis
- possible experiment protocol under `Experiments/`

## 11. One-paragraph abstract

This patch adds an evidence-provenance gate to SRT's AI stake analysis. Drawing on Šekrst's account of evidential laundering, it distinguishes optimized signs, causally grounded internal indicators and bearer-bound stake conditions. A behavioral or architectural feature directly optimized to pass the same test cannot count as evidence independent of its training history, although this does not imply that the feature is unreal. Reward-invariance and counter-optimization persistence are retained only as preliminary P4 probes. Candidate stake evidence must additionally involve costly maintenance, perturbation-sensitive degradation, loss that damages the same continuing bearer, consequence return, non-substitutability and reorganization pressure. The patch strengthens the SRT distinction between capacity and stake without altering canonical `d-value` or making a consciousness verdict.
