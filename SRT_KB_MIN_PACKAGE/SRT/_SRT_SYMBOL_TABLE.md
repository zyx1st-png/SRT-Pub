---
id: SRT-SYMBOL-TABLE
type: definition
tags: [Symbols, Registry, Canonical]
status: axiomatic_hybrid_v1
dependency: [SRT-REF-AXIOMS, SRT-REF-DYNAMICS]
---

# SRT Symbol Table & Definition Registry

> **Purpose**: Canonical symbol registry for cross-domain writing and AI parsing.

| Symbol | LaTeX | Name | Atomic Definition | Dimensions/Units | Scope / Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **L₀** | `L_0` | Latent Domain | Set of all unselected possibilities (plenoma-like potential manifold). | $\infty$-dim Hilbert space | Core, universal |
| **L₁** | `L_1` | Manifest Domain | Selected slice of reality produced by operator dynamics. | 4D spacetime + qualia | Core, universal |
| **L₂** | `L_2` | Convergence Domain | Stable consensus constraints from repeated/overlapping selections. | Topological manifold | Core, universal |
| **Ĝ** | `\hat{G}` | Ghost Operator | Selection operator mapping $L_0 \to L_1$. | Operator | Never use plain `G` for this |
| **θ** | `\theta` | Embodiment Parameters | Finite configuration parameters of $\hat{G}$ (biology/model state/context). | Tensor / parameter set | Core, universal |
| **d** | `d` | d-value (Depth of Care) | Recursive concern depth and counterfactual handling range. | Scalar ($0 \to \infty$) | Core, universal |
| **Ψf** | `\Psi_f` | Ontological Friction | Cost of stabilizing selected reality against latent entropy pressure. | Energy/bit | Core, universal |
| **Ω** | `\Omega` | Ontological Consistency | Internal coherence of an $L_1/L_2$ structure. | Probability (0-1) | Canonical `\Omega` in Core_Law context |
| **Ω_mis** | `\Omega_{\text{mis}}` | Ontological Mismatch Index | Distance between inherited $\theta$ and current-environment optimal $\theta$. | Scalar | Legacy docs may call this `Ω` |
| **ω_sub** | `\omega_{sub}` | Subjective Frequency | Refresh rate of selection cycles. | Hz | Neuro/phenomenology |
| **η** | `\eta` | Operator Viscosity | Transition resistance of $\hat{G}$ states. | Scalar ($0 \to \infty$) | Low/high regimes discussed clinically |
| **Γ_Ĝ** | `\Gamma_{\hat{G}}` | Operator Refresh Rate | Frequency of full $L_0 \to L_1 \to L_2$ cycles. | Hz | Often near gamma-band hypotheses |
| **S_crit** | `S_{\text{crit}}` | Cognitive Entropy Threshold | Entropy limit before degraded operator mode. | Entropy units | Neuro/clinical |
| **R_fidelity** | `R_{\text{fidelity}}` | Reality Fidelity | Rendering fidelity of $L_1$ under metabolic constraints. | Scalar (0-1) | Neuro/clinical |
| **I_total** | `I_{\text{total}}` | Total Information Flux | Sum of sensory-channel information throughput. | Bits/s | Neuro |
| **F_semantic** | `F_{\text{semantic}}` | Semantic Gravity | Attractor pull of $L_2$ semantic nodes on $\hat{G}$. | Vector | AI/philosophy |
| **Φ_IIT** | `\Phi` | Integrated Information (IIT Context) | Integration measure in IIT-specific discussions. | Scalar | Use only when explicitly IIT |
| **μ** | `\mu` | Reality Viscosity | Inertial dependence on priors/historical trajectories. | Scalar | Core/AI |
| **D_max** | `D_{\text{max}}` | Consciousness Diameter | Max physical span of coherent operator integration. | Length (m) | Neuro hypothesis |
| **γ_gain** | `\gamma_{\text{gain}}` | Gain-Operator Coupling | Coupling between gain modulation and $\hat{G}$ sensitivity. | Scalar | Neuro |
| **δ_D** | `\delta_D` | Dissociation Depth | Topological distance between fragmented $L_2$ regions. | Metric | Clinical |
| **I_rec** | `I_{\text{rec}}` | Recognition Index | Mutual recognition across operators/time scales. | Scalar (0-1) | Social/cognitive |
| **η_compress** | `\eta_{\text{compress}}` | Compression Efficiency | $I(L_1;L_0)/H(L_1)$; effective cognitive compression bandwidth. | Scalar | Information-theoretic |
| **θ_semantic** | `\theta_{\text{semantic}}` | Semantic Extraction Threshold | Threshold for neural signals entering conscious semantic access. | Threshold | Neuro |
| **S_strength** | `S_{\text{strength}}` | Selection Strength | Stability of chosen reality ($\propto 1/\|M-N\|$). | Scalar | Core |
| **D_dev** | `D_{\text{dev}}` | Developmental Dopamine | Developmental initialization parameter in critical periods. | Concentration | Neuro/dev |
| **I_int** | `I_{\text{int}}` | Integrin Coefficient | Structural neural stability factor. | Scalar | Neuro |
| **S_c** | `S_c` | Cognitive Entropy | Resolution deficit of $\hat{G}$. | Entropy units | Core/neuro |
| **F_Bio** | `F_{\text{Bio}}` | Biological Transform Function | Species-specific mapping characteristics for $L_0 \to L_1$. | Function | Comparative neuro |
| **ΔR** | `\Delta R` | Reality Deviation | Magnitude of altered-state deviation from baseline. | Scalar | Clinical/spirituality |
| **C_int** | `C_{\text{int}}` | Integration Capacity | Capacity to integrate altered-state content. | Scalar | Clinical/spirituality |
| **T_immune** | `T_{\text{immune}}` | Immune Threshold | Immune-mediated sensory gating threshold. | Threshold | Neuroimmune |
| **M** | `M` | Modality Set | Weighted sensory modality vector. | Vector | Neuro |

