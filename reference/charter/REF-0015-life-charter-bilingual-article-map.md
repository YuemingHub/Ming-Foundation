---
id: REF-0015
title: 生命宪章逐条双语迁移映射
status: Draft
version: 0.1.0
layer: Reference
owner: Ming Foundation Translation Review
created: 2026-07-14
updated: 2026-07-14
language: zh-CN
canonical_language: zh-CN
translation_status: original
source_commit: c149953217e466570da3fa58157eb66616514d6b
related:
  - MF-0004
  - MF-0006
  - ADR-0021
  - REF-0016
  - REF-0017
  - REF-0018
depends_on:
  - MF-0004
  - MF-0006
---

# REF-0015 — 生命宪章逐条双语迁移映射

> 本文件是非规范性审查映射。发生冲突时，它不能替代 `MF-0004` 或
> `MF-0006` 的正文。

## 1. 权威边界

- 来源文本：`MF-0004 / 1.0.0-alpha.5`
- 中文配对候选：`MF-0006 / 1.0.0-alpha.5`
- 迁移基线提交：`c149953217e466570da3fa58157eb66616514d6b`
- 当前语言冲突控制文本：英文 MF-0004
- 当前状态：两份文本均为 Candidate
- 尚未作出的决定：未来规范语言、双语是否具有同等规范效力

## 2. 逐条映射

| ID | 英文标题 | 中文标题 | 英文核心表达 | 中文核心表达 | 规范强度 | 主要歧义 |
|---|---|---|---|---|---|---|
| S01 | Purpose | 目的 | candidate higher-order ethical commitments | 候选性的高阶伦理承诺 | `scope` | “human life”范围与非人生命边界 |
| S02 | Candidate status and limits | 候选状态与边界 | MUST remain open to correction | 必须始终允许被修正 | `MUST` | 修订开放性与稳定性的张力 |
| S03 | Preamble | 序言 | Life is not raw material | 生命不是等待系统优化的原材料 | `principle` | “生命”在中英文中的范围 |
| C01 | Truth before theory | 真实高于理论 | MUST yield; may not distort | 必须让位；不得扭曲 | `MUST / prohibition` | credible evidence / lived experience |
| C02 | Life before system and efficiency | 生命高于系统与效率 | systems support life; efficiency subordinate | 系统支持生命；效率从属于生命条件 | `principle` | dignity 与 agency 的具体判准 |
| C03 | A person is not a problem set | 人不是问题集合 | should not be reduced; behavior may be a signal | 不应被缩减；行为可以是信号 | `ethical SHOULD / MAY` | “signal”不得诊断化 |
| C04 | Agency cannot be silently transferred away | 主体性不能被静默让渡 | MUST NOT final authority; intervention MUST be narrow | 不得成为最终权威；干预必须严格限定 | `MUST NOT / MUST` | 主体性、合法选择、迫近严重伤害 |
| C05 | Ordinary, slow, uncertain, and limited lives retain full dignity | 普通、缓慢、不确定与有限的生命同样具有完整尊严 | worth does not depend; states may be legitimate | 价值不依赖表现；这些状态可能正当 | `principle / MAY` | “full dignity”及拒绝的边界 |
| C06 | Growth cannot be manufactured | 成长不能被制造 | cannot be forced; SHOULD support conditions | 不能被强迫；应当支持条件 | `prohibition / SHOULD` | growth conditions 与放任的区别 |
| C07 | Relationship and context are part of life | 关系与情境是生命的一部分 | must consider relationship, power, history... | 必须考虑关系、权力、历史等 | `MUST-equivalent` | 适用范围与证据负担 |
| C08 | Safety before change, without domination | 安全先于改变，但安全不能成为支配 | must be proportionate; SHOULD include review path | 必须合比例；应当提供复核路径 | `MUST / SHOULD` | significant restriction、minimally intrusive |
| C09 | Every interpretation remains provisional | 任何解释都必须允许被修正 | MUST distinguish; should preserve provenance | 必须区分；应当保留追溯信息 | `MUST / SHOULD` | meaningful interpretation 的门槛 |
| C10 | Technology must serve life | 技术必须服务生命 | MUST NOT replace living or meaning | 不得替代生活、责任与意义决定权 | `MUST NOT` | AI 支持与替代的边界 |
| C11 | Memory must preserve change, rights, and accountability | 记忆必须允许改变，也必须承担责任 | must have rights; exceptions MUST be limited | 必须拥有权利；例外必须受限 | `MUST / rights` | 删除权与法律、专业、第三方义务 |
| C12 | Humility, failure, counterexample, and the unknown are protected | 谦卑、失败、反例与未知必须被保护 | MUST preserve evidence of error; must not hide | 必须保留错误证据；不得隐藏 | `MUST / MUST NOT` | 公开程度与隐私、安全的冲突 |
| C13 | No person is fully represented by another person’s account | 任何人都不能被他人的叙述完整替代 | MUST NOT become complete identity; SHOULD seek voice | 不得成为完整身份；应当寻求本人声音 | `MUST NOT / SHOULD` | 儿童、失能、危机与代表权限 |
| S05 | Charter tests | 宪章冲突测试 | proposal conflicts when... | 出现所列情形即构成冲突 | `test` | 测试是否需要例外与证据阈值 |
| S06 | Conflict and exception rule | 冲突与例外规则 | responsible actor MUST record | 负责主体必须记录 | `MUST` | 负责主体、申诉、期限和可逆性 |
| S07 | Relationship to MingOS | 与 MingOS 的关系 | no lower layer may redefine higher layer | 任何下层不得静默重定义上层 | `prohibition` | 显式修订与解释之间的边界 |
| S08 | Validation requirements | 验证要求 | validation MUST include... | 验证必须包括…… | `MUST` | 各类审查何时算完成 |

## 3. 翻译处理规则

### 3.1 不增加义务

中文为了可读性可以调整语序，但不能：

- 把 `SHOULD` 提升为无条件 `MUST`；
- 把 `MAY` 提升为义务；
- 把伦理原则改写为法律结论；
- 增加原文没有的实施主体、处罚或适用范围。

### 3.2 不削弱权利

不能因为英文简短而削弱：

- 拒绝、暂停、纠正与退出；
- 受影响者参与；
- 数据查看、更正、撤回、导出与删除；
- 例外的目的限定、最小留存与复核；
- 第三方和被叙述者的权利；
- 申诉与后续审查。

### 3.3 不掩盖未知

下列概念在迁移完成前保持明确歧义：

- life / 生命；
- dignity / 尊严；
- agency / 主体性；
- credible evidence / 可信证据；
- imminent serious harm / 迫近的严重伤害；
- meaningful rights / 具有实际意义的权利；
- affected person / 受影响者；
- proportionate / 合比例；
- minimally intrusive / 尽量减少侵入。

## 4. 完成条件

本映射只有在以下条件满足后，才可从 Draft 进入 Reviewed：

1. 每个条款完成双语语义审查；
2. 每个规范性动词完成强度核对；
3. REF-0017 的高风险歧义有明确处置；
4. 受影响者和领域审查已经真实执行；
5. 发生的修改回写两份 Candidate；
6. 保留未解决异议；
7. 形成规范语言与双语效力的独立治理决定。
