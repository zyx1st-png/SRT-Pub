---
id: SRT-STRATEGY-MATHEMATICAL-REACHABILITY-PROBLEM-INDIVIDUATION
title: "数学可达结构、研究问题制度与条件性重新个体化：论文写作大纲与策略"
title_en: "Mathematical Reachability, Research-Problem Regimes, and Conditional Re-Individuation"
status: strategy_note_v0_6
canonical: false
layer: philosophy_bridge
epistemic_layer: bridge
claim_mode: mixed
primary_claim_level: P3
date: 2026-08-02
supersedes:
  - strategy_note_v0_5 @ 1f1f9b4fd214e3293bfd7dc30287c8844f4598c8
proposed_paper_title: "When Mathematical Problems Change: Forcing and the Historical Reconstitution of Resolution"
target_journals:
  - Philosophia Mathematica
  - Synthese
  - Foundations of Science
claim_governance:
  framework_claims: P2/P3 philosophical proposals
  strong_semantic_reindividuation: conditional on C2 evidence
  research_regime_reconstruction: primary paper claim
  srt_domain_mapping: P3 bridge
  mathematical_history_claims: externally sourced evidence required
  curvature_kappa0_godel: interpretive extensions only
machine_summary: >
  Version 0.6 separates semantic question identity from the broader research-problem regime.
  The semantic layer is Q_sem=<D,R_t>; the research layer adds background theories, local
  methods and an evaluation map. Forcing is claimed to reconstruct the CH research regime
  and the set-theoretic update regime. Strong semantic re-individuation is conditional on
  evidence that no conservative role translation exists. Conservative translation is now
  typed by explicit role and value maps. C2 and C5 are load-bearing; C3 and C4 are only
  corroborative. A calibrated result-innovation control case is mandatory. M_t is defined as
  the restriction of the global update regime U_t to a question. C6 is recast as a structural
  quasi-inverse relative to an explicit output-equivalence relation. The SRT section has a
  preregistered three-level fallback from directional prediction to explanatory mapping to
  deletion from the submitted paper.
---

# 数学可达结构、研究问题制度与条件性重新个体化
## 论文写作大纲与策略 v0.6

> **文件性质**：内部策略文件，不是投稿正文。  
> **本版任务**：完成最后一轮形式硬化，不再增加新的宏观概念。  
> **核心修订**：区分“语义问题身份”与“研究问题制度”；修复 C2/C3 的类型；将 C2 与 C5 设为不同层次的承重条件；增加保守标定案例；预注册 SRT 三级回退。  
> **治理纪律**：forcing、CH、潜在主义、问题语义学与数学史事实必须由外部原始或权威文献支持；SRT 文档只支持 P3 桥接。

---

# 0. 一句话裁剪标准

\[
\boxed{
\text{forcing 没有创造 CH 的命题问题核或改变其直接答案核；}
\atop
\text{它确定地重构了 CH 的研究问题制度与集合论更新制度，}
\atop
\text{并可能在更强意义上重构其响应角色结构。}
}
\]

全文只承担四项任务：

1. 区分语义问题身份与研究问题制度；
2. 证明 forcing 改写了可继承的集合论更新制度；
3. 用 C2 判断是否发生强语义重新个体化，用 C5 判断是否发生制度重构；
4. 说明该改写历史生成但受形式约束。

若正文只能证明“方法变得更方便”，论文失败。

---

# 1. 论文定位

## 1.1 首选题目

**When Mathematical Problems Change: Forcing and the Historical Reconstitution of Resolution**

中文：**当数学问题发生改变：Forcing 与解决制度的历史重构**

## 1.2 可选的更精确题目

**Forcing and the Reconstitution of the Continuum-Hypothesis Research Problem**  
**Forcing 与连续统假设研究问题的重构**

若历史材料不足以支持强语义重新个体化，投稿题目应优先采用第二个版本。

## 1.3 目标期刊

1. **Philosophia Mathematica**
2. **Synthese**
3. **Foundations of Science**

## 1.4 暂不承担

