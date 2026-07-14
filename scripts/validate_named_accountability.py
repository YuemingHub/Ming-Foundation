#!/usr/bin/env python3
"""Validate Day 17 public accountability without fabricating real assignments."""

from pathlib import Path
import json
import re

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

    public = load("standards/review/NAMED_ACCOUNTABILITY_PUBLIC_REGISTER.json")
    if public["overall_state"] != "FrameworkCompleteNoNamedAssignees":
        errors.append("public register state mismatch")
    if len(public["roles"]) != 8:
        errors.append("expected eight public accountability roles")
    codes = {item["public_accountability_id"] for item in public["roles"]}
    if len(codes) != 8 or any(not re.fullmatch(r"RA-\d{2}", code) for code in codes):
        errors.append("public accountability ID set mismatch")
    for item in public["roles"]:
        if item["nomination_state"] != "NotNominated":
            errors.append(f"{item['role_id']}: nomination must remain NotNominated")
        if item["restricted_identity_ref"] is not None:
            errors.append(f"{item['role_id']}: fabricated restricted identity reference")
        if item["public_display_name"] is not None:
            errors.append(f"{item['role_id']}: real or display name may not be fabricated")
        if item["acceptance_state"] != "NotAccepted":
            errors.append(f"{item['role_id']}: acceptance must remain NotAccepted")
        for key in ["qualification_check", "conflict_check", "independence_check"]:
            if item[key] != "NotCompleted":
                errors.append(f"{item['role_id']}: {key} must remain NotCompleted")
        if item["activation_authority"] is not False:
            errors.append(f"{item['role_id']}: activation authority must remain false")

    expected_summary = {
        "roles_defined": 8,
        "roles_nominated": 0,
        "roles_accepted": 0,
        "qualification_checks_complete": 0,
        "conflict_checks_complete": 0,
        "independence_checks_complete": 0,
        "activation_authorities": 0,
    }
    if public["summary"] != expected_summary:
        errors.append("public accountability summary mismatch")

    topology = load("standards/review/SMALL_TEAM_ACCOUNTABILITY_TOPOLOGY.json")
    if topology["topology_state"] != "DesignedNotStaffed":
        errors.append("small-team topology state mismatch")
    if topology["minimum_distinct_people"] != {
        "CP2_internal_staff_rehearsal": 3,
        "CP3_affected_person_pilot": 4,
        "reason": "CP3 requires independent facilitation or jurisdiction/professional review outside the minimum three-person operating core.",
    }:
        errors.append("minimum distinct-person topology mismatch")
    if len(topology["internal_role_clusters"]) != 4:
        errors.append("expected four small-team role clusters")
    if len(topology["absolute_separation_rules"]) != 6:
        errors.append("expected six absolute separation rules")
    assumptions = topology["public_team_assumptions"]
    if assumptions["real_person_count_claimed"] != 0:
        errors.append("real person count must remain unclaimed")
    if any(assumptions[key] is not False for key in [
        "candidate_identity_claimed",
        "consent_to_role_claimed",
        "private_team_details_publishable",
    ]):
        errors.append("private team assumptions must remain false")

    nomination = load("standards/review/ROLE_NOMINATION_AND_ACCEPTANCE_PLAN.json")
    if nomination["execution_state"] != "ReadyForRestrictedIntakeNotExecuted":
        errors.append("nomination execution state mismatch")
    if len(nomination["workflow"]) != 10:
        errors.append("expected ten nomination workflow states")
    for key in [
        "nominations_started",
        "restricted_identity_records",
        "acceptances_complete",
        "qualification_checks_complete",
        "conflict_checks_complete",
        "active_assignments",
    ]:
        if nomination["summary"][key] != 0:
            errors.append(f"nomination summary {key} must remain zero")

    scenarios = load("standards/review/NAMED_ACCOUNTABILITY_TABLETOP_SCENARIOS.json")
    results = load("standards/review/NAMED_ACCOUNTABILITY_TABLETOP_RESULTS.json")
    if len(scenarios["scenarios"]) != 10 or len(results["results"]) != 10:
        errors.append("expected ten tabletop scenarios and results")
    if scenarios["data_policy"] != "SyntheticOnly" or results["data_policy"] != "SyntheticOnly":
        errors.append("tabletop data policy mismatch")
    scenario_ids = {item["scenario_id"] for item in scenarios["scenarios"]}
    if scenario_ids != {item["scenario_id"] for item in results["results"]}:
        errors.append("tabletop scenario/result coverage mismatch")
    for item in scenarios["scenarios"]:
        if item["contains_real_person_data"] is not False:
            errors.append(f"{item['scenario_id']}: real person data not allowed")
        if item["contains_sensitive_case_data"] is not False:
            errors.append(f"{item['scenario_id']}: sensitive case data not allowed")
        if item["input_class"] != "SyntheticFixture":
            errors.append(f"{item['scenario_id']}: input class mismatch")
    for item in results["results"]:
        if item["result"] != "Pass":
            errors.append(f"{item['scenario_id']}: tabletop result must pass")
        if item["synthetic_only"] is not True or item["real_evidence_detected"] is not False:
            errors.append(f"{item['scenario_id']}: tabletop boundary mismatch")
    if results["summary"] != {
        "executed": 10,
        "passed": 10,
        "failed": 0,
        "stopped": 0,
        "real_evidence_detected": 0,
    }:
        errors.append("tabletop result summary mismatch")
    for key in [
        "human_staff_rehearsals", "participants_recruited",
        "participant_sessions", "participant_evidence_records"
    ]:
        if results[key] != 0:
            errors.append(f"{key} must remain zero")

    templates = [
        ROOT / "governance/templates/GOV-TPL-0023-role-nomination-record.md",
        ROOT / "governance/templates/GOV-TPL-0024-role-acceptance-qualification-conflict-record.md",
        ROOT / "governance/templates/GOV-TPL-0025-separation-of-duties-exception-record.md",
        ROOT / "governance/templates/GOV-TPL-0026-human-use-protocol-signoff.md",
        ROOT / "governance/templates/GOV-TPL-0027-evidence-environment-deployment-verification.md",
        ROOT / "governance/templates/GOV-TPL-0028-human-review-activation-decision.md",
    ]
    if any(not path.exists() or frontmatter_status(path) != "Accepted" for path in templates):
        errors.append("Day 17 template set missing or not Accepted")

    if errors:
        print("Named-accountability validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        "Named-accountability validation passed. Validated 8 public role codes, "
        "zero nominations and assignments, a 3-person CP2 / 4-person CP3 "
        "small-team topology, 6 absolute separation rules, a 10-state "
        "restricted nomination workflow, 10 passed synthetic tabletop "
        "scenarios, zero real evidence, and 6 Accepted templates."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
