#!/usr/bin/env python3
"""Validate the governed MingOS Kernel specification family."""

from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_DOCS = {
    "KERNEL-0000": ROOT / "standards/kernel/KERNEL-0000-specification-family-index.md",
    "KERNEL-0001": ROOT / "standards/kernel/KERNEL-0001-core-operational-contract.md",
}
RESERVED_NOT_CREATED = ["KERNEL-0002", "KERNEL-0003", "KERNEL-0004", "KERNEL-0005"]
JSON_PATH = ROOT / "reference/kernel/mingos-kernel-core-requirements.json"
REQ_PATTERN = re.compile(r"^\|\s*(KCR-\d{4})\s*\|", re.MULTILINE)

def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated frontmatter")
    out = {}
    for line in text[4:end].splitlines():
        if line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[key.strip()] = value.strip()
    return out

def main() -> int:
    errors: list[str] = []

    for doc_id, path in EXPECTED_DOCS.items():
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        meta = frontmatter(text)
        if meta.get("id") != doc_id:
            errors.append(f"{path.relative_to(ROOT)} id mismatch")
        if meta.get("status") != "Draft":
            errors.append(f"{doc_id} must remain Draft")

    for doc_id in RESERVED_NOT_CREATED:
        matches = list((ROOT / "standards/kernel").glob(f"{doc_id}-*.md"))
        if matches:
            errors.append(f"reserved document unexpectedly exists: {doc_id}")

    core_text = EXPECTED_DOCS["KERNEL-0001"].read_text(encoding="utf-8")
    requirement_ids = REQ_PATTERN.findall(core_text)
    if len(requirement_ids) != 36:
        errors.append(f"KERNEL-0001 requirement count {len(requirement_ids)} != 36")
    if len(set(requirement_ids)) != len(requirement_ids):
        errors.append("duplicate KCR IDs in KERNEL-0001")

    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    if data.get("schema") != "mingos.kernel-core-requirements.v0.1":
        errors.append("Kernel JSON schema mismatch")
    json_ids = [item["id"] for item in data.get("requirements", [])]
    if json_ids != requirement_ids:
        errors.append("Kernel JSON requirement IDs do not match Markdown order")
    integrity = data.get("integrity", {})
    if integrity.get("requirement_count") != 36:
        errors.append("Kernel JSON requirement count mismatch")
    if integrity.get("ambiguity_count") != 30:
        errors.append("Kernel JSON ambiguity count mismatch")
    if integrity.get("vocabulary_count") != 30:
        errors.append("Kernel JSON vocabulary count mismatch")
    if integrity.get("created_kernel_document_count") != 2:
        errors.append("created Kernel document count mismatch")
    if integrity.get("reserved_not_created_count") != 4:
        errors.append("reserved-not-created count mismatch")
    if integrity.get("implementation_conformance_claim") is not False:
        errors.append("implementation conformance claim must be false")
    if data.get("review", {}).get("state") != "PreparedNotExecuted":
        errors.append("review state must remain PreparedNotExecuted")
    if data.get("conformance", {}).get("current_claim") != "NoCurrentKernelConformanceClaim":
        errors.append("current Kernel conformance boundary mismatch")

    adr = (ROOT / "governance/decisions/ADR-0026-define-mingos-kernel-specification-family.md").read_text(encoding="utf-8")
    if frontmatter(adr).get("status") != "Proposed":
        errors.append("ADR-0026 must remain Proposed")
    state = (ROOT / "governance/status/GOV-0001-current-canonical-state.md").read_text(encoding="utf-8")
    if "Foundation 1.0 / Day 17" not in state or "1.0.0-alpha.17" not in state:
        errors.append("Day 17 stage/version changed")

    forbidden = [
        "CurrentKernelConformanceClaim: true",
        "current_kernel_conformance_claim: true",
        "Kernel certified",
        "all products conform",
    ]
    corpus = "\n".join(
        path.read_text(encoding="utf-8")
        for path in [*EXPECTED_DOCS.values(), JSON_PATH]
    )
    for phrase in forbidden:
        if phrase in corpus:
            errors.append(f"forbidden conformance phrase: {phrase}")

    if errors:
        print("Kernel family validation failed:")
        for error in errors:
            print(" -", error)
        return 1

    print(
        "Kernel family validation passed. "
        f"2 Draft Kernel documents, 36 requirements, "
        f"30 ambiguities, 30 vocabulary terms, "
        "4 reserved documents not created."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
