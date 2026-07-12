---
id: ADR-0016
title: Adopt Current Requirement Baseline and Retain Profiles as Proposed
status: Accepted
version: 1.0.1
layer: Cross-layer
owner: Ming Foundation Architecture
created: 2026-07-12
updated: 2026-07-12
related:
  - GOV-0056
  - GOV-0057
  - GOV-0058
  - GOV-0059
  - GOV-0060
  - PROF-0001
  - PROF-0002
  - PROF-0003
  - PROF-0004
depends_on:
  - ADR-0015
  - GOV-0059
---

# ADR-0016 — Adopt Current Requirement Baseline and Retain Profiles as Proposed

## Decision 1 — Requirement baseline

Adopt:

```text
115 current requirements
115 current implementation acceptance-test specifications
63 archived legacy requirements
63 archived legacy acceptance-test specifications
63 explicit legacy mappings
52 new current requirement IDs
```

The current registry is a complete derived index for the present RFC source
versions.

## Decision 2 — Identity continuity

All 63 legacy requirement IDs remain valid identifiers and map to current
requirements.

No identifier is retired in Day 13.

## Decision 3 — Profile status

Retain:

```text
PROF-0001  Proposed
PROF-0002  Proposed
PROF-0003  Proposed
PROF-0004  Proposed
```

Profiles require review before they may be treated as accepted standards.

## Decision 4 — RFC status

Retain RFC-0001 through RFC-0005 at `Proposed`.

## Consequence

Day 13 closes the machine re-baseline work items R2R-005 and R2R-006.

It does not close profile ambiguities, execute affected-person review, or
establish implementation conformance.

## Day 14 confirmation

The 115-requirement baseline remains adopted.

PROF-0001 through PROF-0004 remain Proposed after internal review and are
governed by ADR-0018 for further review and promotion.
