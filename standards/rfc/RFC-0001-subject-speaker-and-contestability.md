---
created: 2026-07-12
depends_on:
- MF-0004
- PROJECT-MINGOS-0002
- ADR-0005
id: RFC-0001
layer: Layer 1 — Standards
owner: Ming Foundation Standards
related:
- MF-0004
- PROJECT-MINGOS-0002
- GOV-0009
- GOV-0010
- GOV-0012
- GOV-0014
- GOV-0019
- ADR-0007
status: Proposed
title: Subject Speaker and Contestability Protocol
updated: 2026-07-12
version: 0.1.0
---

# RFC-0001 — Subject, Speaker, and Contestability Protocol

## Status

Proposed minimum protocol. It is not yet an implemented or accepted
standard.

## 1. Problem

A MingOS operator may describe another person.

Examples include:

- a parent describing a child;
- a partner describing another partner;
- a teacher describing a student;
- a professional documenting a family member;
- an AI inferring a pattern about someone who is not operating the
  interface.

Without an explicit protocol, one person’s account can silently become
another person’s identity.

## 2. Core rule

Every material assertion MUST distinguish:

``` text
Who is being described?
Who supplied the information?
What kind of knowledge object is it?
What evidence supports it?
Who has confirmed or contested it?
For what purpose and period may it be used?
```

No third-party statement may silently become a subject-confirmed fact.

## 3. Required objects

### 3.1 Subject

The person, relationship, family, or system condition being described.

Minimum fields:

- `subject_id`;
- `subject_type`;
- `age_or_capacity_band` where relevant;
- `relationship_to_speaker`;
- `participation_status`;
- `visibility_policy`.

### 3.2 Speaker

The person, system, document, sensor, or model that supplied the
information.

Minimum fields:

- `speaker_id`;
- `speaker_type`;
- `role`;
- `relationship_to_subject`;
- `authority_scope`;
- `source_time`.

### 3.3 Assertion

A statement about a subject.

Minimum fields:

- `assertion_id`;
- `subject_id`;
- `speaker_id`;
- `knowledge_status`;
- `content`;
- `evidence_refs`;
- `confidence`;
- `uncertainty`;
- `created_at`;
- `valid_from`;
- `review_or_expiry_at`;
- `purpose`;
- `visibility`;
- `confirmation_status`;
- `counterevidence_refs`;
- `revision_history`.

### 3.4 Contestation

A request to disagree with, contextualize, limit, correct, suspend, or
remove an assertion.

Minimum fields:

- `contestation_id`;
- `assertion_id`;
- `requester_id`;
- `requester_relationship`;
- `requested_action`;
- `reason`;
- `safety_or_legal_constraints`;
- `reviewer`;
- `decision`;
- `decision_reason`;
- `appeal_path`;
- `resolved_at`.

## 4. Knowledge-status vocabulary

Implementations MUST represent at least:

- direct self-report;
- third-party report;
- observed event;
- imported record;
- model inference;
- professional hypothesis;
- pattern candidate;
- confirmed fact within a stated scope;
- disputed;
- superseded;
- unknown;
- decision;
- action.

A user-interface label may be simpler, but the stored distinction MUST
remain inspectable.

## 5. Participation ladder

Participation should be age-, capacity-, context-, and safety-aware.

Possible states:

1.  not yet informed;
2.  informed through an appropriate representative;
3.  directly informed;
4.  invited to comment;
5.  able to correct or contextualize;
6.  able to approve specific uses;
7.  able to restrict or revoke specific uses;
8.  temporarily excluded for a documented safety reason;
9.  unable to participate, with reason and review date recorded.

No state should be inferred solely from age.

## 6. Contestability workflow

``` text
Assertion created
  ↓
Source and knowledge status displayed
  ↓
Affected person or representative may contest
  ↓
Use may be paused when impact is high
  ↓
Independent or role-appropriate review
  ↓
Correct / contextualize / restrict / retain / remove
  ↓
Reason and appeal path recorded
```

High-impact contested assertions SHOULD NOT drive irreversible or
punitive actions while review is pending, unless a narrowly documented
safety duty requires action.

## 7. Prohibited behavior

An implementation MUST NOT:

- label parent-authored data as the child’s confirmed profile;
- hide a model inference as a fact;
- retain a disputed label without the dispute being visible;
- use a temporary crisis state as a permanent identity;
- remove original source and revision history;
- deny contestability merely because the speaker is a professional;
- treat refusal to agree as evidence that the assertion is correct;
- expose one family member’s private statement to another without a
  governed basis.

## 8. User experience requirements

A person reviewing an interpretation SHOULD be able to see:

- what was said;
- who said it;
- whether AI inferred anything;
- what evidence was used;
- how certain the system is;
- how long the interpretation remains active;
- whether anyone has disputed it;
- how to correct or contextualize it;
- what decisions currently depend on it.

## 9. Acceptance tests

A conforming implementation must demonstrate:

1.  a parent report remains visibly attributed to the parent;
2.  a model inference cannot be stored as confirmed fact without an
    explicit transition;
3.  a contested assertion preserves both original and corrected context;
4.  an expired interpretation stops driving current recommendations;
5.  a child or third-party representative can request review through an
    age-appropriate route;
6.  high-impact use records the responsible actor and basis;
7.  every assertion used in a decision can be traced to source and
    status.

## 10. Open questions

- How should direct child access vary by age, jurisdiction, family
  safety, and service type?
- When may a representative act without direct subject participation?
- Which disputes require an independent reviewer?
- Which assertions should never be made available to another family
  member?
- What minimum review period is appropriate for different assertion
  types?
