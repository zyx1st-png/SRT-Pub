---
source_id: SRC-2026-08-11-NEURO-MENETREY-SEQUENTIAL-DYNAMICS-INTEGRATED-PERCEPT
title: Sequential neural dynamics underlie unconscious integration and conscious perception of visual stimuli
source_type: peer_reviewed_primary_full_text
domain: Neuroscience
authors: [Maëlan Q. Menétrey, Michael H. Herzog, David Pascucci]
publication: PLOS Biology 24(7): e3003894
url: https://doi.org/10.1371/journal.pbio.3003894
doi: 10.1371/journal.pbio.3003894
date_published: 2026-07-06
date_added: 2026-08-11
evidence_level: peer_reviewed_primary_human_EEG_psychophysics_full_text
reliability_level: high_for_within_paradigm_temporal_decoding_moderate_for_consciousness_stage_identification
srt_relevance: very_high
integration_priority: very_high
related_srt_claims: [temporal_integration, postdictive_perception, objectification, L1, conscious_access, report, phase_dependent_eligibility, NEURAL23, NEURAL28, NEURAL29]
tags: [SQM, sequential-metacontrast, EEG, LDA, temporal-generalization, postdiction, unconscious-integration, conscious-percept, occipital, parietal, P300, alpha, object-formation, temporal-closure]
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
id: SRC-2026-08-11-NEURO-MENETREY-SEQUENTIAL-DYNAMICS-INTEGRATED-PERCEPT
---

# SourceCard — Menétrey, Herzog & Pascucci (2026): sequential neural dynamics, unconscious integration, and the integrated percept

## 0. Provenance status

This card is based on the user-supplied published full PDF of:

- Maëlan Q. Menétrey, Michael H. Herzog, and David Pascucci (2026), *Sequential neural dynamics underlie unconscious integration and conscious perception of visual stimuli*, *PLOS Biology* 24(7): e3003894.
- DOI: `10.1371/journal.pbio.3003894`.
- Published: 2026-07-06.
- The article is open access under CC BY. The paper reports that data and analysis scripts are available through Zenodo (`10.5281/zenodo.20729504`).

The load-bearing claims below come from the paper itself. One important endogenous-state result discussed by the authors — prestimulus alpha-band fluctuations predicting whether the first or second vernier dominates a V–AV report — is **cited prior work**, not a result newly established by this experiment. Respiratory and cardiac phase were not measured in the present study.

---

## 1. One-line summary

In the Sequential Metacontrast (SQM) paradigm, physically distinct visual events retain decodable spatiotemporal identity during several hundred milliseconds of unconscious processing even when they are not consciously accessible as separate events; a later transition from an occipital-dominated to a centro-parietal-dominated EEG pattern tracks the shift toward a unified integrated percept, while the exact moment of phenomenal consciousness remains unresolved.

---

## 2. Experimental paradigm

The SQM stream consisted of a central line followed by five progressively displaced flankers. Each display lasted 27.8 ms with a 20.8 ms interstimulus interval; the entire physical sequence lasted 270.8 ms.

Six conditions were used:

```text
NV       no vernier; all lines straight
V0       one vernier at stream onset
V2       one vernier ~100 ms after onset
V4       one vernier ~200 ms after onset
V0-AV2   central vernier + opposite anti-vernier at the second flanker
V0-AV4   central vernier + opposite anti-vernier at the fourth flanker
```

Participants attended the rightward stream and reported the perceived offset direction at the end of each trial. Offset magnitude was individually calibrated with a PEST procedure to produce roughly 70–80% discrimination in single-vernier conditions.

The sample comprised 18 healthy, naive participants aged 18–23 years (9 female). Each participant completed 12 blocks of 96 trials, yielding 1,152 trials total and 192 trials per condition.

---

## 3. Core findings of the source

### C1. Conscious percepts need not preserve the individual events that generated them

With one vernier, participants could report its direction well. With two opposite verniers in the same integration window, performance relative to the first vernier fell to approximately chance. The established SQM literature places the relevant integration window at roughly 290–450 ms; when opposite offsets are separated by more than about 450 ms, they can become separately reportable.

The paper therefore distinguishes:

```text
physical event sequence
!=
final consciously accessible event inventory
```

The current forced-choice task does **not** determine whether V–AV trials produce a perfectly straight percept, a weak residual offset, or trialwise dominance of one vernier. Chance-level performance is not itself a phenomenal description.

### C2. Neural activity preserves event chronology even when conscious access does not

Temporal-generalization LDA decoded single verniers at systematically shifted latencies:

```text
V0 vs NV  -> significant decoding from ~240 ms
V2 vs NV  -> from ~330 ms
V4 vs NV  -> from ~370 ms
```

