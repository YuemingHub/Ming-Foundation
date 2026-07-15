---
id: KERNEL-0001
title: MingOS Kernel Core Operational Contract
status: Draft
version: 0.1.0-draft.1
layer: Layer 2 — Standards
owner: Ming Foundation Kernel Architecture
created: 2026-07-15
updated: 2026-07-15
language: en
canonical_language: en
translation_status: original
decision_base_commit: 0397834984b9d9ad0e08a142dce2a98ed5b1a795
related:
  - MF-0004
  - MF-0006
  - PROJECT-MINGOS-0002
  - PROJECT-MINGOS-0003
  - ADR-0001
  - ADR-0002
  - ADR-0005
  - ADR-0026
  - MOS-0000
  - RFC-0001
  - RFC-0002
  - RFC-0003
  - RFC-0004
  - RFC-0005
  - PROF-0001
  - PROF-0002
  - PROF-0003
  - PROF-0004
  - KERNEL-0000
  - REF-0031
  - REF-0032
  - REF-0033
  - REF-0034
depends_on:
  - KERNEL-0000
  - ADR-0026
  - MOS-0000
---

# KERNEL-0001 — MingOS Kernel Core Operational Contract

> **Draft operational contract for review.**
>
> These requirements are not an implementation-conformance claim. Detailed
> RFCs and Profiles remain Proposed. Required object models, state machines,
> conformance rules and tests do not yet exist.

## 1. Purpose

KERNEL-0001 defines the smallest current cross-implementation operational
obligation set proposed for MingOS systems, agents, products, services,
professional workflows and organizations.

It answers:

> What minimum behavior must remain visible and governable before a mechanism
> can later be evaluated as part of a MingOS Kernel implementation?

## 2. Scope

This Draft applies as a design and review source to operations that:

- represent or interpret a person, relationship, event, state or need;
- collect, retain, transform, infer, disclose or reuse personal information;
- recommend or execute actions with material consequences;
- involve AI, professional, representative, safety or organizational power;
- make claims about MingOS capability, safety, review or conformance.

It does not make all obligations identical for every context. Applicability,
jurisdiction, role, service and domain qualifications remain future Profile and
conformance work.

## 3. Normative language

`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT` and `MAY` follow `MOS-0000`.

Because this document is Draft:

- normative wording requests review of the proposed obligation;
- it does not establish current product conformance;
- unresolved ambiguities remain open;
- source conflicts must not be hidden.

## 4. Core requirements

