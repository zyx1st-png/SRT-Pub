---
id: SRT-NB1-W0-DATA-ACCESS-PROVENANCE-20260812
type: access_record
status: active
canonical: false
claim_level: P4
claim_mode: lab_hypothesis
layer: neuroscience_lab
epistemic_layer: bridge
created: 2026-08-12
updated: 2026-08-12
search_as_of: 2026-08-12
request_status: draft_not_sent
lane_a_status: access_unknown_request_required
ai_do_not_use_for_definition: true
dependency:
  - Neuroscience/SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md
  - Operations/SRT_NEURAL_NORMALIZATION_BEHAVIORAL_SELECTION_FLOOR_AUDIT_2026-08-12.md
tags: [Neuroscience, P3-Scale-NB1, P4, W0, data-access, provenance, mOFC]
---

# NB1 W0：数据访问与来源记录

## 0. W0 判决

**状态：🟡 部分完成。** 公开来源核查与最小请求包已经完成，但外部数据请求尚未发送，作者是否会提供数据、代码及再利用许可仍是开放问题。因此：

- Lane A 目前是 `access_unknown_request_required`；
- 不得把论文图表、补充材料或跨研究数据拼接成 trial-level 原始数据；
- 即使数据完整取得，Lane A 仍只承担回溯复现与可行性审计，不足以单独把 `P3-Scale-NB1` 转绿；
- 在 W0 得到明确访问结果前，本工作流不进入 W1。

本记录不发送邮件、不代表作者已经同意共享，也不建立任何 canonical 主张。

---

## 1. 本步唯一连接

本步只检验：

```text
published Yamada workline
→ accessible, licensed, trial-linked neural + behavioral package
→ Lane A reproduction is technically admissible
```

### 负担标注

| 判断 | 标签 | 状态 |
|---|---:|---|
| 论文存在且明确给出通信作者和数据获取口径 | D | 已核实 |
| 若能取得 trial-linked 神经与行为数据，Lane A 可尝试复现 | C | 条件已列明 |
| 当前公开网页已经提供可下载原始数据和分析代码 | O | 未发现，不能断言绝对不存在 |
| 作者会提供足够数据、代码和再利用许可 | O | 未知；须经外部请求验证 |
| Lane A 可以给出完整 P3 绿色裁决 | S / 不成立 | 缺少同工作线神经干预，且论文描述的是单神经元记录 |

### 裸句

> 只有当原研究的数据包保留 trial、unit、session、task condition、offer、choice 与 neural response 的稳定关联，并允许合法再分析时，Lane A 才能进入复现；论文级统计量和图片不满足这一条件。

---

## 2. 公开来源核查

核查日期：2026-08-12。

| 入口 | 核查结果 | W0 含义 |
|---|---|---|
| Nature Communications 正式文章 | 正式文章与 PDF 可访问；文章声明相关数据可向作者获取 | 数据不是文内直接下载包；须联系作者 |
| 正式 PDF / 作者公开 PDF | 给出通信作者 Hiroshi Yamada 及材料请求邮箱；没有给出公共数据仓库标识 | 存在可执行的请求路径 |
| Supplementary Information | 论文提供补充图表／方法材料 | 不能替代 raw trial-level neural and behavioral data |
| DOI／标题精确检索 | 截至核查日，没有定位到明确归属于该论文的 GitHub、OSF、Zenodo、Figshare、DANDI、OpenNeuro 或 CRCNS 原始数据／代码包 | 记为“未定位到”，不是“证明不存在” |
| 论文 Code availability | 该 2018 文章未提供独立的可执行代码仓库入口 | 分析代码必须一并请求；如不可得，W1 只能做规范重实现 |

主要来源：

- Yamada et al. (2018), *Nature Communications*: <https://www.nature.com/articles/s41467-017-02614-w>
- Publisher PDF: <https://www.nature.com/articles/s41467-017-02614-w.pdf>
- Author-hosted PDF: <https://www.cns.nyu.edu/~klouie/papers/YamadaLouieTymulaGlimcher2018.pdf>
- Author publication page: <https://www.cns.nyu.edu/~klouie/publications.html>

**检索边界：** 公共网页的负面检索不能证明私人、失效、未索引或后续迁移的数据包不存在。W0 的结论只是“没有可确认的公共直达包，当前应走作者请求路径”。

---

## 3. 论文内可确认的复现边界

文章描述了两个猴子的 mOFC 单神经元记录、cued-lottery task、四个 payoff blocks、free／forced trial 条件、20 个 lottery pairs，以及对 advanced fractional、simple fractional、difference 与 range-normalization 模型的比较。文章也报告了训练／测试式交叉验证。

这些信息足以重建一个**方法级候选**，但不足以完成 NB1 的冻结读出，因为公开文章没有提供：

1. 可直接下载的 trial × unit × session 原始表；
2. 与每个神经 trial 稳定对应的选择事件、时序和排除标记；
3. 原始 spike times 或可验证的窗口化 firing counts；
4. 原模型拟合、初始化、参数边界、随机分割与诊断代码；
5. 面向 NB1 外层 held-out 读出的预先固定分割；
6. 同工作线神经干预数据。

