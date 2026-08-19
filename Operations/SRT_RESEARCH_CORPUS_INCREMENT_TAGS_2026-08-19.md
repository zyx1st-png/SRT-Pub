---
id: SRT-RESEARCH-CORPUS-INCREMENT-TAGS-2026-08-19
type: research_corpus_audit
status: active
version: v1
layer: meta
epistemic_layer: os
claim_mode: evidence
canonical: false
tags: [ResearchCorpus, IncrementTriage, OTrack, DTrack, ChronologicalScan]
---

# 研究目录 SRT 增量标签审计

> **阶段说明（2026-08-19 二轮裁决）**：Finder 标签与本文件承担召回和导航，不承担最终 novelty verdict。正式去重结果见 `Operations/Proposals/SRT_RESEARCH_CORPUS_INCREMENT_PR_PACKET_2026-08-19.md`；`SRT-O-CANDIDATE` 不等于可直接融入，更不等于 D-track 已成立。

## 结论先行

已对本机研究根目录（下文记为 `$RESEARCH_ROOT`）下可读文档做全量盘点，并按文件系统修改时间（mtime，UTC）由旧到新建立顺序。原文没有被改写；标签保存在独立 sidecar 台账中。

召回与初筛阶段形成的不是 86 份互不相关的文档，而是 5 个待二轮裁决内容簇：

1. **AAT / 具身选择 / 信息—效价遗产**：72 个独立内容文件。初筛时作为 O-track 的信息生成、具身选择、效价与资源倾斜接口召回；同时对当前 Gate 0、HP-B-B 和 `d`/`Ψ_f` 边界形成强压力。二轮去重后不形成新 owner 节点，且不能把 Universal Attention、E&O 目的论或“感受质=效价”原样升格。
2. **对象—过程互补与记忆—持续性**：`思想与思考者：论对象与过程的互补性.pdf`。初筛时是最干净的外部 O-track 候选，直接触及对象化、系统边界、记忆、时间、身份持续和多尺度干预；二轮裁决为 B2 near-duplicate guardrail。
3. **预测心智的时间/反事实深度与冥想去构成**：6 个文件，核心锚点为 `paper/LaukkonenSlagter2021.pdf`。最终增量是禁止把预测深度／精度变化写成 `L_2` 脚本全局悬置、无 Selection 或 `L_0` 接触；没有 SRT 独有 D-track 结果。
4. **语言作为注意力路由与共同焦点系统**：6 个文件。可细化语言如何把注意力、语境、共享指称和社会 L2 约束组织起来；目前主要是综合报告，需回溯一手研究。
5. **记忆的未来效用筛选与系统巩固**：1 个文件。可为历史写回、未来可选择性和 `d` 的边界提供 O+D 候选，但必须先把报告中的二手/综合表述拆回原始研究，不能把“未来效用”直接当作 canonical `d`。

按时间正序，进入上述候选簇的最早代表依次是：

| mtime（UTC） | 代表文件 | 当前判断 |
|---|---|---|
| 2024-04-03 | `$RESEARCH_ROOT/paper/LaukkonenSlagter2021.pdf` | O-track，`T_dir`/L2/reselectability 候选 |
| 2025-02-14 | `$RESEARCH_ROOT/注意力代理理论.docx` | O-track，Gate 0 / HP-B-B 压力候选 |
| 2025-04-27 | `$RESEARCH_ROOT/作为具身选择的信息 042704.docx` | O-track，信息—具身选择—效价候选 |
| 2025-05-12 | `$RESEARCH_ROOT/思想与思考者：论对象与过程的互补性.pdf` | O-track，对象化/持续性高优先候选 |
| 2025-06-05 | `$RESEARCH_ROOT/deep research/语言作为引导注意力的系统.pdf` | O-track，L2 语言接口候选 |
| 2025-06-05 | `$RESEARCH_ROOT/deep research/大脑的记忆筛选策略：基于未来效用的神经机制探索.pdf` | O+D 候选，需一手研究复核 |

## 标签含义

