---
source_id: SRC-2026-09-21-TRANSPORT-INDUCED-DEMAND-VARIABLE-DEMAND
id: SRC-2026-09-21-TRANSPORT-INDUCED-DEMAND-VARIABLE-DEMAND
title: "Transport planning — induced demand, fixed versus variable demand, and road-capacity appraisal"
source_type: target_domain_practice_audit
domain: transport_planning_transport_economics
date_added: "2026-09-21"
evidence_level: official_guidance_plus_empirical_synthesis
reliability_level: high_for_target_practice_ownership
srt_relevance: very_high_for_GRG_M4_02_absorption
integration_priority: very_high
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
tags: [GRG, M4, X4b, Transport, InducedDemand, VariableDemand, Absorption]
---

# SourceCard — transport induced demand and variable-demand appraisal

## 1. Audit purpose

This source card was opened only after the M4-02 target/design charter was frozen at commit:

~~~text
32f6279b4af41bdff27a7c681cd81c113e3362dc
~~~

Target:

~~~text
X4b recursive reconstructed-field feedback
-> road-capacity expansion / induced travel
~~~

Frozen candidate transfer:

~~~text
same capacity intervention
+
fixed-demand / no-adaptation control
vs
adaptive demand / route / trip response

measure later erosion / retention of the initial travel-time benefit.
~~~

## 2. UK Department for Transport 2026

Current official research:

~~~text
How additional road capacity affects travel demand
UK Department for Transport
published 28 May 2026
~~~

Public route:

https://www.gov.uk/government/publications/how-additional-road-capacity-affects-travel-demand

The research explicitly assesses:

- how additional road capacity affects travel demand;
- how induced demand alters traffic forecasts;
- implications for appraisal;
- implications for value for money;
- when and why new capacity generates extra travel.

This directly owns the frozen M4-02 target question at policy-appraisal level.

## 3. Australian Transport Assessment and Planning guidance

Official ATAP model-design guidance:

https://www.atap.gov.au/tools-techniques/travel-demand-modelling/3-model

The guidance explicitly distinguishes:

~~~text
Fixed Trip Matrix / fixed demand:
demand independent of cost.

own-cost elasticity:
demand varies with corresponding cost.

Variable Trip Matrix / variable demand:
demand can respond across trip cells and cost cells.
~~~

It states that VTM is required to assess induced demand across changes such as:

- route;
- time of day;
- mode;
- trip redistribution;
- trip generation;
- land use.

The guidance also describes iterative feedback of assignment costs to trip distribution / mode split and notes accessibility-mediated land-use effects.

Therefore the exact M4-02 frozen contrast:

~~~text
fixed demand
vs
adaptive / variable demand after capacity change
~~~

is already standard target-domain model design.

## 4. FHWA benefit-cost practice

FHWA P3 analytical guidance:

https://www.fhwa.dot.gov/ipd/p3/toolkit/analytical_tools/p3_value/user_guide/pt2_ch_5.aspx

The guidance explicitly represents:

~~~text
road capacity increase
-> lower user cost
-> increased volume of trips
~~~

and incorporates induced traffic into user-benefit calculations.

Historical FHWA / Volpe work also incorporated short-run and long-run demand elasticities in highway investment analysis.

## 5. NCST / UC Davis induced travel practice

Public induced-travel resources:

https://travelcalculator.ncst.ucdavis.edu/about.html

https://ncst.ucdavis.edu/research-product/increasing-highway-capacity-induces-more-auto-travel

The source-native approach estimates induced VMT from road-capacity expansion using lane-mile / VMT elasticities and distinguishes short- and long-run responses.

The public material also recognizes route/time changes and longer-run residential / business location effects.

## 6. M4-E0 ownership test

Frozen GRG element:

~~~text
first-order capacity effect
!=
later adaptive demand / route / trip feedback
~~~

Target-domain ownership:

~~~text
STRONG / EXPLICIT
~~~

Frozen GRG control:

~~~text
fixed-demand/no-adaptation
vs
variable/adaptive demand
~~~

Target-domain ownership:

~~~text
STRONG / EXPLICIT
~~~

Frozen GRG variable:

~~~text
later erosion / retention of initial capacity benefit
~~~

Target-domain ownership:

~~~text
STRONG IN SUBSTANCE
~~~

Target field already evaluates induced demand effects on forecasts, appraisal, user benefits and congestion.

## 7. Repository-local ownership

Bounded repository search for:

- induced demand;
- induced traffic;
- road capacity;
- transport demand;
- traffic congestion

found no pre-existing transport-domain matched control equivalent.

Therefore:

~~~text
repository-local absorption = NO / NOT LOCATED
target-domain absorption = STRONG
~~~

Target-domain absorption alone is sufficient for M4-E0.

## 8. Verdict pressure

~~~text
M4-02 target practice pre-ownership = STRONG

duplicate transport simulation / empirical analysis
for the purpose of claiming GRG transfer gain
= NOT WARRANTED
~~~
