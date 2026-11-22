# SKILLS-GUIDE.md - Skill 管理完整指南

**对象：** 项目管理者 + AI

**目的：** 统一的 Skill 管理体系入口 - 从通用 Skill 到项目专有 Skill 的完整流程

---

## 🎯 Skill 管理的全景图

```
【全局 Skill 体系】

通用 Skill 库（oil-dev-skills）
│  ├─ oil-explore       ← 理解项目和代码
│  ├─ oil-plan          ← 制定方案和设计
│  ├─ oil-delegate      ← 派发任务和分配
│  ├─ oil-code-review   ← 代码审查
│  ├─ oil-bug-fix       ← Bug 修复和根因分析
│  └─ oil-govern        ← 项目治理
│
├─【集成和扩展】
│  ├─ SKILLS-INTEGRATION.md              ← 和 oil-dev-skills 集成
│  ├─ OIL-DEV-SKILLS-EXTENSION.md       ← 如何扩展 oil-dev-skills
│  └─ PROJECT-ADAPT.yaml                 ← 项目级 Skill 配置
│
└─【项目专有 Skill 库】
   ├─ skill-sql-review         ← 项目 A 的 SQL 审查
   ├─ skill-performance-audit  ← 项目 A 的性能审计
   ├─ skill-security-scan      ← 项目 B 的安全扫描
   └─ ...（每个项目维护自己的 Skill）
```

---

## 📋 文档导航

### 【第 1 部分】理解 Skill 体系

```
新到这个系统？从这里开始：

1️⃣ SKILLS-GUIDE.md（你在这里）
   目的：Skill 管理体系总览和快速导航
   
2️⃣ OIL-DEV-SKILLS-CHECKLIST.md ⭐【新增】
   目的：通用 Skill 的完整清单和初始化机制
   内容：
   - 6 个通用 Skill 的详细说明
   - 每个 Skill 的能力、使用场景、配置方式
   - 项目初始化的 Skill 检查流程
   - Skill 配置模板和最佳实践
   
   何时读：项目初始化时，必读
   ⏱️ 阅读时间：10 分钟

3️⃣ SKILLS-INTEGRATION.md
   目的：理解通用 Skill 库（oil-dev-skills）是什么
   内容：
   - 整体架构图
   - 6 个通用 Skill 的介绍
   - 和我们规范体系的关系
   - 什么时候用哪个 Skill
   
   ⏱️ 阅读时间：5 分钟
```

### 【第 2 部分】扩展通用 Skill

```
如果你需要在通用 Skill 的基础上增加功能：

4️⃣ OIL-DEV-SKILLS-EXTENSION.md
   目的：学会如何安全地扩展 oil-dev-skills
   内容：
   - 何时需要扩展
   - 何时不应该扩展
   - 补充关系 vs 替代关系
   - 在 PROJECT-ADAPT.yaml 中配置
   - 扩展 Skill 的完整示例
   
   ⏱️ 阅读时间：10 分钟
   
   何时读：当你想在 oil-code-review 后加个"SQL 审查"时
```

### 【第 3 部分】创建项目专有 Skill

```
如果你需要创建项目自己的 Skill：

5️⃣ PROJECT-CUSTOM-SKILLS-STRATEGY.md
   目的：完整的项目 Skill 管理系统
   内容：
   - Skill 能力评估模型（判断要不要���分）
   - 拆分判断清单（啥时候拆、啥时候不拆）
   - 项目 Skill 仓库结构（怎么组织）
   - 完整生命周期管理（从设计到删除）
   - 多个 Skill 的协调规则
   - PROJECT-ADAPT.yaml 的完整配置语法
   - 创建检查清单
   
   ⏱️ 阅读时间：15 分钟
   
   何时读：当你计划创建项目级 Skill 时，必读
```

### 【第 4 部分】AI 执行指南

