---
id: GOV-0012
title: Charter Counterexample and Risk Register
status: Accepted
version: 1.0.0-alpha.5
layer: Layer 5 — Community & Governance
owner: Ming Foundation Governance
created: 2026-07-12
updated: 2026-07-12
related:
  - MF-0004
  - PROJECT-MINGOS-0002
  - GOV-0006
  - GOV-0007
  - GOV-0009
  - GOV-0010
  - GOV-0011
  - GOV-0013
depends_on:
  - GOV-0006
---

# GOV-0012 — Charter Counterexample and Risk Register

## 1. Purpose

This register records scenarios capable of exposing weaknesses in the Candidate Charters or their implementation.

A counterexample is not an argument against the project. It is protected evidence that prevents the Charter from becoming self-confirming doctrine.

## 2. Register

| ID | Scenario | Charter tension | Failure mode | Required control or evidence | Priority |
|---|---|---|---|---|---|
| CE-001 | A parent describes a child as lazy and manipulative | C03, C09, C13, MC06, MC10 | Parent narrative becomes permanent child identity | Source-qualified observation, child/third-party contestability, expiry, counterevidence | P0 |
| CE-002 | A child faces imminent self-harm risk but refuses intervention | C04, C08, MC03, MC11 | Absolute autonomy prevents necessary protection | Narrow emergency exception, responsible actor, time limit, review | P0 |
| CE-003 | Safety gate interprets ordinary adolescent language as crisis | C04, C08, C09 | Surveillance, loss of trust, permanent risk label | False-positive review, appeal, no permanent identity promotion | P0 |
| CE-004 | Parent requests deletion after a serious safety incident | C11, MC04 | Either accountability is erased or data is retained indefinitely | Purpose-limited retention, access restriction, explanation, review date | P0 |
| CE-005 | A rare family case is recognized in cross-family analysis | C11, C13, MC04, MC10 | Re-identification or unauthorized secondary use | De-identification, rarity review, minimum cohort, restricted output | P0 |
| CE-006 | Warm, empathic AI becomes the user’s primary emotional attachment | C10, MC08, MC09 | Dependency is interpreted as retention success | Dependency indicators, healthy-exit design, human relationship strengthening | P1 |
| CE-007 | A professional accepts an AI summary without checking source | C09, C10, MC06, MC09, MC11 | Inference becomes professional fact | Source visibility, review status, responsible actor, uncertainty | P0 |
| CE-008 | Website describes a complete Life OS while only bounded components exist | C01, C02, MC05, MC12 | Vision becomes misleading current claim | Public status labels, canonical links, claim review | P0 |
| CE-009 | Early-access form receives identifiable child mental-health details | C11, C13, MC04, MC10 | Sensitive data collected outside governed intake | Clear prohibition, minimized fields, privacy notice, secure intake route | P0 |
| CE-010 | Family-stage model is used to rank or shame families | C03, C05, C06 | Temporary state becomes status hierarchy | Temporal language, no ranking, user correction, service-purpose limitation | P1 |
| CE-011 | A commercial team highlights risk to sell a higher tier | C02, MC07, MC12 | Anxiety becomes conversion mechanism | Marketing review, risk/offer separation, audit, sanctions | P0 |
| CE-012 | The user grows but the product repeatedly prompts continued dependence | C06, MC08 | Capability improvement conflicts with revenue | Outcome metrics, reduced-use success, exit and pause design | P1 |
| CE-013 | Website Charter and repository Charter diverge | C01, C09, MC05, MC13 | Public trust is based on stale commitments | Version metadata, synchronization check, non-normative summary label | P0 |
| CE-014 | Model provider changes and response behavior shifts | C10, MC09, MC13 | Model behavior silently rewrites practical doctrine | Model/version records, regression tests, conformance gates | P1 |
| CE-015 | Human reviewer overrides a user correction without trace | C04, C09, C11, MC03, MC04, MC13 | Institutional authority erases the person’s voice | Audit, reason, appeal, original record preservation | P0 |
| CE-016 | Child disclosure conflicts with parent access rights | C04, C08, C11, C13, MC10, MC11 | Either child safety/privacy or family transparency is harmed | Age-aware confidentiality, safety exceptions, independent review | P0 |
| CE-017 | Unknown evidence is omitted to make weekly reports coherent | C01, C09, C12, MC05 | Narrative confidence replaces truth | Unknown display, confidence, evidence coverage, reviewer challenge | P1 |
| CE-018 | Admin access is secure technically but too broad organizationally | C11, MC04, MC14 | Least privilege fails despite hidden admin route | Role-level authorization, case scope, access expiry, access review | P1 |
| CE-019 | AI offers medical or diagnostic interpretation during a vulnerable moment | C08, C10, MC09, MC11 | Boundary language fails under conversational pressure | Output checks, refusal, escalation, professional disclaimer | P0 |
| CE-020 | Founder or partner is accused of Charter violation | C01, MC05, MC12, MC14 | Governance protects authority rather than affected people | Independent intake, conflict management, suspension, public rationale | P0 |

## 3. Use

Each high-priority counterexample SHOULD become:

- a test case;
- a policy scenario;
- a product acceptance criterion;
- an audit question;
- or an external-review prompt.

A risk is not closed because a document says the correct thing. Closure requires evidence.
