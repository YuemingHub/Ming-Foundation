#!/usr/bin/env python3
"""Validate Day 17 human activation readiness and blocking invariants."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

def frontmatter_status(path):
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    for line in text[4:end].splitlines():
        if line.startswith("status:"):
            return line.split(":", 1)[1].strip()
    return None

def main():
    errors = []

    protocols = load("standards/review/HUMAN_USE_PROTOCOL_APPROVAL_PLAN.json")
    if protocols["overall_state"] != "AwaitingNamedApprovers":
        errors.append("protocol approval readiness state mismatch")
    if len(protocols["protocols"]) != 7:
        errors.append("expected seven human-use protocols")
    for item in protocols["protocols"]:
        if item["approval_state"] != "NotApproved":
            errors.append(f"{item['approval_id']}: human use must remain NotApproved")
        if item["named_primary_approver"] is not None:
            errors.append(f"{item['approval_id']}: fabricated primary approver")
        if item["named_independent_reviewer"] is not None:
            errors.append(f"{item['approval_id']}: fabricated independent reviewer")
    if protocols["summary"] != {
        "protocols": 7,
        "approval_routes_defined": 7,
        "named_primary_approvers": 0,
        "named_independent_reviewers": 0,
        "human_use_approved": 0,
    }:
        errors.append("protocol approval readiness summary mismatch")

    environment = load("standards/review/EVIDENCE_ENVIRONMENT_DEPLOYMENT_PLAN.json")
    if environment["overall_state"] != "PlannedNotProvisioned":
        errors.append("environment deployment state mismatch")
    if environment["live_evidence_ingestion"] != "Prohibited":
        errors.append("live evidence ingestion must remain prohibited")
    if len(environment["controls"]) != 8:
        errors.append("expected eight deployment controls")
    for item in environment["controls"]:
        if item["deployment_state"] != "NotStarted":
            errors.append(f"{item['control_id']}: deployment must remain NotStarted")
        if item["verification_state"] != "NotVerified":
            errors.append(f"{item['control_id']}: verification must remain NotVerified")
        if item["verification_evidence_refs"] != []:
            errors.append(f"{item['control_id']}: fabricated verification evidence")
    if environment["summary"] != {
        "controls": 8,
        "deployment_started": 0,
        "deployed": 0,
        "verified": 0,
        "live_evidence_controls_ready": 0,
    }:
        errors.append("environment deployment summary mismatch")

    cp2 = load("standards/review/CP2_STAFF_REHEARSAL_READINESS.json")
    if cp2["overall_state"] != "FrameworkReadyNamedStaffRequired":
        errors.append("CP2 readiness state mismatch")
    if cp2["authorization_state"] != "Blocked" or cp2["execution_state"] != "NotExecuted":
        errors.append("CP2 must remain blocked and unexecuted")
    for key in ["participants_allowed", "participant_evidence_allowed", "live_system_actions_allowed"]:
        if cp2[key] is not False:
            errors.append(f"CP2 {key} must remain false")

    gate = load("standards/review/DAY17_HUMAN_ACTIVATION_READINESS_GATE.json")
    if gate["overall_state"] != "NamedAccountabilityFrameworkCompleteHumanActivationBlocked":
        errors.append("Day 17 gate state mismatch")
    if gate["summary"] != {"gate_items": 16, "pass": 9, "blocked": 7, "fail": 0}:
        errors.append("Day 17 gate summary mismatch")
    if gate["named_accountability_framework_complete"] is not True:
        errors.append("named accountability framework must be complete")
    if gate["named_accountable_people"] != 0:
        errors.append("named accountable people must remain zero")
    for key in [
        "human_review_activation_authorized", "cp2_authorized", "cp3_authorized",
        "recruitment_authorized", "sessions_authorized", "participant_evidence_exists"
    ]:
        if gate[key] is not False:
            errors.append(f"Day 17 gate {key} must remain false")

    roles = load("standards/review/REVIEW_ROLE_ASSIGNMENT_REGISTRY.json")
    if roles["summary"] != {
        "roles_defined": 8,
        "roles_assigned": 0,
        "conflict_checks_complete": 0,
        "qualification_checks_complete": 0,
    }:
        errors.append("Day 16 role registry zero-state mismatch")
    for item in roles["roles"]:
        if item["assignment_state"] != "Unassigned" or item["assignee"] is not None:
            errors.append(f"{item['role_id']}: assignment must remain empty")

    activation = load("standards/review/REVIEW_OPERATIONAL_ACTIVATION.json")
    if activation["activation_state"] != "SyntheticPilotOnly":
        errors.append("operational activation must remain SyntheticPilotOnly")
    if activation["human_review_activation_state"] != "NotActivated":
        errors.append("human review activation must remain NotActivated")
    if activation["summary"]["roles_assigned"] != 0:
        errors.append("operational roles assigned must remain zero")
    if activation["summary"]["approvals_completed"] != 0:
        errors.append("operational approvals completed must remain zero")
    if activation["summary"]["environment_controls_ready"] != 0:
        errors.append("operational live controls ready must remain zero")
    for key in ["scheduling_authorized", "recruitment_authorized", "sessions_authorized"]:
        if activation[key] is not False:
            errors.append(f"operational {key} must remain false")

    pilot = load("standards/review/CONTROLLED_PILOT_AUTHORIZATION.json")
    states = {
        item["class_id"]: (item["authorization_state"], item["execution_state"])
        for item in pilot["classes"]
    }
    expected_states = {
        "CP0": ("Authorized", "Complete"),
        "CP1": ("Authorized", "Complete"),
        "CP2": ("Blocked", "NotExecuted"),
        "CP3": ("Blocked", "NotExecuted"),
    }
    if states != expected_states:
        errors.append("controlled pilot states changed")
    for key in [
        "human_review_authorized", "recruitment_authorized",
        "participant_sessions_authorized", "live_evidence_authorized",
        "product_decision_effect_authorized", "public_conformance_claim_authorized"
    ]:
        if pilot[key] is not False:
            errors.append(f"pilot {key} must remain false")

    affected = load("standards/review/AFFECTED_PERSON_REVIEW_PLAN.json")
    if affected["execution_state"] != "PreparedNotExecuted":
        errors.append("affected-person review must remain PreparedNotExecuted")
    for key in ["participants_recruited", "sessions_completed", "results_recorded"]:
        if affected["summary"][key] != 0:
            errors.append(f"affected-person {key} must remain zero")

    profiles = load("standards/profiles/RESIDUAL_PROFILE_REGISTRY.json")
    if any(item["status"] != "Proposed" for item in profiles["profiles"]):
        errors.append("all Profiles must remain Proposed")

    ambiguities = load("standards/review/RFC_AMBIGUITIES.json")
    if len(ambiguities["ambiguities"]) != 19 or any(
        item["status"] != "Open" for item in ambiguities["ambiguities"]
    ):
        errors.append("all 19 ambiguities must remain Open")

    dissent = load("standards/review/RFC_DISSENT_REGISTER.json")
    if len(dissent["items"]) != 8 or any(item["status"] != "Open" for item in dissent["items"]):
        errors.append("all eight dissent items must remain Open")

    implementation_tests = load("standards/requirements/RFC_ACCEPTANCE_TESTS.json")
    if len(implementation_tests["tests"]) != 115:
        errors.append("expected 115 implementation-test specifications")
    if any(item["test_state"] != "SpecificationOnly" for item in implementation_tests["tests"]):
        errors.append("implementation tests must remain SpecificationOnly")

    baseline = load("standards/conformance/FOUNDATION_CONFORMANCE_BASELINE.json")
    if baseline["results"] != []:
        errors.append("implementation conformance baseline must remain empty")
    day17 = baseline["day17_named_accountability"]
    if day17["named_accountable_people"] != 0:
        errors.append("baseline named accountable people must remain zero")
    if day17["human_review_activation_authorized"] is not False:
        errors.append("baseline human activation must remain false")
    if day17["implementation_tests_executed"] != 0:
        errors.append("baseline implementation tests executed must remain zero")

    expected_statuses = {
        "foundation/charter/MF-0004-life-charter.md": "Candidate",
        "projects/mingos/PROJECT-MINGOS-0002-mingos-charter.md": "Candidate",
        "standards/profiles/PROF-0001-participation-and-representative-decision-profile.md": "Proposed",
        "standards/profiles/PROF-0002-representative-authority-evidence-profile.md": "Proposed",
        "standards/profiles/PROF-0003-retention-and-backup-completion-profile.md": "Proposed",
        "standards/profiles/PROF-0004-service-response-and-resource-freshness-profile.md": "Proposed",
    }
    for rel, expected in expected_statuses.items():
        path = ROOT / rel
        if path.exists() and frontmatter_status(path) != expected:
            errors.append(f"{rel}: status must remain {expected}")

    if errors:
        print("Human-activation readiness validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        "Human-activation readiness validation passed. Validated 7 unapproved "
        "human-use protocol routes, 8 not-started environment controls, CP2 and "
        "CP3 blocking, a 16-item gate (9 Pass, 7 Blocked), zero named people, "
        "zero role checks, zero human approvals, zero participants and sessions, "
        "19 open ambiguities, 8 open dissent items, 115 unexecuted implementation "
        "test specifications, and an empty implementation-conformance baseline."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
