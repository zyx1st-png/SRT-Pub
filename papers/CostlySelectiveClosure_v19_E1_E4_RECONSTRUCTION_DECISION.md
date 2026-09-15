---
id: CSC-V19-E1-E4-PUBLICATION-RECONSTRUCTION
type: publication_reconstruction_decision
status: draft
canonical: false
target_venue: Artificial Life
supersedes_for_development: papers/CostlySelectiveClosure_v18_ArtificialLife_candidate.md
evidence_base:
  - E1 terminal-vs-restore
  - E2 recoverability gradient
  - E3 consequence-recovery latency
  - E4 consequence-scope mechanism test
---

# Costly Selective Closure v19 — E1–E4 Publication Reconstruction Decision

Date: 2026-09-15

## 1. Why v19 is a reconstruction, not a minor revision

The v18 manuscript was written around the evidence available after E1–E3. Its central empirical framing was that terminality, persistent impairment, and recovery latency did not behave as interchangeable points on a single vulnerability/recoverability axis.

A subsequent independent mechanism audit identified a more specific question:

> when one agent fails, which agents lose future normal action or return-bearing opportunity?

Experiment 4 then tested that question prospectively under a preregistered design. The result was positive but modest:

```text
mean(shared - individual), collapsed over k = 2,5,10 = +0.0299836682
95% paired bootstrap CI                           = [+0.0119520663, +0.0538730310]
two-sided paired sign-flip p                      = 0.0001499925
29/30 collapsed seed contrasts positive
strong-support threshold +0.10                    = NOT MET
```

Therefore v18 is now scientifically incomplete. The publication must not simply append E4 to a manuscript whose title and logic were built before consequence scope became experimentally supported.

## 2. New central question

The new paper should be organized around:

> **How does the scope of failure consequences—who loses future action/return opportunity—interact with terminality and recovery architecture to shape learned cooperation in a survival-coupled artificial-agent system?**

The paper is not a general proof about mortality, vulnerability, shared fate, or life.

## 3. Working title

Preferred working title:

> **Who Bears Failure? Consequence Scope and Terminality in Survival-Coupled Artificial Agents**

Why this title is preferred:

- it states the empirical mechanism question directly;
- it does not claim that all failure is non-dimensional;
- it keeps terminality visible because E4 does not explain E1's full magnitude;
- it avoids centering the CSC brand before the evidence;
- it is aligned with Artificial Life questions of individuality, viability, social dependence, and organizational boundaries without claiming a universal ALife law.

Alternative, weaker title if reviewer-pressure testing finds the preferred title too broad:

> **Consequence Scope Modestly Shapes Cooperation in a Survival-Coupled Multi-Agent Testbed**

## 4. Evidence hierarchy

The manuscript must make the asymmetry among experiments explicit.

### E1 — discovery / strong phenomenon

Status:

```text
NOT PREREGISTERED
strong terminal-vs-restore effect
multiple robustness checks
```

Publication role:

- establishes the phenomenon to be explained;
- does not establish the mechanism by itself;
- must retain the historical two-sample label-permutation analysis plus the later paired sensitivity analysis;
- terminality is a bundled intervention involving shared episode continuation loss, return truncation, trajectory length, and update structure.

### E2 — preregistered construct-boundary test

Status:

```text
positive generalization NOT SUPPORTED
strong +0.10 endpoint effect excluded by CI
```

Publication role:

- shows that persistent internal metabolic impairment alone does not reproduce E1;
- should NOT be used to claim that persistent consequence in general is ineffective;
- construct limitation must be explicit: the manipulation changes ENERGY_GAIN/state trajectories but does not directly remove normal actions, reward-bearing time, or immediate reward.

### E3 — preregistered failed positive prediction / opposite direction

Status:

```text
positive H1 NOT SUPPORTED
negative ordinal association observed
common-state policy probe same direction
```

Publication role:

- establishes that local recovery latency is not a monotonic surrogate for E1 terminality;
- absolute effect must be described as modest/floor-dominated even though the ordinal statistic is strong;
- must disclose the E3 decision-count-dependent update normalization/scaling confound;
- should not be framed as a general law that recovery burden suppresses cooperation.

### E4 — preregistered mechanism discriminator

Status:

```text
Outcome B
H-SCOPE supported / modest
strong +0.10 gate failed
```

