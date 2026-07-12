---
id: PROF-0004
title: Service Response and Resource Freshness Profile
status: Proposed
version: 0.1.0
layer: Layer 1 — Standards
owner: Ming Foundation Standards
created: 2026-07-12
updated: 2026-07-12
related:
  - RFC-0003
  - GOV-0055
  - GOV-0058
  - ADR-0016
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
