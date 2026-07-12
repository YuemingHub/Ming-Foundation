---
id: GOV-0030
title: External Implementation Evidence Intake Protocol
status: Accepted
version: 1.0.0
layer: Layer 5 — Community & Governance
owner: Ming Foundation Validation
created: 2026-07-12
updated: 2026-07-12
related:
  - GOV-0002
  - GOV-0018
  - GOV-0021
  - GOV-0027
  - GOV-0028
  - GOV-0029
  - GOV-TPL-0004
  - ADR-0009
depends_on:
  - GOV-0018
  - ADR-0009
---

# GOV-0030 — External Implementation Evidence Intake Protocol

## 1. Purpose

This protocol defines how evidence from a website, application, service, private repository, runtime, or operational process may enter Ming Foundation governance.

It does not authorize access to another system.

## 2. Entry gate

External evidence may be collected only when:

1. the user or authorized governance process explicitly identifies the target;
2. scope and intended use are stated;
3. access is authorized;
4. personal, restricted, and security-sensitive data boundaries are defined;
5. revision and method can be recorded.

## 3. Required record

Use `GOV-TPL-0004` or a conforming JSON record.

The record must state:

- scope authorization;
- target and revision;
- method;
- evidence authority;
- limitations;
- classification;
- reviewer;
- related requirements;
- findings;
- disposition;
- that the evidence is non-blocking for canonical repository governance.

## 4. Authority

External evidence may:

- support or challenge a standard;
- establish bounded implementation-conformance findings;
- reveal a need to revise the repository;
- support a Charter validation stream.

External evidence may not:

- become canonical merely because it is current;
- silently change an RFC;
- require work in another repository without explicit scope;
- expose restricted data in the public repository;
- block unrelated repository governance.

## 5. Evidence levels

### Direct external evidence

Current source, tests, page, runtime, or operational record directly reviewed at a named revision.

### Documentary external evidence

A dated code wiki, report, screenshot, export, or structured summary that was not independently reproduced.

### Restricted external evidence

Evidence reviewed under `GOV-0018` that cannot be published in raw form.

## 6. Disposition

Allowed dispositions:

- Accepted as evidence;
- Accepted with limitations;
- Rejected;
- Further verification required.

Acceptance as evidence is not acceptance of a Charter, RFC, product, or organization.
