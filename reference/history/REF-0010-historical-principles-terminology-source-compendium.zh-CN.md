---
id: REF-0010
title: MingOS 历史原则、术语与来源映射总集
status: Draft
version: 0.2.0-draft.1
layer: Reference
owner: Ming Foundation Reference
created: 2026-07-13
updated: 2026-07-13
language: zh-CN
canonical_language: zh-CN
translation_status: original
related:
  - MF-0003
  - MF-0004
  - MF-0005
  - PROJECT-MINGOS-0002
  - GOV-0081
  - GOV-0082
  - REF-0002
  - REF-0011
  - REF-0012
  - REF-0013
  - REF-0014
depends_on:
  - MF-0005
  - GOV-0081
  - GOV-0082
---

# REF-0010 — MingOS 历史原则、术语与来源映射总集

> **状态：Draft。**
>
> 本文件是 Round 03 合集的唯一主入口。REF-0011 至 REF-0014 和
> `mingos-historical-concept-map.json` 是配套映射，不构成新的根文本。
>
> 本合集保存项目记忆，但不把历史提法静默提升为当前标准。

## 1. 为什么需要这个合集

MingOS 在形成正式仓库之前，已经产生了大量原则、隐喻、方法、产品对象、
安全门和架构名称。

这些内容既包含项目最有价值的思想来源，也包含几个风险：

- 同一个概念在不同阶段使用不同名称；
- 早期口号比当前规范更容易被记住，形成“影子标准”；
- 方法论可能被误当成普遍生命规律；
- 产品代码可能反向定义 Foundation；
- 已被吸收的旧原则仍被当作独立权威；
- 原始文本没有恢复时，后来者可能凭记忆重新编造；
- 私人对话和家庭案例可能被错误搬进公共仓库。

本合集的目标不是“证明历史一直正确”，而是让历史可追溯、可修正、
可放弃、可继承。

## 2. 合集结构

```text
REF-0010  历史原则、术语与来源映射总集（主入口）
   ├── REF-0011  历史原则演化对照表
   ├── REF-0012  核心术语状态矩阵
   ├── REF-0013  来源、追溯与隐私登记
   ├── REF-0014  方法体系与 Kernel 边界图
   └── mingos-historical-concept-map.json
       机器可读、非规范派生映射
```

本轮不修改 `REF-0002 — Core Terms`。正式术语表的更新应以本合集审查结果
为依据，在后续独立修订中完成。

## 3. 权威边界

本合集是 Reference Draft，不是：

- 《生命宪章》；
- 《MingOS 宪章》；
- MingOS Kernel；
- 家庭教育应用标准；
- 已验证科学理论；
- 对历史私人对话的公开归档；
- 对旧代码继续有效的承诺。

当本合集与当前仓库文件冲突时，应按状态、依赖关系和明确替代记录判断。
历史来源不能覆盖 Accepted 决议或 Candidate 宪章。

## 4. 来源可信度原则

本合集使用四个来源判断维度：

1. **来源是否可定位**：能否找到文件、提交、记录或明确时间段；
2. **文本是否完整**：是逐条原文、片段、摘要还是二手记忆；
3. **当前是否被吸收**：是否已进入 MF、Charter、ADR、RFC 或 Profile；
4. **是否适合公开**：是否包含私人表达、家庭案例或可识别信息。

来源和隐私规则详见 REF-0013。

## 5. 三轴映射模型

历史材料不能只用一个 `current_status` 字段描述。

一个历史概念至少同时包含三个不同问题：

1. **来源证据状态**：我们凭什么知道它曾经存在、内容是否完整；
2. **历史处置状态**：当前决定保留、吸收、收窄、降级还是继续等待；
3. **术语权威状态**：这个词目前是项目名、术语表定义、RFC 用语、解释性概念还是历史名称。

如果三者混在一个“状态”字段中，就会出现：

- 来源尚未恢复，却看起来已经完成处置；
- 一个词被当前文件引用，却看起来已经成为正式术语；
- 代码中存在一个对象，就看起来已经进入 Kernel；
- “待验证”同时表示证据不足、定义未定和治理未决。

### 5.1 来源证据状态

| 状态 | 含义 |
|---|---|
| CurrentRepositoryEvidence | 当前仓库可以定位到该概念或边界，但不自动证明其早期原文 |
| LocatedHistoricalEvidence | 历史来源已有可核验定位、版本或完整性记录 |
| ImplementationEvidence | 代码、产品文档或运行记录可以证明某种实现曾存在 |
| SecondaryOnly | 当前只有摘要、二手整理或回忆，不能作为逐条原文 |
| NamedOnly | 只能确认集合名或概念名，无法确认完整内容 |
| SourceMissing | 连名称、语境或来源都不足以支持历史判断 |

### 5.2 历史处置状态

