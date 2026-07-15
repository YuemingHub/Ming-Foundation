---
id: REF-0036
title: Kernel Lifecycle Transition and Invariant Matrix
status: Draft
version: 0.1.0-draft.1
layer: Reference
owner: Ming Foundation Kernel Architecture
created: 2026-07-15
updated: 2026-07-15
language: en
canonical_language: en
translation_status: original
decision_base_commit: a0b8234567c211896085f0e1259b96bcb53effd1
related:
  - KERNEL-0002
  - KERNEL-0003
  - REF-0035
  - REF-0037
  - REF-0038
  - REF-0039
depends_on:
  - KERNEL-0003
---

# REF-0036 — Kernel Lifecycle Transition and Invariant Matrix

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

Forbidden shortcuts include: authority directly to high-impact action without
review; initiated handoff directly to closed; deletion request directly to
complete; stale resource remaining current; incident reported directly to
closed; AI proposal represented as human authorization.
