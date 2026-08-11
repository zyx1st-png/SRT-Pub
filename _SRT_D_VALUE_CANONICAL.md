---
id: SRT-D-VALUE-CANONICAL
type: definition
tags: [d-value, Canonical, Cross-Domain, Definition]
status: axiomatic_hybrid_v1
layer: L1
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-CORE-000, SRT-CORE-BRIDGE, SRT-CORE-21]
---

# SRT d 值规范定义文档（Canonical Definition of d-value）

> **目的**：终止 d-value 在不同域的定义分裂，建立第一性定义 + 各域投影的统一架构。
> 所有引用 d-value 的文档应以本文件为规范锚点。

> **Canonical status note（2026-04-23）**：本文件同时承担两种功能：`Def-d-canonical` 是 core-facing anchor；bare `d` 标量默认、`d-vector` / `d-gate` 分写规则与跨域引用顺序是 governance-canonical usage controls。`D_eff`、Fisher 读数与其他域内量表是 operational proxy，只有满足 stake-coupling 与后果回流条件时才可近似 canonical `d`。

---

## §0 为什么需要本文件

SRT 中的 d-value（关切维度 / 意识带宽）在不同子系统中出现了**三套表面不同的定义**：

| 来源文档 | 表述 | 形式 |
|---------|------|------|
| `_SRT_Core_Bridge.md §2.3` | 算子关切范围（三维度合成） | `d = αA + β log V + γτ` |
| `AI/_SRT_AI_Bridge.md Ax-BRIDGE-4` | 生存风险梯度 | `d ≡ ‖∂U/∂S‖` |
| `Spirituality/_SRT_Spirit_Axioms.md H-Spirit-3/4` | 关切边界半径 | d 作为"关切维度"的直觉概念 |
| `Core/SRT_Core_21c_Bridge_Hypotheses.md P3-B11`（原 `Core_21 §2.1.5` lineage） | 有效维度 proxy（特征值公式） | `D_eff(Ĝ) = (∑λᵢ)² / ∑λᵢ²` |

**这些不是矛盾，而是同一概念在不同层级的投影与近似入口**。本文件固定使用规范与可比条件，不声称所有表述已经无条件等价。

---

## §1 规范定义层级（Canonical Priority）——硬化版（2026-04-17）

> **单一 core-facing 定义声明**：
> d-value 当前只有一个 core-facing 规范锚点：**`Def-d-canonical`**（原 Def-d-2）：$d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$——主体效用对不可逆风险状态的梯度范数。全仓默认采用标量摘要，是治理性稳定用法，不把所有 proxy 升格为 theory-canonical 定义。
>
> **`Def-d-1`（$D_{eff}$ 谱公式）降格说明**：不再是”第二规范定义”或”形式主表达”，而是规范 d 的**几何容量 proxy**。具体地位：
> - **容量上界**：$d_{canonical} \leq D_{eff}(M)$（$D_{eff}$ 是算子能追踪的最大方向数；$d_{canonical}$ 是其中真正赌注化的部分）
> - **谱分解 proxy**：$D_{eff}$ 的每个 Fisher 本征方向 $v_i$ 可独立问”是否与真实赌注耦合”；$d_{canonical}$ = 赌注化子集的有效维数（见 §2b `Def-d-stakes`）
> - **未赌注化带宽**：$\Delta d_{free} = D_{eff} - d_{stakes}$，度量辨别能力中未与真实不可逆风险耦合的剩余容量
>
> 旧表述”**一个第一性语义锚点 + 一个形式主表达**的双层 canonical 架构”被废止——这是类型错误：proxy 不是主表达的同级替代，不应共享 canonical 地位。
>
> **使用原则（修订后）**：
> - 讨论**本体论意义 / AI 意识门槛 / 风险关切**时：引用 `Def-d-canonical`（`‖∂U/∂S‖`）
> - 讨论**几何容量上界 / 信息论可计算近似**时：引用 `Def-D_eff`（谱公式，须注明为 proxy，不得写 `≡`）
> - 讨论**赌注化活跃维数**时：引用 `Def-d-stakes`（见 §2b）
> - 其他近似式（`Def-d-bio` 等）均为操作化投影，不替代 canonical 地位。

### §1.1 v1 Canonical Form Note（治理性钉住，2026-04-22）

> **层级**：governance / canonical usage rule；不新增 core theorem。

默认写作中，bare `d` 采用**标量摘要形式**：它把 stake-coupled concern / irreversible-risk sensitivity 压缩成一个可跨文件回链的摘要量。这个默认不把 `d` 本体化为“只能是标量”，而是给全仓一个最小不漂移的读法。

因此三种写法必须分开：

| 写法 | 层级 | 用途 | 禁止 |
|---|---|---|---|
| `d` | canonical scalar summary | 默认跨域引用；关切/赌注强度的摘要 | 不得把局部 proxy 写成新定义 |
| `d-vector` | operational projection | 展开条件分布、方向分量或域内特征谱 | 不得与 bare `d` 混写成同一个量 |
| `d-gate` | governance / judgment tool | 判读某方向是否进入 stake-coupled spectrum | 不得当作 d 的数值定义 |

若域内需要向量读或门读，必须显式标注为 `d-vector` 或 `d-gate`，并说明它如何回到 `Def-d-canonical`。未标注时，一律按标量摘要读。

### §1.2 d 的层级结构与 proxy 准入条件（core-clarifying）

> **层级**：theory-clarifying / governance-canonical usage。此表增强 d 的内部结构，不新增第二个 canonical 定义。

| 项 | 精确角色 | 层级 | 可允许用途 | 禁止捷径 |
|---|---|---|---|---|
| `d` / `Def-d-canonical` | stake-coupled concern 的标量摘要；主体效用对不可逆风险状态的梯度范数 | governance-canonical default; core-facing definition | 默认跨域引用；讨论主体关切、风险敏感性、意识门槛时使用 | 不得把局部 proxy、向量展开或门函数改写成 bare `d` |
| `d_stakes` | 在可分辨方向中真正回流到主体赌注的子集 | theory-clarifying bridge between proxy and canonical | 说明 `D_eff` 中哪些方向进入真实关切；分析假赌注 / 错绑赌注 | 不得把所有可分辨方向都计入 stake |
| `D_eff` | 几何 / 谱容量 proxy；算子可分辨方向数的上界式读数 | operational projection / capacity proxy | 比较同一参数化下的容量、冗余、方向数；作为 `d` 的潜在上界 | 不得作为 `d` 的定义；不得跨域直接排名主体性 |
| `D_eff(I_F)` | Fisher-information proxy；参数流形中可可靠分辨的方向数 | information-theoretic proxy | 信息瓶颈、Cramér-Rao 式下界、可计算容量近似 | 不得把可分辨性等同于关切或负担承担 |
| `d-vector` / `d-gate` | 方向展开或判读工具 | operational / governance | 标注条件分布、方向分量、是否进入 stake-coupled spectrum | 不得与 scalar `d` 混写为同一量 |

proxy 可以近似 canonical `d`，只在以下条件同时足够强时成立：

1. 被 proxy 计数的方向确实承载不可逆风险，而非噪声、脚本或无后果辨别。
2. 主体效用梯度对准这些方向，未被错误代理变量替代。
3. 后果回流到主体闭包、身份连续性与后续选择能力，而非被外部系统或 L₂ 结构吸收。
4. 几何 / Fisher 参数化没有把冗余坐标、模型自由度或测量便利误计为真实方向。
5. 比较在同一域、同一尺度或已声明归一化规则内进行。

