---
id: ADR-0009
title: Separate Canonical Repository Audit from External Implementation Evidence
status: Accepted
version: 1.0.0
layer: Cross-layer
owner: Ming Foundation Architecture
created: 2026-07-12
updated: 2026-07-12
related:
  - ADR-0004
  - ADR-0008
  - GOV-0001
  - GOV-0002
  - GOV-0020
  - GOV-0021
  - GOV-0027
depends_on:
  - ADR-0004
  - GOV-0027
---

# ADR-0009 — Separate Canonical Repository Audit from External Implementation Evidence

## Context

`ADR-0004` established `YuemingHub/Ming-Foundation` as the canonical public repository.

Day 7 verified that repository, but its records then mixed repository audit completion with access to website and Family OS implementation sources.

This made an external evidence limitation appear to be a canonical repository blocker.

## Decision

Ming Foundation separates two governance activities.

### Canonical repository audit

The audit target is:

```text
YuemingHub/Ming-Foundation
```

A canonical repository audit evaluates the repository itself.

Its completion does not depend on access to:

- `Mingos-life`;
- another Family OS repository;
- `mingos.cn`;
- `ymai.love`;
- production systems.

### External implementation-conformance validation

External systems may be examined to determine whether products conform to repository standards.

Such evidence:

- is scope-limited;
- must identify its revision and method;
- does not become canonical authority;
- does not block repository governance unless a specific accepted decision explicitly requires it;
- requires explicit user scope before another repository is changed.

## Status of Day 7

The Day 7 canonical repository audit is accepted.

The Day 7 external implementation evidence remains bounded and incomplete.

These two statements are compatible.

## Consequences

### Positive

- the canonical source of truth remains unambiguous;
- repository work can continue without unrelated access blockers;
- implementation evidence can still challenge or validate standards;
- future agents cannot silently expand repository scope;
- user authorization remains the boundary for work in other repositories.

### Negative

- repository standards may exist before product conformance is proven;
- later Charter acceptance may still require implementation and affected-person evidence;
- external evidence must be tracked separately.

## Supersession

This ADR supersedes `ADR-0008` where `ADR-0008` treated incomplete external access as a limitation on the Day 7 audit as a whole.

`ADR-0008` remains in history with status `Superseded`.

## Follow-up

1. Apply the corrections in `GOV-0027`.
2. Reclassify Day 7 product tasks as external evidence targets.
3. Add automated scope validation.
4. Continue Day 8 in `YuemingHub/Ming-Foundation`.
5. Enter another repository only after explicit user instruction.