| 标签 | 含义 |
|---|---|
| `SRT-O-CANDIDATE` | 有明确本体论整合或结构压缩潜力；不等于证明 SRT。 |
| `SRT-D-POSSIBLE` | 可能形成经验/判别增量；必须继续做 bounded rival、预注册或干预审计。 |
| `SRT-GATE0-PRESSURE` | 会碰到 L0 内容无涉结构、全局目的/效价/最优等准入边界。 |
| `SRT-HP-B-B-PRESSURE` | 会碰到 structural bearing 与 phenomenal bearing 的分离；不能直接宣称解决难问题。 |
| `SRT-OBJECTIFICATION-PRESSURE` | 触及对象化、系统边界、身份和过程优先问题。 |
| `SRT-T-DIR-PRESSURE` | 可能帮助形式化方向透明度/重定向，而不是 reward 或一般 coherence。 |
| `SRT-L2-RESELECTABILITY-PRESSURE` | 可能帮助区分 L2 脚本、历史写回和可再选择性。 |
| `SRT-L2-LANGUAGE-PRESSURE` | 可能细化语言、共享语境与社会 L2 约束。 |
| `SRT-FUTURE-SELECTABILITY-PRESSURE` | 可能连接记忆、未来可达性与历史性选择能力。 |
| `SRT-ALREADY-RECORDED` | 当前仓库材料/桥接/运行台账已有记录，不计为本轮新增。 |
| `SRT-HISTORICAL-REFERENCE` | 旧 SRT 版本、备份或合并稿；只用于谱系和废弃主张审计。 |
| `SRT-CURRENT-BASELINE` | 当前 SRT 构造或生成快照；是比较基线，不是外部增量。 |
| `SRT-SOURCE-REVIEW-QUEUE` | 相关书籍/长文，尚未完成路线化 close-read，暂不判为增量。 |
| `SRT-MACHINE-REVIEW-ONLY` | 关键词召回候选，尚未通过当前理论边界复核。 |
| `SRT-PARSE-FAILED` | 解析失败；不作理论价值判断。 |

## 当前 SRT 对照纪律

本审计按 `Governance/SRT_GOV_SYN01_Ontological_Synthesis_and_Empirical_Discrimination_Protocol_v0_1.md` 分开记录 O-track 与 D-track：O-track 可以成立而不要求独有经验预测；D-track 只有在有界竞争理论和前瞻性判别中才成立。

候选内容还必须回到当前锚点校验：

- `Governance/SRT_CLAIM_LADDER.md`：外部材料通常最多先落在 P2/P3/P4，不能反向定义 P0/P1。
- `Core/SRT_OPEN_TENSIONS.md §3–§5、§7、§13–§18`：`T_dir`、L2 支持/替代、stable ISP、primitive actualisation、选择事件阈值、EX-A 与 CΨ 仍需按现状表述。
- `SRT_AI_START.md §3–§8`：尤其是 `d`、`Ψ_f`、`T_dir`、L0/L1/L2、AI 与现象性边界。
- 当前作者裁决 HP-B-B、RC-A、PD-A、ST-A、EX-A、C-A：不得把旧材料中的“真实选择时刻”、全球最优、全局目的性或直接感受质还原读法复活为当前结论。

## 扫描范围与质量说明

- 文档文件：**62,103**；独立内容哈希：**12,039**；重复路径文件：**50,064**。
- 纳入：Markdown、TXT、PDF、DOCX、EPUB、HTML/XHTML、TeX、CSV/TSV、JSON/JSONL/NDJSON、YAML/YML、RTF、SRT/VTT 等。
- 排除：`.git`、`node_modules`、`.venv`、`__pycache__`、`.pytest_cache`、`dist`、`build` 等明确机器目录；图片、音视频、模型权重和源代码不作为“文档”纳入本轮理论筛选。
- PDF 使用 Poppler 限前 24 页文本抽取，DOCX 使用本地 OOXML 文本抽取；4 个独立内容因坏 ZIP/DOCX 结构解析失败，已保留 `SRT-PARSE-FAILED` 标签。
- “mtime”是可复核的遍历顺序，不等同于思想/写作发生时间；每行另有 `date_hint` 字段（若文件名或正文能抽到日期）。

## 机器可读台账

- 全量独立标签（轻量版）：`data/research_increment_tagging_2026-08-19/srt_increment_labels_compact.jsonl`（local-only）
- 仅候选内容簇：`data/research_increment_tagging_2026-08-19/srt_increment_shortlist.jsonl`（local-only）
- 标签统计：`data/research_increment_tagging_2026-08-19/srt_increment_label_summary.json`（local-only）
- 扫描摘要：`data/research_increment_tagging_2026-08-19/scan_summary.json`（local-only）

这些 sidecar 含本机绝对路径或大规模路径清单，不进入公开 PR；本报告保留其方法、统计与最终可追溯摘要。
- 原始抽取摘录已压缩保存为 `document_inventory.jsonl.gz`、`machine_review_candidates.jsonl.gz`、`srt_increment_labels.jsonl.gz`，用于复核机器召回，不是理论判断的唯一依据。

这份报告及台账是 Operations / evidence 层产物，不生成新的 canonical 定义，也不自动触发正文回写。
