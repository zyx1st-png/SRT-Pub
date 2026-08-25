---
id: SRC-2026-08-24-NEURO-ZHANG-IPA-TBI-MFN2
source_id: SRC-2026-08-24-NEURO-ZHANG-IPA-TBI-MFN2
type: source_card
status: active
layer: materials
epistemic_layer: evidence
claim_mode: evidence
canonical: false
title: "Microbial metabolite indole-3-propionic acid preserves astrocytic mitochondrial mitofusin 2 to limit neuroinflammation after traumatic brain injury"
source_type: peer_reviewed_primary_research
domain: neuroscience_neurotrauma_gut_brain_axis_astrocyte_mitochondria
authors: [Ziwen Zhang, Kai Wang, Liangbo Wang, Wencong Li, Hao Guo, Meng Xu, Tinghao Wang, Jiahui Ren, Ting Zhu, Jiahui Wang, Wenxing Cui, Jinpeng Zhou, Yang Tian, Liying Han, Chengxuan Guo, Shuoyao Ma, Qiang Wang, Zhihong Li, Yaning Cai, Jingyu Dong, Xun Wu, Haixiao Liu, Yan Qu]
publication: Interdisciplinary Medicine
date_published: 2026-07-02
date_added: 2026-08-24
doi: "10.1002/inmd.70156"
url: "https://doi.org/10.1002/inmd.70156"
evidence_level: peer_reviewed_primary_human_association_plus_mouse_intervention_mechanistic
authority_level: high_for_reported_mechanism_bounded_for_translation
srt_relevance: high
integration_priority: high
verdict: A
related_srt_claims:
  - HEF-3/HEF-4
  - P1-T06
  - SRT-INDIVIDUATION
  - PH-IND05
  - PH-IND06
  - PH-MEM01
  - SRT-D-VALUE-CANONICAL
  - SRT-PROCESSUAL-BEARER-CONSTRAINT-BRIDGE
tags: [TBI, IPA, Postbiotic, Astrocyte, AhR, IRF1, RFFL, MFN2, Mitochondria, Neuroinflammation, Regulation, Constraint, Bearer, d-value]
---

# SourceCard — Zhang et al. 2026, IPA / TBI / MFN2

## 1. One-line summary

Zhang et al. report that lower serum indole-3-propionic acid (IPA) is associated with worse edema and neurological outcome after human TBI, while mouse IPA intervention reduces secondary injury through an astrocytic `AhR -> IRF1 -> RFFL -> MFN2` pathway that preserves mitochondrial organization and limits reactive astrogliosis / neuroinflammation.

---

## 2. Bibliographic anchor

- Ziwen Zhang et al.
- *Microbial metabolite indole-3-propionic acid preserves astrocytic mitochondrial mitofusin 2 to limit neuroinflammation after traumatic brain injury*.
- *Interdisciplinary Medicine* (2026), e70156.
- Version of Record online: 2026-07-02.
- DOI: `10.1002/inmd.70156`.

A New Scientist article dated 2026-08-18 was used as the discovery entry in the guided-reading conversation, but all load-bearing mechanism claims in this SourceCard are anchored to the primary paper above.

---

## 3. Source-backed findings

### 3.1 Human association

The study reports that lower serum IPA after TBI is associated with greater peri-contusional cerebral edema and poorer neurological outcome.

Guard:

```text
human association
!= treatment efficacy
!= causal proof from the human cohort
```

### 3.2 Mouse intervention

In the mouse TBI model, oral IPA intervention reduced lesion volume, preserved blood-brain barrier integrity, reduced neuronal apoptosis / edema and improved neurological function.

For SRT use, the strongest bounded reading is that a prior biological condition can alter the later trajectory following a common injury. Do not promote this into an established post-injury human therapy claim.

### 3.3 Astrocyte mechanism

The reported mechanism is:

