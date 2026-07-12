#!/usr/bin/env python3
"""Validate the current requirement and implementation-test registries."""

from pathlib import Path
from validation_utils import canonical_text_blob_sha
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "standards/requirements/RFC_REQUIREMENTS.json"
TESTS = ROOT / "standards/requirements/RFC_ACCEPTANCE_TESTS.json"
AMB = ROOT / "standards/review/RFC_AMBIGUITIES.json"

RFC_PATHS = {
    "RFC-0001": ROOT / "standards/rfc/RFC-0001-subject-speaker-and-contestability.md",
    "RFC-0002": ROOT / "standards/rfc/RFC-0002-consent-and-data-rights-lifecycle.md",
    "RFC-0003": ROOT / "standards/rfc/RFC-0003-safety-escalation-handoff-appeal-and-incident.md",
    "RFC-0004": ROOT / "standards/rfc/RFC-0004-case-and-cross-family-evidence-governance.md",
    "RFC-0005": ROOT / "standards/rfc/RFC-0005-public-claim-charter-sync-and-capability-status.md",
}


def main():
    errors = []
    req = json.loads(REQ.read_text(encoding="utf-8"))
    tests = json.loads(TESTS.read_text(encoding="utf-8"))
    ambiguities = json.loads(AMB.read_text(encoding="utf-8"))

    requirements = req.get("requirements", [])
    test_items = tests.get("tests", [])
    if len(req.get("source_documents", [])) != 5:
        errors.append("expected 5 RFC sources")
    if len(requirements) != 115:
        errors.append(f"expected 115 current requirements, found {len(requirements)}")
    if len(test_items) != 115:
        errors.append(f"expected 115 current test specifications, found {len(test_items)}")
    if len(ambiguities.get("ambiguities", [])) != 19:
        errors.append("expected 19 ambiguities")

    req_ids = [item.get("requirement_id") for item in requirements]
    test_ids = [item.get("test_id") for item in test_items]
    if len(set(req_ids)) != 115:
        errors.append("requirement IDs are not unique")
    if len(set(test_ids)) != 115:
        errors.append("test IDs are not unique")

    source_docs = {item["id"]: item for item in req["source_documents"]}
    if set(source_docs) != set(RFC_PATHS):
        errors.append("RFC source coverage mismatch")
    for rfc, path in RFC_PATHS.items():
        if source_docs[rfc]["source_blob_sha"] != canonical_text_blob_sha(path):
            errors.append(f"{rfc}: source blob mismatch")

    test_by_id = {item["test_id"]: item for item in test_items}
    counts = {}
    for item in requirements:
        rid = item["requirement_id"]
        rfc = item["source_document"]
        counts[rfc] = counts.get(rfc, 0) + 1
        if not re.fullmatch(r"RFC-\d{4}-R\d{3}", rid):
            errors.append(f"{rid}: invalid requirement ID")
        refs = item.get("acceptance_test_refs", [])
        if len(refs) != 1 or refs[0] not in test_by_id:
            errors.append(f"{rid}: acceptance-test mapping mismatch")
        elif test_by_id[refs[0]].get("requirement_id") != rid:
            errors.append(f"{rid}: reverse test mapping mismatch")
        if item.get("baseline_state") != "Current":
            errors.append(f"{rid}: baseline_state must be Current")
        if item.get("current_source_state") not in {"CurrentRebaselined", "CurrentConfirmed"}:
            errors.append(f"{rid}: invalid current source state")
        if rfc in {"RFC-0001", "RFC-0002", "RFC-0003"}:
            marker = item.get("source_marker")
            if not marker or marker not in RFC_PATHS[rfc].read_text(encoding="utf-8"):
                errors.append(f"{rid}: source marker not found")
        for pref in item.get("profile_refs", []):
            if not re.fullmatch(r"PROF-\d{4}", pref):
                errors.append(f"{rid}: invalid profile ref {pref}")

    if counts != {
        "RFC-0001": 29,
        "RFC-0002": 34,
        "RFC-0003": 28,
        "RFC-0004": 13,
        "RFC-0005": 11,
    }:
        errors.append(f"requirement count by RFC mismatch: {counts}")

    if any(item.get("test_state") != "SpecificationOnly" for item in test_items):
        errors.append("implementation tests must remain SpecificationOnly")
    if any(item.get("automation_state") != "NotImplemented" for item in test_items):
        errors.append("implementation tests must remain NotImplemented")

    if errors:
        print("Requirement validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1
    print(
        "Requirement validation passed. Validated 5 RFC sources, "
        "115 current requirements, 115 current acceptance-test specifications, "
        "and 19 ambiguities."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
