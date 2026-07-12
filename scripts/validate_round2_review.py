#!/usr/bin/env python3
"""Validate Day 12 Round 2 review, source tests, and truthful fidelity state."""

from __future__ import annotations
from pathlib import Path
from validation_utils import canonical_text_blob_sha
import json

ROOT = Path(__file__).resolve().parents[1]

RFC_PATHS = {
    "RFC-0001": ROOT / "standards/rfc/RFC-0001-subject-speaker-and-contestability.md",
    "RFC-0002": ROOT / "standards/rfc/RFC-0002-consent-and-data-rights-lifecycle.md",
    "RFC-0003": ROOT / "standards/rfc/RFC-0003-safety-escalation-handoff-appeal-and-incident.md",
}

def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def frontmatter_value(path, key):
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    for line in text[4:end].splitlines():
        if line.startswith(f"{key}:"):
            return line.split(":", 1)[1].strip()
    return None

def main():
    errors = []

    review = load("standards/review/RFC_INTERNAL_REVIEW_ROUND2_RESULTS.json")
    scope = review["review_scope"]
    if scope["round"] != "InternalArchitectureRound2" or scope["complete"] is not True:
        errors.append("Round 2 scope is incorrect")
    for field in (
        "external_review_complete",
        "affected_person_review_complete",
        "legal_review_complete",
        "implementation_conformance_complete",
    ):
        if scope[field] is not False:
            errors.append(f"{field} must remain false")

    summary = review["summary"]
    expected = (3, 27, 14, 10, 3, 12, 8, 4, 0)
    actual = (
        summary["rfc_count"], summary["dimension_count"], summary["pass"],
        summary["revise"], summary["blocked"], summary["ambiguities_reviewed"],
        summary["accepted_for_internal_architecture"],
        summary["needs_further_revision"], summary["rejected"],
    )
    if actual != expected:
        errors.append(f"Round 2 summary mismatch: {actual}")

    results = review["results"]
    if {item["source_document"] for item in results} != set(RFC_PATHS):
        errors.append("Round 2 RFC coverage mismatch")
    counts = {"Pass": 0, "Revise": 0, "Blocked": 0}
    for item in results:
        if item["review_state"] != "Complete":
            errors.append(f"{item['source_document']}: review not complete")
        if item["promotion_recommendation"] != "RetainProposed":
            errors.append(f"{item['source_document']}: promotion mismatch")
        if item["requirement_registry_state"] != "RebaselinedForDraft0.2":
            errors.append(f"{item['source_document']}: requirement registry state mismatch")
        if len(item["dimensions"]) != 9:
            errors.append(f"{item['source_document']}: expected 9 dimensions")
        for dimension in item["dimensions"]:
            counts[dimension["disposition"]] += 1
        path = RFC_PATHS[item["source_document"]]
        if item["source_blob_sha"] != canonical_text_blob_sha(path):
            errors.append(f"{item['source_document']}: blob mismatch")
        if frontmatter_value(path, "status") != "Proposed":
            errors.append(f"{item['source_document']}: must remain Proposed")
        if frontmatter_value(path, "version") != "0.2.0-draft.1":
            errors.append(f"{item['source_document']}: version mismatch")
    if counts != {"Pass": 14, "Revise": 10, "Blocked": 3}:
        errors.append(f"dimension totals mismatch: {counts}")

    dispositions = load("standards/review/RFC_ROUND2_AMBIGUITY_DISPOSITIONS.json")
    items = dispositions["items"]
    if len(items) != 12:
        errors.append("expected 12 ambiguity dispositions")
    accepted = sum(item["round2_disposition"] == "AcceptedForInternalArchitecture" for item in items)
    revise = sum(item["round2_disposition"] == "NeedsFurtherRevision" for item in items)
    rejected = sum(item["round2_disposition"] == "Rejected" for item in items)
    if (accepted, revise, rejected) != (8, 4, 0):
        errors.append("ambiguity disposition totals mismatch")
    if any(item["status_after_round2"] != "Open" for item in items):
        errors.append("all reviewed ambiguities must remain Open")

    ambiguity_registry = load("standards/review/RFC_AMBIGUITIES.json")
    if len(ambiguity_registry["ambiguities"]) != 19:
        errors.append("ambiguity count changed")
    if any(item["status"] != "Open" for item in ambiguity_registry["ambiguities"]):
        errors.append("all 19 ambiguities must remain Open")

    source_tests = load("standards/review/RFC_SOURCE_REVIEW_TESTS.json")
    source_results = load("standards/review/RFC_SOURCE_REVIEW_TEST_RESULTS.json")
    if len(source_tests["tests"]) != 12 or len(source_results["results"]) != 12:
        errors.append("expected 12 source tests and results")
    specs = {item["test_id"]: item for item in source_tests["tests"]}
    for result in source_results["results"]:
        spec = specs.get(result["test_id"])
        if not spec:
            errors.append(f"unknown source test {result['test_id']}")
            continue
        text = RFC_PATHS[spec["source_document"]].read_text(encoding="utf-8")
        missing = [marker for marker in spec["required_markers"] if marker not in text]
        if missing or result["result"] != "Pass":
            errors.append(f"{result['test_id']}: source test failed")
        if result["source_blob_sha"] != canonical_text_blob_sha(RFC_PATHS[spec["source_document"]]):
            errors.append(f"{result['test_id']}: blob mismatch")

    requirements = load("standards/requirements/RFC_REQUIREMENTS.json")
    if len(requirements["requirements"]) != 115:
        errors.append("current requirement count must be 115")
    if requirements["round2_review"]["current_complete_index_claimed"] is not True:
        errors.append("current complete requirement index must be claimed after rebaseline")
    for item in requirements["requirements"]:
        if item["source_document"] in RFC_PATHS:
            if item.get("current_source_state") != "CurrentRebaselined":
                errors.append(f"{item['requirement_id']}: must be CurrentRebaselined")

    implementation_tests = load("standards/requirements/RFC_ACCEPTANCE_TESTS.json")
    if len(implementation_tests["tests"]) != 115:
        errors.append("implementation test count must be 115")
    if implementation_tests["round2_review"]["implementation_tests_executed"] != 0:
        errors.append("implementation tests must remain unexecuted")
    if any(item["test_state"] != "SpecificationOnly" for item in implementation_tests["tests"]):
        errors.append("implementation tests must remain SpecificationOnly")

    plan = load("standards/review/RFC_REVISION_PLAN.json")
    statuses = {item["revision_id"]: item["status"] for item in plan["items"]}
    accepted_ids = {"REV-0001","REV-0002","REV-0004","REV-0005","REV-0008","REV-0009","REV-0010","REV-0012"}
    revise_ids = {"REV-0003","REV-0006","REV-0007","REV-0011"}
    if any(statuses.get(rid) != "InternallyAcceptedPendingExternalReview" for rid in accepted_ids):
        errors.append("accepted revision statuses mismatch")
    if any(statuses.get(rid) not in {"NeedsFurtherRevision", "ProfileDesignedPendingReview", "ProfileReviewedNeedsRevision", "ProfileInternallyReadyPendingAffectedPersonReview"} for rid in revise_ids):
        errors.append("residual revision statuses mismatch")

    dissent = load("standards/review/RFC_DISSENT_REGISTER.json")
    if len(dissent["items"]) != 8 or any(item["status"] != "Open" for item in dissent["items"]):
        errors.append("all dissent must remain Open")

    baseline = load("standards/conformance/FOUNDATION_CONFORMANCE_BASELINE.json")
    if baseline["results"] != []:
        errors.append("implementation baseline must remain empty")
    if baseline["round2_review"]["product_implementation_tests_executed"] != 0:
        errors.append("product tests must remain zero")

    residual = load("standards/review/RFC_R2_RESIDUAL_PLAN.json")
    residual_states = {item["item_id"]: item["status"] for item in residual["items"]}
    if len(residual_states) != 7:
        errors.append("residual plan item count mismatch")
    for iid in {"R2R-001", "R2R-002", "R2R-003", "R2R-004"}:
        if residual_states.get(iid) not in {"Planned", "DesignedPendingReview", "ReviewedNeedsRevision", "InternallyReadyPendingAffectedPersonReview"}:
            errors.append(f"{iid}: invalid residual design state")
    for iid in {"R2R-005", "R2R-006"}:
        if residual_states.get(iid) not in {"Planned", "Complete"}:
            errors.append(f"{iid}: invalid rebaseline state")
    if residual_states.get("R2R-007") not in {"Planned", "PreparedNotExecuted", "ContentReadyOperationallyBlocked"}:
        errors.append("R2R-007 must remain Planned or PreparedNotExecuted")

    if errors:
        print("Round 2 review validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        "Round 2 review validation passed. "
        "Validated 3 RFC reviews, 27 dimension dispositions, "
        "12 ambiguity decisions (8 internally accepted, 4 needing revision), "
        "12 passed repository source tests, 115 current requirements, "
        "115 unexecuted implementation test specifications, 19 open ambiguities, "
        "8 open dissent items, 7 tracked residual items, and an empty implementation baseline."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
