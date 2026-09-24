---
id: SRT-GRG-CASE2-ENGAGEMENT-VERTICAL-DECOMPOSITION-RESULT-20260924
type: audit
status: draft
date: 2026-09-24
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
research_mode: TEST
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_DECISION_GRG_CASE2_ENGAGEMENT_2026-09-24.md
  - Operations/GRG/Fusion_Cases/SRT_GRG_CASE2_ENGAGEMENT_VERTICAL_DECOMPOSITION_PREREG_2026-09-24.md
  - Operations/Handoffs/SRT_GRG_CASE2_ENGAGEMENT_EXECUTION_HANDOFF_2026-09-24.md
tags: [GRG, Case2, Engagement, RecommenderSystems, TestResult, StopLoss]
---

# Result — prospective case 2: engagement as a bundled optimization object

## 0. Freeze integrity

The target and test were merged to main before source-literature inspection.

Frozen before source inspection:

- target = engagement as an optimization object / metric in recommender and platform systems;
- source-adequacy gate A0–A3;
- strongest baseline families;
- E0–E5 prospective decomposition;
- T1–T6;
- P1–P6;
- positive threshold;
- allowed verdicts;
- §8.1 accounting;
- no-post-result-widening rule.

No target, probe, test, threshold or verdict was changed during execution.

## 1. Source set inspected after freeze

### Industrial engagement objective / metric use

1. Covington, Adams & Sargin (2016), *Deep Neural Networks for YouTube Recommendations*.
   - production-scale candidate generation + ranking;
   - final ranking objective described as generally a function of expected watch time per impression;
   - CTR is explicitly rejected as sufficient because it can favor clickbait while watch time better captures engagement.

2. Yi et al. (2019), *Recommending What Video to Watch Next: A Multitask Ranking System*.
   - large-scale multi-objective ranking;
   - explicitly handles multiple competing ranking objectives and selection bias in user feedback.

3. Zou et al. (2019), *Reinforcement Learning to Optimize Long-term User Engagement in Recommender Systems*.
   - explicitly targets long-term user engagement;
   - distinguishes instant feedback such as clicks / orders from delayed feedback such as dwell time / revisit.

4. Ie et al. (2019), *SlateQ: A Tractable Decomposition for Reinforcement Learning with Recommendation Sets*.
   - explicitly contrasts immediate user engagement with long-term effects on subsequent user behavior;
   - optimizes long-term user engagement / long-term value;
   - models slate-level and item-level value.

### Exposure / selection-bias baseline

5. Schnabel et al. (2016), *Recommendations as Treatments: Debiasing Learning and Evaluation*.
   - logged recommendation data are selection-biased;
   - exposure to an item is treated as an intervention;
   - separates exposure propensity from observed outcome.

6. Chen et al. (2019), *Top-K Off-Policy Correction for a REINFORCE Recommender System*.
   - logged implicit feedback includes clicks / dwell time;
   - explicitly corrects bias induced by previous recommendation policies.

### Long-term / state-change / feedback baseline

7. Chaney, Stewart & Engelhardt (2018), *How Algorithmic Confounding in Recommendation Systems Increases Homogeneity and Decreases Utility*.
   - data generated under recommendations feed back into later recommendation;
   - recommendation policy can alter observed user behavior and utility.

8. Sinha, Gleich & Ramani (2017), *Deconvolving Feedback Loops in Recommender Systems*.
   - recommendation acceptance changes later collaborative-filtering predictions;
   - distinguishes intrinsic preference from recommendation-influenced observations.

9. Xu et al. (2022), *Surrogate for Long-Term User Experience in Recommender Systems*.
   - explicitly states a shift from short-term engagement toward long-term user experience;
   - uses immediate behavior signals as surrogates for longer-term revisiting;
   - validates surrogates in industrial live experiments.

10. Christakopoulou et al. (2021), *Reward Shaping for User Satisfaction in a REINFORCE Recommender*.
    - treats survey-based satisfaction as orthogonal information to engagement / interaction data;
    - uses satisfaction-oriented reward shaping rather than equating engagement with satisfaction.

