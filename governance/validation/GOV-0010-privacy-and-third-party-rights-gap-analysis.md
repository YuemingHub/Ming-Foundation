---
id: GOV-0010
title: Privacy and Third-Party Rights Gap Analysis
status: Accepted
version: 1.0.0-alpha.5
layer: Layer 5 — Community & Governance
owner: Ming Foundation Governance
created: 2026-07-12
updated: 2026-07-12
related:
  - MF-0004
  - PROJECT-MINGOS-0002
  - GOV-0006
  - GOV-0007
  - GOV-0008
  - GOV-0009
  - GOV-0013
depends_on:
  - GOV-0006
  - GOV-0009
---

# GOV-0010 — Privacy and Third-Party Rights Gap Analysis

## 1. Purpose

This analysis identifies privacy and rights gaps revealed when the Candidate Charters are compared with current public and implementation evidence.

It is not legal advice and does not replace jurisdiction-specific review.

## 2. Core principle

A person operating the interface cannot automatically grant MingOS unlimited authority over another person.

Parent consent may be necessary for some processing involving a child. It is not equivalent to:

- ownership of the child’s identity or narrative;
- authorization for unlimited collection;
- permission for permanent profiling;
- permission for unrestricted staff or research access;
- permission for model training;
- removal of correction, deletion, participation, or contestability rights.

## 3. Priority gaps

### P0 — Child and third-party contestability

No complete mechanism is evidenced for a child or other described family member to:

- know what has been recorded;
- distinguish parent report from confirmed fact;
- contest or contextualize an interpretation;
- restrict reuse;
- request correction or deletion;
- participate according to age, capacity, safety, and context.

Required direction:

- preserve source and speaker;
- never promote one person’s account into another person’s confirmed identity;
- support age-appropriate participation;
- document when direct participation is unavailable or unsafe;
- provide independent review for high-impact disputes.

### P0 — Purpose, consent, and scope

No complete cross-channel consent model is evidenced.

Required direction:

- purpose-specific consent;
- separate consent where sensitivity or use requires it;
- consent version and timestamp;
- subject and data scope;
- recipient and access scope;
- retention period;
- revocation and consequence;
- emergency/legal exception;
- audit history.

### P0 — Retention, deletion, export, and appeal

Partial delete routes and correction stores exist, but a complete data-rights lifecycle is not evidenced.

Required direction:

- user-accessible data inventory;
- correction and interpretation history;
- export;
- deletion and archive;
- restricted retention exceptions;
- human review;
- response deadlines;
- appeal;
- evidence of completion.

### P0 — Case and cross-family analysis

Case records, summaries, and cross-family analysis can create re-identification and secondary-use risk.

Required direction:

- strict purpose limitation;
- de-identification standard;
- minimum cohort and rarity review;
- restricted access;
- no raw case publication;
- no model-training reuse without separate governance;
- provenance and withdrawal handling;
- output review for sensitive or unique patterns.

### P1 — Profile semantics

`family_profiles` and stage models require a governed assertion model.

Every meaningful profile item SHOULD include:

- subject;
- source speaker;
- knowledge status;
- evidence reference;
- confidence;
- uncertainty;
- time and valid period;
- confirmation status;
- counterevidence;
- revision history;
- visibility;
- permitted purpose;
- expiry or review date.

### P1 — Role and minimum-access model

Admin isolation is a strong security boundary, but role-specific access is not fully evidenced.

Required direction:

- parent, professional, operations, safety, research, and system roles;
- minimum necessary data;
- case-specific authorization;
- access expiry;
- purpose-based views;
- conflict-of-interest controls;
- immutable access logs;
- break-glass review.

### P1 — Storage and backups

File and SQLite persistence require explicit protection.

Required direction:

- encryption at rest where appropriate;
- backup encryption and access;
- key separation;
- secure deletion;
- production/test separation;
- restricted case storage;
- retention schedule;
- incident recovery without silent over-retention.

### P1 — Public collection

Early-access and contact forms require clear public notice.

The form SHOULD avoid collecting identifiable family or child case details unless a separately governed intake process exists.

## 4. Prohibited shortcuts

MingOS MUST NOT:

- call parent-authored data “the child’s profile” without source qualification;
- train or evaluate models on private cases merely because the cases exist;
- expose family cases to contributors through the public repository;
- make deletion impossible by scattering data across channels;
- retain “unknown future value” as a purpose;
- treat de-identification as removing names only;
- use research access as a broader version of professional access;
- hide a safety exception inside general consent.

## 5. Validation recommendation

V3 remains:

```text
Privacy and data governance: Partial
```

The Candidate Charters should remain Candidate until the P0 gaps have accepted designs and implementation evidence.
