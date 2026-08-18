---
id: SRT-AUDIT-AGING01-P4-MODEL-SELECTION-FEASIBILITY-2026-08-18
type: experimental_feasibility_audit
status: active
record_stage: audit_v1
layer: operations
epistemic_layer: experimental
claim_mode: audit
claim_level: P4-P5
canonical: false
created: 2026-08-18
target_protocol: Experiments/SRT_AGING01_Recovered_Present_Restored_Future_Protocol_v0_1.md
dependency:
  - Experiments/SRT_AGING01_Recovered_Present_Restored_Future_Protocol_v0_1.md
  - Operations/Audits/SRT_AGING_SELECTIVE_MAINTENANCE_SUBTRACTIVE_AUDIT_2026-08-17.md
  - 03_Bridges/hooks/AGING01_Selective_Maintenance_Aging_Integration_Hook.md
  - Core/SRT_Validation_Template.md
tags:
  - aging
  - feasibility
  - model-selection
  - repeated-challenge
  - organoid
  - hematopoiesis
  - epidermis
  - skeletal-muscle
  - tendon
  - rival-model
---

# AGING01 P4 Model-Selection / Feasibility Audit — 2026-08-18

> **Decision first**: do not freeze one “best aging model” yet. Use a staged program. **Intestinal organoid / epithelial regeneration is the current engineering-pilot leader; human HSC / haematopoietic inflammatory-memory systems are the current decisive-test leader.** Epidermis is retained as the cleanest selective-maintenance event model, skeletal muscle as a strong repeated-injury / reserve / niche **killer-rival control**, and tendon as an exploratory fibrosis-vs-regeneration route model.
>
> This audit assigns no execution priority in `Experiments/SRT_Experimental_Roadmap_v1.md`, makes no canonical change, and does not claim that any source validates AGING01.

---

## 0. Audit question

The protocol requires a biological model capable of implementing:

```text
H_A vs H_B
-> overlapping / adjustable T1 present state
-> standardized P2 rechallenge
-> measurable alternative maintenance routes
-> route blockade / switching test
-> bearer-specific consequence readout
-> pre-frozen rich rival comparison
```

The practical question is therefore not:

```text
which system shows aging most clearly?
```

but:

> **Which system can most cleanly separate present-state recovery from restoration of future maintenance-route structure while allowing ordinary damage / resource / reliability / misrepair / hidden-state rivals to compete fairly?**

---

## 1. Scoring discipline

The 12 protocol gates are scored only as:

- `YES` — demonstrated or directly implementable with established methods in the cited model family;
- `PARTIAL` — plausible and partly demonstrated, but the exact AGING01 contrast has not been closed;
- `NO / WEAK` — important missing capability or serious mismatch with the target.

No numerical sum is treated as theory evidence. A high score means experimental suitability only.

The 12 gates are:

```text
G1  H_A/H_B without merely changing chronological age
G2  overlapping / adjustable T1 present endpoint
G3  >=2 P2 maintenance routes independently identifiable
G4  early elimination / replacement / lineage change resolvable
G5  burden / damage before P2 measurable
G6  resource / reserve / reliability measurable
G7  misrepair / persistent structure measurable
G8  major clonal / niche / hidden-state rivals measurable
G9  route blockade / switching manipulation feasible
G10 standardized P2 feasible
G11 prospective replication / confirmatory cohort feasible
G12 ethical / animal-use burden proportionate to discrimination value
```

---

## 2. Candidate A — intestinal organoid / epithelial regeneration

### Primary anchors

- Ayyaz et al., *Single-cell transcriptomes of the regenerating intestine reveal a revival stem cell*, **Nature** (2019), DOI `10.1038/s41586-019-1154-y`.
- Liu et al., *Establishment of intestinal organoid cultures modeling injury-associated epithelial regeneration*, **Cell Research** (2021), DOI `10.1038/s41422-020-00453-x`.
- Moyer et al., *p53 promotes revival stem cells in the regenerating intestine after severe radiation injury*, **Nature Communications** (2024), DOI `10.1038/s41467-024-47124-8`.
- Castillo et al., *Epigenetic memory of colitis promotes tumour growth*, **Nature** (2026), DOI `10.1038/s41586-026-10258-4`.

