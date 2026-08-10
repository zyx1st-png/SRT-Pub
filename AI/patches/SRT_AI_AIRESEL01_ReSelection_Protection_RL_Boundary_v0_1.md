---
id: SRT-AI-AIRESEL01
-type: bridge_patch
+type: bridge_patch
tags: [AI, ReSelection, Stake, SameBearer, ReinforcementLearning, BoundaryTest]
status: active_v0_1
layer: L1
epistemic_layer: bridge
claim_mode: bridge
claim_level: P3-P4
canonical: false
created: 2026-08-10
dependency:
  - SRT-AI-POSITIONING-NOTE
  - SRT-D-VALUE-CANONICAL
  - PAPER-STAKE-FUTURE-SELECTABILITY-MVP-DECISION
  - PAPER-SELECTIVE-RESYNCHRONIZATION-MVP-SPEC-LOCK-20260710
---

# AIRESEL01 — ReSelection Protection and the Standard-RL Boundary

## 0. Status and evidence provenance

This is a **non-canonical AI bridge / boundary note**. It does not modify canonical `d`, `Psi_f`, Core axioms, subjecthood, consciousness, or the earlier experimental verdicts.

The note consolidates three AI-side empirical pressure tests:

1. the selective-resynchronization program, whose locked Fashion-MNIST MVP ended in NO-GO;
2. the Stake–Future Selectability MVP, whose locked verdict is `UNINTERPRETABLE PROTOCOL` and whose predictive bridge was independently unfavorable;
3. the History-Bearing ReSelection Capacity Experiment (HBRCE), reported by the author as a completed local formal run on branch `codex/history-bearing-reselection-capacity` at the time this note was written, with result commit `9303d888` and preregistration/lock commit `4afd1c75`, not yet pushed when this bridge note was created.

The HBRCE values below therefore record **author-supplied formal-run provenance pending remote publication** rather than a GitHub-visible result at this exact commit. They must be replaced by a direct repository cross-link once that branch is published or merged.

## 1. HBRCE result to preserve

Reported formal design and result:

- 40 master seeds × 4 conditions = 160/160 structural cells passing the frozen manipulation gates;
- immediate OPEN/LOCK reward difference = exactly `0`;
- choice ordering: `P(OPEN|S)=0.684 > P(OPEN|T)=0.568 > P(OPEN|E)=0.497`;
- the ordering held in `40/40` master seeds;
- standard RL value alone reached leave-one-seed-out CV `R^2 = 0.9760`;
- adding the condition block reduced CV `R^2` by `0.00071`;
- the preregistered residual contrasts crossed zero;
- formal verdict: **NARROW**.

The result therefore licenses the narrow statement:

> A history-bearing artificial agent can learn to protect future re-selection capacity when present reward is matched, and same-bearer persistence can systematically alter current OPEN/LOCK behavior; under this implementation, however, ordinary long-horizon RL value already explains essentially all of that behavior, so no independent SRT-specific re-selection-protection effect was identified.

## 2. What this result does and does not show

### 2.1 Positive structural result

The experiment supports an AI-domain structural claim:

```text
current selection
-> persistent change in the same process's future re-selection capacity
-> changed current policy preference
```

This is stronger than merely assigning an `integrity`, `health`, or loss label. The manipulated consequence concerns the agent's future ability to revise, reopen, or form alternative strategies.

### 2.2 The critical reduction result

The same behavior was almost completely captured by ordinary long-horizon RL value. Therefore:

```text
future-option protection
!= evidence for canonical d
!= independent evidence for SRT stake
```

A policy that protects its future re-selection capacity may simply be maximizing expected future return under ordinary reinforcement-learning semantics.

The fact that a consequence returns to the same persistent process is not, by itself, evidence that a new explanatory variable beyond value optimization has appeared.

## 3. Three-experiment boundary

Taken together, the current AI experimental sequence supports the following negative/limiting distinctions:

### 3.1 Adaptive reorganization is not enough

The selective-resynchronization NO-GO showed that a constructed trajectory/reorganization score did not earn stable incremental prediction beyond simpler controls under the locked Fashion-MNIST protocol.

### 3.2 Programmed persistent consequence sensitivity is not enough

The Stake–Future Selectability MVP showed that persistent capability-loss architecture can induce a learned critic sensitivity, but that sensitivity did not robustly predict later adaptability. The locked Reach20 gate also proved unsuitable as a monotonic manipulation validator in all layouts.

