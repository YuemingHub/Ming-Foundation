---
id: REF-0034
title: Kernel Core Provisional Vocabulary and Status Map
status: Draft
version: 0.1.0-draft.1
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

> This is not the final object model. Terms marked Provisional, Open,
> RFC-dependent or Profile-dependent remain review inputs for Round 08.

## 1. Vocabulary

| Term | Working meaning | Status |
|---|---|---|
| Person | A human being; never reducible to account, role, profile, record, or model output. | `Core semantic` |
| AffectedPerson | A person whose rights, welfare, identity, relationship, opportunity, or safety may be materially affected. | `Provisional` |
| Subject | The person, group, relationship, event, or object being described. | `Provisional` |
| Speaker | The source of a statement, observation, correction, or claim. | `Provisional` |
| Representative | A person acting for or with another person under scoped authority. | `Profile-dependent` |
| Operator | An actor initiating or controlling an operation or interface. | `Provisional` |
| AccountableHuman | A human responsible for a bounded decision or operation. | `Provisional` |
| AccountableOrganization | The entity responsible for governance, service, or a claim. | `Provisional` |
| AIComponent | A model or agent performing bounded generated, inferred, or execution functions. | `Provisional` |
| Purpose | The declared reason and allowed scope for an operation or data use. | `RFC-dependent` |
| AuthorityBasis | The documented basis that permits an action, role, or data operation. | `Profile/jurisdiction-dependent` |
| Consent | A scoped authority state where consent is the applicable basis; not a universal basis for all action. | `RFC-dependent` |
| Observation | A time- and source-bound record of what was perceived or measured. | `Provisional` |
| Statement | Content asserted by a speaker, distinct from verified fact. | `Provisional` |
| Inference | A derived interpretation that remains distinguishable from source records. | `Provisional` |
| Hypothesis | A testable or revisable possible explanation. | `Provisional` |
| Pattern | A proposed recurrence or relationship across records, not automatic causation. | `Provisional` |
| Judgment | A human or system evaluation under stated criteria and authority. | `Provisional` |
| Decision | A selection or authorization with consequences and accountability. | `Provisional` |
| Evidence | A source-linked record used to support or challenge a claim or decision. | `Provisional` |
| Confidence | A bounded assessment of support or uncertainty; never equivalent to truth. | `Open` |
| Unknown | A material absence, uncertainty, conflict, or unresolved question. | `Core semantic` |
| Memory | A retained record or derived state that can affect later operations. | `RFC-dependent` |
| Action | A proposed or executed change with actor, target, purpose, authority, and expected effects. | `Provisional` |
| Feedback | Observed or reported information about an action, state, interpretation, or outcome. | `Provisional` |
| Risk | A possible harmful consequence characterized by severity, likelihood, immediacy, uncertainty, and reversibility. | `RFC-dependent` |
| Incident | A suspected or confirmed harmful, unauthorized, or materially nonconforming event. | `RFC-dependent` |
| Appeal | A request for review, correction, suspension, or reversal of a material decision or record. | `RFC-dependent` |
| ServiceAvailability | Current evidence that a human, professional, emergency, or external resource can actually respond. | `Profile-dependent` |
| HighImpactOperation | A provisional category for operations with material rights, safety, identity, relationship, opportunity, or lasting consequence. | `Open` |

## 2. Status distinctions

```text
TermDefined
  ≠ ObjectSchemaDefined

RoleNamed
  ≠ RoleAssigned

RequirementDrafted
  ≠ RequirementAccepted

ReviewPrepared
  ≠ ReviewExecuted

TestSpecified
  ≠ TestPassed

RepositoryValidated
  ≠ ImplementationConforming
```

## 3. Round 08 handoff

Round 08 must decide:

- object identifiers and references;
- role-assignment representation;
- provenance and derivation links;
- temporal and relationship models;
- authority and consent records;
- memory and evidence objects;
- lifecycle state machines;
- compatibility and migration;
- privacy and access boundaries;
- which candidate enums remain implementation-specific.

Cultural metaphors and domain-specific methods must not become universal object
types without explicit admission review.