- 数学真理由历史创造；
- forcing 改变 CH 的直接真值核；
- 统一数学曲率；
- \(\kappa_0>0\) 推出 Gödel 不完备性；
- 数学不存在终极基础。

---

# 2. 最近邻理论与解释缺口

## 2.1 范围表

| 路线 | 潜在对象／扩展 | 本文处理 |
|---|---|---|
| forcing／width potentialism | 泛型扩展、新子集 | 直接最近邻，详细讨论 |
| height potentialism | 更高秩／层级 | 比较对象 |
| class potentialism | 类、谓词、真理资源 | 提醒汇聚公理可失败 |
| arithmetic potentialism | 算术模型扩展 | 后续推广 |
| strict／loose | 真理承担者条件 | 第一篇不裁决 |
| convergent／divergent | 是否有共同上界 | 限制全局汇聚叙述 |

## 2.2 篇幅纪律

第二节约 1,050 词：

- forcing／width potentialism：650—700词；
- 数学实践哲学：140—170词；
- 固定背景发现论：140—170词；
- 其他潜在主义：80—120词＋上表。

不能写成潜在主义分类巡礼。

## 2.3 正面差异

forcing potentialism 研究对象层访问关系，例如：

\[
M\preceq_F M[G].
\]

本文研究历史—实践层问题：

> 这种模型访问结构如何成为可公开重构、复用、传授和继承的数学操作，并进一步改变围绕 CH 的响应角色、进展标准与后续研究操作？

核心区分：

\[
\boxed{
\text{model accessibility}
\neq
\text{historical institutionalization of an accessibility operation}
}
\]

若该差异只能靠更换术语表达，论文失败。

---

# 3. 双层问题结构

## 3.1 命题问题核与直接答案

令：

\[
Q_{CH}=\text{“CH 是否成立？”}
\]

直接答案核：

\[
D(Q_{CH})=\{CH,\neg CH\}.
\]

第一篇明确承认：

- \(Q_{CH}\) 在 Cohen 之前已经存在；
- forcing 没有改变 \(D(Q_{CH})\)；
- 独立性不是对唯一宇宙中 CH 真假的直接 yes/no 回答。

## 3.2 语义问题身份层

定义：

\[
\boxed{
Q_t^{sem}(Q_\varphi)=\langle D(Q_\varphi),R_t(Q_\varphi)\rangle
}
\]

其中：

- \(D\)：直接答案核；
- \(R_t\)：响应角色结构，例如 direct answer、partial answer、metamathematical diagnosis、dissolution、problem splitting。

这一层承担“问题在语义—响应意义上是否被重新个体化”的主张，并直接与 Hamblin、Belnap & Steel、Wiśniewski 及当代 question semantics 对话。

## 3.3 研究问题制度层

令 \(\mathcal O_t(Q_\varphi)\) 为围绕问题产生的候选研究输出。定义：

\[
\boxed{
Q_t^{research}(Q_\varphi)
=
\langle
Q_t^{sem},B_t,M_t,E_t
\rangle
}
\]

其中：

- \(B_t\)：默认背景理论与可竞争扩展；
- \(M_t\)：对该问题可实施的方法集合；
- \(E_t\)：评价映射：

\[
E_t:\mathcal O_t(Q_\varphi)\to R_t\times V_t,
\]

- \(V_t\)：充分性、证据强度或进展地位的预序／偏序。

类型关系：

\[
R_t=\text{响应角色结构},
\qquad
E_t=\text{把候选输出归入角色并赋予进展地位的规则}.
\]

因此 \(R_t\) 与 \(E_t\) 不是两个同类内容坐标。

## 3.4 两种结论强度

### 强语义重新个体化

若 \(R_t\) 发生不可保守翻译的结构变化，则：

\[
Q_t^{sem}\not\equiv_c Q_{t+1}^{sem}.
\]

### 研究问题制度重构

若背景、方法、评价和操作生成关系发生可继承、非局部的非保守变化，则：

