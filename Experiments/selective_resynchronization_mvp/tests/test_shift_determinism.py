import torch

from src.shifts import apply_background_shift, remap_label


def test_background_shift_is_deterministic_and_seeded():
    image = torch.zeros(1, 28, 28)
    first = apply_background_shift(image.clone(), 17, 1101, 7, 0.35, 0.2)
    second = apply_background_shift(image.clone(), 17, 1101, 7, 0.35, 0.2)
    other = apply_background_shift(image.clone(), 17, 1102, 7, 0.35, 0.2)
    assert torch.equal(first, second)
    assert not torch.equal(first, other)


def test_partial_label_rule_is_fixed():
    mapping = {0: 6, 6: 0, 2: 4, 4: 2}
    assert [remap_label(i, mapping) for i in range(10)] == [6, 1, 4, 3, 2, 5, 0, 7, 8, 9]
