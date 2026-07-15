---
id: REF-0034
title: Kernel Core Provisional Vocabulary and Status Map
status: Draft
version: 0.2.0-draft.2
layer: Reference
owner: Ming Foundation Kernel Architecture
created: 2026-07-15
updated: 2026-07-15
language: en
canonical_language: en
translation_status: original
decision_base_commit: 0397834984b9d9ad0e08a142dce2a98ed5b1a795
related:
  - KERNEL-0000
  - KERNEL-0001
  - REF-0031
  - REF-0032
  - REF-0033
depends_on:
  - KERNEL-0001
---

# REF-0034 — Kernel Core Provisional Vocabulary and Status Map

| ID | Term | Working meaning | Status |
|---|---|---|---|
| KVT-0001 | Person | A human being; never reducible to account, role, profile, record, or model output. | `Core semantic` |
| KVT-0002 | AffectedPerson | A person whose rights, welfare, identity, relationship, opportunity, or safety may be materially affected. | `Provisional` |
| KVT-0003 | Subject | The person, group, relationship, event, or object being described. | `Provisional` |
| KVT-0004 | Speaker | The source of a statement, observation, correction, or claim. | `Provisional` |
| KVT-0005 | Representative | A person acting for or with another person under scoped authority. | `Profile-dependent` |
| KVT-0006 | Operator | An actor initiating or controlling an operation or interface. | `Provisional` |
| KVT-0007 | AccountableHuman | A human responsible for a bounded decision or operation. | `Provisional` |
| KVT-0008 | AccountableOrganization | The entity responsible for governance, service, or a claim. | `Provisional` |
| KVT-0009 | AIComponent | A model or agent performing bounded generated, inferred, or execution functions. | `Provisional` |
| KVT-0010 | Purpose | The declared reason and allowed scope for an operation or data use. | `RFC-dependent` |
| KVT-0011 | AuthorityBasis | The documented basis that permits an action, role, or data operation. | `Profile/jurisdiction-dependent` |
| KVT-0012 | Consent | A scoped authority state where consent is the applicable basis; not a universal basis for all action. | `RFC-dependent` |
| KVT-0013 | Observation | A time- and source-bound record of what was perceived or measured. | `Provisional` |
| KVT-0014 | Statement | Content asserted by a speaker, distinct from verified fact. | `Provisional` |
| KVT-0015 | Inference | A derived interpretation that remains distinguishable from source records. | `Provisional` |
| KVT-0016 | Hypothesis | A testable or revisable possible explanation. | `Provisional` |
| KVT-0017 | Pattern | A proposed recurrence or relationship across records, not automatic causation. | `Provisional` |
| KVT-0018 | Judgment | A human or system evaluation under stated criteria and authority. | `Provisional` |
| KVT-0019 | Decision | A selection or authorization with consequences and accountability. | `Provisional` |
| KVT-0020 | Evidence | A source-linked record used to support or challenge a claim or decision. | `Provisional` |
| KVT-0021 | Confidence | A bounded assessment of support or uncertainty; never equivalent to truth. | `Open` |
| KVT-0022 | Unknown | A material absence, uncertainty, conflict, or unresolved question. | `Core semantic` |
| KVT-0023 | Memory | A retained record or derived state that can affect later operations. | `RFC-dependent` |
| KVT-0024 | Action | A proposed or executed change with actor, target, purpose, authority, and expected effects. | `Provisional` |
| KVT-0025 | Feedback | Observed or reported information about an action, state, interpretation, or outcome. | `Provisional` |
| KVT-0026 | Risk | A possible harmful consequence characterized by severity, likelihood, immediacy, uncertainty, and reversibility. | `RFC-dependent` |
| KVT-0027 | Incident | A suspected or confirmed harmful, unauthorized, or materially nonconforming event. | `RFC-dependent` |
| KVT-0028 | Appeal | A request for review, correction, suspension, or reversal of a material decision or record. | `RFC-dependent` |
| KVT-0029 | ServiceAvailability | Current evidence that a human, professional, emergency, or external resource can actually respond. | `Profile-dependent` |
| KVT-0030 | HighImpactOperation | A provisional category for operations with material rights, safety, identity, relationship, opportunity, or lasting consequence. | `Open` |

```text
TermDefined ≠ ObjectSchemaDefined
RoleNamed ≠ RoleAssigned
RequirementDrafted ≠ RequirementAccepted
ReviewPrepared ≠ ReviewExecuted
TestSpecified ≠ TestPassed
RepositoryValidated ≠ ImplementationConforming
```

Round 08 may revise, qualify, merge or reject these terms.
