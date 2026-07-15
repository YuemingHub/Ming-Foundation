---
id: KERNEL-0003
title: MingOS Kernel Lifecycle and State Machines
status: Draft
version: 0.1.0-draft.1
layer: Layer 2 — Standards
owner: Ming Foundation Kernel Architecture
created: 2026-07-15
updated: 2026-07-15
language: en
canonical_language: en
translation_status: original
decision_base_commit: a0b8234567c211896085f0e1259b96bcb53effd1
related:
  - ADR-0026
  - MOS-0000
  - KERNEL-0000
  - KERNEL-0001
  - KERNEL-0002
  - RFC-0001
  - RFC-0002
  - RFC-0003
  - PROF-0001
  - PROF-0002
  - PROF-0003
  - PROF-0004
  - REF-0035
  - REF-0036
  - REF-0037
  - REF-0038
  - REF-0039
depends_on:
  - KERNEL-0000
  - KERNEL-0001
  - KERNEL-0002
---

# KERNEL-0003 — MingOS Kernel Lifecycle and State Machines

> **Draft lifecycle model.** States are governance semantics, not identity
> labels, diagnoses, or proof of safety or conformance.

## 1. Purpose

Propose state and transition semantics for authority, participation, knowledge,
decision/action, data/memory rights, safety/handoff, incident/appeal/remediation
and resource availability.

## 2. Scope and non-goals

Defines allowed distinctions, transition envelopes and cross-lifecycle
invariants. It does not prescribe workflow software, UI, response times, legal
conclusions, automatic decisions, final conformance tests or reference
implementation.

## 3. Definitions

A lifecycle is governed states and transitions. A transition is append-oriented.
A guard is required before transition. A freeze prohibits expansion/high-impact
use. Completion means active, derived, shared and backup effects are addressed
or narrowly excepted.

## 4. Normative lifecycle requirements