| 状态 | 含义 |
|---|---|
| CanonicalReferenced | 当前权威文本已经明确规定，本合集只做引用 |
| InterpretiveCurrent | 已进入当前 Draft 解释层，但不是独立规范 |
| CulturalMaxim | 保留文化和传播价值，不能替代工程、权利和治理要求 |
| MethodCandidate | 实践方法候选，需要应用规范、证据和边界验证 |
| ImplementationHistorical | 历史运行标签，具体实现已迁移或需要迁移 |
| ImplementationSpecific | 特定产品或代码对象，不自动成为 Foundation 或 Kernel 标准 |
| HistoricalMetaphor | 适合解释，不适合作为可审计规范 |
| HistoricalAlias | 保留项目记忆，正式文本使用更清晰的当前名称 |
| NarrowedSlogan | 原表达有传播价值，但因因果过强或边界不足需要收窄 |
| HistoricalExplanatoryFrame | 历史解释框架，尚未成为正式命名或定义 |
| ArchitectureDirection | 架构方向较稳定，具体对象和协议尚未完成 |
| StrategyLabel | 战略表达，不得被当作已经交付的能力 |
| HistoricalStrategyLabel | 历史战略名称，当前正式体系由其他文件承载 |
| OpenResearchConcept | 开放研究概念，不能声称已被验证 |
| PartiallyAbsorbed | 部分内容进入后续文本，但不能假定完全一一对应 |
| RetainedPendingSource | 保留概念或集合名，等待原始来源恢复后再决定最终处置 |

### 5.3 术语权威状态

术语矩阵使用独立的 `term_authority_status`：

| 状态 | 含义 |
|---|---|
| CurrentProjectName | 当前项目或仓库正式使用的名称 |
| DraftGlossary | 已进入 Draft 术语表 |
| InterpretiveCurrent | 已进入当前解释文本，但尚未成为正式术语定义 |
| CanonicalReferenced | 已由当前原则、宪章或 Accepted 决议明确引用 |
| NeedsGlossaryReview | 需要进入下一次术语表审查 |
| RFCReferenced | 已被 Proposed RFC 使用，权威不高于 RFC 当前状态 |
| MethodCandidate | 应用方法候选术语 |
| HistoricalMetaphor | 历史隐喻，不作为正式技术术语 |
| HistoricalStrategyLabel | 历史战略名称，当前体系由其他文件承载 |
| OpenResearchConcept | 开放研究概念 |
| ImplementationSpecific | 特定产品或代码对象 |

三个轴必须分别记录。任何机器可读映射也必须使用三个命名空间，
不得继续使用含义不清的通用 `current_status`。

## 6. 五个历史概念家族

### 6.1 根原则与安全边界

包括：

- 九条公理；
- 十六条禁止；
- L1 安全门；
- 先人后事；
- 灵魂与安全线；
- 超层挑战。

其中，九条公理和十六条禁止的集合名称与历史作用可以确认，但目前没有
足够可靠的逐条原文来源。

因此，本合集明确：

> **不得根据后来的 MF-0003、MF-0004 或个人记忆反向“还原”一套看似
> 完整的九条和十六条。**

当前文本可以映射其功能，但不能声称一一等价。

### 6.2 家庭实践方法

包括：

- 规律—关系—驱动—投资；
- 目标系统—事件系统—因果系统；
- 事件链；
- 目标树；
- 循环图；
- 断点设计。

这些内容是用户长期家庭工作中形成的重要方法骨架。

它们当前应定位为 **MethodCandidate**：

- 可以进入家庭教育应用规范；
- 可以形成模板、训练和案例验证；
- 部分通用对象可以为 Kernel 提供输入；
- 不能直接升级为所有生命场景的普遍规律；
- 不能未经受影响者和证据审查就成为 Foundation 根原则。

### 6.3 教育与文化隐喻

包括：

- 木匠与园丁；
- 从听话到对话；
- 安内后攘外；
- 成绩是果，思维与关系是因。

这些表达保留了项目的实践语言，但规范地位不同：

- “木匠与园丁”“听话到对话”已进入 MF-0005 解释层；
- “安内后攘外”应在正式文本中改为“先稳定，再处理任务”；
- “成绩是果……”必须收窄为多因素表达，不能作为单向因果结论。

### 6.4 MingOS 身份概念

包括：

- Life Signal / 生命信号；
- 一次真实、可纠正、值得信赖的生命对话；
- 共同创造条件；
- AI 只能照亮，不能占据；
- 不是替你决定，而是帮助你看见。

这些概念已进入 MF-0005，但仍属于解释性身份层。

它们为未来 Kernel 和产品提供方向，却不能代替：

- 同意；
- 权限；
- 数据对象；
- 风险升级；
- 人类负责；
- 审计；
- 符合性测试。

### 6.5 架构、命名与学习循环

包括：

- OS 的 Organizing / Orientation / Open System / Support System；
- 反馈驱动的持续进化；
- 生命信息基础设施；
- 开放生命协议；
- 生命语法；
- LifeMoment；
- Parent Understanding。

必须区分：

