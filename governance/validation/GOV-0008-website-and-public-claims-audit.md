---
id: GOV-0008
title: MingOS Website and Public Claims Audit
status: Accepted
version: 1.0.0-alpha.5
layer: Layer 5 — Community & Governance
owner: MingOS Project Governance
created: 2026-07-12
updated: 2026-07-12
related:
  - ADR-0003
  - ADR-0004
  - MF-0004
  - PROJECT-MINGOS-0001
  - PROJECT-MINGOS-0002
  - GOV-0002
  - GOV-0006
  - GOV-0007
  - GOV-0013
depends_on:
  - ADR-0003
  - GOV-0006
---

# GOV-0008 — MingOS Website and Public Claims Audit

## 1. Scope

This audit evaluates the official MingOS website against the Candidate Charters.

Sources:

- `SRC-0002` — official website;
- `SRC-0011` — website implementation and deployment snapshot;
- `SRC-0013` — structured website design and deployment evidence;
- repository Candidate Charter records.

## 2. Evidence limitation

The website was reported as deployed on `mingos.cn`, with HTTPS, a `/charter` route, and an operational early-access form.

The Day 5 review environment could not independently retrieve the live pages. This audit therefore evaluates available source/design and deployment records, not a complete live DOM, accessibility, network, form-data, or security audit.

A direct live audit remains required.

## 3. Observed public narrative

Available materials show a public narrative organized around:

- MingOS as a Life Operating System;
- a five-layer model: Life, Relationship, Cognition, Growth, Intelligence;
- Human + AI;
- a future product ecosystem;
- the Charter;
- early participation.

This direction is consistent with a life-centered public identity and does not primarily frame MingOS as a conventional course, diagnosis tool, or productivity SaaS.

## 4. Findings

| ID | Area | Finding | State | Severity |
|---|---|---|---|---|
| WEB-001 | Official identity | `mingos.cn` is clearly designated as the official public website | Aligned | — |
| WEB-002 | Charter presence | A `/charter` route is reported in production | Aligned but sync unverified | High |
| WEB-003 | Human agency | Public design emphasizes AI as support rather than final authority | Aligned | — |
| WEB-004 | Commercial tone | Available design avoids urgency, fear, discounting, and aggressive education-sales language | Aligned | — |
| WEB-005 | Current versus future | The five-layer architecture and future ecosystem may be interpreted as completed capability unless status is explicit | Gap | High |
| WEB-006 | Canonical traceability | Available evidence does not establish that material website claims link to accepted repository records and versions | Gap | High |
| WEB-007 | Charter version | The production Charter may predate `MF-0004` and `PROJECT-MINGOS-0002` Candidate texts | Gap | High |
| WEB-008 | Product priority | The relationship between MingOS, Ming Family, Family OS, current product, and future ecosystem may remain unclear | Gap | Medium |
| WEB-009 | Data transparency | The early-access form is reported to persist data, but purpose, fields, retention, access, deletion, and contact information were not evidenced | Gap | High |
| WEB-010 | Children and third parties | No public child/third-party data and contestability explanation was evidenced | Gap | High |
| WEB-011 | AI and professional limits | No complete public statement of AI limits, professional role, crisis boundaries, and escalation responsibility was evidenced | Gap | High |
| WEB-012 | Incident and appeal | No public route for correction, privacy request, Charter concern, or incident report was evidenced | Gap | Medium |
| WEB-013 | Public status | No verified public page distinguishes current, in-development, experimental, and long-term capabilities | Gap | High |
| WEB-014 | Accessibility | Keyboard, reduced-motion, contrast, screen-reader, and Chinese typography conformance were not directly verified | Unknown | Medium |
| WEB-015 | Source freshness | No visible “last updated / governing version” evidence was available for Charter and architecture pages | Gap | Medium |

## 5. Required public corrections

### P0 — Before broader public acquisition

1. Synchronize `/charter` with Candidate repository texts or clearly label the public page as a non-normative summary.
2. Add a visible current-status section:
   - exists now;
   - being developed;
   - experimental;
   - long-term direction;
   - not yet validated.
3. Add repository traceability for Charter, architecture, and governance claims.
4. Add a privacy and data-use notice for early-access collection:
   - purpose;
   - fields;
   - retention;
   - access;
   - deletion/request route;
   - processor/controller contact;
   - whether child information should be submitted.
5. Explicitly prohibit submission of identifiable child cases through general early-access fields.
6. State that MingOS is not emergency, medical, psychological-diagnostic, or legal care.

### P1

1. Clarify the product map:
   - MingOS — platform and standards;
   - Ming Family — first product direction;
   - Family OS / `ymai.love` — implementation seed or current product surface;
   - future products — not currently available.
2. Add public data principles and children/third-party rights.
3. Add correction, privacy-request, and Charter-concern contact paths.
4. Add page-level version and update metadata.
5. Add accessible reduced-motion and keyboard validation.

## 6. Public claim rules

The website SHOULD NOT claim that MingOS currently provides:

- a complete Life Operating System;
- a validated general theory of life;
- a complete life model;
- universal psychological or educational authority;
- verified outcome improvement without evidence;
- a stable public SDK, Kernel, cloud, certification, or ecosystem;
- direct child understanding based solely on parent reports.

Preferred status language:

> MingOS is building and validating standards and systems for Living Intelligence. Current work includes Candidate Charters, a public knowledge repository, an official website, and bounded family-support implementation evidence.

## 7. Decision

The website direction is broadly Charter-aligned, but public-claim governance is not yet sufficiently evidenced.

Website validation state:

```text
V5 Commercial and communication audit: Partial
```

A direct live audit and remediation evidence are required before V5 can be considered complete.
