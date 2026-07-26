#!/usr/bin/env python3
"""Tests for `build_srt_context_bundles.py`.

These assert the *substance* of the extracted guardrails, not merely that some
regex still fires. Two review findings motivate that distinction:

- G1 once carried a hand-written "the only unconditional claim is `if τ<∞`
  then not a stable ISP", which dropped the audit's S1/pathwise qualifier and
  reintroduced exactly the semantic promotion the audit warns against.
- G3 once summarised all three `partial` hooks as blocked on `T_dir`, when the
  source table shows two on `T_dir` and one on `Occlusion_Dynamics`.

Both were shaped correctly enough to pass an anchor-exists check, so the tests
below pin counts, grouping, and the presence of the limiting clause.

Run: `uv run python scripts/test_build_context_bundles.py`
"""

from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_srt_context_bundles as B  # noqa: E402

FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    if not condition:
        FAILURES.append(f"{label}{': ' + detail if detail else ''}")


# --------------------------------------------------------------------------
# G3 — grouping must come from the table, not a hand-written summary
# --------------------------------------------------------------------------

def test_hook_grouping() -> None:
    rows, groups = B.parse_open_hooks()

    check("G3 row count", len(rows) == 6, f"got {len(rows)}")
    check("G3 group count", len(groups) == 3, f"got {sorted(groups)}")

    by_target = {k: sorted(v) for k, v in groups.items()}
    t_dir = [k for k in by_target if "T_dir" in k]
    occl = [k for k in by_target if "Occlusion_Dynamics" in k]
    planned = [k for k in by_target if "planned target" in k]

    check("G3 has a T_dir group", len(t_dir) == 1, f"got {t_dir}")
    check("G3 has an Occlusion_Dynamics group", len(occl) == 1, f"got {occl}")
    check("G3 has a planned-target group", len(planned) == 1, f"got {planned}")
    if not (t_dir and occl and planned):
        return

    # The exact miscount the review caught: T_dir must be 2, never 3.
    check("G3 T_dir count is 2", len(by_target[t_dir[0]]) == 2, f"got {by_target[t_dir[0]]}")
    check("G3 Occlusion_Dynamics count is 1", len(by_target[occl[0]]) == 1,
          f"got {by_target[occl[0]]}")
    check("G3 planned-target count is 3", len(by_target[planned[0]]) == 3,
          f"got {by_target[planned[0]]}")

    check("G3 T_dir hooks are AG02/AG03",
          by_target[t_dir[0]] == ["PH_AG02_Reasoning_Bias", "PH_AG03_Constitutive_Commitment"],
          f"got {by_target[t_dir[0]]}")
    check("G3 Occlusion hook is SEM01",
          by_target[occl[0]] == ["PH_SEM01_Bilateral_Incompatibility"],
          f"got {by_target[occl[0]]}")

    rendered = B.render_guardrail(B.guard_hooks())
    check("G3 does not claim all three partials share one blocker",
          "三张 partial 的共同阻塞点" not in rendered)
    check("G3 names Occlusion_Dynamics in the grouping", "Occlusion_Dynamics" in rendered)


# --------------------------------------------------------------------------
# G1 — the S1/pathwise qualifier must survive into the usage policy
# --------------------------------------------------------------------------

def test_p1_t07_semantics() -> None:
    g = B.guard_p1_t07()
    rendered = B.render_guardrail(g)

    check("G1 keeps the S1/pathwise qualifier in policy",
          "S1 / pathwise" in g.policy or "S1/pathwise" in g.policy)
    check("G1 policy names the S2 condition", "P(τ<∞)>0" in g.policy)
    check("G1 policy names the S3 condition", "P(τ=∞)=0" in g.policy)
    check("G1 policy forbids the unqualified process-level verdict",
          "process-level" in g.policy and "不得" in g.policy)

    # The regression itself: an unqualified "τ<∞ ⇒ not a stable ISP" must not
    # appear as a standalone licensed claim.
    check("G1 does not license the unqualified claim",
          "唯一可无条件陈述的是" not in rendered)

    # The 1.3 stratification clause must be among the verbatim extracts, since
    # dropping it as "revision noise" is what allowed the regression.
    extracts = " ".join(text for _, text in g.extracts)
    check("G1 extracts include the stratification clause",
          "stratified by semantics" in extracts)
    check("G1 extracts include the S1 pathwise wording",
          "S1 pathwise" in extracts)

    check("G1 flags that OPEN_TENSIONS does not register the gap",
          "OPEN_TENSIONS" in g.interpretation or "OPEN_TENSIONS" in g.policy)


# --------------------------------------------------------------------------
# Provenance labelling — extract vs interpretation must stay separable
# --------------------------------------------------------------------------

def test_guardrail_sections() -> None:
    for factory in (B.guard_p1_t07, B.guard_dqo, B.guard_hooks, B.guard_shorthands):
        g = factory()
        rendered = B.render_guardrail(g)
        check(f"{g.gid} labels its interpretation as generated",
              "GENERATED INTERPRETATION" in rendered)
        check(f"{g.gid} labels its usage policy", "USAGE POLICY" in rendered)
        check(f"{g.gid} cites a policy source", bool(g.policy_source.strip()))
        if g.extracts:
            check(f"{g.gid} labels its source extract", "SOURCE EXTRACT" in rendered)


