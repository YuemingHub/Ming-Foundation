#!/usr/bin/env python3
"""Validate canonical text identity independently of LF/CRLF checkout form."""

from pathlib import Path
import json

from validation_utils import canonical_text_blob_sha

ROOT = Path(__file__).resolve().parents[1]

RFC_PATHS = {
    "RFC-0001": ROOT / "standards/rfc/RFC-0001-subject-speaker-and-contestability.md",
    "RFC-0002": ROOT / "standards/rfc/RFC-0002-consent-and-data-rights-lifecycle.md",
    "RFC-0003": ROOT / "standards/rfc/RFC-0003-safety-escalation-handoff-appeal-and-incident.md",
    "RFC-0004": ROOT / "standards/rfc/RFC-0004-case-and-cross-family-evidence-governance.md",
    "RFC-0005": ROOT / "standards/rfc/RFC-0005-public-claim-charter-sync-and-capability-status.md",
}

def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

def main():
    errors = []
    attrs = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    for marker in [
        "*.md text eol=lf",
        "*.json text eol=lf",
        "*.py text eol=lf",
        "*.yml text eol=lf",
        "*.yaml text eol=lf",
        "*.mmd text eol=lf",
    ]:
        if marker not in attrs:
            errors.append(f".gitattributes missing {marker}")

    requirements = load("standards/requirements/RFC_REQUIREMENTS.json")
    sources = {item["id"]: item for item in requirements["source_documents"]}
    for rfc, path in RFC_PATHS.items():
        if sources[rfc]["source_blob_sha"] != canonical_text_blob_sha(path):
            errors.append(f"{rfc}: canonical text blob mismatch")

    profile_registry = load("standards/profiles/RESIDUAL_PROFILE_REGISTRY.json")
    for item in profile_registry["profiles"]:
        path = ROOT / item["path"]
        if item["source_blob_sha"] != canonical_text_blob_sha(path):
            errors.append(f"{item['id']}: canonical text blob mismatch")

    if errors:
        print("Text-integrity validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        "Text-integrity validation passed. Validated LF policy and canonical "
        "text blob identity for 5 RFC sources and 4 Profile sources."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
