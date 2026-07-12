---
id: GOV-0009
title: Family OS Implementation-to-Charter Mapping
status: Accepted
version: 1.0.0-alpha.5
layer: Layer 5 — Community & Governance
owner: MingOS Project Governance
created: 2026-07-12
updated: 2026-07-12
related:
  - MF-0004
  - PROJECT-MINGOS-0002
  - GOV-0002
  - GOV-0006
  - GOV-0007
  - GOV-0010
  - GOV-0011
  - GOV-0012
  - GOV-0013
depends_on:
  - GOV-0006
---

# GOV-0009 — Family OS Implementation-to-Charter Mapping

## 1. Scope

This mapping evaluates current Family OS implementation evidence against the Candidate Charters.

Primary source:

- `SRC-0012` — `CODE_WIKI.md`, repository snapshot dated 2026-07-09.

Supporting source:

- `SRC-0013` — structured architecture and deployment evidence.

## 2. Evidence limitation

This is a documentary implementation audit.

The Day 5 review did not receive a current direct source checkout, execute the test suite, inspect production data, or verify current deployed behavior. Modules and tests described in the snapshot may have changed.

“Supported” means supported by the snapshot, not independently proven in production.

## 3. Positive implementation evidence

| Capability | Evidence in snapshot | Charter relationship | Finding |
|---|---|---|---|
| Unified safety gate | Red, yellow, orange, green risk handling; professional escalation | C08, MC11 | Strong documentary support |
| Observation before action | Serial judgment and staged response before framework output | C07, C09, MC06 | Strong documentary support |
| Relationship-sensitive response | Parent state, relationship temperature, loop detection | C07, MC01 | Supported |
| Small and reversible action | Four-step process includes small action and follow-up | C06, MC03 | Supported |
| Anti-manipulation | `kernel-guard` anti-manipulation and warm-control checks | C01, C02, MC07, MC09 | Supported |
| Refusal and absence | Life State decline and absence routes; silent 204 behavior | C04, MC03 | Supported but scope limited |
| Correction and uncertainty stores | `corrections`, `failures`, `unknowns`, `sp_versions` | C09, C12, MC05, MC13 | Strong base |
| Safety and quality review | Quality gate, science-review gate, warmth keeper | C01, C08, MC11 | Supported |
| Security boundaries | Parent/admin process separation, independent sessions, authentication, rate limits, CSRF, hidden admin | C11, MC04 | Supported for application security |
| Test coverage | 117 test files including safety, privacy, red team, science review, E2E, resilience | C12, MC13 | Strong process evidence |
| Escalation | Escalation route, logs, crisis/escalation branches | C08, MC11 | Supported but accountability incomplete |
| Feedback loop | Feedback, cases, weekly analysis, rule candidates | C12, MC13 | Supported with privacy conditions |

## 4. Partial or conflicting implementation evidence

| Area | Evidence | Charter concern | Finding |
|---|---|---|---|
| Family profiles | `family_profiles`, `family-profile-system`, profile writeback | C03, C09, C13, MC06, MC10 | Risk of freezing identity if provenance, confidence, expiry, confirmation, and contestability are incomplete |
| Family stages | Five-stage classification | C03, C05 | May become ranking or fixed identity without temporal and non-judgment rules |
| Parent-created child understanding | Parent is primary operator | C13, MC10 | No complete child or third-party voice mechanism evidenced |
| Knowledge-status data model | Judgment engine metadata exists | C09, MC06 | No complete proof that every stored assertion distinguishes fact, observation, hypothesis, pattern, judgment, and decision |
| User-facing correction | Corrections table and memory-candidate delete route exist | C04, C11, MC03, MC04 | No complete user-facing inspection, appeal, history, export, or comprehensive deletion flow evidenced |
| Case records | Per-family cases and summaries | C11, C13, MC04, MC10 | Consent, minimization, de-identification, access, reuse, and retention not established |
| Cross-family analyzer | Cross-family pattern analysis | C11, C13, MC04, MC10 | High privacy and re-identification risk without strict governance |
| Single source of truth | Multiple frontends, H5, enterprise WeChat, Life State, parent/admin channels | MC04, MC06 | Unified identity, consent, memory, and audit core is not evidenced as complete |
| AI disclosure | DeepSeek-backed response generation | C10, MC09 | No complete UI evidence that generated/inferred content and model limitations are visible |
| Commercial restraint | Product and tier structures exist | MC07, MC08, MC12 | No implemented tests proving no anxiety-based conversion or dependency-based retention |
| Charter enforcement | Audit and monitoring components exist | MC14 | No complete Charter-violation intake, remediation, suspension, and appeal workflow evidenced |
| Data protection at rest | SQLite and file-based runtime stores | C11, MC04 | Encryption, backup access, retention schedules, key governance, and restricted-store boundaries not evidenced |
| Human-support accountability | Admin and escalation tooling exist | MC09, MC11, MC14 | Qualification, assignment, minimum access, conflict declarations, and full modification audit not evidenced |

## 5. Charter theme assessment

| Theme | State |
|---|---|
| Understanding before advice | Supported |
| Relationship and context | Supported |
| Safety and escalation | Partial-to-strong |
| Refusal and non-coercion | Partial |
| Fact versus inference | Partial |
| Memory correction and change | Partial |
| Child and third-party rights | Material gap |
| Privacy and data rights | Material gap |
| Anti-manipulation | Supported at response layer; commercial layer unverified |
| Capability over dependency | Principle present; outcome and business tests absent |
| Failure and unknown preservation | Supported |
| Enforcement and appeal | Material gap |
| Single source of truth | In progress / gap |

## 6. Implementation decision

Family OS provides credible implementation evidence for the Charter direction.

It does not yet prove full Charter conformance.

The implementation SHOULD be treated as:

> A valuable Ming Family and MingOS Core seed whose safety, judgment, feedback, and correction mechanisms should be preserved, while privacy, third-party rights, profile semantics, cross-channel identity, and enforcement are redesigned or completed.

## 7. Direct audit requirements

A future direct code audit MUST verify:

- schema fields and migrations;
- actual profile assertion provenance and expiry;
- child/third-party data handling;
- every data-rights route and authorization rule;
- case and cross-family de-identification;
- safety escalation ownership and notifications;
- model disclosure in the UI;
- commercial and retention mechanics;
- audit immutability and access;
- current test results;
- production configuration without exposing secrets or personal data.