# --------------------------------------------------------------------------
# fail-loud — a missing anchor must abort, never degrade silently
# --------------------------------------------------------------------------

def test_fail_loud() -> None:
    real = B.read_text
    cases = [
        ("audit status block", "Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md",
         B.guard_p1_t07),
        ("theorem body", "Core/SRT_Core_21b_Constitutive_Theorems.md", B.guard_p1_t07),
        ("STATUS embargo", "STATUS.md", B.guard_dqo),
        ("hook audit table", "Operations/Audits/Hook_Closure_Audit_2026-07-25.md",
         B.guard_hooks),
        ("claim ladder section", "SRT_AI_START.md", B.build_claim_discipline),
    ]
    for label, target, fn in cases:
        B.read_text = lambda rel, _t=target: ("" if rel == _t else real(rel))
        stderr, sys.stderr = sys.stderr, open(os.devnull, "w")  # expected aborts are noisy
        try:
            fn()
            FAILURES.append(f"fail-loud {label}: did not abort on a missing anchor")
        except SystemExit as exc:
            if not exc.code:
                FAILURES.append(f"fail-loud {label}: exited 0")
        finally:
            sys.stderr.close()
            sys.stderr = stderr
            B.read_text = real


# --------------------------------------------------------------------------
# determinism — same provenance + same sources must give identical bytes
# --------------------------------------------------------------------------

def test_determinism() -> None:
    prov = B.Provenance(sha="deadbee", branch="test-branch",
                        generated="2026-01-01", dirty=False)
    with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
        B.generate(prov, Path(a))
        B.generate(prov, Path(b))
        names_a = sorted(p.name for p in Path(a).glob("*.md"))
        names_b = sorted(p.name for p in Path(b).glob("*.md"))
        check("determinism: same file set", names_a == names_b)
        for name in names_a:
            same = (Path(a) / name).read_bytes() == (Path(b) / name).read_bytes()
            check(f"determinism: {name} byte-identical", same)

        # Every bundle in one run must record the same provenance. This is the
        # bug where a per-bundle `git status` let bundle 1 say clean and the
        # rest say dirty, because writing bundle 1 dirtied the tree.
        for name in names_a:
            fm, _ = B.split_frontmatter((Path(a) / name).read_text(encoding="utf-8"))
            check(f"provenance sha in {name}", fm.get("source_commit") == "deadbee",
                  f"got {fm.get('source_commit')}")
            check(f"provenance date in {name}", fm.get("generated") == "2026-01-01",
                  f"got {fm.get('generated')}")
            check(f"provenance dirty in {name}", fm.get("source_dirty") == "false",
                  f"got {fm.get('source_dirty')}")


def test_porcelain_path() -> None:
    """`git()` strips stdout, so the first porcelain line loses its leading
    space and fixed-width slicing eats a character off the path. That bug hid
    behind a fake whose payload was never strip()ed."""
    cases = [
        ("M Operations/Context_Bundles/README.md",  # first line, already stripped
         "Operations/Context_Bundles/README.md"),
        (" M Operations/Context_Bundles/SPINE.md",
         "Operations/Context_Bundles/SPINE.md"),
        ("?? scripts/new_file.py", "scripts/new_file.py"),
        ("MM Core/SRT_Core_22_Equations.md", "Core/SRT_Core_22_Equations.md"),
        ("R  Core/old.md -> Core/new.md", "Core/new.md"),
        ("", ""),
    ]
    for line, want in cases:
        got = B.porcelain_path(line)
        check(f"porcelain_path({line!r})", got == want, f"got {got!r}, want {want!r}")


def test_dirty_excludes_bundle_dir() -> None:
    """The bundles' own churn must not count as a dirty source tree."""
    real = B.git

    def with_status(payload: str):
        def fake(*args: str) -> str:
            # Mirror git(): the real helper strips the whole stdout, which is
            # exactly what removed the first line's leading space.
            return payload.strip() if args[:2] == ("status", "--porcelain") else real(*args)
        return fake

    bundle_only = (
        " M Operations/Context_Bundles/README.md\n"
        " M Operations/Context_Bundles/SRT_CONTEXT_BUNDLE_SPINE.md"
    )
    B.git = with_status(bundle_only)
    try:
        check("dirty check ignores the bundle dir", B.working_tree_dirty() is False)
    finally:
        B.git = real

    B.git = with_status(" M Core/SRT_Core_22_Equations.md")
    try:
        check("dirty check still catches source edits", B.working_tree_dirty() is True)
    finally:
        B.git = real

    # A source edit listed after bundle churn must still register.
    B.git = with_status(bundle_only + "\n M STATUS.md")
    try:
        check("dirty check catches a source edit among bundle churn",
              B.working_tree_dirty() is True)
    finally:
        B.git = real


def run() -> None:
    test_hook_grouping()
    test_p1_t07_semantics()
    test_guardrail_sections()
    test_fail_loud()
    test_determinism()
    test_porcelain_path()
    test_dirty_excludes_bundle_dir()

    if FAILURES:
        for failure in FAILURES:
            print(f"FAIL: {failure}")
        raise SystemExit(1)
    print("test_build_context_bundles: all cases pass")


if __name__ == "__main__":
    run()
