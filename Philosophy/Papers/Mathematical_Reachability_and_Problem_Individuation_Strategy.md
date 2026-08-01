---
id: SRT-STRATEGY-MATHEMATICAL-REACHABILITY-PROBLEM-INDIVIDUATION
title: "数学可达结构与问题个体化：论文写作大纲与策略"
title_en: "Mathematical Reachability and Problem Individuation: Paper Outline and Writing Strategy"
status: strategy_note_v0_2
canonical: false
layer: philosophy_bridge
epistemic_layer: bridge
claim_mode: mixed
primary_claim_level: P3
date: 2026-08-01
supersedes:
  - "SRT_Mathematical_Accessibility_Paper_Strategy_v0_1.md (local strategy artifact)"
proposed_paper_title: "When Mathematical Problems Change: Forcing, Reachability, and the Historical Constitution of Mathematical Practice"
dependencies:
  - Core/SRT_Core_12a_Ontology_L0L1.md
  - Core/SRT_Core_12b_Ontology_L2.md
  - Core/Ontology_L2_Split/01_Part02.md
  - Core/SRT_Core_01_Axioms.md
  - Governance/SRT_CLAIM_LADDER.md
  - Core/SRT_OPEN_TENSIONS.md
  - Philosophy/SRT_L0_Ontological_Status.md
  - _SRT_SYMBOL_TABLE.md
machine_summary: >
  Revised strategy for an SRT bridge paper in philosophy of mathematics. The paper
  argues that major mathematical innovations can be practice-constitutive without
  being truth-constitutive: they can re-individuate mathematical problems and alter
  the update regime through which later mathematics proceeds. The main case is
  forcing. The proposition CH predates Cohen, but forcing changed the background
  theories, admissible methods, model-relative questions, and standards of resolution
  under which CH and related problems are pursued. The paper distinguishes result
  innovation from landscape innovation by whether an innovation materially changes
  the future update regime or the individuation of a nontrivial family of problems.
  Noncommutativity is a strong diagnostic signature, not the definition. Formal
  constraints are supplied by independence, model theory, interpretability, relative
  consistency, and the observed near-prewellordering of consistency strengths among
  many natural theories. The SRT mapping to L1-to-L2 writeback, scaffolding,
  hysteresis, and semantic gravity is explicitly P3. Kappa0, curvature, Psi_f, and
  Gödel-style openness remain interpretive extensions rather than premises.
---

# 数学可达结构与问题个体化  
## 新版论文写作大纲与策略 v0.2

> **文件性质**：内部论文策略文件，不是投稿正文。  
> **主张硬度**：SRT 到数学哲学的整体映射为 **P3 bridge**。  
> **关键修订**：相较 v0.1，本版不再只主张“数学实践的可达性具有历史路径依赖”，而将承重点提升到两个构成性层面：  
> 1. 数学创新可以重新个体化一个研究问题；  
> 2. 数学创新可以改变后续数学活动的更新制度。  
> 这两项都比“知识增加”更强，但仍不直接主张数学真值由历史创造。

---

# 0. 一句话裁剪标准

\[
\boxed{
\text{本文不是论证数学真理随历史改变，而是论证重大数学创新会改变后来什么算同一个问题，以及数学可以怎样继续更新。}
}
\]

凡不能服务于这一命题的内容，删除或移至后续论文。

---

# 1. 论文的核心定位

## 1.1 首选题目

**When Mathematical Problems Change: Forcing, Reachability, and the Historical Constitution of Mathematical Practice**

中文：

**当数学问题发生改变：Forcing、可达结构与数学实践的历史构成**

## 1.2 备选题目

**Forcing and the Re-Individuation of Mathematical Problems**

中文：

**Forcing 与数学问题的重新个体化**

或：

**Result Innovation and Landscape Innovation in Mathematics**

中文：

**数学中的结果型创新与景观型创新**

## 1.3 暂不使用的题目

- *Mathematics Deforms Its Own Possibility Space*
- *Selection, Curvature, and Mathematical Necessity*
- *Mathematical Accessibility as an SRT Ontology*

原因：

- “可能性空间”容易被理解为数学真值或全部模态事实随历史变化；
- “曲率”在当前 SRT 仓库中承担多个尚未完全统一的角色；
- 第一篇论文应首先证明实践—结构构成性，而不是直接承担高承诺数学本体论。

---

# 2. 目标问题

传统讨论常在以下两端之间摆动：

\[
\text{数学是对先在结构的发现}
\quad\text{vs.}\quad
\text{数学是历史实践中的构造}
\]

如果文章只说“数学方法和研究路径有历史”，固定背景柏拉图主义完全可以接受：

> 数学对象和真理没有变化，变化的只是我们的知识和方法。

因此，本文必须提出一个固定背景发现论不能仅靠让步就完全吸收的问题：

> **数学历史是否能够改变一个研究问题由什么背景、方法、答案空间和解决标准所个体化，并改变后来数学活动可以使用的更新制度？**

