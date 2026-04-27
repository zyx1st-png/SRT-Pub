---
id: SRT-VALIDATION-TEMPLATE-2026-04-27
type: validation_template
tags:
  - SRT
  - Core
  - Validation
  - Claim-Package
  - PH-SS
  - Non-Reductive-Validation
  - Proxy-Measurement
  - Failure-Condition
  - Differential-Prediction
status: active_v1
layer: meta_core
epistemic_layer: workflow
claim_mode: template
claim_level: P5
canonical: false
priority: high
date: 2026-04-27
dependency:
  - Core/SRT_Core_24_Floor_Normativity_Verification.md
  - Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md
  - Philosophy/PH_SS_Hardening_Audit_2026-04-27.md
  - SRT_NEXT_OPTIMIZATION_TODO.md
machine_summary: >
  Standard validation package template for SRT claims. It turns strong philosophical,
  cognitive, neural, AI, ethical, or social claims into testable packages with layer,
  claim level, nearby theory, SRT-specific prediction, proxy measurement, baseline,
  expected result, failure condition, narrowing condition, strengthening condition,
  and owner file. It operationalizes PH-SS-11 non-reductive validation without making
  non-reduction a shield against empirical risk.
---

# SRT Validation Template

> **Purpose**: Convert SRT claims into testable, comparable, reviewable claim packages.  
> **Status**: Workflow / validation template. It does not define canonical SRT primitives.  
> **Core rule**: Non-reductive validation is not an excuse to avoid empirical risk.

---

## 0. Why this template exists

SRT contains strong cross-domain claims. Without a standard validation format, these claims can look too broad, too philosophical, or too difficult to falsify.

This template converts a strong SRT claim into a structured package:

```text
claim -> layer -> nearby theory -> SRT-specific prediction -> proxy -> baseline -> failure condition
```

Minimum validation package:

```text
proxy measurement
+ structural consequence
+ differential prediction
+ withdrawal / narrowing condition
```

This implements the PH-SS-11 guardrail:

> SRT can be non-reductive without becoming unfalsifiable.

---

## 1. Standard claim package

Use this template for any SRT claim that presents itself as empirical, quasi-empirical, cross-domain, or theory-distinguishing.

```md
## Validation Package: <Claim Name>

### 1. Claim

<One clear sentence.>

### 2. Layer

Choose one or more:

- Core ontology
- Information geometry
- Cognitive science
- Neuroscience
- AI / agency
- Ethics
- Social / political theory
- Experimental proxy
- Public / interpretive bridge

### 3. Claim level

Choose:

- P0: primitive / definitional anchor
- P1: canonical constitutive theorem
- P2: strong theory claim
- P3: bridge claim
- P4: empirical / operational hypothesis
- P5: guide / index / workflow / public explanation

### 4. Nearby theory / competing explanation

List the closest alternatives:

- FEP / predictive processing
- reinforcement learning
- active inference
- GNW
- IIT
- standard information geometry
- social construction theory
- pragmatism
- physicalism
- constructivism
- institutional theory
- behavioral economics
- other

### 5. SRT-specific prediction

What does SRT predict that nearby theories do not clearly predict, or do not predict in the same structured way?

### 6. Proxy measurement

What can be measured?

Examples:

- reaction time
- error rate
- switching cost
- memory persistence
- bodily response
- action reorganization
- model-update path length
- hysteresis
- path dependence
- cross-subject alignment
- institutional resistance
- friction export
- exit / correction channel

### 7. Baseline

What simpler model must SRT beat?

Examples:

- salience
- confidence
- reward
- utility
- prediction error
- arousal
- attention
- habit strength
- ordinary memory
- social convention
- institutional stability
- market efficiency

### 8. Expected result if SRT is right

<State the expected pattern.>

### 9. Failure condition

What result would weaken the claim?

### 10. What would narrow SRT

If the failure condition occurs, how should SRT retreat or specialize?

### 11. What would strengthen SRT

What result would make the SRT reading more credible than nearby alternatives?

### 12. Owner file

Where should this claim live?

### 13. Current status

Choose:

- proposed
- bridge hypothesis
- operationalized
- pilot-ready
- tested
- narrowed
- retired
```

---

## 2. Compact one-line version

For fast use:

```text
Claim:
Layer:
Level:
Nearby theory:
SRT-specific prediction:
Proxy:
Baseline:
Expected result:
Failure condition:
Narrowing condition:
Strengthening condition:
Owner:
Status:
```

---

## 3. Validation levels

