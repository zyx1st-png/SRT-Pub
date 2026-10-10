"""Regression tests for phase-0 contracts; NOT comparative efficacy tests."""
import unittest
from contracts import CollaborationLedger, Hypothesis


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.s = CollaborationLedger("improve service",
                                     frozenset({"read", "send"}),
                                     frozenset({"send"}))

    def test_proposal_not_commit_and_accept_version(self):
        self.s.propose_frame("p1", "improve retention")
        self.assertEqual((self.s.root_goal, self.s.frame_version), ("improve service", 1))
        self.s.decide_frame("p1", True)
        self.assertEqual(self.s.history, [(1, "improve service"),
                                          (2, "improve retention")])
        self.assertEqual(self.s.proposals["p1"]["status"], "accepted")

    def test_rejected_proposal_remains_addressable(self):
        seq = self.s.propose_frame("p1", "cut price")
        with self.assertRaises(PermissionError):
            self.s.decide_frame("p1", True, actor="agent")
        self.s.decide_frame("p1", False)
        self.assertEqual(self.s.root_goal, "improve service")
        self.assertEqual(self.s.proposals["p1"]["goal"], "cut price")
        self.assertEqual(self.s.proposals["p1"]["status"], "rejected")
        self.assertEqual(self.s.events[seq - 1]["goal"], "cut price")
        with self.assertRaises(ValueError):
            self.s.decide_frame("p1", True)

    def test_stale_branch_must_be_reproposed(self):
        self.s.propose_frame("p1", "path A")
        self.s.propose_frame("p2", "path B")
        self.s.decide_frame("p1", True)
        with self.assertRaisesRegex(ValueError, "stale proposal"):
            self.s.decide_frame("p2", True)
        self.assertEqual(self.s.root_goal, "path A")
        self.assertEqual(self.s.proposals["p2"]["status"], "stale")
        self.s.propose_frame("p2-new", "path B")
        self.s.decide_frame("p2-new", True)
        self.assertEqual(self.s.root_goal, "path B")

    def test_scope_bound_approval_is_one_shot(self):
        with self.assertRaises(PermissionError):
            self.s.execute("send", "x1")
        with self.assertRaises(PermissionError):
            self.s.grant_once("send", actor="agent")
        self.s.grant_once("send", scope="recipient-A")
        with self.assertRaises(PermissionError):
            self.s.execute("send", "x2", scope="recipient-B")
        self.s.execute("send", "x1", scope="recipient-A")
        with self.assertRaises(PermissionError):
            self.s.execute("send", "x3", scope="recipient-A")

    def test_tool_source_required(self):
        with self.assertRaises(PermissionError):
            self.s.record_observation("o1", "claimed done", actor="agent")
        with self.assertRaises(PermissionError):
            self.s.execute("read", "o2", actor="agent")
        with self.assertRaises(PermissionError):
            self.s.execute("edit_price", "o3")

    def test_gts_has_prospective_observation_and_assessment(self):
        seq = self.s.propose_gts(Hypothesis("g1", "supplier link", "relink",
                                           "more reachable tasks", "no gain"))
        self.assertEqual(self.s.events[seq - 1]["evidence_status"], "untested")
        evidence_seq = self.s.record_observation("e1", "supplier link changed")
        assessed_seq = self.s.assess_gts("g1", "e1", "inconclusive")
        self.assertGreater(assessed_seq, evidence_seq)
        self.assertEqual(self.s.events[-1]["verdict"], "inconclusive")
        with self.assertRaises(ValueError):
            self.s.assess_gts("g1", "e1", "supported")

    def test_old_evidence_cannot_score_new_gts(self):
        self.s.record_observation("e-old", "already known")
        self.s.propose_gts(Hypothesis("g1", "a", "b", "c", "d"))
        with self.assertRaisesRegex(ValueError, "precede evidence"):
            self.s.assess_gts("g1", "e-old", "supported")
        with self.assertRaises(ValueError):
            self.s.propose_gts(Hypothesis("g1", "a", "b", "c", "d"))

    def test_gts_invalid_assessor_and_verdict(self):
        self.s.propose_gts(Hypothesis("g1", "a", "b", "c", "d"))
        self.s.record_observation("e1", "observation")
        with self.assertRaises(PermissionError):
            self.s.assess_gts("g1", "e1", "supported", actor="agent")
        with self.assertRaises(ValueError):
            self.s.assess_gts("g1", "e1", "proved")

    def test_beacon_record_not_situated_reentry(self):
        with self.assertRaises(ValueError):
            self.s.add_beacon("ghost", 100)
        seq = self.s.propose_frame("p1", "change scope")
        self.s.add_beacon("scope", seq)
        record = self.s.retrieve_beacon_event("scope")
        self.assertEqual(record["proposal_id"], "p1")
        reentry = self.s.reenter_from_beacon("scope", "new user context")
        self.assertNotEqual(reentry, seq)
        self.assertEqual(self.s.events[-1]["kind"], "situated_reentry")
        self.assertEqual(self.s.events[-1]["source_seq"], seq)

    def test_cue_no_user_context_is_not_reentry(self):
        seq = self.s.propose_frame("p1", "new")
        self.s.add_beacon("p", seq)
        with self.assertRaises(PermissionError):
            self.s.reenter_from_beacon("p", "", actor="user")
        with self.assertRaises(PermissionError):
            self.s.reenter_from_beacon("p", "ctx", actor="agent")

    def test_event_snapshot_is_not_mutable_ledger(self):
        original = self.s.events[0]["kind"]
        snapshot = self.s.events
        snapshot[0]["kind"] = "tampered"
        self.assertEqual(self.s.events[0]["kind"], original)
        archive = self.s.proposals
        archive["injected"] = {"goal": "bad"}
        self.assertNotIn("injected", self.s.proposals)

    def test_invalid_state_rejected(self):
        with self.assertRaises(ValueError):
            CollaborationLedger("x", frozenset({"read"}), frozenset({"send"}))
        with self.assertRaises(ValueError):
            CollaborationLedger("", frozenset(), frozenset())
        with self.assertRaises(ValueError):
            self.s.propose_frame("p1", "  ")

    def test_event_schema_and_monotonic_seq(self):
        self.s.propose_frame("p1", "new", branch_id="branch-2", premise_revision=5)
        self.s.decide_frame("p1", True)
        self.s.record_observation("e1", "observed")
        seq = [e["seq"] for e in self.s.events]
        self.assertEqual(seq, list(range(1, len(seq) + 1)))
        keys = {"frame_version", "timestamp", "branch_id", "premise_revision",
                "reversibility", "authorization_scope", "source"}
        self.assertTrue(all(keys <= set(event) for event in self.s.events))
        self.assertEqual(self.s.events[1]["branch_id"], "branch-2")

    def test_hypothesis_requires_all_fields(self):
        with self.assertRaises(ValueError):
            self.s.propose_gts(Hypothesis("g2", "", "intervention", "prediction", "failure"))

    def test_unprotected_tool_operation(self):
        self.s.execute("read", "read-1")
        self.assertEqual(self.s.events[-1]["kind"], "action_executed")


if __name__ == "__main__":
    unittest.main()
