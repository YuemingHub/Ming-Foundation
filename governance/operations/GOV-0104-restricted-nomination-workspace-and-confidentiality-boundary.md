---
id: GOV-0104
title: Restricted Nomination Workspace and Confidentiality Boundary
status: Accepted
version: 1.0.0
layer: Layer 5 — Community & Governance
owner: Ming Foundation Review Governance
created: 2026-07-15
updated: 2026-07-15
related:
  - GOV-0094
  - GOV-0096
  - GOV-0105
  - GOV-0106
  - ADR-0027
  - GOV-TPL-0029
  - GOV-TPL-0030
depends_on:
  - GOV-0094
  - ADR-0024
---

# GOV-0104 — Restricted Nomination Workspace and Confidentiality Boundary

## Decision

Real names, personal contact details, signatures, certificates, identity
evidence, conflict details, qualification evidence, and role acceptance
records MUST remain outside the public repository.

The default local workspace is:

```text
.ming-private/day18-role-nomination/
```

It MUST be ignored by Git.

## Public repository boundary

The public repository may record:

- public accountability IDs;
- slot and role states;
- non-identifying restricted-record references;
- aggregate completion counts;
- decision and expiry states.

It MUST NOT contain the private source records.

## Current state

```text
Workspace claimed initialized: no
Real identity records claimed: 0
Nominations claimed:           0
Acceptances claimed:           0
Verification records claimed:  0
```
