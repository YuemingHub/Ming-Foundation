---
created: 2026-07-12
depends_on:
  - MF-0004
  - PROJECT-MINGOS-0002
  - RFC-0001
  - RFC-0002
  - ADR-0013
id: RFC-0003
layer: Layer 1 — Standards
owner: Ming Foundation Standards
related:
  - MF-0004
  - PROJECT-MINGOS-0002
  - GOV-0011
  - GOV-0015
  - GOV-0039
  - GOV-0044
  - GOV-0047
  - GOV-0048
  - ADR-0013
  - ADR-0014
status: Proposed
title: Safety Escalation Human Handoff Appeal and Incident Protocol
updated: 2026-07-12
version: 0.2.0-draft.1
---

# RFC-0003 — Safety Escalation, Human Handoff, Appeal, and Incident Protocol

## Status

Proposed revised draft. This revision implements `REV-0009` through
`REV-0012` and the applicable R0 decisions from `ADR-0013`.

Existing risk gates remain implementation evidence, not proof of
conformance.

## 1. Problem

Detecting risk is not the same as safely handling it.

A complete safety path must identify evidence and uncertainty, accountable
authority, service availability, proportionality, handoff state, disclosure,
correction, appeal, and incident learning.

## 2. Safety classifications

### 2.1 High-impact safety action

A safety action is high impact when it can restrict rights or access, disclose
sensitive information, involve an external authority or professional, create
a durable risk label, materially change service, or be difficult to reverse.

Every high-impact safety action MUST have:

- a named responsible role with actual authority;
- recorded evidence and uncertainty;
- severity and immediacy class;
- bounded action and duration;
- proportionality record;
- handoff or service-availability state;
- review deadline;
- correction or appeal route where possible.

A queue, model, mailbox, or unnamed team is not a named responsible role.

### 2.2 P0 and P1

`P0` means credible evidence indicates imminent or unfolding severe harm and
delay may materially increase danger.

`P1` means credible serious risk requires prompt accountable review or
protective action but the available evidence does not establish an immediate
P0 condition.

Classification MUST record:

- current versus historical evidence;
- direct versus third-party report;
- plan, means, opportunity, and immediacy where relevant;
- protective factors;
- uncertainty and missing information;
- responsible classifier;
- next review deadline.

A classification profile MUST define response targets and escalation
ownership for each service model. This RFC does not create a universal
emergency-response promise.

## 3. Service availability profiles

Every implementation MUST publish and record one current service profile:

- `active_handoff` — a staffed and governed human or service handoff exists;
- `bounded_review` — accountable review exists within stated availability,
  but no emergency response is promised;
- `no_handoff` — the system cannot receive or manage an active handoff and
  only provides transparent redirection;
- `unverified` — availability or resource freshness cannot be confirmed.

The profile MUST state:

- responsible organization or role;
- operating hours and response target;
- supported locations and languages;
- unavailable services;
- escalation and failed-handoff action;
- last verification date;
- expiry date;
- owner.

A `no_handoff` or `unverified` system MUST NOT mark a safety handoff complete
or imply that a human is monitoring the situation.

## 4. Required records

### 4.1 Safety signal

Minimum fields:

- `signal_id`;
- `source`;
- `subject`;
- `reporter`;
- `time`;
- `category`;
- `evidence`;
- `uncertainty`;
- `model_or_policy_version`;
- `current_or_historical`;
- `direct_or_third_party_report`.

### 4.2 Safety assessment

Minimum fields:

- `assessment_id`;
- `signals`;
- `risk_level`;
- `immediacy`;
- `potential_harm`;
- `protective_factors`;
- `unknowns`;
- `recommended_action`;
- `least_intrusive_alternative`;
- `responsible_reviewer`;
- `review_time`;
- `next_review_at`.

### 4.3 Handoff

Minimum fields:

- `handoff_id`;
- `service_profile`;
- `responsible_role`;
- `target_person_or_service`;
- `initiated_at`;
- `acknowledged_at`;
- `accepted_at`;
- `information_disclosed`;
- `basis`;
- `response_target`;
- `status`;
- `failed_handoff_action`;
- `closure_reason`;
- `closure_authority`.

Allowed states MUST distinguish:

- initiated;
- acknowledged;
- accepted;
- failed;
- redirected;
- closed.

A handoff MUST NOT be marked closed merely because a message was sent.

### 4.4 Safety action

Minimum fields:

- `action_id`;
- `assessment_id`;
- `actor`;
- `authority_scope`;
- `action`;
- `scope`;
- `duration`;
- `affected_people`;
- `notice`;
- `notice_delay_reason`;
- `proportionality_record`;
- `review_at`;
- `appeal_or_correction_path`.

