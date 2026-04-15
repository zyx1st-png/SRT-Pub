---
id: SRT-ANNEX-14-ST-RHYTHM-SPATIAL
type: working_draft
status: annex_candidate
layer: L1
claim_mode: conditional_structural
dependency: [T-Scale-Rhythm-1, T-Scale-Rhythm-2, T-Scale-08, Lemma-Scale-Budget-Embed-1]
created: 2026-04-15
note: 工作草稿，经过 /srt-harden 五刀承重测试后写入。母命题（无纯时空均匀解）达到 Annex 可入门槛；Spatial-S1 条件投影尚不进主链。待 T-Scale-08 维度无关性核实后再决定升格。
---

# ST-Rhythm-Spatial: 时空节律对偶工作草稿

> **文件状态**：Annex 工作草案（Working Draft）  
> **进入条件**：经五刀 /srt-harden 承重测试后达到 Annex 准入门槛  
> **未进入主链的原因**：Lemma-Spatial-Boundary-Cost-1 尚为 schema-preserving 弱化版，需核实 T-Scale-08 维度无关性后升格；Spatial-S1 本身为条件投影，额外前提（时间出口封闭）尚未在主链引理中正式化  
> **最高诚实结论**：无纯时空均匀解（Prop-ST-NoUniform）；Spatial-S1 = 该命题在时间预算充裕条件下的投影，最高只能推出"非零空间带宽"，不直接推出 Turing 图样 / 晶格 / 皮层柱等具体周期结构

---

## 动机

T-Scale-Rhythm-1 至 Rhythm-5 刻画了**时间维度**上有限算子的间歇结构。但"有限"不只锁时间——也锁空间。一个具有空间外延的算子若被要求在其全部空间外延上密集锚定多个目标，面临同构的预算超载。本草稿证明：空间上的均匀密集锚定在一般条件下不可行。

**与时间 Rhythm 链的关系**：
- Rhythm-1 是 Prop-ST-NoUniform 的**时间投影**（时间出口 E1）
- Spatial-S1 是 Prop-ST-NoUniform 的**空间投影**（空间出口 E2，在 E1 关闭后）
- traveling waves / spiral waves / cortical traveling waves 是 E1+E2 联合的时空出口，不是后补丁

---

## 引理体系

### Lemma-Spatiotemporal-CoPresence-1（Bounded-Delay Co-Maintenance，切口 1）

设 $\Sigma_{co}$ 是一个**非可分共同维持目标集**。对任一 $\sigma_i \in \Sigma_{co}$，其在时刻 $t$ 的维持依赖于其他相关成员在某个有界时延 $\tau_{co} < \infty$ 内对它保持**可读 / 可调制 / 可约束**（bounded-delay mutual accessibility）。

设任意纯时间扫描方案在 $\Omega$ 上造成的最坏重访时延 $T_{revisit}^*$ 满足：
$$T_{revisit}^* > \tau_{co}$$

则纯时间扫描解不可行；系统必须在空间上保留某种**同时活跃的分离支撑**（simultaneously active distributed support）。

**负担类型**：$[\mathbf{C}]$（条件性：依赖 $\Sigma_{co}$ 的非可分性与 $\tau_{co}$ 的有限性）  
**关键参数**：$\tau_{co}$（有界维持时延）；$T_{revisit}^*$（最坏扫描重访时延）  
**神经层特例**：$\tau_{co} \approx \Delta t_{coh}$（相干窗口）；$v_{prop}$ 给出时延的物理实现  
**边界**：非可分性需显式检验——若 $\Sigma_{co}$ 可分解为独立单目标，则 Lemma 1 触发条件失效，纯时间扫描可行

---

### Prop-ST-Uniform-Block-1（连续场均匀不可行性，切口 2）

对每个 $\sigma_i \in \Sigma_{co}$，给定一个 **substrate-relative realization kernel** $\rho_i(x) \ge 0$（桥接/实现层对象，不 canonize 为新 L1 名词；表示位置 $x$ 处的局部锚定对 $\sigma_i$ 维持能贡献多少）和窗口阈值 $m_i > 0$，满足在共同维持窗口 $W$（$|W|=\tau_{co}$）内：
$$\int_\Omega a_{j(i)}(x,t)\,\rho_i(x)\,dx \;\ge\; m_i \qquad (\forall t \in W)$$

