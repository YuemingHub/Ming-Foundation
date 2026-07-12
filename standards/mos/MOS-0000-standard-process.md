---
id: MOS-0000
title: Ming Open Standards Process
status: Draft
version: 1.0.0-alpha.3
layer: Layer 2 — Standards
owner: Ming Foundation Standards
created: 2026-07-12
updated: 2026-07-12
related:
  - MF-0000
  - MF-0003
  - GOV-0029
  - ADR-0010
  - ADR-0011
  - GOV-0033
  - GOV-0034
  - REF-0001
depends_on:
  - MF-0001
  - MF-0002
  - MF-0003
---

# MOS-0000 — Ming Open Standards Process

## 1. Purpose

This document defines how Ming Open Standards are proposed, reviewed, tested, accepted, revised, deprecated, and withdrawn.

## 2. Standard classes

- **Core Standard:** ontology, identity, consent, evidence, memory, observation, and other cross-project requirements.
- **Protocol Standard:** interoperable flows and message contracts.
- **Data Standard:** schemas, identifiers, status models, and validation.
- **Application Profile:** constrained use of standards in a domain.
- **Governance Standard:** review, audit, safety, participation, and decision rules.

## 3. Status lifecycle

```text
Idea
  → Draft
  → Review
  → Candidate
  → Stable
  → Deprecated
  → Withdrawn
```

### Idea

A problem statement without a complete proposal.

### Draft

A documented proposal open to structural change.

### Review

A draft with explicit requests for architecture, ethics, domain, and implementation feedback.

### Candidate

A proposal considered coherent enough for reference implementation and compatibility testing.

### Stable

A standard with implementation evidence, governance approval, conformance criteria, and documented limitations.

### Deprecated

A standard retained for compatibility but not recommended for new systems.

### Withdrawn

A standard judged unsafe, invalid, obsolete, or fundamentally incompatible with the Foundation.

## 4. Required sections

Every MOS document MUST include:

1. purpose;
2. scope and non-goals;
3. definitions;
4. normative requirements;
5. data or process model;
6. human-agency and ethics considerations;
7. privacy and consent considerations;
8. safety and escalation considerations;
9. conformance criteria;
10. examples;
11. limitations and open questions;
12. version and change history.

## 5. Normative language

The terms MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are normative.

## 6. Review requirements

A Core Standard MUST receive:

- architecture review;
- ethics and human-agency review;
- privacy and consent review;
- implementation review;
- affected-user or domain-practitioner review where applicable.

## 7. Evidence requirements

A claim about human behavior, development, mental health, education, or relationships MUST identify its evidence basis and limitations. Citation does not automatically make a claim normative.

## 8. User correction requirement

Any standard that creates, transforms, or uses personal interpretation MUST define how the person can:

- inspect it;
- distinguish fact from inference;
- correct it;
- reject it;
- add context;
- revoke permission where possible;
- view significant downstream effects.

## 9. Compatibility

Breaking changes require:

- a migration path;
- versioning impact;
- affected projects;
- data conversion or coexistence strategy;
- rollback considerations.

## 10. Stable status gate

A standard cannot become Stable until:

- at least one reference implementation exists;
- conformance tests or review criteria exist;
- known failure modes are documented;
- real-world cases have tested correction and consent;
- architecture and ethics reviews are recorded;
- no unresolved Charter conflict remains.

## 11. Emergency suspension

A standard or implementation may be suspended when credible evidence indicates serious harm, hidden coercion, unsafe handling of sensitive data, or systematic violation of human agency.

Suspension must be documented and reviewed; urgency does not justify secrecy beyond what is necessary to protect affected people.
## 12. Machine-readable requirement indexes

A Draft, Review, Candidate, or Stable RFC MAY have a machine-readable requirement index.

The index MUST:

- identify the source RFC and section;
- preserve the normative level;
- identify the source repository revision;
- remain implementation-neutral;
- identify verification methods and evidence types;
- state that source RFC text remains authoritative.

The index MUST NOT:

- promote an RFC;
- strengthen or weaken the source requirement;
- replace architecture, ethics, privacy, safety, or affected-person review;
- treat a product module name as conformance evidence.

See `ADR-0010` and `GOV-0029`.
## 13. Review readiness and promotion

A review checklist in `Prepared` state means that review can begin.

It does not mean:

- a qualified review was completed;
- objections were resolved;
- implementation evidence exists;
- an RFC should advance.

Status promotion requires a dedicated proposal and decision.

Open `BlockingForCandidate` ambiguities MUST be resolved, or an Accepted decision MUST document why a bounded deferral is safe.
