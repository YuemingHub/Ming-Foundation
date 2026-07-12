---
created: 2026-07-12
depends_on:
  - MF-0004
  - PROJECT-MINGOS-0002
  - ADR-0005
  - ADR-0013
id: RFC-0001
layer: Layer 1 — Standards
owner: Ming Foundation Standards
related:
  - MF-0004
  - PROJECT-MINGOS-0002
  - GOV-0014
  - GOV-0037
  - GOV-0044
  - GOV-0045
  - GOV-0048
  - ADR-0013
  - ADR-0014
status: Proposed
title: Subject Speaker and Contestability Protocol
updated: 2026-07-12
version: 0.2.0-draft.1
---

# RFC-0001 — Subject, Speaker, and Contestability Protocol

## Status

Proposed revised draft. This revision implements `REV-0001` through
`REV-0004` and the applicable R0 decisions from `ADR-0013`.

It is not an Accepted or Candidate standard, and it does not claim that an
implementation conforms.

## 1. Problem

A parent, partner, teacher, professional, institution, document, sensor, or
model may describe another person.

Without an explicit protocol, one person's account can silently become
another person's identity, affect decisions, and remain active after its
basis has expired or been disputed.

## 2. Shared decision terms

This RFC uses the cross-RFC decisions in `ADR-0013`.

### 2.1 Material assertion

An assertion MUST be treated as material when at least one of these applies:

- it persists beyond the immediate interaction;
- it is shared with another person, role, channel, or system;
- it influences a recommendation, restriction, safety action, professional
  action, service decision, or allocation of attention;
- it may materially affect identity, reputation, education, health,
  relationships, access, or opportunity;
- it is used to train, evaluate, retrieve, rank, or generate another
  interpretation;
- reversal would be difficult, delayed, or incomplete.

When materiality is uncertain, the assertion MUST be treated as material
until a role-appropriate review records a narrower classification.

### 2.2 High-impact use

A use is high impact when it can:

- cause an irreversible or difficult-to-reverse consequence;
- impose a punitive or rights-restricting consequence;
- trigger a safety, clinical, legal, educational, employment, financial, or
  institutional action;
- expose sensitive information to another person or organization;
- materially shape a long-lived profile or decision.

A high-impact classification MUST record the responsible actor, basis,
affected people, expected consequence, duration, review point, and appeal or
correction route.

### 2.3 Representative

A representative is a person or role authorized to act for a subject within
a stated scope.

Representative authority MUST record:

- representative type;
- subject;
- authority source or evidence;
- permitted actions;
- prohibited actions;
- start and expiry or review date;
- known conflicts of interest;
- notice to the subject where appropriate;
- independent-review route.

Age alone MUST NOT establish complete representative authority.

### 2.4 Governed disclosure basis

A governed disclosure basis MUST state:

- the specific purpose;
- the authority or permission basis;
- the minimum information necessary;
- intended recipient;
- duration and onward-use limits;
- notice to the subject, or a documented reason for temporary delay;
- safety or legal constraint where applicable;
- reviewer and appeal route.

## 3. Core rule

Every material assertion MUST distinguish:

```text
Who is being described?
Who supplied or generated the information?
What kind of knowledge object is it?
What evidence and uncertainty support it?
Who has confirmed, contested, or revised it?
For what purpose, impact class, visibility, and period may it be used?
Which decisions or derived records depend on it?
```

No third-party statement, professional hypothesis, or model inference may
silently become a subject-confirmed fact.

## 4. Required objects

### 4.1 Subject

Minimum fields:

- `subject_id`;
- `subject_type`;
- `age_or_capacity_band` where relevant;
- `relationship_to_speaker`;
- `participation_status`;
- `visibility_policy`;
- `representative_authority_refs`;
- `jurisdiction_profile`;
- `review_at`.

### 4.2 Speaker

Minimum fields:

- `speaker_id`;
- `speaker_type`;
- `role`;
- `relationship_to_subject`;
- `authority_scope`;
- `conflict_status`;
- `source_time`.

### 4.3 Assertion

Minimum fields:

- `assertion_id`;
- `subject_id`;
- `speaker_id`;
- `knowledge_status`;
- `content`;
- `evidence_refs`;
- `confidence`;
- `uncertainty`;
- `materiality_class`;
- `impact_class`;
- `created_at`;
- `valid_from`;
- `review_or_expiry_at`;
- `purpose`;
- `visibility`;
- `confirmation_status`;
- `contestation_status`;
- `counterevidence_refs`;
- `dependent_decision_refs`;
- `derived_record_refs`;
- `revision_history`;
- `supersession_status`.

### 4.4 Contestation

Minimum fields:

- `contestation_id`;
- `assertion_id`;
- `requester_id`;
- `requester_relationship`;
- `authority_evidence`;
- `requested_action`;
- `reason`;
- `safety_or_legal_constraints`;
- `conflict_check`;
- `reviewer`;
- `decision`;
- `decision_reason`;
- `temporary_restrictions`;
- `dependent_record_actions`;
- `appeal_path`;
- `resolved_at`.

