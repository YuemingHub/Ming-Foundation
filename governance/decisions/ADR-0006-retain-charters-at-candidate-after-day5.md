---
id: ADR-0006
title: Retain Both Charters at Candidate After Day 5
status: Accepted
version: 1.0.0
layer: Cross-layer
owner: Ming Foundation Architecture
created: 2026-07-12
updated: 2026-07-12
related:
  - MF-0004
  - PROJECT-MINGOS-0002
  - ADR-0005
  - GOV-0006
  - GOV-0007
  - GOV-0013
depends_on:
  - ADR-0005
  - GOV-0006
  - GOV-0013
---

# ADR-0006 — Retain Both Charters at Candidate After Day 5

## Context

Day 4 moved the Charter of Life and MingOS Charter to Candidate status and required structured validation.

Day 5 examined:

- website and public communication evidence;
- Family OS implementation evidence;
- privacy and third-party rights;
- safety and professional boundaries;
- counterexamples and risk;
- the requirements of `GOV-0006`.

Available evidence shows meaningful implementation alignment but also material unresolved gaps.

## Decision

Ming Foundation retains:

```text
MF-0004                 Candidate
PROJECT-MINGOS-0002     Candidate
```

Neither Charter moves to `Accepted` or `Stable`.

## Reasons

- affected-person validation is not complete;
- child and third-party contestability is not complete;
- privacy and data-rights architecture is partial;
- direct live website and direct source-code audits are incomplete;
- safety accountability and appeal are incomplete;
- commercial anti-anxiety and anti-dependency behavior is not verified;
- Charter violation enforcement is incomplete;
- legal and jurisdiction review is not complete.

## Consequences

### Positive

- repository status remains evidence-based;
- the project does not convert internal confidence into false consensus;
- implementation strengths are preserved without hiding gaps;
- Day 6 has a concrete remediation target.

### Negative

- MingOS cannot yet publicly present the Charters as accepted standards;
- public website and product material require careful Candidate/status wording;
- additional external and implementation review work is required.

## Rejected alternative

### Accept both Charters because the direction is clearly correct

Rejected.

A credible Charter must survive disagreement, affected-person review, implementation conflict, legal qualification, and counterexample testing. Internal coherence and founder alignment are not sufficient.

## Follow-up

1. Execute the P0 remediation priorities in `GOV-0007`.
2. Prepare external-review materials.
3. Audit the live website and current implementation directly.
4. Reconsider status only through a dedicated future governance decision.
