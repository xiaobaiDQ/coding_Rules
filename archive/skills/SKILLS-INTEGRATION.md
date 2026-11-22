# SKILLS-INTEGRATION.md - 与 oil-dev-skills 库的集成

说明如何在规范库中集成和使用成熟的 oil-dev-skills 能力库。

---

## 🔗 整体架构

```
vibcoding-rules/（规范库）← 我们维护
├── specs/              ← 编码原则、工作流、GitHub查证
├── templates/          ← 项目模板
├── AGENTS.md           ← 导航中枢
└── SKILLS-INTEGRATION.md ← 你在这里

    ↓ 指向

oil-dev-skills/（成熟的能力库）← 油油团队维护
├── skills/
│   ├── oil-explore       ← 理解项目和代码
│   ├── oil-plan          ← 制定方案和设计
│   ├── oil-delegate      ← 派发任务和分配
│   ├── oil-code-review   ← 代码审查
│   ├── oil-bug-fix       ← Bug 修复
│   └── oil-govern        ← 项目治理
├── scripts/              ← 生产级脚本和工具
├── evals/                ← 完整的评测套件
└── README.md
```

---

## 🎯 核心理念

**vibcoding-rules** 定义"是什么"和"为什么"：
- 编码原则
- 工作流框架（简单 / 常规 / 复杂）
- 决策流程

**oil-dev-skills** 定义"怎么做"：
- 6 个成熟、生产级的 skill
- 完整的执行脚本和工具
- 真实项目的验证

**配合使用：**
```
vibcoding-rules 说：常规改动需要调用 explore → plan → ...
oil-dev-skills 说：这是 oil-explore / oil-plan / ... 的完整实现
```

---

## 📊 Skill 在工作流中的位置

### 简单改动工作流

```
需求 → 【oil-explore】→ 实现 → 完成

涉及 skill：
- oil-explore (快速模式，只读理解)

验证清单：
✅ 已配置 oil-explore：是否启用？
✅ 确认项目只做简单改动���是否永远不会做常规+？
```

### 常规改动工作流

```
需求 
  → 【验证Skill配置】⭐
  → 【oil-explore】(代码理解)
  → 【GitHub 查证】(可选)
  → 【oil-plan】
  → 【用户确认】👤
  → 【oil-delegate】(本地 CLI agents)
  → 实现
  → 【oil-code-review】(diff 审查)
  → 【oil-govern】(文档和治理)
  → 完成

涉及 skill：
- oil-explore - 理解项目结构和相关代码
- oil-plan - 编写可读的方案文档
- oil-delegate - 分派给本地 CLI agent（Codex/Claude Code 等）
- oil-code-review - 审查代码改动，对比计划
- oil-govern - 记录决策，管理分支

验证清单：
✅ 已配置 oil-explore：是？
✅ 已配置 oil-plan：是？（L2必需）
✅ 已配置 oil-code-review：是？（强烈推荐）
✅ 已配置 oil-govern：是？（推荐）
⚠️ 缺失的推荐Skill？（通知用户但可继续）
```

### 复杂改造工作流

```
深度 oil-explore (分布式)
  → 【验证Skill配置】⭐
  → GitHub 深度查证
  → oil-plan (完整规格)
  → 【用户确认】👤
  → oil-delegate (多个子 agent，分阶段)
  → 【多轮迭代】
    → 实现
    → oil-code-review (中间审查，检查 scope 漂移)
  → oil-bug-fix (问题追踪和修复)
  → oil-code-review (最终审查)
  → oil-govern (完整治理报告、分支管理)
  → 完成

涉及 skill：
- oil-explore (分布式，多个并行 sub-agent)
- oil-plan (多方案对比，完整设计)
- oil-delegate (分阶段派发给多个 agent)
- oil-code-review (多轮审查，scope 检查)
- oil-bug-fix (根因分析，系统扫描修复)
- oil-govern (完整的治理报告和分支清理)

验证清单：
✅ 已配置所有必需Skill：oil-explore/plan/delegate/code-review/bug-fix/govern都启用？
✅ 是否有缺失：缺失任何一个都会影响复杂改造工作流
```

