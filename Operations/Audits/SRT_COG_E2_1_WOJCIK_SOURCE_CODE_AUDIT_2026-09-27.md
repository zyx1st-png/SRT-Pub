---
id: SRT-COG-E2-1-WOJCIK-SOURCE-CODE-AUDIT-20260927
type: audit
status: active
canonical: false
layer: operations
epistemic_layer: os
claim_mode: source_code_audit
created: 2026-09-27
updated: 2026-09-27
research_mode: U
dependency:
  - Operations/Proposals/SRT_PREOBJECT_COGNITION_E2E4_DISCRIMINATOR_PACKET_2026-09-27.md
tags: [Cognition, NeuralGeometry, Wójcik, SourceAudit, CodeAudit, E2]
---

# COG-E2-1 — Wójcik 2026 source / code audit

> **Purpose:** verify that the first E2 dataset can support a fair held-out geometry duel before downloading / executing the 32.11 GB dataset.
>
> **External code lock:** `m-j-wojcik/pfc_learning@48ada8054940f6a7ac26e8e83d150357a9f249d2` (latest repository commit checked 2026-09-27).
>
> **Canonical impact:** NONE.

## 1. Public package verified

Paper:

Wójcik et al. (2026), *Learning shapes neural geometry in the primate prefrontal cortex*, Nature Neuroscience 29:1966–1975.

DOI: `10.1038/s41593-026-02333-w`

Data:

Dryad `10.5061/dryad.c2fqz61kb`, total listed package size 32.11 GB.

Code:

`m-j-wojcik/pfc_learning`

The code README explicitly supports regeneration of the main figure analyses and identifies:

- time-resolved linear SVM decoding;
- cross-generalisation;
- shattering dimensionality;
- selectivity-space regression;
- cross-stimulus-set generalisation.

## 2. Session structure

From `config.yml`:

### Experiment 1

Womble:

~~~text
17 sessions
2020-09-10 -> 2020-10-02
~~~

Wilfred:

~~~text
10 sessions
2020-10-20 -> 2020-11-03
~~~

With `N_STAGES = 4`, `combine_session_lists(mode='stages')` uses chronological `np.array_split` separately per animal, then combines animal sessions within stage.

Expected session counts per pooled stage:

~~~text
Womble: 5 / 4 / 4 / 4
Wilfred: 3 / 3 / 2 / 2
combined: 8 / 7 / 6 / 6 sessions
~~~

### Experiment 2

Womble:

~~~text
8 sessions
2020-10-05 -> 2020-10-14
~~~

Wilfred:

~~~text
15 sessions
2020-11-04 -> 2020-11-25
~~~

Expected pooled stage counts:

~~~text
Womble: 2 / 2 / 2 / 2
Wilfred: 4 / 4 / 4 / 3
combined: 6 / 6 / 6 / 5 sessions
~~~

## 3. Important analysis implication — no fake longitudinal neuron identity

The code pools sessions into stage-level pseudopopulations.

`get_data_stages`:

- reads session data;
- filters sampled PFC areas;
- stores stage/session data;
- downstream functions construct pseudopopulations across sessions.

Therefore this case must not be narrated as:

~~~text
the same neuron rotates its coding axis across learning.
~~~

The safe unit is:

~~~text
session/stage-level population geometry
and condition/selectivity relations.
~~~

This is a methodological advantage for the present E2 programme because condition geometry can be compared across stage-specific populations without assuming neuron identity.

## 4. Declared analysis windows

From `config.yml`:

~~~text
N_STAGES = 4
N_WINDOWS = 3

EXP1 selectivity window = [140, 150]
EXP1 colour-locked = [50, 150]
EXP1 shape-locked = [100, 150]

EXP2 selectivity window = [70, 100]
EXP2 colour-locked = [50, 100]
EXP2 shape-locked = [100, 150]
~~~

The current first pass should inherit these published windows.

Changing time windows before reproducing the source result would create unnecessary researcher degrees of freedom.

## 5. Task coding

### Experiment 1

Eight conditions factor:

- colour;
- shape;
- width;
- XOR/reward.

The source code explicitly distinguishes an irrelevant interaction term in selectivity analyses.

### Experiment 2

Sixteen conditions factor:

- context;
- task set;
- shape;
- width;
- XOR;
- alternate XOR/task relation.

The code supports:

- ordinary decoding;
- cross-generalisation across task set/context;
- task-1 vs task-2 selectivity vectors;
- cosine-similarity comparisons across tasks;
- shuffled-neuron nulls.

This makes Experiment 2 particularly valuable for held-out structural tests.

## 6. Existing source analysis already pays E1

The original pipeline already measures:

- learning-stage decoding;
- cross-generalisation;
- shattering dimensionality;
- selectivity coefficients;
- early-vs-late geometry;
- Experiment-2 cross-task / cross-context alignment.

Therefore the new execution must **not** claim gain for merely reproducing:

~~~text
geometry changes with learning;
abstraction increases;
cross-generalisation increases;
irrelevant coding decreases.
~~~

Those are source-owned findings / E1.

## 7. First E2 split — revised after code inspection

A fair first split should exploit the factorial structure rather than invent a new post-hoc scalar.

### Training structure

Fit geometry using a subset of relations:

