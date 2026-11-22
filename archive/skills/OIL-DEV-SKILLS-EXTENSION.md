# OIL-DEV-SKILLS-EXTENSION.md - 扩展 oil-dev-skills

**对象：** 用户 + AI

**目的：** 如何在项目中扩展、自定义或覆盖 oil-dev-skills 的行为

---

## 🎯 核心概念

### 两类使用方式

```
通用 oil-dev-skills（oil-oil 维护）
├─ 特点：所有项目共用
├─ 维护：由油油团队维护
├─ 更新：所有项目受益
└─ 修改：通过配置，不修改源码

项目级扩展（项目自己维护）
├─ 特点：项目专有
├─ 维护：项目自己维护
├─ 更新：只影响这个项目
└─ 方式：在 PROJECT-ADAPT.yaml 中配置
```

---

## ✅ 何时需要扩展 oil-dev-skills

### 应该扩展的情况

✅ **技术栈特定**
```
你的项目用 PostgreSQL，有复杂的数据迁移需求
现状：oil-code-review 通用的检查不了 SQL 性能

处理：
1. 在项目中创建 skill-sql-review
2. 在 PROJECT-ADAPT.yaml 中配置为 supplement
3. 工作流中：oil-code-review + skill-sql-review 一起跑
```

✅ **项目特定的流程**
```
你的项目有严格的性能审查要求
现状：oil-code-review 的性能检查不够严格

处理：
1. 创建 skill-performance-audit
2. 配置为 supplement
3. 在涉及性能相关改动时触发
```

### 不应该扩展的情况

❌ **完全重复 oil-dev-skills**
```
不要创建和 oil-code-review 功能一样的东西
应该：直接用 oil-code-review，或创建覆盖规范
```

❌ **还在试验的流程**
```
如果这个流程还在试验阶段
不要立即扩展
应该：等流程稳定后再创建
```

❌ **只用一次的东西**
```
如果这个任务只会做一次
不要创建 skill
应该：直接在工作流中处理
```

---

## 🛠️ 如何扩展 oil-dev-skills

### 步骤 1：设计项目 Skill

如果你需要扩展，创建项目级的 skill：

```
your-project/skills/
└── skill-name/
    └── SKILL.md
```

**定义文件：** `your-project/skills/skill-name/SKILL.md`

例子：

```markdown
# skill-sql-review - SQL 性能审查

## 目的
检查 SQL 语句的性能问题。

## 触发时机
- L2/L3 工作流中涉及数据库改动时
- 在 oil-code-review 之后

## 执行流程

### 检查项
1. 查询复杂度分析
2. 索引使用检查
3. N+1 查询检测
4. 锁表风险检查

## 输出
- SQL 审查报告
- 性能建议
- 优化方案（如果有）

## 质量标准
- 必须在 dev 环境执行 EXPLAIN ANALYZE
- 必须检查执行计划
- 必须验证新增索引的有效性
```

### 步骤 2：在 PROJECT-ADAPT.yaml 中配置

```yaml
# your-project/PROJECT-ADAPT.yaml

oil_skills_handling:
  
  # 类型 1：补充关系
  oil_code_review:
    type: supplement              # 补充，不替代
    with:
      - skill_name: skill_sql_review
        path: skills/skill_sql_review
        trigger: when_sql_involved
    merge_strategy: combine        # 结果合并
  
  # 类型 2：替代关系（不推荐）
  oil_plan:
    type: replace                  # 替代
    with: skill_custom_plan        # 用什么替代
    reason: "我们有自己成熟的规划流程"
  
  # 类型 3：条件使用
  oil_explore:
    type: supplement
    with:
      - skill_name: skill_arch_analysis
        trigger: when_large_scope  # 大范围改动时触发
        path: skills/skill_arch_analysis
```

---

## 🔄 Skill 冲突的处理

### 场景 1：补充关系（推荐）

```
oil-code-review 和 skill-sql-review

工作流中：
1. 先跑 oil-code-review（通用检查）
2. 再跑 skill-sql-review（SQL 检查）
3. 结果合并

配置：
oil_code_review:
  type: supplement
  with:
    - skill_name: skill_sql_review
      trigger: when_sql_involved
```

### 场景 2：替代关系（谨慎使用）

```
oil-plan 被完全替代为 skill-custom_plan

工作流中：
1. 只跑 skill-custom_plan
2. 完全不调用 oil-plan

配置：
oil_plan:
  type: replace
  with: skill_custom_plan
  
注意：
- 下次 oil-dev-skills 升级时，新功能无法受益
- 维护成本高
- 只在有充分理由时使用
```

---

## 📝 在工作流中使用扩展 Skill

### AI 的处理流程

```python
def execute_skill_step(skill_name):
    
    # 1. 加载项目配置
    project_config = load_yaml('PROJECT-ADAPT.yaml')
    
    # 2. 检查是否有项目级扩展
    extensions = project_config.get_oil_skills_handling(skill_name)
    
    if extensions:
        
        for ext in extensions:
            
            if ext.type == 'supplement':
                # 补充：都跑
                result1 = run_oil_skill(skill_name)
                result2 = run_project_skill(ext.with)
                
                # 检查触发条件
                if should_trigger(ext.trigger):
                    return merge(result1, result2)
                else:
                    return result1
            
            elif ext.type == 'replace':
                # 替代：只跑项目的
                return run_project_skill(ext.with)
    
    else:
        # 没有扩展，只跑 oil 的
        return run_oil_skill(skill_name)
```

---

## ✅ 项目 Skill 的维护

### 检查清单

```
【定期检查】每月一次

- [ ] 所有项目 skill 还有用吗？
- [ ] 有没有和新的 oil-dev-skills 重叠？
- [ ] 有没有不再适用的 skill？
- [ ] 有没有需要更新的 skill？

【和 oil-dev-skills 同步】

- [ ] oil-dev-skills 有升级吗？
- [ ] 我们的项目 skill 还兼容吗？
- [ ] 新功能能用吗？
- [ ] 需要调整吗？
```

---

## 📋 决策记录

```
当添加或修改项目 skill 时，记录：

# 决策记录 - 添加 skill-sql-review

## 为什么
项目需要管理 SQL 性能，oil-code-review 的 SQL 检查不够专业。

## 选择
- 选项 A：修改 oil-code-review（不行，会影响其他项目）
- 选项 B：创建项目 skill-sql-review（✅ 选择这个）

## 和 oil-dev-skills 的关系
补充关系：
- oil-code-review 检查通用代码质量
- skill-sql-review 检查 SQL 性能
两个都会运行

## 状态
✅ 已创建
✅ 在 PROJECT-ADAPT.yaml 中配置
✅ 在工作流中可用
```

---

## 🎯 最佳实践

```
1. 优先用 oil-dev-skills 的配置能力
   不要轻易扩展

2. 如果必须扩展，选择补充关系
   而不是替代关系

3. 文档要清晰
   说明为什么扩展，何时触发

4. 定期维护
   检查是否还需要

5. 避免过度扩展
   "更多 skill" 不等于"更好"
```

---

## 📊 oil-dev-skills 官方文档

详见：[oil-dev-skills 的完整文档](https://github.com/oil-oil/oil-dev-skills)

包括：
- Dev profile 配置
- 完整的工作流指南
- 生产级脚本使用
- 分布式探索配置
- 个人偏好设置