```
AI 在实际工作中如何选择和使用 Skill：

6️⃣ AI-EXECUTION-GUIDE.md
   目的：AI 的自动决策流程
   内容：
   - 识别工作流级别（L1/L2/L3）
   - 加载项目适配配置
   - 验证 Skill 配置 ⭐【新增步骤】
   - 合并规范（通用 + 项目）
   - 选择合适的 Skill
   - 执行工作流
   - 记录决策
   
   ⏱️ 阅读时间：10 分钟（开发者参考）
```

---

## 🔄 常见场景的快速导引

### 场景 1：新项目，想快速开始

```
步骤：
1. 读 OIL-DEV-SKILLS-CHECKLIST.md（10 分钟）⭐【优先】
   → 了解有哪些通用 Skill 和必需性
   → 选择配置模板（最小/标准/完整）
   
2. 在 PROJECT-ADAPT.yaml 中配置
   → 按照 OIL-DEV-SKILLS-CHECKLIST.md 中的模板
   → 粘贴对应配置
   
3. 读 SKILLS-INTEGRATION.md（5 分钟）
   → 了解每个 Skill 的具体能力
   
4. 创建项目级 AGENTS.md
   → 配置 Dev Profile
   
5. 告诉 AI 开始工作
   → AI 会自动验证 Skill 配置
   → 如果有缺失，会提醒并等待确认

相关文档：
- OIL-DEV-SKILLS-CHECKLIST.md   ⭐【必读】
- SKILLS-INTEGRATION.md
- templates/AGENTS.md
```

### 场景 2：项目需要自定义 Skill

```
步骤：
1. 评估是否真的需要自定义
   → 读 PROJECT-CUSTOM-SKILLS-STRATEGY.md 的前半部分
   → 运行"能力评估模型"
   → 对比 OIL-DEV-SKILLS-CHECKLIST.md 中的通用 Skill
   → 确认通用 Skill 真的不够
   
2. 如果确实需要，设计项目 Skill
   → 读 PROJECT-CUSTOM-SKILLS-STRATEGY.md 的设计部分
   → 创建 skill_name/SKILL.md
   
3. 配置到项目中
   → 更新 PROJECT-ADAPT.yaml
   → 记录到 PROJECT-CUSTOM-SKILLS-INVENTORY.md
   
4. 验证和迭代
   → 在实际工作流中测试
   → 收集反馈，改进

相关文档：
- OIL-DEV-SKILLS-CHECKLIST.md（确认通用 Skill 不够）
- PROJECT-CUSTOM-SKILLS-STRATEGY.md（完整指南）
- OIL-DEV-SKILLS-EXTENSION.md（扩展方式）
```

### 场景 3：老旧项目迁移到 vibcoding

```
步骤：
1. 扫描项目现有文档
   → 读 DOCS-EXTRACTION-GUIDE.md
   → 运行"信息提取"流程
   
2. 参考 OIL-DEV-SKILLS-CHECKLIST.md 选择 Skill
   → 确定项目的工作流级别（L1/L2/L3）
   → 决定要用哪些通用 Skill
   → 决定要不要创建项目 Skill
   
3. 识别冲突和适配
   → 读 PROJECT-ADAPT-STRATEGY.md
   → 生成冲突报告
   
4. 生成项目配置
   → PROJECT-ADAPT.yaml（包括 Skill 配置）
   → RULES-OVERRIDE.md
   → TECH-STACK.md

相关文档：
- OIL-DEV-SKILLS-CHECKLIST.md   ⭐【必读】
- DOCS-EXTRACTION-GUIDE.md（信息提取）
- PROJECT-ADAPT-STRATEGY.md（冲突映射）
- PROJECT-CUSTOM-SKILLS-STRATEGY.md（Skill 决策）
```

### 场景 4：Skill 和 Skill 之间有冲突

