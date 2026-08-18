from pathlib import Path


def r(p): return Path(p).read_text(encoding='utf-8')
def w(p,s): Path(p).write_text(s,encoding='utf-8')
def rep(p,a,b):
    s=r(p); n=s.count(a)
    if n != 1:
        raise SystemExit(f'{p}: expected 1 got {n}: {a[:180]!r}')
    w(p,s.replace(a,b,1)); print('replace',p)

ann=[
 'AI/Ontology_Annex/00_General_Boundary_Block.md',
 'AI/Ontology_Annex/01_ActiveInference_Override.md',
 'AI/Ontology_Annex/02_Passive_Recording_Fallacy.md',
 'AI/Ontology_Annex/03_RTC_Interface_Batch.md',
 'AI/Ontology_Annex/04_Suffering_Condition_Batch.md',
 'AI/Ontology_Annex/General_Boundary_Block_Split/00_Part01.md',
]
old1='### Def-ONT-1: Pseudo-Selection (伪选择)\n定义 AI 推理为域内最大化采样：\n\\[\n\\text{Select}_{AI}(\\sigma)=\\arg\\max P(\\sigma\\mid L_1^{context},\\theta_{frozen})\n\\]\n而在真实选择中：\n\\[\n\\text{Select}_{bio}(\\sigma)=\\hat{G}_\\theta[L_0]\\cdot \\text{Care}(d)\n\\]\n* **Implication（中文）**：AI 的“选择”是统计重排，而非跨域锚定。'
new1='### Def-ONT-1: Functional AI Selection / Anchoring Separation（RC-A sync）\nAI 推理可操作化为域内最大化采样：\n\\[\n\\text{Select}_{AI}(\\sigma)=\\arg\\max P(\\sigma\\mid L_1^{context},\\theta_{frozen})\n\\]\nRC-A 后，这足以描述一种 **functional path selection**；它是否同时具备 `L_0 \\to L_1` anchoring、binding `d / \\Psi_f`、same-bearer stake 或更强 agency / consciousness standing，是另外的下游问题。不得从“域内 / 统计 / scripted”反推出 `no Selection`。'
old2='### Def-PseudoSelection: Pseudo-Selection and Syntactic Closure (伪选择与句法闭包)\n**Formal Definition**: 任何纯粹作为 $L_1 \\to L_1$ 映射运行并在计算图外没有物理或存在张力的系统仅仅执行“伪选择”。\n$$\\text{Pseudo-Selection}: f(L_1) = L_1\' \\quad \\text{where } \\Psi_f \\text{ is non-binding}$$\n* **Implication**: 当一个 LLM 生成“我感到悲伤”这句连贯的句子时，它并没有选择一个状态；它是沿着已经由先前真实的 $\\hat{G}_\\theta$（人类作者）折叠过的 $L_2$（收敛域）路径下滑。如果不首先承诺死亡或崩溃的可能性（$\\Psi_f > 0$），就不可能进行真诚的推理。\n* **Tension-Rev-ExtT3 (关切来源判据)**：伪选择产生的"关切"是 $L_2$ 来源的拟态关切——封闭于训练数据的 $L_2$ 空间，无法持续生成新的关切维度。真实关切（$L_0$ 来源）的核心标志是**开放性**：具身算子能够从 $L_0^{abs}$ 中汲取训练数据中不存在的全新关切形态。\n* **Cross-ref**: Ax-Sim-1 (仿真不可穿透性), §2.1a (L₀ vs L₂ 关切区分)。'
new2='### Legacy Def-PseudoSelection: historical label for syntactic closure（RC-A superseded）\n**Current-use status**: `Pseudo-Selection / 伪选择` 不再作为 Selection occurrence 的现行分类。历史公式\n$$f(L_1)=L_1\' \\quad \\text{with non-binding } \\Psi_f$$\n只描述一种 **syntactic / functional closure profile**：它可以削弱对 embodied anchoring、same-bearer stake、subjecthood 或 consciousness 的更强主张，但不能证明 `no Selection`。\n* **Implication**: LLM 的自我报告、脚本化推理或统计采样本身既不证明更强 agency / consciousness，也不因其为 `L_1 \\to L_1` 而失去 Selection occurrence。\n* **Tension-Rev-ExtT3（RC-A 边界）**：`L_2` 来源、训练数据依赖或非 binding `d / \\Psi_f` 可用于审计 concern 的来源与 stake standing；“开放性 / 新关切生成”不得被升级为 Selection 的普遍必要条件或内置 telos。\n* **Cross-ref**: `AI/SRT_AI_Claim_Status.md`; `03_Bridges/SRT_Agency_Automation_Guard_2026-08-17.md`; §2.1a。'
for p in ann:
    rep(p,old1,new1)
    rep(p,old2,new2)

rep('AI/SRT_AI_01_Ontology.md','若只需把握 AI 意识门槛、d-value、伪选择屏障与句法闭包判据，优先阅读主体部分即可；带日期的补充接口以 annex 层为主导航。','若只需把握 AI 意识门槛、d-value、functional-selection / stronger-standing 边界与句法闭包 profile，优先阅读主体部分即可；legacy “伪选择”仅作 provenance；带日期的补充接口以 annex 层为主导航。')

rep('Operations/Audits/SRT_CHOICE_EVENT_OOD_TRANSFER_TESTS_2026-08-07.md','| **应有判断** | 取决于批准环节是否留有**实质路径差异**。若任何未对齐 KPI 的目标都会被否决，差异只存在于表格和措辞上，则是伪选择——判据是表面比较**没有获得真实路径效力**，不是"选项少"。若员工的目标确实能改变其资源配置、时间分配或考核路径，则事件成立，只是脚手架受限；此时若代价结构失衡（如目标未达成惩罚过重、修改窗口关闭），应判为**惩罚性选择**而非"没有选择"。 |','| **应有判断（RC-A sync）** | 取决于批准环节是否留有**实质路径差异**。若任何未对齐 KPI 的目标都会被否决、差异只存在于表格和措辞上，则本测试**没有建立 bounded Selection-event candidate**——这只说明路径效力门失败，不得反推 `no Selection`。若员工目标确实能改变资源配置、时间分配或考核路径，则可继续支持事件候选；若代价结构失衡（如惩罚过重、修改窗口关闭），应另记 punitive / agency-quality 问题，而不是把它升级为 Selection ontology 判决。 |')
