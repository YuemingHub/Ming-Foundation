---
id: GOV-0003
title: Conversation-to-Repository Workflow
status: Accepted
version: 1.0.0-alpha.2
layer: Layer 5 — Community & Governance
owner: Ming Foundation Governance
created: 2026-07-12
updated: 2026-07-12
related:
  - GOV-0001
  - GOV-0002
  - MOS-0000
  - ADR-0003
  - ADR-0004
depends_on:
  - GOV-0001
  - GOV-0002
  - MOS-0000
---

# GOV-0003 — Conversation-to-Repository Workflow

## 1. Purpose

This workflow defines how outputs from conversations, workshops, coding agents, research sessions, and architecture discussions become governed Ming Foundation assets.

Its purpose is not to slow discussion. Its purpose is to preserve meaning while preventing duplication, privacy breaches, untraceable claims, and accidental promotion of speculation into authority.

## 2. Core rule

> A conversation may generate a proposal. The repository records the project decision.

No conversational output is canonical until it has been classified, reviewed at the appropriate level, and merged into the canonical repository.

## 3. Workflow

```text
Conversation or working session
  ↓
Outcome extraction
  ↓
Source and privacy review
  ↓
Conflict and duplication check
  ↓
Artifact classification
  ↓
Draft creation with metadata
  ↓
Architecture / ethics / domain review as required
  ↓
Validation
  ↓
Merge
  ↓
Index, changelog, and status update
```

## 4. Step 1 — Extract outcomes

At the end of a material conversation, record:

- what was confirmed;
- what was corrected or rejected;
- what remains uncertain;
- what evidence or implementation constraint was introduced;
- what repository artifact, if any, should change;
- the single best next action.

Do not treat the entire transcript as the outcome.

## 5. Step 2 — Separate knowledge status

Each substantive statement should be classified as one of:

- fact;
- observation;
- hypothesis;
- pattern;
- judgment;
- decision;
- open question.

A hypothesis MUST NOT be rewritten as a fact merely to make a document sound decisive.

## 6. Step 3 — Apply privacy and publication review

Before public repository inclusion, remove or exclude:

- identifiable personal or family information;
- confidential case details;
- secrets and credentials;
- unnecessary personal history;
- copyrighted source material beyond permitted quotation or summary;
- operational details that create avoidable security risk.

When useful learning depends on sensitive cases, use a separately governed de-identification and consent process rather than copying raw conversation content.

## 7. Step 4 — Check existing authority

Before creating a new file:

1. read `GOV-0001`;
2. check `REPOSITORY_INDEX.md`;
3. search existing IDs and terminology;
4. inspect related Accepted ADRs;
5. identify whether the new outcome confirms, extends, conflicts with, or supersedes existing material.

Repeated wording is not a new standard. Conflicting wording requires explicit resolution.

## 8. Step 5 — Select the artifact type

| Outcome | Preferred artifact |
|---|---|
| Foundational commitment | `MF-*` Charter or principle document |
| Material architecture decision | `ADR-*` |
| Proposed cross-layer change | `RFC-*` |
| Stable implementation-independent requirement | `MOS-*` |
| Current governance state or process | `GOV-*` |
| MingOS project boundary or plan | `PROJECT-MINGOS-*` |
| Definition, glossary, example, or reference model | `REF-*` or reference material |
| Research synthesis | Research document with evidence and limitations |
| Implementation-only change | Code, test, implementation task, or project-specific record |

One conversation may update several artifacts, but each artifact should have one clear responsibility.

## 9. Step 6 — Assign status conservatively

Use the least authoritative status that accurately reflects review:

- `Draft` for working documents;
- `Proposed` for a decision awaiting acceptance;
- `Accepted` for a reviewed governing decision;
- `Candidate` for a standard undergoing implementation validation;
- `Stable` only after defined evidence and compatibility requirements are met;
- `Experimental` for intentional trials;
- `Superseded` when replaced;
- `Archived` for retained historical material.

Detail and confidence of writing are not substitutes for review.

## 10. Step 7 — Review gates

Review depth depends on impact.

### Editorial change

Requires clarity, metadata, link, and validation checks.

### Project decision

Requires project boundary and compatibility review.

### Architecture or standard change

Requires affected-layer analysis, alternatives, compatibility, human-agency review, and evidence.

### Safety-sensitive change

Requires explicit review of consent, correction, privacy, dependency, coercion, escalation, and foreseeable harm.

## 11. Step 8 — Merge and record

A merged material change SHOULD update, where applicable:

- `REPOSITORY_INDEX.md`;
- `CHANGELOG.md`;
- `GOV-0001-current-canonical-state.md`;
- related document metadata;
- source registry;
- roadmap or implementation task.

The commit or pull request should explain what was added, what was not added, and why.

## 12. Required conversation closeout

For significant MingOS conversations, the closing summary SHOULD use this structure:

```text
Confirmed in this conversation
Corrected or rejected
Repository artifacts affected
Next best action
```

When no repository change is justified, state that explicitly.

## 13. Definition of done

A conversation outcome is integrated only when:

- its source is known;
- private material has been handled safely;
- conflicts have been checked;
- status is explicit;
- required metadata is present;
- repository validation passes;
- the change is merged;
- entry points are updated when needed.

A ZIP package, local document, or chat response is a transfer artifact, not proof of repository integration.
