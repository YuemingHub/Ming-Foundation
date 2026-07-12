#!/usr/bin/env python3
"""Validate Ming Foundation governed documents, dependencies, and index rows."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import unquote
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
    "id", "title", "status", "version", "layer", "owner",
    "created", "updated", "related", "depends_on",
}
ALLOWED_STATUSES = {
    "Idea", "Draft", "Proposed", "Review", "Candidate", "Accepted",
    "Stable", "Experimental", "Superseded", "Deprecated", "Withdrawn",
}
ID_PATTERN = re.compile(
    r"^(MF|MOS|RFC|ADR|REF|GOV|PROF|PROJECT-[A-Z0-9-]+)-[A-Z0-9][A-Z0-9._-]*$"
)
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
INDEX_ROW_PATTERN = re.compile(
    r"^\|\s*([A-Z][A-Z0-9._-]*)\s*\|\s*\[[^\]]+\]\(([^)]+)\)\s*\|\s*([^|]+?)\s*\|\s*$"
)


def parse_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("unterminated YAML frontmatter")

    data: dict[str, object] = {}
    current_list: str | None = None
    for raw in text[4:end].splitlines():
        if not raw.strip():
            continue
        if raw.startswith("- ") and current_list:
            value = raw[2:].strip()
            cast = data.setdefault(current_list, [])
            if isinstance(cast, list):
                cast.append(value)
            continue
        if raw.startswith("  - ") and current_list:
            value = raw[4:].strip()
            cast = data.setdefault(current_list, [])
            if isinstance(cast, list):
                cast.append(value)
            continue
        if raw.startswith(" "):
            continue
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        key, value = key.strip(), value.strip()
        if value == "[]":
            data[key] = []
            current_list = None
        elif value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            data[key] = [item.strip() for item in inner.split(",") if item.strip()]
            current_list = None
        elif value:
            data[key] = value
            current_list = None
        else:
            data[key] = []
            current_list = key
    return data


def governed_docs() -> list[Path]:
    docs: list[Path] = []
    for dirname in SCANNED_DIRS:
        base = ROOT / dirname
        if base.exists():
            docs.extend(sorted(base.rglob("*.md")))
    return docs


def validate_index(
    metas: dict[str, tuple[Path, dict[str, object]]],
    errors: list[str],
) -> tuple[int, int]:
    index_path = ROOT / "REPOSITORY_INDEX.md"
    if not index_path.exists():
        errors.append("missing REPOSITORY_INDEX.md")
        return 0, 0

    row_ids: set[str] = set()
    link_count = 0
    for lineno, line in enumerate(index_path.read_text(encoding="utf-8").splitlines(), 1):
        match = INDEX_ROW_PATTERN.match(line)
        if not match:
            continue
        doc_id, raw_link, status = match.groups()
        if doc_id == "ID":
            continue
        status = status.strip()
        raw_link = unquote(raw_link.split("#", 1)[0])
        if "://" in raw_link or raw_link.startswith("#"):
            continue
        link_count += 1
        linked = (ROOT / raw_link).resolve()
        try:
            linked.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"REPOSITORY_INDEX.md:{lineno}: link escapes repository: {raw_link}")
            continue
        if not linked.exists():
            errors.append(f"REPOSITORY_INDEX.md:{lineno}: missing linked file {raw_link}")
            continue
        if doc_id in row_ids:
            errors.append(f"REPOSITORY_INDEX.md:{lineno}: duplicate index ID {doc_id}")
        row_ids.add(doc_id)
        if doc_id not in metas:
            errors.append(f"REPOSITORY_INDEX.md:{lineno}: indexed ID {doc_id} not found in governed documents")
            continue
        meta_path, meta = metas[doc_id]
        if linked != meta_path.resolve():
            errors.append(
                f"REPOSITORY_INDEX.md:{lineno}: {doc_id} points to {raw_link}, "
                f"but document is {meta_path.relative_to(ROOT)}"
            )
        if meta.get("status") != status:
            errors.append(
                f"REPOSITORY_INDEX.md:{lineno}: {doc_id} status {status!r} "
                f"does not match frontmatter {meta.get('status')!r}"
            )
    return len(row_ids), link_count


def main() -> int:
    errors: list[str] = []
    metas: dict[str, tuple[Path, dict[str, object]]] = {}
    dependency_count = 0

    for path in governed_docs():
        rel = path.relative_to(ROOT)
        try:
            meta = parse_frontmatter(path)
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue

        missing = REQUIRED_KEYS - set(meta)
        if missing:
            errors.append(f"{rel}: missing keys {sorted(missing)}")
            continue

        doc_id = str(meta["id"])
        if not ID_PATTERN.match(doc_id):
            errors.append(f"{rel}: invalid id format {doc_id!r}")
        if doc_id in metas:
            errors.append(
                f"{rel}: duplicate id {doc_id!r}, already used by "
                f"{metas[doc_id][0].relative_to(ROOT)}"
            )
        else:
            metas[doc_id] = (path, meta)

        status = str(meta["status"])
        if status not in ALLOWED_STATUSES:
            errors.append(f"{rel}: unsupported status {status!r}")

        for key in ("created", "updated"):
            value = str(meta[key])
            if not DATE_PATTERN.match(value):
                errors.append(f"{rel}: invalid {key} date {value!r}")

        for key in ("related", "depends_on"):
            if not isinstance(meta[key], list):
                errors.append(f"{rel}: {key} must be a YAML list")

    known_ids = set(metas)
    for doc_id, (path, meta) in metas.items():
        for key in ("related", "depends_on"):
            refs = meta.get(key, [])
            if not isinstance(refs, list):
                continue
            for ref in refs:
                dependency_count += 1
                if ref not in known_ids:
                    errors.append(
                        f"{path.relative_to(ROOT)}: {key} references unknown ID {ref!r}"
                    )
        if doc_id in meta.get("depends_on", []):
            errors.append(f"{path.relative_to(ROOT)}: document depends on itself")

    index_rows, index_links = validate_index(metas, errors)

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        "Repository validation passed. "
        f"Validated {len(metas)} document IDs, {dependency_count} references, "
        f"{index_rows} index rows, and {index_links} index links."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
