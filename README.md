# Ming Foundation

> Building the standards, infrastructure, and ecosystem for Living Intelligence.  
> 构建生命智能的标准、基础设施与生态。

Ming Foundation is an open standards initiative dedicated to one question:

> **How can technology help life understand itself without replacing, controlling, or reducing life?**  
> **技术如何帮助生命理解自己，而不是替代、控制或简化生命？**

## Current status

This repository is at **Foundation 1.0 / Day 3 — Charter Consolidation Draft**. Day 1 established the repository architecture. Day 2 established the canonical public surfaces, source registry, current-state baseline, and conversation-to-repository workflow. Day 3 introduces reviewable drafts of the Charter of Life and MingOS Charter, and proposes a strict boundary between Charter and Kernel.

**Important:** “Ming Foundation” is currently the name of an open standards initiative and repository. It does not by itself claim to be a legally registered foundation.

## Official project surfaces

- **Official MingOS website:** [`mingos.cn`](https://mingos.cn)
- **Canonical public repository:** [`YuemingHub/Ming-Foundation`](https://github.com/YuemingHub/Ming-Foundation)

Conversation windows, coding-agent sessions, and ZIP handoff packages are working or transfer sources. Project-relevant outcomes become formal project assets through review and repository integration. Private case data, personal information, secrets, and unsafe material must not be published merely to preserve discussion history.

See:

- [`governance/status/GOV-0001-current-canonical-state.md`](governance/status/GOV-0001-current-canonical-state.md)
- [`governance/sources/GOV-0002-source-registry.md`](governance/sources/GOV-0002-source-registry.md)
- [`governance/workflows/GOV-0003-conversation-to-repository.md`](governance/workflows/GOV-0003-conversation-to-repository.md)

Day 3 Charter drafts:

- [`foundation/charter/MF-0004-life-charter.md`](foundation/charter/MF-0004-life-charter.md)
- [`projects/mingos/PROJECT-MINGOS-0002-mingos-charter.md`](projects/mingos/PROJECT-MINGOS-0002-mingos-charter.md)
- [`governance/decisions/ADR-0005-three-root-texts-and-boundaries.md`](governance/decisions/ADR-0005-three-root-texts-and-boundaries.md)
- [`governance/reviews/GOV-0004-day3-charter-consolidation-record.md`](governance/reviews/GOV-0004-day3-charter-consolidation-record.md)

**Status note:** the two Charters are `Draft`; the boundary ADR is `Proposed`. They are not yet Accepted standards.

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

## Charter stack under review

```text
The Charter of Life
  ↓
MingOS Charter
  ↓
MingOS Kernel
  ↓
Products, agents, services, research, and operations
```

The Charter of Life states higher ethical commitments. The MingOS Charter states project self-restraints. The Kernel operationalizes them through protocols, data models, safety gates, tests, and runtime behavior. These layers must not be collapsed into one document.

## Initial documents

- [`foundation/0000-architecture-blueprint.md`](foundation/0000-architecture-blueprint.md)
- [`foundation/charter/MF-0001-mission.md`](foundation/charter/MF-0001-mission.md)
- [`foundation/charter/MF-0002-vision.md`](foundation/charter/MF-0002-vision.md)
- [`foundation/principles/MF-0003-first-principles.md`](foundation/principles/MF-0003-first-principles.md)
- [`foundation/charter/MF-0004-life-charter.md`](foundation/charter/MF-0004-life-charter.md)
- [`standards/mos/MOS-0000-standard-process.md`](standards/mos/MOS-0000-standard-process.md)
- [`governance/decisions/ADR-0001-ai-is-not-the-center.md`](governance/decisions/ADR-0001-ai-is-not-the-center.md)
- [`governance/decisions/ADR-0002-observation-before-advice.md`](governance/decisions/ADR-0002-observation-before-advice.md)
- [`governance/decisions/ADR-0003-mingos-cn-is-the-official-website.md`](governance/decisions/ADR-0003-mingos-cn-is-the-official-website.md)
- [`governance/decisions/ADR-0004-ming-foundation-is-the-canonical-public-repository.md`](governance/decisions/ADR-0004-ming-foundation-is-the-canonical-public-repository.md)
- [`governance/decisions/ADR-0005-three-root-texts-and-boundaries.md`](governance/decisions/ADR-0005-three-root-texts-and-boundaries.md)

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

Current repository foundation version: **1.0.0-alpha.3**

## License

Documentation and standards are licensed under **CC BY 4.0**.  
Software and executable examples are licensed under **Apache License 2.0**.

See [`LICENSE.md`](LICENSE.md).
