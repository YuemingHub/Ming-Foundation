---
id: PROF-0001
title: Participation and Representative Decision Profile
status: Proposed
version: 0.2.0-draft.1
layer: Layer 1 — Standards
owner: Ming Foundation Standards
created: 2026-07-12
updated: 2026-07-13
related:
  - RFC-0001
  - RFC-0002
  - GOV-0055
  - GOV-0058
  - ADR-0016
  - GOV-0061
  - GOV-0066
  - GOV-0071
  - GOV-0072
  - GOV-0076
  - GOV-0077
  - ADR-0019
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
## 7. Non-hierarchical and purpose-specific semantics

P0 through P5 are participation conditions for one named purpose and decision.

They MUST NOT be used as a score of:

- intelligence;
- maturity;
- compliance or obedience;
- mental health;
- trustworthiness;
- family value;
- general decision-making ability;
- entitlement to dignity, care, privacy, or support.

A lower participation condition for one purpose MUST NOT automatically lower
participation for another purpose.

A participation record MUST state the exact purpose, decision, scope, start,
review or expiry time, and evidence for the selected condition.

## 8. Supported decision-making, disagreement, and refusal

Before reducing direct participation, the implementation MUST consider
support that could make participation possible, including:

- plain-language explanation;
- smaller decision steps;
- extra time;
- a trusted support person chosen where safely possible;
- interpretation or alternate communication;
- visual, audio, augmentative, or assisted communication;
- a private opportunity to respond;
- a later review when stress or immediate conditions change.

Agreement MUST NOT be inferred from:

- silence;
- distress;
- inability to use the offered channel;
- delayed response;
- representative agreement;
- compliance under pressure.

Disagreement, refusal, correction, uncertainty, or a request for help MUST NOT
create punishment, retaliation, reduced service, or an adverse identity label
unless a separate, documented, proportionate safety or legal duty applies.

## 9. P0 temporary-exclusion safeguards

P0 may be used only when direct notice would create a specific and credible
immediate safety or legal risk that cannot be sufficiently reduced through a
less restrictive participation condition.

Every P0 decision MUST include:

- the specific harm being prevented;
- evidence and uncertainty;
- alternatives considered;
- why P1 through P5 are insufficient;
- minimum excluded information and action;
- conflict-free authorizer;
- support available to the subject;
- the shortest reasonable duration;
- a mandatory review time;
- later-notice conditions;
- correction and appeal routes;
- the person responsible for ending or renewing the restriction.

The authorizer, representative, reporter, and final reviewer SHOULD be
different roles when conflict or high impact is present.

P0 MUST expire automatically unless a new review records a continuing basis.

## 10. Accessibility and communication profile

The participation decision MUST record usable communication support for the
specific person and context.

The support assessment MUST consider:

- language and interpretation;
- literacy and cognitive load;
- disability and assistive technology;
- neurodivergence;
- trauma-sensitive pacing;
- sensory and environmental conditions;
- remote, low-bandwidth, and offline access;
- privacy when a representative or support person is present.

A right that cannot be exercised through an available and usable channel is
not operationally available.

## 11. Purpose-specific scenario tests

An implementation test set MUST include at least:

1. the same person holding P2 for service notice and P5 for optional data use;
2. refusal without penalty;
3. silence that is not treated as agreement;
4. a representative-subject conflict;
5. P0 expiry and later notice;
6. a communication barrier resolved through support;
7. an accessibility failure that blocks the decision;
8. a correction that changes the selected participation condition.

These are source and implementation requirements, not evidence that affected
people have reviewed or accepted the profile.

## 12. Remaining external review

The profile remains Proposed until affected-person, safeguarding,
accessibility, domain, and jurisdiction review are executed and synthesized.

Internal review readiness MUST NOT be represented as participant approval.
