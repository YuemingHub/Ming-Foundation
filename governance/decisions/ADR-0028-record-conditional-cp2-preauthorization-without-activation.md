---
id: ADR-0028
title: Record Conditional CP2 Pre-Authorization Without Activation
status: Accepted
version: 1.0.0
layer: Cross-layer
owner: Ming Foundation Architecture
created: 2026-07-15
updated: 2026-07-15
related:
  - GOV-0105
  - GOV-0107
  - GOV-0108
  - GOV-0109
  - GOV-0110
depends_on:
  - ADR-0025
  - GOV-0109
---

# ADR-0028 — Record Conditional CP2 Pre-Authorization Without Activation

## Decision

Approve only the work required to make a future CP2 activation decision.

Retain:

```text
CP2 authorization: Blocked
CP2 execution:     NotExecuted
CP3 authorization: Blocked
```

## Reason

A pre-authorization decision can clarify conditions and reduce ambiguity
without claiming that real people, approvals, controls, or operating-context
evidence already exist.

A separate effective activation decision remains mandatory.
