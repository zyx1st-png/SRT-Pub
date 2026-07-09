---
id: SRT-CHOICE-TRACE-LOG
type: ledger
tags: [Article, Writing, ChoiceMap, Trace, Convergence, RevealedStake, dValue]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
created: 2026-07-02
provenance: 文章工作流 R 段落地（发散→收敛配对轨迹，作者收敛函数的 revealed-stake 台账）
dependency: [_SRT_ARTICLE_WORKFLOW, _SRT_DIRECTION3_CHOICEMAP_PROTOTYPE_SEED, SRT_TOPIC_ARTICLE_INDEX]
---

# SRT 收敛轨迹台账：作者收敛函数的显影

> **性质与边界（先读）**
> - 本文件是 `_SRT_ARTICLE_WORKFLOW.md` R 段的落地物：记录每次"发散→收敛"的配对轨迹。
> - 记录的**不是文章内容**，而是**作者的收敛函数**——在一个由 LLM 发散出的更大选择空间里，作者选了什么、跳过了什么众数选项、为什么。
> - **非 canonical，不定义术语。** 这是运行层的行为留痕，不是理论证据，也不构成对 d-value 的任何形式化测量。它只是作者品味与判断的经验轨迹。

---

## 0. 为什么记这个（一段话）

扩散模型学的是"加噪→去噪"的轨迹配对，不是图片。本台账记的是"发散→收敛"的轨迹配对，目的是让作者的**收敛偏置**可积累、可回看、将来可作为条件。

- 单条轨迹几乎没信息。
- 几十条轨迹开始显影出一个稳定的形状：作者反复选哪类角度、每次都跳过哪类众数选项、闭包边界习惯设在哪。
- 那个形状 = 用 AI 又不丢锋芒的锋芒本身。将来生成/诊断可以 condition 在它上面，而不是 condition 在互联网平均品味上。

> 理论自指：d-value 在攸关下由选择揭示。本台账是对作者自身 d-value 的 revealed-stake 提取（ChoiceMap 种子文档 §3–§5 的"编码层"）。**但它只是 proxy，不是 ground truth。**

---

## 1. 字段定义（这几个字段决定它将来能不能当条件用）

每条轨迹 = 一次 **命题锻造 → 分层递归发散 → 作者收敛**（对齐 `_SRT_ARTICLE_WORKFLOW.md` v2）。**必填字段**如下，缺一条这条轨迹就不可用于回看/条件：

| 字段 | 含义 | 为什么必须记 |
|---|---|---|
| `trace_id` | `CT-YYYYMMDD-NN` | 唯一定位 |
| `trace_type` | `article`（缺省）/ `intuition_mining` / `decision` | 三种用途的发散/收敛边界不同（见 `_SRT_CHOICEMAP_TRACE_WORKFLOW.md §1`），混记会毁掉回看的可比性。非 `article` 类 trace 通常以独立文件存在，本台账只记指针条目（见 §2a） |
| `date` | 收敛发生日期 | 时间序，看偏置漂移 |
| `seed_fragment` | 作者投喂的原始碎片想法（**逐字**，不润色） | 条件的输入端；润色过就污染了 |
| `layered_options` | 逐层的**选项全集**（LLM 产出）：命题锻造命中项 → 层1 思路结构 → 层2 理论内容（含 canonical 核对状态）→ 层3 写作手法 → 被划掉的不相容分支。结构见 §2 模板 | 没有"每层可选项全集 + 被划掉的分支"，就无法定义"作者在每层的选择" |
| `chosen` | 作者在**每层选了**哪个（含是否杂交、杂交了哪两个） | 选择的正例；逐层记录 |
| `skipped_mode` | 作者**主动跳过**的众数选项（D2 陷阱 + D1 里的显然角度）；确无可跳过时填 `none_detected` **并附一句原因** | **与 chosen 同等重要**：收敛函数的形状由"选了什么"和"避开了什么"共同定义 |
| `reason` | 收敛理由，**一句话，作者亲写** | 条件的标签；LLM 代拟的理由是众数理由，直接毁掉这条轨迹的价值 |
| `closure_boundary` | 作者设定的"谁承受后果 / 看多远" | 作者的边界偏好是收敛函数的核心维度之一 |
| `attack_target` | 这篇文章要拆的"世界本来如此"的哪一块 | 攻击面选择也是品味 |

**可选字段**（有则记，用于后续回流分析）：

| 字段 | 含义 |
|---|---|
| `reason_note` | `reason` 之外的补充说明（几句展开、动机、背景）；`reason` 仍保持一句话，富信息放这里 |
| `late_entry` | `true` 表示非当场记录、事后补记；缺省视为当场记录。补记的 `reason` 是重构，回看时按此降权 |
| `pruned` | 为"一文一刀"而主动 park 掉的、本可展开的分支（区别于 `skipped_mode` 里的众数选项——`pruned` 是被砍掉的**真东西**） |
| `reclaimed` | 若某个 `pruned` 分支被作者的判断力事后讨还（折入本篇或另开新篇），记在此。"先砍到一把刀、再讨还完整性"是收敛函数最强的信号之一 |
| `article_ref` | 成文后的文章链接 / 归档路径 |
| `platform` | 发布平台 |
| `reader_resistance` | 读者实际的抵抗点 / 反驳（发布后回填） |
| `topic_index_id` | 若命中 `SRT_TOPIC_ARTICLE_INDEX.md` 的某行，记其 ID |
| `note` | 其他 |

### 记录纪律（防污染，等同于数据质量）

