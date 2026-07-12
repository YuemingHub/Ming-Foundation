---
created: 2026-07-12
depends_on:
- MF-0000
- ADR-0001
- ADR-0002
- ADR-0003
- ADR-0004
id: GOV-0001
layer: Cross-layer
owner: Ming Foundation Architecture
related:
- MF-0000
- MF-0001
- MF-0002
- MF-0003
- MF-0004
- ADR-0001
- ADR-0002
- ADR-0003
- ADR-0004
- ADR-0005
- GOV-0004
- PROJECT-MINGOS-0000
- PROJECT-MINGOS-0001
- PROJECT-MINGOS-0002
- ADR-0006
- ADR-0007
- GOV-0007
- GOV-0008
- GOV-0009
- GOV-0010
- GOV-0011
- GOV-0012
- GOV-0013
- GOV-0014
- GOV-0015
- GOV-0016
- GOV-0017
- GOV-0018
- GOV-0019
- RFC-0001
- RFC-0002
- RFC-0003
- RFC-0004
- RFC-0005
status: Accepted
title: Current Canonical State
updated: 2026-07-12
version: 1.0.0-alpha.6
---

# GOV-0001 — Current Canonical State

## 1. Purpose

This document records the current accepted baseline of Ming Foundation
and MingOS. It exists so that contributors, AI coding agents,
researchers, and future conversations can distinguish current decisions
from proposals, experiments, and historical drafts.

This is a living governance record. It MUST be updated when an accepted
decision materially changes the project identity, official surfaces,
scope, authority model, or current stage.

## 2. Official public surfaces

The following facts are accepted:

- **Official website:** `https://mingos.cn`
- **Canonical public repository:**
  `https://github.com/YuemingHub/Ming-Foundation`
- **Repository visibility:** public
- **Current repository stage:** Foundation 1.0 / Day 6 — Validation
  Remediation and External Review Preparation
- **Current repository version:** `1.0.0-alpha.6`

`mingos.cn` is the official public interface of MingOS. It communicates
the project to users, contributors, researchers, partners, and the wider
public.

`YuemingHub/Ming-Foundation` is the canonical public knowledge
repository for the formalized outcomes of MingOS discussions,
architecture work, standards work, research synthesis, project
decisions, and governance records.

## 3. Current project state

### Completed

- Day 1 repository architecture and layer model;
- contribution and governance scaffolding;
- document metadata and identifier rules;
- initial mission, vision, first principles, and architecture blueprint;
- initial architecture decisions;
- repository validation tooling;
- Day 2 canonical public surface and source-of-truth decisions;
- Day 2 conversation-to-repository workflow;
- Day 3 consolidation of historical Charter material into reviewable
  Drafts;
- Day 3 proposal separating the Charter of Life, MingOS Charter, and
  MingOS Kernel;
- Day 4 acceptance of the three-layer boundary;
- Day 4 article-by-article Charter review and Candidate revisions;
- Day 4 Charter validation plan;
- Day 5 website and public-claims evidence audit;
- Day 5 Family OS implementation mapping;
- Day 5 privacy, third-party-rights, safety, professional-boundary, and
  counterexample analyses;
- Day 5 decision to retain both Charters at Candidate;
- Day 6 minimum remediation protocols for contestability, data rights,
  safety, case governance, and public claims;
- Day 6 external and affected-person review instruments;
- Day 6 restricted evidence-handling protocol;
- Day 6 decision requiring remediation contracts before Charter
  acceptance.

### In progress

- review and promotion of Day 1 Draft documents;
- direct live website and direct source-code audit against RFC-0001
  through RFC-0005;
- implementation backlog and acceptance-test mapping;
- review and revision of Proposed remediation protocols;
- recruitment and execution of affected-person and independent external
  review;
- privacy, child-rights, safety, commercial, legal, and professional
  review;
- systematic import of relevant conclusions from historical
  conversations;
- consolidation of Charter-level documents;
- consolidation of terminology, ontology, and evidence models;
- connection between accepted standards and real MingOS implementations.

### Not yet complete

The following MUST NOT be described as complete merely because they have
appeared in discussion:

- a stable Ming Foundation 1.0 standard set;
- an Accepted Charter of Life or MingOS Charter;
- a complete MOSS specification;
- a complete MingOS Kernel specification;
- a production-ready general-purpose Life Operating System;
- a stable public SDK, cloud platform, certification system, or
  developer ecosystem;
- complete import of all historical conversations;
- legal establishment of an entity called “Ming Foundation.”

## 4. Authority order

When sources conflict, use this order:

1.  Accepted or Stable documents merged into the default branch of
    `YuemingHub/Ming-Foundation`;
2.  accepted ADRs and recorded governance decisions in the repository;
3.  Draft, Proposed, Candidate, or Experimental documents in the
    repository;
4.  open pull requests, RFCs, and issues;
5.  structured but unmerged handoff packages;
6.  conversation outputs, notes, and exploratory drafts;
7.  memory, recollection, or unsupported summaries.

A newer statement does not automatically override an accepted decision.
Material changes require the repository process appropriate to the
affected layer.

## 5. Meaning of “all discussed content”

The repository is intended to account for all project-relevant
discussion outcomes over time. Accounting for a discussion means that it
is eventually:

- accepted and incorporated;
- retained as a Draft or Experimental proposal;
- rejected with reasons;
- marked Superseded;
- archived for historical traceability; or
- excluded because it contains private, unsafe, irrelevant, or
  non-project material.

This does not require publishing raw conversations, personal data,
confidential family cases, credentials, or sensitive operational
information.

## 6. Discussion is not automatic authority

Conversation windows are working spaces. They MAY generate:

- hypotheses;
- language;
- architecture proposals;
- research questions;
- product decisions;
- implementation plans;
- critiques and alternatives.

They do not become canonical merely because they are detailed, repeated,
recent, or produced by an AI system. They become project assets through
the workflow defined in `GOV-0003`.

## 7. Current architectural commitments

The accepted commitments currently include:

- life before system;
- understanding before advice;
- relationship before method;
- growth is not reducible to optimization;
- interpretations remain revisable;
- human agency cannot be delegated away;
- evidence, confidence, consent, correction, and auditability are
  first-class concerns;
- AI is a replaceable component and not the architectural center;
- observation precedes advice;
- channels must not become incompatible sources of truth.

## 8. Update rule

Any update to this document MUST:

- identify the decision or evidence that caused the change;
- update `REPOSITORY_INDEX.md` and `CHANGELOG.md` when material;
- preserve prior state through Git history;
- avoid promoting unresolved discussion into accepted fact;
- state what remains uncertain.

## 9. Next canonical work

After Day 6, the next canonical work is Direct Audit and Remediation
Implementation Backlog:

1.  obtain current revision identifiers for `mingos.cn` and
    implementation repositories;
2.  map current behavior to every MUST-level requirement in RFC-0001
    through RFC-0005;
3.  distinguish implemented, partial, absent, conflicting, and
    unverifiable requirements;
4.  produce implementation tasks with owner, dependency, risk,
    acceptance test, and evidence;
5.  run counterexamples from `GOV-0012` against current product paths;
6.  prepare the first external and affected-person review cycle using
    `GOV-0016` and `GOV-0017`;
7.  keep both Charters at Candidate.
