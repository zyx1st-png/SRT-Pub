---
id: SRT-DEEP-NAV-TODO
type: operations_plan
tags: [Navigation, TODO, Deep Theory, Retrieval, Maintenance]
status: active_v1
layer: operations
epistemic_layer: meta
claim_mode: navigation
dependency: [_SRT_CONTEXT_ROUTER, _SRT_DEEP_THEORY_MAP, _SRT_INDEX]
---

# SRT Deep Navigation TODO Plan

> **Purpose**: This plan maintains deep-content navigation so that important SRT theory files are not lost during context retrieval. It is operational, not theoretical.

> **Operating principle**: Do not keep expanding theory before the navigation layer can reliably route existing theory.

---

## 0. Current Diagnosis

SRT already contains many deep theory files. The main risk is not lack of content, but **retrieval loss**:

- Deep concepts are distributed across canonical files, bridge files, equations, domain files, graphify outputs, papers, and operations logs.
- Existing indexes tell readers where entry surfaces are, but not always which files should be retrieved together for a recurring deep question.
- Adjacent-theory interfaces, `Ψ_f`, d-value, `L2`, AI consciousness, political philosophy, spirituality, and quantum measurement each require multi-file context.

Therefore the navigation layer now has three complementary files:

1. `_SRT_INDEX.md` — machine entry index and authority order.
2. `_SRT_CONTEXT_ROUTER.md` — query type → retrieval route.
3. `_SRT_DEEP_THEORY_MAP.md` — theory node → primary/support files.

---

## 1. Ongoing Maintenance Cadence

### Weekly / after each major theory edit

- Check whether new or edited files need route updates in `_SRT_CONTEXT_ROUTER.md`.
- Check whether new or edited files belong to a deep node in `_SRT_DEEP_THEORY_MAP.md`.
- Check whether `_SRT_INDEX.md` needs only an entrypoint update, not every file addition.

### After new canonical or bridge file

- Add to `_SRT_INDEX.md` only if it is an entry surface, canonical anchor, bridge hub, or domain hub.
- Add to `_SRT_CONTEXT_ROUTER.md` if it should be retrieved for common questions.
- Add to `_SRT_DEEP_THEORY_MAP.md` if it represents or supports a major theory node.
- Add a boundary note if it risks being mistaken for a core theorem.

### After major paper / longform update

- Identify which theory node the paper affects.
- Add it as support file unless it is the new primary canonical anchor.
- Avoid making papers outrank canonical files.

---

## 2. Priority Backlog

### P0 — Immediate routing stabilization

- [x] Add `_SRT_CONTEXT_ROUTER.md`.
- [x] Add `_SRT_DEEP_THEORY_MAP.md`.
- [x] Add `Bridge/SRT_Adjacent_Theory_Interface_Index.md`.
- [ ] Update `_SRT_INDEX.md` to include `_SRT_CONTEXT_ROUTER.md` and `_SRT_DEEP_THEORY_MAP.md` as meta navigation surfaces.
- [ ] Verify all routes in `_SRT_CONTEXT_ROUTER.md` point to existing files.
- [ ] Verify all deep nodes in `_SRT_DEEP_THEORY_MAP.md` point to existing files.

### P1 — Deep route quality pass

- [ ] Expand route for `Ψ_f` measurement / experimental proxies.
- [ ] Expand route for `L2` subject-status problem: sedimentation vs emergent operator.
- [ ] Expand route for `d-value` and consciousness conditions.
- [ ] Expand route for AI consciousness / non-binding friction.
- [ ] Expand route for political philosophy and rights.
- [ ] Expand route for spirituality / subject-position / return path.
- [ ] Add route for publication / paper preparation if needed.

### P2 — Cross-file consistency pass

- [ ] Search for direct `Ψ_f = Fisher` or `Ψ_f ≡ g_F` style residues outside warning contexts.
- [ ] Search for `d = D_eff` style residues outside proxy contexts.
- [ ] Search for `L2 = landscape` style residues outside projection contexts.
- [ ] Search for “FEP = SRT” or equivalent reduction language.
- [ ] Search for “IIT/GNW defines consciousness” style overclaims.
- [ ] Search for quantum-collapse reduction language.