这里的“改变问题”不表示原有命题字符串消失，也不表示数学真值由共同体投票生成。它表示：

> 同一个命题表达式可以在不同历史阶段构成不同的研究问题，因为其默认背景理论、允许方法、相关模型、辅助公理和解决标准已经改变。

---

# 3. 中心论题

## 3.1 不可让步的中心主张

> **重大数学创新不仅增加新结果，还可能重新个体化一类数学问题，并改变后续数学实践可使用的更新制度。**

这一主张包含两层。

### A. 问题个体化的历史内生性

数学问题不是仅由一个命题字符串 \(\varphi\) 个体化。

定义一个时刻 \(t\) 的研究问题：

\[
q_t=
\langle
\varphi,\,
B_t,\,
A_t,\,
M_t,\,
\Sigma_t
\rangle
\]

其中：

- \(\varphi\)：命题内容或问题核；
- \(B_t\)：默认背景理论；
- \(A_t\)：允许或正在竞争的辅助公理、扩展原则与模型假设；
- \(M_t\)：允许的证明、构造和模型方法；
- \(\Sigma_t\)：何种结果被视为充分解决、部分解决或问题重述的标准。

即使：

\[
\varphi_t=\varphi_{t+1}
\]

也可能出现：

\[
q_t\neq q_{t+1}
\]

因为：

\[
(B_t,A_t,M_t,\Sigma_t)
\neq
(B_{t+1},A_{t+1},M_{t+1},\Sigma_{t+1})
\]

本文将这种变化称为：

> **问题的重新个体化**（re-individuation of a mathematical problem）。

### B. 更新制度的历史内生性

定义数学实践状态：

\[
\mathfrak S_t=
\big(
\mathcal P_t,\,
\mathfrak U_t,\,
\mathcal I_t
\big)
\]

其中：

- \(\mathcal P_t\)：理论、模型、概念、证明和问题构成的可达景观；
- \(\mathfrak U_t\)：时刻 \(t\) 可用、可复用和可传承的数学更新制度；
- \(\mathcal I_t\)：问题个体化函数或问题族的个体化结构。

\(\mathfrak U_t\)包括：

- 可接受的证明转换；
- 模型构造操作；
- 理论扩展方式；
- 翻译、解释和归约操作；
- 可复用的方法脚手架；
- 哪些操作能够被教学、形式化和继承。

一次重要创新 \(h_t\) 可以诱导：

\[
F_{h_t}:
\mathfrak S_t
\longrightarrow
\mathfrak S_{t+1}
\]

若它不仅增加内容，还导致：

\[
\Delta\mathfrak U_t\neq0
\]

或者使一个非平凡问题族发生：

\[
\Delta\mathcal I_t\neq0
\]

则该创新具有景观构成作用。

---

# 4. 实践—结构构成性，而非真值构成性

## 4.1 真值构成性

一项历史事件 \(h_t\) 若决定命题 \(\varphi\) 为何为真，则它具有 truth-constitutive 作用。

第一篇论文不主张：

\[
h_t
\text{ 是 }
\varphi
\text{ 的 truthmaker}
\]

也不主张共同体活动可以改变给定模型中的满足关系。

## 4.2 实践—结构构成性

定义：

\[
h_t
\text{ is practice-constitutive}
\]

当且仅当它在一个非平凡数学领域中实质改变：

- 问题的个体化；
- 可实施的更新操作；
- 允许的转换；
- 解决标准；
- 后续方法的默认背景。

紧凑写法：

\[
h_t\text{ is practice-constitutive}
\iff
\Delta\mathfrak U_t\neq0
\;\lor\;
\Delta\mathcal I_t\neq0
\]

并要求变化不是单个研究者的偶然心理变化，而能够：

- 被公开重构；
- 被后续研究继承；
- 形成稳定方法或问题结构；
- 受到形式结果的约束。

第一篇论文要证明的是实践—结构构成性。

更强的数学本体构成论留待后续。

---

# 5. 结果型创新与景观型创新

## 5.1 结果型创新

结果型创新主要改变当前数学内容：

\[
\Delta\mathcal P_t\neq0
\]

但不显著改变相关领域的更新制度与问题个体化：

\[
\Delta\mathfrak U_t\approx0,
\qquad
\Delta\mathcal I_t\approx0
\]

典型表现：

- 在成熟方法下证明一个已明确提出的定理；
- 增加一个可引用的结果节点；
- 改善某条路径的局部成本，但没有产生新的可复用操作类型。

“结果型”不等于“不重要”。有些结果极其重要，但仍不构成新的更新制度。

## 5.2 景观型创新

景观型创新的结构判据是：

\[
\boxed{
\Delta\mathfrak U_t\neq0
\quad\text{或}\quad
\Delta\mathcal I_t\neq0
}
\]

它改变：

