#!/usr/bin/env python3
"""Validate the machine-readable RFC requirement registry and examples."""

from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "standards/requirements/RFC_REQUIREMENTS.json"
MATRIX = ROOT / "reference/examples/conformance-matrix.example.json"
EVIDENCE = ROOT / "reference/examples/external-implementation-evidence.example.json"
TESTS = ROOT / "standards/requirements/RFC_ACCEPTANCE_TESTS.json"
AMBIGUITIES = ROOT / "standards/review/RFC_AMBIGUITIES.json"

REQ_ID = re.compile(r"^RFC-\d{4}-R\d{3}$")
RFC_ID = re.compile(r"^RFC-\d{4}$")
LEVELS = {"MUST", "MUST_NOT", "SHOULD", "SHOULD_NOT", "MAY", "UNSPECIFIED"}
STATES = {"Implemented", "Partial", "Absent", "Conflicting", "Unverifiable", "NotApplicable"}


def parse_scalar_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    data: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        if raw.startswith(" ") or raw.startswith("-") or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        if value.strip():
            data[key.strip()] = value.strip()
    return data


def main() -> int:
    errors: list[str] = []

    if not REGISTRY.exists():
        print("Requirement validation failed:\n - missing registry")
        return 1

    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if data.get("canonical_repository") != "YuemingHub/Ming-Foundation":
        errors.append("registry canonical_repository is incorrect")
    if data.get("authority", {}).get("governing_decision") != "ADR-0010":
        errors.append("registry does not identify ADR-0010")
    if "never overrides" not in data.get("authority", {}).get("registry_role", ""):
        errors.append("registry authority boundary is missing")

    source_docs: dict[str, dict] = {}
    for source in data.get("source_documents", []):
        sid = source.get("id", "")
        if not RFC_ID.match(sid):
            errors.append(f"invalid source document ID {sid!r}")
            continue
        path = ROOT / source.get("path", "")
        if not path.exists():
            errors.append(f"{sid}: source file does not exist")
            continue
        meta = parse_scalar_frontmatter(path)
        if meta.get("id") != sid:
            errors.append(f"{sid}: source frontmatter ID mismatch")
        if meta.get("status") != source.get("status"):
            errors.append(f"{sid}: source status mismatch")
        if meta.get("version") != source.get("version"):
            errors.append(f"{sid}: source version mismatch")
        source_docs[sid] = source

    seen: set[str] = set()
    test_refs: set[str] = set()
    ambiguity_refs: set[str] = set()
    coverage: dict[str, int] = {sid: 0 for sid in source_docs}
    for requirement in data.get("requirements", []):
        rid = requirement.get("requirement_id", "")
        if not REQ_ID.match(rid):
            errors.append(f"invalid requirement ID {rid!r}")
        if rid in seen:
            errors.append(f"duplicate requirement ID {rid}")
        seen.add(rid)
        source = requirement.get("source_document")
        if source not in source_docs:
            errors.append(f"{rid}: unknown source document {source!r}")
        else:
            coverage[source] += 1
        if requirement.get("normative_level") not in LEVELS:
            errors.append(f"{rid}: invalid normative level")
        if not requirement.get("source_section"):
            errors.append(f"{rid}: missing source_section")
        if not requirement.get("statement"):
            errors.append(f"{rid}: missing statement")
        if not requirement.get("verification_methods"):
            errors.append(f"{rid}: missing verification_methods")
        if not requirement.get("evidence_types"):
            errors.append(f"{rid}: missing evidence_types")
        if requirement.get("implementation_neutral") is not True:
            errors.append(f"{rid}: implementation_neutral must be true")
        refs = requirement.get("acceptance_test_refs", [])
        if not refs:
            errors.append(f"{rid}: missing acceptance_test_refs")
        test_refs.update(refs)
        fidelity = requirement.get("fidelity_review", {})
        if fidelity.get("state") != "Confirmed":
            errors.append(f"{rid}: fidelity state is not Confirmed")
        ambiguity_refs.update(fidelity.get("ambiguity_refs", []))

    for source, count in coverage.items():
        if count < 5:
            errors.append(f"{source}: only {count} registered requirements")

    tests_data = json.loads(TESTS.read_text(encoding="utf-8"))
    test_ids = {test.get("test_id") for test in tests_data.get("tests", [])}
    if len(test_ids) != 63:
        errors.append(f"expected 63 unique acceptance tests, found {len(test_ids)}")
    for test in tests_data.get("tests", []):
        if test.get("requirement_id") not in seen:
            errors.append(f"{test.get('test_id')}: unknown requirement")
        if test.get("test_state") != "SpecificationOnly":
            errors.append(f"{test.get('test_id')}: Day 9 test must remain SpecificationOnly")
    for ref in test_refs:
        if ref not in test_ids:
            errors.append(f"requirement references unknown acceptance test {ref}")

    ambiguity_data = json.loads(AMBIGUITIES.read_text(encoding="utf-8"))
    ambiguity_ids = {item.get("ambiguity_id") for item in ambiguity_data.get("ambiguities", [])}
    for ref in ambiguity_refs:
        if ref not in ambiguity_ids:
            errors.append(f"requirement references unknown ambiguity {ref}")

    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    if matrix.get("canonical_repository") != "YuemingHub/Ming-Foundation":
        errors.append("example matrix canonical_repository is incorrect")
    for result in matrix.get("results", []):
        rid = result.get("requirement_id")
        if rid not in seen:
            errors.append(f"example matrix references unknown requirement {rid}")
        if result.get("state") not in STATES:
            errors.append(f"example matrix has invalid state for {rid}")
        if result.get("state") == "NotApplicable" and not result.get("not_applicable_reason"):
            errors.append(f"{rid}: NotApplicable requires a reason")

    evidence = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    if evidence.get("non_blocking_for_canonical_repository") is not True:
        errors.append("external evidence example must be non-blocking")
    for rid in evidence.get("related_requirements", []):
        if rid not in seen:
            errors.append(f"external evidence example references unknown requirement {rid}")

    if errors:
        print("Requirement validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        "Requirement validation passed. "
        f"Validated {len(source_docs)} RFC sources, {len(seen)} requirements, "
        f"{len(test_ids)} acceptance tests, and {len(ambiguity_ids)} ambiguities."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
