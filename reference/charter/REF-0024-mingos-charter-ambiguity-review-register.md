---
id: REF-0024
title: MingOS 宪章双语歧义与领域审查登记
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
owner: Ming Foundation Charter Review
related:
  - PROJECT-MINGOS-0002
  - PROJECT-MINGOS-0003
  - REF-0021
  - REF-0022
  - REF-0023
  - REF-0025
depends_on:
  - PROJECT-MINGOS-0002
  - PROJECT-MINGOS-0003
---

# REF-0024 — MingOS 宪章双语歧义与领域审查登记

> 登记不表示问题已经解决，也不表示任何正式受影响者、法律、安全、商业、专业或翻译审查已经执行。

## 1. 风险等级

- `Critical`：可能改变权利、安全、儿童、第三方、数据、专业、商业执行或 MingOS 名称使用；
- `High`：可能实质改变承诺范围、强度、治理或实现；
- `Medium`：可能造成一致性或可测试性差异；
- `Low`：编辑性问题，不改变主要承诺。

## 2. 登记表

| ID | 位置 | 术语/表达 | 歧义或风险 | 等级 | 所需审查 | 当前处理 | 状态 |
|---|---|---|---|---|---|---|---|
| AMB-MC-001 | S01 | passed an internal article-by-article review | 内部文本准备可能被误解为验证完成 | `High` | governance, affected-person | 保持 Candidate；区分文本准备与外部验证 | `PreparedNotExecuted` |
| AMB-MC-002 | S02 | life-centered approach / 以生命为中心 | 可能成为不可测试的品牌修辞 | `High` | affected-person, philosophy, public-claims | 用具体决定、失败与伤害路径检验 | `PreparedNotExecuted` |
| AMB-MC-003 | MC01 | stands with life, not with a role | 可能被误读为角色中立，忽略权力不对等与保护义务 | `Critical` | child-rights, safety, legal, affected-person | 不自动站队不等于不承担保护责任 | `PreparedNotExecuted` |
| AMB-MC-004 | MC01 | all affected lives | 范围可能包括非用户、家庭成员、工作人员与群体 | `High` | affected-person, architecture | 明确受影响者识别与冲突处理 | `PreparedNotExecuted` |
| AMB-MC-005 | MC02 | does not own / 不拥有 | 记录保管、知识产权和个人对身份意义之权利边界未明确 | `High` | privacy, legal, governance | 区分记录保管、版权与人格/数据权利 | `PreparedNotExecuted` |
| AMB-MC-006 | MC03 标题 | A person / 用户 / 人 | 历史中文标题把 person 缩减为 user，可能排除儿童与第三方 | `Critical` | affected-person, child-rights, translation | 中文配对稿使用“人”，保留历史差异 | `PreparedNotExecuted` |
| AMB-MC-007 | MC03 | should be able to | 是伦理方向、最低产品能力还是可执行权利尚未决定 | `High` | privacy, legal, product | 规范强度保持 provisional | `PreparedNotExecuted` |
| AMB-MC-008 | MC03 | within defined limits | 撤回限定可能被平台任意扩大 | `Critical` | privacy, legal, affected-person | 限定必须来自明确合同、目的与复核 | `PreparedNotExecuted` |
| AMB-MC-009 | MC03 | law, imminent safety, incident handling, protection of others | 四类例外的权威、证据、期限与通知义务不同 | `Critical` | safety, legal, privacy | 逐类合同化，不允许一般例外 | `PreparedNotExecuted` |
| AMB-MC-010 | MC04 标题 | accountable to the person / 向生命负责 / 向本人负责 | “生命”可能掩盖具体权利主体 | `High` | privacy, affected-person, translation | 中文配对稿使用“本人” | `PreparedNotExecuted` |
| AMB-MC-011 | MC04 | meaningful controls | 仅有按钮但无法完成是否算控制 | `Critical` | privacy, accessibility, product | 必须可理解、可执行、有完成证据与救济 | `PreparedNotExecuted` |
| AMB-MC-012 | MC04 | cannot be fully honored | 删除、撤回、备份、审计与第三方义务的边界 | `Critical` | privacy, legal, safety | 依赖 RFC-0002/PROF-0003 与司法辖区 | `PreparedNotExecuted` |
| AMB-MC-013 | MC05 | evidence is above authority | 证据、真实经验、专业判断与紧急行动冲突时如何排序 | `High` | evidence, professional, affected-person | 记录证据强度、未知与可修正性 | `PreparedNotExecuted` |
| AMB-MC-014 | MC05 | preserve contradiction and failure | 透明度与隐私、安全、商业秘密之间存在冲突 | `High` | privacy, governance, evidence | 至少保留受控、可审计证据 | `PreparedNotExecuted` |
| AMB-MC-015 | MC06 | fact / observation / hypothesis / pattern / judgment / decision | 跨系统字段、界面标签和决定依赖可能不一致 | `High` | architecture, affected-person | 依赖 RFC-0001 与未来 Kernel | `PreparedNotExecuted` |
| AMB-MC-016 | MC07 | anxiety / urgency / shame | 风险告知与操纵性商业话术的界限 | `Critical` | commercial, affected-person, safety | 审计内容、触发条件、受众与转化目标 | `PreparedNotExecuted` |
| AMB-MC-017 | MC07 | conversion, retain, upsell, compliance | 不同商业动作和非商业服从被放在同一禁止中 | `High` | commercial, governance | 建立商业行为分类与证据 | `PreparedNotExecuted` |
| AMB-MC-018 | MC08 | dependency | 依赖、信任、连续照护、习惯与必要辅助难以区分 | `Critical` | affected-person, professional, product | 需要独立合同与退出结果指标 | `PreparedNotExecuted` |
| AMB-MC-019 | MC08 | capacity without the system | 不应把完全独立作为所有人的成功标准 | `High` | accessibility, affected-person, professional | 保护可持续支持与选择性使用 | `PreparedNotExecuted` |
| AMB-MC-020 | MC09 | human professional | 不同司法辖区与专业角色定义不同 | `High` | professional, legal, public-claims | 角色、资质、可用性与责任必须可见 | `PreparedNotExecuted` |
| AMB-MC-021 | MC09 | high-impact decisions | 高影响门槛与参与最低要求尚未统一 | `Critical` | affected-person, safety, architecture | 映射 RFC-0001/3 与 Round 06 | `PreparedNotExecuted` |
| AMB-MC-022 | MC09 | appropriate human and affected-person participation | 何时参与充分、何时暂时不可行 | `Critical` | affected-person, child-rights, safety | 记录目的、影响、能力、代表与复核 | `PreparedNotExecuted` |
| AMB-MC-023 | MC10 | parent participation | 照料、同意、代表权限与数据访问经常被混淆 | `Critical` | child-rights, privacy, legal | 依赖 PROF-0001/2 与司法辖区 | `PreparedNotExecuted` |
| AMB-MC-024 | MC10 | where possible | 可能成为长期排除儿童或第三方的借口 | `Critical` | child-rights, accessibility | 记录期限、支持、替代参与与复核 | `PreparedNotExecuted` |
| AMB-MC-025 | MC10 | performance management | 家庭支持与绩效化监控边界不清 | `High` | affected-person, education, product | 禁止排名、羞辱与长期行为画像 | `PreparedNotExecuted` |
| AMB-MC-026 | MC11 | appropriate escalation | 没有可用服务时，升级可能只是生成链接 | `Critical` | safety, professional, operational | 使用 RFC-0003/PROF-0004 服务状态 | `PreparedNotExecuted` |
| AMB-MC-027 | MC11 | system competence | 能力范围由谁判断、如何更新与公开 | `High` | professional, architecture, public-claims | 记录能力状态、版本、证据与过期 | `PreparedNotExecuted` |
| AMB-MC-028 | MC12 标题 | commercial power / 商业 / root commitments / 根原则 | 历史中文标题可能缩小权力主体并改变文档层级 | `High` | commercial, translation, governance | 中文配对稿使用“商业权力/根本承诺” | `PreparedNotExecuted` |
| AMB-MC-029 | MC12 | actor with authority independent of immediate commercial objective | 独立主体尚未确定、授权或运营 | `Critical` | governance, commercial | 进入治理激活与冲突裁决合同 | `PreparedNotExecuted` |
| AMB-MC-030 | MC13 | maintain mechanisms | 机制存在、可访问、可执行与完成之间存在差异 | `Critical` | affected-person, operational, accessibility | 每个机制需要服务状态与完成证据 | `PreparedNotExecuted` |
| AMB-MC-031 | MC13 | independent criticism | 独立程度、保护和对治理的约束力不明确 | `High` | governance, community | 定义利益冲突、保护与回应义务 | `PreparedNotExecuted` |
| AMB-MC-032 | MC14 | good-faith reports | 谁判断善意，如何避免报复或压制异议 | `Critical` | governance, affected-person, legal | 提供保护、安全联系与独立复核 | `PreparedNotExecuted` |
| AMB-MC-033 | MC14 | withdraw MingOS name | 名称使用权、程序正义、恢复与公开说明未定义 | `Critical` | governance, legal, commercial | GOV-0015 与未来符合性合同 | `PreparedNotExecuted` |
| AMB-MC-034 | S04 | permanent disciplines | “永久”与宪章可修正性存在张力 | `High` | governance, philosophy | 解释为长期纪律，不取消显式修订 | `PreparedNotExecuted` |
| AMB-MC-035 | S05 | decision precedence | 固定顺序可能与法律义务、权利冲突与具体情境不一致 | `Critical` | legal, safety, affected-person | 不是自动公式，必须记录冲突 | `PreparedNotExecuted` |
| AMB-MC-036 | S06 | conformance questions | 问题清单容易被当作通过即合规 | `High` | architecture, governance | Round 09 转为有证据且可失败的测试 | `PreparedNotExecuted` |
| AMB-MC-037 | S07 | Kernel must operationalize | Kernel 尚未完成范围与权威决议 | `Critical` | architecture, governance | 保持 FutureKernelDecision | `PreparedNotExecuted` |
| AMB-MC-038 | S07 | all implementations must satisfy | MingOS 名称使用与符合性门槛尚未定义 | `Critical` | governance, architecture, commercial | Round 06/09 决议 | `PreparedNotExecuted` |
| AMB-MC-039 | S08 | current website, Family OS, communication, sales, implementation audits | 审计范围、证据时效与仓库访问可能不同 | `High` | governance, implementation, commercial | 分离仓库证据与外部实现证据 | `PreparedNotExecuted` |
| AMB-MC-040 | 全局 | MUST / must / should / may | MingOS 宪章未正式采用 RFC 2119/8174 | `High` | governance, translation, architecture | 所有强度映射保持 provisional，除明确大写案例 | `PreparedNotExecuted` |

## 3. 当前审查状态

```text
ReviewMaterialPrepared
OperationalAuthorizationNotGranted
ReviewNotExecuted
```

Critical 项未处置前，不得宣布双语等效、实现符合、名称使用符合或提升 Charter 状态。