- 品牌与哲学解释；
- Foundation 架构方向；
- MOS/RFC 正式协议；
- 产品实现对象；
- 开放研究概念。

旧代码和旧命名不能反向定义当前 Foundation。

## 7. 当前处理决议摘要

### 保留并进入当前解释层

- 先人后事；
- 木匠与园丁；
- 从听话到对话；
- Life Signal；
- 可信生命对话；
- 共同创造条件；
- AI 两句边界表达；
- OS 不是操作生命的四重解释。

### 保留但降级为历史名称或传播简语

- 灵魂与安全线；
- 安内后攘外；
- 生命信息基础设施；
- 开放生命协议。

### 保留为方法候选

- 规律—关系—驱动—投资；
- 三系统；
- 事件链；
- 目标树；
- 循环图；
- 断点设计。

### 必须收窄

- “成绩是果，思维与关系是因”；
- 生命自组织与自修复的普遍表达；
- 把关系或内驱力写成单一原因的表达。

### 等待原始来源恢复

- 九条公理逐条文本；
- 十六条禁止逐条文本；
- 超层挑战的原始程序；
- “灵魂与安全线”的原始组成与适用范围。

### 保留为实现特定概念

- LifeMoment；
- Parent Understanding；
- 旧安全级别和产品内部模式。

## 8. 不能做的历史迁移

不得：

- 用当前条款伪造早期原文；
- 用历史口号覆盖当前宪章；
- 把家庭方法当作全局 Kernel；
- 把代码中的字段当作生命本体；
- 把私人案例作为公开来源证据；
- 因为某个概念“很像 MingOS”就自动保留；
- 把“曾经使用”写成“仍然有效”；
- 把外部理论名称当成 MingOS 已经验证的科学依据。

## 9. 与 REF-0002 的关系

REF-0002 当前定义了 Life、Person、Relationship、Context、Event、State、
Need、Emotion、Observation、Hypothesis、Pattern、Memory、Meaning、Growth、
Agency、Consent、Confidence 和 Evidence。

本合集建议下一次术语表修订优先审查：

- Life Logic / 生命逻辑；
- Life Signal / 生命信号；
- Living Intelligence / 生命智能；
- Trustworthy Life Dialogue / 可信生命对话；
- Co-created Conditions / 共同创造条件；
- Affected Person / 受影响者；
- Speaker / Subject；
- Responsibility / 责任；
- Correction / Contestability；
- Safety without Domination；
- Agency without Abandonment。

本轮不直接修改 REF-0002，避免把历史映射和正式定义变更混为一次操作。

## 10. 与 Kernel 的关系

本合集不定义 Kernel。

未来 Kernel 可以评估：

- Life Signal 是否成为对象、状态或解释标签；
- 可信生命对话是否成为运行单元、结果指标或审计对象；
- 事件链和循环图如何映射 Event、Timeline、Pattern；
- 最小断点如何映射 Action 和 Feedback；
- 共同创造条件如何进入 Consent、Participation 和 Decision；
- 超层挑战如何进入冲突升级和停止权。

具体边界见 REF-0014。

## 11. 来源缺口登记

当前最重要的来源缺口：

1. 九条公理的逐条原文；
2. 十六条禁止的逐条原文；
3. L1 安全门最早版本及版本差异；
4. 超层挑战的原始定义、触发者和程序；
5. 灵魂与安全线的最早完整文本；
6. 历史命名首次出现的时间和替代链。

来源缺口不是失败。

> **未知被明确保存，比填补一个看似完整但并不真实的历史更重要。**

## 12. Round 03 完成标准

Round 03 合集只有在以下条件满足后才可作为 Draft 合并：

- REF-0010 至 REF-0014 内容一致；
- 机器可读映射完整包含概念、术语、来源与 Kernel 边界，并与 Markdown 一致；
- 所有来源缺口保持可见；
- 没有可识别家庭或私人信息；
- 没有历史概念被静默升级为 Accepted；
- 没有修改两部宪章、Kernel、RFC、Profile 或 Conformance；
- 仓库校验通过；
- PR 保持 Draft，接受整体审查。

## 13. 后续路线

Round 03 合并后，不再继续拆分历史映射。

下一阶段应以“合集”为单位进入：

1. **Round 04 合集：生命宪章中文迁移包**
   - 中文 Candidate；
   - 逐条双语映射；
   - 规范强度矩阵；
   - 歧义与审查登记；
   - 不改变 Candidate 状态。

2. **Round 05 合集：MingOS 宪章中文迁移包**

3. **Round 06–09 合集：Kernel 范围、核心规范、数据模型与符合性**

## 14. 变更历史

- `0.2.0-draft.1` — 将单一状态拆分为来源证据、历史处置和术语权威三轴；补齐来源定位规则、机器映射范围和 Kernel 范围边界。
- `0.1.0` — 建立历史原则、术语、来源、隐私和 Kernel 边界的一体化映射总集。
