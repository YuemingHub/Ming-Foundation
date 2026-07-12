---
id: ADR-0018
title: Retain Profiles as Proposed and Require Affected-Person Review
status: Accepted
version: 1.0.0
layer: Cross-layer
owner: Ming Foundation Architecture
created: 2026-07-13
updated: 2026-07-13
related:
  - PROF-0001
  - PROF-0002
  - PROF-0003
  - PROF-0004
  - GOV-0061
  - GOV-0066
  - GOV-0067
  - GOV-0069
  - GOV-0070
depends_on:
  - ADR-0016
  - GOV-0061
---

# ADR-0018 — Retain Profiles as Proposed and Require Affected-Person Review

## Decision

Retain PROF-0001 through PROF-0004 at `Proposed`.

Before a profile may be considered for Candidate or Accepted status, it must:

1. complete the planned internal source revisions;
2. complete internal re-review;
3. complete applicable affected-person and domain review;
4. complete jurisdiction or professional-duty qualification where required;
5. preserve dissent, minority views, counterexamples, and unresolved limits;
6. obtain a separate promotion decision.

## Preparation boundary

`PreparedNotExecuted` is a valid governance state.

It must never be described as participant approval, consultation completed,
or evidence gathered.