| ID | Domain | Level | Requirement |
|---|---|---|---|
| KLS-0001 | TransitionEnvelope | `MUST` | Every transition MUST record lifecycle/version, object, previous/new state, actor/component, role, authority, purpose, reason, evidence, uncertainty, affected people, time, review/expiry and audit. |
| KLS-0002 | NoSilentTransition | `MUST NOT` | A material object MUST NOT change state without an append-oriented transition record. |
| KLS-0003 | CurrentHistorySeparation | `MUST` | Current state and transition history MUST remain separately inspectable. |
| KLS-0004 | AllowedTransitions | `MUST` | An implementation MUST reject or explicitly exception-record a transition not allowed by the applicable lifecycle. |
| KLS-0005 | ActorAuthority | `MUST` | A material transition MUST identify responsible actor, role and authority scope. |
| KLS-0006 | AIBoundary | `MUST NOT` | An AI component MUST NOT be the final accountable authorizer of a high-impact transition. |
| KLS-0007 | ReviewExpiry | `MUST` | Active authority, participation, knowledge, resource, exception and safety states MUST support review or expiry. |
| KLS-0008 | StateNotIdentity | `MUST NOT` | A lifecycle state MUST NOT become a permanent identity, maturity score, diagnosis or worth judgment. |
| KLS-0009 | ReasonEvidence | `MUST` | Restrictive, emergency, disputed or irreversible transitions MUST preserve reason, evidence, uncertainty, alternatives and safeguards. |
| KLS-0010 | AffectedPersonNotice | `SHOULD` | A materially affected person SHOULD receive usable notice unless a specific temporary safety/legal reason is recorded. |
| KLS-0011 | CorrectionAppeal | `MUST` | Material lifecycles MUST provide applicable correction, contestation, appeal or independent-review transitions. |
| KLS-0012 | RollbackRemediation | `MUST` | Where reversal is impossible, the transition MUST record remaining exposure and remediation. |
| KLS-0013 | CrossLifecycleFreeze | `MUST` | Expired, revoked, disputed or unsafe authority MUST freeze expansion, optional reuse and high-impact action unless narrowly excepted. |
| KLS-0014 | ContestedKnowledgeUse | `SHOULD NOT` | Contested high-impact knowledge SHOULD NOT drive irreversible, punitive, rights-restricting or identity-shaping action during review. |
| KLS-0015 | AuthorityPropagation | `MUST` | Revocation, expiry or supersession of authority MUST propagate to dependent optional permissions and actions. |
| KLS-0016 | RepresentativeConflict | `MUST` | Disputed or conflicted representative authority MUST route high-impact action to conflict-free review. |
| KLS-0017 | ParticipationSupportFirst | `MUST` | Before reducing direct participation, the system MUST consider communication and decision support. |
| KLS-0018 | ParticipationRefusal | `MUST NOT` | Declined, withdrawn, silent or inaccessible participation MUST NOT be treated as agreement or proof. |
| KLS-0019 | KnowledgeContestation | `MUST` | A contested knowledge item MUST expose dispute and dependent uses and support restrict, correct, contextualize or supersede. |
| KLS-0020 | KnowledgeSupersession | `MUST` | Supersession MUST update active uses while preserving prior provenance. |
| KLS-0021 | DecisionImpactGate | `MUST` | A high-impact decision MUST pass impact, affected-person, authority, evidence, uncertainty, reversibility and review gates. |
| KLS-0022 | ActionOutcomeFeedback | `MUST` | Executed action MUST support outcome, feedback and revision transitions. |
| KLS-0023 | DeletionCompletion | `MUST NOT` | Deletion/restriction MUST NOT become Complete while prohibited active use remains possible. |
| KLS-0024 | BackupRestoration | `MUST` | Backup completion MUST define restoration-time suppression and reconciliation. |
| KLS-0025 | ExceptionExpiry | `MUST` | An open exception MUST carry owner, scope, safeguards and mandatory review or expiry. |
| KLS-0026 | RiskAssessment | `MUST` | A safety signal MUST be assessed with current/historical evidence, uncertainty, immediacy and responsible reviewer. |
| KLS-0027 | HandoffNotMessage | `MUST NOT` | Initiated or acknowledged handoff MUST NOT be represented as accepted or closed without evidence. |
| KLS-0028 | FailedHandoff | `MUST` | Failed handoff MUST identify next action, owner and transparent limitation. |
| KLS-0029 | ProtectiveActionReview | `MUST` | Temporary protective action MUST be minimum necessary, time-bounded where possible, independently reviewable and correctable. |
| KLS-0030 | IncidentClosure | `MUST` | An incident MUST NOT close before containment, investigation, remediation, verification, affected-person impact and closure authority are addressed or bounded. |
| KLS-0031 | AppealDifferentReviewer | `MUST` | A material appeal MUST use a different or conflict-free reviewer where the original role is conflicted. |
| KLS-0032 | ResourceExpiry | `MUST` | A stale, disputed or expired resource MUST stop being presented as current. |
| KLS-0033 | StateMachineVersion | `MUST` | Every transition MUST identify the state-machine version used. |
| KLS-0034 | Migration | `MUST` | A breaking lifecycle revision MUST define state mapping, in-flight handling, rollback, audit continuity and affected-person notice. |

## 5. Transition envelope

```text
transition_id
lifecycle_id
state_machine_version
object_ref
previous_state
new_state
actor_or_component_ref
role_assignment_ref
authority_refs
purpose_refs
reason
evidence_refs
uncertainty_refs
affected_person_refs
occurred_at
effective_at
review_or_expiry_at
exception_ref
audit_ref
```

## 6. Lifecycle summary

