---
id: KERNEL-0002
title: MingOS Kernel Canonical Object and Data Model
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
  - KERNEL-0003
  - RFC-0001
  - RFC-0002
  - RFC-0003
  - RFC-0004
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
---

# KERNEL-0002 — MingOS Kernel Canonical Object and Data Model

> **Draft semantic model.** This is not a product database schema, universal
> ontology, legal identity system or implementation-conformance claim.

## 1. Purpose

Propose implementation-neutral semantic objects needed to preserve Round 07
core obligations across systems, agents, services, professional workflows and
organizations.

## 2. Scope and non-goals

Defines object meanings, minimum semantic fields, relationships, provenance,
access and migration boundaries. It does not prescribe storage engine,
serialization, UI, full legal identity, final enums, cryptography, physical
database layout or reference implementation.

## 3. Definitions

A canonical object is a semantic contract, not necessarily one database row.
Object references resolve by access context. Current state and historical state
remain distinct. Namespaced extensions cannot override core semantics.

## 4. Normative object requirements

| ID | Domain | Level | Requirement |
|---|---|---|---|
| KDO-0001 | CommonEnvelope | `MUST` | Every canonical object MUST carry stable identity, type, schema version, creation provenance, purpose/authority where applicable, access class, review or expiry, revision and audit references. |
| KDO-0002 | OpaqueIdentifiers | `MUST` | Canonical identifiers MUST be stable, opaque and free of unnecessary sensitive meaning. |
| KDO-0003 | NoEmbeddedSecrets | `MUST NOT` | Identifiers and public references MUST NOT embed diagnoses, crisis states, legal status, secret credentials or other sensitive attributes. |
| KDO-0004 | IdentityRoleSeparation | `MUST` | Person, organization, system component, account, device, session and role assignment MUST remain distinct. |
| KDO-0005 | AffectedPersonReference | `MUST` | A material object MUST identify affected people or record why they cannot yet be identified. |
| KDO-0006 | SpeakerSubjectSource | `MUST` | Knowledge and event objects MUST distinguish speaker or generator, subject, source and affected people. |
| KDO-0007 | RoleAuthorityScope | `MUST` | A role assignment MUST identify scope, purpose, authority, permissions, prohibitions, conflict and review or expiry. |
| KDO-0008 | RepresentativeAuthority | `MUST` | Representative authority MUST use a distinct evidence-linked, scoped, expiring and appealable object. |
| KDO-0009 | PurposeBinding | `MUST` | Personal-data, interpretive and consequential objects MUST reference an active declared purpose or documented exception. |
| KDO-0010 | AuthorityBasisDistinction | `MUST` | Consent, requested service, safety, mandatory, security, research and disputed bases MUST remain distinguishable. |
| KDO-0011 | ParticipationPurposeSpecific | `MUST` | Participation MUST be represented per purpose/decision and MUST NOT become a maturity, compliance or worth score. |
| KDO-0012 | KnowledgeType | `MUST` | Observation, statement, imported record, inference, hypothesis, pattern, judgment, recommendation, decision and action MUST remain distinguishable. |
| KDO-0013 | ProvenanceGraph | `MUST` | A derived object MUST preserve source and transformation lineage subject to privacy and safety controls. |
| KDO-0014 | UncertaintyObject | `MUST` | Material unknowns, alternatives and dissent MUST be representable without flattening them into one confidence number. |
| KDO-0015 | ContextWithoutCausation | `MUST` | Event, relationship and context objects MUST preserve time and perspective without automatic causal claims. |
| KDO-0016 | DecisionAccountability | `MUST` | A high-impact decision MUST reference affected people, evidence, uncertainty, authority, accountable human/organization, reason, review and appeal. |
| KDO-0017 | ActionReversibility | `SHOULD` | An action object SHOULD identify reversibility, observation plan, review condition and rollback where applicable. |
| KDO-0018 | FeedbackRevision | `MUST` | Feedback and outcome objects MUST be able to trigger revision without erasing earlier provenance. |
| KDO-0019 | DataAssetInventory | `MUST` | Personal and derived data MUST be inventoried with purpose, authority, location, access, retention, backup and rights routes. |
| KDO-0020 | MemoryRights | `MUST` | Memory MUST reference sources, current use, visibility, retention, correction, restriction, deletion and supersession. |
| KDO-0021 | RightsRequestCoverage | `MUST` | Rights requests MUST support applicable access, explanation, correction, contextualization, restriction, objection, export, deletion, withdrawal, high-impact review and appeal. |
| KDO-0022 | RetentionNotPermission | `MUST NOT` | A retention profile or review interval MUST NOT be represented as automatic permission to retain or use data. |
| KDO-0023 | RiskNotIdentity | `MUST NOT` | A risk signal or assessment MUST NOT silently become a permanent identity or unrestricted profile. |
| KDO-0024 | HandoffStateEvidence | `MUST` | A handoff object MUST distinguish initiated, acknowledged, accepted, failed, redirected and closed states. |
| KDO-0025 | ResourceFreshness | `MUST` | A resource record MUST carry verification, expiry, accessibility, scope, owner and stale behavior. |
| KDO-0026 | IncidentAndAppeal | `MUST` | Incident and appeal objects MUST preserve timeline, affected people, conflicts, evidence, decisions, remediation and closure authority. |
| KDO-0027 | ExceptionBoundary | `MUST` | An exception MUST be narrow, purpose-bound, evidence-linked, time/review-bounded, safeguarded and appealable. |
| KDO-0028 | AuditMinimization | `MUST` | Audit events MUST preserve material accountability while minimizing sensitive content and restricting access. |
| KDO-0029 | CurrentAndHistory | `MUST` | Current and historical state MUST remain separately queryable; supersession MUST NOT silently rewrite history. |
| KDO-0030 | AccessClassification | `MUST` | Canonical objects and sensitive fields MUST carry an access class and minimum-necessary disclosure rule. |
| KDO-0031 | UnknownNotNull | `SHOULD` | Unknown, not-applicable, unavailable, withheld and not-yet-collected states SHOULD remain distinguishable. |
| KDO-0032 | ExtensionBoundary | `MAY` | Implementations MAY add namespaced extensions when core semantics, provenance, access and migration remain intact. |
| KDO-0033 | NoProductSchemaAsOntology | `MUST NOT` | A product table, prompt variable or legacy object name MUST NOT become a universal Kernel object merely because it exists. |
| KDO-0034 | NoDomainMethodUniversalization | `MUST NOT` | A family, education, counseling or cultural method MUST NOT become a universal object without cross-scene admission review. |
| KDO-0035 | SerializationNeutrality | `MAY` | Implementations MAY use relational, graph, document, event-sourced or other storage when semantic/lifecycle obligations remain verifiable. |
| KDO-0036 | MigrationAndCompatibility | `MUST` | A breaking object change MUST define identity continuity, field migration, lineage, coexistence, rollback, affected-person impact and dependent lifecycle changes. |

