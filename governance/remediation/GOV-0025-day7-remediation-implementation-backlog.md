---
id: GOV-0025
title: Day 7 Canonical Repository Remediation Backlog and External Evidence Targets
status: Accepted
version: 1.0.2
layer: Layer 5 — Community & Governance
owner: Ming Foundation Architecture
created: 2026-07-12
updated: 2026-07-12
related:
  - GOV-0019
  - GOV-0020
  - GOV-0021
  - GOV-0022
  - GOV-0023
  - GOV-0024
  - GOV-0026
  - GOV-0027
  - ADR-0009
depends_on:
  - GOV-0020
  - GOV-0027
  - ADR-0009
---

# GOV-0025 — Day 7 Canonical Repository Remediation Backlog and External Evidence Targets

## 1. Purpose

This backlog separates work performed in the canonical repository from optional external implementation-evidence work.

Canonical repository:

```text
YuemingHub/Ming-Foundation
```

Product repositories and live services are not automatically in scope.

## 2. Canonical repository backlog

| ID | Priority | Owner role | Task | Status | Acceptance criteria |
|---|---|---|---|---|---|
| D7-FND-001 | P0 | Governance | Record the Day 7 audit-scope correction | Completed by correction package | `GOV-0027` is Accepted |
| D7-FND-002 | P0 | Architecture | Supersede ADR-0008 with a correct scope decision | Completed by correction package | `ADR-0008` is Superseded and `ADR-0009` is Accepted |
| D7-FND-003 | P0 | Governance | Separate canonical audit from external evidence in Day 7 records | Completed by correction package | GOV-0020 through GOV-0026 use the corrected authority model |
| D7-FND-004 | P0 | Validation Engineering | Add automated scope-regression validation | Completed by correction package | `scripts/validate_audit_scope.py` passes |
| D7-FND-005 | P1 | Standards Engineering | Add machine-readable RFC requirement and conformance-matrix schema | Completed by Day 8 | Requirements can be traced without assuming a product repository |
| D7-FND-006 | P1 | Governance Engineering | Add an external evidence intake template | Completed by Day 8 | External evidence records revision, method, authority, limitation, and explicit scope |
| D7-FND-007 | P1 | Repository Engineering | Validate index links, duplicate IDs, statuses, and dependency references | Planned | Repository validation reports broken references and invalid dependencies |
| D7-FND-008 | P1 | Architecture Board | Produce a Foundation-only Day 8 implementation plan | Completed by Day 8 | Plan modifies only `Ming-Foundation` unless the user explicitly expands scope |
| D7-FND-009 | P2 | Documentation | Normalize Markdown code-fence and index formatting without broad reflow | Planned | No semantic changes and `git diff --check` passes |
| D7-FND-010 | P2 | Release Governance | Validate changelog version progression and canonical-stage consistency | Planned | README, GOV-0001, index, and changelog report one version and stage |

## 3. External implementation evidence targets

The earlier Day 7 task IDs concerning website, Family OS, runtime, product data, product safety, cases, commercial behavior, or professional workspaces are retained as possible evidence targets.

They are now classified as:

```text
scope: external_implementation
non_blocking_for_canonical_repository: true
```

They are not tasks to be executed in `Ming-Foundation` unless they produce standards, templates, evidence records, or an explicitly scoped integration artifact.

The machine-readable backlog preserves the earlier targets under `external_implementation_evidence_targets`.

## 4. Scope rule

A task may move from external evidence into active implementation work only when:

1. the user explicitly identifies the target repository or system;
2. the repository is accessible;
3. the intended change is stated;
4. authority and data boundaries are known;
5. the change does not silently alter canonical standards.

## 5. Corrected implementation order

```text
Wave C0 — Scope correction
D7-FND-001 to D7-FND-004

Wave C1 — Foundation validation infrastructure
D7-FND-005 to D7-FND-007

Wave C2 — Foundation Day 8 architecture
D7-FND-008

Wave C3 — Repository quality and release discipline
D7-FND-009, D7-FND-010
```

External implementation evidence is scheduled separately and never blocks these waves.

## 6. Completion rule

A canonical backlog item is complete only when:

- the change exists in `Ming-Foundation`;
- repository validation passes;
- authority and status are accurate;
- no other repository was modified without explicit user scope;
- evidence and limitations are preserved.
## 7. Day 8 disposition

Day 8 completes D7-FND-005, D7-FND-006, D7-FND-007, D7-FND-008, and D7-FND-010.

D7-FND-009 remains planned. Formatting normalization must be narrow and must not create broad non-functional diffs.
