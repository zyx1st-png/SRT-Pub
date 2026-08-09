---
id: HOOK-NEURO-NEURAL27-PROSPECTIVE-MEMORY-EVENT-BOUNDARY-HISTORICAL-EFFICACY
patch_id: PATCH-NEURO-NEURAL27-PROSPECTIVE-MEMORY-EVENT-BOUNDARY-HISTORICAL-EFFICACY
type: integration_hook
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
domain: neuroscience_memory_historical_efficacy
status: active
integration_status: pending
landing_ledger:
  - target: "Neuroscience/SRT_Neural_Mechanisms_CompactCore.md"
    state: pending
    blocked_by: "Await next neuroscience compact-core synthesis. Integrate only as a history-use / prospective-control bridge; do not redefine memory, L2, hippocampus, Psi_f or choice."
  - target: "Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md"
    state: pending
    blocked_by: "Future synthesis file is planned but not yet the active owner. Fold NEURAL27 together with N10, N11 and NEURAL25 rather than creating a parallel hardening trunk."
  - target: "Neuroscience/SRT_NEURAL25_EXPERIMENT_PROTOCOL_v0_1.md"
    state: pending
    blocked_by: "Use MEGA-like history-difference replay as an observational/no-report assay only when the next protocol revision opens; preserve NEURAL25's matched-current-state controls and causal-history requirements."
  - target: "Operations/SRT_HISTORICAL_EFFICACY_OPERATIONAL_TEST_2026-08-04.md"
    state: pending
    blocked_by: "Operational protocol is governance-sensitive. Add only as an example distinguishing HEF-2 active history use from HEF-3 admission; do not weaken the causal-carrier or future-organization gates."
---

# NEURAL27 Integration Hook — Prospective memory and event boundaries

## 1. Target documents

```text
Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md
Neuroscience/SRT_NEURAL25_EXPERIMENT_PROTOCOL_v0_1.md
Operations/SRT_HISTORICAL_EFFICACY_OPERATIONAL_TEST_2026-08-04.md
```

## 2. Insert after

### Neural mechanisms CompactCore

Insert after the current `L2 as sedimented selection constraint` section or in the future memory/history subsection after NEURAL25.

### Future N1-N13 synthesis

Place after the rapid-hardening section and before the experimental roadmap:

```text
N10: how recent experience can harden
-> NEURAL27: when/update boundary + prospective history-use readout
-> N11: how accumulated history deforms future reachability
```

### NEURAL25 protocol

Add as a no-report observational assay under the matched-current-state / different-history family.

### Historical efficacy protocol

Use only as a worked example:

```text
same current sensory stream + different episode history -> anticipatory path divergence
```

with an explicit note that this is HEF-2 strong / HEF-3-shaped until causal-carrier and future-organization gates are satisfied.

---

## 3. Suggested native paragraph

> A memory can matter without first becoming a verbal report. In repeated naturalistic viewing, prior episode history can redirect gaze toward a future event location before that event appears. This gives a useful history-difference assay: much of the current sensory stream can be held fixed while the system's prior episode history changes the next perceptual path. The result should be read as evidence that memory can exert prospective control, not as a direct identification of memory with `L2` or of anticipatory gaze with selection itself.

---

## 4. Suggested boundary paragraph

> Event boundaries are best treated as candidate update opportunities rather than choice events. Hippocampal and posterior-medial-network responses around event transitions may indicate moments when recent experience is re-indexed or consolidated for later use, but a context switch, scene cut or surprise can occur without any SRT-grade Real Choice Moment. Boundary processing therefore belongs to the implementation of historical updating, not to the definition of selection.

---

## 5. Suggested table

| Observation | SRT-safe use | Do not infer |
|---|---|---|
| hippocampal/PMN response at event boundaries | candidate update / indexing opportunity | hippocampus = `L2` |
| boundary connectivity predicts later memory | temporal bias in memory formation | every boundary creates durable write-back |
| repeated viewing produces anticipatory gaze | active history-use / prospective path-bias readout | gaze = `T_dir` or real choice |
| sleep strengthens no-report memory expression | report/control dissociation and consolidation window | sleep = `L2` |
| curiosity improves some hippocampal learning | active information-seeking bridge | curiosity = `d` / `Psi_f` / `T_dir` |

---

## 6. Do not include

- `memory is not about the past` as a literal SRT claim;
- `memory = prediction`;
- `memory = L2`;
- `event boundary = real choice moment`;
- `event boundary = BTSP plateau`;
- `prediction error = Psi_f`;
- `anticipatory gaze = T_dir`;
- any claim that a boundary-response measure is already a validated clinical diagnostic;
- any weakening of the HEF causal-carrier gate.

---

## 7. Future synthesis target

Compress NEURAL27 into four pieces when the neural-mechanisms synthesis reopens:

1. one reconstruction guard (`recall != replay`);
2. one event-boundary update-opportunity paragraph;
3. one prospective history-use paragraph centered on anticipatory gaze;
4. one experimental note separating verbal report, active history use and stronger HEF-3 write-back.

Source patch:

```text
Neuroscience/patches/SRT_Neuro_NEURAL27_Prospective_Memory_Event_Boundary_Historical_Efficacy_v0_1.md
```