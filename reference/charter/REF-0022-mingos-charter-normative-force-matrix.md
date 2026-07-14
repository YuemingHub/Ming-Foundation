---
id: REF-0022
title: MingOS 宪章规范强度与关键词矩阵
status: Draft
version: 0.2.0-draft.1
layer: Reference
created: 2026-07-14
updated: 2026-07-14
language: zh-CN
canonical_language: zh-CN
translation_status: original
migration_base_commit: 2a5dab9eccc998fdd634ecb7fd57f20ee6fe4934
source_text_commit: d1f0e9c15fa59b14ec45c5be8585f415edec7018
owner: Ming Foundation Translation Review
related:
  - PROJECT-MINGOS-0002
  - PROJECT-MINGOS-0003
  - ADR-0021
  - REF-0021
  - REF-0023
  - REF-0024
depends_on:
  - PROJECT-MINGOS-0002
  - PROJECT-MINGOS-0003
---

# REF-0022 — MingOS 宪章规范强度与关键词矩阵

> **边界：** `PROJECT-MINGOS-0002` 尚未正式采用 RFC 2119/8174。本矩阵用于比较双语强度，不能自动生成技术符合性义务。明确大写 `MUST` 可以直接匹配；小写规范表达、普通语义禁止、原则、纪律与指令均为 `ProvisionalInterpretation`。

## 1. 映射状态

- `DirectCaseMatch`：来源使用明确大写规范词，译文保持同类强度；
- `ProvisionalInterpretation`：来源使用小写、普通禁止、原则、纪律或指令，强度仍待治理和领域审查。

## 2. 逐项矩阵

