---
id: REF-0017
title: 生命宪章双语歧义与专业审查登记
status: Draft
version: 0.2.0-draft.1
layer: Reference
owner: Ming Foundation Charter Review
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
  - REF-0015
  - REF-0016
  - REF-0018
depends_on:
  - MF-0004
  - MF-0006
---

# REF-0017 — 生命宪章双语歧义与专业审查登记

> 本登记保存未解决问题。列入本表不表示问题已经解决，也不表示某个领域
> 审查已经真实发生。

## 1. 风险等级

- `Critical`：可能改变安全、儿童、同意、数据权利、法律义务或第三方权利；
- `High`：可能实质改变条款范围、主体性或执行方式；
- `Medium`：可能造成一致性、可测试性或跨场景解释差异；
- `Low`：编辑与表达问题，不改变主要权利义务。

## 2. 登记表

| ID | 位置 | 术语/表达 | 歧义或风险 | 等级 | 所需审查 | 当前处理 |
|---|---|---|---|---|---|---|
| AMB-001 | 全局 | life / 生命 | 可能指生物生命、人生、生活世界或伦理主体 | `High` | philosophy, affected-person, translation | 保持开放；不扩张为完整生态伦理 |
| AMB-002 | S01 | human life | 是否包括胎儿、严重失能者、逝者数据与群体利益 | `High` | legal, ethics, affected-person | 需要适用范围说明 |
| AMB-003 | C01 | credible evidence / 可信证据 | 谁判断可信、证据标准是否随场景变化 | `High` | evidence, professional, affected-person | 与 Evidence/Confidence 规范映射 |
| AMB-004 | C01 | lived experience / 真实生活经验 | 个人经验与可验证事实冲突时如何处理 | `High` | affected-person, evidence | 不得抹除经验，也不得把经验自动当作全部事实 |
| AMB-005 | C02/C05 | dignity / 尊严 | 缺少可操作判准，容易变成修辞 | `High` | affected-person, child-rights, legal | 通过反例和产品决定测试 |
| AMB-006 | C02/C04 | agency / 主体性 | 自主、能力、责任、依赖与关系性之间的边界 | `High` | affected-person, child-rights, professional | 与年龄、能力和代表权限一起审查 |
| AMB-007 | S02/C04 | lawful choices / 合法选择 | 不同司法辖区差异大，合法不自动等于伦理正当 | `High` | legal, ethics | 法律是下限，不替代宪章判断 |
| AMB-008 | C04 | imminent serious harm / 迫近的严重伤害 | 迫近性、严重性和证据阈值未定义 | `Critical` | safety, clinical, legal | 必须由安全协议与专业责任限定 |
| AMB-009 | C04 | ordinary consent / 普通同意 | 安全干预、监护同意与本人同意的关系 | `Critical` | privacy, legal, child-rights | 明确同意类型与代表权限 |
| AMB-010 | C05 | refusal / 拒绝 | 拒绝何时应被尊重，何时涉及他人权利或迫近风险 | `High` | affected-person, safety, legal | 不得把主体性等同无限免责 |
| AMB-011 | C06 | growth / 成长 | 谁定义成长，是否把适应系统当作成长 | `High` | affected-person, philosophy | 目标由当事人参与形成 |
| AMB-012 | C06 | conditions in which growth may occur | 系统支持条件与隐性操纵之间的边界 | `High` | affected-person, product, ethics | 共同创造、可拒绝、可退出 |
| AMB-013 | C07 | must consider | 需要考虑到何种深度才算满足 | `Medium` | architecture, evidence | 未来形成最低证据与记录要求 |
| AMB-014 | C08 | proportionate / 合比例 | 缺乏跨场景统一计算方式 | `Critical` | safety, legal, affected-person | 记录风险、替代方案、期限和副作用 |
| AMB-015 | C08 | minimally intrusive / 尽量减少侵入 | 技术、关系和制度侵入如何比较 | `High` | privacy, safety, child-rights | 采用最小必要与可逆原则 |
| AMB-016 | C08 | significant restrictions / 重大限制 | 何种限制触发完整记录和申诉 | `High` | legal, safety, privacy | 未来建立阈值与示例 |
| AMB-017 | C09 | meaningful interpretation / 具有实质影响的解释 | 哪些解释需要完整追溯 | `Medium` | architecture, affected-person | 按影响权利、行动与画像的程度判断 |
| AMB-018 | C10 | replace living / 替代生活本身 | 陪伴、自动化与替代之间缺少可测试边界 | `High` | affected-person, product, ethics | 以能力削弱、依赖和主体位置测试 |
| AMB-019 | C11 | meaningful rights / 具有实际意义的权利 | 仅提供按钮但无法完成是否算权利 | `Critical` | privacy, legal, accessibility | 必须可理解、可执行、有时限和救济 |
| AMB-020 | C11 | delete / 删除 | 备份、法定义务、事件证据与第三方权利冲突 | `Critical` | privacy, legal, safety | 依赖 retention/backup profile |
| AMB-021 | C12 | preserve failure and counterexample | 公开透明与隐私、安全、商业秘密冲突 | `High` | privacy, evidence, governance | 至少保留受控、可审计记录 |
| AMB-022 | C13 | affected person’s voice | 儿童、失语、危机与无法直接参与者如何表达 | `Critical` | child-rights, accessibility, professional | 多种表达方式与明确不可参与理由 |
| AMB-023 | C13 | currently possible or safe | 谁判断不可参与，如何防止长期排除 | `Critical` | affected-person, safety, legal | 期限、复核、替代参与和申诉 |
| AMB-024 | S05 | conflicts with this Charter | 测试是否允许合比例例外 | `High` | governance, legal | 由 S06 记录冲突与例外，不静默豁免 |
| AMB-025 | S08 | passing validation | 什么证据足以完成各审查轨道 | `High` | governance, all reviewers | 建立独立完成标准，不以开会代替验证 |
| AMB-026 | 全局 | MUST / SHOULD / MAY 大小写与强度 | MF-0004 尚未正式采用 RFC 2119/8174，当前强度矩阵只能是临时解释 | `High` | governance, translation, architecture | 标记为 provisional；不得据此自动产生技术符合性要求 |
| AMB-027 | C05 标题 | retain full dignity / 同样值得尊重 / 具有完整尊严 | “尊严”与“值得尊重”并非完全等价，可能改变权利强度 | `High` | affected-person, philosophy, translation | MF-0006 暂按英文来源；保留历史中文标题差异 |
| AMB-028 | C07 标题 | are part of life / 是生命展开的环境 / 是生命的一部分 | “构成生命的一部分”与“生命展开的环境”具有不同本体与关系含义 | `High` | philosophy, affected-person, translation | 不静默统一，进入语义审查 |
| AMB-029 | C12 标题 | are protected / 必须被保留 / 必须被保护 | “保护”可能比“保留证据”范围更广 | `High` | governance, privacy, translation | MF-0006 暂按英文标题；正文义务继续限定为保留错误证据和不隐藏 |
| AMB-030 | C04 干预条件 | lawful and proportionate intervention is required | “合法”“合比例”“必要”在中文句法中的修饰关系可能改变安全授权范围 | `Critical` | safety, legal, translation | Rev A 改为“有必要采取合法且合比例的干预”，仍待领域审查 |
| AMB-031 | C09 | meaningful interpretation | “重要解释”“有意义的解释”“具有实质影响的解释”可能形成不同追溯门槛 | `High` | affected-person, architecture, translation | Rev A 使用“重要解释”，保留门槛问题 |


