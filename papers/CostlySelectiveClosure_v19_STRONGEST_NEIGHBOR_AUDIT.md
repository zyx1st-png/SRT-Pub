---
id: CSC-V19-STRONGEST-NEIGHBOR-AUDIT
type: publication_novelty_audit
status: active
canonical: false
target_venue: Artificial Life
manuscript: papers/CostlySelectiveClosure_v19_ArtificialLife_candidate.md
---

# Costly Selective Closure v19 — Strongest-Neighbor Audit

Date: 2026-09-15

## 1. Audit question

After E4, can the v19 manuscript claim novelty for the idea that **shared failure consequences promote cooperation**?

Verdict:

```text
NO
```

The surviving contribution must be narrower.

## 2. Tampuu et al. (2017): shared team penalty can induce cooperation

Tampuu et al., *Multiagent cooperation and competition with deep reinforcement learning* (PLOS ONE 12(4):e0172395, 2017), explicitly manipulate the reward scheme in two-agent Pong.

In their fully cooperative condition, whenever the ball leaves play **both players receive a punitive reward regardless of which player missed**. The purpose is to make the agents learn to keep the ball alive jointly. Their broader result is that changing reward structure can move multi-agent learning between competitive and collaborative regimes.

This is a direct prior example of a failure-like event whose consequence is assigned at team scope rather than only to the locally responsible agent.

Therefore v19 must not claim:

- first demonstration that shared consequences can promote cooperation;
- first multi-agent experiment in which one agent's failure affects both agents;
- novelty for the generic principle that team-level penalty changes social policy.

Important difference from v19:

- Tampuu et al. manipulate the **reward assigned to a scoring/conceding event**;
- E4 holds the immediate reward table fixed and manipulates **who temporarily loses normal action opportunity after failure**;
- E4 is a mechanism discriminator nested inside the E1→E2→E3 decomposition rather than a stand-alone reward-sharing experiment.

The difference is meaningful, but it is not grounds for broad priority language.

## 3. Scott & Pitt (2023): cooperative survival and interdependence are established ALife topics

Scott and Pitt, *Interdependent Self-Organizing Mechanisms for Cooperative Survival* (*Artificial Life* 29(2):198–234, 2023), define cooperative-survival situations in which **no one survives unless everyone survives** and study artificial societies facing recurring catastrophe under interdependent resource-management games.

Their work makes two novelty boundaries especially clear:

1. shared survival dependence is already an explicit Artificial Life research object;
2. cooperation under collective survival constraints is already connected to self-organization, governance, resource dependence, and multi-agent interaction.

Therefore v19 must not claim novelty for:

- the idea that individual survival can depend on collective survival;
- the phrase or general concept of cooperative survival;
- the generic claim that shared fate or interdependence can organize cooperation.

Important difference from v19:

- Scott & Pitt study multi-agent cooperative-survival systems with multiple self-organizing mechanisms and collective resource games;
- v19 studies a much smaller matched RL testbed and experimentally decomposes several **failure-transition architectures** while holding much of the learning environment fixed.

## 4. Other already-non-novel components

The manuscript already acknowledges additional close neighbors:

- enactive precariousness and adaptivity;
- organizational life-likeness and dimensional accounts;
- artificial mortality/death states;
- reset/termination effects in reinforcement learning;
- stochastic or restricted action availability.

Accordingly, none of the following should carry novelty:

```text
mortality matters
precariousness matters
termination changes return
reset rules matter
actions can become unavailable
life-likeness can be multidimensional
shared/team consequence can promote cooperation
collective survival can generate interdependence
```

## 5. Surviving empirical contribution

The strongest defensible empirical contribution is the **controlled evidence sequence**, not any one ingredient:

```text
E1 — discovery
terminal vs restore
large policy separation + robustness checks

E2 — preregistered decomposition attempt
persistent internal metabolic impairment
positive generalization NOT SUPPORTED

E3 — separately preregistered decomposition attempt
individual-scoped recovery latency
positive H1 NOT SUPPORTED; opposite ordinal direction

mechanism audit
identifies consequence scope, terminality, victim burden,
and update mechanics as competing explanations

E4 — separately preregistered mechanism discriminator
same non-terminal recovery mechanism
individual vs shared action-opportunity consequence
positive but modest scope effect
```