### 3.3 Protecting future re-selection capacity is still not enough

HBRCE moved the intervention closer to SRT's own language: choices changed the same agent's later ability to select again, with immediate reward matched. The agent protected that capacity strongly and consistently, but ordinary future-value optimization already explained the effect.

Thus the current empirical boundary is:

```text
adaptive reorganization
!= stake

programmed consequence sensitivity
!= canonical d

future re-selection protection
!= SRT-specific stake
```

## 4. Revised role of AI experiments

The AI line should currently be treated primarily as a **boundary / insufficiency program** rather than a positive definition engine for `d` or real stake.

Artificial systems remain highly useful for asking:

- which structures are insufficient for real stake;
- whether history changes future reachability;
- whether same-bearer consequence return changes policy;
- whether an SRT-looking effect survives reward, value, plasticity, empowerment, and controllability baselines;
- whether a proposed SRT proxy earns genuine incremental explanatory value.

They are currently weaker for establishing positive evidence that a stake is **constitutive rather than assigned**, because the agent's learned value regime is still ultimately produced by an externally specified optimization setup.

This is consistent with the active AI positioning rule: AI is a pressure-test / boundary-test field, and persistence or embodied consequence return opens the stake question without settling it.

## 5. Re-selection capacity remains useful, but at a lower claim level

Let `R` denote an operational re-selection-capacity family: the ability of a history-bearing system to revise a stabilized strategy, reopen previously closed alternatives, and form an effective new selection under held-out change.

At the present evidence level:

- `R` may be measured as a structural/behavioral property;
- a same-bearer loss of `R` may serve as a **simulated stake architecture**;
- preference for preserving `R` may serve as a **re-selection-protection behavior**;
- none of these may be identified with canonical `d` or genuine stake without additional evidence.

Do not collapse `R` into mere reachable-state count, policy entropy, empowerment, or generic plasticity. Those remain required competitor explanations whenever `R` is used experimentally.

## 6. Stronger unresolved question

The remaining SRT-specific question is no longer:

> Will an artificial agent protect future re-selection capacity?

HBRCE indicates that ordinary RL can already do so.

The stronger open question is:

> What makes a loss of future re-selection capacity a **constitutive stake for the bearer**, rather than merely a future cost represented inside an externally specified value function?

This question should be resolved theoretically and/or moved toward systems with endogenous self-maintenance before another ordinary reward-defined AI benchmark is launched.

A useful conceptual ladder for future work is:

```text
assigned objective
-> learned value sensitivity
-> structural re-selection capacity
-> same-bearer re-selection loss
-> constitutive stake
-> stake-governed selection
```

No arrow in this ladder is currently an identity claim.

## 7. Research-line decision

**Current recommendation: PAUSE ordinary reward-defined AI re-selection experiments as a route to positive canonical-`d` evidence.**

Do not launch an HBRCE v2 merely by:

- adding seeds;
- changing architecture;
- changing the re-selection metric;
- tuning reward horizons;
- searching for a residual after the locked NARROW result.

### Named revival triggers

Re-open this AI line only if at least one of the following becomes available:

1. a theoretically defensible architecture in which preservation of re-selection capacity is not trivially reducible to researcher-defined scalar future reward/value;
2. an endogenous self-maintenance or closure criterion whose loss is borne by the continuing system rather than assigned by the evaluator;
3. a cross-domain biological result that supplies an independently motivated operational signature of constitutive stake and can be translated back into AI as a controlled sufficiency test;
4. a preregistered competing-theory design in which SRT predicts a behavior that standard RL value, empowerment, plasticity, and controllability predict differently.

Until a revival trigger is met, further ordinary RL benchmark proliferation should not be treated as priority SRT evidence generation.

## 8. Claim boundary

Allowed:

- HBRCE reports a robust same-bearer ordering in re-selection protection under matched immediate reward.
- Standard long-horizon RL value explains that ordering extremely well under the reported protocol.
- Re-selection protection is therefore not currently an SRT-specific empirical discriminator.
- Artificial consequence/re-selection architectures remain useful negative and boundary tests.
- The constitutive-versus-assigned status of stake remains open.

Not allowed:

- HBRCE validates or refutes canonical `d`.
- AI re-selection capacity is stake by definition.
- same-bearer persistence is sufficient for subjecthood or consciousness.
- ordinary RL's success proves that SRT stake is reducible to reward in biological or subject-level systems.
- a future change of metric may be used post hoc to convert the current NARROW into support.
