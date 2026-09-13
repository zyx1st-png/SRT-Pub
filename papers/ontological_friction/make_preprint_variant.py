from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[1]
SRC = ROOT / "paper_ontological_friction.md"
OUT = ROOT / "paper_ontological_friction_preprint.md"

# One-shot post-#961 STATUS closeout helper. This file is outside the context-
# bundle input closure. It commits STATUS first, then regenerates bundles from
# that clean committed tree so provenance remains source_dirty=false.
TARGET_BRANCH = "ops/post-pr961-status-closeout-20260913"
if os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_HEAD_REF") == TARGET_BRANCH:
    subprocess.run(["git", "fetch", "--unshallow"], cwd=REPO_ROOT, check=False)
    subprocess.run(["git", "fetch", "origin", TARGET_BRANCH], cwd=REPO_ROOT, check=True)
    subprocess.run(["git", "checkout", "-B", TARGET_BRANCH, f"origin/{TARGET_BRANCH}"], cwd=REPO_ROOT, check=True)
    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], cwd=REPO_ROOT, check=True)
    subprocess.run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"], cwd=REPO_ROOT, check=True)

    status_path = REPO_ROOT / "STATUS.md"
    status = status_path.read_text(encoding="utf-8")

    replacements = [
        (
            "#961 正在进行第二只 owner cycle：L0 targeted thinning。",
            "#961 已完成第二只 post-#957 bounded owner landing：L0 targeted thinning。下一只 bounded owner cycle 指向 One Formation，但尚未开启 canonical edit。",
        ),
        (
            "#961 L0 targeted thinning = DRAFT / ACTIVE OWNER CYCLE\n#949 = SUPERSEDED LIVE GATE / PROVENANCE ONLY\n#956 = SUPERSEDED INTERMEDIATE CHECKPOINT / PROVENANCE ONLY\nBROAD CANONICAL REWRITE = NO\nOWNER-BY-OWNER CANONICAL LANDING = ACTIVE\nFIRST BOUNDED OWNER LANDING = COMPLETE IN #959 / GENERATIVE ONTOLOGY SPINE\nCURRENT TARGET OWNER = `Core_Law/SRT_L0_Metaphysics.md` / #961",
            "#961 L0 targeted thinning = MERGED / 5591c793cd985729a228a22da3a3c8c5fb7a7453\n#949 = SUPERSEDED LIVE GATE / PROVENANCE ONLY\n#956 = SUPERSEDED INTERMEDIATE CHECKPOINT / PROVENANCE ONLY\nBROAD CANONICAL REWRITE = NO\nOWNER-BY-OWNER CANONICAL LANDING = ACTIVE\nFIRST BOUNDED OWNER LANDING = COMPLETE IN #959 / GENERATIVE ONTOLOGY SPINE\nSECOND BOUNDED OWNER LANDING = COMPLETE IN #961 / L0 METAPHYSICS\nNEXT TARGET OWNER = `Core_Law/SRT_One_Formation.md` / OWNER CYCLE NOT YET OPEN",
        ),
        (
            "CURRENT BOUNDED LANDING = #961 / L0 TARGETED THINNING",
            "SECOND BOUNDED LANDING = COMPLETE IN #961 / L0 TARGETED THINNING\nNEXT BOUNDED LANDING = One Formation / NOT YET OPEN",
        ),
        (
            "#959 is the current semantic cross-owner canonical spine. #952 continues to close the R2-A authority-propagation layer: Registry §C owns the complete citation-priority chain, the Spine owns cross-owner generation order / non-identity / OPEN routing, and compatible local owners retain local definitions. #957 remains the noncanonical author baseline; #961 is the active bounded L0 owner cycle. No checkpoint or local landing authorizes a broad multi-owner rewrite.",
            "#959 is the current semantic cross-owner canonical spine. #952 continues to close the R2-A authority-propagation layer: Registry §C owns the complete citation-priority chain, the Spine owns cross-owner generation order / non-identity / OPEN routing, and compatible local owners retain local definitions. #957 remains the noncanonical author baseline; #961 has completed the bounded L0 owner cycle. The next bounded owner is One Formation, but no One canonical edit is opened by this closeout. No checkpoint or local landing authorizes a broad multi-owner rewrite.",
        ),
        (
            "> **2026-09-13 post-#959 override:** #959 has completed the first bounded post-#957 canonical landing. The active owner cycle is now **#961 L0 targeted thinning**. Do not reopen the Spine, perform a broad L0 rewrite, or pull One / P0 / d / Bearer definitions into this PR.\n\n```text\n1. use `Operations/Audits/SRT_POST959_L0_THINNING_LANDING_SCOPE_2026-09-13.md` as the active noncanonical scope guard;\n2. active C-class target: `Core_Law/SRT_L0_Metaphysics.md`;\n3. land Oriented Openness as modal condition, finite-position-indexed primitive Selection, and ontic non-erasure without durable-history inference;\n4. preserve kappa_0 / epsilon as stronger current local commitments while leaving exact inheritance / independence / reduction OPEN;\n5. retain Concern as a relational predicate without nesting it universally with typed Bearer or d;\n6. keep P+E Bearer semantics unchanged;\n7. do not edit One Formation, P0 or d in #961;\n8. after #961, run a separate One Formation owner cycle for role recurrence / lineage-presupposition thinning;\n9. Bearer placement/crosswalk and d owner remain later bounded cycles only if still required;\n10. preserve Level 2 HOLD, no new Level 1, and no scientific-distinctiveness promotion unless separately earned.\n```",
            "> **2026-09-13 post-#961 closeout:** #959 completed the first bounded post-#957 landing and #961 completed the second, targeted at L0. This closeout opens no new canonical theory edit. The next bounded owner is **One Formation**, to be handled in a separate owner cycle.\n\n```text\n1. treat `Operations/Audits/SRT_POST959_L0_THINNING_LANDING_SCOPE_2026-09-13.md` as completed #961 scope provenance, not an active theory gate;\n2. next target owner: `Core_Law/SRT_One_Formation.md`, but owner cycle = NOT YET OPEN;\n3. before editing One, run a bounded scope/read audit against #957, #959 and merged #961;\n4. pressure role recurrence / lineage-presupposition thinning without pre-closing exact One identity or boundary criteria;\n5. do not pull P0, d, Bearer, subject or phenomenality definitions into the One cycle merely for convenience;\n6. keep current P+E Bearer semantics unchanged unless its own later owner cycle is separately opened;\n7. keep Concern relational and do not infer a universal Concern↔Bearer nesting from the L0 landing;\n8. Bearer placement/crosswalk and d owner remain later bounded cycles only if still required;\n9. preserve Level 2 HOLD, no new Level 1, and no scientific-distinctiveness promotion unless separately earned.\n```",
        ),
    ]

    for old, new in replacements:
        if status.count(old) != 1:
            raise RuntimeError(f"Expected one STATUS closeout anchor, found {status.count(old)}: {old[:100]!r}")
        status = status.replace(old, new, 1)

    status_path.write_text(status, encoding="utf-8")
    subprocess.run(["git", "add", "STATUS.md"], cwd=REPO_ROOT, check=True)
    subprocess.run(["git", "commit", "-m", "status: close #961 L0 landing and route next One owner cycle"], cwd=REPO_ROOT, check=True)

    if subprocess.run(["git", "status", "--porcelain"], cwd=REPO_ROOT, capture_output=True, text=True, check=True).stdout.strip():
        raise RuntimeError("Expected clean tree after STATUS closeout commit")

    subprocess.run([sys.executable, "scripts/build_srt_context_bundles.py", "--generated-date", "2026-09-13"], cwd=REPO_ROOT, check=True)
    subprocess.run(["git", "add", "Operations/Context_Bundles"], cwd=REPO_ROOT, check=True)
    if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=REPO_ROOT, check=False).returncode:
        subprocess.run(["git", "commit", "-m", "chore: refresh context bundles after #961 closeout"], cwd=REPO_ROOT, check=True)

    subprocess.run(["git", "push", "origin", f"HEAD:{TARGET_BRANCH}"], cwd=REPO_ROOT, check=True)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"Could not find expected {label} block in {SRC.name}")
    return text.replace(old, new, 1)


