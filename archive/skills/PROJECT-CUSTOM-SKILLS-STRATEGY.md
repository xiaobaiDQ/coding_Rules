# PROJECT-CUSTOM-SKILLS-STRATEGY.md - 项目专有 Skill 管理系统

**对象：** 项目管理者 + AI

**目的：** 明确何时创建项目专有 Skill，以及如何管理和维护

---

## 🎯 核心理念

```
Skill 不是越多越好，也不是越大越好

目标：找到最合适的粒度
  ├─ 能力强、功能丰富、内聚性强 → 不拆
  ├─ 能力适中、功能清晰 → 一个 Skill
  └─ 能力太分散、职责混乱 → 拆分
```

---

## 📊 Skill 能力评估模型

### 评估维度

```
维度 1：功能内聚性
├─ 高内聚（都是同一类工作）→ 保持一体
├─ 中内聚（有主有次）→ 保持一体或小拆
└─ 低内聚（完全不同的工作）→ 拆分

维度 2：功能覆盖范围
├─ 窄范围（只做一件事）→ 适合一个 Skill
├─ 中范围（做几件相关的事）→ 一个或两个 Skill
└─ 宽范围（做很多不相关的事）→ 需要拆分

维度 3：复杂度
├─ 低复杂度（< 200 行执行逻辑）→ 一个 Skill
├─ 中复杂度（200-500 行）→ 一个 Skill
└─ 高复杂度（> 500 行）→ 考虑拆分

维度 4：使用频率
├─ 高频（每个项目都用）→ 保持完整
├─ 中频（60% 的项目用）→ 保持完整
└─ 低频（< 30% 的项目用）→ 考虑拆分或可选
```

### 评估得分

```python
def evaluate_skill_complexity(skill_def):
    """评估 Skill 是否需要拆分"""
    
    score = 0
    
    # 【维度 1】功能内聚性（0-25 分）
    cohesion = measure_cohesion(skill_def.functions)
    if cohesion > 0.8:
        score += 25  # 高内聚，不拆
    elif cohesion > 0.6:
        score += 15  # 中内聚，可保持
    else:
        score -= 20  # 低内聚，倾向拆分
    
    # 【维度 2】功能范围（0-25 分）
    scope = measure_scope(skill_def.functions)
    if scope <= 2:
        score += 25  # 窄范围
    elif scope <= 4:
        score += 10  # 中范围
    else:
        score -= 15  # 宽范围
    
    # 【维度 3】复杂度（0-25 分）
    complexity = measure_complexity(skill_def.code)
    if complexity < 200:
        score += 25
    elif complexity < 500:
        score += 15
    else:
        score -= 20
    
    # 【维度 4】使用频率（0-25 分）
    frequency = measure_usage_frequency(skill_def)
    if frequency > 0.7:
        score += 25
    elif frequency > 0.5:
        score += 10
    else:
        score -= 15
    
    # 决策
    if score >= 50:
        return 'keep_as_is'  # 保持不拆
    elif score >= 20:
        return 'keep_with_caution'  # 可保持，但要监控
    else:
        return 'consider_split'  # 考虑拆分
```

---

## ✅ Skill 拆分判断清单

### 什么时候**不用拆分**

✅ **能力强、功能丰富、内聚性高**

```markdown
示例：skill-code-review-extended
└─ 检查代码质量
├─ 检查性能问题
├─ 检查安全隐患
├─ 检查 scope 漂移
└─ 检查高风险文件

特征：
- 都是"审查"这一大类工作
- 内部逻辑关联性强
- 用户场景统一（代码审查时都需要）
- 拆分会增加复杂度

决策：不拆
```

✅ **功能适中、职责清晰**

```markdown
示例：skill-sql-review
├─ SQL 性能分析
├─ 索引使用检查
└─ 锁表风险检查

特征：
- 都是"SQL 检查"这一类
- 功能单一明确
- 总代码量不超过 300 行
- 维护成本低

决策：不拆
```

### ❌ 什么时候**需要拆分**

❌ **能力太分散、职责混乱**

```markdown
反例：skill-everything（千万不要）
├─ 代码审查
├─ 性能测试
├─ 安全扫描
├─ 文档检查
├─ 合规检查
└─ 日志分析

特征：
- 功能完全不相关
- 内聚性极低
- 代码复杂度高
- 维护困难
- 用户场景分散

决策：必须拆分
↓
skill_code_review
skill_performance_test
skill_security_scan
skill_documentation_check
skill_compliance_check
skill_log_analysis
```

❌ **代码过于复杂、难以维护**

```markdown
反例：skill-deploy（过于复杂）
├─ 预部署检查
├─ 灰度部署策略
├─ 健康检查
├─ 回滚机制
├─ 监控告警
└─ 事后分析

特征：
- 总代码超过 800 行
- 条件分支超过 15 个
- 依赖超过 10 个外部模块
- 新人难以理解

决策：拆分
↓
skill_deploy_check（预检查）
skill_deploy_strategy（部署策略）
skill_deploy_monitor（监控和回滚）
```

