---
id: GOV-0029
title: RFC Requirement Registry and Conformance Infrastructure
status: Accepted
version: 1.0.1
layer: Layer 5 — Community & Governance
owner: Ming Foundation Standards and Validation
created: 2026-07-12
updated: 2026-07-12
related:
  - MOS-0000
  - RFC-0001
  - RFC-0002
  - RFC-0003
  - RFC-0004
  - RFC-0005
  - GOV-0028
  - GOV-0031
  - ADR-0010
  - REF-0001
depends_on:
  - ADR-0010
  - MOS-0000
---

# GOV-0029 — RFC Requirement Registry and Conformance Infrastructure

## 1. Purpose

This infrastructure makes RFC requirements traceable and testable without tying the standards to a particular product repository.

## 2. Source of truth

The source RFC Markdown document remains authoritative.

The registry is a derived index used for:

- requirement identification;
- conformance matrices;
- test planning;
- evidence intake;
- impact analysis;
- promotion review.

Where registry and RFC differ, the RFC governs and the registry must be corrected.

## 3. Requirement identifier

Format:

```text
RFC-0001-R001
```

An identifier remains stable while the underlying requirement remains materially the same.

A material semantic change should:

- create a new requirement ID;
- mark the old requirement as superseded in a future registry model;
- preserve migration and compatibility notes.

## 4. Required fields

Every registered requirement contains:

- `requirement_id`;
- `source_document`;
- `source_section`;
- `kind`;
- `normative_level`;
- `statement`;
- `implementation_neutral`;
- `external_evidence_required`;
- `verification_methods`;
- `evidence_types`.

## 5. Conformance states

A conformance matrix uses:

- `Implemented`;
- `Partial`;
- `Absent`;
- `Conflicting`;
- `Unverifiable`;
- `NotApplicable`.

`NotApplicable` requires a reason.

No state may be assigned from a module name or document title alone.

## 6. Evidence rule

A conformance result must identify:

- target;
- revision;
- method;
- reviewer;
- limitations;
- requirement;
- state;
- evidence references;
- finding.

External evidence remains non-canonical and non-blocking for repository governance unless an Accepted decision explicitly creates a gate.

## 7. Promotion rule

A Proposed RFC does not advance because its requirements were indexed.

Promotion still requires the review process in `MOS-0000`, evidence appropriate to the requested status, and a dedicated decision.
## 8. Day 9 extension

The infrastructure now includes:

- source blob SHAs;
- requirement-level fidelity review;
- one acceptance-test specification per registered requirement;
- open ambiguity references;
- RFC review checklists;
- a non-implementation baseline.

The new fields increase traceability. They do not change the authority boundary defined by `ADR-0010`.
