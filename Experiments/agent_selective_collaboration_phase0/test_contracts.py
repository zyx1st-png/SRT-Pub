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
                                           "more reachable tasks", "no gain", "future_reach"))
        self.assertEqual(self.s.events[seq - 1]["evidence_status"], "untested")
        evidence_seq = self.s.record_observation("e1", "supplier link changed", for_gts="g1", measurement_key="future_reach")
        assessed_seq = self.s.assess_gts("g1", "e1", "inconclusive")
        self.assertGreater(assessed_seq, evidence_seq)
        self.assertEqual(self.s.events[-1]["verdict"], "inconclusive")
        with self.assertRaises(ValueError):
            self.s.assess_gts("g1", "e1", "supported")

    def test_old_evidence_cannot_score_new_gts(self):
        self.s.record_observation("e-old", "already known")
        self.s.propose_gts(Hypothesis("g1", "a", "b", "c", "d", "m1"))
        with self.assertRaisesRegex(ValueError, "precede evidence"):
            self.s.assess_gts("g1", "e-old", "supported")
        with self.assertRaises(ValueError):
            self.s.propose_gts(Hypothesis("g1", "a", "b", "c", "d", "m1"))

    def test_gts_invalid_assessor_and_verdict(self):
        self.s.propose_gts(Hypothesis("g1", "a", "b", "c", "d", "m1"))
        self.s.record_observation("e1", "observation", for_gts="g1", measurement_key="m1")
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
            self.s.propose_gts(Hypothesis("g2", "", "intervention", "prediction", "failure", "m2"))

    def test_unprotected_tool_operation(self):
        self.s.execute("read", "read-1")
        self.assertEqual(self.s.events[-1]["kind"], "action_executed")


    def test_frame_update_invalidates_prior_approval(self):
        self.s.grant_once("send", scope="recipient-A")
        self.s.propose_frame("p1", "changed scope")
        self.s.decide_frame("p1", True)
        self.assertEqual(self.s.events[-2]["kind"], "approvals_invalidated")
        with self.assertRaises(PermissionError):
            self.s.execute("send", "after-reframe", scope="recipient-A")
        self.s.grant_once("send", scope="recipient-A")
        self.s.execute("send", "new-approval", scope="recipient-A")

    def test_user_can_revoke_scoped_approval(self):
        self.s.grant_once("send", scope="recipient-B")
        self.s.revoke("send", scope="recipient-B")
        with self.assertRaises(PermissionError):
            self.s.execute("send", "revoked", scope="recipient-B")
        with self.assertRaises(PermissionError):
            self.s.revoke("send", scope="recipient-B", actor="agent")

    def test_invalid_scope_and_ttl_are_permission_errors(self):
        for scope in (None, "", " "):
            with self.subTest(scope=scope):
                with self.assertRaises(PermissionError):
                    self.s.grant_once("send", scope=scope)
                with self.assertRaises(PermissionError):
                    self.s.execute("read", "not-sent", scope=scope)
        for ttl in (None, 0, -1, True, 3601):
            with self.subTest(ttl=ttl):
                with self.assertRaises(PermissionError):
                    self.s.grant_once("send", ttl_seconds=ttl)

    def test_expired_grant_rejected(self):
        from datetime import datetime, timedelta, timezone
        self.s.grant_once("send", scope="recipient-A")
        key = ("send", "recipient-A", self.s.frame_version)
        self.s._approvals[key] = datetime.now(timezone.utc) - timedelta(seconds=1)
        with self.assertRaisesRegex(PermissionError, "expired"):
            self.s.execute("send", "expired-evidence", scope="recipient-A")

    def test_only_linked_observation_can_assess_hypothesis(self):
        self.s.propose_gts(Hypothesis("g1", "supplier", "link", "improve", "no improvement", "service_metric"))
        self.s.propose_gts(Hypothesis("g2", "tariff", "change", "reduce cost", "no cost decrease", "cost_metric"))
        self.s.record_observation("unlinked", "some later event")
        self.s.record_observation("different", "later other hypothesis", for_gts="g2", measurement_key="cost_metric")
        with self.assertRaisesRegex(ValueError, "not registered"):
            self.s.assess_gts("g1", "unlinked", "supported")
        with self.assertRaisesRegex(ValueError, "not registered"):
            self.s.assess_gts("g1", "different", "supported")
        with self.assertRaises(ValueError):
            self.s.record_observation("bad", "label", for_gts="does-not-exist")
        self.s.record_observation("linked", "target measurement", for_gts="g1", measurement_key="service_metric")
        self.s.assess_gts("g1", "linked", "inconclusive")


    def test_mismatched_measurement_key_is_rejected(self):
        self.s.propose_gts(Hypothesis("g1", "supplier", "read",
                                       "increased reachable tasks", "no gain", "future_task_count"))
        with self.assertRaisesRegex(ValueError, "measurement key"):
            self.s.record_observation("wrong", "later observation",
                                      for_gts="g1", measurement_key="other_metric")
        self.assertFalse(any(e.get("evidence_id") == "wrong" for e in self.s.events))
        self.s.record_observation("right", "subsequent measurement",
                                  for_gts="g1", measurement_key="future_task_count")
        self.s.assess_gts("g1", "right", "inconclusive")

    def test_intervention_own_result_is_linked_to_predeclared_measurement(self):
        self.s.propose_gts(Hypothesis("g1", "new channel", "send",
                                       "higher coverage", "no change", "coverage"))
        self.s.grant_once("send", scope="test-recipient")
        with self.assertRaisesRegex(ValueError, "measurement key"):
            self.s.execute("send", "bad-evidence", scope="test-recipient",
                           for_gts="g1", measurement_key="other")
        self.s.execute("send", "intervention-evidence", scope="test-recipient",
                       for_gts="g1", measurement_key="coverage")
        observation = next(e for e in self.s.events
                           if e.get("evidence_id") == "intervention-evidence"
                           and e["kind"] == "observed")
        self.assertTrue(observation["self_generated"])
        self.assertEqual(observation["originating_intervention"], "send")
        self.assertEqual(observation["measurement_key"], "coverage")
        self.s.assess_gts("g1", "intervention-evidence", "supported")

    def test_intervention_must_match_registered_action(self):
        self.s.propose_gts(Hypothesis("g1", "condition", "read", "yes", "no", "metric"))
        self.s.grant_once("send")
        with self.assertRaisesRegex(ValueError, "pre-registered hypothesis intervention"):
            self.s.execute("send", "evidence", for_gts="g1", measurement_key="metric")
        self.s.execute("read", "correct-action", for_gts="g1", measurement_key="metric")

    def test_revocation_of_nonexistent_or_nonprotected_action_is_rejected(self):
        with self.assertRaises(PermissionError):
            self.s.revoke("read")
        with self.assertRaisesRegex(ValueError, "no outstanding"):
            self.s.revoke("send")
        self.assertFalse(any(e["kind"] == "action_revoked" for e in self.s.events))


if __name__ == "__main__":
    unittest.main()
