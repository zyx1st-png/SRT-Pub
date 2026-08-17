---
id: SRT-MATERIAL-ADJUDICATION-WORKFLOW
type: workflow
tags: [Material, Adjudication, SecondRound, NotebookLM]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-EXECUTION-PLAN, SRT-MATERIAL-LOG, SRT-GOV-SYN01-ONTOLOGICAL-SYNTHESIS-DISCRIMINATION]
---

# SRT 材料第二轮结构裁决工作流

> **定位**：这是一个**独立辅助工作流**，不是六条主流水线之一。  
> **用途**：处理已经做过第一轮扩建的材料，或处理高争议、高过拟合风险、跨域、高传播风险材料。  
> **关系**：本工作流不替代 `Pipeline 1`；它的产出应回注到 `Pipeline 1`，由后者决定正文修改与台账落地。若最终建议为 `A`，默认还应进入 `Pipeline 1` 的一轮“去材料化改写”。  
> **贡献纪律**：所有裁决同时遵守 `Governance/SRT_GOV_SYN01_Ontological_Synthesis_and_Empirical_Discrimination_Protocol_v0_1.md`，不得把“独有经验增量”当成唯一理论价值标准。

---

## 1. 何时启动

出现以下任一情况时，推荐启动：

1. 材料已经先经过 `NotebookLM / Gemini / 其他预处理器`，形成候选接口稿
2. 材料很容易“看起来像 SRT”，但你怀疑只是漂亮类比
3. 材料跨域很强，主/备落点不清楚
4. 材料证据等级不稳，但又可能对 SRT 形成重要约束
5. 你不确定该给 `A / B / C` 中哪一个
6. 材料的局部机制已被成熟理论解释，但可能具有重要的 SRT 本体论整合价值
7. 第一轮因为“已有理论能解释”准备降级，但尚未检查 O-track synthesis value

推荐触发词：

- `材料裁决 <内容/URL/文件>`
- `二轮裁决 <内容/URL/文件>`

---

## 2. 输入要求

最少输入：

1. 原材料
   - 文本 / URL / 文件 / DOI 其一
2. 证据等级说明
   - `新闻解释 / 评论 / review / preprint / peer-reviewed / primary`

推荐附加输入：

3. 第一轮扩建输出
   - 候选接口
   - 反向修正
   - 五问预判
   - 过拟合警报

原则：

- 若只有第一轮输出、没有原材料，不启动裁决
- 若材料无法锚定到一手来源或可访问文本，必须在风险声明中保留证据缺口
- 任何 SRT synthesis 都必须能回到 source-derived 层，不得让 SRT 解释覆盖来源事实

---

## 3. 核心任务

本工作流做四件事：

1. 审查第一轮候选接口是否能承重
2. 先判断材料属于 `O-track / D-track / O+D / source-only`
3. 把材料压成最小可写命题
4. 给出 `A / B / C` 建议与文件落点建议

它**不负责**：

- 直接写正文 patch
- 直接修改仓库文档
- 把候选接口自动升格为正式结论
- 为了证明 SRT 独特而强造新变量、机制、scalar 或预测

但它应尽量为后续正文原生化提供条件，即：

- 把 surviving claim 压到足够短、足够硬，便于直接写成章节主句
- 避免输出只能以“这条材料真正补上的不是……”才能成立的候选命题
- 对 O-track 明确写出“外部理论提供局部机制 / 证据，SRT 提供关系组织”的边界
- 对 D-track 明确写出 SRT 额外承担什么可失败风险

---

## 4. 固定输出顺序

### 4.1 裁决建议

- `A / B / C`
- 用 `2-4` 句说明原因

### 4.2 贡献轨道

必须标明：

- `O-track`：本体论整合
- `D-track`：经验 / 判别增量
- `O + D`
- `source-only`

并分别回答：

```text
O-track value:
- 是否把已有的成熟结果放进一个非平凡的共同 SRT 结构？
- 是否澄清层级、bearer、boundary、history、stability 或 selection relation？
- 是否反过来约束 / 修正 SRT？

D-track value:
- 是否真的新增预测、干预、反事实区分或不可替代解释？
- 若没有，明确写 none / not claimed；不得强造。
```

### 4.3 最小可承重命题

只保留 `1-3` 条 surviving claims。

每条必须写：

- `Surviving claim:`
- `Epistemic level:` `OS / Bridge / Lab`
- `Contribution route:` `O / D / O+D`
- `Status:` `可写正文 / 只记台账 / 仅作暂定锚`

### 4.4 候选接口审查

对第一轮每条候选接口逐条标记：

- `保留`
- `降级`
- `拒绝`

每条只解释 `1-2` 句。

特别规则：

```text
“其他理论已解释局部机制”
!= 自动拒绝接口
```

先判断该机制是否仍能成为可靠的 O-track 结构材料；只有当它既无 synthesis payoff、也无 D-track increment、也不形成 guardrail / pressure 时，才因重复而降为 C。

### 4.5 文件落点

必须给出：

- 主落点文件
- 备选落点文件
- 不应落点文件

目标不是“多给选择”，而是减少错误 patch。

