---
id: GOV-0027
title: Day 7 Audit Scope Correction Record
status: Accepted
version: 1.0.0
layer: Layer 5 — Community & Governance
owner: Ming Foundation Governance
created: 2026-07-12
updated: 2026-07-12
related:
  - GOV-0001
  - GOV-0020
  - GOV-0021
  - GOV-0022
  - GOV-0023
  - GOV-0024
  - GOV-0025
  - GOV-0026
  - ADR-0008
  - ADR-0009
depends_on:
  - GOV-0020
  - ADR-0008
---

# GOV-0027 — Day 7 Audit Scope Correction Record

## 1. Purpose

This record corrects a scope error introduced during Day 7.

The only canonical repository under development, audit, and governance in this phase is:

```text
https://github.com/YuemingHub/Ming-Foundation
```

The website, Family OS, `Mingos-life`, `mingos.cn`, and `ymai.love` may provide external implementation evidence. They are not canonical repositories and are not prerequisites for accepting a `Ming-Foundation` repository commit.

## 2. Error

Day 7 correctly verified `YuemingHub/Ming-Foundation`, but several records then treated inaccessible website and Family OS implementations as though their availability determined whether the repository audit itself was complete.

That mixed two different activities:

1. canonical repository audit;
2. external implementation-conformance validation.

The first was completed. The second remained bounded.

## 3. Correction

The project now uses the following separation:

### Canonical repository audit

Scope:

- repository architecture;
- document metadata;
- status consistency;
- dependency and authority rules;
- index and changelog integrity;
- governance decisions;
- standards and RFC quality;
- machine-readable backlog integrity.

Authority:

- `YuemingHub/Ming-Foundation`.

Day 7 result:

```text
Completed and accepted
```

### External implementation evidence

Scope may include:

- public website behavior;
- website source;
- Family OS source and tests;
- runtime behavior;
- production or de-identified operational evidence.

Authority:

- evidence only;
- never automatic canonical authority;
- included only through an explicitly scoped review.

Day 7 result:

```text
Bounded and incomplete
```

Its incompleteness does not invalidate or block the canonical repository audit.

## 4. Corrected decision

- Day 7 repository delivery is accepted.
- External implementation access is not a prerequisite for `Ming-Foundation` repository progress.
- `ADR-0008` is superseded by `ADR-0009`.
- Product-specific tasks remain external evidence targets until their implementation repositories are explicitly placed in scope.
- Day 8 must proceed inside `Ming-Foundation` unless the user explicitly selects another repository.

## 5. Historical preservation

The prior error remains visible through Git history and this correction record.

The project does not erase the earlier wording or pretend it was never accepted. It records why it was wrong, which decision replaces it, and how future work must avoid recurrence.

## 6. Regression rule

A future governance document MUST NOT:

- describe access to another repository as a prerequisite for auditing `Ming-Foundation`;
- call an external implementation repository canonical;
- mix repository acceptance with product conformance;
- expand work into another repository without explicit user scope;
- treat unavailable external evidence as a failure of the canonical repository.
