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

The five checks mirror the EA-1..EA-5 criteria of the 2026-08-06 audit, minus
EA-1, which is a judgement about content and cannot be mechanized. The checker
therefore verifies the *carriers* of assimilation, not its substance; a green
result means "nothing structural is missing", not "the theory is good".
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

# A node may only be called effectively_assimilated when every carrier is present.
FULL_BAR = "effectively_assimilated"
MIN_REGRESSION_TESTS = 8

CSV_COLUMNS = [
    "node_id",
    "title",
    "assimilation_status",
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


def count_regression_tests(rel: str | None) -> int:
    if not rel:
        return 0
    text = read(rel)
    if not text:
        return 0
    return len(re.findall(r"^##\s+T-\d+", text, re.M))


def check_node(node: dict, bundles: dict[str, str]) -> dict:
    problems: list[str] = []
    status = node.get("assimilation_status", "")

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
    n_tests = count_regression_tests(node.get("regression_tests"))
    if node.get("regression_tests") and n_tests == 0:
        problems.append(f"regression test file has no `## T-NN` blocks: {node['regression_tests']}")

    # --- EA-4: old-formulation handling ---
    old_handled = node.get("old_text_handled") or ""
    old_ok = bool(old_handled) and old_handled != "n/a"

    if status == FULL_BAR:
        if not owners_ok:
            problems.append("claims effectively_assimilated without a resolvable active owner")
        if not (router_ok or deep_ok):
            problems.append("claims effectively_assimilated without a resolvable retrieval path")
        if not bundle_loaded:
            problems.append("claims effectively_assimilated but no context bundle loads it")
        if n_tests < MIN_REGRESSION_TESTS:
            problems.append(
                f"claims effectively_assimilated with {n_tests} regression tests "
                f"(minimum {MIN_REGRESSION_TESTS})"
            )
        if not old_ok:
            problems.append("claims effectively_assimilated without recording old-text handling")

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
        "assimilation_status": status,
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

    tally: dict[str, int] = {}
    for row in rows:
        tally[row["assimilation_status"]] = tally.get(row["assimilation_status"], 0) + 1

    print("== active theory assimilation ==")
    for row in rows:
        mark = "ok  " if not row["problems"] else "WARN"
        print(f"{mark} {row['node_id']:<28} {row['assimilation_status']:<26} tests={row['regression_tests_count']:<3} bundle={row['bundle_loaded']}")
        if row["problems"]:
            for problem in row["problems"].split(" | "):
                print(f"       - {problem}")

    print("\n-- status tally --")
    for status in manifest.get("status_enum", []):
        if tally.get(status):
            print(f"  {status}: {tally[status]}")

    assimilated = tally.get(FULL_BAR, 0)
    print(f"\nnodes: {len(rows)}  effectively_assimilated: {assimilated}")

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
