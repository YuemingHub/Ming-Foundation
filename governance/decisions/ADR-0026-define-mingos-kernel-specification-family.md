---
id: ADR-0026
title: Define MingOS Kernel as a Governed Specification Family
status: Proposed
version: 0.1.0
layer: Cross-layer
owner: Ming Foundation Architecture
created: 2026-07-14
updated: 2026-07-14
language: en
canonical_language: en
translation_status: original
decision_base_commit: 394f494f00ebfccf38572e3846cf6b6e3f699abf
related:
  - ADR-0005
  - ADR-0010
  - ADR-0020
  - ADR-0021
  - ADR-0022
  - ADR-0023
  - MOS-0000
  - MF-0004
  - MF-0006
  - PROJECT-MINGOS-0002
  - PROJECT-MINGOS-0003
  - GOV-0082
  - REF-0014
  - REF-0019
  - REF-0023
  - REF-0026
  - REF-0027
  - REF-0028
  - REF-0029
  - REF-0030
depends_on:
  - ADR-0005
  - MOS-0000
  - PROJECT-MINGOS-0002
---

# ADR-0024 — Define MingOS Kernel as a Governed Specification Family

> **Proposed scope and authority decision.**
>
> This ADR does not create the Kernel core specification, data model, state
> machines, conformance suite, reference implementation, or a current claim of
> Kernel conformance.

## 1. Context

`ADR-0005` separates the Charter of Life, the MingOS Charter, and the MingOS
Kernel. It defines the Kernel as the operational layer containing protocols,
data models, state transitions, safety gates, tests, review loops, incident
handling, runtime behavior, and implementation conformance.

The repository now also contains:

- Candidate English and Chinese versions of both Charters;
- Proposed RFC-0001 through RFC-0005;
- Proposed PROF-0001 through PROF-0004;
- a Draft standards process in `MOS-0000`;
- Day 16 review-operation and controlled-pilot governance;
- historical methods and possible Kernel objects in `REF-0014`;
- no complete Kernel specification;
- no current product or implementation that may claim Kernel conformance.

A single undifferentiated Kernel document would mix durable common obligations,
data structures, lifecycle machines, conformance claims, and test artifacts.
It would also make replaceable implementation mechanisms appear immutable.

## 2. Decision

### 2.1 The Kernel is a specification family

MingOS Kernel SHALL be governed as a versioned specification family, not as:

- a single system prompt;
- a model personality;
- a product repository;
- a counseling or consulting script;
- a fixed software package;
- a brand metaphor;
- a copy of historical Family OS code;
- a single monolithic document.

The family will integrate common operational obligations while preserving
separate documents for objects, lifecycles, conformance requirements, and tests.

### 2.2 Repository location and identifier namespace

The governed location is:

```text
standards/kernel/
```

The reserved identifier namespace is:

```text
KERNEL-0000 through KERNEL-0005
```

Reservation does not create a document or confer status.

The planned family is:

| ID | Planned artifact | Planned round | Normative role |
|---|---|---:|---|
| KERNEL-0000 | Specification Family Index and Lifecycle | Round 07 | family entry point, version set, dependencies and change map |
| KERNEL-0001 | Core Operational Contract | Round 07 | common mandatory runtime obligations and shared semantics |
| KERNEL-0002 | Canonical Object and Data Model | Round 08 | governed objects, identifiers, provenance and relationship rules |
| KERNEL-0003 | Lifecycle and State Machines | Round 08 | consent, memory, safety, appeal, remediation and revision lifecycles |
| KERNEL-0004 | Conformance Requirements and Evidence Classes | Round 09 | claim unit, mandatory requirements, evidence and exception rules |
| KERNEL-0005 | Test Specifications and Derived Indexes | Round 09 | test cases, requirement indexes and reference verification artifacts |

### 2.3 Normative boundary

The following source classes remain distinct:

1. **The Charter of Life** — higher-order ethical constraints.
2. **MingOS Charter** — MingOS-specific organizational and product
   self-restraints.
3. **Accepted architecture decisions** — boundaries, authority and structural
   decisions.
4. **MOS process** — lifecycle and review process for standards; it does not
   create substantive runtime requirements by itself.
5. **Kernel family** — integrated cross-implementation operational obligations.
6. **RFCs** — detailed protocols and message or lifecycle contracts referenced
   by the Kernel.
7. **Profiles** — bounded domain, role, service or jurisdiction qualifications.
8. **Implementations** — replaceable software, prompts, models, workflows and
   services.
9. **Public communication** — representations that must map to governed sources
   but cannot create normative authority.
10. **Derived machine indexes and tests** — synchronized artifacts whose source
    text remains authoritative.

No lower layer may silently redefine a higher layer. A conflict must be
recorded, reviewed, and resolved through the process appropriate to the
affected source.

### 2.4 Status-aware authority

Authority is not determined by document type alone.

- Draft and Proposed documents do not establish a current implementation
  conformance claim.
- A lower-status detailed document cannot be presented as overriding a
  higher-layer commitment.
- Candidate Charters remain governing constraints for design and review, while
  their unresolved ambiguities and incomplete validation remain visible.
