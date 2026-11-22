# AI-EXECUTION-GUIDE.md - AI 执行决策树

**对象：** AI（自动执行的决策流程）

**目的：** 当 AI 接到任务时，应该如何自动决策和执行

---

## 🎯 核心决策流程

```
用户: "实现用户导出功能"
         ↓
【第 1 步】判断改动类型（简单 / 常规 / 复杂）
         ↓
【第 2 步】加载项目适配配置
         ↓
【第 2.5 步】验证 Skill 配置 ⭐
         ↓
【第 3 步】合并规范（通用 + 项目）
         ↓
【第 4 步】选择合适的 skill
         ↓
【第 5 步】执行工作流
         ↓
【第 6 步】记录决策
         ↓
完成
```

---

## 📋 第 1 步：判断改动类型

### 决策标准

```
🟢 简单改动 - 同时满足所有条件
├─ 代码改动 < 50 行
├─ 单文件改动（或最多 2-3 个紧密相关文件）
├─ 不改 API 签名、数据结构、公开接口
├─ 原因明确，做法固定
├─ 没有系统级影响
└─ 没有高风险操作

🟡 常规改动 - 满足任何一个
├─ 代码改动 50-500 行
├─ 新增功能模块
├─ 修改现有模块的关键逻辑
├─ 需要外部依赖（新库、新服务调用）
├─ 性能优化
├─ 安全相关改动
├─ 数据库迁移或表结构变更
├─ 需要制定方案
└─ 有系统级设计但不复杂

🔴 复杂改造 - 满足任何一个
├─ 代码改动 > 500 行
├─ 跨多个子系统的改动
├─ 架构级改变
├─ 高风险改动（认证、支付、数据处理等）
├─ 需要多个依赖项更新
├─ 重大的不确定性
├─ 需要多个团队配合
└─ 需要多个 Agent 分阶段执行
```

### 歧义处理

```
如果不确定是简单还是常规：
  → 倾向于常规（保守，会要求方案确认）

如果不确定是常规还是复杂：
  → 看"重大不确定性"是否存在
  → 有 → 复杂
  → 没有 → 常规

如果用户明确指定了类型：
  → 遵循用户的指定
  → 但在执行前再确认一遍："我理解这是常规改动，对吗？"
```

---

## 🔧 第 2 步：加载项目适配配置

### 加载顺序

```python
def load_project_rules():
    # 1. 优先级最高：PROJECT-ADAPT.yaml
    if exists('PROJECT-ADAPT.yaml'):
        return load('PROJECT-ADAPT.yaml')
    
    # 2. 其次：项目的覆盖规范
    if exists('RULES-OVERRIDE.md'):
        parse('RULES-OVERRIDE.md')
    
    # 3. 最后：通用规范
    return load('vibcoding-rules/specs/')
```

### 加载内容

```
✅ 项目的编码原则覆盖
✅ 项目的工作流覆盖
✅ 项目的技术栈约定
✅ 项目的 skill 映射
✅ 项目的验收标准
```

---

## ⭐ 第 2.5 步：验证 Skill 配置

**目的：** 确保项目的 Skill 配置完整有效

### 验证检查清单

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
    
    # 3. 检查必需的 Skill 是否都配置了
    all_required = get_all_required_skills(config)
    configured = skills_config.get('required', [])
    missing = all_required - configured
    
    if missing:
        print(f"❌ 缺失必需的 Skill：{missing}")
        print("需要用户决策添加这些 Skill")
        return False
    
    # 4. 检查推荐的 Skill
    all_recommended = get_recommended_skills(config)
    configured_optional = skills_config.get('optional', [])
    not_configured_recommended = all_recommended - configured_optional
    
    if not_configured_recommended:
        print(f"⚠️ 推荐但未配置的 Skill：{not_configured_recommended}")
        print("用户可以选择添加")
    
    # 5. 检查项目自定义 Skill
    custom_skills = skills_config.get('custom', [])
    for skill in custom_skills:
        if not exists(f'skills/{skill}/SKILL.md'):
            print(f"❌ 项目 Skill '{skill}' 的文档缺失")
            return False
    
    # 6. 检查 Skill 关系配置
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

---

## 🔀 第 3 步：合并规范（通用 + 项目）

