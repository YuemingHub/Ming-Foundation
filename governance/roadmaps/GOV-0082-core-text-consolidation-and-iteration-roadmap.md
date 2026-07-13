---
id: GOV-0082
title: Core Text Consolidation and Iteration Roadmap
status: Draft
version: 0.1.0
layer: Layer 5 — Community & Governance
owner: Ming Foundation Architecture
created: 2026-07-13
updated: 2026-07-13
related:
  - GOV-0001
  - GOV-0003
  - GOV-0081
  - ADR-0021
  - MF-0003
  - MF-0004
  - PROJECT-MINGOS-0002
  - REF-0002
depends_on:
  - GOV-0001
  - GOV-0003
  - ADR-0005
---

# GOV-0082 — Core Text Consolidation and Iteration Roadmap

## 1. Purpose

This Draft roadmap sequences the consolidation, review, bilingual governance, engineering specification, validation, and publication of MingOS core texts.

It is intentionally incremental. It does not declare the core texts complete, does not promote either Charter, and does not replace the current Day 15 review-readiness and operational-activation work.

## 2. Governing approach

The roadmap uses the following default:

> One repository, one canonical Markdown source per governed language, one primary document per round, one reviewable Pull Request, and no status promotion without evidence.

Each round MUST:

- name one primary document;
- state what is excluded;
- preserve current authority;
- record downstream impacts;
- pass repository validation;
- remain unmerged until owner review;
- avoid modifying implementation evidence outside scope.

## 3. Current baseline

At the creation of this roadmap:

- repository stage is Foundation 1.0 / Day 15;
- repository version is `1.0.0-alpha.15`;
- both Charters remain `Candidate`;
- RFC-0001 through RFC-0005 remain `Proposed`;
- PROF-0001 through PROF-0004 remain `Proposed`;
- affected-person review is prepared but not executed;
- a complete MingOS Kernel specification does not yet exist;
- historical conversation import remains incomplete;
- the current conformance baseline does not prove product implementation conformance.

## 4. Workstreams

The roadmap contains two parallel but non-conflicting workstreams.

### Workstream A — Existing Day 15 continuation

This workstream remains governed by the current canonical state:

- assignment of accountable operational roles;
- approval of review protocols;
- restricted evidence-environment readiness;
- controlled pilot authorization;
- preserved ambiguity and dissent;
- no unsupported promotion.

### Workstream B — Core-text consolidation

This workstream establishes and reviews the philosophy, Charters, Kernel, and application guidance.

Workstream B MUST NOT modify Profile or RFC status without the appropriate existing process.

## 5. Round sequence

### Round 01 — Install core-text governance

Primary artifacts:

- `GOV-0081`;
- `ADR-0021`;
- this roadmap.

Outcome:

- a Draft PR;
- no Charter or Kernel text change;
- no status promotion;
- an agreed iteration method.

Exit gate:

- repository validation passes;
- no identifier conflict;
- owner reviews the workflow;
- unresolved language-authority questions remain visible.

### Round 02 — Core Thought, Culture, and Philosophy Compendium

Primary document:

- proposed `MF-0005` Chinese Draft.

Purpose:

- create the unified Chinese interpretation entry point;
- consolidate mission, worldview, life logic, human view, growth view, relationship view, technology view, culture, boundaries, and governance meaning;
- distinguish philosophy, ethics, science hypotheses, product principles, and legal requirements;
- identify material simplified or omitted from historical discussions.

Explicit exclusions:

- no Charter status change;
- no complete Kernel specification;
- no claim of scientific validation;
- no application handbook.

Required review:

- terminology;
- cross-text consistency;
- historical source mapping;
- unsupported universality claims;
- privacy and case-publication boundary.

### Round 03 — Historical principles and terminology mapping

Primary artifacts:

- historical principle evolution map;
- updated `REF-0002` or a successor glossary;
- mapping of early axioms, prohibitions, safety gates, and later Charter articles.

Purpose:

- preserve project memory;
- show retained, consolidated, rejected, superseded, and unresolved concepts;
- prevent old slogans from becoming shadow standards.

### Round 04 — Charter of Life Chinese migration candidate

Primary document:

- paired Chinese candidate for `MF-0004`.

Purpose:

