#!/usr/bin/env python3
"""Validate Day 9 RFC review preparation and non-claiming baseline."""

from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "standards/requirements/RFC_REQUIREMENTS.json"
TESTS = ROOT / "standards/requirements/RFC_ACCEPTANCE_TESTS.json"
CHECKLISTS = ROOT / "standards/review/RFC_REVIEW_CHECKLISTS.json"
AMBIGUITIES = ROOT / "standards/review/RFC_AMBIGUITIES.json"
BASELINE = ROOT / "standards/conformance/FOUNDATION_CONFORMANCE_BASELINE.json"

EXPECTED_RFCS = {f"RFC-{number:04d}" for number in range(1, 6)}
EXPECTED_DIMENSIONS = {
    "scope_and_definitions",
    "architecture_and_data_model",
    "human_agency_and_ethics",
    "privacy_and_consent",
    "safety_and_escalation",
    "implementation_and_conformance",
    "affected_person_or_domain_review",
    "compatibility_and_migration",
    "evidence_and_limitations",
}


def main() -> int:
    errors: list[str] = []

    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    requirement_ids = {
        item["requirement_id"] for item in registry.get("requirements", [])
    }
    if len(requirement_ids) != 63:
        errors.append(f"expected 63 requirements, found {len(requirement_ids)}")

    tests = json.loads(TESTS.read_text(encoding="utf-8"))
    test_ids = {item["test_id"] for item in tests.get("tests", [])}
    tested_requirements = {
        item["requirement_id"] for item in tests.get("tests", [])
    }
    if len(test_ids) != 63:
        errors.append(f"expected 63 unique tests, found {len(test_ids)}")
    if tested_requirements != requirement_ids:
        errors.append("acceptance tests do not cover exactly the registered requirements")

    checklists = json.loads(CHECKLISTS.read_text(encoding="utf-8"))
    checklist_rfcs = {item["source_document"] for item in checklists.get("checklists", [])}
    if checklist_rfcs != EXPECTED_RFCS:
        errors.append(f"checklist RFC coverage mismatch: {sorted(checklist_rfcs)}")
    for checklist in checklists.get("checklists", []):
        if checklist.get("review_state") != "Prepared":
            errors.append(f"{checklist.get('checklist_id')}: state must be Prepared")
        if checklist.get("promotion_recommendation") != "RetainProposed":
            errors.append(f"{checklist.get('checklist_id')}: must retain Proposed")
        dimensions = {item["dimension"] for item in checklist.get("dimensions", [])}
        if dimensions != EXPECTED_DIMENSIONS:
            errors.append(f"{checklist.get('checklist_id')}: dimension coverage mismatch")

    ambiguity_data = json.loads(AMBIGUITIES.read_text(encoding="utf-8"))
    ambiguities = ambiguity_data.get("ambiguities", [])
    ambiguity_ids = {item["ambiguity_id"] for item in ambiguities}
    if len(ambiguity_ids) != 19:
        errors.append(f"expected 19 ambiguities, found {len(ambiguity_ids)}")
    if any(item.get("status") != "Open" for item in ambiguities):
        errors.append("Day 9 ambiguities must remain Open")
    for item in ambiguities:
        for rid in item.get("affected_requirements", []):
            if rid not in requirement_ids:
                errors.append(f"{item.get('ambiguity_id')}: unknown requirement {rid}")

    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    if baseline.get("canonical_repository") != "YuemingHub/Ming-Foundation":
        errors.append("baseline canonical repository is incorrect")
    if set(baseline.get("selected_requirements", [])) != requirement_ids:
        errors.append("baseline does not enumerate all requirements")
    if baseline.get("results") != []:
        errors.append("Day 9 baseline results must be intentionally empty")
    boundary = baseline.get("claim_boundary", {})
    for field in (
        "implementation_target_selected",
        "product_conformance_claimed",
        "charter_validation_claimed",
    ):
        if boundary.get(field) is not False:
            errors.append(f"baseline claim boundary {field} must be false")

    template_files = [
        ROOT / f"governance/templates/gov-tpl-{number:04d}-rfc-{number-4:04d}-review-checklist.md"
        for number in range(5, 10)
    ]
    for path in template_files:
        if not path.exists():
            errors.append(f"missing checklist template {path.relative_to(ROOT)}")

    if errors:
        print("Review-baseline validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        "Review-baseline validation passed. "
        "Validated 5 RFC checklists, 63 tests, 19 ambiguities, "
        "and an empty 63-requirement baseline."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
