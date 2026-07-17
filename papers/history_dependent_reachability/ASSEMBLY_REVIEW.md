# Assembly & global review report — MANUSCRIPT.md

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

## 4. TODO — references (none fabricated; to be added and verified pre-submission)

The manuscript currently has **no bibliography**. Citation-needed points:

1. §1/§5.2 framework anchors: dynamical systems & hysteresis; optimal control /
   controllability; RL habit formation & metaplasticity; FEP / active inference;
   predictive processing.
2. §2.4/§5.2 self-citations once identifiers exist: Costly Selective Closure
   (Adaptive Behavior submission) and ontological friction Ψ_f (Frontiers ms
   1837760) — cite as manuscripts; do not overstate status.
3. §2 methodological anchors: master-yoked control design (learned-helplessness
   tradition); equivalence testing (TOST-style); percentile bootstrap; committor /
   Kramers escape (S1 functionals); Euler–Maruyama.
4. §5.2 possibly IIT if named at review (currently not named in body — decide
   whether to keep it unnamed).

## 5. TODO — pre-submission statistical extraction (no new experiments; frozen-JSON
reads plus at most one authorized deterministic re-run)

1. Per-class four-bar arrival vectors [P(G0),P(G1),P(G2),P(∅)] for the planned
   Fig 5 panel (raw vectors not stored in frozen JSON).
2. S4 latent-erosion trace (episode-end z is in the aggregate; end-of-observation
   z is not).
3. Per-seed summary tables for all primary metrics (supplementary).
4. Unified statistics script reading only frozen JSONs, emitting every CI in the
   paper from one source.
5. Decision item: optional per-seed (volatility-averaged) re-bootstrap of Phase 2c
   as a robustness footnote — would require an authorized analysis run; currently
   disclosed as limitation instead.

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
