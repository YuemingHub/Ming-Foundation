---
id: ADR-0003
title: mingos.cn Is the Official MingOS Website
status: Accepted
version: 1.0.0
layer: Layer 4 — Projects
owner: MingOS Project
created: 2026-07-12
updated: 2026-07-12
related:
  - PROJECT-MINGOS-0000
  - PROJECT-MINGOS-0001
  - GOV-0001
  - GOV-0002
  - ADR-0004
depends_on:
  - PROJECT-MINGOS-0000
---

# ADR-0003 — mingos.cn Is the Official MingOS Website

## Context

MingOS discussions, prototypes, and implementation work occur across multiple tools and interfaces. Without an explicit official public website, outside audiences may be unable to distinguish an approved MingOS representation from a prototype, product surface, social account, or third-party description.

## Decision

`https://mingos.cn` is the official website of MingOS.

The website is the primary public interface for explaining:

- what MingOS is;
- its purpose and commitments;
- its Charter and architecture as they become accepted;
- public project status;
- participation and contribution paths;
- official product and implementation links.

The website is an official representation, not an independent source of normative truth. Material claims SHOULD be traceable to accepted records in `YuemingHub/Ming-Foundation`.

## Reasons

- One official domain reduces ambiguity and impersonation risk.
- Public communication needs a coherent interface distinct from repository navigation.
- The repository can preserve detailed provenance while the website provides accessible explanation.
- Separating presentation from governance prevents marketing language from silently redefining standards.

## Consequences

### Positive

- Contributors and the public have one recognized website.
- Website content can be audited against repository decisions.
- Future products can be linked from a stable official domain.
- The website and repository have clearly different responsibilities.

### Negative

- The website requires ongoing synchronization with accepted repository records.
- Stale website content can create public inconsistency and must be corrected.
- Public copy cannot be treated as a shortcut around architecture and governance review.

## Alternatives considered

### Multiple equal official websites

Rejected because it creates ambiguity about authority and synchronization.

### GitHub repository as the only public interface

Rejected because a standards repository is not an adequate public explanation or product gateway.

### Social media account as the official source

Rejected because platform ownership, format, discoverability, and archival control are insufficient for long-term project identity.

## Follow-up

- Website claims should link to or derive from repository records where practical.
- Public status pages should clearly distinguish current, experimental, and future capabilities.
- Website changes that redefine project identity or commitments require repository review first.
