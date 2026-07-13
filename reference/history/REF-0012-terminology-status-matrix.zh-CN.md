---
id: REF-0012
title: MingOS 核心术语状态矩阵
status: Draft
version: 0.2.0-draft.1
layer: Reference
owner: Ming Foundation Reference
created: 2026-07-13
updated: 2026-07-13
language: zh-CN
related:
  - REF-0002
  - REF-0010
  - REF-0011
  - MF-0005
depends_on:
  - REF-0010
---

# REF-0012 — MingOS 核心术语状态矩阵

> 本矩阵记录“当前如何使用某个词”，不直接修改 REF-0002。

## 1. 为什么不在本轮直接改术语表

历史映射需要先回答：

- 这个词最初做什么；
- 它是否已进入当前文本；
- 它是哲学、方法、产品对象还是规范术语；
- 哪些边界仍不清楚；
- 哪些英文翻译会改变含义。

在这些问题审查完成前直接修改 REF-0002，会让未决历史问题看起来已经定稿。

## 2. 术语权威状态

本文件的状态只回答“这个词当前以什么权威被使用”，不回答历史来源是否完整，
也不回答概念最终应被保留还是替代。

允许值：

| 状态 | 含义 |
|---|---|
| CurrentProjectName | 当前项目或仓库正式使用的名称 |
| DraftGlossary | 已进入 Draft 术语表 |
| InterpretiveCurrent | 已进入当前解释文本，但不是正式术语定义 |
| CanonicalReferenced | 当前原则、宪章或 Accepted 决议已经明确引用 |
| NeedsGlossaryReview | 尚未进入术语表，但应优先审查 |
| RFCReferenced | 已被 Proposed RFC 使用，权威不高于 RFC 状态 |
| MethodCandidate | 应用方法候选术语 |
| HistoricalMetaphor | 历史隐喻 |
| HistoricalStrategyLabel | 历史战略名称 |
| OpenResearchConcept | 开放研究概念 |
| ImplementationSpecific | 特定产品或代码对象 |

## 3. 状态矩阵