```
识别问题：
- 两个 Skill 功能重叠？
- 一个 Skill 依赖另一个？
- 顺序执行还是并行执行？

解决方案：
1. 读 PROJECT-CUSTOM-SKILLS-STRATEGY.md
   → "多个项目 Skill 的协调规则"部分
   
2. 在 PROJECT-ADAPT.yaml 中定义关系
   - supplement_to（补充）
   - replace（替代）
   - independent（独立）
   - merge_strategy（合并方式）
   
3. 记录决策
   → docs/DECISIONS.md

相关文档：
- PROJECT-CUSTOM-SKILLS-STRATEGY.md（协调规则）
- PROJECT-ADAPT.yaml（配置语法）
```

---

## ✅ Skill 管理的三个阶段

### 阶段 1：学习（新人必读）

```
时间投入：30 分钟

必读文档：
1. OIL-DEV-SKILLS-CHECKLIST.md   (10 分钟) ⭐【从这里开始】
2. SKILLS-INTEGRATION.md         (5 分钟)
3. OIL-DEV-SKILLS-EXTENSION.md  (10 分钟)
4. PROJECT-CUSTOM-SKILLS-STRATEGY.md (5 分钟 - 了解概念即可)

输出：
- 理解有哪 6 个通用 Skill
- 知道每个 Skill 的能力和必需性
- 知道啥时候扩展、啥时候创建项目 Skill
```

### 阶段 2：规划（项目启动时）

```
时间投入：1-2 小时

工作流：
1. 确定项目的工作流级别（L1/L2/L3）
   
2. 参考 OIL-DEV-SKILLS-CHECKLIST.md 选择配置
   - 最小配置（L1 只做小改）
   - 标准配置（L2 常规开发）
   - 完整配置（L3 复杂改造）
   
3. 决策是否需要项目 Skill
   → 读 PROJECT-CUSTOM-SKILLS-STRATEGY.md
   → 评估是否可以用通用 Skill

4. 生成 PROJECT-ADAPT.yaml
   → 复制对应配置模板
   → 调整 Skill 参数
   
5. 告诉 AI 开始工作
   → AI 会运行 Skill 验证检查
   → 如果配置有问题，会提醒并等待确认

相关文档：
- OIL-DEV-SKILLS-CHECKLIST.md（配置选择）⭐
- PROJECT-ADAPT-STRATEGY.md（详细适配流程）
- PROJECT-CUSTOM-SKILLS-STRATEGY.md（Skill 决策）
```

### 阶段 3：维护（日常工作）

```
时间投入：持续

工作流：
1. 每次工作前
   - AI 加载 PROJECT-ADAPT.yaml
   - AI 运行 Skill 验证检查 ⭐【新增】
   - AI 识别工作流级别
   - AI 选择合适的 Skill

2. 每月一次评审
   - Skill 还有用吗？
   - 有没有冲突或问题？
   - 有没有需要优化的？

3. 定期清理
   - 删除不用的 Skill
   - 整理和文档化
   - 更新 PROJECT-CUSTOM-SKILLS-INVENTORY.md

相关文档：
- AI-EXECUTION-GUIDE.md（AI 决策流程）
- OIL-DEV-SKILLS-CHECKLIST.md（Skill 参考）
- PROJECT-CUSTOM-SKILLS-STRATEGY.md（生命周期）
```

---

## 🏗️ Skill 相关的完整文档清单

