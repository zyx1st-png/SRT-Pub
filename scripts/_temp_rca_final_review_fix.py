from pathlib import Path

helper = Path("scripts/_temp_rca_final_review_fix_v2.py")
code = helper.read_text(encoding="utf-8")
exec(compile(code, str(helper), "exec"))
helper.unlink()