**不可行性条件**：若满足以下三条：
1. $\Sigma_{co}$ 满足 Lemma-Spatiotemporal-CoPresence-1 的 bounded-delay co-maintenance
2. 窗口 $W$ 内局部可用预算有上界 $E_{avail}^{local}(W)$（由 Lemma-Spatial-Locality-1 给出）
3. 任一 x-均匀候选解 $a_j(x,t)=c_j(t)$ 的最低成本下界，在按 $\mathcal{R}_i(W)$ / minimum irreducible cover 计费后，仍超过局部可用预算：
$$C_{unif}^{min}(W) \;\gtrsim\; |W|\,|\Omega|\sum_{\text{cover}} \frac{m_i}{\|\rho_i\|_1} \;>\; E_{avail}^{local}(W)$$
（$\gtrsim$ 为粗记号；对重叠支撑需按**最小不可约 cover** 计费，避免重复计数）

**结论**：x-均匀解不可行；存在 $t^* \in W$ 与某个 $j$ 使得：
$$\operatorname{Var}_x\!\bigl[a_j(\cdot, t^*)\bigr] > 0$$

**负担类型**：$[\mathbf{C}]/[\mathbf{S}]$ 混合——条件 3 为可检验的定量约束，结论为直接推论  
**关键对象**：$\rho_i(x)$（桥接层，不做 L1 本体词升格）；$C_{unif}^{min}(W)$（均匀候选的成本下界）  
**边界**：此命题不推出 $\operatorname{Var}_x > 0$ 的空间模式——只推出非零方差存在性；条件 3 的具体数值取决于 $\rho_i$、$|\Omega|$、$E_{avail}^{local}$ 的系统参数化

---

### Lemma-Spatial-Boundary-Cost-1（空间边界成本，schema-preserving 弱化版，切口 3）

T-Scale-08 给出边界维持成本的规范形式。空间非常值结构的维持，可视为该同一成本形式在空间界面上的实现：

$$F_{boundary}^{spatial}[a_j] \;\equiv\; \int_{\partial\,\text{supp}(a_j)}\!\!\!\bigl[L_{class}^{spatial} + \lambda_1\,\Psi_f^{maint} + \lambda_2\,\Psi_f^{switch}\!\!\restriction_\partial\bigr]\,d\Sigma$$

其中 $\Psi_f^{switch}\!\restriction_\partial$ 不是新对象，只是 $\Psi_f^{switch}$ 在空间界面穿越上的实例记号（"内/外切换"与时间上"前/后切换"共享同一摩擦本质，但当前**不宣称** T-Scale-08 的推导已覆盖空间维度）。

T-Scale-08 给出边界强制的规范成本形式；空间边界是这一形式的**自然对偶扩展**，而非当前已核实的直接推论。  
**待升格条件**：核实 T-Scale-08 的原始推导不依赖时间序列的本质性步骤；若确认维度无关，则本 Lemma 可升格为"$F_{boundary}$ 的维度无关投影"。

**负担类型**：$[\mathbf{C}]$（依赖待核条件）+ $[\mathbf{T}]$ schema 类比（schema-preserving，非 load-bearing 的完整推论）  
**关键承重方向**：不引入 $\Psi_f^\nabla$ 作为新摩擦分量；不将承重偷塞入 $\rho_i$ 的形状；空间结构成本由 $F_{boundary}^{spatial}$ 承担  
**边界**：弱化版不给出"锐利 vs 平滑边界"的代价差异的完整解释；该差异的精确处理待 Spatial-S2 / 后续推论

---

### Lemma-Spatial-Locality-1（传播时间局部预算，切口 4）

