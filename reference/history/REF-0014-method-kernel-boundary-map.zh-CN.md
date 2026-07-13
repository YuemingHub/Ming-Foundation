---
id: REF-0014
title: MingOS 方法体系与 Kernel 边界图
status: Draft
version: 0.1.0
layer: Reference
owner: Ming Foundation Architecture
created: 2026-07-13
updated: 2026-07-13
language: zh-CN
related:
  - REF-0010
  - REF-0011
  - MF-0005
  - ADR-0005
  - RFC-0001
  - RFC-0002
  - RFC-0003
depends_on:
  - REF-0010
  - ADR-0005
---

# REF-0014 — MingOS 方法体系与 Kernel 边界图

## 1. 目的

MingOS 的历史方法非常丰富。未来 Kernel 需要从中学习，但不能把所有方法
直接写进内核。

本文件区分：

```text
哲学与宪章
  ↓ 约束
Kernel 通用对象与运行协议
  ↓ 支撑
家庭、教育、个人、社区等应用规范
  ↓ 实现
具体产品、Agent、H5 和服务流程
```

家庭方法可以验证 Kernel，但不能反向成为所有生命场景的普遍结构。

## 2. 边界矩阵

| 概念 | 原始层级 | 可能进入的位置 | 可以贡献 | 不得发生 |
|---|---|---|---|---|
| 规律—关系—驱动—投资 | 家庭方法体系 | 应用规范 | 可提供家庭理解顺序和内容框架 | 不能成为 Kernel 普遍推理顺序 |
| 三系统 | 家庭方法体系 | 应用规范 / 对象映射 | 目标、事件、因果可映射通用对象 | 不能整套复制为 Foundation 三层结构 |
| 事件链 | 家庭工具 | Event / Timeline 候选映射 | 帮助区分触发、行动、结果和时间 | 不能把解释写进事实链 |
| 目标树 | 家庭工具 | Goal / Need 候选映射 | 支持多层目标和需要确认 | 不能自动推断深层需要 |
| 循环图 | 家庭工具 | Pattern / Relationship Graph 候选映射 | 支持互动模式观察 | 不能抹平权力、伤害和责任 |
| 断点设计 | 家庭工具 | Action / Feedback 候选映射 | 支持小、安全、可逆行动 | 不能成为影响他人的操纵技术 |
| Life Signal | 解释性身份概念 | 未来 Kernel 决议 | 可成为观察入口、解释标签或状态候选 | 当前不是诊断或正式数据类型 |
| 可信生命对话 | 解释性工作单元 | 未来 Runtime / Outcome 决议 | 可帮助定义质量、纠正和反馈 | 当前不是正式会话协议 |
| 共同创造条件 | 参与原则 | Consent / Participation / Decision | 要求受影响者参与目标和行动 | 不抹平角色能力与法定责任 |
| L1 安全门 | 历史实现标签 | RFC-0003 / Profile | 提供风险阻断和接管历史经验 | 不作为所有实现固定等级 |
| 超层挑战 | 历史治理概念 | 未来 governance escalation | 可启发下层冲突上报和停止权 | 原程序未恢复前不能赋权 |
| OS 四重解释 | 品牌与架构解释 | 公共解释 | 说明 OS 不操作生命 | 不进入 runtime 对象 |
| 反馈驱动持续进化 | 架构方向 | Observatory / Lab / audit | 支持证据、反例和版本修正 | 反馈不自动等于知识 |
| LifeMoment | 实现对象 | 产品 / 待评审 | 可以承载事件、对话与状态 | 旧代码对象不自动进入 Kernel |
| Parent Understanding | 实现对象 | 产品 / RFC 映射 | 支持可纠正和版本化理解 | 不得用于商业操纵和永久画像 |

## 3. Kernel 只应吸收什么

Kernel 可以吸收跨场景、可审计、可测试的通用能力，例如：

- Person、Speaker、Subject；
- Relationship；
- Event 与 Timeline；
- Observation、Hypothesis、Pattern；
- State；
- Consent 与 Purpose；
- Memory 与 Revision；
- Risk、Incident、Appeal；
- Action、Feedback；
- Evidence、Confidence、Unknown；
- Audit 与 Version。

Kernel 不应吸收：

- 某个课程的章节顺序；
- “规律—关系—驱动—投资”作为硬编码推理顺序；
- 木匠、园丁、灵魂层等隐喻；
- 特定产品的按钮、模式和内部枚举；
- 未经证据支持的家庭因果假设；
- 只适用于家长场景的语言模板。

## 4. 方法进入 Kernel 的门槛

一个历史方法进入 Kernel 前必须回答：

1. 是否跨场景成立；
2. 是否可以清晰定义；
3. 是否可以区分事实和推断；
4. 是否允许受影响者纠正；
5. 是否有错误和副作用测试；
6. 是否与宪章权利一致；
7. 是否需要人工负责；
8. 是否能够版本化和废弃；
9. 是否已有更通用对象承载；
10. 是否会把文化隐喻固化为技术本体。

## 5. 家庭应用层建议

后续 Family application collection 可以包含：

- 规律—关系—驱动—投资解释；
- 三系统方法；
- 事件链模板；
- 目标树模板；
- 循环图模板；
- 断点设计；
- 家长状态门；
- 儿童与第三方声音；
- 风险与转介；
- 跟进与反馈；
- 失败、反例和案例边界。

它应依赖 Kernel，而不是替代 Kernel。

## 6. 历史实现迁移规则

旧代码或产品对象进入新架构时：

- 先说明历史用途；
- 映射到当前对象；
- 检查是否含操纵、画像和隐私风险；
- 记录保留、重写或废弃；
- 不保留仅因“已经写了很多代码”；
- 不使用旧 Kernel 名称证明当前 Kernel 已完成；
- 经测试和治理后才进入符合性声明。

## 7. 变更历史

- `0.1.0` — 建立历史方法、身份概念、实现对象与未来 Kernel 的边界。
