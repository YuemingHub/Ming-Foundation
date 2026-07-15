---
id: KERNEL-0000
title: MingOS Kernel Specification Family Index and Lifecycle
status: Draft
version: 0.1.0-draft.1
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
  - REF-0026
  - REF-0027
  - REF-0028
  - REF-0029
  - REF-0030
  - REF-0031
  - REF-0032
  - REF-0033
  - REF-0034
depends_on:
  - ADR-0026
  - MOS-0000
---

# KERNEL-0000 — MingOS Kernel Specification Family Index and Lifecycle

> **Draft family entry point.**
>
> This document does not establish Kernel conformance. `ADR-0026` remains
> Proposed. All KERNEL documents created in Round 07 remain Draft.

## 1. Purpose

This document defines the versioned document family, dependency direction,
lifecycle, compatibility, migration, source synchronization, and current active
set of the MingOS Kernel specifications.

It does not define final objects, state machines, conformance semantics, tests,
or a reference implementation.

## 2. Current family result

```text
Family decision:                 ADR-0026 / Proposed
KERNEL-0000:                     Draft / 0.1.0-draft.1
KERNEL-0001:                     Draft / 0.1.0-draft.1
KERNEL-0002:                     ReservedNotCreated
KERNEL-0003:                     ReservedNotCreated
KERNEL-0004:                     ReservedNotCreated
KERNEL-0005:                     ReservedNotCreated
Current implementation claims:   0

Overall:
NoCurrentKernelConformanceClaim
```

## 3. Family documents

| ID | Role | Current status | Authority in Round 07 |
|---|---|---|---|
| KERNEL-0000 | family index, lifecycle, active version set and migration | Draft | non-final family coordination |
| KERNEL-0001 | core operational contract | Draft | proposed requirements for review |
| KERNEL-0002 | canonical object and data model | Not created | none |
| KERNEL-0003 | lifecycle and state machines | Not created | none |
| KERNEL-0004 | conformance requirements and evidence classes | Not created | none |
| KERNEL-0005 | test specifications and derived indexes | Not created | none |

A reserved ID is not a source document.

## 4. Active version-set declaration

The Round 07 active Draft set is:

```text
kernel_family_set: kernel-family/0.1.0-draft.1
decision:
  ADR-0026: Proposed / 0.2.0
documents:
  KERNEL-0000: Draft / 0.1.0-draft.1
  KERNEL-0001: Draft / 0.1.0-draft.1
not_created:
  KERNEL-0002
  KERNEL-0003
  KERNEL-0004
  KERNEL-0005
claim:
  NoCurrentKernelConformanceClaim
```

This set can support review and later drafting. It cannot support a product,
organization, model, prompt, workflow, professional, or service conformance
claim.

## 5. Dependency direction

```text
Charter of Life Candidate
  ↓ current ethical design and review constraint
MingOS Charter Candidate
  ↓ current project design and review constraint
Accepted architecture boundaries + Proposed ADR-0026
  ↓ structure and provisional family decision
KERNEL family
  ↓ integrates and references
RFCs and Profiles
  ↓ implemented and evidenced by
Products, agents, services, workflows, professionals and organizations
```

Candidate and Proposed status MUST remain visible. A lower layer MUST NOT
silently redefine a higher source.

## 6. Source-use rules

A KERNEL document MUST:

1. identify source document, version, status and section;
2. distinguish copied normative text from summarized or newly integrated text;
3. preserve RFC/Profile ownership of detailed delegated requirements;
4. record conflicts, gaps and unresolved ambiguity;
5. preserve cross-language source traceability where relevant;
6. treat machine-readable indexes as derived artifacts;
7. avoid making implementation evidence normative because it already exists.

## 7. Lifecycle

Each KERNEL document follows `MOS-0000` independently:

```text
Draft → Review → Candidate → Stable → Deprecated → Withdrawn
```

Family members MAY advance at different times. A family-level release MUST
identify the status and version of every included document.

No family member may become Stable without:

- applicable architecture, ethics, agency, privacy, consent, safety,
  affected-person, domain and implementation review;
- conformance or review criteria appropriate to its scope;
- known failure modes and limitations;
- compatibility and migration analysis;
- no unresolved higher-source conflict;
- evidence required by `MOS-0000`.

## 8. Change classes

### Editorial

No normative meaning, object identity, lifecycle, authority, evidence or
compatibility change.

### Compatible

Adds or clarifies a requirement while preserving valid prior behavior and
claim interpretation.

### Breaking

Changes a mandatory obligation, role, object meaning, state transition,
delegated source, claim unit, evidence class, exception, or protected right.

A breaking change MUST identify:

- affected documents and implementations;
- migration path;
- coexistence period;
- data conversion implications;
- rollback or suspension behavior;
- public-claim impact;
- affected-person impact.

## 9. Conflict and supersession

A conflict record MUST identify exact sources, versions, sections, affected
people, interim behavior, responsible decision route, migration consequences and
unresolved dissent.

A newer file, more technical source, deployed implementation, or passing test
does not automatically prevail.

Supersession MUST be explicit. Historical requirements remain traceable.

## 10. Machine-readable synchronization

`reference/kernel/mingos-kernel-core-requirements.json` is a derived index.

It MUST:

- preserve source IDs, versions and statuses;
- match the KCR requirement IDs in KERNEL-0001;
- preserve normative level;
- identify delegated documents and unresolved gaps;
- state that Markdown source text remains authoritative;
- fail repository validation when counts or identities diverge.

## 11. Round 07 non-goals

Round 07 does not:

- create KERNEL-0002 through KERNEL-0005;
- establish final object fields or state machines;
- establish active conformance states or certification;
- claim any implementation conforms;
- promote ADR-0026, either Charter, an RFC, a Profile, MOS-0000, or a KERNEL
  document;
- activate human review or CP2/CP3;
- change the Day 17 stage or repository version.

## 12. Open questions

1. Whether KERNEL-0000 eventually becomes Candidate before KERNEL-0001.
2. How family releases identify partial applicability.
3. How jurisdictional Profiles modify a version set.
4. How cross-language normative equality is governed.
5. How emergency suspension affects a family release.
6. Which compatibility guarantees are required before a reference
   implementation exists.
