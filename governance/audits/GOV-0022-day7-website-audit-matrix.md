---
created: 2026-07-12
depends_on:
- RFC-0005
- GOV-0021
id: GOV-0022
layer: Layer 5 — Community & Governance
owner: MingOS Project Governance
related:
- GOV-0008
- GOV-0020
- GOV-0021
- GOV-0025
- RFC-0005
- ADR-0008
status: Accepted
title: Day 7 MingOS Website External Implementation Evidence Matrix
updated: 2026-07-12
version: 1.0.1
---

# GOV-0022 — Day 7 MingOS Website External Implementation Evidence Matrix

## 1. Scope and authority

This document is a supporting external implementation-evidence record. It does not determine whether the canonical `Ming-Foundation` repository audit is complete.

Targets:

- official website `mingos.cn`;
- known private source repository `YuemingHub/Mingos-life`;
- RFC-0005 requirements.

## 2. Access boundary

The current private source repository was not accessible to the
connected GitHub application.

The live domain could not be retrieved from the Day 7 environment.

The matrix therefore combines:

- direct access results;
- a dated documentary source snapshot;
- explicit Unverifiable classifications.

## 3. Known documentary source

The dated source analysis identified a Next.js website with:

- `app/page.tsx`;
- `components/mingos/hero.tsx`;
- `architecture.tsx`;
- `philosophy.tsx`;
- `applications.tsx`;
- `charter.tsx`;
- a `/charter` route;
- an early-access form;
- architecture, Human + AI, ecosystem, and Charter sections.

The same analysis identified prototype-stage gaps including unclear
current product status, mixed CTA meaning, incomplete privacy and data
explanation, and absent public product proof.

## 4. RFC-0005 requirement matrix

| Requirement                                                              | Evidence                                                                                                     | Day 7 state                              | Backlog    |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------------------------------|------------|
| Capability status vocabulary is visible                                  | Documentary design uses future ecosystem but no Available/Pilot/Experimental/Planned/Vision system evidenced | Absent in snapshot; current unverifiable | D7-WEB-002 |
| Every material claim is source- or status-traceable                      | No source ID, repository version, evidence record, or claim manifest evidenced                               | Absent                                   | D7-WEB-001 |
| Charter page identifies governing source, status, version, and sync date | `/charter` exists in deployment record; current source metadata not evidenced                                | Partial / Unverifiable                   | D7-WEB-001 |
| Public summary states it is non-normative when applicable                | No evidence                                                                                                  | Unverifiable                             | D7-WEB-001 |
| Material pages show owner and correction route                           | No evidence                                                                                                  | Absent / Unverifiable                    | D7-WEB-005 |
| Current and future capabilities are separated                            | Ecosystem narrative exists; current priority and maturity were identified as unclear                         | Conflicting / Partial                    | D7-WEB-002 |
| Claims have evidence, limitations, and review date                       | No claim-review record evidenced                                                                             | Absent                                   | D7-WEB-006 |
| Forms state purpose, fields, recipient, retention, and request route     | Form and later data persistence are documented; complete notice not evidenced                                | Partial                                  | D7-WEB-003 |
| General forms prohibit child, medical, crisis, or consultation details   | No evidence                                                                                                  | Absent                                   | D7-WEB-003 |
| AI involvement and limitations are visible                               | Human + AI philosophy exists; operational disclosure not evidenced                                           | Partial                                  | D7-WEB-004 |
| Human or professional review status is visible                           | No evidence                                                                                                  | Absent / Unverifiable                    | D7-WEB-004 |
| Emergency, diagnosis, legal, and response limits are visible             | No complete public boundary statement evidenced                                                              | Absent / Unverifiable                    | D7-WEB-004 |
| Repository-to-site synchronization exists                                | No manifest or automated check evidenced                                                                     | Absent / Unverifiable                    | D7-WEB-006 |
| Stale Charter content blocks or warns deployment                         | No evidence                                                                                                  | Absent                                   | D7-WEB-006 |
| Public discrepancy reporting exists                                      | No evidence                                                                                                  | Absent                                   | D7-WEB-005 |
| Accessibility and reduced-motion behavior pass current audit             | Design mentions motion and prior analysis recommends reduced motion; live audit unavailable                  | Unverifiable                             | D7-WEB-007 |

## 5. Acceptance-test matrix

| RFC-0005 test                                                      | Day 7 state                        |
|--------------------------------------------------------------------|------------------------------------|
| Charter page identifies source and status                          | Unverifiable                       |
| Future capability is labeled Planned or Vision                     | Not evidenced                      |
| Available capability is reachable or eligibility is clear          | Unverifiable                       |
| Early-access form displays purpose and sensitive-data restrictions | Partial / not evidenced completely |
| No page claims Charters are Accepted                               | Unverifiable                       |
| AI and professional boundaries are visible before sensitive use    | Not evidenced                      |
| Stale source triggers warning or failure                           | Not evidenced                      |
| Inaccurate information can be reported                             | Not evidenced                      |
| Outcome claims have evidence and review dates                      | Not evidenced                      |

## 6. Website conclusion

The website has a coherent life-centered narrative and an established
implementation snapshot.

It does not yet have sufficient evidence for RFC-0005 conformance.

Current status:

``` text
RFC-0005 website implementation: Partial and Unverifiable
```

A current source checkout and live-page audit remain necessary only for a future website-conformance claim. They are not prerequisites for `Ming-Foundation` repository progress.