11. Boutilier, Mladenov & Tennenholtz (2024), *Modeling Recommender Ecosystems*.
    - treats recommender systems as coupled ecosystems involving users, providers, advertisers and other actors;
    - criticizes purely local / myopic user-level optimization and emphasizes long-horizon, multi-actor effects.

12. Burke & Abdollahpouri (2017), *Patterns of Multistakeholder Recommendation*.
    - explicitly treats recommendation as involving multiple stakeholder utilities rather than only a single end-user objective.

## 2. Source-adequacy gate A0–A3

### A0 — mature source family

PASS.

The bounded source family includes mature industrial recommender-system work with explicit ranking objectives, long-term engagement optimization, bias correction, RL, satisfaction / long-term experience, feedback-loop and ecosystem analysis.

### A1 — source-native event / process unit

PASS.

The source family provides source-native units sufficient to distinguish:

```text
recommendation / exposure opportunity
-> predicted response / expected value
-> realized interaction
-> logged reward / metric
-> later user/system state
-> later recommendation / outcome
```

The exact unit varies by model, but the preregistration only required sufficient source-native structure for the declared decomposition.

### A2 — strongest reasonable baseline

PASS.

The preregistered baseline families were all found in mature source work:

```text
exposure / selection bias:
  YES

click / watch / dwell prediction:
  YES

counterfactual / off-policy correction:
  YES

long-term recommendation / sequential decision:
  YES

feedback loops / recommender-induced state change:
  YES

metric alignment / satisfaction / long-term outcome:
  YES

multi-stakeholder / ecosystem recut:
  YES
```

### A3 — actual bundled-object use

PASS.

The source family explicitly uses engagement-related quantities as ranking / optimization targets:

- expected watch time per impression;
- immediate engagement;
- long-term user engagement;
- clicks / dwell time / revisit as reward or feedback signals.

Therefore:

```text
SOURCE_ADEQUACY = PASS
CASE2_COUNT = YES
```

This is prospectively adequate §8.1 case 2.

Its status cannot be changed after the GRG result.

## 3. E0–E5 source realization

### E0 — opportunity / exposure formation

Source-native realization:

- recommendation policy determines which items are shown;
- exposure probabilities create selection bias;
- previous policies determine which feedback becomes observable.

Disposition:

```text
SOURCE-REAL
SOURCE-OWNED
```

### E1 — response propensity under context

Source-native realization:

- models estimate click / response / value conditional on user, item, context and recommendation state;
- ranking position, slate context, user history and policy affect response.

Disposition:

```text
SOURCE-REAL
SOURCE-OWNED
```

### E2 — realized interaction

Source-native realization:

- click;
- watch / dwell;
- order / conversion;
- revisit;
- other logged interaction.

Disposition:

```text
SOURCE-REAL
SOURCE-OWNED
```

### E3 — metric attribution / aggregation

Source-native realization:

- CTR;
- expected watch time per impression;
- weighted ranking objectives;
- multi-objective ranking;
- reward construction for RL.

Disposition:

```text
SOURCE-REAL
SOURCE-OWNED
```

### E4 — downstream state writeback

Source-native realization:

- recommendations alter later user behavior;
- logged policy-induced behavior becomes later training data;
- RL models later user state / long-term value;
- recommendation feedback loops alter later predictions / distributions.

Disposition:

```text
SOURCE-REAL
SOURCE-OWNED
```

### E5 — longer-horizon consequence

Source-native realization:

- long-term engagement;
- revisiting;
- satisfaction;
- long-term user experience;
- ecosystem / stakeholder welfare.

Disposition:

```text
SOURCE-REAL
SOURCE-OWNED
```

## 4. Frozen separation tests T1–T6

### T1 — exposure != preference / propensity

Prediction:

```text
not observed
does not imply
not preferred
```

Source result:

Schnabel et al. explicitly treat exposure as a policy-dependent intervention and correct for selection bias. Off-policy work likewise distinguishes behavior policy from observed feedback.

Verdict:

```text
T1 = PASS AS SOURCE-REAL
SOURCE OWNERSHIP = STRONG
GRG EXTRA PAYOFF = NONE
```