### 合并逻辑

```
对于通用规范的每一项：

1. 检查项目是否有覆盖
   
   if 有覆盖:
       使用项目覆盖
   else:
       使用通用规范

2. 如果有冲突（项目覆盖和通用规范矛盾）：
   
   → 这是错误的适配配置
   → 应该已经在适配阶段解决了
   → 如果还有冲突，记录到 DECISIONS.md
```

### 合并示例

```
通用规范：所有 PR 都需要 code review
项目覆盖：只有 > 100 行的 PR 需要 review

合并后的规范：
"这个项目：只有 > 100 行的 PR 需要 review"
（项目覆盖优先）
```

---

## 🎯 第 4 步：选择合适的 Skill

### Skill 选择矩阵

```
改动类型 | 涉及的 Skill                              | 顺序
---------|------------------------------------------|----------
简单     | oil-explore                             | explore → 完成
常规     | oil-explore,                            | explore → plan → 👤确认
         | oil-plan,                               | → delegate → 实现 → code-review 
         | oil-delegate,                           | → govern
         | oil-code-review,                        |
         | oil-govern                              |
复杂     | oil-explore(分布),                      | explore(深度) → plan(完整)
         | oil-plan(完整),                         | → 👤确认 → delegate(分阶段)
         | oil-delegate(分阶段),                   | → 实现 → code-review(中间审查)
         | oil-code-review(多轮),                  | → bug-fix(问题修复)
         | oil-bug-fix,                            | → code-review(最终)
         | oil-govern                              | → govern
```

### Skill 选择规则

```python
def select_skills(change_type, project_rules):
    
    if change_type == SIMPLE:
        return [oil_explore]  # 快速模式，只读理解
    
    elif change_type == REGULAR:
        skills = [
            oil_explore,      # 理解代码
            oil_plan,         # 编写可读方案
            oil_delegate,     # 派发给 CLI agent
            oil_code_review,  # 审查 diff，检查 scope 漂移
            oil_govern        # 文档、分支管理、决策记录
        ]
        
        # 检查项目是否需要扩展或替代
        project_config = load_yaml('PROJECT-ADAPT.yaml')
        for skill in skills:
            custom_handling = project_config.get_skill_handling(skill)
            
            if custom_handling == 'replace':
                # 项目完全替代这个 skill
                skills[i] = get_project_custom_implementation(skill)
            elif custom_handling == 'supplement':
                # 在这个 skill 后添加项目的补充 skill
                pass  # 在工作流中插入补充 skill
        
        return skills
    
    elif change_type == COMPLEX:
        return [
            oil_explore,         # 分布式，多个 sub-agent
            oil_plan,            # 完整规格，多方案对比
            oil_delegate,        # 分阶段派发给多个 agent
            oil_code_review,     # 中间审查，检查 scope 漂移
            oil_bug_fix,         # 根因分析，系统扫描修复
            oil_code_review,     # 最终审查
            oil_govern           # 完整治理报告、分支清理
        ]
```

---

## ⚙️ 第 5 步：执行工作流

### 简单改动执行

```
1. 【skill-explore】理解任务 (1-2分钟)
2. 【实现改动】遵循四大原则 (5-10分钟)
3. 【快测】确保改动生效 (2-5分钟)
4. 【完成】更新进度文档
```

### 常规改动执行

```
1. 【skill-explore】理解项目和需求 (15-30分钟)
2. 【GitHub查证】(如需要，10-20分钟)
3. 【skill-plan】制定方案 (20-30分钟)
4. 👤 【等用户确认】
5. 【skill-delegate】分解任务 (10-15分钟)
6. 【实现】编写代码 (1-4小时)
7. 【快测】验证改动 (10-30分钟)
8. 【skill-code-review】代码审查 (15-30分钟)
9. 【skill-govern】决策记录 (5-10分钟)
10. 【完成】更新所有文档
```

### 复杂改造执行