| ID | 位置 | 英文表达 | 中文表达 | 来源形式 | 中文词 | 映射状态 | 说明 |
|---|---|---|---|---|---|---|---|
| N01 | MC01 | must not automatically side | 不得自动站在任何角色一边 | `lowercase must not` | `不得` | `ProvisionalInterpretation` | 不自动站队不取消保护义务 |
| N02 | MC01 | must ask what protects... | 必须追问什么能够保护…… | `lowercase must` | `必须` | `ProvisionalInterpretation` | 需要可审计决策记录 |
| N03 | MC02 | may maintain authorized records | 可以维护经过授权的记录 | `lowercase may` | `可以` | `ProvisionalInterpretation` | 许可不等于授权来源已成立 |
| N04 | MC02 | does not own identity, meaning, story... | 不拥有身份、意义、故事等 | `principle/prohibition` | `不拥有` | `ProvisionalInterpretation` | 限制系统支配而非否定合法保管 |
| N05 | MC02 | No product language may imply... | 任何产品语言都不得暗示…… | `No ... may` | `不得` | `ProvisionalInterpretation` | 公共语言禁止 |
| N06 | MC03 | A person should be able to... | 一个人应当能够…… | `lowercase should` | `应当` | `ProvisionalInterpretation` | 权利方向，仍需可用机制 |
| N07 | MC03 | Refusal must not be treated... | 拒绝不得被视为…… | `lowercase must not` | `不得` | `ProvisionalInterpretation` | 拒绝不构成系统正确证据 |
| N08 | MC03 | exception ... MUST be narrowly stated... | 例外必须严格限定…… | `MUST` | `必须` | `DirectCaseMatch` | 四类例外需分别限定 |
| N09 | MC04 | must provide meaningful controls | 必须提供具有实际意义的控制 | `lowercase must` | `必须` | `ProvisionalInterpretation` | 需要 RFC-0002 与 Profile 支撑 |
| N10 | MC04 | Memory must not freeze... | 记忆不得冻结…… | `lowercase must not` | `不得` | `ProvisionalInterpretation` | 防止过去状态变永久身份 |
| N11 | MC04 | vulnerability must not become a permanent profile | 暂时脆弱不得成为永久画像 | `lowercase must not` | `不得` | `ProvisionalInterpretation` | 状态与身份分离 |
| N12 | MC04 | MingOS must explain... | MingOS 必须说明…… | `lowercase must` | `必须` | `ProvisionalInterpretation` | 删除与撤回例外透明度 |
| N13 | MC05 | are not above evidence | 不能凌驾于证据之上 | `principle/prohibition` | `不能` | `ProvisionalInterpretation` | 权威必须可被证据修正 |
| N14 | MC05 | must preserve contradiction, failure... | 必须保留矛盾、失败、反例…… | `lowercase must` | `必须` | `ProvisionalInterpretation` | 仍受隐私、安全和访问边界约束 |
| N15 | MC06 | must not convert inference into fact | 不得把推断转化为事实 | `lowercase must not` | `不得` | `ProvisionalInterpretation` | 知识状态分离 |
| N16 | MC06 | must remain traceable | 必须始终可追溯 | `lowercase must` | `必须` | `ProvisionalInterpretation` | 来源、主体、版本和修订 |
| N17 | MC07 | must not exaggerate/manufacture/shame... | 不得夸大、制造紧迫、羞辱或暗示失败 | `lowercase must not` | `不得` | `ProvisionalInterpretation` | 商业与服从目标禁止 |
| N18 | MC07 | Business design must not intensify fear | 商业设计不得加剧恐惧 | `lowercase must not` | `不得` | `ProvisionalInterpretation` | 需要销售和内容证据 |
| N19 | MC08 | service should strengthen capacity | 服务应当增强离开系统后的能力 | `lowercase should` | `应当` | `ProvisionalInterpretation` | 不承诺完全独立或具体结果 |
| N20 | MC08 | dependency-created retention is a failure | 依赖形成的留存是失败 | `failure test` | `失败` | `ProvisionalInterpretation` | 需区分必要持续支持 |
| N21 | MC09 | AI may summarize... | AI 可以总结并辅助…… | `lowercase may` | `可以` | `ProvisionalInterpretation` | 许可不等于当前能力 |
| N22 | MC09 | AI must not [six prohibitions] | AI 不得实施六类行为 | `lowercase must not` | `不得` | `ProvisionalInterpretation` | 参与门槛待合同化 |
| N23 | MC10 | parent participation does not automatically authorize... | 父母参与不自动授权…… | `prohibition` | `不自动授权` | `ProvisionalInterpretation` | 代表权限需要独立证据 |
| N24 | MC10 | MingOS must design for... | MingOS 必须围绕七项要求设计 | `lowercase must` | `必须` | `ProvisionalInterpretation` | RFC/Profile 仍为 Proposed |
| N25 | MC11 | does not replace qualified services or duties | 不替代专业服务或法定义务 | `prohibition` | `不替代` | `ProvisionalInterpretation` | 公开与产品边界 |
| N26 | MC11 | must slow down, disclose limits, and support escalation | 必须减速、披露限制并支持升级 | `lowercase must` | `必须` | `ProvisionalInterpretation` | 升级可用性必须真实 |
| N27 | MC12 | cannot silently override the Charter | 不能静默推翻本宪章 | `cannot` | `不能` | `ProvisionalInterpretation` | 商业权力边界 |
| N28 | MC12 | conflicts must be documented, reviewable, and independently governed | 冲突必须记录、复核并独立治理 | `lowercase must` | `必须` | `ProvisionalInterpretation` | 独立主体尚未运营 |
| N29 | MC13 | must maintain mechanisms | 必须维护八类机制 | `lowercase must` | `必须` | `ProvisionalInterpretation` | 机制存在不等于可用 |
| N30 | MC14 | A credible Charter must constrain conduct | 可信宪章必须约束行为 | `lowercase must` | `必须` | `ProvisionalInterpretation` | 需要执行与制裁合同 |
| N31 | MC14 | must define a process | 必须定义处理过程 | `lowercase must` | `必须` | `ProvisionalInterpretation` | GOV-0015 仍为 Proposed |
| N32 | MC14 | No person ... is exempt | 任何角色都不能免责 | `No ... is` | `不能` | `ProvisionalInterpretation` | 包括创始人、伙伴、专业人员与 AI |
| N33 | S04 | decisions must be testable | 决定必须可检验 | `lowercase must` | `必须` | `ProvisionalInterpretation` | 纪律尚未形成正式测试 |
| N34 | S05 | use this order | 使用这一顺序 | `directive` | `使用` | `ProvisionalInterpretation` | 不是自动公式 |
| N35 | S05 | conflicts must be documented | 冲突必须形成记录 | `lowercase must` | `必须` | `ProvisionalInterpretation` | 依赖 MF-0004 冲突规则 |
| N36 | S06 | reviewers should ask | 审查者应当询问 | `lowercase should` | `应当` | `ProvisionalInterpretation` | 问题清单不是符合性套件 |
| N37 | S07 | Kernel must operationalize | Kernel 必须转化承诺 | `lowercase must` | `必须` | `ProvisionalInterpretation` | Round 06 尚未定义 Kernel |
| N38 | S07 | all implementations must satisfy | 所有实现都必须满足 | `lowercase must` | `必须` | `ProvisionalInterpretation` | 名称使用与符合性尚未定义 |
| N39 | S08 | validation MUST resolve | 验证必须解决九个领域 | `MUST` | `必须` | `DirectCaseMatch` | Candidate 提升前置条件 |

## 3. 禁区

不得把“应当能够”写成已运营的权利保证；不得把“AI 可以”写成当前能力；不得把 Proposed RFC/Profile 写成当前符合；不得把商业纪律弱化为品牌口号；不得把安全或法律例外扩大为无限授权；不得把未来 Kernel 写成已完成。

## 4. 完成边界

本矩阵登记 39 项表达，但不决定它们的最终规范效力。正式采用规范词语义需要独立治理决定。