---

## 🏗️ 项目 Skill 仓库结构

### 推荐结构

```
your-project/
├── AGENTS.md                           ← 项目配置
│
├── skills/                             ← 项目专有 Skill 仓库
│   ├── README.md                       ← Skill 总览
│   │
│   ├── skill-sql-review/
│   │   ├── SKILL.md                    ← Skill 定义
│   │   ├── validators/                 ← 质量检查
│   │   │   └── sql_validator.py
│   │   └── references/                 ← 真实案例
│   │       └── example_1.md
│   │
│   ├── skill-performance-audit/
│   │   ├── SKILL.md
│   │   ├── validators/
│   │   └── references/
│   │
│   └── skill-security-scan/
│       ├── SKILL.md
│       ├── validators/
│       └── references/
│
├── PROJECT-ADAPT.yaml                  ← Skill 配置
├── PROJECT-CUSTOM-SKILLS-INVENTORY.md  ← Skill 清单
│
└── docs/
    ├── DECISIONS.md                    ← 决策记录
    └── SKILL-LIFECYCLE.md              ← Skill 生命周期
```

### Skill 命名规范

```
【命名约定】
skill_<domain>_<action>

示例：
✅ skill_sql_review         ← SQL 审查
✅ skill_perf_audit         ← 性能审计
✅ skill_security_scan      ← 安全扫描
❌ skill_everything         ← 太宽泛
❌ skill_1                  ← 无意义
❌ skill_a_b_c_d_e          ← 太复杂
```

---

## 📋 项目 Skill 清单

### 维护清单文件：PROJECT-CUSTOM-SKILLS-INVENTORY.md

```markdown
# 项目 Skill 清单

## 现有的项目 Skill

### skill_sql_review
- 版本：v1.0.0
- 状态：✅ 活跃
- 功能：SQL 性能审查
- 创建于：2026-11-20
- 最后更新：2026-11-22
- 和 oil-dev-skills 的关系：supplement to oil-code-review
- 维护人：@team
- 文档：[skills/skill-sql-review/SKILL.md](./skills/skill-sql-review/SKILL.md)

### skill-performance-audit
- 版本：v1.0.0
- 状态：✅ 活跃
- 功能：性能指标审计
- ...

## 计划中的项目 Skill

### skill-compliance-check（计划中）
- 目的：检查合规性
- 预计完成：2026-12-15
- 负责人：@compliance-team

## 已废弃的项目 Skill

### skill-legacy-review（已废弃）
- 原因：被 oil-code-review 替代
- 废弃于：2026-11-01
- 迁移指南：[...]
```

---

## 🔄 Skill 生命周期管理

### 阶段 1：设计和评估

```
【输入】新 Skill 的想法

【步骤 1】功能定义
- 这个 Skill 做什么？
- 和现有 oil-dev-skills 的关系是什么？
- 和其他项目 Skill 的关系是什么？

【步骤 2】能力评估
- 运行评估模型
- 获得评分
- 判断要不要拆分

【步骤 3】决策记录
如果决定创建：
doc/DECISIONS.md 中记录：
- 为什么要创建这个 Skill
- 拆分评估结果
- 和 oil-dev-skills 的关系
```

### 阶段 2：实现

```
【创建 Skill 文件】
skills/skill_name/
├── SKILL.md         ← 完整的 Skill 定义
├── validators/      ← 质量检查脚本
└── references/      ← 真实案例

【SKILL.md 包含的内容】
- 目的和触发时机
- 执行流程（伪代码）
- 输入和输出规范
- 质量标准
- 和其他 Skill 的关系
```

### 阶段 3：集成到工作流

```
【在 PROJECT-ADAPT.yaml 中配置】

oil_skills_handling:
  oil_code_review:
    type: supplement
    with:
      - skill_name: skill_sql_review
        trigger: when_sql_involved
        path: skills/skill_sql_review

【在 AI-EXECUTION-GUIDE.md 中更新】
- Skill 选择矩阵
- 执行决策树
```

### 阶段 4：维护和迭代

```
【定期检查】每月一次

- [ ] Skill 还有用吗？
- [ ] 功能有没有漂移？
- [ ] 有没有和新的 oil-dev-skills 重叠？
- [ ] 有没有遗留问题？

【版本管理】
- v1.0.0：初版
- v1.1.0：修复 Bug
- v2.0.0：重大功能变化

【文档同步】
- 更新 SKILL.md
- 更新 PROJECT-CUSTOM-SKILLS-INVENTORY.md
- 记录变更到 SKILL-LIFECYCLE.md
```

### 阶段 5：清理或替代

```
【何时删除项目 Skill】

✅ 情况 1：被 oil-dev-skills 新版本替代
  → 迁移指南
  → 标记为废弃
  → 保留一段时间后删除

✅ 情况 2：项目需求变化，不再需要
  → 评估迁移成本
  → 决定立即删除还是逐步删除
  → 记录决策理由

❌ 不要做的：
- 不要直接删除，要有迁移期
- 不要忘记更新文档
- 不要留下孤立的 Skill
```

