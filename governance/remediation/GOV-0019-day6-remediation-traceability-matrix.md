---
created: 2026-07-12
depends_on:
- GOV-0007
- GOV-0014
id: GOV-0019
layer: Layer 5 — Community & Governance
owner: Ming Foundation Architecture
related:
- GOV-0007
- GOV-0010
- GOV-0011
- GOV-0012
- GOV-0014
- GOV-0015
- GOV-0016
- GOV-0017
- GOV-0018
- RFC-0001
- RFC-0002
- RFC-0003
- RFC-0004
- RFC-0005
- ADR-0007
status: Accepted
title: Day 6 Remediation Traceability Matrix
updated: 2026-07-12
version: 1.0.0-alpha.7
---

# GOV-0019 — Day 6 Remediation Traceability Matrix

## 1. Purpose

This matrix prevents Day 5 gaps from being lost inside broad
architecture work.

A gap is not closed by writing a protocol. Closure requires
implementation and evidence.

## 2. Matrix

| Gap                                         | Governing artifact    | Required implementation evidence                                             | Required review                         | Closure state at Day 6 |
|---------------------------------------------|-----------------------|------------------------------------------------------------------------------|-----------------------------------------|------------------------|
| Parent report becomes child identity        | RFC-0001              | Source-qualified assertion model, contestation route, expiry, decision trace | Affected person, child rights, product  | Design proposed        |
| Missing child/third-party correction        | RFC-0001              | Age-aware participation and independent dispute review                       | Child rights, safeguarding, privacy     | Design proposed        |
| Fragmented consent across channels          | RFC-0002              | Purpose registry, permission/basis records, revocation propagation           | Privacy, legal, implementation          | Design proposed        |
| Incomplete access/export/deletion/appeal    | RFC-0002              | User workflow, derived-store handling, restricted exceptions, appeal         | Privacy, legal, affected person         | Design proposed        |
| Safety flag without accountable handoff     | RFC-0003              | Responsible role, acknowledgment, failed-handoff state, response evidence    | Safety, professional, operations        | Design proposed        |
| Incorrect safety classification             | RFC-0003              | Appeal, false-positive/negative review, downstream correction                | Safety, affected person                 | Design proposed        |
| Case reuse without clear basis              | RFC-0004              | Evidence zones, purpose, access, export approval, withdrawal handling        | Privacy, research ethics                | Design proposed        |
| Cross-family re-identification              | RFC-0004              | Rarity review, minimum cohort, output suppression, restricted drill-down     | Privacy, security, affected person      | Design proposed        |
| Website presents vision as current          | RFC-0005              | Capability labels, claim records, release checks                             | Public communication, commercial ethics | Design proposed        |
| Website Charter drift                       | RFC-0005              | Source ID/version/status, sync manifest, stale-content failure               | Governance, website engineering         | Design proposed        |
| Sensitive data in public forms              | RFC-0002 and RFC-0005 | Minimized form, notice, content prohibition, secure intake separation        | Privacy, website, security              | Design proposed        |
| Charter violation lacks remedy              | GOV-0015              | Reporting route, independent owner, containment, appeal, remediation         | Governance, affected person, legal      | Procedure proposed     |
| Friendly expert endorsement replaces review | GOV-0016              | Conflict disclosure, conditional conclusions, preserved dissent              | Independent reviewers                   | Protocol accepted      |
| Affected-person review becomes testimonial  | GOV-0017              | Non-leading interview, voluntary consent, disagreement preservation          | Research ethics, affected person        | Instrument accepted    |
| Raw review evidence enters public repo      | GOV-0018              | Restricted storage, access logs, public summaries, retention                 | Privacy, security                       | Protocol accepted      |
| Founder or partner conflict                 | GOV-0015 and GOV-0016 | Independent owner, suspension authority, public rationale                    | Governance independence                 | Design proposed        |

## 3. Requirement states for Day 7

Day 7 should use:

- `Implemented`;
- `Partial`;
- `Absent`;
- `Conflicting`;
- `Unverifiable`;
- `Not applicable with reason`.

No requirement may be marked implemented based only on a document or
module name.

## 4. Evidence standard

Implementation evidence should include, as applicable:

- current code path;
- schema or migration;
- user interface;
- access rule;
- test;
- production configuration;
- operational owner;
- sample de-identified audit record;
- failure and counterexample result;
- current revision or deployment.

## 5. Closure rule

A P0 gap closes only when:

1.  its governing protocol is sufficiently reviewed;
2.  implementation exists;
3.  acceptance tests pass;
4.  affected-person or independent review is complete where required;
5.  material objections are resolved or explicitly accepted;
6.  evidence is recorded without exposing restricted material.
## 6. Day 7 evidence state

| Gap group | Day 7 evidence state | Backlog authority |
|---|---|---|
| Subject, speaker, and contestability | Partial; complete assertion and subject-facing workflow not evidenced | `GOV-0023`, `GOV-0025` |
| Consent and data-rights lifecycle | Partial; complete purpose, permission, export, deletion propagation, retention, and appeal absent | `GOV-0023`, `GOV-0025` |
| Safety accountability | Detection and escalation foundations exist; handoff, appeal, and incident lifecycle partial | `GOV-0023`, `GOV-0025` |
| Case and cross-family evidence | Active implementation areas exist; privacy and reuse controls incomplete | `GOV-0023`, `GOV-0025` |
| Public claim and Charter synchronization | Current source and live audit unavailable; snapshot indicates material gaps | `GOV-0022`, `GOV-0025` |
| Charter violation enforcement | Operational process mostly absent | `GOV-0023`, `GOV-0025` |

No gap is closed by Day 7.