对位于 $x_i$ 的目标 $\sigma_i$，在共同维持窗口 $W$（$|W|=\tau_{co}$）内，定义其**传播时间可达域**（propagation-time reachability domain）：
$$\mathcal{R}_i(W) \;\equiv\; \bigl\{y\in\Omega : T_{prop}(y\to x_i)\le\tau_{co}\bigr\}$$

其中 $T_{prop}(y\to x_i)$ 为从 $y$ 到 $x_i$ 的物理传播时间（各向异性、非均匀介质均适用）。则其局部可用预算满足上界：
$$E_{avail}^{local}(\sigma_i,W) \;\le\; \int_W\!\!\int_{\mathcal{R}_i(W)} P_{supply}(y,t)\,dy\,dt$$

**独立性条件**：若 $\mathcal{R}_i(W)\cap\mathcal{R}_j(W)=\varnothing$，则 $\sigma_i,\sigma_j$ 在窗口 $W$ 内的预算池彼此独立，**不能被当作窗口内完全可替代资源**。

**重叠修正**：若存在重叠 $\mathcal{R}_i(W)\cap\mathcal{R}_j(W)\neq\varnothing$，则重叠部分**按一次计费**（minimum irreducible cover / flow-constrained allocation 修正），不允许双重计入。

**推论（各向同性均匀介质特例）**：当 $T_{prop}(y\to x_i)=|y-x_i|/v_{prop}$ 时，$\mathcal{R}_i(W)=B(x_i,\,v_{prop}\,\tau_{co})$（欧氏球），独立条件退化为：
$$|x_i - x_j| > 2\,v_{prop}\,\tau_{co}$$

**负担类型**：$[\mathbf{C}]$（依赖 $T_{prop}$ 存在性 + $P_{supply}$ 可积性）；推论为 $[\mathbf{A}]$（在各向同性假设下直接析出）  
**关键参数**：$T_{prop}(y\to x_i)$（传播时间函数，系统基底决定）；$P_{supply}(y,t)$（局部供能率场）  
**边界**：$\mathcal{R}_i(W)$ 的计算依赖基底物理（传导率、扩散系数等），本 Lemma 不给通用数值；$E_{avail}^{local}$ 为上界，实际可用量可能严格更小

---

## 母命题

### Prop-ST-NoUniform（无纯时空均匀解）

设有限扩展算子 $\hat{G}_\theta$ 需在空间外延 $\Omega$ 内维持非可分共同维持集 $\Sigma_{co}$，满足以下条件：

- **[C1]** $\Sigma_{co}$ 满足 Lemma-Spatiotemporal-CoPresence-1 的 bounded-delay co-maintenance（$\tau_{co}$ 有界，$T_{revisit}^* > \tau_{co}$）
- **[C2]** 每个目标 $\sigma_i$ 的维持依赖 substrate-relative realization kernel $\rho_i(x)$，且局部预算受 Lemma-Spatial-Locality-1 的 $\mathcal{R}_i(W)$ 封顶
- **[C3]** 在窗口 $W$ 内，按 $\mathcal{R}_i(W)$ / minimum irreducible cover 计费后，均匀候选解的最低成本下界仍超过局部可用预算：
$$C_{unif}^{min}(W) > E_{avail}^{local}(W)$$

**结论**：不存在同时满足以下三条的可行解：

1. 时间上无间歇（$a_j(x,t)$ 在 $t$ 上连续且密集，无切换）
2. 空间上均匀（$\operatorname{Var}_x[a_j(\cdot,t)]=0$ 对所有 $j,t$）
3. 对 $\Sigma_{co}$ 全体成员在 $W$ 内同时满足维持阈值 $m_i$

任意可行解必须在以下三个出口中至少选其一：

| 出口 | 内容 | 对接 |
|------|------|------|
| **E1** 时间出口 | 在 $t$ 方向产生间歇（$\operatorname{Var}_t[a_j(\cdot,\cdot)] > 0$） | Rhythm-1 时间分时 |
| **E2** 空间出口 | 在 $x$ 方向产生非均匀（$\exists t^*, j: \operatorname{Var}_x[a_j(\cdot,t^*)] > 0$） | 空间结构（非零空间带宽） |
| **E3** 目标放弃 | 降低 $|\Sigma_{co}|$，退出 co-maintenance 要求 | 功能降级 |