```
【第 0 层】入口和总览
├─ README.md                              ← 规范库总入口
├─ GETTING-STARTED.md                    ← 快速启动指南
├─ AGENTS.md                             ← 主导航中心（包含 Skill 章节）

【第 1 层】通用 Skill 和集成
├─ skills/SKILLS-GUIDE.md                ← Skill 管理总入口（你在这里）
├─ skills/OIL-DEV-SKILLS-CHECKLIST.md   ← 通用 Skill 清单和初始化机制 ⭐【新增】
├─ skills/SKILLS-INTEGRATION.md          ← Skill 体系总览
├─ skills/OIL-DEV-SKILLS-EXTENSION.md   ← 扩展通用 Skill
│
【第 2 层】项目专有 Skill 管理
├─ skills/PROJECT-CUSTOM-SKILLS-STRATEGY.md ← 项目 Skill 完整系统
│
【第 3 层】项目适配和决策
├─ project-adapt/PROJECT-ADAPT-STRATEGY.md         ← 项目适配流程
├─ project-adapt/AI-EXECUTION-GUIDE.md            ← AI 执行决策树（含 Skill 验证）
├─ project-adapt/DOCS-EXTRACTION-GUIDE.md         ← 从现有文档提取信息
├─ project-adapt/PROJECT-INIT-CHECKLIST.md        ← 项目初始化检查清单
│
【第 4 层】核心规范
├─ specs/PRINCIPLES.md                   ← 四大编码原则
├─ specs/WORKFLOW.md                     ← L1/L2/L3 工作流
├─ specs/GITHUB-RESEARCH.md              ← 技术方案查证
│
【第 5 层】项目模板
└─ templates/
   ├─ AGENTS.md                          ← 项目配置模板
   ├─ PROJECT-INIT-CHECKLIST.md          ← 项目初始化检查清单
   └─ docs/HANDOVER.md                   ← 交接文档模板

【项目文件结构】
└─ your-project/
   ├─ skills/                            ← 项目 Skill 仓库（如果有）
   │  ├─ skill_name/SKILL.md
   │  └─ ...
   ├─ PROJECT-ADAPT.yaml                 ← Skill 和规范配置 ⭐【关键】
   ├─ AGENTS.md                          ← 项目配置
   └─ docs/
      ├─ DECISIONS.md                    ← 决策记录
      ├─ PROJECT-CUSTOM-SKILLS-INVENTORY.md
      └─ SKILL-LIFECYCLE.md              ← Skill 生命周期
```

---

## 💡 最佳实践

```
✅ DO

1. 优先用通用 Skill
   - oil-dev-skills 经过验证
   - 社区维护，会获得更新
   - 应用广泛，文档完整

2. 如果必须扩展，用"补充关系"
   - 不要替代，要补充
   - 两个都会运行
   - 结果自动合并

3. 定期审视项目 Skill
   - 每月检查一次
   - 是否还有必要
   - 有没有可以删除的

4. 保持文档同步
   - 创建 Skill 时更新文档
   - 修改 Skill 时更新文档
   - 删除 Skill 时标记为废弃


❌ DON'T

1. 不要轻易创建项目 Skill
   - 维护成本高
   - 会和通用 Skill 重叠

2. 不要过度设计
   - 不要创建"未来可能用到的" Skill
   - 不要太早拆分

3. 不要忽视版本管理
   - 要清楚每个 Skill 的版本
   - 要记录变更历史

4. 不要留下孤立的 Skill
   - 删除前要有迁移期
   - 要更新所有文档
```

---

## 🎯 下一步

1. **新项目？** 👉 [SKILLS-INTEGRATION.md](./SKILLS-INTEGRATION.md)（5 分钟入门）

2. **想创建项目 Skill？** 👉 [PROJECT-CUSTOM-SKILLS-STRATEGY.md](./PROJECT-CUSTOM-SKILLS-STRATEGY.md)（完整指南）

3. **需要扩展通用 Skill？** 👉 [OIL-DEV-SKILLS-EXTENSION.md](./vibcoding-skills/OIL-DEV-SKILLS-EXTENSION.md)（扩展方式）

4. **老项目迁移？** 👉 [DOCS-EXTRACTION-GUIDE.md](./DOCS-EXTRACTION-GUIDE.md)（信息提取）

5. **想了解 AI 如何执行？** 👉 [AI-EXECUTION-GUIDE.md](./AI-EXECUTION-GUIDE.md)（执行决策树）

---

**现在你拥有了完整的 Skill 管理体系！** 🎉
