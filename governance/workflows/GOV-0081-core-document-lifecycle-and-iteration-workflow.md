---
id: GOV-0081
title: Core Document Lifecycle and Iteration Workflow
status: Proposed
version: 0.1.0
layer: Layer 5 — Community & Governance
owner: Ming Foundation Governance
created: 2026-07-13
updated: 2026-07-13
related:
  - GOV-0001
  - GOV-0003
  - ADR-0004
  - ADR-0005
  - ADR-0017
  - MF-0004
  - PROJECT-MINGOS-0002
  - ADR-0021
  - GOV-0082
depends_on:
  - GOV-0001
  - GOV-0003
  - ADR-0004
  - ADR-0005
  - ADR-0017
---

# GOV-0081 — Core Document Lifecycle and Iteration Workflow

## 1. Purpose

This Proposed workflow defines how Ming Foundation and MingOS create, review, revise, translate, publish, and supersede core philosophical, Charter, Kernel, and culture documents.

It extends `GOV-0003` for a narrower problem: long-lived core texts that may influence multiple standards, products, agents, professional practices, public claims, and governance decisions.

Its purpose is to prevent:

- multiple uncontrolled copies of the same root text;
- chat outputs, DOCX files, ZIP packages, or translations becoming accidental sources of authority;
- simultaneous editing of interdependent root texts without traceability;
- status promotion based on writing quality rather than review and evidence;
- silent semantic drift between Chinese and English;
- generated publication artifacts diverging from repository sources;
- a later document silently redefining a higher or already Accepted layer.

## 2. Scope

This workflow applies to:

- mission, vision, first principles, and philosophy;
- the Core Thought, Culture, and Philosophy Compendium;
- the Charter of Life;
- the MingOS Charter;
- the MingOS Kernel and future Kernel specifications;
- core terminology and ontology;
- official Chinese and English versions;
- generated DOCX, PDF, ZIP, website, and release editions;
- historical principle mappings and supersession records.

This workflow does not replace:

- the status rules in `GOV-0003`;
- RFC and MOS review requirements;
- affected-person, legal, privacy, child-rights, safety, or professional review;
- implementation conformance;
- the current Day 15 Profile review and revision work.

## 3. Core rules

### 3.1 One repository

`YuemingHub/Ming-Foundation` is the canonical public repository for governed Ming Foundation and MingOS core texts.

No second repository, website, local folder, AI memory, or conversation may silently become a competing source of truth.

### 3.2 One canonical editable source

The canonical editable form of a governed core text is UTF-8 Markdown committed to the canonical repository.

DOCX, PDF, website pages, release ZIPs, slides, and other rendered artifacts are derived publication forms. They may be authoritative publications of a version, but they are not independent editing sources.

### 3.3 One document per review round

The default review unit is one governed document.

A review round MUST identify:

- the single primary document;
- the baseline commit;
- the proposed version;
- the review question;
- the intended status;
- related documents that may be affected;
- documents explicitly excluded from the round.

A review MAY record downstream changes without modifying all downstream documents in the same round.

### 3.4 No silent cross-layer redefinition

A lower-layer document MUST NOT silently redefine a higher-layer commitment.

When a proposed change conflicts with an Accepted decision, Candidate Charter, Proposed RFC, or governed term, the conflict MUST be identified and resolved through the appropriate ADR, RFC, Charter, or governance process.

### 3.5 Status remains conservative

Writing, translation, formatting, or publication does not promote status.

- `Draft` means active working text.
- `Proposed` means a governing decision or process awaiting acceptance.
- `Candidate` requires defined validation.
- `Accepted` requires the appropriate review decision.
- `Stable` requires the evidence, compatibility, and maturity gates defined for that artifact.

### 3.6 Generated editions remain traceable

Every generated DOCX, PDF, ZIP, website edition, or public release SHOULD identify:

- source repository;
- source commit;
- document ID;
- source version;
- language;
- generation date;
- status;
- whether the artifact is normative or informational.

## 4. Review round lifecycle

```text
Select one primary document
  ↓
Read current canonical state and related authority
  ↓
Declare scope and exclusions
  ↓
Create topic branch and Draft PR
  ↓
Revise the primary Markdown source
  ↓
Run terminology, cross-text, privacy, ethics, and status checks
  ↓
Record disagreements, open questions, and downstream impacts
  ↓
Run repository validation
  ↓
User / owner review
  ↓
Architecture, affected-person, legal, safety, or domain review as required
  ↓
Merge without automatic status promotion
  ↓
Update index, changelog, mappings, and generated releases
```

