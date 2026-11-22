# PROJECT-ADAPT-STRATEGY.md - 项目适配策略

**对象：** AI（自动执行） + 用户（决策审核）

**目的：** 将通用规范自动适配到具体项目

---

## 🎯 适配的三个层级

### 层级 1：扫描项目现状

```
AI 需要理解：
✅ 项目的技术栈是什么
✅ 项目现有的编码规范
✅ 项目现有的工作流
✅ 项目的开发水平和成熟度
✅ 项目是否已有文档化的规范
```

**AI 的扫描方式：**

```python
def scan_project(project_path):
    # 1. 技术栈识别
    - 读 package.json / pom.xml / Cargo.toml 等
    - 识别：语言、框架、版本、依赖
    
    # 2. 代码规范识别
    - 查找：.eslintrc / .prettierrc / .flake8 等
    - 识别：已有的代码风格配置
    
    # 3. 工作流识别
    - 读 README.md / CONTRIBUTING.md
    - 查找：PR 流程、review 流程、发布流程
    
    # 4. 文档结构识别
    - 查找：是否有 docs/ 目录
    - 识别：是否有编码规范文档
    - 识别：是否有决策记录
    
    # 5. 成熟度评估
    - 代码行数 → 项目规模
    - 是否有测试 → 质量意识
    - 是否有版本管理 → 流程成熟度
```

---

### 层级 2：对比并识别冲突

```
比对内容：

1. 编码原则冲突
   通用：Simplicity First（尽可能简单）
   项目：性能优先（某些关键路径可以复杂）
   → 冲突项 #1

2. 工作流冲突
   通用：简单 / 常规 / 复杂三级
   项目：只有 feature branch / hotfix 两级
   → 冲突项 #2

3. 验收标准冲突
   通用：所有代码都需要 code review
   项目：只有 PR > 100 行需要 review
   → 冲突项 #3

4. 技术栈冲突
   通用：推荐用 GitHub 查证方案
   项目：团队已有决策历史，不想重新查证
   → 冲突项 #4
```

**AI 的对比方式：**

```python
def identify_conflicts(project_scan, universal_rules):
    conflicts = []
    
    for rule in universal_rules:
        project_practice = project_scan.get(rule.category)
        
        if not project_practice:
            # 新增规则（不是冲突，只是新加）
            conflicts.append({
                'type': 'new_rule',
                'rule': rule,
                'action': 'inform_user'
            })
        
        elif project_practice != rule.standard:
            # 真正的冲突
            conflicts.append({
                'type': 'conflict',
                'rule': rule,
                'project_practice': project_practice,
                'universal_standard': rule.standard,
                'impact': rule.calculate_impact()
            })
    
    return conflicts
```

---

### 层级 3：生成冲突报告

**冲突报告的结构：**

```markdown
# 项目适配冲突报告

## 冲突总览
- 总冲突数：5
- 高影响冲突：2
- 中影响冲突：2
- 低影响冲突：1

## 冲突详情

### 冲突 #1：编码原则 - Simplicity First
**通用规范：**
- 原则：最小代码，拒绝过度工程
- 深化规则：没有好的理由不要用 fancy 的东西

**项目现状：**
- 实际做法：性能关键路径允许复杂优化
- 理由：用户导入 100w 数据时需要 < 100ms

**影响评估：**
- ⚠️ 高影响
- 影响：所有代码审查的标准
- 建议：项目级覆盖

**决策选项：**
- 选项 A：保留项目做法（允许例外）
- 选项 B：迁移到通用规范
- 选项 C：混合（大多数地方用通用，性能路径例外）

---

### 冲突 #2：工作流 - L1 定义
...
```

---

## 🔄 完整的适配流程

### 步骤 1：初始扫描（AI 自动）

```
AI 扫描项目 → 收集现状信息
```

**输出：**
- 项目信息文件（技术栈、现有规范、工作流等）

---

### 步骤 2：对比识别（AI 自动）

```
AI 对比（项目现状 vs 通用规范）→ 生成冲突列表
```

**输出：**
- 冲突项列表（3-10 个）
- 每个冲突的影响评估

---

### 步骤 3：生成报告（AI 自动）

```
AI 生成详细的冲突报告 → 显示给用户
```

