---
created: 2026-07-12
depends_on:
- PROJECT-MINGOS-0002
- GOV-0005
- GOV-0013
id: GOV-0015
layer: Layer 5 — Community & Governance
owner: Ming Foundation Governance
related:
- PROJECT-MINGOS-0002
- GOV-0011
- GOV-0012
- GOV-0014
- GOV-0016
- GOV-0018
- GOV-0019
- RFC-0003
- ADR-0007
status: Proposed
title: Charter Violation Reporting and Remediation Procedure
updated: 2026-07-12
version: 0.1.0
---

# GOV-0015 — Charter Violation Reporting and Remediation Procedure

## Status

Proposed governance procedure. It requires independent review before
acceptance.

## 1. Purpose

A Charter has no practical force if violations cannot be reported,
investigated, corrected, appealed, and traced.

This procedure applies to alleged violations by:

- products;
- AI systems;
- professionals;
- maintainers;
- employees or contractors;
- commercial partners;
- reviewers;
- governance members;
- founders.

No role is exempt.

## 2. Reporting channels

A future implementation SHOULD provide:

- a public Charter-concern route;
- a privacy and data-rights route;
- an internal staff route;
- a protected route for serious conflicts involving leadership;
- an emergency route clearly separated from ordinary Charter reporting.

A reporter should be able to state whether contact or public attribution
is safe.

## 3. Intake record

Minimum fields:

- report ID;
- time;
- reporter relationship;
- affected people;
- alleged commitment;
- product, process, person, or decision involved;
- ongoing-harm indicator;
- safety and privacy constraints;
- supporting evidence;
- requested outcome;
- conflict-of-interest flags;
- handling classification.

## 4. Severity

Suggested classes:

### S0 — Question or interpretation request

No alleged harm; clarification or correction may resolve it.

### S1 — Local non-conformance

Limited impact, reversible, no ongoing material harm.

### S2 — Material violation

Meaningful rights, safety, professional, privacy, or commercial impact.

### S3 — Severe or systemic violation

Serious harm, repeated misconduct, leadership conflict, vulnerable
people, deliberate concealment, or broad affected population.

Severity must not be reduced to protect reputation.

## 5. Process

``` text
Report received
  ↓
Safety and conflict screening
  ↓
Independent case owner assigned
  ↓
Contain ongoing harm
  ↓
Preserve evidence with restricted access
  ↓
Affected people consulted where safe
  ↓
Finding and remediation
  ↓
Notification and appeal
  ↓
Root-cause and recurrence review
  ↓
Public or restricted transparency record
```

## 6. Conflict management

A person MUST NOT control the investigation when they:

- are the subject of the report;
- approved the disputed action;
- have a direct commercial interest;
- supervise the reporter or affected reviewer;
- have a close personal or organizational conflict.

Reports involving a founder or governance authority require a reviewer
with sufficient independence to recommend restriction, suspension, or
public disclosure.

## 7. Immediate containment

Containment may include:

- stopping a public claim;
- disabling a feature;
- restricting access;
- freezing a disputed profile assertion;
- pausing a data export or model use;
- changing a safety route;
- separating a conflicted reviewer;
- notifying an affected person;
- preserving evidence.

Containment is not a final finding.

## 8. Outcomes

Possible outcomes include:

- no violation found;
- clarification;
- correction;
- data repair;
- apology;
- user remedy;
- access restriction;
- policy or product change;
- retraining;
- independent audit;
- partner suspension;
- withdrawal of MingOS naming or conformance claim;
- referral to an appropriate external authority where required.

## 9. Appeal

A material finding SHOULD allow appeal to a reviewer who did not make
the initial decision.

The appeal record must preserve:

- original finding;
- new evidence;
- reviewer;
- decision;
- rationale;
- changed remediation.

## 10. Transparency

Public reporting should provide enough information to show that
governance is real without exposing private or unsafe material.

A transparency record may include:

- category;
- affected scope;
- confirmed commitments;
- action;
- remediation;
- recurrence control;
- unresolved disagreement.

## 11. Acceptance requirements

Before this procedure may become Accepted:

- independent reviewer authority must be defined;
- reporting channels must exist;
- evidence access must follow `GOV-0018`;
- severe-report conflict rules must be tested;
- appeal must be operational;
- at least one tabletop exercise involving a founder or commercial
  conflict must be completed;
- sanctions and reinstatement criteria must be reviewed.
