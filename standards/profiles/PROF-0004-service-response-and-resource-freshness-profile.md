---
id: PROF-0004
title: Service Response and Resource Freshness Profile
status: Proposed
version: 0.2.0-draft.1
layer: Layer 1 — Standards
owner: Ming Foundation Standards
created: 2026-07-12
updated: 2026-07-13
related:
  - RFC-0003
  - GOV-0055
  - GOV-0058
  - ADR-0016
  - GOV-0061
  - GOV-0066
  - GOV-0071
  - GOV-0075
  - GOV-0076
  - GOV-0077
  - ADR-0019
depends_on:
  - RFC-0003
---

# PROF-0004 — Service Response and Resource Freshness Profile

## Status boundary

This profile defines evidence required before publishing a response promise.

It does not turn MingOS into an emergency service and does not create a
universal response time.

## 1. Service classes

| Class | Meaning | Permitted claim |
|---|---|---|
| S0 — no_handoff | No governed human or service acceptance path | Transparent redirection only |
| S1 — bounded_review | Accountable review exists during published windows | Review target within published operating window |
| S2 — active_handoff | Staffed, governed acknowledgment and acceptance path | Evidence-backed acknowledgment and acceptance targets |
| S3 — unverified | Availability or resource evidence is absent or expired | No current response or monitoring claim |

## 2. Response-target evidence

A published response target MUST identify:

- service class;
- responsible organization and role;
- staffing evidence;
- operating hours and time zone;
- supported locations and languages;
- acknowledgment target;
- acceptance or review target;
- escalation and failed-handoff owner;
- measurement period and performance evidence;
- last verification date;
- expiry date;
- unavailable services.

A target without current staffing or performance evidence MUST be marked
unverified.

## 3. Resource freshness classes

| Resource class | Maximum default verification age |
|---|---|
| F0 — emergency or crisis contact | 30 days |
| F1 — safeguarding, mandated reporting, or urgent professional route | 60 days |
| F2 — professional directory or service availability | 90 days |
| F3 — general educational or non-urgent information | 180 days |

These are conservative publication defaults, not legal mandates.

## 4. Required resource record

```text
resource_id
resource_class
name
location
language
service_scope
source
verified_by
verification_method
verified_at
expires_at
failure_or_staleness_behavior
owner
```

## 5. Stale and failure behavior

An expired or failed resource MUST:

- be removed, quarantined, or visibly marked unavailable;
- stop being presented as current;
- trigger a replacement or escalation task;
- preserve the prior record for audit;
- record who reviewed and changed it.

S0 and S3 systems MUST NOT:

- imply active human monitoring;
- mark a handoff acknowledged or accepted;
- promise emergency or professional response;
- hide operating limitations behind general language.

## 6. Review questions

- Are the freshness intervals feasible across operating regions?
- What staffing evidence is sufficient for S2?
- How should performance evidence be independently reviewed?
- Which resources require local affected-person verification?
## 7. Risk- and context-sensitive freshness

F0 through F3 are maximum default review ages, not evidence that a resource
remains correct until the maximum age.

A shorter verification interval MUST be used when any of these apply:

- contact, eligibility, hours, cost, or service scope changes frequently;
- the resource is used for emergency, safeguarding, or high-impact action;
- local conditions, law, conflict, disaster, outage, or public-health
  conditions change;
- affected-person or local evidence reports failure;
- the resource has a history of stale or inaccurate information;
- the source is indirect or cannot confirm operational availability.

A stale, disputed, or insufficiently verified resource MUST move to S3 or be
removed from current presentation.

## 8. Active-handoff evidence floor

S2 — active_handoff MUST NOT be claimed without current evidence of:

- a named responsible organization and accountable role;
- actual staffing during published hours;
- supported location, language, age, and eligibility scope;
- acknowledgment and acceptance definitions;
- measured performance over a stated period;
- queue, overload, outage, and capacity limits;
- after-hours behavior;
- failed-handoff ownership and next action;
- escalation and closure authority;
- privacy and minimum-disclosure rules;
- last verification, expiry, and independent review.

A sent message, generated referral, open queue, or unattended mailbox is not
an accepted handoff.

When evidence expires or actual performance materially fails the published
claim, the service MUST downgrade to S1, S0, or S3 and update public wording.

## 9. Accessible resource metadata

A resource record MUST include, where applicable:

```text
supported_languages
interpretation_available
disability_access
communication_modes
age_range
eligibility
cost_or_fee
insurance_or_payment_constraints
operating_hours_and_timezone
safe_contact_options
privacy_or_confidentiality_limits
mandatory_disclosure_or_safeguarding_limits
remote_or_in_person
transport_or_location_constraints
```

Missing information MUST be shown as unknown rather than inferred.

A resource that cannot be safely contacted by the affected person MUST NOT be
presented as a universally usable option.

## 10. Independent and local verification

F0 and F1 resources MUST have:

- direct operational verification or two credible independent sources;
- a named verifier;
- a local or jurisdiction-aware review where feasible;
- evidence of supported scope;
- a dispute and correction route;
- a shorter review interval when uncertainty is material.

F2 resources used for high-impact decisions SHOULD meet the same standard.

Local, affected-person, and minority evidence that a resource fails in
practice MUST be recorded and reviewed even when an official directory lists
the resource as available.

## 11. Service-failure scenarios

Implementation tests MUST include:

1. S2 staffing becomes unavailable;
2. an acknowledgment occurs without acceptance;
3. an after-hours request;
4. overload or queue failure;
5. a resource expires;
6. a resource is technically active but inaccessible by language or
   disability;
7. a local reviewer disputes an official listing;
8. a failed handoff requires redirection without claiming completion.

## 12. Remaining external review

S0 through S3 and F0 through F3 are technical governance classes.

They do not establish emergency-service capability, legal compliance, or
professional adequacy.

The profile remains Proposed pending affected-person, local, accessibility,
safety, operational, and jurisdiction review.