### T2 — propensity != realized interaction

Prediction:

```text
response tendency
!=
realized engagement event
```

Source result:

Ranking models estimate probabilities / expected values while clicks, watch time and other interactions are realized observations. RL / off-policy work also distinguishes expected return / policy value from sampled logged outcomes.

Verdict:

```text
T2 = PASS AS SOURCE-REAL
SOURCE OWNERSHIP = STRONG
GRG EXTRA PAYOFF = NONE
```

### T3 — realized interaction != engagement metric

Prediction:

```text
event occurrence
!=
aggregation / weighting rule used as engagement objective
```

Source result:

YouTube's 2016 ranking work explicitly uses a ranking objective based on expected watch time per impression rather than treating a click as the objective itself. Multi-task ranking explicitly represents multiple objectives. RL work explicitly defines reward functions from observed feedback.

Verdict:

```text
T3 = PASS AS SOURCE-REAL
SOURCE OWNERSHIP = STRONG
GRG EXTRA PAYOFF = NONE
```

### T4 — engagement event != state-changing event

This was the preregistered high-value seam.

Prediction:

> two events can have similar immediate engagement value while differing in how they change later user / model / exposure conditions.

Source result:

Mature work already explicitly distinguishes immediate response from long-term impact:

- SlateQ contrasts immediate engagement with long-term impact on subsequent user behavior;
- RL engagement work separates instant and delayed feedback;
- feedback-loop work studies recommendation-induced changes in later data / behavior;
- long-term experience work studies immediate behavior signals only as surrogates for later outcomes.

Verdict:

```text
T4 = PASS AS SOURCE-REAL
SOURCE OWNERSHIP = STRONG
GRG EXTRA PAYOFF = NONE
```

The prospective seam was real, but not source-missing.

### T5 — metric gain != target-consequence gain

Prediction:

```text
higher engagement metric
-/>
higher justified long-horizon consequence
```

Source result:

This distinction is explicit:

- short-term engagement is distinguished from long-term user experience;
- immediate behaviors are treated as surrogates rather than identical to long-term outcomes;
- satisfaction surveys supply orthogonal information to engagement / interaction data;
- ecosystem work distinguishes myopic engagement from longer-term multi-actor utility.

Verdict:

```text
T5 = PASS AS SOURCE-REAL
SOURCE OWNERSHIP = STRONG
GRG EXTRA PAYOFF = NONE
```

### T6 — grain recut

Prediction:

> event / session / user / cohort / platform cuts can change what the engagement quantity means.

Source result:

The exact preregistered sequence of grains is not standardized in one framework, but mature source work already performs material recuts:

- item -> slate;
- immediate interaction -> long-term user state;
- individual user -> multiple stakeholders;
- local recommendation -> recommender ecosystem.

Verdict:

```text
T6 = PARTIAL / SOURCE-REAL RECUT FAMILY
SOURCE OWNERSHIP = STRONG ENOUGH TO ABSORB GENERIC RECUT CLAIM
GRG EXTRA PAYOFF = NONE ESTABLISHED
```

## 5. Frozen GRG probes P1–P6

### P1 — differential actualisation

Probe result:

The source already distinguishes:

```text
available candidate
-> exposed item
-> predicted response
-> realized interaction
```

The distinction is operationally important for causal / counterfactual learning.

```text
P1:
  SOURCE-OWNED
  NO EXTRA PAYOFF
```

### P2 — foreground / background

Probe result:

The source already models:

- user history;
- item context;
- slate interactions;
- ranking / exposure policy;
- position / selection effects;
- latent user state.

```text
P2:
  SOURCE-OWNED
  NO EXTRA PAYOFF
```

### P3 — retained efficacy

Probe result:

The source explicitly separates immediate interaction from later user / system state and long-term value.

A recommendation can produce an immediate response without the same long-term consequence.

```text
P3:
  SOURCE-OWNED
  NO EXTRA PAYOFF
```

### P4 — consequence reach

Probe result:

The source already distinguishes local interaction from wider propagation through:

- logged training data;
- policy update;
- future exposure;
- long-term user state;
- ecosystem effects.