\[
Q_t^{research}\not\equiv_c Q_{t+1}^{research}.
\]

第一篇的**最低必须证明结论**是第二项。第一项是条件性加强，不得在历史证据完成前预先宣布。

---

# 4. 类型正确的保守翻译框架

## 4.1 翻译数据

比较时刻 \(t\) 与 \(t+1\) 的制度，需要：

\[
\tau_{\mathcal O}:\mathcal O_t\to\mathcal O_{t+1},
\qquad
\rho_{\mathcal O}:\mathcal O_{t+1}\to\mathcal O_t,
\]

\[
\tau_M:M_t\to M_{t+1},
\qquad
\rho_M:M_{t+1}\to M_t,
\]

\[
\sigma_R:R_t\to R_{t+1},
\qquad
\rho_R:R_{t+1}\to R_t,
\]

\[
\sigma_V:V_t\to V_{t+1},
\qquad
\rho_V:V_{t+1}\to V_t.
\]

## 4.2 C1：直接答案连续性

\[
\tau_{\mathcal O}[D]=D,
\qquad
\rho_{\mathcal O}[D]=D.
\]

C1 的作用是确认问题核连续，不用于证明问题改变。

## 4.3 C2：响应角色保守可译性——语义承重条件

\[
\boxed{
\pi_R E_{t+1}(\tau_{\mathcal O}(o))
=
\sigma_R\bigl(\pi_R E_t(o)\bigr)
}
\]

反向亦然。

C2 失败的最强见证之一是：

\[
\exists r^*\in R_{t+1}
\quad
\forall r\in R_t,
\quad
\sigma_R(r)\neq r^*.
\]

即新制度存在无保守原像的响应角色。

但“\(\sigma_R\) 不满射”只是强充分条件，不是全部非保守性的定义。即使集合论上存在满射，角色内部结构、推论作用或生成关系也可能无法保持。

## 4.4 C3：评价序保持——佐证条件

对翻译像上的评价：

\[
v_1\preceq_{V_t}v_2
\Longrightarrow
\sigma_V(v_1)\preceq_{V_{t+1}}\sigma_V(v_2),
\]

反向亦然。

C3 单独失败不足以证明制度重构，因为普通新结果也可能改变局部证据排序。

## 4.5 C4：推论功能保持——佐证条件

候选输出的支持、阻断、问题生成、问题分化和方法迁移功能应由翻译保持。

C4 单独失败不足以证明制度型创新，必须与 C2 或 C5 的结构性变化共同出现。

## 4.6 C5：操作—输出生成保持——制度承重条件

若：

\[
m\leadsto_t o,
\]

则保守翻译要求：

\[
\boxed{
\tau_M(m)\leadsto_{t+1}\tau_{\mathcal O}(o)
}
\]

反向亦然。

C5 失败是 forcing 超出“新增一个结果节点”的核心证据：新制度中出现可继承、非局部、可背景化的操作，而旧制度没有保守对应物。

## 4.7 C6：结构准逆

定义输出等价：

\[
o\approx_t o'
\]

当且仅当二者在以下方面等价：

- 响应角色；
- 评价地位；
- 推论功能；
- 操作生成轮廓。

要求：

\[
\rho_{\mathcal O}\circ\tau_{\mathcal O}
\approx_t
\operatorname{id}_{\mathcal O_t},
\]

\[
\tau_{\mathcal O}\circ\rho_{\mathcal O}
\approx_{t+1}
\operatorname{id}_{\mathcal O_{t+1}}.
\]

投稿正文只需写“存在结构准逆”；完整定义可放脚注或附录。

## 4.8 判据分级

\[
\boxed{
\text{C2 承载强语义重新个体化；C5 承载研究制度重构；}
\atop
\text{C3、C4 只作佐证；C1 确认连续性；C6 控制翻译强度。}
}
\]

不得再写“C2—C5 中任意一项失败均同等证明非保守性”。

---

# 5. 实践状态、局部方法与制度创新

## 5.1 实践状态

\[
\mathfrak S_t=(\mathcal P_t,\mathfrak U_t)
\]

