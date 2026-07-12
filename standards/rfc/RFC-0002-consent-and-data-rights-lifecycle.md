---
created: 2026-07-12
depends_on:
  - MF-0004
  - PROJECT-MINGOS-0002
  - RFC-0001
  - ADR-0013
id: RFC-0002
layer: Layer 1 — Standards
owner: Ming Foundation Standards
related:
  - MF-0004
  - PROJECT-MINGOS-0002
  - GOV-0010
  - GOV-0018
  - GOV-0038
  - GOV-0044
  - GOV-0046
  - GOV-0048
  - ADR-0013
  - ADR-0014
status: Proposed
title: Consent and Data Rights Lifecycle Protocol
updated: 2026-07-12
version: 0.2.0-draft.1
---

# RFC-0002 — Consent and Data Rights Lifecycle Protocol

## Status

Proposed revised draft. This revision implements `REV-0005` through
`REV-0008` and the applicable R0 decisions from `ADR-0013`.

It does not claim legal compliance in every jurisdiction or current product
conformance.

## 1. Problem

Consent cannot be a single permanent checkbox.

Data may move through public forms, parent interfaces, human-support
workflows, safety records, family profiles, cases, summaries, analysis
systems, model evaluation, backups, and audit logs.

Without a lifecycle protocol, purpose, authority, rights, retention,
correction, and deletion become fragmented.

## 2. Jurisdiction and basis boundary

This RFC defines technical governance categories, not universal legal bases.

Every implementation MUST declare a jurisdiction profile that identifies:

- applicable operating locations;
- asserted legal or professional bases and qualified reviewer;
- age and representative rules;
- rights and response obligations;
- retention and deletion constraints;
- safeguarding and mandatory-disclosure duties;
- unresolved or conflicting requirements;
- review date and owner.

Where the jurisdiction profile is absent, expired, or uncertain, the
implementation MUST NOT claim that processing is lawful merely because it
matches a technical category in this RFC.

## 3. Core rule

Every material collection or use MUST have a traceable basis containing:

- subject;
- operator;
- purpose;
- technical processing-basis category;
- jurisdiction qualification where claimed;
- data scope;
- access scope;
- processing or use;
- retention profile;
- review point;
- revocation, objection, or rights route;
- representative authority where applicable;
- exception basis and review where relevant.

“Future improvement,” “unknown future value,” or “the data already exists”
is not a sufficient purpose.

## 4. Processing-basis categories

An implementation MUST distinguish at least:

- explicit optional permission;
- requested service operation;
- safety or protection operation;
- mandatory institutional or legal operation;
- security, fraud, or incident operation;
- separately approved research, validation, or evaluation use;
- unknown or disputed basis.

These are technical categories. A jurisdiction profile MUST state whether and
how a category maps to a lawful or professional basis.

Mandatory, emergency, safety, or institutional processing MUST NOT be
misrepresented as freely given consent.

## 5. Required records

### 5.1 Purpose definition

Minimum fields:

- `purpose_id`;
- `name`;
- `description`;
- `affected_people`;
- `data_categories`;
- `allowed_operations`;
- `recipients`;
- `processing_basis_categories`;
- `jurisdiction_profile`;
- `retention_profile`;
- `risk_class`;
- `review_owner`;
- `status`.

### 5.2 Permission or processing basis

Minimum fields:

- `basis_id`;
- `person_or_representative`;
- `representative_authority_ref`;
- `purpose_id`;
- `basis_category`;
- `jurisdiction_qualification`;
- `scope`;
- `version`;
- `recorded_at`;
- `expires_or_reviews_at`;
- `withdrawal_or_objection_method`;
- `constraints`;
- `exception_basis`;
- `evidence_of_notice`;
- `conflict_status`.

### 5.3 Representative authority

Minimum fields:

- `authority_id`;
- `representative`;
- `subject`;
- `representative_type`;
- `authority_source_or_evidence`;
- `permitted_actions`;
- `prohibited_actions`;
- `conflicts_of_interest`;
- `starts_at`;
- `expires_or_reviews_at`;
- `subject_notice_or_reason_for_delay`;
- `independent_review_route`.

Age or family role alone MUST NOT create unlimited authority.

A conflict, disputed authority, or high-impact request MUST route to a
conflict-free reviewer.

### 5.4 Data asset inventory

Minimum fields:

- `asset_id`;
- `subjects`;
- `source`;
- `data_category`;
- `sensitivity`;
- `storage_locations`;
- `purposes`;
- `authorized_roles`;
- `retention_profile`;
- `deletion_dependencies`;
- `backup_handling`;
- `derived_asset_refs`;
- `exportability`;
- `audit_refs`.

