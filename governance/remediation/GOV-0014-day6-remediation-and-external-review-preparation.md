---
created: 2026-07-12
depends_on:
- GOV-0007
- GOV-0013
- ADR-0006
id: GOV-0014
layer: Layer 5 — Community & Governance
owner: Ming Foundation Governance
related:
- GOV-0006
- GOV-0007
- GOV-0010
- GOV-0011
- GOV-0012
- GOV-0013
- GOV-0015
- GOV-0016
- GOV-0017
- GOV-0018
- GOV-0019
- ADR-0007
- RFC-0001
- RFC-0002
- RFC-0003
- RFC-0004
- RFC-0005
status: Accepted
title: Day 6 Validation Remediation and External Review Preparation
  Record
updated: 2026-07-12
version: 1.0.0-alpha.6
---

# GOV-0014 — Day 6 Validation Remediation and External Review Preparation Record

## 1. Purpose

Day 6 converts the material gaps found in Day 5 into reviewable minimum
contracts, external-review procedures, evidence-handling rules, and
reusable review instruments.

Day 6 is not a second audit. It is the transition from:

``` text
We know the gaps
```

to:

``` text
We know what must be designed, implemented, reviewed, and evidenced to close them
```

## 2. Decisions

Day 6 decides:

1.  five minimum remediation protocols are required before either
    Charter may become `Accepted`;
2.  those protocols begin as `Proposed`, not as implemented standards;
3.  affected-person and external review must use structured instruments
    rather than informal approval;
4.  raw identifiable review evidence must not enter the public
    repository;
5.  Charter-violation handling must be independently reviewable,
    including when the subject is a founder, reviewer, professional, or
    commercial partner;
6.  both Charters remain `Candidate`;
7.  Day 7 must perform direct audit and implementation planning against
    these protocols.

## 3. Minimum remediation protocols

| Protocol   | Gap addressed                                                                                 | Day 6 status |
|------------|-----------------------------------------------------------------------------------------------|--------------|
| `RFC-0001` | A person being defined by another person’s account; missing contestability                    | Proposed     |
| `RFC-0002` | Incomplete consent, retention, deletion, export, and appeal lifecycle                         | Proposed     |
| `RFC-0003` | Safety escalation without complete ownership, handoff, appeal, and incident accountability    | Proposed     |
| `RFC-0004` | Case and cross-family analysis privacy, reuse, and re-identification risk                     | Proposed     |
| `RFC-0005` | Website Charter drift, unclear current/future capability status, and public-data transparency | Proposed     |

## 4. Governance and review instruments

| Artifact       | Function                                                                        | Status   |
|----------------|---------------------------------------------------------------------------------|----------|
| `GOV-0015`     | Charter-violation reporting, containment, remediation, appeal, and traceability | Proposed |
| `GOV-0016`     | Independent external-review protocol                                            | Accepted |
| `GOV-0017`     | Affected-person review instrument                                               | Accepted |
| `GOV-0018`     | Restricted validation-evidence handling protocol                                | Accepted |
| `GOV-0019`     | Remediation traceability matrix                                                 | Accepted |
| `GOV-TPL-0001` | External reviewer response form                                                 | Accepted |
| `GOV-TPL-0002` | Affected-person interview record                                                | Accepted |
| `GOV-TPL-0003` | Validation finding record                                                       | Accepted |

## 5. Remediation principles

Every remediation design must preserve:

- the difference between source, observation, interpretation, decision,
  and action;
- the affected person’s voice and right to contest where possible;
- minimum necessary collection and access;
- explicit purpose and time boundaries;
- safety without unlimited authority;
- evidence, uncertainty, counterexample, and appeal;
- technical and organizational responsibility;
- public claims that distinguish current capability from future
  direction;
- the rule that documentation is not implementation evidence.

## 6. What Day 6 does not claim

Day 6 does not claim that:

- children or third parties can already inspect and contest all records;
- a complete consent and data-rights system is deployed;
- current escalation workflows satisfy `RFC-0003`;
- current cases or cross-family analysis satisfy `RFC-0004`;
- the live website satisfies `RFC-0005`;
- an independent review board already exists;
- any external, legal, clinical, privacy, or child-rights review has
  been completed;
- the Candidate Charters are ready to become Accepted.

## 7. Day 6 exit criteria

Day 6 is complete when:

- each Day 5 P0 gap maps to a proposed protocol or governance process;
- external and affected-person review can be conducted with reusable
  instruments;
- restricted evidence has a handling rule;
- Charter-violation reporting has a reviewable proposed process;
- repository entry points and traceability are updated;
- both Charters remain Candidate;
- the package passes repository-overlay validation.

## 8. Day 7 entry gate

Day 7 should begin only after Day 6 is merged.

Recommended Day 7 scope:

> **Direct Audit and Remediation Implementation Backlog**

Day 7 should:

1.  obtain current website and implementation revisions;
2.  map existing code and public pages to every MUST-level requirement
    in RFC-0001 through RFC-0005;
3.  mark each requirement as implemented, partial, absent, conflicting,
    or unverifiable;
4.  produce implementation tasks with owners, evidence, acceptance
    criteria, and migration risk;
5.  identify which Proposed RFCs are ready for Candidate or Accepted
    review;
6.  avoid broad Kernel expansion unrelated to the P0 gaps.
