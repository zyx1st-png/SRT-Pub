from pathlib import Path

TARGETS = {
    "Core_Law/SRT_Core_Text_CN.md": "companion_exposition",
    "Core_Law/SRT_Core_Text_CN_Euclid.md": "companion_exposition",
    "Core_Law/SRT_Selection_Argument.md": "companion_exposition",
    "D_VALUE_ALIGNMENT.md": "companion_exposition",
    "SRT_FAQ_CRITICAL.md": "companion_exposition",
    "memory/README.md": "navigation",
}

for filename, new_mode in TARGETS.items():
    path = Path(filename)
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise SystemExit(f"missing frontmatter: {filename}")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise SystemExit(f"unterminated frontmatter: {filename}")
    fm = text[: end + 1]
    body = text[end + 1 :]

    if "claim_mode: canonical" in fm:
        fm = fm.replace("claim_mode: canonical", f"claim_mode: {new_mode}", 1)
    elif f"claim_mode: {new_mode}" not in fm:
        raise SystemExit(f"unexpected claim_mode in {filename}")

    if "\ncanonical:" not in fm:
        marker = f"claim_mode: {new_mode}\n"
        if marker not in fm:
            raise SystemExit(f"cannot locate claim_mode marker: {filename}")
        fm = fm.replace(marker, marker + "canonical: false\n", 1)
    elif "canonical: false" not in fm:
        raise SystemExit(f"unexpected canonical flag in {filename}")

    path.write_text(fm + body, encoding="utf-8")

print("Batch A authority truth-up applied")