- 后来数学家可以做哪些类型的操作；
- 一类问题如何被提出和区分；
- 什么模型或扩展成为相关；
- 什么算作解决；
- 后续结果通过哪些方法成为可达。

## 5.3 非交换性：强签名，不是定义

如果创新 \(a\) 改变了后续创新 \(b\) 会做什么，可能出现：

\[
F_b(F_a(\mathfrak S))
\neq
F_a(F_b(\mathfrak S))
\]

或者其中一个组合在原状态下无定义：

\[
F_b(\mathfrak S)
\text{ undefined, but }
F_b(F_a(\mathfrak S))
\text{ defined}
\]

这表明 \(a\) 具有强路径构成作用。

但不可交换性不是景观创新的充分必要定义：

- 普通引理依赖也可能产生顺序不对称；
- 两个重大方法创新最终可能在粗粒度上可交换；
- 有时关键变化是操作定义域被创建，而不是两个操作简单不相等。

因此：

> **不可交换性是景观型创新的一项强诊断签名，而非唯一判据。**

## 5.4 最低判定要求

一项创新只有同时满足以下至少三项，才可在正文中称为景观型创新：

1. 产生新的可复用操作类型或改变既有操作的适用域；
2. 重新个体化一个非平凡问题族；
3. 改变后续研究的解决标准；
4. 形成可继承的方法脚手架；
5. 对大量后续结果的证明形态或模型组织方式产生结构影响；
6. 其影响不能被完全描述为“新增一个可引用定理”。

这里的“大量”不能单独作为判据，只能作为结构变化的经验辅助证据。

---

# 6. 数学可达结构

## 6.1 术语统一

全文主术语统一为：

- **reachability**：可达性／可达结构；
- **reachability landscape**：可达景观；
- **update regime**：更新制度；
- **problem individuation**：问题个体化。

“accessibility relation”保留给模态逻辑和潜在主义的技术语境。

论文必须明确：

> Reachability here concerns historically available transitions among problems, methods, theories, and models. It is not identical to the possible-world accessibility relation of modal logic, although the two may later be formally related.

## 6.2 可达景观

定义：

\[
\mathcal P_t=
(\mathcal T_t,\mathcal R_t,c_t)
\]

其中：

- \(\mathcal T_t\)：可明确表达、使用和继承的理论、模型、概念、问题与工具；
- \(\mathcal R_t\)：扩展、解释、翻译、归约、模型构造、证明依赖和方法迁移关系；
- \(c_t\)：进入、构造、证明、理解、迁移与修订的多维成本。

## 6.3 多维成本，不设统一标量

候选成本剖面：

\[
c_t(p)=
\big(
c_{\mathrm{formal}},
c_{\mathrm{constructive}},
c_{\mathrm{proof}},
c_{\mathrm{translation}},
c_{\mathrm{inheritance}}
\big)
\]

其中：

- \(c_{\mathrm{formal}}\)：一致性、解释性、证明论强度与模型条件负担；
- \(c_{\mathrm{constructive}}\)：构造模型或对象的技术负担；
- \(c_{\mathrm{proof}}\)：证明搜索、长度或复杂度负担；
- \(c_{\mathrm{translation}}\)：跨框架翻译负担；
- \(c_{\mathrm{inheritance}}\)：改写证明库、教材、术语和问题结构的负担。

第一篇只要求局部比较、偏序或方向变化，不主张这些成本全局可通约。

---

# 7. 主案例：forcing 与 CH 问题的重新个体化

## 7.1 核心纪律

不能写：

> Cohen 之前 CH 问题不存在。

CH 的命题内容和研究问题早已存在。

应写：

> **forcing 与独立性结果没有创造 CH 的句法核心，但重新个体化了 CH 作为研究问题的背景理论、相关模型、允许方法、辅助公理和解决标准。**

## 7.2 forcing 前后的问题结构

以：

\[
q_t^{CH}=
\langle
\mathrm{CH},
B_t,
A_t,
M_t,
\Sigma_t
\rangle
\]

表示 CH 问题。

forcing 与独立性结果前，主导问题形态可粗略表述为：

> 在标准集合论基础中证明或反驳 CH。

独立性结果之后，问题结构分化为：

- CH相对于哪些背景理论可决定？
- 哪些模型满足 CH 或 \(\neg\mathrm{CH}\)？
- 哪些新公理能够决定 CH 或相关连续统问题？
- 新公理的相对一致性强度和解释力如何？
- CH应在单一宇宙观还是多宇宙观下理解？
- 某种“解决”需要真值裁决、独立性说明、公理选择，还是模型生态解释？

这里：

\[
\varphi=\mathrm{CH}
\]

可以保持不变，但：

\[
(B,A,M,\Sigma)
\]

发生结构变化。

## 7.3 forcing 作为更新制度创新

forcing的哲学承重点不是它仅产生了一个结果，而是它成为一种可复用的模型扩展与独立性研究操作。

要论证：

\[
\Delta\mathfrak U_t\neq0
\]

