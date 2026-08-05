---
id: SRT-REVIEW-QUEUE
type: review_queue
status: active
version: v2
layer: meta
epistemic_layer: os
claim_mode: governance
canonical: false
tags: [ReviewQueue, Gaps, Tensions, HumanReview]
dependency: [SRT-DAILY-REVIEW-PIPELINE, SRT-EQ-HYP-MAP]
updated: 2026-08-05
---

# SRT 待人工审查队列

> 本文件只保留真正需要人工裁决或明确工作线触发的事项。旧检查结果不能因为长期未关闭而自动保持有效；架构、owner 或任务主线变化后，必须先重新裁决。

## 优先级

- **High**：需要作者决定，或会影响入口、变量、claim level 与下游引用；
- **Med**：有效研究／工程任务，但不阻塞当前主线；
- **Low**：触碰相关文件时顺带修复的治理债务。

---

## A. 当前需要作者裁决

| 编号 | 来源 | 决策问题 | 当前护栏 | 优先级 | 状态 |
|---|---|---|---|---|---|
| RQ-2026-08-A01 | `Core_Law/SRT_Core_Text_CN.md` / `SRT_Core_Text_CN_Euclid.md` / `SRT_Selection_Argument.md` | Euclid 版是否进入正式 registry / canonical 导航；中文普通版与形式版是否并列；`Selection_Argument` 是否继续降负担 | 未裁决前不建立第二定义 owner，不扩大 `claim_mode` 枚举 | High | Awaiting author |
| RQ-2026-08-A02 | `01_Source_Intuition/Conversations/2026-07-25_具身位_d_q_o_收尾审计.md` | `q` 是 stake gate 后的构成深度剖面还是独立轴；`o` 是否操作化、是否设符号 | 符号重命名和形式选择完成前，`d/q/o` 不得进入书稿、公共内容、bridge 或论文 | High | Awaiting author |
| RQ-2026-08-A03 | PHYSICS31 Bell / PHYSICS32 Decoherence / PHYSICS33 Born Rule author-landing batch | 三张 patch 继续独立停驻、合入未来 Physics v0.2，还是进入现有量子 owner | 不得将 Bell、退相干或 Born rule 写成 SRT 证明；不直接改 canonical | High | Awaiting author |

统一裁决包：

`Operations/Decision_Packets/SRT_AUTHOR_DECISION_PACKET_DQO_PHYSICS_EUCLID_2026-08-05.md`

---

## B. 触发式延期任务

| 编号 | 原发现日期 | 来源 | 当前裁决 | 复活触发 | 优先级 | 状态 |
|---|---|---|---|---|---|---|
| RQ-DEF-01 | 2026-03-11 | `_SRT_VERTICAL_INTEGRATION.md §4.5` / Eq-Multi-03 | `D_eff(F_collective)` 测量代理仍是有效 P4 问题，但不属于当前材料／投稿收口 | 集体选择实验或 unified formal-core paper 正式重启 | Med | Deferred |
| RQ-DEF-02 | 2026-03-16 | `_SRT_EQ_HYP_MAP.md` / G2 Wikimedia MVP | LDP 数据管线为 Partial 后续，不再作为当前 High gap；小样本扩展需独立实验计划 | G2 / LDP 工作线点名，且先冻结窗口、映射和判断规则 | Med | Deferred |
| RQ-DEF-03 | 2026-03-02 | `_SRT_EQ_HYP_MAP.md` | 经济学和演化 bridge 未建立，但休眠域不因旧季度计划自动开工 | 论文、书稿或跨域审计明确需要该 bridge | Med | Deferred |
| RQ-DEF-04 | 2026-03-09 | `Operations/_SRT_DAILY_REVIEW_PIPELINE.md` | 占位模式示例可能产生误报；只在审查器下一次实质修改时加入示例白名单 | Pipeline 6 checker 被触碰或误报再次出现 | Low | Touch-based |
| RQ-DEF-05 | 2026-03-09 | 旧扫描中的 26 个 d-value 引用命中 | 旧计数已过期，禁止按“26 文件”盲目批处理 | 新 governance audit 重新生成当前清单后再处理 | Low | Re-audit required |

这些条目不是当前欠账，不应被自动排入每日施工。

---

## C. 本轮判定为已解决或被取代

| 原发现日期 | 处理日期 | 来源 | 原问题 | 处理方式 | 状态 |
|---|---|---|---|---|---|
| 2026-03-02 | 2026-08-05 | `Core/SRT_Core_01_Axioms.md` | A10/A11 Part B 缺标准化实验钩 | 该文件与旧 A-numbering 已被 Core 21 P0/P1/P2-P4 分层和现有实验／bridge 路由取代；不得向旧 owner 回写。未来若仍有实验缺口，从当前 owner 重新立项 | Superseded |
| 2026-03-16 | 2026-03-16 | `_SRT_EQ_HYP_MAP.md` | Eq-LDP-01 / Eq-LDP-02 为 Gap | 已通过相关一手文献推进为 Partial；后续数据执行转入 RQ-DEF-02 | Resolved at mapping level |
| 2026-03-05 | 2026-03-16 | `_SRT_EQ_HYP_MAP.md` | Eq-Select-Thermo / Eq-LDP-01 / Eq-LDP-02 三条 Gap | Eq-Select-Thermo 通过三代理与文献锚推进为 Partial；不得继续写作“三条 Gap 未补” | Resolved at mapping level |
| 2026-03-02 | 2026-03-11 | `_SRT_VERTICAL_INTEGRATION.md §4` | d_collective 聚合方案未形式化 | 框架层改为 collective landscape 优先与 Eq-Multi-01/02/03；实证代理另列 RQ-DEF-01 | Resolved at framework level |
| 2026-03-02 | 2026-03-02 | 多文件 | d-value 定义分裂 | `_SRT_D_VALUE_CANONICAL.md` 已统一定义 | Resolved |
| 2026-03-02 | 2026-03-02 | `Neuroscience/SRT_Neuro_10_Advanced_Models.md` | 感受—摩擦循环 | 已加入单向因果链声明 | Resolved |
| 2026-03-02 | 2026-03-02 | `Core/_SRT_Core_Bridge.md` | L2 语义漂移 | 已增加热力学封闭条件；后续以当前 Core 21 owner 为准 | Resolved |
| 2026-03-02 | 2026-03-02 | `AI/_SRT_AI_Bridge.md` | AI 屏障永久／可突破歧义 | 已加入工程性／原则性区分 | Resolved |
| 2026-03-02 | 2026-03-02 | `Spirituality/_SRT_Spirit_Axioms.md` | Omega 拓扑极限与具身公理冲突 | 已加入边界声明 | Resolved |

---

## D. 入队规则

新的 review item 必须同时写明：

1. 当前 owner；
2. 它是否需要作者决定；
3. 不处理会阻塞什么；
4. 复活触发或完成定义；
5. 是否可能被新版架构取代。

禁止：

- 用旧扫描计数代替当前审计；
- 把 open tension 自动转成开发 TODO；
- 把 trigger-based parked item 当作按时间排队的欠账；
- 向 superseded owner 文件补功能；
- 在未经过作者门时自动修改符号、入口或 canonical claim level。