```text
P4:
  SOURCE-OWNED
  NO EXTRA PAYOFF
```

### P5 — reconstruction / writeback

Probe result:

This is strongly source-owned.

Feedback-loop / algorithmic-confounding work directly studies the fact that recommendation policy changes the observations and behavior from which later policies learn.

```text
P5:
  SOURCE-OWNED
  NO EXTRA PAYOFF
```

### P6 — recut survival

Probe result:

The source contains legitimate recuts across item/slate, short/long horizon, user/stakeholder/ecosystem.

The exact GRG-neutral role family does not produce an additional source-side diagnostic beyond those existing recuts.

```text
P6:
  SOURCE-OWNED / PARTIAL BY SUBFRAMEWORK
  NO EXTRA PAYOFF
```

## 6. Strongest-baseline absorption

The strongest-baseline family collectively already organizes all of the prospectively predicted burdens:

```text
exposure selection
response prediction
realized interaction
reward / metric construction
long-term state transition
feedback / policy-induced data
surrogate mismatch
satisfaction vs engagement
multi-stakeholder / ecosystem effects
```

This is not merely component presence.

Several mature frameworks explicitly organize the critical interfaces:

### Exposure -> observation

Causal / off-policy recommendation work.

### Immediate response -> long-term value

Sequential / RL recommendation work.

### Interaction -> future observation process

Feedback-loop / algorithmic-confounding work.

### Engagement proxy -> long-term user experience / satisfaction

Surrogate and satisfaction-oriented work.

### User-local objective -> ecosystem / stakeholder consequences

Multistakeholder / ecosystem work.

Therefore the prospective decomposition does not expose a target-source seam that the source family lacks.

## 7. Target-source payoff audit

Frozen positive threshold required a source-checkable diagnostic / intervention / negative control / failure boundary not already organized by the mature source.

Candidate payoffs tested:

### Candidate A

> separate exposure opportunity from preference.

Already owned.

### Candidate B

> separate immediate engagement from long-term state change.

Already owned.

### Candidate C

> distinguish metric improvement from satisfaction / long-term user experience.

Already owned.

### Candidate D

> model the recommender as changing its own future observation distribution.

Already owned by feedback-loop / off-policy / ecosystem work.

### Candidate E

> recut engagement across local / system levels.

Already substantially owned by slate / long-horizon / multistakeholder / ecosystem work.

Result:

```text
TARGET-SOURCE EXTRA PAYOFF:
  NONE ESTABLISHED
```

## 8. GRG-label deletion test

Delete:

- differential actualisation;
- foreground / background;
- retained efficacy;
- reach;
- reconstruction / writeback;
- cross-objectification vocabulary.

What remains is a mature recommender-system research programme:

```text
exposure-bias correction
+
response modeling
+
reward / objective construction
+
sequential state transition
+
feedback-loop analysis
+
long-term / satisfaction alignment
+
multi-stakeholder ecosystem analysis
```

No additional source-side burden survives that requires GRG to state.

## 9. Grain-recut test

At least one legitimate recut was required.

Recut used:

```text
single recommendation / item
-> recommendation slate
-> user trajectory
-> multi-stakeholder / ecosystem
```

The source literature already explicitly works across these grains.

The core GRG-predicted separations do not generate a new invariant constraint not already represented in those source-native recuts.

```text
RECUT PAYOFF:
  NONE ESTABLISHED
```

## 10. Primary verdict

From the frozen allowed set:

```text
SOURCE_OWNED_DECOMPOSITION_NO_GRG_GAIN
```

This verdict is not based on the target being inadequate.

The case is source-native adequate and the prospectively predicted seams are real.

The negative result is stronger than a source-inadequacy failure:

> the preregistered role separations were source-real, but mature recommender-system research already owns those separations and the relevant interfaces; no additional target-source payoff survived.

However, **causal credit for generating those preregistered seams is unresolved**.

The preregistration was frozen before explicit source-literature inspection, but it was authored by a language model whose training data may already contain the relevant recommender-system literature. The strongest-baseline categories written into the preregistration also align closely with the later-failed T/P seams.

Therefore this test does **not** establish:

```text
GRG itself caused the successful anticipation of the seams.
```

It establishes only:

```text
the seams were preregistered before explicit retrieval
and were subsequently confirmed as source-real and source-owned.
```

## 11. §8.1 accounting

Because source adequacy A0–A3 passed:

```text
FRR:
  adequate no-gain case 1

ENGAGEMENT / RECOMMENDER CASE:
  prospectively adequate no-gain case 2

§8.1 count:
  2 adequate no-gain cases
```

Per the frozen preregistration:

```text
fusion lane:
  PAUSE / CONTRACT

replacement target:
  NO

third rescue domain:
  NO

post hoc narrower engagement metric:
  NO

GRG v0.4:
  NO
```

This stop-loss consequence is not optional after the result.

## 12. What survives from the fusion programme

The negative result does not make the entire GRG programme empty.

It supports retaining the following **method guards**:

1. source-first reconstruction;
2. no term-to-term mapping;
3. GRG cuts are probes and explananda;
4. prospective role-separation hypotheses must be frozen before source inspection;
5. source adequacy must be declared before outcome interpretation;
6. target-source payoff is required for vertical-gain credit;
7. cross-domain recurrence alone is insufficient;
8. role separation already owned by the target source earns no GRG gain;
9. legitimate recut survival remains useful as a stress test;
10. stop-loss must be allowed to terminate a fusion lane.

These are primarily **method / governance guards** learned from the programme.

They do not by themselves establish that GRG is a superior decomposition tool relative to ordinary causal / systems analysis.

A post-stop-loss no-GRG ablation control is recorded separately to inspect that narrower question; it does not alter this case verdict or §8.1 accounting.

## 13. Scientific status

```text
new recommender-system mechanism:
  NO

new target-source distinction:
  NO

new GRG scientific gain:
  NO

preregistered seams confirmed source-real:
  YES

GRG-specific predictive contribution:
  NOT ESTABLISHED
  (LLM prior-knowledge contamination not controlled in the primary test)

source absorption of those seams:
  YES

GRG scientific distinctiveness from this case:
  NOT ESTABLISHED

governance / test-discipline calibration:
  POSITIVE

GRG as a superior decomposition tool:
  NOT ESTABLISHED

fusion lane:
  PAUSE / CONTRACT
```

## 14. Non-claims

This result does not claim:

- engagement is a bad metric in general;
- recommender research has solved all long-term alignment problems;
- all platforms optimize the same engagement definition;
- no future non-fusion GRG research is possible;
- the GRG programme as a whole is false;
- SRT is refuted;
- no cross-objectification structure can ever be scientifically useful.

It claims only that this prospectively adequate case 2 did not produce GRG-specific target-domain gain under the frozen standard, thereby triggering the predeclared fusion-lane stop-loss.

## 15. LLM-prior-knowledge limitation

This case is prospectively frozen relative to **explicit retrieval**, not relative to the language model's training corpus.

Important limitation:

```text
the model may already have internalized:
  exposure-bias literature;
  long-horizon recommender work;
  feedback-loop research;
  satisfaction / surrogate-objective work;
  multi-stakeholder / ecosystem work.
```

The close alignment between preregistered strongest-baseline categories and the later T/P failures is consistent with that possibility.

Therefore:

```text
“preregistered before web/source retrieval”
!=
“blind to the source literature”
```

This does not weaken:

- source adequacy;
- the primary no-gain verdict;
- §8.1 case-2 counting;
- the stop-loss consequence.

It **does** weaken any positive claim that GRG itself demonstrated superior prospective decomposition.

Future prospective tests executed by an LLM should, where feasible, add at least one of:

1. same-model no-GRG control;
2. author-written predictions frozen before model analysis;
3. a target drawn from genuinely private / unpublished practice unavailable in model training.

## 16. Next route

The next action is not another fusion case.

It is:

```text
independent review
-> if verdict upheld:
     land stop-loss / fusion-lane pause
     contract retained method guards
     leave broader GRG research only outside this exhausted fusion lane
```

No new target may be selected inside this lane without a future explicit author reopening decision that acknowledges the §8.1 stop-loss result.