必须显示 forcing：

- 建立新的系统模型构造方式；
- 改变独立性问题的标准研究流程；
- 使一类此前不能系统组织的问题进入共同方法；
- 改变后续公理比较与模型研究的操作背景；
- 形成可被传授、复用、变体化和形式化的方法脚手架。

## 7.4 forcing 案例的技术准确性清单

论文必须选择一种主要技术叙述路线，并保持元理论条件一致。

必须明确区分：

1. **句法独立性**
   \[
   \mathrm{ZFC}\nvdash\mathrm{CH},
   \qquad
   \mathrm{ZFC}\nvdash\neg\mathrm{CH}
   \]

2. **相对一致性**
   对相应理论一致性的条件性表述，不把相对一致性误写成无条件存在性。

3. **模型真值**
   CH 或 \(\neg\mathrm{CH}\) 在特定模型／扩展中的满足关系。

4. **技术呈现路径**
   可数传递模型、generic extension、Boolean-valued models 等表达方式不得无提示混用。

5. **元理论假设**
   不从单纯 \(\operatorname{Con}(\mathrm{ZFC})\) 无条件推出可数传递模型存在。

6. **ground model 与 extension**
   明确对象层和元层，避免把外部构造语言与内部真值混为一谈。

7. **Gödel 与 Cohen 的分工**
   分清相容性／不可证明性结果的历史和技术作用。

## 7.5 对宇宙观／多宇宙观的立场

第一篇采取：

> **本体论中立、解释性比较。**

文章不裁决：

- 是否存在唯一预期集合论宇宙；
- 多个模型是否具有同等本体地位。

而是主张：

- 宇宙观和多宇宙观都必须解释 forcing 之后问题个体化与更新制度的变化；
- 二者对“景观”的本体解释不同；
- 论文的实践—结构构成性不依赖先选定其中一方。

若文章最终不得不依赖多宇宙观才能成立，则必须在主张—撤回表中升级承诺并重新评估投稿定位。

---

# 8. 形式约束：为什么景观不是共同体自由建构

## 8.1 固定协议内后承只是背景

以下命题保留为背景：

\[
\text{选择协议}
\neq
\text{选择协议后果}
\]

但它不再承担原创性。

## 8.2 正面形式约束

景观更新受到以下结构限制：

- 独立性；
- 模型存在与满足；
- 相对一致性；
- 可解释性；
- 保守扩展；
- 证明论强度；
- 一致性强度；
- 翻译与归约是否成立。

共同体能够选择关注和评价标准，却不能自由重置这些关系。

## 8.3 自然理论的一致性强度结构

正文应加入一个正面论证：

> 在大量自然发生的形式理论中，一致性强度呈现近似预良序或高度有序的经验现象；这一结构并非由共同体投票任意设定，因此可作为跨理论景观具有非社会形式约束的一项证据。

必须同时保留限制：

- 对一般任意理论，一致性强度不必线性或良基；
- “自然理论”的范围尚无无争议精确定义；
- 近似预良序是需要解释的现象，不是本文可直接当作完整定理的结论；
- 一致性强度只是：
  \[
  c_{\mathrm{formal}}
  \]
  的一个候选坐标，不是完整成本函数。

## 8.4 不使用单轴公理价格表

不得把：

- \(V=L\)；
- 大基数；
- forcing axioms；
- 内模型纲领；
- 多宇宙方法；

压缩为一条简单的“便宜—昂贵”直线。

应展示：

> 数学景观可以在某些形式维度高度有序，在其他解释、自然性和实践维度保持多轴、局部与有争议。

---

# 9. SRT 的必要增量

## 9.1 SRT 不能只提供“路径依赖＋迟滞”

若 SRT 部分只说数学具有：

- 历史；
- 路径依赖；
- 迟滞；
- 社会沉积；

则会被实践哲学、STS 或制度理论吸收。

SRT 必须提供一个更明确的二阶写回解释：

> 一次数学显现只有在改变后续选择和更新条件时，才从一个 \(L_1^{math}\) 结果成为 \(L_2^{math}\) 级脚手架。

形式桥接：

\[
L_1^{math}
\longrightarrow
L_2^{math}
\]

不只是：

\[
\text{结果进入知识库}
\]

而是：

\[
\Delta\mathfrak U_t\neq0
\quad\text{或}\quad
\Delta\mathcal I_t\neq0
\]

## 9.2 最小 SRT 映射

### \(L_0^{math}\)

相对于当前数学实践，尚未稳定显现但具有非均匀可表达性、可构造性和可达性的候选结构与路径。

禁止读作：

- 完整数学对象仓库；
- 层拓扑斯本身；
- 预存的柏拉图世界。

### \(L_1^{math}\)

一次明确完成的：

- 定理；
- 证明；
- 模型；
- 反例；
- 独立性结果；
- 新方法事件。

### \(L_2^{math}\)

已经背景化并能约束后续数学活动的：

