#!/usr/bin/env python3
"""Validate canonical stage and release version consistency."""

from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]

VERSION_RE = re.compile(r"Current repository foundation version:\s*\*\*([^*]+)\*\*")
STAGE_RE = re.compile(r"This repository is at \*\*([^*]+)\*\*")
CHANGELOG_RE = re.compile(r"^## \[([^\]]+)\] - ", re.MULTILINE)


def frontmatter_scalar(path: Path, key: str) -> str | None:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    for raw in text[4:end].splitlines():
        if raw.startswith(" ") or raw.startswith("-") or ":" not in raw:
            continue
        k, value = raw.split(":", 1)
        if k.strip() == key:
            return value.strip()
    return None


def main() -> int:
    errors: list[str] = []
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    gov1 = ROOT / "governance/status/GOV-0001-current-canonical-state.md"
    registry = json.loads(
        (ROOT / "standards/requirements/RFC_REQUIREMENTS.json").read_text(encoding="utf-8")
    )

    version_match = VERSION_RE.search(readme)
    stage_match = STAGE_RE.search(readme)
    changelog_match = CHANGELOG_RE.search(changelog)
    if not version_match:
        errors.append("README version not found")
    if not stage_match:
        errors.append("README stage not found")
    if not changelog_match:
        errors.append("CHANGELOG top version not found")

    readme_version = version_match.group(1) if version_match else None
    readme_stage = stage_match.group(1) if stage_match else None
    gov_version = frontmatter_scalar(gov1, "version")
    gov_text = gov1.read_text(encoding="utf-8")
    gov_stage_match = re.search(r"\*\*Current repository stage:\*\*\s*(.+?)(?:\n-|\n\n)", gov_text, re.DOTALL)
    gov_stage = " ".join(gov_stage_match.group(1).split()) if gov_stage_match else None

    expected_version = registry.get("registry_version")
    values = {
        "README": readme_version,
        "GOV-0001": gov_version,
        "CHANGELOG": changelog_match.group(1) if changelog_match else None,
        "requirement registry": expected_version,
    }
    unique_versions = {value for value in values.values() if value}
    if len(unique_versions) != 1:
        errors.append(f"release versions differ: {values}")

    if readme_stage and gov_stage and readme_stage != gov_stage:
        errors.append(
            f"stage differs: README={readme_stage!r}, GOV-0001={gov_stage!r}"
        )

    if errors:
        print("Release-state validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        f"Release-state validation passed. Version {readme_version}; "
        f"stage {readme_stage}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