```text
IPA
-> astrocytic AhR activation
-> suppression of IRF1
-> suppression of RFFL induction
-> reduced RFFL-dependent MFN2 ubiquitination / degradation
-> preserved mitochondrial dynamics / function
-> reduced astrocyte-derived toxic / chemokine output
-> reduced peripheral immune-cell infiltration
-> reduced secondary injury
```

Astrocyte-specific `Rffl` deletion reproduced major neuroprotective effects, strengthening the pathway-level mechanistic interpretation.

---

## 4. Source limits

1. Human evidence is observational / associative, not an IPA efficacy trial.
2. Mouse intervention and mechanistic evidence do not establish clinical dosing, timing, efficacy or safety in humans.
3. The source does not test SRT Selection, Stable ISP, bearer identity, d-value, subjecthood or consciousness.
4. The source does not distinguish SRT from autopoiesis, organizational closure, active inference, allostasis or ordinary multiscale control accounts.
5. The source supports a biological mechanism and trajectory effect; all processual-bearer / objectification / copy / cancer implications are SRT-side synthesis and must remain separately marked.

---

## 5. GOV-SYN01 contribution separation

### Layer A — source-backed pressure / evidence

Claimed:

- IPA-human-outcome association;
- mouse IPA intervention changing post-TBI damage / recovery trajectory;
- astrocyte AhR / IRF1 / RFFL / MFN2 mechanism;
- RFFL-deletion support for the proposed pathway;
- a useful multiscale example in which microbial product, host cellular reader and organism-level consequence are not the same unit.

### Layer B — SRT ontological synthesis / correction

Permitted only as bounded interpretation:

- `state correction != regulatory-capacity preservation`;
- `producer != carrier != reader != consequence bearer`;
- external proxy/support can participate in a bearer's maintenance without becoming the bearer;
- the guided-reading discussion triggered temporal-objectification and copy/bifurcation hardening;
- cancer was introduced as an independent cross-scale pressure case on collective-d landscape nesting, not as a finding of this paper.

### Layer C — discriminating empirical increment

**None claimed in this pass.**

The source does not provide a matched empirical test uniquely discriminating SRT from established biological/control rivals.

---

## 6. Owner-side subtraction outcome

Direct theory writeback is restricted to:

`Philosophy/patches/SRT_Philosophy_PH_IND07_Processual_Bearer_Active_Maintenance_Stake_Integration_v0_1.md`

with audit:

`Operations/Audits/SRT_PH_IND07_OWNER_SUBTRACTION_2026-08-25.md`

After subtraction:

```text
temporal objectification guard -> retained P3 hardening
copying != process bifurcation -> retained P3 hardening
self-maintenance != self-sufficiency -> guard only
R/A/C stake integration -> already owned by d canonical §2b
d non-additivity -> already owned / qualified by d canonical §6
stake-entry theorem -> already owned by Core/SRT_OPEN_TENSIONS.md §1
cancer -> retained only as reverse pressure on §6.1 landscape-nesting antecedent
```

---

## 7. Integration / consolidation decision

Pipeline 1 landing:

- SourceCard: this file;
- reading note: `Materials/2026/READING_2026_08_24_IPA_TBI_Postbiotic.md`;
- P3 theory hardening: PH-IND07;
- owner-subtraction audit;
- Material Log + JSONL registry + retrieval indexes.

**Consolidation exception:** no separate IntegrationHook is created in this pass because no canonical/dormant owner landing is authorized and the surviving direct hardening is already concentrated in PH-IND07. This exception must remain explicit in the Material Log.

---

## 8. Hard guardrails

Do not write:

```text
IPA proves SRT
New Scientist is the primary source
IPA is established post-TBI human therapy
MFN2 = stake / d / Selection
microbiome = host bearer
constraint preservation = consciousness
active self-maintenance = bearer by definition
cancer is evidence from Zhang et al.
cancer falsifies d-value canonical §6.1
```
