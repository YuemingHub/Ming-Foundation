---
id: ADR-0005
title: Separate the Charter of Life, MingOS Charter, and MingOS Kernel
status: Proposed
version: 1.0.0-alpha.3
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
depends_on:
  - MF-0000
---

# ADR-0005 — Separate the Charter of Life, MingOS Charter, and MingOS Kernel

## Context

Historical MingOS discussions used “Life Charter,” “MingOS Charter,” “Constitution of Life,” “Kernel,” “Soul Layer,” and “immutable core” in overlapping ways.

The overlap preserved important ideas but created architectural ambiguity:

- universal ethical claims were mixed with MingOS-specific promises;
- project commitments were mixed with runtime protocols;
- website language could appear more authoritative than repository records;
- a prompt or implementation artifact could be mistaken for the Charter;
- changing a technical mechanism could appear to change the root commitments.

Day 3 requires a stable boundary before the Charter can be reviewed or implemented.

## Proposed decision

Ming Foundation should maintain three distinct root texts.

### 1. The Charter of Life

Scope:

- higher ethical commitments concerning how life should be treated;
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
- commitments concerning data, AI, business, professional roles, children, safety, governance, and correction;
- conformance expectations for using the MingOS name.

Primary question:

> How does MingOS commit to practice the Charter of Life?

Repository artifact:

- `PROJECT-MINGOS-0002 — MingOS Charter`

### 3. MingOS Kernel

Scope:

- operational protocols, data models, state transitions, safety gates, tests, review loops, runtime behavior, and implementation conformance;
- replaceable mechanisms governed by the Charters;
- subject to validation by real use, failure, counterexample, and evidence.

Primary question:

> How must MingOS systems, agents, professionals, products, and organizations work in practice?

Future repository artifacts:

- infrastructure, standards, RFCs, schemas, and implementation records;
- not completed by this Day 3 package.

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

## Change thresholds

### The Charter of Life

Changes should require:

- explicit public proposal;
- ethical and philosophical review;
- evidence and limitations;
- affected-person participation;
- compatibility analysis;
- documented reasons for revision.

### MingOS Charter

Changes should require:

- project governance review;
- commercial-conflict review;
- privacy, child-rights, safety, and human-agency review;
- public changelog and supersession record.

### MingOS Kernel

Changes should require:

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
- implementation evidence can challenge a Draft without becoming automatic doctrine.

### Negative

- the project must maintain traceability across three layers;
- some historical files and website language will require reclassification;
- duplicate principles must be removed or linked rather than copied indefinitely;
- the distinction may initially feel more complex than one unified manifesto.

## Alternatives considered

### One combined Charter and Kernel document

Rejected because it mixes durable commitments with replaceable implementation.

### MingOS Charter as the universal Charter

Rejected because MingOS should not claim ownership over the ethical treatment of life.

### Kernel or system prompt as the highest authority

Rejected because implementation artifacts are model-, product-, and context-dependent.

### Website Charter as the canonical source

Rejected because `mingos.cn` is the official public representation, while accepted repository records govern normative content.

## Follow-up

1. Review `MF-0004` and `PROJECT-MINGOS-0002`.
2. Audit `mingos.cn` for mixed Charter terminology after the Drafts are accepted.
3. Inventory existing Family OS and Kernel artifacts as implementation evidence, not automatic canonical standards.
4. Define a future Kernel conformance map only after the Charter boundary is accepted.
5. Change this ADR from `Proposed` to `Accepted`, revise it, or reject it with reasons after review.