| ID | Domain | Level | Requirement | Primary sources | Type | Delegated or future detail |
|---|---|---|---|---|---|---|
| KCR-0001 | BoundaryAndAccountability | `MUST` | An implementation boundary MUST identify its version, governed surfaces, accountable organization, and accountable human role. | PROJECT-MINGOS-0002:MC14; ADR-0026:2.5 | `Core` | KERNEL-0004 |
| KCR-0002 | VersionSet | `MUST` | A Kernel-governed operation MUST identify the applicable Kernel family version set and the status of each source. | ADR-0026:2.4; KERNEL-0000:4 | `Core` | KERNEL-0000 |
| KCR-0003 | SourceIntegrity | `MUST_NOT` | A lower-layer artifact MUST NOT silently redefine a Charter, accepted architecture boundary, or authoritative source text. | ADR-0005:Dependency direction; ADR-0026:2.3 | `Core` | KERNEL-0000 |
| KCR-0004 | AffectedPersonIdentification | `MUST` | A material operation MUST identify people who may be affected even when they are not account holders or interface operators. | PROJECT-MINGOS-0002:MC10; REF-0029:2 | `Core` | KERNEL-0002 |
| KCR-0005 | RoleSeparation | `MUST` | The system MUST preserve separations among affected person, subject, speaker, representative, operator, reviewer, accountable human, accountable organization, AI component, and service provider. | RFC-0001; REF-0029:2 | `Core` | KERNEL-0002 |
| KCR-0006 | RepresentativeAuthority | `MUST` | Representative authority MUST be scoped, evidenced, purpose-bound, time-bounded, contestable, and revocable where applicable. | PROF-0001; PROF-0002; PROJECT-MINGOS-0002:MC10 | `Delegated` | RFC-0001/PROF-0001/PROF-0002 |
| KCR-0007 | PurposeBeforeOperation | `MUST` | A personal-data or interpretive operation MUST record a legitimate declared purpose before collection, transformation, recommendation, disclosure, or reuse. | RFC-0002; PROJECT-MINGOS-0002:MC04 | `Delegated` | RFC-0002 |
| KCR-0008 | ConsentStatus | `MUST` | Where consent is the applicable authority basis, its scope, state, evidence, expiry, revocation, and exceptions MUST remain inspectable. | RFC-0002; MF-0004:C04 | `Delegated` | RFC-0002/KERNEL-0003 |
| KCR-0009 | RefusalBoundary | `MUST_NOT` | Refusal, silence, withdrawal, or disagreement MUST NOT be treated as failure, resistance, consent, or proof that an interpretation is correct. | PROJECT-MINGOS-0002:MC03; MF-0004:C04 | `Core` | KERNEL-0001 |
| KCR-0010 | ContestabilityAndCorrection | `MUST` | A materially affected person MUST have a usable path to inspect, contest, correct, contextualize, and appeal significant interpretation or decision records. | RFC-0001; PROJECT-MINGOS-0002:MC03/MC13 | `Delegated` | RFC-0001/KERNEL-0003 |
| KCR-0011 | ThirdPartyMinimization | `MUST` | Third-party and non-user information MUST be purpose-limited, minimized, access-controlled, and protected from unlimited representative disclosure. | PROJECT-MINGOS-0002:MC10; RFC-0002; RFC-0004 | `Delegated` | RFC-0002/RFC-0004 |
| KCR-0012 | KnowledgeStatusSeparation | `MUST` | Fact, observation, statement, inference, hypothesis, pattern, judgment, recommendation, and decision MUST remain distinguishable. | PROJECT-MINGOS-0002:MC06; RFC-0001 | `Core` | KERNEL-0002 |
| KCR-0013 | Provenance | `MUST` | A significant knowledge item MUST preserve source, speaker, subject, time, context, transformation history, and applicable authority. | RFC-0001; PROJECT-MINGOS-0002:MC05/MC06 | `Core` | KERNEL-0002 |
| KCR-0014 | UncertaintyAndUnknown | `MUST` | A significant inference MUST preserve uncertainty, limitations, unresolved alternatives, and unknowns; confidence MUST NOT be represented as truth. | MF-0004:C09; PROJECT-MINGOS-0002:MC05/MC06 | `Core` | KERNEL-0002 |
| KCR-0015 | ContradictionAndCounterexample | `MUST` | Contradictions, corrections, failures, counterexamples, dissent, and superseded interpretations MUST remain traceable subject to privacy and safety controls. | PROJECT-MINGOS-0002:MC05/MC13; RFC-0004 | `Core` | KERNEL-0002 |
| KCR-0016 | ObservationBeforeAdvice | `SHOULD` | The system SHOULD gather and distinguish relevant observation, context, uncertainty, and affected-person perspective before offering consequential advice. | ADR-0002; MF-0005 | `Core` | KERNEL-0001 |
| KCR-0017 | RelationshipAndTimelineContext | `SHOULD` | Consequential interpretation SHOULD preserve relevant relationship, sequence, change over time, and structural or material context without assuming that context proves causation. | MF-0005; REF-0014 | `Core` | KERNEL-0002 |
| KCR-0018 | UserChosenAction | `SHOULD` | A proposed action SHOULD preserve meaningful choice and identify whose goal, need, and authority the action serves. | MF-0005; PROJECT-MINGOS-0002:MC01/MC03 | `Core` | KERNEL-0001 |
| KCR-0019 | SmallSafeReversibleAction | `SHOULD` | When uncertainty or impact is material, the system SHOULD prefer the smallest reasonably safe, reversible, observable action. | MF-0005; PROJECT-MINGOS-0002:S05/S06 | `Core` | KERNEL-0001 |
| KCR-0020 | AffectedImpactReview | `MUST` | Before a high-impact operation, the system MUST identify affected people, foreseeable consequences, alternatives, reversibility, notice, correction, appeal, and review conditions. | PROJECT-MINGOS-0002:MC09/MC10; REF-0029:5 | `Core` | KERNEL-0003 |
| KCR-0021 | NoHiddenPersuasion | `MUST_NOT` | The system MUST NOT use hidden persuasion, anxiety, shame, dependency, urgency, or vulnerability to obtain consent, compliance, purchase, retention, or disclosure. | PROJECT-MINGOS-0002:MC07/MC08; RFC-0005 | `Core` | KERNEL-0001 |
| KCR-0022 | RiskRecognition | `MUST` | A system operating in a domain with foreseeable serious harm MUST define risk recognition, uncertainty, escalation, stop, and incident-recording behavior. | RFC-0003; PROJECT-MINGOS-0002:MC11 | `Delegated` | RFC-0003/KERNEL-0003 |
| KCR-0023 | CapabilityBoundary | `MUST` | Current capability, professional status, jurisdiction, service availability, limitations, and unavailable functions MUST be represented honestly. | RFC-0003; RFC-0005; PROF-0004 | `Delegated` | RFC-0003/RFC-0005/PROF-0004 |
| KCR-0024 | HandoffAvailability | `MUST_NOT` | Generating a referral, resource, message, or link MUST NOT be represented as a completed handoff unless availability and completion evidence support that claim. | RFC-0003; PROF-0004 | `Delegated` | RFC-0003/PROF-0004 |
| KCR-0025 | AppealAndIncident | `MUST` | A material adverse decision or failure MUST have a traceable appeal, incident, containment, review, correction, and follow-up path appropriate to its scope. | RFC-0003; PROJECT-MINGOS-0002:MC13/MC14 | `Delegated` | RFC-0003/KERNEL-0003 |
| KCR-0026 | EmergencyIntervention | `MUST` | An emergency or protective intervention MUST be lawful where applicable, necessary, proportionate, purpose-limited, time-bounded where possible, reviewable, and distinct from consent. | MF-0004:C04; PROJECT-MINGOS-0002:MC03 | `Core` | KERNEL-0003 |
| KCR-0027 | MemoryInspectionCorrection | `MUST` | A person materially represented in memory MUST have an applicable path to inspect, correct, contextualize, contest, and identify significant downstream effects. | RFC-0002; PROJECT-MINGOS-0002:MC04 | `Delegated` | RFC-0002/KERNEL-0003 |
| KCR-0028 | MemoryRevocationRetentionDeletion | `MUST` | Memory authority, revocation, retention, deletion, backup exceptions, access, and completion evidence MUST be represented explicitly. | RFC-0002; PROF-0003 | `Delegated` | RFC-0002/PROF-0003/KERNEL-0003 |
| KCR-0029 | NoPermanentVulnerabilityProfile | `MUST_NOT` | Temporary distress, vulnerability, conflict, diagnosis, risk, or limitation MUST NOT become an unreviewable permanent identity or commercial profile. | PROJECT-MINGOS-0002:MC04/MC07; MF-0005 | `Core` | KERNEL-0002 |
| KCR-0030 | SecondaryUseDisclosure | `MUST` | Secondary use, cross-context inference, model or system improvement, research, analytics, and training use MUST have a disclosed authority basis, purpose, data boundary, retention rule, and refusal or exception path. | RFC-0002; RFC-0004; MF-0005 | `Delegated` | RFC-0002/RFC-0004 |
| KCR-0031 | AIIdentityCapabilityLimits | `MUST` | An AI component MUST expose its role, relevant provider or model version, capabilities, limitations, generated or inferred status, and significant provenance. | ADR-0001; PROJECT-MINGOS-0002:MC09; RFC-0005 | `Core` | KERNEL-0002 |
| KCR-0032 | HumanAccountability | `MUST` | A high-impact decision MUST identify a human and organization with sufficient information, authority, independence, stop capacity, and review responsibility. | PROJECT-MINGOS-0002:MC09/MC14; REF-0029 | `Core` | KERNEL-0002 |
| KCR-0033 | AffectedPersonParticipation | `MUST` | A high-impact design or decision MUST define how affected-person participation, refusal, representation, accessibility, and situations where participation is unsafe or impossible are handled. | PROJECT-MINGOS-0002:MC09/MC10; PROF-0001 | `Core` | KERNEL-0002 |
| KCR-0034 | FeedbackAndStateRevision | `MUST` | Observed outcome, affected-person feedback, correction, failure, and new evidence MUST be able to revise relevant state without erasing prior provenance. | PROJECT-MINGOS-0002:MC13; MF-0004:C09 | `Core` | KERNEL-0003 |
| KCR-0035 | AuditVersionFailureUnknown | `MUST` | Material operations MUST preserve audit, version, source, decision, exception, failure, counterexample, dissent, and unknown records according to applicable privacy and safety controls. | PROJECT-MINGOS-0002:MC05/MC13/MC14; RFC-0004 | `Core` | KERNEL-0002 |
| KCR-0036 | NoPrematureConformanceClaim | `MUST_NOT` | No product, organization, model, prompt, workflow, or repository MUST be described as Kernel conforming before applicable conformance requirements, tests, evidence, review, exceptions, and claim-expiry rules exist and are satisfied. | ADR-0026:2.5; REF-0028 | `Core` | KERNEL-0004/KERNEL-0005 |

