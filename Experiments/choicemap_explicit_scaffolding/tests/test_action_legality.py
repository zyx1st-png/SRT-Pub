import unittest
from src.environment import HiddenRegimeWorld
from src.environment_generator import generate_world

class TestActionLegality(unittest.TestCase):
    def test_rejects_illegal_action(self):
        env = HiddenRegimeWorld(generate_world(1, "Stable-Reversible"), 9)
        with self.assertRaises(ValueError): env.step("read_oracle")