- 标准方法；
- 问题分类；
- 证明库；
- 基础框架；
- 教材和术语；
- 更新制度；
- 解决标准。

## 9.3 L₂ 级别判据

一个数学结果或方法达到 \(L_2^{math}\) 级别，不是因为它被多数人知道，而是因为它满足：

1. 可继承；
2. 可复用；
3. 可背景化；
4. 对后续问题个体化或更新制度产生稳定约束。

可写成：

\[
L_2^{math}\text{-grade}
\Rightarrow
\Delta\mathfrak U_t\neq0
\;\lor\;
\Delta\mathcal I_t\neq0
\]

这是 P3 桥接，不是 SRT Core 中已经证明的数学定理。

## 9.4 语义引力的有限使用

Ax-L2-08 可被桥接为：

> 一种方法一旦沉积为训练、教材、工具和证明库，兼容后续路径通常会获得局部成本优势。

候选预测：

\[
c_{t+1}^{compatible}(p)
<
c_t^{compatible}(p)
\]

但必须限制：

- 这是局部方向偏置，不是唯一全局吸引子；
- 不预测所有集合论都单向走向更多 forcing；
- 不宣称 V=L 或竞争纲领被历史淘汰；
- 局部成本下降可以与竞争研究纲领并存。

## 9.5 \(\kappa_0\) 的位置

\(\kappa_0>0\)只在结尾作为 P3 解释性候选：

> 若任何有限数学沉积都无法穷尽未来合法更新，则可把这种不可约开放性视为 SRT 原初非平坦性的数学实践投影。

不得写成：

- SRT 推出哥德尔不完备性；
- forcing 观测到 \(\kappa_0\)；
- 一致性强度就是曲率；
- 数学开放性已由 \(\kappa_0\)证明。

## 9.6 \(\Psi_f\) 的位置

\(\Psi_f\)只进入展望：

> 多维成本 \(c_t\) 可能构成 \(\Psi_f\) 的领域投影族。

不把不同成本强行统一为一个数值。

---

# 10. 完整论文大纲

目标长度：英文约 9,000—10,500 词。

## 1. Introduction: When Does a Mathematical Problem Change?  
约 1,000—1,200 词

任务：

- 从 CH 在 forcing 前后的问题形态切入；
- 明确命题表达式不变不等于研究问题个体化不变；
- 提出实践—结构构成性；
- 区分结果型与景观型创新；
- 说明文章不主张历史改变给定模型中的数学真值；
- 列出三项贡献。

引言中心句：

> Mathematical history can be constitutive without being truth-constitutive: a major innovation may leave the proposition under discussion unchanged while altering what counts as the problem, which transformations are available, and what would count as a resolution.

## 2. Existing Accounts and the Missing Constitutive Level  
约 1,300—1,500 词

讨论：

1. 柏拉图主义；
2. 结构主义；
3. 形式主义／Carnap 式框架论；
4. 潜在主义；
5. 数学实践哲学。

建立解释缺口：

> 现有理论可以承认知识、语言和方法变化，但仍需解释数学内部事件如何重新个体化问题并改变后续更新制度。

纪律：

- 不说实践哲学只研究社会史；
- 不说潜在主义一律固定可及关系；
- 不说柏拉图主义否认数学史；
- 不说 Carnap 允许框架内后果任意变化。

## 3. Problem Individuation and Practice-Constitutive Change  
约 1,400—1,600 词

建立：

\[
q_t=
\langle
\varphi,B_t,A_t,M_t,\Sigma_t
\rangle
\]

重点：

- 命题、问题和研究计划的区别；
- 何谓问题重新个体化；
- 何谓实践—结构构成性；
- 为什么这强于“知识增加”，又弱于真值构成论；
- 问题身份变化的边界：不能仅因措辞或个人关注变化就算重新个体化。

## 4. Result Innovation and Landscape Innovation  
约 1,300—1,500 词

建立：

\[
\mathfrak S_t=
(\mathcal P_t,\mathfrak U_t,\mathcal I_t)
\]

以及：

\[
F_h:\mathfrak S_t\to\mathfrak S_{t+1}
\]

核心内容：

- 结果型创新；
- 景观型创新；
- \(\Delta\mathfrak U\)和\(\Delta\mathcal I\)判据；
- 不可交换性作为强签名；
- 多维成本与可达关系；
- 防止“任何新定理都改变一点成本”导致区分坍塌。

## 5. Forcing as a Practice-Constitutive Innovation  
约 2,200—2,500 词

结构：

1. CH问题的历史背景；
2. Gödel与Cohen结果；
3. forcing 的必要技术说明；
4. CH问题的重新个体化；
5. forcing 对更新制度的改变；
6. 模型、扩展与新公理问题；
7. 宇宙观／多宇宙观中立比较；
8. 为什么 forcing 不只是增加一个可引用结果。

本节必须是全文最扎实部分。

## 6. Formal Constraint Across Theories  
约 1,000—1,200 词