## 5. Requirement interpretation rules

1. A requirement applies only within a declared boundary and applicable context.
2. A source citation does not automatically make every source sentence a
   KERNEL requirement.
3. A delegated requirement remains governed by its RFC/Profile source.
4. A summary MUST NOT strengthen or weaken its source.
5. Candidate Charter ambiguity MUST remain visible.
6. A missing human service MUST NOT be hidden by generated language.
7. An exception MUST identify authority, scope, purpose, affected people,
   evidence, duration, review and appeal.
8. Safety does not authorize unlimited surveillance or control.
9. Agency does not remove responsibility for consequences and other people's
   rights.
10. Human-in-the-loop does not prove meaningful human accountability.

## 6. Organizational applicability

Where applicable, an accountable organization MUST:

- assign owners for governed obligations;
- prevent commercial goals from silently overriding the Charters;
- preserve reporting, appeal, incident, correction and audit routes;
- represent current capability and service availability honestly;
- prevent AI output from becoming unowned organizational action;
- support suspension when credible evidence indicates serious harm;
- preserve affected-person and minority views;
- maintain version, migration and public-claim traceability.

Exact organizational conformance remains future work.

## 7. AI boundary

An AI component MAY summarize, infer, generate, classify, retrieve, recommend,
or execute bounded operations only within declared capability, authority,
purpose, provenance, review and accountability constraints.