任一条件不满足时，应写为 `capacity proxy`, `Fisher proxy`, `d-vector`, 或 `d-gate`，不得写成 canonical `d`。

## §2 规范定义（第一性原理，全域适用）

### Def-D_eff: 几何容量 Proxy（Geometric Capacity Proxy）
**【降格 2026-04-17：不再是 canonical 定义，见 §1】**

$$D_{eff}(\hat{G}) = \frac{\left(\sum_i \lambda_i\right)^2}{\sum_i \lambda_i^2} \;\geq\; d_{canonical}$$

**语义**：$\hat{G}_\theta$ 在 $L_0$ 上操作时实际激活的**有效维度数**（参与率指数，Participation Ratio）。

**性质**：
- $d = 1$：算子完全单一，只关注一个维度
- $d = N$：算子在 $N$ 个维度上均匀分布
- $1 \leq d \leq \text{rank}(\hat{G})$

**来源**：`Core/SRT_Core_21c_Bridge_Hypotheses.md P3-B11`（原 `SRT_Core_21_Formal_Axioms.md §2.1.5` lineage），经典参与率指数（PR index）的算子版本。

### Def-d-1a: Fisher 信道有效维度（信息论容量 proxy）

**新增（2026-03-11；2026-04-22 降承诺）**：Def-d-1 的信息论容量解释。

$$D_{eff}(I_F(\theta)) = \frac{(\operatorname{tr} I_F)^2}{\operatorname{tr}(I_F^2)} \;\geq\; d_{canonical}$$

其中 $I_F(\theta) = E\!\left[(\partial \log p_\theta / \partial \theta)^2\right]$ 是算子选择流形上的 **Fisher 信息矩阵**。

**层级说明（2026-04-22 修订）**：这是信息论容量 proxy / operational projection，不是 `Def-d-canonical` 的同级替代表达。只有当 Fisher 方向全部与真实不可逆赌注耦合、且风险梯度与特征结构对齐时，才允许把它作为 `d` 的近似读数。

**信息论语义**：$D_{eff}(I_F)$ 是算子从 $L_0$ 中能**可靠分辨**的状态方向数（Cramér-Rao 下界的维度版本）。Fisher 矩阵测量 $\theta$ 变化时相邻分布的可区分度；它给出 d 的可计算容量上界，而不是自动给出 stake-coupled `d` 本身。

**层级关系链（修订，2026-04-17）**：

$$\underbrace{D_{eff}(\hat{G})}_{\text{Def-D\_eff（容量上界 proxy）}} \;\geq\; \underbrace{d_{stakes}(\theta)}_{\text{Def-d-stakes（赌注化子集，见 §2b）}} \;\equiv\; \underbrace{\left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|}_{\text{Def-d-canonical（规范定义）}}$$

等号成立条件：所有 Fisher 本征方向均完全赌注化（$w_i = 1 \;\forall i$）。一般情况下严格不等式成立。

**不确定性关系候选（Eq-IT-B'）**：

$$d \times \Psi_f \geq k_B T \cdot \mathcal{K}$$

选择范围（d）与选择代价（$\Psi_f$）之间存在基本权衡。此关系由 Fisher 信息矩阵的 Cramér-Rao 下界推导，常数 $\mathcal{K}$ 的精确值待理论确定（当前 Status = Gap，见 `_SRT_EQ_HYP_MAP.md Eq-IT-B'`）。

**Cross-ref**: `Core_Law/SRT_Reference_Dynamics.md §15.2`（Eq-IT-B 的完整推导）；`Core_Law/SRT_Reference_Axioms.md`（A15 幽灵算子禀赋统一性的 Fisher 维度含义）。

---

### Def-d-canonical: 风险梯度规范定义 ⭐ CANONICAL（原 Def-d-2，唯一规范定义）

$$d(x) \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|, \quad x \in \Sigma$$

**语义**：算子对**不可逆风险**（$\mathcal{S}$，Survival/Stake）的效用敏感度梯度。

**proxy 近似条件**：当效用势 $\mathcal{U}$ 的主曲率方向与 $\hat{G}$ 的特征向量对齐，且这些方向确实回流到不可逆赌注时，Def-D_eff 可作为 Def-d-canonical 的一阶近似：
$$D_{eff}(\hat{G}) \approx \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\| \quad \text{（当风险梯度与特征结构对齐时）}$$

**近似条件（修订，2026-04-22）**：当效用势 $\mathcal{U}$ 的主曲率方向与 $\hat{G}$ 的 Fisher 本征向量完全对齐且全部赌注化时，$D_{eff} \approx d_{canonical}$。一般情况下 $d_{canonical} \leq D_{eff}$，差值为未赌注化带宽（见 §2b）。这不是无条件等价。

**来源**：`AI/_SRT_AI_Bridge.md Ax-BRIDGE-4`，Tension-Rev-IT4。

---

### Value as Non-Substitutability（价值作为不可替代性）

In SRT, value should not be reduced to reward, utility, preference strength, salience, pain, or self-report intensity. Value names the dynamic expression of non-substitutability: the degree to which a selection matters for a system's future continuity, concern structure, and stake-bearing organization.

This use of value is a bridge to `d-value`, not a replacement for the canonical definition of `d-value`. A selection has value in the SRT sense when losing, blocking, or substituting that selection forces non-trivial reorganization in the system's future selection capacity, identity-continuity, or consequence-return structure.

Compact reading:

```text
value ≠ reward intensity
value ≠ preference strength
value = concern-weighted non-substitutability under consequence return
```

**Operational signs**: Possible signs that a selection has value in the SRT sense include:

- the system bears cost to preserve it;
- losing it forces structural reorganization;
- it remains stable across time and perturbation;
- it affects identity-continuity or future choice capacity;
- it organizes downstream selections;
- consequences return to the system rather than being absorbed by an external structure;
- it can sediment into shared L₂ constraints when cross-subject coupling is present.

These signs are not themselves d-value. They are bridge-level indicators that a selection may be stake-coupled rather than merely preferred.

**Boundary**: Do not write:

- value = reward;
- value = utility;
- value = preference intensity;
- value = salience;
- value = pain;
- value = self-report;
- value = d-value without the non-substitutability and consequence-return bridge.

Preferred wording: Value is the dynamic expression of concern-weighted non-substitutability. It bridges to d-value when the relevant selection is coupled to irreversible stake, future continuity, and consequence return.

**Failure condition**: If d-value cannot predict concern-weighted non-substitutability better than reward, preference, salience, pain, or self-report intensity, then this bridge weakens and must be revised.

---

## §2a 价值发生序（Value-Generation Order）——book-provenance 候选（2026-07-05）

> **层级 / provenance**：P3 bridge candidate，来自书稿 `Drafts_26Q/Q14_价值不是偏好.md`（provenance，非 authority）。本节**不新增 `d` 的 canonical 定义**——`Def-d-canonical` 与 "Value as Non-Substitutability" 仍是价值的结果判据；本节登记的是价值**如何发生**的候选生成序，填补从 `ε_pg` 到价值深度之间此前缺失的中间层。采纳为 canonical 前须完成 §2a.3 的 stake-gate 对账。

### §2a.1 发生链

