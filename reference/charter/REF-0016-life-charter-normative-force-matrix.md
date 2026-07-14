---
id: REF-0016
title: 生命宪章规范强度与关键词矩阵
status: Draft
version: 0.2.0-draft.1
layer: Reference
owner: Ming Foundation Translation Review
created: 2026-07-14
updated: 2026-07-14
language: zh-CN
canonical_language: zh-CN
translation_status: original
migration_base_commit: c149953217e466570da3fa58157eb66616514d6b
source_text_commit: 22332a0c8d8858c9ccf652f2a40dee5821d53c6c
related:
  - MF-0004
  - MF-0006
  - ADR-0021
  - REF-0015
depends_on:
  - MF-0004
  - MF-0006
---

# REF-0016 — 生命宪章规范强度与关键词矩阵

## 1. 规范词约定


> **重要边界：** MF-0004 尚未通过独立决议正式采用 RFC 2119/8174 的规范词
> 语义。本矩阵使用 `MUST`、`SHOULD` 等标签，是为了审查翻译强度的临时映射，
> 不是把技术标准语义自动导入《生命宪章》。所有小写 `must`、`should`、
> `may`、`cannot` 和 `No ... may` 的强度判断均为 `ProvisionalInterpretation`。

| 英文 | 中文 | 强度 |
|---|---|---|
| MUST | 必须 | 无条件强制要求，除非条款本身明确限定适用条件 |
| MUST NOT | 不得 | 无条件强制禁止，除非条款本身明确限定适用条件 |
| SHOULD | 应当 | 强建议；偏离需要可说明、可复核的理由 |
| SHOULD NOT | 不应 | 强烈不建议；偏离需要理由 |
| MAY | 可以 / 可能 | 许可、可能性或可选能力，不构成义务 |
| must / must not | 必须 / 不得 | 结合宪章语境判断是否为等同强制义务 |
| should / should not | 应当 / 不应 | 伦理性强建议，不自动提升为法律义务 |
| may / cannot / no person | 可以、可能、不能、任何人不得/不应 | 依据句子功能记录，不只看大小写 |

## 2. 逐项矩阵

