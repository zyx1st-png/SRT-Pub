---
id: EC-NEURO-EDGE-TIME-SERIES-INTERACTION
type: evidence_card
status: draft_v1
layer: external_convergence
claim_mode: external_convergence
canonical: false
domain: neuroscience_network_neuroscience_systems_neuroscience
evidence_level: E3
target_srt_anchor:
  - T_dir
  - L0_L1_L2
  - d-value
  - Lambda_conjugacy
  - relational_selection
  - reselectability
  - context_sensitive_closure
  - behavior_output_interface
---

# Evidence Card: Edge Time Series as Interaction Terms for Relational Selection and Behavior-Relevant Dynamic Connectivity

This draft card records an external convergence and pressure case from network neuroscience, systems neuroscience, dynamic functional connectivity, and statistical modeling. It is not canonical, not accepted evidence, and not proof of SRT.

The source article is an empirical paper with a clear mathematical operation, multi-species datasets, multiple imaging modalities, and openly available data / code links. Its role here is operational-proxy support for a relational-selection bridge, not direct validation of SRT ontology.

## 1. External finding

Haily Merritt, Amanda Mejia, and Richard Betzel's article, *The dual interpretation of edge time series: Time-varying connectivity versus statistical interaction* (iScience, 2026), argues that `edge time series` have a dual interpretation.

Given two z-scored neural activity time series, `z_i(t)` and `z_j(t)`, the edge time series is calculated as the element-wise product:

```text
r_ij(t) = z_i(t) · z_j(t)
```

This quantity can be interpreted in two ways:

1. as an instantaneous co-fluctuation or time-varying connectivity estimate between neural elements `i` and `j`;
2. as the statistical interaction term in a multilinear model explaining a time-varying behavior or stimulus variable:

```text
y = β_i z_i + β_j z_j + β_ij z_i z_j + β_0 + ε
```

The paper then uses this equivalence to let node activations and edge interactions compete for the same behavioral variance. If `β_ij` remains significant after including `z_i` and `z_j`, the edge / interaction term carries explanatory power beyond isolated node activity.

Empirical findings:

- In larval zebrafish light-sheet imaging, edge interaction terms explain fictive swimming and eye-movement variables above and beyond node activity.
- In human fMRI movie-watching data, edge interaction terms explain time-varying semantic / stimulus annotations above and beyond activity.
- In *C. elegans* light-sheet microscopy during mating behavior, edge interaction terms explain multiple mating-related behavior variables above and beyond neuronal activity.
- Across datasets, interaction patterns are context-sensitive: precisely which edges matter depends on stimulus or behavioral context.
- The authors conclude that time-varying connectivity, at least when operationalized through edge time series, is likely not mere statistical noise.

For SRT, the finding is best treated as a concrete operational bridge for relational selection: pairwise relations among neural elements can explain behavior beyond isolated local activation states.

## 2. Source domain

Network neuroscience / systems neuroscience / dynamic functional connectivity / computational neuroscience / statistical modeling / behavior prediction.

## 3. SRT construct involved

Primary SRT anchors:

- `T_dir`: edge interaction terms provide a candidate direction-readable trace of how relational co-fluctuations bias behavior or time-varying outputs.
- `L0/L1/L2`: the result supports a layered distinction between local activity states, relational interaction surfaces, and higher-order behavior or task structure.
- `d-value`: behavioral relevance is context-sensitive; the importance of a relation depends on current task, stimulus, and behavior, not activation magnitude alone.
- `Λ` / Lambda conjugacy: the same interaction-over-node principle appears across humans, zebrafish, and worms, suggesting a candidate cross-scale structural echo.
- relational selection: behavior-relevant structure is not reducible to individual node states; relational terms carry additional explanatory information.
- reselectability: context-sensitive interaction matrices can be interpreted as transient relational channels through which future behavior becomes selectable or constrained.
- context-sensitive closure: significant relations shift across stimulus or behavioral conditions, suggesting temporary closures rather than fixed static connectivity.
- behavior-output interface: edge terms form an explicit bridge between neural dynamics and time-varying behavioral output.

This card is especially relevant to the SRT claim that selectable reality and behavior cannot be reduced to isolated local state activations.

## 4. Support type

Operational-proxy candidate / structural convergence / bridge-support candidate / pressure case.

The operational contribution is strong because the paper provides:

- a simple mathematical expression for edge time series;
- a direct equivalence between edge time series and regression interaction terms;
- a model in which node activity and edge interaction compete for the same behavioral variance;
- multi-species, multi-modal empirical tests;
- context-sensitivity analyses;
- data and code availability.

The SRT convergence is:

> behaviorally relevant selection is not exhausted by local node activation; relational interaction terms among elements carry additional explanatory power and vary by context.

The pressure case is that the same result may be explained entirely by ordinary statistics and network neuroscience without SRT.

## 5. Evidence level: E0-E5

E3 = operational-proxy candidate.

Reason for E3: unlike a purely conceptual bridge, this paper offers a measurable quantity (`z_i z_j`), an explicit statistical framework, multi-dataset empirical demonstrations, and a clear test of whether relational terms explain behavior above and beyond node states.

Reason not to rate E4: the paper does not test SRT-specific hypotheses directly. It does not measure `d-value`, `Psi_f`, subjecthood, consciousness, foreclosure, or reselectability in SRT's own terms. The reported relationships are explanatory and non-causal. Therefore, the card is E3 draft only.

## 6. Why it matters