### What is already available

The intestinal system already supplies several components that the AGING01 protocol needs:

```text
standardized irradiation / inflammatory history;
Lgr5+ homeostatic stem-cell compartment;
Clu+ revival-stem-cell / fetal-like regenerative route;
lineage tracing;
single-cell transcriptional readout;
organoid culture after removal from the original tissue environment;
p53-dependent route manipulation;
Lgr5 / Clu pathway perturbation;
serial passaging / repeated challenge feasibility.
```

The colitis-memory work is especially useful as a history-carrier control: stem-cell-derived organoids can retain a cell-intrinsic epigenetic state after removal from the inflammatory tissue environment, and initially similar cultures can later diverge in regenerative / hyperplastic behaviour. This is an ordinary epigenetic-memory explanation that AGING01 must treat as a **rival carrier**, not as proof of abstract history.

### Gate table

| Gate | Status | Reason |
|---|---|---|
| G1 | **YES** | radiation, p53 manipulation, inflammatory history and culture history can vary without changing chronological age |
| G2 | **PARTIAL→YES candidate** | cultures can be returned to common conditions and gross morphology/function can converge, but exact T1 equivalence must be preregistered |
| G3 | **YES** | homeostatic Lgr5 route, Clu+/fetal-like revival route and other epithelial regenerative states are separable |
| G4 | **YES** | lineage tracing / cell-state tracking can resolve loss and regeneration routes |
| G5 | **YES** | irradiation dose and damage-response state are directly measurable |
| G6 | **PARTIAL** | clonogenicity / stem-cell compartment / serial-passage capacity are useful reserve proxies, but not a complete reliability model |
| G7 | **PARTIAL** | epithelial structural failure is measurable, but tissue-scale fibrosis / systemic misrepair is attenuated in organoids |
| G8 | **YES** | scRNA / epigenetic / lineage / culture-state rivals can be richly measured |
| G9 | **YES** | p53 inhibition, Mdm2 manipulation, Clu / Lgr5 ablation or pathway perturbation provide route-switch tests |
| G10 | **YES** | radiation / defined culture challenge is standardizable |
| G11 | **YES** | batches, donor / mouse lines and confirmatory organoid cohorts are feasible |
| G12 | **YES** | organoid-first design substantially reduces animal burden for feasibility work |

### Audit disposition

**Best current role: engineering / measurement pilot.**

Why:

> It is the easiest system in which to debug `H -> T1 matching -> P2 -> route identity -> blockade` before paying the cost of a whole-organism aging experiment.

But:

```text
organoid feasibility success
!= organismal aging evidence
!= systemic bearer accounting
!= proof of future generative restoration in vivo
```

### Recommended pilot question

A clean pilot should not begin with “young vs old”. One possible family is:

```text
H_A: severe injury resolved through intact / permitted p53-revSC program
H_B: same broad injury with transiently altered route recruitment
-> recovery under common medium
-> T1 match gross organoid growth + damage + cell-state composition as far as feasible
-> common irradiation P2
-> compare Lgr5 / Clu route recruitment and blockade response
```

The exact manipulation needs an implementation-specific power / toxicity audit before execution.

---

## 3. Candidate B — human HSC / haematopoietic inflammatory-memory xenograft

### Primary anchor

- Zeng et al., *Human haematopoietic stem cells remember inflammatory stress*, **Nature** 655, 458–467 (2026), DOI `10.1038/s41586-026-10522-7`.

### What is already available

The 2026 study provides a unusually strong pre-existing scaffold:

```text
human cord-blood HSC xenografts;
TNF / LPS inflammatory challenges;
single vs repeated challenge;
long recovery windows;
single-cell RNA + chromatin multiomics;
engraftment and progenitor composition;
secondary transplantation / limiting dilution;
identified HSC inflammatory-memory subset;
stimulus-dependent durable molecular state;
physiological links to ageing / clonal-haematopoiesis datasets.
```

Critically, one inflammatory challenge showed long-term functional recovery in the reported xenograft measures, whereas repeated challenges left durable functional / molecular differences after recovery. This makes the model highly relevant to the broad `recovery history -> future capacity` question.

