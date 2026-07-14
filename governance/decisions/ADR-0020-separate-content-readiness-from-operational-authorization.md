---
id: ADR-0020
title: Separate Content Readiness from Operational Authorization
status: Accepted
version: 1.0.1
layer: Cross-layer
owner: Ming Foundation Review Governance
created: 2026-07-13
updated: 2026-07-13
related:
  - GOV-0067
  - GOV-0069
  - GOV-0077
  - GOV-0078
  - GOV-0079
depends_on:
  - ADR-0018
  - GOV-0077
---

# ADR-0020 — Separate Content Readiness from Operational Authorization

## Decision

Ming Foundation separates:

```text
ContentReady
OperationallyReadyToSchedule
RecruitmentAuthorized
SessionsAuthorized
EvidenceCollected
ReviewComplete
```

These states MUST NOT be collapsed.

## Day 15 state

```text
ContentReady:                  yes
OperationallyReadyToSchedule:  no
RecruitmentAuthorized:         no
SessionsAuthorized:            no
EvidenceCollected:             no
ReviewComplete:                no
```

## Authorization rule

A separate activation decision is required after:

- real accountable role assignment;
- conflict and qualification checks;
- protocol approval;
- evidence-environment provisioning and testing;
- jurisdiction and professional qualification;
- independent facilitator assignment where required.

A template, role name, or planned control is not evidence that the control is
operational.

## Day 16 extension

Synthetic rehearsal authorization is now an additional state between content
readiness and human operational authorization. It does not satisfy any human
activation gate.
