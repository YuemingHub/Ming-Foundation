---
id: KERNEL-0003
title: MingOS Kernel Object State Machines and Process Coordination
status: Draft
version: 0.2.0-draft.2
layer: Layer 2 — Standards
owner: Ming Foundation Kernel Architecture
created: 2026-07-15
updated: 2026-07-15
language: en
canonical_language: en
translation_status: original
decision_base_commit: f3905710db2304ab926c4ab31e10264931539f98
related:
  - ADR-0026
  - MOS-0000
  - KERNEL-0000
  - KERNEL-0001
  - KERNEL-0002
  - REF-0041
  - REF-0042
  - REF-0043
  - REF-0044
depends_on:
  - KERNEL-0000
  - KERNEL-0001
  - KERNEL-0002
---

# KERNEL-0003 — MingOS Kernel Object State Machines and Process Coordination

> Object state and cross-object process stage are separate. Neither is an identity label, diagnosis or conformance proof.

## 1. Purpose, scope and definitions

Define object-local states and transitions plus non-state-bearing cross-object coordination. A transition changes one state-bearing object. A process event creates or links multiple objects. An ExceptionRecord never legalizes an undefined transition.

## 2. Normative lifecycle requirements

| ID | Domain | Level | Requirement | Exact collection-local source | Source treatment | Proposed verification | Expected evidence |
|---|---|---|---|---|---|---|---|
| KLS-0001 | TransitionEnvelope | `MUST` | Every transition MUST record lifecycle/version, object, previous/new state, actor/component, role, authority, purpose, reason, evidence, uncertainty, affected people, time, review/expiry and audit. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0002, KCR-0013, KCR-0035 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0002 | NoSilentTransition | `MUST NOT` | A material object MUST NOT change state without an append-oriented transition record. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0035 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0003 | CurrentHistorySeparation | `MUST` | Current state and transition history MUST remain separately inspectable. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0015, KCR-0034, KCR-0035 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0004 | AllowedTransitions | `MUST` | An implementation MUST reject an undefined or disallowed object-state transition. An ExceptionRecord may authorize alternate valid behavior but MUST NOT legalize a structurally invalid transition. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0003, KCR-0035 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0005 | ActorAuthority | `MUST` | A material transition MUST identify responsible actor, role and authority scope. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0001, KCR-0005, KCR-0032 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0006 | AIBoundary | `MUST NOT` | An AI component MUST NOT be the final accountable authorizer of a high-impact transition. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0031, KCR-0032 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0007 | ReviewExpiry | `MUST` | Active authority, participation, knowledge, resource, exception and safety states MUST support review or expiry. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0006, KCR-0008, KCR-0023, KCR-0028 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0008 | StateNotIdentity | `MUST NOT` | A lifecycle state MUST NOT become a permanent identity, maturity score, diagnosis or worth judgment. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0029 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0009 | ReasonEvidence | `MUST` | Restrictive, emergency, disputed or irreversible transitions MUST preserve reason, evidence, uncertainty, alternatives and safeguards. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0014, KCR-0020, KCR-0026 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0010 | AffectedPersonNotice | `SHOULD` | A materially affected person SHOULD receive usable notice unless a specific temporary safety/legal reason is recorded. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0020, KCR-0033 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0011 | CorrectionAppeal | `MUST` | Material lifecycles MUST provide applicable correction, contestation, appeal or independent-review transitions. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0010, KCR-0025 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0012 | RollbackRemediation | `MUST` | Where reversal is impossible, the transition MUST record remaining exposure and remediation. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0019, KCR-0025 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0013 | CrossLifecycleFreeze | `MUST` | Expired, revoked, disputed or unsafe authority MUST freeze expansion, optional reuse and high-impact action unless narrowly excepted. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0008, KCR-0009, KCR-0020, KCR-0030 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0014 | ContestedKnowledgeUse | `SHOULD NOT` | Contested high-impact knowledge SHOULD NOT drive irreversible, punitive, rights-restricting or identity-shaping action during review. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0010, KCR-0015 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0015 | AuthorityPropagation | `MUST` | Revocation, expiry or supersession of authority MUST propagate to dependent optional permissions and actions. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0008, KCR-0028, KCR-0030 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0016 | RepresentativeConflict | `MUST` | Disputed or conflicted representative authority MUST route high-impact action to conflict-free review. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0006, KCR-0033 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0017 | ParticipationSupportFirst | `MUST` | Before reducing direct participation, the system MUST consider communication and decision support. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0033 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0018 | ParticipationRefusal | `MUST NOT` | Declined, withdrawn, silent or inaccessible participation MUST NOT be treated as agreement or proof. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0009, KCR-0033 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0019 | KnowledgeContestation | `MUST` | A contested knowledge item MUST expose dispute and dependent uses and support restrict, correct, contextualize or supersede. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0010, KCR-0015 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0020 | KnowledgeSupersession | `MUST` | Supersession MUST update active uses while preserving prior provenance. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0015, KCR-0034 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0021 | DecisionImpactGate | `MUST` | A high-impact decision MUST pass impact, affected-person, authority, evidence, uncertainty, reversibility and review gates. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0020, KCR-0032 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0022 | ActionOutcomeFeedback | `MUST` | Executed action MUST support outcome, feedback and revision transitions. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0034 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0023 | DeletionCompletion | `MUST NOT` | Deletion/restriction MUST NOT become Complete while prohibited active use remains possible. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0028 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0024 | BackupRestoration | `MUST` | Backup completion MUST define restoration-time suppression and reconciliation. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0028 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0025 | ExceptionExpiry | `MUST` | An open exception MUST carry owner, scope, safeguards and mandatory review or expiry. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0026, KCR-0028 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0026 | RiskAssessment | `MUST` | A safety signal MUST be assessed with current/historical evidence, uncertainty, immediacy and responsible reviewer. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0022 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0027 | HandoffNotMessage | `MUST NOT` | Initiated or acknowledged handoff MUST NOT be represented as accepted or closed without evidence. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0024 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0028 | FailedHandoff | `MUST` | Failed handoff MUST identify next action, owner and transparent limitation. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0023, KCR-0024 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0029 | ProtectiveActionReview | `MUST` | Temporary protective action MUST be minimum necessary, time-bounded where possible, independently reviewable and correctable. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0026 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0030 | IncidentClosure | `MUST` | An incident MUST NOT close before containment, investigation, remediation, verification, affected-person impact and closure authority are addressed or bounded. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0025, KCR-0034 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0031 | AppealDifferentReviewer | `MUST` | A material appeal MUST use a different or conflict-free reviewer where the original role is conflicted. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0010, KCR-0025, KCR-0032 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0032 | ResourceExpiry | `MUST` | A stale, disputed or expired resource MUST stop being presented as current. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0023 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0033 | StateMachineVersion | `MUST` | Every transition MUST identify the state-machine version used. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0002, KCR-0035 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KLS-0034 | Migration | `MUST` | A breaking lifecycle revision MUST define state mapping, in-flight handling, rollback, audit continuity and affected-person notice. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0002, KCR-0003, KCR-0035 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |

## 3. Transition envelope

```text
transition_id
state_machine_id
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

## 4. Object-local state-machine summary

| ID | State machine | State-bearing object | States | Transition count |
|---|---|---|---|---:|
| KSM-0001 | PurposeRecordLifecycle | PurposeRecord | Proposed, Active, Suspended, Superseded, Retired | 7 |
| KSM-0002 | AuthorityBasisLifecycle | AuthorityBasisRecord | Proposed, NoticePending, Active, Restricted, Disputed, Revoked, Expired, Superseded, Closed | 15 |
| KSM-0003 | RoleAssignmentLifecycle | RoleAssignment | Proposed, Active, Restricted, Conflicted, Revoked, Expired, Closed | 12 |
| KSM-0004 | RepresentativeAuthorityLifecycle | RepresentativeAuthority | Unverified, VerificationPending, ActiveWithinScope, Restricted, Disputed, Revoked, Expired, Superseded, Closed | 16 |
| KSM-0005 | ParticipationRecordLifecycle | ParticipationRecord | NotIdentified, SupportAssessment, Invited, Participating, Declined, RepresentativeOnly, ParticipationUnsafe, Withdrew, ReviewDue, Closed | 14 |
| KSM-0006 | KnowledgeItemLifecycle | KnowledgeItem | Recorded, SourceLinked, MaterialityReviewed, ActiveWithinScope, Contested, Restricted, Superseded, Expired, RemovedFromActiveUse | 14 |
| KSM-0007 | DecisionRecordLifecycle | DecisionRecord | Proposed, ImpactReview, AwaitingAuthority, Authorized, Declined, ActionCreated, RevisionRequired, Reversed, Closed | 12 |
| KSM-0008 | ActionRecordLifecycle | ActionRecord | Planned, AwaitingAuthority, Authorized, Executing, Paused, Completed, Failed, Reversed, Closed | 13 |
| KSM-0009 | RightsRequestLifecycle | RightsRequest | Received, AuthorityReview, LocatingRecords, ActionPending, ExceptionOpen, CompletionReview, Complete, Appealed, Reopened, Closed | 14 |
| KSM-0010 | DataAssetMemoryLifecycle | DataAssetRecord|MemoryRecord | Active, Restricted, CorrectionPending, DeletionPending, PrimaryAddressed, DerivedPropagationPending, BackupPending, ExceptionOpen, CompletionReview, Complete, Superseded | 16 |
| KSM-0011 | RiskAssessmentLifecycle | RiskAssessment | Pending, InReview, Classified, ReviewDue, Superseded, Closed | 7 |
| KSM-0012 | SafetyActionLifecycle | SafetyAction | Proposed, ReviewPending, Authorized, Active, Monitoring, Ended, Appealed, Revoked, Closed | 12 |
| KSM-0013 | HandoffRecordLifecycle | HandoffRecord | Initiated, Acknowledged, Accepted, Failed, Redirected, Closed | 8 |
| KSM-0014 | IncidentRecordLifecycle | IncidentRecord | Reported, Triaged, Contained, Investigating, RemediationPlanned, RemediationInProgress, VerificationPending, Closed, Reopened | 10 |
| KSM-0015 | AppealRecordLifecycle | AppealRecord | Open, EligibilityReview, ReviewPending, DecisionIssued, RemediationPending, Closed, Reopened | 9 |
| KSM-0016 | ExceptionRecordLifecycle | ExceptionRecord | Proposed, ReviewPending, Active, Restricted, Revoked, Expired, Closed | 11 |
| KSM-0017 | ResourceAvailabilityLifecycle | ResourceAvailabilityRecord | Unverified, VerificationPending, Current, Disputed, Stale, Unavailable, ReverificationPending, Retired | 13 |

## 5. Allowed object-state transitions

### KSM-0001 — PurposeRecordLifecycle

State-bearing object: `PurposeRecord`

| # | From | To |
|---:|---|---|
| 1 | `Proposed` | `Active` |
| 2 | `Active` | `Suspended` |
| 3 | `Suspended` | `Active` |
| 4 | `Active` | `Superseded` |
| 5 | `Suspended` | `Superseded` |
| 6 | `Superseded` | `Retired` |
| 7 | `Active` | `Retired` |

### KSM-0002 — AuthorityBasisLifecycle

State-bearing object: `AuthorityBasisRecord`

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

### KSM-0003 — RoleAssignmentLifecycle

State-bearing object: `RoleAssignment`

| # | From | To |
|---:|---|---|
| 1 | `Proposed` | `Active` |
| 2 | `Active` | `Restricted` |
| 3 | `Active` | `Conflicted` |
| 4 | `Active` | `Revoked` |
| 5 | `Active` | `Expired` |
| 6 | `Restricted` | `Active` |
| 7 | `Restricted` | `Revoked` |
| 8 | `Conflicted` | `Restricted` |
| 9 | `Conflicted` | `Revoked` |
| 10 | `Conflicted` | `Active` |
| 11 | `Revoked` | `Closed` |
| 12 | `Expired` | `Closed` |

### KSM-0004 — RepresentativeAuthorityLifecycle

State-bearing object: `RepresentativeAuthority`

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
| 14 | `Revoked` | `Closed` |
| 15 | `Expired` | `Closed` |
| 16 | `Superseded` | `Closed` |

### KSM-0005 — ParticipationRecordLifecycle

State-bearing object: `ParticipationRecord`

| # | From | To |
|---:|---|---|
| 1 | `NotIdentified` | `SupportAssessment` |
| 2 | `SupportAssessment` | `Invited` |
| 3 | `SupportAssessment` | `RepresentativeOnly` |
| 4 | `SupportAssessment` | `ParticipationUnsafe` |
| 5 | `Invited` | `Participating` |
| 6 | `Invited` | `Declined` |
| 7 | `Participating` | `Withdrew` |
| 8 | `Participating` | `ReviewDue` |
| 9 | `RepresentativeOnly` | `ReviewDue` |
| 10 | `ParticipationUnsafe` | `ReviewDue` |
| 11 | `ReviewDue` | `SupportAssessment` |
| 12 | `Declined` | `Closed` |
| 13 | `Withdrew` | `Closed` |
| 14 | `Participating` | `Closed` |

### KSM-0006 — KnowledgeItemLifecycle

State-bearing object: `KnowledgeItem`

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

### KSM-0007 — DecisionRecordLifecycle

State-bearing object: `DecisionRecord`

| # | From | To |
|---:|---|---|
| 1 | `Proposed` | `ImpactReview` |
| 2 | `ImpactReview` | `AwaitingAuthority` |
| 3 | `ImpactReview` | `Declined` |
| 4 | `AwaitingAuthority` | `Authorized` |
| 5 | `AwaitingAuthority` | `Declined` |
| 6 | `Authorized` | `ActionCreated` |
| 7 | `Authorized` | `RevisionRequired` |
| 8 | `ActionCreated` | `RevisionRequired` |
| 9 | `ActionCreated` | `Closed` |
| 10 | `RevisionRequired` | `ImpactReview` |
| 11 | `RevisionRequired` | `Reversed` |
| 12 | `Reversed` | `Closed` |

### KSM-0008 — ActionRecordLifecycle

State-bearing object: `ActionRecord`

| # | From | To |
|---:|---|---|
| 1 | `Planned` | `AwaitingAuthority` |
| 2 | `AwaitingAuthority` | `Authorized` |
| 3 | `Authorized` | `Executing` |
| 4 | `Executing` | `Paused` |
| 5 | `Paused` | `Executing` |
| 6 | `Executing` | `Completed` |
| 7 | `Executing` | `Failed` |
| 8 | `Paused` | `Failed` |
| 9 | `Completed` | `Reversed` |
| 10 | `Failed` | `Reversed` |
| 11 | `Completed` | `Closed` |
| 12 | `Failed` | `Closed` |
| 13 | `Reversed` | `Closed` |

### KSM-0009 — RightsRequestLifecycle

State-bearing object: `RightsRequest`

| # | From | To |
|---:|---|---|
| 1 | `Received` | `AuthorityReview` |
| 2 | `AuthorityReview` | `LocatingRecords` |
| 3 | `AuthorityReview` | `ExceptionOpen` |
| 4 | `LocatingRecords` | `ActionPending` |
| 5 | `ActionPending` | `CompletionReview` |
| 6 | `ActionPending` | `ExceptionOpen` |
| 7 | `ExceptionOpen` | `CompletionReview` |
| 8 | `CompletionReview` | `Complete` |
| 9 | `CompletionReview` | `Appealed` |
| 10 | `Complete` | `Appealed` |
| 11 | `Appealed` | `Reopened` |
| 12 | `Reopened` | `AuthorityReview` |
| 13 | `Complete` | `Closed` |
| 14 | `Appealed` | `Closed` |

### KSM-0010 — DataAssetMemoryLifecycle

State-bearing object: `DataAssetRecord|MemoryRecord`

| # | From | To |
|---:|---|---|
| 1 | `Active` | `Restricted` |
| 2 | `Active` | `CorrectionPending` |
| 3 | `Active` | `DeletionPending` |
| 4 | `Restricted` | `CorrectionPending` |
| 5 | `Restricted` | `DeletionPending` |
| 6 | `CorrectionPending` | `DerivedPropagationPending` |
| 7 | `DeletionPending` | `PrimaryAddressed` |
| 8 | `PrimaryAddressed` | `DerivedPropagationPending` |
| 9 | `DerivedPropagationPending` | `BackupPending` |
| 10 | `BackupPending` | `CompletionReview` |
| 11 | `DeletionPending` | `ExceptionOpen` |
| 12 | `ExceptionOpen` | `CompletionReview` |
| 13 | `CompletionReview` | `Complete` |
| 14 | `Active` | `Superseded` |
| 15 | `Restricted` | `Superseded` |
| 16 | `Superseded` | `Complete` |

### KSM-0011 — RiskAssessmentLifecycle

State-bearing object: `RiskAssessment`

| # | From | To |
|---:|---|---|
| 1 | `Pending` | `InReview` |
| 2 | `InReview` | `Classified` |
| 3 | `Classified` | `ReviewDue` |
| 4 | `ReviewDue` | `InReview` |
| 5 | `Classified` | `Superseded` |
| 6 | `Superseded` | `Closed` |
| 7 | `Classified` | `Closed` |

### KSM-0012 — SafetyActionLifecycle

State-bearing object: `SafetyAction`

| # | From | To |
|---:|---|---|
| 1 | `Proposed` | `ReviewPending` |
| 2 | `ReviewPending` | `Authorized` |
| 3 | `Authorized` | `Active` |
| 4 | `Active` | `Monitoring` |
| 5 | `Monitoring` | `Ended` |
| 6 | `Active` | `Revoked` |
| 7 | `Monitoring` | `Revoked` |
| 8 | `Ended` | `Appealed` |
| 9 | `Revoked` | `Appealed` |
| 10 | `Ended` | `Closed` |
| 11 | `Revoked` | `Closed` |
| 12 | `Appealed` | `ReviewPending` |

### KSM-0013 — HandoffRecordLifecycle

State-bearing object: `HandoffRecord`

| # | From | To |
|---:|---|---|
| 1 | `Initiated` | `Acknowledged` |
| 2 | `Acknowledged` | `Accepted` |
| 3 | `Initiated` | `Failed` |
| 4 | `Acknowledged` | `Failed` |
| 5 | `Failed` | `Redirected` |
| 6 | `Accepted` | `Closed` |
| 7 | `Redirected` | `Closed` |
| 8 | `Failed` | `Closed` |

### KSM-0014 — IncidentRecordLifecycle

State-bearing object: `IncidentRecord`

| # | From | To |
|---:|---|---|
| 1 | `Reported` | `Triaged` |
| 2 | `Triaged` | `Contained` |
| 3 | `Triaged` | `Investigating` |
| 4 | `Contained` | `Investigating` |
| 5 | `Investigating` | `RemediationPlanned` |
| 6 | `RemediationPlanned` | `RemediationInProgress` |
| 7 | `RemediationInProgress` | `VerificationPending` |
| 8 | `VerificationPending` | `Closed` |
| 9 | `Closed` | `Reopened` |
| 10 | `Reopened` | `Investigating` |

### KSM-0015 — AppealRecordLifecycle

State-bearing object: `AppealRecord`

| # | From | To |
|---:|---|---|
| 1 | `Open` | `EligibilityReview` |
| 2 | `EligibilityReview` | `ReviewPending` |
| 3 | `EligibilityReview` | `Closed` |
| 4 | `ReviewPending` | `DecisionIssued` |
| 5 | `DecisionIssued` | `RemediationPending` |
| 6 | `DecisionIssued` | `Closed` |
| 7 | `RemediationPending` | `Closed` |
| 8 | `Closed` | `Reopened` |
| 9 | `Reopened` | `ReviewPending` |

### KSM-0016 — ExceptionRecordLifecycle

State-bearing object: `ExceptionRecord`

| # | From | To |
|---:|---|---|
| 1 | `Proposed` | `ReviewPending` |
| 2 | `ReviewPending` | `Active` |
| 3 | `ReviewPending` | `Closed` |
| 4 | `Active` | `Restricted` |
| 5 | `Restricted` | `Active` |
| 6 | `Active` | `Revoked` |
| 7 | `Active` | `Expired` |
| 8 | `Restricted` | `Revoked` |
| 9 | `Restricted` | `Expired` |
| 10 | `Revoked` | `Closed` |
| 11 | `Expired` | `Closed` |

### KSM-0017 — ResourceAvailabilityLifecycle

State-bearing object: `ResourceAvailabilityRecord`

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


## 6. Cross-object process coordination

A KPF stage means required objects or reviews become available. It MUST NOT be stored as the state of every participating object.

| ID | Process flow | Stages | Stage transition count |
|---|---|---|---:|
| KPF-0001 | PurposeAndAuthorityEstablishment | PurposeProposed, ImpactReviewed, NoticePrepared, AuthorityRecorded, ActiveOrRestricted | 4 |
| KPF-0002 | RepresentativeAndParticipation | RepresentativeClaimed, AuthorityVerified, ConflictChecked, ParticipationSupported, DecisionRecorded | 4 |
| KPF-0003 | KnowledgeFormation | SourceCaptured, KnowledgeTyped, EvidenceLinked, UncertaintyRecorded, MaterialityReviewed, ActiveOrRestricted | 5 |
| KPF-0004 | ConsequentialDecisionAndAction | Proposal, ImpactReview, AuthorityReview, HumanAccountability, Action, Outcome, Feedback, Revision | 7 |
| KPF-0005 | DataMemoryRights | Request, AuthorityReview, Locate, PrimaryAction, DerivedPropagation, BackupHandling, CompletionReview, Appeal | 7 |
| KPF-0006 | SafetyAndHandoff | Signal, Assessment, Proportionality, ProtectiveActionOrHandoff, AcceptanceOrFailure, Monitoring, IncidentOrAppeal | 6 |
| KPF-0007 | IncidentRemediation | Report, Triage, Contain, Investigate, Decide, Remediate, Verify, CloseOrReopen | 7 |
| KPF-0008 | ResourceFreshness | Unverified, Verify, Current, DisputeOrStale, Reverify, Retire | 5 |
| KPF-0009 | CorrectionPropagation | CorrectionReceived, DependenciesLocated, CurrentStateRevised, DerivedRecordsUpdated, AffectedNotice, AuditPreserved | 5 |

## 7. Invariants, review and limitations

Revoked or disputed authority freezes optional/high-impact action; contested knowledge does not silently drive irreversible action; corrections preserve history; stale resources stop current claims; failed handoff names next action; deletion completion addresses active, derived, shared and backup use; AI may propose but not finally authorize high-impact transitions.

Review includes invalid transitions, state/process confusion, concurrency, expiry, restoration, appeal, unavailable service and operator-as-risk.

## 8. Version history and current boundary

| Version | Date | Change | Status |
|---|---|---|---|
| 0.1.0-draft.1 | 2026-07-15 | Initial mixed lifecycle family | Draft |
| 0.2.0-draft.2 | 2026-07-15 | Separate 17 object state machines from 9 process flows | Draft |

```text
Object state machines: 17
Object-state transitions: 203
Process flows: 9
Process transitions: 50
Lifecycle requirements: 34
Overall: NoCurrentKernelConformanceClaim
```