However, the same study also supplies a powerful ordinary explanation: **HSC-iM is a measurable present transcriptional / epigenetic state**. AGING01 does not get to call this “history beyond state”. If HSC-iM and other rich current variables fully predict the future response, then the protocol should record that history's efficacy is exhausted by current carriers.

### Gate table

| Gate | Status | Reason |
|---|---|---|
| G1 | **YES** | TNF / LPS / repetition histories vary without chronological-age manipulation |
| G2 | **PARTIAL** | single-challenge recovery is demonstrated, but repeated-stress groups retain differences; a deliberately convergent T1 design is still needed |
| G3 | **PARTIAL→YES candidate** | quiescence, activation, differentiation / lineage output, self-renewal and clone expansion are measurable, but “maintenance route” ontology must be frozen prospectively |
| G4 | **PARTIAL** | population / progenitor changes are measurable; full clonal fate tracking remains a stated limitation |
| G5 | **PARTIAL** | inflammatory burden and response are measurable, but “damage” is not the sole or always relevant state variable |
| G6 | **YES** | stem-cell frequency, engraftment, self-renewal / repopulating capacity and output provide strong reserve / reliability competitors |
| G7 | **NO / WEAK for classic misrepair** | fibrosis / structural misrepair is not the central explanatory axis of this model |
| G8 | **YES** | multiome, composition, mutation / CH state and transcriptional programs support a very rich rival model |
| G9 | **PARTIAL** | cytokine / pathway perturbation and transplantation challenges are possible, but a clean alternative-route blockade is more complex than in organoids |
| G10 | **YES** | defined TNF / LPS challenge schedules are standardizable |
| G11 | **YES** | independent cord-blood pools / xenograft cohorts / secondary transplants support prospective replication |
| G12 | **PARTIAL→YES if discriminating design is strong** | animal + human-cell work is substantial; justified only after pilot de-risks endpoints |

### Audit disposition

**Best current role: high-value decisive target after a pilot.**

This system has a major scientific advantage over a “friendly” SRT model: its ordinary competitors are excellent. A positive residual would therefore be much harder to manufacture.

The decisive design should aim for:

```text
different inflammatory / maintenance histories
-> deliberately select / wait for an overlapping T1 functional window
-> freeze HSC-iM + composition + reserve + mutation / niche variables
-> common P2
-> prospective lineage-output / self-renewal / transplantation / route-response endpoint
```

If `HSC-iM + current composition + reserve + niche` fully absorb the result, that is a legitimate **negative AGING01 result**, not a failed experiment.

---

## 4. Candidate C — epidermal stem-cell dynamic selection

### Primary anchor

- Kato et al., *Dynamic stem cell selection safeguards the genomic integrity of the epidermis*, **Developmental Cell** 56 (2021), 3309–3320.e5, DOI `10.1016/j.devcel.2021.11.018`.

### What is already available

This is the cleanest primary example currently in the AGING01 material for a bounded **selective-maintenance event candidate** in ordinary biological language:

```text
DNA DSB induction in epidermal stem cells;
fate tracing of damaged cells;
p53–Notch / p21-mediated differentiation and delamination;
selective elimination from the stem-cell niche;
augmented symmetric division / clonal expansion of surrounding intact EpiSCs;
UVB generalization of the clonal-expansion response.
```

It is therefore unusually well suited to the bearer-accounting question:

```text
local damaged-cell elimination
+
neighboring intact-clone expansion
-> tissue-level genomic-quality maintenance
```

But the published experiment is not yet the AGING01 repeated-challenge design. It does not by itself establish that two recovered epidermal tissues with different elimination / replacement histories later differ under a matched rechallenge.

### Gate table

