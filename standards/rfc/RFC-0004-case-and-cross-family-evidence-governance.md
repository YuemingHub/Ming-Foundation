---
created: 2026-07-12
depends_on:
- RFC-0001
- RFC-0002
id: RFC-0004
layer: Layer 1 — Standards
owner: Ming Foundation Standards
related:
- MF-0004
- PROJECT-MINGOS-0002
- GOV-0009
- GOV-0010
- GOV-0012
- GOV-0014
- GOV-0018
- GOV-0019
- ADR-0007
status: Proposed
title: Case and Cross-Family Evidence Governance Protocol
updated: 2026-07-12
version: 0.1.0
---

# RFC-0004 — Case and Cross-Family Evidence Governance Protocol

## Status

Proposed minimum protocol.

## 1. Problem

Family cases and cross-family pattern analysis can improve
understanding, quality, and safety.

They can also:

- reveal identifiable families;
- turn consultation records into research material without permission;
- preserve sensitive child narratives;
- produce false generalizations;
- allow rare patterns to re-identify people;
- train models on data gathered for another purpose.

## 2. Core rule

Case and cross-family evidence MUST remain purpose-limited,
access-restricted, provenance-preserving, and resistant to
re-identification.

Implementation convenience is not a sufficient basis for reuse.

## 3. Evidence zones

### Zone A — Operational service record

Used to deliver the current service.

Controls:

- subject and source attribution;
- role-based access;
- current-purpose limitation;
- retention and rights handling;
- no public or general research access.

### Zone B — Safety and incident record

Used for narrowly defined safety, quality, or accountability purposes.

Controls:

- restricted access;
- explicit basis;
- incident linkage;
- separate retention review;
- no routine commercial reuse.

### Zone C — De-identified validation evidence

Used for Charter, product, or quality validation.

Controls:

- removal and transformation of direct and indirect identifiers;
- rarity review;
- minimum necessary excerpts;
- reviewer confidentiality;
- withdrawal and provenance handling;
- no public raw records.

### Zone D — Aggregate or cross-family analysis

Used to identify possible patterns across families.

Controls:

- minimum cohort rule;
- rare-pattern suppression;
- no individual drill-down for ordinary analysts;
- documented purpose;
- output review;
- uncertainty and counterexample preservation;
- prohibition on family ranking.

### Zone E — Public evidence

Only summaries that are safe, authorized, and non-identifying.

Public repository records SHOULD contain:

- method;
- limitations;
- aggregate findings;
- objections;
- decisions.

They MUST NOT contain raw identifiable family or child material.

## 4. De-identification review

Removing names is insufficient.

Review must consider:

- rare events;
- exact ages;
- schools, cities, jobs, dates, diagnoses, and family structure;
- distinctive language;
- linked events across records;
- small cohorts;
- public social-media information;
- reviewer knowledge;
- combinations of otherwise ordinary details.

A record should be considered identifiable when a reasonable informed
person could connect it to an individual or family.

## 5. Cross-family analysis rules

Cross-family analysis MUST:

- state its purpose;
- use the minimum fields required;
- document inclusion and exclusion;
- preserve uncertainty;
- prevent a pattern from becoming a universal rule;
- record counterexamples;
- avoid ranking families;
- prevent analysts from browsing unrelated cases;
- undergo privacy and bias review;
- expire or revalidate derived rules.

## 6. Model training and evaluation

Case availability does not authorize model training.

Training, fine-tuning, retrieval, evaluation, or prompt-example use
requires a separately governed basis that states:

- purpose;
- data categories;
- de-identification;
- provider or processor;
- retention;
- withdrawal handling;
- expected benefit;
- risk;
- approval;
- publication limits.

External model providers MUST NOT receive case data merely because the
application uses their API.

## 7. Restricted evidence exports

An evidence export must record:

- purpose;
- requester;
- approving authority;
- included fields;
- transformations;
- date;
- expiry;
- permitted recipients;
- prohibition on onward use;
- deletion confirmation.

## 8. Prohibited behavior

An implementation MUST NOT:

- commit raw family cases to the public repository;
- publish “anonymous” cases containing recognizable combinations;
- reuse consultation data for marketing;
- allow cross-family analysis to create family scores or rankings;
- use rare cases as model examples without separate review;
- let analysts access full cases when aggregates suffice;
- treat generated summaries as de-identified by default;
- preserve data indefinitely because future research may be useful.

## 9. Acceptance tests

A conforming implementation must demonstrate:

1.  operational and validation evidence are separated;
2.  analyst access cannot browse unrelated raw cases;
3.  rare-pattern outputs are suppressed or reviewed;
4.  an evidence export expires and records deletion;
5.  a withdrawn case can be traced through derived datasets;
6.  model-training use cannot occur without a separate approval record;
7.  public summaries pass re-identification review;
8.  cross-family rules preserve counterexamples and validity periods;
9.  family-stage outputs cannot be used as comparative rankings.

## 10. Open questions

- What minimum cohort is appropriate for different risk levels?
- Which transformations are required before external review?
- How should withdrawal affect previously published aggregate findings?
- Which derived rules require revalidation after data deletion?
- What independent review is required for model evaluation?