- \(\mathcal P_t\)：理论、模型、问题、概念和方法构成的可达景观；
- \(\mathfrak U_t\)：可公开重构、复用、传授和继承的全局更新制度。

## 5.2 局部方法与全局制度

明确：

\[
\boxed{
M_t(Q_\varphi)
=
\mathfrak U_t\!\restriction_{Q_\varphi}
}
\]

即 \(M_t\) 是全局更新制度在特定问题上的局部限制。

因此：

\[
\Delta M_t(Q)\neq0
\centernot\Rightarrow
\Delta\mathfrak U_t\neq0.
\]

只有当方法变化满足：

1. 可继承性；
2. 非局部性；
3. 背景化潜力；

才上升为制度型创新。

## 5.3 结果型与制度型创新

结果型创新：

\[
\Delta\mathcal P_t\neq0,
\qquad
\Delta\mathfrak U_t\approx0.
\]

制度型创新：

\[
\boxed{
h_t\text{ is regime-innovative}
\iff
\Delta\mathfrak U_t\neq0}
\]

并满足上述三项范围约束。

## 5.4 两种非交换性

| 类型 | 形式 | 作用对象 |
|---|---|---|
| 模态非交换性 | \(\Diamond_h\Diamond_w\varphi\stackrel{?}{\leftrightarrow}\Diamond_w\Diamond_h\varphi\) | 模型、世界、公式真值 |
| 历史非交换性 | \(F_b(F_a(\mathfrak S))\stackrel{?}{=}F_a(F_b(\mathfrak S))\) | 方法定义域、训练、实践状态 |

最小示例：

- 模态问题：先作高度扩展再作宽度扩展，是否到达与反向操作同类的世界？
- 历史问题：forcing 尚未制度化时，forcing iteration 这一更新操作可能尚无定义；forcing 形成后才进入 \(\mathfrak U_t\)。

二者类型不同，不能相互推出。历史非交换性只是强签名，不是制度创新的定义。

---

# 6. 表示中立性与可达景观

## 6.1 非模态示范

模态记法：

\[
M\preceq_F N.
\]

非模态二元关系：

\[
R_F(M,N)
\iff
\exists\mathbb P\in M\,
\exists G\subseteq\mathbb P\,
\bigl(
G\text{ is }M\text{-generic for }\mathbb P
\land
N=M[G]
\bigr).
\]

需要时再定义：

\[
M\models\Diamond_F\varphi
\iff
\exists N\bigl(R_F(M,N)\land N\models\varphi\bigr).
\]

中心论证只要求：

1. \(R_F\) 或等价扩展关系严格定义；
2. forcing 成为可继承操作；
3. 该操作改变 \(\mathfrak U_t\) 与 \(Q_t^{research}\)。

第一篇无须引入额外 forcing-poset 范畴。

## 6.2 可达景观

\[
\mathcal P_t=(\mathcal T_t,\mathcal R_t,c_t).
\]

- \(\mathcal T_t\)：当前可表达、调用和继承的理论、模型、问题、概念与方法；
- \(\mathcal R_t\)：扩展、解释、翻译、模型构造和证明依赖关系；
- \(c_t\)：多维路径成本。

\[
c_t(p)=
(c_{formal},c_{constructive},c_{proof},c_{translation},c_{training},c_{inheritance}).
\]

不假定成本维度可通约。

---

# 7. 主案例与标定案例

## 7.1 forcing 主案例的最低结论

论文必须证明：

\[
\boxed{
Q_{pre}^{research}(Q_{CH})
\not\equiv_c
Q_{post}^{research}(Q_{CH})
}
\]

主要承重于 C5：forcing 建立旧制度中没有保守对应物的可继承模型扩展操作，并改变后续独立性证明、公理评估、模型比较和问题生成。

## 7.2 强语义重新个体化的条件性结论

只有当历史材料支持 C2 失败，才写：

\[
Q_{pre}^{sem}(Q_{CH})\not\equiv_c Q_{post}^{sem}(Q_{CH}).
\]

