---
id: ADR-0013
title: Adopt R0 Cross-RFC Revision Foundations
status: Accepted
version: 1.0.0
layer: Cross-layer
owner: Ming Foundation Architecture
created: 2026-07-12
updated: 2026-07-12
related:
  - RFC-0001
  - RFC-0002
  - RFC-0003
  - RFC-0004
  - RFC-0005
  - GOV-0034
  - GOV-0042
  - GOV-0044
  - GOV-0048
  - ADR-0012
depends_on:
  - GOV-0036
  - GOV-0042
---

# ADR-0013 — Adopt R0 Cross-RFC Revision Foundations

## Context

Internal Architecture Review Round 1 identified four decisions that cannot be
resolved independently inside one RFC:

- `REV-X001` — shared impact terms;
- `REV-X002` — jurisdiction qualification;
- `REV-X003` — affected-person review gates;
- `REV-X004` — migration and lineage.

## Decision 1 — Shared impact terms

Revised RFCs must define and consistently use:

- **material** — persistent, shared, decision-driving, identity-shaping, or
  difficult-to-reverse information or use;
- **high impact** — capable of causing rights restriction, punitive or
  irreversible consequence, sensitive disclosure, safety or professional
  action, or durable profile effect;
- **irreversible** — not fully correctable through ordinary correction,
  deletion, notice, or rollback;
- **punitive** — imposing disadvantage, exclusion, restriction, sanction, or
  adverse treatment;
- **sensitive use** — involving intimate, child, health, safety, family,
  professional, legal, or similarly consequential information.

Uncertainty defaults to the safer classification until reviewed.

## Decision 2 — Jurisdiction qualification

Ming Foundation standards may define technical governance categories.

They must not present those categories as universal legal conclusions.

An implementation claiming legal or professional validity must identify:

- jurisdiction and operating context;
- qualified reviewer or accountable basis;
- applicable age, consent, safeguarding, rights, retention, and disclosure
  rules;
- conflicts and unknowns;
- review date and owner.

## Decision 3 — Affected-person review gates

Before Candidate status, an RFC that governs personal interpretation, data
rights, safety, case reuse, or public reliance must either:

- complete the applicable affected-person and domain review classes; or
- obtain an Accepted bounded-deferral decision stating scope, reason,
  safeguards, expiry, dissent, and the review that remains mandatory.

Internal review alone cannot satisfy this gate.

## Decision 4 — Migration and lineage

A revised RFC governing personal or evidence records must require:

- original source and status preservation;
- transformation and migration history;
- dependent-record identification;
- correction and supersession propagation;
- rollback or remediation limits;
- review of historical labels and authority;
- non-erasure of necessary audit evidence.

## Scope

R0 is implemented in RFC-0001 through RFC-0003 in Day 11.

Application to RFC-0004 and RFC-0005 remains part of R2.

This ADR guides Proposed drafts and does not itself promote an RFC.