**反证**：反设存在同时满足 1+2+3 的解。由反设中的**空间上均匀**条件，得 $a_j(x,t)=c_j(t)$（与 $x$ 无关）。由 Prop-ST-Uniform-Block-1：在 [C1][C2][C3] 下，此均匀解的最低成本下界（按 $\mathcal{R}_i(W)$ / minimum irreducible cover 计费后）超过局部可用预算——违反条件 3。矛盾。∎

**负担类型**：$[\mathbf{C}]/[\mathbf{S}]$ 混合——三个 C 条件给出触发域，反证为 $[\mathbf{S}]$  
**最高合法结论**：无纯时空均匀解；E2 出口必须有非零空间方差  
**不能推出**：具体空间模式（Turing 图样 / 晶格 / 皮层柱 / 取向柱）；空间频谱主峰位置；周期性（只推出非常值，不推出周期性）

---

## 条件投影

### T-Scale-Rhythm-S1（空间非零带宽定理，条件投影版）

**额外前提 [C4]**：$\Sigma_{co}$ 与各维持阈值 $m_i$ 被**外生固定**，不允许通过删目标、降阈值或拆解 co-maintenance 要求来规避（E3 关闭）；且时间预算充裕，Rhythm-1 不被触发，无需时间间歇（E1 关闭）。

**结论**：在 [C1][C2][C3][C4] 下，系统必须走 E2——存在 $t^* \in W$ 与某个 $j$ 使得：
$$\operatorname{Var}_x\!\bigl[a_j(\cdot,t^*)\bigr] > 0$$

等价地，锚定场的时间平均空间功率谱在非零空间频率上有正测度：
$$\int_{|k|>0} \overline{S_a^{spatial}}(k)\,dk > 0$$

**位置**：Turing pattern / 皮层柱 / 晶格的**上位必要条件**，不是直接解释。要从 T-Scale-Rhythm-S1 推进到这些具体结构，需要额外的对称破缺条件（Spatial-S2 可行窗口）和周期化条件（Spatial-S3，对应 Rhythm-3 的空间类比）。

**Cross-ref**：T-Scale-Rhythm-1（时间对偶；E1 出口）；Prop-ST-NoUniform（上位母命题）；Lemma-Spatiotemporal-CoPresence-1；Lemma-Spatial-Locality-1；Prop-ST-Uniform-Block-1；T-Scale-08（$F_{boundary}$ 规范来源）；Lemma-Spatial-Boundary-Cost-1（空间边界成本 schema）

---

## 理论边界 / 防误用声明

- **不主张**：空间节律是时间节律的"派生"或"特例"——两者在逻辑上独立，均为 Prop-ST-NoUniform 的不同投影
- **不主张**：任何具体空间图样（Turing / 皮层柱 / 晶格）直接由本草稿推出——本草稿只推出**上位必要条件**
- **不主张**：Lemma-Spatial-Boundary-Cost-1 已经是 T-Scale-08 的推论——当前为 schema-preserving 扩展，待升格
- **不主张**：$\rho_i(x)$ 是 L1 本体词——它是桥接层实现核，与 L1 的具体对象个体化的联系需要独立论证
- **开放问题 [O]**：Spatial-S2（空间占空比可行窗口）和 Spatial-S3（空间耦合驱动的周期化）是本草稿的自然后续，但当前未写；写法应对称 Rhythm-2 / Rhythm-3 的时间版本，加入空间特有的各向异性和拓扑约束

---

## 升格路径

| 条件 | 当前状态 | 升格触发 |
|------|---------|---------|
| Lemma-Spatial-Boundary-Cost-1 弱化 | schema-preserving 扩展 | 核实 T-Scale-08 不依赖时间序列的本质步骤 |
| Spatial-S1 为条件投影 | 需 E1+E3 关闭 | 给出 [C4] 的形式判据（时间预算充裕的量化条件） |
| 母命题进主链 | Annex 草案 | Spatial-S2/S3 写完、Spatial 链形成闭合 |