| Gate | Status | Reason |
|---|---|---|
| G1 | **YES** | DSB / UVB and pathway manipulations do not require age manipulation |
| G2 | **PARTIAL** | epidermal barrier / gross tissue can recover, but explicit T1 matched-state design must be built |
| G3 | **YES** | differentiation/elimination and compensatory clonal expansion are directly separable routes / consequences |
| G4 | **YES** | fate tracing is a core strength |
| G5 | **YES** | DSB burden is directly induced and measurable |
| G6 | **PARTIAL** | intact stem-cell pool / clonal expansion can proxy reserve, but reliability architecture needs explicit modeling |
| G7 | **PARTIAL** | persistent structural residue is not the central published endpoint |
| G8 | **YES** | clone composition, differentiation state and niche occupancy can be measured as ordinary rivals |
| G9 | **YES candidate** | p53–Notch / p21 / ITGB1 axis offers route intervention handles |
| G10 | **YES** | DSB or UVB rechallenge is standardizable |
| G11 | **YES** | lineage-tracing mouse cohorts are replicable |
| G12 | **PARTIAL→YES** | animal burden is moderate but must be justified by repeated-challenge discrimination |

### Audit disposition

**Best current role: selective-maintenance mechanism bridge / second pilot candidate.**

It is conceptually cleaner than HSC for CG-0..CG-4 auditing, but less mature than intestinal organoid for the exact recovered-present / restored-future design.

A future version could ask:

```text
H_A: DSB episode resolved predominantly by damaged-cell differentiation / delamination + intact-clone expansion
H_B: experimentally altered resolution route
-> allow barrier / gross stem-cell metrics to converge
-> common P2 DSB or UVB
-> lineage-specific route use / clone recruitment / depletion / switching
```

The manipulation must avoid creating a trivial persistent genotype difference that predetermines P2.

---

## 5. Candidate D — skeletal muscle repeated injury

### Primary anchors

- Rayagiri et al., *Basal lamina remodeling at the skeletal muscle stem cell niche mediates stem cell self-renewal*, **Nature Communications** (2018), DOI `10.1038/s41467-018-03425-3`.
- Lazure et al., *GLI3 regulates muscle stem cell entry into GAlert and self-renewal*, **Nature Communications** (2022), DOI `10.1038/s41467-022-31695-5`.
- Wang et al., *In vivo partial reprogramming of myofibers promotes muscle regeneration by remodeling the stem cell niche*, **Nature Communications** (2021), DOI `10.1038/s41467-021-23353-z`.

### What is already available

Skeletal muscle has perhaps the best **repeated-injury infrastructure** among the candidates:

```text
standardized cardiotoxin injury;
serial injuries;
satellite-cell / stem-cell quantification;
self-renewal and reserve depletion;
niche / basal-lamina manipulation;
fibrosis;
regeneration / myofiber outcome;
lineage and histological readouts.
```

The Lama1 niche study is especially valuable as a rival-model demonstration: after repeated injury, failure can be explained through defective stem-cell self-renewal, progressive reserve depletion, niche structure and fibrosis. This is exactly the sort of result AGING01 must **not relabel** as generative-reselectability evidence.

### Gate table

| Gate | Status | Reason |
|---|---|---|
| G1 | **PARTIAL** | repeat count / transient interventions can create histories, but many published contrasts rely on persistent genotype differences |
| G2 | **YES candidate** | early rounds can show substantial tissue regeneration before later divergence; exact Match-2 design remains to be built |
| G3 | **YES** | satellite-cell regeneration, self-renewal, fibrotic compensation and alternative progenitor contributions can be separated |
| G4 | **YES** | stem-cell / progenitor dynamics are trackable |
| G5 | **YES** | injury is standardized and histologically measurable |
| G6 | **YES** | stem-cell reserve / self-renewal is a central readout |
| G7 | **YES** | fibrosis / ECM / basal-lamina remodeling are measurable |
| G8 | **YES** | niche and reserve rivals are unusually strong |
| G9 | **YES candidate** | satellite-cell depletion / signaling / niche perturbations are possible, though specificity matters |
| G10 | **YES** | serial CTX injury is standardizable |
| G11 | **YES** | repeated-injury cohorts are established |
| G12 | **PARTIAL** | three-round injury studies carry non-trivial animal burden; needs strong incremental question |

### Audit disposition

**Best current role: killer-rival / negative-control model, not first SRT-positive target.**

This is strategically valuable. If future failure after repeated injury is already predicted by:

```text
satellite-cell reserve
+ basal-lamina / niche state
+ fibrosis
+ ordinary regenerative kinetics
```

