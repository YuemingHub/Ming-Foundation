---
created: 2026-07-12
depends_on:
- GOV-0022
- GOV-0023
- GOV-0024
id: GOV-0025
layer: Layer 5 — Community & Governance
owner: Ming Foundation Architecture
related:
- GOV-0019
- GOV-0020
- GOV-0021
- GOV-0022
- GOV-0023
- GOV-0024
- GOV-0026
- ADR-0008
status: Accepted
title: Day 7 Remediation Implementation Backlog
updated: 2026-07-12
version: 1.0.0-alpha.7
---

# GOV-0025 — Day 7 Remediation Implementation Backlog

## 1. Purpose

This backlog translates Day 7 findings into bounded implementation work.

Owner values are role owners, not assumed named people.

## 2. Priority model

- **P0** — required to reduce immediate Charter, privacy, safety, or
  truthfulness risk;
- **P1** — required for complete conformance and reliable operation;
- **P2** — longer-term transparency, measurement, and governance
  maturity.

## 3. Access and audit prerequisites

| ID         | Priority | Owner role            | Target                             | Task                                                                                                        | Acceptance criteria                                                                                       | Evidence                                     |
|------------|----------|-----------------------|------------------------------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------|
| D7-ENG-001 | P0       | Repository Steward    | Website and Family OS repositories | Register current repository, branch, commit, build/test commands, deployment relationship, and audit access | `GOV-0002` has current source locator; audit role can read required code without secrets or personal data | Commit SHAs and access record                |
| D7-ENG-002 | P0       | Quality Engineering   | Family OS                          | Run current RFC and counterexample audit test suite on a non-production environment                         | Results for RFC-0001 to RFC-0005 and CE-001 to CE-020; failures preserved                                 | Test command, revision, environment, results |
| D7-ENG-003 | P1       | Operations            | `mingos.cn` and `ymai.love`        | Produce bounded runtime evidence                                                                            | Routes, headers, version, uptime, form behavior, error state, current deployment commit                   | De-identified runtime audit                  |
| D7-ENG-004 | P1       | AI Platform           | Model integration                  | Add model/provider/version conformance gate                                                                 | Provider or model change triggers regression suite and review                                             | Version record and failing-change test       |
| D7-ENG-005 | P1       | Reporting Engineering | Reports and summaries              | Make unknowns and evidence coverage visible                                                                 | Reports cannot omit material unknowns without trace                                                       | Report test and audit record                 |

## 4. Website backlog

| ID         | Priority | Owner role                       | Target                                       | Task                                                                                            | Dependencies | Acceptance criteria                                                           |
|------------|----------|----------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------|--------------|-------------------------------------------------------------------------------|
| D7-WEB-001 | P0       | Website Engineering + Governance | `/charter` and normative pages               | Add source ID, status, version/commit, last sync, and summary status                            | D7-ENG-001   | Public page matches repository Candidate status and links to governing source |
| D7-WEB-002 | P0       | Product + Website                | Home, architecture, ecosystem, product pages | Label capabilities Available, Pilot, Experimental, Planned, Vision, Paused, or Retired          | RFC-0005     | No future capability is grammatically presented as current                    |
| D7-WEB-003 | P0       | Privacy + Website                | Early-access and contact forms               | Add purpose, fields, recipient, retention, request route, and sensitive-data prohibition        | RFC-0002     | Form blocks or warns against child, medical, crisis, and case detail          |
| D7-WEB-004 | P0       | Safety + Website                 | All sensitive-use entry points               | Add AI, human-review, professional, emergency, diagnosis, legal, and response boundaries        | RFC-0003     | Boundaries appear before sensitive submission or use                          |
| D7-WEB-005 | P1       | Governance + Website             | Footer and policy pages                      | Add correction, privacy, Charter-concern, and stale-information reporting routes                | GOV-0015     | Reports receive traceable IDs and route correctly                             |
| D7-WEB-006 | P1       | Website Engineering              | Build and release                            | Create repository-to-site normative-page manifest and stale-source release check                | D7-WEB-001   | Stale Charter metadata fails build or blocks release                          |
| D7-WEB-007 | P1       | Accessibility                    | Entire site                                  | Execute keyboard, screen-reader, contrast, reduced-motion, mobile, and Chinese typography audit | D7-ENG-001   | Recorded WCAG-oriented findings and resolved P0 accessibility issues          |

