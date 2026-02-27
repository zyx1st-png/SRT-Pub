# SRT-mTOR 选择性现实模型（方法草案）

## 1. 生成模型

对回路 \(i\) 在离散时间窗 \(\Delta t\) 的放电计数：

\[
N_i(t) \sim \mathrm{Poisson}(\mu_i(t)), \quad
\mu_i(t)=\lambda_i^{(\omega)}(t)\Delta t
\]

其中

\[
\lambda_i^{(\omega)}(t)=\lambda_i^{(0)}(t)\exp(\omega U_i(t)),
\]

\[
\lambda_i^{(0)}(t)=\lambda_{i,\mathrm{base}}+\alpha_i\sigma\big(k_i(x_i(t)-\theta_i)\big),
\quad
\sigma(z)=\frac{1}{1+e^{-z}}.
\]

mTOR 动力学：

\[
\dot x_i = a_i s_i(t)-b_i x_i+\xi_i(t).
\]

---

## 2. SRT 解释

- \(U_i(t)\)：选择性现实效用（由任务目标/观测偏好定义）
- \(\omega\)：观测权重强度（塌陷参数）
  - \(\omega=0\)：无 SRT 偏置
  - \(\omega>0\)：概率质量向高 \(U\) 状态重分配

路径测度等价形式：

\[
\mathbb{P}_\omega(\mathcal N)=\frac{e^{\omega\mathcal U(\mathcal N)}\mathbb{P}_0(\mathcal N)}{Z(\omega)}.
\]

---

## 3. 估计与检验

### 3.1 MLE
通过最小化 Poisson NLL 拟合 \((\lambda_{base},\alpha,\theta,\omega)\)。

### 3.2 似然比检验（LRT）

\[
H_0:\omega=0 \quad vs \quad H_1:\omega\neq0,
\]

\[
LR=2(\ell_1-\ell_0)=2(\mathrm{NLL}_0-\mathrm{NLL}_1).
\]

### 3.3 贝叶斯后验
在两条件或多条件干预下估计后验 \(p(\omega\mid D)\)，报告：
- \(\mathbb E[\omega\mid D]\)
- 95% CI
- \(P(\omega>0\mid D)\)

### 3.4 信息论判据（SRT一致性）
对时间窗计数 \(N\) 与效用离散分箱 \(U_b\) 计算：

\[
\Delta I = I(N;U_b)_{\omega>0} - I(N;U_b)_{\omega=0}.
\]

若 \(\Delta I>0\) 且 \(P(\omega>0)\) 高，则支持“选择性现实偏置”。

---

## 4. 可辨识性约束（关键）

单条件下 \(\alpha,\theta,\omega\) 存在耦合替代。必须至少满足：

1. 多条件输入干预（改变 \(s(t)\) 统计）
2. 对 \(\theta\) 给生理先验
3. 共享/层级先验稳定 \(\omega\)

否则“塌陷”可能只是阈值曲线重参数化。

---

## 5. 当前本地结果摘要

- 单条件 MLE：能检出 \(\omega\neq0\)，但有参数耦合
- 双条件贝叶斯：\(P(\omega>0)\approx1\)，CI 与真值重叠，恢复稳定

该结果支持 SRT 版“选择性现实偏置”作为可检验统计假设，而非不可证叙事。
