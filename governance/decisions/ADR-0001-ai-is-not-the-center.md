---
id: ADR-0001
title: AI Is Not the Center of Ming Foundation
status: Accepted
version: 1.0.0
layer: Cross-layer
owner: Ming Foundation Architecture
created: 2026-07-12
updated: 2026-07-12
related:
  - MF-0000
  - MF-0003
depends_on: []
---

# ADR-0001 — AI Is Not the Center

## Context

Modern product architecture often places a language model or agent at the center and treats identity, memory, tools, and user interfaces as supporting components.

That structure makes the system dependent on a model vendor and encourages the false assumption that intelligence is equivalent to model output.

Ming Foundation is concerned with life, relationship, context, meaning, memory, reflection, and agency. These remain meaningful even when no generative model is present.

## Decision

AI models are replaceable components inside the Intelligence and Reasoning implementation layer.

The architectural center is the combination of:

- Charter;
- ontology;
- identity and consent;
- observation;
- evidence and confidence;
- revisable memory;
- relationship and event context;
- reflection, choice, action, and feedback;
- audit and governance.

## Consequences

### Positive

- Model providers can change without redefining the system.
- Non-AI and human-supported workflows remain first-class.
- AI output cannot silently become authoritative system truth.
- Standards can be implemented across different technologies.

### Negative

- Initial architecture is more demanding than a chatbot wrapper.
- Data status, consent, audit, and correction must be implemented explicitly.
- Some rapid prototype shortcuts are disallowed.

## Rejected alternative

**AI-agent-first architecture:** rejected because it makes model behavior the implicit ontology and weakens user correction, interoperability, and long-term stability.
