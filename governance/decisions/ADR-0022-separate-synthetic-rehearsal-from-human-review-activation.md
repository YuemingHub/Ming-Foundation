---
id: ADR-0022
title: Separate Synthetic Rehearsal from Human Review Activation
status: Accepted
version: 1.0.0
layer: Cross-layer
owner: Ming Foundation Architecture
created: 2026-07-14
updated: 2026-07-14
related:
  - ADR-0020
  - GOV-0084
  - GOV-0085
  - GOV-0086
  - GOV-0087
  - GOV-0090
depends_on:
  - ADR-0020
---

# ADR-0022 — Separate Synthetic Rehearsal from Human Review Activation

## Decision

Ming Foundation separates:

```text
protocol design
synthetic rehearsal authorization
internal staff rehearsal authorization
human participant review activation
product implementation conformance
```

Passing a synthetic rehearsal MUST NOT create authority to recruit, schedule,
collect participant evidence, act on a person, or claim product conformance.

## Day 16 consequence

CP0 and CP1 may proceed. CP2 and CP3 remain blocked.