**报告包含：**
- 冲突总览（表格）
- 冲突详情（每个冲突）
- 建议决策方案
- 影响分析

---

### 步骤 4：用户决策（👤 用户参与）

```
用户逐个审核冲突 → 做出决策
```

**决策选项：**
```
对于每个冲突，用户可以选择：
A. 保留项目做法
B. 采用通用规范
C. 自定义（混合方案）
D. 标记为"例外"，记录理由
```

---

### 步骤 5：应用决策（AI 自动）

```
AI 根据用户的所有决策 → 生成项目适配配置
```

**生成的文件：**

```yaml
# PROJECT-ADAPT.yaml

project_name: "My Project"

adapts:
  - rule: "PRINCIPLES.Simplicity First"
    decision: "keep_project"  # A
    reason: "性能需求优先"
    
  - rule: "WORKFLOW.简单改动定义"
    decision: "merge"  # C
    override: |
      简单改动定义增加：需要更新性能指标
    
  - rule: "GITHUB-RESEARCH.required_for_all"
    decision: "mark_exception"  # D
    reason: "团队已有决策历史，不再查证"
    
  - rule: "new_rule_from_universal"
    decision: "adopt"  # B（新规则，直接采用）
    when: "2026-12-01"
```

---

### 步骤 6：生成项目文件（AI 自动）

```
AI 根据 PROJECT-ADAPT.yaml → 生成项目级规范文件
```

**生成的文件：**

```
your-project/
├── PROJECT-ADAPT.yaml          ← 决策记录
├── RULES-OVERRIDE.md           ← 项目级覆盖规范
├── TECH-STACK.md               ← 项目技术栈约定
├── WORKFLOW-ADAPT.md           ← 项目工作流调整
└── docs/HANDOVER.md            ← 交接文档（已更新）
```

---

### 步骤 7：记录决策（AI 自动）

```
AI 记录：
- 适配时间
- 所有冲突项的决策
- 推理过程
- 未来可能的改动
```

**记录到：** `docs/DECISIONS.md`

---

## 📋 AI 执行检查清单

```
【步骤 1】扫描项目
- [ ] 读了 package.json / pom.xml / Cargo.toml
- [ ] 读了 README.md / CONTRIBUTING.md
- [ ] 查找了现有的 linter/formatter 配置
- [ ] 评估了项目成熟度
- [ ] 记录了所有发现

【步骤 2】对比规范
- [ ] 逐项对比通用原则
- [ ] 逐项对比工作流
- [ ] 逐项对比验收标准
- [ ] 标记了每个冲突的影响等级

【步骤 3】生成报告
- [ ] 冲突总览完整
- [ ] 每个冲突的详情清晰
- [ ] 决策选项写得够清楚
- [ ] 影响分析准确

【步骤 4】等用户决策
- [ ] 展示了冲突报告
- [ ] 给出了建议方案
- [ ] 等待用户逐个决策

【步骤 5】应用决策
- [ ] 正确理解了用户的所有决策
- [ ] 生成了 PROJECT-ADAPT.yaml
- [ ] 记录了理由和时间戳

【步骤 6】生成项目文件
- [ ] 生成了 RULES-OVERRIDE.md
- [ ] 生成了 TECH-STACK.md
- [ ] 生成了 WORKFLOW-ADAPT.md
- [ ] 更新了 HANDOVER.md

【步骤 7】记录决策
- [ ] 创建了 docs/DECISIONS.md
- [ ] 记录了完整的决策历史
```

---

## 🎯 适配后的状态

```
此后，当 AI 执行任务时：

1. 读通用规范
   vibcoding-rules/specs/

2. 加载项目适配
   your-project/PROJECT-ADAPT.yaml

3. 合并（通用 + 项目覆盖）
   合并后的规范 = 这个项目的真实规范

4. 按项目规范执行
   100% 遵循项目规范，不再有冲突
```

---

## 📝 决策原则 - 项目规范覆盖的权限边界

**关键问题：项目规范能覆盖通用规范的什么部分？**

### 分类框架

