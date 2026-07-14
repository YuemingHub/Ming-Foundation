---
id: GOV-0087
title: Controlled Pilot Classification and Authorization Matrix
status: Accepted
version: 1.0.0
layer: Layer 5 — Community & Governance
owner: Ming Foundation Architecture and Review Governance
created: 2026-07-14
updated: 2026-07-14
related:
  - GOV-0077
  - GOV-0078
  - GOV-0088
  - GOV-0089
  - GOV-0090
  - ADR-0022
  - ADR-0023
depends_on:
  - GOV-0077
  - GOV-0078
---

# GOV-0087 — Controlled Pilot Classification and Authorization Matrix

| Class | Description | Day 16 state | Real people | Real evidence | Live decision effect |
|---|---|---|---:|---:|---:|
| CP0 | Document tabletop walkthrough | Authorized and complete | No | No | No |
| CP1 | Synthetic-data operational rehearsal | Authorized and complete | No | No | No |
| CP2 | Internal staff process rehearsal | Blocked | No participant evidence | No | No |
| CP3 | Affected-person controlled pilot | Blocked | Yes | Restricted | Potentially yes |

## CP0 and CP1 boundaries

- synthetic or no data only;
- repository validation environment only;
- no production integration;
- no person-level decision or recommendation;
- no service, safety, legal, professional, or conformance claim;
- any real or identifiable evidence triggers stop and deletion review.

## Authorization result

```text
Overall: SyntheticOnlyAuthorized
Authorized: CP0, CP1
Blocked: CP2, CP3
```
