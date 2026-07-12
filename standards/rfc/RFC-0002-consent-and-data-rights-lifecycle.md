---
created: 2026-07-12
depends_on:
- MF-0004
- PROJECT-MINGOS-0002
- RFC-0001
id: RFC-0002
layer: Layer 1 — Standards
owner: Ming Foundation Standards
related:
- MF-0004
- PROJECT-MINGOS-0002
- GOV-0010
- GOV-0014
- GOV-0018
- GOV-0019
- ADR-0007
status: Proposed
title: Consent and Data Rights Lifecycle Protocol
updated: 2026-07-12
version: 0.1.0
---

# RFC-0002 — Consent and Data Rights Lifecycle Protocol

## Status

Proposed minimum protocol. It does not assert that current products
already conform.

## 1. Problem

Consent cannot be a single permanent checkbox.

Data can move through:

- public website forms;
- parent interfaces;
- H5 and enterprise WeChat channels;
- human-support workflows;
- safety records;
- family profiles;
- cases and summaries;
- analysis and model-evaluation systems;
- backups and audit logs.

Without a lifecycle protocol, purpose, rights, and retention become
fragmented.

## 2. Core rule

Every material collection or use MUST have a traceable basis containing:

- subject;
- operator;
- purpose;
- data scope;
- access scope;
- processing or use;
- retention rule;
- review point;
- revocation or objection route;
- exception basis where relevant.

“Future improvement” or “unknown future value” is not a sufficient
purpose.

## 3. Required records

### 3.1 Purpose definition

Minimum fields:

- `purpose_id`;
- `name`;
- `description`;
- `affected_people`;
- `data_categories`;
- `allowed_operations`;
- `recipients`;
- `retention_rule`;
- `risk_class`;
- `review_owner`;
- `status`.

### 3.2 Permission or processing basis

Minimum fields:

- `grant_id`;
- `person_or_representative`;
- `purpose_id`;
- `scope`;
- `version`;
- `granted_at`;
- `expires_or_reviews_at`;
- `withdrawal_method`;
- `constraints`;
- `exception_basis`;
- `evidence_of_notice`.

The protocol uses “permission or processing basis” because not every
lawful or safety-sensitive operation is ordinary consent.
Implementations MUST not mislabel mandatory or emergency processing as
freely given consent.

### 3.3 Data asset inventory

Minimum fields:

- `asset_id`;
- `subjects`;
- `source`;
- `data_category`;
- `sensitivity`;
- `storage_locations`;
- `purposes`;
- `authorized_roles`;
- `retention_rule`;
- `deletion_dependencies`;
- `backup_handling`;
- `exportability`;
- `audit_refs`.

### 3.4 Rights request

Supported request types SHOULD include:

- access;
- source explanation;
- correction;
- contextualization;
- restriction;
- objection;
- export;
- deletion;
- withdrawal;
- review of automated or high-impact interpretation;
- appeal.

Minimum fields:

- requester;
- represented subject if any;
- scope;
- identity or authority verification;
- received time;
- responsible owner;
- status;
- data located;
- exceptions;
- decision;
- completion evidence;
- appeal route.

## 4. Lifecycle

``` text
Purpose proposed
  ↓
Risk and affected-person review
  ↓
Notice and permission/basis recorded
  ↓
Minimum data collected
  ↓
Use and access logged
  ↓
Periodic purpose and retention review
  ↓
Correction / restriction / export / deletion request
  ↓
Completion or narrowly justified exception
  ↓
Evidence and appeal
```

## 5. Retention and deletion

A retention rule MUST state:

- why the data is kept;
- which data is kept;
- where it is kept;
- who can access it;
- when it is reviewed;
- what causes deletion or archival;
- how backups are handled;
- whether a restricted exception applies.

Exceptions based on safety, legal duty, incident investigation, fraud
prevention, or protection of others MUST be:

- specific;
- minimally scoped;
- access-restricted;
- time- or review-bounded;
- explained to the requester where safe and lawful;
- appealable or independently reviewable where appropriate.

## 6. Cross-channel identity

All MingOS channels SHOULD resolve to a governed identity, permission,
memory, and audit layer.

A channel-specific local record MUST NOT become an untraceable shadow
profile.

Required controls include:

- stable person and family identifiers;
- channel linkage with authorization;
- duplicate and conflict handling;
- purpose propagation;
- revocation propagation;
- deletion propagation;
- audit continuity;
- separation of public lead data from service and case data.

## 7. Public forms

General early-access or contact forms SHOULD:

- minimize fields;
- state purpose and retention;
- state who receives the information;
- provide a request/contact route;
- prohibit submission of identifiable child, medical, crisis, or private
  consultation details unless a separately governed secure intake
  exists;
- avoid pre-checked optional permissions;
- distinguish newsletter, research contact, product access, and
  consultation requests.

## 8. Prohibited behavior

An implementation MUST NOT:

- collect sensitive child cases through a general marketing field
  without a governed basis;
- reuse case data for model training merely because it exists;
- scatter data so broadly that correction or deletion is impossible;
- retain data indefinitely for unspecified improvement;
- hide a retention exception inside general terms;
- call an emergency or mandatory process voluntary consent;
- provide staff broader access than their current purpose requires;
- delete only the visible record while silently retaining active copies
  elsewhere.

## 9. Acceptance tests

A conforming implementation must demonstrate:

1.  every stored data category maps to at least one active purpose;
2.  a revoked optional purpose stops future use across channels;
3.  an access request returns data source, purpose, status, and storage
    scope;
4.  correction preserves revision history without preserving a false
    current interpretation;
5.  deletion reaches primary stores, derived indexes, and scheduled
    backup handling;
6.  a retained exception records its basis and next review;
7.  public lead data cannot be accessed as if it were a counseling case;
8.  staff access is purpose- and role-limited;
9.  an appeal can be routed to a different responsible reviewer.

## 10. Open questions

- Which permissions must be separate rather than bundled?
- How should representative authority be verified?
- What data should be portable in a first implementation?
- What retention periods are justified for safety, cases, and audit?
- Which requests can be automated and which require human review?
