# GETTING-STARTED.md - 快速启动指南

5分钟快速理解和应用 vibcoding 通用规范库。

---

## ⚡ 新对话框快速切换

**如果你在新对话框中继续接手项目：**

👉 **直接查看项目的 `docs/HANDOVER.md`**

在那里你能找到：
- 📌 项目状态快照（进度、目标）
- 🔄 进行中的工作（详细状态和卡点）
- ✅ 已完成的工作（总结）
- ⚠️ 待处理和冲突项（**需要立即解决的问题**）
- 🚀 下一步工作计划（优先级排序）
- 🔗 重要链接和命令

**然后你就能快速恢复工作，无需重新理解上下文。**

---

## 🎯 核心概念（1分钟理解）

**vibcoding 规范库由 3 层组成：**

### 层1：通用规范（所有项目共用）
```
vibcoding-rules/specs/
├── PRINCIPLES.md       ← 四大编码原则 + 4条规则
├── WORKFLOW.md         ← 简单改动/常规改动/复杂改造工作流 + AI自主性范围
└── GITHUB-RESEARCH.md  ← GitHub方案查证指南
```

### 层2：项目模板（新项目复制）
```
vibcoding-rules/templates/
├── AGENTS.md           ← 项目AGENTS.md的模板（只填三部分）
└── docs/
    └── HANDOVER.md     ← 交接文档的模板
```

### 层3：项目规范（每个项目必有）
```
your-project/
├── AGENTS.md           ← 复制模板后编辑三部分
└── docs/
    ├── HANDOVER.md     ← 交接文档
    ├── requirements.md ← 需求清单
    ├── decisions.md    ← 决策记录
    ├── progress.md     ← 进度跟踪
    └── memory.md       ← 知识沉淀
```

---

## 🚀 快速启动（4分钟）

### 步骤1：复制规范库到你的项目
```bash
# 复制通用规范
cp -r /path/to/vibcoding-rules/specs your-project/

# 复制项目模板
cp -r /path/to/vibcoding-rules/templates/* your-project/
```

### 步骤2：复制并配置项目级 AGENTS.md
```bash
# 模板已复制为 AGENTS.md，编辑三部分：
```

**编辑内容 1：Dev Profile（你的项目的命令）**
```markdown
- quick-test: npm test -- --testPathPattern="{target}"
- merge-gate: npm run build && npm test && npm run lint
- high-risk: src/auth/**, src/payment/**, src/database/migrations/**
- do-not-edit: vendor/, src/generated/**, dist/, node_modules/
```

**编辑内容 2：项目目录设计（你的项目结构）**
```markdown
改成你的实际目录结构
```

**编辑内容 3：团队角色（你的团队分工）**
```markdown
改成你团队的实际分工
```

### 步骤3：创建项目规范文档
```bash
# docs 文件夹已创建，补充其他文件
touch docs/requirements.md
touch docs/decisions.md
touch docs/progress.md
touch docs/memory.md
```

### 步骤4：告诉 AI
```text
我已按照 vibcoding 规范库初始化了项目。
现在请按照规范工作：
1. 遵循 specs/PRINCIPLES.md 中的四大原则
2. 按 specs/WORKFLOW.md 中的工作流工作
3. 重要决策查证 specs/GITHUB-RESEARCH.md
4. 完成后更新 docs/progress.md 和 docs/HANDOVER.md
```

---

## 📚 核心概念解释

### 什么是四大原则？

1. **Think Before Coding** - 不假设，不隐瞒困惑
2. **Simplicity First** - 最小代码，拒绝过度工程（包括4条深化规则）
3. **Surgical Changes** - 只改必需，只清理自己的烂摊子
4. **Goal-Driven Execution** - 定义标准，验证循环

**详细说明：** 见 `specs/PRINCIPLES.md`

### 什么是 L1/L2/L3？

三个级别的工作流，根据改动复杂度选择：

| 级别 | 适用场景 | AI行为 |
|------|---------|--------|
| **L1** | <50行，原因明确 | 完全自主执行，完成后说明 |
| **L2** | 常规功能，需要方案 | 方案确认后自主执行到底 |
| **L3** | 复杂改造，高风险 | 关键决策等待确认，分阶段执行 |

**详细说明：** 见 `specs/WORKFLOW.md`

### 什么时候查证 GitHub？

技术决策时必查。例如：
- 选择框架或库
- 选择架构方案
- 核心模块设计

**详细说明：** 见 `specs/GITHUB-RESEARCH.md`

### 什么是交接文档？

当上下文太多需要切换对话框时，用来快速恢复的文档。包含：
- 项目状态快照
- 进行中的工作
- 已��成的工作
- ⚠️ 待处理和冲突项
- 下一步计划

**使用方式：** 新对话框中直接查看 `docs/HANDOVER.md`

---

## ✅ 检查清单

初始化完成后，检查：

- [ ] 复制了 specs/ 和 templates/ 到项目
- [ ] AGENTS.md 已配置（三部分都填了）
- [ ] docs/ 文件夹已创建（至少5个文件）
- [ ] 阅读了 specs/PRINCIPLES.md 中的四大原则
- [ ] 理解了 specs/WORKFLOW.md 中的 L1/L2/L3
- [ ] 知道什么时候查证 GitHub（见 specs/GITHUB-RESEARCH.md）

---

## 🎯 下一步

### 对于新人/新项目

1. 从上往下读：specs/PRINCIPLES.md → specs/WORKFLOW.md → specs/GITHUB-RESEARCH.md
2. 理解四大原则和工作流
3. 在每个任务中应用这些原则

### 对于现有项目迁移

1. 复制 specs/ 和 templates/ 到项目
2. 配置项目级 AGENTS.md
3. 把现有的文档迁移到 docs/ 文件夹
4. 在 docs/decisions.md 中补充历史决策
5. 从今天开始按新规范工作

### 对于多项目管理

1. 保持一份 vibcoding-rules（中央规范库）
2. 每个项目复制 specs/ 和使用 templates/
3. 每个项目有自己的 AGENTS.md 和 docs/
4. 定期回顾和更新中央规范库

---

## ❓ 常见问题

**Q: 四大原则和我原来的编码风格冲突怎么办？**
A: vibcoding 规范会逐步演进。如果有冲突，优先遵循 vibcoding，可以在 docs/decisions.md 中记录为什么这样做。

**Q: 我的项目语言不是 JavaScript/TypeScript，能用这个规范吗？**
A: 完全可以！vibcoding 是通用规范，不限于特定语言。只需要在 AGENTS.md 的 Dev Profile 中填入你的语言对应的命令即可。

**Q: 如何处理现有项目的遗留代码？**
A: 新改动遵循 Surgical Changes 原则，不要重构遗留代码。在 docs/decisions.md 中记录为什么这样做。后期可以专项处理遗留代码重构。

**Q: 什么时候需要更新 specs/ 中的规范？**
A: 季度或半年审查一次。如果发现多个项目都重复遇到某个问题，可能需要在中央规范库中补充指引。

---

## 更新日志

**2026-11-22** - 初始版本
- 核心概念解释
- 4 步快速启动
- 检查清单
- 常见问题

---

## 🏁 现在开始

1. 按上面的"快速启动"4步初始化你的项目
2. 告诉 AI 开始工作
3. 在项目中应用规范，逐步习惯新的流程

**就这样，你有了一套完整的 AI 开发规范体系！** 🎉
