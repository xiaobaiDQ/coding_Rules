# AGENTS.md - vibcoding 通用开发规范库

融合 Andrej Karpathy 编码原则 + oil-dev-skills 工作流 + GitHub 方案查证的**通用 AI 开发规范体系**。

这是导航中心。具体内容见下面的链接。

---

## 📋 快速导航

👉 **不知道从哪里开始？看 [FRAMEWORK-HIERARCHY.md](./FRAMEWORK-HIERARCHY.md)** ⭐

**按你的情况选择：**

| 我要... | 看这个 | 时间 |
|--------|--------|------|
| 快速上手项目 | [FRAMEWORK-HIERARCHY.md 场景1](./FRAMEWORK-HIERARCHY.md#场景-1新ai接手项目15分钟) | 15分钟 |
| 理解整个规范 | [FRAMEWORK-HIERARCHY.md 场景2](./FRAMEWORK-HIERARCHY.md#场景-2新人想理解规范1小时) | 1小时 |
| 启动新项目 | [FRAMEWORK-HIERARCHY.md 场景3](./FRAMEWORK-HIERARCHY.md#场景-3项目初始化2小时) | 2小时 |
| 项目需要扩展 | [FRAMEWORK-HIERARCHY.md 场景4](./FRAMEWORK-HIERARCHY.md#场景-4项目需要扩展1-3小时) | 1-3小时 |

---

## 📚 分层文档导航

### 【L0】最小启动

| 文档 | 用途 |
|------|------|
| [FRAMEWORK-HIERARCHY.md](./FRAMEWORK-HIERARCHY.md) ⭐ | **分层结构总入口，从这里开始** |
| [GETTING-STARTED.md](./GETTING-STARTED.md) | 快速启动指南 |

### 【L1】核心规范

| 文档 | 用途 |
|------|------|
| [specs/PRINCIPLES.md](./specs/PRINCIPLES.md) | Karpathy四原则 + 4条深化规则 |
| [specs/WORKFLOW.md](./specs/WORKFLOW.md) | 简单改动/常规改动/复杂改造工作流 |

### 【L2】应用框架

| 文档 | 用途 |
|------|------|
| [specs/GITHUB-RESEARCH.md](./specs/GITHUB-RESEARCH.md) | 技术方案查证指南 |
| [skills/OIL-DEV-SKILLS-CHECKLIST.md](./skills/OIL-DEV-SKILLS-CHECKLIST.md) | 通用Skill清单（即插即用配置） |
| [project-adapt/PROJECT-ADAPT-STRATEGY.md](./project-adapt/PROJECT-ADAPT-STRATEGY.md) | 项目适配流程 |
| [project-adapt/AI-EXECUTION-GUIDE.md](./project-adapt/AI-EXECUTION-GUIDE.md) | AI执行决策树 |

### 【L3】扩展深化

| 文档 | 用途 |
|------|------|
| [skills/OIL-DEV-SKILLS-EXTENSION.md](./skills/OIL-DEV-SKILLS-EXTENSION.md) | 在通用Skill基础上扩展 |
| [skills/PROJECT-CUSTOM-SKILLS-STRATEGY.md](./skills/PROJECT-CUSTOM-SKILLS-STRATEGY.md) | 创建项目专有Skill |
| [project-adapt/DOCS-EXTRACTION-GUIDE.md](./project-adapt/DOCS-EXTRACTION-GUIDE.md) | 老项目迁移 |

### 【参考资源】

| 文档 | 用途 |
|------|------|
| [skills/SKILLS-GUIDE.md](./skills/SKILLS-GUIDE.md) | Skill管理总入口 |
| [skills/SKILLS-INTEGRATION.md](./skills/SKILLS-INTEGRATION.md) | Skill体系总览 |

### 【L4】项目专有配置

```
你的项目/
├─ AGENTS.md                  ← 项目级配置
├─ PROJECT-ADAPT.yaml         ← Skill和规范配置
└─ docs/
   ├─ HANDOVER.md            ← 交接文档
   ├─ DECISIONS.md           ← 决策记录
   └─ PROGRESS.md            ← 进度记录
```

---

## 🎯 核心四大原则（通用）

详见：[specs/PRINCIPLES.md](./specs/PRINCIPLES.md)

- **原则 1：Think Before Coding** - 不假设，不隐瞒困惑，表面化权衡
- **原则 2：Simplicity First** - 最小代码，拒绝过度工程（包括 4 条深化规则）
- **原则 3：Surgical Changes** - 只改必需，只清理自己的烂摊子
- **原则 4：Goal-Driven Execution** - 定义标准，验证循环

**新增强制规则（在 Simplicity First 中）：**
- 低概率防御先确认，禁止私自膨胀代码
- 入口单次校验，内部靠类型系统流转
- 拒绝提前抽象，单次逻辑就近内联
- 控制复杂度，优先极简实现

---

## 🔍 GitHub 方案查证体系（通用）

详见：[specs/GITHUB-RESEARCH.md](./specs/GITHUB-RESEARCH.md)

**触发条件**：涉及技术选型、架构设计、系统方案时

**工作流**：
1. 确定搜索关键词
2. 筛选高质量项目（stars、维护度、文档、测试）
3. 对比分析（至少 2-3 个项目）
4. 记录决策（在项目的 `docs/decisions.md`）
5. 标记参考来源

---

## 🛠️ 开发工作流（通用）

详见：[specs/WORKFLOW.md](./specs/WORKFLOW.md)

三个级别的流程，每个级别都调用不同的 skills：

- **简单改动** - <50行，原因明确，快速直达 → 调用 `skill-explore` → AI 完全自主
- **常规改动** - 50-500行，需要方案 → 调用 `oil-explore` → `oil-plan` → 👤确认 → `oil-delegate` → `oil-code-review` → `oil-govern`
- **复杂改造** - >500行，高风险，需分阶段 → 深度 `oil-explore` + 完整 `oil-plan` → 👤确认 → 分阶段 `oil-delegate` → 多轮 `oil-code-review` → `oil-bug-fix` → `oil-govern`

---

## 📚 Skill 管理体系（新增）

**总入口：** 👉 **[SKILLS-GUIDE.md](./SKILLS-GUIDE.md)** ⭐

### 【第 1 层】通用 Skill 库

详见：[SKILLS-INTEGRATION.md](./SKILLS-INTEGRATION.md)

我们不维护 Skill，而是用成熟的 **oil-dev-skills**（油油团队维护）：

```
oil-explore    ← 理解项目和代码
oil-plan       ← 制定方案和设计
oil-delegate   ← 派发任务和分配
oil-code-review ← 代码审查
oil-bug-fix    ← Bug 修复和根因分析
oil-govern     ← 项目治理
```

### 【第 2 层】扩展 Skill

详见：[OIL-DEV-SKILLS-EXTENSION.md](./vibcoding-skills/OIL-DEV-SKILLS-EXTENSION.md)

如果需要在通用 Skill 基础上增加功能（例如 SQL 审查、性能测试），可以通过"补充"关系扩展。

### 【第 3 层】项目专有 Skill

详见：[vibcoding-skills/PROJECT-CUSTOM-SKILLS-STRATEGY.md](./vibcoding-skills/PROJECT-CUSTOM-SKILLS-STRATEGY.md)

如果项目有特殊需求，可以创建项目级 Skill，但需要满足：
- ✅ 能力强、功能丰富、内聚性高（不拆）
- ❌ 或者能力太分散时必须拆分
- 在 PROJECT-ADAPT.yaml 中配置关系（supplement/replace/independent）

---

## 🔄 项目适配层

详见：[PROJECT-ADAPT-STRATEGY.md](./PROJECT-ADAPT-STRATEGY.md)

新项目或老项目迁移时：
1. 扫描项目现状（技术栈、工作流、规范）
2. 对比通用规范识别冲突
3. 生成冲突报告供用户决策
4. 执行决策生成 PROJECT-ADAPT.yaml

---

## 🤖 AI 执行

详见：[AI-EXECUTION-GUIDE.md](./AI-EXECUTION-GUIDE.md)

AI 在实际工作中的自动决策流程：
1. 识别工作流级别（L1/L2/L3）
2. 加载项目适配配置
3. 合并规范（通用 + 项目）
4. 选择合适的 Skill
5. 执行工作流
6. 记录决策
- **L2：常规功能** - 需要方案 + GitHub 查证 → 调用 `skill-explore` → `skill-plan` → `skill-delegate` → `skill-code-review` → `skill-govern`
- **L3：复杂改造** - 完整设计 + 深度 GitHub 调研 → 调用所有 6 个 skills → 关键决策等待确认

**Skills 映射详见：** [vibcoding-skills/integrations/WORKFLOW-MAPPING.md](./vibcoding-skills/integrations/WORKFLOW-MAPPING.md)

**工作流概览：**
```
需求提出
  ↓
【核心】涉及技术决策？→ GitHub 方案查证
  ↓
【判断复杂度】用决策树判断 L1/L2/L3
  ↓
【按工作流执行】
  ├─ L1 轻量改动 → AI 完全自主
  ├─ L2 常规功能 → 方案确认后自主
  └─ L3 复杂改造 → 关键决策等待确认
  ↓
【全程参考】PRINCIPLES.md 四大原则
  ↓
【完成】
  ├─ 更新项目的 docs/progress.md
  ├─ 记录决策到 docs/decisions.md（特别是GitHub参考）
  ├─ 更新 docs/HANDOVER.md
  └─ 下一个任务
```

---

## 🔄 工作流决策树

**我该遵循哪个级别的流程？**

```
是不是 typo 或单行改动？
├─ 是 → 简单改动（快速直达）
└─ 否 → 下一步

原因明确吗？改动<50行吗？
├─ 是 → 简单改动（快速直达）
└─ 否 → 下一步

需要方案吗？涉及技术决策吗？
├─ 是 → 常规改动（需要方案 + 可能需要GitHub查证）
└─ 否 → 简单改动（快速直达）

跨模块改造吗？高风险改动吗？架构变更吗？
├─ 是 → 复杂改造（完整设计 + 深度调研）
└─ 否 → 常规改动（需要方案 + GitHub查证）
```

---

## 📚 完整文档清单

### 通用规范（所有项目共用）
| 文档 | 位置 | 用途 | 更新频率 |
|------|------|------|---------|
| PRINCIPLES.md | specs/ | 编码准则详解 | 低（规范稳定） |
| WORKFLOW.md | specs/ | 工作流详解 | 低 |
| GITHUB-RESEARCH.md | specs/ | 方案查证指南 | 低 |

### 项目模板（新项目复制这些）
| 模板 | 位置 | 用途 |
|------|------|------|
| AGENTS.md | templates/ | 项目AGENTS.md的模板 |
| HANDOVER.md | templates/docs/ | 交接文档的模板 |

---

## 🎯 核心约束

### 禁止清单

| 类别 | 禁止内容 | 后果 |
|------|--------|------|
| **超出范围** | 改动超出派发契约的文件范围 | 被阻挡 |
| **没有验证** | 改动完不运行快测 | 无法合并 |
| **忽视方案** | 在确认方案前开始写代码 | 返工 |
| **不查证** | 技术方案不查GitHub直接设计 | 可能重复造轮子 |
| **代码膨胀** | 低概率防御私自添加，未经确认 | 代码复杂度过高 |
| **重复校验** | 层层重复判空、判格式、判范围 | 代码冗余 |
| **提前抽象** | 单次使用的逻辑就是不抽象 | 过度工程 |
| **不记录** | 完成后不更新进度和决策 | 团队信息不对称 |

### 必做检查清单

**开始任何改动前，问自己：**

- [ ] Think Before Coding
  - [ ] 我明确了所有假设吗？
  - [ ] 我问了所有不确定的地方吗？
  - [ ] 我列出了多种做法的权衡吗？
  - [ ] 【新】涉及技术方案时，我在 GitHub 查找了参考吗？

- [ ] Simplicity First
  - [ ] 这段代码做的事情超出需求吗？
  - [ ] 有多余的抽象吗？
  - [ ] 能用 50 行代替 200 行吗？
  - [ ] 【新】我为低概率事件添加防御了吗？是否经用户确认？
  - [ ] 【新】我有层层重复的校验代码吗？
  - [ ] 【新】我为单次使用的逻辑拆分了函数吗？
  - [ ] 【新】我用 try-catch 了吗？能简化吗？

- [ ] Surgical Changes
  - [ ] 我是否改动了相邻的无关代码？
  - [ ] 我是否匹配了现有的代码风格？
  - [ ] 每改一行都能追溯到需求吗？

- [ ] Goal-Driven Execution
  - [ ] 我明确定义了成功标准吗？
  - [ ] 我有验证计划吗？
  - [ ] 完成后我验证了吗？

---

## 🚀 AI 能力库（Skills）

**新增：** vibcoding-skills 能力库

每个 skill 都是一个完整的能力包（不仅是文档），包含：
- SKILL.md - 完整定义
- templates/ - 执行模板
- examples/ - 真实案例
- prompts/ - 预设 AI prompt
- validators/ - 质量验证
- utils/ - 辅助工具

**6 个核心 Skills：**
1. `skill-explore` - 理解项目和代码
2. `skill-plan` - 制定方案和架构
3. `skill-delegate` - 派发任务
4. `skill-code-review` - 代码审查
5. `skill-bug-fix` - Bug 修复
6. `skill-govern` - 项目治理

**快速开始：**
- 👉 看 [vibcoding-skills/README.md](./vibcoding-skills/README.md) - 能力库说明
- 👉 看 [SKILLS-INTEGRATION.md](./SKILLS-INTEGRATION.md) - 与规范库的集成
- 👉 看 [vibcoding-skills/SKILLS-INDEX.md](./vibcoding-skills/SKILLS-INDEX.md) - 所有 skill 总览
- 👉 看 [vibcoding-skills/integrations/WORKFLOW-MAPPING.md](./vibcoding-skills/integrations/WORKFLOW-MAPPING.md) - 工作流中的 skill 映射

**AI 驱动的 Skill 管理：**
```
你: "替换 skill-X 为..."
或: "改进 skill-Y: ..."

我: 自动处理所有细节，只在关键点等你决策

详见：[vibcoding-skills/SKILL-MANAGER.md](./vibcoding-skills/SKILL-MANAGER.md)
```

---

## ❓ 常见问题

**Q: 新人应该先看什么？**
A: 按顺序：GETTING-STARTED.md → specs/PRINCIPLES.md → specs/WORKFLOW.md

**Q: 什么时候查证GitHub方案？**
A: L2和L3涉及技术决策时必查。L1不需要。

**Q: 我能绕过某些步骤吗？**
A: 不能。四原则 + GitHub查证 + 工作流缺一不可。

**Q: 决策记录该怎么写？**
A: 看你的项目 docs/decisions.md。记录参考的GitHub项目、对比分析、选择理由。

**Q: 什么时候更新进度？**
A: 完成任何功能或Bug修复时立即更新你的项目 docs/progress.md。

---

## 🏗️ 目录结构

```
vibcoding-rules/（通用规范库）
├── README.md              ← 项目说明
├── AGENTS.md              ← 你在这里（导航中枢）
├── GETTING-STARTED.md     ← 快速启动
│
├── specs/                 ← 规范文档（所有项目共用）
│   ├── PRINCIPLES.md      ← 编码四原则
│   ├── WORKFLOW.md        ← 工作流
│   └── GITHUB-RESEARCH.md ← 方案查证
│
└── templates/             ← 项目模板（新项目复制这些）
    ├── AGENTS.md          ← 项目AGENTS.md的模板
    └── docs/
        └── HANDOVER.md    ← 交接文档的模板
```

---

## 更新日志

**2026-11-22** - v1.0 初始版本
- 拆分通用规范 (specs/) 和项目模板 (templates/)
- Karpathy 四原则 + 4 条深化规则
- oil-dev-skills 工作流集成
- GitHub 方案查证体系
- AI 自主性范围定义
- 交接文档功能

---

## 🚀 现在就开始

1. 📖 读 [GETTING-STARTED.md](./GETTING-STARTED.md)
2. 📋 读 [specs/PRINCIPLES.md](./specs/PRINCIPLES.md)
3. 🔄 读 [specs/WORKFLOW.md](./specs/WORKFLOW.md)
4. 🏗️ 复制 templates/ 和 specs/ 到你的项目
5. ⚙️ 配置项目级 AGENTS.md
6. 🚀 告诉 AI："开始按这个规范工作"

**现在你有了一套完整的 AI 开发规范体系！** 🎉
