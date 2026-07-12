---
id: SRT-BOOK-RETRIEVAL-GOVERNANCE-PASS-2026-07-12
type: governance_closure_report
status: implemented_in_pr
canonical: false
scope: book_retrieval_and_version_routing
created: 2026-07-12
claim_mode: operations_provenance
---

# Book Retrieval Governance Pass — 2026-07-12

## 1. Trigger

A conceptual book discussion retrieved highly relevant files from `Archive_52Chapter/` before the current `Drafts_26Q/` chapters were loaded. The archived material was then initially treated as if it represented the latest manuscript.

The direct execution error was failure to follow `AGENTS.md` and `_SRT_AGENT_RETRIEVAL_PROFILE.md` before keyword search. The incident also exposed engineering weaknesses:

- current state depended on addendum override chains;
- search ranking had no machine-readable currentness layer;
- the archive README still pointed to an obsolete 26-question planning stage;
- the book retrieval profile named an older architecture map before the current five-act map;
- CI checked manuscript presence but did not check active-vs-archive routing.

## 2. Governance decision

The repository now distinguishes three independent axes:

1. **authority** — whether a file can define SRT;
2. **retrieval value** — whether it is useful context;
3. **currentness** — whether it is the active construction source.

An archived file can have high retrieval value while having no current construction authority.

## 3. Implemented controls

### 3.1 Machine-readable currentness manifest

Added:

`01_Source_Intuition/BOOK/BOOK_ACTIVE_MANIFEST.json`

It records:

- the single construction entry;
- the active manuscript root;
- the current five-act structure map;
- archive roots;
- hard retrieval rules;
- concept-to-current-chapter routes.

### 3.2 Single-entry status consolidation

Updated `BOOK_CURRENT_STATUS.md` so that the current state is stated directly rather than requiring agents to resolve a stale freeze statement through an addendum chain.

It now states:

- the RC1 body freeze was lifted on 2026-07-02;
- the book is in the generative-philosophy strategic assembly round;
- canonical theory freeze remains unaffected;
- the current positioning is a generative-philosophy book using SRT as an engine, not an SRT manual.

### 3.3 Runtime hard guard

Updated `AGENTS.md` with a mandatory current-book-first route:

1. current status;
2. active manifest;
3. current `Drafts_26Q/` primary;
4. archive only for labelled historical comparison.

### 3.4 Retrieval profile hardening

Updated `_SRT_AGENT_RETRIEVAL_PROFILE.md` to separate authority, retrieval value, and currentness; prioritize the five-act map; and prohibit archive-first current-book answers or patches.

### 3.5 Archive demotion

Updated `Archive_52Chapter/README.md` with:

- `active_construction: false`;
- current replacement paths;
- explicit historical-only use;
- prohibition against using old drafts as current patch mothers.

### 3.6 CI enforcement

Extended `scripts/check_book_outline_split.py` so governance preflight verifies:

- the active manifest exists and is valid JSON;
- current root and five-act map are correct;
- archive roots are explicitly registered;
- required hard rules remain enabled;
- concept-route primaries resolve only under `Drafts_26Q/`;
- archive files are not promoted through concept routes;
- stale active freeze and old-positioning statements do not return to `BOOK_CURRENT_STATUS.md`;
- the archive README retains its demotion guards.

The existing `scripts/governance_preflight.py` already invokes this checker, so no parallel workflow was created.

## 4. Boundaries

This pass changes repository routing and governance only.

It does not:

- change SRT canonical definitions;
- rewrite book chapters;
- alter claim levels;
- delete historical material;
- prohibit historical comparison;
- assert that archived material has low intellectual value.

## 5. Remaining debt

The large root `_SRT_INDEX.md` still contains some stale book-description wording, including older act and architecture summaries. This pass does not rewrite that long mixed-domain index because the immediate failure path is now blocked by the single-authority `AGENTS.md`, the dedicated retrieval profile, the active manifest, and CI.

A later narrow index-synchronization pass should update only the book subsection and add `BOOK_ACTIVE_MANIFEST.json` to the machine routing table without disturbing unrelated domain entries.

## 6. Closure criterion

This pass is complete when the governance workflow confirms the updated book checker passes and a reviewer verifies that:

- a search hit under `Archive_52Chapter/` cannot be treated as current without violating an explicit runtime rule;
- the current chapter route is discoverable from a machine-readable file;
- the status file no longer requires an override chain to know whether body editing is active.