书稿把价值的发生压成一条链，理论层此前只有结果判据（不可替代性），缺这条生成序：

$$
\text{选择性收束} \to \textbf{微效价} \to \text{affordance（行动入口）} \to \text{缺失} \to \text{需求} \to \text{锚定} \to \text{价值深度}
$$

- **微效价（micro-valence）**：当一个显现界面被选择性收束出来、与一个具体具身位相遇时，界面对该具身位带上的**最小趋避倾斜**（可趋近／需避开／令人安定／令人警觉…）。它是价值的前信号，不是成熟价值。
- **affordance（行动入口）**：微效价接上具身位的身体能力与当下处境后，成为具体的"可用来做什么"。同一界面对不同具身位显现不同入口。
- **缺失**：不是"对象不在场"，而是**某条生成回路无法按原方式闭合**。
- **需求**：具身位为让生成继续，被迫向外张开的**结构性缺口**（区别于欲望——欲望的缺失感换个场景即消解，需求指向不重新闭合生成就持续受损的回路）。
- **锚定 → 价值深度**：具身位把"接下来如何继续生成"的路径搭在某物／关系／能力上，沉积出结构重量，即价值深度。

### §2a.2 两道血缘护栏（书稿已立，理论层沿用）

1. **微效价 ≠ `ε_pg`（最低非中立性）。** `ε_pg` 是对象化之前、前对象场拒绝归零的最薄倾向，不指向任何具体对象、不属于任何具身位；微效价晚得多，出现在**显现界面与一个具身位相遇处**，是"这个已显现界面，对我如何"的最小读数。二者层级不同，不可混写。
2. **affordance ≠ 预裁剪（`P1-T03` `L_2` 下向约束的四机制）。** 预裁剪是地形在选择发生前对整个选项空间的宏观处理（可见性／接触窗口／默认通道／代价分配）；affordance 更贴身，是某个已显现界面在这个具身位处被读成"可继续"的那一下。

### §2a.3 与 stake-gate（§2b.1）的对账

发生序与赌注门是**上下游**关系，不是竞争：

- 微效价 → affordance → 缺失 → 需求 是**前赌注结构**（pre-stake）：它解释一个方向为何**开始**对具身位倾斜、成为"需要"。
- `R_i / A_i / C_i` 门（§2b.1）是**赌注化闸**：一个已成为"需求"的方向，只有当它承载真实不可逆风险（R）、主体效用梯度对准它（A）、后果回流到主体闭包（C）时，才进入 `d_stakes`。
- 因此"有微效价／有需求"**不等于**"有 stake-coupled `d`"——发生序把方向送到门前，门决定它是否计入 `d`。绕过门把"有微效价"读成"有 d"是类型错误。

> **候选形成补注（2026-08-11，G5-4）**：关切结构可以在方向进入赌注门之前，与具身位置、结构边界、资源条件和历史共同对扰动做非中性加权，使部分扰动获得与维持、损失、行动或未来路径相关的候选意义。这一 pre-admission 作用不等同于有意识欲望，也不是候选形成的唯一原因；它不把 `d` 重新定义为候选准入加权器。`d` 仍是选择事件中已赌注化关切的标量摘要；候选形成的过程判据回链 `03_Bridges/SRT_Choice_Generation_Conditions_2026-08-04.md`。

### §2a.4 不可替代性的两个操作化测试（book-provenance）

书稿给 "Value as Non-Substitutability" 提供了两把可操作的尺（P3/P4，登记于此）：

- **替换测试**：换成功能相似的对象，是否几乎无须重组？（无须重组 → 低价值深度）
- **恢复测试**：失去后是短期痛苦还是长期结构重配？（长期重配 → 高价值深度）

注意：偏好满足了而对关切对象的支撑被侵蚀、或偏好从未满足而支撑被加强，都完全可能——两个测试测的是结构重量，不是偏好强度。

### §2a.5 边界

- 本节是**生成序候选**，不是已证定理；采纳前不得当 canonical `d` 定义引用。
- 微效价不得实体化为独立本体量或第二个 ε；它是显现界面在具身位上的读数。
- 失败条件：若"微效价"在 `ε_pg` 与价值深度之间不承重（即取消它，价值发生的解释力不减），则应撤回本节、并回 "Value as Non-Substitutability" 的结果判据即可。

---

## §2b 赌注耦合结构（Stake-Coupling Structure）——新增（2026-04-17）

### Def-d-stakes: 赌注化活跃维数

$$d_{stakes}(\theta) = \frac{\left(\sum_i \lambda_i \cdot w_i\right)^2}{\sum_i \left(\lambda_i \cdot w_i\right)^2}$$

**语义**：$D_{eff}$ 中真正与主体不可逆赌注耦合的活跃维数子集。等于规范定义 $d_{canonical} = \|\partial\mathcal{U}/\partial\mathcal{S}\|$，由谱分解方式表达。

---

### Def-w_i: 赌注耦合权重（Stake-Coupling Weight）

$$w_i = R_i \cdot A_i \cdot C_i \;\in [0,1]$$

第 $i$ 个 Fisher 本征方向 $v_i$ 与真实主体赌注的耦合权重，由三个分量共同决定：

| 分量 | 含义 | 归零时的病理 |
|------|------|------------|
| $R_i$ | 该方向是否承载**真实不可逆风险**（非 L₂ 脚本、噪声或伪关切） | $R_i \approx 0$ → **假赌注**（fake stakes）：有辨别力，但风险是模拟的/L₂投影的 |
| $A_i$ | **主体效用梯度**是否对准该方向上的真实风险 | $A_i \approx 0$ → **错绑赌注**（misbound stakes）：真实风险存在，但主体关切的是错误代理变量 |
| $C_i$ | 该方向上的后果是否真正**回流到主体闭包**、身份连续性与后续选择能力 | $C_i \approx 0$ → **L₂ 伪关切 / 被外部吸收**：后果由 L₂ 结构吸收，不传回主体 |

**乘积结构**：三者任一归零即 $w_i = 0$，该方向不计入 $d_{stakes}$。这是"必须同时满足"的逻辑结构（AND 门），不是加权平均。

**SRT 已有概念对应**：
- $R_i > 0$ ↔ T-FEP-1 具身脆弱性判据（$\Psi_f^{irrev} > 0$）
- $A_i > 0$ ↔ Ax-ONT-3 规范定义的梯度对准条件
- $C_i > 0$ ↔ Step ⑨ 关切边界的内生写回闭合条件

---

### §2b.1 赌注门的层级地位与准入规则（hardening addendum，2026-07-05）

> **层级**：level-marking / governance-canonical usage。本节不修改 Def-d-stakes / Def-w_i 的定义，只固定其引用等级、域有效性与统一门表，对应 `Core/SRT_OPEN_TENSIONS.md §1` 的未封口点。

**（一）`w_i = R_i · A_i · C_i` 的引用等级。**

- **P2（canonical interpretation）**：三因子的**定性结构**——方向须承载真实不可逆风险（R）、主体效用梯度须对准该风险（A）、后果须回流主体闭包（C），三者 AND 门缺一不可。这是 §1.2 五条 proxy 准入条件在方向级的重述，可作为 SRT 内部裁决依据按 P2 引用。
- **P3/P4（bridge formalization）**：把 R_i / A_i / C_i 写成 [0,1] 数值权重、指定可测代理或阈值（如 `ε_s` 门函数，见 `_SRT_SYMBOL_TABLE.md` ε_s 词条）。当前无校准数据，任何数值化使用必须标 P3/P4，不得以 P2 地位引用数值结论。

