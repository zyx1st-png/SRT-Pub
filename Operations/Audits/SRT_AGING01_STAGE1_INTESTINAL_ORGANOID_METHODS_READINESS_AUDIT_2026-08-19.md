---
id: SRT-AUDIT-AGING01-STAGE1-INTESTINAL-ORGANOID-METHODS-READINESS-2026-08-19
type: methods_readiness_audit
status: active
record_stage: methods_close_read_v1
layer: operations
epistemic_layer: experimental
claim_mode: evidence
claim_level: P4-P5
canonical: false
created: 2026-08-19
target_protocol: Experiments/SRT_AGING01_Recovered_Present_Restored_Future_Protocol_v0_1.md
target_packet: Experiments/SRT_AGING01_Stage1_Intestinal_Organoid_Feasibility_Packet_v0_1.md
dependency:
  - Experiments/SRT_AGING01_Recovered_Present_Restored_Future_Protocol_v0_1.md
  - Experiments/SRT_AGING01_Stage1_Intestinal_Organoid_Feasibility_Packet_v0_1.md
  - Operations/Audits/SRT_AGING01_P4_MODEL_SELECTION_FEASIBILITY_AUDIT_2026-08-18.md
source_anchors:
  - DOI:10.1038/s41586-019-1154-y
  - DOI:10.1038/s41467-024-47124-8
  - DOI:10.1038/s41556-024-01550-4
  - DOI:10.1242/dev.202941
  - DOI:10.1038/s42003-026-09533-x
  - DOI:10.1016/j.jcmgh.2026.101774
  - DOI:10.1038/s41586-026-10258-4
tags:
  - aging
  - organoid
  - intestinal-regeneration
  - methods-readiness
  - revival-stem-cell
  - Lgr5
  - Clu
  - p53
  - TGFbeta
  - blockade
  - repeated-challenge
---

# AGING01 Stage-1 Methods Readiness Audit — Intestinal Organoid Repeated-Challenge Program

> **Purpose**: determine which parts of the Stage-1 intestinal-organoid design are already supported by published primary methods, which are only plausible, and which remain unvalidated. This audit does not authorize wet-lab execution.

## 0. Bottom line

The Stage-1 model family remains viable, but the experimental program should be split into three roles rather than treated as one monolithic assay:

```text
Stage-0 positive-control architecture:
  prior inflammatory history -> durable present carrier -> altered rechallenge response
  goal: validate analysis / rival-localization logic

Stage-1A switching-calibration:
  transient Lgr5-route suppression in organoids
  goal: identify a non-saturating blockade window that stresses route switching without collapsing the culture

Stage-1B history-topology feasibility:
  same P1 injury + transient early regenerative-route perturbation
  -> washout -> T1 overlap audit -> common P2 -> route-specific outcome
  goal: test whether the full Recovered Present / Restored Future grammar can be implemented
```

No current primary paper already executes all three layers together.

---

## 1. Technical requirement matrix