此外，论文描述的是 single-neuron recordings，而不是一个明确的 simultaneously recorded population。即使获得全部历史数据，任何跨 unit 聚合都应标为 pseudo-population；它可以检验可行性，不能替代 Lane B 的同时群体记录与干预门。

---

## 4. 最小可接受数据包

只有下列字段能够稳定关联，W1 才可启动。

### A. Trial table

- anonymized animal ID, session ID, unit ID, trial ID;
- payoff block、lottery-pair ID、free／forced task label;
- risky/safe magnitude、probability、expected value;
- screen side、cue/order condition、trial timestamps;
- chosen target、saccade onset/landing、reaction time、outcome;
- fixation break、abort、omission、invalid／exclusion code;
- reward history or at least immediately preceding outcome variables used by the original analysis.

### B. Neural table

- raw spike timestamps preferred; otherwise the exact window-level counts used in publication;
- cue、saccade、feedback event timestamps and window definitions;
- unit quality metadata, recording date/session, electrode/site metadata at the releasable resolution;
- explicit mapping between each neural record and the corresponding trial row.

### C. Analysis provenance

- original analysis scripts if available;
- exact equations for M1–M10 and behavioral models;
- optimizer, initialization, bounds, convergence criteria and software versions;
- unit/epoch screening logic and the mapping from 182 sampled units to the reported 101-unit and 81-activity analysis sets;
- cross-validation split construction, seeds or stored fold identifiers;
- data dictionary, README, licence/reuse terms and citation requirements.

### Non-negotiable gate

If neural activity cannot be linked to the animal's trial-level choice and task condition without reconstructive guessing, Lane A closes. Aggregated figure values, condition means without trial identifiers, or neural data without behavioral event linkage are insufficient.

---

## 5. 数据／代码请求草稿（未发送）

**Request log**

| Field | Value |
|---|---|
| prepared | 2026-08-12 |
| recipient route | corresponding author listed in the article: Hiroshi Yamada (`h-yamada@md.tsukuba.ac.jp`) |
| status | `draft_not_sent` |
| external action | requires explicit user authorization and sender identity／affiliation |
| follow-up | one courteous follow-up after 14 calendar days if sent; no repeated contact without new instruction |

### Subject

Request for trial-level data and analysis code for Yamada et al. (2018)

### Body

> Dear Professor Yamada,
>
> I am preparing a methodological reproduction and feasibility analysis of the neural normalization models reported in “Free choice shapes normalized value signals in medial orbitofrontal cortex” (Nature Communications, 2018; DOI: 10.1038/s41467-017-02614-w).
>
> Would it be possible to share the trial-level neural and behavioral data underlying the reported analyses, together with the analysis code or sufficient implementation details to reproduce the model comparisons? The minimum useful package would preserve the mapping among anonymized animal/session/unit/trial identifiers, offer variables, free/forced condition, choice and saccade events, exclusion flags, neural spike times or analysis-window counts, model-screening membership, and cross-validation folds. A data dictionary and reuse/citation terms would also be appreciated.
>
> The intended use is a non-clinical methodological reproduction and an explicitly exploratory held-out neural-to-choice feasibility test. Any pseudo-population limitation would be reported, and the work would not claim that the historical dataset contains a causal intervention or establishes a unique neural mechanism.
>
> If full trial-level release is not possible, please let me know whether a de-identified reduced dataset, original analysis scripts, or stored model inputs and fold assignments can be shared instead.
>
> Sincerely,
>
> [Name]
> [Affiliation]
> [Contact information]

This draft deliberately avoids claiming collaboration, approval, preregistration, or guaranteed publication.

---

## 6. Response coding and W0 exit rule

| Code | Response | Lane A decision |
|---|---|---|
| A | trial-linked neural + behavioral data, sufficient provenance, and reuse permission supplied | W0 green; start W1 reproduction |
| B | partial package supplied | compare against §4; start only the analyses whose gates are satisfied; otherwise request one clarification |
| C | data unavailable, permission denied, or linkage irrecoverable | close Lane A red; retain paper as design evidence only |
| D | no response after initial request plus one authorized follow-up | mark access unresolved; do not infer refusal; close active W1 scheduling and proceed only after a new decision |

W0 exits only after A, B, C, or D is recorded with date and evidence. “Email drafted” is not an exit condition.

---

## 7. 当前地板状态

```text
published workline -> identifiable source/provenance                 🟢
source/provenance -> publicly downloadable trial-level package      🔴 not located
author request -> adequate reusable package                          🟡 open
adequate package -> technically admissible Lane A reproduction       🟡 conditional
Lane A reproduction -> full local P3 pass                            🔴 insufficient by design
```

### 最强反例

即使作者提供全部历史数据，原研究的单神经元记录、既有筛选和无神经干预设计仍可能只允许一个带选择偏差的 pseudo-population 复现。回应不是放宽 P3 门，而是把 Lane A 的上限固定为“复现／可行性／失败侦测”，把完整判决留给 Lane B。

### W0 判决

**🟡 条件连接。** 访问路径存在，但可用数据包尚未获得。下一动作是经授权发送一次请求；在收到可编码结果前，不进入 W1。