可接受的证据包括：

- forcing 后形成旧角色结构中无保守原像的新响应角色或稳定子类型；
- 原有角色虽可集合映射，但其推论功能与问题生成结构不能保守保持。

不得简单写“独立性角色在 forcing 前不存在”。Gödel 的相对一致性工作与更早逻辑史必须被纳入比较。

## 7.3 forcing 前后审计

| 条件 | forcing 前 | forcing 后 | 预期 | 证据 |
|---|---|---|---|---|
| C1 直接答案 | \(CH,\neg CH\) | \(CH,\neg CH\) | 保持 |  |
| C2 响应角色结构 |  |  | 待历史审计 |  |
| C3 评价次序 |  |  | 佐证 |  |
| C4 推论功能 |  |  | 佐证 |  |
| C5 操作生成 | 无 Cohen forcing 对应操作 | 可继承 forcing 操作 | 预期失败 |  |
| C6 结构准逆 |  |  | 由 C2/C5 结果决定 |  |

## 7.4 保守标定案例——强制要求

必须选择一个**结果型创新对照案例**，证明判据并非对所有历史变化都报阳性。

对照案例要求：

1. 位于成熟且稳定的方法制度内；
2. 是重要新结果，但没有新操作类型；
3. 没有明显改变响应角色结构；
4. 没有形成新的可继承、非局部脚手架；
5. 有足够历史与技术材料支持保守翻译。

预期：

\[
Q_t^{sem}\equiv_c Q_{t+1}^{sem},
\qquad
Q_t^{research}\equiv_c Q_{t+1}^{research}
\]

至少在 C1、C2、C5 上保持。

策略阶段不凭印象指定具体定理。应在 forcing 技术史档案完成后，从成熟 forcing 实践或相近集合论领域中筛选一个公认的结果型创新。

## 7.5 标定矩阵

| 案例 | C2 | C5 | 结论 |
|---|---:|---:|---|
| forcing 制度形成 | 待审计 | 预期失败 | 至少研究制度重构 |
| 结果型对照案例 | 预期保持 | 预期保持 | 保守变化 |
| 可选边界案例 | 部分变化 | 部分变化 | 检验阈值与解释范围 |

没有保守标定案例，不进入投稿稿阶段。

## 7.6 技术准确性

正文必须：

1. 区分句法独立性、相对一致性与模型存在；
2. 不从 \(\operatorname{Con}(ZFC)\) 无条件推出可数传递模型存在；
3. 明确 ground model、generic extension 和外部元理论；
4. 正确处理 Boolean-valued models；
5. 区分模型真值与 ZFC 不可判定性；
6. 不把方法多样性直接推成多宇宙本体论；
7. 不把某一 forcing 模态逻辑推广到全部潜在主义。

## 7.7 宇宙观／多宇宙观中立

多宇宙论者重视 forcing extensions；宇宙论者也使用 generic absoluteness、\(\Omega\)-logic、内模型和新公理分析。两方真值观不同，但均可支持研究制度层的变化。

强语义重新个体化是否成立，不由宇宙观／多宇宙观立场预先决定，而由 C2 的角色结构审计决定。

---

# 8. 形式约束

“协议固定时后果不能投票改变”只作背景。

正面约束包括：

- 独立性；
- 模型满足；
- 相对一致性；
- 可解释性；
- 保守扩展；
- 证明论强度；
- 构造可行性。

自然理论的一致性强度结构只提供：

\[
\boxed{
\text{约束性证据，而非约束来源的归属性证据。}
}
\]

不得写：

\[
\text{一致性强度}=\text{完整数学成本}=\kappa.
\]

---

# 9. SRT 桥接与三级回退

## 9.1 非独有部分

数学有历史、路径依赖、迟滞、问题制度变化和 \(\Delta\mathfrak U_t\neq0\) 均非 SRT 独有。

## 9.2 P3 候选增量

SRT 的可区别候选增量：

