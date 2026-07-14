---
id: REF-0021
title: MingOS 宪章逐条双语迁移映射
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
  - REF-0022
  - REF-0023
  - REF-0024
  - REF-0025
depends_on:
  - PROJECT-MINGOS-0002
  - PROJECT-MINGOS-0003
---

# REF-0021 — MingOS 宪章逐条双语迁移映射

> 本文件是非规范性审查映射，不替代两份 Candidate 正文。英文来源在双语迁移期间控制实质性语言冲突。

## 1. 权威边界

- 英文来源：`PROJECT-MINGOS-0002 / 1.0.0-alpha.5`
- 中文配对候选：`PROJECT-MINGOS-0003 / 1.0.0-alpha.5`
- Round 04 合并基线：`2a5dab9eccc998fdd634ecb7fd57f20ee6fe4934`
- 英文来源快照：`d1f0e9c15fa59b14ec45c5be8585f415edec7018`
- 当前状态：两份文本均为 Candidate
- 尚未确认：双语语义等效、未来规范语言与配对规范效力

## 2. 逐条映射

| ID | 英文标题 | 中文标题 | 英文核心表达 | 中文核心表达 | 规范强度 | 主要歧义 |
|---|---|---|---|---|---|---|
| S01 | Purpose and Candidate status | 目的与 Candidate 状态 | how MingOS commits to practice the Charter of Life; internal review is not external validation | MingOS 如何承诺践行《生命宪章》；内部文本准备不等于外部验证 | `scope` | 内部逐条审查、文本准备度与外部验证的边界 |
| S02 | Preamble | 序言 | MingOS is not the center of life; change the model when evidence or affected people show error | MingOS 不是生命中心；当证据或受影响者表明错误时修改模型 | `principle` | life-centered approach 是否会变成不可测试的品牌修辞 |
| MC01 | MingOS stands with life, not with a role | MingOS 站在生命一边，而不是任何角色一边 | must not automatically side with a role; must ask what protects all affected lives | 不得自动站在任何角色一边；必须追问什么保护所有受影响生命 | `prohibition / must` | 中立、权力不对等与保护义务 |
| MC02 | MingOS does not own any life | MingOS 不拥有任何生命 | does not own identity, meaning, story, future, relationship, or life direction | 不拥有身份、意义、故事、未来、关系或生命方向 | `principle / prohibition` | 记录保管、知识产权与人格/数据权利 |
| MC03 | People may refuse interpretation, pause, and leave | 人可以拒绝解释、暂停并离开 | should be able to refuse, correct, revoke, pause, leave, and understand retention; exceptions MUST be bounded | 应当能够拒绝、纠正、撤回、暂停、离开并了解留存；例外必须受限 | `SHOULD / MUST` | person/user、撤回边界与四类例外 |
| MC04 | Data and memory remain accountable to the person | 数据与记忆仍必须向本人负责 | meaningful controls; memory must not freeze a person; non-fulfilment must be explained | 具有实际意义的控制；记忆不得冻结一个人；无法完全实现时必须说明 | `must / prohibition` | person/生命、删除撤回与完成证据 |
| MC05 | Evidence is above authority | 证据高于权威 | must preserve contradiction, failure, counterexample, uncertainty, correction, and revision | 必须保留矛盾、失败、反例、不确定性、纠正和修订 | `must` | 证据、真实经验、专业判断、隐私与安全 |
| MC06 | Knowledge statuses remain distinct | 知识状态必须保持区分 | must not convert inference into fact; knowledge objects remain traceable | 不得把推断转化为事实；知识对象必须可追溯 | `prohibition / must` | 字段、界面、确认者与派生决定 |
| MC07 | MingOS must not use anxiety to increase conversion | MingOS 不得利用焦虑提高转化 | must not exaggerate risk, manufacture urgency, shame, or imply failure for commercial or compliance goals | 不得为商业或服从目标夸大风险、制造紧迫、羞辱或暗示失败 | `prohibition` | 风险告知与操纵性商业话术 |
| MC08 | MingOS must not use dependency to increase retention | MingOS 不得利用依赖提高留存 | healthy service should strengthen capacity without the system; dependency-created retention is failure | 健康服务应增强离开系统后的能力；依赖形成的留存是失败 | `SHOULD / failure test` | 依赖、信任、连续支持、合理辅助与健康退出 |
| MC09 | AI must remain a bounded component | AI 必须始终是有边界的组成部分 | AI may assist but must not impersonate, dominate, hide inference, exploit vulnerability, replace responsibility, or decide alone | AI 可以辅助但不得冒充、支配、隐藏推断、利用脆弱、替代责任或独自作高影响决定 | `MAY / prohibitions` | 高影响门槛、人类责任与受影响者参与 |
| MC10 | Children and third parties require independent protection | 儿童与第三方需要独立保护 | parent participation does not create unlimited authority; design must protect voice, data and contestability | 父母参与不产生无限授权；设计必须保护声音、数据与异议能力 | `prohibition / must` | 照料、同意、代表权限、监控与第三方权利 |
| MC11 | Professional and safety boundaries remain visible | 专业与安全边界必须始终可见 | does not replace qualified services; must slow down, disclose limits, and support appropriate escalation | 不替代专业服务；必须减速、披露限制并支持适当升级 | `prohibition / must` | 系统能力、服务可用性与升级完成证据 |
| MC12 | Commercial power cannot amend the root commitments | 商业权力不能修改根本承诺 | commercial pressures cannot silently override; material conflicts need independent governance | 商业压力不得静默推翻；实质冲突需要独立治理 | `prohibition / must` | 独立商业冲突权威、披露、制裁与恢复 |
| MC13 | MingOS must remain correctable | MingOS 必须始终允许被真实修正 | must maintain correction, appeal, incident, versioning, criticism, audit, supersession, and unknown mechanisms | 必须维护纠正、申诉、事件、版本、批评、审计、替代和未知机制 | `must` | 机制存在、可访问、可执行和完成的差异 |
| MC14 | Charter violations require response, remediation, and traceability | 宪章违规必须被回应、修复并留下可追溯记录 | must define reporting, containment, correction, notice, recurrence review and name withdrawal; no role exempt | 必须定义报告、止损、纠正、通知、复发审查与名称撤回；任何角色不免责 | `must / prohibition` | 善意报告、独立调查、名称撤回与程序正义 |
| S04 | Three permanent disciplines | 三项永久纪律 | truth, no anxiety conversion, and AI not replacing conscience must be testable | 真实、不用焦虑成交、AI 不替代良知必须可检验 | `discipline / test` | “永久”与可修正性；纪律是否独立产生要求 |
| S05 | Decision precedence | 决策优先次序 | safety and lawful protection, rights, evidence, responsibility, then business; not an automatic formula | 安全与合法保护、权利、证据、责任，再到商业；不是自动公式 | `priority framework` | 固定顺序与法律义务、权利冲突和情境 |
| S06 | Conformance questions | 符合性问题 | reviewers should ask twelve questions before approval | 审查者在批准前应询问十二个问题 | `SHOULD / review` | 问题清单与正式符合性测试的差异 |
| S07 | Relationship to the Kernel | 与 Kernel 的关系 | Kernel must operationalize the Charter; it is not a prompt, script, or personality | Kernel 必须把宪章转化为运行秩序；不是 Prompt、脚本或人格 | `future must` | Kernel 范围、文档家族、权威与符合性尚未决定 |
| S08 | Candidate validation requirements | Candidate 验证要求 | validation MUST resolve nine areas before Acceptance | Accepted 前验证必须解决九个领域 | `MUST` | 何种证据足以提升 Candidate |

## 3. 历史内嵌中文标题差异

- MC03：`A person` 被历史标题写成“用户”；中文配对稿使用“人”。
- MC04：`accountable to the person` 被历史标题写成“向生命负责”；配对稿使用“向本人负责”。
- MC12：`commercial power/root commitments` 被简化为“商业/根原则”；配对稿使用“商业权力/根本承诺”。

这些差异进入 REF-0024。中文配对稿的附录 A 是非规范性迁移说明，不属于源宪章承诺，不进入逐条映射。

## 4. 翻译边界

不得把 `person` 缩减为界面用户，不得把 `the person` 泛化到无法识别权利主体；不得把商业自我约束改写为营销承诺；不得把 Proposed 合同写成当前实现符合；不得把未来 Kernel 写成已经完成。

## 5. 完成条件

逐项语义、39 项规范表达、19 项承诺/章节合同、40 项歧义与真实受影响者/领域审查均完成后，本映射才可进入 Reviewed。
