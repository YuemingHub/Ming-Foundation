---
id: REF-0011
title: MingOS 历史原则演化对照表
status: Draft
version: 0.2.0-draft.1
layer: Reference
owner: Ming Foundation Reference
created: 2026-07-13
updated: 2026-07-13
language: zh-CN
related:
  - REF-0010
  - MF-0003
  - MF-0004
  - MF-0005
  - PROJECT-MINGOS-0002
depends_on:
  - REF-0010
---

# REF-0011 — MingOS 历史原则演化对照表

> 本表说明历史概念现在被如何理解和安置。它不证明历史原文已经完整恢复。

## 1. 使用规则

- `source_status` 说明历史证据强度；`disposition_status` 说明当前处置，两者不得混用；
- “映射到”不代表逐条等价；
- `confidence` 表示对历史作用和迁移判断的可信程度；
- 来源缺失时必须保持 `UnresolvedSource`；
- 任何新原始证据都可以推翻本表。

## 2. 对照表

| 编号 | 历史概念 | 历史作用 | 来源证据 | 当前处置 | 当前映射 | 建议去向 | 可信度 |
|---|---|---|---|---|---|---|---|
| HIST-001 | 九条公理 | 早期不可变底座的原则集合，用来定义系统为何存在以及不可越过的方向。 | `NamedOnly` | `RetainedPendingSource` | MF-0003<br>MF-0004<br>MF-0005<br>PROJECT-MINGOS-0002 | 历史集合名保留；逐条原文恢复后再决定是否形成来源附录。 | medium |
| HIST-002 | 十六条禁止 | 早期负面边界集合，用禁止项限制控制、标签、越权、操纵和不安全输出。 | `NamedOnly` | `PartiallyAbsorbed` | MF-0004<br>PROJECT-MINGOS-0002<br>RFC-0003<br>MF-0005 | 保留集合名；逐条来源恢复后映射到宪章测试、产品禁止项和安全协议。 | medium |
| HIST-003 | L1 安全门 | 高风险场景进入常规理解和建议前的阻断、减速、人工接管或转介门。 | `ImplementationEvidence` | `ImplementationHistorical` | MF-0003:P10<br>MF-0004<br>RFC-0003 | 上层保留安全原则；具体级别、类别和动作由 RFC 与实现 Profile 管理。 | high |
| HIST-004 | 先人后事 | 先看见人及其处境，再处理行为、任务和结果。 | `SecondaryOnly` | `InterpretiveCurrent` | MF-0003:P01<br>MF-0003:P02<br>MF-0005 | 作为文化性简语保留；规范层使用“生命先于系统”“理解先于建议”。 | high |
| HIST-005 | 灵魂与安全线 | 把人文关怀、语言温度、主体性与风险边界放在同一底座中。 | `SecondaryOnly` | `HistoricalMetaphor` | MF-0005<br>MF-0003:P10<br>RFC-0003 | 拆分为文化表达、输出规范和安全协议；不作为正式架构层名。 | medium |
| HIST-006 | 超层挑战 | 当下层实现、方法或业务目标与更高层生命原则冲突时，允许触发跨层质疑和停止。 | `SecondaryOnly` | `RetainedPendingSource` | ADR-0005<br>GOV-0003<br>GOV-0081<br>MF-0004 | 未来治理规范中的跨层冲突与升级机制；恢复原始定义前不作为正式术语。 | low |
| METH-001 | 规律—关系—驱动—投资 | 家庭教育内容主轴：尊重发展与现实规律，理解关系环境，看见内部驱动，审查长期投入方向。 | `SecondaryOnly` | `MethodCandidate` | MF-0005 | 家庭教育应用规范与证据地图，不进入 Foundation 根原则编号。 | high |
| METH-002 | 目标系统—事件系统—因果系统 | 区分家庭想去哪里、实际发生了什么、哪些循环与信念维持现状。 | `SecondaryOnly` | `MethodCandidate` | MF-0005 | Family application profile；其中通用对象可被未来 Kernel 借鉴，但不能整套复制。 | high |
| METH-003 | 事件链 | 把抽象评价还原为触发、反应、行动、短期结果和后续循环。 | `SecondaryOnly` | `MethodCandidate` | MF-0005<br>ADR-0002 | 家庭应用模板；与 Kernel Event/Timeline 对象建立映射。 | high |
| METH-004 | 目标树 | 区分表层目标、中层保护和深层需要或生命方向。 | `SecondaryOnly` | `MethodCandidate` | MF-0005<br>REF-0002:Need | 家庭应用模板与训练材料。 | high |
| METH-005 | 循环图 | 呈现关系中相互强化的行动、解释和结果。 | `SecondaryOnly` | `MethodCandidate` | MF-0005<br>REF-0002:Pattern | 家庭应用规范与 Pattern 数据映射。 | high |
| METH-006 | 断点设计 | 寻找家庭当前能够承担的小、安全、可逆变化点。 | `SecondaryOnly` | `MethodCandidate` | MF-0003:P02<br>MF-0005 | 家庭应用规范；未来与最小行动协议关联。 | high |
| METH-007 | 木匠与园丁 | 从按图塑造儿童转向支持生命在条件中成长。 | `SecondaryOnly` | `InterpretiveCurrent` | MF-0005 | 课程、公共沟通和应用导读；不作为科学分类。 | high |
| METH-008 | 从听话到对话 | 让儿童逐步进入规则理解、表达、协商和责任承担。 | `SecondaryOnly` | `InterpretiveCurrent` | MF-0005 | 教育应用规范与儿童参与规则。 | high |
| METH-009 | 安内后攘外 | 在学习、返校或行为要求之前，先处理情绪、安全和关系稳定。 | `SecondaryOnly` | `HistoricalAlias` | MF-0005<br>RFC-0003 | 公共文本改写为“先稳定，再处理任务”；原语保留于历史映射。 | high |
| METH-010 | 成绩是果，思维与关系是因 | 提醒家长不要只购买结果，而要理解能力、思维、情绪和关系条件。 | `SecondaryOnly` | `NarrowedSlogan` | MF-0005 | 保留为传播史料；正式表达改为“成绩是多因素结果”。 | high |
| IDEN-001 | Life Signal / 生命信号 | 把问题行为转为需要继续理解、核对和回应的生命表达。 | `CurrentRepositoryEvidence` | `InterpretiveCurrent` | MF-0005 | Round 06/07 决定是否进入 Kernel 对象模型；当前不视为诊断类别。 | high |
| IDEN-002 | 一次真实、可纠正、值得信赖的生命对话 | 把价值单位从回答数量和使用时长转向可信理解与可修正行动。 | `CurrentRepositoryEvidence` | `InterpretiveCurrent` | MF-0005 | 未来 Kernel 运行单元和产品指标候选；当前不替代正式协议。 | high |
| IDEN-003 | 共同创造条件 | 系统与受影响者共同形成支持条件，而非专家单方面设计成长环境。 | `CurrentRepositoryEvidence` | `InterpretiveCurrent` | MF-0005<br>MF-0004 | 参与、同意与行动协议；保留角色责任差异。 | high |
| IDEN-004 | AI 只能照亮，不能占据 | 限制 AI 占据人的意义、关系、判断和生活主体位置。 | `CurrentRepositoryEvidence` | `CulturalMaxim` | MF-0005<br>ADR-0001<br>MF-0004 | 公共文化表达；技术约束仍由同意、权限、审计和安全协议承担。 | high |
| IDEN-005 | 不是替你决定，而是帮助你看见 | 说明 AI 支持反思、澄清与选项，但不成为最终作者。 | `CurrentRepositoryEvidence` | `CulturalMaxim` | MF-0003:P06<br>MF-0005 | 公共沟通与产品语言；不能覆盖必要安全义务。 | high |
| ARCH-001 | OS 四重解释 | 解释 OS 不是操作生命，而是组织理解、支持方向、保持开放和提供支持。 | `CurrentRepositoryEvidence` | `HistoricalExplanatoryFrame` | MF-0005 | 品牌与架构解释；不得声称为已接受的官方英文展开。 | high |
| ARCH-002 | 反馈驱动的持续进化 | 现实—观察—抽象—实践—反馈—修正—再验证的学习循环。 | `CurrentRepositoryEvidence` | `ArchitectureDirection` | MF-0000<br>MF-0005 | Observatory、Lab、Kernel learning loop 和治理版本机制。 | high |
| ARCH-003 | 生命信息基础设施 | 用身份、关系、时间、状态、记忆、同意和修正支撑生命智能系统。 | `CurrentRepositoryEvidence` | `StrategyLabel` | MF-0001<br>MF-0005 | 使命和架构解释；不要作为已实现能力声明。 | medium |
| ARCH-004 | 开放生命协议 | 跨产品、跨组织表达生命、关系、同意和修正的开放协议设想。 | `CurrentRepositoryEvidence` | `HistoricalStrategyLabel` | MOS-0000<br>RFC-0001<br>RFC-0002 | 保留为历史愿景；正式协议由 MOS/RFC 体系承载。 | medium |
| ARCH-005 | 生命语法 | 尝试描述生命事件、关系、状态、意义和变化的基本表达结构。 | `CurrentRepositoryEvidence` | `OpenResearchConcept` | MF-0000<br>REF-0002 | 研究问题和数据模型探索；不作为已发现的普遍语法。 | medium |
| IMPL-001 | LifeMoment | 产品中用于承载家庭真实时刻和连续对话的对象设想。 | `ImplementationEvidence` | `ImplementationSpecific` | — | 产品实现或未来 Kernel 评审；不得由旧代码反向定义 Foundation。 | medium |
| IMPL-002 | Parent Understanding | 系统对家长的可纠正、版本化和受限理解对象。 | `ImplementationEvidence` | `ImplementationSpecific` | RFC-0001<br>RFC-0002 | 产品实现评审；名称和字段不得成为人格画像或商业操纵工具。 | medium |

