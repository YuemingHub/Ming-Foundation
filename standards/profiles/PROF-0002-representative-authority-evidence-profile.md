---
id: PROF-0002
title: Representative Authority Evidence Profile
status: Proposed
version: 0.2.0-draft.1
layer: Layer 1 — Standards
owner: Ming Foundation Standards
created: 2026-07-12
updated: 2026-07-13
related:
  - RFC-0001
  - RFC-0002
  - GOV-0055
  - GOV-0058
  - ADR-0016
  - GOV-0061
  - GOV-0066
  - GOV-0071
  - GOV-0073
  - GOV-0076
  - GOV-0077
  - ADR-0019
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
## 8. Least-evidence verification

The implementation MUST use the least intrusive evidence sufficient for the
specific action, impact, and jurisdiction.

It MUST NOT request a document when identity, subject designation, scoped
confirmation, or another lower-intrusion method is sufficient.

Evidence escalation MUST record:

- the action requiring authority;
- impact and reversibility;
- evidence already available;
- why a lower evidence level is insufficient;
- the additional evidence requested;
- who may inspect it;
- retention and deletion handling;
- an alternative route for a person who cannot reasonably provide it.

Failure to possess conventional documents MUST NOT be treated as evidence of
fraud, incapacity, lack of family relationship, or lack of support.

## 9. Care, support, contact, and authority separation

The implementation MUST distinguish:

```text
caregiver_or_supporter
trusted_contact
emergency_contact
communication_assistant
subject_designated_representative
delegated_service_representative
legal_or_institutional_authority
unknown_or_disputed_authority
```

Providing care, financial support, housing, transportation, translation,
emotional support, or emergency contact information does not by itself grant
access, disclosure, deletion, restriction, consent, or high-impact authority.

A supporter MAY assist communication without receiving decision authority or
private information.

## 10. Subject challenge and conflict escalation

A subject MUST have an accessible route to:

- see that representative authority is being used;
- understand its stated scope and expiry;
- challenge identity, evidence, scope, purpose, conflict, or action;
- request a different reviewer;
- restrict optional use while a material dispute is pending;
- receive a reasoned decision where safe and lawful;
- appeal or request later review.

Conflict-free review MUST be triggered when:

- the subject alleges coercion, violence, exploitation, or retaliation;
- the operator or representative may be the source of harm;
- the representative requests protected-source information;
- the representative benefits from the decision;
- the same role verifies, acts, and closes the authority;
- evidence is inaccessible to the subject;
- the proposed action is irreversible or highly restrictive.

An immediate protective action under uncertainty MUST be minimum necessary,
time-limited, independently reviewed, and correctable.

## 11. Authority-evidence lifecycle

Authority evidence MUST be separated from general identity, behavior,
immigration, financial, clinical, education, or risk profiling.

The authority record MUST state:

- collection purpose;
- evidence category and minimum scope;
- access roles;
- verification result;
- permitted and prohibited uses;
- start, expiry, review, revocation, and dispute state;
- retention profile;
- deletion or restriction propagation;
- derived records and indexes;
- later correction and appeal.

Evidence MUST NOT be reused for an unrelated purpose without a separately
governed basis.

Expired, revoked, disproved, or out-of-scope evidence MUST stop authorizing
new action and MUST propagate to dependent permissions and decisions.

## 12. Accessible and alternate verification

Verification and challenge routes MUST provide reasonable alternatives for:

- language and interpretation needs;
- disability and assistive technology;
- low literacy;
- remote or low-bandwidth access;
- people without government-issued documents;
- people at risk from the representative or household;
- people who need a private contact route.

A verification method that systematically excludes a group MUST be revised or
qualified before use.

## 13. Remaining external review

E0 through E4 remain technical evidence classes, not universal legal
conclusions.

The profile remains Proposed pending affected-person, safeguarding,
accessibility, institutional, and jurisdiction review.
