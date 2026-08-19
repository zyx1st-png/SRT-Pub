---
id: SRT-RESEARCH-CORPUS-INCREMENT-PR-PACKET-20260819
type: proposal
status: active
version: v1
record_stage: proposal_v1
layer: operations
epistemic_layer: os
claim_mode: operations_proposal
claim_level: P3/P4_candidate
canonical: false
ai_do_not_use_for_definition: true
date: 2026-08-19
dependency:
  - SRT-MATERIAL-PIPELINE
  - SRT-GOV-SYN01
  - SRT-CANONICAL-FREEZE
  - SRT-EDIT-PROTOCOL
  - SRT-SPIRITUALITY-CLAIM-STATUS
  - SRT-OPEN-TENSIONS
source_artifacts:
  - Operations/SRT_RESEARCH_CORPUS_INCREMENT_TAGS_2026-08-19.md
  - Operations/SRT_INITIAL_DEEP_READ_2026-08-19.md
---

# 研究语料增量 PR 裁决包（2026-08-19）

## 1. 结论

本轮把本机研究根目录的全量召回、86 文件初次深读与当前 owner 结构做了二轮去重。最终只授权一个 owner-level 改动：

> 冥想中的预测／反事实时间深度降低，不等于取消 Selection、停用 `L_2` 或接触 `L_0`。

该改动是 A 类、O-track 的 bounded corrective guardrail，不是新 canonical 命题，也不建立 D-track。Fields–Levin 的对象／过程互补论文保留为 B2 guardrail 来源卡；其余初筛簇只保留检索和谱系价值，不产生新 patch、hook、registry node 或 canonical rewrite。

## 2. 审计范围与方法

- 全量盘点：62,103 个文档路径、12,039 个独立内容哈希。
- 深读队列：86 个独立候选文件，H 级 73 个、M 级 13 个；包含 PDF 书籍、论文、DOCX、HTML 导出与碎片笔记。
- 初筛分布：`independent_candidate` 5、`conditional` 14、`source_map` 4、`guardrail` 8、`no_independent_increment` 55。
- 二轮判据：先以 current owner 和既有 SourceCard 去重，再按 `GOV-SYN01` 分开判断 O-track 与 D-track；自 authored 重述、翻译、版式副本和 AI 扩写不按独立增量计数。
- 本 PR 不提交全文抽取缓存、62k 路径 sidecar、Finder xattr 审计或语料副本。

## 3. 二轮裁决矩阵

| 初筛接口 | 当前已有承载 | 最小剩余命题 | 最终裁决 | 本 PR 动作 |
|---|---|---|---|---|
| 信息作为相对确定化／具身选择 | P0-01、AM-A、`Selection != Agency`、信息 writeback 的后置条件口径 | `selection event != information relation != bearer-relative evaluative use` | 不形成独立 owner 增量；O-track 谱系候选，D-track 无 | 保留初读台账；不建 SourceCard／patch |
| 对象—过程—记忆 | ST-A、EX-A、PH-DIFF01、PH-MEM01 与对象化 owner 已覆盖持续、重构、历史效力 | 对象／过程是持续性的互补描述；观察依赖可用记忆，但描述互补不自动给出 bearer individuation | **B2**；O-track guardrail，D-track 无 | 新建 Fields–Levin SourceCard；停驻并写明复活条件 |
| 冥想—预测加工 | Spirituality owner 已把 FA／OM／ND 直接映射为 `L_1/L_2/L_0`，且存在 `DMN=L_2` 式过强表述；RC-A 已固定 `Selection != Agency` | 降低时间／反事实深度或某类先验精度，不推出无 Selection、`L_2` 全局停用、`L_0` 接触或 DMN 身份映射 | **A，bounded corrective guardrail**；O-track only，D-track 无 | 新建 SourceCard；修正 `SRT_Spirit_07_Meditation_Neuro.md` 的 claim status 与非同一性 |
| 语言作为注意力路由 | `SRT_SocTheory_05_Language_Eco.md` 已承载 attention modulation / L2 constraint propagation | 只有回到 primary experiment 后，才可能增加具名 readout | C for current bundle / source-map only | 不建新节点；待一手实验触发 |
| 记忆的未来效用 | NEURAL28 → NEURAL29 → NEURAL25 → NEURAL27 已覆盖重识别、转化、可访问／控制／写回和未来使用 | 汇编报告未给出超出既有链条的独立机制或冻结 rival | C for current report / duplicate map | 不建新节点；只保留检索线索 |
| Thompson 书籍及宽泛意识／冥想材料 | 现有 self、neurophenomenology、HP-B-B 与 Spirituality claim-status 文档已有更精确路由 | 可作跨传统背景，不承担精确机制或证据升级 | B3/reference only | 不建 SourceCard；未来书稿或公共表达按章节触发 |

## 4. 唯一 owner 增量的承重边界

### 4.1 来源能支持什么

Laukkonen 与 Slagter（2021）提出一个预测加工综述框架，把 focused attention、open monitoring 与 non-dual practice 放在逐步降低时间／反事实深度的连续谱上，并提出练习类型和状态相关的可检验预测。论文自身把该模型限定为 practices and associated states，且明确要求更严格实验、神经现象学与 no-report 设计。

### 4.2 来源不能支持什么

该综述不能单独建立：

```text
reduced temporal/counterfactual depth = no Selection
reduced policy/precision weighting = no agency in every sense
open monitoring or non-dual practice = L2 suspension
non-dual state = contact with L0
DMN = L2
predictive model = L2
prediction error = L1 - L2
reported pure awareness = phenomenal or ontological theorem
```

### 4.3 SRT 侧允许保留的句子

> 冥想可被研究为对历史形成的预测习惯施加干预的一组实践；不同练习可能改变预测的时间／反事实深度与精度分配，但这些变化不决定 canonical Selection status，也不提供 `L_0/L_1/L_2` 的神经身份映射。

这是去材料化后的 P3/P5 bridge 句，不是对来源的改写，也不反向定义 Core。

## 5. O-track / D-track 结算

- O-track：一个有效增量，即把预测加工的局部机制变量与 SRT 层级／Selection 非同一化，关闭 owner 中的过强身份映射。
- D-track：本轮为 **0**。没有候选材料冻结 SRT 与 richer predictive-processing、active-inference、memory 或 process-ontology rivals，并给出独有结果变量。
- 外部来源支持 source claim；owner guardrail 是 SRT 的关系定位。两者不得写成“论文证明 SRT”。

## 6. 停驻项与复活条件

### Fields–Levin（B2）

只在以下任一条件出现时重开：

1. ST-A、selector individuation 或 bearer-boundary owner 被点名重审；
2. 实验设计需要把“记忆是观察资源”压成可操作的 reference-state / pointer-state 判据；
3. 新材料提供对象／过程描述无法互译的明确失败例，而不只是一般过程哲学重述。

### 信息／语言／未来效用记忆簇

只有 primary source close-read 给出当前 owner 未承载的具名关系、失败条件或 bounded rival discrimination，才重开。版本数量、关键词密度、生成稿长度或 Finder 标签均不构成触发。

## 7. PR 边界

本 PR 包含：两份审计报告、两张来源卡、一份索引、一处休眠域 owner 降级修正、Material Log 与 Status 同步。

本 PR 不包含：canonical 修改、新符号、新 patch/hook、全文语料复制、Finder 标签重写、书稿回写、经验验证或“初筛候选 = 已融入”的状态升级。
