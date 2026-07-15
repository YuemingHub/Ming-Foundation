---
id: REF-0032
title: Kernel Core Ambiguity Dissent and Open-Question Register
status: Draft
version: 0.1.0-draft.1
layer: Reference
owner: Ming Foundation Kernel Review
created: 2026-07-15
updated: 2026-07-15
language: en
canonical_language: en
translation_status: original
decision_base_commit: 0397834984b9d9ad0e08a142dce2a98ed5b1a795
related:
  - KERNEL-0000
  - KERNEL-0001
  - REF-0031
  - REF-0033
  - REF-0034
depends_on:
  - KERNEL-0001
---

# REF-0032 — Kernel Core Ambiguity Dissent and Open-Question Register

> Every item remains Open. Recording an ambiguity does not resolve it.

## 1. Risk levels

- `Critical`: may alter rights, safety, authority, participation, data,
  professional, commercial or conformance boundaries.
- `High`: may materially alter scope, interoperability, review or implementation.
- `Medium`: may cause inconsistency or reduced testability.
- `Low`: editorial without material normative change.

## 2. Register

| ID | Area | Open issue | Risk | Status |
|---|---|---|---|---|
| KCA-001 | Kernel applicability | Does the core govern software only, or also human professional and organizational operations? | `Critical` | `Open` |
| KCA-002 | Affected person | How far indirect, group, relational, future, or non-user impact extends. | `Critical` | `Open` |
| KCA-003 | Role multiplicity | When one person may hold several roles without destroying independence. | `High` | `Open` |
| KCA-004 | Representative authority | How authority varies by age, capacity, jurisdiction, urgency, and conflict. | `Critical` | `Open` |
| KCA-005 | Declared purpose | Required granularity and when a changed purpose requires renewed authority. | `High` | `Open` |
| KCA-006 | Consent basis | When consent is inapplicable, invalid, coerced, or insufficient. | `Critical` | `Open` |
| KCA-007 | Refusal and safety | When refusal can be overridden for lawful protective action. | `Critical` | `Open` |
| KCA-008 | Correction propagation | Which derived records and decisions must be updated after correction. | `High` | `Open` |
| KCA-009 | Third-party rights | How a user can inspect their own record without exposing another person's protected information. | `Critical` | `Open` |
| KCA-010 | Knowledge statuses | Boundary among observation, statement, inference, hypothesis, pattern, judgment, and decision. | `High` | `Open` |
| KCA-011 | Observation before advice | When immediate safe guidance may precede complete observation. | `High` | `Open` |
| KCA-012 | Confidence | Whether numeric confidence is meaningful across human and AI interpretation. | `High` | `Open` |
| KCA-013 | Unknown and dissent | How unknowns and minority views affect operations rather than becoming passive notes. | `High` | `Open` |
| KCA-014 | Relationship context | How to preserve context without creating intrusive relationship surveillance. | `Critical` | `Open` |
| KCA-015 | Small and reversible | What small, safe, and reversible mean in different domains. | `High` | `Open` |
| KCA-016 | Hidden persuasion | Boundary between supportive communication, risk disclosure, recommendation, and manipulation. | `Critical` | `Open` |
| KCA-017 | High-impact operation | Thresholds for impact, likelihood, reversibility, duration, scale, and vulnerable groups. | `Critical` | `Open` |
| KCA-018 | Risk threshold | When uncertainty itself requires stopping, escalation, or human review. | `Critical` | `Open` |
| KCA-019 | Unavailable handoff | Obligations when qualified human or emergency services are unavailable. | `Critical` | `Open` |
| KCA-020 | Emergency intervention | Who determines necessity and proportionality, with what evidence and review. | `Critical` | `Open` |
| KCA-021 | Memory deletion | Conflicts among deletion, backup, audit, safety, legal, and other-person rights. | `Critical` | `Open` |
| KCA-022 | Secondary use | Whether and how learning from sensitive interaction can be authorized without exploitation. | `Critical` | `Open` |
| KCA-023 | AI disclosure | What model and provenance detail is meaningful to an affected person. | `High` | `Open` |
| KCA-024 | Accountable human | Required competence, independence, information, authority, and availability. | `Critical` | `Open` |
| KCA-025 | Participation impossible | How to proceed when participation is unsafe, inaccessible, declined, or impossible. | `Critical` | `Open` |
| KCA-026 | Organization obligations | Which requirements apply directly to organizational policy, sales, staffing, and governance. | `High` | `Open` |
| KCA-027 | Requirement delegation | How referenced RFC/Profile requirements remain synchronized without copying. | `High` | `Open` |
| KCA-028 | Candidate Charter change | How Kernel Drafts respond when a Candidate Charter is revised. | `High` | `Open` |
| KCA-029 | Cross-language traceability | How English and Chinese sources remain semantically traceable. | `High` | `Open` |
| KCA-030 | Conformance future | Which Draft requirements eventually become mandatory, conditional, optional, or removed. | `Critical` | `Open` |

## 3. Current result

```text
Open items:                 30
Resolved items:             0
Affected-person review:     not executed
Domain review:              not executed
Implementation review:      not executed
Legal/jurisdiction review:  not executed

Overall:
PreparedNotExecuted
```

## 4. Disposition values

- `SourceRevisionRequired`
- `KernelRevisionRequired`
- `RFCOrProfileRevisionRequired`
- `DomainQualificationRequired`
- `EvidenceRequired`
- `EquivalentWithQualification`
- `BoundedDeferral`
- `UnresolvedDissent`
- `Rejected`
- `Resolved`

No Critical item may be silently closed.
