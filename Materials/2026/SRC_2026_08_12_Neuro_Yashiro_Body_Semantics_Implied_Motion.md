---
source_id: SRC-2026-08-12-NEURO-YASHIRO-BODY-SEMANTICS-IMPLIED-MOTION
title: Probing the content of semantic representations in body-selective regions
source_type: peer_reviewed_primary_full_text
domain: Neuroscience
authors: [Ryuto Yashiro, Masataka Sawayama, Ayumu Yamashita, Kaoru Amano]
publication: Imaging Neuroscience, Volume 4, 2026
url: https://doi.org/10.1162/IMAG.a.1309
doi: 10.1162/IMAG.a.1309
date_published: 2026-07-02
date_added: 2026-08-12
evidence_level: peer_reviewed_primary_human_7T_fMRI_behavioral_rating_full_text
reliability_level: high_for_within_dataset_body_feature_correlations_moderate_for_general_mechanistic_inference
srt_relevance: very_high
integration_priority: very_high
related_srt_claims: [high_level_visual_representation, structured_candidate_construction, L1, objectification, action_relevance, relational_representation, representation_stabilization, NEURAL18, NEURAL28, NEURAL30]
tags: [EBA, FBA, NSD, MS-COCO, caption-embedding, MPNet, co-occurrence, NMF, implied-motion, body-size, number-of-people, action-recognition, semantic-representation, relational-candidate]
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
id: SRC-2026-08-12-NEURO-YASHIRO-BODY-SEMANTICS-IMPLIED-MOTION
---

# SourceCard — Yashiro et al. (2026): body-selective cortex, relational scene semantics, and implied human motion

## 0. Provenance status

This card is based on the user-supplied published full PDF of:

- Ryuto Yashiro, Masataka Sawayama, Ayumu Yamashita, and Kaoru Amano (2026), *Probing the content of semantic representations in body-selective regions*, *Imaging Neuroscience*, Volume 4.
- DOI: `10.1162/IMAG.a.1309`.
- Received 2026-02-16; revised 2026-05-23; accepted 2026-06-27; available online 2026-07-02.
- Open access under CC BY 4.0.
- The paper reports behavioral data and analysis code at Figshare (`10.6084/m9.figshare.32348043`) and GitHub (`amano-k-lab/interpret_semrep`).

**Source-location rule used below:** page numbers refer to the published PDF supplied by the user. Load-bearing claims retain section / figure / page anchors because this material supports a P3 bridge.

---

## 1. One-line summary

In human body-selective visual cortex, natural-scene responses are not exhausted by the presence of a human body: model-guided co-occurrence analysis and direct fMRI feature tests identify **implied human body motion**, **number of people**, and **body size** as separable contributors, with implied motion explaining the largest unique cortical fraction for most participants and showing strong category specificity for human bodies over animals or vehicles.

---

## 2. What problem the paper addresses

Traditional category-selective accounts often describe the extrastriate body area (EBA) and fusiform body area (FBA) as regions preferentially responsive to human bodies. The authors begin from a more nuanced literature in which category-selective cortex also carries information about other stimulus dimensions and natural-scene context (PDF p. 1, Introduction).

Recent caption-based encoding work motivates a second problem: full natural-language captions can predict high-level visual responses well, but language-model embeddings mix physical and semantic dimensions in a way that is hard to interpret. Yashiro et al. therefore ask which **interpretable scene properties** contribute to the semantic representations captured by caption-based encoding models (PDF pp. 1–2, Abstract / Introduction).

Their central move is to use **object co-occurrence structure** as an interpretable bridge from caption semantics to predicted EBA response and then to test candidate scene features against actual fMRI responses.

---

## 3. Experimental and analytic pipeline

### 3.1 fMRI dataset

The study uses the Natural Scenes Dataset (NSD): eight participants viewed approximately 9,000–10,000 natural images each during 7T fMRI; 1,000 images were shared across all participants, with an additional 8,000–9,000 unique images per participant (PDF p. 3, §2.1).