1. **`seed_fragment` 与 `reason` 必须是作者原话**，不许 LLM 润色或代拟——它们是条件的输入端和标签端，一旦众数化，整条轨迹作废。富信息可放可选字段 `reason_note`，但 `reason` 本身保持一句话。
2. **`skipped_mode` 不许留空**。"这次没跳过什么"本身可疑：说明 D 段发散不够，或作者其实选了众数。确实无可跳过时填 `none_detected` **并附一句原因**，不要强填伪数据。
3. LLM 可以帮忙**填 `layered_options`**（它本来就是逐层发散的产出），但**不许填 `chosen / skipped_mode / reason / closure_boundary / attack_target`**——这些是收敛动作，只能作者填。
4. **优先当场记录。** 当场记的 `reason` 才是当时的收敛；隔天记的是重构。允许事后补记，但必须标 `late_entry: true`，回看时（§3）对补记条目降权，而不是完全禁止追溯。

---

## 2. 条目模板（复制这段）

```markdown
### CT-YYYYMMDD-NN

- **date**: YYYY-MM-DD
- **seed_fragment**（作者原话，逐字）: …
- **layered_options**（LLM 逐层产出的选项全集）:
  - 命题锻造命中项（压力测试点名的、作者必须拍板的决定）: …
  - 层1 · 思路结构选项全集: ① … ② … ③ …（列全）
  - 层2 · 理论内容选项全集 + canonical 核对状态（每件标 已核 / NEEDS_RETRIEVAL）: …
  - 层3 · 写作手法选项全集: … （提醒：手法必须最后一层）
  - 被划掉的不相容分支（因某层选择而死掉的下游分支）: …
- **chosen**（作者在每层选了哪个；逐层写）:
  - 命题: …
  - 层1: …　层2: …　层3: …
- **skipped_mode**（主动跳过的众数选项；确无则填 none_detected + 原因）: …
- **reason**（作者亲写，一句话）: …
- **reason_note**（可选，几句展开）: …
- **closure_boundary**（谁承受后果 / 看多远）: …
- **attack_target**（拆哪块"本来如此"）: …
- **pruned**（为"一文一刀"主动 park 掉的真东西，非众数）: …
- **reclaimed**（某个 pruned 分支被事后讨还：折入本篇 / 另开新篇）: …
- **late_entry**（事后补记则填 true，缺省视为当场记录）: …
- **article_ref**: （成文后回填）
- **platform**: （发布后回填）
- **reader_resistance**: （发布后回填）
- **topic_index_id**: （若命中）
- **note**: 
```

## 2a. 指针条目模板（非 article 类 trace 用）

`intuition_mining` / `decision` 类 trace 的完整记录以独立文件存在（字段与协议按 `_SRT_CHOICEMAP_TRACE_WORKFLOW.md`），本台账只登记指针，保证台账仍是全部轨迹的唯一总目录：

```markdown
### CT-YYYYMMDD-NN（pointer）

- **trace_type**: intuition_mining / decision
- **trace_mode**: live / retro_writeback
- **date**: YYYY-MM-DD
- **trace_file**: （独立 trace 文件路径）
- **one_line**: （这条轨迹挖了什么，一句话）
- **breakout_count**: （越界选择次数；越界是 revealed-stake 最浓的样本）
- **pending_confirmations**: （assistant_proposal_pending 的条目；无则 none）
- **closure_pipeline_done**: true / false（`_SRT_CHOICEMAP_TRACE_WORKFLOW.md §5` 收尾管线是否走完）
```

---

## 3. 周期性回看（每积累约 20 条做一次）

不解读单条，解读**分布**：

- **偏置显影**：`chosen` 里反复出现的角度类型 / 借用的领域 —— 作者的稳定切入面。
- **反众数指纹**：`skipped_mode` 里反复被跳过的众数类型 —— 这是"锋芒"最直接的负空间刻画。
- **边界偏好**：`closure_boundary` 的分布 —— 作者习惯把后果看多远、算谁进来。
- **塌缩预警**：若近 N 条的 `chosen` 开始向少数母题集中（对齐 `SRT_TOPIC_ARTICLE_INDEX.md` 的塌缩警告），说明发散池老化，需要换素材源。
- **回流校准**：把 `reader_resistance` 与当初的 `attack_target` 对照 —— 真实读者在哪里顶住了，这是将来若重开书稿修订时最有价值的弹道数据（比内部自洽性优化更有证据价值）。

> 回看产出写入 `Operations/` 的周期留痕，不改写本台账已有条目（append-only）。

---

## 4. 轨迹记录区（append-only，最新在下）

<!-- 从这里开始按时间顺序追加轨迹条目。不修改历史条目。 -->

### CT-20260709（pointer）

- **trace_type**: intuition_mining
- **trace_mode**: retro_writeback
- **date**: 2026-07-09
- **trace_file**: `01_Source_Intuition/SRT_FIRST_INTUITION_SELECTION_BEFORE_EXISTENCE_CHOICE_TRACE_2026-07-09.md`
- **one_line**: 挖掘"选择先于存在"的第一直觉，收敛出 P1–P14 源头命题簇（非自我抹除、失败选择生成边界、熵=去选择化画像、耗散结构桥定位）。
- **breakout_count**: 3+（CT-05 选项外给出「非自我抹除」；CT-14 上移一层；CT-17/18/19 连续以自答替代选项）
- **pending_confirmations**: CT-13（P8「选对」定义为 assistant proposal，未二次确认）；CT-23（耗散结构 C+D 排序为 assistant analysis proposal，trace 内已标注）
- **closure_pipeline_done**: true（收尾审计见 trace 文件 §6，2026-07-09 补做）
