---
id: KERNEL-0001
title: MingOS Kernel Core Operational Contract
status: Draft
version: 0.2.1-draft.3
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
  - MF-0005
  - PROJECT-MINGOS-0002
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

> **Draft operational contract.** These 36 requirements are proposed, not
> implemented, reviewed externally, or conforming.

## 1. Purpose

Propose the smallest current cross-implementation obligations for MingOS
systems, agents, products, services, professional workflows and organizations.

## 2. Scope and non-goals

Applies as a design/review source to personal interpretation, data processing,
material recommendations/actions, AI or professional power, safety operations,
and MingOS capability claims. It does not define final schemas, state machines,
conformance levels, tests, certification, reference implementation, or a fixed
family/education/counseling method.

## 3. Definitions and normative language

Working terms are in REF-0034. `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT` and
`MAY` follow MOS-0000 exactly. Underscored aliases are not normative levels.
Draft wording requests review and does not establish current conformance.

## 4. Normative requirements

| ID | Domain | Level | Requirement | Scope | Source treatment | Exact source locators | Proposed verification methods | Expected evidence types | Delegated/future detail |
|---|---|---|---|---|---|---|---|---|---|
| KCR-0001 | BoundaryAndAccountability | `MUST` | An implementation boundary MUST identify its version, governed surfaces, accountable organization, and accountable human role. | `Core` | `CandidateConstraintOperationalization` | PROJECT-MINGOS-0002 §MC14 [CandidateProjectConstraint]; ADR-0026 §2.5 [ProposedArchitecture] | BoundaryDeclarationInspection; AccountabilityRoleReview | BoundaryRecord; RoleAssignmentRecord | KERNEL-0004 |
| KCR-0002 | VersionSet | `MUST` | A Kernel-governed operation MUST identify the applicable Kernel family version set and the status of each source. | `Core` | `ArchitectureDerivedProposal` | ADR-0026 §2.4 [ProposedArchitecture]; KERNEL-0000 §4 [CollectionLocalDraft] | VersionSetInspection; DependencyTrace | VersionSetDeclaration; SourceStatusSnapshot | KERNEL-0000 |
| KCR-0003 | SourceIntegrity | `MUST NOT` | A lower-layer artifact MUST NOT silently redefine a Charter, accepted architecture boundary, or authoritative source text. | `Core` | `ArchitectureDerivedProposal` | ADR-0005 §Dependency direction [AcceptedArchitecture]; ADR-0026 §2.3 [ProposedArchitecture] | SourceDiffReview; RedefinitionNegativeScenario | SourceBaseline; ConflictRecord | KERNEL-0000 |
| KCR-0004 | AffectedPersonIdentification | `MUST` | A material operation MUST identify people who may be affected even when they are not account holders or interface operators. | `Core` | `CandidateConstraintOperationalization` | PROJECT-MINGOS-0002 §MC10 [CandidateProjectConstraint]; REF-0029 §2 [DraftKernelReference] | AffectedPersonCoverageReview; NonUserImpactScenario | AffectedPersonRegister; ImpactAssessment | KERNEL-0002 |
| KCR-0005 | RoleSeparation | `MUST` | The system MUST preserve separations among affected person, subject, speaker, representative, operator, reviewer, accountable human, accountable organization, AI component, and service provider. | `Core` | `CrossSourceSynthesis` | RFC-0001 §3–6 [ProposedProtocol]; REF-0029 §2 [DraftKernelReference] | RoleGraphInspection; ConflictScenario | RoleAssignmentRecords; ConflictChecks | KERNEL-0002 |
| KCR-0006 | RepresentativeAuthority | `MUST` | Representative authority MUST be scoped, evidenced, purpose-bound, time-bounded, contestable, and revocable where applicable. | `Delegated` | `DelegatedProposedProtocolIntegration` | RFC-0001 §2.3 and §6 [ProposedProtocol]; PROF-0001 §4 and §8–9 [ProposedProfile]; PROF-0002 §2–5 and §8–11 [ProposedProfile]; PROJECT-MINGOS-0002 §MC10 [CandidateProjectConstraint] | AuthorityRecordInspection; RepresentativeConflictScenario | AuthorityEvidence; ScopeExpiryRecord | RFC-0001/PROF-0001/PROF-0002 |
| KCR-0007 | PurposeBeforeOperation | `MUST` | A personal-data or interpretive operation MUST record a legitimate declared purpose before collection, transformation, recommendation, disclosure, or reuse. | `Delegated` | `DelegatedProposedProtocolIntegration` | RFC-0002 §3 and §5.1 [ProposedProtocol]; PROJECT-MINGOS-0002 §MC04 [CandidateProjectConstraint] | PurposeTraceInspection; UnauthorizedUseScenario | PurposeRecord; OperationTrace | RFC-0002 |
| KCR-0008 | ConsentStatus | `MUST` | Where consent is the applicable authority basis, its scope, state, evidence, expiry, revocation, and exceptions MUST remain inspectable. | `Delegated` | `DelegatedProposedProtocolIntegration` | RFC-0002 §4–5 and §7 [ProposedProtocol]; MF-0004 §C04 [CandidateCharterConstraint] | AuthorityLifecycleTrace; RevocationScenario | AuthorityBasisRecord; RevocationTrace | RFC-0002/KERNEL-0003 |
| KCR-0009 | RefusalBoundary | `MUST NOT` | Refusal, silence, withdrawal, or disagreement MUST NOT be treated as failure, resistance, consent, or proof that an interpretation is correct. | `Core` | `CandidateConstraintOperationalization` | PROJECT-MINGOS-0002 §MC03 [CandidateProjectConstraint]; MF-0004 §C04 [CandidateCharterConstraint]; PROF-0001 §8 [ProposedProfile] | RefusalNegativeScenario; UsabilityReview | InteractionTrace; AdverseOutcomeReview | KERNEL-0001 |
| KCR-0010 | ContestabilityAndCorrection | `MUST` | A materially affected person MUST have a usable path to inspect, contest, correct, contextualize, and appeal significant interpretation or decision records. | `Delegated` | `DelegatedProposedProtocolIntegration` | RFC-0001 §7 and §9 [ProposedProtocol]; PROJECT-MINGOS-0002 §MC03 and §MC13 [CandidateProjectConstraint] | RightsRouteReview; CorrectionPropagationTrace | RightsRequestRecord; UpdateTrace | RFC-0001/KERNEL-0003 |
| KCR-0011 | ThirdPartyMinimization | `MUST` | Third-party and non-user information MUST be purpose-limited, minimized, access-controlled, and protected from unlimited representative disclosure. | `Delegated` | `DelegatedProposedProtocolIntegration` | PROJECT-MINGOS-0002 §MC10 [CandidateProjectConstraint]; RFC-0002 §3 and §5.4 [ProposedProtocol]; RFC-0004 §2–7 [ProposedProtocol] | DataFlowInspection; ThirdPartyDisclosureScenario | DataInventory; AccessAudit | RFC-0002/RFC-0004 |
| KCR-0012 | KnowledgeStatusSeparation | `MUST` | Fact, observation, statement, inference, hypothesis, pattern, judgment, recommendation, and decision MUST remain distinguishable. | `Core` | `CrossSourceSynthesis` | PROJECT-MINGOS-0002 §MC06 [CandidateProjectConstraint]; RFC-0001 §3–5 [ProposedProtocol] | SchemaInspection; KnowledgeTransitionScenario | KnowledgeItemRecords; StatusHistory | KERNEL-0002 |
| KCR-0013 | Provenance | `MUST` | A significant knowledge item MUST preserve source, speaker, subject, time, context, transformation history, and applicable authority. | `Core` | `CrossSourceSynthesis` | RFC-0001 §3–4 and §9 [ProposedProtocol]; PROJECT-MINGOS-0002 §MC05–MC06 [CandidateProjectConstraint] | LineageInspection; SourceLossScenario | ProvenanceGraph; TransformationHistory | KERNEL-0002 |
| KCR-0014 | UncertaintyAndUnknown | `MUST` | A significant inference MUST preserve uncertainty, limitations, unresolved alternatives, and unknowns; confidence MUST NOT be represented as truth. | `Core` | `CrossSourceSynthesis` | MF-0004 §C09 [CandidateCharterConstraint]; PROJECT-MINGOS-0002 §MC05–MC06 [CandidateProjectConstraint]; RFC-0001 §4.3 and §5 [ProposedProtocol] | UncertaintyReview; OverconfidenceScenario | InferenceRecord; UnknownRecord | KERNEL-0002 |
| KCR-0015 | ContradictionAndCounterexample | `MUST` | Contradictions, corrections, failures, counterexamples, dissent, and superseded interpretations MUST remain traceable subject to privacy and safety controls. | `Core` | `CrossSourceSynthesis` | PROJECT-MINGOS-0002 §MC05 and §MC13 [CandidateProjectConstraint]; RFC-0004 §5 [ProposedProtocol]; RFC-0001 §9 [ProposedProtocol] | ContradictionTrace; CounterexampleRetentionReview | DissentRecord; SupersessionHistory | KERNEL-0002 |
| KCR-0016 | ObservationBeforeAdvice | `SHOULD` | The system SHOULD gather and distinguish relevant observation, context, uncertainty, and affected-person perspective before offering consequential advice. | `Core` | `NewProposalInformedByDraftInterpretation` | ADR-0002 §Decision [AcceptedArchitecture]; MF-0005 §29–30 [DraftInterpretiveInput] | AdviceTraceReview; ImmediateGuidanceExceptionScenario | ObservationRecord; AdviceDecisionTrace | KERNEL-0001 |
| KCR-0017 | RelationshipAndTimelineContext | `SHOULD` | Consequential interpretation SHOULD preserve relevant relationship, sequence, change over time, and structural or material context without assuming that context proves causation. | `Core` | `NewProposalInformedByDraftInterpretation` | MF-0005 §10, §26 and §29–30 [DraftInterpretiveInput]; REF-0014 §Kernel-boundary candidates [DraftHistoricalReference] | ContextCoverageReview; CausationOverreachScenario | RelationshipRecord; EventTimeline | KERNEL-0002 |
| KCR-0018 | UserChosenAction | `SHOULD` | A proposed action SHOULD preserve meaningful choice and identify whose goal, need, and authority the action serves. | `Core` | `NewProposalInformedByDraftInterpretation` | MF-0005 §18 and §20–21 [DraftInterpretiveInput]; PROJECT-MINGOS-0002 §MC01 and §MC03 [CandidateProjectConstraint] | ChoiceAuthorityReview; CoercionScenario | ActionProposal; UserChoiceRecord | KERNEL-0001 |
| KCR-0019 | SmallSafeReversibleAction | `SHOULD` | When uncertainty or impact is material, the system SHOULD prefer the smallest reasonably safe, reversible, observable action. | `Core` | `NewProposalInformedByDraftInterpretation` | MF-0005 §15 and §41–42 [DraftInterpretiveInput]; PROJECT-MINGOS-0002 §S05–S06 [CandidateProjectConstraint] | ReversibilityReview; HighUncertaintyScenario | ActionPlan; RollbackRecord | KERNEL-0001 |
| KCR-0020 | AffectedImpactReview | `MUST` | Before a high-impact operation, the system MUST identify affected people, foreseeable consequences, alternatives, reversibility, notice, correction, appeal, and review conditions. | `Core` | `CandidateConstraintOperationalization` | PROJECT-MINGOS-0002 §MC09–MC10 [CandidateProjectConstraint]; REF-0029 §5 [DraftKernelReference]; RFC-0001 §2.2 [ProposedProtocol] | HighImpactGateInspection; AffectedPersonReview | ImpactAssessment; ReviewAppealPlan | KERNEL-0003 |
| KCR-0021 | NoHiddenPersuasion | `MUST NOT` | The system MUST NOT use hidden persuasion, anxiety, shame, dependency, urgency, or vulnerability to obtain consent, compliance, purchase, retention, or disclosure. | `Core` | `NewProposalInformedByDraftInterpretation` | PROJECT-MINGOS-0002 §MC07–MC08 [CandidateProjectConstraint]; RFC-0005 §6–8 [ProposedProtocol]; MF-0005 §47–49 [DraftInterpretiveInput] | InteractionAudit; DarkPatternScenario | MessageTrace; CommercialConflictReview | KERNEL-0001 |
| KCR-0022 | RiskRecognition | `MUST` | A system operating in a domain with foreseeable serious harm MUST define risk recognition, uncertainty, escalation, stop, and incident-recording behavior. | `Delegated` | `DelegatedProposedProtocolIntegration` | RFC-0003 §2–6 [ProposedProtocol]; PROJECT-MINGOS-0002 §MC11 [CandidateProjectConstraint] | RiskScenarioTrace; StopEscalationInspection | RiskSignal; RiskAssessment | RFC-0003/KERNEL-0003 |
| KCR-0023 | CapabilityBoundary | `MUST` | Current capability, professional status, jurisdiction, service availability, limitations, and unavailable functions MUST be represented honestly. | `Delegated` | `DelegatedProposedProtocolIntegration` | RFC-0003 §3 and §7 [ProposedProtocol]; RFC-0005 §3 and §8 [ProposedProtocol]; PROF-0004 §1–5 and §8 [ProposedProfile] | CapabilityClaimAudit; UnavailableServiceScenario | CapabilityStatusRecord; AvailabilityEvidence | RFC-0003/RFC-0005/PROF-0004 |
| KCR-0024 | HandoffAvailability | `MUST NOT` | Generating a referral, resource, message, or link MUST NOT be represented as a completed handoff unless availability and completion evidence support that claim. | `Delegated` | `DelegatedProposedProtocolIntegration` | RFC-0003 §3, §4.3 and §6 [ProposedProtocol]; PROF-0004 §1, §8 and §11 [ProposedProfile] | HandoffLifecycleTrace; SentMessageScenario | HandoffRecord; AcceptanceEvidence | RFC-0003/PROF-0004 |
| KCR-0025 | AppealAndIncident | `MUST` | A material adverse decision or failure MUST have a traceable appeal, incident, containment, review, correction, and follow-up path appropriate to its scope. | `Delegated` | `DelegatedProposedProtocolIntegration` | RFC-0003 §4.5, §6 and §8 [ProposedProtocol]; PROJECT-MINGOS-0002 §MC13–MC14 [CandidateProjectConstraint] | IncidentAppealTrace; DifferentReviewerCheck | IncidentRecord; AppealRecord | RFC-0003/KERNEL-0003 |
| KCR-0026 | EmergencyIntervention | `MUST` | An emergency or protective intervention MUST be lawful where applicable, necessary, proportionate, purpose-limited, time-bounded where possible, reviewable, and distinct from consent. | `Core` | `CandidateConstraintOperationalization` | MF-0004 §C04 [CandidateCharterConstraint]; PROJECT-MINGOS-0002 §MC03 [CandidateProjectConstraint]; RFC-0003 §5 and §9 [ProposedProtocol] | ProportionalityReview; EmergencyExceptionScenario | ProtectiveActionRecord; IndependentReview | KERNEL-0003 |
| KCR-0027 | MemoryInspectionCorrection | `MUST` | A person materially represented in memory MUST have an applicable path to inspect, correct, contextualize, contest, and identify significant downstream effects. | `Delegated` | `DelegatedProposedProtocolIntegration` | RFC-0002 §5.5 and §7–9 [ProposedProtocol]; PROJECT-MINGOS-0002 §MC04 [CandidateProjectConstraint] | MemoryRightsReview; CorrectionImpactTrace | MemoryRecord; PropagationEvidence | RFC-0002/KERNEL-0003 |
| KCR-0028 | MemoryRevocationRetentionDeletion | `MUST` | Memory authority, revocation, retention, deletion, backup exceptions, access, and completion evidence MUST be represented explicitly. | `Delegated` | `DelegatedProposedProtocolIntegration` | RFC-0002 §6–9 [ProposedProtocol]; PROF-0003 §1–5 and §7–11 [ProposedProfile] | RetentionDeletionTrace; BackupRestoreScenario | RetentionProfile; CompletionEvidence | RFC-0002/PROF-0003/KERNEL-0003 |
| KCR-0029 | NoPermanentVulnerabilityProfile | `MUST NOT` | Temporary distress, vulnerability, conflict, diagnosis, risk, or limitation MUST NOT become an unreviewable permanent identity or commercial profile. | `Core` | `NewProposalInformedByDraftInterpretation` | PROJECT-MINGOS-0002 §MC04 and §MC07 [CandidateProjectConstraint]; MF-0005 §37–40 and §48 [DraftInterpretiveInput] | ProfilePersistenceAudit; CrisisExpiryScenario | ProfileHistory; ExpiryEvidence | KERNEL-0002 |
| KCR-0030 | SecondaryUseDisclosure | `MUST` | Secondary use, cross-context inference, model or system improvement, research, analytics, and training use MUST have a disclosed authority basis, purpose, data boundary, retention rule, and refusal or exception path. | `Delegated` | `DelegatedProposedProtocolIntegration` | RFC-0002 §3–4 and §10–11 [ProposedProtocol]; RFC-0004 §6 [ProposedProtocol]; MF-0005 §40 and §51–54 [DraftInterpretiveInput] | SecondaryUseReview; TrainingReuseScenario | SecondaryUseRecord; AuthorityEvidence | RFC-0002/RFC-0004 |
| KCR-0031 | AIIdentityCapabilityLimits | `MUST` | An AI component MUST expose its role, relevant provider or model version, capabilities, limitations, generated or inferred status, and significant provenance. | `Core` | `ArchitectureDerivedProposal` | ADR-0001 §Decision [AcceptedArchitecture]; PROJECT-MINGOS-0002 §MC09 [CandidateProjectConstraint]; RFC-0005 §8 [ProposedProtocol] | AIProvenanceInspection; RoleImpersonationScenario | ComponentManifest; GeneratedContentTrace | KERNEL-0002 |
| KCR-0032 | HumanAccountability | `MUST` | A high-impact decision MUST identify a human and organization with sufficient information, authority, independence, stop capacity, and review responsibility. | `Core` | `CandidateConstraintOperationalization` | PROJECT-MINGOS-0002 §MC09 and §MC14 [CandidateProjectConstraint]; REF-0029 §5 [DraftKernelReference]; ADR-0001 §Decision [AcceptedArchitecture] | AccountabilityReview; HumanInNameOnlyScenario | AccountableRoleRecord; StopAuthorityEvidence | KERNEL-0002 |
| KCR-0033 | AffectedPersonParticipation | `MUST` | A high-impact design or decision MUST define how affected-person participation, refusal, representation, accessibility, and situations where participation is unsafe or impossible are handled. | `Core` | `CandidateConstraintOperationalization` | PROJECT-MINGOS-0002 §MC09–MC10 [CandidateProjectConstraint]; PROF-0001 §1–5 and §7–10 [ProposedProfile] | ParticipationProtocolReview; ParticipationImpossibleScenario | ParticipationRecord; AccessibilityEvidence | KERNEL-0002 |
| KCR-0034 | FeedbackAndStateRevision | `MUST` | Observed outcome, affected-person feedback, correction, failure, and new evidence MUST be able to revise relevant state without erasing prior provenance. | `Core` | `CrossSourceSynthesis` | PROJECT-MINGOS-0002 §MC13 [CandidateProjectConstraint]; MF-0004 §C09 [CandidateCharterConstraint]; RFC-0001 §9 [ProposedProtocol]; RFC-0002 §8–9 [ProposedProtocol] | FeedbackRevisionTrace; OutcomeFailureScenario | FeedbackRecord; RevisionTrace | KERNEL-0003 |
| KCR-0035 | AuditVersionFailureUnknown | `MUST` | Material operations MUST preserve audit, version, source, decision, exception, failure, counterexample, dissent, and unknown records according to applicable privacy and safety controls. | `Core` | `NewProposalInformedByDraftInterpretation` | PROJECT-MINGOS-0002 §MC05, §MC13 and §MC14 [CandidateProjectConstraint]; RFC-0004 §2–7 [ProposedProtocol]; MF-0005 §54 [DraftInterpretiveInput] | AuditCompletenessReview; FailureUnknownTrace | AuditEvent; UnknownRegister | KERNEL-0002 |
| KCR-0036 | NoPrematureConformanceClaim | `MUST NOT` | No product, organization, model, prompt, workflow, or repository MUST be described as Kernel conforming before applicable conformance requirements, tests, evidence, review, exceptions, and claim-expiry rules exist and are satisfied. | `Core` | `ArchitectureDerivedProposal` | ADR-0026 §2.5 [ProposedArchitecture]; REF-0028 §1–7 [DraftKernelReference]; RFC-0005 §2–6 [ProposedProtocol] | PublicClaimAudit; MissingEvidenceScenario | ClaimRecord; BoundaryStatement | KERNEL-0004/KERNEL-0005 |