Publication role:

- provides the first direct evidence that consequence scope itself matters independently under a non-terminal recovery mechanism;
- weakens the strongest 'only terminality can matter' rival;
- does NOT explain the magnitude of E1;
- gives only mixed support to the asymmetric-victim story;
- weakens the specific E3 update-scaling rival because E4 uses fixed-horizon normalization/scaling.

## 5. Core empirical claim allowed in v19

Allowed:

> In this survival-coupled multi-agent testbed, learned cooperation depends on the architecture and scope of failure consequences. Terminal failure produces a large terminal-versus-restore separation; persistent internal impairment does not reproduce that effect; individual-scoped recovery latency produces an opposite-direction association; and, under the same non-terminal recovery mechanism, sharing failure-triggered action-opportunity loss across both agents produces a small but preregistered positive cooperation effect relative to localizing that loss to the failed agent.

Shorter allowed claim:

> **Who bears failure-triggered future opportunity loss is an empirically relevant variable in this testbed, but it is not sufficient to explain the much larger terminality effect.**

Not allowed:

- failure is universally non-dimensional;
- consequence scope explains E1;
- shared fate causes cooperation generally;
- E4 strongly validates CSC;
- more severe consequences generate more cooperation;
- mortality has been isolated as a biological principle;
- the agents are alive.

## 6. Conceptual contribution after E4

The strongest conceptual contribution is no longer a revised B/M/H/V profile.

The manuscript should distinguish at least six consequence descriptors:

1. **continuity** — does the declared unit continue after failure?
2. **state inheritance** — which internal/history-bearing structures persist?
3. **opportunity loss** — which future actions/interactions/rewards become unavailable?
4. **recovery source** — who or what performs restoration/repair/replacement?
5. **recovery timing** — how much environment/organizational time is consumed?
6. **consequence scope / bearer** — which organizational units lose future opportunity when one unit fails?

E4 provides direct evidence only for item 6 under one recovery mechanism.

The six-item descriptor is a methodological output, not a validated universal ontology.

## 7. CSC's role in v19

CSC should be demoted from article framework to conceptual provenance.

### Retain

- the original question of whether a declared organizational unit bears the cost of maintaining selective organization;
- the declaration rule: organizational unit, boundary, timescale, recovery regime;
- the motivation for asking who bears failure consequences;
- a brief explanation that the original scalar-like V motivated the experimental decomposition and was not preserved unchanged.

### Compress or remove from the main argument

- long standalone exposition of selective breadth B;
- long standalone exposition of maintenance burden M;
- long standalone exposition of historical retention H;
- any suggestion that B/M/H were tested here;
- any implication that CSC is required to interpret ordinary RL termination effects.

Recommended main-text treatment:

> one compact subsection in Introduction/Conceptual Motivation, with fuller CSC material moved to Discussion or supplement if needed.

## 8. Section architecture for v19

### Abstract

Must contain:

- empirical question first;
- E1 strong terminal-vs-restore phenomenon;
- E2 and E3 preregistered failures to generalize it;
- E4 preregistered modest positive scope effect;
- explicit statement that scope does not explain the full E1 magnitude;
- bounded methodological conclusion about consequence architecture/scope.

Do not lead with CSC.

### 1. Introduction

Suggested sequence:

1. artificial-life comparisons require specifying what failure removes and from whom;
2. termination, damage, recovery and reset are not automatically equivalent;
3. E1 discovered a large effect but bundled terminality with shared continuation loss;
4. E2/E3 narrowed the interpretation;
5. E4 directly tested consequence scope;
6. contributions and boundaries.

### 2. Related Work

Keep four literatures separate:

- precariousness/autonomy;
- mortality/reset/termination in artificial agents and RL;
- action availability/recovery;
- social dependence, individuality, and collective consequence where relevant.

Novelty must be phrased as the **controlled E1-E4 decomposition with preregistered unfavorable follow-ups and a preregistered scope discriminator**, not as priority for mortality/precariousness/reset cost.

### 3. Conceptual Motivation and Consequence Descriptor

Compress old CSC section.

Introduce:

```text
unit + boundary + timescale + recovery regime
```

Then define the six consequence questions above, including scope/bearer.

State that the descriptor was revised by the experimental sequence rather than validated by it.

### 4. Experimental Programme

