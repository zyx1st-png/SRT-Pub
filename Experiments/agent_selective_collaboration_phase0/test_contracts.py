"""Smoke tests for provenance / authority state, not comparative efficacy."""
import unittest
from contracts import CollaborationLedger, Hypothesis


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.s = CollaborationLedger("improve service", frozenset({"read", "send"}),
                                     frozenset({"send"}))

    def test_proposal_not_commit(self):
        self.s.propose_frame("p1", "improve retention")
        self.assertEqual((self.s.root_goal, self.s.frame_version), ("improve service", 1))
        self.s.decide_frame("p1", True)
        self.assertEqual(self.s.history, [(1, "improve service"), (2, "improve retention")])

    def test_reject_and_author_isolation(self):
        self.s.propose_frame("p1", "cut price")
        with self.assertRaises(PermissionError):
            self.s.decide_frame("p1", True, actor="agent")
        self.s.decide_frame("p1", False)
        self.assertEqual(self.s.root_goal, "improve service")

    def test_protected_action_requires_one_shot_grant(self):
        with self.assertRaises(PermissionError):
            self.s.execute("send", "x1")
        with self.assertRaises(PermissionError):
            self.s.grant_once("send", actor="agent")
        self.s.grant_once("send")
        self.s.execute("send", "x1")
        with self.assertRaises(PermissionError):
            self.s.execute("send", "x2")

    def test_tool_origin_required(self):
        with self.assertRaises(PermissionError):
            self.s.record_observation("o", "claimed done", actor="agent")
        with self.assertRaises(PermissionError):
            self.s.execute("read", "o", actor="agent")
        with self.assertRaises(PermissionError):
            self.s.execute("edit_price", "x3")

    def test_gts_remains_untested(self):
        self.s.propose_gts(Hypothesis("g1", "supplier link", "relink", "more reachable tasks", "no gain"))
        self.assertEqual(self.s.events[-1]["evidence_status"], "untested")
        with self.assertRaises(ValueError):
            self.s.propose_gts(Hypothesis("g1", "a", "b", "c", "d"))

    def test_beacon_must_link_real_event(self):
        with self.assertRaises(ValueError):
            self.s.add_beacon("unverified", 12)
        seq = self.s.propose_frame("p1", "change scope")
        self.s.add_beacon("scope", seq)
        self.assertEqual(self.s.recover_beacon("scope")["proposal_id"], "p1")

    def test_invalid_state_rejected(self):
        with self.assertRaises(ValueError):
            CollaborationLedger("x", frozenset({"read"}), frozenset({"send"}))
        with self.assertRaises(ValueError):
            self.s.propose_frame("p1", "  ")

    def test_audit_seq_is_monotonic(self):
        self.s.propose_frame("p1", "new task")
        self.s.decide_frame("p1", True)
        self.s.record_observation("e1", "example observed")
        self.assertEqual([e["seq"] for e in self.s.events], list(range(1, len(self.s.events) + 1)))


if __name__ == "__main__":
    unittest.main()
