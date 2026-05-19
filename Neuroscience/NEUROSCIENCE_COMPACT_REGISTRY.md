---
id: SRT-NEUROSCIENCE-COMPACT-REGISTRY
type: index
tags: [Neuroscience, Compact Core, Registry]
status: active_v2
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
dependency: [SRT-CANONICAL-REGISTRY, SRT-NEUROSCIENCE-CLAIM-STATUS, SRT-NEURO-AXIOMS-001]
---

# SRT Neuroscience Compact Registry

> **Metadata cleanup note（2026-05）**：本 registry 是 navigation layer，`canonical: false`；它路由 neuroscience materials，不定义 `d-value`、`Ψ_f`、consciousness、clinical diagnosis 或 treatment claims。
本页汇总 Neuroscience 板块当前的 compact core、桥接入口、claim-status guardrail 与 hardening draft，并给出最短阅读路径。

## 0. Current structure

Neuroscience 现在采用五层结构：

1. **Directory / Registry Layer**：目录入口、compact registry、机器可读分流。
2. **Canonical-facing Bridge Layer**：神经科学三域映射、公理化桥接、历史 theorem / hypothesis 标签。
3. **Formal Compact Core Layer**：当前正式 compact core，承载最新神经机制与意识机制主干。
4. **Hardening / Lab Draft Layer**：N1-N9 工作草稿、实验路线、未来 citation 层。
5. **Longform / Measurement Layer**：长文、临床测量、IIT/PCI 接口与扩展讨论。

重要警戒：`_SRT_Neuro_Axioms.md` 是 canonical-facing hybrid bridge，不应被整文件当作 all-canonical definition source。claim-level 状态必须参考 `SRT_Neuro_Axioms_Claim_Status.md`。

---

## 1. Neuroscience Entry Coverage

### A. Directory / Registry Layer

- `README.md` — human-facing directory entry; separates canonical-facing material, compact cores, and hardening drafts.
- `NEUROSCIENCE_COMPACT_REGISTRY.md` — this compact registry.
- `SRT_Neuroscience_Claim_Status.md` — folder-level guardrail for clinical, FEP, NDE, AI-comparison, `Psi_f` proxy, and `d-value` proxy language.
- `SRT_Neuro_Axioms_Claim_Status.md` — claim-status audit for `_SRT_Neuro_Axioms.md`; prevents file-level canonical over-reading.

### B. Canonical-facing Bridge Layer

- `_SRT_Neuro_Axioms.md` — historical / formal neuroscience bridge. Use with claim-status audit. Do not assume every internal theorem/proxy/discourse claim is canonical.

### C. Formal Compact Core Layer

- `SRT_Neural_Mechanisms_CompactCore.md` — current formal compact core for neural mechanisms. Integrates the 2026-04 N1-N5 / N7-N9 hardening.
- `SRT_Consciousness_Mechanisms_CompactCore.md` — current formal compact core for consciousness mechanisms. Integrates N6: consciousness as stable concern-weighted `L1` anchoring.

### D. Hardening / Lab Draft Layer

- `SRT_Neuroscience_Hardening_N1_N9_v0_1.md` — full staging draft for the 2026-04 N1-N9 neuroscience hardening cycle. Non-canonical unless later promoted through the claim ladder.
- `_SRT_Neuroscience_Hardening_Index.md` — domain index for hardening drafts and Pipeline 1 material patches.
- `patches/` and `hooks/` — Pipeline 1 patch notes and integration hooks. These are bridge records, not canonical definitions.

### E. Longform Counterparts

- `SRT_Neural_Mechanisms.md` — longform neural mechanisms text. May lag behind compact core until fully synchronized.
- `SRT_Consciousness_Mechanisms.md` — longform consciousness mechanisms text. May lag behind compact core until fully synchronized.

### F. Clinical / Measurement Layer

- `SRT_Clin_00_IIT_PCI.md` — clinical / measurement interface around IIT, PCI, and consciousness-state measurement. Should be read with the N6 hardening: PCI/Φ-like measures are not by themselves identical with SRT consciousness; SRT also requires `L1` anchoring, `d-value`, action/self coupling, and possible `L2` sedimentation.

---

## 2. Recommended Reading Order

### 最短主线（第一次进入 Neuroscience）

1. `README.md`
2. `SRT_Neuroscience_Claim_Status.md`
3. `SRT_Neuro_Axioms_Claim_Status.md`
4. `SRT_Neural_Mechanisms_CompactCore.md`
5. `SRT_Consciousness_Mechanisms_CompactCore.md`
6. `SRT_Neuroscience_Hardening_N1_N9_v0_1.md`（if you need the full N1-N9 staging record）

### canonical-facing bridge path

