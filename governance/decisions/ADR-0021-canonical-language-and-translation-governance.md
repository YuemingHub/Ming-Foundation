---
id: ADR-0021
title: Canonical Language and Translation Governance
status: Proposed
version: 0.1.0
layer: Cross-layer
owner: Ming Foundation Architecture
created: 2026-07-13
updated: 2026-07-13
related:
  - GOV-0001
  - GOV-0003
  - ADR-0004
  - ADR-0005
  - ADR-0017
  - GOV-0081
  - GOV-0082
  - MF-0004
  - PROJECT-MINGOS-0002
depends_on:
  - GOV-0001
  - ADR-0004
  - ADR-0005
  - ADR-0017
---

# ADR-0021 — Canonical Language and Translation Governance

## Context

MingOS emerged from Chinese-language life practice, family work, philosophical discussion, and product design. The canonical repository currently contains core governed documents whose primary maintained text is largely English, while substantial Chinese root-text and philosophy drafts now exist outside the repository.

Without an explicit decision, the project risks:

- two language versions diverging;
- a translated DOCX or ZIP being mistaken for a canonical source;
- Chinese concepts being reduced to approximate English terms;
- English normative keywords changing the force of Chinese commitments;
- silent replacement of existing Candidate Charters;
- future contributors not knowing which language controls a dispute;
- generated website or release text becoming an accidental third version.

The project also must preserve the current authority order. Existing governed files cannot lose authority merely because a later translation is more complete or more recent.

## Proposed decision

### 1. Repository Markdown remains canonical

The only canonical editable source for governed text is UTF-8 Markdown committed to `YuemingHub/Ming-Foundation`.

Rendered DOCX, PDF, ZIP, website, and presentation forms are derived publications and MUST identify their source commit.

### 2. Every governed core text declares language metadata

Core texts introduced or materially revised after this decision SHOULD declare:

```yaml
language: zh-CN
canonical_language: zh-CN
translation_status: original
```

or the corresponding values for another language.

Permitted translation states SHOULD include:

- `original`;
- `draft-translation`;
- `reviewed-translation`;
- `normative-translation`;
- `informational-translation`;
- `out-of-sync`;
- `superseded`.

### 3. Authority is document-specific, not assumed globally

The project does not declare that one language automatically controls every current and future document.

Instead:

- each governed document MUST declare its canonical language;
- a paired translation MUST identify the source document version and commit;
- the authority of an existing document remains unchanged until an explicit migration review is completed;
- translation does not change status or normative force by itself.

### 4. Chinese is the proposed original language for new philosophy and culture texts

For the planned `MingOS Core Thought, Culture, and Philosophy Compendium`, Chinese (`zh-CN`) is the proposed canonical original language because the source practice, conceptual development, and primary affected community are Chinese-language.

An English edition may become a reviewed or normative translation only after semantic review.

### 5. Existing Charters are not silently migrated

`MF-0004` and `PROJECT-MINGOS-0002` remain governed in their current repository form and current Candidate status until a dedicated bilingual migration round:

1. creates a Chinese source candidate and an English paired candidate;
2. maps every article and normative keyword;
3. records additions, omissions, and semantic risks;
4. receives architecture and translation review;
5. receives affected-person and domain review where meaning may change rights or duties;
6. records an explicit decision on canonical language and paired normative force;
7. preserves Git history and previous versions.

No file in a local handoff package may automatically supersede the existing Candidate Charters.

### 6. Normative keywords require semantic mapping

For documents using `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, or `MAY`, the Chinese version MUST preserve the intended force.

A translation map SHOULD record at least:

- article or requirement ID;
- source wording;
- translated wording;
- normative strength;
- known ambiguity;
- reviewer;
- review date;
- source commit;
- translation status.

### 7. Semantic conflict triggers review

When language versions conflict materially:

- neither version may silently overwrite the other;
- the conflict must be recorded;
- the affected article or requirement is marked for review;
- product, public-claim, or enforcement use must follow the last explicitly governed authority;
- if the conflict affects rights, safety, consent, children, third parties, professional duty, or commercial restraint, the relevant specialist review is required.

### 8. Machine-readable indexes remain derived

Translation maps, generated registries, glossaries, and public editions are derived indexes unless an Accepted decision explicitly grants them normative authority.

## Reasons

- MingOS must preserve the depth and origin of its Chinese-language life philosophy.
- The repository must remain compatible with international technical and governance work.
- Existing Candidate documents must not be displaced without review.
- Authority should be explicit, traceable, and document-specific.
- Semantic uncertainty must be visible rather than hidden by polished translation.
- Translation is a governance activity when it changes rights, duties, prohibitions, or exceptions.

## Consequences

### Positive

- avoids uncontrolled bilingual divergence;
- protects the original Chinese conceptual context;
- preserves existing repository authority during migration;
- makes generated editions traceable;
- enables article-level review;
- supports future international collaboration;
- prevents translation quality from being confused with status promotion.

### Negative

- bilingual maintenance requires additional review;
- paired files and mapping records increase repository complexity;
- some terms may remain intentionally unresolved;
- Charter migration will take multiple rounds;
- a single convenient global “one language always wins” rule is rejected.

## Alternatives considered

### English always controls

Rejected as a universal rule because it would disconnect future philosophy and culture texts from their original Chinese conceptual and practice context.

### Chinese immediately replaces current English Charters

Rejected because it would silently change the authority of current Candidate files without article-level migration and review.

### Both languages automatically have equal authority

Rejected because unresolved conflicts would create ambiguous obligations.

### Translation remains informal

Rejected because root-text translation can change rights, duties, prohibitions, exceptions, and public claims.

## Follow-up

1. review this ADR as a Proposed decision;
2. define language metadata in the repository schema if accepted;
3. create a bilingual article-mapping template;
4. introduce the Chinese philosophy compendium as a Draft;
5. conduct a dedicated migration round for each Charter;
6. do not begin Kernel bilingual migration until the Kernel source and authority model are defined;
7. update public releases to display source commit, language, and status.
