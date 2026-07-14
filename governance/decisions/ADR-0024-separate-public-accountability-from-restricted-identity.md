---
id: ADR-0024
title: Separate Public Accountability from Restricted Identity
status: Accepted
version: 1.0.0
layer: Cross-layer
owner: Ming Foundation Review Governance
created: 2026-07-14
updated: 2026-07-14
related:
  - GOV-0094
  - GOV-0095
  - GOV-0096
  - GOV-0100
depends_on:
  - ADR-0020
  - GOV-0094
---

# ADR-0024 — Separate Public Accountability from Restricted Identity

## Decision

Use public role codes and status evidence in the repository.

Store real names, personal contacts, identity evidence, certificates,
signatures, and conflict details in a restricted register outside the public
repository.

## Consequence

The public repository can prove whether a role is nominated, accepted,
verified, active, expired, or replaced without publishing unnecessary
personal information.

A null restricted reference means no assignment exists.