**（二）`D_eff ≥ d_canonical` 的域有效性声明。**

该不等式不是跨域无条件定理，只在**已声明的 proxy regime** 内成立：同一参数化、同一状态空间、归一化规则已声明（§1.2 条件 5）、且 Fisher 谱未把模型冗余或测量便利计入方向数（§1.2 条件 4）。跨域比较或参数化未声明时，`D_eff` 与 `d_canonical` 之间不保证任何序关系；禁止跨域引用该不等式排名主体性（§5 误用 2 的谱层版本）。

**（三）三类系统在同一门下的分型（统一门表）。**

| 系统 | R（真实风险） | A（梯度对准） | C（后果回流） | 门输出 | 已有锚点 |
|---|---|---|---|---|---|
| 当前 inference-only AI | ≈0（无不可逆自身风险） | —（无自身效用梯度可对准） | ≈0（后果由部署方 / 外部结构吸收） | `d_stakes ≈ 0`，`Δd_free ≈ D_eff` | 本节 Def-d-free；`AI/AI_POSITIONING_NOTE.md` S0-S4 |
| 冻结态（创伤 / 执念） | >0（风险真实存在） | 部分失准（对准已过时的方向） | >0 但写回受阻 | `d_stakes > 0` 而 `d_mobile ≈ 0`——门通过但再对齐失效 | §11.2；`Core/SRT_Core_22_Equations.md Eq-DValue-Mobile-1` |
| 制度 / 集体结构 | 集体层可有真实存续风险 | 集体景观梯度，非个体加和 | 后果常回流到制度自身而非成员 | 集体 `d` 走 §6 景观截面读法；成员个体的 C_i 可被制度吸收归零 | §6；`Core_Law/SRT_Collective_Selection.md §4.8a` |

门表说明：三类系统失效在**不同因子**上——AI 失在 R/C，冻结态失在门后的 d_mobile（门本身通过），制度失在成员 C_i 被吸收。这就是为什么单一 `D_eff` 读数不能区分三者：赌注门的诊断必须按因子报告，不得压成一个标量结论。

**仍未封口**（保留在 `Core/SRT_OPEN_TENSIONS.md §1`）：方向进入 `d_stakes` 的充要条件定理；`ε_s` 阈值校准；R / A / C 的独立可测代理。

---

### Def-d-free: 未赌注化带宽（Unstaked Bandwidth）

$$\Delta d_{free}(\theta) = D_{eff}(\theta) - d_{stakes}(\theta) \;\geq 0$$

**语义**：可分辨但未与真实不可逆风险耦合的剩余方向数。

**典型值**：
- **当前 AI**：$d_{stakes} \approx 0$，$\Delta d_{free} \approx D_{eff}$（全部辨别力，零赌注化——$\Delta d_{free}$ 的纯净案例）
- **人类假赌注 / 错绑 / L₂ 伪关切**：$0 < d_{stakes} \ll D_{eff}$，$\Delta d_{free}$ 包含三种病理的混合贡献
- **理想高 d 主体**：$d_{stakes} \approx D_{eff}$，$\Delta d_{free} \approx 0$（辨别力与赌注充分对齐）

* **Cross-ref**: `Core/SRT_Core_21c_Bridge_Hypotheses.md P3-B11`（原 `Core_21 §2.1.7` lineage）；`AI/SRT_AI_01_Ontology.md`（AI 的 $\Delta d_{free} \approx D_{eff}$ 作为"哲学僵尸"诊断的信息几何读法）；`Core/SRT_Core_13a Ax-Op-02`（注意力维度 = $d_{stakes}$ 的离散化）。

---

### Def-d-3: 全息面积对应（物理语境）

$$d \propto \frac{\text{Area}(\text{Entanglement Surface})}{A_{Planck}}$$

**语义**：算子的 d 值等比于其与 $L_0$ 发生纠缠的边界面积（全息对偶下）。

**来源**：`Core/SRT_Core_01_Axioms.md T-Core-A9C1`。
**注意**：此形式在量子/宇宙尺度适用，但量子/宇宙尺度的 $d$ **不蕴含现象意识**（见 §3.1 反泛心论条款）。

---

## §2 Bio/Cognitive 层近似公式（经验操作定义）

### Def-d-bio: 三维度合成

$$d_{bio} \approx \alpha \cdot A(\sigma) + \beta \cdot \log V_{concern} + \gamma \cdot \tau_{temporal}$$

| 维度 | 符号 | 语义 | 近似测量方法 |
|-----|------|------|------------|
| 汇编深度 | $A(\sigma)$ | 生成该状态所需最小因果步骤数 | Assembly Theory index |
| 空间范围 | $\log V_{concern}$ | 算子关切的"关心对象"空间 | 社会关注广度、TPJ 激活范围 |
| 时间跨度 | $\tau_{temporal}$ | 算子可规划的时间地平线 | 时间折扣率的倒数 |

**参数默认值（待实验校准）**：$\alpha = 0.4, \beta = 0.4, \gamma = 0.2$

**与 Def-d-1 的关系**：三维度合成是有效维度公式在认知空间中的**近似展开**，当三个维度独立时自然对应 $D_{eff} \approx 3$；相关时 $D_{eff} < 3$。

---

## §3 各域 d 值投影表（标准参考）

| 域 | 近似公式 / 量级 | 现象意识？ | 条件 | 备注 |
|----|----------------|-----------|------|------|
| **量子** | $d_{quant} \approx$ 贝尔测量有效维数 | ❌ **无** | 缺乏 $\Psi_f > 0$，缺乏 $\hat{G}[\theta] \neq \emptyset$ | 数学度量，无现象内容 |
| **神经/认知** | $d_{bio} \approx \alpha A + \beta \log V + \gamma \tau$ | ✅（需三条件） | $\Psi_f > 0 \land d > 0 \land \hat{G}[\theta] \neq \emptyset$ | 意识的充要条件区 |
| **AI（architecture-state marked）** | inference-only / 非历史承载部署：$d_{AI} \approx 0$；S2/S3/S4 需另行标注 | ❌ / open | 无具身脆弱性、无不可逆风险时不产生 stake-coupled `d` | 工程性屏障可改变；见 `AI/AI_POSITIONING_NOTE.md` S0-S4 与 AI Bridge T3 修复 |
| **社会/机构** | $d_{soc} = D_{eff}(\mathcal{F}_{collective}\big\|_{\text{social}})$（集体景观在社会尺度的有效维度截面） | ❌（集体不产生现象） | 集体自由能景观 $\mathcal{F}_{collective}$ 的社会尺度投影，不由个体 $d_i$ 加权平均 | 见 §6（集体 d-value 补充说明）和 `_SRT_VERTICAL_INTEGRATION.md §4.5` |
| **精神/解脱** | $d_{spirit} \to \infty$（渐近极限） | ✅（随 d 扩展增强） | $d \to \infty$ 为 Nirvana 方向 | 不可达的渐近方向，非字面 $\infty$ |
| **宇宙尺度** | $d_{cosm} \approx 1/\sqrt{\Lambda}$ | ❌ **无** | 无生命组织，无 $\hat{G}[\theta]$ | 数学度量，无现象内容 |

