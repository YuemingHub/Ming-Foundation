#!/usr/bin/env python3
"""Initialize a Git-ignored local workspace for restricted Day 18 records."""

from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
import json
import subprocess

REQUIRED_IGNORE_LINES = [
    ".ming-private/",
    "restricted-accountability/",
    "private/accountability/",
]

DIRECTORIES = [
    "nomination-intake",
    "role-acceptance",
    "qualification-and-conflict",
    "protocol-signoffs",
    "environment-verification",
    "cp2-activation",
    "incident-and-stop",
]


def ensure_gitignore(repo: Path) -> None:
    path = repo / ".gitignore"
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    lines = existing.splitlines()
    changed = False
    for item in REQUIRED_IGNORE_LINES:
        if item not in lines:
            lines.append(item)
            changed = True
    if changed:
        path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    ensure_gitignore(repo)

    workspace = repo / ".ming-private/day18-role-nomination"
    workspace.mkdir(parents=True, exist_ok=True)
    for name in DIRECTORIES:
        (workspace / name).mkdir(parents=True, exist_ok=True)

    register = workspace / "restricted-accountability-register.json"
    if not register.exists():
        register.write_text(
            json.dumps(
                {
                    "register_id": "LOCAL-DAY18-RESTRICTED-ACCOUNTABILITY",
                    "storage_class": "RestrictedOutsidePublicRepository",
                    "created_by": None,
                    "assignments": [],
                    "warning": "Do not commit this file or copy real identity data into the public repository."
                },
                ensure_ascii=False,
                indent=2
            ) + "\n",
            encoding="utf-8",
            newline="\n"
        )

    readme = workspace / "README_PRIVATE.md"
    if not readme.exists():
        readme.write_text(
            "# Private Day 18 Workspace\n\n"
            "This directory may contain real names, contacts, signatures, "
            "qualifications, conflict findings, and role-acceptance evidence. "
            "It must remain outside Git and must not contain affected-person "
            "or real case evidence.\n",
            encoding="utf-8",
            newline="\n"
        )

    completed = subprocess.run(
        ["git", "check-ignore", "-q", str(workspace)],
        cwd=repo,
        capture_output=True,
        text=True
    )
    if completed.returncode != 0:
        print("Workspace was created but Git does not report it as ignored.")
        return 1

    print(f"Restricted workspace initialized: {workspace}")
    print("No real nomination or assignment was created.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