内容：

- 独立性与模型约束；
- 相对一致性；
- 可解释性和证明论比较；
- 自然理论的一致性强度近似预良序现象；
- 为什么数学景观不是共同体任意设计；
- 为什么形式约束又不能被压缩为单轴成本。

## 7. The SRT Bridge: From Result to Scaffold  
约 1,100—1,300 词

内容：

- \(L_1^{math}\to L_2^{math}\)；
- 二阶写回；
- 问题个体化和更新制度作为数学 \(L_2\) 的承重内容；
- 迟滞与背景化；
- 语义引力的局部预测；
- 明确 P3；
- \(\kappa_0\)、曲率和 \(\Psi_f\) 后置。

## 8. Objections and Failure Conditions  
约 1,400—1,700 词

### Objection 1：固定背景柏拉图主义可以接受全部历史变化

回答：

- 区分真值构成与实践—结构构成；
- 迫使对方承认问题身份和更新制度不是纯外部注释；
- 若柏拉图主义能完整解释这种构成作用，本文不必宣称其被推翻，只主张其解释范围需要扩展。

### Objection 2：这只是 Lakatos 或数学实践哲学

回答：

- 承认历史问题和概念变化已有传统；
- 本文新增问题个体化结构、更新制度和景观创新判据；
- 用 forcing 同时联结形式约束与历史构成。

### Objection 3：任何新定理都会改变后续路径，区分仍是程度差异

回答：

- 景观型创新要求 \(\Delta\mathfrak U\) 或 \(\Delta\mathcal I\)；
- 局部引用成本下降不足以满足；
- 不可交换性只是辅助签名。

### Objection 4：问题没有改变，只是我们发现原来公理不足

回答：

- 承认命题核保持；
- 论证背景理论、允许方法、答案空间和解决标准构成研究问题身份；
- 若这些不属于问题身份，反对者需提供更充分的问题个体化理论。

### Objection 5：更新制度只是社会规范

回答：

- forcing 的方法可用性受到严格模型和一致性条件约束；
- 社会采纳影响传播，但不能自由制造有效模型构造。

### Objection 6：宇宙观和多宇宙观会给出不同结论

回答：

- 第一篇保持本体论中立；
- 两者均需解释实践结构变化；
- 强模态本体论不作为文章成立条件。

### Objection 7：SRT只是后加标签

回答：

- SRT 必须提供二阶写回、L₂背景化和局部语义引力预测；
- 若这些没有解释增量，SRT 节按撤回条件缩减。

## 9. Implications: Openness Without Truth Relativism  
约 500—700 词

讨论：

- 问题可历史构成，不等于真值相对主义；
- 不完备性可作为有限形式闭合无法穷尽更新空间的解释性实例；
- \(\kappa_0\)只作为后续本体论方向；
- 动态模态结构与严格几何留待后续论文。

## 10. Conclusion  
约 350—450 词

只保留：

1. 问题个体化可历史改变；
2. 景观型创新改变更新制度；
3. forcing 是实践—结构构成性案例；
4. 这种构成受形式约束，不等于社会任意主义或真值构成论。

---

# 11. 写作顺序

## 第一步：建立 forcing 技术—历史档案

在写任何 SRT 段落前，完成：

- Gödel与Cohen结果的准确分工；
- forcing 主要技术叙述路线；
- 元理论假设；
- ground model／extension／Boolean-valued 表述边界；
- forcing 前后问题结构和研究方法的可靠历史材料；
- 宇宙观与多宇宙观文献矩阵。

止损条件：

> 若无法证明 forcing 改变了更新制度或问题个体化，而只能证明它增加了知识，则收缩论文。

## 第二步：建立问题个体化案例表

对 CH 填写：

| 维度 | forcing 前 | forcing 后 | 证据 |
|---|---|---|---|
| 命题核 \(\varphi\) |  |  |  |
| 背景理论 \(B\) |  |  |  |
| 辅助公理／模型 \(A\) |  |  |  |
| 方法 \(M\) |  |  |  |
| 解决标准 \(\Sigma\) |  |  |  |

只有在表格有实质内容后，才写“重新个体化”。

## 第三步：建立更新制度变化表

| forcing 前可用操作 | forcing 后新增／改变操作 | 是否可复用 | 是否改变后续问题 |
|---|---|---|---|

必须区分：

- 单次证明技巧；
- 可复用方法；
- 领域更新制度。

## 第四步：写第三、四、五节

先写：

1. 问题个体化；
2. 结果型／景观型区分；
3. forcing案例。

不要先写引言和 SRT。

## 第五步：写最强反对意见

首先尝试用以下立场吸收论文：

- 固定背景柏拉图主义；
- Lakatos式实践哲学；
- 社会建构论；
- 集合论多宇宙观。

若它们可以原样接受且无需增加解释承诺，则中心主张仍需加强。

## 第六步：最后写 SRT 桥接

SRT 节必须回答：

