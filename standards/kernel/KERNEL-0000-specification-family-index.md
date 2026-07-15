---
id: KERNEL-0000
title: MingOS Kernel Specification Family Index and Lifecycle
status: Draft
version: 0.3.0-draft.3
layer: Layer 2 — Standards
owner: Ming Foundation Kernel Architecture
created: 2026-07-15
updated: 2026-07-15
language: en
canonical_language: en
translation_status: original
decision_base_commit: 0397834984b9d9ad0e08a142dce2a98ed5b1a795
related:
  - ADR-0005
  - ADR-0026
  - MOS-0000
  - KERNEL-0001
  - REF-0031
  - REF-0032
  - REF-0033
  - REF-0034
depends_on:
  - ADR-0026
  - MOS-0000
---

# KERNEL-0000 — MingOS Kernel Specification Family Index and Lifecycle

> **Draft family entry point.** ADR-0026 remains Proposed. This document does
> not establish Kernel or product conformance.

## 1. Purpose

Define the Kernel document family, active version set, dependency direction,
source-use rules, lifecycle, compatibility, migration, and derived-index
synchronization.

## 2. Scope and non-goals

This Draft coordinates governed KERNEL documents. It does not define final
objects, state machines, conformance levels, certification, tests, reference
implementation, human-review authorization, CP2/CP3, or a status promotion.

## 3. Definitions

- **Kernel family:** the explicit versioned set of governed KERNEL documents.
- **Source baseline:** exact ID, status, version, path, commit, Blob and locator.
- **Derived index:** machine-readable companion subordinate to Markdown.
- **Reserved ID:** planned identifier with no authority until its document exists.
- **Collection-local source:** source revised in the same commit, still identified
  by ID, version, status and locator.

## 4. Data and process model

```text
Governed source baseline
  ↓ classified source treatment
KERNEL-0000 family/version rules
  ↓
KERNEL-0001 proposed core requirements
  ↓ future
KERNEL-0002 object/data model
  ↓
KERNEL-0003 lifecycle/state machines
  ↓
KERNEL-0004 conformance requirements
  ↓
KERNEL-0005 test specifications and derived indexes
```

```text
family_version: kernel-family/0.2.0-draft.2
ADR-0026: Proposed / 0.2.0
KERNEL-0000: Draft / 0.2.0-draft.2
KERNEL-0001: Draft / 0.2.0-draft.2
KERNEL-0002: Draft / 0.1.0-draft.1
KERNEL-0003: Draft / 0.1.0-draft.1
KERNEL-0004..0005: ReservedNotCreated
claim: NoCurrentKernelConformanceClaim
```

## 5. Normative requirements

A KERNEL requirement MUST identify source ID, status, version, path, baseline
commit, Blob and exact locator. It MUST classify source role, source treatment,
requirement scope, proposed verification methods and expected evidence types.

A lower layer MUST NOT silently redefine a higher source. Draft and Proposed
status MUST remain visible. Machine indexes MUST match requirement identity and
meaning, not counts alone.

## 6. Human agency and ethics

The family MUST preserve person/role separation, affected-person participation,
refusal, correction, appeal, meaningful choice, human accountability, failure,
counterexample, uncertainty and the right not to become a permanent profile.

A schema or state machine MUST NOT silently become a theory of life.

## 7. Privacy and consent

Source baselines and indexes MUST minimize personal information and MUST NOT
contain raw identifiable family, child, clinical, crisis or consultation records.
Purpose, authority, consent, representative scope, access, retention, deletion,
exception and audit remain distinguishable.

## 8. Safety and escalation

Changes affecting risk, emergency action, disclosure, handoff, incident or
appeal require dedicated safety review. Repository validation and synthetic
rehearsal MUST NOT be represented as human-use or product-safety evidence.

## 9. Review and future conformance criteria

Round 07 is review-ready only when all 36 requirements have complete source,
scope, treatment, verification and evidence records; all MOS levels are exact;
all required sections exist; Markdown and JSON are semantically synchronized;
30 ambiguities and 30 vocabulary identities match; and KERNEL-0002..0005 remain
absent.

These are review criteria, not implementation-conformance criteria.

## 10. Non-normative examples

- A Proposed RFC may be referenced without promotion.
- A passing repository test proves structural consistency, not deployed behavior.
- A model provider may change while applicable obligations remain unchanged.

## 11. Limitations and open questions

Partial applicability, cross-language equality, emergency suspension,
compatibility before reference implementation, and treatment of unresolved
Candidate Charter ambiguity remain open.

## 12. Lifecycle, compatibility and migration

Each document follows MOS-0000:
`Idea → Draft → Review → Candidate → Stable → Deprecated → Withdrawn`.

Breaking changes require affected-person impact, migration, coexistence, data
conversion, rollback or suspension, public-claim implications and dissent.
Supersession MUST be explicit and history preserved.

## 13. Version and change history

| Version | Date | Change | Status |
|---|---|---|---|
| 0.1.0-draft.1 | 2026-07-15 | Initial family index | Draft |
| 0.2.0-draft.2 | 2026-07-15 | MOS completeness, exact source baseline and semantic synchronization | Draft |

## 14. Round 08 family update

KERNEL-0002 and KERNEL-0003 are added as Drafts. KERNEL-0004/0005 remain absent. No conformance claim is created.
