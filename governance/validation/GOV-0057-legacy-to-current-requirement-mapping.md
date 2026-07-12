---
id: GOV-0057
title: Legacy to Current Requirement Identity Mapping
status: Accepted
version: 1.0.0
layer: Layer 5 — Community & Governance
owner: Ming Foundation Validation
created: 2026-07-12
updated: 2026-07-12
related:
  - GOV-0032
  - GOV-0056
  - GOV-0059
  - ADR-0010
  - ADR-0016
depends_on:
  - GOV-0056
---

# GOV-0057 — Legacy to Current Requirement Identity Mapping

## Mapping result

```text
Legacy requirement IDs:     63
Current requirement IDs:   115
Retained legacy IDs:        63
New current IDs:            52
Retired legacy IDs:          0
Unmapped legacy IDs:         0
```

## Identity rules

- A legacy ID is preserved only when its underlying obligation still exists.
- Refinement of wording does not create a new ID when the governed obligation
  remains substantially continuous.
- A genuinely new normative obligation receives the next available ID in its
  RFC namespace.
- A legacy ID MUST NOT be reassigned to an unrelated obligation.
- Future split, merge, replacement, or retirement must remain explicit.

Machine-readable mapping:

```text
standards/requirements/RFC_REQUIREMENT_ID_MAP.json
```

## Evidence boundary

Identity continuity does not imply that an implementation previously tested
against the old wording automatically conforms to the current requirement.