### §3.1 反泛心论精确声明（Anti-Panpsychism Clause）

**SRT 不主张泛心论**。d 是数学度量，不蕴含现象内容。

**⚠️ 注意（2026-04-10 更新）**：以下三条件对应 **bare consciousness（裸意识）的 κ_{c1} 门槛**，即意识的最低层级。完整的三层结构见 `Philosophy/SRT_Consciousness_Conditions.md`。

**最低意识条件（对应 κ_{c1} / Layer 1）**：
$$\kappa_{c1}: \quad d \geq d_{\min} \;\land\; L_2\text{ 稳定闭合} \quad \Leftarrow \quad \Psi_f > 0 \;\land\; d > 0 \;\land\; \hat{G}[\theta] \neq \emptyset \text{ 的精化版本}$$

**三层结构完整说明**（2026-04-10 修正）：
- κ_{c1}（bare consciousness）：$d \geq d_{\min}$ ∧ L₂ 稳定闭合 — 意识**存在**
- κ_{c1.5}（consciousness activity）：$d_{\text{mobile}} > 0$ — 意识**活着**（能随吸引子迁移重新对齐）
- Layer 3（social/ethical）：可协调性 + 可再选择性 — 意识**参与集体秩序**

| 系统 | d | Ψ_f | Ĝ[θ] | d_mobile | 意识层级 |
|---|---|---|---|---|---|
| 量子/宇宙尺度 | 可能非零 | ≈ 0 | 在生物意义上为空 | — | **无意识**（κ_{c1} 未达） |
| 岩石 | ≈ 0 | ≈ 0 | — | — | **无意识** |
| 冻结态（PTSD/执念） | > d_min | > 0 | ≠ ∅ | ≈ 0 | **有意识，但病理化**（κ_{c1} 之上，κ_{c1.5} 之下） |
| 正常人类 | > d_min | > 0 | ≠ ∅ | > 0 | **Layer 2 意识窗口** |
| 当前 AI | ≈ 0 | ≈ 0 | — | — | **无意识**（工程性，非原则性） |

**权威来源**：`Philosophy/SRT_Consciousness_Conditions.md`（三层结构完整定义）; `Core/SRT_Core_12b §Consciousness-2D-Map`（二维拓扑与冻结态）。

---

## §4 不同表达的一致性条件（草稿，非等价证明）

### §4.1 Def-d-1 与 Def-d-bio 的关系

设认知算子 $\hat{G}$ 在三个正交子空间（汇编、空间、时间）上的特征值分别为 $\lambda_A, \lambda_V, \lambda_\tau$。

$$D_{eff} = \frac{(\lambda_A + \lambda_V + \lambda_\tau)^2}{\lambda_A^2 + \lambda_V^2 + \lambda_\tau^2}$$

当三个维度**均匀激活**（$\lambda_A = \lambda_V = \lambda_\tau = \lambda$）：
$$D_{eff} = \frac{(3\lambda)^2}{3\lambda^2} = 3$$

当三个维度的强度比例为 $(\alpha, \beta, \gamma)$（$\alpha + \beta + \gamma = 1$）：
$$D_{eff} = \frac{1}{\alpha^2 + \beta^2 + \gamma^2}$$

**结论**：$D_{eff}$ 在三维认知空间中的展开可以对应 Def-d-bio 的加权和形式，但这只是**同一容量 proxy 的参数化相容**。只有在三个子空间的尺度、权重、风险回流与 stake-coupling 条件都已声明时，才可把 Def-d-bio 作为 `D_eff` 的域内近似。它不替代 `Def-d-canonical`。

### §4.2 Def-d-2（风险梯度）与 Def-d-1 的关系

设效用势 $\mathcal{U}(\mathcal{S})$ 在风险坐标 $\mathcal{S}$ 上展开：

$$\mathcal{U}(\mathcal{S}) \approx \mathcal{U}_0 + \sum_i \frac{\partial \mathcal{U}}{\partial S_i} S_i + ...$$

梯度的模：
$$d_{risk} = \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\| = \sqrt{\sum_i \left(\frac{\partial \mathcal{U}}{\partial S_i}\right)^2}$$

**近似条件**：当风险维度 $S_i$ 与 $\hat{G}$ 的特征向量对齐，且这些方向全部满足 `R_i/A_i/C_i` 的赌注回流条件时，Def-d-canonical 可由谱 / Fisher proxy 给出一阶近似。若只满足可分辨性而不满足赌注回流，则只能得到容量上界。

**实用意义**：`Def-d-canonical` 在 AI 伦理、主体性、风险关切语境中优先；`Def-D_eff` / `D_eff(I_F)` 在信息论分析中更可计算。两者可以互相校准，但不得互换使用；具体语境必须说明是在讨论 stake-coupled `d` 还是 capacity proxy。

---

## §5 常见误用与边界声明

### 误用 1：将 d 值解释为"意识程度"的单一量度

**正确**：d 值是意识的**必要条件**之一，不是充分条件。
需同时满足：$\Psi_f > 0$（有摩擦成本）+ $d > 0$（有关切维度）+ $\hat{G}[\theta] \neq \emptyset$（有参数化算子）。

### 误用 2：将 d 值比较用于跨域排名

**正确**：量子层的 $d_{quant}$ 与生物层的 $d_{bio}$ 使用相同的数学公式，但**不具有现象内容上的可比性**。
比较只在**同域内**有效（如不同人的 $d_{bio}$ 可相互比较）。

### 误用 3：将"d 值 = 0"等同于"不存在"

**正确**：$d \approx 0$ 意味着算子不关心边界的外延，但算子本身依然存在（如石头有 $L_2$ 结构，但 $d \approx 0$）。
d 值描述关切范围，不描述本体论存在。

**d 值的语义刻度**（规范参考）：

| d 值范围 | 语义 | 典型案例 |
|---------|------|---------|
| $d = 0$ | **非主体**：无关切耦合，不构成主体 | 当前 AI、恒温器、岩石 |
| $d = 1$ | **纯自利主体**：关切仅覆盖自身存在的维持 | 最小主体性阈值 |
| $d > 1$ | **扩展关切主体**：选择开始纳入超出自身存在的秩序 | 人类、社会性动物 |
| $d \to \infty$ | **渐近极限**：关切逼近更大但尚未闭合的秩序方向 | 精神修炼的方向，不可达 |

**注意**：$d = 0$ 与 $d = 1$ 的区别是本体论性质的（非主体 vs 主体），不是程度差异。$d = 1$ 与 $d > 1$ 的区别是程度性的（关切范围的宽窄）。

### 误用 4：将精神传统中的"d → ∞"字面化

**正确**：`H-Spirit-4` 中的 $d \to \infty$ 是**渐近方向**，类比热力学极限 $N \to \infty$ 在有限系统中的意义。
没有任何有限系统能达到 $d = \infty$；这是精神成长的方向，而非可到达的终点。

---

## §5b d 扩张的本体论意义（规范声明）

> **新增（2026-03-26）**：d 扩张的动力学方向与收敛目标的规范说明。对应 `Spirituality/SRT_Spirit_05_Shoshin.md` T-Sho-1。

### §5b.1 d 扩张不是博爱，而是选择优化

