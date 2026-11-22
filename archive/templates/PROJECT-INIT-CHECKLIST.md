# PROJECT-INIT-CHECKLIST.md - 新项目初始化检查清单

**对象：** AI（自动执行）+ 用户（决策）

**目的：** 新项目快速集成 vibcoding 规范体系

---

## 🚀 初始化流程

```
新项目复制规范库
         ↓
AI 执行 【阶段 1】项目扫描
         ↓
AI 执行 【阶段 2】规范对比
         ↓
用户做 【阶段 3】决策
         ↓
AI 执行 【阶段 4】配置生成
         ↓
✅ 完成，项目准备好了
```

---

## 【阶段 1】项目扫描

### 技术栈识别

```
任务：自动识别项目的技术栈

检查清单：
- [ ] 读 package.json（Node.js）
  输出：Node 版本、主要框架、依赖
  
- [ ] 读 pom.xml（Java）
  输出：Java 版本、主要框架、依赖
  
- [ ] 读 Cargo.toml（Rust）
  输出：Rust 版本、主要库
  
- [ ] 读 setup.py / requirements.txt（Python）
  输出：Python 版本、主要库
  
- [ ] 读 go.mod（Go）
  输出：Go 版本、主要库
  
- [ ] 读 .github/workflows/（CI/CD）
  输出：自动化流程、测试框架、部署方式

输出文件：tech-stack-scan.txt
```

### 现有规范识别

```
任务：自动识别项目是否已有规范

检查清单：
- [ ] 是否有 README.md
  如果有：
    - 提取编码规范部分
    - 提取工作流部分
    
- [ ] 是否有 CONTRIBUTING.md
  如果有：
    - 提取贡献指南
    - 提取 PR 流程
    - 提取 review 标准
    
- [ ] 是否有 docs/ 目录
  如果有：
    - 列出所有文档
    - 提取相关规范
    
- [ ] 是否有 .eslintrc / .flake8 等 linter 配置
  如果有：
    - 提取代码风格约定
    
- [ ] 是否有 CODE_OF_CONDUCT.md
  如果有：
    - 提取团队约定

输出文件：existing-standards.txt
```

### 项目成熟度评估

```
任务：评估项目的开发成熟度

指标 1：项目规模
- 代码行数 < 10k    → 小型项目
- 代码行数 10k-100k → 中型项目
- 代码行数 > 100k   → 大型项目

指标 2：测试覆盖率
- 有测试 + 覆盖 > 80% → 高成熟度
- 有测试 + 覆盖 50-80% → 中成熟度
- 有测试 + 覆盖 < 50% → 低成熟度
- 没有测试            → 需要补充

指标 3：文档质量
- 有详细文档 → 高
- 有基础文档 → 中
- 文档缺失  → 低

指标 4：流程规范
- 有 CI/CD → 自动化程度高
- 只有 manual → 自动化程度低

输出文件：maturity-assessment.txt
```

### 生成扫描报告

```markdown
# 项目扫描报告

## 技术栈
- 语言：Node.js 18.0+
- 框架：Express 4.18
- 数据库：PostgreSQL 14
- 测试：Jest 29
- 部署：Docker + Kubernetes

## 现有规范
- ✅ 有 CONTRIBUTING.md
- ✅ 有 .eslintrc.json
- ❌ 没有编码原则文档
- ❌ 没有 HANDOVER 文档

## 项目成熟度
- 规模：中型（52k 行代码）
- 测试覆盖：78%
- 文档质量：中等
- 自动化：CI/CD 完整

## 建议
这个项目适合集成 vibcoding，建议重点关注：
1. 新增编码原则文档（现在没有）
2. 新增 HANDOVER 文档（便于交接）
3. 保留现有的 .eslintrc 配置（已稳定）
```

---

## 【阶段 2】规范对比

### 自动对比规范