```
1. 【skill-explore - 深度】深度分析系统 (1-2小时)
2. 【GitHub深度查证】查3-5个参考项目 (1-2小时)
3. 【skill-plan - 完整】完整设计文档 (2-4小时)
4. 【独立审查】由另一个Agent审查 (1-2小时)
5. 👤 【等用户确认】确认关键决策
6. 【skill-delegate - 分阶段】派发分阶段任务
7. 【分阶段迭代实现】
   - 实现阶段N
   - 中间测试
   - 中间审查
   - 有bug则修复
   - 进行下一阶段
8. 【skill-code-review - 最终】整体审查和集成测试
9. 【skill-govern】项目治理和决策记录
10. 【完成】更新所有文档
```

---

## 📝 第 6 步：记录决策

### 记录内容

```markdown
# 决策记录 - 实现用户导出功能

## 任务信息
- 时间：2026-11-22 10:00
- 改动类型：常规改动
- 参与的 Skills：explore → plan → delegate → code-review → govern

## 关键决策

### 决策 1：导出格式选择
**时间：** 2026-11-22 10:30
**选项：**
- A: CSV（简单）
- B: JSON（灵活）
- C: Excel（用户友好）

**用户选择：** C（Excel）
**理由：** 用户群体以非技术为主
**记录：** 在 skill-plan 阶段做的

### 决策 2：性能优化方案
**时间：** 2026-11-22 11:00
**冲突：** 项目规范说"Simplicity First"，但导出 100w 数据需要优化
**决策：** 允许在导出器中使用流式处理优化
**记录：** PRINCIPLES 中的例外

## 执行结果
- 代码行数：287 行
- 测试覆盖：95%
- Code Review 通过：✅
- 部署状态：已合并

## 相关链接
- PR：#123
- 相关 issue：#456
```

### 记录到哪里

```
docs/DECISIONS.md
  ├─ 按时间顺序记录
  ├─ 每个决策都有理由
  └─ 未来查证时的参考
```

---

## 🚨 异常处理

### 异常 1：规范冲突

```
如果在执行时发现规范有矛盾：

例如：
- 项目覆盖说"性能优先"
- 通用原则说"Simplicity First"
- 两个冲突

处理：
1. 记录这个冲突到 DECISIONS.md
2. 显示给用户："发现规范冲突，怎么处理？"
3. 更新 PROJECT-ADAPT.yaml
```

### 异常 2：Skill 冲突

```
如果有多个 skill 都可以处理这个任务：

例如：
- 通用 skill-code-review
- 项目自定义 skill-performance-review
- 两个都可用

处理：
1. 显示选项给用户
2. 询问："用哪个 skill？"
3. 记录用户的选择
4. 下次同样的场景推荐这个选择
```

### 异常 3：不确定改动类型

```
如果不确定是简单/常规/复杂：

处理：
1. 倾向于保守（选高一级）
2. 显示推理过程给用户
3. 询问："我判断这是常规，对吗？"
4. 等用户确认再执行
```

---

## ✅ 执行检查清单

```
【准备阶段】
- [ ] 判断了改动类型
- [ ] 加载了 PROJECT-ADAPT.yaml
- [ ] 合并了规范
- [ ] 选择了合适的 skills
- [ ] 没有规范冲突

【执行阶段】
- [ ] 按顺序调用了所有 skills
- [ ] 每个 skill 都验证了质量
- [ ] 在关键点等待了用户
- [ ] 记录了所有决策
- [ ] 没有遗漏任何步骤

【完成阶段】
- [ ] 所有代码都过了检查
- [ ] 所有决策都记录了
- [ ] 文档都更新了
- [ ] 更新了 HANDOVER.md
- [ ] 完成
```

---

## 🎯 决策优先级

```
1️⃣ 用户的显式指定
   "这是常规改动"
   → 遵循用户指定

2️⃣ 规范的明确约定
   "> 500 行代码 = 复杂"
   → 遵循规范

3️⃣ 项目的覆盖规则
   "这个项目：所有功能都是常规"
   → 遵循项目规则

4️⃣ AI 的判断
   "根据内容判断应该是常规"
   → AI 判断（但要确认）

5️⃣ 安全性考虑
   "不确定就选高一级"
   → 宁可保守
```

---

## 📊 执行后的产出

```
对于每个任务，应该有：

✅ 代码（实现）
✅ 测试（质量保证）
✅ 文档（使用说明）
✅ 决策记录（为什么这样做）
✅ HANDOVER.md 更新（下一个 AI 的接手点）
```