| Requirement | Primary support | Readiness | Interpretation |
|---|---|---|---|
| injury-induced Clu+ revSC route exists | Ayyaz et al. 2019; Morral et al. 2024; Fink et al. 2024 | **GO** | revSC / fetal-like regenerative state is experimentally grounded |
| Clu-lineage can regenerate Lgr5+ compartment | Ayyaz et al. 2019; Morral et al. 2024 | **GO** | route endpoint can be lineage-based rather than marker-only |
| transient p53 activity controls revSC induction / reprogramming | Morral et al. 2024 | **GO as mechanism; CONDITIONAL as formation handle** | p53 is load-bearing for route induction, but the required washout -> T1 overlap -> P2 design was not tested |
| prolonged p53 manipulation preserves viability | Morral et al. 2024 | **NO-GO as default** | sustained p53 activation impaired budding / clonogenicity and caused culture collapse; do not use prolonged p53 activation as the formation history |
| TGFbeta / Hippo can induce or compensate for revSC formation | Fink et al. 2024 | **GO as alternative route-control family** | supports transient morphogen-cue manipulation, but redundancy means single-path perturbation may be compensated |
| Lgr5+ cells can be specifically ablated in intestinal organoids | Lgr5-DTR organoid protocols; Lee et al. 2024; Kirino et al. 2026 | **GO** | blockade is technically established |
| transient Lgr5 ablation can be non-saturating | Lee et al. 2024 | **GO for calibration principle** | short DT pulse markedly reduced Lgr5 while not necessarily causing complete long-term culture loss; exact dose cannot be imported blindly into another line |
| revSC-rich organoids can withstand inflammatory / chemical stress | Kirino et al. 2026 | **GO as route robustness evidence** | useful for route contrast, not evidence that route diversity itself equals generative health |
| durable intestinal inflammatory history can persist outside original tissue environment | Hamdan et al. 2026; Nagaraja et al. 2026 | **GO** | strong Stage-0 positive-control architecture |
| history-positive groups can be fully T1-matched on rich state | not established | **NO EVIDENCE YET** | this is the central unresolved requirement for an AGING01 residual test |
| route-specific P2 difference after rich T1 matching | not established | **NO EVIDENCE YET** | must be generated prospectively |
| H x blockade interaction after T1 matching | not established | **NO EVIDENCE YET** | strongest Stage-1 endpoint remains novel experimental grammar, not known biology |

---

## 2. Ayyaz 2019 — what is actually reusable

Ayyaz et al. identify a rare damage-induced Clu-high revival stem-cell state that expands after irradiation, Lgr5+ CBC ablation, and DSS injury. Clu-lineage descendants can repopulate the Lgr5+ compartment and multiple intestinal lineages.

Methods-level value for AGING01:

```text
CluCreERT2 lineage tracing exists;
Lgr5-associated homeostatic compartment is separable;
injury produces a transient regenerative state;
Clu+ cells are functionally required for efficient regeneration;
Lgr5 depletion and Clu recruitment can be placed in the same regenerative architecture.
```

Limit:

```text
Ayyaz 2019 does not perform recovery -> T1 matching -> common rechallenge.
```

It supplies route identity and lineage architecture, not the repeated-challenge claim.

---

## 3. Morral et al. 2024 — p53 handle is real but narrower than the previous packet implied

Correction: the 2024 p53/revSC paper is **Morral et al.**, not “Moyer 2024”.

The paper uses intestinal organoids carrying:

```text
CluCreERT2;
Rosa26-LSL-tdTomato;
Lgr5-DTR-GFP
```

and tracks Clu-lineage contribution to later Lgr5+ regenerated structures after irradiation.

Key result:

```text
transient p53 activity is required for proper Clu+ revSC reprogramming;
acute p53 inhibition reduces Clu-lineage contribution to regenerated Lgr5+ crypts;
continuous Mdm2 inhibition / prolonged p53 activation impairs budding, clonogenicity and secondary passage.
```

### Readiness consequence

The packet should retain p53 as a **candidate early formation handle**, but should not call it the preferred implementation until one additional feasibility condition is demonstrated:

```text
transient p53 perturbation
-> measurable route divergence
-> complete washout
-> convergence into a non-trivial T1 overlap window
```

The published study does not establish that final step.

Therefore:

```text
p53 mechanism = GO
p53 Stage-1 history manipulation = CONDITIONAL GO
prolonged p53 activation = NO-GO default
```

---

## 4. Fink et al. 2024 — a better backup route-control family

Fink et al. show that damage-induced crypt chromatin remodelling converges on transient TGFbeta and Hippo signalling; TGFbeta can induce functional Clu+ revSC-like states from multiple differentiated lineages, while combined interference with TGFbeta and Hippo causes much stronger regenerative failure than either pathway alone.

Methods implication:

```text
TGFbeta / Hippo are not merely markers;
they are manipulable regenerative-control nodes;
there is built-in compensatory redundancy.
```

This makes them useful for AGING01 in two opposite ways:

1. **formation-history candidate** — transiently bias regenerative route recruitment while preserving the possibility of later recovery;
2. **killer rival** — if redundancy / compensatory control fully explains future route behavior, AGING01 has no extra empirical work.

Do not interpret redundancy itself as generative reselectability.

---

## 5. Lee et al. 2024 + Lgr5-DTR protocols — blockade feasibility is stronger than previously stated

The key new methods result is that intestinal organoids can be subjected to **transient Lgr5+ stem-cell ablation** rather than only chronic ablation.

Lee et al. tested short diphtheria-toxin pulses in Lgr5-2A-DTR organoids and found a window in which Lgr5 expression was substantially reduced while overall organoid survival was not necessarily eliminated at later readout.

This is highly relevant to the AGING01 blockade arm because the desired perturbation is not:

```text
remove Lgr5 route so completely that all cultures die
```

but:

```text
partially / transiently suppress the preferred homeostatic route
-> create demand for alternative route recruitment
-> measure history x blockade interaction
```

Readiness:

```text
Lgr5 blockade concept = GO
non-saturating pulse calibration = GO as a methods objective
exact concentration / pulse duration = UNFROZEN for the chosen line
```

Kirino et al. 2026 independently use Lgr5-DTR-EGFP organoids and show that Lgr5+ CBC deletion can be integrated into a revSC / fetal-reversion experimental context, further strengthening technical compatibility.

---

## 6. Kirino et al. 2026 — route topology is richer than a two-route cartoon

Kirino et al. provide direct evidence for bidirectional and multi-origin regenerative plasticity:

```text
CBC -> revSC;
revSC -> CBC;
enterocyte -> revSC -> CBC.
```

They also show revSC-rich states can be comparatively stress tolerant under 5-FU challenge.

Consequence for Stage-1:

The route model should not be frozen as merely:

```text
Lgr5 route vs Clu route
```

A better minimal representation is:

```text
homeostatic CBC persistence / re-expansion;
fetal-reversion / revSC transition;
differentiated-lineage contribution into revSC/CBC recovery.
```

For the first pilot, only two routes need to be measurable, but the analysis must acknowledge that additional plasticity routes may act as ordinary compensatory rivals.

---

## 7. Hamdan 2026 and Nagaraja 2026 — Stage-0 positive control should be added

Two 2026 primary studies substantially strengthen the “history can persist outside the acute environment” architecture.

### Hamdan et al. 2026 — human UC organoids

Paired organoids derived from previously inflamed versus noninflamed regions of the same UC patients retained distinct chromatin accessibility after long-term propagation. Upon later inflammatory or injury rechallenge, previously inflamed organoids showed altered responses, while also differing in clonogenicity and barrier function.

Interpretation for AGING01:

```text
history effect = supported
complete T1 matching = not supported
known present carrier family = chromatin / stem-cell state
```

Therefore this is ideal for checking whether the analysis pipeline correctly concludes:

> history matters biologically, but the current-state carrier may already exhaust the explanation.

### Nagaraja et al. 2026 — mouse colitis memory

Colonic stem cells retain an inflammation-associated chromatin memory after disease resolution for more than 100 days, propagated cell-intrinsically through stem-cell divisions and linked to later AP-1-biased responses after oncogenic perturbation.

Again, the correct AGING01 use is:

```text
positive control for durable history / causal carrier
!= evidence for history beyond current state
```

These two studies reduce the need to manufacture a “history effect” in Stage-1. The hard problem is now specifically **matched current state + future route topology**, not whether biological history can persist at all.

---

## 8. Revised Stage structure

### Stage-0 — history-positive / carrier-known control

Use existing human or mouse inflammatory-memory organoid logic to validate analysis behavior.

Required outcome:

```text
history label predicts rechallenge response;
rich current epigenetic / functional state captures much or all of that prediction;
pipeline reports localization rather than fake residual novelty.
```

Success criterion:

> The analysis correctly says “history is real but currently embodied.”

### Stage-1A — switching-pressure calibration

