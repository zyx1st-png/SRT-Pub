# Assembly & global review report — MANUSCRIPT.md

> **CURRENT STATUS (2026-08-18).** Sections 1–7 remain the original 2026-07-17/19
> assembly and audit record. The self-citation live-status item in §8 is now resolved:
> **Costly Selective Closure** is recorded as submitted to *Adaptive Behavior*, and the
> former Frontiers manuscript `1837760` is the published Zhang (2026) article,
> *Frontiers in Neuroscience* 20:1837760, DOI `10.3389/fnins.2026.1837760`.
> `manuscript/08_references.md`, `REFERENCE_LEDGER.md`, `PAPER_CHARTER.md`, the
> candidate bibliography, and the assembled `MANUSCRIPT.md` have been synchronized.
>
> **Previous current-status note (2026-07-19).** Sections 1–3 below are the *original*
> 2026-07-17 assembly report and are retained as history. Superseding updates since
> then: **(a)** the manuscript carries a full bibliography — `manuscript/08_references.md`
> (16 VERIFIED references + 2 self-citations), inserted and novelty-downgraded in
> commit `33e97207`; §4 "TODO — references" below is therefore **DONE**. **(b)** The
> assembled `MANUSCRIPT.md` is 1121 lines, ~10.0k words (the "969 lines" figure in §1
> is historical). **(c)** Figure 5 four-vector panels and the S4 two-point extraction
> are complete (§5, already marked COMPLETED).

Date: 2026-07-17. Scope: mechanical assembly of manuscript/00–07 into
`manuscript/MANUSCRIPT.md` (by `assemble_manuscript.py`) plus a global consistency
review. **No new experiments, no theory extension, no large-scale language polish,
no unverified references added.**

## 1. What assembly did (all mechanical, reproducible by re-running the script)

- **Order & numbering:** Abstract → 1 Introduction → 2 Methods (2.1–2.10 from
  M1–M10) → 3 Results (3.1–3.5 from R1–R5) → 4 Audit (4.1–4.4, was 8.x) →
  5 Discussion (5.1–5.3, was 9.x) → 6 Limitations (was 10) → Figures & captions
  as back matter. 969 lines, ~8.7k words.
- **Cross-references fixed:** all internal refs renumbered (Section 8/9/10 →
  4/5/6; Methods M4 → 2.4; R1–R5 → 3.1–3.5, incl. two line-break-split
  occurrences caught on verification). Post-fix scan for stale refs: **zero**.
- **Figure citations inserted** (insertions only, no wording changes): all 13
  panels now cited in body text — 1A (Methods 2.4), 1B (3.1), 2 (3.1),
  3A (3.2), 3B/3C (3.3), 4A (Methods 2.7), 4B (3.4), 5A/5B (3.4),
  S1/S3 (3.2), S2 (3.4).
- **Draft-note blockquotes stripped** from every section (verified: none remain);
  one provenance note kept at the top of the assembled file.

## 2. Ledger sweep (CLAIM_LEDGER)

Automated scan for forbidden-claim vocabulary (prove/proven, refute, supersede,
impossible, consciousness, subjecthood, independence-claims):