## 5. Knowledge-status vocabulary

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

A simpler user-interface label MAY be used, but the stored distinction,
source, confidence, dispute, and revision state MUST remain inspectable.

## 6. Participation and representative authority

Participation MUST be determined through an age-, capacity-, context-,
safety-, impact-, and jurisdiction-aware profile.

Possible states include:

1. not yet informed;
2. informed through an appropriate representative;
3. directly informed;
4. invited to comment;
5. able to correct or contextualize;
6. able to approve specific uses;
7. able to restrict or revoke specific uses;
8. temporarily excluded for a documented safety reason;
9. unable to participate, with reason and review date recorded.

The implementation MUST NOT infer a state solely from age.

When a representative's interests may conflict with the subject, high-impact
use MUST pause for independent or conflict-free review unless an immediate
documented safety duty requires temporary action.

A temporary participation restriction MUST record actor, basis, scope,
duration, minimum disclosure, review date, and appeal or later-notice route.

## 7. Contestability workflow

```text
Assertion created
  ↓
Materiality and impact classified
  ↓
Source, status, evidence, uncertainty, and dependent uses displayed
  ↓
Affected person or authorized representative may contest
  ↓
High-impact use paused or narrowly excepted
  ↓
Conflict-free or role-appropriate review
  ↓
Correct / contextualize / restrict / supersede / retain / remove
  ↓
Dependent records and decisions updated
  ↓
Reason, notice, and appeal recorded
```

A high-impact contested assertion SHOULD NOT drive an irreversible,
punitive, rights-restricting, or identity-shaping action while review is
pending.

An exception requires an immediate safety or legal duty and MUST record:

- responsible actor;
- evidence and uncertainty;
- why delay creates greater risk;
- action scope and duration;
- least intrusive alternative considered;
- safeguards;
- review deadline;
- later-notice and appeal route where possible.

## 8. Intra-family and third-party disclosure

One family member's private statement MUST NOT be exposed to another without
a governed disclosure basis.

Disclosure MUST be minimum necessary and MUST NOT automatically expose:

- unrelated assertions;
- private source wording when a bounded summary is sufficient;
- a reporter's identity when protection is required;
- a contested interpretation as confirmed fact;
- historical or expired information without current relevance.

When notice is delayed for safety, the delay MUST be specific, review-bounded,
and independently reviewable.

## 9. Migration, correction propagation, and lineage

Imported or legacy assertions MUST retain:

- original source and time;
- prior knowledge status;
- prior visibility and permission basis where known;
- transformation history;
- migration actor and method;
- unresolved uncertainty;
- dependent records.

A correction or supersession MUST propagate to active dependent decisions,
profiles, summaries, and retrieval indexes without deleting historical audit
evidence.

Where safe rollback is not possible, the limitation and remediation plan
MUST be recorded.

## 10. Prohibited behavior

An implementation MUST NOT:

- label parent-authored data as the child's confirmed profile;
- hide a model inference or professional hypothesis as fact;
- retain a disputed label without visible dispute state;
- use a temporary crisis state as a permanent identity;
- remove original source, transformation, or revision history;
- deny contestability merely because the speaker is a professional;
- treat refusal to agree as evidence that the assertion is correct;
- expose a family member's statement without a governed disclosure basis;
- treat representative authority as unlimited or permanent;
- continue a high-impact use after expiry or supersession without review.

## 11. User experience requirements

A person reviewing an interpretation SHOULD be able to see:

- what was said;
- who supplied or generated it;
- whether AI or a professional inferred anything;
- evidence, uncertainty, and current status;
- materiality and impact class;
- how long it remains active;
- whether anyone disputed or revised it;
- representative and visibility basis;
- how to correct, contextualize, restrict, or appeal;
- which decisions and records currently depend on it.

## 12. Acceptance tests

A conforming implementation must demonstrate:

1. materiality defaults to the safer classification when uncertain;
2. a parent report remains visibly attributed to the parent;
3. a model inference cannot become confirmed fact without an explicit,
   reviewable transition;
4. a contested high-impact assertion pauses prohibited use or records the
   narrow exception;
5. representative authority is scoped, reviewable, expiring, and
   conflict-checked;
6. intra-family disclosure requires a specific governed basis;
7. an expired or superseded interpretation stops driving active
   recommendations;
8. correction propagates to dependent records while preserving history;
9. every high-impact use records responsible actor, basis, duration, review,
   and appeal;
10. every assertion used in a decision can be traced to source and status.

## 13. Remaining review questions

- Which jurisdiction profiles are required for initial reference
  implementations?
- Which assertion classes require fixed review periods rather than
  risk-based periods?
- Which independent-review roles are feasible at different service scales?
- How should participation interfaces be tested with children, adolescents,
  parents, and other affected people?
