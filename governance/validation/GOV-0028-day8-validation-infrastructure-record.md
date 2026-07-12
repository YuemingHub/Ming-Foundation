---
id: GOV-0028
title: Day 8 Foundation Validation Infrastructure Implementation Record
status: Accepted
version: 1.0.0
layer: Layer 5 — Community & Governance
owner: Ming Foundation Validation
created: 2026-07-12
updated: 2026-07-12
related:
  - GOV-0025
  - GOV-0027
  - GOV-0029
  - GOV-0030
  - GOV-0031
  - ADR-0010
  - REF-0001
depends_on:
  - GOV-0025
  - ADR-0009
---

# GOV-0028 — Day 8 Foundation Validation Infrastructure Implementation Record

## 1. Purpose

Day 8 implements the canonical-repository work that remained after the Day 7 scope correction.

The work is limited to:

```text
YuemingHub/Ming-Foundation
```

No product repository or runtime is modified or required.

## 2. Implemented backlog items

| Day 7 item | Day 8 result |
|---|---|
| D7-FND-005 | Completed — machine-readable RFC requirement registry and conformance model |
| D7-FND-006 | Completed — external evidence intake protocol, schema, template, and example |
| D7-FND-007 | Completed — repository validator now checks IDs, statuses, dependencies, index rows, and local index links |
| D7-FND-008 | Completed — Foundation-only remediation architecture plan |
| D7-FND-010 | Completed — release-stage and version consistency validator |

`D7-FND-009` remains planned because broad formatting changes are intentionally avoided.

## 3. Infrastructure added

### Machine-readable standards layer

- `standards/requirements/RFC_REQUIREMENTS.json`;
- `reference/schemas/rfc-requirement-registry.schema.json`;
- `reference/schemas/conformance-matrix.schema.json`;
- conformance example;
- requirement validator.

### Evidence-intake layer

- `GOV-0030`;
- `GOV-TPL-0004`;
- external-evidence JSON schema;
- safe example record.

### Repository validation layer

- enhanced `scripts/validate_repository.py`;
- `scripts/validate_requirements.py`;
- `scripts/validate_release_state.py`;
- `scripts/validate_all.py`;
- existing `scripts/validate_audit_scope.py`;
- GitHub Actions validation workflow.

## 4. Authority boundary

The machine-readable registry is a derived index.

It:

- supports traceability and automated checking;
- does not promote an RFC;
- does not rewrite normative text;
- does not establish product conformance;
- must be revised when the governing RFC changes.

`ADR-0010` governs this boundary.

## 5. Requirement coverage

The initial registry contains:

```text
5 source RFCs
63 machine-readable requirements
```

Each requirement records:

- source document;
- source section;
- normative level;
- statement;
- verification methods;
- expected evidence types;
- whether external implementation evidence is required.

## 6. Validation commands

```bash
python scripts/validate_repository.py
python scripts/validate_audit_scope.py
python scripts/validate_requirements.py
python scripts/validate_release_state.py
python scripts/validate_all.py
```

The aggregate command must fail if any individual validator fails.

## 7. Status boundary

Day 8 does not change:

```text
MF-0004                 Candidate
PROJECT-MINGOS-0002     Candidate
RFC-0001 — RFC-0005     Proposed
GOV-0015                Proposed
```

Validation infrastructure is not validation completion.

## 8. Day 8 completion rule

Day 8 is complete when:

- registry and schemas validate;
- repository metadata and dependencies validate;
- index links and status rows validate;
- release version and stage are consistent;
- audit-scope regression validation passes;
- CI workflow runs the aggregate validator;
- no external repository is required.
