---
id: GOV-0034
title: RFC Ambiguity and Revision Register
status: Accepted
version: 1.0.1
layer: Layer 5 — Community & Governance
owner: Ming Foundation Standards
created: 2026-07-12
updated: 2026-07-12
related:
  - RFC-0001
  - RFC-0002
  - RFC-0003
  - RFC-0004
  - RFC-0005
  - GOV-0032
  - GOV-0033
  - ADR-0011
depends_on:
  - GOV-0032
---

# GOV-0034 — RFC Ambiguity and Revision Register

## 1. Purpose

This register records questions that remain after the requirement index was confirmed as faithful.

It prevents faithful indexing from being mistaken for complete specification.

## 2. Summary

```text
Open ambiguities: 19
Blocking for Candidate:    15
Candidate clarifications:   4
```

## 3. Severity

### BlockingForCandidate

The RFC should not advance to Candidate until the ambiguity is resolved or an Accepted decision explains why it is safe to proceed.

### CandidateClarification

The issue requires clarification, examples, a profile, or a bounded deferral before wider conformance claims.

### Editorial

Meaning is stable, but wording or structure requires correction.

## 4. Register

| ID | RFC | Issue | Severity | Status |
|---|---|---|---|---|
| AMB-0001 | RFC-0001 | Material assertion threshold | BlockingForCandidate | Open |
| AMB-0002 | RFC-0001 | High-impact use classification | BlockingForCandidate | Open |
| AMB-0003 | RFC-0001 | Age, capacity, and representative authority | BlockingForCandidate | Open |
| AMB-0004 | RFC-0001 | Governed basis for intra-family disclosure | BlockingForCandidate | Open |
| AMB-0005 | RFC-0002 | Processing-basis taxonomy | BlockingForCandidate | Open |
| AMB-0006 | RFC-0002 | Representative authority verification | BlockingForCandidate | Open |
| AMB-0007 | RFC-0002 | Minimum retention profiles | BlockingForCandidate | Open |
| AMB-0008 | RFC-0002 | Governed identity authority | CandidateClarification | Open |
| AMB-0009 | RFC-0003 | High-impact safety action threshold | BlockingForCandidate | Open |
| AMB-0010 | RFC-0003 | Least-intrusive decision standard | CandidateClarification | Open |
| AMB-0011 | RFC-0003 | Service availability and resource freshness | BlockingForCandidate | Open |
| AMB-0012 | RFC-0003 | Independent review trigger | BlockingForCandidate | Open |
| AMB-0013 | RFC-0004 | Reasonable informed person test | BlockingForCandidate | Open |
| AMB-0014 | RFC-0004 | Minimum cohort and rare-pattern thresholds | BlockingForCandidate | Open |
| AMB-0015 | RFC-0004 | Separate approval authority | BlockingForCandidate | Open |
| AMB-0016 | RFC-0004 | Withdrawal after aggregate publication | CandidateClarification | Open |
| AMB-0017 | RFC-0005 | Material public claim threshold | BlockingForCandidate | Open |
| AMB-0018 | RFC-0005 | Bilingual semantic review | CandidateClarification | Open |
| AMB-0019 | RFC-0005 | Release-blocking synchronization failures | BlockingForCandidate | Open |

## 5. Machine-readable authority

The detailed question, affected requirement IDs, and recommended resolution are stored in:

```text
standards/review/RFC_AMBIGUITIES.json
```

The machine register is derived from this governance record and the source RFCs.

## 6. Status effect

All five RFCs remain `Proposed`.

No ambiguity is resolved merely because it has been assigned an ID.

## Day 10 disposition

All 19 ambiguities remain Open and now map to `REV-0001` through `REV-0019` in `RFC_REVISION_PLAN.json`.