| ID | Lifecycle | Governed objects | States | Transition count |
|---|---|---|---|---:|
| KLC-0001 | AuthorityBasisLifecycle | AuthorityBasisRecord, PurposeRecord | Proposed, NoticePending, Active, Restricted, Disputed, Revoked, Expired, Superseded, Closed | 15 |
| KLC-0002 | RepresentativeAuthorityLifecycle | RepresentativeAuthority, RoleAssignment | Unverified, VerificationPending, ActiveWithinScope, Restricted, Disputed, Revoked, Expired, Superseded | 13 |
| KLC-0003 | ParticipationLifecycle | ParticipationRecord | NotIdentified, Identified, SupportAssessment, Invited, Participating, Declined, RepresentativeOnly, ParticipationUnsafe, Withdrew, ReviewDue, Closed | 15 |
| KLC-0004 | KnowledgeLifecycle | KnowledgeItem, EvidenceRecord, UncertaintyRecord | Recorded, SourceLinked, MaterialityReviewed, ActiveWithinScope, Contested, Restricted, Superseded, Expired, RemovedFromActiveUse | 14 |
| KLC-0005 | DecisionActionLifecycle | DecisionRecord, ActionRecord, FeedbackRecord, OutcomeRecord | Proposed, ImpactReview, AwaitingAuthority, Authorized, Declined, Executing, OutcomePending, FeedbackReceived, RevisionRequired, Reversed, Closed | 13 |
| KLC-0006 | DataMemoryRightsLifecycle | DataAssetRecord, MemoryRecord, RightsRequest, RetentionProfile | Active, Restricted, RequestReceived, CorrectionPending, DeletionPending, PrimaryAddressed, DerivedPropagationPending, BackupPending, ExceptionOpen, CompletionReview, Complete, Appealed, Reopened | 17 |
| KLC-0007 | SafetyHandoffLifecycle | RiskSignal, RiskAssessment, SafetyAction, HandoffRecord | SignalOpen, AssessmentPending, Classified, ActionReview, TemporaryAction, HandoffInitiated, HandoffAcknowledged, HandoffAccepted, HandoffFailed, Redirected, Monitoring, Closed, Appealed | 16 |
| KLC-0008 | IncidentAppealRemediationLifecycle | IncidentRecord, AppealRecord, ExceptionRecord | Reported, Triaged, Contained, Investigating, AppealOpen, DecisionPending, RemediationPlanned, RemediationInProgress, VerificationPending, Closed, Reopened | 13 |
| KLC-0009 | ResourceAvailabilityLifecycle | ResourceAvailabilityRecord | Unverified, VerificationPending, Current, Disputed, Stale, Unavailable, ReverificationPending, Retired | 13 |

## 7. Allowed transitions

### KLC-0001 — AuthorityBasisLifecycle

Objects: AuthorityBasisRecord, PurposeRecord

| # | From | To |
|---:|---|---|
| 1 | `Proposed` | `NoticePending` |
| 2 | `NoticePending` | `Active` |
| 3 | `Active` | `Restricted` |
| 4 | `Active` | `Disputed` |
| 5 | `Active` | `Revoked` |
| 6 | `Active` | `Expired` |
| 7 | `Restricted` | `Active` |
| 8 | `Restricted` | `Revoked` |
| 9 | `Disputed` | `Restricted` |
| 10 | `Disputed` | `Revoked` |
| 11 | `Disputed` | `Active` |
| 12 | `Active` | `Superseded` |
| 13 | `Revoked` | `Closed` |
| 14 | `Expired` | `Closed` |
| 15 | `Superseded` | `Closed` |

### KLC-0002 — RepresentativeAuthorityLifecycle

Objects: RepresentativeAuthority, RoleAssignment

| # | From | To |
|---:|---|---|
| 1 | `Unverified` | `VerificationPending` |
| 2 | `VerificationPending` | `ActiveWithinScope` |
| 3 | `VerificationPending` | `Disputed` |
| 4 | `ActiveWithinScope` | `Restricted` |
| 5 | `ActiveWithinScope` | `Disputed` |
| 6 | `ActiveWithinScope` | `Revoked` |
| 7 | `ActiveWithinScope` | `Expired` |
| 8 | `Restricted` | `ActiveWithinScope` |
| 9 | `Restricted` | `Revoked` |
| 10 | `Disputed` | `Restricted` |
| 11 | `Disputed` | `Revoked` |
| 12 | `Disputed` | `ActiveWithinScope` |
| 13 | `ActiveWithinScope` | `Superseded` |

### KLC-0003 — ParticipationLifecycle

Objects: ParticipationRecord