An AI component MUST NOT:

- impersonate an affected person, representative, professional, reviewer, or
  accountable human;
- claim final authority over identity, meaning, diagnosis or life direction;
- hide that content is generated or inferred;
- exploit vulnerability, dependence, fear, urgency or shame;
- convert missing human review into simulated approval;
- represent a generated handoff as completed service;
- erase source uncertainty or disagreement;
- become the final accountable actor for a high-impact decision.

## 8. Affected-person boundary

A materially affected person must not be reduced to:

- an account owner;
- the current speaker;
- a parent or representative's narrative;
- a professional interpretation;
- an AI-generated profile;
- a risk score;
- a behavior target;
- a training or growth resource.

Participation, refusal, correction, accessibility, representation and situations
where direct participation is unsafe or impossible require explicit handling.

## 9. Safety and non-domination

The core principle is:

```text
Safety without domination.
Agency without abandonment.
```

Protective action must be bounded by necessity, proportionality, purpose,
evidence, time, review and affected-person rights where applicable.

The absence of complete information may require slowing, limiting, stopping or
escalating rather than producing a confident answer.

## 10. Evidence and revision

The Kernel must support revision when confronted by:

- affected-person correction;
- contradictory evidence;
- failed outcome;
- counterexample;
- changed context;
- expired authority;
- unavailable service;
- incident or appeal;
- source revision;
- unknown or dissent.

Revision must preserve prior provenance rather than silently rewriting history.

## 11. Explicit exclusions

This Draft does not define:

- canonical object fields;
- database schemas;
- final role or participation enums;
- consent, memory, safety or appeal state machines;
- high-impact thresholds;
- confidence calculation;
- conformance levels;
- certification;
- test cases;
- reference implementation;
- a fixed counseling, parenting or educational method.

## 12. Current conformance boundary

```text
KERNEL-0001 status:               Draft
KERNEL-0002 through 0005:         not created
Formal external review:           not executed
Implementation assessment:        not executed
Current conforming products:      0

Overall:
NoCurrentKernelConformanceClaim
```

## 13. Open questions

The open questions and blockers in REF-0032 remain part of this Draft's review
scope. They must not be represented as resolved by repository validation.