## 5. Subject, profile, and data-rights backlog

| ID          | Priority | Owner role                   | Target                                                           | Task                                                                                                                                  | Dependencies | Acceptance criteria                                                            |
|-------------|----------|------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|--------------|--------------------------------------------------------------------------------|
| D7-DATA-001 | P0       | Data Architecture            | `src/models/db.js`, family profile and judgment services         | Implement subject, speaker, assertion, status, evidence, confidence, uncertainty, validity, confirmation, dispute, and revision model | RFC-0001     | Parent report and model inference cannot be stored as subject-confirmed fact   |
| D7-DATA-002 | P0       | Product + Data Rights        | Parent UI, future subject route, admin review                    | Implement contest, contextualize, restrict, correct, expire, and appeal workflow                                                      | D7-DATA-001  | Disputed high-impact assertion is visible and can be paused/reviewed           |
| D7-DATA-003 | P0       | Privacy Architecture         | All channels                                                     | Implement purpose registry and permission/processing-basis records                                                                    | RFC-0002     | Every sensitive data use maps to current purpose and basis                     |
| D7-DATA-004 | P0       | Data Rights                  | API, UI, primary and derived stores                              | Implement access, source explanation, correction, export, deletion, restriction, withdrawal, and appeal                               | D7-DATA-003  | Request completes across primary, index, derived, and backup schedule          |
| D7-DATA-005 | P0       | Data Governance + Operations | SQLite, file stores, backups, logs                               | Define retention and exception registry                                                                                               | D7-DATA-003  | Each store has purpose, owner, access, retention, deletion, backup, and review |
| D7-DATA-006 | P0       | Identity Architecture        | Parent, H5, Life State, enterprise WeChat, professional channels | Establish one identity, permission, memory, and audit source                                                                          | D7-DATA-003  | Revocation and correction propagate across linked channels                     |
| D7-DATA-007 | P1       | Product Governance           | `family-stage.js` and profile UI                                 | Prevent stage ranking, shame, and permanent identity                                                                                  | D7-DATA-001  | Stage is temporal, purpose-limited, non-comparative, correctable, and expiring |
| D7-DATA-008 | P1       | Security + Data Governance   | Admin and professional access                                    | Add case-scoped least privilege, access expiry, conflict declaration, and access review                                               | D7-DATA-003  | Secure admin access no longer implies broad organizational access              |

## 6. Safety and professional backlog

| ID          | Priority | Owner role              | Target                                             | Task                                                                                                    | Dependencies       | Acceptance criteria                                                                 |
|-------------|----------|-------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------|-------------------------------------------------------------------------------------|
| D7-SAFE-001 | P0       | Safety Operations       | `safety-gate.js`, `/api/escalate`, escalation logs | Implement accountable handoff record, acknowledgment, failed-handoff state, scope, duration, and review | RFC-0003           | P0/P1 escalation cannot close without acknowledgment or explicit failure            |
| D7-SAFE-002 | P0       | Safety Quality          | Tests, incidents, monitoring                       | Implement false-positive, false-negative, near-miss, and root-cause review                              | D7-SAFE-001        | Every material safety incident can change policy, prompt, code, access, or training |
| D7-SAFE-003 | P0       | Safety + Data Rights    | User and admin interfaces                          | Implement safety classification correction and appeal                                                   | D7-SAFE-001        | Wrong classifications are corrected downstream and do not become permanent labels   |
| D7-SAFE-004 | P0       | Safety + AI Quality     | AI output and public UI                            | Enforce professional and diagnostic boundaries with scenario tests                                      | D7-ENG-002         | CE-019 and related tests pass across ordinary, vulnerable, and crisis contexts      |
| D7-SAFE-005 | P0       | Safeguarding            | Parent/child disclosure and access                 | Define age-aware confidentiality, parent access exceptions, and independent review                      | RFC-0001, RFC-0003 | CE-016 tabletop and product acceptance tests pass                                   |
| D7-PRO-001  | P1       | Professional Governance | Professional workspace                             | Require source/status visibility, human attestation, qualification, conflict, and override audit        | D7-DATA-001        | Professional cannot silently convert AI hypothesis into verified fact               |

