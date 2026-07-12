---
id: PROF-0001
title: Participation and Representative Decision Profile
status: Proposed
version: 0.1.0
layer: Layer 1 — Standards
owner: Ming Foundation Standards
created: 2026-07-12
updated: 2026-07-12
related:
  - RFC-0001
  - RFC-0002
  - GOV-0055
  - GOV-0058
  - ADR-0016
depends_on:
  - RFC-0001
  - ADR-0013
---

# PROF-0001 — Participation and Representative Decision Profile

## Status boundary

This is a Proposed reference profile.

It does not establish universal age thresholds, legal capacity, or
representative authority. A jurisdiction and safeguarding profile remains
required.

## 1. Decision inputs

Every participation decision MUST evaluate:

- subject preference where safely obtainable;
- age and developmental information;
- functional understanding of the specific decision;
- ability to communicate agreement, disagreement, uncertainty, or refusal;
- decision impact and reversibility;
- privacy and disclosure risk;
- immediate safety constraints;
- representative authority and conflict state;
- jurisdiction profile;
- communication and accessibility needs;
- review date.

Age MUST NOT be the sole decision input.

## 2. Participation levels

| Level | Meaning | Minimum evidence |
|---|---|---|
| P0 | Temporarily not directly informed | Documented immediate safety or legal reason, narrow scope, review date, later-notice route |
| P1 | Informed through a representative | Verified representative scope and reason direct notice is not currently appropriate |
| P2 | Directly informed | Comprehensible notice and communication support |
| P3 | May comment, correct, or contextualize | P2 plus a usable response route |
| P4 | May approve or reject a specific optional use | P3 plus demonstrated understanding of purpose and consequence |
| P5 | May restrict or revoke a specific optional use | P4 plus propagation and appeal capability |

A person MAY have different levels for different purposes.

## 3. Impact minimums

- Low-impact, reversible use SHOULD provide at least P2 where feasible.
- Material interpretation SHOULD provide at least P3.
- Optional high-impact use SHOULD require P4 or P5 unless a qualified profile
  records why this is not possible.
- Temporary safety action MAY use P0 only with a documented, expiring
  exception and conflict-free review.
- Refusal or inability to participate MUST NOT be treated as confirmation of
  an assertion.

## 4. Conflict rules

A conflict exists when:

- the representative may benefit from the proposed use;
- the subject alleges harm by the representative;
- the representative requests protected source information;
- the action restricts the subject's rights or access;
- the same role reports, decides, and closes the matter;
- subject and representative preferences materially differ.

High-impact use MUST pause for a conflict-free reviewer unless a documented
immediate duty requires a temporary action.

## 5. Required decision record

```text
participation_decision_id
subject
purpose
impact_class
selected_level
decision_inputs
communication_support
representative_authority_ref
conflict_state
safety_or_legal_constraint
reason
starts_at
reviews_or_expires_at
later_notice_route
appeal_route
reviewer
```

## 6. Review questions

- Are the levels comprehensible to children, adolescents, parents, and
  professionals?
- Which jurisdiction profiles require stronger direct participation?
- Which communication supports are required for disability and language
  access?
- Which decisions must never be delegated solely to a representative?