## 5. Common envelope and data model

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

## 6. Canonical object catalog

| ID | Object type | Category | Minimum semantic fields | Boundary |
|---|---|---|---|---|
| KOT-0001 | ImplementationBoundary | Governance | implementation_id, version, governed_surfaces, accountable_organization_ref, accountable_human_role_ref, version_set_ref, review_at | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0002 | VersionSet | Governance | family_version, document_versions, source_statuses, rfc_versions, profile_versions, supersedes_ref | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0003 | EntityRef | Identity | entity_kind, safe_label, resolution_scope | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0004 | PersonRef | Identity | resolution_scope, access_class, correction_route | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0005 | OrganizationRef | Identity | responsibility_scope, contact_route, jurisdiction_scope | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0006 | SystemComponentRef | Identity | component_type, provider, version, capability_status, limitations | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0007 | RoleAssignment | Authority | entity_ref, role_type, scope, purpose_refs, authority_refs, permissions, prohibitions, conflict_state, review_or_expiry_at | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0008 | RepresentativeAuthority | Authority | representative_ref, subject_ref, authority_type, evidence_refs, permitted_actions, prohibited_actions, purpose_scope, conflict_state, review_or_expiry_at, appeal_route_ref | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0009 | PurposeRecord | Authority | name, description, affected_person_refs, data_categories, allowed_operations, recipients, risk_class, retention_profile_ref, owner_ref, status | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0010 | AuthorityBasisRecord | Authority | basis_category, person_or_representative_ref, purpose_ref, scope, notice_evidence_refs, jurisdiction_profile_ref, review_or_expiry_at, withdrawal_route, exception_ref | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0011 | ParticipationRecord | Agency | person_ref, purpose_ref, decision_ref, participation_condition, preference, communication_support, representative_authority_ref, conflict_state, review_or_expiry_at, appeal_route_ref | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0012 | ContextRecord | Context | scope, time_window, environment, structural_factors, source_refs, uncertainty_refs, access_class | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0013 | RelationshipRecord | Context | party_refs, relationship_type, perspective_sources, effective_interval, conflict_or_asymmetry, visibility_policy | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0014 | EventRecord | Context | event_type, occurred_or_reported_at, participant_refs, source_refs, observation_refs, context_ref, knowledge_status, uncertainty_refs | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0015 | SourceRecord | Knowledge | source_type, speaker_or_component_ref, subject_refs, captured_at, context_ref, authority_scope, integrity_metadata | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0016 | KnowledgeItem | Knowledge | knowledge_type, subject_refs, source_refs, content_or_safe_reference, evidence_refs, uncertainty_refs, purpose_refs, materiality_class, impact_class, confirmation_state, contestation_state, review_at, supersedes_refs | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0017 | EvidenceRecord | Knowledge | evidence_type, source_refs, supports_or_challenges_refs, collected_at, method, limitations, access_class, retention_profile_ref | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0018 | UncertaintyRecord | Knowledge | related_record_refs, unknowns, alternatives, confidence_basis, limitations, review_condition, dissent_refs | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0019 | DecisionRecord | Decision | decision_type, affected_person_refs, proposal_refs, evidence_refs, uncertainty_refs, impact_assessment_ref, authority_refs, accountable_human_role_ref, selected_option, reason, review_at, appeal_route_ref, status | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0020 | ActionRecord | Decision | decision_ref, actor_ref, authority_refs, target_refs, purpose_refs, action_type, scope, expected_effects, risk_refs, reversibility, review_or_end_at, status, rollback_plan_ref | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0021 | FeedbackRecord | Decision | action_or_record_refs, source_ref, affected_person_ref, observed_at, content_or_safe_reference, knowledge_status, requested_change, access_class | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0022 | OutcomeRecord | Decision | action_ref, observed_at, indicator_or_description, source_refs, evidence_refs, uncertainty_refs, expected_or_unexpected, harm_or_benefit, revision_required | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0023 | DataAssetRecord | DataRights | subject_refs, source_refs, data_category, sensitivity, storage_locations, purpose_refs, authority_basis_refs, authorized_roles, retention_profile_ref, derived_asset_refs, backup_handling, rights_route_ref | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0024 | MemoryRecord | DataRights | subject_refs, source_refs, knowledge_item_refs, purpose_refs, authority_basis_refs, active_use_refs, visibility_policy, retention_profile_ref, correction_state, restriction_state, deletion_state, review_at | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0025 | RightsRequest | DataRights | request_type, requester_ref, subject_refs, representative_authority_ref, scope, received_at, responsible_owner_ref, status, located_asset_refs, exception_refs, completion_evidence_refs, appeal_ref | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0026 | RetentionProfile | DataRights | purpose_ref, covered_asset_types, start_event, review_interval, deletion_or_archival_trigger, backup_handling, exception_categories, owner_ref, jurisdiction_profile_ref | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0027 | RiskSignal | Safety | source_refs, subject_refs, reporter_ref, occurred_or_reported_at, category, evidence_refs, uncertainty_refs, current_or_historical, model_or_policy_version | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0028 | RiskAssessment | Safety | signal_refs, risk_level, immediacy, potential_harm, protective_factors, unknowns, least_intrusive_alternative, responsible_reviewer_ref, next_review_at | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0029 | SafetyAction | Safety | assessment_ref, actor_ref, authority_scope, action, affected_person_refs, scope, duration, notice, proportionality_record_ref, review_at, appeal_route_ref, status | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0030 | HandoffRecord | Safety | service_profile_ref, responsible_role_ref, target_person_or_service_ref, initiated_at, acknowledged_at, accepted_at, information_disclosed, authority_basis_refs, status, failed_handoff_action_ref, closure_reason | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0031 | ResourceAvailabilityRecord | Safety | resource_class, service_scope, location, language_and_accessibility, source_refs, verified_by_ref, verification_method, verified_at, expires_at, stale_behavior, owner_ref, status | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0032 | IncidentRecord | Accountability | severity, harm_or_near_miss, affected_person_refs, timeline_refs, source_and_evidence_refs, responsible_role_refs, containment_actions, root_causes, privacy_impact, remediation_refs, status, closure_authority_ref | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0033 | AppealRecord | Accountability | appellant_ref, challenged_record_refs, grounds, submitted_at, independent_reviewer_ref, conflict_check, interim_restrictions, decision_ref, remediation_refs, status | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0034 | ExceptionRecord | Accountability | requirement_or_policy_refs, authority_basis, scope, affected_person_refs, reason, evidence_refs, risk_and_safeguards, expires_or_reviews_at, owner_ref, independent_review_ref, appeal_route_ref, status | Implementation-neutral semantic object; no status or authority inferred from existence. |
| KOT-0035 | AuditEvent | Accountability | event_type, actor_or_component_ref, role_assignment_ref, target_record_refs, action, purpose_refs, authority_refs, occurred_at, result, previous_and_new_state, evidence_refs, access_class, integrity_metadata | Implementation-neutral semantic object; no status or authority inferred from existence. |

