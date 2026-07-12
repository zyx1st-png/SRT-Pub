#!/usr/bin/env python3
"""Validate the current book manuscript layout and retrieval routing.

The old 52-chapter outline split is archived. The current mainline lives in
01_Source_Intuition/BOOK/Drafts_26Q/ as Q00-Q28 plus the Q04b/Q15b topic
chapters, act prefaces/interludes, and appendices.

This check also prevents archived book material from silently becoming the
current construction source through search ranking or stale status metadata.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BOOK_DIR = ROOT / "01_Source_Intuition" / "BOOK"
STATUS = BOOK_DIR / "BOOK_CURRENT_STATUS.md"
MANIFEST = BOOK_DIR / "BOOK_ACTIVE_MANIFEST.json"
DRAFTS_DIR = BOOK_DIR / "Drafts_26Q"
ARCHIVE_52 = BOOK_DIR / "Archive_52Chapter"
ARCHIVE_META = BOOK_DIR / "Archive_Meta"
ARCHIVE_README = ARCHIVE_52 / "README.md"
FIVE_ACT_MAP = BOOK_DIR / "BOOK_ARCHITECTURE_MAP_5ACT_2026-06-24.md"

EXPECTED_DRAFTS = [
    "致读者.md",
    "Q00_序章.md",
    "Q01_给定性.md",
    "Q02_对象化.md",
    "Q03_前对象场.md",
    "Q04_最低非中立性.md",
    "幕间桥_一二幕.md",
    "幕前_二幕.md",
    "Q04b_选材.md",
    "Q05_选择不是挑选.md",
    "Q06_排除与阴影.md",
    "Q07_锚定.md",
    "Q08_不可逆性.md",
    "Q09_现实厚度.md",
    "Q10_秩序背景化.md",
    "幕间桥_二三幕.md",
    "幕前_三幕.md",
    "Q11_被选择.md",
    "Q12_攸关.md",
    "Q13_在乎.md",
    "Q14_价值不是偏好.md",
    "Q15_关切维度.md",
    "Q15b_能动性.md",
    "Q16_主体沉积.md",
    "Q17_意识.md",
    "幕间桥_三四幕.md",
    "幕前_四幕.md",
    "Q18_秩序与自由.md",
    "Q19_脚手架与牢笼.md",
    "Q20_遮蔽.md",
    "Q21_苦难.md",
    "Q22_方向.md",
    "幕间桥_四五幕.md",
    "幕前_五幕.md",
    "Q23_共同体.md",
    "幕间桥_Q23_Q24.md",
    "Q24_AI.md",
    "幕间桥_Q24_Q25.md",
    "Q25_选择广于意识.md",
    "Q26_可证伪性.md",
    "Q27_理论自反.md",
    "Q28_回到生成.md",
    "附录_三问使用指南.md",
    "附录_跨域难题_重述而非解决.md",
    "附录_术语表.md",
]

MAX_DRAFT_BYTES = 45_000
EXPECTED_ACTIVE_ROOT = "01_Source_Intuition/BOOK/Drafts_26Q"
EXPECTED_STATUS = "01_Source_Intuition/BOOK/BOOK_CURRENT_STATUS.md"
EXPECTED_STRUCTURE_MAP = (
    "01_Source_Intuition/BOOK/BOOK_ARCHITECTURE_MAP_5ACT_2026-06-24.md"
)
EXPECTED_ARCHIVE_ROOTS = {
    "01_Source_Intuition/BOOK/Archive_52Chapter",
    "01_Source_Intuition/BOOK/Archive_Meta",
}
REQUIRED_HARD_RULES = {
    "load_current_status_first": True,
    "load_active_primary_before_archive": True,
    "archive_may_seed_current_draft": False,
    "archive_use_requires_historical_label": True,
}
STALE_STATUS_PHRASES = [
    "正文默认冻结，改动须经治理批准",
    "当前书稿定位为：**非学院化的 SRT 奠基书**",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def require_frontmatter(path: Path, text: str) -> None:
    if not text.startswith("---\n"):
        fail(f"missing frontmatter: {path.relative_to(ROOT)}")
    if "\n---\n" not in text[4:]:
        fail(f"unterminated frontmatter: {path.relative_to(ROOT)}")


def load_manifest() -> dict[str, Any]:
    try:
        data = json.loads(read(MANIFEST))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {MANIFEST.relative_to(ROOT)}: {exc}")
    if not isinstance(data, dict):
        fail("BOOK_ACTIVE_MANIFEST root must be an object")
    return data


def validate_manifest(manifest: dict[str, Any]) -> int:
    if manifest.get("status") != "active":
        fail("BOOK_ACTIVE_MANIFEST status must be active")
    if manifest.get("construction_entry") != EXPECTED_STATUS:
        fail("BOOK_ACTIVE_MANIFEST construction_entry is not BOOK_CURRENT_STATUS")
    if manifest.get("active_root") != EXPECTED_ACTIVE_ROOT:
        fail("BOOK_ACTIVE_MANIFEST active_root is not Drafts_26Q")
    if manifest.get("structure_map") != EXPECTED_STRUCTURE_MAP:
        fail("BOOK_ACTIVE_MANIFEST must use the five-act structure map")

    archive_roots = set(manifest.get("archive_roots", []))
    if archive_roots != EXPECTED_ARCHIVE_ROOTS:
        fail("BOOK_ACTIVE_MANIFEST archive_roots are incomplete or unexpected")

    hard_rules = manifest.get("hard_rules")
    if not isinstance(hard_rules, dict):
        fail("BOOK_ACTIVE_MANIFEST hard_rules must be an object")
    for key, expected in REQUIRED_HARD_RULES.items():
        if hard_rules.get(key) is not expected:
            fail(f"BOOK_ACTIVE_MANIFEST hard rule mismatch: {key}")

    routes = manifest.get("concept_routes")
    if not isinstance(routes, list) or not routes:
        fail("BOOK_ACTIVE_MANIFEST concept_routes must be a non-empty list")

    primary_count = 0
    archive_prefixes = tuple(root + "/" for root in EXPECTED_ARCHIVE_ROOTS)
    for index, route in enumerate(routes, start=1):
        if not isinstance(route, dict):
            fail(f"concept route {index} must be an object")
        keywords = route.get("keywords")
        primary = route.get("primary")
        if not isinstance(keywords, list) or not keywords:
            fail(f"concept route {index} has no keywords")
        if not isinstance(primary, str):
            fail(f"concept route {index} has no primary path")
        if not primary.startswith(EXPECTED_ACTIVE_ROOT + "/"):
            fail(f"concept route {index} primary is not under Drafts_26Q: {primary}")
        primary_path = ROOT / primary
        if not primary_path.is_file():
            fail(f"concept route {index} primary does not exist: {primary}")
        primary_count += 1

        secondary = route.get("secondary", [])
        if not isinstance(secondary, list):
            fail(f"concept route {index} secondary must be a list")
        for path_text in secondary:
            if not isinstance(path_text, str):
                fail(f"concept route {index} has non-string secondary path")
            if path_text.startswith(archive_prefixes):
                fail(f"concept route {index} promotes archive material: {path_text}")
            if not (ROOT / path_text).is_file():
                fail(f"concept route {index} secondary does not exist: {path_text}")

    return primary_count


def validate_status(status_text: str) -> None:
    require_frontmatter(STATUS, status_text)
    required_fragments = [
        "Drafts_26Q/",
        "BOOK_ACTIVE_MANIFEST.json",
        "BOOK_ARCHITECTURE_MAP_5ACT_2026-06-24.md",
        "生成哲学战略总装轮",
        "只作历史材料和差异审计",
    ]
    for fragment in required_fragments:
        if fragment not in status_text:
            fail(f"BOOK_CURRENT_STATUS missing current routing marker: {fragment}")
    for phrase in STALE_STATUS_PHRASES:
        if phrase in status_text:
            fail(f"BOOK_CURRENT_STATUS retains stale active statement: {phrase}")


def validate_archive_guard() -> None:
    archive_text = read(ARCHIVE_README)
    require_frontmatter(ARCHIVE_README, archive_text)
    required_fragments = [
        "status: archived",
        "active_construction: false",
        "BOOK_ACTIVE_MANIFEST.json",
        "不得直接复制旧稿作为当前正文初稿或补丁母版",
    ]
    for fragment in required_fragments:
        if fragment not in archive_text:
            fail(f"Archive_52Chapter README missing guard: {fragment}")


def main() -> None:
    status_text = read(STATUS)
    validate_status(status_text)

    if not FIVE_ACT_MAP.is_file():
        fail(f"missing current structure map: {FIVE_ACT_MAP.relative_to(ROOT)}")
    if not ARCHIVE_52.is_dir() or not ARCHIVE_META.is_dir():
        fail("book archive roots are missing")

    manifest = load_manifest()
    primary_count = validate_manifest(manifest)
    validate_archive_guard()

    oversized = []
    for filename in EXPECTED_DRAFTS:
        path = DRAFTS_DIR / filename
        text = read(path)
        require_frontmatter(path, text)
        # Book drafts must remain non-canonical source text. The real convention
        # is claim_mode: companion_exposition (致读者 uses navigation; the glossary
        # appendix omits the field), and no draft carries canonical: false. So we
        # enforce the rule negatively: a draft must not promote itself to canonical.
        if "canonical: true" in text:
            fail(f"book draft must remain non-canonical: {path.relative_to(ROOT)}")
        if len(text.encode("utf-8")) > MAX_DRAFT_BYTES:
            oversized.append(filename)

    if oversized:
        fail("book draft(s) exceed connector-safe size: " + ", ".join(oversized))

    print("OK: current book manuscript layout and retrieval routing are guarded")
    print(f"drafts={len(EXPECTED_DRAFTS)} concept_route_primaries={primary_count}")


if __name__ == "__main__":
    main()