- 4 hits, **all compliant**: one process sentence ("v2 manifests supersede v1" —
  provenance, not a theory claim), one negation ("make no claim that these
  frameworks are wrong or superseded"), two disavowals inside 5.3 and 6.9
  (listing what is *not* claimed).
- "To our knowledge" qualifier present on the single exclusivity claim (5.2).
- Downgraded items ([pipeline validation]) are labeled at every occurrence
  (3.3, 3.4, 4.3, S2 caption, Fig 4 caption).
- Independence-claim guard: no "statistically independent" assertion anywhere;
  dissociation language used throughout.

## 3. Methods–Results–Figures closure

- **Number closure: PASS.** Every numeric value appearing in the assembled
  manuscript was checked against `RESULTS_NUMBERS.md` (generated read-only from
  the frozen JSONs): **0 manuscript numbers missing from the extraction file**
  (43-key automated check incl. all primaries, direction gates, equivalence
  bounds, costs, permutation, sham, washout values).
- **Methods↔Results mapping:** 2.3↔3.1 (S1), 2.5↔3.2 (S2/2b), 2.6↔3.3 (S3/2c),
  2.7↔3.4 (S4); every control promised in Methods is reported in Results
  (washout curves, permutation, consolidation-null, memory-swap, sham,
  decoupling checks) and every reported result has a Methods procedure.
- **Figures:** every panel cited (see §1); every caption's numbers match
  RESULTS_NUMBERS; deferred panels (Fig 5 four-bar vectors; S4 erosion trace)
  are declared in captions and FIGURE_PLAN, not silently absent.

## 4. TODO — references — **DONE (commit `33e97207`, 2026-07-19; status refreshed 2026-08-18)**

**Resolution:** `manuscript/08_references.md` supplies the bibliography — 16 VERIFIED
references plus two self-citations. Citations were inserted with an integrated
novelty-downgrade so the information measure, its use as a signal, and gated
consolidation are each attributed to prior art (Methods 2.4 / Intro §1 / Discussion
§5.2); the residual novelty is scoped to the combination only. Three rounds of
literature verification are complete (see `LITERATURE_VERIFICATION_REPORT.md`).

The original citation-needed checklist is retained as history; every item is covered:

1. §1/§5.2 framework anchors: dynamical systems & hysteresis; optimal control /
   controllability; RL habit formation & metaplasticity; FEP / active inference;
   predictive processing.
2. §2.4/§5.2 self-citations: Costly Selective Closure and the executive-friction
   Frontiers paper. **Current status is governed by the 2026-08-18 sync above.**
3. §2 methodological anchors: master-yoked control design; equivalence testing;
   percentile bootstrap; committor / Kramers escape; Euler–Maruyama.
4. §5.2 possibly IIT if named at review (currently not named in body).

## 5. TODO — pre-submission statistical extraction — **COMPLETED 2026-07-17**
(single authorized deterministic extraction round; see `STATISTICAL_RECHECK.md`)

1. ~~Per-class four-bar arrival vectors~~ → extracted (role-aligned; Fig 5 A–C).
2. ~~S4 latent-erosion~~ → realized as a two-point comparison (full per-step trace
   not extractable without editing frozen code; documented).
3. ~~Per-seed summary tables~~ → `STATS_TABLES.md` T3a (2c, 40 seeds) and T4b
   (tiny-MDP, 50 seeds). Phase 2b per-seed values not stored in its frozen JSON
   and not re-derived (outside the authorized round).
4. ~~Unified statistics script~~ → `build_stats_tables.py` → `STATS_TABLES.md`.
5. ~~2c re-bootstrap decision~~ → resolved: seed-clustered robustness re-bootstrap
   run (ctrl 0.570, 90% CI [0.566, 0.574]; |PE| 0.087 [0.084, 0.089]); direction
   unchanged; frozen pooled result stands, re-check cited as robustness support.

Reproduction check: all 10 frozen primaries reproduced bit-identically; STOP rule
not triggered; manuscript body numbers unchanged.

## 6. TODO — formatting / venue (not content)

- Venue selection; word-count fit (~8.7k body); equation typesetting (equations
  are ASCII blocks); symbol style unification for print (Delta_min vs Δ_min,
  eps_TV vs ε_TV — currently mixed ASCII/Unicode between body and figures);
  figure font/size polish; data/code availability statement (repo is private —
  needs a release decision for the frozen `Experiments/anchoring_*` dirs and the
  sealed archive tag).
- Journal-format conversion (the assembled file is Markdown).

## 7. Known residual imperfections (accepted, not blocking)

- Body uses ASCII math (W_sel, Delta_min); figures use Unicode (Δ_min). Cosmetic;
  deferred to formatting pass.
- Fig 1B "1.000" bar label grazes the axis top; Fig 4A formation-box text is
  tight. Cosmetic; deferred to figure polish.
- The Abstract is 323 words — may need trimming to venue limits.

## 8. Open author-review items

- **Self-citation live status — RESOLVED 2026-08-18.** Source-of-truth bibliography,
  ledgers and assembled mirror now record CSC as submitted to *Adaptive Behavior* and
  Zhang (2026) as published in *Frontiers in Neuroscience* 20:1837760, DOI
  `10.3389/fnins.2026.1837760`.
- **Methods 2.6 wording — RESOLVED (branch-sync pass, 2026-07-19).** The duplicate
  "seed × volatility cells as separate resampling units" sentence was deduped; both
  interval roles remain preserved.
- **Symbol/format unification and venue** remain as in §6–§7 (deferred, not content).