| 中文 | 英文/标识 | 类别 | 术语权威状态 | 当前含义 | 不应被理解为 |
|---|---|---|---|---|---|
| MingOS | MingOS | 项目名称 | `CurrentProjectName` | 项目和系统工程名称；正式英文全称仍待品牌治理 | 不得自动等同某一个产品或 AI |
| 生命操作系统 | Life Operating System | 中文解释/品牌方向 | `HistoricalStrategyLabel` | 解释 MingOS 的方向 | 不得理解为操作和控制生命 |
| 生命智能 | Living Intelligence | 核心术语 | `DraftGlossary` | 扎根生命、关系、情境、不确定性、意义、成长和主体性的智能 | 不得作为已验证科学学科名称 |
| 生命逻辑 | Life Logic | 哲学解释 | `InterpretiveCurrent` | 把生命、真实、关系、时间、主体性、责任和可修正性置于中心的秩序 | 不是温柔语气或万能方法 |
| 生命信号 | Life Signal | 身份概念 | `InterpretiveCurrent` | 暂停问题化判断并继续理解的解释性概念 | 不是诊断、分类或伤害合理化 |
| 生命时刻 | LifeMoment | 实现对象 | `ImplementationSpecific` | 产品中承载真实事件与连续对话的对象候选 | 不属于当前 Foundation 正式术语 |
| 可信生命对话 | Trustworthy Life Dialogue | 身份概念 | `InterpretiveCurrent` | 真实、可纠正、值得信赖的支持性对话 | 尚不是 Kernel 正式运行单元 |
| 共同创造条件 | Co-create Conditions | 参与原则 | `InterpretiveCurrent` | 受影响者参与支持条件、目标、行动和反馈形成 | 不等于角色责任完全相同 |
| 主体性 | Agency | 核心术语 | `DraftGlossary` | 理解、选择、拒绝、修正和行动的能力与权利 | 不等于任性或忽略他人权利 |
| 自主而不遗弃 | Agency without Abandonment | 文化原则 | `InterpretiveCurrent` | 尊重选择同时不在风险和脆弱中撤回责任 | 不是正式宪章条款 |
| 安全而不支配 | Safety without Domination | 第一原则 | `CanonicalReferenced` | 安全机制必须合比例、可解释、避免不必要控制 | 不等于不介入风险 |
| 受影响者 | Affected Person | 治理术语 | `NeedsGlossaryReview` | 受到系统决定、数据、解释或行动影响的人 | 不限于直接用户 |
| 发言者 | Speaker | 协议术语 | `RFCReferenced` | 向系统提供陈述的人 | 不自动等于被叙述者 |
| 被叙述者 | Subject | 协议术语 | `RFCReferenced` | 陈述、画像或决定所指向的人 | 不能被发言者完整代表 |
| 观察 | Observation | 核心术语 | `DraftGlossary` | 带证据、避免把解释写成确定性的描述 | 不是判断 |
| 假设 | Hypothesis | 核心术语 | `DraftGlossary` | 需要确认、证据或修正的可能解释 | 不是事实 |
| 循环 | Interaction Loop | 方法术语 | `MethodCandidate` | 反复互动中相互强化的行动与结果 | 不能抹平权力不对等 |
| 断点 | Breakpoint | 方法术语 | `MethodCandidate` | 改变循环走向的小、安全、可逆行动点 | 不是操纵他人的技巧 |
| 三系统 | Goal–Event–Causal Systems | 方法体系 | `MethodCandidate` | 目标、事件与因果三个实践视角 | 不是 Foundation 三层根文本 |
| 灵魂层 | Soul Layer | 历史隐喻 | `HistoricalMetaphor` | 强调人文、主体性和语言温度 | 不作为可审计架构层 |
| 开放生命协议 | Open Life Protocol | 历史战略名 | `HistoricalStrategyLabel` | 开放、可互操作的生命信息协议愿景 | 当前正式协议由 MOS/RFC 承担 |
| 生命语法 | Life Grammar | 研究概念 | `OpenResearchConcept` | 探索事件、关系、状态和意义的表达结构 | 不得声称已发现生命客观语法 |

## 4. 优先进入下一次 REF-0002 修订的术语

建议优先评审：

1. Life Logic / 生命逻辑；
2. Affected Person / 受影响者；
3. Speaker / Subject；
4. Responsibility / 责任；
5. Correction / Contestability；
6. Life Signal / 生命信号；
7. Trustworthy Life Dialogue；
8. Co-created Conditions；
9. Safety without Domination；
10. Agency without Abandonment。

进入术语表前应明确：

- 是否为规范定义；
- 是否跨场景适用；
- 是否需要证据限定；
- 是否有法律、临床或文化歧义；
- 中英文是否同等权威。

## 5. 明确不建议成为当前正式术语的表达

- 灵魂层；
- 安内后攘外；
- 成绩是果，思维与关系是因；
- 已发现的生命规律；
- AI 心理咨询师；
- 全自动生命画像；
- 万能家庭教育系统。

这些表达可以保留历史和传播语境，但不应作为当前规范标题。

## 6. 翻译风险

### 生命

`Life` 可能被读为生物生命、人生、生活世界或伦理主体。本项目当前主要
讨论人的生命与受系统影响的人际世界，不能假设所有语境完全等价。

### 主体性

`Agency` 强调行动与选择能力，但中文“主体性”还包含不被替代和作为
意义主体的哲学含义。翻译应保留责任和相互依存。

### 关系

`Relationship` 不能只表达社交连接，还包含历史、信任、照料、权力、
期待和冲突。

### 意义

`Meaning` 不能被系统当作可分配标签。系统可以支持探索，不能成为最终作者。

## 7. 变更历史

- `0.2.0-draft.1` — 为术语矩阵建立独立且完整的 `term_authority_status` 词表。
- `0.1.0` — 建立核心、方法、文化、实现和研究术语的状态矩阵。
