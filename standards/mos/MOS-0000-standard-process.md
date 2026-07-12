---
id: MOS-0000
title: Ming Open Standards Process
status: Draft
version: 1.0.0-alpha.9
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
## 14. Review-class completion

A review record MUST identify its class and limitations. Review classes include internal architecture, agency and ethics, privacy and consent, safety, affected-person or domain, legal or jurisdiction, and implementation conformance.

Completing one class MUST NOT be described as completing all review. Promotion proposals MUST identify completed, incomplete, and deferred classes. Minority views MUST remain traceable.
## 15. Draft source implementation and ambiguity state

A planned revision may be marked `ImplementedPendingReview` when:

- source text has been changed;
- derived registries and tests are synchronized;
- repository validation passes;
- the ambiguity remains Open;
- the next review round is explicitly required.

`ImplementedPendingReview` MUST NOT be represented as:

- resolved;
- reviewed;
- conforming;
- Candidate;
- Stable.

A cross-RFC item may be `PartiallyImplemented` when it has been applied to
only part of its declared source scope.
## 16. Internal acceptance and current fidelity

A source answer may be `AcceptedForInternalArchitecture` when internal review
finds the normative structure coherent and testable.

That state MUST NOT:

- close an ambiguity whose required external review is incomplete;
- imply legal or jurisdiction validity;
- imply affected-person acceptance;
- imply implementation conformance;
- promote an RFC.

When source revision materially expands normative clauses, a previously
confirmed machine requirement index MUST be marked historical or pending
re-baselining until it is re-derived from the current source.
## 17. Requirement identity and re-baselining

A current derived requirement baseline MUST:

- identify the exact source version and blob;
- enumerate every indexed normative obligation;
- preserve stable IDs where obligation identity continues;
- create new IDs for new obligations;
- never reassign a legacy ID to unrelated meaning;
- publish a legacy-to-current mapping;
- preserve prior registries as archives;
- maintain one-to-one requirement-to-test traceability;
- distinguish test specification from test execution.

A profile in `DesignedPendingReview` state MUST remain Proposed and MUST NOT
close an ambiguity until the required review classes complete.

## 18. Profile document namespace

Governed residual and reference profile documents use the `PROF-*` ID
namespace.

A `PROF-*` document:

- is a governed standards-layer document;
- must carry ordinary metadata, status, version, owner, and dependency fields;
- remains Proposed until reviewed through the applicable MOS process;
- must not use machine-only ambiguity IDs as frontmatter document references;
- may reference ambiguity IDs inside its governed body and machine registry.
## 19. Profile review

A `PROF-*` document MUST complete a Profile review before promotion.

The review MUST address:

- scope and definitions;
- agency and non-coercion;
- proportionality and minimization;
- privacy and data rights;
- safety and safeguarding;
- accessibility and development;
- operational evidence;
- jurisdiction and limitations.

Internal review completion MUST NOT replace affected-person, domain,
jurisdiction, or implementation review.

## 20. Affected-person review states

Affected-person and domain review states include:

```text
NotPrepared
PreparedNotExecuted
InExecution
EvidenceCollected
Synthesized
Complete
StoppedForSafeguarding
```

`PreparedNotExecuted` means instruments and safeguards exist, but no
participant recruitment, session, result, or approval may be claimed.

## 21. Review evidence protection

Affected-person review MUST:

- be voluntary and non-coercive;
- use appropriate consent and assent;
- support skip, stop, withdrawal, and deletion;
- collect minimum necessary evidence;
- prohibit general collection of identifiable sensitive cases;
- preserve minority views and counterexamples;
- avoid model training or personalization from review evidence;
- use independent facilitation where conflicts or vulnerable participants
  require it.

## 22. Canonical text integrity

Governed UTF-8 text identity MUST use canonical LF newline semantics.

Validators MUST NOT report equivalent LF and CRLF working-tree text as
different governed content.
## 23. Profile source revision completion

A Profile revision item may be `Complete` only when:

- the current Profile source implements the planned change;
- the previous source is preserved or traceable;
- a source marker and source-test result exist;
- current source identity is recorded;
- internal re-review accepts the source change;
- unresolved affected-person, domain, jurisdiction, and implementation
  boundaries remain visible.

## 24. Review-readiness gates

Review readiness MUST separate at least:

```text
ContentReady
OperationallyReadyToSchedule
RecruitmentAuthorized
SessionsAuthorized
EvidenceCollected
ReviewComplete
```

A later state MUST NOT be inferred from an earlier state.

## 25. Operational activation

Affected-person review MUST NOT be scheduled until:

- named accountable people accept required roles;
- role conflicts and qualifications are checked;
- consent, assent, safeguarding, accessibility, recruitment, compensation,
  evidence, deletion, and jurisdiction protocols are approved;
- restricted evidence infrastructure is provisioned and tested;
- a separate activation decision authorizes scheduling.

Role names, templates, plans, and schemas are not operational controls by
themselves.
