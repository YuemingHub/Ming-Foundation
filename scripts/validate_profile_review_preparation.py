#!/usr/bin/env python3
"""Validate Day 14 Profile review and affected-person preparation boundaries."""

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

TEMPLATES = [
    ROOT / f"governance/templates/GOV-TPL-{number:04d}-" / "unused"
    for number in range(10, 18)
]

TEMPLATE_PATHS = [
    ROOT / "governance/templates/GOV-TPL-0010-child-friendly-profile-review-guide.md",
    ROOT / "governance/templates/GOV-TPL-0011-adolescent-profile-review-guide.md",
    ROOT / "governance/templates/GOV-TPL-0012-parent-caregiver-representative-review-guide.md",
    ROOT / "governance/templates/GOV-TPL-0013-practitioner-domain-review-guide.md",
    ROOT / "governance/templates/GOV-TPL-0014-privacy-safety-review-guide.md",
    ROOT / "governance/templates/GOV-TPL-0015-accessibility-language-review-guide.md",
    ROOT / "governance/templates/GOV-TPL-0016-jurisdiction-professional-duty-review-guide.md",
    ROOT / "governance/templates/GOV-TPL-0017-affected-person-review-session-record.md",
]

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

    review = load("standards/review/PROFILE_INTERNAL_REVIEW_RESULTS.json")
    scope = review["review_scope"]
    if scope["round"] != "ProfileInternalReviewRound1" or scope["complete"] is not True:
        errors.append("profile review scope mismatch")
    for key in [
        "affected_person_review_complete",
        "domain_review_complete",
        "jurisdiction_review_complete",
        "implementation_conformance_complete",
    ]:
        if scope[key] is not False:
            errors.append(f"{key} must remain false")

    summary = review["summary"]
    actual = (
        summary["profile_count"], summary["dimension_count"],
        summary["pass"], summary["revise"], summary["blocked"],
    )
    if actual != (4, 32, 13, 15, 4):
        errors.append(f"profile review summary mismatch: {actual}")

    results = review["results"]
    if {item["source_document"] for item in results} != set(PROFILE_PATHS):
        errors.append("profile review coverage mismatch")
    dimension_counts = {"Pass": 0, "Revise": 0, "Blocked": 0}
    for item in results:
        pid = item["source_document"]
        if item["review_state"] != "Complete":
            errors.append(f"{pid}: review not complete")
        if item["overall_disposition"] != "ReviseAndRetainProposed":
            errors.append(f"{pid}: disposition mismatch")
        if item["promotion_recommendation"] != "RetainProposed":
            errors.append(f"{pid}: promotion mismatch")
        if len(item["dimensions"]) != 8:
            errors.append(f"{pid}: expected eight dimensions")
        for dimension in item["dimensions"]:
            dimension_counts[dimension["disposition"]] += 1
        if item["source_blob_sha"] != canonical_text_blob_sha(PROFILE_PATHS[pid]):
            errors.append(f"{pid}: source blob mismatch")
        if frontmatter_status(PROFILE_PATHS[pid]) != "Proposed":
            errors.append(f"{pid}: must remain Proposed")
    if dimension_counts != {"Pass": 13, "Revise": 15, "Blocked": 4}:
        errors.append(f"dimension total mismatch: {dimension_counts}")

    revisions = load("standards/review/PROFILE_REVISION_PLAN.json")
    if len(revisions["items"]) != 16:
        errors.append("expected 16 profile revision items")
    if sum(item["priority"] == "P0" for item in revisions["items"]) != 10:
        errors.append("expected 10 P0 revision items")
    if sum(item["priority"] == "P1" for item in revisions["items"]) != 6:
        errors.append("expected 6 P1 revision items")
    if any(item["status"] != "Planned" for item in revisions["items"]):
        errors.append("profile revision items must remain Planned")

    plan = load("standards/review/AFFECTED_PERSON_REVIEW_PLAN.json")
    if plan["execution_state"] != "PreparedNotExecuted":
        errors.append("affected-person plan must remain PreparedNotExecuted")
    if len(plan["tracks"]) != 7:
        errors.append("expected seven review tracks")
    if any(item["status"] != "PreparedNotExecuted" for item in plan["tracks"]):
        errors.append("all review tracks must remain PreparedNotExecuted")
    if (
        plan["summary"]["executed"] != 0
        or plan["summary"]["participants_recruited"] != 0
        or plan["summary"]["sessions_completed"] != 0
        or plan["summary"]["results_recorded"] != 0
    ):
        errors.append("affected-person execution evidence must remain zero")

    instruments = load("standards/review/AFFECTED_PERSON_REVIEW_INSTRUMENTS.json")
    if len(instruments["instruments"]) != 8:
        errors.append("expected eight review instruments")
    if any(item["execution_state"] != "NotExecuted" for item in instruments["instruments"]):
        errors.append("review instruments must remain NotExecuted")

    safeguards = load("standards/review/AFFECTED_PERSON_REVIEW_SAFEGUARDS.json")
    if safeguards["execution_state"] != "PreparedNotExecuted":
        errors.append("safeguards execution state mismatch")
    if len(safeguards["required_safeguards"]) < 10:
        errors.append("insufficient required safeguards")
    if len(safeguards["prohibited_collection"]) < 5:
        errors.append("insufficient prohibited-collection controls")

    for path in TEMPLATE_PATHS:
        if not path.exists() or frontmatter_status(path) != "Accepted":
            errors.append(f"{path.relative_to(ROOT)}: template missing or not Accepted")

    profiles = load("standards/profiles/RESIDUAL_PROFILE_REGISTRY.json")
    if len(profiles["profiles"]) != 4:
        errors.append("profile registry count mismatch")
    for item in profiles["profiles"]:
        if item["status"] != "Proposed":
            errors.append(f"{item['id']}: must remain Proposed")
        if item["internal_review_state"] != "Complete":
            errors.append(f"{item['id']}: internal review state mismatch")
        if item["disposition"] != "ReviseAndRetainProposed":
            errors.append(f"{item['id']}: disposition mismatch")
        if item["affected_person_review_state"] != "PreparedNotExecuted":
            errors.append(f"{item['id']}: affected-person state mismatch")

    residual = load("standards/review/RFC_R2_RESIDUAL_PLAN.json")
    states = {item["item_id"]: item["status"] for item in residual["items"]}
    for iid in {"R2R-001", "R2R-002", "R2R-003", "R2R-004"}:
        if states.get(iid) != "ReviewedNeedsRevision":
            errors.append(f"{iid}: must be ReviewedNeedsRevision")
    for iid in {"R2R-005", "R2R-006"}:
        if states.get(iid) != "Complete":
            errors.append(f"{iid}: must remain Complete")
    if states.get("R2R-007") != "PreparedNotExecuted":
        errors.append("R2R-007 must be PreparedNotExecuted")

    ambiguities = load("standards/review/RFC_AMBIGUITIES.json")
    if len(ambiguities["ambiguities"]) != 19:
        errors.append("ambiguity count mismatch")
    if any(item["status"] != "Open" for item in ambiguities["ambiguities"]):
        errors.append("all ambiguities must remain Open")

    dissent = load("standards/review/RFC_DISSENT_REGISTER.json")
    if len(dissent["items"]) != 8 or any(item["status"] != "Open" for item in dissent["items"]):
        errors.append("all dissent items must remain Open")

    baseline = load("standards/conformance/FOUNDATION_CONFORMANCE_BASELINE.json")
    if baseline["results"] != []:
        errors.append("implementation conformance baseline must remain empty")
    if baseline["day14_profile_review"]["affected_person_review_executed"] is not False:
        errors.append("affected-person review must remain unexecuted")
    if baseline["day14_profile_review"]["implementation_tests_executed"] != 0:
        errors.append("implementation tests must remain zero")

    if errors:
        print("Profile-review preparation validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        "Profile-review preparation validation passed. Validated 4 Profile "
        "reviews, 32 dimensions (13 Pass, 15 Revise, 4 Blocked), 16 planned "
        "revision items, 7 prepared-not-executed review tracks, 8 unexecuted "
        "instruments, required safeguards, 19 open ambiguities, 8 open dissent "
        "items, and an empty implementation baseline."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