- relevant feature axes available in Experiment 1;
- stage structure;
- within-task condition relations;
- no Experiment-2 cross-task target labels in the first fit.

### Held-out targets

Primary candidates:

1. cross-task-set alignment in Experiment 2;
2. held-out context cross-generalisation;
3. held-out XOR/reward abstraction across task sets;
4. width-irrelevance / normalization relation.

The exact primary/secondary ordering must be frozen in preregistration before data execution.

## 8. Baseline implications from source code

The published pipeline itself already includes strong simple baselines:

- linear decoding;
- shuffled labels;
- shuffled-neuron early/late controls;
- random-vs-structured selectivity-space comparison.

These remain source controls.

They are **not enough** for the new question because the current programme asks whether H3 geometry adds value beyond a strong latent representation account.

Therefore COG-E2-1 must add a fair H2 family.

## 9. H2 baseline freeze recommendation

Preferred first H2 family:

~~~text
cross-validated reduced-rank / factor representation
with task-variable interactions
and session/stage conditioning.
~~~

Reasons:

- interpretable;
- complexity can be matched;
- compatible with pseudopopulation condition structure;
- less likely than a very flexible deep model to turn the first duel into an optimization contest;
- strong enough to absorb low-dimensional geometry if geometry is merely a re-expression of latent coding.

A flexible nonlinear H2 model may be a sensitivity analysis later.

Do not begin with a weak PCA-only straw baseline.

## 10. H3 geometry representation — source-faithful minimum

First H3 should avoid introducing a new field variable.

Use source-faithful geometry objects:

- condition/selectivity vectors;
- cross-validated pairwise distances;
- cosine relations across task representations;
- factorization / abstraction structure.

The H3 claim is only:

> one shared organization of relations predicts several held-out local probes.

No claim of literal neural field.

## 11. Pseudopopulation leakage guard

Because sessions / neurons are pooled into stage-level pseudopopulations, train/test splitting must avoid letting the same source trial or derived pseudo-trial contribute to both sides of a target comparison.

Required preregistration checks:

- split at source-trial / session-aware level where feasible;
- verify pseudo-population construction does not create duplicated information across folds;
- keep Experiment-2 target variables hidden from H3 fitting when they are held-out outcomes;
- report whether pooling across animals changes the result;
- include leave-one-animal-out or animal-stratified sensitivity despite only two animals.

## 12. Two-animal limitation

The neural sample is rich in trials / units / sessions but biological replication is only two animals.

Therefore:

- session-level inference must not be treated as population-level N=number-of-sessions independence;
- report both animals separately;
- pooled pseudopopulation results are organizational evidence, not broad population generality;
- any E2 PASS is dataset-bounded.

## 12.1 Data-package / code naming mismatch — execution blocker

The current Dryad landing page exposes session archives as:

~~~text
m1_ses1.zip ... m1_ses25.zip
m2_ses1.zip ... m2_ses25.zip
~~~

whereas the analysis repository `config.yml` and README use date-labelled session IDs:

~~~text
WomYYYYMMDD
WilYYYYMMDD
~~~

The totals are structurally compatible:

~~~text
Womble = 17 exp1 + 8 exp2 = 25 sessions
Wilfred = 10 exp1 + 15 exp2 = 25 sessions
Dryad m1 = 25 sessions
Dryad m2 = 25 sessions
~~~

But this does **not** authorize guessing:

~~~text
m1 = Womble
m2 = Wilfred
or
sesN = the Nth date in config
~~~

Required before data execution:

1. recover an explicit source mapping from archive contents, source README, metadata or manuscript;
2. verify at least two sessions per animal against trial structure / dates or event metadata;
3. document any rename / symlink adapter;
4. leave original downloaded filenames untouched;
5. fail closed if mapping remains ambiguous.

Disposition:

~~~text
DATA/CODE SESSION-ID MAPPING = OPEN EXECUTION BLOCKER.
~~~

## 13. Compute / storage burden

Dryad total:

~~~text
32.11 GB
~~~

Many session archives are hundreds of MB to >2 GB.

The first local execution should therefore not download the full package blindly.

Recommended preparation:

1. clone source code at the locked commit;
2. inspect Dryad per-session archive manifest;
3. identify minimum sessions needed to reproduce one published E1 result;
4. download a bounded subset first;
5. verify preprocessing / cache generation;
6. only then decide whether full Experiment 1 + 2 download is justified.

## 14. Stage A verdict

~~~text
source availability = PASS
code availability = PASS
factorial structure = STRONG
longitudinal learning structure = STRONG
novel-stimulus generalisation = AVAILABLE
source-owned E1 geometry result = STRONG
E2 held-out duel feasibility = PASS
E3 causal test in this dataset = NO
E4 causal recursion in this dataset = NO / only preliminary lagged structure
full-data immediate download = NO
first execution = bounded reproducibility subset AFTER session-ID mapping is verified
~~~

## 15. Next bounded action

Prepare a preregistration / execution handoff containing:

- one exact E1 reproduction target;
- minimum session subset;
- primary E2 held-out target;
- H1/H2/H3 frozen definitions;
- leakage checks;
- metric + no-gain threshold;
- full-download trigger.

No data execution is authorized by this audit alone.