This card is important because it gives SRT a concrete, empirical, and mathematically clean interface for the idea that relations matter over and above local states.

The SRT translation is:

> Edge time series provide a candidate operational proxy for relational selection: pairwise co-fluctuation / interaction terms explain time-varying behavior beyond isolated node activity, suggesting that the behavior-relevant interface is relational and context-sensitive.

### 6.1 Relational selection beyond node activation

If behavior can be better explained by node-pair interaction terms than by node activity alone, then the relevant system state is not merely a list of activated elements. It includes how those elements jointly vary in time.

For SRT, this supports the idea that a selected reality slice is not a collection of independent local states, but a relational configuration through which future action becomes possible.

### 6.2 `T_dir` as relational readout

A direction-readable trace need not be attached to one node, region, or scalar activity. It can be encoded in a relation. Edge time series provide one possible family of `T_dir`-like probes: they read how pairwise neural co-fluctuations align with future or concurrent behavioral outputs.

### 6.3 `d-value` as context-sensitive explanatory relevance

The paper shows that interaction patterns vary by stimulus / context. This matters for SRT because `d-value` is not a fixed property of a node or feature. It depends on how a relation contributes to the current system-level task, behavioral constraint, or future option structure.

### 6.4 Cross-scale structural echo

The same modeling logic applies to zebrafish, humans, and worms, despite differences in phylogeny, imaging modality, and spatial scale. For SRT, this makes the paper a candidate bridge to `Λ` / Lambda-conjugacy: similar relational-selection forms can recur across scales without being identical mechanisms.

### 6.5 Context-sensitive closure

Interaction matrices are not static. The relevant relational pattern changes across stimulus conditions and contexts. This supports an SRT-friendly interpretation of closure as temporary, task-sensitive, and reconfigurable rather than fixed once and for all.

## 7. Alternative explanations

The same external findings can be explained without SRT:

- ordinary multilinear regression may explain the effect as statistical interaction;
- network neuroscience may explain the effect as dynamic functional connectivity;
- control theory may explain behavior as state-dependent coupling among neural populations;
- predictive processing / active inference may explain context-sensitive coupling through task-dependent prediction-error minimization;
- dynamical systems theory may explain the result through phase coordination, attractors, or context-dependent trajectories;
- behavioral neuroscience may treat interaction terms as useful predictors without implying any deeper relational ontology;
- statistical models may capture shared variance, confounds, or nonlinearities without identifying causal mechanisms.

The strongest alternative is statistical reduction:

> edge time series may be ordinary interaction terms with explanatory value but no SRT-specific implication for reselectability, ontology, subjecthood, or consciousness.

## 8. What would weaken this

This card should be downgraded toward E2 or E1 if:

- edge interaction terms fail to replicate across additional datasets, tasks, or measurement regimes;
- the explanatory advantage disappears under stronger controls for autocorrelation, motion, hemodynamics, signal leakage, sampling variability, or behavioral convolution choices;
- node activity plus nonlinear transformations explains the same behavioral variance without relational terms;
- edge terms are not stable enough to support subject-level or context-level interpretation;
- significant edges are found to be mainly artifacts of preprocessing, parcellation, or sampling variability;
- intervention studies fail to show that disrupting interaction patterns changes behavior;
- SRT cannot define a measurable distinction between relational selection and ordinary statistical interaction.

The card should be split if future SRT work differentiates fMRI edge dynamics, calcium-imaging co-fluctuations, single-neuron interactions, EEG / MEG fast coupling, and causal effective connectivity into separate empirical classes.

## 9. Boundary: what this does not prove

This card does not establish any canonical SRT definition.

Specifically:

- It does not prove SRT.
- It does not prove that edge time series are causal mechanisms.
- It does not prove that time-varying connectivity causes behavior.
- It does not prove consciousness, subjecthood, qualia, or `d-value`.
- It does not prove `T_dir` in SRT's full canonical sense.
- It does not show foreclosure, concern, or consequence return.
- It does not imply that every statistically significant interaction is an SRT-relevant relation.
- It does not override the distinction between explanatory prediction and causal intervention.

## 10. Upgrade path

Possible next steps:

1. Create a bridge note: edge interaction terms as a neuroscience proxy for relational selection and `T_dir`.
2. Define an SRT lab hypothesis: relational interaction terms should predict option-space shifts better than isolated activation states.
3. Define a causal test: optogenetic, chemogenetic, stimulation, or perturbational disruption of behavior-relevant interaction terms should alter future selectable behavior if the relation is SRT-relevant.
4. Define a context-closure test: interaction matrices should reorganize systematically when task demands or future option structures change.
5. Define a `d-value` test: the same edge should change relevance when the behavioral consequence or future-option cost changes.
6. Pair this card with `CL-NEURO-EDGE-INTERACTION-STATISTICAL-REDUCTION` before any public-facing claim.
7. Keep the card at E3 until SRT-specific hypotheses distinguish relational selection from generic statistical interaction.

## Sources Checked

The following source was checked for this draft. It is used only to support external network-neuroscience and behavior-modeling background, not to establish SRT.

- [S1] Haily Merritt, Amanda Mejia, and Richard Betzel, “The dual interpretation of edge time series: Time-varying connectivity versus statistical interaction,” *iScience* 29, 115949, 2026, DOI: 10.1016/j.isci.2026.115949. Used for the edge time-series / interaction-term equivalence, regression model framework, zebrafish, human movie-watching, and *C. elegans* findings, context sensitivity, limitations, and data / code availability.