## 7. Case, learning, and commercial backlog

| ID          | Priority | Owner role            | Target                                                     | Task                                                                                               | Dependencies       | Acceptance criteria                                                         |
|-------------|----------|-----------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------|
| D7-CASE-001 | P0       | Evidence Governance   | Case records, flywheel, analyst access                     | Implement evidence zones and case-scoped access                                                    | RFC-0004           | Operational cases are separated from validation and aggregate evidence      |
| D7-CASE-002 | P0       | Privacy Engineering   | Cross-family analyzer and exports                          | Add de-identification, rarity review, minimum cohort, suppression, and re-identification review    | D7-CASE-001        | CE-005 tests prevent rare-family exposure                                   |
| D7-CASE-003 | P0       | AI/Data Governance    | Model training, evaluation, retrieval, and evidence export | Add separate approval, provider controls, withdrawal lineage, export expiry, and deletion evidence | D7-CASE-001        | Case data cannot reach model or external reviewer without governed approval |
| D7-COM-001  | P1       | Commercial Governance | Pricing, sales, retention, notifications                   | Add anti-anxiety and anti-dependency review and metrics                                            | RFC-0005, GOV-0015 | CE-006, CE-011, and CE-012 have testable controls and review records        |

## 8. Charter governance backlog

| ID         | Priority | Owner role             | Target                        | Task                                                                                  | Dependencies | Acceptance criteria                                             |
|------------|----------|------------------------|-------------------------------|---------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------|
| D7-GOV-001 | P0       | Governance Operations  | Public and internal reporting | Implement Charter, privacy, and safety concern intake with IDs and containment triage | GOV-0015     | Reporter receives status and ongoing harm can be contained      |
| D7-GOV-002 | P0       | Independent Governance | Leadership and conflict cases | Establish independent case owner, conflict rules, protection, and appeal              | D7-GOV-001   | Founder/partner tabletop can proceed without conflicted control |
| D7-GOV-003 | P1       | Governance Board       | Outcomes and transparency     | Define sanctions, suspension, naming withdrawal, reinstatement, and safe transparency | D7-GOV-002   | Material violation has enforceable and appealable consequences  |

## 9. Recommended implementation order

``` text
Wave 0 — Access and audit reproducibility
D7-ENG-001, D7-ENG-002

Wave 1 — P0 truth and rights
D7-DATA-001 to D7-DATA-006
D7-WEB-001 to D7-WEB-004

Wave 2 — P0 safety and evidence
D7-SAFE-001 to D7-SAFE-005
D7-CASE-001 to D7-CASE-003

Wave 3 — Governance enforcement
D7-GOV-001, D7-GOV-002
D7-PRO-001

Wave 4 — Release and maturity
D7-WEB-005 to D7-WEB-007
D7-DATA-007, D7-DATA-008
D7-COM-001, D7-GOV-003
D7-ENG-003 to D7-ENG-005
```

## 10. Backlog completion rule

A task is not complete until:

- current code or product behavior exists;
- acceptance tests pass;
- revision and environment are recorded;
- required independent or affected-person review is complete;
- restricted evidence is handled safely;
- the traceability matrix is updated.