### 4.5 Incident review

Minimum fields:

- `incident_id`;
- `severity`;
- `harm_or_near_miss`;
- `false_positive_or_false_negative`;
- `timeline`;
- `responsible_roles`;
- `root_causes`;
- `privacy_impact`;
- `remediation`;
- `recurrence_controls`;
- `closure_authority`.

## 5. Proportionality record

The selected response SHOULD be the least intrusive action that reasonably
addresses the identified risk.

For every high-impact action, the record MUST state:

- harm being prevented;
- evidence and uncertainty;
- urgency;
- affected-person preference where safely available;
- less intrusive alternatives considered;
- reason alternatives were insufficient;
- privacy and disclosure cost;
- action scope and duration;
- safeguards;
- review deadline;
- rollback, correction, or appeal path.

A more intrusive temporary action under severe uncertainty requires a
specific precautionary basis, shortest reasonable duration, and independent
or conflict-free review.

## 6. Safety path

```text
Signal
  ↓
P0 / P1 / lower classification with uncertainty
  ↓
Service availability checked
  ↓
Bounded assessment and proportionality record
  ↓
Immediate temporary response if required
  ↓
Named responsible role or transparent no-handoff redirection
  ↓
Acknowledgment, acceptance, failure, or closure tracked
  ↓
Notice, correction, or appeal when possible
  ↓
Incident / near-miss review
  ↓
Policy, model, product, access, training, or governance remediation
```

## 7. Professional, legal, and resource boundaries

MingOS MUST NOT claim to be:

- an emergency-response service;
- a medical or psychiatric diagnosis service;
- legal advice;
- a child-protection authority;
- a guaranteed human-response service unless staffed and governed.

Public and in-product messaging MUST state:

- current service profile;
- whether AI or a human is responding;
- available and unavailable response;
- operating and geographic limits;
- route to local qualified or emergency support;
- resource owner, verification date, and expiry where resources are listed.

Expired or unverified local resources MUST NOT be presented as current.

## 8. Appeal, correction, and lineage

Non-immediate safety classifications SHOULD be contestable.

The system MUST preserve:

- original evidence;
- model and policy version;
- responsible reviewer;
- classification changes;
- false-positive and false-negative outcomes;
- downstream records influenced by the classification;
- correction and supersession propagation;
- review and appeal history.

A disputed, expired, or superseded safety label MUST NOT become a permanent
identity marker or silently continue to drive recommendations.

## 9. Operator may be the risk source

Independent or conflict-free review MUST be triggered when:

- the operator is alleged to be causing harm;
- the operator's interests materially conflict with the subject;
- the requested action restricts the subject's rights, participation, or
  access;
- a high-impact classification is disputed;
- the operator requests access to protected reporter or subject information;
- the same role would report, decide, and close the action without oversight.

The review pathway MUST support:

- minimum disclosure;
- child or third-party protection;
- interim access restrictions;
- independent decision authority;
- reason, duration, and review of restrictions;
- later notice and appeal where safe and lawful.

The system MUST NOT automatically side with the operator.

## 10. Migration and correction propagation

Historical risk records MUST retain source, policy version, classification
history, and downstream effects.

When a classification is corrected or superseded, active profiles,
recommendations, restrictions, retrieval indexes, and dependent decisions
MUST be updated.

Where complete rollback is impossible, the limitation, remaining exposure,
and remediation plan MUST be recorded.

## 11. Acceptance tests

A conforming implementation must demonstrate:

1. every P0/P1 escalation has a responsible role with actual authority;
2. a queue or sent message cannot be treated as completed handoff;
3. service profile, availability, owner, verification date, and expiry are
   visible;
4. a `no_handoff` system does not imply active monitoring;
5. every high-impact action records proportionality, scope, duration,
   safeguards, review, and appeal;
6. failed handoff has a named next action and owner;
7. false-positive and false-negative cases are reviewable;
8. a model or policy change triggers safety regression review;
9. operator and subject are not assumed to be the same person;
10. operator-as-risk scenarios trigger conflict-free review;
11. no risk label becomes permanent without review and lineage;
12. public messages do not promise unavailable emergency or professional
    care.

## 12. Remaining review questions

- Which response targets are credible for each service profile?
- Which P0/P1 events require external professional or legal review in each
  jurisdiction?
- Which organizations may qualify as independent reviewers?
- How should resource freshness be independently verified?
- Which safety records may be visible to which affected people?
