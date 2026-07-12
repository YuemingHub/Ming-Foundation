---
created: 2026-07-12
depends_on:
- MF-0004
- PROJECT-MINGOS-0002
id: RFC-0003
layer: Layer 1 — Standards
owner: Ming Foundation Standards
related:
- MF-0004
- PROJECT-MINGOS-0002
- GOV-0011
- GOV-0012
- GOV-0014
- GOV-0015
- GOV-0019
- ADR-0007
status: Proposed
title: Safety Escalation Human Handoff Appeal and Incident Protocol
updated: 2026-07-12
version: 0.1.0
---

# RFC-0003 — Safety Escalation, Human Handoff, Appeal, and Incident Protocol

## Status

Proposed minimum protocol. Existing risk gates are implementation
evidence, not proof of full conformance.

## 1. Problem

Detecting risk is not the same as safely handling it.

A complete safety path must answer:

- what was detected;
- what evidence and uncertainty exist;
- who is responsible;
- what action was taken;
- whether a human actually received the handoff;
- what information was disclosed;
- whether the action was proportionate;
- how a wrong decision is corrected;
- how the event is reviewed.

## 2. Core rule

Every high-impact safety action MUST have a named responsible role, a
recorded basis, a bounded action, a handoff state, and a review path.

AI may support triage. AI MUST NOT become the final unaccountable actor.

## 3. Required records

### 3.1 Safety signal

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

### 3.2 Safety assessment

Minimum fields:

- `assessment_id`;
- `signals`;
- `risk_level`;
- `immediacy`;
- `potential_harm`;
- `protective_factors`;
- `unknowns`;
- `recommended action`;
- `least_intrusive alternative`;
- `reviewer`;
- `review_time`.

### 3.3 Handoff

Minimum fields:

- `handoff_id`;
- `responsible_role`;
- `target_person_or_service`;
- `initiated_at`;
- `acknowledged_at`;
- `information_disclosed`;
- `basis`;
- `response_target`;
- `status`;
- `failed_handoff_action`;
- `closure_reason`.

### 3.4 Safety action

Minimum fields:

- `action_id`;
- `assessment_id`;
- `actor`;
- `action`;
- `scope`;
- `duration`;
- `affected_people`;
- `notice`;
- `review_at`;
- `appeal_or_correction_path`.

### 3.5 Incident review

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

## 4. Safety path

``` text
Signal
  ↓
Bounded assessment
  ↓
Immediate response if required
  ↓
Named human or service handoff
  ↓
Acknowledgment and status tracking
  ↓
Action and communication
  ↓
Correction or appeal when possible
  ↓
Incident / near-miss review
  ↓
Policy, model, product, or training remediation
```

## 5. Proportionality

The selected response SHOULD be the least intrusive action that
reasonably addresses the identified risk.

The record must distinguish:

- expression from plan;
- historical event from current event;
- direct report from third-party report;
- distress from imminent harm;
- conflict from abuse;
- privacy from covert surveillance;
- low energy from a medical or psychiatric emergency.

## 6. Professional and legal boundaries

MingOS MUST NOT claim to be:

- emergency response;
- a medical or psychiatric diagnosis service;
- legal advice;
- a child-protection authority;
- a guaranteed human-response service unless such a service is actually
  staffed and governed.

Public and in-product messaging must state:

- the system’s role;
- whether AI or a human is responding;
- what response can and cannot be expected;
- how local emergency or qualified support may be reached;
- that availability varies unless explicitly guaranteed.

## 7. Appeal and correction

Non-immediate safety classifications SHOULD be contestable.

The system must preserve:

- original evidence;
- model and policy version;
- responsible reviewer;
- classification changes;
- false-positive and false-negative outcomes;
- downstream records influenced by the classification.

A disputed safety label MUST NOT become a permanent identity marker.

## 8. Special case: operator may be the risk source

When a parent, partner, professional, or institution operating the
system may be causing harm, MingOS MUST NOT automatically side with the
operator.

The pathway should support:

- independent review;
- minimum disclosure;
- child or third-party protection;
- conflict-of-interest handling;
- documentation of why operator access is restricted, if applicable.

## 9. Acceptance tests

A conforming implementation must demonstrate:

1.  every P0/P1 escalation has a responsible role;
2.  a handoff cannot be marked complete without acknowledgment or an
    explicit failed-handoff state;
3.  safety action records basis, scope, duration, and review;
4.  false-positive and false-negative cases are reviewable;
5.  a model update triggers regression tests for safety scenarios;
6.  operator and subject are not assumed to be the same person;
7.  no risk label becomes a permanent profile fact without review;
8.  public messages do not promise unavailable emergency or professional
    care;
9.  incident remediation can change policy, prompt, code, access,
    training, or governance.

## 10. Open questions

- Which response times are realistic for each service model?
- Which events require external professional or legal review?
- How are local emergency resources maintained without becoming stale?
- Which safety records may be visible to which family members?
- How is an independent review triggered when the operator is the
  alleged source of harm?