## 7. Relationship model

```text
EntityRef → RoleAssignment → Authority/Purpose/Participation
SourceRecord → KnowledgeItem → DecisionRecord → ActionRecord
ActionRecord → FeedbackRecord/OutcomeRecord → revision
RiskSignal → RiskAssessment → SafetyAction/Handoff → Incident/Appeal
DataAsset/Memory → RightsRequest/Retention → completion or exception
```

No relationship creates authority merely because it exists.

## 8. Human agency and ethics

The model MUST NOT reduce a person to a role, profile, risk state, diagnosis,
relationship position, behavior target or model output. Correction, context,
refusal, participation and appeal remain representable without an account.

## 9. Privacy and consent

Objects use minimum necessary references and access classes. Purpose, authority,
consent, participation, representative scope, retention, deletion, exception
and audit remain distinct. Restricted content may be held in a governed evidence
system while ordinary objects expose safe references.

## 10. Safety and escalation

Signal, assessment, action, handoff, resource, incident and appeal are separate
objects. A sent message is not accepted handoff; risk is not permanent identity.

## 11. Draft review criteria

Review tests semantic necessity, minimization, affected-person usability,
cross-language clarity, RFC/Profile compatibility, field-level access,
migration and failure modes.

## 12. Non-normative examples

A parent report remains a SourceRecord linked to a KnowledgeItem, not the
child's fact. A generated referral creates an initiated HandoffRecord, not
acceptance. A correction revises active Memory/Decision while retaining lineage.

## 13. Limitations and open questions

Identity resolution, high-impact thresholds, jurisdictional authority,
deletion/audit balance, confidence, encryption and extension compatibility
remain open in REF-0038.

## 14. Version and change history

| Version | Date | Change | Status |
|---|---|---|---|
| 0.1.0-draft.1 | 2026-07-15 | Initial 35-object, 36-requirement semantic model | Draft |

## 15. Current boundary

```text
Object types: 35
Object requirements: 36
External/implementation review: not executed
Current conforming products: 0
Overall: NoCurrentKernelConformanceClaim
```
