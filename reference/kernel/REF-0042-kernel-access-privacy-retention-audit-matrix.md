---
id: REF-0042
title: Kernel Access Privacy Retention and Audit Boundary Matrix
status: Draft
version: 0.2.0-draft.2
layer: Reference
owner: Ming Foundation Kernel Privacy
created: 2026-07-15
updated: 2026-07-15
language: en
canonical_language: en
translation_status: original
decision_base_commit: f3905710db2304ab926c4ab31e10264931539f98
related:
  - KERNEL-0002
  - KERNEL-0003
depends_on:
  - KERNEL-0002
---

# REF-0042 — Kernel Access Privacy Retention and Audit Boundary Matrix

| ID | Class | Scope | Access rule | Prohibited default |
|---|---|---|---|---|
| KAC-00 | PublicGoverned | Approved public normative/governance or aggregate content | Public under publication/correction controls | No raw identifiable personal or restricted evidence |
| KAC-10 | InternalGoverned | Non-public operational/architecture records without sensitive personal detail | Named governed roles | No public or unrelated staff access |
| KAC-20 | RestrictedPersonal | Personal, relationship, interpretation, memory and rights records | Purpose- and role-bound access | No marketing, unrestricted analytics or general model training |
| KAC-30 | RestrictedSafety | Risk, safeguarding, safety action, incident and protected-source records | Need-to-know safety roles with independent review | No unnecessary representative/operator disclosure |
| KAC-40 | RestrictedEvidence | Review, validation, qualification and identity evidence | Approved evidence environment and custodian | No public repository, sales, personalization or unrelated reuse |
| KAC-50 | SecretCredential | Secrets, tokens, private keys and authentication material | Dedicated secret-management systems | Never ordinary Kernel object content |

Field-level classification may be stricter than its object. Audit does not authorize full-content duplication.
