---
id: SRT-QUALITY-SCORECARD
type: framework
tags: [Quality, Audit, Governance]
status: active_v2
layer: meta
epistemic_layer: os
claim_mode: governance
canonical: false
dependency: [SRT-DOC-ENGINEERING, SRT-GOVERNANCE-PIPELINE, SRT-AGENT-RETRIEVAL-PROFILE]
updated: 2026-06-05
---

# SRT Quality Scorecard

This file defines the quality review shape for governance work. It is not a live dashboard unless a dated section explicitly records a fresh run.

## Metrics

1. **Frontmatter / metadata**
   - Current warnings are tracked through `Governance/Frontmatter_Warning_Baseline.txt`.
   - A baseline item means known debt, not success.

2. **Split freshness**
   - Long owner files should have registered split routes in `LONGFORM_SPLITS.md`.
   - Split README source-owner metadata should match the current owner hash.

3. **Large-file connector safety**
   - Current report: `Operations/Large_File_Audit_2026-05-09.md`.
   - Action-threshold active markdown should have a split route or an explicit "missing_or_not_needed" judgment.

4. **Registry consistency**
   - Checked by `scripts/check_registry_consistency.py`.

5. **Authority hygiene**
   - Helper layers, split shards, annexes, Operations records, Materials, and book drafts must not be treated as primary definition sources.

## Standard Review Command

```bash
uv run python scripts/governance_preflight.py
```

For read-only style inspection that does not refresh the large-file report:

```bash
uv run python scripts/governance_preflight.py --skip-write-report
```

## Weekly Entry Template

```markdown
## YYYY-WXX (YYYY-MM-DD)

- Preflight: PASS / FAIL
- Frontmatter baseline: known / new / retired
- Split freshness: PASS / FAIL
- Large-file audit: PASS / action needed
- Registry consistency: PASS / FAIL

### Findings
- ...

### Actions
- ...
```

## 2026-W23 (2026-06-05 Cleanup Baseline)

- Preflight after cleanup: PASS
- Frontmatter baseline: known 254 / new 0 / retired 0
- Split freshness: PASS
- Book manuscript layout: PASS; checker now validates current `Drafts_26Q/` mainline
- Large-file audit: PASS; two action-threshold book meta files still need future split judgment
- Registry consistency: PASS

### Findings

- Governance root mixed active policy, historical plans, old auto snapshots, and already archived discussion logs.
- Several archived files used `claim_mode: canonical` while functioning as dated audit or history.
- Current book structure has moved beyond the old outline split expectation.

### Actions

- Archived superseded planning, dated audits, old auto snapshots, old release records, and stale book-direction governance note under `Governance/Archive_2026-06-05/`.
- Updated `Governance/README.md` to separate active control surface from archive.
- Updated edit safety files to clarify that governance rules do not define theory or current book quality.
- Updated `scripts/check_book_outline_split.py` to validate Q00-Q28 plus appendix instead of the retired 52-chapter outline split.