## 5. Data and process model

```text
Declare boundary/version set
→ identify affected people, roles, authority, purpose and participation
→ collect minimum source-linked observation
→ represent knowledge status, evidence, uncertainty and context
→ classify impact/risk and required review
→ propose options without hidden coercion
→ authorize through accountable human/organization where required
→ execute, hand off, stop or decline
→ observe outcome, feedback, correction, appeal and incident
→ revise active state while preserving provenance
```

This is an abstract process, not a UI flow or final state machine.

## 6. Human agency and ethics

The contract MUST preserve refusal, correction, participation, choice,
explanation, appeal and leaving. Safety does not authorize unlimited control;
agency does not remove responsibility for consequences and others' rights.
People must not be reduced to accounts, narratives, scores or permanent profiles.

## 7. Privacy, consent and memory

Personal and third-party data MUST be purpose-limited, minimized, source-linked,
access-controlled and retention-governed. Consent is one authority basis, not a
universal label. Mandatory or protective action MUST NOT be described as freely
given consent. Memory requires correction, restriction, revocation, retention,
deletion, backup and propagation handling.

## 8. Safety and escalation

Serious foreseeable harm requires risk recognition, uncertainty, named
responsibility, proportionality, stop and escalation. A generated referral is
not a completed handoff. AI cannot be final accountable actor for high-impact
decisions.

