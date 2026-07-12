#!/usr/bin/env python3
"""Validate Day 13 requirement identity, current baseline, and residual profiles."""

from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]

def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

def status(path):
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    for line in text[4:end].splitlines():
        if line.startswith("status:"):
            return line.split(":", 1)[1].strip()
    return None

def main():
    errors = []

    current = load("standards/requirements/RFC_REQUIREMENTS.json")
    current_tests = load("standards/requirements/RFC_ACCEPTANCE_TESTS.json")
    legacy = load("standards/requirements/archive/RFC_REQUIREMENTS_DAY12_LEGACY.json")
    legacy_tests = load("standards/requirements/archive/RFC_ACCEPTANCE_TESTS_DAY12_LEGACY.json")
    mapping = load("standards/requirements/RFC_REQUIREMENT_ID_MAP.json")
    profiles = load("standards/profiles/RESIDUAL_PROFILE_REGISTRY.json")
    residual = load("standards/review/RFC_R2_RESIDUAL_PLAN.json")
    ambiguities = load("standards/review/RFC_AMBIGUITIES.json")
    dissent = load("standards/review/RFC_DISSENT_REGISTER.json")
    baseline = load("standards/conformance/FOUNDATION_CONFORMANCE_BASELINE.json")

    current_ids = {item["requirement_id"] for item in current["requirements"]}
    current_test_ids = {item["test_id"] for item in current_tests["tests"]}
    legacy_ids = {item["requirement_id"] for item in legacy["requirements"]}
    legacy_test_ids = {item["test_id"] for item in legacy_tests["tests"]}

    if len(current_ids) != 115 or len(current_test_ids) != 115:
        errors.append("current baseline must contain 115 requirements and tests")
    if len(legacy_ids) != 63 or len(legacy_test_ids) != 63:
        errors.append("legacy archive must contain 63 requirements and tests")
    if not legacy_ids.issubset(current_ids):
        errors.append("all legacy requirement IDs must be preserved")
    if len(current_ids - legacy_ids) != 52:
        errors.append("expected 52 new requirement IDs")

    mappings = mapping["legacy_mappings"]
    if len(mappings) != 63:
        errors.append("expected 63 legacy mappings")
    mapped_legacy = {item["legacy_requirement_id"] for item in mappings}
    if mapped_legacy != legacy_ids:
        errors.append("legacy mapping coverage mismatch")
    for item in mappings:
        if item["retired"] is not False:
            errors.append(f"{item['legacy_requirement_id']}: may not be retired")
        if not set(item["current_requirement_ids"]).issubset(current_ids):
            errors.append(f"{item['legacy_requirement_id']}: maps to unknown current ID")

    if mapping["summary"] != {
        "legacy_requirements": 63,
        "current_requirements": 115,
        "retained_ids": 63,
        "new_ids": 52,
        "retired_ids": 0,
        "unmapped_legacy_ids": 0,
    }:
        errors.append("mapping summary mismatch")

    profile_items = profiles["profiles"]
    if len(profile_items) != 4:
        errors.append("expected four residual profiles")
    profile_ids = {item["id"] for item in profile_items}
    if profile_ids != {"PROF-0001", "PROF-0002", "PROF-0003", "PROF-0004"}:
        errors.append("profile ID set mismatch")
    for item in profile_items:
        path = ROOT / item["path"]
        if not path.exists() or status(path) != "Proposed":
            errors.append(f"{item['id']}: profile must exist and remain Proposed")
        if item["status"] != "Proposed":
            errors.append(f"{item['id']}: registry status mismatch")

    residual_states = {item["item_id"]: item["status"] for item in residual["items"]}
    for iid in {"R2R-001", "R2R-002", "R2R-003", "R2R-004"}:
        if residual_states.get(iid) != "DesignedPendingReview":
            errors.append(f"{iid}: must be DesignedPendingReview")
    for iid in {"R2R-005", "R2R-006"}:
        if residual_states.get(iid) != "Complete":
            errors.append(f"{iid}: must be Complete")
    if residual_states.get("R2R-007") != "Planned":
        errors.append("R2R-007 must remain Planned")

    if len(ambiguities["ambiguities"]) != 19 or any(item["status"] != "Open" for item in ambiguities["ambiguities"]):
        errors.append("all 19 ambiguities must remain Open")
    profile_ambs = {"AMB-0003", "AMB-0006", "AMB-0007", "AMB-0011"}
    for item in ambiguities["ambiguities"]:
        if item["ambiguity_id"] in profile_ambs:
            if item.get("profile_design_state") != "DesignedPendingReview":
                errors.append(f"{item['ambiguity_id']}: profile state mismatch")

    if len(dissent["items"]) != 8 or any(item["status"] != "Open" for item in dissent["items"]):
        errors.append("all eight dissent items must remain Open")

    if baseline["results"] != []:
        errors.append("implementation baseline must remain empty")
    if len(baseline["selected_requirements"]) != 115:
        errors.append("baseline must select 115 current requirements")
    if baseline["day13_rebaseline"]["implementation_tests_executed"] != 0:
        errors.append("implementation tests must remain unexecuted")

    if errors:
        print("Requirement re-baseline validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        "Requirement re-baseline validation passed. "
        "Validated 115 current requirements, 115 current unexecuted test specifications, "
        "63 archived legacy requirements, 63 preserved legacy IDs, 52 new IDs, "
        "four Proposed residual profiles, two completed re-baseline items, "
        "four designed-pending-review profile items, one planned affected-person review item, "
        "19 open ambiguities, 8 open dissent items, and an empty implementation baseline."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