---

## 🔀 多个项目 Skill 的协调规则

### 规则 1：避免功能重叠

```
【检查】两个 Skill 是否有重叠功能

skill_sql_review:
  - SQL 性能分析
  - 索引检查

skill_database_audit:
  - 表结构检查
  - 索引设计
  ⚠️ 和 skill_sql_review 有重叠！

【解决方案】
选项 A：合并成一个 Skill（如果功能相关）
选项 B：明确分工（性能 vs 结构）
选项 C：一个 supplement 另一个
```

### 规则 2：依赖关系清晰

```
【定义】Skill 之间的调用关系

skill_sql_review
  ↓ 依赖
  oil_code_review
  ↓ 依赖
  oil_explore

【规则】
- 不允许循环依赖
- 依赖链不超过 3 层
- 要在 PROJECT-ADAPT.yaml 中明确定义
```

### 规则 3：统一的输入输出

```
【约定】所有 Skill 的输入输出格式统一

标准格式：
{
  "status": "success|warning|failure",
  "findings": [...],
  "recommendations": [...],
  "metadata": {
    "execution_time": "2.3s",
    "version": "v1.0.0"
  }
}

【好处】
- AI 可以自动处理多个 Skill 的结果
- 易于集成和组合
- 结果可以自动合并
```

---

## 📊 项目 Skill 配置语法

### PROJECT-ADAPT.yaml 中的完整配置

```yaml
# 项目专有 Skill 配置

project_skills:
  
  # Skill 1：补充 oil-code-review
  - name: skill_sql_review
    type: supplement_to
    target_skill: oil_code_review
    trigger:
      - when: sql_files_changed
        confidence: 95%
      - when: database_config_changed
        confidence: 100%
    execution_order: after_base_skill
    merge_strategy: combine_findings
    version: v1.0.0
    maintained_by: project
    path: skills/skill_sql_review
    documentation: skills/skill_sql_review/SKILL.md
    
  # Skill 2：独立的 Skill（不基于 oil-* 的补充）
  - name: skill_performance_audit
    type: independent
    trigger:
      - when: large_scope_changes
        complexity_threshold: "lines > 500"
    execution_phase: after_implementation
    version: v1.0.0
    maintained_by: project
    path: skills/skill_performance_audit

oil_skills_handling:
  
  # 配置如何使用 oil-code-review
  oil_code_review:
    type: supplement
    with:
      - skill_name: skill_sql_review
        trigger: when_sql_involved
    merge_findings: true  # 自动合并结果

  # 其他 oil-* skill 的配置...
```

---

## ✅ 项目 Skill 创建检查清单

```
【决策阶段】

- [ ] 这个能力是通用的还是项目专有的？
  如果通用 → 建议贡献给 oil-dev-skills
  如果专有 → 继续

- [ ] 能力强弱评估
  运行评估模型 → 获得评分
  
- [ ] 拆分决策
  评分 >= 50 → 保持一体
  评分 < 50 → 考虑拆分

【设计阶段】

- [ ] 功能定义清晰（< 200 字）
- [ ] 触发条件明确
- [ ] 和 oil-dev-skills 的关系确定
- [ ] 命名规范（skill_<domain>_<action>）

【实现阶段】

- [ ] 创建 SKILL.md（完整文档）
- [ ] 创建 validators/（质量检查）
- [ ] 创建 references/（真实案例）
- [ ] 总代码行数 < 500 行

【集成阶段】

- [ ] 更新 PROJECT-ADAPT.yaml
- [ ] 更新 AI-EXECUTION-GUIDE.md
- [ ] 更新 PROJECT-CUSTOM-SKILLS-INVENTORY.md
- [ ] 记录决策到 docs/DECISIONS.md

【验证阶段】

- [ ] 在实际工作流中测试
- [ ] 验证输入输出格式
- [ ] 验证和其他 Skill 的协调
- [ ] 收集反馈
```

---

## 💡 最佳实践

```
1️⃣ 优先用 oil-dev-skills
   不要轻易创建项目 Skill

2️⃣ 如果创建，坚持"小而精"
   单一职责，功能内聚
   
3️⃣ 定期评估
   每月检查是否还需要

4️⃣ 避免过度设计
   不要创建"未来可能用到的" Skill

5️⃣ 文档要清晰
   新人应该能看懂

6️⃣ 版本和生命周期
   明确维护周期和弃用计划

7️⃣ 社区分享
   如果项目 Skill 通用性强，考虑贡献给 oil-dev-skills
```

---

## 📚 相关文档

- [OIL-DEV-SKILLS-EXTENSION.md](./vibcoding-skills/OIL-DEV-SKILLS-EXTENSION.md) - 扩展 oil-dev-skills
- [AI-EXECUTION-GUIDE.md](./AI-EXECUTION-GUIDE.md) - AI 执行决策树
- [PROJECT-ADAPT-STRATEGY.md](./PROJECT-ADAPT-STRATEGY.md) - 项目适配策略