### 5.5 Rights request

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
- representative authority evidence;
- conflict check;
- scope;
- identity verification;
- received time;
- responsible owner;
- status;
- data located;
- derived and backup locations;
- exceptions;
- decision;
- completion evidence;
- independent or different-reviewer route;
- appeal route.

## 6. Retention profiles

Every asset MUST map to a named retention profile.

A retention profile MUST state:

- purpose;
- covered data;
- storage and backup locations;
- access roles;
- start event;
- review interval;
- deletion, archival, or anonymization trigger;
- backup-deletion or cryptographic-erasure handling;
- exception categories;
- exception owner;
- maximum exception period or mandatory review;
- completion evidence;
- appeal or independent-review route where appropriate.

At minimum, implementations SHOULD distinguish:

- transient intake;
- active service;
- safety or incident;
- security and audit;
- restricted validation evidence;
- public or permanently published record.

This RFC does not prescribe one universal duration. Each duration MUST be
defined and justified in the jurisdiction and service profile.

Indefinite retention for unspecified improvement MUST NOT be permitted.

## 7. Rights lifecycle

```text
Purpose proposed
  ↓
Risk, jurisdiction, and affected-person review
  ↓
Notice and permission or basis recorded
  ↓
Minimum data collected
  ↓
Use, sharing, derivation, and access logged
  ↓
Periodic purpose, authority, and retention review
  ↓
Correction / restriction / export / deletion / objection
  ↓
Propagation to dependent and backup processes
  ↓
Completion or narrowly justified exception
  ↓
Evidence, different-reviewer route, and appeal
```

## 8. Cross-channel authority and conflict resolution

An implementation MAY use a centralized, federated, or hybrid identity,
permission, memory, and audit architecture.

It MUST maintain an explicit authority map that identifies which system or
role is authoritative for:

- identity linkage;
- active purpose;
- permission and withdrawal;
- subject correction;
- representative authority;
- retention profile;
- audit and incident evidence.

When channels conflict:

1. a verified subject correction supersedes an inference or third-party
   assertion as the current interpretation, without deleting history;
2. the most restrictive current instruction governs optional use while the
   conflict is reviewed;
3. an unresolved identity or authority conflict freezes expansion, sharing,
   training, or high-impact use;
4. safety or mandatory exceptions require a specific basis, minimum scope,
   named actor, and review point;
5. correction, withdrawal, and deletion events MUST propagate across linked
   channels and derived assets;
6. a channel-specific record MUST NOT become an untraceable shadow profile.

## 9. Migration, lineage, and completion

Imported data MUST preserve:

- original source and collection context where known;
- original purpose and basis where known;
- transformation and migration steps;
- current and historical authority;
- derived assets and dependent decisions;
- unresolved uncertainty;
- rollback or remediation limits.

A rights request is not complete until active primary, derived, indexed,
shared, and scheduled backup handling has been addressed or a narrow
exception is recorded.

## 10. Public forms

General early-access or contact forms SHOULD:

- minimize fields;
- state purpose and retention profile;
- state who receives the information;
- identify automated and human follow-up;
- provide a rights request route;
- prohibit identifiable child, medical, crisis, or private consultation
  details unless a separately governed secure intake exists;
- avoid pre-checked optional permissions;
- separate newsletter, research, product access, and consultation purposes.

## 11. Prohibited behavior

An implementation MUST NOT:

- collect sensitive child cases through a general marketing field without a
  governed basis;
- reuse case data for model training merely because it exists;
- scatter data so broadly that rights cannot propagate;
- retain data indefinitely for unspecified improvement;
- hide a retention exception inside general terms;
- call an emergency or mandatory process voluntary consent;
- provide staff access broader than the active purpose;
- treat family role as unlimited representative authority;
- resolve channel conflicts by silently choosing the most permissive record;
- delete only the visible record while retaining active copies elsewhere.

## 12. Acceptance tests

A conforming implementation must demonstrate:

1. every data category maps to an active purpose, technical basis,
   jurisdiction profile, and retention profile;
2. missing jurisdiction qualification prevents a universal lawfulness claim;
3. representative authority is evidenced, scoped, conflict-checked, and
   expiring;
4. revoked optional use stops across channels and derived processes;
5. a verified correction propagates without erasing history;
6. an unresolved cross-channel conflict freezes expanded or high-impact use;
7. deletion addresses primary, derived, indexed, shared, and backup handling;
8. a retained exception records basis, scope, owner, review, and appeal;
9. public lead data cannot be accessed as a counseling case;
10. an appeal routes to a different or conflict-free responsible reviewer.

## 13. Remaining review questions

- Which jurisdiction profiles are required for the first reference
  implementations?
- Which retention-profile durations require external legal or professional
  review?
- Which rights requests may be safely automated?
- Which representative-authority evidence is proportionate for different
  impact classes?
