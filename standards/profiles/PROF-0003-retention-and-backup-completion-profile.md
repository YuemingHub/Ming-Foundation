---
id: PROF-0003
title: Retention and Backup Completion Profile
status: Proposed
version: 0.2.0-draft.1
layer: Layer 1 — Standards
owner: Ming Foundation Standards
created: 2026-07-12
updated: 2026-07-13
related:
  - RFC-0002
  - GOV-0055
  - GOV-0058
  - ADR-0016
  - GOV-0061
  - GOV-0066
  - GOV-0071
  - GOV-0074
  - GOV-0076
  - GOV-0077
  - ADR-0019
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
## 7. Purpose-end deletion and review-interval boundary

A default maximum review interval is a latest review deadline.

It is not:

- permission to retain until the deadline;
- evidence that the purpose still exists;
- a substitute for data minimization;
- a legal retention period;
- authorization to continue optional training, profiling, sharing, or
  high-impact use.

When the purpose ends, authority is withdrawn, the asset is no longer
necessary, or a shorter applicable rule exists, deletion, restriction,
anonymization, or justified archival MUST begin without waiting for the
maximum review interval.

Every continuation decision MUST record current necessity, basis, minimum
scope, alternatives, next review, and responsible owner.

## 8. Plain-language retained-data status

An affected person SHOULD be able to see, in usable language:

- what information remains;
- whether it is active, restricted, archived, in backup, or under exception;
- where it remains at a meaningful system level;
- why it remains;
- who can use it and for what;
- which uses are prohibited;
- expected deletion, expiry, or next review;
- backup and restoration handling;
- exception owner and basis;
- correction, challenge, and appeal routes.

The display MUST NOT falsely state “deleted” when an active or restorable copy
can still be used for the prohibited purpose.

## 9. Safety evidence and competing-rights balancing

Retention of safety, incident, or safeguarding evidence MUST balance:

- protection from serious harm;
- reporter and source protection;
- subject access and correction;
- false-positive and outdated-label risk;
- privacy and disclosure harm;
- legal or professional duties;
- minimum necessary detail;
- expiry, review, and appeal;
- independent review when the operator or representative may be involved.

A safety label MUST NOT become a permanent identity marker merely because
supporting evidence is retained.

A correction or supersession MUST propagate to active recommendations,
summaries, indexes, and future use while preserving necessary audit history.

## 10. Backup restoration controls

A backup plan MUST define behavior when data is restored.

It MUST include:

- a suppression list or equivalent control for deleted, restricted, revoked,
  or corrected records;
- restoration-time application of current rights and authority state;
- a reconciliation job for derived assets and indexes;
- completion monitoring and evidence;
- failure escalation;
- exception expiry;
- a post-restoration propagation test.

Restored data MUST NOT silently return to active use under an expired purpose,
authority, safety label, or representative state.

## 11. Completion evidence

A deletion or restriction action may be marked complete only when:

- active primary copies are addressed;
- derived assets and indexes are addressed;
- shared copies are addressed or a bounded exception is recorded;
- backup handling is scheduled and enforceable;
- restoration controls are verified;
- exceptions are minimum necessary and review-bounded;
- the result is visible through an appropriate rights route.

## 12. Remaining external review

T0 through T5 are Foundation review classes, not universal legal periods.

The profile remains Proposed pending affected-person, privacy, safeguarding,
operational, and jurisdiction review.