EBA and FBA were defined from functional-localizer maps. Because EBA partially overlaps motion-sensitive MT/MST, the authors also defined MT/MST masks and later excluded overlapping EBA vertices when quantifying feature correlations, reducing the risk that an implied-motion result is merely ordinary motion-area contamination (PDF p. 4, §2.1; p. 10–11, §3.3 / Fig. 3).

### 3.2 Caption-based encoding model

Each NSD image has five human captions. Each caption was embedded with `all-mpnet-base-v2` into a 768-dimensional vector, and the five caption embeddings for an image were averaged. Subject-specific fractional ridge models were trained on each participant's 8,000–9,000 unique images and evaluated on the shared 1,000-image held-out set (PDF p. 4, §2.2.1).

The resulting caption-based models predicted mean EBA responses with Pearson correlations of approximately `r = 0.44–0.72` across participants (PDF p. 8, §3.1).

### 3.3 Co-occurrence decomposition

The authors mapped caption nouns into 12 superordinate COCO categories and counted all 66 pairwise co-occurrences. They predicted EBA response for 73,000 captions, sorted captions by predicted response, divided them into 73 groups of 1,000, constructed one co-occurrence matrix per group, and decomposed the resulting `66 x 73` matrix with Bayesian non-negative matrix factorization (PDF p. 5, §2.2.2; Fig. 1 on p. 3).

The optimal decomposition contained three major components corresponding to high, moderate, and low predicted EBA responses (PDF p. 8, §3.1; Fig. 2 on p. 9).

---

## 4. Core findings of the source

### C1. The same broad category label does not determine EBA response magnitude

The high-response component was dominated by `person x sports`, whereas moderate-response components prominently included `person x accessory` and `person x vehicle`. Low-response components were dominated by non-person scene relations such as food / kitchen combinations (PDF pp. 8–9, §3.1; Fig. 2).

Safe source claim:

```text
human body present
!=
fixed EBA response independent of relational scene context
```

The co-occurring category matters.

### C2. `Person x sports` points to latent action-related features, not merely the label “sports”

Visual inspection of representative images led the authors to hypothesize that high-response scenes tend to imply faster human body motion and often contain more people. They also identified possible low-/mid-level confounds: body size, face size, distance from center, and RMS contrast (PDF pp. 9–10, §3.2; Fig. 2).

The six tested features were therefore:

```text
implied body motion
number of people
body size
face size
distance from image center
RMS contrast
```

### C3. Implied motion is a stable behavioral property of static scenes

Five participants rated implied motion from static images on a 1–5 scale. They were explicitly instructed to judge the overall scene context rather than only the semantic category; the paper uses the contrast between a surfer riding a wave and a surfer standing on the shore as an example. Person-image between-participant reliability was high (`Spearman rho = 0.80–0.90`) (PDF pp. 6–7, §2.4; p. 10, §3.2).

Safe source claim:

> A static image can support a reproducible judgment of latent body-motion speed even when no physical motion unfolds on the screen.

### C4. Actual EBA/FBA responses are dominated by three interpretable body-related features

Vertex-wise correlations against actual fMRI responses showed that implied motion, number of people, and body size explained substantially more of EBA/FBA response structure than face size, distance from center, or RMS contrast. In EBA, the largest significant-vertex proportions were for number of people and implied motion. In FBA, implied motion and body size were most prominent (PDF pp. 10–11, §3.3; Fig. 3).

The authors summarize implied motion as the most broadly represented feature across both regions, with number of people relatively more prominent in EBA and body size relatively more prominent in FBA (PDF p. 11, §3.3).

### C5. Implied motion has unique explanatory variance, not merely shared covariance with size or number

Because implied motion, body size, and number of people are not orthogonal, the authors used seven cross-validated linear models and variance partitioning to estimate unique and shared explained variance (PDF pp. 7, 12, §2.5 / §3.4).

Most explainable vertices were best accounted for by a single feature rather than only by shared feature combinations. **Implied body motion uniquely explained the largest fraction of vertices in EBA for 7/8 participants and in FBA for 5/8 participants** (PDF p. 12, §3.4; Fig. 4).