> **选择性二阶写回：某些成功显现不仅被记录，还以方向不对称的方式降低兼容路径成本，并成为未来更新的背景脚手架。**

最小映射：

- \(L_0^{math}\)：尚未稳定显现、非均匀可达的候选路径；
- \(L_1^{math}\)：证明、模型、反例、独立性结果或方法创新；
- \(L_2^{math}\)：被继承和背景化的方法、证明库、训练和制度。

## 9.3 局部比较预测

\[
\boxed{
\Delta c_t(p_{compatible}\mid L_2^k)
<
\Delta c_t(p_{incompatible}\mid L_2^k)
}
\]

允许多个局部脚手架、分叉及不可合并路径，不预设全局汇聚。

兼容性必须事前定义，可依据方法复用、证明工具、背景公理、翻译接口、中间结果与训练库。

## 9.4 三级回退

### Level A：预测获得支持

保留约 650—750词 SRT 节，主张局部方向性二阶写回具有可区别的 P3 解释力。

### Level B：预测无显著差异

删除方向性预测，将 SRT 节缩至 300—400词，仅保留：

\[
L_1^{math}\to L_2^{math}
\]

的解释性映射，不声称相对一般数学实践哲学具有经验增量。

### Level C：解释映射也无额外内容

从投稿正文删除 SRT 独立章节，只在结尾或后续研究中注明该领域映射尚未成熟。

回退不能影响第3—8节的独立成立。

## 9.5 后置内容

\(\kappa_0\)、曲率、\(\Psi_f\) 与 Gödel 式开放性只作展望，不进入主论证。

---

# 10. 完整论文大纲与字数

目标正文约 **9,150词**；含形式附注上限 **9,800词**。

| 节 | 词数 | 任务 |
|---|---:|---|
| 1. Introduction | 700 | 两层问题结构、forcing 主结论、条件性强结论 |
| 2. Forcing Potentialism and the Missing Historical-Practical Level | 1,050 | 最近邻理论，重点 forcing potentialism |
| 3. Semantic Question Identity and Research-Problem Regimes | 1,250 | \(D,R_t\) 身份层；\(B,M,E\) 生成层；C2/C5 |
| 4. Forcing and the Reconstitution of the CH Research Regime | 2,600 | 主案例、技术史、C5、条件性 C2 |
| 5. Calibration and Formal Constraint | 800 | 保守对照、形式约束、一致性强度 |
| 6. The SRT Bridge | 650 | P3预测与三级回退 |
| 7. Objections and Failure Conditions | 1,450 | 最强反对意见 |
| 8. Implications | 400 | 开放性、表示中立、后续研究 |
| 9. Conclusion | 250 | 最低结论与条件性加强 |
| **正文合计** | **9,150** |  |

形式附注或附录最多 500—650词，用于完整 C1—C6 与 \(\approx_t\) 定义。

正文第三节只详细呈现 C1、C2、C5；C3/C4/C6 简述并指向形式附注。

---

# 11. 必须处理的反对意见

1. 固定背景发现论可接受全部变化；
2. 这只是数学实践哲学；
3. 直接答案没变，所以问题没变；
4. 研究问题制度只是语境，不属于问题身份；
5. 任何方法都改变制度；
6. C2 角色变化没有历史证据；
7. 判据对所有历史变化都报阳性；
8. 宇宙论者不接受重新个体化；
9. 一致性层级更支持柏拉图主义；
10. 这只是 forcing potentialism 的实践注释；
11. 模态装置可被非模态化；
12. 两种非交换性被混淆；
13. 语义引力预设全局汇聚；
14. SRT 只是后加标签。

关键回答纪律：

- Objection 3：承认 \(D\) 连续；强语义变化只由 C2 支撑；
- Objection 4：区分语义身份层与研究制度层，不用被争议的实践变量循环证明语义身份；
- Objection 5：要求 C5 具有可继承性、非局部性、背景化潜力；
- Objection 7：必须使用保守标定案例；
- Objection 10：对象层 accessibility 与实践层 reachability 分开；
- Objection 14：执行三级回退。

