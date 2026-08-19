---
id: SRT-AUDIT-AGING01-STAGE1-G4-G5-REVERSIBLE-FORMATION-GATE-2026-08-19
type: methods_gate_audit
status: active
record_stage: gate_close_read_v1
layer: operations
epistemic_layer: experimental
claim_mode: evidence
claim_level: P4-P5
canonical: false
created: 2026-08-19
target_packet: Experiments/SRT_AGING01_Stage1_Intestinal_Organoid_Feasibility_Packet_v0_1.md
target_methods_audit: Operations/Audits/SRT_AGING01_STAGE1_INTESTINAL_ORGANOID_METHODS_READINESS_AUDIT_2026-08-19.md
dependency:
  - Experiments/SRT_AGING01_Recovered_Present_Restored_Future_Protocol_v0_1.md
  - Experiments/SRT_AGING01_Stage1_Intestinal_Organoid_Feasibility_Packet_v0_1.md
  - Operations/Audits/SRT_AGING01_STAGE1_INTESTINAL_ORGANOID_METHODS_READINESS_AUDIT_2026-08-19.md
source_anchors:
  - DOI:10.1038/s41467-024-47124-8
  - DOI:10.1016/j.stem.2023.09.015
  - DOI:10.1016/j.stem.2017.11.001
  - DOI:10.1038/s41556-024-01550-4
tags:
  - aging
  - organoid
  - G4
  - G5
  - washout
  - T1-matching
  - YAP-TAZ
  - TGFB1
  - p53
  - reversible-reprogramming
---

# AGING01 Stage-1 G4/G5 Gate Audit — Reversible Formation and T1 Convergence

> **Question**: does published primary intestinal-organoid work already support a formation manipulation that can (G4) be fully removed before T1 and (G5) permit a reproducible non-trivial present-state overlap between different histories?
>
> **Answer**: no published study yet closes the full G4 + G5 + P2 chain. However, the evidence is no longer symmetric across candidate handles. ECM/YAP-TAZ matrix switching is the strongest G4/G5 engineering-calibration candidate; TGFB1 is a strong G4 / visible-state-persistence control; p53 remains a strong route-control mechanism but weak G4/G5 candidate.

---

## 1. Gate definitions

### G4 — formation manipulation removed

The causal formation intervention must no longer be applied at the T1 comparison.

This means:

```text
external formation condition absent at T1
```

not:

```text
all consequences of the formation condition erased at T1
```

Residual consequences are exactly what the protocol is designed to measure and give to the rich current-state rival.

### G5 — non-trivial T1 overlap

After G4, the two histories must enter a preregisterable overlapping window on the declared present-state panel.

At minimum:

```text
gross morphology / viability;
current damage / death burden;
major regenerative-state composition;
reserve / clonogenicity proxy.
```

A merely common culture medium does not establish G5.

A merely similar morphology does not establish G5.

---

## 2. Candidate A — acute p53 inhibition after irradiation

**Primary source:** Morral et al. 2024, DOI `10.1038/s41467-024-47124-8`.

### What the paper establishes

Morral et al. use `CluCreERT2; Rosa26-LSL-tdTomato; Lgr5-DTR-GFP` organoids and show that p53 is required for proper Clu+ revSC reprogramming after radiation injury. Acute p53 inhibition with Pifithrin-alpha reduces the contribution of Clu-lineage cells to regenerated Lgr5+ crypts. The same study shows endogenous p53 activation is transient through an Mdm2-mediated feedback loop, while continuous p53 activation through Mdm2 inhibition is detrimental to budding, clonogenicity and passage survival.

### G4 verdict

**NOT DEMONSTRATED for the published Pifithrin-alpha formation manipulation.**

In the reported lineage-tracing experiment, organoids are placed into PF-alpha or vehicle conditions at passage after irradiation and then assessed during the subsequent regeneration period. The study does not provide a separate:

```text
PF-alpha exposure
-> complete withdrawal
-> recovery in common medium
-> T1 comparison
```

sequence.

Endogenous p53 itself being transient does not substitute for demonstrating washout of the experimental inhibition.

### G5 verdict

**NOT DEMONSTRATED.**

The experiment is designed to show altered regeneration under p53 inhibition, not convergence of previously divergent histories after the inhibitor is removed.

### Disposition

```text
route-mechanism support = strong
G4 support = absent for the needed design
G5 support = absent
Stage-1B formation-handle status = CONDITIONAL / secondary
```

