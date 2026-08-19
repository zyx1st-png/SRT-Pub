---
id: SRT-AUDIT-AGING01-PUBLIC-DATA-G5-PRECHECK-2026-08-19
type: public_data_feasibility_audit
status: active
record_stage: closed_v1
closes_into: 03_Bridges/hooks/AGING01_Goal_Directedness_Consensus_Integration_Hook.md
layer: operations
epistemic_layer: experimental
claim_mode: evidence
claim_level: P4-P5
canonical: false
created: 2026-08-19
dependency:
  - Experiments/SRT_AGING01_Recovered_Present_Restored_Future_Protocol_v0_1.md
  - Operations/Audits/SRT_AGING01_STAGE1_G4_G5_REVERSIBLE_FORMATION_GATE_AUDIT_2026-08-19.md
  - Experiments/SRT_AGING01_Stage1_Intestinal_Organoid_Feasibility_Packet_v0_1.md
source_anchors:
  - GSE127172
  - GSE178698
  - GSE178700
  - DOI:10.1016/j.jcmgh.2026.101774
  - DOI:10.1016/j.cell.2019.10.015
  - DOI:10.1016/j.celrep.2021.110283
tags:
  - aging
  - public-data
  - GEO
  - intestinal-organoid
  - repeated-injury
  - G5
  - matched-state
  - feasibility
---

# AGING01 Public-Data G5 Precheck — Can Existing Intestinal Datasets Decide `Recovered Present / Restored Future`?

> **Question**: can existing public intestinal injury / organoid datasets already test the AGING01 Stage-1B residual `rich T1 overlap -> common P2 -> route-specific future difference` without new wet-lab work?
>
> **Verdict**: **NO for the decisive test. YES for calibration / predecessor checks.** Existing datasets strongly establish repeated injury, persistent current-state changes, and history-conditioned future response. They do not provide the combination of rich matched T1, common later rechallenge, and route-specific future endpoints required for the current AGING01 discriminator.

---

## 1. Decision target

The target is **not**:

```text
prior injury changes later recovery
```

That proposition is already established.

The target is:

```text
different prior maintenance / injury-route history
+ predeclared rich T1 overlap
+ same later challenge P2
-> different route identity / probability / switching / bearer distribution
beyond frozen current-state rivals
```

A public dataset can only support a decisive Stage-1B reanalysis if it contains all of the following:

```text
H — known prior history contrast;
T1 — post-history, pre-P2 measurements rich enough for matching / adjustment;
P2 — later common challenge;
Y — route-specific future response rather than only scalar severity;
replication — enough independent biological units for a fair rival-vs-history comparison.
```

---

## 2. Wang et al. 2019 / GSE127172

**Primary study:** Wang et al., *Cell* 2019, DOI `10.1016/j.cell.2019.10.015`.

**Public RNA-seq:** `GSE127172`.

### What the experimental system establishes

The study establishes a long-lived mouse colonic epithelial monolayer system that can cycle through:

```text
homeostatic-like ALI state
-> re-submersion injury
-> Hopx+ / fetal-like regenerative phase
-> re-exposure to ALI
-> homeostatic-like restoration
```

The published figures also show repeated injury / repair cycling, including a second cycle at morphology / marker level.

### What GSE127172 contains

The RNA-seq series contains three sets:

```text
ALI maturation trajectory:
  ALI d0 / d4 / d7 / d14 / d21

early ALI trajectory:
  d0 / d1 / d2

re-submersion injury trajectory:
  Re-Sub 0h (= ALI d21) / 8h / 24h / d7
```

### Critical G5 limitation

The public RNA-seq series does **not** include the later `Re-ALI d14` homeostatic-like restoration state shown by histology / immunostaining in the paper.

Therefore the dataset can estimate:

```text
homeostatic-like -> injury / regeneration transcriptomic movement
```

but not:

```text
prior injury history
-> rich transcriptomic reconvergence after recovery
-> later common rechallenge
```

The second-cycle evidence is morphological / marker-level rather than a rich T1 omics panel.

### Disposition

```text
repeated-cycle plumbing = strong positive precedent
G4 / return-to-common-condition precedent = strong
rich G5 transcriptomic test from public RNA-seq = NO
common P2 after rich T1 = NO
route-specific future distribution = NO
```

Use this dataset for **trajectory / state-space calibration**, not for an AGING01 matched-present residual claim.

---

## 3. Rees et al. 2022 / GSE178698 + GSE178700

**Primary study:** Rees et al., *Cell Reports* 2022, DOI `10.1016/j.celrep.2021.110283`.

**Public data:**

```text
RNA-seq: GSE178698
DNA methylation: GSE178700
```

### What the public RNA-seq design contains

`GSE178698` contains 12 RNA-seq samples from two human colonoid sources / sites, covering:

```text
Day-10 growth;
ALI differentiated d7;
submergence injury round 1, day 3;
submergence injury round 5, day 3;
with or without FliC in the injury conditions.
```