The shift tracked the true presentation time of the offset. Cross-condition generalization likewise preserved the expected ~100 ms and ~200 ms temporal displacements.

Safe source claim:

> The neural representation retained information about when an individual vernier physically occurred, even though the conscious percept did not separately expose that spatiotemporal event.

This is stronger than merely showing that unseen stimulation affects behavior: the chronology itself remained decodable.

### C3. Two dominant EEG topographic regimes appear sequentially

Decoder activation patterns clustered into two main spatial topographies:

1. an earlier occipital-dominated pattern;
2. a later centro-parietal/parietal-dominated pattern.

Their transition shifted with vernier position (approximately 360 ms for V0, 460 ms for V2, and 570 ms for V4 in the single-vernier contrasts). The authors interpret the earlier pattern as primarily related to unconscious processing of the physical offset and the later pattern as related to the integrated percept / later processing stage.

The source does **not** license an anatomical identity such as:

```text
occipital = unconsciousness
parietal = consciousness
```

The result is a temporal-regime distinction within this paradigm, not a universal brain-region ontology.

### C4. An unreportable second vernier remains neurally distinguishable

In V0-AV2 and V0-AV4, the two opposite offsets were not normally accessible as separate conscious events, yet EEG decoding still distinguished the two-offset conditions from NV.

More importantly, V0-AV2 and V0-AV4 could be distinguished from each other. The distinct spatiotemporal position of the second vernier remained decodable from about 420 ms onward, and this decoding was dominated by the occipital-like pattern.

Safe source claim:

```text
not consciously accessible as a separate event
!=
not neurally represented with event-specific temporal structure
```

### C5. Report-linked information appears later and is parietal-dominated

The authors separately decoded correct versus incorrect reports in the single-vernier conditions. Significant decoding emerged later — around 480 ms for V0, 460 ms for V2, and 570 ms for V4 — and was dominated by the centro-parietal pattern.

This gives a useful stage separation:

```text
event-specific physical / temporal information
-> later integrated-percept / report-associated information
```

It does not prove that the late pattern is consciousness itself.

### C6. P300-like activity is not identified with phenomenal consciousness

The late centro-parietal pattern resembles P300, a component often associated with conscious access. The authors explicitly note, however, that P300 can reflect post-perceptual decision or response-related processing and may be absent in no-report paradigms or for consciously perceived but task-irrelevant stimuli.

Motor execution is unlikely to explain the present late pattern by itself because button responses occurred much later, around 885–920 ms. A post-perceptual interpretation nevertheless remains possible.

The authors therefore place more interpretive weight on the **transition between the two topographies** than on the P300-like state alone.

### C7. The integration / transition timing is flexible rather than a fixed perceptual frame rate

The temporal dynamics were not invariant. When a vernier appeared later in the stream, the latency from physical presentation to significant decoding could shorten, while the durations of the two topographic regimes changed. The authors suggest that the first offset may initiate an integration window while subsequent offsets or stream termination can accelerate the sequence's resolution into a unified percept.

Safe source claim:

> SQM supports a temporally extended but dynamically adjustable processing window, not a universal fixed 300–450 ms consciousness clock.

### C8. The authors favor a two-stage, temporally rich model

The discussion aligns the data with a two-stage model:

```text
Stage 1:
precise event encoding + temporal position
-> high-capacity buffer
-> unconscious integration

Stage 2:
resolution / sense-making over the preceding hundreds of milliseconds
-> coherent integrated representation / percept
```

The paper describes this as compatible with discrete retentional models in which a percept may be momentary yet temporally rich: the percept occurs later than stimulus onset but contains information derived from an extended preceding interval.

### C9. Prestimulus state is a live but not directly tested mechanism in this study

The discussion cites prior work showing that prestimulus alpha-band EEG fluctuations can predict whether the first or second vernier dominates the reported V–AV percept. The authors use this to motivate future frequency-resolved work.

Evidence boundary:

```text
current paper directly tests ERP/decoder dynamics
!=
current paper directly tests alpha-phase causation
!=
current paper measures respiration or cardiac phase
```

---

## 4. Evidence / method assessment

| Component | Method | Strength / caution |
|---|---|---|
| behavioral integration | calibrated SQM psychophysics, 1,152 trials/participant | strong within paradigm; forced choice does not specify exact phenomenal percept |
| event chronology | time-resolved LDA + cross-condition generalization | strong evidence that event timing remains decodable |
| two topographic regimes | forward-model activation patterns + dissimilarity graph + Louvain clustering | useful data-driven group-level regime structure; not proof of two literally discrete states in every individual |
| report-related stage | correct-vs-incorrect LDA | supports later report/percept-associated information; fewer incorrect trials and smaller pseudo-trials |
| statistical control | cluster-based permutation / surrogate analysis, 10,000 permutations | appropriate time-series multiple-comparison control |
| temporal precision | EEG resampled to 100 Hz; 7-sample sliding window (~70 ms effective resolution) | transition numbers are approximate windows, not exact consciousness timestamps |
| individual robustness | participant-level topographic correlations + Cohen's d checks | strengthens group pattern, but clustering itself was performed on group-averaged data |

