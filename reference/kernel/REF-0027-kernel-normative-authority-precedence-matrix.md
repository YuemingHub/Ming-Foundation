---
id: REF-0027
title: MingOS Kernel Normative Authority and Precedence Matrix
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
  - ADR-0005
  - ADR-0026
  - MOS-0000
  - MF-0004
  - MF-0006
  - PROJECT-MINGOS-0002
  - PROJECT-MINGOS-0003
  - REF-0026
  - REF-0028
depends_on:
  - ADR-0026
---

# REF-0027 — MingOS Kernel Normative Authority and Precedence Matrix

## 1. No simple total order

Authority is determined by:

- source class;
- scope;
- document status;
- explicit dependency;
- version;
- applicable jurisdiction or Profile;
- recorded exception;
- conflict and supersession history.

A detailed lower-layer document is not automatically more authoritative than a
higher-layer commitment, and a higher-layer commitment is not automatically a
complete implementation instruction.

## 2. Source matrix

| Source class | Governs | May do | Must not do | Conflict route |
|---|---|---|---|---|
| Charter of Life | candidate higher-order ethical treatment of life | constrain all lower layers; expose ethical conflict | define product fields, code or complete runtime | Charter review and explicit revision |
| MingOS Charter | MingOS organizational and product self-restraint | constrain Kernel, business, AI, data and name use | claim implementation compliance without contracts and evidence | Charter governance and commitment-contract mapping |
| Accepted ADR | architecture, separation, authority and structural decisions | choose family structure, locations and precedence | replace substantive runtime standards or implementation evidence | new ADR or explicit supersession |
| MOS process | status lifecycle, document classes, review and evidence process | govern how standards change and advance | create substantive runtime obligations solely by process text | MOS revision |
| KERNEL core | integrated cross-implementation operational obligations | define common roles, invariants and delegated requirements | override either Charter or erase RFC/Profile sources | Kernel revision plus source conflict review |
| RFC | detailed protocol, state or message contract | define specific interoperable requirements | silently redefine Kernel common semantics or Charter rights | RFC/Kernel compatibility decision |
| Profile | bounded role, domain, service or jurisdiction qualification | narrow applicability and add context-specific constraints | weaken mandatory rights without explicit bounded authority | Profile review and exception record |
| Implementation | software, prompt, model, workflow, service and operations | choose replaceable mechanisms and provide evidence | become normative because it exists or is deployed | implementation remediation or standards proposal |
| Public communication | website, sales, content, interface and documentation | represent current governed claims | create authority or overstate status, capability or conformance | RFC-0005 and public-claims audit |
| Derived index/test | machine-readable registry, test spec and result | trace, verify and report source-linked requirements | replace, strengthen or weaken source text | regenerate from source and record discrepancy |

## 3. Status rules

### Draft

A documented proposal open to structural change. It cannot support a current
conformance claim.

### Proposed

A governed proposal that may guide review and design but does not prove
implementation conformance.

### Candidate

A coherent source prepared for broader validation. Candidate status does not
mean universally valid, fully enforceable or operationally implemented.

### Accepted architecture or governance record

An accepted decision or record governs its declared scope. It does not promote
dependent Draft, Proposed or Candidate documents.

### Stable standard

A future status requiring implementation evidence, conformance criteria,
documented limitations and completed review gates under `MOS-0000`.

## 4. Conflict handling

When two governed sources appear to conflict, record:

1. exact documents, versions and sections;
2. source class and status;
3. affected people, systems and claims;
4. whether the conflict is semantic, normative, jurisdictional, operational or
   implementation-specific;
5. the least harmful reversible interim behavior;
6. responsible reviewer and decision route;
7. migration and compatibility implications;
8. unresolved dissent.

No conflict may be resolved merely by choosing the newer file, the more
technical file, or the already-deployed implementation.

## 5. Precedence examples

- A Profile may require a shorter response time but cannot remove a data right
  established by an applicable higher source.
- An RFC may define a consent message contract but cannot redefine valid
  representative authority without explicit compatibility review.
- A Kernel test may detect a failure but cannot silently invent a requirement.
- A product may use a different storage engine if retention, correction,
  deletion, audit and evidence obligations remain satisfied.
- A public page cannot claim “Kernel conforming” while KERNEL-0004 and
  KERNEL-0005 do not exist.