then the correct AGING01 result is:

```text
history/topology residual = absent for this target
```

Muscle should therefore be used to test whether the protocol can correctly **refuse false novelty**.

---

## 6. Candidate E — tendon fibrosis vs regeneration

### Primary anchors

- Nichols et al., *Epitenon-derived progenitors drive fibrosis and regeneration after flexor tendon injury in a spatially-dependent manner*, **Nature Communications** (2025), DOI `10.1038/s41467-025-60704-6`.
- Howell et al., *Novel Model of Tendon Regeneration Reveals Distinct Cell Mechanisms Underlying Regenerative and Fibrotic Tendon Healing*, **Scientific Reports** (2017), DOI family corresponding to article `srep45238`.

### Structural attraction

The epitenon work identifies one progenitor source contributing to both:

```text
regenerative tendon healing
and
peritendinous fibrosis
```

with lineage tracing, scRNA-seq and selective ablation of pro-fibrotic epitenon-derived cells improving function.

This makes tendon attractive for a future **route-allocation** question: the same broad progenitor family can contribute to very different repair outcomes.

### Main blocker

The current primary evidence is much stronger for **acute route identity** than for:

```text
H_A/H_B
-> matched T1
-> common repeated P2
-> future route-switching topology
```

Therefore tendon remains exploratory until repeated-challenge feasibility is demonstrated.

---

## 7. Cross-model decision matrix

| Candidate | Best role now | Main strength | Main blocker |
|---|---|---|---|
| **Intestinal organoid** | **Stage-1 engineering pilot** | controlled H, lineage routes, route blockade, rich state, low execution burden | weak systemic / organismal-aging bearer |
| **Human HSC xenograft** | **Stage-2 decisive target** | human stem cells, repeated inflammation, recovery, multiome, secondary transplant, strong rivals | exact T1 convergence + route-blockade design not yet closed |
| **Epidermis** | selective-maintenance mechanism bridge | unusually clean elimination / replacement / clone-expansion event chain | repeated matched-state rechallenge not yet demonstrated |
| **Skeletal muscle** | killer-rival / negative control | serial injury, reserve, niche, fibrosis, strong ordinary explanation | high risk that ordinary reliability / niche model fully explains result — deliberately useful |
| **Tendon** | exploratory route-allocation model | same progenitor source can generate regeneration vs fibrosis | repeated-challenge architecture immature |

---

## 8. Recommended staged program

### Stage 0 — no biology yet: freeze measurement grammar

Before choosing a lab implementation, freeze:

```text
what counts as a route;
what counts as T1 recovery;
what counts as a bearer;
what route blockade means;
which competitor variables enter Match-2;
what prospective gain counts as non-trivial.
```

### Stage 1 — intestinal organoid feasibility

Goal:

> Demonstrate that the full protocol plumbing can be executed without claiming SRT support.

Exit criteria:

```text
H_A/H_B feasible;
T1 overlap measurable;
>=2 routes identifiable;
P2 standardized;
blockade exposes switching;
rival model can be frozen;
prospective holdout possible.
```

A Stage-1 GO only means **pilot mechanics work**.

### Stage 2 — human HSC / haematopoietic hard test

Goal:

> Test whether a history/topology augmentation adds anything after an unusually rich current-state model.

Required hardening before execution:

```text
engineer / identify a T1 overlap window;
freeze HSC-iM and other multiomic carriers as rival variables;
define >=2 future route outcomes;
choose a causal switching / challenge endpoint;
predeclare donor-pool / xenograft hierarchy;
predeclare negative disposition if current carriers fully absorb H.
```

### Stage 3 — mechanism / generalization branches

- epidermis for bounded selective-maintenance event audit;
- muscle for killer-rival failure test;
- tendon for fibrosis-vs-regeneration route allocation;
- only after these should a whole-organism aging intervention be considered.

---

## 9. Why not jump directly to old-vs-young mice

A standard young-vs-old injury/recovery experiment would almost certainly show differences, but it would be weak for the current AGING01 residual because age simultaneously changes:

```text
damage;
inflammation;
reserve;
clonal composition;
niche;
ECM;
mitochondria;
chromatin;
systemic signals;
metabolism;
reliability;
recovery kinetics.
```

