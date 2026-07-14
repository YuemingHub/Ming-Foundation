---
id: REF-0028
title: MingOS Kernel Conformance Replaceability and Claim Boundary
status: Draft
version: 0.1.0
layer: Reference
owner: Ming Foundation Architecture
created: 2026-07-14
updated: 2026-07-14
language: en
canonical_language: en
translation_status: original
decision_base_commit: 394f494f00ebfccf38572e3846cf6b6e3f699abf
related:
  - ADR-0026
  - RFC-0005
  - REF-0026
  - REF-0027
  - REF-0029
  - REF-0030
depends_on:
  - ADR-0026
---

# REF-0028 — MingOS Kernel Conformance Replaceability and Claim Boundary

## 1. Current result

```text
Kernel specifications created:       0
Kernel conformance requirements:      0
Kernel test specifications:           0
Kernel reference implementations:     0
Product Kernel assessments:           0
Current Kernel-conforming products:   0

Overall:
NoCurrentKernelConformanceClaim
```

## 2. Future conformance unit

A conformance claim must bind to a complete tuple:

```text
implementation_id
implementation_version
declared_boundary
kernel_version_set
applicable_rfc_versions
applicable_profile_versions
operating_context
jurisdiction
evidence_snapshot
exceptions_and_limitations
accountable_organization
accountable_human_role
assessment_result
expiry_or_review_condition
```

A claim cannot apply implicitly to:

- all products of an organization;
- all versions of a product;
- all prompts using a name;
- the MingOS brand;
- the repository;
- the website;
- an AI model family;
- future deployments.

## 3. Future assessment states

These names are reserved for design review and are not yet active:

- `NotAssessed`
- `AssessmentPrepared`
- `EvidenceIncomplete`
- `NonConforming`
- `ConformingCandidate`
- `Conforming`
- `Suspended`
- `Expired`
- `Withdrawn`

Only future KERNEL-0004 may define their exact semantics.

## 4. Replaceable mechanisms

| Mechanism | Default | Condition |
|---|---|---|
| model provider and model version | Replaceable | capability and limitation claims remain current |
| prompts and orchestration | Replaceable | requirements, provenance and accountability remain satisfied |
| UI, language and interaction pattern | Replaceable | access, correction, refusal and affected-person rights remain usable |
| database and storage engine | Replaceable | retention, deletion, backup, audit and evidence rules remain satisfied |
| programming language and framework | Replaceable | verification evidence remains available |
| hosting and deployment topology | Replaceable | privacy, safety, jurisdiction and service obligations remain satisfied |
| workflow and tool provider | Replaceable | role, authority and audit boundaries remain visible |
| domain method or curriculum | Replaceable/application-specific | it is not promoted into universal Kernel ontology |
| commercial and delivery channel | Replaceable | Charter commercial restraints remain satisfied |

## 5. Non-replaceable governed obligations for a claim

A future conforming implementation must not replace away:

- the distinction between person, subject, speaker and representative;
- scoped and evidenced authority;
- purpose and consent lifecycle;
- contestability and correction;
- knowledge-status separation;
- evidence, confidence, uncertainty and provenance;
- affected-person and third-party rights;
- safety, handoff, appeal and incident handling;
- memory inspection, correction, revocation, retention and deletion;
- human accountability and AI limits;
- failure, counterexample, unknown and revision records;
- audit and version traceability.

The exact requirements remain future work.

## 6. Claim language before Round 09

Allowed:

- “designed against current Candidate Charters and Proposed RFCs”;
- “mapping prepared”;
- “repository validation passed”;
- “synthetic scenario passed”;
- “Kernel scope decision proposed”;
- “implementation evidence not yet assessed.”

Not allowed:

- “Kernel compliant”;
- “MingOS certified”;
- “Charter compliant”;
- “safe by design” without a qualified bounded claim;
- “clinically validated”;
- “approved for children”;
- “affected-person reviewed”;
- “all requirements passed.”

## 7. Evidence separation

```text
repository validation
  ≠ implementation test

test specification
  ≠ test execution

synthetic execution
  ≠ human-use validation

partial evidence
  ≠ conformance

conformance at one version
  ≠ permanent conformance
```
