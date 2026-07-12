#!/usr/bin/env python3
"""Validate Profile Round 2 and the affected-person review readiness gate."""

from pathlib import Path
import json

from validation_utils import canonical_text_blob_sha

ROOT = Path(__file__).resolve().parents[1]

PROFILE_PATHS = {
    "PROF-0001": ROOT / "standards/profiles/PROF-0001-participation-and-representative-decision-profile.md",
    "PROF-0002": ROOT / "standards/profiles/PROF-0002-representative-authority-evidence-profile.md",
    "PROF-0003": ROOT / "standards/profiles/PROF-0003-retention-and-backup-completion-profile.md",
    "PROF-0004": ROOT / "standards/profiles/PROF-0004-service-response-and-resource-freshness-profile.md",
}

def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

def main():
    errors = []

    review = load("standards/review/PROFILE_INTERNAL_REVIEW_ROUND2_RESULTS.json")
    scope = review["review_scope"]
    if scope["round"] != "ProfileInternalReviewRound2" or scope["complete"] is not True:
        errors.append("Profile Round 2 scope mismatch")
    for key in [
        "affected_person_review_complete",
        "domain_review_complete",
        "jurisdiction_review_complete",
        "implementation_conformance_complete",
    ]:
        if scope[key] is not False:
            errors.append(f"{key} must remain false")

    summary = review["summary"]
    if (
        summary["profile_count"], summary["dimension_count"],
        summary["pass"], summary["revise"], summary["blocked"]
    ) != (4, 32, 28, 0, 4):
        errors.append("Profile Round 2 summary mismatch")

    counts = {"Pass": 0, "Revise": 0, "Blocked": 0}
    for item in review["results"]:
        pid = item["source_document"]
        if item["source_blob_sha"] != canonical_text_blob_sha(PROFILE_PATHS[pid]):
            errors.append(f"{pid}: Round 2 source blob mismatch")
        if item["review_state"] != "Complete":
            errors.append(f"{pid}: Round 2 incomplete")
        if item["overall_disposition"] != "InternallyReadyPendingAffectedPersonReview":
            errors.append(f"{pid}: Round 2 disposition mismatch")
        if item["promotion_recommendation"] != "RetainProposed":
            errors.append(f"{pid}: promotion recommendation mismatch")
        if len(item["dimensions"]) != 8:
            errors.append(f"{pid}: expected eight Round 2 dimensions")
        for dimension in item["dimensions"]:
            counts[dimension["disposition"]] += 1
    if counts != {"Pass": 28, "Revise": 0, "Blocked": 4}:
        errors.append(f"Round 2 dimension totals mismatch: {counts}")

    gate = load("standards/review/AFFECTED_PERSON_REVIEW_READINESS_GATE.json")
    if gate["overall_state"] != "ContentReadyOperationallyBlocked":
        errors.append("readiness gate overall state mismatch")
    if gate["content_ready"] is not True:
        errors.append("content must be ready")
    for key in [
        "operationally_ready_to_schedule",
        "recruitment_authorized",
        "sessions_authorized",
        "participant_evidence_exists",
    ]:
        if gate[key] is not False:
            errors.append(f"{key} must remain false")
    if gate["summary"] != {"gate_items": 9, "pass": 5, "blocked": 4, "fail": 0}:
        errors.append("readiness gate counts mismatch")

    activation = load("standards/review/REVIEW_OPERATIONAL_ACTIVATION.json")
    if activation["activation_state"] != "NotActivated":
        errors.append("operational activation must remain NotActivated")
    if len(activation["roles"]) != 8:
        errors.append("expected eight operational roles")
    if any(item["assignment_state"] != "Unassigned" for item in activation["roles"]):
        errors.append("all operational roles must remain Unassigned")
    if any(item["assignee"] is not None for item in activation["roles"]):
        errors.append("no role assignee may be fabricated")
    if len(activation["approvals"]) != 7:
        errors.append("expected seven protocol approvals")
    if any(item["state"] != "NotApproved" for item in activation["approvals"]):
        errors.append("all protocol approvals must remain NotApproved")
    if any(value == "Ready" for value in activation["environment"].values()):
        errors.append("evidence environment may not be marked Ready")
    for key in ["scheduling_authorized", "recruitment_authorized", "sessions_authorized"]:
        if activation[key] is not False:
            errors.append(f"activation {key} must remain false")

    plan = load("standards/review/AFFECTED_PERSON_REVIEW_PLAN.json")
    if plan["execution_state"] != "PreparedNotExecuted":
        errors.append("affected-person plan state mismatch")
    for key in ["participants_recruited", "sessions_completed", "results_recorded"]:
        if plan["summary"][key] != 0:
            errors.append(f"affected-person {key} must remain zero")

    profiles = load("standards/profiles/RESIDUAL_PROFILE_REGISTRY.json")
    for item in profiles["profiles"]:
        if item["status"] != "Proposed":
            errors.append(f"{item['id']}: must remain Proposed")
        if item["internal_review_state"] != "Round2Complete":
            errors.append(f"{item['id']}: Round 2 state mismatch")
        if item["operational_readiness"] != "Blocked":
            errors.append(f"{item['id']}: operational readiness must remain Blocked")

    residual = load("standards/review/RFC_R2_RESIDUAL_PLAN.json")
    states = {item["item_id"]: item["status"] for item in residual["items"]}
    for iid in {"R2R-001", "R2R-002", "R2R-003", "R2R-004"}:
        if states.get(iid) != "InternallyReadyPendingAffectedPersonReview":
            errors.append(f"{iid}: readiness state mismatch")
    if states.get("R2R-007") != "ContentReadyOperationallyBlocked":
        errors.append("R2R-007 state mismatch")

    ambiguities = load("standards/review/RFC_AMBIGUITIES.json")
    if len(ambiguities["ambiguities"]) != 19 or any(
        item["status"] != "Open" for item in ambiguities["ambiguities"]
    ):
        errors.append("all 19 ambiguities must remain Open")

    dissent = load("standards/review/RFC_DISSENT_REGISTER.json")
    if len(dissent["items"]) != 8 or any(item["status"] != "Open" for item in dissent["items"]):
        errors.append("all eight dissent items must remain Open")

    tests = load("standards/requirements/RFC_ACCEPTANCE_TESTS.json")
    if len(tests["tests"]) != 115 or any(
        item["test_state"] != "SpecificationOnly" for item in tests["tests"]
    ):
        errors.append("115 implementation tests must remain unexecuted specifications")

    baseline = load("standards/conformance/FOUNDATION_CONFORMANCE_BASELINE.json")
    if baseline["results"] != []:
        errors.append("implementation baseline must remain empty")
    if baseline["day15_profile_revision_and_readiness"]["operationally_ready_to_schedule"] is not False:
        errors.append("baseline must preserve operational block")

    if errors:
        print("Review-readiness gate validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        "Review-readiness gate validation passed. Validated 4 Profile Round 2 "
        "reviews, 32 dimensions (28 Pass, 0 Revise, 4 Blocked), a 9-item gate "
        "(5 Pass, 4 Blocked), 8 unassigned roles, 7 unapproved protocols, "
        "an unprovisioned evidence environment, zero participants and sessions, "
        "19 open ambiguities, 8 open dissent items, 115 unexecuted implementation "
        "test specifications, and an empty implementation baseline."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