That design answers:

```text
age changes recovery
```

not:

```text
maintenance history changes future path structure beyond current-state rivals
```

Chronological age should therefore enter later as a moderator / replication axis, not as the first causal manipulation.

---

## 10. Subtractive interpretation of the candidates

The candidate ranking itself follows GOV-SUB01 discipline.

### Organoid

If epigenetic / transcriptional state fully predicts P2 route behavior, retain the biology and drop any abstract history residual.

### HSC

If HSC-iM + composition + reserve + niche explain later response, the history has a carrier and the AGING01 residual closes locally.

### Epidermis

If clone composition after P1 fully predicts P2, then “selective-maintenance history” adds no extra empirical work beyond clonal state.

### Muscle

If reserve / niche / fibrosis explains future regenerative decline, that is the expected killer-rival success.

### Tendon

If spatial progenitor fate and fibrosis burden explain outcome, retain ordinary lineage / repair biology without SRT inflation.

---

## 11. Current decision

```text
MODEL FREEZE: NO

engineering-pilot leader:
  intestinal organoid / epithelial regeneration

decisive-test leader:
  human HSC / haematopoietic inflammatory-memory system

mechanism bridge:
  epidermal dynamic stem-cell selection

killer-rival control:
  skeletal muscle repeated injury

exploratory:
  tendon fibrosis / regeneration
```

No candidate is yet `pilot-ready V5` in the strict repository sense because the exact `H_A/H_B`, T1 matching set, primary endpoint, blockade, sample hierarchy and power plan have not been frozen.

---

## 12. Next action

Do **not** expand AGING01 theory.

The next useful artifact is a narrow Stage-1 implementation packet for the intestinal-organoid pilot containing only:

```text
candidate H_A/H_B manipulation;
T1 matching panel;
P2 challenge;
route definitions;
blockade;
Match-2 rivals;
primary outcome;
holdout / replication unit;
GO / NO-GO feasibility criteria.
```

Only after that packet survives a methods / novelty review should `Experiments/SRT_Experimental_Roadmap_v1.md` be reopened for priority assignment.

---

## Sources checked for this feasibility audit

Primary empirical sources only were used for the scientific feasibility claims above:

1. Zeng AGX et al. *Human haematopoietic stem cells remember inflammatory stress*. Nature. 2026. DOI `10.1038/s41586-026-10522-7`.
2. Ayyaz A et al. *Single-cell transcriptomes of the regenerating intestine reveal a revival stem cell*. Nature. 2019. DOI `10.1038/s41586-019-1154-y`.
3. Liu Y et al. *Establishment of intestinal organoid cultures modeling injury-associated epithelial regeneration*. Cell Research. 2021. DOI `10.1038/s41422-020-00453-x`.
4. Moyer et al. *p53 promotes revival stem cells in the regenerating intestine after severe radiation injury*. Nature Communications. 2024. DOI `10.1038/s41467-024-47124-8`.
5. Castillo et al. *Epigenetic memory of colitis promotes tumour growth*. Nature. 2026. DOI `10.1038/s41586-026-10258-4`.
6. Kato et al. *Dynamic stem cell selection safeguards the genomic integrity of the epidermis*. Developmental Cell. 2021. DOI `10.1016/j.devcel.2021.11.018`.
7. Rayagiri et al. *Basal lamina remodeling at the skeletal muscle stem cell niche mediates stem cell self-renewal*. Nature Communications. 2018. DOI `10.1038/s41467-018-03425-3`.
8. Lazure et al. *GLI3 regulates muscle stem cell entry into GAlert and self-renewal*. Nature Communications. 2022. DOI `10.1038/s41467-022-31695-5`.
9. Wang et al. *In vivo partial reprogramming of myofibers promotes muscle regeneration by remodeling the stem cell niche*. Nature Communications. 2021. DOI `10.1038/s41467-021-23353-z`.
10. Nichols et al. *Epitenon-derived progenitors drive fibrosis and regeneration after flexor tendon injury in a spatially-dependent manner*. Nature Communications. 2025. DOI `10.1038/s41467-025-60704-6`.
