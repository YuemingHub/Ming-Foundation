#!/usr/bin/env python3
"""Validate the review definitions and empty current conformance baseline."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

def main():
    errors = []
    checklists = load("standards/review/RFC_REVIEW_CHECKLISTS.json")
    requirements = load("standards/requirements/RFC_REQUIREMENTS.json")
    tests = load("standards/requirements/RFC_ACCEPTANCE_TESTS.json")
    ambiguities = load("standards/review/RFC_AMBIGUITIES.json")
    baseline = load("standards/conformance/FOUNDATION_CONFORMANCE_BASELINE.json")

    if len(checklists.get("checklists", [])) != 5:
        errors.append("expected 5 RFC checklists")
    req_ids = {item["requirement_id"] for item in requirements["requirements"]}
    test_ids = {item["test_id"] for item in tests["tests"]}
    if len(req_ids) != 115:
        errors.append("expected 115 current requirements")
    if len(test_ids) != 115:
        errors.append("expected 115 current test specifications")
    if len(ambiguities["ambiguities"]) != 19:
        errors.append("expected 19 ambiguities")
    if set(baseline["selected_requirements"]) != req_ids:
        errors.append("baseline requirement coverage mismatch")
    if baseline["results"] != []:
        errors.append("implementation baseline must remain empty")
    if baseline["claim_boundary"]["implementation_target_selected"] is not False:
        errors.append("implementation target must remain unselected")
    if baseline["claim_boundary"]["product_conformance_claimed"] is not False:
        errors.append("product conformance must remain unclaimed")

    if errors:
        print("Review-baseline validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1
    print(
        "Review-baseline validation passed. Validated 5 RFC checklists, "
        "115 current test specifications, 19 ambiguities, "
        "and an empty 115-requirement baseline."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
