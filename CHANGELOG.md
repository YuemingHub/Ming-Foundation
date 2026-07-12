# Changelog

All notable repository-level changes are documented here.

## [1.0.0-alpha.7.1] - 2026-07-12

### Fixed

- Corrected the Day 7 audit scope: `YuemingHub/Ming-Foundation` is the canonical and only active repository for this phase.
- Separated canonical repository audit from external implementation-conformance evidence.
- Added `GOV-0027` as the accepted correction record.
- Added `ADR-0009` and superseded the scope framing in `ADR-0008`.
- Reclassified website and Family OS records as bounded, non-blocking external evidence.
- Replaced the mixed product backlog with a canonical repository backlog plus external evidence targets.
- Added automated scope-regression validation.
- Updated README, canonical state, source registry, validation plan, traceability matrix, index, and status recommendation.

### Decision

- The Day 7 `Ming-Foundation` repository audit is accepted.
- External repository access is not a prerequisite for canonical repository progress.
- Both Charters remain Candidate.
- RFC-0001 through RFC-0005 and `GOV-0015` remain Proposed.
- Another repository enters scope only through explicit user instruction.

## [1.0.0-alpha.7] - 2026-07-12

### Added

- Day 7 direct audit attempt and remediation backlog record (`GOV-0020`).
- Audit evidence and access register (`GOV-0021`).
- MingOS website audit matrix (`GOV-0022`).
- Family OS implementation audit matrix (`GOV-0023`).
- Counterexample execution-readiness matrix (`GOV-0024`).
- Remediation implementation backlog (`GOV-0025`).
- Day 7 status recommendation (`GOV-0026`).
- Accepted decision treating Day 7 as a bounded audit (`ADR-0008`).
- Machine-readable Day 7 backlog.

### Changed

- Repository status advanced to Day 7 — Direct Audit Attempt and Remediation Implementation Backlog.
- `GOV-0019` now records Day 7 evidence states and backlog authority.
- Changelog version headings were restored to unescaped Keep a Changelog form.
- Current work now prioritizes repository access, reproducible audit, and the first P0 implementation wave.

### Decision

- Both Charters remain Candidate.
- RFC-0001 through RFC-0005 remain Proposed.
- `GOV-0015` remains Proposed.
- Day 7 does not claim completed current-source or production conformance.

### Evidence limitations

- The current private website repository was not accessible to the connected GitHub application.
- The current Family OS source repository was not available.
- Live `mingos.cn` and `ymai.love` retrieval failed in the audit environment.
- Documentary code snapshots were used only as bounded evidence.

## [1.0.0-alpha.6] - 2026-07-12

### Added

- Day 6 remediation and external-review preparation record (`GOV-0014`).
- Proposed subject, speaker, and contestability protocol (`RFC-0001`).
- Proposed consent and data-rights lifecycle protocol (`RFC-0002`).
- Proposed safety escalation, handoff, appeal, and incident protocol
  (`RFC-0003`).
- Proposed case and cross-family evidence-governance protocol
  (`RFC-0004`).
- Proposed public-claim, Charter-sync, and capability-status protocol
  (`RFC-0005`).
- Proposed Charter-violation reporting and remediation procedure
  (`GOV-0015`).
- External Charter review protocol (`GOV-0016`).
- Affected-person Charter review instrument (`GOV-0017`).
- Restricted validation-evidence handling protocol (`GOV-0018`).
- Day 6 remediation traceability matrix (`GOV-0019`).
- Reusable external-review, affected-person, and validation-finding
  templates.
- Accepted decision requiring minimum remediation contracts before
  Charter acceptance (`ADR-0007`).
- Registered external-review, affected-person, and future direct-audit
  evidence sources.

### Changed

- Repository status advanced to Day 6 — Validation Remediation and
  External Review Preparation.
- `GOV-0001` related metadata was synchronized with Day 5 and Day 6
  records.
- `GOV-0006` now records Day 6 preparation without overstating
  validation progress.
- README and repository index now expose remediation protocols and
  review instruments.

### Status boundary

- `MF-0004` remains Candidate.
- `PROJECT-MINGOS-0002` remains Candidate.
- RFC-0001 through RFC-0005 remain Proposed.
- `GOV-0015` remains Proposed.
- No implementation, external review, affected-person review, or legal
  review is represented as complete.

## [1.0.0-alpha.5] - 2026-07-12

### Added