| ID | 位置 | 英文表达 | 中文表达 | 来源强度 | 中文规范词 | 映射状态 | 说明 |
|---|---|---|---|---|---|---|---|
| N01 | S02 | MUST remain open to correction | 必须始终允许被修正 | `MUST` | `必须` | `DirectCaseMatch` | 保持强制义务 |
| N02 | C01 | MUST yield | 必须让位 | `MUST` | `必须` | `DirectCaseMatch` | 现实与可信证据冲突时适用 |
| N03 | C01 | No system may distort | 任何系统都不得扭曲 | `prohibition` | `不得` | `ProvisionalInterpretation` | 按禁止性义务处理 |
| N04 | C03 | No person should be reduced | 任何人都不应被缩减 | `ethical SHOULD NOT` | `不应` | `ProvisionalInterpretation` | 不提升为法律绝对禁止 |
| N05 | C03 | behavior may be a signal | 行为可以是一种信号 | `MAY` | `可以` | `DirectCaseMatch` | 表达可能性而非诊断 |
| N06 | C04 | MUST NOT become the final authority | 不得成为最终权威 | `MUST NOT` | `不得` | `DirectCaseMatch` | 强制禁止 |
| N07 | C04 | People should be able to... | 人们应当能够…… | `SHOULD` | `应当` | `ProvisionalInterpretation` | 强权利方向，仍需能力与情境审查 |
| N08 | C04 | intervention MUST be narrowly scoped... | 干预必须严格限定范围…… | `MUST` | `必须` | `DirectCaseMatch` | 迫近严重伤害例外 |
| N09 | C04 | must not be misrepresented as ordinary consent | 不得被错误表述为一般意义上的同意 | `MUST NOT` | `不得` | `ProvisionalInterpretation` | 安全干预不伪装成同意 |
| N10 | C05 | states may be legitimate parts of life | 这些状态可能是生命中正当的部分 | `MAY` | `可能` | `ProvisionalInterpretation` | 不是自动正当化所有拒绝或停滞 |
| N11 | C06 | Growth cannot be forced | 成长不能被强行制造 | `prohibition` | `不能` | `ProvisionalInterpretation` | 原则性禁止操纵式制造 |
| N12 | C06 | Systems SHOULD support conditions | 系统应当支持条件 | `SHOULD` | `应当` | `DirectCaseMatch` | 强建议，不承诺结果 |
| N13 | C07 | support must consider... | 支持必须考虑…… | `MUST-equivalent` | `必须` | `ProvisionalInterpretation` | 原文小写但语义为核心义务 |
| N14 | C08 | action may be necessary | 行动可能是必要的 | `MAY` | `可能` | `ProvisionalInterpretation` | 不是自动授权 |
| N15 | C08 | It must be proportionate... | 行动必须合比例…… | `MUST-equivalent` | `必须` | `ProvisionalInterpretation` | 安全行动的强制约束 |
| N16 | C08 | restrictions SHOULD include... | 重大限制应当说明…… | `SHOULD` | `应当` | `DirectCaseMatch` | 偏离需要说明理由 |
| N17 | C09 | MUST be distinguished | 必须被区分 | `MUST` | `必须` | `DirectCaseMatch` | 知识状态分离 |
| N18 | C09 | interpretation should preserve... | 解释应当保留…… | `SHOULD` | `应当` | `ProvisionalInterpretation` | 追溯与修订义务候选 |
| N19 | C10 | Technology may help | 技术可以帮助 | `MAY` | `可以` | `DirectCaseMatch` | 能力许可，不是保证 |
| N20 | C10 | MUST NOT replace... | 不得替代…… | `MUST NOT` | `不得` | `DirectCaseMatch` | 强制禁止 |
| N21 | C11 | Memory should preserve continuity | 记忆应当保留连续性 | `SHOULD` | `应当` | `ProvisionalInterpretation` | 与删除、撤回权保持张力 |
| N22 | C11 | People must have meaningful rights | 人们必须拥有具有实际意义的权利 | `MUST-equivalent` | `必须` | `ProvisionalInterpretation` | 需要实现与司法辖区限定 |
| N23 | C11 | exception MUST be purpose-limited... | 例外必须限定目的…… | `MUST` | `必须` | `DirectCaseMatch` | 所有留存例外的强约束 |
| N24 | C12 | MUST preserve evidence | 必须保留证据 | `MUST` | `必须` | `DirectCaseMatch` | 仍受隐私与安全边界约束 |
| N25 | C12 | must not be hidden | 不得被隐藏 | `MUST NOT-equivalent` | `不得` | `ProvisionalInterpretation` | 不允许为声誉或转化隐藏 |
| N26 | C13 | account MUST NOT become... | 叙述不得成为…… | `MUST NOT` | `不得` | `DirectCaseMatch` | 代表性边界 |
| N27 | C13 | Systems SHOULD seek... | 系统应当寻求…… | `SHOULD` | `应当` | `DirectCaseMatch` | 直接参与不可行时须记录理由 |
| N28 | S06 | responsible actor MUST record | 负责主体必须记录 | `MUST` | `必须` | `DirectCaseMatch` | 冲突与例外记录 |
| N29 | S06 | No exception may silently become... | 任何例外都不得静默成为…… | `prohibition` | `不得` | `ProvisionalInterpretation` | 防止例外常态化 |
| N30 | S07 | No lower layer may silently redefine | 任何下层都不得静默重定义 | `prohibition` | `不得` | `ProvisionalInterpretation` | 显式治理修订仍允许 |
| N31 | S08 | validation MUST include | 验证必须包括 | `MUST` | `必须` | `DirectCaseMatch` | Acceptance 前置条件 |

## 3. 翻译禁区

不得：

- 把 `MAY` 翻译为“必须”；
- 把 `SHOULD` 无记录地翻译为绝对“必须”；
- 用“建议”削弱 `MUST`；
- 用“可以不”削弱 `MUST NOT`；
- 把安全例外翻译成无限授权；
- 把数据权利翻译成由平台自由决定的功能；
- 把“受影响者参与”缩减为“用户体验反馈”。

## 4. 仍需审查的强度问题

1. C03 的小写 `should not` 是否应在未来英文修订中提升为大写 `MUST NOT`；
2. C07 的小写 `must consider` 是否应规范化为大写 `MUST`；
3. C11 的小写 `must have meaningful rights` 是否需要拆成可测试的具体要求；
4. C12 的小写 `must not be hidden` 是否需要列出隐私、安全和法律例外；
5. Charter tests 是否为绝对冲突判定，还是需要记录例外程序；
6. “No ... may” 在各条中应统一归为禁止还是条件性禁止。

本轮只记录，不静默改写英文来源。

## 5. 变更历史

- `0.2.0-draft.1` — 明确规范词语义为临时审查映射；为每项要求增加`DirectCaseMatch` 或 `ProvisionalInterpretation` 状态；修正来源快照。
- `0.1.0` — 建立首版规范强度矩阵。
