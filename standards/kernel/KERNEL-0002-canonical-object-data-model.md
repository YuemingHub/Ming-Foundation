---
id: KERNEL-0002
title: MingOS Kernel Canonical Object and Data Model
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
  - KERNEL-0003
  - REF-0040
  - REF-0042
  - REF-0043
  - REF-0044
depends_on:
  - KERNEL-0000
  - KERNEL-0001
---

# KERNEL-0002 — MingOS Kernel Canonical Object and Data Model

> Draft semantic model; not a product schema, universal ontology, legal identity system or conformance claim.

## 1. Purpose, scope and definitions

Define implementation-neutral semantic objects that operationalize KCR requirements. An object-local state belongs to one object type. Append/reference records are corrected by new records or supersession. Cross-object process flows are defined separately in KERNEL-0003.

## 2. Normative object requirements

| ID | Domain | Level | Requirement | Exact collection-local source | Source treatment | Proposed verification | Expected evidence |
|---|---|---|---|---|---|---|---|
| KDO-0001 | CommonEnvelope | `MUST` | Every canonical object MUST carry stable identity, type, schema version, creation provenance, purpose/authority where applicable, access class, review or expiry, revision and audit references. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0001, KCR-0002, KCR-0013, KCR-0035 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0002 | OpaqueIdentifiers | `MUST` | Canonical identifiers MUST be stable, opaque and free of unnecessary sensitive meaning. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0013, KCR-0035 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0003 | NoEmbeddedSecrets | `MUST NOT` | Identifiers and public references MUST NOT embed diagnoses, crisis states, legal status, secret credentials or other sensitive attributes. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0011, KCR-0029, KCR-0035 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0004 | IdentityRoleSeparation | `MUST` | Person, organization, system component, account, device, session and role assignment MUST remain distinct. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0005, KCR-0031, KCR-0032 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0005 | AffectedPersonReference | `MUST` | A material object MUST identify affected people or record why they cannot yet be identified. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0004, KCR-0020, KCR-0033 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0006 | SpeakerSubjectSource | `MUST` | Knowledge and event objects MUST distinguish speaker or generator, subject, source and affected people. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0005, KCR-0012, KCR-0013 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0007 | RoleAuthorityScope | `MUST` | A role assignment MUST identify scope, purpose, authority, permissions, prohibitions, conflict and review or expiry. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0005, KCR-0006, KCR-0032 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0008 | RepresentativeAuthority | `MUST` | Representative authority MUST use a distinct evidence-linked, scoped, expiring and appealable object. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0006, KCR-0033 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0009 | PurposeBinding | `MUST` | Personal-data, interpretive and consequential objects MUST reference an active declared purpose or documented exception. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0007, KCR-0030 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0010 | AuthorityBasisDistinction | `MUST` | Consent, requested service, safety, mandatory, security, research and disputed bases MUST remain distinguishable. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0008, KCR-0026, KCR-0030 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0011 | ParticipationPurposeSpecific | `MUST` | Participation MUST be represented per purpose/decision and MUST NOT become a maturity, compliance or worth score. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0009, KCR-0033 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0012 | KnowledgeType | `MUST` | Observation, statement, imported record, inference, hypothesis, pattern, judgment, recommendation, decision and action MUST remain distinguishable. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0012, KCR-0014 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0013 | ProvenanceGraph | `MUST` | A derived object MUST preserve source and transformation lineage subject to privacy and safety controls. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0013, KCR-0015, KCR-0035 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0014 | UncertaintyObject | `MUST` | Material unknowns, alternatives and dissent MUST be representable without flattening them into one confidence number. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0014, KCR-0015 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0015 | ContextWithoutCausation | `MUST` | Event, relationship and context objects MUST preserve time and perspective without automatic causal claims. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0017, KCR-0014 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0016 | DecisionAccountability | `MUST` | A high-impact decision MUST reference affected people, evidence, uncertainty, authority, accountable human/organization, reason, review and appeal. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0020, KCR-0032 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0017 | ActionReversibility | `SHOULD` | An action object SHOULD identify reversibility, observation plan, review condition and rollback where applicable. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0018, KCR-0019 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0018 | FeedbackRevision | `MUST` | Feedback and outcome objects MUST be able to trigger revision without erasing earlier provenance. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0034 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0019 | DataAssetInventory | `MUST` | Personal and derived data MUST be inventoried with purpose, authority, location, access, retention, backup and rights routes. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0011, KCR-0030, KCR-0035 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0020 | MemoryRights | `MUST` | Memory MUST reference sources, current use, visibility, retention, correction, restriction, deletion and supersession. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0027, KCR-0028, KCR-0029 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0021 | RightsRequestCoverage | `MUST` | Rights requests MUST support applicable access, explanation, correction, contextualization, restriction, objection, export, deletion, withdrawal, high-impact review and appeal. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0010, KCR-0027, KCR-0028 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0022 | RetentionNotPermission | `MUST NOT` | A retention profile or review interval MUST NOT be represented as automatic permission to retain or use data. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0028 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0023 | RiskNotIdentity | `MUST NOT` | A risk signal or assessment MUST NOT silently become a permanent identity or unrestricted profile. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0022, KCR-0029 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0024 | HandoffStateEvidence | `MUST` | A handoff object MUST distinguish initiated, acknowledged, accepted, failed, redirected and closed states. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0024 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0025 | ResourceFreshness | `MUST` | A resource record MUST carry verification, expiry, accessibility, scope, owner and stale behavior. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0023, KCR-0024 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0026 | IncidentAndAppeal | `MUST` | Incident and appeal objects MUST preserve timeline, affected people, conflicts, evidence, decisions, remediation and closure authority. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0025 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0027 | ExceptionBoundary | `MUST` | An exception MUST be narrow, purpose-bound, evidence-linked, time/review-bounded, safeguarded and appealable. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0026 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0028 | AuditMinimization | `MUST` | Audit events MUST preserve material accountability while minimizing sensitive content and restricting access. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0035 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0029 | CurrentAndHistory | `MUST` | Current and historical state MUST remain separately queryable; supersession MUST NOT silently rewrite history. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0015, KCR-0034, KCR-0035 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0030 | AccessClassification | `MUST` | Canonical objects and sensitive fields MUST carry an access class and minimum-necessary disclosure rule. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0011, KCR-0035 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0031 | UnknownNotNull | `SHOULD` | Unknown, not-applicable, unavailable, withheld and not-yet-collected states SHOULD remain distinguishable. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0014 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0032 | ExtensionBoundary | `MAY` | Implementations MAY add namespaced extensions when core semantics, provenance, access and migration remain intact. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0003, KCR-0035 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0033 | NoProductSchemaAsOntology | `MUST NOT` | A product table, prompt variable or legacy object name MUST NOT become a universal Kernel object merely because it exists. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0003 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0034 | NoDomainMethodUniversalization | `MUST NOT` | A family, education, counseling or cultural method MUST NOT become a universal object without cross-scene admission review. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0003, KCR-0017 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0035 | SerializationNeutrality | `MAY` | Implementations MAY use relational, graph, document, event-sourced or other storage when semantic/lifecycle obligations remain verifiable. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0001, KCR-0002, KCR-0003 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |
| KDO-0036 | MigrationAndCompatibility | `MUST` | A breaking object change MUST define identity continuity, field migration, lineage, coexistence, rollback, affected-person impact and dependent lifecycle changes. | KERNEL-0001 / Draft / 0.2.2-draft.4 / `standards/kernel/KERNEL-0001-core-operational-contract.md` / §KCR-0002, KCR-0003, KCR-0035 / CollectionLocalDraft | `OperationalizationOfDraftCore` | StructuralInspection; NegativeOrBoundaryScenario | GovernedRecord; ReviewFinding |