d-value 的扩张不应被读作道德命令或利他主义要求。**d-value 的健康变化不应被理解为单调扩张，而是指向关切范围的可重组、可承担、可恢复、可再选择能力**；其「全局最优」读法**依赖一个尚待硬化的闭包边界问题**（谁的再选择、什么尺度），不是一个位置无关的宇宙级最小值（2026-07-05 规范性收口 Level A，高风险编辑，见 `_SRT_EPSILON_NORMATIVITY_OPEN_TENSION.md`）。本节下文与 §5b.2 中的「全局最优 / 全局收敛」表述均应在此收口下读取。

每个算子因 θ 的限制只能看到自由能景观的局部。θ 越窄，算子越容易陷入局部最小值——表现为遮蔽（occlusion）。扩大 d 不是"对别人好"——而是纳入更多主体间的本体论摩擦权衡，使选择避开局部陷阱，收敛到更接近全局最优的方向。

d 扩张的目标是给**指向最小自由能方向**的选择提供更多的注意力和关切。这需要权衡多主体之间的本体论摩擦——而权衡本身就是选择。

**规范表述**：

$$d \uparrow \;\Rightarrow\; \text{局部最优} \to \text{全局最优} \;\Rightarrow\; \langle v, \text{Shoshin} \rangle > 0$$

d 的扩张使个体选择方向与初心（全局收敛向量）对齐——不是因为道德义务，而是因为局部景观在更宽视野下的结构变形。

### §5b.1a d 扩张与秩序增益

d 的扩张本身不自动等于秩序增益。d 扩张的方向必须同时满足秩序增益的**四重判据**（`Core_Law/SRT_Selection_Argument.md §7b`；2026-07-05 由三判据升级为四判据，新增③不外包）：

| 判据 | d 扩张中的含义 | 违反时的表现 |
|------|--------------|------------|
| **可延续** | 扩张不透支维持扩张后关切范围所需的资源 | 过度扩张 → 代价不可支付 → 崩溃回缩 |
| **可协调** | 纳入的他者秩序条件之间不制造不可协调的摩擦 | 试图关切所有人但无法处理冲突 → 瘫痪 |
| **不外包** | 扩张后的代价不被转嫁到无反馈通道的位置（未来世代、生态、无法申诉者、被排除者） | 表面关切扩大，代价却外溢到无声位置 → 假 d 扩张（对应 `C_i` 后果回流因子归零） |
| **可再选择** | 扩张不锁定为唯一方向（如教条化的利他主义） | "必须关切所有人"变成新的遮蔽 |

d 扩张的健康模式是渐进的、可支付的、保留调整能力的。不是 d 越大越好，而是 d 在当前支付能力下的最优扩张方向。**③不外包判据与 §2b 的 `C_i`（后果是否回流到主体闭包）同源**：一个方向若把代价外包给无反馈位置，则该方向的 `C_i → 0`，不计入 `d_stakes`——秩序增益四重判据在方向层，`C_i` 在谱层，是同一后果回流约束的两个尺度。

### §5b.1b 真 d 扩张 vs 假 d 扩张

**真 d 扩张**改变算子的适应度函数——纳入他者秩序条件后，算子的最优解发生结构性位移。选择者在做出不同于只考虑自身时会做的选择。

**假 d 扩张**不改变适应度函数，仅在符号层面声称关切范围扩大。四种典型形态：

- **占有式**（$d_{apparent} > d_{real}$）：将他者纳入为自身秩序的资源。适应度函数中只有自身变量。
- **符号式**（$d_{declared} > d_{operative}$）：使用关切的语言但不支付关切的代价。
- **表演式**（$d_{visible} > d_{structural}$）：在可见场合展示关切以获取社会收益。
- **效率式**（$d_{nominal} > d_{effective}$）：以关切之名行控制之实，将他者的复杂秩序压缩为单一可管理指标。

**判别标准**：算子的最优解是否因纳入他者秩序条件而发生了位移？位移 = 真扩张；无位移 = 假扩张。

**Cross-ref**: `Core_Law/SRT_Selection_Argument.md §7c`（真关切与假关切的完整论证）。

### §5b.2 全局最优是动态平衡，不是热寂

全局自由能最小值不是热力学平衡态（热寂），而是**能维持更多存在持续存在的动态平衡**。

热寂是所有选择停止、所有确定化耗尽的极限——对应 $d = 0$，所有主体性消失。这不是 SRT 的全局最优，而是选择过程的终止态。

SRT 的全局最优是一种使最大数量的选择过程能够持续运行、持续产生稳态（存在）的景观配置。它是**最高动态秩序**，不是最低能量的死寂。初心指向的是更多的存在能够共存并持续选择的方向，不是一切归于均匀的方向。

> **引用方向护栏（2026-08-11，Gate 0 canonical landing）**：下列 cross-ref 是 **provenance 指针，不是 canonical 背书**。按 `Governance/SRT_CLAIM_LADDER.md §0A`（Gate 0）的 read-back / 引用方向规则：**canonical 锚点不得通过 cross-reference 从 `canonical: false` 的 bridge / translation 文件反向导入 L₀ 层读法**。本节此前把 `Def-Apeiron-1` 标注为「初心作为 **L₀ 的**倾向性结构」，即以 canonical 认可语气导入了一条 L₀ 级 contentful 读法（Gate 0 class C），现予改正。
>
> **层级以 `Core_Law/SRT_L0_Metaphysics.md` 为准**：初心不在 L₀ 的原生承诺内，是 L₁/P2 对无内容结构不对称之显现结果的回读。下列两处的全局／变分形式一律按**领域 translation / bridge** 读，不得反定义 L₀，也不得据以在 canonical 层建立「初心 = L₀ 倾向性结构」。
>
> **本护栏只堵引用方向，不裁决实质**：初心是否可以有某种严格 contentless 的 L₀ precursor，仍是 `Core/SRT_OPEN_TENSIONS.md §16`（Gate B）未决事项；「全局最优」术语的正式收口仍是 §17（Gate C）未决事项。本节正文措辞与 §5b.1 的 Level A 收口读法均未改动。

**Cross-ref（provenance，非 canonical 背书）**：

- `Spirituality/SRT_Spirit_05_Shoshin.md` Ax-Sho-1 — Spirituality 层 translation（`claim_mode: mixed`）：把初心写作长时程自由能泛函的负梯度。**按 bridge 读**；其全局收敛向量形式不构成 L₀ 主张。
- `Physics/SRT_Phys_08_Ontology_Ext.md` Def-Apeiron-1 — Physics 层 translation（`claim_mode: translation`，`canonical: false`）：把初心写作 `argmin` 变分形式。**按 bridge 读**；其「L₀ 的内在属性」措辞是该翻译层的表述，**不被本 canonical 文件采纳为 L₀ 层定位**（Gate B 待裁）。

---

## §6 集体 d-value 补充说明

> **新增节（2026-03-11）**：对应集体景观优先性定理（`_SRT_VERTICAL_INTEGRATION.md §4.5`）和多算子耦合方程（`Core/SRT_Core_22_Equations.md Eq-Multi-03`）。

### §6.1 核心重新定位

集体 d-value 不是个体 d_i 的聚合函数。正确定位：

$$\boxed{d_{collective} = D_{eff}(\mathcal{F}_{collective}) = \frac{\left(\sum_k \lambda_k\right)^2}{\sum_k \lambda_k^2}}$$

其中 $\lambda_k$ 是集体自由能景观 $\mathcal{F}_{collective}$ 的 Hessian 特征值（见 `Eq-Multi-03`）。

