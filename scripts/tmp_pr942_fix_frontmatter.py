from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    s = p.read_text()
    if old not in s:
        raise RuntimeError(f"anchor not found in {path}: {old!r}")
    p.write_text(s.replace(old, new, 1))

replace_once(
    "Core_Law/SRT_One_Formation.md",
    "status: draft_v0\nlayer: L1",
    "status: draft\nversion: v0\nlayer: L1",
)
replace_once(
    "CANONICAL_REGISTRY.md",
    "status：draft_v0 / claim-mode：canonical / claim-level：P1-candidate",
    "status：draft / version：v0 / claim-mode：canonical / claim-level：P1-candidate",
)
print("PR942 frontmatter ratchet fix applied")