- translate and review article by article;
- preserve Candidate status;
- map normative force and exceptions;
- identify philosophical, legal, safety, and affected-person ambiguities.

Required review:

- affected-person;
- child-rights;
- privacy;
- safety;
- professional boundary;
- legal qualification;
- translation semantics.

### Round 05 — MingOS Charter Chinese migration candidate

Primary document:

- paired Chinese candidate for `PROJECT-MINGOS-0002`.

Purpose:

- translate organizational, product, data, commercial, professional, and technical self-restraints;
- preserve Candidate status;
- map every commitment to implementation or unresolved contracts.

### Round 06 — Kernel scope and authority decision

Primary artifact:

- an ADR or RFC defining what “MingOS Kernel” is.

Must decide:

- whether Kernel is a single specification or a specification family;
- document IDs and repository location;
- normative boundary between Charter, RFC, MOS, Profile, and implementation;
- what constitutes Kernel conformance;
- what remains replaceable;
- how AI, human, and affected-person roles are represented.

### Round 07 — Kernel core specification

Primary document:

- Kernel Draft.

Minimum domains:

- identity, subject, speaker, and representative authority;
- consent and purpose;
- knowledge-status separation;
- evidence and confidence;
- relationship and timeline context;
- observation before advice;
- safety, handoff, appeal, and incident;
- memory inspection, correction, revocation, retention, and deletion;
- user-chosen, small, reversible action;
- feedback and state revision;
- audit, versioning, failure, counterexample, and unknown;
- human responsibility and AI limits.

### Round 08 — Kernel data model and state machines

Primary artifacts:

- canonical object model;
- consent lifecycle;
- memory lifecycle;
- safety and handoff state machine;
- appeal and remediation lifecycle;
- language and source traceability.

### Round 09 — Kernel conformance suite

Primary artifacts:

- requirements;
- test specifications;
- machine-readable derived indexes;
- empty baseline;
- reference test cases.

No product may be called conforming merely because tests are specified.

### Round 10 — Application standards

One application document per round:

- family and parenting practice;
- professional support boundary;
- AI product design;
- content and language;
- commercial and sales ethics;
- Observatory;
- Lab and evidence;
- child and third-party participation;
- partner and name-use conformance.

## 6. Round priority rule

The next round is selected by:

1. unresolved authority risk;
2. potential harm to affected people;
3. dependency order;
4. ability to produce reviewable evidence;
5. implementation need;
6. communication convenience.

Public visibility or writing enthusiasm alone does not determine priority.

## 7. Status policy

This roadmap does not predetermine status promotion.

- The Compendium begins as `Draft`.
- Bilingual Charter files remain `Candidate` only if they are governed as part of the existing Candidate migration; otherwise they begin as Draft translation artifacts.
- Kernel documents begin as `Draft` or `Proposed` according to artifact type.
- Conformance remains unclaimed until executed evidence exists.
- Generated publications use `Generated` or `Reference` labeling and inherit source status.

## 8. Required outputs per round

Each round SHOULD produce:

- primary Markdown source;
- source and authority note;
- change summary;
- open questions;
- downstream impact map;
- validation report;
- Draft PR;
- owner decision;
- updated index and changelog when merged;
- generated publication only after source review.

## 9. Pause conditions

A round pauses when:

- identifier conflicts exist;
- current canonical state changed materially;
- the working tree is not clean and ownership is unclear;
- a proposed change conflicts with Accepted authority;
- translation changes a right, exception, or obligation without review;
- personal or family data appears in public material;
- a safety-sensitive statement lacks qualified review;
- validation fails;
- the primary document expands into several uncontrolled documents;
- implementation claims exceed evidence.

## 10. Success criteria

The roadmap succeeds when:

- contributors can locate the current source of each core commitment;
- Chinese and English authority is explicit;
- each revision is visible and reversible;
- historical thought is accounted for without becoming shadow authority;
- Charters remain concise and governed;
- Kernel commitments become executable requirements and tests;
- public publications are reproducible from repository sources;
- affected people can understand and challenge how the system represents them;
- no status is promoted merely because a document is polished.

## 11. Immediate next action

Complete Round 01 as a Draft PR.

After owner review of Round 01, begin Round 02 with exactly one primary document: the Chinese `MingOS Core Thought, Culture, and Philosophy Compendium` Draft.