> 除了给动态景观换名，SRT 多解释了什么？

最低答案：

- \(L_1\)事件何时成为 \(L_2\)脚手架；
- 为什么背景化会改变后续更新制度；
- 为什么兼容路径获得局部成本优势；
- 为什么这不等于全局单向决定论。

## 第七步：最后写摘要和题目

摘要不得：

- 声称已排除所有固定背景实在论；
- 声称数学真理随历史改变；
- 声称 forcing 证明 SRT；
- 声称一致性强度是数学曲率。

---

# 12. 主张—证据—撤回条件

| 主张 | 层级 | 所需证据 | 撤回／缩减条件 |
|---|---|---|---|
| 数学问题可被历史重新个体化 | 论文核心 | CH问题的 \(B,A,M,\Sigma\) 变化 | 若只能证明知识增加，删除“个体化” |
| 景观型创新改变更新制度 | 论文核心 | forcing 形成可复用操作制度 | 若只增加结果节点，降为结果型创新 |
| 不可交换性是强签名 | 辅助主张 | 明确后续更新依赖 | 若普通引理依赖无法区分，限制适用范围 |
| 数学历史具有实践—结构构成性 | 论文核心 | \(\Delta\mathfrak U\)或\(\Delta\mathcal I\) | 若变化完全是个人心理／社会关注，主张失败 |
| 景观更新受非社会形式约束 | 论文核心 | 独立性、模型、相对一致性、解释关系 | 若所谓约束可由共同体自由重置，反任意性失败 |
| 自然理论的一致性强度呈高度有序现象 | 正面证据 | 逻辑文献与范围限定 | 若“自然理论”范围无法合理控制，降为开放现象 |
| 论文对宇宙观／多宇宙观保持中立 | 方法承诺 | 两种解释均可容纳主论证 | 若论证实质依赖一方，必须公开站位 |
| SRT 提供二阶写回解释 | P3 | \(L_1\to L_2\)、脚手架、语义引力映射 | 若无额外解释后果，缩减 SRT 节 |
| 语义引力产生局部方向偏置 | P3候选 | 方法沉积后兼容路径成本下降 | 若历史材料不支持，删除预测 |
| \(\kappa_0\)解释不可约开放性 | P3/P4展望 | 后续严格桥接 | 第一篇不成立不影响主论证 |
| \(\Psi_f\)统一多维成本 | P3/P4展望 | 通约性与操作化 | 未证明前不得进入主定义 |

---

# 13. 新颖性压力测试

## 13.1 固定背景发现论测试

对手是否可以说：

> 一切变化都只是我们对固定数学世界的知识变化。

论文必须迫使其进一步回答：

- 什么构成同一个数学研究问题？
- 为什么背景理论、方法和解决标准不属于问题身份？
- 数学内部创新如何成为后续实践的组成条件？

若对手无需回答这些问题就能吸收全文，论文仍过弱。

## 13.2 Lakatos 吸收测试

若 Lakatos式框架已能完整处理：

- 问题重新个体化；
- 更新制度；
- 形式约束；
- forcing 的模型操作结构；

则本文必须明确增量只是形式统一，而不能宣称新的哲学位置。

目标是显示：

> 本文把问题身份、方法制度和非社会形式约束放入同一个更新结构。

## 13.3 “任何结果都改变景观”测试

对任一普通定理问：

- 是否改变操作类型？
- 是否改变问题族个体化？
- 是否改变解决标准？
- 是否形成可继承脚手架？

只有局部引用便利变化，不足以构成景观型创新。

## 13.4 社会建构论测试

若社会偏好可以解释所有成本与方向变化，则形式约束部分失败。

## 13.5 SRT删除测试

删除 SRT 后，数学哲学论文应仍成立。

但重新加入 SRT 后，必须新增：

- 结果到脚手架的分层；
- 二阶写回；
- 局部方向偏置；
- 不可约开放性的后续解释。

若没有新增，SRT 节应缩减为简短应用说明。

## 13.6 隐喻测试

“景观”“更新制度”“问题个体化”都必须对应：

- 明确对象；
- 可引用历史变化；
- 可反驳的边界；
- 至少局部的结构判据。

---

# 14. 禁止裸用清单

第一篇禁止未经独立论证直接使用：

- \(\mathcal P_t=L_0\)；
- \(c_t=\kappa(t)\)；
- 一致性强度 \(=\Psi_f\)；
- 一致性强度 \(=\) 完整数学成本；
- \(H(L_0)+H(L_2)=\mathrm{const}\) 作为数学史定律；
- \(\dot\kappa\ge0\)；
- 耦合方程推出“数学没有终局基础”；
- \(\kappa_0>0\)推出哥德尔不完备性；
- forcing 是 \(\kappa\) 的直接观测；
- \(L_0\) 等同层拓扑斯；
- 数学真理是 \(\hat G\) 的源代码；
- Cohen之前 CH 问题不存在；
- 所有景观型创新都与其他更新不可交换；
- forcing 之后所有集合论都沿同一低成本方向发展。

