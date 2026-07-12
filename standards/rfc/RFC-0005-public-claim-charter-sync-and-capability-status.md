---
created: 2026-07-12
depends_on:
- ADR-0003
- ADR-0004
- ADR-0005
id: RFC-0005
layer: Layer 1 — Standards
owner: Ming Foundation Standards
related:
- ADR-0003
- ADR-0004
- MF-0004
- PROJECT-MINGOS-0002
- GOV-0008
- GOV-0012
- GOV-0014
- GOV-0019
- ADR-0007
status: Proposed
title: Public Claim Charter Synchronization and Capability Status
  Protocol
updated: 2026-07-12
version: 0.1.0
---

# RFC-0005 — Public Claim, Charter Synchronization, and Capability Status Protocol

## Status

Proposed minimum protocol for `mingos.cn` and other official public
surfaces.

## 1. Problem

A public website may unintentionally:

- present vision as current capability;
- display a Charter version that no longer matches the repository;
- describe an experimental system as complete;
- collect sensitive information without sufficient notice;
- imply professional, emergency, or outcome guarantees;
- omit limitations because they weaken marketing.

## 2. Core rule

Every material public claim MUST be traceable to a repository source, an
evidence source, or an explicit capability-status label.

Public clarity is part of Charter conformance.

## 3. Capability-status vocabulary

Official public surfaces SHOULD use the following statuses.

### Available

A user can access the stated capability now under defined conditions.

Requirements:

- current route or service;
- owner;
- support boundary;
- known limitations;
- evidence date.

### Pilot

Available to a bounded group with active evaluation.

Requirements:

- eligibility;
- duration or review point;
- known risks;
- feedback route;
- no implication of broad production readiness.

### Experimental

A hypothesis or prototype under test.

Requirements:

- not represented as reliable or generally available;
- no unsupported outcome claim;
- reversible participation;
- explicit data-use notice.

### Planned

Approved direction without a current available implementation.

### Vision

Long-term possibility or design direction.

Vision MUST NOT be worded as a delivered capability.

### Paused or Retired

No longer available or intentionally stopped, with appropriate data and
support information.

## 4. Charter publication

The official website may publish:

1.  the full current repository text;
2.  a translated version that preserves meaning and version;
3.  a non-normative public summary.

A summary MUST state:

- that it is a summary;
- the governing repository document;
- status;
- version;
- last synchronized date;
- link to change history;
- how to report a discrepancy.

The website MUST NOT silently rewrite Candidate or Accepted commitments
for marketing.

## 5. Page metadata

Material architecture, Charter, product, and governance pages SHOULD
display:

- source document ID;
- source version or commit;
- status;
- last reviewed date;
- capability status where relevant;
- owner;
- feedback or correction route.

## 6. Claim review

Claims requiring review include:

- “complete” or “first” category claims;
- outcome or effectiveness claims;
- scientific, psychological, medical, educational, or legal claims;
- safety and professional-support claims;
- privacy and data-control claims;
- AI capability claims;
- child-understanding claims;
- ecosystem, SDK, Kernel, cloud, or certification availability.

A claim record SHOULD preserve:

- exact wording;
- audience;
- supporting source;
- limitations;
- reviewer;
- publication date;
- expiry or re-review date.

## 7. Forms and public collection

Public forms MUST state:

- purpose;
- required and optional fields;
- recipient;
- retention;
- request route;
- whether follow-up is human or automated;
- prohibited sensitive content;
- relevant privacy notice.

A general early-access form SHOULD NOT solicit identifiable child,
crisis, medical, or consultation details.

## 8. Professional and AI disclosure

Official surfaces MUST make visible:

- when AI is involved;
- that AI output can be incomplete or wrong;
- whether a human has reviewed content;
- what professional role, if any, is available;
- what emergency or clinical service is not provided;
- that response availability is not guaranteed unless operationally
  governed.

## 9. Synchronization control

A future implementation SHOULD provide:

- repository-to-site content synchronization;
- a manifest of public normative pages;
- automated checks for document ID, status, and version;
- build failure or release warning on stale Charter content;
- a public discrepancy-report route;
- release notes for material claim changes.

## 10. Acceptance tests

A conforming website must demonstrate:

1.  every Charter page identifies its governing source and status;
2.  every future capability is labeled Planned or Vision;
3.  every Available capability can be reached or its eligibility is
    clear;
4.  early-access forms display purpose and sensitive-data restrictions;
5.  no page claims the Charters are Accepted while they remain
    Candidate;
6.  AI and professional boundaries are visible before sensitive use;
7.  a stale source version triggers a release warning or failure;
8.  a user can report inaccurate or stale public information;
9.  outcome claims have evidence, limitations, and review dates.

## 11. Open questions

- Which pages must fail deployment when synchronization breaks?
- Which public claims require independent rather than internal review?
- How should bilingual translations record semantic review?
- What minimum public transparency is required before wider acquisition?