This is stronger than a simple correlation claim.

### C6. The implied-motion effect is category-specific rather than a generic motion signal

To test whether EBA/FBA merely respond to implied motion in any category, the authors collected the same kind of implied-motion ratings for animal and vehicle images. Participants could reliably rate those categories as well, especially vehicles, but the proportion of body-selective vertices significantly correlated with implied motion was substantially smaller for animal and vehicle images than for person images (`Wilcoxon signed-rank T = 0.0, p = 0.007`) (PDF p. 13, §3.5; Fig. 5).

Safe source claim:

```text
generic implied motion
!=
body-selective cortical implied-motion representation
```

Within this dataset, EBA/FBA preferentially represent implied motion tied to **human bodies**.

### C7. The authors interpret EBA as an intermediate feature-construction stage, not a simple body detector

The Discussion suggests that EBA may integrate lower-/mid-level information such as orientation and shape to compute several body-related features that serve as intermediate building blocks for downstream action recognition. The authors connect number of people to social context and body size to physical proximity, while explicitly presenting this broader computational account as a speculation rather than a directly proven circuit mechanism (PDF p. 15, Discussion).

### C8. The three identified features do not exhaust body semantics

The authors explicitly note that their three-feature model does not explain all EBA/FBA vertices. Emotion, social information, and posture are plausible additional dimensions, and distributed multivertex patterns may encode further body information (PDF p. 15, Discussion / limitations).

Safe source claim:

```text
body semantics
superset-of
{implied motion, number of people, body size}
```

not an equality.

---

## 5. Evidence / method assessment

| Component | Method | Strength / caution |
|---|---|---|
| natural-scene neural anchor | NSD 7T fMRI, 8 participants, 9k–10k images/participant | high-quality intensive dataset; population N remains small |
| caption model | 768-D MPNet embeddings + subject-specific fractional ridge | held-out prediction `r ~ 0.44–0.72`; useful but not a direct causal model of neural computation |
| large-scale co-occurrence discovery | 73,000 captions sorted by **predicted** EBA response + Bayesian NMF | strong exploratory scale; initial category components depend on model extrapolation, not measured fMRI for all 73k images |
| candidate-feature construction | visual inspection of representative co-occurrence groups | interpretable but partly exploratory / hypothesis-generating |
| implied-motion rating | 5 raters, 100 person images plus animal/vehicle comparison sets | high reliability for person and vehicle judgments; very small behavioral N, one rater was an author |
| neural feature test | vertex-wise correlation against actual fMRI | directly tests candidate features against measured responses |
| confound control | body size, face size, distance, RMS; EBA vertices overlapping MT/MST excluded | substantially strengthens implied-motion interpretation; does not remove every natural-scene confound |
| unique-contribution test | seven five-fold-cross-validated regression models + variance partitioning | strong within-sample evidence that motion/number/size are partly separable contributors |
| category-specificity test | person vs animal vs vehicle implied-motion correlation | important negative control against a generic-motion account |

---

## 6. Limits

1. **Model-assisted discovery is not direct 73k-image fMRI evidence.** The `person x sports` / co-occurrence structure is discovered by sorting captions according to model-predicted EBA responses. The paper reports that restricting the co-occurrence analysis to the 1,000 measured shared images yields only one component, showing that the large-scale structure depends on encoding-model extrapolation (PDF p. 14, Discussion).
2. **Small behavioral-rating sample.** Implied-motion ratings come from five participants; one was an author. Reliability is high for person images, but generality remains limited.
3. **Exploratory feature selection.** The six candidate features were proposed after inspecting the data-driven co-occurrence patterns and representative images. This is a sensible discovery pipeline but not a fully preregistered confirmatory feature set.
4. **fMRI is correlational.** The study identifies representational associations and unique explained variance, not causal necessity of EBA/FBA for computing implied motion.
5. **Natural-scene residual confounding remains possible.** Size, position, face area, RMS and MT/MST overlap are controlled, but natural images contain many additional correlated properties.
6. **No direct test of affordances, action policies, candidate competition, selection, or stabilization.** The study concerns semantic/feature representation and action-relevant interpretation, not SRT selection dynamics.
7. **No consciousness claim.** EBA/FBA semantic representation in this study must not be identified with conscious access, phenomenality, subjecthood, or bearer formation.
8. **No canonical `L0/L1/L2`, `G_hat_theta`, `d`, or `Psi_f` identification.** These are SRT terms and are not variables in the source.

