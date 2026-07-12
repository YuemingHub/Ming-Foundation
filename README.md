# Ming Foundation

> Building the standards, infrastructure, and ecosystem for Living Intelligence.  
> 构建生命智能的标准、基础设施与生态。

Ming Foundation is an open standards initiative dedicated to one question:

> **How can technology help life understand itself without replacing, controlling, or reducing life?**  
> **技术如何帮助生命理解自己，而不是替代、控制或简化生命？**

## Current status

This repository is at **Foundation 1.0 / Day 1**. It establishes the repository architecture, governance rules, document standards, first principles, and initial architecture decisions.

**Important:** “Ming Foundation” is currently the name of an open standards initiative and repository. It does not by itself claim to be a legally registered foundation.

## Mission

Build the foundational standards and infrastructure for Living Intelligence so that people, families, communities, and future applications can continuously understand life, relationships, context, change, and growth while preserving human agency.

## The core distinction

Ming Foundation is not primarily building:

- another AI chatbot;
- a system that scores, predicts, or controls people;
- a replacement for human relationships or professional care;
- a single family-education product.

It is building a durable foundation for:

- **Life Ontology** — a shared language for life, relationship, event, state, need, meaning, memory, and growth;
- **Life Protocols** — how observation, understanding, reflection, choice, action, and learning should flow;
- **Life Memory** — long-term, revisable, evidence-aware memory beyond conversation history;
- **Living Infrastructure** — reusable core capabilities for applications such as MingOS, Ming Family, Ming Education, and future systems.

## Repository map

```text
foundation/       Charter, mission, vision, principles, ethics
standards/        Ming Open Standards (MOS), protocols, RFCs
infrastructure/   Kernel, core, runtime, SDK, APIs
reference/        Ontology, glossary, examples, diagrams
research/         Psychology, education, neuroscience, systems, philosophy
projects/         MingOS and application projects
governance/       Roadmaps, decisions, releases, review records
architecture/     System maps and reference architecture
docs/             Templates and contributor documentation
scripts/          Repository validation
```

## Layer model

```text
Layer 0 — Charter
Layer 1 — Philosophy & Science
Layer 2 — Standards
Layer 3 — Infrastructure
Layer 4 — Projects
Layer 5 — Community & Governance
```

Applications must not bypass the foundation:

```text
Charter
  ↓
Ontology & Standards
  ↓
Kernel & Core
  ↓
SDK / Protocols
  ↓
Projects
```

## Initial documents

- [`foundation/0000-architecture-blueprint.md`](foundation/0000-architecture-blueprint.md)
- [`foundation/charter/MF-0001-mission.md`](foundation/charter/MF-0001-mission.md)
- [`foundation/charter/MF-0002-vision.md`](foundation/charter/MF-0002-vision.md)
- [`foundation/principles/MF-0003-first-principles.md`](foundation/principles/MF-0003-first-principles.md)
- [`standards/mos/MOS-0000-standard-process.md`](standards/mos/MOS-0000-standard-process.md)
- [`governance/decisions/ADR-0001-ai-is-not-the-center.md`](governance/decisions/ADR-0001-ai-is-not-the-center.md)
- [`governance/decisions/ADR-0002-observation-before-advice.md`](governance/decisions/ADR-0002-observation-before-advice.md)

## Working principles

1. **Life before system.**
2. **Understanding before advice.**
3. **Relationship before method.**
4. **Growth is not optimization.**
5. **Every interpretation remains revisable.**
6. **Human agency cannot be delegated away.**
7. **Evidence, confidence, consent, and auditability are first-class concerns.**

## Contribution flow

```text
Issue / Discussion
  ↓
RFC
  ↓
Architecture & Ethics Review
  ↓
MOS Candidate Standard
  ↓
Implementation
  ↓
Validation
  ↓
Stable Standard
```

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Version

Current repository foundation version: **1.0.0-alpha.1**

## License

Documentation and standards are licensed under **CC BY 4.0**.  
Software and executable examples are licensed under **Apache License 2.0**.

See [`LICENSE.md`](LICENSE.md).
