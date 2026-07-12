#!/usr/bin/env python3
"""Validate Day 15 Profile source revisions and source tests."""

from pathlib import Path
import json

from validation_utils import canonical_text_blob_sha

ROOT = Path(__file__).resolve().parents[1]
CURRENT_VERSION = "0.2.0-draft.1"

PROFILE_PATHS = {
    "PROF-0001": ROOT / "standards/profiles/PROF-0001-participation-and-representative-decision-profile.md",
    "PROF-0002": ROOT / "standards/profiles/PROF-0002-representative-authority-evidence-profile.md",
    "PROF-0003": ROOT / "standards/profiles/PROF-0003-retention-and-backup-completion-profile.md",
    "PROF-0004": ROOT / "standards/profiles/PROF-0004-service-response-and-resource-freshness-profile.md",
}

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

    evidence = load("standards/review/PROFILE_SOURCE_REVISION_EVIDENCE.json")
    specs = load("standards/review/PROFILE_SOURCE_REVISION_TESTS.json")
    results = load("standards/review/PROFILE_SOURCE_REVISION_TEST_RESULTS.json")
    revisions = load("standards/review/PROFILE_REVISION_PLAN.json")
    registry = load("standards/profiles/RESIDUAL_PROFILE_REGISTRY.json")

    if len(evidence["profiles"]) != 4:
        errors.append("expected four revised Profiles")
    if evidence["summary"]["revision_items"] != 16:
        errors.append("expected 16 revision items")
    if evidence["summary"]["source_tests_passed"] != 16:
        errors.append("expected 16 passed source tests")

    evidence_by_id = {item["profile_id"]: item for item in evidence["profiles"]}
    registry_by_id = {item["id"]: item for item in registry["profiles"]}

    for pid, path in PROFILE_PATHS.items():
        item = evidence_by_id.get(pid)
        if not item:
            errors.append(f"{pid}: missing revision evidence")
            continue
        archive = ROOT / item["archive_path"]
        if not archive.exists():
            errors.append(f"{pid}: missing 0.1.0 archive")
            continue
        if item["previous_blob_sha"] != canonical_text_blob_sha(archive):
            errors.append(f"{pid}: previous blob mismatch")
        if item["current_blob_sha"] != canonical_text_blob_sha(path):
            errors.append(f"{pid}: current blob mismatch")
        if frontmatter(path, "version") != CURRENT_VERSION:
            errors.append(f"{pid}: current version mismatch")
        if frontmatter(path, "status") != "Proposed":
            errors.append(f"{pid}: must remain Proposed")
        reg = registry_by_id[pid]
        if reg["version"] != CURRENT_VERSION:
            errors.append(f"{pid}: registry version mismatch")
        if reg["source_revision_state"] != "Complete":
            errors.append(f"{pid}: source revision not complete")
        if reg["source_test_state"] != "Passed":
            errors.append(f"{pid}: source tests not passed")

    if len(specs["tests"]) != 16 or len(results["results"]) != 16:
        errors.append("expected 16 source test specs and results")
    spec_by_id = {item["test_id"]: item for item in specs["tests"]}
    for result in results["results"]:
        spec = spec_by_id.get(result["test_id"])
        if not spec:
            errors.append(f"unknown source test {result['test_id']}")
            continue
        text = PROFILE_PATHS[spec["source_document"]].read_text(encoding="utf-8")
        if spec["required_marker"] not in text:
            errors.append(f"{result['test_id']}: required marker missing")
        if result["result"] != "Pass":
            errors.append(f"{result['test_id']}: result must be Pass")
        if result["source_blob_sha"] != canonical_text_blob_sha(
            PROFILE_PATHS[spec["source_document"]]
        ):
            errors.append(f"{result['test_id']}: source blob mismatch")

    if len(revisions["items"]) != 16 or any(
        item["status"] != "Complete" for item in revisions["items"]
    ):
        errors.append("all 16 Profile revisions must be Complete")

    if errors:
        print("Profile source-revision validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        "Profile source-revision validation passed. Validated 4 revised "
        "Profile sources at 0.2.0-draft.1, 4 archived 0.1.0 sources, "
        "16 completed revision items, and 16 passed source tests."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
