---
id: REF-0003
title: RFC Review and Conformance Baseline Guide
status: Accepted
version: 1.0.0
layer: Layer 3 — Reference
owner: Ming Foundation Standards and Validation
created: 2026-07-12
updated: 2026-07-12
related:
  - GOV-0032
  - GOV-0033
  - GOV-0034
  - GOV-0035
  - ADR-0011
depends_on:
  - GOV-0033
  - GOV-0035
  - ADR-0011
---

# REF-0003 — RFC Review and Conformance Baseline Guide

## Use this sequence

```text
Read source RFC
  ↓
Check requirement fidelity
  ↓
Review open ambiguities
  ↓
Complete RFC checklist
  ↓
Revise or retain source
  ↓
Make a separate status decision
  ↓
Select implementation target
  ↓
Execute conformance tests
```

## Key files

- `RFC_REQUIREMENTS.json`;
- `RFC_ACCEPTANCE_TESTS.json`;
- `RFC_REVIEW_CHECKLISTS.json`;
- `RFC_AMBIGUITIES.json`;
- `FOUNDATION_CONFORMANCE_BASELINE.json`;
- GOV-TPL-0005 through GOV-TPL-0009.

## Do not collapse these statements

```text
The requirement is faithfully indexed.
The RFC is ready for Candidate.
A test specification exists.
The test was executed.
The test passed.
A product conforms.
The Charter is validated.
```

Each statement requires separate evidence.
