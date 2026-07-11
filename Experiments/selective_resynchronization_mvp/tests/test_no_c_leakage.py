from dataclasses import fields

import pytest

from src.protocol import ABArtifacts, assert_ab_only_schema, freeze_preC_files


def test_ab_schema_has_no_c_stage_fields():
    assert_ab_only_schema()
    names = {field.name for field in fields(ABArtifacts)}
    assert not any(name.startswith("c_") for name in names)
    assert "q_c" not in names


def test_freeze_rejects_c_fields(tmp_path):
    with pytest.raises(ValueError):
        freeze_preC_files(tmp_path, {"seed": 1, "C_accuracy": 0.5})
