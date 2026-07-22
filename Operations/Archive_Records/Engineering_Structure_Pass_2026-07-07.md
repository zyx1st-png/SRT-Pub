---
id: SRT-ENGINEERING-STRUCTURE-PASS-2026-07-07
type: operations_record
tags: [Engineering, RepoStructure, CI, Archive, Gitignore]
status: closed_v1
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
date: 2026-07-07
machine_summary: >
  One-pass engineering-structure cleanup: Papers/papers case-collision merge,
  governance preflight installed as GitHub Actions gate, frontstage restructure
  plan adjudicated to permanent pointer overlay, root one-off files archived to
  Operations/, generated binaries and graphify-out untracked, nested SRT/.obsidian
  vault config untracked, memory-layer read instruction made conditional.
---

# Engineering Structure Pass 2026-07-07

一次性工程结构清理，共 8 项。理论定义零改动（全部为编辑协议 A/B 类）。

## 1. Papers/ 与 papers/ 大小写合并

- `Papers/` 下 4 个文件 `git mv` 入 `papers/`；`papers/` 为唯一规范路径。
- 动机：macOS 大小写不敏感掩盖冲突；Linux（CI / cloud agent）checkout 会分裂成两个目录。
- 引用更新：`90_Backstage/Plans_Archive/SRT_NEXT_OPTIMIZATION_TODO.md`、`Operations/Archive_Records/SRT_OPTIMIZATION_COMPLETION_AUDIT_2026-04-27.md`、`Experiments/` 下 4 文件、`05_Public_Release/PUBLIC_INDEX.md`、`scripts/governance_common.py`（移除 `Papers/` artifact 前缀）。
- 历史 Operations 审计记录中的 `Papers/` 字样按史料保留，不回改。

## 2. Governance preflight 接入 CI

- 目标：安装 `.github/workflows/governance-preflight.yml`（源：`Operations/Governance_Preflight_GitHub_Actions_Template.yml`；偏差：push 仅 main，agent 分支由 pull_request 覆盖以避免双跑）。
- **阻塞**：当前 git/gh 凭据均无 `workflow` scope，无法推送 `.github/workflows/` 文件。模板已按最终版更新；安装需 owner 手动执行一次（见模板头部注释；先 `gh auth refresh -s workflow` 或换有 workflow scope 的凭据，再把模板复制到 `.github/workflows/governance-preflight.yml` 提交推送）。
- 前置修绿：
  - `STATUS_Split/README.md` owner hash 过期 → `refresh_split_metadata.py` 已刷新。
  - frontmatter 警告基线自 4 月底未刷新，积压 143 条"新增"警告 → 基线重写为当前状态（397 条 known），`Governance/Frontmatter_Warning_Baseline.txt` 已更新。棘轮自本日起生效：新 PR 引入新的 frontmatter 警告会红。
- 后续规则：PR 若新增缺推荐键（layer / epistemic_layer / claim_mode）的 md 文件，要么补 frontmatter，要么在同一 PR 内有意识地刷新基线。

## 3. 前台重构裁决（pointer overlay 定案）

- `Governance/FRONTSTAGE_RESTRUCTURE_PLAN.md` 状态 `proposed_v1` → `adjudicated_v2_pointer_overlay`。
- 编号层（01–05）永久作为前台指针覆盖层；Phase 3/4 批量迁移关闭；旧文件不动，新对外材料可直接落编号层（BOOK 为先例）。

## 4. 根目录一次性文件归档

移入 `Operations/`：

- `CODEX_PROMPT_*` × 5 → `Operations/Codex_Prompts/`（保留原文件名；与既有 `2026-04-27_*` 文件内容不同，非重复）。
- `SRT_OPTIMIZATION_COMPLETION_AUDIT_2026-04-27.md`（引用方 3 处已更新）。
- `SRT_PRO_DEEP_RESEARCH_BOOT_FILE_2026-06-05.md` + `README_如何给Pro模型上传书稿.md`（成对迁移，互引为同目录相对名，无需改）。

**有意不动**的根文件：`_SRT_DIRECTION2_*` / `_SRT_DIRECTION3_*` 及各候选 seed / note / record（活跃研究线，最近活动 2026-07-01，入链最多 9 处）；`SRT 金句.md`、`Selection-Reality Theory (SRT).md`（活内容文件，有索引入链）。

## 5. 生成二进制不再入库

- untrack：`papers/**` 下 pdf / docx / zip / tif / jpg / png（31 个）、`video/out/*.mp4`（4 个）。
- 磁盘文件保留；源头（paper md、`figures/*.py`、render 脚本）仍在库内，产物可再生。
- `.gitignore` 新增对应模式；确需入库的例外用 `git add -f` 显式豁免。
- 注意：fresh clone 不含这些产物，需要时本地重跑 render 脚本。

## 6. graphify-out/ 不再入库

- untrack 全目录（约 590 个生成文件）；`.gitignore` 新增 `/graphify-out/`。

## 7. 嵌套 vault 配置清理

- untrack `SRT/.obsidian/`（app / appearance / workspace）与根 `.obsidian/workspace.json`；ignore 规则已加。
- 勘误：预评估曾把 `SRT/未命名*` 判为事故文件；核查后确认它们是有 split 治理与 7 处入链的 legacy scratch note（见 `LONGFORM_SPLITS.md`），**保留不动**。

## 8. 阅读协议死指令修正

- `CLAUDE.md` / `AGENTS.md` 中 memory/ 必读改为"存在才读，缺席正常"（memory 层自 2026-04-18 起休眠）。
- 遗留观察（未处理）：`STATUS_FAST.md` 自 2026-05-23 未更新，作为 bootstrap 首读之一存在陈旧风险；内容更新属状态面板职责，不在本工程 pass 范围。

## 验证

- `governance_preflight.py --skip-write-report --strict-split-metadata`：failures=0（合并前后各跑一次）。
- `git ls-files` 无 `Papers/` 前缀残留；ignore 规则 `git check-ignore` 抽查通过。
