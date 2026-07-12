---
id: ADR-0010
title: Machine-Readable Requirements Are Derived Indexes
status: Accepted
version: 1.0.0
layer: Cross-layer
owner: Ming Foundation Architecture
created: 2026-07-12
updated: 2026-07-12
related:
  - MOS-0000
  - GOV-0028
  - GOV-0029
  - GOV-0031
  - REF-0001
depends_on:
  - ADR-0009
  - MOS-0000
---

# ADR-0010 — Machine-Readable Requirements Are Derived Indexes

## Context

Automated validation and conformance work require stable requirement identifiers and structured fields.

A machine-readable registry creates a risk: generated or manually indexed data could appear more authoritative than the RFC text it summarizes.

## Decision

Machine-readable requirement registries are derived indexes.

The governing authority remains the source RFC Markdown document merged into the canonical repository.

A registry:

- must identify its source document and section;
- must preserve normative level;
- must identify the source revision;
- must not strengthen, weaken, or rewrite the source;
- must be corrected when divergence is found;
- may be used for automation, conformance, and impact analysis;
- does not promote RFC status.

## Conflict rule

When registry and RFC differ:

```text
RFC source text wins.
Registry must be corrected.
Conformance decisions based on the incorrect entry must be reviewed.
```

## Consequences

### Positive

- requirements become traceable and testable;
- automation does not replace governance;
- product-neutral standards remain possible;
- registry errors are correctable without silently changing the RFC.

### Negative

- source and registry must be maintained together;
- semantic changes require impact review;
- automation cannot safely infer every requirement without human review.

## Follow-up

1. Maintain `RFC_REQUIREMENTS.json`.
2. Validate every referenced RFC and section.
3. Review registry fidelity before RFC promotion.
4. Preserve requirement-ID history when the schema supports supersession.