| Level | Meaning | Example |
|---|---|---|
| V0 | conceptual clarity only | term is defined but not operationalized |
| V1 | proxy family identified | possible measurements named |
| V2 | differential prediction stated | SRT predicts a pattern beyond nearby theory |
| V3 | baseline specified | SRT must beat salience / reward / PE / etc. |
| V4 | failure condition stated | result that would narrow / weaken SRT is explicit |
| V5 | pilot-ready design | task, measure, comparison, analysis plan sketched |
| V6 | tested / reviewed | empirical or case study result exists |

Minimum standard for serious empirical claims:

```text
V2 + V3 + V4
```

Minimum standard for pilot proposals:

```text
V5
```

---

## 4. Example package — `d-value` vs salience

### 1. Claim

`d-value` is not reducible to salience, confidence, reward, or preference intensity.

### 2. Layer

Cognitive science / neuroscience / ethics bridge.

### 3. Claim level

P3 bridge claim; P4 when operationalized.

### 4. Nearby theory / competing explanation

Salience, arousal, confidence, reward, utility, attention.

### 5. SRT-specific prediction

High-`d-value` contents should predict downstream reorganization better than salience alone.

### 6. Proxy measurement

- memory persistence;
- action-path change;
- bodily response;
- willingness to bear cost;
- identity-relevance rating;
- later `L_2` sedimentation / habit change.

### 7. Baseline

Salience, confidence, arousal, reward magnitude.

### 8. Expected result if SRT is right

After controlling for salience/confidence/arousal, high-`d-value` items still predict stronger memory persistence, action change, and future decision weighting.

### 9. Failure condition

If salience/confidence/arousal fully explain downstream effects, `d-value` must be narrowed or treated as a redescription rather than an independent construct.

### 10. What would narrow SRT

SRT should restrict `d-value` to contexts involving identity, non-substitutability, or future-selectability rather than all high-priority cognition.

### 11. What would strengthen SRT

If `d-value` proxies predict future action reorganization and memory sedimentation beyond salience and reward.

### 12. Owner file

`_SRT_D_VALUE_CANONICAL.md`, Philosophy ethics guardrails, Neuroscience consciousness mechanisms.

### 13. Current status

Bridge hypothesis; pilot-ready after measure design.

---

## 5. Example package — `Psi_f` vs prediction error

### 1. Claim

`Psi_f` is not reducible to prediction error; it tracks transition cost / selection friction across model, body, and norm layers.

### 2. Layer

Core / information geometry / cognitive science / social theory.

### 3. Claim level

P3 bridge claim; P4 when operationalized.

### 4. Nearby theory / competing explanation

Prediction error, free energy, task difficulty, switching cost, cognitive load.

### 5. SRT-specific prediction

Some transitions with similar prediction error should differ in `Psi_f` because they require different degrees of re-anchoring, identity update, embodied cost, or social norm revision.

### 6. Proxy measurement

- task-switching cost;
- model-update path length;
- hesitation / reaction time;
- error volatility;
- physiological stress;
- resistance to reframing;
- institutional compliance cost;
- cross-operator coordination cost.

### 7. Baseline

Prediction error, objective task difficulty, cognitive load.

### 8. Expected result if SRT is right

Reframing or identity-threatening updates show higher transition friction than prediction error alone predicts.

### 9. Failure condition

If prediction error and task difficulty fully explain all transition costs, `Psi_f` must be narrowed to an interpretive wrapper over existing constructs.

### 10. What would narrow SRT

Separate `Psi_f^inf` from broader `Psi_f^emb` and `Psi_f^norm`; keep Fisher-like cost only in the information-geometric slice.

### 11. What would strengthen SRT

Evidence of layer-specific transition costs that predict behavior beyond prediction error.

### 12. Owner file

`_SRT_PSI_F_CANONICAL.md`, Core24, Philosophy axiom guardrails.

### 13. Current status

Bridge hypothesis; partial operational families identified.

---

## 6. Example package — `L_2` hardening vs ordinary memory

### 1. Claim

`L_2` hardening is not ordinary memory alone; it is reduced local selection cost plus increased global constraint and hysteresis.

### 2. Layer

Core / cognitive science / social theory / institutional theory.

### 3. Claim level

P2/P3 theory claim; P4 when operationalized.

### 4. Nearby theory / competing explanation

Memory, habit, convention, schema, institution, attractor state.

### 5. SRT-specific prediction

A hardened `L_2` should show both automation and constraint: faster local selection but harder global reselection.

### 6. Proxy measurement

- habit automaticity;
- reduced deliberation time;
- resistance to violation;
- hysteresis;
- path dependence;
- backlash when norm is challenged;
- recovery cost after disruption;
- cross-context replication.

### 7. Baseline

Memory strength, habit strength, social convention frequency.

