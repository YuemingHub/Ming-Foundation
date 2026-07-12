---
id: ADR-0017
title: Canonical Text Integrity Across Platforms
status: Accepted
version: 1.0.0
layer: Cross-layer
owner: Ming Foundation Validation
created: 2026-07-13
updated: 2026-07-13
related:
  - GOV-0059
  - GOV-0061
depends_on:
  - ADR-0016
---

# ADR-0017 — Canonical Text Integrity Across Platforms

## Context

Day 13 local validation exposed a Windows `core.autocrlf=true` failure:

- Git stored the governed RFC source with LF;
- the working tree contained CRLF;
- validators calculated a raw-byte blob SHA;
- equivalent governed text was reported as a source mismatch.

## Decision

1. Add `.gitattributes` with LF rules for governed text formats.
2. Calculate governed text blob identity after canonical newline
   normalization.
3. Keep binary files byte-exact.
4. Do not require users to change global Git configuration.
5. Validate the text-integrity policy in the repository suite.

## Consequence

LF and CRLF working-tree representations of the same governed UTF-8 text
produce the same canonical validation identity.

This does not weaken source integrity; it aligns validation with the
repository's canonical text semantics.
