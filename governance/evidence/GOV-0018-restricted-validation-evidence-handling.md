---
created: 2026-07-12
depends_on:
- GOV-0002
- GOV-0006
id: GOV-0018
layer: Layer 5 — Community & Governance
owner: Ming Foundation Governance
related:
- GOV-0002
- GOV-0014
- GOV-0016
- GOV-0017
- GOV-0019
- GOV-TPL-0002
- GOV-TPL-0003
- RFC-0002
- RFC-0004
status: Accepted
title: Restricted Validation Evidence Handling Protocol
updated: 2026-07-12
version: 1.0.0-alpha.6
---

# GOV-0018 — Restricted Validation Evidence Handling Protocol

## 1. Purpose

Charter validation may involve sensitive experience, family
relationships, child information, safety events, professional practice,
commercial conflicts, and criticism of identifiable people.

The public repository must preserve governance outcomes without
publishing unsafe raw evidence.

## 2. Evidence classes

### Public

Safe for the public repository.

Examples:

- protocol;
- aggregate finding;
- non-identifying objection;
- decision and rationale;
- remediation status.

### Restricted

Accessible only to approved reviewers for a defined purpose.

Examples:

- de-identified interview record;
- detailed implementation finding;
- confidential expert review;
- limited case excerpt.

### Highly restricted

Access limited to a small named group.

Examples:

- identifiable child or family information;
- active safety incident;
- legal advice;
- allegation involving a named person;
- credentials or security-sensitive evidence.

### Prohibited from collection

Evidence not necessary or safe for the validation purpose.

Examples:

- unrelated private case history;
- passwords or tokens;
- full medical record when a narrow excerpt suffices;
- identifiable content submitted merely for illustration.

## 3. Minimum handling record

Each restricted evidence item must record:

- evidence ID;
- class;
- purpose;
- subjects and affected people;
- source;
- steward;
- approved reviewers;
- storage location;
- retention and review date;
- permitted use;
- de-identification state;
- publication constraint;
- deletion or archival outcome.

## 4. Storage and access

Restricted evidence SHOULD use:

- storage separate from the public repository;
- encryption appropriate to sensitivity;
- named access;
- access logs;
- no public-link sharing;
- no personal-device copies unless governed;
- no model-provider upload without separate approval;
- expiration and access review.

## 5. De-identification

De-identification must consider direct and indirect identifiers.

The public summary should use the minimum detail necessary to explain:

- the issue;
- the affected commitment;
- the decision;
- the remediation;
- unresolved disagreement.

## 6. Reviewer use

A reviewer MUST NOT:

- reuse evidence for unrelated research;
- copy raw evidence into personal notes beyond the governed environment;
- publish or contact the subject independently;
- upload evidence to an external AI system without approval;
- attempt re-identification;
- retain evidence after access expires.

## 7. Withdrawal

Participants should be told:

- how to withdraw;
- which raw evidence can be deleted;
- whether already aggregated findings can be fully withdrawn;
- whether safety or legal exceptions apply;
- how a withdrawal is recorded.

Withdrawal must not erase a confirmed governance action that must remain
accountable, but the retained record should be minimized.

## 8. Public repository rule

The public repository may contain:

- evidence IDs;
- classification;
- aggregate finding;
- project response;
- status;
- limitations.

It MUST NOT contain:

- raw identifiable interview transcripts;
- private consultation or case records;
- active safety information;
- confidential legal advice;
- secrets or credentials;
- identifiable allegations without a lawful, reviewed basis.

## 9. Incident handling

Unauthorized access, loss, publication, or model upload of restricted
evidence must trigger:

- containment;
- steward notification;
- affected-person assessment;
- access revocation;
- incident record;
- remediation;
- recurrence review.

## 10. Acceptance tests

The evidence process must demonstrate:

1.  public and restricted stores are separated;
2.  each item has a purpose and steward;
3.  access expires;
4.  public summaries pass privacy review;
5.  an unauthorized export is detectable;
6.  withdrawal can be executed and evidenced;
7.  reviewer access can be revoked;
8.  no raw sensitive material is required to understand the public
    governance decision.
