---
id: ADR-0005
title: Separate the Charter of Life, MingOS Charter, and MingOS Kernel
status: Accepted
version: 1.0.0
layer: Cross-layer
owner: Ming Foundation Architecture
created: 2026-07-12
updated: 2026-07-12
related:
  - MF-0000
  - MF-0004
  - PROJECT-MINGOS-0000
  - PROJECT-MINGOS-0002
  - GOV-0004
  - GOV-0005
depends_on:
  - MF-0000
---

# ADR-0005 — Separate the Charter of Life, MingOS Charter, and MingOS Kernel

## Context

Historical MingOS discussions used “Life Charter,” “MingOS Charter,” “Constitution of Life,” “Kernel,” “Soul Layer,” and “immutable core” in overlapping ways.

The overlap preserved important ideas but created architectural ambiguity:

- higher-order ethical claims were mixed with MingOS-specific promises;
- project commitments were mixed with runtime protocols;
- website language could appear more authoritative than repository records;
- a prompt or implementation artifact could be mistaken for the Charter;
- changing a technical mechanism could appear to change the root commitments.

Day 4 reviewed the proposed separation against the current architecture, governance, Charter drafts, implementation needs, and authority model.

## Decision

Ming Foundation maintains three distinct root layers.

### 1. The Charter of Life

Scope:

- candidate higher-order ethical commitments concerning how life should be treated;
- broader than MingOS;
- not owned by a product or organization;
- intentionally humble about scientific and universal claims.

Primary question:

> How should any organization, technology, or profession treat life?

Repository artifact:

- `MF-0004 — The Charter of Life`

### 2. MingOS Charter

Scope:

- MingOS-specific organizational and product self-restraints;
- commitments concerning data, AI, business, professional roles, children, safety, governance, correction, and enforcement;
- conformance expectations for using the MingOS name.

Primary question:

> How does MingOS commit to practice the Charter of Life?

Repository artifact:

- `PROJECT-MINGOS-0002 — MingOS Charter`

### 3. MingOS Kernel

Scope:

- operational protocols, data models, state transitions, safety gates, tests, review loops, runtime behavior, incident handling, and implementation conformance;
- replaceable mechanisms governed by both Charters;
- subject to validation by real use, failure, counterexample, and evidence.

Primary question:

> How must MingOS systems, agents, professionals, products, and organizations work in practice?

Future repository artifacts:

- infrastructure, standards, RFCs, schemas, and implementation records;
- not completed by Day 4.

## Dependency direction

```text
The Charter of Life
  ↓ constrains
MingOS Charter
  ↓ constrains
MingOS Kernel
  ↓ constrains
Products, agents, services, content, sales, research, and operations
```

A lower layer may reveal that a higher layer requires revision, but it may not silently redefine it.

## Authority and status

Acceptance of this ADR accepts the separation of the three layers.

It does not automatically accept every article in either Charter.

At Day 4:

- `MF-0004` is `Candidate`;
- `PROJECT-MINGOS-0002` is `Candidate`;
- complete Kernel conformance standards remain future work.

## Change thresholds

### The Charter of Life

Changes require:

- explicit proposal;
- ethical and philosophical review;
- evidence and limitations;
- affected-person participation;
- compatibility analysis;
- documented reasons for revision.

### MingOS Charter

Changes require:

- project governance review;
- commercial-conflict review;
- privacy, child-rights, safety, and human-agency review;
- public changelog and supersession record.

### MingOS Kernel

Changes require:

- RFC or standard process appropriate to the affected layer;
- implementation evidence;
- tests and failure analysis;
- compatibility and migration planning;
- confirmation that the change remains within both Charters.

## Consequences

### Positive

- ethical commitments remain distinguishable from brand promises and technical mechanisms;
- website content can map to the correct source;
- technical evolution does not silently rewrite the Charter;
- Charter violations become easier to identify;
- implementation evidence can challenge a Candidate without becoming automatic doctrine.

### Negative

- the project must maintain traceability across three layers;
- some historical files and website language require reclassification;
- duplicate principles must be removed or linked rather than copied indefinitely;
- conformance and exception handling require additional governance work.

## Alternatives considered

### One combined Charter and Kernel document

Rejected because it mixes durable commitments with replaceable implementation.

### MingOS Charter as the higher-order Charter

Rejected because MingOS should not claim ownership over the ethical treatment of life.

### Kernel or system prompt as the highest authority

Rejected because implementation artifacts are model-, product-, and context-dependent.

### Website Charter as the canonical source

Rejected because `mingos.cn` is the official public representation, while repository records govern normative content.

## Follow-up

1. Execute the validation plan in `GOV-0006`.
2. Audit `mingos.cn` for mixed Charter terminology.
3. Inventory existing Family OS and Kernel artifacts as implementation evidence.
4. Keep both Charters at `Candidate` until review evidence supports acceptance.
5. Define canonical Kernel conformance only after the relevant Charter commitments are sufficiently validated.
