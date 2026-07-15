---
id: SRT-TEMPLATE-SAFE-PATCH-PROMPT
type: template
tags: [Template, SafePatch, Codex, LongFile]
status: active_v1
claim_mode: prompt
canonical: false
date: 2026-07-15
usage: >
  给 Codex / Claude Code / 任意 agent 的大文件最小补丁 paste-ready 提示词。
  这是 Operations/Codex_Prompts/ 那类手写提示的可复用骨架——换掉 <尖括号> 即可。
---

# 大文件安全补丁 · Paste-ready 提示词模板

```
You are working in the zyx1st-png/SRT-Pub repository.

Goal: <一句话说明只加什么，例如：给这些长文件加 PH-SS 护栏指针与局部注记>.
Do MINIMAL targeted edits only. Do not rewrite full files. Do not delete or
reorder existing long sections. Do not promote companion files to canonical.

First verify repository and branch:
  git remote -v
  git branch --show-current
  git rev-parse HEAD
If not on zyx1st-png/SRT-Pub and the expected branch, stop and report the mismatch.

Context files to read first (report any missing, continue with the visible ones):
- <上下文/guardrail/index/execution-plan 文件清单>

Target files (patch if they exist; skip+report if missing; do not create replacements):
- <目标文件清单>

Required edits:
- <逐处：在哪个锚点之后、插入什么短块/注记；护栏措辞从 <哪份 canonical/guardrail 文档> 取，不自造>
- If a file already has similar guardrails, merge wording without duplication.

After editing:
  git diff -- <目标目录>
Confirm only targeted insertions/notes were made; no full-file rewrite, no deletions, no reordering.

Safety rules:
1. No full-file rewrites.  2. No deleting existing content.
3. Do not canonicalize companion files.  4. Do not change P0/P1 definitions.
5. Do not convert bridge claims into canonical.  6. No math changes except formula-role/guardrail notes.
7. Keep additions short, visible, grep-able.  8. Only mark TODO/status done if actually inserted.

Final response format:
  Patched files: ...
  Skipped files: ... (why)
  Key inserted guardrails: ...
  No full-file rewrites performed: yes/no
  Potential follow-up: ...
```
