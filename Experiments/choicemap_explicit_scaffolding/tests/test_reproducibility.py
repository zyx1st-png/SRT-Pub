import unittest
from src.environment_generator import FAMILIES, generate_world

class TestReproducibility(unittest.TestCase):
    def test_generator_is_pure(self):
        for family in FAMILIES:
            self.assertEqual(generate_world(42, family), generate_world(42, family))

