---
id: ADR-0027
title: Keep Restricted Nomination Records Outside the Public Repository
status: Accepted
version: 1.0.0
layer: Cross-layer
owner: Ming Foundation Review Governance
created: 2026-07-15
updated: 2026-07-15
related:
  - GOV-0104
  - GOV-0106
  - GOV-0108
depends_on:
  - ADR-0024
  - GOV-0104
---

# ADR-0027 — Keep Restricted Nomination Records Outside the Public Repository

## Decision

Use a Git-ignored local or separately controlled workspace for real identity,
contact, signature, qualification, conflict, and acceptance records.

The public repository stores only non-identifying accountability IDs,
aggregate states, and restricted references.

## Consequence

A public status change without a corresponding restricted source record is
invalid.

Private records MUST NOT be committed for convenience or audit visibility.
