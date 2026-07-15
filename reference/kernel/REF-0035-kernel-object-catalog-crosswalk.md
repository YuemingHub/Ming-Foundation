---
id: REF-0035
title: Kernel Object Catalog and Core Requirement Crosswalk
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
  - KERNEL-0001
  - KERNEL-0002
  - KERNEL-0003
  - REF-0036
  - REF-0037
  - REF-0038
  - REF-0039
depends_on:
  - KERNEL-0002
---

# REF-0035 — Kernel Object Catalog and Core Requirement Crosswalk

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

| KCR range | Primary object groups |
|---|---|
| KCR-0001–0011 | Boundary, identity, roles, authority, purpose, participation |
| KCR-0012–0017 | Source, knowledge, evidence, uncertainty, event and context |
| KCR-0018–0021 | Decision, action, feedback and outcome |
| KCR-0022–0026 | Risk, safety, handoff, resource, incident and appeal |
| KCR-0027–0030 | Data asset, memory, rights, retention and exception |
| KCR-0031–0036 | Components, accountability, audit and version set |

A new canonical object requires cross-scene necessity, source/KCR mapping,
access/retention/lifecycle analysis, affected-person review and migration.