Do not infer washout feasibility from the drug class or from p53's endogenous kinetics.

---

## 3. Candidate B — single-pulse TGFB1 regenerative reprogramming

**Primary source:** Chen et al. 2023, DOI `10.1016/j.stem.2023.09.015`.

### What the paper establishes

Irradiated intestinal organoids receive a **single 24-hour TGFB1 treatment**. Fetal / regenerative / revival-cell / YAP-associated signatures rise rapidly and remain elevated for at least five days after that single treatment. Morphological effects also remain detectable in the post-treatment period.

### G4 verdict

**GO at the external-intervention level.**

The study explicitly uses a time-limited pulse rather than continuous TGFB1 exposure. Therefore it provides a real precedent for:

```text
transient formation signal
-> signal removed
-> later state still differs
```

### G5 verdict

**FAILS / NOT REACHED within the published five-day observation window.**

The persistence of regenerative markers after the pulse is useful evidence of durable writeback, but it means that a rich T1 panel would still see an obvious current-state difference during the measured interval.

Thus Chen et al. support:

```text
G4 passed
+ history embodied in persistent current state
```

not:

```text
G4 passed
+ current state re-converged
+ later future response still differs
```

### Disposition

```text
G4 control = strong
G5 calibration = negative / unresolved beyond measured window
Stage-0 / visible-carrier control = very strong
Stage-1B matched-present handle = not yet supported
```

This is scientifically valuable because it gives the rich-state rival an obvious carrier family rather than forcing a residual history claim.

---

## 4. Candidate C — ECM/YAP-TAZ reversible state switching

**Primary source:** Yui et al. 2018, DOI `10.1016/j.stem.2017.11.001`.

### What the paper establishes

Yui et al. show that adult intestinal epithelial cells cultured in collagen type I with Wnt support acquire a repairing / fetal-like YAP/TAZ-high state. Cells propagated for multiple passages under collagen conditions can then be **physically transferred back into Matrigel** under adult organoid conditions.

After transfer:

```text
complex adult-like organoid morphology reappears;
Sca1 and Ctgf change back toward the adult condition;
Olfm4 and multiple differentiated-lineage markers are reversibly regulated by the matrix;
```

The authors explicitly interpret the experiment as reversible transition between repair-like and adult epithelial states.

### G4 verdict

**GO.**

The formation condition is physically changed:

```text
collagen / repair-like environment
-> remove cells from collagen
-> replate into Matrigel / adult ENR environment
```

This is a cleaner intervention-removal logic than a persistent small-molecule exposure.

### G5 verdict

**PARTIAL GO — strongest current primary precedent, but not sufficient for AGING01.**

The study demonstrates substantial convergence at morphology and selected transcriptional markers after replating. It therefore proves that a history-producing regenerative-like state can be driven back toward an adult-like current phenotype after the inducing environment is removed.

However, it does **not** demonstrate:

```text
rich Match-2 equivalence;
matched damage burden;
matched reserve / clonogenicity;
matched cell-state composition at the same declared T1;
common later P2 rechallenge;
H x blockade interaction.
```

Therefore this is not a positive AGING01 history-topology result.

### Disposition

```text
G4 = GO
G5 = PARTIAL GO
best current G4/G5 engineering-calibration family = YES
full Stage-1B proof = NO
```

---

## 5. Candidate D — TGFbeta / Hippo redundancy after injury

**Primary source:** Fink et al. 2024, DOI `10.1038/s41556-024-01550-4`.

Fink et al. show transient crypt-localized TGFbeta and Hippo activation after damage and demonstrate that TGFbeta can induce functional Clu+ revSCs from several differentiated lineages. Loss of one arm can be partially compensated; combined interference produces severe regeneration defects.

### Gate value

This study strengthens the biological plausibility of a reversible, compensatory regenerative-control family but does not itself provide a clean:

```text
transient perturbation
-> complete removal
-> current-state convergence
-> common rechallenge
```

sequence.

Disposition:

```text
formation-control family = plausible
G4 direct support = incomplete
G5 direct support = absent
killer-rival value = high because compensatory redundancy is explicit
```

---

## 6. Revised candidate ranking

For **G4/G5 engineering calibration**, not for theoretical importance:

| Rank | Candidate | G4 | G5 | Best role |
|---|---|---|---|---|
| 1 | ECM / YAP-TAZ matrix switch | **GO** | **PARTIAL GO** | best reversible-state / convergence calibration |
| 2 | single-pulse TGFB1 | **GO** | **not reached in tested window** | durable visible-carrier positive control |
| 3 | transient TGFbeta/Hippo route bias | plausible | absent | backup formation family / redundancy rival |
| 4 | PF-alpha p53 inhibition | not demonstrated | absent | route-mechanism evidence, not current G4/G5 leader |

This ranking does not say ECM/YAP is the best aging model. It says it is the cleanest available **methods bridge for the two unresolved gates**.

---

## 7. Revised experimental sequencing

The Stage-1 program should therefore add a dedicated gate-calibration layer before the full injury-history test.

### Stage-1A0 — G4/G5 convergence calibration

Use a published reversible state-switch family such as matrix-driven YAP/TAZ reprogramming.

Purpose:

```text
prove that the laboratory / analysis pipeline can:
1. generate a clear formation-state divergence;
2. remove the formation condition;
3. prospectively identify a T1 overlap window;
4. declare GO / NO-GO without looking at P2.
```

A successful Stage-1A0 does **not** require a later history effect.

In fact:

```text
T1 overlap + no P2 history effect
```

is a useful successful calibration result because it shows the matching procedure can erase a formation effect when the system truly re-converges.

### Stage-1A1 — switching-pressure calibration

Separately calibrate a non-saturating Lgr5-route blockade.

### Stage-1B — full history-topology feasibility

Only then combine:

```text
common injury P1
+ reversible route-bias history H_A/H_B
+ G4 washout
+ G5 preregistered T1 overlap
+ common P2
+ optional blockade
+ rich current-state rival
```

---

## 8. Minimal G4/G5 decision rule

Do not freeze exact dose, duration or assay chemistry from this audit.

For any formation handle, predeclare three phases:

```text
F — formation divergence window
W — withdrawal / return-to-common-condition window
T1 — candidate overlap window
```

### F gate

Require a reproducible route / state difference while the formation condition is active.

### W gate

Require the external intervention to be absent by design before T1.

### T1 gate

Before any P2 outcome is inspected, require overlap on the frozen panel.

Possible decisions:

```text
GO:
  predeclared T1 overlap achieved
  -> proceed to P2

CONDITIONAL GO:
  gross overlap but rich-state divergence remains
  -> exploratory P2 only; no N1 attempt

NO-GO:
  no overlap within the predeclared recovery horizon
  -> retire that formation family
```

Do not lengthen the recovery horizon post hoc until the groups happen to meet.

---

## 9. What would count as a genuine G5 success

G5 is stronger than “the markers moved in the same direction.”

A serious Stage-1B T1 should require, at minimum:

```text
no large viability difference;
no large residual injury/death difference;
predeclared regenerative-state composition within overlap bounds;
predeclared reserve/clonogenicity proxy within overlap bounds;
common P2 deliverable without dose adjustment by history.
```

A richer Match-2 attempt should additionally give transcriptomic / epigenetic / signaling state to the ordinary rival model.

The scientific burden is intentionally asymmetric:

> if current state still visibly differs, call it a current-state explanation first.

---

## 10. Strong negative interpretations

### If matrix/YAP histories fully converge and P2 is identical

Interpretation:

```text
reversible state history did not leave a detectable future disposition under the tested horizon
```

This validates the matching/control architecture and weakens any generic claim that all maintenance history must alter future topology.

### If TGFB1 history continues to predict P2 but T1 signatures remain different

Interpretation:

```text
history effect exists but is not a matched-present result;
persistent current regenerative state remains the default explanation.
```

### If a candidate achieves rich T1 overlap and later P2 differs

Interpretation:

```text
history-conditioned future-response evidence
```

not yet:

```text
history beyond current physical state;
SRT Selection;
Psi_f;
generative reselectability;
aging mechanism.
```

The next job would be carrier localization and frozen-rival comparison.

---

## 11. Current gate disposition

After this close-read:

```text
G4 feasibility in intestinal organoids = ESTABLISHED IN PRINCIPLE
G5 partial convergence feasibility = ESTABLISHED IN PRINCIPLE via ECM/YAP state reversal
G4+G5+common P2 history test = NOT ESTABLISHED
Stage-1 pilot-ready = NO
```

The remaining methodological gap is narrower than before:

> **not “can intestinal organoids ever revert after a transient regenerative state?” — yes, that has a strong primary precedent. The unresolved question is whether a biologically relevant injury-route history can be removed, richly re-converged at T1, and still alter a later route-specific rechallenge.**

That is the correct Stage-1B target.