### 8. Expected result if SRT is right

Hardening produces a paired signature: local ease + global rigidity.

### 9. Failure condition

If ordinary memory or habit strength fully explains the pattern, `L_2` should be narrowed to a broader integrative vocabulary rather than a distinct mechanism.

### 10. What would narrow SRT

Treat `L_2` as a cross-domain abstraction over memory/habit/institution unless hysteresis and constraint signatures add explanatory value.

### 11. What would strengthen SRT

Cases where local automation and global rigidity co-vary across neural, cognitive, and social systems.

### 12. Owner file

Core L2 files, Philosophy Foundations Compact Core, Social Economics.

### 13. Current status

Strong bridge claim; proxy-ready.

---

## 7. Example package — subjecthood vs AI self-report

### 1. Claim

AI self-report, memory, or risk coupling is not sufficient for subjecthood.

### 2. Layer

AI / philosophy / consciousness / ethics.

### 3. Claim level

P3/P4 bridge claim.

### 4. Nearby theory / competing explanation

Behaviorism, functionalism, self-report tests, Turing-style evaluation, agent benchmarks.

### 5. SRT-specific prediction

Systems may produce high-quality self-reports while lacking boundary maintenance, cross-time reidentification, counterfactual access, and own-future selectability stakes.

### 6. Proxy measurement

- persistent self-boundary;
- memory continuity;
- counterfactual self-model;
- action ownership;
- cost-bearing over time;
- failure-sensitive self-update;
- ability to preserve or revise own future selectable states.

### 7. Baseline

Self-report quality, task performance, tool use, memory persistence.

### 8. Expected result if SRT is right

Some systems pass self-report and planning tests but fail S4/S5 subjecthood or agency conditions.

### 9. Failure condition

If self-report and task performance fully track all S4/S5 indicators, SRT's stricter threshold may be too conservative.

### 10. What would narrow SRT

Limit SRT's subjecthood threshold to moral / existential subjecthood rather than all functional consciousness.

### 11. What would strengthen SRT

Dissociations between self-report competence and deeper continuity / boundary / stake indicators.

### 12. Owner file

`Philosophy/SRT_Subjecthood_Threshold_Interface.md`, `AI/SRT_AI_03_Consciousness_Framework_CompactCore.md`.

### 13. Current status

Bridge hypothesis; rubric-needed.

---

## 8. Example package — social legitimacy vs institutional stability

### 1. Claim

Institutional stability is not sufficient for social or political legitimacy.

### 2. Layer

Social / political philosophy / ethics.

### 3. Claim level

P3 bridge claim; P4 when case-operationalized.

### 4. Nearby theory / competing explanation

Institutionalism, social construction theory, coordination theory, market efficiency, legal positivism.

### 5. SRT-specific prediction

Stable institutions can remain illegitimate when they export hidden `Psi_f`, block reselection, or separate power from consequence return.

### 6. Proxy measurement

- hidden compliance cost;
- exit cost;
- appeal channel effectiveness;
- burden distribution;
- correction latency;
- affected-agent testimony;
- mismatch between formal participation and actual gate-rule influence.

### 7. Baseline

Institutional stability, efficiency, compliance rate, legal validity.

### 8. Expected result if SRT is right

Some stable and efficient institutions show high hidden friction export and low future-selectability for affected groups.

### 9. Failure condition

If institutional stability and efficiency reliably predict low friction export and high reselection capacity, SRT's legitimacy diagnostics need narrowing.

### 10. What would narrow SRT

Apply friction-export diagnostics mainly to contested or asymmetric institutions.

### 11. What would strengthen SRT

Cases where SRT diagnostics predict institutional failure, resentment, or reform pressure better than stability/efficiency metrics.

### 12. Owner file

`Philosophy/SRT_Social_Political_PH_SS_Guardrails.md`, Social Economics, Political Philosophy.

### 13. Current status

Bridge / case-study ready.

---

## 9. How to use this template in future files

When adding a strong claim, ask:

```text
Can this claim be turned into a validation package?
Does it name its nearby theories?
Does it specify what SRT predicts differently?
Does it name proxies?
Does it name a failure condition?
Does it say what would narrow SRT?
```

If not, label it as:

```text
conceptual proposal / bridge hypothesis / public metaphor / legacy expression
```

rather than empirical claim.

---

## 10. Minimal conclusion

SRT should become harder to dismiss by making every strong claim pay four debts:

```text
comparison debt: what nearby theory already explains;
proxy debt: what can be measured;
failure debt: what would weaken the claim;
narrowing debt: how SRT retreats if the claim fails.
```

This keeps SRT bold without letting it become unfalsifiable.
