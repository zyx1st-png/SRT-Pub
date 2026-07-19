---
id: SRT-AGENT-CONTEXT-RETRIEVAL-AUDIT-2026-05-10
type: audit_report
tags: [AgentContext, Retrieval, ConnectorSafety, BookWriting, Governance]
status: active_v1
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
created: 2026-05-10
dependency: [_SRT_AGENT_RETRIEVAL_PROFILE, SRT-LARGE-FILE-AUDIT-2026-05-09, SRT-LONGFORM-SPLITS]
---

# Agent Context Retrieval Audit 2026-05-10

> Purpose: evaluate why external agents may retrieve too little from the SRT repository, especially when the repo is used through Codex, ChatGPT, Claude Code, or GitHub-style connectors for theory advancement and book writing.
>
> This is an Operations audit. It does not create theory definitions.

---

## 0. Executive Judgment

The user's concern is substantively correct.

The repository contains a large amount of valuable context, but the current agent-facing bootstrap can cause under-retrieval because authority controls, connector safety controls, and task routing controls are partly conflated.

The main failure mode:

```text
canonical:false / split / bridge / operations / backstage
→ correctly treated as not authoritative
→ incorrectly skipped as low-value context
```

The fix is not to weaken canonical discipline. The fix is to separate:

1. definition authority;
2. retrieval priority;
3. task profile;
4. connector-safe reading path.

This audit creates and registers `_SRT_AGENT_RETRIEVAL_PROFILE.md` as the agent-facing contract for that separation.

---

## 1. Evidence Observed

Repository scale at audit time:

- total files: about `1501`;
- markdown files: about `1258`;
- files carrying `canonical: false`: about `334`;
- compact-core files: about `18`;
- longform split registry exists: `LONGFORM_SPLITS.md`;
- large-file audit exists: `Operations/Archive_Records/Large_File_Audit_2026-05-09.md`.

The current bootstrap path before this patch emphasized:

1. `SRT_AI_START.md`
2. `STATUS.md`
3. `_SRT_INDEX.md`
4. `_SRT_SYMBOL_TABLE.md`

This is safe for avoiding overclaiming, but too narrow for theory development and book writing.

Existing repository evidence already admits connector risk:

- `Operations/Archive_Records/Large_File_Audit_2026-05-09.md` flags many active text files as warning/action/urgent size.
- `LONGFORM_SPLITS.md` provides split paths for long owner files.
- `STATUS.md` itself is connector-sensitive and has `STATUS_Split/README.md`.

Existing navigation evidence already admits missed-context risk:

- `_SRT_CONTEXT_ROUTER.md` routes deep questions to multiple primary and secondary files.
- `_SRT_DEEP_THEORY_MAP.md` maps theory nodes beyond folder structure.
- `_SRT_*_COVERAGE_INDEX.md` files exist specifically to recover unreferenced or under-routed material.

Book-writing evidence:

- `01_Source_Intuition/BOOK/` and `90_Backstage/Restructure_2026/BOOK_PROJECT/` contain current manuscript state, inclusion matrices, style notes, and consistency passes.
- These files are non-canonical by design but high retrieval value for writing.

---

## 2. Diagnosed Problems

| Problem | Effect | Fix |
|---|---|---|
| Authority and retrieval are conflated | Agents skip useful non-canonical files | Add `_SRT_AGENT_RETRIEVAL_PROFILE.md` |
| Default agent bootstrap is too skeletal for real work | Answers lean on canonical skeleton and miss domain/book context | Add retrieval profile to AGENTS, Claude, README, START_HERE, `_SRT_INDEX` |
| `_SRT_CONTEXT_ROUTER.md` was framed as deep-only | Medium-depth questions may never route | Reframe it for any non-simple SRT question |
| Split files are marked non-authoritative | Connectors may avoid them and then truncate owner files | State split files are connector-safe copies with high retrieval value |
| Book-writing materials are backstage | Codex/Claude may miss current chapter state and inclusion decisions | Add book-writing profile pointing to `01_Source_Intuition/BOOK/` and `90_Backstage/.../BOOK_PROJECT/` |
| Coverage indexes are follow-up only | Valuable underreferenced files stay dormant | Reclassify as missed-context recovery for relevant task profiles |
| No future frontmatter distinction | New files may continue overloading `canonical` | Propose `authority_level` and `retrieval_priority` fields |

---

## 3. Applied Fixes

Created:

- `_SRT_AGENT_RETRIEVAL_PROFILE.md`

Updated:

- `AGENTS.md`
- `SRT_AI_START.md`
- `_SRT_INDEX.md`
- `_SRT_CONTEXT_ROUTER.md`
- `CLAUDE.md`
- `START_HERE.md`
- `README.md`
- `Operations/README.md`
- `Governance/README.md`

The new profile defines task modes:

1. quick orientation;
2. theory advancement;
3. book writing;
4. source-intuition / philosophical prose;
5. domain deep dive;
6. material fusion;
7. public release / external onboarding;
8. governance / repository engineering.

It also introduces the core rule:

```text
canonical:false means not definition authority.
It does not mean do not retrieve.
```

---

## 4. New Operational Rule

For substantial SRT work, agents should follow this sequence:

1. Read the minimal bootstrap.
2. Read `_SRT_AGENT_RETRIEVAL_PROFILE.md`.
3. Classify the task profile.
4. Load canonical authority anchors.
5. Load high-value non-canonical context for the task.
6. Use `_SRT_CONTEXT_ROUTER.md` for non-simple theory/domain questions.
7. Use `LONGFORM_SPLITS.md` for long files.
8. Mark whether each cited file is canonical, bridge, support, evidence, backstage writing context, or operations provenance.

---

## 5. Recommended Next Passes

### 5.1 Frontmatter Normalization

Future metadata pass should add optional fields to high-value non-canonical files:

```yaml
authority_level: bridge_support
retrieval_priority:
  theory_advancement: high
  book_writing: medium
  public_release: low
```

This is not required for current operation because the new profile gives inference rules.

### 5.2 Book Writing Index

Create or strengthen:

- `01_Source_Intuition/BOOK/BOOK_CURRENT_STATUS.md`
- `01_Source_Intuition/BOOK/Outline_Parts/README.md`
- a root-level `BOOK_CONTEXT.md` only if book work becomes the dominant external-agent workflow.

### 5.3 Router Expansion

Add explicit routes in `_SRT_CONTEXT_ROUTER.md` for:

- book writing;
- source-intuition writing;
- public release;
- external convergence;
- rights / political philosophy if not already covered deeply enough;
- book-chapter continuity.

### 5.4 Connector Regression Check

Run a periodic check that asks:

1. Which files are large and unsplit?
2. Which high-value files have no router path?
3. Which book/backstage files are current but not reachable from agent bootstrap?
4. Which coverage index entries should be promoted to router routes?

---

## 6. Residual Risk

This patch improves agent behavior through instructions and routing. It does not guarantee that every external tool will honor those instructions.

To maximize compliance when using external systems:

- pin `AGENTS.md`;
- pin `SRT_AI_START.md`;
- pin `_SRT_AGENT_RETRIEVAL_PROFILE.md`;
- explicitly ask the agent to classify the task profile before answering;
- for book work, explicitly name the target chapter or book pass.

---

## 7. Closure

The repository's canonical discipline should remain strict.

The retrieval layer should now be more generous.

Valuable non-canonical content should be treated as:

```text
not authoritative, but often essential.
```
