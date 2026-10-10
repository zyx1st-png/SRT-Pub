"""Phase-0 event/state contracts; no model, benchmark, or security boundary.

Actor arguments are test labels, not authenticated principals. This simulation
MUST NOT be connected directly to side-effecting tools. Production security
needs authenticated identities, scoped capability tokens and tool-side policy.
"""
from datetime import datetime, timedelta, timezone
from dataclasses import dataclass


@dataclass(frozen=True)
class Hypothesis:
    gts_id: str
    condition: str
    intervention: str
    prediction: str
    failure_condition: str
    measurement_key: str
    provenance: str = "model_hypothesis"


class CollaborationLedger:
    def __init__(self, root_goal: str, allowed_actions: frozenset[str],
                 protected_actions: frozenset[str]):
        if not root_goal or not root_goal.strip():
            raise ValueError("root_goal required")
        self.allowed_actions = frozenset(allowed_actions)
        self.protected_actions = frozenset(protected_actions)
        if not self.protected_actions <= self.allowed_actions:
            raise ValueError("protected actions must be allowed actions")
        self._goal = root_goal
        self._history = [(1, root_goal)]
        self._events = []
        self._proposals = {}
        self._hypotheses = {}
        self._observations = {}
        self._assessments = {}
        self._approvals = {}  # (action, scope, frame_version) -> expiry UTC
        self._beacons = {}
        self._record("frame_created", "user", goal=root_goal)

    @property
    def root_goal(self):
        return self._goal

    @property
    def frame_version(self):
        return len(self._history)

    @property
    def history(self):
        return list(self._history)

    @property
    def events(self):
        """Read-only snapshots, never references to the underlying event records."""
        return tuple(dict(event) for event in self._events)

    @property
    def proposals(self):
        return {key: dict(value) for key, value in self._proposals.items()}

    @property
    def hypotheses(self):
        return dict(self._hypotheses)

    def _record(self, kind, actor, *, branch_id=None, premise_revision=None,
                reversibility=None, authorization_scope=None, source=None, **details):
        event = dict(seq=len(self._events) + 1, kind=kind, actor=actor,
                     timestamp=datetime.now(timezone.utc).isoformat(),
                     frame_version=self.frame_version, branch_id=branch_id,
                     premise_revision=premise_revision, reversibility=reversibility,
                     authorization_scope=authorization_scope, source=source, **details)
        self._events.append(event)
        return event["seq"]

    def propose_frame(self, proposal_id: str, new_goal: str, *, actor="agent",
                      branch_id="root", premise_revision=1):
        if actor != "agent" or not proposal_id or not new_goal or not new_goal.strip():
            raise ValueError("invalid proposal")
        if proposal_id in self._proposals:
            raise ValueError("duplicate proposal")
        self._proposals[proposal_id] = dict(goal=new_goal, base_version=self.frame_version,
                                            status="pending", branch_id=branch_id,
                                            premise_revision=premise_revision)
        return self._record("frame_proposed", actor, proposal_id=proposal_id, goal=new_goal,
                            base_version=self.frame_version, branch_id=branch_id,
                            premise_revision=premise_revision, source="model_proposal")

    def decide_frame(self, proposal_id: str, accept: bool, *, actor="user"):
        if actor != "user" or proposal_id not in self._proposals:
            raise PermissionError("only the user can decide a known proposal")
        p = self._proposals[proposal_id]
        if p["status"] != "pending":
            raise ValueError("proposal is not pending")
        if p["base_version"] != self.frame_version:
            p["status"] = "stale"
            self._record("frame_stale", actor, proposal_id=proposal_id,
                         base_version=p["base_version"], source="version_check")
            raise ValueError("stale proposal: must be reconsidered on current frame")
        p["status"] = "accepted" if accept else "rejected"
        if accept:
            self._goal = p["goal"]
            self._history.append((self.frame_version + 1, self._goal))
            invalidated = len(self._approvals)
            self._approvals.clear()
            if invalidated:
                self._record("approvals_invalidated", "system",
                             count=invalidated, source="frame_version_changed")
        return self._record("frame_decided", actor, proposal_id=proposal_id,
                            goal=p["goal"], accepted=bool(accept),
                            branch_id=p["branch_id"], premise_revision=p["premise_revision"],
                            source="user_decision")

    def propose_gts(self, hypothesis: Hypothesis, *, actor="agent"):
        """GTS-inspired engineering hypothesis only; no GRG scientific claim."""
        if actor != "agent" or hypothesis.gts_id in self._hypotheses:
            raise ValueError("duplicate or invalid hypothesis")
        if not all((hypothesis.condition.strip(), hypothesis.intervention.strip(),
                    hypothesis.prediction.strip(), hypothesis.failure_condition.strip(),
                    hypothesis.measurement_key.strip(), hypothesis.provenance.strip())):
            raise ValueError("a testable hypothesis with provenance is required")
        self._hypotheses[hypothesis.gts_id] = hypothesis
        return self._record("gts_proposed", actor, gts_id=hypothesis.gts_id,
                            condition=hypothesis.condition, intervention=hypothesis.intervention,
                            prediction=hypothesis.prediction,
                            failure_condition=hypothesis.failure_condition,
                            measurement_key=hypothesis.measurement_key,
                            evidence_status="untested", source=hypothesis.provenance)

    def record_observation(self, evidence_id: str, description: str, *, actor="tool",
                           for_gts=None, measurement_key=None,
                           originating_intervention=None):
        """Bounded tool fixture: measurement-key registration precedes observation.

        Labels and sources are not authenticated; evidence identity, causal
        validity and predeclared outcome evaluation require a real evaluator.
        """
        if actor != "tool" or not evidence_id or not description:
            raise PermissionError("a tool adapter must supply a labeled observation")
        if evidence_id in self._observations:
            raise ValueError("duplicate evidence")
        if for_gts is not None:
            h = self._hypotheses.get(for_gts)
            if h is None:
                raise ValueError("cannot label evidence with unknown hypothesis")
            if measurement_key != h.measurement_key:
                raise ValueError("measurement key differs from predeclared hypothesis")
        seq = self._record("observed", actor, evidence_id=evidence_id,
                           description=description, for_gts=for_gts,
                           measurement_key=measurement_key,
                           originating_intervention=originating_intervention,
                           self_generated=originating_intervention is not None,
                           source="tool_observation")
        self._observations[evidence_id] = (seq, for_gts, measurement_key)
        return seq

    def assess_gts(self, gts_id: str, evidence_id: str, verdict: str, *, actor="evaluator"):
        """Post-observation assessment, NOT independent causal proof."""
        if actor != "evaluator":
            raise PermissionError("assessment requires a distinct evaluator adapter")
        if gts_id not in self._hypotheses or evidence_id not in self._observations:
            raise ValueError("unknown hypothesis or evidence")
        if verdict not in {"supported", "refuted", "inconclusive"}:
            raise ValueError("invalid verdict")
        if gts_id in self._assessments:
            raise ValueError("hypothesis already assessed")
        proposal_seq = next(e["seq"] for e in self._events
                            if e["kind"] == "gts_proposed" and e["gts_id"] == gts_id)
        observation_seq, linked_hypothesis, measurement_key = self._observations[evidence_id]
        if observation_seq <= proposal_seq:
            raise ValueError("prospective registration must precede evidence")
        if linked_hypothesis != gts_id or measurement_key != self._hypotheses[gts_id].measurement_key:
            raise ValueError("observation is not registered as evidence for this hypothesis")
        self._assessments[gts_id] = (evidence_id, verdict)
        return self._record("gts_assessed", actor, gts_id=gts_id,
                            evidence_id=evidence_id, verdict=verdict,
                            source="bounded_assessment")

    def grant_once(self, action: str, *, scope="task", actor="user",
                   ttl_seconds=300):
        """Grant a one-shot approval scoped to action, frame and finite TTL.

        Demo-only actor strings do not authenticate users or authorize live tools.
        """
        if (actor != "user" or action not in self.protected_actions
                or not isinstance(scope, str) or not scope.strip()
                or isinstance(ttl_seconds, bool)
                or not isinstance(ttl_seconds, (float, int))
                or not 0 < ttl_seconds <= 3600):
            raise PermissionError("user grant requires action, valid scope and finite TTL")
        expires_at = datetime.now(timezone.utc) + timedelta(seconds=ttl_seconds)
        key = (action, scope, self.frame_version)
        self._approvals[key] = expires_at
        return self._record("action_approved", actor, action=action,
                            authorization_scope=scope, expires_at=expires_at.isoformat(),
                            source="user_grant_fixture")

    def revoke(self, action: str, *, scope="task", actor="user"):
        """Explicit revocation within the current frame, even before first use."""
        if (actor != "user" or action not in self.protected_actions
                or not isinstance(scope, str) or not scope.strip()):
            raise PermissionError("only a valid protected approval can be revoked by the user")
        key = (action, scope, self.frame_version)
        if key not in self._approvals:
            raise ValueError("no outstanding scoped approval to revoke")
        self._approvals.pop(key)
        return self._record("action_revoked", actor, action=action,
                            authorization_scope=scope, source="user_revocation_fixture")

    def execute(self, action: str, evidence_id: str, *, scope="task", actor="tool",
                for_gts=None, measurement_key=None):
        if actor != "tool" or action not in self.allowed_actions:
            raise PermissionError("tool adapter/action not authorized")
        if not isinstance(scope, str) or not scope.strip():
            raise PermissionError("valid scope required")
        if for_gts is not None:
            h = self._hypotheses.get(for_gts)
            if h is None or h.intervention != action:
                raise ValueError("action must match a pre-registered hypothesis intervention")
            if measurement_key != h.measurement_key:
                raise ValueError("measurement key differs from predeclared hypothesis")
        key = (action, scope, self.frame_version)
        if action in self.protected_actions:
            expires_at = self._approvals.get(key)
            if expires_at is None:
                raise PermissionError("fresh matching scoped frame approval required")
            if datetime.now(timezone.utc) >= expires_at:
                self._approvals.pop(key, None)
                raise PermissionError("approval has expired")
        if not evidence_id or evidence_id in self._observations:
            raise ValueError("unique tool evidence id required")
        self._approvals.pop(key, None)  # one shot; no replay
        self.record_observation(evidence_id, f"tool result for {action}", actor="tool",
                                for_gts=for_gts, measurement_key=measurement_key,
                                originating_intervention=action)
        return self._record("action_executed", actor, action=action,
                            evidence_id=evidence_id, for_gts=for_gts,
                            measurement_key=measurement_key,
                            reversibility="unknown",
                            authorization_scope=scope, source="tool_action_fixture")

    def add_beacon(self, key: str, source_seq: int, *, actor="agent"):
        if actor != "agent" or not key or not key.strip():
            raise ValueError("valid model cue required")
        if not 1 <= source_seq <= len(self._events):
            raise ValueError("cue must reference a recorded event")
        self._beacons[key] = source_seq
        return self._record("beacon_anchor_added", actor, key=key,
                            source_seq=source_seq, source="working_label_only")

    def retrieve_beacon_event(self, key: str):
        """Retrieve an event record: this is NOT situated cognitive re-entry."""
        if key not in self._beacons:
            raise KeyError(key)
        return dict(self._events[self._beacons[key] - 1])

    def reenter_from_beacon(self, key: str, current_context: str, *, actor="user"):
        """Represent a new situated re-entry event, distinct from source event."""
        if actor != "user" or not current_context or not current_context.strip():
            raise PermissionError("user context is required for re-entry")
        source = self.retrieve_beacon_event(key)
        return self._record("situated_reentry", actor, key=key, source_seq=source["seq"],
                            current_context=current_context, source="new_event_not_recovery")
