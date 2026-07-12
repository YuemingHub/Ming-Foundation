---
id: GOV-0005
title: Day 4 Charter Article Review and Decision Record
status: Accepted
version: 1.0.0-alpha.4
layer: Layer 5 — Community & Governance
owner: Ming Foundation Governance
created: 2026-07-12
updated: 2026-07-12
related:
  - MF-0004
  - PROJECT-MINGOS-0002
  - ADR-0005
  - GOV-0004
  - GOV-0006
depends_on:
  - GOV-0004
  - ADR-0005
---

# GOV-0005 — Day 4 Charter Article Review and Decision Record

## 1. Purpose

This record documents the Day 4 internal article-by-article review of the Charter of Life and MingOS Charter.

The review decides what is retained, revised, added, accepted as an architectural boundary, and deferred to external or implementation validation.

## 2. Decision summary

Day 4 decides:

1. accept the three-layer separation in `ADR-0005`;
2. move `MF-0004` from `Draft` to `Candidate`;
3. move `PROJECT-MINGOS-0002` from `Draft` to `Candidate`;
4. retain neither Charter as `Accepted` or `Stable`;
5. require the validation plan in `GOV-0006`;
6. begin no canonical complete Kernel specification until Candidate validation produces sufficient evidence.

## 3. Charter of Life review

| Article | Disposition | Day 4 decision |
|---|---|---|
| C01 Truth before theory | Retain | Foundational and consistent with evidence-aware governance |
| C02 Life before system and efficiency | Retain | Necessary constraint against metric and institutional domination |
| C03 A person is not a problem set | Retain | Core anti-reduction principle |
| C04 Agency cannot be transferred away | Revise | Clarified that imminent-harm duties require narrow, documented, reviewable intervention |
| C05 Ordinary and slow lives retain dignity | Retain | Prevents achievement and productivity from becoming measures of worth |
| C06 Growth cannot be manufactured | Retain | Preserves the difference between supporting conditions and coercing outcomes |
| C07 Relationship and context are part of life | Retain | Required for non-isolated interpretation |
| C08 Safety without domination | Revise | Added basis, responsible actor, scope, duration, and challenge requirements |
| C09 Interpretation remains provisional | Retain | Supports knowledge-status separation and correction |
| C10 Technology must serve life | Retain | Correctly bounds AI and automation |
| C11 Memory preserves change and rights | Revise | Added accountable exceptions for lawful retention, safety, incidents, duties, and protection of others |
| C12 Failure, counterexample, and unknown are protected | Retain | Required for epistemic humility and institutional correction |
| C13 No person is fully represented by another’s account | Add | Resolves the child and third-party voice gap identified in Day 3 |

## 4. MingOS Charter review

| Commitment | Disposition | Day 4 decision |
|---|---|---|
| MC01 Stand with life, not a role | Retain | Prevents automatic alignment with operator or purchaser |
| MC02 MingOS owns no life | Retain | Establishes non-ownership boundary |
| MC03 Refuse, pause, and leave | Revise | Added narrow, explicit exceptions rather than absolute language |
| MC04 Data and memory accountability | Revise | Added explanation duties when deletion or revocation is limited |
| MC05 Evidence above authority | Retain | Applies to founder, expert, institution, and model |
| MC06 Knowledge statuses remain distinct | Retain | Prevents inference becoming fact |
| MC07 No anxiety for conversion | Retain | Mandatory commercial restraint |
| MC08 No dependency for retention | Retain | Aligns success with capability rather than attachment |
| MC09 AI remains bounded | Retain | Preserves human responsibility and affected-person participation |
| MC10 Children and third parties protected | Retain | Required for non-operator rights |
| MC11 Professional and safety boundaries visible | Retain | Prevents role and competence misrepresentation |
| MC12 Commercial power cannot amend roots | Revise | Added independent review of material commercial conflicts |
| MC13 MingOS remains correctable | Retain and strengthen | Linked to incident, appeal, version, and audit mechanisms |
| MC14 Violations require response and remediation | Add | Prevents the Charter from remaining unenforceable branding |

## 5. Cross-cutting revisions

Day 4 adds:

- explicit Candidate status;
- conflict and exception recording;
- emergency-safety qualification without unlimited authority;
- deletion and retention accountability;
- affected-person voice where one person describes another;
- decision precedence;
- violation, remediation, and traceability duties;
- a defined validation gate before acceptance.

## 6. Rejected directions

Day 4 rejects:

- marking either Charter `Accepted` solely because an internal review was completed;
- treating the founder’s approval as sufficient external validation;
- using absolute autonomy language that ignores imminent danger and lawful protective duties;
- presenting deletion rights without acknowledging narrow accountability and legal exceptions;
- leaving Charter violations without a response process;
- starting broad SDK, cloud, certification, or ecosystem expansion before validation.

## 7. Unresolved and external-review items

The following remain unresolved:

- jurisdiction-specific legal language;
- precise child assent, consent, and contestability mechanisms;
- independent reviewer composition and authority;
- emergency-risk thresholds and escalation rules;
- data-retention schedules;
- sanctions, suspension, and reinstatement for non-conforming implementations;
- public use of the MingOS name and certification-like claims;
- whether every higher-order article is universal or should be reframed as a Ming Foundation commitment.

## 8. Definition of Day 4 completion

Day 4 is complete when:

- `ADR-0005` is Accepted;
- both Charters are revised and marked Candidate;
- every prior article has a recorded disposition;
- new articles address identified gaps;
- a validation plan exists;
- entry points, status, and changelog are updated;
- repository validation passes.

Completion of Day 4 is not acceptance of the Charters.
