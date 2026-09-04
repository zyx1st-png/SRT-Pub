from pathlib import Path
import subprocess


def require_replace(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"anchor changed: {label}")
    return text.replace(old, new, 1)


# Reuse the already-reviewed Architecture-v2 bootstrap text from the pre-merge
# #890 history rather than regenerate it by hand.
content = subprocess.check_output(
    ["git", "show", "6164f0e9e04f13b7c459cfc9feeffd1c33f7a9a8:SRT_AI_START.md"],
    text=True,
)
Path("SRT_AI_START.md").write_text(content, encoding="utf-8")

# AGENTS: preserve the three-file session bootstrap but route theory advancement
# through Architecture v2 and the active Domain Framework template.
p = Path("AGENTS.md")
s = p.read_text(encoding="utf-8")
s = require_replace(
    s,
    """4. `Operations/Proposals/SRT_CONSTITUTION_DOMAIN_RECONSTRUCTION_BLUEPRINT_2026-08-29.md`
5. `Operations/Proposals/SRT_CONSTITUTION_DOMAIN_EXECUTION_PLAN_2026-08-29.md`
6. `Governance/SRT_GOV_CONSTITUTION_DOMAIN_RECONSTRUCTION_2026-08-29.md`
7. `Operations/Proposals/SRT_CONSTITUTION_SOURCE_RECOVERY_MAP_2026-08-29.md` when recovering existing SRT intuition rather than answering a narrow factual question.""",
    """4. `Operations/Proposals/SRT_CONSTITUTION_DOMAIN_ARCHITECTURE_V2_2026-09-04.md` — active post-Constitution architecture.
5. `Operations/Proposals/SRT_CONSTITUTION_DOMAIN_RECONSTRUCTION_BLUEPRINT_2026-08-29.md` — compact historical/identity blueprint.
6. `Operations/Proposals/SRT_CONSTITUTION_DOMAIN_EXECUTION_PLAN_2026-08-29.md` — execution plan as amended by Architecture v2.
7. `Operations/Templates/SRT_DOMAIN_RECONSTRUCTION_FRAMEWORK_TEMPLATE.md` for new/backfilled domain work.
8. `Governance/SRT_GOV_CONSTITUTION_DOMAIN_RECONSTRUCTION_2026-08-29.md`.
9. `Operations/Proposals/SRT_CONSTITUTION_SOURCE_RECOVERY_MAP_2026-08-29.md` when recovering existing SRT intuition rather than answering a narrow factual question.""",
    "AGENTS programme expansion",
)
s = require_replace(
    s,
    """SRT Constitution
= bearer-involved perspective framework

Domain research
= formalization / evidence / proof / testing layer""",
    """SRT Constitution
= bearer-involved perspective framework

Domain Reconstruction Framework
= Constitution × domain starting picture × inherited SRT assets × materials
  -> problem-space / objectification / bearer-position / problem families / deep-well queue

Domain Theory / Hypothesis / Model
= mechanisms / formalisms / proxies / candidate explanations

Deep Well / Evidence
= bounded test / strongest baseline / Case A-B-C / data / proof / archive""",
    "AGENTS identity guard",
)
p.write_text(s, encoding="utf-8")

# STATUS: bounded routing/status refresh only; canonical owner sections remain
# untouched.
p = Path("STATUS.md")
s = p.read_text(encoding="utf-8")
s = require_replace(s, "updated: 2026-08-29", "updated: 2026-09-04", "STATUS frontmatter date")
s = require_replace(s, "> **最后更新**：2026-08-29", "> **最后更新**：2026-09-04", "STATUS date")
s = require_replace(
    s,
    "> **当前作者级方向**：`Operations/Proposals/SRT_CONSTITUTION_DOMAIN_RECONSTRUCTION_BLUEPRINT_2026-08-29.md`",
    "> **当前作者级方向**：`Operations/Proposals/SRT_CONSTITUTION_DOMAIN_ARCHITECTURE_V2_2026-09-04.md`",
    "STATUS direction",
)
anchor = "> **当前执行计划**：`Operations/Proposals/SRT_CONSTITUTION_DOMAIN_EXECUTION_PLAN_2026-08-29.md`\n"
if anchor not in s:
    raise SystemExit("anchor changed: STATUS execution plan")
s = s.replace(
    anchor,
    anchor + "> **当前领域框架模板**：`Operations/Templates/SRT_DOMAIN_RECONSTRUCTION_FRAMEWORK_TEMPLATE.md`\n",
    1,
)
s = require_replace(
    s,
    "- **领域工作流**：`WHO participates? -> GIVEN ONE -> objectification/detachment -> SRT re-entry -> reorganization -> new problems -> domain test -> domain increment gate`。证明、数学、实验、统计、D2/D3 和 rival comparison 在 domain 侧支付。",
    "- **领域工作流（Architecture v2）**：`select domain -> Pre-framework Material Re-entry -> Domain Reconstruction Framework v0.1 -> author/scope lock -> one bounded deep well -> strongest-baseline / Case A-B-C -> productive adequacy -> Phase 9.5 framework writeback`。Framework 主要承担 Layer B 的领域重组，不因材料进入框架而自动获得 Layer C / Case C。",
    "STATUS domain workflow",
)
s = require_replace(
    s,
    "- **只挖一口深井**：Constitution v1 后先选一个领域做穿，不并行铺开 Physics/Biology/AI/Neuroscience/Consciousness/Social 等全套工作线。Consciousness/Neuroscience 是有积累的候选，但尚未被本状态页预选。",
    "- **单主井纪律继续有效**：Neuroscience 第一口井作为 grandfathered pilot 保留其 Case B / access-blocked / translation-only 等记录，并允许按具名条件后续重开；Epistemology 已被作者选为第二口主井，但在继续扩展前先补建其 Domain Reconstruction Framework。不得因新 Layer 2 而并行展开多个主 deep-well programme。",
    "STATUS single-well discipline",
)
first = "- 首读顺序唯一权威仍是 `AGENTS.md §Session Start`。\n"
amendment = "- **2026-09-04 Architecture v2 已落 main**：Constitution 与具体 deep well 之间新增 `Domain Reconstruction Framework`；Blueprint §6 仍为紧凑历史前身，新/回填领域工作统一使用 active framework template。\n"
if amendment not in s:
    if first not in s:
        raise SystemExit("anchor changed: STATUS Fast Status")
    s = s.replace(first, first + amendment, 1)
p.write_text(s, encoding="utf-8")