```
【能覆盖】项目级的工作流调整
├─ L1/L2/L3 的具体条件（例如"这个项目所有功能都是L2"）
├─ Skill 的选择和配置（例如"不用 oil-plan，直接 oil-delegate"）
├─ 验收标准（例如"50行以上才需要code review"）
├─ 技术栈约定（例如"性能路径允许优化"）
└─ 文档结构（例如"决策记录放在 ADR/ 而不是 DECISIONS.md"）

【有条件地覆盖】核心编码原则
├─ Simplicity First：只能在性能/安全/可靠性有明确需求时覆盖，必须记录理由
├─ Surgical Changes：不能覆盖，这是代码质量底线
├─ Think Before Coding：不能覆盖，这是思维方法底线
└─ Goal-Driven Execution：不能覆盖，这是交付标准底线

【不能覆盖】核心编码原则的本质
├─ ❌ 能跳过"思考"这一步吗？不能
├─ ❌ 能做过度工程化吗？不能（即使项目说允许也不行）
├─ ❌ 能随意修改无关代码吗？不能
├─ ❌ 能跳过验证吗？不能
```

### 覆盖的正确方式

```yaml
# PROJECT-ADAPT.yaml

adapts:
  
  # ✅ 正确的覆盖方式 1：工作流调整
  - rule: "WORKFLOW.L1_definition"
    type: "override"
    override: |
      本项目的L1定义增加：
      - 条件：所有API改动都升级到L2
      - 理由：这个项目的API改动很容易引起级联影响
    
  # ✅ 正确的覆盖方式 2：性能需求覆盖Simplicity First
  - rule: "PRINCIPLES.Simplicity_First"
    type: "override_with_condition"
    scope: "性能关键路径（src/core/optimizer/）"
    override: |
      在这个模块允许复杂优化，理由：
      - 性能需求：导出100w数据需要<100ms
      - 衡量：已有性能测试验证
    when: "2026-11-22"
  
  # ✅ 正确的覆盖方式 3：Skill选择调整
  - rule: "SKILLS-INTEGRATION.L2_skills"
    type: "override"
    override: |
      本项目L2工作流使用的Skill：
      - oil-explore
      - oil-delegate（替代oil-plan）
      - oil-code-review
      理由：项目已有成熟的设计文档模板，不需要额外的plan阶段
  
  # ❌ 错误的覆盖方式 1：跳过思考
  - rule: "PRINCIPLES.Think_Before_Coding"
    type: "override"  # ❌ 不能这样
    override: "我们追求速度，所以跳过思考步骤"
  
  # ❌ 错误的覆盖方式 2：模糊的"兼容性"
  - rule: "PRINCIPLES.Simplicity_First"
    type: "override"
    override: "为了兼容可能的未来需求，允许多个配置选项"
    # ❌ 理由不够具体，"可能的未来"不是有效覆盖理由
```

### 审查检查清单

**如果项目想覆盖某个规则，请审视这个清单：**

```
[ ] 我想覆盖什么规则？（明确写出来）
[ ] 是核心编码原则吗？（Think/Simplicity/Surgical/Goal-Driven）
    ├─ 是 Think/Surgical/Goal-Driven → ❌ 不能覆盖，停止
    ├─ 是 Simplicity First
    │  [ ] 是否有明确的业务理由？（性能/安全/可靠性指标）
    │  [ ] 理由是否可量化？（例如"<100ms"而不是"可能快点"）
    │  [ ] 覆盖范围是明确的吗？（某个模块 vs 整个项目）
    │  ☐ 是否会在代码注释中说明？
    └─ 都是 → ✅ 允许覆盖
[ ] 是工作流调整吗？
    ├─ 是 → ✅ 允许覆盖
    └─ 记录到 PROJECT-ADAPT.yaml
[ ] 是Skill选择吗？
    ├─ 是 → ✅ 允许覆盖
    └─ 记录到 PROJECT-ADAPT.yaml
```


---

## 🔄 未来改动

**如果规范更新了怎么办？**

```
vibcoding-rules v1.0 → v1.1 (小更新)
  → AI 自动检查 PROJECT-ADAPT.yaml
  → 识别新增的规则
  → 询问用户："要采用这个新规则吗？"
  → 更新 PROJECT-ADAPT.yaml

vibcoding-rules v1.0 → v2.0 (大更新)
  → AI 自动重新运行适配流程
  → 重新生成冲突报告
  → 询问用户重新决策
```

