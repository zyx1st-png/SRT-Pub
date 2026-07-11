from dataclasses import fields

from src.endpoint_matching import BMatchInput, assert_b_only_schema


def test_matching_schema_contains_no_future_fields():
    assert_b_only_schema()
    names = {field.name.lower() for field in fields(BMatchInput)}
    assert not any(name.startswith("c_") or name.startswith("q_") or "future" in name for name in names)
