---
created: 2026-07-12
depends_on:
- GOV-0002
- GOV-0018
id: GOV-0021
layer: Layer 5 — Community & Governance
owner: Ming Foundation Governance
related:
- GOV-0002
- GOV-0018
- GOV-0020
- GOV-0022
- GOV-0023
- GOV-0025
- ADR-0008
status: Accepted
title: Day 7 Audit Evidence and Access Register
updated: 2026-07-12
version: 1.0.0-alpha.7
---

# GOV-0021 — Day 7 Audit Evidence and Access Register

## 1. Purpose

This register identifies what Day 7 actually accessed and what remained
unavailable.

It prevents the phrase “direct audit” from being used without a current
revision, method, and evidence path.

## 2. Evidence register

| Evidence ID | Target                                | Revision or date                                                   | Method                                         | Access                               | Authority for Day 7             | Limitation                                                          |
|-------------|---------------------------------------|--------------------------------------------------------------------|------------------------------------------------|--------------------------------------|---------------------------------|---------------------------------------------------------------------|
| D7-EV-001   | `YuemingHub/Ming-Foundation`          | `b1162a0cd856d2ce1867150df9cd144d64ea4510`                         | GitHub connector commit and file reads         | Direct                               | Repository-verified             | Does not prove website or product conformance                       |
| D7-EV-002   | `YuemingHub/Mingos-life`              | Known historical commit `d4570975cf90e213f034f986b27600091c0bc003` | GitHub repository access attempt               | Denied / not installed for connector | Unverifiable current source     | Private repository may exist and be current, but was not accessible |
| D7-EV-003   | `mingos.cn`                           | 2026-07-12 audit attempt                                           | Browser and direct HTTP resolution attempt     | Unavailable                          | Unverifiable live behavior      | Audit environment could not resolve or retrieve the domain          |
| D7-EV-004   | MingOS website source/design analysis | 2026-07-10 to 2026-07-11                                           | Structured source-analysis record              | Documentary                          | Bounded evidence                | May not match current source or deployment                          |
| D7-EV-005   | `CODE_WIKI.md` Family OS snapshot     | 2026-07-09                                                         | Full structured code inventory                 | Documentary code evidence            | Bounded implementation evidence | No direct source checkout or test execution                         |
| D7-EV-006   | `ymai.love` runtime report            | 2026-07-11 to 2026-07-12                                           | Structured server and health inspection record | Documentary runtime evidence         | Bounded operational evidence    | Current runtime not independently rechecked                         |
| D7-EV-007   | `ymai.love` live routes               | 2026-07-12 audit attempt                                           | Browser and direct HTTP resolution attempt     | Unavailable                          | Unverifiable current behavior   | Domain resolution failed in audit environment                       |
| D7-EV-008   | Restricted production data and logs   | Current                                                            | Not requested or inspected                     | Not accessed                         | Outside public audit scope      | Must use restricted evidence governance                             |
| D7-EV-009   | Affected-person outcomes              | Current                                                            | No interviews in Day 7                         | Not collected                        | No authority                    | Required through `GOV-0017`                                         |
| D7-EV-010   | Legal review                          | Current                                                            | No qualified review                            | Not collected                        | No authority                    | Jurisdiction review remains required                                |

## 3. Audit classification rule

A finding is:

- **Implemented** only when the current behavior is directly evidenced;
- **Partial** when a relevant mechanism exists but the complete
  requirement is not evidenced;
- **Absent** when available evidence shows no required mechanism;
- **Conflicting** when current behavior appears to violate the
  requirement;
- **Unverifiable** when current evidence is unavailable or stale;
- **Not applicable with reason** only when the requirement does not
  apply and the reason is recorded.

Document names, route names, table names, or module names alone do not
establish implementation.

## 4. Access prerequisite

Before a complete Day 7 re-audit can occur, the project needs:

1.  current repository locator and commit for the official website;
2.  current repository locator, branch, and commit for Family OS;
3.  read access for the audit mechanism;
4.  build and test instructions;
5.  production-versus-development boundaries;
6.  safe access to de-identified operational evidence;
7.  a source registration update in `GOV-0002`.

## 5. Security boundary

The access prerequisite does not authorize:

- credentials in public repository records;
- raw family or child data;
- production database copies;
- unrestricted logs;
- direct access broader than the audit purpose.

Restricted evidence remains governed by `GOV-0018`.
