---
id: ADR-0002
title: Observation Before Advice
status: Accepted
version: 1.0.0
layer: Layer 2 — Standards
owner: Ming Foundation Architecture
created: 2026-07-12
updated: 2026-07-12
related:
  - MF-0003
depends_on:
  - ADR-0001
---

# ADR-0002 — Observation Before Advice

## Context

Advice-oriented systems often respond immediately to a reported problem. In family, education, growth, and emotionally sensitive contexts, the reported event is rarely equivalent to its cause.

Immediate advice can:

- misread the situation;
- increase blame or anxiety;
- ignore relationship history;
- encourage control;
- create false certainty;
- bypass the user’s own meaning and choice.

## Decision

Ming-conforming systems should establish an observation before giving consequential advice.

An observation should identify, as applicable:

- what happened;
- who is involved;
- time and context;
- the user’s account and uncertainty;
- emotions and needs;
- relationship dynamics;
- relevant history;
- possible interpretations;
- evidence and confidence;
- what requires user confirmation.

Advice may be brief in low-risk, low-ambiguity situations, but it must not conceal uncertainty or replace the person’s choice.

## Consequences

### Positive

- More accurate and contextual support.
- Clear distinction between user statement and system inference.
- Better long-term memory and pattern quality.
- Greater opportunity for user correction.

### Negative

- Responses may take longer.
- The system must ask better questions rather than maximize instant answers.
- Product metrics based on answer speed may conflict with this decision.

## Implementation note

The first MingOS reference loop should support:

```text
Expression
  → Structured Observation
  → User Confirmation or Correction
  → Options
  → User Choice
  → Follow-up
```