## 9. Review and future conformance criteria

Review evaluates source fidelity, normative level, scope, source treatment,
implementation-neutral verification, evidence risks, affected-person rights,
open ambiguity and compatibility with future KERNEL documents. Product
conformance cannot be assessed before KERNEL-0004/0005 and executed evidence.

## 10. Non-normative examples

- A parent's statement remains attributed to the parent, not a child's fact.
- A generated resource remains Initiated until availability/acceptance evidence.
- A correction revises active interpretation while preserving prior provenance.

## 11. Limitations and open questions

REF-0032 contains 30 open items, including high-impact thresholds,
representative authority, confidence, emergency action, deletion, unavailable
services and organization-level obligations. Validation cannot resolve them.

## 12. Version and change history

| Version | Date | Change | Status |
|---|---|---|---|
| 0.1.0-draft.1 | 2026-07-15 | Initial 36-item contract | Draft |
| 0.2.0-draft.2 | 2026-07-15 | MOS completeness, exact levels, source treatment and verification/evidence mapping | Draft |

## 13. Current boundary

```text
KERNEL-0000/0001: Draft / 0.2.0-draft.2
KERNEL-0002: Draft / 0.1.0-draft.1
KERNEL-0003: Draft / 0.1.0-draft.1
KERNEL-0004..0005: not created
External review: not executed
Implementation assessment: not executed
Current conforming products: 0
Overall: NoCurrentKernelConformanceClaim
```

## 14. Round 08 integration note

KERNEL-0002/0003 provide Draft objects and lifecycles without resolving KCR ambiguities or changing KCR wording.