The study shows that repeated injury reduces later regrowth and TLR responsiveness and is associated with mRNA and DNA-methylation changes.

### Why this is a predecessor, not a G5 success

RD1-D3 and RD5-D3 are **injury-state samples**, not a common post-history recovered T1 collected before a separate future P2.

The repeated-injury cultures also show measurable current-state deterioration / reprogramming, including:

```text
reduced regenerative capacity;
reduced inflammatory responsiveness;
transcriptomic change;
DNA-methylation change.
```

Therefore a later response difference is expected to be explainable, at least in part, by current measurable state.

### Replication limitation

The public RNA-seq matrix is valuable for descriptive state-separation analysis, but with only two colonoid sources / sites across the main conditions it is not an adequate basis for a serious same-information-budget held-out comparison between a rich current-state model and a history/topology augmentation.

### Disposition

```text
repeated injury -> altered future response = established predecessor
current molecular writeback = established
rich recovered T1 = absent
common later P2 after T1 = absent
route-specific switching endpoint = absent
decisive held-out AGING01 comparison = NO
```

Use these data to test whether the analysis pipeline correctly recognizes **visible current-state separation**, not to infer history beyond current state.

---

## 4. Hamdan et al. 2026 — human UC organoid inflammatory memory

**Primary study:** Hamdan et al., *Intestinal Stem Cells From Patients With Inflammatory Bowel Disease Retain an Epigenetic Memory of Inflammation*, *Cellular and Molecular Gastroenterology and Hepatology* (2026), DOI `10.1016/j.jcmgh.2026.101774`.

### What it adds

Patient-derived organoids from previously inflamed regions retain chromatin accessibility differences during long-term culture. Most genes associated with the primed chromatin are not constitutively upregulated, and inflammatory / injury rechallenge elicits altered future responses.

This is a strong architecture precedent for:

```text
past inflammation
-> durable present carrier
-> later common challenge
-> altered future response
```

### Why it is still not rich G5

The prior-inflamed organoids also show measurable current functional differences, including reduced clonogenicity and impaired barrier function.

Therefore:

```text
future-response difference
```

cannot be treated as arising after a fully matched present.

The chromatin state itself is also an explicit present causal carrier and belongs in the ordinary rival model.

### Disposition

```text
Stage-0 history-positive / carrier-known control = excellent
rich matched-present residual = NO
```

---

## 5. What a public-data analysis can still do

Although no existing dataset closes Stage-1B, three useful low-cost analyses remain legitimate.

### 5.1 State-separation sanity check

For `GSE178698` / `GSE178700`:

```text
quantify whether RD1 vs RD5 are already separated in transcriptomic / methylation state;
identify whether repeated-injury future deficits co-occur with obvious current-state changes.
```

Expected interpretation:

```text
if clearly separated:
  confirms current-state rival is strong;
  does not test matched-present residual.
```

### 5.2 Trajectory calibration

For `GSE127172`:

```text
map ALI homeostasis -> re-submersion injury / regeneration trajectory;
identify marker panels that are maximally sensitive to regenerative-state divergence;
```

This can help design a future T1 panel but cannot establish T1 reconvergence after injury because the required Re-ALI recovery transcriptome is missing.

### 5.3 Positive-control analysis

For the Hamdan et al. 2026 UC inflammatory-memory dataset, if public data and metadata permit:

```text
show that current chromatin features carry information about later response;
verify that the analysis framework attributes explanatory power to present carriers before adding H.
```

This is a test of **methodological honesty**, not SRT novelty.

---

## 6. Public-data stop rule

Do **not** claim a P4-N1 result from existing public intestinal datasets unless a dataset is found that has:

```text
post-history recovered T1;
rich current-state measurements at T1;
a later common P2;
route-specific response endpoints;
adequate independent biological replication.
```

If one of these is absent, classify the result as:

```text
trajectory evidence;
current-state writeback evidence;
rechallenge / memory evidence;
or feasibility calibration.
```

not:

```text
matched-present future-topology evidence.
```

---

## 7. Final disposition

Current public intestinal data close several lower-level questions:

```text
repeated injury / recovery is technically realizable = YES;
repeated injury changes later recovery = YES;
persistent molecular / epigenetic history carriers exist = YES;
repair-like states can sometimes return toward adult / homeostatic phenotypes = YES;
```

But the decisive AGING01 Stage-1B cell remains open:

```text
rich T1 overlap
+ common P2
+ route-specific future response difference
= NOT YET ESTABLISHED
```

Therefore:

```text
public-data decisive test = NO-GO at present;
public-data calibration = GO;
wet-lab parameter freezing = still NOT authorized;
Stage-1B remains pre-pilot.
```

This is a productive negative result: it prevents the program from relabeling established repeated-injury memory as a novel SRT prediction and identifies exactly what new measurement structure is required.