---

## 🎯 Skill 配置验证流程（第 2.5 步）

**时机：** AI 第一次接手项目，或每次工作前

### 验证步骤

```python
def verify_skill_config():
    """
    AI 第一次接手项目或每次工作前运行
    """
    
    # 1. 检查 PROJECT-ADAPT.yaml 是否存在
    if not exists('PROJECT-ADAPT.yaml'):
        print("⚠️ 警告：项目没有 PROJECT-ADAPT.yaml")
        print("建议：创建一个基础配置")
        return False
    
    # 2. 加载 Skill 配置
    config = load_yaml('PROJECT-ADAPT.yaml')
    skills_config = config.get('skills', {})
    
    # 3. 判断项目工作流类型
    workflow_type = detect_workflow_type(config)  # 简单/常规/复杂
    
    # 4. 检查必需的 Skill 是否都配置了
    required_skills = get_required_skills_for_type(workflow_type)
    configured_mandatory = skills_config.get('mandatory', [])
    missing_mandatory = required_skills - configured_mandatory
    
    if missing_mandatory:
        print(f"❌ 缺失必需的 Skill（{workflow_type}需要）：{missing_mandatory}")
        print("需要用户决策添加这些 Skill")
        return False
    
    # 5. 检查推荐的 Skill
    all_recommended = get_recommended_skills_for_type(workflow_type)
    configured_recommended = skills_config.get('recommended', [])
    not_configured_recommended = all_recommended - configured_recommended
    
    if not_configured_recommended:
        print(f"⚠️ 推荐但未配置的 Skill（{workflow_type}推荐）：{not_configured_recommended}")
        print("用户可以选择添加")
    
    # 6. 检查项目自定义 Skill
    custom_skills = skills_config.get('custom', [])
    for skill in custom_skills:
        if not exists(f'skills/{skill}/SKILL.md'):
            print(f"❌ 项目 Skill '{skill}' 的文档缺失")
            return False
    
    # 7. 检查 Skill 关系配置
    skill_relations = skills_config.get('relations', {})
    for skill, relation in skill_relations.items():
        if relation.get('type') not in ['supplement', 'replace', 'independent']:
            print(f"❌ Skill '{skill}' 的关系类型无效")
            return False
    
    return True
```

### 验证流程（第一次接手项目时）

```
AI 接到任务
  ↓
运行 verify_skill_config()
  ↓
【情况 1】验证通过 ✅
  → 显示"Skill 配置验证通过"
  → 继续工作
  
【情况 2】缺失必需 Skill ❌
  → 显示缺失清单和原因
  → 提示用户在 PROJECT-ADAPT.yaml 中补齐
  → 等待用户确认后继续
  
【情况 3】推荐 Skill 未配置 ⚠️
  → 显示推荐清单
  → 询问用户是否添加
  → 根据用户选择继续
```

### 验证结果示例

```
🔍 Skill 初始化检查

项目：my-project
工作流级别：L2（已检测）

✅ 已配置的必需 Skill（L2需要）：
   - oil-explore    (理解项目)
   - oil-plan       (制定方案)
   - oil-code-review (代码审查)

⚠️ 推荐但未配置的 Skill（L2推荐）：
   - oil-bug-fix    (bug修复)
   - oil-govern     (项目治理)

❌ 缺失的必需 Skill：
   （无 - 配置完整）

📌 项目自定义 Skill：
   - skill-sql-review       (supplement to oil-code-review)
   - skill-performance-audit (independent)

👉 建议操作：
   1. 建议添加 oil-bug-fix（L2可能遇到bug）
   2. 可选：添加 oil-govern（定期做审计时使用）
   
   在 PROJECT-ADAPT.yaml 中更新，然后继续工作
```

---

## 🚀 如何使用 oil-dev-skills

### 安装

