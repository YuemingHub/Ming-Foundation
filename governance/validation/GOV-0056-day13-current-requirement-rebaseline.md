---
id: GOV-0056
title: Day 13 Current Requirement Re-baseline
status: Accepted
version: 1.0.0
layer: Layer 5 — Community & Governance
owner: Ming Foundation Standards and Validation
created: 2026-07-12
updated: 2026-07-12
related:
  - RFC-0001
  - RFC-0002
  - RFC-0003
  - RFC-0004
  - RFC-0005
  - GOV-0049
  - GOV-0055
  - GOV-0057
  - GOV-0059
  - ADR-0016
depends_on:
  - GOV-0049
  - GOV-0055
---

# GOV-0056 — Day 13 Current Requirement Re-baseline

## Scope

```text
Canonical source commit: bb8ca9ca06b56d65d68e91c46301638f393978eb

RFC-0001  0.2.0-draft.1
RFC-0002  0.2.0-draft.1
RFC-0003  0.2.0-draft.1
RFC-0004  0.1.0
RFC-0005  0.1.0
```

## Result

| RFC | Previous requirements | Current requirements | New |
|---|---:|---:|---:|
| RFC-0001 | 13 | 29 | 16 |
| RFC-0002 | 16 | 34 | 18 |
| RFC-0003 | 10 | 28 | 18 |
| RFC-0004 | 13 | 13 | 0 |
| RFC-0005 | 11 | 11 | 0 |
| **Total** | **63** | **115** | **52** |

## Method

For RFC-0001 through RFC-0003, the re-baseline:

1. reviewed every normative section in `0.2.0-draft.1`;
2. preserved the existing requirement IDs where the obligation remained;
3. added IDs only for newly introduced or previously unindexed obligations;
4. recorded a source marker for each current requirement;
5. linked every requirement to one current implementation test specification;
6. linked relevant profile and ambiguity dependencies;
7. preserved source blob SHA and review lineage.

RFC-0004 and RFC-0005 retain their existing confirmed requirement sets.

## Authority boundary

The RFC Markdown source remains normative.

`RFC_REQUIREMENTS.json` is a derived current index and cannot override source
text.

## Historical preservation

The Day 12 registries are archived at:

```text
standards/requirements/archive/RFC_REQUIREMENTS_DAY12_LEGACY.json
standards/requirements/archive/RFC_ACCEPTANCE_TESTS_DAY12_LEGACY.json
```

No legacy requirement ID was retired or silently reassigned.