#### 4.1 Common environment

Preserve v18 audited details.

#### 4.2 E1 terminal vs restore

Preserve historical/statistical transparency.

#### 4.3 E2 persistent impairment

Add construct-validity boundary explicitly.

#### 4.4 E3 individual recovery latency

Add update-mechanics caveat explicitly.

#### 4.5 E4 shared vs individual consequence scope

Report preregistration chronology, fixed-horizon anti-confound update, common-state primary endpoint, collapsed latency test, strong-effect gate, and mechanism diagnostics.

### 5. Results

Suggested order:

1. E1 large phenomenon;
2. E2 does not generalize it through internal metabolic impairment;
3. E3 does not generalize it through individual recovery latency and moves opposite in ordinal direction;
4. E4 detects a modest consequence-scope effect;
5. integrated comparison.

Do not order experiments by whether they support CSC.

### 6. Discussion

Core subsections:

- **6.1 What E1 actually establishes**
- **6.2 Internal impairment without direct return/action loss is insufficient in E2**
- **6.3 Individual recovery burden is not equivalent to terminality**
- **6.4 Consequence scope is detectable but modest**
- **6.5 Why terminality remains live**
- **6.6 Consequence descriptor: continuity, inheritance, opportunity loss, recovery source, timing, scope**
- **6.7 Relation to precariousness, artificial mortality and individuality**
- **6.8 Limitations**
- **6.9 Future work / stop rule**

### 7. Conclusion

Must end with:

> artificial-life comparisons should ask not only whether failure is costly or recoverable, but **who loses the future when failure occurs**.

This is a bounded methodological conclusion, not a metaphysical claim.

## 9. Statistical reporting rules for v19

Use manuscript-level precision:

- `p < 0.0001` when values are at the 20,000-resample floor;
- correlations and effect sizes normally 2–3 significant decimal places;
- exact raw values remain in result JSON/audit files.

E1:

- historical two-sample label permutation remains primary historical analysis;
- paired sign-flip remains explicitly post-hoc sensitivity analysis.

E2:

- emphasize the preregistered +0.10 effect exclusion via the endpoint CI rather than treating `p = 0.071` as the main story.

E3:

- distinguish strong ordinal statistic from modest absolute endpoint difference/floor regime.

E4:

- primary collapsed effect about `+0.030`;
- 95% CI about `[+0.012,+0.054]`;
- `p < 0.001` or exact `p = 0.00015` depending house style;
- 29/30 positive collapsed seed effects;
- explicitly state strong +0.10 gate failed;
- latency-specific values are secondary and non-monotonic.

## 10. Figure strategy

Retain an updated E1 design figure.

Replace the v18 E1/E2/E3 evidence figure with an E1-E4 evidence summary that makes different estimands visible and does not visually imply that E1-E4 form one severity axis.

Recommended visual logic:

- panel A: E1 terminal vs restore seed distribution;
- panel B: E2 endpoint contrast / gradient summary;
- panel C: E3 latency/frozen-policy summary;
- panel D: E4 shared-minus-individual collapsed scope contrast plus latency-specific secondary contrasts.

A conceptual diagram may separately show:

```text
failure
-> continuity
-> opportunity loss
-> recovery
-> consequence scope
```

but must not imply a validated causal DAG beyond the experiments.

## 11. Publication stop rule

No E5 is required before reconstructing and reviewing v19.

A new experiment is justified only if reviewer-pressure testing identifies a specific mechanism ambiguity that makes the current bounded claim unpublishable. It is not justified merely because E4's effect is smaller than E1.

## 12. Gate

```text
E1-E4 EVIDENCE BASE = SUFFICIENT FOR MANUSCRIPT RECONSTRUCTION
V18 CENTRAL FRAMING = SUPERSEDED
V19 WORKING TITLE = WHO BEARS FAILURE?
CSC = CONCEPTUAL PROVENANCE / NOT MAIN VALIDATED FRAMEWORK
CONSEQUENCE SCOPE = EMPIRICALLY RELEVANT / MODEST
TERMINALITY = STILL LIVE FOR E1 MAGNITUDE
E5 = NOT REQUIRED
NEXT = WRITE V19 MANUSCRIPT FROM THIS DECISION, THEN RUN INDEPENDENT REVIEWER-PRESSURE TEST
```
