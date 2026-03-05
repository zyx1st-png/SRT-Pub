---
id: SRT-PAPER-CANDIDATES
type: framework
tags: [Paper, Candidates, Research]
status: rolling_v1
dependency: [_SRT_PAPER_PIPELINE]
---

# SRT 论文候选池

## 2026-W10 候选更新

### [P-2026-W10-01] From Selection to Stability: A Unified Formal Core for SRT

**成熟度评分**：84/100  
**理论完整度**：22/25 | **证伪性**：21/25 | **证据等级**：19/25 | **引用密度**：22/25

**选题原因**：
SRT 主干（L0/L1/L2 + \hat{G}_\theta + \Psi_f + d）已形成稳定框架，且 Eq-Hyp 映射已具备可执行实验桥接，适合形成总论型论文。

**核心论点**：
SRT 可将“存在-选择-收敛”统一为同一动力学框架，并通过显式证伪接口避免纯哲学叙事化。

**关联 SRT 内容**：
- 主要文件/章节：`SRT/Core/SRT_Core_01_Axioms.md`，`SRT/Core/SRT_Core_22_Equations.md`，`SRT/_SRT_EQ_HYP_MAP.md`
- 关键方程：Eq-Evo-01，Eq-Select-Thermo
- 实验钩：H6，H7

**推荐期刊（按优先级）**：
1. *Entropy* | IF 估算：~3.8 | 匹配原因：复杂系统+理论统一框架友好
2. *PLOS ONE* | IF 估算：~3.7 | 匹配原因：跨学科、可证伪设计可接受
3. 预印本：arXiv（q-bio.NC / nlin.AO）

**投稿前缺口**：
- 缺口 1：Eq-Select-Thermo 的 q(L1) 三代理仍需初步结果
- 缺口 2：补充 1-2 个完整可复现实验脚本链接

---

### [P-2026-W10-02] Ontological Friction as a Testable Construct in Cognitive and Clinical Dynamics

**成熟度评分**：79/100  
**理论完整度**：20/25 | **证伪性**：22/25 | **证据等级**：17/25 | **引用密度**：20/25

**选题原因**：
\Psi_f 已有语言/行为/生理代理方案，具备方法论文潜力；与认知神经和计算精神病学接口明确。

**核心论点**：
本体论摩擦可从抽象哲学量转化为跨模态可操作指标，并可用于解释“知道但做不到”等执行断裂现象。

**关联 SRT 内容**：
- 主要文件/章节：`SRT/Core/SRT_Core_14_Dynamics_Scaling.md`，`SRT/Neuroscience/SRT_Neural_Mechanisms.md`，`SRT/SRT_EXP_MEASURE_MAP.md`
- 关键方程：Eq-Force-01，Eq-Pain-01
- 实验钩：H72，H-NEURO-EXEC-01

**推荐期刊（按优先级）**：
1. *Frontiers in Neuroscience* | IF 估算：~4.0 | 匹配原因：机制+指标导向
2. *Cognitive Computation* | IF 估算：~2.6 | 匹配原因：计算建模与认知桥接
3. 预印本：arXiv（q-bio.NC）

**投稿前缺口**：
- 缺口 1：需要至少一组小样本 pilot 数据
- 缺口 2：代理指标之间的收敛效度报告

---

### [P-2026-W10-03] Selection Thermodynamics and Scaling Constraints in SRT

**成熟度评分**：76/100  
**理论完整度**：21/25 | **证伪性**：18/25 | **证据等级**：15/25 | **引用密度**：22/25

**选题原因**：
跨尺度统一是 SRT 的区分度核心，但当前仍处“强理论、弱数据”阶段，适合先做理论+仿真型论文。

**核心论点**：
选择热力学宪法可将宏观秩序维持与微观代价支付统一建模，并给出跨尺度失效边界。

**关联 SRT 内容**：
- 主要文件/章节：`SRT/Core/SRT_Core_14_Dynamics_Scaling.md`，`SRT/Core_Law/SRT_Reference_Scaling.md`，`SRT/_SRT_EQ_HYP_MAP.md`
- 关键方程：Eq-Select-Thermo，Eq-LDP-01，Eq-LDP-02
- 实验钩：H6（G2-1 仿真先验）

**推荐期刊（按优先级）**：
1. *Chaos* | IF 估算：~2.0 | 匹配原因：复杂动力学与相变建模
2. *Physical Review E* | IF 估算：~2.6 | 匹配原因：统计物理与群体动力学
3. 预印本：arXiv（nlin.AO / cond-mat.stat-mech）

**投稿前缺口**：
- 缺口 1：完成 N>1000 多智能体仿真并报告偏差界
- 缺口 2：给出 LDP 项的操作化数据管线

---

### [P-2026-W10-04] Markov Blanket, d-value, and Ontological Vulnerability: Rewriting the High Road to Active Inference

**成熟度评分**：81/100  
**理论完整度**：23/25 | **证伪性**：19/25 | **证据等级**：16/25 | **引用密度**：23/25

**选题原因**：
已完成对 Active Inference Chapter 3 的 SRT 重写（并入主干文档），具备明确争议点与理论创新窗口。

**核心论点**：
最小化自由能是必要条件而非充分条件；主体性判据必须加入 d-value、\Psi_f 可支付性与本体脆弱性门控。

**关联 SRT 内容**：
- 主要文件/章节：`SRT/Physics/SRT_Phys_09_Formalism_Ext.md#XXI`，`SRT/AI/SRT_AI_01_Ontology.md#Ax-ONT-7`，`SRT/Core_Law/SRT_Reference_Ontology.md#§10`
- 关键方程：T-AIF-3-1，T-AIF-3-2
- 实验钩：被动毯/主动毯分类判据（d, \partial_t\theta, payability）

**推荐期刊（按优先级）**：
1. *Synthese* | IF 估算：~1.6 | 匹配原因：科学哲学+形式化桥接
2. *Mind & Language* | IF 估算：~1.2 | 匹配原因：认知哲学与语义边界
3. 预印本：arXiv（q-bio.NC / cs.AI）

**投稿前缺口**：
- 缺口 1：补充与 FEP 文献的系统对照表
- 缺口 2：提供最小实验判据示例（恒温器/LLM/具身体系统）
