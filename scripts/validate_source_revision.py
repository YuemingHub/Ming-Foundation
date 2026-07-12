#!/usr/bin/env python3
"""Validate Day 11 R0/R1 source revisions without implying promotion."""

from __future__ import annotations
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DRAFT = "0.2.0-draft.1"

RFC_PATHS = {
    "RFC-0001": ROOT / "standards/rfc/RFC-0001-subject-speaker-and-contestability.md",
    "RFC-0002": ROOT / "standards/rfc/RFC-0002-consent-and-data-rights-lifecycle.md",
    "RFC-0003": ROOT / "standards/rfc/RFC-0003-safety-escalation-handoff-appeal-and-incident.md",
    "RFC-0004": ROOT / "standards/rfc/RFC-0004-case-and-cross-family-evidence-governance.md",
    "RFC-0005": ROOT / "standards/rfc/RFC-0005-public-claim-charter-sync-and-capability-status.md",
}

REQUIRED_MARKERS = {
    "RFC-0001": [
        "## 2. Shared decision terms",
        "### 2.1 Material assertion",
        "### 2.2 High-impact use",
        "### 2.3 Representative",
        "### 2.4 Governed disclosure basis",
        "## 9. Migration, correction propagation, and lineage",
    ],
    "RFC-0002": [
        "## 2. Jurisdiction and basis boundary",
        "## 4. Processing-basis categories",
        "### 5.3 Representative authority",
        "## 6. Retention profiles",
        "## 8. Cross-channel authority and conflict resolution",
        "## 9. Migration, lineage, and completion",
    ],
    "RFC-0003": [
        "### 2.1 High-impact safety action",
        "### 2.2 P0 and P1",
        "## 3. Service availability profiles",
        "## 5. Proportionality record",
        "## 9. Operator may be the risk source",
        "## 10. Migration and correction propagation",
    ],
}


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    data = {}
    for line in text[4:end].splitlines():
        if line.startswith(" ") or line.startswith("-") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        if value.strip():
            data[key.strip()] = value.strip()
    return data


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def main() -> int:
    errors = []

    for rfc_id in ("RFC-0001", "RFC-0002", "RFC-0003"):
        path = RFC_PATHS[rfc_id]
        meta = frontmatter(path)
        if meta.get("status") != "Proposed":
            errors.append(f"{rfc_id}: status must remain Proposed")
        if meta.get("version") != DRAFT:
            errors.append(f"{rfc_id}: expected version {DRAFT}")
        text = path.read_text(encoding="utf-8")
        for marker in REQUIRED_MARKERS[rfc_id]:
            if marker not in text:
                errors.append(f"{rfc_id}: missing {marker}")

    for rfc_id in ("RFC-0004", "RFC-0005"):
        meta = frontmatter(RFC_PATHS[rfc_id])
        if meta.get("status") != "Proposed" or meta.get("version") != "0.1.0":
            errors.append(f"{rfc_id}: R2 source must remain Proposed 0.1.0")

    plan = load("standards/review/RFC_REVISION_PLAN.json")
    statuses = {item["revision_id"]: item["status"] for item in plan["items"]}
    for number in range(1, 13):
        if statuses.get(f"REV-{number:04d}") not in {"ImplementedPendingReview", "InternallyAcceptedPendingExternalReview", "NeedsFurtherRevision"}:
            errors.append(f"REV-{number:04d}: invalid reviewed revision status")
    for number in range(13, 20):
        if statuses.get(f"REV-{number:04d}") != "Planned":
            errors.append(f"REV-{number:04d}: R2 item must remain Planned")
    for number in range(1, 5):
        if statuses.get(f"REV-X{number:03d}") != "PartiallyImplemented":
            errors.append(f"REV-X{number:03d}: must be PartiallyImplemented")

    ambiguity_data = load("standards/review/RFC_AMBIGUITIES.json")
    ambiguities = ambiguity_data["ambiguities"]
    if len(ambiguities) != 19 or any(item["status"] != "Open" for item in ambiguities):
        errors.append("all 19 ambiguities must remain Open")
    for item in ambiguities:
        number = int(item["ambiguity_id"].split("-")[1])
        expected = "ImplementedPendingReview" if number <= 12 else "Planned"
        if item.get("source_revision_state") != expected:
            errors.append(f"{item['ambiguity_id']}: expected {expected}")

    requirements = load("standards/requirements/RFC_REQUIREMENTS.json")
    sources = {item["id"]: item for item in requirements["source_documents"]}
    for rfc_id in ("RFC-0001", "RFC-0002", "RFC-0003"):
        if sources[rfc_id]["version"] != DRAFT:
            errors.append(f"{rfc_id}: requirement source version mismatch")
        if sources[rfc_id]["source_blob_sha"] != blob_sha(RFC_PATHS[rfc_id]):
            errors.append(f"{rfc_id}: source blob SHA mismatch")
    if len(requirements["requirements"]) != 63:
        errors.append("requirement count must remain 63")
    for item in requirements["requirements"]:
        if item["source_document"] in {"RFC-0001", "RFC-0002", "RFC-0003"}:
            if item.get("current_source_state") not in {"RevisedPendingReview", "LegacyIndexPendingRebaseline"}:
                errors.append(f"{item['requirement_id']}: current source state mismatch")

    tests = load("standards/requirements/RFC_ACCEPTANCE_TESTS.json")
    if len(tests["tests"]) != 63:
        errors.append("acceptance test count must remain 63")
    for test in tests["tests"]:
        if test["source_document"] in {"RFC-0001", "RFC-0002", "RFC-0003"}:
            if test.get("revision_state") != "UpdatedPendingExecution":
                errors.append(f"{test['test_id']}: revision state mismatch")
            if test.get("test_state") != "SpecificationOnly":
                errors.append(f"{test['test_id']}: test must remain SpecificationOnly")

    dissent = load("standards/review/RFC_DISSENT_REGISTER.json")
    if len(dissent["items"]) != 8 or any(item["status"] != "Open" for item in dissent["items"]):
        errors.append("all eight dissent items must remain Open")

    baseline = load("standards/conformance/FOUNDATION_CONFORMANCE_BASELINE.json")
    if baseline.get("results") != []:
        errors.append("implementation conformance baseline must remain empty")
    if baseline.get("day11_source_revision", {}).get("implementation_results_populated") is not False:
        errors.append("source revision must not populate conformance results")

    for rel in [
        "governance/decisions/ADR-0013-r0-cross-rfc-revision-foundations.md",
        "governance/decisions/ADR-0014-retain-r1-revised-rfcs-proposed.md",
        "governance/remediation/GOV-0044-day11-r0-r1-source-revision-record.md",
        "governance/reviews/GOV-0048-r0-r1-ambiguity-source-disposition.md",
    ]:
        text = (ROOT / rel).read_text(encoding="utf-8")
        if "status: Accepted" not in text:
            errors.append(f"{rel}: must be Accepted")

    if errors:
        print("Source-revision validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        "Source-revision validation passed. "
        "Validated 3 revised RFC drafts, 12 implemented-pending-review items, "
        "4 partially implemented cross-RFC items, 7 planned R2 items, "
        "19 open ambiguities, 63 requirements, 63 unexecuted test specifications, "
        "8 open dissent items, and an empty implementation baseline."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
