---
id: PROF-0003
title: Retention and Backup Completion Profile
status: Proposed
version: 0.1.0
layer: Layer 1 — Standards
owner: Ming Foundation Standards
created: 2026-07-12
updated: 2026-07-12
related:
  - RFC-0002
  - GOV-0055
  - GOV-0058
  - ADR-0016
depends_on:
  - RFC-0002
---

# PROF-0003 — Retention and Backup Completion Profile

## Status boundary

These are conservative Foundation defaults for review and completion
behavior. They are not universal legal retention periods.

A qualified jurisdiction profile may require a shorter or longer period and
must record its basis.

## 1. Profile classes

| Class | Purpose | Default maximum review interval |
|---|---|---|
| T0 | Transient intake not converted into service | 30 days |
| T1 | Active service and directly necessary context | 180 days after last material use |
| T2 | Safety, incident, or safeguarding evidence | 90 days while active; annual after closure |
| T3 | Security, access, and integrity audit | Annual |
| T4 | Restricted validation or research evidence | At project end and at least annually |
| T5 | Public or governance record | Annual truth, status, and correction review |

The interval is a mandatory review deadline, not automatic permission to
retain until that date.

## 2. Required retention record

```text
retention_profile_id
profile_class
purpose
covered_assets
subjects
storage_locations
backup_locations
access_roles
start_event
review_interval
deletion_or_archival_trigger
backup_completion_method
exception_categories
exception_owner
maximum_exception_period
jurisdiction_profile
completion_evidence
appeal_or_review_route
```

## 3. Completion states

```text
requested
primary_restricted
primary_removed
derived_assets_addressed
indexes_addressed
shared_copies_addressed
backup_expiry_scheduled
backup_erased_or_expired
exception_open
complete
```

A request MUST NOT be marked complete while an active copy can still be used
for the prohibited purpose.

## 4. Backup handling

Backup handling MUST state one of:

- deletion from mutable backup;
- scheduled expiry from immutable backup;
- cryptographic erasure;
- restoration-time suppression;
- narrow retained exception.

A scheduled backup action requires:

- target date;
- responsible owner;
- affected systems;
- restoration control;
- completion evidence;
- exception and appeal route.

## 5. Exception controls

An exception MUST be:

- tied to a named purpose and basis;
- minimum necessary;
- access-restricted;
- time- or review-bounded;
- independently reviewable where high impact;
- visible to the affected person where safe and lawful;
- closed or renewed through an explicit decision.

## 6. Review questions

- Are the default review intervals sufficiently conservative?
- Which jurisdictions or professional duties require different intervals?
- Which backup systems can provide reliable completion evidence?
- How should deletion be represented when immutable audit evidence must
  remain?
