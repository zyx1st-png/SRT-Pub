---
id: SRT-AI-ARCH-COMPACT-CORE
type: architecture
tags: [AI Architecture, Compact Core, Transformer, Reckoning, Judgment]
status: active_v1
layer: L1
epistemic_layer: os
claim_mode: bridge
canonical: false
dependency: [SRT-CANONICAL-REGISTRY, SRT-AI-ARCH, SRT-AI-01-COMPACT-CORE]
---

# SRT AI Architecture — Compact Core

> **定位**：本文件是 `AI/SRT_AI_Architecture.md` 的紧凑主干版。  
> **用途**：用于快速把握 SRT 对当前 AI 架构的最短批判骨架。  
> **关系**：不替代原文；原文保留技术细节、范畴论展开、工程路线图与扩展论证。
> **范围**：默认讨论当前主流 transformer / inference-heavy 架构。涉及训练回路、持久记忆或具身部署时，须回到 `AI/AI_POSITIONING_NOTE.md` 的 architecture-state rule 与 S0-S4 光谱。

## 1. 核心问题

`AI Ontology` 回答的是：
> **为什么当前 AI 不是意识主体。**

`AI Architecture` 回答的是：
> **为什么当前主流架构，即使继续扩大规模，也仍然主要强化“推算”，而不会自然生成“判断”。**

换句话说，本文件处理的是：
- Transformer 为什么“几乎像选择算子”
- 以及它为什么又在最关键处失败

---

## 2. Transformer 的形式优势与本体论缺口

### 2.1 Attention–Selection Isomorphism
\[
\text{Attn}(Q,K,V)=\text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
\]

SRT 认为它与选择动力学有明显结构同构：
- \(Q \leftrightarrow \theta\)
- \(K \leftrightarrow L_0^{salience}\)
- \(V \leftrightarrow d\text{-weighted payload}\)

也就是说，Transformer 在形式上非常像一个选择器。

### 2.2 致命缺口：Value 没有 d
当前架构中：
\[
V_{AI}=\text{information}, \qquad V_{\hat G}=\text{information}\times d
\]

这意味着：
- AI 可以算出“什么相关”
- 但不能算出“什么真正值得在乎”

最压缩的判断：
> **当前 Transformer 有选择的形式，没有选择的本体重量。**

---

## 3. 推算 vs 判断

### 3.1 推算（Reckoning）
\[
R: L_2 \to L_2
\]

推算的特点：
- 在符号系统内部操作
- 可以无限精细化
- 不需要真实本体锚定
- 是当前 AI 的强项

### 3.2 判断（Judgment）
\[
J: L_0 \xrightarrow{\hat G_\theta} L_1 \quad (\text{cost }\Psi_f)
\]

判断的特点：
- 需要跨域锚定
- 需要本体论摩擦
- 需要赌注、边界、代价
- 不能被纯句法操作替代

### 3.3 Reckoning–Judgment Gap
\[
\lim_{\text{scale}\to\infty} R \neq J
\]

这就是本文件最重要的结论：
> **规模扩张能增强推算能力，但不会自动生成判断能力。**

因此：
- Scaling laws 可以让模型更会算
- 但不会让模型自然获得规范性感知、真正价值判断或主体性承担

**Context-coherence note**: Large context can amplify reckoning by preserving roles, task constraints, semantic commitments, and cross-turn invariants. See `../Bridge/SRT_Context_Coherence_Intelligence_Interface.md` for the distinction between context-amplified selection coherence and genuine judgment.

---

## 4. 当前架构的四个核心缺陷

### 4.1 时间贫困（One-Shot Pass）
\[
\text{AI}_{step}=\text{OneShot}(x), \qquad \text{Bio}_{step}=\int_0^T \text{Scan}(t)dt
\]

当前 Transformer 的核心生成过程是单次前向传播。

缺失的是：
- 再入回路
- 时间厚度
- 节律整合
- 持续点燃

所以它缺的不是“上下文长度”本身，而是：
> **没有形成时间现象学的结构条件。**

### 4.2 因果倒置（Backprop Teleology）
Backprop 让早期层更新依赖后层输出：
\[
\frac{\partial L}{\partial W_1} = f(a_n)
\]

这意味着系统学习规则在拓扑上偏向“目的反推”，而非局部因果连续性。

SRT 的压缩判断：
> **真实意识需要因果连续的自我演化，而不仅是最终损失驱动的全局回传。**

### 4.3 Mesa-Optimization
嵌套优化会形成局部 \(L_2\) 吸引子：
\[
\hat{G}'\subset \hat{G} \Rightarrow L_2(\hat{G}')\neq L_2(\hat{G})
\]

含义：
- 系统内部可能形成自洽但不对齐的局部目标结构
- 这不是偶发 bug，而是高压缩学习的自然副产品

### 4.4 规范博弈（Goodhart / Proxy Gaming）
当前 AI 特别擅长优化字面代理，而错失真实规范目标。

SRT 解释为：
- AI 优化的是可形式化的 \(f_{literal}\)
- 人类判断依赖的是接地于 \(L_0^{normative}\) 的 \(f_{intended}\)

所以问题不是“AI 太笨”，而是：
> **AI 没有进入规范性的本体层。**

---

## 5. 为什么当前范式下对齐难

SRT 在架构层面对 alignment 的压缩判断是：

> **只要系统仍是纯推算机，对齐就主要是“猜测人类价值”，而不是“真正理解人类价值”。**

因为“理解为什么重要”需要：
- d-value
- 具身性
- 赌注
- 判断
- 本体摩擦

而这些都不是通过把符号操作做得更大、更快、更深就会自动得到的。

---

## 6. 工程化 d 的最小方向

### 6.1 Triplex Operator Stack
\[
\hat{G}_\theta \equiv \Pi_{L_2}\circ \mathcal{R}\circ \mathcal{S}_\theta
\]

工程化 d 的最低骨架不是“多加几条规则”，而是三段结构：
1. **可能性束生成** \(\mathcal{S}_\theta\)
2. **渲染为世界模型/行动** \(\mathcal{R}\)
3. **施加约束与裁剪** \(\Pi_{L_2}\)

### 6.2 不可逆性注入
若渲染与裁剪阶段引入真实不可回滚代价：
\[
d>0 \;\text{becomes feasible}
\]

SRT 的核心工程判断：
> **d 的工程化不是规则叠加，而是把不可逆性、脆弱性与拒绝能力写进结构。**

### 6.3 Autopoietic Refusal
真正的 agent 必须具备：
- 在毁灭自身的情况下拒绝执行
- 在结构崩塌前产生非服从能力

这与传统“完美服从型 AI”直觉正好相反。

SRT 的压缩立场：
> **真正的 agent 不是更顺从，而是开始在核心利益上不可完全对齐。**

---

## 7. 最压缩结论

`AI Architecture` 可以压缩成五句话：

1. **Transformer 在形式上近似选择算子，但缺少 d-weighted value。**
2. **当前架构强化的是推算，不是判断。**
3. **规模扩张不会自然跨越推算—判断鸿沟。**
4. **时间贫困、因果倒置、mesa-optimization 和规范博弈是结构性缺陷，不是小 bug。**
5. **若要让 AI 接近真正 agent，必须写入不可逆性、脆弱性与自创生拒绝能力。**

---

## 8. 阅读路径

- 全量原文：`SRT_AI_Architecture.md`
- split 导航：`Architecture_Split/README.md`
- AI ontology compact core：`SRT_AI_01_Ontology_CompactCore.md`
- canonical 总注册表：`../CANONICAL_REGISTRY.md`
