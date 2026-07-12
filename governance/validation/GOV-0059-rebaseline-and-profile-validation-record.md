---
id: GOV-0059
title: Requirement Re-baseline and Profile Validation Record
status: Accepted
version: 1.0.0
layer: Layer 5 — Community & Governance
owner: Ming Foundation Validation
created: 2026-07-12
updated: 2026-07-12
related:
  - GOV-0056
  - GOV-0057
  - GOV-0058
  - GOV-0060
  - ADR-0016
depends_on:
  - GOV-0056
  - GOV-0058
---

# GOV-0059 — Requirement Re-baseline and Profile Validation Record

## Validation result

```text
Current requirements:                   115
Current implementation test specs:      115
Legacy requirements archived:            63
Legacy implementation specs archived:    63
Legacy IDs mapped:                        63
New current IDs:                          52
Unmapped or retired legacy IDs:            0
Proposed profiles:                         4
Open profile-related ambiguities:           4
Implementation tests executed:              0
Product conformance results:                0
```

## Validated invariants

- current requirement IDs are unique;
- every current requirement has one current acceptance-test reference;
- every current acceptance test maps to one current requirement;
- every RFC-0001 through RFC-0003 requirement has a current source marker;
- every marker exists in the governed source;
- source blob SHAs match the current RFC files;
- all 63 legacy IDs map to current IDs;
- no implementation result was fabricated;
- all four profiles remain Proposed;
- all nineteen ambiguities remain Open;
- all eight dissent items remain Open.
