#!/usr/bin/env python3
"""Validate Ming Foundation document metadata and identifier uniqueness."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SCANNED_DIRS = [
    "foundation",
    "standards",
    "infrastructure",
    "reference",
    "research",
    "projects",
    "governance",
]

REQUIRED_KEYS = {
    "id",
    "title",
    "status",
    "version",
    "layer",
    "owner",
    "created",
    "updated",
    "related",
    "depends_on",
}

ID_PATTERN = re.compile(
    r"^(MF|MOS|RFC|ADR|REF|GOV|PROJECT-[A-Z0-9-]+)-[A-Z0-9][A-Z0-9._-]*$"
)


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("unterminated YAML frontmatter")

    data: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        if not raw or raw.startswith(" ") or raw.startswith("-"):
            continue
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def main() -> int:
    errors: list[str] = []
    seen_ids: dict[str, Path] = {}

    for dirname in SCANNED_DIRS:
        base = ROOT / dirname
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            if path.name.lower() == "readme.md":
                # Project READMEs in this repository are normative and include metadata.
                pass
            try:
                meta = parse_frontmatter(path)
            except ValueError as exc:
                errors.append(f"{path.relative_to(ROOT)}: {exc}")
                continue

            missing = REQUIRED_KEYS - set(meta)
            if missing:
                errors.append(
                    f"{path.relative_to(ROOT)}: missing keys {sorted(missing)}"
                )
                continue

            doc_id = meta["id"]
            if not ID_PATTERN.match(doc_id):
                errors.append(
                    f"{path.relative_to(ROOT)}: invalid id format '{doc_id}'"
                )

            if doc_id in seen_ids:
                errors.append(
                    f"{path.relative_to(ROOT)}: duplicate id '{doc_id}', "
                    f"already used by {seen_ids[doc_id].relative_to(ROOT)}"
                )
            else:
                seen_ids[doc_id] = path

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(f"Repository validation passed. Validated {len(seen_ids)} document IDs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