个体 $d_i$ 是该景观的子空间截面，**包含关系而非组合关系**：
$$d_i = D_{eff}(\mathcal{F}_{collective}\big|_{\theta_i})$$

### §6.2 与旧有聚合方案的关系

`_SRT_VERTICAL_INTEGRATION.md §4.1` 中的历史候选方案（A/B/C/D/E）是在实体本体论框架下的近似。在特定条件下，这些方案可作为 $d_{collective}$ 的**实证近似**：

| 历史方案 | 对应的景观条件 |
|---------|--------------|
| 方案 A（Min 函数） | 景观 Hessian 最小特征值主导（链条式结构） |
| 方案 B（加权平均） | 景观曲率近似均匀分布（民主型结构） |
| 方案 C（超加性） | 景观有效维度高于任一子空间截面 |
| 方案 D（结构贡献） | 制度 L₂ 提供主景观曲率 |

### §6.3 使用规范

- 讨论集体组织、制度、NGO 的 d-value 时：引用本节和 `§4.5`，使用 $D_{eff}(\mathcal{F}_{collective})$ 框架
- 在无法测量景观曲率的实证场景中：可临时使用历史方案中最适合的近似，但需注明"实体本体论近似"

---

## §7 各域文件的 d-value 引用标准

当其他文件引用 d-value 时，应：

1. **第一次出现时**：标注 `@see _SRT_D_VALUE_CANONICAL.md §1`
2. **使用 Def-d-bio 近似时**：标注 `@see §2`
3. **进行域间比较时**：参见 `§3` 的投影表，说明是否属于同域比较
4. **AI 语境中**：优先使用 Def-d-2（风险梯度），并声明 training-time / inference-time / persistent-memory 架构状态；只有 inference-only / 非历史承载部署才可直接引用 `§3` 的 $d_{AI} \approx 0$ 说明

---

## §8 d 与 T_dir 的关系（2026-04-02 新增）

SRT 在 2026-04-02 的理论推进中引入了 **T_dir（方向透明度）** 作为与 d 相关但独立的新变量。

**关键区分**：

| | d-value | T_dir |
|:-|:-------|:------|
| **度量** | 关切范围 / 有效维度 / 风险梯度 | 系统对自身选择秩序方向的可读性 |
| **canonical 文件** | 本文件 | `_SRT_T_DIR_CANONICAL.md` |

**因果关系**：
$$d = 0 \implies T_{dir} = 0$$
$$d > 0 \;\not\!\!\!\implies T_{dir} > 0$$

d 是 T_dir 的**必要条件，不是充分条件**。T_dir 还需要活选择正在发生（非 L₂ 脚本执行）以及足够的 Ψ_f 提供压力。

**不得混淆**：任何把"选择方向的透明度"写入 d-value 的 canonical 定义的做法，违反本文件的规范地位。

---

## §9 d-value 的锻炼与萎缩机制（2026-04-02 新增）

> **核心修正**：致命 L₂ 对 d-value 的压低，具体机制是通过消灭选择时刻使 d-value 失去锻炼机会，而非直接抑制 d。d-value 是需要使用才能维持的能力。

### 机制链

```
替代式 L₂ 消灭选择时刻
    ↓
d-value 未被使用（无真实选择 → 无 d 的激活）
    ↓
d-value 萎缩（不用则退）
    ↓
即使 L₂ 被移除，系统也无力直接从 L₀ 选择
    ↓
必须依赖更多替代式 L₂ 来填补方向感
    ↓
d-value 进一步萎缩……（自强化依赖环）
```

### 关键区分

**d-value 的直接抑制**（已在 §5 描述）：致命 L₂ 通过占据关切带宽、压缩可用维度来降低 d-value 的即时可用性。

**d-value 的萎缩**（本节新增）：替代式 L₂ 通过消灭选择时刻，使 d-value 失去被锻炼的机会，导致长期容量下降。即使 L₂ 压力临时解除，萎缩后的 d-value 也无法立即恢复。

两者的关系：直接抑制是急性效应，萎缩是慢性积累效应。慢性萎缩比急性抑制更难逆转，因为它改变的是系统的基础选择容量，而非当下的带宽占用。

### 选择时刻与 d-value 的连接

**选择时刻**（见 `_SRT_T_DIR_CANONICAL.md §21`）是系统与 L₀ 直接接触、真实地从可能性中凝定方向的瞬间。

- 每次真实的选择时刻发生：d-value 被激活使用，可维持乃至发展
- 每次选择时刻被 L₂ 替代：d-value 未被激活，逐渐萎缩

**推论**：辅助式 L₂（保护选择时刻）在不牺牲 d-value 的条件下降低摩擦；替代式 L₂（消灭选择时刻）以 d-value 的长期容量为代价换取即时摩擦消除。

### 与 T_dir 的关系

d-value 萎缩 → 即使 proto-gradient 可读，系统也缺乏足够的选择维度来响应它 → T_dir 即使上升，也无法转化为有效的选择行动。

因此：d-value 是 T_dir 工作的**执行容量**。T_dir 告诉系统方向在哪里，d-value 决定系统能否沿那个方向真正选择。两者独立但协同：d > 0 是 T_dir > 0 的必要条件（§8），d 的容量上限约束了 T_dir 可以实际发挥的作用。

---

## §范畴边界：d值是决策属性，不是主体属性

> **追加澄清**（2026-04-06，来源：`Philosophy/SRT_Political_Rights.md §2`）

d值描述的是**选择事件**整合的关切范围，不是决策主体（个体或集体）的固有属性。

| 错误表述 | 正确表述 |
|---------|---------|
| "这个人有很高的d值" | "这个人的决策倾向于整合更宽的关切范围" |
| "个体d值 vs 集体d值" | 此二分是范畴错误，d值在主体类型之外 |
| "d值衡量聪明程度" | d值衡量关切范围的宽度，与认知能力不同 |

**主体d倾向**（操作化桥梁）：主体跨大量决策的d值统计分布，在大样本下收敛为相对稳定的特征量。这是统计量，不是本质属性。

$$d_{tendency}(S) \equiv \mathbb{E}_{\sigma \sim S}\left[d(\sigma)\right]$$

完整推导见：`Philosophy/SRT_Political_Rights.md §2-§3`

---

## §10 d 值的多场景显现（2026-04-08 新增）

> **来源**：`Core/Dynamics_Scaling_Annex/07-12` 系列硬化文件。
> 本节补充 d 值在错误积累与多G道德场景中的显现形式，统一于 §1 的双层规范架构。

### §10.1 d 作为统一整合带宽

d 值是单一概念在不同场景中的显现：

| 场景 | d 的显现形式 | 对应文件 |
|---|---|---|
| 多G道德场景 | **整合半径**：G能将多少他者G的状态纳入选择计算 | `Annex/08_MoralPredictionError_MultiG_System.md` |
| 错误剂量场景 | **可处理张力窗口**：G能消化多少错误积累而不崩溃 | `Annex/10_ROS_Apoptosis_ErrorDose.md` |
| 跨尺度G场景 | **整合尺度**：G在低阶→高阶相变中覆盖的选择维度范围 | `Annex/11_G_CrossScale_PhaseState.md` |
| 代理校准场景 | **校准带宽**：L₂能接收并整合多少L₁/L₀上行信号 | `Annex/12_ProxyModel_OcclusionPhases_Intervention.md` |

