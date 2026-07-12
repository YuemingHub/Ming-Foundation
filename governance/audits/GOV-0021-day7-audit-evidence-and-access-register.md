---
id: GOV-0021
title: Day 7 Repository Audit and External Evidence Register
status: Accepted
version: 1.0.1
layer: Layer 5 — Community & Governance
owner: Ming Foundation Governance
created: 2026-07-12
updated: 2026-07-12
related:
  - GOV-0002
  - GOV-0018
  - GOV-0020
  - GOV-0022
  - GOV-0023
  - GOV-0025
  - GOV-0027
  - ADR-0009
depends_on:
  - GOV-0002
  - GOV-0018
---

# GOV-0021 — Day 7 Repository Audit and External Evidence Register

## 1. Purpose

This register separates canonical repository evidence from external implementation evidence.

Only the canonical repository evidence determines whether the `Ming-Foundation` repository audit is complete.

## 2. Canonical repository evidence

| Evidence ID | Target | Revision | Method | Result | Authority |
|---|---|---|---|---|---|
| D7-EV-001 | `YuemingHub/Ming-Foundation` | `e2d62543a31822fa7b31b8f6bf4363aa49894de1` | GitHub commit, file, compare, index, status, and backlog inspection | Directly verified | Canonical repository authority |

The repository audit is complete and accepted.

## 3. External implementation evidence

| Evidence ID | Target | Revision or date | Evidence type | State | Repository-audit effect |
|---|---|---|---|---|---|
| D7-EV-002 | Historical website source reference | Historical | Documentary | Bounded | None |
| D7-EV-003 | `mingos.cn` | Day 7 attempt | Live external evidence | Unavailable | None |
| D7-EV-004 | Website source/design analysis | 2026-07-10 to 2026-07-11 | Documentary | Bounded | None |
| D7-EV-005 | `CODE_WIKI.md` Family OS snapshot | 2026-07-09 | Documentary code evidence | Bounded | None |
| D7-EV-006 | `ymai.love` runtime report | 2026-07-11 to 2026-07-12 | Documentary runtime evidence | Bounded | None |
| D7-EV-007 | `ymai.love` live routes | Day 7 attempt | Live external evidence | Unavailable | None |
| D7-EV-008 | Restricted production data and logs | Current | Restricted evidence | Not accessed | None |
| D7-EV-009 | Affected-person outcomes | Current | Validation evidence | Not collected | None |
| D7-EV-010 | Legal review | Current | Expert evidence | Not collected | None |

These sources may affect future Charter or implementation-conformance decisions. They do not affect acceptance of the canonical repository commit.

## 4. Authority rule

Use this rule:

```text
Canonical repository evidence
  → decides repository state and governance

External implementation evidence
  → tests whether products conform to repository standards
```

External evidence may reveal that a repository standard requires revision. It cannot silently become canonical authority.

## 5. Scope-expansion rule

Another repository may enter an active work scope only when the user explicitly identifies it.

A remembered repository name, historical source, domain, or implementation snapshot is not sufficient authorization.

## 6. Security boundary

External evidence access never authorizes:

- credentials in public repository records;
- raw family or child data;
- production database copies;
- unrestricted logs;
- access broader than the stated evidence purpose.