EEG was recorded with 128 channels at 2,048 Hz, downsampled to 250 Hz for preprocessing, low-pass filtered at 40 Hz, and later resampled to 100 Hz for decoding. Eye/muscle artifacts were handled through epoch/channel rejection and ICA.

---

## 5. Limits

1. **No phenomenal/access separation.** The authors explicitly state that the paradigm is not designed to distinguish phenomenal consciousness from access consciousness; their broad use of “conscious processing” can include post-perceptual decision processes.
2. **No exact consciousness timestamp.** Stimulus-locked decoding or a topographic transition does not imply that conscious experience begins at that instant (“vehicle problem”).
3. **No direct percept reconstruction in V–AV trials.** Forced choice cannot distinguish complete cancellation, weak residual offset, or trialwise winner dynamics.
4. **No respiration / ECG measurement.** Any link to respiratory or cardiac phase is an SRT P4 extension, not a source finding.
5. **Alpha result is cited prior work.** Prestimulus alpha predicting dominance is not a new analysis in this paper.
6. **Small-N / high-trial design.** `N=18` is compensated by intensive within-participant sampling but still limits population generality.
7. **Group-level clustering.** The two-map community structure was derived on group-averaged patterns, though participant-level consistency checks were positive.
8. **Task specificity.** SQM motion and postdictive integration may use longer windows than other perceptual tasks; the authors explicitly reject a fixed universal latency.
9. **P300 ambiguity.** The late centro-parietal signal can include decision/report processing.
10. **No claim about subjecthood, bearer formation, qualia generation, canonical SRT `L2`, `d`, `Psi_f`, or `G_hat_theta`.**

---

## 6. SRT relevance — three evidence layers kept separate

### 6.1 Directly source-supported pressure

The paper supports a neuroscience-facing separation among:

```text
physical event occurrence
!=
event-specific neural representation
!=
separate conscious accessibility
!=
integrated percept-related representation
!=
behavioral report
```

It also supports:

```text
not separately manifest
!=
structureless
```

because the temporal position of an event can remain decodable even when that event is not consciously available as an individual item.

### 6.2 Bounded P3 SRT bridge

The strongest de-materialized bridge is:

> **A manifest percept can be temporally local while its content is temporally thick. The system may preserve a structured history of candidate events that never become separate conscious objects, then resolve that history into a unified object whose identity is not a simple copy of the event list.**

This pressures an overly instantaneous reading of objectification:

```text
A, B, R(A,B), Δt
-> temporally extended integration
-> C
```

where the relation and timing among events can participate in the formation of the final object. This is a P3 object-formation bridge; it is not evidence that the paper has established SRT ontology.

A second bridge is:

```text
current integrated percept O
!=
full generating history H
```

The history may remain causally/representationally structured even after the current percept no longer exposes its elements separately.

### 6.3 P4 SRT extension: endogenous-state-conditioned closure

NEURAL23 already treats respiratory, cardiac, gastric, and neural timing as candidate modifiers of momentary pre-anchoring eligibility. The present paper supplies a distinct downstream window in which event-specific representations are integrated before a unitary percept/report-related state emerges.

A natural combined hypothesis is therefore:

```text
endogenous / embodied temporal state
-> momentary candidate eligibility
-> event-specific encoding
-> structured temporal integration
-> regime transition / closure
-> integrated percept
-> decision / report
```

The paper itself directly supports only the middle sequence. The role of prestimulus alpha comes from cited prior work; respiratory/cardiac conditioning of closure remains an untested SRT P4 prediction.

---

## 7. Suggested patch target

Primary patch:

```text
Neuroscience/patches/SRT_Neuro_NEURAL30_Temporal_Integration_Closure_Object_Formation_v0_1.md
```

Integration hook:

```text
Neuroscience/hooks/NEURAL30_Temporal_Integration_Closure_Object_Formation_Integration_Hook.md
```

Future synthesis targets:

```text
Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md
Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
Neuroscience/SRT_Neuro_Predictions_Table.md
Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md
01_Source_Intuition/BOOK/Drafts_26Q/Q02_对象化.md
```

Do not directly edit those owner/body documents in this material pass. The current neuroscience layer is dormant/frozen and the current book workline defers material-triggered local manuscript rewrites until the material-backflow phase reopens.