---

## 7. SRT relevance — evidence and interpretation kept separate

### 7.1 Direct source-supported pressure

The strongest source-backed pressure is:

```text
high-level visual representation
!= isolated category label
```

and, more specifically:

```text
static relational scene
-> reproducibly inferred latent human-body dynamics
-> category-specific cortical representation
```

The paper provides a concrete empirical case in which represented content contains a latent, context-sensitive dynamic property that is not simply the currently instantiated physical motion of the stimulus.

### 7.2 Bounded P3 SRT bridge: structured perceptual candidates

A defensible SRT-side inference is:

> **Perceptual candidates should not be modeled by default as isolated object labels. A candidate may instead be a structured relational state carrying entities, relations, latent dynamics, and action-relevant properties.**

Local bridge notation only:

```text
c_i = <E_i, R_i, D_i, A_i, ...>
```

where:

- `E_i` = currently discriminated entities / bodies;
- `R_i` = scene relations;
- `D_i` = latent / implied dynamics;
- `A_i` = action- or interaction-relevant content.

This notation does **not** define canonical SRT candidate ontology.

### 7.3 Representation-before-stabilization guard

The source also creates a useful wording pressure on the neuroscience slogan `neural selection before representation`.

The authors' own computational speculation assumes that lower- and mid-level information such as orientation and shape is already available to EBA before higher-level body-related features are computed (PDF p. 15, Discussion). Therefore the safe SRT neuroscience reading is:

> **Selection precedes stabilized / committed `L1` representation, not every precursor encoding or provisional representation.**

A safer implementation sequence is:

```text
precursor feature encoding
-> structured candidate construction
-> competition / weighting / gating
-> stabilization / commitment
-> L1
```

Only the first two stages are directly pressured by this source. The selection / gating / stabilization stages are SRT architecture, not findings of Yashiro et al.

### 7.4 Category-conditioned dynamics as a non-additive representation pressure

The person-versus-animal/vehicle result motivates another bounded bridge:

```text
represented dynamic property
may be conditioned by category / body identity
rather than encoded as a context-free scalar
```

This pressures overly atomic feature-list models of candidate content. It does not prove that cortical representation is formally non-compositional.

---

## 8. What this source does not license

Do not write:

- `EBA = L1`;
- `FBA = L1`;
- `EBA/FBA = G_hat_theta`;
- implied motion = future selectability;
- implied motion = affordance;
- number of people = social `d-value`;
- body size = stake;
- action relevance = real choice;
- category specificity = subjecthood;
- static-image inferred dynamics proves that the brain “creates reality” in an ontological sense;
- caption embeddings reveal the brain's native semantic code;
- the paper proves selection-before-representation;
- all representation is relational;
- the three identified features exhaust body semantics.

---

## 9. Suggested patch target

Primary patch:

```text
Neuroscience/patches/SRT_Neuro_NEURAL32_Relational_Candidate_Construction_Implied_Dynamics_v0_1.md
```

Integration hook:

```text
Neuroscience/hooks/NEURAL32_Relational_Candidate_Construction_Implied_Dynamics_Integration_Hook.md
```

Future synthesis targets:

```text
Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
Neuroscience/SRT_Neuro_Predictions_Table.md
Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md
01_Source_Intuition/BOOK/Drafts_26Q/Q02_对象化.md
```

Do not directly edit those owner/body documents in this material pass. The main value here is a P3 candidate-construction / representation-stabilization guard, not a new canonical neural mechanism.