```bash
# 方式 1：安装完整集合
npx skills add oil-oil/oil-dev-skills

# 方式 2：只安装特定 skill
npx skills add oil-oil/oil-dev-skills --skill oil-code-review
```

### 对于用户

**第 1 步：** 理解工作流

读 `specs/WORKFLOW.md`，了解 L1/L2/L3

**第 2 步：** 看对应的 oil-dev-skill

打开 oil-dev-skills/ 中对应的 skill 文件夹

**第 3 步：** 在项目中创建 Dev Profile

在你的项目 `AGENTS.md` 中添加：

```markdown
## Dev profile (oil-dev)

- quick-test: `pytest tests/{target} -q`
- merge-gate: `make ci`
- high-risk: `src/storage/**`, `src/auth/**`
- do-not-edit: `vendor/`, `src/generated/**`
```

**第 4 步：** 使用 oil-dev-skills

告诉 AI 你要做什么，它会自动调用合适的 skill：

```
"Use oil-explore to understand the user export system"
"Use oil-plan to design the export feature"
"Use oil-code-review to review the changes"
```

详见：[oil-dev-skills README.md](https://github.com/oil-oil/oil-dev-skills)

---

### 对于 AI

**执行任务时的流程：**

```
1. 识别工作流级别（L1/L2/L3）
   参考：specs/WORKFLOW.md

2. 根据工作流判断需要哪个 oil-dev-skill
   L1 → oil-explore
   L2 → oil-explore → oil-plan → oil-delegate → oil-code-review → oil-govern
   L3 → 所有 skills，可能还包括 oil-bug-fix

3. 打开对应的 oil-dev-skill
   位置：oil-dev-skills/skills/oil-name/SKILL.md

4. 参考执行说明和真实案例
   位置：oil-dev-skills/skills/oil-name/references/

5. 按照 oil-dev-skills 的脚本进行检查
   位置：oil-dev-skills/scripts/

6. 完成任务
   记录到：docs/{progress.md, decisions.md, HANDOVER.md}
```

---

## 📋 Oil-Dev-Skills 快速索引

| Skill | 作用 | 触发时机 | 文档 |
|-------|------|---------|------|
| oil-explore | 理解项目和代码（读写分离） | L1/L2/L3 开始 | [SKILL.md](https://github.com/oil-oil/oil-dev-skills/blob/main/skills/oil-explore/SKILL.md) |
| oil-plan | 编写可读的方案和规格 | L2/L3 中期 | [SKILL.md](https://github.com/oil-oil/oil-dev-skills/blob/main/skills/oil-plan/SKILL.md) |
| oil-delegate | 派发任务给本地 CLI agents | L2/L3 实现前 | [SKILL.md](https://github.com/oil-oil/oil-dev-skills/blob/main/skills/oil-delegate/SKILL.md) |
| oil-code-review | 代码审查，检查 scope 漂移 | L2/L3 实现后 | [SKILL.md](https://github.com/oil-oil/oil-dev-skills/blob/main/skills/oil-code-review/SKILL.md) |
| oil-bug-fix | 根因分析和系统修复 | L3 修复过程 | [SKILL.md](https://github.com/oil-oil/oil-dev-skills/blob/main/skills/oil-bug-fix/SKILL.md) |
| oil-govern | 文档审计、分支管理、决策记录 | 全程 | [SKILL.md](https://github.com/oil-oil/oil-dev-skills/blob/main/skills/oil-govern/SKILL.md) |

---

## 🔄 工作流 + Oil-Dev-Skill 的完整例子

### L2 例子：添加用户导出功能

```
【工作流】L2 常规功能

【步骤 1】需求理解
├─ oil-explore
│  └─ 理解用户系统和相关代码
│     输出：项目理解报告

【步骤 2】方案设计
├─ GitHub 查证（可选）
│  └─ 查找导出库的最佳实践
├─ oil-plan
│  └─ 决定导出格式（CSV/JSON/Excel）
│     输出：方案文档

【步骤 3】用户确认 👤
└─ 用户："用 CSV，全量导出"

【步骤 4】任务派发
├─ oil-delegate
│  └─ 分解成子任务并派发给 CLI agent
│     输出：任务清单

【步骤 5】实现和验证
├─ CLI agent 负责
│  └─ 编写代码、运行 quick-test

【步骤 6】代码审查
├─ oil-code-review
│  ├─ 检查 scope 漂移（vs 计划）
│  ├─ 检查高风险文件（vs AGENTS.md）
│  └─ 深度审查代码质量
│     输出：审查报告

【步骤 7】决策记录
├─ oil-govern
│  └─ 记录关键决策、管理分支、审计文档
│     输出：治理报告

【完成】更新文档
└─ docs/progress.md、docs/decisions.md、docs/HANDOVER.md
```

---

## 📚 相关文档

**在 vibcoding-rules 中：**
- [specs/WORKFLOW.md](./specs/WORKFLOW.md) - 工作流详解（L1/L2/L3）
- [specs/PRINCIPLES.md](./specs/PRINCIPLES.md) - 编码原则
- [specs/GITHUB-RESEARCH.md](./specs/GITHUB-RESEARCH.md) - GitHub 查证指南
- [AI-EXECUTION-GUIDE.md](./AI-EXECUTION-GUIDE.md) - AI 执行决策树
- [PROJECT-ADAPT-STRATEGY.md](./PROJECT-ADAPT-STRATEGY.md) - 项目适配策略

**在 oil-dev-skills 中：**
- [README.md](https://github.com/oil-oil/oil-dev-skills) - 能力库说明
- [skills/oil-explore/SKILL.md](https://github.com/oil-oil/oil-dev-skills/blob/main/skills/oil-explore/SKILL.md)
- [skills/oil-plan/SKILL.md](https://github.com/oil-oil/oil-dev-skills/blob/main/skills/oil-plan/SKILL.md)
- [skills/oil-delegate/SKILL.md](https://github.com/oil-oil/oil-dev-skills/blob/main/skills/oil-delegate/SKILL.md)
- [skills/oil-code-review/SKILL.md](https://github.com/oil-oil/oil-dev-skills/blob/main/skills/oil-code-review/SKILL.md)
- [skills/oil-bug-fix/SKILL.md](https://github.com/oil-oil/oil-dev-skills/blob/main/skills/oil-bug-fix/SKILL.md)
- [skills/oil-govern/SKILL.md](https://github.com/oil-oil/oil-dev-skills/blob/main/skills/oil-govern/SKILL.md)

---

## 🎯 下一步

1. **安装 oil-dev-skills**
   ```bash
   npx skills add oil-oil/oil-dev-skills
   ```

2. **阅读** [oil-dev-skills 的 README](https://github.com/oil-oil/oil-dev-skills)

3. **创建项目 Dev Profile**
   在你的项目 AGENTS.md 中添加油油的 dev profile 部分

4. **使用** 告诉 AI 你要做什么，它会自动调用合适的 oil-dev-skill

---

## 💡 核心理念再次强调

**规范库 (vibcoding-rules)：**
- ✅ 定义原则和工作流（L1/L2/L3）
- ✅ 告诉你"为什么"和"什么时候"
- ✅ 保持相对稳定和通用

**能力库 (oil-dev-skills)：**
- ✅ 实现 6 个成熟的 skill
- ✅ 告诉你"怎么做"
- ✅ 生产级脚本和工具
- ✅ 完整的评测套件

**配合使用：**
- ✅ 规范库指导工作流决策
- ✅ 能力库提供具体实现工具
- ✅ AI 自动选择正确的 skill
- ✅ 用户只在关键点决策

**这样做的好处：**
- ✅ 不重复造轮子，用成熟的系统
- ✅ 社区维护 oil-dev-skills，我们专注规范
- ✅ 项目可以自定义 oil-dev-skills 的使用方式
- ✅ 完整的权限边界和决策清晰

