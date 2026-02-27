# SRT Alignment Audit (v1~v6)

> 目的：把现有建模脚本逐条映射到 SRT 公理/方程，标出一致、冲突、待修正。

---

## 0) 对齐基准（来自 SRT 目录）

- 三域：`L_0 / L_1 / L_2`
- 算子：`\hat{G}_\theta`
- 核心命题：Existence = Selection
- 动力学核：
  - `dσ/dt = \hat{G}_\theta[σ] - ∇F + A`
  - `Ψ_f` 为本体论摩擦
- 关键指标：`d-value, Ψ_f, θ`

---

## 1) 文件级映射

### 1. `srt_mtor_sim.py`

**做了什么**：mTOR 阈值门控 + `exp(ωU)` 对泊松强度重权。

**SRT 对齐**
- ✅ 对齐 Ax-Core-A1/A2：把“显现概率”写成选择输出 + 代价重分配
- ✅ 对齐 Eq-Evo-01（弱对齐）：有选择项（`ωU`）和状态门控
- ⚠️ 缺失：`Ψ_f` 未显式出现，仅被隐含进参数

**结论**：可作为 L1 统计层的最小可运行近似，但不是完整 SRT 动力学。

---

### 2. `fit_srt_mtor.py`

**做了什么**：单条件 MLE + LRT 检验 `ω != 0`。

**SRT 对齐**
- ✅ 对齐“可证伪性”要求（Axioms/Experimental 方向）
- ⚠️ 冲突风险：单条件下 `α, θ, ω` 可互相吸收，违反 SRT 对参数语义分离的要求

**结论**：统计显著不等于理论显著，必须多条件。

---

### 3. `bayes_srt_mtor.py`

**做了什么**：双条件后验，输出 `P(ω>0)`。

**SRT 对齐**
- ✅ 强对齐 Ax-Core-A5（规范闭包）：通过多条件压实收敛结构
- ✅ 强对齐 Experimental falsifiability：后验 + CI + 方向概率
- ⚠️ 仍缺 `L_2` 显式变量，仅以条件代理

**结论**：是目前最接近“理论可检验形态”的版本之一。

---

### 4. `run_experiments.py` + `experiments_srt_mtor.csv`

**做了什么**：扫 `ω, θ, σ`，输出 rate/MI/ΔMI。

**SRT 对齐**
- ✅ 对齐信息-存在等价（A6）方向：用信息量变化作为现实偏置证据
- ⚠️ MI 指标仍是观测层，不等价于完整 `ii(s)` 定义

**结论**：可作为 SRT-A6 的经验代理，不可直接宣称“ii已测量”。

---

### 5. `fit_real_pipeline_v2.py`

**做了什么**：group split + baseline random effect proxy。

**SRT 对齐**
- ✅ 对齐 A4（具身有限视角）：按 circuit/session 分组避免伪全局视角
- ⚠️ test 负增益暴露 `U(t)` 的跨域不稳，说明 `\hat{G}` 代理不够稳

**结论**：揭示问题，不是终点。

---

### 6. `fit_real_pipeline_v3.py`

**做了什么**：block 标准化 + 层级 `ω`。

**SRT 对齐**
- ✅ 对齐 A5（规范闭包）与 L2 稳定思想：block 结构引入收敛约束
- ✅ valid/test 双正，说明选择项开始泛化

**结论**：第一版“工程上站稳”的 SRT 近似。

---

### 7. `fit_real_pipeline_v4.py`

**做了什么**：引入 omics-informed `θ/α` 先验，联合拟合。

**SRT 对齐**
- ✅ 对齐 A4（θ具身参数）
- ✅ 对齐 Eq-Evo-02（参数慢变量受约束更新）
- ✅ 把阈值解释力与 SRT 权重解释力拆开

**结论**：理论解释清洁度明显提升。

---

### 8. `fit_real_pipeline_v5.py`

**做了什么**：层级 Empirical-Bayes（`ω_b, θ_i, α_i`）。

**SRT 对齐**
- ✅ 对齐“多尺度一致性”思想（A12方向）
- ✅ 对齐 A11 脆弱性：收缩后置信下降，避免虚假确定性
- ⚠️ `P(μ_ω>0)=0.94` 提醒：仍需更高质量证据链

**结论**：更保守但更可信。

---

### 9. `fit_real_pipeline_v6.py`

**做了什么**：MCMC 后验（fallback 版）。

**SRT 对齐**
- ✅ 对齐“后验不确定性报告”规范
- ⚠️ 不是全 NUTS/HMC；R-hat 缺失，不满足你最终审稿级标准

**结论**：可用，但不是最终版。

---

## 2) 冲突与修正清单（必须做）

1. **`Ψ_f` 未显式建模**（当前最大缺口）
   - 现状：只用 NLL/regularization 间接代理
   - 修正：加入 `Ψ_f` 显式项（可先用预测误差导数或状态偏离积分近似）

2. **`L_2` 仍偏工程代理**
   - 现状：session/block 代替 L2 结构
   - 修正：引入显式 L2 状态变量（规则稳定度、网络模块性、rigidity index）

3. **`ii(s)` 与 MI 混用**
   - 现状：MI 被当作信息强度代理
   - 修正：增加分化项 `i_diff` 与整合项 `i_spec`，按 `ii=min(...)` 实现

4. **`x_hat = sigmoid(u_z)` 属于桥接占位**
   - 现状：缺真实 time-aligned mTOR 序列
   - 修正：接真实 omics/time-linked proxy，去掉桥接近似

---

## 3) v7 建议（SRT-consistent）

### 最小方程组（建议）

- 选择动力学：
  `dσ/dt = \hat{G}_θ[σ] - ∇F[σ] + A`
- 参数慢变量：
  `dθ/dt = γ·A - δ·∂Ψ_f/∂θ - k·(Input-Baseline)`
- 观测层：
  `N_t ~ Poisson( λ_tΔt )`
  `log λ_t = b_i + ω_b U_t + α_i·gate(x_t, θ_i) - c·Ψ_f(t)`

这样才能把 `ω, θ, Ψ_f` 放在同一 SRT 动力学闭环里。

---

## 4) 当前判断（直结论）

- 你这套 v1~v6 **已经有 SRT 主效应雏形**（尤其 v3-v6）。
- 但如果要“理论级”而不是“统计级”结论，必须补齐 `Ψ_f` 与 `L_2` 显式建模。
- 换句话说：现在是 **SRT-compatible**，还不是 **SRT-complete**。
