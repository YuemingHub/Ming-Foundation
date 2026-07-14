---
id: REF-0029
title: MingOS Kernel AI Human and Affected-Person Role Representation Map
status: Draft
version: 0.1.0
layer: Reference
owner: Ming Foundation Architecture
created: 2026-07-14
updated: 2026-07-14
language: en
canonical_language: en
translation_status: original
decision_base_commit: 394f494f00ebfccf38572e3846cf6b6e3f699abf
related:
  - ADR-0001
  - ADR-0026
  - RFC-0001
  - RFC-0002
  - RFC-0003
  - PROF-0001
  - PROF-0002
  - REF-0026
  - REF-0028
depends_on:
  - ADR-0026
---

# REF-0029 — MingOS Kernel AI Human and Affected-Person Role Representation Map

> This Draft defines role-boundary requirements for future Kernel documents. It
> does not define the final object schema.

## 1. Role is not identity

A person, account, model, organization, service and role are different objects.

- one person may hold several roles;
- one role may be assigned for a bounded purpose and time;
- authority must be scoped and evidenced;
- a relationship does not automatically create authority;
- operating the interface does not make someone the sole affected person;
- being described in data may make someone affected even without an account.

## 2. Minimum role set

| Role | Meaning | Minimum future representation | Must not be assumed from |
|---|---|---|---|
| AffectedPerson | person whose rights, welfare, identity, relationship or opportunities may be affected | identity/reference, impact type, participation status, correction route | account ownership |
| Subject | person, group, relationship or event being described | subject reference, scope, provenance, knowledge status | speaker identity |
| Speaker | source of a statement or observation | source, time, context, authority, confidence | subject identity |
| Representative | person acting for or with another person | represented subject, authority basis, scope, expiry, conflicts | parent/partner/professional label alone |
| Operator | person controlling an interface or initiating an operation | actor identity, operation, purpose, permissions | affected-person consent |
| Practitioner | qualified or declared professional role | role, qualification, jurisdiction, scope, availability, limits | generic “expert” label |
| Reviewer | person reviewing text, evidence, decision or implementation | review class, independence, conflict, result, limitations | authorship |
| AccountableHuman | human responsible for a decision or operation | role, authority, decision boundary, escalation, review path | AI output or operator action |
| AccountableOrganization | entity responsible for governance, service or claim | legal/operational identity, scope, contact, obligations | product name |
| AIComponent | model or agent performing bounded functions | provider/model/version, role, capabilities, limitations, provenance | professional or accountable-human status |
| ServiceProvider | external or internal service/resource source | service type, status, freshness, jurisdiction, limits | successful link generation |
| EvidenceCustodian | role controlling restricted evidence | environment, access scope, retention, audit and disclosure duties | repository maintainer status |

## 3. Authority record

Future role assignment must be able to record:

```text
role_assignment_id
actor_or_entity
role_type
subject_or_scope
purpose
authority_basis
permissions
prohibitions
effective_time
expiry_or_review_time
conflicts
evidence
assigning_authority
revocation_status
audit_reference
```

## 4. Required separations

The Kernel must not silently collapse:

- parent and child;
- operator and affected person;
- speaker and subject;
- representative and represented person;
- practitioner and final decision authority;
- author and independent reviewer;
- commercial owner and Charter-conflict adjudicator;
- evidence custodian and unrestricted product analytics;
- AI component and accountable human;
- generated response and verified service availability.

## 5. High-impact decisions

A future high-impact decision model must identify:

- affected people;
- decision and possible consequences;
- evidence and uncertainty;
- AI contribution;
- responsible human and organization;
- representative authority where applicable;
- required independent review;
- least harmful and reversible option;
- notice, correction, appeal and follow-up;
- time boundary and re-evaluation condition.

AI must not be the final accountable actor.

## 6. Participation status

Future Kernel documents should distinguish at least:

- `NotIdentified`
- `IdentifiedNotContacted`
- `ParticipationNotPossible`
- `ParticipationUnsafe`
- `RepresentativeOnly`
- `Invited`
- `Participating`
- `Declined`
- `Withdrew`
- `CorrectionRequested`
- `AppealOpen`

These labels are candidates, not an adopted state machine.

## 7. Day 16 boundary

Day 16 role definitions and synthetic pilots are governance evidence for control
architecture. They do not assign Kernel roles to real people, approve human use,
or satisfy affected-person participation.