- Day 5 Charter validation evidence summary (`GOV-0007`).
- MingOS website and public-claims audit (`GOV-0008`).
- Family OS implementation-to-Charter mapping (`GOV-0009`).
- Privacy and third-party-rights gap analysis (`GOV-0010`).
- Safety and professional-boundary gap analysis (`GOV-0011`).
- Charter counterexample and risk register (`GOV-0012`).
- Day 5 Charter status recommendation (`GOV-0013`).
- Accepted decision to retain both Charters at Candidate (`ADR-0006`).
- Registered bounded website, Family OS, and structured deployment
  evidence sources.

### Changed

- Repository status advanced to Day 5 — Charter Validation Against
  Reality.
- `GOV-0006` now records validation-stream progress.
- README Charter section heading was corrected and expanded.
- Current canonical state now prioritizes remediation and external
  review preparation.

### Decision

- `MF-0004` remains Candidate.
- `PROJECT-MINGOS-0002` remains Candidate.
- No claim of Accepted or Stable Charter status is made.

### Evidence limitations

- No direct affected-person or child-rights review was completed.
- No qualified legal review was completed.
- Live website and current implementation repositories were not
  independently retrieved in the Day 5 review environment.
- Documentary implementation evidence does not equal production
  conformance.

## [1.0.0-alpha.4] - 2026-07-12

### Added

- Day 4 article-by-article Charter review and decision record
  (`GOV-0005`).
- Charter Candidate validation plan (`GOV-0006`).
- New Charter of Life article protecting a person from being fully
  represented by another person’s account (`C13`).
- MingOS Charter commitment requiring violation response, remediation,
  and traceability (`MC14`).

### Changed

- `ADR-0005` moved from Proposed to Accepted.
- `MF-0004` moved from Draft to Candidate after internal review and
  revision.
- `PROJECT-MINGOS-0002` moved from Draft to Candidate after internal
  review and revision.
- Agency, emergency safety, deletion, retention, third-party voice,
  conflict handling, commercial review, and enforcement language were
  strengthened.
- `GOV-0004` was accepted as the historical Day 3 consolidation record.
- Repository status advanced to Day 4 — Charter Review and Candidate
  Decision.

### Not completed

- Neither Charter is Accepted or Stable.
- External, affected-person, legal, privacy, safety, child-rights, and
  implementation validation remains required.
- A complete MingOS Kernel conformance specification is not introduced.

## [1.0.0-alpha.3] - 2026-07-12

### Added

- Reviewable Draft of the Charter of Life (`MF-0004`).
- Reviewable Draft of the MingOS Charter (`PROJECT-MINGOS-0002`).
- Proposed decision separating the Charter of Life, MingOS Charter, and
  MingOS Kernel (`ADR-0005`).
- Day 3 Charter consolidation and source-handling record (`GOV-0004`).

### Changed

- Repository status advanced from Day 2 to Day 3 — Charter Consolidation
  Draft.
- Root README now distinguishes the universal ethical Charter, MingOS
  project commitments, and operational Kernel.
- Repository index now records the Day 3 Draft and Proposed artifacts.
- Current canonical state now identifies Charter review as the next
  gate.

### Not completed

- The Charter drafts are not yet Accepted.
- `ADR-0005` is not yet Accepted.
- No complete MingOS Kernel specification is introduced by Day 3.

## [1.0.0-alpha.2] - 2026-07-12

### Added

- Current canonical state record (`GOV-0001`).
- Source registry for repository, website, conversations, handoff
  packages, implementations, research, and cases (`GOV-0002`).
- Conversation-to-repository workflow (`GOV-0003`).
- Accepted decision that `mingos.cn` is the official MingOS website
  (`ADR-0003`).
- Accepted decision that `YuemingHub/Ming-Foundation` is the canonical
  public repository (`ADR-0004`).
- MingOS public surfaces and authority map (`PROJECT-MINGOS-0001`).

### Changed

- Repository status advanced from Day 1 to Day 2.
- Root README now distinguishes official website, canonical repository,
  discussion sources, and privacy boundaries.
- Repository index now includes governance baseline and public-surface
  decisions.

## [1.0.0-alpha.1] - 2026-07-12

### Added

- Repository architecture and layer model.
- Ming Foundation mission, vision, and first principles.
- MOS standards process.
- Initial architecture decisions.
- Core terminology reference.
- Governance and contribution workflow.
- Document templates and repository validator.
- Initial MingOS project boundary.
