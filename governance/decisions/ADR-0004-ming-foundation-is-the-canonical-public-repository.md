---
id: ADR-0004
title: Ming-Foundation Is the Canonical Public Repository
status: Accepted
version: 1.0.0
layer: Cross-layer
owner: Ming Foundation Architecture
created: 2026-07-12
updated: 2026-07-12
related:
  - MF-0000
  - GOV-0001
  - GOV-0002
  - GOV-0003
  - ADR-0003
  - PROJECT-MINGOS-0001
depends_on:
  - MF-0000
---

# ADR-0004 — Ming-Foundation Is the Canonical Public Repository

## Context

MingOS has been explored across many conversation windows, documents, ZIP packages, coding-agent sessions, website prototypes, and implementation efforts. Without one canonical public repository, repeated discussions can produce incompatible definitions, lost decisions, uncertain status, and an inability to trace why the project changed.

The repository `YuemingHub/Ming-Foundation` has already been initialized with architecture, governance, documentation standards, identifiers, and validation tooling.

## Decision

`https://github.com/YuemingHub/Ming-Foundation` is the canonical public knowledge repository for MingOS and Ming Foundation formalized project outcomes.

The repository is the place where project-relevant discussions are progressively accounted for through:

- accepted documents;
- Draft or Experimental proposals;
- ADRs and RFCs;
- standards and schemas;
- research syntheses;
- project records;
- implementation references;
- supersession, rejection, and archive records.

Conversation windows, local ZIP files, coding-agent outputs, and website copy are source or transfer artifacts. They do not override accepted repository records unless a governed repository change is made.

This decision does not require publishing private data, confidential case material, secrets, or unsafe information.

## Reasons

- One repository creates traceable project memory across time and tools.
- Git history preserves authorship, change, review, and supersession.
- Public visibility supports accountability and contribution.
- Structured identifiers and statuses distinguish accepted decisions from exploration.
- The repository can govern both human- and AI-generated project work.

## Consequences

### Positive

- New conversations can begin from a verifiable baseline.
- Contributors can identify current authority and unresolved work.
- Website and implementation projects can reference stable decisions.
- Duplicate concepts and conflicting drafts can be reconciled systematically.
- AI agents can be instructed to inspect the repository before proposing changes.

### Negative

- Historical content requires careful, time-consuming consolidation.
- Maintainers must keep indexes, statuses, and links current.
- Not every useful conversation can be copied verbatim because of privacy, relevance, or quality.
- Public governance requires clear separation between project knowledge and sensitive operational information.

## Alternatives considered

### Treat every conversation as equally authoritative

Rejected because conversations can conflict, omit context, and change without traceable review.

### Maintain several equal master repositories

Rejected for project knowledge because it creates divergent sources of truth. Separate implementation repositories may exist, but their authority and relationship must be registered.

### Use only a private document archive

Rejected as the canonical public knowledge model because it prevents open review and weakens durable public accountability. Private restricted stores may still be required for sensitive information.

## Follow-up

- Use `GOV-0002` to register material sources.
- Use `GOV-0003` to process future conversation outputs.
- Update `GOV-0001` when project identity or authority changes.
- Import historical discussion by topic and status, not by blindly copying transcripts.