## Usage Rules
1. Never use `G` (gravity constant) to refer to `\hat{G}` (Ghost Operator).
2. `L_0` is not "nothingness"; it is structured potentiality.
3. Use `\Psi_f` for ontological friction; reserve `\Phi` for IIT context only.
4. Use `\Omega` for consistency and `\Omega_{\text{mis}}` for mismatch to avoid symbol collision.

## D-Value Alignment (d 值专题规范)

### 1) 单一主定义（Canonical Definition）
**唯一主定义（必须优先引用）**
$d(x) \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|$
其中：
- $\mathcal{U}$：效用势（utility potential）
- $\mathcal{S}$：生存/不可逆风险坐标（survival / irreversible-risk coordinate）
*规范来源*：`SRT/AI/SRT_AI_01_Ontology.md`（Ax-ONT-3）

### 2) 局部近似语境 (Local Approximations)
| 表达式 | 所在语境 | 与主定义关系 |
| :--- | :--- | :--- |
| $d \approx \alpha A + \beta\log V + \gamma\tau$ | 认知-行为操作化 | 主定义在认知域的降维近似（投影），**不可单独当主定义** |
| $d_{quantum}, d_{bio}, d_{cosmic}$ | 跨尺度动力学 | 主定义经尺度映射 $\Pi_{scale}(d)$ 的实例化 |
| $d \propto A_{surface}/l_{Planck}^2$ | 全息对应 | 主定义的对偶几何表示 |

### 3) d 值编辑规则（避免冲突）
- **规则 R1**：不得将局部公式写成“d 的定义是 ……”（除非就是 canonical）。
- **规则 R2**：局部公式必须标注“近似 / 投影 / 操作化”。
- **规则 R3**：涉及跨文件引用时，优先回链到 Ax-ONT-3。
- **规则 R4**：任何“d→0 / d>0”的意识结论，需同时说明与 $\Psi_f$ 或不可逆风险边界的关系。
