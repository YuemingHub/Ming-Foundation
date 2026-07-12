---
created: 2026-07-12
depends_on:
- ADR-0005
- ADR-0006
- GOV-0013
id: ADR-0007
layer: Cross-layer
owner: Ming Foundation Architecture
related:
- MF-0004
- PROJECT-MINGOS-0002
- ADR-0005
- ADR-0006
- GOV-0014
- GOV-0019
- RFC-0001
- RFC-0002
- RFC-0003
- RFC-0004
- RFC-0005
status: Accepted
title: Require Minimum Remediation Contracts Before Charter Acceptance
updated: 2026-07-12
version: 1.0.0
---

# ADR-0007 — Require Minimum Remediation Contracts Before Charter Acceptance

## Context

Day 5 found that the Candidate Charters have meaningful implementation
support but material unresolved P0 gaps.

Without explicit remediation contracts, the project could:

- move directly into broad Kernel design;
- treat module names as proof of conformance;
- close risks through prose rather than implementation;
- conduct unstructured external review;
- lose traceability between Charter commitment, product behavior, and
  evidence.

## Decision

Before either Charter may move to `Accepted`, Ming Foundation requires
reviewed minimum contracts covering:

1.  subject, speaker, knowledge status, and contestability;
2.  consent and the complete data-rights lifecycle;
3.  safety escalation, human handoff, appeal, and incident review;
4.  case and cross-family evidence governance;
5.  public claims, Charter synchronization, and capability status;
6.  Charter-violation reporting and remediation;
7.  external and affected-person review;
8.  restricted validation-evidence handling.

The initial contracts are:

- `RFC-0001` through `RFC-0005`;
- `GOV-0015` through `GOV-0018`.

## Status boundary

Acceptance of this ADR means the contracts are required.

It does not mean every Proposed RFC or procedure is already accepted or
implemented.

## Conformance evidence

A contract may support Charter acceptance only when:

- the requirement is mapped to current implementation;
- gaps and conflicts are recorded;
- acceptance tests are executed;
- responsible owners exist;
- affected-person and independent review is completed where required;
- restricted evidence is handled under `GOV-0018`.

## Consequences

### Positive

- P0 gaps cannot be bypassed by unrelated architecture expansion;
- external review has concrete objects to evaluate;
- implementation work becomes traceable;
- Charter acceptance becomes evidence-based.

### Negative

- acceptance will take longer;
- current products may expose substantial remediation work;
- some protocols may require jurisdiction-specific variants;
- broad Kernel work remains constrained until foundational gaps are
  addressed.

## Rejected alternatives

### Accept the Charters first and implement details later

Rejected because core rights and safety mechanisms are part of the
commitment, not optional later features.

### Treat existing Family OS modules as automatic conformance

Rejected because documentary module evidence does not prove behavior,
coverage, rights, accountability, or production operation.

### Create one large Kernel specification immediately

Rejected because it would mix critical remediation with speculative
ecosystem architecture.

## Follow-up

1.  Merge Day 6 artifacts.
2.  Perform Day 7 direct audit and backlog mapping.
3.  Review Proposed RFCs with affected and independent reviewers.
4.  Promote, revise, split, or reject each protocol based on evidence.
