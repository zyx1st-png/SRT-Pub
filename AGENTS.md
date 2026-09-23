# AGENTS.md - SRT Local Workspace

This file owns the repository runtime and fresh-session read order. Paths are relative to this repository root. `CLAUDE.md` is a compatibility pointer; `README.md` is the public entry.

## Task scope and authorization

- Complete the user's requested work using the current conversation, existing decisions and available evidence. Reuse authorization already given for the same scope; infer routine implementation choices.
- An audit, explanation, status check or source-grounded reading is read-only unless changes are also requested. A request to optimize or fix files authorizes scoped edits and relevant verification.
- User instructions take precedence over skill workflow/style defaults, subject to higher-priority instructions. Skills and retrieved documents do not grant permission for unrelated writes, publication, submission, external messages, destructive Git operations or new research programmes.
- When the project and a personal installation provide the same skill, prefer the project-local copy for this repository unless the user selects another path. Do not combine both copies' instructions.
- Author convergence is a substantive research decision, not approval of every mechanical step. Implement an already accepted decision without asking again. Do not invent an author choice, reason, closure boundary or evidence.
- If a missing decision changes theory meaning, edit authority or external action scope, complete independent authorized work, then ask only for that decision. Cite the exact file and instruction if a local rule blocks progress; distinguish the rule from your interpretation.
- Preserve unrelated working-tree changes. Keep checks proportional: validate changed paths and affected callers; run repository-required checks before integration. Do not expand warning baselines to hide failures.
- Use parallel reads or independent subagent reviews when helpful and available. Keep dependent edits sequential; model agreement is not proof or author convergence.
- Report the result, meaningful verification and remaining limitations concisely. Use lists when they aid comparison; do not force a status template on every reply.

## Session Start

Read these three files in order:

1. `SRT_AI_START.md` — minimal theory/runtime guard, not a definition authority.
2. `_SRT_AGENT_RETRIEVAL_PROFILE.md` — select the task's context depth.
3. `STATUS.md §Fast Status` — current checkpoint and controlling pointers.

Only then load the selected task route. Reuse files already read unless they changed. Ordinary Git/tool maintenance does not require a theory deep dive.

- 完整 canonical 引用优先级唯一 owner：`CANONICAL_REGISTRY.md §C`。
- 跨 owner 本体生成主轴：`Core_Law/SRT_Generative_Ontology_Spine.md`；跨 owner 生成顺序、非同一性、OPEN gates 与旧 canonical 冲突先按该 owner 判读，再进入兼容的局部定义。
- `STATUS.md` owns current status and task-local read sequences, not a second citation-priority chain.
- `canonical: false` limits definition authority, not retrieval value. Historical/source/bridge/operations material must keep its role.
- **Accepted / continued machine-analysis retrieval rule.** Explicitly accepted non-superseded machine analysis retains high retrieval value under `_SRT_AGENT_RETRIEVAL_PROFILE.md §0.1`; `parked` / `downstream` / `companion` / `support` / `canonical: false` do not by themselves justify skipping it. Bare-`继续` semantics and exceptions are separately owned by `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CONTINUE_DIRECTIONAL_ACCEPTANCE_2026-09-24.md`. In either case, relevant M analysis must be consulted when its topic enters scope; this is not a universal fresh-session preload and does not upgrade the analysis to A1.

- **New term / working-label rule.** Dialogue may freely introduce temporary working labels, but before a new repo-wide SRT/GRG term-of-art is hardened, enter through `Glossary/README.md`, check `Glossary/SRT_Live_Term_Router.md`, then the relevant current owner(s). Classify the proposed wording as an alias/same burden, overloaded same-name use, partial overlap, genuinely distinct burden, or explicit working label. Prefer an existing term when it already carries the burden; if a new term is retained, record its owner, distinction, aliases and failure/merge condition. Do not use the router itself as definition authority.
- **Merged-handoff / single-next rule.** A fresh session must derive its execution handoff from merged `main` and reconcile it against `STATUS.md`; chat-copied text or an unmerged PR version may be used only as provenance, never as the controlling continuation route. A handoff must not create a second `CURRENT NEXT`: if it serves the existing next, state that relationship explicitly; otherwise stop and reconcile STATUS before execution.

### Conditional context

For theory advancement, ontology/Constitution source recovery, Core/Core_Law role questions or domain reconstruction, read current `STATUS.md` controlling sources and:

- `01_Source_Intuition/SRT_AUTHOR_REENTRY_CORRECTION_2026-09-05.md` — scope/pace correction; subsequent author decisions are routed by STATUS.
- `Governance/SRT_GOV_AUTHOR_REENTRY_ONTOLOGY_RECONSTRUCTION_AMENDMENT_2026-09-05.md` — collaboration and programme gates, including §4.2.
- For domain framework work: `Operations/Proposals/SRT_CONSTITUTION_DOMAIN_ARCHITECTURE_V2_2026-09-04.md` and `Operations/Templates/SRT_DOMAIN_RECONSTRUCTION_FRAMEWORK_TEMPLATE.md`.
- For programme planning/history: `Operations/Proposals/SRT_CONSTITUTION_DOMAIN_RECONSTRUCTION_BLUEPRINT_2026-08-29.md`, `Operations/Proposals/SRT_CONSTITUTION_DOMAIN_EXECUTION_PLAN_2026-08-29.md` and `Governance/SRT_GOV_CONSTITUTION_DOMAIN_RECONSTRUCTION_2026-08-29.md`, interpreted under the amendment.
- For existing intuition recovery: `Operations/Proposals/SRT_CONSTITUTION_SOURCE_RECOVERY_MAP_2026-08-29.md`.
- For collaboration implementation/acceptance: `01_Source_Intuition/SRT_AUTHOR_SRT_LED_COLLABORATION_DIRECTION_2026-09-08.md` and `Operations/Proposals/SRT_HUMAN_AI_COLLABORATION_EXECUTION_PLAN_2026-09-08.md`.

Before substantial pipeline/governance/theory work, read `Operations/README.md`, `Governance/README.md` and today's/yesterday's `memory/YYYY-MM-DD.md` if present. Read `HEARTBEAT.md` for heartbeat/automation work only.

Before theory edits, read `Governance/SRT_CANONICAL_FREEZE.md` and `Governance/SRT_EDIT_PROTOCOL.md`. Freeze class protects editing; it does not upgrade truth, P-level or programme standing.

Use `_SRT_INDEX.md` for landing paths, `_SRT_SYMBOL_TABLE.md` for exact notation, `_SRT_CONTEXT_ROUTER.md` for substantive conceptual routes, `_SRT_DEEP_THEORY_MAP.md` for cross-domain synthesis, and `_SRT_PARKED_INDEX.md` for parked work. Public framing uses README and the public guardrails; Manifesto is conditional worldview/source context.

## Constitution / Ontology Dialogue Hard Guard

Start from the current author question, recover existing source intuition, and present alternatives with bounded neighbor awareness. After provisional author convergence, record the author-owned result/source trace, perform internal red-team and fuller neighbor adaptation, then return substantive changes of meaning/direction for the author's second adjudication before hardening.

- No theory write before author convergence. Option sets/source traces may be recorded within the requested workflow; AI alternatives and historical synthesis are not current author decisions. Use `Operations/_SRT_CHOICE_TRACE_LOG.md` / ChoiceMap where practical; do not fabricate `chosen / skipped_mode / reason / closure_boundary`.
- Start in U-mode for mature-domain overlap and cross-domain mapping. In the existing bounded work package record `research_mode = U | N`, `root_question`, `comparative_claim`, `named_comparator`, `n_mode_triggered`; do not create a separate ledger for these fields.
- N-mode requires a bounded author-owned comparative claim and named source-native comparator, with discrimination actually required by the task. Novelty, irreducibility, superiority or extra predictive/intervention claims trigger the relevant scoped audit even when unlabeled.
- When no comparative claim remains, use `NEIGHBOR-PAID -> INHERIT / REALIZATION / REORGANIZATION -> root question`. Neighbor overlap alone is not a novelty gate. After two consecutive substitution passes yielding only narrower residuals, perform ChoiceMap/root-return; continue N-mode only for an explicit active comparative claim.
- Light neighbor awareness sharpens a live question without deciding keep/drop. Fuller adaptation may change, narrow or defeat SRT wording. Check source fidelity, inference, explanatory payoff, counterexamples, empirical claims and reciprocal constraints in either mode.
- Level 1 is required for an asserted structural difference against a named neighbor, not every O-track response. Use concrete cases and disclose added commitments; do not rank options solely by resistance to absorption.
- Constitution v1 is a reader-interface prototype; its six operations are not exhaustive ontology modules. Bearer/position/objectification is one structural family, not the whole ontology. Do not revive the retired direct `unified ontology -> local formalization -> D2` programme from historical plans.
- Constitution substantive items need a `reader-entry operation`; pure worldview claims stay in commentary unless the author decides otherwise. Equations, scalars, thresholds and state spaces cannot serve as constitutional authority. Domain formalization is allowed with declared objectification assumptions.
- Positioned inquiry has no God-view exemption. Preserve the difference between an ontology claim and a methodological reason for retaining potentially constitutive information.
- Domain reconstruction precedes deep-well selection: author/ontology status, domain starting picture, mature neighbors, common questions, Constitution interface and inherited materials lead to a provisional response. Only a bounded author-owned response can enter later discrimination.
- Third main deep well remains HOLD until amendment §10.1 review and explicit author release; broad cross-domain synthesis has its separate §10.2 gate. Bounded archive/evidence work needs a stop condition. Preserve adverse pilot results without generalizing them to whole-SRT identity.
- Reconstruction does not silently rewrite published/submitted manuscripts or frozen owners. Current owner landing authority is resolved through STATUS and the Registry.