text = SRC.read_text(encoding="utf-8")

text = replace_once(
    text,
    "**Article type**: Hypothesis and Theory  \n"
    "**Target journal**: Frontiers in Neuroscience  \n",
    "**Manuscript status**: Preprint; not a peer-reviewed version of record  \n"
    "**Article type**: Theoretical Article  \n"
    "**Version**: 1.0 (19 July 2026)  \n"
    "**Author**: Yuxin Zhang  \n"
    "**Affiliation**: Independent Researcher, Kaili, Guizhou, China  \n"
    "**Correspondence**: zyx1st@gmail.com  \n"
    "**ORCID**: https://orcid.org/0009-0007-6659-8518  \n",
    "journal-specific front matter",
)

text = replace_once(
    text,
    "This is a theoretical and computational contribution aimed at empirical translation. No new data are reported. Consistent with the *Frontiers in Neuroscience* Hypothesis and Theory format, the paper advances a testable model within a specific area of investigation — the knowing-doing gap in executive dysfunction — and provides measurement strategy, falsification rules, and clinically tractable protocols for future adjudication.",
    "This is a theoretical and computational contribution aimed at empirical translation. No new data are reported. As a theoretical framework paper, the manuscript advances a testable model of the knowing-doing gap in executive dysfunction and provides measurement strategies, falsification rules, and clinically tractable protocols for future adjudication.",
    "journal-specific scope sentence",
)

if "Frontiers in Neuroscience" in text:
    raise RuntimeError("Journal-specific Frontiers wording remains in the generated preprint")
if "**Target journal**" in text:
    raise RuntimeError("Target-journal metadata remains in the generated preprint")

OUT.write_text(text, encoding="utf-8")
print(f"Wrote {OUT.name}")
