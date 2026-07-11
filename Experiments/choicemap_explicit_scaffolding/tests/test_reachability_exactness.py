import unittest
from src.environment import HiddenRegimeWorld
from src.environment_generator import generate_world

class TestReachability(unittest.TestCase):
    def test_closed_target_removed_exactly(self):
        env = HiddenRegimeWorld(generate_world(10, "Hidden-Irreversible"), 11)
        initial = env.reachable_future_tasks()
        env.closed_nodes.add(8)
        after = env.reachable_future_tasks()
        self.assertEqual(initial - after, {"future_0"})