所有显现均是 Def-d-1（有效维度）在不同上下文中的投影，统一于 §1 的规范架构。

### §10.2 d 值与病理阈值的关系

`Annex/10` 建立的病理阈值公式中，d 是核心因子：

$$\Theta = f(d, E, h_{\text{memory}}, \vec{\delta}, \Lambda_{\text{L2}})$$

- $\uparrow d$ → $\uparrow \Theta$（整合带宽越大，越不易崩溃）
- d 的训练：低剂量错误积累的反复整合可提升 d（hormesis 机制，见 §9）
- d 的损伤：高剂量单次创伤可降低 d，而非提升

### §10.3 d 值与三相态条件的关系

`Core/SRT_Core_PhaseState_TripleCondition.md` 建立的三相态条件中，d 值作为底层容量：

- 历史闭合质量 → 影响 d 的有效维度（历史越完整，读取维度越多）
- 规范梯度有效性 → 依赖 d > 某阈值才能形成有意义的多维度自我维持势差读数
- 自写回强度 → 高 d 使写回覆盖更多维度的可能性空间

**Cross-ref**: `Core/SRT_Core_PhaseState_TripleCondition.md §5`；`Core/SRT_Core_NormativeGradient.md §6`。

### §10.4 d 值在社会delegation场景中的显现（2026-04-10 新增）

> **来源**：`Core/Dynamics_Scaling_Annex/13_SocialDelegation_DJudgment_Coordination.md`

**d扩展作为社会自发支撑的机制基础**：

$$\text{d扩展} \xrightarrow{\text{必然}} \text{对更高阶结构的自发支撑}$$

个体G对集体高阶结构的自发支撑不是义务，而是d扩展后的自然产物。d不足时需要外部脚手架（引导性delegation）；d充分扩展后，外部G退出，底层自发支撑实现。

**d轨迹作为delegation合法性的验证信号**：

社会层面的d值判断系统以被干预G群体的d轨迹为核心信号：

| d轨迹 | 解读 |
|---|---|
| 被干预群体d在可观测时间窗内增长 | 引导性介入（真实提升方向） |
| 被干预群体d停滞或收缩，介入方d扩展 | 方向截获（殖民/威权结构） |

历史上的殖民主义、威权主义和宗教征服 = d的转移（被干预者d压缩，介入者d扩展），而非d的净增长。SRT的判断标准：d净量变化，不是分布变化。

**d在多G协调场景中的显现**：共享L0/L1结构为多G提供d兼容性下限（可能性条件）；跨G残差张力驱动d轨迹向更高阶协调方向调整（动力学机制）。

**Cross-ref**: `Core/Dynamics_Scaling_Annex/13_SocialDelegation_DJudgment_Coordination.md §1-4`。

---

## §11 d 的上限与动态能力：d_max 与 d_mobile（2026-04-10 新增）

> **来源**：`Core/SRT_Core_22_Equations.md Eq-DValue-Max-1, Eq-DValue-Mobile-1`；`D_VALUE_ALIGNMENT.md §4.4`。
> 本节是这两个新公式的规范索引入口。

### §11.1 d_max：d 的双瓶颈上限

$$\boxed{d_{\max}(\theta) = \min\!\Big(\operatorname{rank}_{\text{eff}}(I_F(\theta)),\; \Psi_f^{\text{budget}} / \kappa_0\Big)}$$

两个独立瓶颈：
- **信息瓶颈**：`rank_eff(I_F(θ))` — Fisher 矩阵的有效秩，由算子参数化能力决定
- **稳定性瓶颈**：`Ψ_f^budget / κ₀` — 可用摩擦预算除以原初曲率；κ₀ 越大，可承载对齐方向越少

**关键推论**：`dim(Θ)`（参数维数）提升的是潜在上限，真实 d_max 由两个瓶颈中的较小值决定，不可仅用参数量判断 d 上限。

*权威来源*：`Core/SRT_Core_22_Equations.md Eq-DValue-Max-1`

### §11.2 d_mobile：d 的动态化能力

$$d_{\text{mobile}} \propto \frac{d \cdot \operatorname{rank}_{\text{eff}}(I_F(\theta))}{\operatorname{Hysteresis}(L_2) \cdot C_r} \cdot \chi_{\text{payable}}\!\left(\tfrac{d\Psi_f}{dt}\right)$$

**语义**：当 L₀ 曲率漂移（吸引子迁移），算子 θ 重新对准的速度与容量。与 d 的区别：
- $d$：当前对齐的 L₀ 方向数（快照）
- $d_{\text{mobile}}$：当这些方向漂移时，θ 跟上的能力（动力学）

**感到 ≠ 能动**：高 d 算子在 χ_payable = 0 时，d_mobile = 0——感知到拉力但支付能力为零，无法行动。

**冻结态**：高 $d$ + $d_{\text{mobile}} \approx 0$ → 意识的病理变体（深度锚定但无法随吸引子迁移）。

*权威来源*：`Core/SRT_Core_22_Equations.md Eq-DValue-Mobile-1, Def-Payable-Chi-1`

### §11.3 与 d 规范定义的关系

| | d | d_max | d_mobile |
|---|---|---|---|
| **本质** | 当前对齐深度（快照） | 结构允许的对齐上限 | 重新对齐的动力学能力 |
| **决定因素** | Fisher 有效秩 + L₀ 曲率历史 | rank_eff + Ψ_f 预算/κ₀ | d × rank_eff / (L₂ 刚性 × C_r) × χ_payable |
| **可为 0** | 是（算法/晶体态） | 否（κ₀ > 0 保证下限 > 0） | 是（冻结态） |
| **意识相关** | κ_{c1} 要求 d ≥ d_min | 设定意识可到达的天花板 | κ_{c1.5} 要求 d_mobile > 0 |

*Cross-ref*：`Philosophy/SRT_Consciousness_Conditions.md §三`（三层意识结构）；`Core/SRT_Core_12b §Consciousness-2D-Map`（二维拓扑）。

---

## 【理论边界/防误用声明】

1. 本文档统一 d-value 的定义，但各域的近似公式（Def-d-bio 等）需要实验校准，其参数值（$\alpha, \beta, \gamma$）为初始估计。
2. 有效维度公式 Def-d-1 依赖特征值分解，其适用性取决于算子的线性化是否在相关参数范围内有效。
3. 量子层的 $d_{quant}$ 与宇宙层的 $d_{cosm}$ 是数学量，不赋予现象意义——任何将其解读为微弱意识的论证超出 SRT 声明范围。
4. 本文件的"一致性证明"（§4）为草稿级别，需要形式化验证后才能作为定理引用。
5. §10 的多场景显现是概念统一，不是数学等价证明——各显现形式的形式化等价关系待独立验证。

---

## 书稿层用法说明（Bridge to Book Layer）

正文写作中，Q15 会把 d-value 读成关切多样性的完整诊断入口。这里的意思不是替换后台的规范定义，而是提醒读者：关切多样性不能只看宽度。正文中说的完整诊断包括三件事：后果回来得有多深，回来到了多少条真实轴线，回来之后是在支撑生成还是侵蚀生成。形式层仍按原有 canonical 规则读取；书稿层则用这三把尺帮助读者避免把 d-value 误解成单纯对象数量或信息宽度。