Use a compatible Lgr5-DTR organoid system to identify a non-saturating blockade window.

Required outcome:

```text
Lgr5 route measurably suppressed;
organoids remain sufficiently viable;
alternative regenerative-state recruitment is measurable;
blockade does not trivially set Y = death.
```

This is a methods calibration, not the AGING01 test.

### Stage-1B — full history-topology feasibility

Only after Stage-1A:

```text
common P1
-> H_A / H_B early route perturbation
-> washout
-> T1 overlap audit
-> common P2 +/- calibrated blockade
-> route-specific future readout
-> rich current-state rival comparison
```

This is the first point at which the AGING01 residual hypothesis is actually tested.

---

## 9. Formation-history candidate ranking after close-read

### Candidate 1 — transient p53 suppression

**Status:** CONDITIONAL GO.

Pros:
- direct control of revSC induction / reprogramming;
- lineage-trace-compatible model already published.

Cons:
- p53 affects survival / DNA-damage response broadly;
- may make T1 overlap impossible;
- published work does not show later washout normalization and rechallenge.

### Candidate 2 — transient TGFbeta/Hippo bias

**Status:** CONDITIONAL GO / preferred backup.

Pros:
- direct regenerative reprogramming role;
- redundancy may preserve viability;
- may generate route differences without gross irreversible collapse.

Cons:
- redundancy may make route separation weak;
- pathway state itself may remain an obvious rich-current-state carrier.

### Candidate 3 — inflammatory-memory history

**Status:** GO for Stage-0; not preferred for Stage-1B.

Pros:
- durable history already established;
- strong current carrier measurements available.

Cons:
- baseline / current functional differences remain;
- route identity and switching are not the primary published endpoints.

---

## 10. Updated readiness gates

Move the packet from `pre_pilot_design` to `pilot-ready` only if all of the following become true:

```text
G1 chosen organoid line supports route tracing;
G2 chosen line supports calibrated non-saturating route blockade;
G3 formation manipulation produces route divergence;
G4 manipulation is fully withdrawn before T1;
G5 a reproducible T1 overlap window exists;
G6 T1 panel includes damage + composition + reserve / clonogenicity;
G7 P2 is common and non-saturating;
G8 primary route endpoint is lineage-validated;
G9 rich current-state rival is frozen;
G10 biological replicate hierarchy is frozen;
G11 holdout / validation batch is frozen;
G12 methods / biosafety / ethics review is complete.
```

Current status after this audit:

```text
G1: PARTIAL GO
G2: METHODS GO, line-specific calibration pending
G3: supported in principle, implementation pending
G4: not demonstrated for selected formation handle
G5: not demonstrated
G6: design-ready, assays unfrozen
G7: dose / challenge unfrozen
G8: route family supported; exact implementation pending
G9: design-ready
G10: unfrozen
G11: unfrozen
G12: pending
```

Therefore:

```text
pilot-ready = NO
methods-feasible = YES, conditionally
```

---

## 11. Strong stop rules

Stop Stage-1B if any of the following occurs:

1. every route-divergence manipulation necessarily leaves large T1 viability / damage differences;
2. route identity cannot be lineage-validated in the selected line;
3. calibrated blockade still collapses all cultures;
4. rich T1 state fully predicts P2 and H adds no prospective gain;
5. H x blockade is absent under held-out replication;
6. the effect appears only after changing endpoints post hoc;
7. interpretation requires calling route count, Clu fraction or switching cost a canonical SRT variable.

A clean negative result is a successful protocol outcome.

---

## 12. Final disposition

The intestinal-organoid route remains the best **engineering** entry point, but the methods literature now suggests a stricter sequencing:

```text
first prove the pipeline can localize a known history effect to a present carrier;
then calibrate a reversible switching pressure;
only then attempt matched-present / different-history topology.
```

This sharply reduces the risk that AGING01 merely rediscovers epigenetic memory, stem-cell reserve, or ordinary regenerative plasticity under new vocabulary.
