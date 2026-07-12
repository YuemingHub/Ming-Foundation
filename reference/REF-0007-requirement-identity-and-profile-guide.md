---
id: REF-0007
title: Requirement Identity and Residual Profile Guide
status: Accepted
version: 1.0.0
layer: Layer 3 — Reference
owner: Ming Foundation Standards and Validation
created: 2026-07-12
updated: 2026-07-12
related:
  - GOV-0056
  - GOV-0057
  - GOV-0058
  - GOV-0059
  - ADR-0016
depends_on:
  - ADR-0016
---

# REF-0007 — Requirement Identity and Residual Profile Guide

## Requirement states

```text
CurrentRebaselined
CurrentConfirmed
ArchivedLegacy
```

## Mapping types

```text
Unchanged
RetainedAndRefined
Split
Merged
Replaced
Retired
```

Day 13 uses only `Unchanged` and `RetainedAndRefined`.

## Profile state

```text
DesignedPendingReview
```

means:

- a concrete configuration model exists;
- machine requirements may reference it;
- it has not completed required review;
- linked ambiguities remain Open;
- it must not be treated as universal law or product behavior.

## Key distinction

```text
Complete derived baseline
≠ RFC Candidate
≠ profile Accepted
≠ affected-person acceptance
≠ legal validity
≠ implementation conformance
```