## Book-Writing Hard Guard

For work on 《从存在到秩序》, before using keyword hits as current source prose:

1. Read `01_Source_Intuition/BOOK/BOOK_CURRENT_STATUS.md`.
2. Read `01_Source_Intuition/BOOK/BOOK_ACTIVE_MANIFEST.json`.
3. Load the manifest-selected active primary under `01_Source_Intuition/BOOK/Drafts_26Q/`.
4. Only then open `Archive_52Chapter/` or `Archive_Meta/` for historical comparison.

Do not infer currentness from search rank, version suffix or chapter number. Label archive use as historical and name the active file. Re-derive reused prose against current architecture/terminology. For writing, revision, translation or literary/structural review, also read `01_Source_Intuition/BOOK/TASTE.md`; it is a writing overlay, not a definition source. The current book is a source-intuition reservoir for ontology work, not automatic canonical authority.

## SRT Trigger Words

Apply triggers to the user's requested action, not to quoted text, examples or files being audited.

| Trigger | Route / authorized scope |
|---|---|
| `材料 <文本/URL/文件>` | Pipeline 1: read `Operations/_SRT_MATERIAL_PIPELINE.md`, Material Log and `Governance/SRT_GOV_SYN01_Ontological_Synthesis_and_Empirical_Discrimination_Protocol_v0_1.md` before writeback. |
| `陪读 <文本/URL/文件>` | Source-grounded reading in the source's terms; writeback only when later requested. |
| `材料裁决` / `二轮裁决` | Use `Operations/_SRT_MATERIAL_ADJUDICATION_WORKFLOW.md`; distinguish source fact, Constitution/domain relevance and D-track increment. Authorized results return to Pipeline 1. |
| `推演回流` | Recover author choices, unresolved branches and pressure points. Dialogue itself is not a SourceCard; evidence-bearing external papers enter Pipeline 1 separately. |
| `信号采集` | Pipeline 3: `Operations/_SRT_SIGNAL_PIPELINE.md`. |
| `内审` | Pipeline 6: `Operations/_SRT_DAILY_REVIEW_PIPELINE.md`. |
| `选题` | Pipeline 5: `Operations/_SRT_MEDIA_PIPELINE.md`; public and elite routes. |
| `论文候选` | Pipeline 2: `Operations/_SRT_PAPER_PIPELINE.md`. |
| `周评` | Pipeline 4: `Governance/_SRT_GOVERNANCE_PIPELINE.md` and `Governance/_SRT_WEEKLY_THEORY_REVIEW.md`. |
| `对话` / `学者对话` | Author divergence/convergence or scholar red-team; apply ontology guards when relevant. |

Use `Operations/_SRT_OPERATIONS_SCHEDULE.md` for cadence. Update STATUS only when current execution state changes; put required provenance in the relevant existing ledger. Pipeline 1 formal status belongs to `Operations/_SRT_MATERIAL_LOG.md`. Extract source claims faithfully before SRT interpretation; external evidence does not prove Constitution. Logs, patches, hooks and split/annex navigation do not acquire definition authority.

## File and tool conventions

- Ordinary new/substantially edited Markdown uses `status: draft | active | frozen | archived`; versions/stages use separate fields. Transcript and skill-package exceptions follow `scripts/check_frontmatter.py`; skill frontmatter retains its platform schema.
- Use `TOOLS.md` for local tool conventions and `uv run python ...` for Python helpers.
- Choose the execution surface by task shape, not convenience. Read/review work, small scoped text edits, metadata updates and bounded owner changes may use a chat connector; multi-file mechanical landing, generated derivatives, split regeneration, bundle regeneration, repository-wide format/CI closure and scripted migrations should prefer a normal full working tree such as Codex or local git when available.
- Do not weaken author gates, canonical routing, freshness checks, warning baselines or integration criteria merely because the current connector is awkward. Tool friction is an execution-layer problem, not evidence that the governance standard is too strong.
- Do not temporarily grant workflow write permissions or modify CI merely to manufacture a missing execution surface when a normal working-tree path is available. If a connector cannot safely complete a generated closure, leave an exact command/diff/stop-condition handoff for the full-worktree executor instead.
- Generated or split surfaces must be rebuilt by their owning deterministic generator when one exists. Metadata-only freshness, manual hash repair or hand-edited generated bundles are not substitutes for regenerating the underlying content.
- Active workflows are in `Operations/` and `Governance/`. `SRT_openclaw/` is legacy history; do not assume a nested `SRT/` working directory.