## 2.1 三轴解释

本表只显示来源证据和历史处置两个轴。术语权威由 REF-0012 单独管理。

例如：

- “九条公理”是 `NamedOnly + RetainedPendingSource`；
- “十六条禁止”是 `NamedOnly + PartiallyAbsorbed`；
- “Life Signal”是 `CurrentRepositoryEvidence + InterpretiveCurrent`。

这比单一状态更准确：来源不完整，不等于当前不能决定“保留集合名”；
已经部分吸收，也不等于原始文本已经恢复。

## 3. 集合级历史结论

### 九条公理

可以确认：

- 它是早期不可变底座的一部分；
- 它承担正向原则功能；
- 后续第一原则、生命宪章和 MingOS 宪章吸收了相近方向。

不能确认：

- 九条的可靠逐条原文；
- 当前十二条 First Principles 是否由九条逐条演化；
- 哪些条目被删除、拆分或重写。

因此不制作虚构的 1:1 对照。

### 十六条禁止

可以确认：

- 它承担负面边界和输出禁止功能；
- 后续宪章测试、商业禁止、安全协议和产品语言规范吸收了相近边界。

不能确认：

- 十六条原文；
- 当前禁止项与历史十六条的完整对应；
- 不同历史版本是否保持同一数量和内容。

### L1 安全门

可以确认：

- 它是一种进入常规建议前的风险门；
- 后续实现出现过 RED/YELLOW/ORANGE/GREEN 等具体分级；
- 当前 Foundation 已由 P10、Charter 和 RFC-0003 承担上层安全边界。

不得把某一个产品版本的风险枚举固化为所有 MingOS 实现的永久规范。

## 4. 状态变更程序

历史概念只有在满足下列条件时才能改变本表状态：

1. 找到可定位来源；
2. 完成文本完整性审查；
3. 明确与当前权威文本的关系；
4. 审查隐私与公开边界；
5. 记录保留、合并、收窄、拒绝或替代理由；
6. 通过 Draft PR。

## 5. 变更历史

- `0.2.0-draft.1` — 将历史来源证据与当前处置拆分为两个独立轴。
- `0.1.0` — 建立首轮历史原则、方法、身份概念和架构命名对照。
