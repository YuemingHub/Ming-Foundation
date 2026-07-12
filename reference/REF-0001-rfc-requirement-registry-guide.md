---
id: REF-0001
title: RFC Requirement Registry Guide
status: Accepted
version: 1.0.0
layer: Layer 3 — Reference
owner: Ming Foundation Standards and Validation
created: 2026-07-12
updated: 2026-07-12
related:
  - MOS-0000
  - GOV-0029
  - ADR-0010
depends_on:
  - GOV-0029
  - ADR-0010
---

# REF-0001 — RFC Requirement Registry Guide

## Purpose

This guide explains how to use the machine-readable RFC requirement registry.

## Files

- `standards/requirements/RFC_REQUIREMENTS.json`;
- `reference/schemas/rfc-requirement-registry.schema.json`;
- `reference/schemas/conformance-matrix.schema.json`;
- `reference/examples/conformance-matrix.example.json`;
- `scripts/validate_requirements.py`.

## Authority

The registry is not the normative source.

Always read the governing RFC before interpreting or implementing a requirement.

## Workflow

```text
Select RFC requirement
  ↓
Read source RFC section
  ↓
Identify target and revision
  ↓
Select verification method
  ↓
Collect bounded evidence
  ↓
Assign conformance state
  ↓
Record limitations and next action
```

## Conformance state

- Implemented;
- Partial;
- Absent;
- Conflicting;
- Unverifiable;
- NotApplicable with reason.

## External targets

Use `GOV-TPL-0004` before collecting evidence from another repository or system.

Explicit user scope remains mandatory.