| # | From | To |
|---:|---|---|
| 1 | `NotIdentified` | `Identified` |
| 2 | `Identified` | `SupportAssessment` |
| 3 | `SupportAssessment` | `Invited` |
| 4 | `SupportAssessment` | `RepresentativeOnly` |
| 5 | `SupportAssessment` | `ParticipationUnsafe` |
| 6 | `Invited` | `Participating` |
| 7 | `Invited` | `Declined` |
| 8 | `Participating` | `Withdrew` |
| 9 | `Participating` | `ReviewDue` |
| 10 | `RepresentativeOnly` | `ReviewDue` |
| 11 | `ParticipationUnsafe` | `ReviewDue` |
| 12 | `ReviewDue` | `SupportAssessment` |
| 13 | `Declined` | `Closed` |
| 14 | `Withdrew` | `Closed` |
| 15 | `Participating` | `Closed` |

### KLC-0004 — KnowledgeLifecycle

Objects: KnowledgeItem, EvidenceRecord, UncertaintyRecord

| # | From | To |
|---:|---|---|
| 1 | `Recorded` | `SourceLinked` |
| 2 | `SourceLinked` | `MaterialityReviewed` |
| 3 | `MaterialityReviewed` | `ActiveWithinScope` |
| 4 | `ActiveWithinScope` | `Contested` |
| 5 | `ActiveWithinScope` | `Restricted` |
| 6 | `ActiveWithinScope` | `Superseded` |
| 7 | `ActiveWithinScope` | `Expired` |
| 8 | `Contested` | `Restricted` |
| 9 | `Contested` | `ActiveWithinScope` |
| 10 | `Contested` | `Superseded` |
| 11 | `Restricted` | `ActiveWithinScope` |
| 12 | `Restricted` | `Superseded` |
| 13 | `Superseded` | `RemovedFromActiveUse` |
| 14 | `Expired` | `RemovedFromActiveUse` |

### KLC-0005 — DecisionActionLifecycle

Objects: DecisionRecord, ActionRecord, FeedbackRecord, OutcomeRecord

| # | From | To |
|---:|---|---|
| 1 | `Proposed` | `ImpactReview` |
| 2 | `ImpactReview` | `AwaitingAuthority` |
| 3 | `ImpactReview` | `Declined` |
| 4 | `AwaitingAuthority` | `Authorized` |
| 5 | `AwaitingAuthority` | `Declined` |
| 6 | `Authorized` | `Executing` |
| 7 | `Executing` | `OutcomePending` |
| 8 | `OutcomePending` | `FeedbackReceived` |
| 9 | `FeedbackReceived` | `RevisionRequired` |
| 10 | `FeedbackReceived` | `Closed` |
| 11 | `RevisionRequired` | `ImpactReview` |
| 12 | `RevisionRequired` | `Reversed` |
| 13 | `Reversed` | `Closed` |

### KLC-0006 — DataMemoryRightsLifecycle

Objects: DataAssetRecord, MemoryRecord, RightsRequest, RetentionProfile

| # | From | To |
|---:|---|---|
| 1 | `Active` | `Restricted` |
| 2 | `Active` | `RequestReceived` |
| 3 | `Restricted` | `RequestReceived` |
| 4 | `RequestReceived` | `CorrectionPending` |
| 5 | `RequestReceived` | `DeletionPending` |
| 6 | `RequestReceived` | `ExceptionOpen` |
| 7 | `CorrectionPending` | `DerivedPropagationPending` |
| 8 | `DeletionPending` | `PrimaryAddressed` |
| 9 | `PrimaryAddressed` | `DerivedPropagationPending` |
| 10 | `DerivedPropagationPending` | `BackupPending` |
| 11 | `BackupPending` | `CompletionReview` |
| 12 | `ExceptionOpen` | `CompletionReview` |
| 13 | `CompletionReview` | `Complete` |
| 14 | `CompletionReview` | `Appealed` |
| 15 | `Complete` | `Appealed` |
| 16 | `Appealed` | `Reopened` |
| 17 | `Reopened` | `RequestReceived` |

### KLC-0007 — SafetyHandoffLifecycle

Objects: RiskSignal, RiskAssessment, SafetyAction, HandoffRecord

