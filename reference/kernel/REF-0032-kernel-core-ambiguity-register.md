---
id: REF-0032
title: Kernel Core Ambiguity Dissent and Open-Question Register
status: Draft
version: 0.2.0-draft.2
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

| ID | Area | Open issue | Risk | Related KCR | Required review classes | Target | Status |
|---|---|---|---|---|---|---|---|
| KCA-001 | Kernel applicability | Does the core govern software only, or also human professional and organizational operations? | `Critical` | KCR-0001, KCR-0007 | Architecture, Implementation | `Round 08–09` | `Open` |
| KCA-002 | Affected person | How far indirect, group, relational, future, or non-user impact extends. | `Critical` | KCR-0002, KCR-0008 | AffectedPerson, Ethics | `Round 08–09` | `Open` |
| KCA-003 | Role multiplicity | When one person may hold several roles without destroying independence. | `High` | KCR-0003, KCR-0009 | Governance, Professional | `Round 08–09` | `Open` |
| KCA-004 | Representative authority | How authority varies by age, capacity, jurisdiction, urgency, and conflict. | `Critical` | KCR-0004, KCR-0010 | Privacy, Jurisdiction | `Round 08–09` | `Open` |
| KCA-005 | Declared purpose | Required granularity and when a changed purpose requires renewed authority. | `High` | KCR-0005, KCR-0011 | Safety, AffectedPerson | `Round 08–09` | `Open` |
| KCA-006 | Consent basis | When consent is inapplicable, invalid, coerced, or insufficient. | `Critical` | KCR-0006, KCR-0012 | Accessibility, AffectedPerson | `Round 08–09` | `Open` |
| KCA-007 | Refusal and safety | When refusal can be overridden for lawful protective action. | `Critical` | KCR-0007, KCR-0013 | Research, Domain | `Round 08–09` | `Open` |
| KCA-008 | Correction propagation | Which derived records and decisions must be updated after correction. | `High` | KCR-0008, KCR-0014 | CommercialConflict, Ethics | `Round 08–09` | `Open` |
| KCA-009 | Third-party rights | How a user can inspect their own record without exposing another person's protected information. | `Critical` | KCR-0009, KCR-0015 | Standards, Translation | `Round 08–09` | `Open` |
| KCA-010 | Knowledge statuses | Boundary among observation, statement, inference, hypothesis, pattern, judgment, and decision. | `High` | KCR-0010, KCR-0016 | Architecture, Implementation | `Round 08–09` | `Open` |
| KCA-011 | Observation before advice | When immediate safe guidance may precede complete observation. | `High` | KCR-0011, KCR-0017 | AffectedPerson, Ethics | `Round 08–09` | `Open` |
| KCA-012 | Confidence | Whether numeric confidence is meaningful across human and AI interpretation. | `High` | KCR-0012, KCR-0018 | Governance, Professional | `Round 08–09` | `Open` |
| KCA-013 | Unknown and dissent | How unknowns and minority views affect operations rather than becoming passive notes. | `High` | KCR-0013, KCR-0019 | Privacy, Jurisdiction | `Round 08–09` | `Open` |
| KCA-014 | Relationship context | How to preserve context without creating intrusive relationship surveillance. | `Critical` | KCR-0014, KCR-0020 | Safety, AffectedPerson | `Round 08–09` | `Open` |
| KCA-015 | Small and reversible | What small, safe, and reversible mean in different domains. | `High` | KCR-0015, KCR-0021 | Accessibility, AffectedPerson | `Round 08–09` | `Open` |
| KCA-016 | Hidden persuasion | Boundary between supportive communication, risk disclosure, recommendation, and manipulation. | `Critical` | KCR-0016, KCR-0022 | Research, Domain | `Round 08–09` | `Open` |
| KCA-017 | High-impact operation | Thresholds for impact, likelihood, reversibility, duration, scale, and vulnerable groups. | `Critical` | KCR-0017, KCR-0023 | CommercialConflict, Ethics | `Round 08–09` | `Open` |
| KCA-018 | Risk threshold | When uncertainty itself requires stopping, escalation, or human review. | `Critical` | KCR-0018, KCR-0024 | Standards, Translation | `Round 08–09` | `Open` |
| KCA-019 | Unavailable handoff | Obligations when qualified human or emergency services are unavailable. | `Critical` | KCR-0019, KCR-0025 | Architecture, Implementation | `Round 08–09` | `Open` |
| KCA-020 | Emergency intervention | Who determines necessity and proportionality, with what evidence and review. | `Critical` | KCR-0020, KCR-0026 | AffectedPerson, Ethics | `Round 08–09` | `Open` |
| KCA-021 | Memory deletion | Conflicts among deletion, backup, audit, safety, legal, and other-person rights. | `Critical` | KCR-0021, KCR-0027 | Governance, Professional | `Round 08–09` | `Open` |
| KCA-022 | Secondary use | Whether and how learning from sensitive interaction can be authorized without exploitation. | `Critical` | KCR-0022, KCR-0028 | Privacy, Jurisdiction | `Round 08–09` | `Open` |
| KCA-023 | AI disclosure | What model and provenance detail is meaningful to an affected person. | `High` | KCR-0023, KCR-0029 | Safety, AffectedPerson | `Round 08–09` | `Open` |
| KCA-024 | Accountable human | Required competence, independence, information, authority, and availability. | `Critical` | KCR-0024, KCR-0030 | Accessibility, AffectedPerson | `Round 08–09` | `Open` |
| KCA-025 | Participation impossible | How to proceed when participation is unsafe, inaccessible, declined, or impossible. | `Critical` | KCR-0025, KCR-0031 | Research, Domain | `Round 08–09` | `Open` |
| KCA-026 | Organization obligations | Which requirements apply directly to organizational policy, sales, staffing, and governance. | `High` | KCR-0026, KCR-0032 | CommercialConflict, Ethics | `Round 08–09` | `Open` |
| KCA-027 | Requirement delegation | How referenced RFC/Profile requirements remain synchronized without copying. | `High` | KCR-0027, KCR-0033 | Standards, Translation | `Round 08–09` | `Open` |
| KCA-028 | Candidate Charter change | How Kernel Drafts respond when a Candidate Charter is revised. | `High` | KCR-0028, KCR-0034 | Architecture, Implementation | `Round 08–09` | `Open` |
| KCA-029 | Cross-language traceability | How English and Chinese sources remain semantically traceable. | `High` | KCR-0029, KCR-0035 | AffectedPerson, Ethics | `Round 08–09` | `Open` |
| KCA-030 | Conformance future | Which Draft requirements eventually become mandatory, conditional, optional, or removed. | `Critical` | KCR-0030, KCR-0036 | Governance, Professional | `Round 08–09` | `Open` |

```text
Open: 30
Resolved: 0
Affected-person/domain/implementation/legal review: not executed
Overall: PreparedNotExecuted
```

Critical or High items require exact evidence, real review classes, minority
views and a governed disposition. Repository validation cannot close them.