1. `_SRT_Neuro_Axioms.md`
2. `SRT_Neuro_Axioms_Claim_Status.md`
3. `SRT_Neural_Mechanisms_CompactCore.md`
4. `SRT_Consciousness_Mechanisms_CompactCore.md`

### research / lab path

1. `SRT_Neuroscience_Hardening_N1_N9_v0_1.md`
2. `SRT_Neural_Mechanisms_CompactCore.md` §10 experimental roadmap
3. `SRT_Consciousness_Mechanisms_CompactCore.md` boundary cases and hardest objections
4. `SRT_Clin_00_IIT_PCI.md`

### 第二层展开

1. `SRT_Neural_Mechanisms.md`
2. `SRT_Consciousness_Mechanisms.md`

---

## 3. Role Split

| Layer | File(s) | Role | Canonical caution |
|---|---|---|---|
| Directory / Registry | `README.md`, this file | navigation and read order | not a theory source |
| Claim-status audit | `SRT_Neuro_Axioms_Claim_Status.md` | classifies claim status of `_SRT_Neuro_Axioms.md` | audit, not replacement |
| Canonical-facing bridge | `_SRT_Neuro_Axioms.md` | formal neuro bridge and historical axiom/discourse container | hybrid; not all internal claims are canonical |
| Compact core | `SRT_Neural_Mechanisms_CompactCore.md`, `SRT_Consciousness_Mechanisms_CompactCore.md` | current concise formal neuroscience summary | hardening content is bridge/lab unless promoted |
| Hardening draft / material patches | `SRT_Neuroscience_Hardening_N1_N9_v0_1.md`, `_SRT_Neuroscience_Hardening_Index.md`, `patches/`, `hooks/` | full N1-N9 staging record plus Pipeline 1 neuroscience patch records | non-canonical working drafts / bridge records |
| Longform | `SRT_Neural_Mechanisms.md`, `SRT_Consciousness_Mechanisms.md` | expanded material | may lag compact core |
| Measurement | `SRT_Clin_00_IIT_PCI.md` | clinical / PCI / IIT interface | measurement proxies are not identities |

---

## 4. N1-N9 Integration Map

| N-claim | Primary integrated file | Secondary reference |
|---|---|---|
| N1 neural systems as embodied selection systems | `SRT_Neural_Mechanisms_CompactCore.md` | `_SRT_Neuro_Axioms.md` Ax-NEURO-1 |
| N2 composite `G_hat_theta` | `SRT_Neural_Mechanisms_CompactCore.md` | N1-N9 draft |
| N3 `Psi_f` as selection friction | `SRT_Neural_Mechanisms_CompactCore.md` | `_SRT_Neuro_Axioms.md` H-NEURO-4b / Ax-NEURO-5 |
| N4 `L2` sedimentation | `SRT_Neural_Mechanisms_CompactCore.md` | N1-N9 draft |
| N5 `d-value` | `SRT_Neural_Mechanisms_CompactCore.md` | N1-N9 draft |
| N6 consciousness as stable concern-weighted `L1` | `SRT_Consciousness_Mechanisms_CompactCore.md` | `SRT_Clin_00_IIT_PCI.md` |
| N7 psychopathology | both compact core files | N1-N9 draft |
| N8 experimental roadmap | `SRT_Neural_Mechanisms_CompactCore.md` | future experimental roadmap file |
| N9 mainstream-theory distinction | `SRT_Neural_Mechanisms_CompactCore.md` | N1-N9 draft |

---

## 5. Current Open Optimization Tasks

1. Add citation layer for N1-N9.
2. Refine the `Psi_f` proxy hierarchy: core proxies, physiological proxies, neural proxies, historical proxies, forbidden identities.
3. Further distinguish `d-value` from salience, reward, precision, motivational relevance, subjective value, affective valence, arousal, and self-relevance.
4. Compress N8 into 1-2 flagship experiments suitable for a pilot or pre-registration.
5. Add sync warnings to longform files if compact cores remain ahead of them.
6. Regenerate graphify-out / wiki artifacts after merge.

---

## 6. Compact Doctrine

The current neuroscience compact doctrine is:

> SRT treats the nervous system as an embodied selection system. Candidate percepts, actions, judgments, and conscious contents emerge from accessible latent spaces through competition, gain modulation, gating, and stabilization. `Psi_f` captures multidimensional anchoring friction; `d-value` captures concern-weighted consequence; `L2` captures sedimented selection constraints. Consciousness is stable concern-weighted `L1` anchoring. Psychopathology is a distortion of anchoring dynamics. Existing neuroscience theories are treated as partial mechanisms inside a broader selection-anchoring architecture, not as direct equivalents of SRT.
