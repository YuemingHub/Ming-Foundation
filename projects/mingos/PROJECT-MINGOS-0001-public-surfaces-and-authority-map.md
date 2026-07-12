---
id: PROJECT-MINGOS-0001
title: MingOS Public Surfaces and Authority Map
status: Accepted
version: 1.0.0-alpha.2
layer: Layer 4 — Projects
owner: MingOS Project
created: 2026-07-12
updated: 2026-07-12
related:
  - PROJECT-MINGOS-0000
  - ADR-0003
  - ADR-0004
  - GOV-0001
  - GOV-0002
  - GOV-0003
depends_on:
  - ADR-0003
  - ADR-0004
---

# PROJECT-MINGOS-0001 — MingOS Public Surfaces and Authority Map

## 1. Purpose

This document distinguishes the public website, canonical repository, discussion spaces, and implementation surfaces of MingOS. It prevents a public interface, conversation, prototype, or product channel from silently becoming the project source of truth.

## 2. Current map

```text
MingOS
├── Official public website
│   └── https://mingos.cn
│
├── Canonical public knowledge repository
│   └── https://github.com/YuemingHub/Ming-Foundation
│
├── Discussion and working sources
│   ├── architecture and product conversations
│   ├── research synthesis sessions
│   ├── Codex and coding-agent sessions
│   └── structured handoff packages
│
└── Implementation surfaces
    └── recorded and governed through project documents and the source registry
```

## 3. Responsibility by surface

### `mingos.cn`

Responsible for:

- public explanation;
- official project identity;
- Charter and architecture presentation;
- public project status;
- contribution and product navigation;
- trust, transparency, and participation information.

It SHOULD NOT independently create normative definitions that conflict with accepted repository records.

### `YuemingHub/Ming-Foundation`

Responsible for:

- accepted project knowledge;
- architecture and governance decisions;
- standards and protocols;
- research synthesis and references;
- project boundaries and roadmaps;
- historical traceability;
- statuses, supersession, and review records.

### Discussion and agent spaces

Responsible for:

- exploration;
- critique;
- drafting;
- alternatives;
- implementation analysis;
- identifying new evidence and constraints.

They are not canonical until processed through repository governance.

### Implementation surfaces

Responsible for:

- proving whether standards and architecture work in real contexts;
- producing runtime evidence, failures, tests, and operational constraints;
- maintaining product-specific code and deployment concerns where appropriate.

Implementation MAY challenge a Draft or reveal a required RFC. It MUST NOT silently redefine accepted foundation concepts.

## 4. Content flow

```text
Discussion / Research / Implementation evidence
  ↓
GOV-0003 review and classification
  ↓
Ming-Foundation repository record
  ↓
Accepted project understanding
  ↓
mingos.cn public representation
```

Feedback may flow in both directions, but authority does not.

## 5. Conflict handling

When surfaces disagree:

- website versus repository: verify the accepted repository record, then correct the stale surface or open a governed change;
- conversation versus repository: treat the conversation as a proposal;
- implementation versus repository: record evidence and open an ADR, RFC, or document revision;
- handoff ZIP versus repository: the merged repository state governs;
- two repository documents: use status, dependencies, version, date, and explicit supersession records.

## 6. Public communication rule

Public statements SHOULD distinguish:

- what exists now;
- what is under development;
- what is experimental;
- what is a long-term direction;
- what has not yet been validated.

A compelling vision must not be presented as completed infrastructure.
