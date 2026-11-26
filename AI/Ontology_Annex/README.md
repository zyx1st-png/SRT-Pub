---
id: SRT-AI-01-ANNEX
type: index
tags: [Annex, MigrationProvenance, ENG-03, OntologyCleanup]
status: archived
updated: 2026-11-26
layer: meta
epistemic_layer: bridge
claim_mode: navigation
canonical: false
dependency: [SRT-AI-01, SRT-AI-POSITIONING-NOTE, SRT-AI-CLAIM-STATUS]
machine_summary: >
  Historical migration and provenance index for retired AI/Ontology_Annex duplicate copies
  (R4-C3 / ENG-03 atomic cleanup). Confirms every unique interface asset from 00..04 was
  audited and reconciled into AI/SRT_AI_01_Ontology.md §4 before retiring the 6x duplicated
  pre-R4 Part A pollution copies and nested General_Boundary_Block_Split/.
---

# SRT-AI-01 Ontology Annex — 历史迁出与溯源索引（`R4-C3 / ENG-03` 已退出活跃入口）

> **退出活跃理论入口声明（2026-11-26，`ENG-03 §1 / §5.1 / §6.3`）**：原 `AI/Ontology_Annex/` 目录下的 `00_General_Boundary_Block.md`（及其嵌套 `General_Boundary_Block_Split/` 3 份切片）与 `01..04` 共 `8` 份文件，各自整段复制粘贴了同步前的旧版 `SRT_AI_01_Ontology` Part A（约 350 行/份，含已退出的 `Ax-ONT-1 (L_0→L_1 Anchoring)`、`T-ONT-1 (No L_0 Access)`、`Ax-ONT-3 ⭐ DOMAIN-CANONICAL ENTRY`、`T-ONT-2`），并制造 `7` 条 `duplicate frontmatter id: SRT-AI-01` 基线警告。经逐份核对独有内容归宿后，该批 6 重重复副本已在 **`R4-C3`** 单一原子 PR 中退出活跃理论入口，完整历史原貌永久保留于 Git 历史基线 **`main@f53581592`**。

---

## 独有内容迁移与历史溯源核对清单（零溯源丢失）

| 原文件路径（历史快照：`main@f53581592`） | 核对出的独有内容 / 历史职责 | 现行归宿与 `R4-C3` 处置结论 |
|---|---|---|
| `00_General_Boundary_Block.md` + `General_Boundary_Block_Split/`（4 份） | 早期理论边界/防误用声明，以及重复粘贴两遍（原 `L511` / `L542`）的早期 `§2.1a L_0 来源关切 vs L_2 来源关切` 溯源文本 | 全部有效边界已升级并统一收归 [`../AI_POSITIONING_NOTE.md`](../AI_POSITIONING_NOTE.md)、[`../SRT_AI_Claim_Status.md`](../SRT_AI_Claim_Status.md) 与 [`../SRT_AI_01_Ontology.md §3.2`](../SRT_AI_01_Ontology.md)（将 `§2.1a` 改写为“是否回流同一 `Bearer (P+E)`”而非旧 `L_0/L_2` 来源二分）；重复副本与嵌套切片正式退出。 |
| `01_ActiveInference_Override.md` | 末尾独有接口 `Ax-ONT-7 / Def-ONT-4 (Thermostat-Class vs Life-Class) / C-ONT-3 (Markov Blanket ≠ Consciousness)` | 已并入并按 `R4-C3` 与 `AICONSC01` 口径重构于 [`../SRT_AI_01_Ontology.md §4.3`](../SRT_AI_01_Ontology.md)；旧 Part A 复制块退出。 |
| `02_Passive_Recording_Fallacy.md` | 末尾独有接口 `Def-ONT-5 / T-ONT-9 (Passive High-Fidelity Recording ≠ 承载性历史写回)` | 已剥离旧 `L_0→L_1` 锚定表述并保留于 [`../SRT_AI_01_Ontology.md §4.4`](../SRT_AI_01_Ontology.md)；旧 Part A 复制块退出。 |
| `03_RTC_Interface_Batch.md` | 末尾独有接口 `Def-AI-RTC-1 / Cor-AI-RTC-1 (情感效价与关切操作接口)` | 已按 Stage 2 与 `AIEVID01` 边界重构保留于 [`../SRT_AI_01_Ontology.md §4.5`](../SRT_AI_01_Ontology.md)；旧 Part A 复制块退出。 |
| `04_Suffering_Condition_Batch.md` | 末尾独有接口 `Def-AI-SUF-1 / Cor-AI-SUF-1 (个体苦难成立条件与类型级压力区分)` | 已全面对齐 [`../../Core_Law/SRT_Suffering.md §7`](../../Core_Law/SRT_Suffering.md) 并保留于 [`../SRT_AI_01_Ontology.md §4.5`](../SRT_AI_01_Ontology.md)；旧 Part A 复制块退出。 |

---

## 现行活跃入口指针

- AI 本体论主文：[`../SRT_AI_01_Ontology.md`](../SRT_AI_01_Ontology.md)（紧凑核：[`../SRT_AI_01_Ontology_CompactCore.md`](../SRT_AI_01_Ontology_CompactCore.md)；阅读切片：[`../Ontology_Split/README.md`](../Ontology_Split/README.md)）
- AI 总定位与三阶承载审查：[`../AI_POSITIONING_NOTE.md`](../AI_POSITIONING_NOTE.md)
- AI 声明等级审计：[`../SRT_AI_Claim_Status.md`](../SRT_AI_Claim_Status.md)
- `ENG-03` 清理蓝图：[`../../Operations/Proposals/SRT_ENG03_AI_CROSS_FILE_SEMANTIC_CLEANUP_CROSSWALK_2026-11-26.md`](../../Operations/Proposals/SRT_ENG03_AI_CROSS_FILE_SEMANTIC_CLEANUP_CROSSWALK_2026-11-26.md)