### 4.6 五问终裁

1. 新增接口
2. 反向修正
3. 加固内容
4. SRT反哺
5. 残余压力

要求：

- 可以回答“弱”或“不成立”
- 不得为了凑满五项而强行补齐
- O-track 的“加固内容”可以是已被外部理论建立、但首次在 SRT 中获得正确层级与共同结构的位置；不要求外部理论提供 SRT 独有事实
- D-track 必须单列其真正新增的风险，不得把 O-track synthesis 冒充为 empirical support

### 4.7 写作动作

固定从以下动作中选择：

- `可直接写正文`
- `只更新台账`
- `等待一手来源`
- `需复核主论文`

若选择“可直接写正文”，应补一行：

- `建议新增小节名：`
- `去材料化主句：`

`去材料化主句` 的要求：

- 不以材料、新闻、作者或“本次新增量”起手
- 直接陈述 SRT 将承重的命题
- 单独抽出后仍能像原生章节开头，而非融入说明
- 若主要为 O-track，优先写成“外部机制在 SRT 中的结构位置”，不伪装成“SRT 新发现了该机制”

### 4.8 风险声明

必须明确指出：

- 哪些地方最可能是偷换
- 哪些地方最可能是过拟合
- 哪些地方最可能是 HARKing
- 哪些地方最可能误判了证据等级
- 哪些地方可能把“source instantiates SRT structure”误写成“source proves SRT”
- 哪些地方可能为了逃避 prior art 而制造不必要的新概念

---

## 5. 裁决规则

### A 的门槛

只有当以下条件同时较稳时，才建议 `A`：

1. 材料具有**稳定贡献**，贡献可以来自：
   - `O-track`：非平凡的本体论整合、跨域结构压缩、层级澄清、对 SRT 的反向约束；
   - `D-track`：真实的预测 / 干预 / 反事实 / 机制判别增量；
   - 或两者同时存在；
2. 主落点明确
3. 至少能稳定回答五问中的两项，且不只是“新增接口”
4. 风险声明没有直接打穿正文动作
5. source-derived / SRT synthesis / SRT discriminating claim 三层可明确区分

因此：

```text
“局部机制已有成熟理论解释”
```

本身不能作为拒绝 A 的理由。

### B 的门槛

出现以下任一情况，优先 `B`：

1. O-track synthesis 疑似存在，但 source fidelity / mapping 尚未闭合
2. D-track increment 疑似存在，但证据等级仍偏低或 rival 未冻结
3. 一手来源未充分核验
4. 文件落点仍摇摆
5. 更像“待验证窗口”，而不是可写正文窗口

### C 的门槛

出现以下任一情况，优先 `C`：

1. 与现有内容高度重复，且不增加 synthesis / correction / constraint / discrimination
2. 只有词汇类比，没有稳定结构关系
3. 第一轮输出明显靠 SRT 过映射撑起来
4. 证据等级与正文负担严重不匹配
5. 必须歪曲来源或改写 SRT 定义才能吸收

---

## 6. 与 Pipeline 1 的关系

### 6.1 回注原则

第二轮结构裁决完成后，应把结果回注给 `Pipeline 1`。

回注内容只保留：

- `A / B / C`
- `贡献轨道：O / D / O+D / source-only`
- 最小可承重命题
- 主落点 / 备选 / 不应落点
- 五问终裁
- 写作动作
- 若为 `A`，追加 `去材料化主句`

第一轮的全部候选接口**不直接抄入台账**。

### 6.2 留痕原则

- 正式台账仍写在 `Operations/_SRT_MATERIAL_LOG.md`
- 正式正文修改仍由 `Pipeline 1` 执行
- 本工作流本身不替代正式执行留痕
- `O / D` 是治理阅读标签，不新增 machine enum；可写在 Material Log 备注、SourceCard 或 Patch 正文

---

## 7. 最小模板

可直接复用以下骨架：

```md
## 裁决建议
- A / B / C：
- 原因：

## 贡献轨道
- O-track：strong / weak / none
- D-track：strong / weak / none / not claimed
- 总体：O / D / O+D / source-only

## 最小可承重命题
- Surviving claim:
- Epistemic level:
- Contribution route:
- Status:

## 候选接口审查
- 接口 X：保留 / 降级 / 拒绝
- 理由：

## 文件落点
- 主落点：
- 备选：
- 不应落点：

## 五问终裁
- 新增接口：
- 反向修正：
- 加固内容：
- SRT反哺：
- 残余压力：

## 写作动作
- 可直接写正文 / 只更新台账 / 等待一手来源 / 需复核主论文
- 建议新增小节名：
- 去材料化主句：

## 三层边界
- Source-derived：
- SRT ontological synthesis：
- SRT discriminating claim（如无则写 none）：

## 风险声明
- ...
```

---

## 8. 一句话原则

> 第一轮负责看清材料，第二轮负责判断它是在**给 SRT 提供本体论构造材料、经验判别增量，还是两者都没有**；Pipeline 1 才负责真的施工。不要为了“独有增量”制造理论，也不要因为“别人已经证明”就拒绝把可靠知识纳入 SRT 的本体论建筑。