```
任务：比对项目现状和通用规范，找出冲突

对比项目 1：编码原则
┌────────────────────────────────────────┐
│ 通用规范：Simplicity First             │
│ 项目现状：性能优先（特定路径）         │
│ → 冲突项 #1                            │
└────────────────────────────────────────┘

对比项目 2：工作流
┌────────────────────────────────────────┐
│ 通用规范：L1/L2/L3 三级                │
│ 项目现状：只有 feature branch 和 hotfix │
│ → 冲突项 #2                            │
└────────────────────────────────────────┘

对比项目 3：Code Review
┌────────────────────────────────────────┐
│ 通用规范：所有 PR 都需要 review        │
│ 项目现状：只有 > 100 行需要 review     │
│ → 冲突项 #3                            │
└────────────────────────────────────────┘

... 更多对比
```

### 生成冲突报告

```markdown
# 规范对比冲突报告

## 冲突总览
总冲突数：4
- 高影响：1
- 中影响：2
- 低影响：1

## 冲突详情

### 冲突 #1（高影响）：Simplicity First
**通用规范：** 最小代码，拒绝过度工程
**项目现状：** 用户导入需要性能优化，允许复杂优化
**影响范围：** 所有 code review 的标准
**建议方案：** 保留项目做法（允许性能优化例外）

### 冲突 #2（中影响）：工作流级别
**通用规范：** L1（< 50行）/ L2（常规）/ L3（复杂）
**项目现状：** 只区分 feature 和 hotfix
**影响范围：** 新功能的流程定义
**建议方案：** 采用通用规范（更清晰）

## 下一步
用户需要逐个审核这些冲突，做出决策
```

---

## 【阶段 3】用户决策

### 显示冲突报告

```
AI 生成的冲突报告 → 显示给用户

用户逐个审核，做出决策：

冲突 #1：Simplicity First
用户选择：保留项目做法（性能优先在关键路径）

冲突 #2：工作流级别
用户选择：采用通用规范（L1/L2/L3）

冲突 #3：Code Review 标准
用户选择：混合（大多数地方全部 review，
         但自动化测试通过的小改动除外）

... 等等
```

### 收集决策

```python
user_decisions = {
    'conflict_1': {
        'rule': 'PRINCIPLES.Simplicity First',
        'decision': 'keep_project',
        'reason': 'Performance critical path needs optimization'
    },
    'conflict_2': {
        'rule': 'WORKFLOW.L1_L2_L3',
        'decision': 'adopt_universal',
        'when': '2026-12-01'
    },
    'conflict_3': {
        'rule': 'CODE_REVIEW.all_prs',
        'decision': 'custom',
        'override': 'review_all_except_automated_fixes'
    },
    # ... 更多
}
```

---

## 【阶段 4】配置生成

### 生成 PROJECT-ADAPT.yaml

```yaml
# your-project/PROJECT-ADAPT.yaml

project_name: "My Backend API"
vibcoding_version: "v1.0.0"
adapted_date: "2026-11-22"

# 技术栈信息
tech_stack:
  language: "Node.js 18"
  framework: "Express 4.18"
  database: "PostgreSQL 14"
  test_framework: "Jest 29"

# 规范适配决策
adapts:
  - rule: "PRINCIPLES.Simplicity First"
    decision: "keep_project"
    reason: "Performance critical path needs optimization"
    
  - rule: "WORKFLOW.L1_L2_L3"
    decision: "adopt_universal"
    
  - rule: "CODE_REVIEW.all_prs"
    decision: "custom"
    override: |
      - 自动化测试通过的小改动（< 20 行）可以跳过 manual review
      - 其他所有改动都需要至少 1 个 review

# 工作流适配
workflows:
  L1:
    added: "需要更新 metrics（如果改动了性能相关代码）"
  
  L2:
    code_review:
      - generic_review: skill-code-review
      - project_review: 检查 SQL 性能（如果涉及数据库）

# 自定义 skills
custom_skills:
  - name: "skill-sql-review"
    path: "skills/skill-sql-review"
    relation: "supplement"  # 补充 skill-code-review
    trigger: "when_sql_involved"

# 验收标准
acceptance_criteria:
  - "所有 code review 都通过"
  - "测试覆盖 > 80%（新代码）"
  - "性能指标检查通过（如果相关）"
  - "文档更新完成"
```

