---
id: REF-0030
title: Round 06 Kernel Decision Traceability and Open Questions
status: Draft
version: 0.1.0
layer: Reference
owner: Ming Foundation Architecture
created: 2026-07-14
updated: 2026-07-14
language: en
canonical_language: en
translation_status: original
decision_base_commit: 394f494f00ebfccf38572e3846cf6b6e3f699abf
related:
  - ADR-0026
  - GOV-0082
  - REF-0014
  - REF-0019
  - REF-0023
  - REF-0026
  - REF-0027
  - REF-0028
  - REF-0029
depends_on:
  - ADR-0026
---

# REF-0030 — Round 06 Kernel Decision Traceability and Open Questions

## 1. Roadmap decision coverage

| GOV-0082 requirement | Round 06 answer | Source |
|---|---|---|
| single specification or family | governed specification family | ADR-0026 §2.1 |
| document IDs and repository location | KERNEL-0000..0005 under `standards/kernel/` | ADR-0026 §2.2; REF-0026 |
| boundary between Charter, RFC, MOS, Profile and implementation | distinct source classes with status-aware authority | ADR-0026 §2.3–2.4; REF-0027 |
| what constitutes Kernel conformance | versioned implementation-bound claim requiring future requirements, tests and evidence | ADR-0026 §2.5; REF-0028 |
| what remains replaceable | mechanisms replaceable; governed obligations preserved | ADR-0026 §2.6; REF-0028 |
| AI, human and affected-person roles | separate role assignments, scoped authority and human accountability | ADR-0026 §2.7; REF-0029 |

## 2. Round 05 commitment traceability

| MingOS Charter area | Round 06 response | Still unresolved |
|---|---|---|
| MC01 affected lives and role conflicts | explicit affected-person and role separation | conflict prioritization details |
| MC03 refusal, correction and leaving | future common obligation and consent/data lifecycle | exact requirement and state machine |
| MC04 data and memory accountability | non-replaceable obligation; KERNEL-0002/3 allocation | object fields, backup/deletion states |
| MC05–MC06 evidence and knowledge status | Kernel core plus source-linked RFCs | confidence model and verification |
| MC08 dependency and healthy exit | not admitted as universal object; remains contract gap | measurable dependency/healthy-support contract |
| MC09 bounded AI | AI role separated from accountability | high-impact threshold and allowed automation |
| MC10 children and third parties | affected-person and representative roles | age, jurisdiction and participation Profiles |
| MC11 professional and safety boundary | practitioner/service roles and safety lifecycle allocation | service freshness and escalation evidence |
| MC12 commercial conflict | architecture boundary preserved | independent adjudicator activation |
| MC13 correction and audit | core obligation; lifecycle and conformance allocation | exact service and evidence requirements |
| MC14 violation and remediation | remediation lifecycle and conformance suspension allocation | reporting, investigation and reinstatement operation |
| S05 decision precedence | conflict recording and role/accountability model | decision algorithm must not become automatic formula |
| S06 conformance questions | future KERNEL-0004/5 | requirement and test design |
| S07 Kernel relationship | family structure decided | all substantive Kernel documents |
| S08 validation | no status promotion or conformance claim | all external and implementation evidence |

## 3. Historical method disposition

The following remain outside the universal Kernel unless separately admitted:

- 规律—关系—驱动—投资;
- 三系统 as a complete architecture;
- event-chain, goal-tree, cycle-map and breakpoint templates;
- gardener/carpenter and soul-layer metaphors;
- parent-specific language and behavior assumptions;
- historical L1 labels;
- old product object names.

Possible generic objects such as Event, Timeline, Relationship, Observation,
Hypothesis, Pattern, Consent, Purpose, Memory, Risk, Incident, Action, Feedback,
Evidence, Unknown, Audit and Version remain candidates for Round 07–08, not
accepted objects in Round 06.

## 4. Open questions for Round 07

1. What is the smallest common obligation set in KERNEL-0001?
2. Which requirements are referenced from RFCs rather than restated?
3. How are Candidate Charter ambiguities represented without freezing them?
4. What role and authority semantics belong in the core versus KERNEL-0002?
5. What constitutes a high-impact operation?
6. How is observation-before-advice stated without imposing one counseling
   method?
7. How are evidence, confidence, unknown and dissent represented?
8. Which obligations apply to organizations as well as software?
9. How are unavailable human services represented honestly?
10. How does a Kernel version set declare compatibility and supersession?
11. What minimum affected-person participation is required for review?
12. How will Chinese and English source traceability be maintained?

## 5. Blocking boundaries

Round 07 must not claim:

- that ADR-0026 is Accepted unless separately decided;
- that reserved KERNEL IDs already exist;
- that current products conform;
- that Day 16 synthetic pilots validate Kernel behavior;
- that historical Family OS code is a reference implementation;
- that the current RFC/Profile set is complete;
- that affected-person or domain review has been executed.

## 6. Exit recommendation

Round 06 is ready for owner review when:

- repository validation passes;
- no identifier or path collision exists;
- all roadmap questions are answered at scope level;
- non-goals remain explicit;
- `NoCurrentKernelConformanceClaim` is preserved;
- Day 16 and core-text workstreams remain separate;
- unresolved Round 07 questions remain visible.
