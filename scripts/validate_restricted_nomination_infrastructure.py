#!/usr/bin/env python3
"""Validate Day 18 restricted nomination infrastructure and privacy boundary."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

def frontmatter_status(path):
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    for line in text[4:end].splitlines():
        if line.startswith("status:"):
            return line.split(":", 1)[1].strip()
    return None

def main():
    errors = []

    ignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    for marker in [".ming-private/", "restricted-accountability/", "private/accountability/"]:
        if marker not in ignore.splitlines():
            errors.append(f".gitignore missing {marker}")

    manifest = load("standards/review/RESTRICTED_NOMINATION_WORKSPACE_MANIFEST.json")
    if manifest["public_repository_contains_real_identity_records"] is not False:
        errors.append("public repository identity boundary mismatch")
    if manifest["workspace_path"] != ".ming-private/day18-role-nomination/":
        errors.append("restricted workspace path mismatch")
    if manifest["gitignore_required"] is not True:
        errors.append("restricted workspace must require Git ignore")
    if manifest["current_state"] != {
        "workspace_claimed_initialized": False,
        "real_identity_records_claimed": 0,
        "nominations_claimed": 0,
        "acceptances_claimed": 0,
        "verification_records_claimed": 0,
    }:
        errors.append("public workspace state must remain zero and unclaimed")

    slots = load("standards/review/CP2_NOMINATION_SLOT_PLAN.json")
    if slots["overall_state"] != "SlotsDefinedNoRealNominations":
        errors.append("slot-plan state mismatch")
    if slots["minimum_distinct_people"] != 3 or len(slots["slots"]) != 4:
        errors.append("slot-plan topology mismatch")
    if slots["summary"] != {
        "slots": 4,
        "minimum_distinct_people": 3,
        "real_people_nominated": 0,
        "slots_accepted": 0,
        "slots_verified": 0,
        "active_slots": 0,
    }:
        errors.append("slot-plan summary mismatch")
    for slot in slots["slots"]:
        if slot["nomination_state"] != "OpenNotNominated":
            errors.append(f"{slot['slot_id']}: nomination must remain open")
        if slot["restricted_assignment_refs"] != []:
            errors.append(f"{slot['slot_id']}: fabricated restricted assignment")
        if slot["acceptance_state"] != "NotAccepted":
            errors.append(f"{slot['slot_id']}: acceptance must remain absent")
        if slot["activation_state"] != "Inactive":
            errors.append(f"{slot['slot_id']}: slot must remain inactive")

    public = load("standards/review/NAMED_ACCOUNTABILITY_PUBLIC_REGISTER.json")
    if len(public["roles"]) != 8:
        errors.append("expected eight public accountability roles")
    for item in public["roles"]:
        if item["restricted_identity_ref"] is not None:
            errors.append(f"{item['role_id']}: fabricated identity reference")
        if item["public_display_name"] is not None:
            errors.append(f"{item['role_id']}: public real name not allowed")
        if item["nomination_state"] != "NotNominated":
            errors.append(f"{item['role_id']}: role nomination must remain zero")

    nomination = load("standards/review/ROLE_NOMINATION_AND_ACCEPTANCE_PLAN.json")
    if nomination["execution_state"] != "ReadyForRestrictedIntakeNotExecuted":
        errors.append("restricted nomination execution state mismatch")
    for key in [
        "nominations_started", "restricted_identity_records",
        "acceptances_complete", "qualification_checks_complete",
        "conflict_checks_complete", "active_assignments"
    ]:
        if nomination["summary"][key] != 0:
            errors.append(f"nomination summary {key} must remain zero")

    if not (ROOT / "scripts/init_restricted_nomination_workspace.py").exists():
        errors.append("restricted workspace initializer missing")

    templates = [
        ROOT / f"governance/templates/GOV-TPL-{number:04d}-" / "unused"
        for number in range(29, 36)
    ]
    actual_templates = [
        ROOT / "governance/templates/GOV-TPL-0029-restricted-nomination-slot-record.md",
        ROOT / "governance/templates/GOV-TPL-0030-restricted-accountability-index.md",
        ROOT / "governance/templates/GOV-TPL-0031-qualification-conflict-and-independence-decision.md",
        ROOT / "governance/templates/GOV-TPL-0032-cp2-protocol-applicability-signoff.md",
        ROOT / "governance/templates/GOV-TPL-0033-cp2-environment-control-verification.md",
        ROOT / "governance/templates/GOV-TPL-0034-cp2-conditional-preauthorization-record.md",
        ROOT / "governance/templates/GOV-TPL-0035-cp2-effective-activation-decision.md",
    ]
    if any(not path.exists() or frontmatter_status(path) != "Accepted" for path in actual_templates):
        errors.append("Day18 template set missing or not Accepted")

    if errors:
        print("Restricted-nomination infrastructure validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        "Restricted-nomination infrastructure validation passed. Validated "
        "three Git-ignore boundaries, a zero-state private workspace manifest, "
        "four open nomination slots, a three-person minimum, eight public "
        "roles with no identity references, zero nomination events, a local "
        "workspace initializer, and seven Accepted templates."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