### 生成项目级规范文件

```
your-project/
├── PROJECT-ADAPT.yaml          ← 决策记录
├── RULES-OVERRIDE.md           ← 编码原则覆盖
├── WORKFLOW-ADAPT.md           ← 工作流调整
├── TECH-STACK.md               ← 技术栈约定
└── docs/
    ├── HANDOVER.md             ← 交接文档（已初始化）
    └── DECISIONS.md            ← 决策记录
```

---

## ✅ AI 执行检查清单

```
【阶段 1：项目扫描】
- [ ] 识别了技术栈
  - [ ] 读了主配置文件（package.json 等）
  - [ ] 识别了语言版本
  - [ ] 识别了主要框架
  - [ ] 识别了测试框架
  
- [ ] 识别了现有规范
  - [ ] 读了 README.md（如果有）
  - [ ] 读了 CONTRIBUTING.md（如果有）
  - [ ] 读了 linter 配置（如果有）
  - [ ] 查找了文档结构
  
- [ ] 评估了项目成熟度
  - [ ] 计算了代码行数
  - [ ] 评估了测试覆盖率
  - [ ] 评估了文档质量
  - [ ] 评估了自动化程度
  
- [ ] 生成了扫描报告

【阶段 2：规范对比】
- [ ] 对比了每一项通用规范
- [ ] 识别了所有冲突项
- [ ] 评估了每个冲突的影响
- [ ] 生成了冲突报告

【阶段 3：用户决策】
- [ ] 显示了冲突报告给用户
- [ ] 给出了建议方案
- [ ] 收集了用户的所有决策
- [ ] 确认了每个决策

【阶段 4：配置生成】
- [ ] 生成了 PROJECT-ADAPT.yaml
- [ ] 生成了 RULES-OVERRIDE.md
- [ ] 生成了 WORKFLOW-ADAPT.md
- [ ] 生成了 TECH-STACK.md
- [ ] 初始化了 docs/HANDOVER.md
- [ ] 初始化了 docs/DECISIONS.md
- [ ] 创建了 docs/progress.md

【完成阶段】
- [ ] 所有配置文件都生成了
- [ ] 项目已经可以开始工作
- [ ] 更新了项目的 README.md
  添加了 vibcoding 规范库的引用
```

---

## 🎯 初始化后的项目结构

```
your-project/
├── README.md                   ← 更新：添加规范库引用
├── CONTRIBUTING.md             ← 可选：更新或创建
│
├── PROJECT-ADAPT.yaml          ← 新增：适配配置
├── RULES-OVERRIDE.md           ← 新增：规范覆盖
├── WORKFLOW-ADAPT.md           ← 新增：工作流调整
├── TECH-STACK.md               ← 新增：技术栈
│
├── docs/
│   ├── HANDOVER.md             ← 新增：交接文档
│   ├── DECISIONS.md            ← 新增：决策记录
│   ├── progress.md             ← 新增：进度追踪
│   └── ...（其他现有文档）
│
├── skills/                     ← 新增：项目 skills（可选）
│   └── skill-name/
│
├── src/
├── tests/
└── ...（其他现有文件）
```

---

## 💡 初始化后的工作方式

```
初始化完成后，项目就可以开始工作了

用户: "实现用户导出功能"

AI:
1. 读 PROJECT-ADAPT.yaml
2. 判断工作流级别：L2
3. 加载规范：通用规范 + PROJECT-ADAPT.yaml 覆盖
4. 合并规范
5. 选择 skills：skill-explore → skill-plan → ...
6. 执行工作流
7. 完成

下一次接手这个项目时：
新 AI 只需要读 docs/HANDOVER.md 就能快速恢复
```

---

## 🚀 快速启动命令

```bash
# 1. 复制规范库到项目
cp -r /path/to/vibcoding-rules your-project/

# 2. 告诉 AI 开始初始化
# "初始化项目，集成 vibcoding 规范"

# AI 自动执行所有阶段

# 3. 完成后
# 项目已经准备好，可以开始工作了
```

