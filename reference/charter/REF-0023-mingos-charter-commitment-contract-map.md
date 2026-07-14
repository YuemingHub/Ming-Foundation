---
id: REF-0023
title: MingOS 宪章承诺—合同—实现状态映射
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
owner: Ming Foundation Architecture
related:
  - PROJECT-MINGOS-0002
  - PROJECT-MINGOS-0003
  - RFC-0001
  - RFC-0002
  - RFC-0003
  - RFC-0004
  - RFC-0005
  - PROF-0001
  - PROF-0002
  - PROF-0003
  - PROF-0004
  - GOV-0015
  - REF-0021
  - REF-0022
  - REF-0024
  - REF-0025
depends_on:
  - PROJECT-MINGOS-0002
  - ADR-0005
---

# REF-0023 — MingOS 宪章承诺—合同—实现状态映射

> 本文件不声明任何当前实现符合 MingOS 宪章。RFC、Profile 与 GOV-0015 的 Proposed 状态必须保持可见。

## 1. 状态词表

### 合同状态

- `CoveredByProposedContracts`：存在明确 Proposed 合同，不表示 Accepted 或已实现；
- `PartiallyCovered`：已有部分合同，仍有跨文档或执行缺口；
- `GovernanceProcedureProposed`：已有 Proposed 治理程序；
- `ReviewMaterialOnly`：只有审查材料，没有运行合同；
- `ReviewMaterialPrepared`：材料已准备，真实执行未开始；
- `FutureKernelDecision`：依赖 Round 06 的 Kernel 范围与权威决定；
- `Unresolved`：当前没有足够合同。

### 证据状态

- `RepositoryEvidenceOnly`：只能证明仓库文本存在；
- `OperationalEvidenceRequired`：需要当前产品、服务或组织运行证据；
- `PreparedNotExecuted`：操作前材料已准备，角色、环境和真实执行未激活；
- `NoCurrentConformanceClaim`：不得作出当前符合性声明。

## 2. 映射表

| 承诺/章节 | 当前合同或来源 | 合同状态 | 证据状态 | 主要缺口 | 下一去向 |
|---|---|---|---|---|---|
| MC01 | ADR-0001; RFC-0001; RFC-0002; RFC-0003 | `PartiallyCovered` | `OperationalEvidenceRequired` | 跨角色权力、利益冲突与保护义务仍缺统一决策记录 | Round 06 Kernel/decision authority contract |
| MC02 | RFC-0001; RFC-0002; PROF-0003; RFC-0005 | `CoveredByProposedContracts` | `OperationalEvidenceRequired` | 产品语言、记录保管与人格/数据权利需要实际审计 | Public claims and data-rights evidence |
| MC03 | RFC-0001; RFC-0002; PROF-0001; PROF-0002; PROF-0003 | `CoveredByProposedContracts` | `OperationalEvidenceRequired` | 退出、撤回与残留数据控制尚未证明可用 | Rights lifecycle implementation evidence |
| MC04 | RFC-0002; PROF-0003; RFC-0001 | `CoveredByProposedContracts` | `OperationalEvidenceRequired` | 备份、派生资产、共享副本与审计记录完成证据缺失 | Retention/deletion implementation |
| MC05 | ADR-0002; RFC-0001; RFC-0004; GOV-0012 | `PartiallyCovered` | `RepositoryEvidenceOnly` | 组织级反例与未知存储、透明度和隐私平衡未形成完整合同 | Evidence/counterexample/unknown repository contract |
| MC06 | ADR-0002; RFC-0001; RFC-0004 | `CoveredByProposedContracts` | `OperationalEvidenceRequired` | 前端标签、存储对象和派生决定的一致性未验证 | Knowledge-status implementation |
| MC07 | RFC-0005; GOV-0008; GOV-0012 | `PartiallyCovered` | `OperationalEvidenceRequired` | 销售话术、转化漏斗、紧迫感与羞耻缺少独立审计合同 | Commercial restraint and claim audit profile |
| MC08 | RFC-0005; MF-0005 | `Unresolved` | `NoCurrentConformanceClaim` | 依赖、连续支持、合理辅助、健康退出与留存指标缺少合同 | Dependency and healthy-exit contract |
| MC09 | ADR-0001; RFC-0001; RFC-0003; RFC-0005 | `PartiallyCovered` | `OperationalEvidenceRequired` | 高影响决定、人类负责、受影响者参与和 AI 能力声明仍分散 | Round 06 Kernel AI/human/affected-person role decision |
| MC10 | RFC-0001; RFC-0002; RFC-0004; PROF-0001; PROF-0002 | `CoveredByProposedContracts` | `OperationalEvidenceRequired` | 儿童与第三方真实参与、无障碍和司法辖区证据未执行 | Affected-person and domain review |
| MC11 | RFC-0003; PROF-0004; RFC-0005; GOV-0011 | `CoveredByProposedContracts` | `OperationalEvidenceRequired` | 服务状态、资源新鲜度、失败升级与实际接收证据缺失 | Service profile operational activation |
| MC12 | ADR-0005; RFC-0005; GOV-0015 | `PartiallyCovered` | `NoCurrentConformanceClaim` | 独立商业冲突裁决主体、权限、披露、制裁与恢复未运营 | Commercial conflict governance contract |
| MC13 | RFC-0001; RFC-0002; RFC-0003; GOV-0015; ADR-0010; ADR-0017 | `PartiallyCovered` | `OperationalEvidenceRequired` | 纠正、申诉、事件、版本、替代与审计未形成统一证明 | Kernel correction/audit contract |
| MC14 | GOV-0015; RFC-0003; GOV-0018 | `GovernanceProcedureProposed` | `PreparedNotExecuted` | 报告渠道、独立调查、申诉、制裁、名称撤回与恢复未运营 | Operational activation and tabletop exercise |
| S04 | MC05; MC07; MC09; RFC-0005 | `PartiallyCovered` | `NoCurrentConformanceClaim` | 三项纪律尚未形成独立测试、发布门与失败处置 | Round 09 conformance suite |
| S05 | MF-0004; RFC-0003; PROF-0001 | `PartiallyCovered` | `NoCurrentConformanceClaim` | 优先次序与司法义务、冲突权利和商业可持续性缺少决策合同 | Round 06 authority and conflict decision |
| S06 | GOV-0005; GOV-0006; GOV-0016; GOV-0017 | `ReviewMaterialOnly` | `PreparedNotExecuted` | 十二问尚未转化为有证据、可失败、可申诉的测试 | Round 09 conformance suite |
| S07 | ADR-0005; GOV-0082; REF-0014 | `FutureKernelDecision` | `NoCurrentConformanceClaim` | Kernel 范围、文档家族、权威、可替换边界和符合性未决定 | Round 06 |
| S08 | GOV-0006; GOV-0016; GOV-0017; GOV-0018; GOV-0067; GOV-0068; GOV-0069 | `ReviewMaterialPrepared` | `PreparedNotExecuted` | 角色、参与者、受限环境与真实证据未激活 | Operational authorization |

## 3. 关键结论

1. 文本存在不等于合同 Accepted。
2. Proposed 合同存在不等于实现符合。
3. 仓库验证通过不等于运营验证通过。
4. MC08 是最明显合同缺口。
5. MC12/MC14 缺少实际独立治理权威与运营渠道。
6. S04–S06 必须进入未来符合性与决策合同，不能从机器映射中遗漏。
7. S07 必须等待 Round 06，不能反向声明 Kernel 已完成。
8. 正式受影响者与领域审查仍为 `PreparedNotExecuted`。