### P3 — Human-facing navigation upgrade

- [ ] Update `SRT_Navigation_Map.md` with a “Deep Theory Routes” section.
- [ ] Add a short public-facing explanation of `_SRT_CONTEXT_ROUTER.md`.
- [ ] Add “If you are asking X, read Y first” table for human readers.
- [ ] Consider a bilingual summary table for Chinese readers.

### P4 — Graphify / generated wiki cleanup

- [ ] Identify graphify-out pages that duplicate canonical content but lack boundary notes.
- [ ] Add references from graphify-derived pages back to canonical files where feasible.
- [ ] Avoid treating graphify-out pages as primary canonical anchors.
- [ ] Consider a generated-output warning in `_SRT_INDEX.md` or `graphify-out/GRAPH_REPORT.md`.

---

## 3. Route Audit Checklist

For every route in `_SRT_CONTEXT_ROUTER.md`, verify:

- [ ] Does it have at least one canonical or primary anchor?
- [ ] Does it include the most relevant bridge file?
- [ ] Does it include domain implementation files only as secondary unless the question is domain-specific?
- [ ] Does it include a boundary note?
- [ ] Does it avoid promoting papers, graphify outputs, or operations logs over canonical files?

---

## 4. Deep Node Audit Checklist

For every node in `_SRT_DEEP_THEORY_MAP.md`, verify:

- [ ] Does the node answer a distinct conceptual question?
- [ ] Are primary files definition-bearing or high-authority?
- [ ] Are support files clearly secondary?
- [ ] Is the boundary note strong enough to prevent common misreadings?
- [ ] Does the node avoid repeating long theoretical content?

---

## 5. Suggested Next Editing Batches

### Batch A — Index integration

Goal: make new navigation files visible.

Files:

- `_SRT_INDEX.md`
- `SRT_Navigation_Map.md` if needed

Actions:

- Add `_SRT_CONTEXT_ROUTER.md` and `_SRT_DEEP_THEORY_MAP.md` to entry surfaces / meta navigation.
- Add `Operations/_SRT_DEEP_NAV_TODO.md` to operations section.
- Do not change theory content.

### Batch B — Route verification

Goal: prevent broken links or missing file references.

Actions:

- Check all file paths in `_SRT_CONTEXT_ROUTER.md`.
- Check all file paths in `_SRT_DEEP_THEORY_MAP.md`.
- Mark nonexistent references as TODO rather than inventing content.

### Batch C — Overclaim residue search

Goal: prevent context router from pointing to files with outdated strong claims.

Search targets:

```text
Ψ_f ≡ g_F
Ψ_f = Fisher
d = D_eff
L2 = landscape
SRT = FEP
SRT = IIT
SRT = quantum collapse
```

Actions:

- Only patch actual overclaims.
- Do not rewrite historical notes unless they are likely to be cited as current claims.

### Batch D — Human navigation upgrade

Goal: make deep routes usable by non-agent readers.

Actions:

- Add a small section to `SRT_Navigation_Map.md`:
  - “Deep question? Start with `_SRT_CONTEXT_ROUTER.md`.”
  - “Want theory overview? Start with `_SRT_DEEP_THEORY_MAP.md`.”

---

## 6. Done Criteria

The deep navigation layer is acceptable when:

1. A query about `Ψ_f`, d-value, Ghost Operator, `L0-L1-L2`, FEP, IIT/GNW, quantum measurement, social reality, AI consciousness, or political philosophy has a route.
2. Each route has primary files, secondary files, and a boundary note.
3. Each major theory node has a primary/support file split.
4. `_SRT_INDEX.md` exposes the router and map.
5. No router entry silently upgrades bridge files to canonical authority.

---

## 7. Non-Goals

This plan does not aim to:

- rewrite theory;
- merge all deep files;
- delete graphify outputs;
- turn all routes into canonical claims;
- replace `CANONICAL_REGISTRY.md`;
- replace `_SRT_INDEX.md`.

It only maintains retrieval quality and context continuity.

