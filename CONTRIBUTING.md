# Contributing to Ming Foundation

Ming Foundation welcomes contributions that improve the standards, models, implementations, and governance of Living Intelligence.

## Before contributing

Read:

1. `foundation/0000-architecture-blueprint.md`
2. `foundation/principles/MF-0003-first-principles.md`
3. `standards/mos/MOS-0000-standard-process.md`
4. `CODE_OF_CONDUCT.md`

## Contribution types

- **Editorial:** clarity, examples, translation, formatting.
- **Research:** evidence review, conceptual comparison, limitations.
- **Standard:** new or changed normative requirements.
- **Architecture:** cross-layer design or system boundaries.
- **Implementation:** code, schema, SDK, tests, reference applications.
- **Casebook:** de-identified cases used to test standards.

## Required workflow

```text
Issue or Discussion
  → RFC for material changes
  → Architecture review
  → Ethics and human-agency review
  → Pull request
  → Validation
  → Decision
```

Small editorial corrections may use a direct pull request.

## Document metadata

Normative documents must start with:

```yaml
---
id:
title:
status:
version:
layer:
owner:
created:
updated:
related:
depends_on:
---
```

## Normative language

The words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** indicate requirement strength.

Chinese equivalents:

- MUST：必须
- MUST NOT：不得
- SHOULD：应当
- SHOULD NOT：不应
- MAY：可以

## Review gates

A proposal cannot enter Candidate status unless reviewers can answer:

- Does it preserve human agency?
- Does it distinguish fact, observation, hypothesis, and judgment?
- Can users inspect, correct, reject, and revoke?
- Does it avoid turning temporary states into permanent labels?
- Is consent explicit and appropriately scoped?
- Can the design be implemented and audited?
- Does it remain useful even if the underlying AI model changes?

## Commit convention

Use Conventional Commits with repository scopes:

```text
feat(charter):
feat(mos):
feat(kernel):
feat(core):
feat(sdk):
feat(project):
docs(reference):
docs(research):
refactor(ontology):
fix(protocol):
chore(repo):
```

## Pull requests

Each pull request should state:

- problem;
- affected layers;
- standards or principles involved;
- alternatives considered;
- migration or compatibility impact;
- safety and ethics impact;
- validation performed.
