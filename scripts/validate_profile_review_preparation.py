#!/usr/bin/env python3
"""Validate historical Day 14 review and current preparation boundaries."""

from pathlib import Path
import json

from validation_utils import canonical_text_blob_sha

ROOT = Path(__file__).resolve().parents[1]

CURRENT_PROFILE_PATHS = {
    "PROF-0001": ROOT / "standards/profiles/PROF-0001-participation-and-representative-decision-profile.md",
    "PROF-0002": ROOT / "standards/profiles/PROF-0002-representative-authority-evidence-profile.md",
    "PROF-0003": ROOT / "standards/profiles/PROF-0003-retention-and-backup-completion-profile.md",
    "PROF-0004": ROOT / "standards/profiles/PROF-0004-service-response-and-resource-freshness-profile.md",
}

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

def frontmatter(path, key):
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    for line in text[4:end].splitlines():
        if line.startswith(f"{key}:"):
            return line.split(":", 1)[1].strip()
    return None

def main():
    errors = []

    round1 = load("standards/review/PROFILE_INTERNAL_REVIEW_RESULTS.json")
    if round1["review_scope"]["round"] != "ProfileInternalReviewRound1":
        errors.append("Round 1 identity mismatch")
    summary = round1["summary"]
    if (
        summary["profile_count"], summary["dimension_count"],
        summary["pass"], summary["revise"], summary["blocked"]
    ) != (4, 32, 13, 15, 4):
        errors.append("Round 1 summary mismatch")

    for item in round1["results"]:
        archive = ROOT / item["source_archive_path"]
        if not archive.exists():
            errors.append(f"{item['source_document']}: missing Round 1 source archive")
            continue
        if item["source_blob_sha"] != canonical_text_blob_sha(archive):
            errors.append(f"{item['source_document']}: historical source blob mismatch")
        if frontmatter(archive, "version") != "0.1.0":
            errors.append(f"{item['source_document']}: historical version mismatch")
        if item.get("historical") is not True:
            errors.append(f"{item['source_document']}: Round 1 must be historical")

    revisions = load("standards/review/PROFILE_REVISION_PLAN.json")
    if len(revisions["items"]) != 16:
        errors.append("expected 16 Profile revision items")
    if any(item["status"] != "Complete" for item in revisions["items"]):
        errors.append("all Profile revision items must be Complete after Day 15")

    plan = load("standards/review/AFFECTED_PERSON_REVIEW_PLAN.json")
    if plan["execution_state"] != "PreparedNotExecuted":
        errors.append("affected-person plan must remain PreparedNotExecuted")
    if len(plan["tracks"]) != 7:
        errors.append("expected seven review tracks")
    if any(item["status"] != "PreparedNotExecuted" for item in plan["tracks"]):
        errors.append("all tracks must remain PreparedNotExecuted")
    for key in ["executed", "participants_recruited", "sessions_completed", "results_recorded"]:
        if plan["summary"][key] != 0:
            errors.append(f"affected-person summary {key} must remain zero")
    if plan["scheduling_authorized"] is not False:
        errors.append("scheduling must remain unauthorized")
    if plan["recruitment_authorized"] is not False:
        errors.append("recruitment must remain unauthorized")
    if plan["sessions_authorized"] is not False:
        errors.append("sessions must remain unauthorized")

    instruments = load("standards/review/AFFECTED_PERSON_REVIEW_INSTRUMENTS.json")
    if len(instruments["instruments"]) != 8:
        errors.append("expected eight review instruments")
    if any(item["execution_state"] != "NotExecuted" for item in instruments["instruments"]):
        errors.append("all review instruments must remain NotExecuted")

    safeguards = load("standards/review/AFFECTED_PERSON_REVIEW_SAFEGUARDS.json")
    if safeguards["execution_state"] != "PreparedNotExecuted":
        errors.append("safeguards execution state mismatch")
    if len(safeguards["required_safeguards"]) < 10:
        errors.append("insufficient safeguards")
    if len(safeguards["prohibited_collection"]) < 5:
        errors.append("insufficient prohibited collection controls")

    for path in TEMPLATE_PATHS:
        if not path.exists() or frontmatter(path, "status") != "Accepted":
            errors.append(f"{path.relative_to(ROOT)}: template missing or not Accepted")

    profiles = load("standards/profiles/RESIDUAL_PROFILE_REGISTRY.json")
    for item in profiles["profiles"]:
        path = CURRENT_PROFILE_PATHS[item["id"]]
        if item["status"] != "Proposed" or frontmatter(path, "status") != "Proposed":
            errors.append(f"{item['id']}: must remain Proposed")
        if item["affected_person_review_state"] != "PreparedNotExecuted":
            errors.append(f"{item['id']}: affected-person state mismatch")

    ambiguities = load("standards/review/RFC_AMBIGUITIES.json")
    if len(ambiguities["ambiguities"]) != 19 or any(
        item["status"] != "Open" for item in ambiguities["ambiguities"]
    ):
        errors.append("all 19 ambiguities must remain Open")

    dissent = load("standards/review/RFC_DISSENT_REGISTER.json")
    if len(dissent["items"]) != 8 or any(item["status"] != "Open" for item in dissent["items"]):
        errors.append("all eight dissent items must remain Open")

    baseline = load("standards/conformance/FOUNDATION_CONFORMANCE_BASELINE.json")
    if baseline["results"] != []:
        errors.append("implementation conformance baseline must remain empty")

    if errors:
        print("Profile-review preparation validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        "Profile-review preparation validation passed. Validated historical "
        "Round 1 evidence against four archived Profile sources, 16 completed "
        "revision items, 7 prepared-not-executed tracks, 8 unexecuted "
        "instruments, required safeguards, 19 open ambiguities, 8 open dissent "
        "items, and an empty implementation baseline."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