---

# 12. 写作顺序

1. 建立 forcing／width potentialism 最近邻矩阵；
2. 核查 question semantics 与 inferential erotetics，仅确认 \(D,R_t\) 的外部锚点；
3. 建立 C2 角色结构审计；
4. 建立 C5 操作—输出与制度写回审计；
5. 筛选并核查保守结果型标定案例；
6. 建立 forcing 技术—历史档案；
7. 先写第3、4、5、7节；
8. 最后写 SRT、摘要、引言和题目。

若 C5 无法证明，立即停止论文。  
若 C5 可证明但 C2 不可证明，保留“研究制度重构”，删除或弱化标题中的“problem change”。

---

# 13. 核心审计表

## 13.1 forcing 主案例

| 条件 | forcing 前 | forcing 后 | 预期 | 证据 |
|---|---|---|---|---|
| C1 直接答案 | \(CH,\neg CH\) | \(CH,\neg CH\) | 保持 |  |
| C2 响应角色 |  |  | 条件性失败 |  |
| C3 评价次序 |  |  | 佐证 |  |
| C4 推论功能 |  |  | 佐证 |  |
| C5 操作生成 | 无 Cohen forcing 对应操作 | 可继承 forcing 操作 | 预期失败 |  |
| C6 结构准逆 |  |  | 由 C2/C5 决定 |  |

## 13.2 保守标定案例

| 条件 | 变化前 | 变化后 | 预期 | 证据 |
|---|---|---|---|---|
| C1 |  |  | 保持 |  |
| C2 |  |  | 保持 |  |
| C5 |  |  | 保持 |  |
| 结果节点 | 无 | 新结果 | 改变 |  |
| 更新制度 | 稳定 | 稳定 | 保持 |  |

---

# 14. 主张、证据与撤回

| 主张 | 级别 | 所需证据 | 撤回／缩减条件 |
|---|---|---|---|
| 问题核／研究制度可区分 | 哲学框架 | question semantics＋实践分析 | 无法保持类型区分 |
| forcing 重构 CH 研究制度 | 中心主张 | C5＋技术史＋继承证据 | 仅增加结果节点 |
| forcing 强语义重新个体化 CH | 条件性主张 | C2 无保守角色翻译 | C2 可保持或证据不足 |
| 判据具有区分力 | 方法主张 | 保守标定案例 | 所有历史变化均报阳性 |
| 双层可达性可区分 | 定位主张 | 潜在主义与历史材料 | 两层可完全互定义 |
| 表示中立 | 方法主张 | \(R_F(M,N)\) 重写 | 核心推论依赖特定模态语义 |
| 一致性强度提供非任意约束 | 支撑主张 | 逻辑文献 | 不得据此裁决本体论 |
| SRT 局部方向性预测 | P3候选 | 匹配历史／形式数据 | 无差异则降级或删除 |

---

# 15. 禁止裸用

不得写：

- Cohen 前 CH 问题不存在；
- forcing 改变 CH 的直接答案核；
- 独立性是 CH 真值的直接回答；
- “独立性”作为响应角色在 forcing 前完全不存在；
- \(\sigma_R\) 非满射是所有非保守变化的唯一定义；
- C3 或 C4 单独失败足以证明制度创新；
- C2、C3 在不同集合上直接用等号或同一预序比较；
- \(M_t\) 与 \(\mathfrak U_t\) 无类型关系；
- 任何新定理都是制度创新；
- 判据无需保守标定案例；
- C6 的“等价于恒等”无需定义 \(\approx_t\)；
- 潜在主义没有研究可达关系；
- accessibility 等同 reachability；
- 两种非交换性相互推出；
- 模态可消除意味着制度问题消失；
- 一致性强度证明 SRT；
- \(L_0\) 等同层拓扑斯；
- \(c_t=\kappa(t)\)；
- \(\kappa_0>0\) 推出 Gödel 不完备性；
- 语义引力要求数学史全局汇聚。

---

# 16. 文献策略

优先建立：

