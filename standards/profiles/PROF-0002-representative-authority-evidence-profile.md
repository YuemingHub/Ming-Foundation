---
id: PROF-0002
title: Representative Authority Evidence Profile
status: Proposed
version: 0.1.0
layer: Layer 1 — Standards
owner: Ming Foundation Standards
created: 2026-07-12
updated: 2026-07-12
related:
  - RFC-0001
  - RFC-0002
  - GOV-0055
  - GOV-0058
  - ADR-0016
depends_on:
  - PROF-0001
  - RFC-0001
  - RFC-0002
---

# PROF-0002 — Representative Authority Evidence Profile

## Status boundary

This profile defines technical evidence levels. It does not determine legal
authority in a jurisdiction.

## 1. Representative types

An implementation MUST distinguish at least:

- subject-designated representative;
- parental or caregiving responsibility;
- court- or institution-appointed authority;
- delegated service representative;
- emergency or safeguarding representative;
- professional representative;
- disputed or unknown authority.

## 2. Evidence levels

| Level | Evidence | Permitted default scope |
|---|---|---|
| E0 | Unsupported assertion | No representative action |
| E1 | Verified representative identity and stated relationship | Receive general information; no sensitive or high-impact action |
| E2 | Verified identity plus corroborated relationship or subject designation | Bounded routine service actions |
| E3 | Documented authority, scope, validity, and conflict check | Material rights or disclosure actions within scope |
| E4 | E3 plus independent legal, institutional, or professional verification | Irreversible, externally reported, or highly restrictive action where applicable |

A higher level does not create unlimited authority.

## 3. Impact mapping

- General information MAY use E1.
- Reversible routine service action SHOULD require E2.
- Access, correction, export, or material disclosure SHOULD require E3.
- Deletion, high-impact restriction, external disclosure, or irreversible
  action SHOULD require E3 or E4 according to jurisdiction and risk.
- Any conflict, dispute, or scope uncertainty MUST pause expansion and route
  to a different reviewer.

## 4. Required authority record

```text
authority_id
representative
subject
representative_type
evidence_level
evidence_refs
verified_by
permitted_actions
prohibited_actions
purpose_scope
data_scope
jurisdiction_profile
conflict_state
starts_at
expires_or_reviews_at
subject_notice
independent_review_route
appeal_route
```

## 5. Evidence handling

Evidence MUST be:

- proportionate to the action;
- purpose-limited;
- access-restricted;
- retained under a named profile;
- reviewable and expiring;
- separated from unsupported family-role assumptions;
- protected from use as a general identity or behavior profile.

## 6. Failure states

The authority state MUST distinguish:

```text
unverified
partially_verified
verified_within_scope
expired
revoked
disputed
conflicted
restricted
```

An expired, revoked, disputed, or conflicted authority MUST NOT authorize new
optional high-impact action.

## 7. Review questions

- Are E1–E4 understandable and proportionate?
- Which actions require jurisdiction-specific E4 evidence?
- How can authority verification avoid unnecessary collection?
- How should a subject safely challenge a representative?