## 5. Required round record

Each material core-text round MUST record:

1. primary document and ID;
2. baseline branch and commit;
3. proposed version and status;
4. reason for revision;
5. sections changed;
6. content deliberately not changed;
7. deleted or consolidated material;
8. related authority checked;
9. privacy and publication boundary;
10. affected people and review needs;
11. unresolved objections and unknowns;
12. downstream documents affected;
13. validators and tests executed;
14. decision and merge state;
15. next single best action.

The Pull Request MAY serve as this record when it contains all required fields.

## 6. Source and publication hierarchy

When representations conflict, apply the following order unless an Accepted ADR states otherwise:

1. governed Markdown source on the canonical repository default branch;
2. Accepted decisions and recorded status governing that source;
3. open Pull Request source for the active review round;
4. generated releases tied to a specific source commit;
5. local handoff packages;
6. conversation text, AI output, recollection, or unsupported summaries.

A newer generated artifact does not override an older canonical source merely because it was created later.

## 7. Translation and multilingual review

Translation governance is defined by `ADR-0021`.

At minimum:

- language must be explicit;
- translation status must be explicit;
- the source commit must be traceable;
- normative force must not be inferred from visual completeness;
- semantic conflicts must be recorded, not hidden;
- translation alone cannot change document status;
- existing authority cannot be silently reassigned during migration.

## 8. Change classification

### 8.1 Editorial

Examples:

- punctuation;
- broken link;
- formatting;
- non-substantive terminology consistency.

Requires source, diff, metadata, and validation review.

### 8.2 Interpretive

Examples:

- explanation added to a principle;
- ambiguity reduced without changing a commitment;
- Chinese and English alignment.

Requires cross-text and translation review.

### 8.3 Normative

Examples:

- new right, duty, prohibition, exception, precedence rule, or status gate;
- change to who may decide, refuse, correct, inspect, appeal, or leave.

Requires affected-layer, human-agency, ethics, and domain review.

### 8.4 Safety-sensitive

Examples:

- emergency exception;
- child participation;
- third-party data;
- surveillance;
- professional handoff;
- retention despite deletion request.

Requires explicit safety, privacy, legal, child-rights, affected-person, and professional review as applicable.

## 9. Conflict handling

A review round MUST stop short of silent resolution when:

- two governed texts impose incompatible obligations;
- Chinese and English carry materially different meaning;
- a proposed philosophy statement is presented as established science;
- a product claim exceeds repository evidence;
- a new document would bypass an existing RFC or Profile;
- a status change lacks the required evidence;
- the responsible owner or affected-person review path is unknown.

The conflict MUST be entered into the relevant PR, ambiguity register, dissent register, ADR, RFC, or validation record.

## 10. Local Agent rules

A local coding or documentation Agent MAY:

- inspect repository authority;
- create a topic branch;
- add Draft or Proposed source files;
- update indexes and changelogs;
- generate diffs and validation reports;
- prepare a Draft Pull Request.

A local Agent MUST NOT, without explicit user instruction and the required decision record:

- merge the Pull Request;
- promote a Charter, RFC, Profile, Kernel, or governance document;
- close dissent or ambiguity;
- modify a root text outside the declared round;
- treat a generated ZIP or DOCX as canonical;
- import identifiable family cases or private conversations;
- enter another repository.

## 11. Definition of done

A core-text review round is complete only when:

- scope and exclusions were explicit;
- canonical authority was checked;
- the primary Markdown source is identified;
- changes are reviewable in Git;
- status is accurate;
- conflicts and unknowns remain visible;
- validation passes;
- required reviewers have acted or the missing review is recorded;
- index, changelog, and mappings are updated when needed;
- generated publications identify their source commit;
- the merge state is explicit.

A Draft PR, local ZIP, or polished document is not by itself proof of integration, acceptance, validation, or implementation conformance.

## 12. Open questions

Before this workflow may become Accepted, review should decide:

1. whether every core-text round requires an Architecture Board reviewer;
2. whether root-text PRs require an affected-person review label;
3. which generated formats are required at release time;
4. how bilingual semantic disputes are adjudicated;
5. whether public philosophical documents require a distinct `MF-*` document class or remain within current Foundation categories;
6. what minimum evidence is required before a Draft Kernel becomes Candidate.