1. Hamblin、Belnap & Steel、Wiśniewski及当代 question semantics；
2. Gödel、Cohen及 forcing 技术史；
3. Hamkins–Linnebo、Brauer 等 forcing／width potentialism；
4. 2026年 *Philosophia Mathematica* 潜在主义专刊；
5. Sutto 分类学；
6. Berry、Linnebo 的模态机制与非模态化；
7. height／class／divergent potentialism；
8. universe／multiverse、generic absoluteness、新公理；
9. 数学实践哲学；
10. 一致性强度与自然理论层级；
11. 数学方法创新、教材史、证明库和知识基础设施；
12. 用于保守标定案例的技术史材料。

问题语义学只直接背书 \(D,R_t\) 层。  
\(B_t,M_t,E_t\) 的构成作用必须由数学实践与历史材料独立论证。

---

# 17. 工作摘要骨架 v0.6

> The continuity of a mathematical sentence does not guarantee the continuity of the research regime organized around it. This paper distinguishes a semantic question layer, consisting of a direct-answer core and a structure of response roles, from a broader research-problem regime containing background theories, available methods, and evaluative practices. The continuum-hypothesis question existed before Cohen, and forcing did not alter its direct yes-or-no answer core. The paper's primary claim is that forcing non-conservatively reconstructed the CH research regime and the update regime of set-theoretic practice by introducing an inheritable, non-local model-extension operation with no conservative predecessor in the earlier methodological repertoire. A stronger claim—that the semantic response-role structure of the CH problem was itself re-individuated—is treated conditionally and tested by whether a structure-preserving role translation exists between pre- and post-forcing regimes. The framework is calibrated against a result innovation expected to preserve both response roles and the update regime. Forcing accessibility is formulated both modally and through an ordinary binary relation among models, leaving the historical-institutional argument representation-neutral. A final P3 bridge to Selective Reality Theory is retained only to the extent that a local, defeasible prediction of asymmetric cost reduction for scaffold-compatible paths survives empirical and historical comparison.

---

# 18. 投稿前检查

- [ ] 已建立 \(Q^{sem}=\langle D,R_t\rangle\) 与 \(Q^{research}\) 的双层结构；
- [ ] C2 使用 \(\sigma_R\)，C3 使用 \(\sigma_V\)；
- [ ] C2 与 C5 被明确设为不同层次的承重条件；
- [ ] C3、C4 仅作佐证；
- [ ] C6 使用明确的 \(\approx_t\)；
- [ ] \(M_t=\mathfrak U_t|_{Q_\varphi}\) 已声明；
- [ ] 没有扩大 CH 的直接答案核；
- [ ] 没有声称 forcing 前完全没有独立性响应；
- [ ] 已完成 forcing 主案例的 C2/C5 审计；
- [ ] 已选择并验证保守标定案例；
- [ ] 已用 \(R_F(M,N)\) 完成非模态重述；
- [ ] 最近邻节主要讨论 forcing potentialism；
- [ ] 已证明 forcing 不只是新增知识节点；
- [ ] universe／multiverse 中立性有跨立场证据；
- [ ] 一致性强度只作约束性证据；
- [ ] SRT 已预注册三级回退；
- [ ] 正文不超过 9,800词；
- [ ] 删除 SRT 后论文仍成立。

---

# 19. 最终执行指令

1. **CH 问题在 Cohen 之前已经存在，其直接答案核保持不变。**
2. **forcing 至少重构了 CH 的研究问题制度与集合论更新制度。**
3. **强语义重新个体化只能由 C2 的角色结构证据支持，不能由方法或评价变化循环证明。**
4. **C5 是 forcing 作为制度型创新的主要承重条件。**
5. **判据必须同时通过 forcing 主案例与一个保守结果型标定案例。**
6. **SRT 预测失败时必须降级或从正文删除。**

若不能证明第2、4、5句，不进入投稿稿阶段。  
若第2、4、5句成立但第3句证据不足，则使用较弱题目并删除“CH 问题本身发生强改变”的表述。
