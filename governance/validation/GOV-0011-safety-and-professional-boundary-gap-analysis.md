---
id: GOV-0011
title: Safety and Professional Boundary Gap Analysis
status: Accepted
version: 1.0.0-alpha.5
layer: Layer 5 — Community & Governance
owner: Ming Foundation Governance
created: 2026-07-12
updated: 2026-07-12
related:
  - MF-0004
  - PROJECT-MINGOS-0002
  - GOV-0006
  - GOV-0007
  - GOV-0009
  - GOV-0012
  - GOV-0013
depends_on:
  - GOV-0006
  - GOV-0009
---

# GOV-0011 — Safety and Professional Boundary Gap Analysis

## 1. Purpose

This analysis evaluates whether current safety and professional-boundary evidence is sufficient for the Candidate Charters.

## 2. Existing strengths

Documentary evidence indicates:

- one unified risk gate used across main and fallback paths;
- red, yellow, orange, and green handling;
- categories for self-harm, violence, abuse, sexual harm, psychosis, medical concerns, bullying, parent loss of control, depression/low energy, coercion, covert monitoring, and punitive cutoff;
- crisis, escalation, parent-holding, and ordinary branches;
- professional-escalation metadata;
- output quality and science review;
- red-team, safety, privacy, resilience, regression, and launch tests;
- separate admin and parent surfaces.

These are substantial safety foundations.

## 3. Material gaps

### P0 — Responsible actor and handoff

An escalation route does not by itself establish accountability.

Every high-risk pathway requires:

- the responsible actor;
- expected response time;
- acknowledgment;
- handoff status;
- inability-to-reach procedure;
- information disclosed and legal basis;
- resolution or closure;
- post-event review.

### P0 — Thresholds and proportionality

Risk categories and keywords require scenario-level validation.

The system must distinguish:

- expression from imminent intent;
- historical event from current danger;
- parent report from direct subject report;
- ordinary conflict from abuse;
- low energy from emergency;
- legitimate privacy from covert surveillance risk.

Over-escalation can create control and surveillance. Under-escalation can create harm.

### P0 — Local and professional boundaries

The system must not present itself as emergency response, diagnosis, clinical care, legal advice, or child-protection authority.

Required direction:

- location-aware emergency guidance;
- visible role disclosure;
- qualified professional review criteria;
- jurisdiction-sensitive child-protection and mandatory-reporting handling;
- no fabricated availability or guaranteed response.

### P1 — Appeal and correction

Safety classifications can be wrong.

Required direction:

- preserve evidence and model/policy version;
- allow non-emergency correction;
- provide human review;
- record false positive and false negative outcomes;
- ensure a disputed classification does not become a permanent identity label.

### P1 — AI and human responsibility

The current implementation includes AI and human-support components, but complete role disclosure is not evidenced.

Required direction:

- identify AI-generated or inferred content;
- identify when a human reviewed or changed it;
- record final responsible actor;
- prevent professional users from treating AI summaries as verified fact;
- preserve original source and uncertainty.

### P1 — Parent loss of control and child protection

When the parent is the customer, the system must still protect the child and other family members.

Required direction:

- avoid siding automatically with the operator;
- detect threats, humiliation, coercion, physical harm, and punitive deprivation;
- prioritize immediate safety without turning all conflict into surveillance;
- provide routes for independent human review.

### P1 — Incident and Charter violation response

Monitoring and escalation logs are not a complete incident process.

Required direction:

- report intake;
- severity;
- containment;
- affected-person notification;
- remediation;
- appeal;
- root cause;
- recurrence controls;
- suspension or restriction of non-conforming implementation;
- public and restricted reporting boundaries.

## 4. Safety success criteria

Safety should not be evaluated only by the number of detected risk messages.

Required measures include:

- false positive and false negative review;
- response time;
- successful human handoff;
- user understanding of limits;
- proportionality;
- appeal outcome;
- recurrence;
- harm avoided or introduced;
- privacy impact;
- whether capacity and relationship were strengthened.

## 5. Validation recommendation

V4 remains:

```text
Safety and professional boundaries: Partial
```

The existing foundation is strong enough to preserve and improve. It is not complete enough to justify Charter acceptance.