## 3. Common envelope

```text
object_id
object_type
schema_version
created_at
created_by_ref
source_refs
purpose_refs
authority_refs
affected_person_refs
access_class
retention_profile_ref
review_or_expiry_at
current_revision
supersedes_refs
audit_refs
extension_namespace
```

## 4. Canonical object catalog

| ID | Object type | Category | Minimum semantic fields | Lifecycle mode | State machine | Boundary |
|---|---|---|---|---|---|---|
| KOT-0001 | ImplementationBoundary | Governance | implementation_id, version, governed_surfaces, accountable_organization_ref, accountable_human_role_ref, version_set_ref, review_at | `GovernedConfiguration` | — | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0002 | VersionSet | Governance | family_version, document_versions, source_statuses, rfc_versions, profile_versions, supersedes_ref | `GovernedConfiguration` | — | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0003 | EntityRef | Identity | entity_kind, safe_label, resolution_scope | `AppendOrReferenceRecord` | — | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0004 | PersonRef | Identity | resolution_scope, access_class, correction_route | `AppendOrReferenceRecord` | — | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0005 | OrganizationRef | Identity | responsibility_scope, contact_route, jurisdiction_scope | `AppendOrReferenceRecord` | — | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0006 | SystemComponentRef | Identity | component_type, provider, version, capability_status, limitations | `AppendOrReferenceRecord` | — | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0007 | RoleAssignment | Authority | entity_ref, role_type, scope, purpose_refs, authority_refs, permissions, prohibitions, conflict_state, review_or_expiry_at | `ObjectStateMachine` | KSM-0003 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0008 | RepresentativeAuthority | Authority | representative_ref, subject_ref, authority_type, evidence_refs, permitted_actions, prohibited_actions, purpose_scope, conflict_state, review_or_expiry_at, appeal_route_ref | `ObjectStateMachine` | KSM-0004 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0009 | PurposeRecord | Authority | name, description, affected_person_refs, data_categories, allowed_operations, recipients, risk_class, retention_profile_ref, owner_ref, status | `ObjectStateMachine` | KSM-0001 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0010 | AuthorityBasisRecord | Authority | basis_category, person_or_representative_ref, purpose_ref, scope, notice_evidence_refs, jurisdiction_profile_ref, review_or_expiry_at, withdrawal_route, exception_ref | `ObjectStateMachine` | KSM-0002 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0011 | ParticipationRecord | Agency | person_ref, purpose_ref, decision_ref, participation_condition, preference, communication_support, representative_authority_ref, conflict_state, review_or_expiry_at, appeal_route_ref | `ObjectStateMachine` | KSM-0005 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0012 | ContextRecord | Context | scope, time_window, environment, structural_factors, source_refs, uncertainty_refs, access_class | `AppendOrReferenceRecord` | — | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0013 | RelationshipRecord | Context | party_refs, relationship_type, perspective_sources, effective_interval, conflict_or_asymmetry, visibility_policy | `AppendOrReferenceRecord` | — | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0014 | EventRecord | Context | event_type, occurred_or_reported_at, participant_refs, source_refs, observation_refs, context_ref, knowledge_status, uncertainty_refs | `AppendOrReferenceRecord` | — | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0015 | SourceRecord | Knowledge | source_type, speaker_or_component_ref, subject_refs, captured_at, context_ref, authority_scope, integrity_metadata | `AppendOrReferenceRecord` | — | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0016 | KnowledgeItem | Knowledge | knowledge_type, subject_refs, source_refs, content_or_safe_reference, evidence_refs, uncertainty_refs, purpose_refs, materiality_class, impact_class, confirmation_state, contestation_state, review_at, supersedes_refs | `ObjectStateMachine` | KSM-0006 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0017 | EvidenceRecord | Knowledge | evidence_type, source_refs, supports_or_challenges_refs, collected_at, method, limitations, access_class, retention_profile_ref | `AppendOrReferenceRecord` | — | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0018 | UncertaintyRecord | Knowledge | related_record_refs, unknowns, alternatives, confidence_basis, limitations, review_condition, dissent_refs | `AppendOrReferenceRecord` | — | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0019 | DecisionRecord | Decision | decision_type, affected_person_refs, proposal_refs, evidence_refs, uncertainty_refs, impact_assessment_ref, authority_refs, accountable_human_role_ref, selected_option, reason, review_at, appeal_route_ref, status | `ObjectStateMachine` | KSM-0007 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0020 | ActionRecord | Decision | decision_ref, actor_ref, authority_refs, target_refs, purpose_refs, action_type, scope, expected_effects, risk_refs, reversibility, review_or_end_at, status, rollback_plan_ref | `ObjectStateMachine` | KSM-0008 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0021 | FeedbackRecord | Decision | action_or_record_refs, source_ref, affected_person_ref, observed_at, content_or_safe_reference, knowledge_status, requested_change, access_class | `AppendOrReferenceRecord` | — | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0022 | OutcomeRecord | Decision | action_ref, observed_at, indicator_or_description, source_refs, evidence_refs, uncertainty_refs, expected_or_unexpected, harm_or_benefit, revision_required | `AppendOrReferenceRecord` | — | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0023 | DataAssetRecord | DataRights | subject_refs, source_refs, data_category, sensitivity, storage_locations, purpose_refs, authority_basis_refs, authorized_roles, retention_profile_ref, derived_asset_refs, backup_handling, rights_route_ref | `ObjectStateMachine` | KSM-0010 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0024 | MemoryRecord | DataRights | subject_refs, source_refs, knowledge_item_refs, purpose_refs, authority_basis_refs, active_use_refs, visibility_policy, retention_profile_ref, correction_state, restriction_state, deletion_state, review_at | `ObjectStateMachine` | KSM-0010 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0025 | RightsRequest | DataRights | request_type, requester_ref, subject_refs, representative_authority_ref, scope, received_at, responsible_owner_ref, status, located_asset_refs, exception_refs, completion_evidence_refs, appeal_ref | `ObjectStateMachine` | KSM-0009 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0026 | RetentionProfile | DataRights | purpose_ref, covered_asset_types, start_event, review_interval, deletion_or_archival_trigger, backup_handling, exception_categories, owner_ref, jurisdiction_profile_ref | `GovernedConfiguration` | — | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0027 | RiskSignal | Safety | source_refs, subject_refs, reporter_ref, occurred_or_reported_at, category, evidence_refs, uncertainty_refs, current_or_historical, model_or_policy_version | `AppendOrReferenceRecord` | — | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0028 | RiskAssessment | Safety | signal_refs, risk_level, immediacy, potential_harm, protective_factors, unknowns, least_intrusive_alternative, responsible_reviewer_ref, next_review_at | `ObjectStateMachine` | KSM-0011 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0029 | SafetyAction | Safety | assessment_ref, actor_ref, authority_scope, action, affected_person_refs, scope, duration, notice, proportionality_record_ref, review_at, appeal_route_ref, status | `ObjectStateMachine` | KSM-0012 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0030 | HandoffRecord | Safety | service_profile_ref, responsible_role_ref, target_person_or_service_ref, initiated_at, acknowledged_at, accepted_at, information_disclosed, authority_basis_refs, status, failed_handoff_action_ref, closure_reason | `ObjectStateMachine` | KSM-0013 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0031 | ResourceAvailabilityRecord | Safety | resource_class, service_scope, location, language_and_accessibility, source_refs, verified_by_ref, verification_method, verified_at, expires_at, stale_behavior, owner_ref, status | `ObjectStateMachine` | KSM-0017 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0032 | IncidentRecord | Accountability | severity, harm_or_near_miss, affected_person_refs, timeline_refs, source_and_evidence_refs, responsible_role_refs, containment_actions, root_causes, privacy_impact, remediation_refs, status, closure_authority_ref | `ObjectStateMachine` | KSM-0014 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0033 | AppealRecord | Accountability | appellant_ref, challenged_record_refs, grounds, submitted_at, independent_reviewer_ref, conflict_check, interim_restrictions, decision_ref, remediation_refs, status | `ObjectStateMachine` | KSM-0015 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0034 | ExceptionRecord | Accountability | requirement_or_policy_refs, authority_basis, scope, affected_person_refs, reason, evidence_refs, risk_and_safeguards, expires_or_reviews_at, owner_ref, independent_review_ref, appeal_route_ref, status | `ObjectStateMachine` | KSM-0016 | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0035 | AuditEvent | Accountability | event_type, actor_or_component_ref, role_assignment_ref, target_record_refs, action, purpose_refs, authority_refs, occurred_at, result, previous_and_new_state, evidence_refs, access_class, integrity_metadata | `AppendOrReferenceRecord` | — | Implementation-neutral semantic object; no status or authority inferred from existence. |

## 5. Human agency, privacy and safety

Relationships do not create authority. The model MUST NOT reduce a person to a role, profile, diagnosis, risk state, process stage or model output. Purpose, consent and other authority bases remain distinct. Signal, assessment, action, handoff, resource, incident and appeal are separate objects.

## 6. Review, examples and limitations

Review tests exact KCR derivation, minimization, comprehension, access, migration and failure modes. A parent report remains attributed; a generated referral is not accepted handoff; correction revises active state while retaining provenance. Identity resolution, group impact, confidence and deletion/audit balance remain open.

## 7. Version history and current boundary

| Version | Date | Change | Status |
|---|---|---|---|
| 0.1.0-draft.1 | 2026-07-15 | Initial 35-object model | Draft |
| 0.2.0-draft.2 | 2026-07-15 | Exact KCR mapping and lifecycle-mode ownership | Draft |

```text
Object types: 35
Object requirements: 36
External/implementation review: not executed
Overall: NoCurrentKernelConformanceClaim
```
