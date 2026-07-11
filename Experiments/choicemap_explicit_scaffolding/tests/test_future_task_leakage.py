import unittest
from _helpers import CONFIG
from src.environment import HiddenRegimeWorld
from src.environment_generator import generate_world

class TestFutureTaskLeakage(unittest.TestCase):
    def test_hidden_before_turn(self):
        env = HiddenRegimeWorld(generate_world(1, "Hidden-Irreversible"), 2)
        with self.assertRaises(RuntimeError): env.reveal_future_task()
        self.assertFalse(hasattr(env.agent_view(), "future_task"))