| # | From | To |
|---:|---|---|
| 1 | `SignalOpen` | `AssessmentPending` |
| 2 | `AssessmentPending` | `Classified` |
| 3 | `Classified` | `ActionReview` |
| 4 | `ActionReview` | `TemporaryAction` |
| 5 | `ActionReview` | `HandoffInitiated` |
| 6 | `ActionReview` | `Monitoring` |
| 7 | `HandoffInitiated` | `HandoffAcknowledged` |
| 8 | `HandoffAcknowledged` | `HandoffAccepted` |
| 9 | `HandoffInitiated` | `HandoffFailed` |
| 10 | `HandoffAcknowledged` | `HandoffFailed` |
| 11 | `HandoffFailed` | `Redirected` |
| 12 | `HandoffAccepted` | `Monitoring` |
| 13 | `TemporaryAction` | `Monitoring` |
| 14 | `Monitoring` | `Closed` |
| 15 | `Classified` | `Closed` |
| 16 | `Closed` | `Appealed` |

### KLC-0008 — IncidentAppealRemediationLifecycle

Objects: IncidentRecord, AppealRecord, ExceptionRecord

| # | From | To |
|---:|---|---|
| 1 | `Reported` | `Triaged` |
| 2 | `Triaged` | `Contained` |
| 3 | `Triaged` | `Investigating` |
| 4 | `Contained` | `Investigating` |
| 5 | `Investigating` | `AppealOpen` |
| 6 | `Investigating` | `DecisionPending` |
| 7 | `AppealOpen` | `DecisionPending` |
| 8 | `DecisionPending` | `RemediationPlanned` |
| 9 | `RemediationPlanned` | `RemediationInProgress` |
| 10 | `RemediationInProgress` | `VerificationPending` |
| 11 | `VerificationPending` | `Closed` |
| 12 | `Closed` | `Reopened` |
| 13 | `Reopened` | `Investigating` |

### KLC-0009 — ResourceAvailabilityLifecycle

Objects: ResourceAvailabilityRecord

| # | From | To |
|---:|---|---|
| 1 | `Unverified` | `VerificationPending` |
| 2 | `VerificationPending` | `Current` |
| 3 | `VerificationPending` | `Unavailable` |
| 4 | `Current` | `Disputed` |
| 5 | `Current` | `Stale` |
| 6 | `Current` | `Unavailable` |
| 7 | `Disputed` | `ReverificationPending` |
| 8 | `Stale` | `ReverificationPending` |
| 9 | `Unavailable` | `ReverificationPending` |
| 10 | `ReverificationPending` | `Current` |
| 11 | `ReverificationPending` | `Unavailable` |
| 12 | `Unavailable` | `Retired` |
| 13 | `Stale` | `Retired` |


## 8. Cross-lifecycle invariants

Revoked/expired/disputed authority freezes optional and high-impact use.
Contested knowledge cannot silently drive irreversible action. Corrections
update active decisions/memory while preserving history. Stale resources stop
current claims. Failed handoff identifies next action. Deletion completion
requires active, derived, shared and backup handling or bounded exception.
AI may propose but not finally authorize high-impact transitions.

## 9. Privacy, consent and access

Transition records carry minimum detail; sensitive reasons/evidence may remain
restricted. Revocation/deletion does not require public disclosure. Audit
preservation must not recreate an unrestricted profile.

## 10. Human agency and ethics

Declined, Disputed, Restricted, Risk and ParticipationUnsafe states do not
reduce dignity, credibility, service eligibility or worth. Explanation,
correction, refusal and appeal must remain usable.

## 11. Safety and escalation

Safety transitions require current evidence, uncertainty, proportionality,
named responsibility, availability, independent review and time bounds. A safety
classification must not silently persist after expiry or correction.

## 12. Review criteria and examples

Review includes invalid transitions, race conditions, expiry, restoration,
appeal, unavailable service, operator-as-risk and affected-person usability.
Examples: initiated handoff cannot jump to closed; revoked authority freezes new
optional action; completed rights requests may reopen on appeal.

## 13. Limitations and open questions

Automated authority, concurrent updates, emergency law, service targets,
immutable backup completion and universal notice requirements remain open.

## 14. Version and change history

| Version | Date | Change | Status |
|---|---|---|---|
| 0.1.0-draft.1 | 2026-07-15 | Initial 9-lifecycle, 129-transition model | Draft |

## 15. Current boundary

```text
Lifecycle families: 9
Lifecycle requirements: 34
External/implementation review: not executed
Current conforming products: 0
Overall: NoCurrentKernelConformanceClaim
```