- Accepted ADRs may define architecture and authority boundaries but do not
  substitute for runtime specifications.
- Kernel requirements may only become claimable according to the lifecycle and
  evidence gates defined by the standards process and future KERNEL documents.

### 2.5 Kernel conformance

Kernel conformance SHALL apply to a declared, versioned implementation
boundary, not to an entire organization, product family, brand, model, or
repository by implication.

A future claim must identify at least:

- implementation and version;
- deployed boundary and surfaces;
- Kernel family version set;
- applicable RFCs and Profiles;
- jurisdiction or operating context;
- evidence date and evidence classes;
- unresolved exceptions and limitations;
- accountable organization and human role;
- conformance result and expiry or review condition.

Until KERNEL-0004 and KERNEL-0005 exist and have appropriate status and
evidence:

```text
NoCurrentKernelConformanceClaim
```

Repository validation, a synthetic pilot, or passing a future test
specification alone SHALL NOT prove product conformance.

### 2.6 Replaceability boundary

Replaceable mechanisms include, unless a future requirement explicitly
constrains them:

- model provider and model version;
- prompts and orchestration;
- user interface and visual design;
- storage engine and deployment topology;
- programming language and framework;
- workflow engine and tool provider;
- specific family, education or consulting methods;
- business and delivery channel;
- implementation-specific names and enumerations.

A conforming implementation may replace those mechanisms only while preserving
the applicable governed obligations, including:

- subject, speaker and affected-person separation;
- representative authority evidence;
- consent, purpose and contestability;
- fact, observation, inference, judgment and decision separation;
- provenance, evidence, uncertainty and revision;
- safety, handoff, appeal and incident handling;
- memory inspection, correction, revocation, retention and deletion;
- human accountability and bounded AI roles;
- affected-person participation;
- audit, failure, counterexample and unknown preservation.

### 2.7 Role representation

The Kernel family must represent roles separately from people, accounts,
devices, sessions or models.

At minimum it must be possible to distinguish:

- affected person;
- subject;
- speaker;
- representative;
- operator;
- practitioner or professional;
- reviewer;
- accountable human;
- accountable organization;
- AI component;
- service or resource provider;
- evidence custodian.

The same person may hold multiple roles only when the combination, scope,
authority, conflict and time boundary are recorded.

AI may assist, infer, propose, summarize or execute bounded operations. AI is
not the final accountable actor for high-impact decisions and cannot silently
stand in for an affected person, representative, professional, reviewer or
responsible organization.

### 2.8 Relationship to Day 16 operations

Day 16 review-operation controls remain a parallel workstream.

```text
Role defined            ≠ Kernel role assigned
Protocol designed       ≠ Kernel protocol accepted
Synthetic pilot passed  ≠ Kernel conformance
Repository test passed  ≠ product conformance
```

Round 06 does not authorize CP2 or CP3, assign operational roles, approve human
use, or create live evidence environments.

## 3. Consequences

### Positive

- durable commitments remain separate from replaceable mechanisms;
- future Kernel documents receive explicit IDs and locations;
- object, lifecycle and conformance work can evolve without becoming a
  monolith;
- RFC and Profile roles become clearer;
- implementation and public claims gain an explicit non-conformance boundary;
- AI, human and affected-person roles cannot be silently collapsed.

### Costs

- the project must maintain version-set compatibility across several documents;
- cross-document traceability and migration become mandatory;
- no single file can be treated as the whole Kernel;
- conformance requires evidence beyond repository validation;
- Round 07 through Round 09 remain substantial work.

## 4. Alternatives considered

### A single Kernel specification

Rejected because core obligations, data models, state machines and test
artifacts have different change rates and review needs.

### Existing RFCs are the Kernel

Rejected because current RFCs cover important protocols but do not define the
integrated operational order, version set, role model or conformance claim.

### Existing Family OS code is the Kernel

Rejected because historical implementation is evidence, not authority.

### A system prompt is the Kernel

Rejected because prompts are replaceable implementation artifacts and cannot
carry full governance, data rights, safety, audit or conformance authority.

### Kernel as an organizational operating manual

Rejected because the Kernel governs operational behavior across systems,
agents, products and services; organizational procedures may implement it but
do not exhaust it.

## 5. Non-goals for Round 06

This round does not:

- write KERNEL-0000 through KERNEL-0005;
- define canonical objects or fields;
- define lifecycle state transitions;
- create a conformance test suite;
- claim any product or organization conforms;
- promote RFCs, Profiles, Charters, MOS-0000 or this ADR;
- activate human review;
- modify the Day 17 stage or repository version.

## 6. Follow-up

1. Round 07 drafts KERNEL-0000 and KERNEL-0001.
2. Round 08 drafts KERNEL-0002 and KERNEL-0003.
3. Round 09 drafts KERNEL-0004 and KERNEL-0005.
4. Existing RFC and Profile requirements are mapped rather than copied without
   traceability.
5. Historical methods remain application or evidence candidates unless they
   pass the cross-scene Kernel admission criteria.
6. Public claims remain `NoCurrentKernelConformanceClaim` until future gates
   are satisfied.
