#!/usr/bin/env python3
"""Check whether SRT theory nodes have actually reached the AI-active layer.

Motivation
----------
The existing checkers answer *provenance* and *engineering* questions: does the
SourceCard exist, is it in the Material Log, does the patch have a hook, does the
hook name a target. None of them answers the only question that matters for
theory: **would a fresh AI session, reading only the entry points the repository
declares, actually retrieve this content and judge differently because of it?**

This checker answers that, against a hand-maintained node manifest.

Design constraints
------------------
* Report-only by default (`Governance/Governance_Anti_Blocking_Gate.md`): a
  repository-wide historical debt must never make unrelated PRs fail.
* `--strict-node ID` escalates to exit 1 for nodes this PR claims to have
  assimilated. New work is held to the full bar; history is not.
* Stdlib only. CI runs `uv run python` without a project environment, so a
  third-party import would fail there and pass locally -- the worst failure mode.
* A hook, a patch, or a searchable file is **never** counted as assimilation.

Three axes, and the checker may only touch one of them
------------------------------------------------------
`structural_assimilation` (Axis A) asks how far an increment travelled through
the repository's structure. Statically checkable, and checked here.

`behavioral_availability` (Axis B) asks whether a fresh session was observed
retrieving this node and using it to judge. **Absolute** — never compared to a
baseline. Not statically checkable: a regression-test file proves a suite was
written, not that it was run. The checker refuses any value but `untested`
unless the manifest carries `behavior_evidence` pointing at a recorded run, and
never sets the axis itself.

`intervention_effect` (Axis C) asks what one specific PR added relative to its
own baseline. It lives per-intervention, not per-node.

Why B and C must not share a field: the 2026-08-07 run found a zero judgment
delta for PR #744, but *both* conditions retrieved and used the node correctly.
Collapsing that into one status would have recorded a working, retrieved,
correctly-applied theory node as behaviorally ineffective. A PR adding nothing
and a theory being unavailable are different facts.

`effectively_assimilated` is derived and is a claim about THE NODE only:

    structural_assimilation  == "active_complete"
    behavioral_availability  == "robustly_observed"
    behavior_observation_mode == "bounded"

Tightened 2026-08-08. `observed` alone no longer qualifies: the project's goal
is theory an AI can reach *fast* and act on, and an unconstrained 27-file dig
that eventually finds the answer does not demonstrate that. `observed` now
means only "at least one real run found and used it, by any route"; the final
label needs repeated bounded runs against a pre-frozen threshold.

EA-1 (is there a genuine native proposition?) is a judgement about content and
cannot be mechanized. The checker verifies the *carriers*, not the substance; a
green result means "nothing structural is missing", not "the theory is good".
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "Operations" / "Audits" / "data" / "srt_active_theory_nodes.json"
BUNDLE_DIR = ROOT / "Operations" / "Context_Bundles"

# Axis A value that means every structural carrier is present.
STRUCTURAL_BAR = "active_complete"
# Axis B values that assert something happened, so they require recorded evidence.
NEEDS_EVIDENCE = {"observed", "robustly_observed", "failed"}
AVAILABILITY_VALUES = {"untested", "observed", "robustly_observed", "failed", "not_applicable"}
# Only `robustly_observed` (and only when bounded) satisfies the final label.
AVAILABLE = {"robustly_observed"}
# `robustly_observed` is reserved for repeated BOUNDED runs.
BOUNDED_REQUIRED_FOR = "robustly_observed"
INTERVENTION_VALUES = {"untested", "none", "retrieval_efficiency_only",
                       "judgment_positive", "judgment_negative", "mixed"}
MIN_REGRESSION_TESTS = 8

CSV_COLUMNS = [
    "node_id",
    "title",
    "structural_assimilation",
    "behavioral_availability",
    "behavior_observation_mode",
    "effectively_assimilated",
    "interventions",
    "active_complete_blockers",
    "active_owners_ok",
    "compact_layer",
    "compact_ok",
    "router_anchor_ok",
    "deep_map_anchor_ok",
    "bundle_loaded",
    "regression_tests_count",
    "old_text_handled",
    "open_tension",
    "author_gates",
    "problems",
]


def load_manifest() -> dict:
    if not MANIFEST.is_file():
        sys.exit(f"manifest not found: {MANIFEST.relative_to(ROOT)}")
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def split_anchor(spec: str | None) -> tuple[str, str] | tuple[None, None]:
    """`path#anchor` -> (path, anchor). A bare path yields an empty anchor."""
    if not spec:
        return None, None
    if "#" in spec:
        path, anchor = spec.split("#", 1)
        return path, anchor
    return spec, ""


def heading_exists(text: str, anchor: str) -> bool:
    """Anchors here are section numbers (`23a`, `19a`, `14`), not slugs.

    Slug matching would be fragile against CJK headings, so we look for a
    Markdown heading whose number matches exactly. `14` must not match `14a`
    or `140`, hence the trailing boundary.
    """
    if not anchor:
        return True
    pattern = rf"^#{{1,4}}\s+{re.escape(anchor)}(?![0-9a-zA-Z])"
    return re.search(pattern, text, re.M) is not None


def bundle_files() -> dict[str, str]:
    if not BUNDLE_DIR.is_dir():
        return {}
    return {p.name: p.read_text(encoding="utf-8", errors="ignore") for p in BUNDLE_DIR.glob("*.md")}


def regression_suites(node: dict) -> list[str]:
    """A node may carry several suites (e.g. an in-distribution one plus an
    out-of-distribution transfer set). Accept both a string and a list."""
    value = node.get("regression_tests")
    if not value:
        return []
    return [value] if isinstance(value, str) else list(value)


def count_regression_tests(rels: list[str]) -> tuple[int, list[str]]:
    """Returns (total probe/test items, suites that exist but declare none).

    Two shapes count, because two shapes are legitimately in use:

    * a written suite, one `## T-NN` block per item;
    * a run record, where the items live in a scoring table -- these declare
      `suite_items: N` in frontmatter.

    `suite_items` is an author declaration, not a derived number. It is
    auditable by reading the file, and it exists so that a real 24-observation
    probe record is not rejected for lacking headings it never needed. It is
    not a way to claim a suite that does not exist: the file must still be
    present, and the run record itself is what any reviewer checks.
    """
    total = 0
    empty: list[str] = []
    for rel in rels:
        text = read(rel)
        if not text:
            empty.append(f"{rel} (missing)")
            continue
        n = len(re.findall(r"^##\s+T-\d+", text, re.M))
        if n == 0:
            declared = re.search(r"^suite_items:\s*(\d+)\s*$", text, re.M)
            n = int(declared.group(1)) if declared else 0
        if n == 0:
            empty.append(rel)
        total += n
    return total, empty


def check_node(node: dict, bundles: dict[str, str]) -> dict:
    problems: list[str] = []
    state = node.get("structural_assimilation", "")
    validation = node.get("behavioral_availability", "untested")
    evidence = node.get("behavior_evidence") or ""
    mode = node.get("behavior_observation_mode") or ""

    if validation not in AVAILABILITY_VALUES:
        problems.append(f"behavioral_availability not in the allowed set: {validation!r}")

    # `robustly_observed` is the only value that carries a reliability claim, so
    # it is the only one gated on bounded retrieval. Without this, an
    # unconstrained 27-file deep dive could be recorded as a fast-layer result.
    if validation == BOUNDED_REQUIRED_FOR and mode != "bounded":
        problems.append(
            f"behavioral_availability={validation} requires behavior_observation_mode=bounded "
            f"(got {mode!r}); see SRT_BOUNDED_RETRIEVAL_PROTOCOL_2026-08-08.md"
        )

    for entry in node.get("interventions") or []:
        effect = entry.get("intervention_effect")
        if effect not in INTERVENTION_VALUES:
            problems.append(f"intervention_effect not in the allowed set: {effect!r}")
        if not entry.get("ref"):
            problems.append("intervention record without a `ref` to its run record")
        elif not (ROOT / str(entry["ref"]).split("#", 1)[0]).is_file():
            problems.append(f"intervention ref points at a missing file: {entry['ref']}")

    # The load-bearing rule of this whole pass. A written suite is not a result.
    if validation in NEEDS_EVIDENCE:
        if not evidence:
            problems.append(
                f"behavioral_availability={validation} without behavior_evidence; "
                "a regression-test file existing is not a recorded run"
            )
        elif not (ROOT / evidence.split("#", 1)[0]).is_file():
            problems.append(f"behavior_evidence points at a missing file: {evidence}")

    # --- EA-2: does every declared active owner exist? ---
    owners = node.get("active_owners") or []
    missing_owners = [o for o in owners if not (ROOT / o).is_file()]
    if missing_owners:
        problems.append("missing active owner: " + ", ".join(missing_owners))
    owners_ok = bool(owners) and not missing_owners
    if not owners:
        problems.append("no active owner declared")

    # --- compact / fast layer ---
    compact = node.get("compact_layer")
    compact_ok = bool(compact) and (ROOT / compact).is_file()
    if compact and not compact_ok:
        problems.append(f"compact layer not found: {compact}")

    # --- EA-3: is there a retrieval path that actually resolves? ---
    def anchor_ok(spec: str | None, must_mention: list[str]) -> bool:
        path, anchor = split_anchor(spec)
        if not path:
            return False
        text = read(path)
        if not text:
            problems.append(f"routing file not found: {path}")
            return False
        if not heading_exists(text, anchor or ""):
            problems.append(f"anchor not found: {spec}")
            return False
        # An anchor that does not name any owner or the compact layer is a
        # heading, not a route. This is the check that distinguishes "the file
        # is mentioned somewhere" from "the AI is sent there".
        if must_mention and not any(m and m in text for m in must_mention):
            problems.append(f"route {spec} names none of the node's files")
            return False
        return True

    targets = [*(owners or []), compact or ""]
    router_ok = anchor_ok(node.get("router_anchor"), targets)
    deep_ok = anchor_ok(node.get("deep_map_anchor"), targets)

    # --- context bundle membership ---
    declared_bundle = bool(node.get("bundle"))
    needle = compact or (owners[0] if owners else "")
    bundle_loaded = bool(needle) and any(needle in text for text in bundles.values())

    # --- EA-5: behavior regression tests ---
    suites = regression_suites(node)
    n_tests, empty_suites = count_regression_tests(suites)
    for rel in empty_suites:
        problems.append(f"regression suite declares no items (no `## T-NN` blocks, no `suite_items:`): {rel}")

    # --- EA-4: old-formulation handling ---
    # `n/a` is ambiguous between "assessed, nothing was superseded" and "nobody
    # looked", so it does not count. A node with no superseded formulation must
    # say so explicitly with `none-required: <reason>`.
    old_handled = node.get("old_text_handled") or ""
    old_ok = bool(old_handled) and old_handled != "n/a"

    if state == STRUCTURAL_BAR:
        if not owners_ok:
            problems.append("claims active_complete without a resolvable active owner (EA-2)")
        if not (router_ok or deep_ok):
            problems.append("claims active_complete without a resolvable retrieval path (EA-3)")
        if not bundle_loaded:
            problems.append("claims active_complete but no default load path reads it (EA-4)")
        if not old_ok:
            problems.append("claims active_complete without recording old-text handling (EA-5)")
        if node.get("active_complete_blockers"):
            problems.append("claims active_complete while listing active_complete_blockers")
    elif not node.get("active_complete_blockers"):
        # A node below the bar must say what is holding it there, otherwise the
        # manifest degrades into unexplained pessimism and nobody can act on it.
        problems.append(f"structural_assimilation={state} with no active_complete_blockers recorded")

    # A behavior suite is required before Axis B can ever leave `untested`, but
    # its size is an Axis B concern, not an Axis A one -- so this is checked
    # against the validation claim, not against active_complete.
    if validation in NEEDS_EVIDENCE and n_tests < MIN_REGRESSION_TESTS:
        problems.append(
            f"behavioral_availability={validation} with only {n_tests} regression tests "
            f"(minimum {MIN_REGRESSION_TESTS})"
        )

    derived = (
        state == STRUCTURAL_BAR
        and validation in AVAILABLE
        and mode == "bounded"
    )

    if declared_bundle and not bundle_loaded:
        problems.append("manifest says bundle: true but no generated bundle contains the node")

    # Open tensions are pointers into a real section; a dangling one silently
    # turns "registered exposure" into "nobody can find the exposure".
    tension = node.get("open_tension")
    if tension:
        tpath, tanchor = split_anchor(tension)
        ttext = read(tpath or "")
        if not ttext or not heading_exists(ttext, tanchor or ""):
            problems.append(f"open tension anchor not found: {tension}")

    return {
        "node_id": node.get("node_id", ""),
        "title": node.get("title", ""),
        "structural_assimilation": state,
        "behavioral_availability": validation,
        "behavior_observation_mode": mode,
        "effectively_assimilated": "yes" if derived else "no",
        "interventions": "; ".join(
            f"{e.get('intervention', '?')}={e.get('intervention_effect', '?')}"
            for e in (node.get("interventions") or [])
        ),
        "active_complete_blockers": " | ".join(node.get("active_complete_blockers") or []),
        "active_owners_ok": "yes" if owners_ok else "no",
        "compact_layer": compact or "",
        "compact_ok": "yes" if compact_ok else ("n/a" if not compact else "no"),
        "router_anchor_ok": "yes" if router_ok else "no",
        "deep_map_anchor_ok": "yes" if deep_ok else "no",
        "bundle_loaded": "yes" if bundle_loaded else "no",
        "regression_tests_count": n_tests,
        "old_text_handled": "yes" if old_ok else "no",
        "open_tension": tension or "",
        "author_gates": "; ".join(node.get("author_gates") or []),
        "problems": " | ".join(problems),
    }


# --------------------------------------------------------------------------
# Reachability survey
# --------------------------------------------------------------------------
# The node manifest is hand-maintained and therefore partial. This survey is the
# unbiased complement: it takes *every* theory-carrying file outside the owner
# layer and asks whether any file on the active retrieval surface names it. It
# answers "how much of the repository is invisible by default" without anyone
# having to curate a list first.

# Files a fresh session plausibly reads by default, per `AGENTS.md §Session
# Start` plus the routing layer those files point into.
SURFACE_FIXED = [
    "SRT_AI_START.md",
    "_SRT_AGENT_RETRIEVAL_PROFILE.md",
    "STATUS.md",
    "_SRT_CONTEXT_ROUTER.md",
    "_SRT_DEEP_THEORY_MAP.md",
    "_SRT_INDEX.md",
    "CANONICAL_REGISTRY.md",
    "_SRT_CROSS_DOMAIN_MATRIX.md",
    "Core/SRT_OPEN_TENSIONS.md",
    "03_Bridges/BRIDGE_INDEX.md",
    "Bridge/SRT_Adjacent_Theory_Interface_Index.md",
]
SURFACE_GLOBS = ["*/README.md", "*/*_COMPACT_REGISTRY.md", "*/_*MACHINE_INDEX.md"]

# Theory-carrying files that are *not* themselves owners: bridges, patches,
# operations protocols, source intuition, evidence cards. Navigation files are
# excluded because being an index is not the same as carrying theory.
CANDIDATE_GLOBS = [
    "03_Bridges/*.md",
    "Bridge/*.md",
    "*/patches/*.md",
    "Operations/SRT_*.md",
    "01_Source_Intuition/*.md",
    "01_Source_Intuition/Conversations/*.md",
    "04_External_Convergence/*/*.md",
]
CANDIDATE_EXCLUDE = {"README.md", "BRIDGE_INDEX.md", "BRIDGE_TEMPLATE.md", "INDEX.md"}


def reachability_survey() -> dict:
    surface = [f for f in SURFACE_FIXED if (ROOT / f).is_file()]
    for pattern in SURFACE_GLOBS:
        surface += [str(p.relative_to(ROOT)) for p in ROOT.glob(pattern)]
    surface += [
        str(p.relative_to(ROOT))
        for p in ROOT.rglob("*CompactCore*.md")
        if ".git" not in str(p) and "Context_Bundles" not in str(p)
    ]
    surface = sorted(set(surface))
    blob = "".join(read(f) for f in surface)

    candidates: list[str] = []
    for pattern in CANDIDATE_GLOBS:
        candidates += [str(p.relative_to(ROOT)) for p in ROOT.glob(pattern)]
    candidates = sorted({c for c in candidates if Path(c).name not in CANDIDATE_EXCLUDE})

    unreferenced = [c for c in candidates if Path(c).name not in blob and c not in blob]
    return {
        "surface": surface,
        "candidates": candidates,
        "unreferenced": unreferenced,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--reachability",
        action="store_true",
        help="Also run the unbiased reachability survey (theory-carrying files no active-surface file names).",
    )
    parser.add_argument(
        "--strict-node",
        action="append",
        default=[],
        metavar="NODE_ID",
        help="Exit nonzero if this node has problems. Repeatable. Use for nodes the current PR claims to have assimilated.",
    )
    parser.add_argument(
        "--strict-all",
        action="store_true",
        help="Exit nonzero on any problem. Not for CI while historical debt exists.",
    )
    parser.add_argument("--csv", metavar="PATH", help="Write the machine-readable table here.")
    args = parser.parse_args()

    manifest = load_manifest()
    bundles = bundle_files()
    if not bundles:
        print("NOTE: no generated context bundles found; bundle_loaded will be 'no' for every node.")

    rows = [check_node(node, bundles) for node in manifest.get("nodes", [])]

    axis_a: dict[str, int] = {}
    axis_b: dict[str, int] = {}
    for row in rows:
        axis_a[row["structural_assimilation"]] = axis_a.get(row["structural_assimilation"], 0) + 1
        axis_b[row["behavioral_availability"]] = axis_b.get(row["behavioral_availability"], 0) + 1

    print("== active theory assimilation ==")
    print("   (A = structural, checked here. B = behavioral availability, absolute, never set here.)")
    print("   (C = per-PR intervention effect, recorded per node in `interventions`.)\n")
    for row in rows:
        mark = "ok  " if not row["problems"] else "WARN"
        print(
            f"{mark} {row['node_id']:<28} A={row['structural_assimilation']:<22} "
            f"B={row['behavioral_availability']:<18} tests={row['regression_tests_count']:<3} "
            f"bundle={row['bundle_loaded']}"
        )
        if row["problems"]:
            for problem in row["problems"].split(" | "):
                print(f"       - {problem}")

    axes = manifest.get("axes", {})
    print("\n-- Axis A: structural_assimilation --")
    for value in axes.get("structural_assimilation", {}).get("values", sorted(axis_a)):
        if axis_a.get(value):
            print(f"  {value}: {axis_a[value]}")
    print("\n-- Axis B: behavioral_availability --")
    for value in axes.get("behavioral_availability", {}).get("values", sorted(axis_b)):
        if axis_b.get(value):
            print(f"  {value}: {axis_b[value]}")

    structural = axis_a.get(STRUCTURAL_BAR, 0)
    derived = sum(1 for r in rows if r["effectively_assimilated"] == "yes")
    untested_complete = sum(
        1 for r in rows
        if r["structural_assimilation"] == STRUCTURAL_BAR and r["behavioral_availability"] == "untested"
    )
    print(
        f"\nnodes: {len(rows)}  active_complete: {structural}  "
        f"of which behavior-untested: {untested_complete}  "
        f"effectively_assimilated (derived): {derived}"
    )
    if derived == 0 and structural:
        print("  note: structural completeness is not availability; no node has a recorded run yet.")

    if args.reachability:
        survey = reachability_survey()
        n_surface = len(survey["surface"])
        n_cand = len(survey["candidates"])
        n_unref = len(survey["unreferenced"])
        pct = (100.0 * n_unref / n_cand) if n_cand else 0.0
        print("\n-- reachability survey --")
        print(f"  active-surface files scanned: {n_surface}")
        print(f"  theory-carrying candidates:   {n_cand}")
        print(f"  named by no surface file:     {n_unref}  ({pct:.1f}%)")
        for rel in survey["unreferenced"]:
            print(f"    - {rel}")

    if args.csv:
        out = Path(args.csv)
        if not out.is_absolute():
            out = ROOT / out
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS)
            writer.writeheader()
            writer.writerows(rows)
        print(f"wrote {out.relative_to(ROOT)}")

    failing = [r for r in rows if r["problems"]]
    strict_ids = set(args.strict_node)
    strict_failures = [r for r in failing if args.strict_all or r["node_id"] in strict_ids]

    unknown = strict_ids - {r["node_id"] for r in rows}
    if unknown:
        print(f"\nFAIL: --strict-node names unknown node(s): {', '.join(sorted(unknown))}")
        sys.exit(1)

    if strict_failures:
        print(f"\nFAIL: {len(strict_failures)} strict node(s) have problems.")
        sys.exit(1)

    if failing:
        print(f"\nreport-only: {len(failing)} node(s) have problems; not failing the build.")
    print("PASS")


if __name__ == "__main__":
    main()