---

# 15. 文献策略

至少建立七个文献组：

1. CH、Gödel与Cohen的技术和历史；
2. forcing 方法史及其后续发展；
3. 集合论宇宙观／多宇宙观和新公理哲学；
4. 数学问题个体化、问题史与研究计划；
5. Lakatos、Kitcher、Maddy、Ferreirós及数学实践哲学；
6. 潜在主义与模态可及关系；
7. 一致性强度、自然理论、可解释性与证明论层级。

引用纪律：

- 技术事实使用原始论文、标准专著或权威数学来源；
- 历史构成性必须有数学史证据；
- 不能用 SRT 仓库文件证明集合论事实；
- 对相邻立场使用代表作者原文，避免稻草人；
- 对“自然理论近似预良序”同时引用支持与限制性讨论。

---

# 16. 工作摘要骨架 v0.2

> Mathematical history can be constitutive without being truth-constitutive. This paper argues that major mathematical innovations may alter not merely what mathematicians know, but how mathematical problems are individuated and which forms of mathematical updating are subsequently available. A problem is treated as more than a proposition: it is individuated by a background theory, admissible auxiliary principles, available methods, and standards of resolution. The development of forcing is the central case. The proposition expressing the continuum hypothesis predates Cohen, but forcing and the resulting independence results transformed the models, methods, axiomatic options, and resolution standards through which the problem is pursued. I distinguish result innovation, which primarily adds content within an existing update regime, from landscape innovation, which materially changes that regime or re-individuates a nontrivial family of problems. Independence, model-theoretic constraints, interpretability, relative consistency, and the highly ordered consistency-strength structure observed among many natural theories show that such historical change is not freely constructed by mathematical communities. A final section develops an explicitly P3 bridge to Selective Reality Theory: mathematical results become L2-grade scaffolds when they modify the conditions of later selection, while semantic gravity predicts a local cost advantage for paths compatible with sedimented methods. Stronger claims about curvature, irreducible modal openness, and mathematical truth are left open.

该摘要为工作骨架，完成案例和文献矩阵后重写。

---

# 17. 投稿前完成标准

- [ ] CH的命题核与问题个体化被明确区分；
- [ ] 不使用“Cohen之前问题不存在”的表述；
- [ ] forcing技术叙述的元理论条件一致；
- [ ] 不混淆句法独立性、相对一致性和模型真值；
- [ ] 已决定并声明宇宙观／多宇宙观中立策略；
- [ ] 景观型创新以 \(\Delta\mathfrak U\) 或 \(\Delta\mathcal I\) 为结构判据；
- [ ] 不可交换性仅作为强签名；
- [ ] 普通结果型定理与 forcing 有清晰对照；
- [ ] 一致性强度被用作正面形式约束证据，同时保留自然理论限制；
- [ ] reachability 与 modal accessibility 明确区分；
- [ ] 实践—结构构成性被正面定义；
- [ ] SRT 节提供二阶写回而非术语贴附；
- [ ] 语义引力只给局部偏置，不给全局单向历史；
- [ ] \(\kappa_0\)、曲率、\(\Psi_f\)没有进入主论证；
- [ ] 摘要不声称已排除所有固定背景柏拉图主义；
- [ ] 删除 SRT 后论文仍有独立贡献，加入 SRT 后又有明确解释增量；
- [ ] 至少一条最强反对意见导致正文结构性修改。

---

# 18. 后续论文路线

## A. 问题身份的形式理论

进一步研究：

\[
q=
\langle
\varphi,B,A,M,\Sigma
\rangle
\]

各分量变化到何种程度仍是同一个问题，何时构成新问题。

## B. 动态更新制度

形式化：

\[
\mathfrak U_t\to\mathfrak U_{t+1}
\]

并研究操作定义域、新方法生成和不可交换更新。

## C. SRT 数学语义引力的经验研究

利用：

- 教材网络；
- 证明依赖图；
- 数学文献引用；
- 形式化数学库；

测试方法沉积是否降低兼容路径成本。

## D. 一致性强度与数学景观几何

研究一致性、解释性和证明论关系能否支持：

- 局部序结构；
- 多维势垒；
- 非对称路径；
- 后续严格曲率模型。

## E. 不可约开放性

在严格限定哥德尔定理适用条件后，讨论：

> 有限形式闭合无法穷尽未来合法更新，是否可以作为 \(\kappa_0>0\) 的 P3 数学实践投影。

---

# 19. 最终执行指令

论文始终维护三个边界：

\[
\boxed{
\begin{aligned}
&\text{命题核不变，不等于研究问题个体化不变；}\\
&\text{历史构成实践结构，不等于历史创造数学真值；}\\
&\text{形式约束限制景观更新，不等于存在单一固定更新方向。}
\end{aligned}
}
\]

这三条共同构成新版策略的中心。
