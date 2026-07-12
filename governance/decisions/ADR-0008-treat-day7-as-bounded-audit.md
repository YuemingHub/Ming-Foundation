---
created: 2026-07-12
depends_on:
- ADR-0007
- GOV-0020
- GOV-0026
id: ADR-0008
layer: Cross-layer
owner: Ming Foundation Architecture
related:
- ADR-0006
- ADR-0007
- GOV-0020
- GOV-0021
- GOV-0025
- GOV-0026
status: Accepted
title: Treat Day 7 as a Bounded Audit and Retain Current Statuses
updated: 2026-07-12
version: 1.0.0
---

# ADR-0008 — Treat Day 7 as a Bounded Audit and Retain Current Statuses

## Context

Day 7 was intended to directly audit:

- current website source and live pages;
- current Family OS source, tests, and runtime evidence;
- Day 6 remediation contracts;
- Day 5 counterexamples.

The canonical Ming Foundation repository was directly accessible.

The private website repository, current Family OS source repository, and
live domains were not accessible to the audit environment.

High-quality documentary snapshots were available, but they cannot be
represented as current direct evidence.

## Decision

Ming Foundation treats Day 7 as:

- a direct access attempt;
- a bounded documentary code audit;
- an accepted remediation implementation backlog.

It does not treat Day 7 as a completed direct current-source or
production conformance audit.

The following statuses remain unchanged:

``` text
MF-0004                 Candidate
PROJECT-MINGOS-0002     Candidate
RFC-0001 — RFC-0005     Proposed
GOV-0015                Proposed
```

## Consequences

### Positive

- the repository preserves evidence honesty;
- inaccessible systems are not guessed;
- current implementation strengths remain visible;
- P0 work is translated into an actionable backlog;
- future audit access becomes an explicit prerequisite.

### Negative

- direct audit remains incomplete;
- some backlog items may change after current source access;
- protocol promotion and Charter acceptance remain blocked;
- additional repository and runtime access coordination is required.

## Rejected alternatives

### Mark the direct audit complete using CODE_WIKI

Rejected because a dated code wiki is documentary evidence, not current
source execution.

### Promote RFCs because the backlog is detailed

Rejected because a design and backlog do not prove implementation or
review.

### Stop Day 7 entirely because access is incomplete

Rejected because bounded evidence can still identify risk, preserve
uncertainty, and define the next implementation work.

## Follow-up

1.  Register current implementation repositories and revisions.
2.  Execute Wave 0 of `GOV-0025`.
3.  Re-run the direct audit with reproducible evidence.
4.  Begin Wave 1 implementation.
5.  Reconsider RFC status only after evidence and review.
