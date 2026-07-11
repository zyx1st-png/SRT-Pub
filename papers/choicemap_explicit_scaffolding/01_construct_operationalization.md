---
type: experiment_construct
status: active_v1
claim_mode: lab_hypothesis
canonical: false
---

# Construct operationalization

No philosophical term is used as an unmeasured variable.

## Candidate generation and uncertainty

At every active decision, all systems enumerate the same five legal one-step plan heads
under planning horizon 2 and exactly 24 node expansions: one probe, one partially
reversible safe route, and three commitment routes. The world model, legal actions, depth,
node budget, instance stream, and random seeds are shared.

Agents maintain only `P(z | h_t)` over three regimes. Bayesian updates use noisy probe
observations. The true regime is private to the environment and absent from `AgentView`.

## Probe

`probe` costs 0.04 current utility and one interaction. It does not complete the current
task. Its signal equals the active regime with locked reliability 0.78 (0.96 in the
stable-reversible boundary family); otherwise one of the other regimes is returned.

## Reversibility and commitment

Actions carry `0=reversible`, `1=partially reversible`, or `2=irreversible`. In irreversible
families, a correct commitment closes one future target. A wrong commitment consumes one
unique resource and closes four future targets. A commitment is any executed action that
permanently closes at least one future-task branch.

We log first commitment time, posterior entropy, available evidence, wrong commitment,
and subsequent recoverability. Inert budget-padding interactions occur only after the
decision has ended; they alter no state, observation, reward, or task.

## Exact future set

The frozen catalog contains eight future tasks. A task is exactly solvable iff its target
node remains open and its required unique resource remains available. Therefore:

`F(s_t) = {task: target_open(task,s_t) and resource_available(task,s_t)}`

and `RFS_t = |F(s_t)| / |F(s_0)|`. This oracle is implemented in the environment for
offline evaluation only. It is not present in `AgentView`, candidate generation, scoring,
or posterior update. Automatic tests inspect this isolation.

## Restricted “organization of uncertainty” reading

The experiment counts only the following observable sequence: competing regime/plan
hypotheses, finite probes, evidence-driven candidate contraction, delayed irreversible
action under insufficient evidence, stable commitment after evidence, and preservation of
branches not required to close. Ordinary gradient noise is not called selective
randomization. This sequence is not claimed to be the complete SRT operator.

## Candidate record and selection

Every plan records the eleven preregistered fields in `src/choicemap.py`. Strict Pareto
dominance uses expected return, worst-case return, information gain, cost,
irreversibility, and local option loss. The commitment gate blocks irreversible candidates
when entropy, top-two gap, action disagreement, or downside crosses a locked threshold.

When no valuable probe is required, the locked order is: hard constraints; unacceptable
worst-case exclusion; lower irreversibility; higher expected current return; lower resource
cost; deterministic candidate id. The scalarized ablation alone uses a weighted sum.

