---
id: ADR-0011
title: Separate Review Readiness from Status Promotion
status: Accepted
version: 1.0.0
layer: Cross-layer
owner: Ming Foundation Architecture
created: 2026-07-12
updated: 2026-07-12
related:
  - MOS-0000
  - GOV-0032
  - GOV-0033
  - GOV-0034
  - GOV-0035
  - REF-0003
depends_on:
  - ADR-0010
  - MOS-0000
---

# ADR-0011 — Separate Review Readiness from Status Promotion

## Context

Day 8 made RFC requirements machine-readable.

Day 9 adds fidelity review, test specifications, review checklists, ambiguity records, and a conformance baseline.

These artifacts can create a false impression that review or implementation has already occurred.

## Decision

Ming Foundation separates:

```text
Review preparation
Review execution
Status promotion
Implementation conformance
```

### Review preparation

Schemas, checklists, test specifications, source revision records, and reviewer instructions exist.

### Review execution

Accountable reviewers complete the checklist, record evidence, preserve objections, and identify required revisions.

### Status promotion

A dedicated proposal and governance decision change the RFC status.

### Implementation conformance

A named implementation revision is tested against selected requirements with bounded evidence.

No stage implies the next stage automatically.

## Consequences

- RFCs may be well prepared but remain Proposed.
- A conforming implementation does not automatically make an RFC Candidate or Stable.
- A promoted RFC does not imply every product conforms.
- An empty baseline can establish structure without making a product claim.
- Ambiguities may block promotion even when registry fidelity is confirmed.

## Decision for Day 9

RFC-0001 through RFC-0005 remain `Proposed`.

The Day 9 review state is `Prepared`, not `Complete`.