The unusual value is that the programme **retains the failed E2/E3 tests and lets them revise the theory before E4**, rather than selecting only manipulations that support a preferred CSC interpretation.

## 6. Surviving methodological contribution

A second defensible contribution is the consequence-description discipline that emerged from the evidence:

```text
organizational unit
boundary
timescale
recovery regime

plus failure descriptors:
continuity
state inheritance
opportunity loss
recovery source
recovery timing
consequence scope / bearer
```

This should be presented as a methodological synthesis motivated by the experiment sequence, not as a validated universal ontology and not as priority over all previous multidimensional or organizational approaches.

E4 provides direct experimental support only for the relevance of **consequence scope** under its specific non-terminal forced-recovery mechanism.

## 7. Surviving novelty statement for the manuscript

Recommended novelty language:

> Prior multi-agent work already shows that shared rewards, shared penalties, and collective-survival constraints can promote cooperation. The contribution here is not the generic idea of shared fate. It is a controlled decomposition of a large terminal-versus-restore effect through three prospectively constrained follow-ups: two preregistered generalizations that fail, followed by a preregistered test that changes only the scope of the same non-terminal recovery burden. This sequence identifies consequence scope as a detectable but modest contributor while leaving terminality-specific mechanisms live.

Short version:

> **Novelty lies in the E1–E4 causal decomposition and evidential revision, not in the generic claim that shared consequences support cooperation.**

## 8. Title adjudication

Current working title:

> **Who Bears Failure? Consequence Scope and Terminality in Survival-Coupled Artificial Agents**

Verdict:

```text
KEEP
```

Reason:

- asks a mechanism question rather than asserting priority;
- distinguishes scope from terminality;
- does not say shared consequence is newly discovered;
- is broad enough for Artificial Life but bounded to the tested agent setting.

The subtitle should remain `Survival-Coupled Artificial Agents`, not `Cooperative Survival`, to avoid sounding as though the paper introduces the Scott–Pitt cooperative-survival concept.

## 9. Required manuscript revisions

Before publication readiness:

1. cite Tampuu et al. (2017) explicitly in the social-dependence/consequence-scope related-work section;
2. cite Scott & Pitt (2023) explicitly as an Artificial Life precedent for cooperative survival/interdependence;
3. state that team-level/shared consequence promoting cooperation is not novel;
4. define v19 novelty as the matched E1–E4 decomposition plus preregistered unfavorable follow-ups and E4 scope discriminator;
5. remove unused v18 references that no longer support a live claim;
6. do not claim first demonstration, discovery, or introduction of shared consequence/shared fate/cooperative survival.

## 10. Gate

```text
SHARED CONSEQUENCE AS GENERIC NOVELTY = REJECTED
COOPERATIVE SURVIVAL AS GENERIC NOVELTY = REJECTED
E1-E4 CONTROLLED DECOMPOSITION = SURVIVES
PREREGISTERED THEORY-NARROWING SEQUENCE = SURVIVES
CONSEQUENCE-SCOPE DISCRIMINATOR = SURVIVES / MODEST
CONSEQUENCE DESCRIPTOR = SURVIVES AS METHODOLOGICAL SYNTHESIS
V19 WORKING TITLE = KEEP
MANUSCRIPT NOVELTY LANGUAGE = REVISE BEFORE READINESS
```

## References added by this audit

- Scott, M., & Pitt, J. (2023). Interdependent Self-Organizing Mechanisms for Cooperative Survival. *Artificial Life, 29*(2), 198–234. https://doi.org/10.1162/artl_a_00403
- Tampuu, A., Matiisen, T., Kodelja, D., Kuzovkin, I., Korjus, K., Aru, J., Aru, J., & Vicente, R. (2017). Multiagent cooperation and competition with deep reinforcement learning. *PLOS ONE, 12*(4), e0172395. https://doi.org/10.1371/journal.pone.0172395
