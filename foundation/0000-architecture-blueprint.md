---
id: MF-0000
title: Ming Foundation Architecture Blueprint
status: Draft
version: 1.0.0-alpha.1
layer: Cross-layer
owner: Ming Foundation Architecture
created: 2026-07-12
updated: 2026-07-12
related:
  - MF-0001
  - MF-0002
  - MF-0003
  - MOS-0000
depends_on: []
---

# Ming Foundation Architecture Blueprint

## 1. Purpose

This blueprint defines the durable structure of Ming Foundation. It prevents the repository from becoming a collection of unrelated ideas, documents, products, and AI features.

The foundation exists to organize **how life may be observed, understood, remembered, reflected upon, and supported** without turning life into an object of control.

## 2. Foundational question

> How can technology help life understand itself while preserving human agency, openness, dignity, context, and the right to change?

Ming Foundation does not claim to possess a complete theory of life. It establishes a disciplined method for building systems that remain humble, revisable, evidence-aware, and accountable.

## 3. Scope

Ming Foundation covers:

- philosophical and ethical commitments;
- life ontology and domain language;
- standards for observation, memory, reasoning, reflection, choice, action, and learning;
- infrastructure and reusable core services;
- reference architectures and applications;
- governance, review, audit, and ecosystem participation.

It does not define a medical diagnosis system, an authority over life choices, or a universal optimization target.

## 4. Architectural layers

### Layer 0 — Charter

Defines why the system exists and what it must never violate.

Canonical concerns:

- mission;
- dignity;
- human agency;
- non-coercion;
- boundaries;
- rights;
- responsibility.

### Layer 1 — Philosophy and Science

Defines the conceptual and research foundations used to reason about life.

Canonical concerns:

- systems thinking;
- development;
- relationship;
- context;
- uncertainty;
- meaning;
- evidence.

Research informs standards but does not automatically become a standard.

### Layer 2 — Standards

Defines stable, implementation-independent normative requirements.

Canonical artifacts:

- MOS standards;
- protocols;
- schemas;
- compatibility rules;
- conformance criteria.

### Layer 3 — Infrastructure

Implements reusable capabilities governed by standards.

Canonical components:

- Kernel;
- Identity;
- Consent;
- Observation;
- Memory;
- Relationship Graph;
- Life Event Timeline;
- State;
- Reasoning;
- Reflection;
- Action and Feedback;
- Audit.

### Layer 4 — Projects

Applies the foundation to real contexts.

Initial projects:

- MingOS;
- Ming Family;
- enterprise WeChat + H5 MVP;
- Ming Education;
- future incubated applications.

Projects may extend the foundation but must not silently redefine it.

### Layer 5 — Community and Governance

Controls how standards evolve, how disagreements are resolved, and how affected people participate.

## 5. Dependency direction

Dependencies flow downward:

```text
Charter
  ↓
Ontology and Standards
  ↓
Kernel and Core
  ↓
SDK and Protocols
  ↓
Applications
```

The following are architectural violations:

- a project invents a conflicting definition of Person, Relationship, Memory, or State without an RFC;
- a user-facing feature bypasses consent, audit, or correction;
- an AI response writes unverified hypotheses into confirmed facts;
- a product metric overrides Charter-level commitments;
- a channel such as enterprise WeChat becomes a separate source of truth.

## 6. Stable core and replaceable components

### Stable

- Charter principles;
- canonical ontology;
- evidence and confidence model;
- revision and correction rights;
- consent and audit rules;
- observation-memory-reflection-action lifecycle.

### Replaceable

- language models;
- vector databases;
- UI frameworks;
- deployment platforms;
- prompt formats;
- notification channels;
- individual application interfaces.

A design that couples the stable core to a specific model vendor is non-conforming.

## 7. Canonical life loop

```text
Expression or Event
  ↓
Observation
  ↓
Contextual Understanding
  ↓
User Confirmation or Correction
  ↓
Reflection
  ↓
Choice
  ↓
Small Action
  ↓
Feedback
  ↓
Memory and State Revision
```

This loop is not a forced workflow. A person may pause, reject, revise, or leave at any point.

## 8. Knowledge status model

Every meaningful assertion must carry a knowledge status.

- **Fact:** explicitly provided or verifiably established.
- **Observation:** a bounded description derived from evidence.
- **Hypothesis:** a possible interpretation requiring confirmation.
- **Pattern:** a repeated relationship supported by multiple observations.
- **Judgment:** a value-laden conclusion; generally avoided or clearly attributed.
- **Decision:** a choice made by a person or authorized actor.

Systems MUST NOT silently promote a hypothesis into a fact.

## 9. Evidence and confidence

Normative records should support:

- evidence references;
- source and time;
- confidence;
- author or producing process;
- user confirmation status;
- revision history;
- expiration or review date where appropriate.

Confidence is not truth. High confidence does not remove the person’s right to disagree.

## 10. Identity and channels

Enterprise WeChat, H5, Web, mobile, and future interfaces are channels. They MUST resolve to a shared identity, consent, relationship, event, memory, and audit foundation.

No channel may maintain a hidden, incompatible life profile.

## 11. Human and AI roles

AI is an implementation component, not the center of the architecture.

AI MAY:

- summarize;
- identify possible patterns;
- propose questions;
- surface uncertainty;
- generate options;
- assist reflection.

AI MUST NOT:

- claim final authority over a person’s meaning, identity, or life decision;
- hide whether a statement is inferred;
- exploit vulnerability to increase dependency;
- present itself as a human professional;
- overwrite user-confirmed information without traceability.

## 12. Reference implementation direction

The first reference implementation should validate one complete loop in a real, bounded context:

> Parent reports a parent-child conflict through enterprise WeChat → the system creates a life event → proposes a revisable observation → the parent confirms or corrects it in H5 → chooses a small action → receives a follow-up → feedback updates memory and state → a weekly reflection becomes available.

This reference path tests the foundation without reducing Ming Foundation to family education.

## 13. Governance

Material changes require:

1. an RFC;
2. affected-layer analysis;
3. architecture review;
4. ethics and human-agency review;
5. implementation evidence;
6. compatibility analysis;
7. documented decision.

## 14. Success criteria

Ming Foundation succeeds when systems built upon it help people:

- feel more accurately understood;
- better distinguish events, emotions, needs, relationships, and patterns;
- correct the system without friction;
- make their own informed choices;
- strengthen relationships and capabilities;
- reduce unhealthy dependency on the system over time.

Usage volume alone is not a success criterion.
