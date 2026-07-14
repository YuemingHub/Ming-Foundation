---
id: REF-0026
title: MingOS Kernel Specification Family and Identifier Allocation Map
status: Draft
version: 0.1.0
layer: Reference
owner: Ming Foundation Architecture
created: 2026-07-14
updated: 2026-07-14
language: en
canonical_language: en
translation_status: original
decision_base_commit: 394f494f00ebfccf38572e3846cf6b6e3f699abf
related:
  - ADR-0005
  - ADR-0026
  - MOS-0000
  - GOV-0082
  - REF-0014
  - REF-0027
  - REF-0028
  - REF-0029
  - REF-0030
depends_on:
  - ADR-0026
---

# REF-0026 — MingOS Kernel Specification Family and Identifier Allocation Map

> This Draft is a non-normative planning and traceability map. Reserved IDs do
> not create specifications or authorize conformance claims.

## 1. Family layout

```text
standards/kernel/
├── KERNEL-0000-specification-family-index.md
├── KERNEL-0001-core-operational-contract.md
├── KERNEL-0002-canonical-object-data-model.md
├── KERNEL-0003-lifecycle-state-machines.md
├── KERNEL-0004-conformance-requirements-evidence.md
└── KERNEL-0005-test-specifications-derived-indexes.md
```

No listed KERNEL document exists in Round 06.

## 2. Allocation table

| ID | Purpose | Earliest round | Planned source status | Must not contain |
|---|---|---:|---|---|
| KERNEL-0000 | family index, version set, dependencies, lifecycle and migration map | 07 | Draft | substantive requirements copied without source links |
| KERNEL-0001 | common operational contract and shared semantics | 07 | Draft | complete object schemas, all state machines, product code |
| KERNEL-0002 | canonical object model, identity, provenance and relationships | 08 | Draft | product database schema as universal ontology |
| KERNEL-0003 | consent, memory, safety, appeal, remediation and revision state machines | 08 | Draft | implementation-specific workflow states without abstraction |
| KERNEL-0004 | conformance claim unit, mandatory requirements, evidence and exceptions | 09 | Draft | claims that repository validation proves product conformance |
| KERNEL-0005 | test specifications, reference cases and derived indexes | 09 | Draft | strengthening or weakening source requirements |

## 3. Required dependency direction

```text
Candidate Charters and accepted architecture boundaries
  ↓ constrain
Kernel family version set
  ↓ integrates and references
RFCs and Profiles
  ↓ verified through
Conformance requirements, tests and evidence
  ↓ implemented by
Products, agents, services, workflows and organizations
```

A lower layer may provide evidence that a higher source requires revision, but
it cannot silently change the source.

## 4. Planned responsibility by document

### KERNEL-0000

- family entry point;
- active version set;
- document and requirement dependencies;
- change, deprecation and migration map;
- known incompatibilities and unresolved conflicts.

### KERNEL-0001

- common roles and accountability;
- minimum rights and operational obligations;
- shared knowledge and evidence semantics;
- common observation-before-advice rule;
- cross-domain safety, correction and audit boundaries;
- requirements delegated to RFCs and Profiles.

### KERNEL-0002

- identifiers and role assignments;
- subject, speaker and representative links;
- event, timeline, relationship and context;
- observation, hypothesis, pattern, judgment and decision provenance;
- consent, purpose, memory, evidence and audit objects.

### KERNEL-0003

- consent lifecycle;
- memory correction, revocation, retention and deletion lifecycle;
- risk, handoff, appeal and incident lifecycle;
- action, feedback and state-revision lifecycle;
- remediation, suspension and reinstatement lifecycle.

### KERNEL-0004

- conformance declaration tuple;
- mandatory/optional/conditional requirement classes;
- applicable RFC and Profile resolution;
- evidence classes and freshness;
- exception, partial evidence and non-conformance handling;
- claim expiry, suspension and withdrawal.

### KERNEL-0005

- source-linked test cases;
- positive, negative and counterexample tests;
- reference traces;
- machine-readable derived indexes;
- test execution result format;
- explicit separation of test specification from product evidence.

## 5. Identifier governance

- No implementation may use a reserved KERNEL ID as proof of conformance.
- Renaming a historical component to `Kernel` does not make it a KERNEL
  specification.
- Each future document must follow `MOS-0000`.
- Machine indexes must follow `ADR-0010`.
- Breaking changes require compatibility, migration and rollback analysis.
- New family documents require an explicit allocation decision rather than
  informal numbering.