## 2.1 内部架构审查边界

AMB-026 至 AMB-031 来自本次内部架构与文本一致性审查。它们的登记只说明
问题已经被发现，不构成翻译、法律、安全、儿童权利或受影响者审查完成证据。

## 3. 审查状态

当前全部项目均为：

```text
PreparedNotExecuted
```

不得把以下行为写成“已完成审查”：

- 由 AI 模拟儿童、家长、法律或临床意见；
- 仅由创始人或开发者内部阅读；
- 没有参与者记录和证据边界的讨论；
- 没有记录异议的共识会议；
- 只检查翻译是否流畅；
- 只检查仓库验证是否通过。

## 4. 歧义处置结果类型

每项审查只能使用以下结果之一：

- `ConfirmedEquivalent`：双语语义和强度等价；
- `EquivalentWithNote`：基本等价，但需保留解释说明；
- `SourceRevisionRequired`：英文来源需要修改；
- `TranslationRevisionRequired`：中文译文需要修改；
- `BothRevisionRequired`：两份文本都需修改；
- `DomainQualificationRequired`：需要司法辖区或专业限定；
- `UnresolvedDissent`：存在未解决异议；
- `BlockedPendingEvidence`：缺少证据，不能决定。

## 5. 合并与状态边界

本登记可以作为 Draft 合并，但：

- 不能据此把宪章提升为 Accepted；
- 不能把 `PreparedNotExecuted` 写成验证完成；
- Critical 项未处置前，不得宣布双语具有同等规范效力；
- 任何实质修改都必须回写正文并更新逐条映射；
- 异议不能因追求发布进度而删除。

## 6. 变更历史

- `0.2.0-draft.1` — 修正来源快照；新增规范词语义、三处内嵌标题差异、C04 干预条件和 C09 解释门槛等内部审查发现。
- `0.1.0` — 建立首版双语歧义登记。
