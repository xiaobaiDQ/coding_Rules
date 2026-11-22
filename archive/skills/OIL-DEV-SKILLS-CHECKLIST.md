# OIL-DEV-SKILLS-CHECKLIST.md - 通用 Skill 清单

**对象：** 项目初始化时的配置检查

**目的：** 明确有哪些通用 Skill，它们的能力范围，以及项目应该如何配置

---

## 🎯 通用 Skill 库概览

通用 Skill 库由 **oil-dev-skills**（油油团队维护）提供。共 **6 个核心 Skill**，覆盖整个开发工作流。

每个 Skill 都是生产级的，经过多个真实项目验证。

---

## 📋 Skill 清单 - 重新分类

### Skill 的四个等级

在重新定义 Skill 前，明确四个等级：

| 等级 | 定义 | 表示 | 是否必须配置 |
|------|------|------|-----------|
| **Mandatory** | 缺少它 AI 无法工作 | ✅ | 是 |
| **Hard Dependency** | 某种工作流必须有，缺少会出问题 | ⚠️ | 看工作流 |
| **Nice to Have** | 不影响工作但增强能力 | 💡 | 否 |
| **Domain-Specific** | 只在特定项目类型需要 | 🎯 | 看项目 |

---

### 1️⃣ oil-explore

**能力：** 理解项目和代码

**具体功能：**
- 扫描和分析项目结构
- 理解代码库的技术栈、架构、依赖关系
- 生成项目理解报告
- 识别关键模块和数据流

**使用场景：**
- 新 AI 接手项目时（第一步）
- 需要理解陌生代码库时
- 评估改动影响时

**配置方式：**
```yaml
skills:
  oil-explore:
    enabled: true
    priority: "critical"  # 必需
    triggers:
      - new-project
      - code-understanding
```

**验证方法：**
```bash
# AI 应该能够：
- [ ] 读懂 README / 项目文档
- [ ] 分析 package.json / build config
- [ ] 理解项目目录结构
- [ ] 识别核心模块和依赖
```

**必需性：** ✅ **Mandatory** - 所有项目都必须配置

**理由：** 没有项目理解，AI 无法做任何工作

---

### 2️⃣ oil-plan

**能力：** 制定方案和设计

**具体功能：**
- 分析需求和目标
- 制定技术方案
- 评估方案的风险和影响
- 制定实施计划和优先级

**使用场景：**
- 常规改动以上（需要方案确认）
- 复杂功能开发
- 架构改造
- 技术选型

**配置方式：**
```yaml
skills:
  oil-plan:
    enabled: true
    priority: "high"  # 常规改动+ 时必需
    triggers:
      - before-implementation
      - design-required
```

**验证方法：**
```bash
# AI 应该能够：
- [ ] 理解需求背景
- [ ] 提出多个可行方案
- [ ] 分析每个方案的 pro/con
- [ ] 给出推荐方案和理由
```

**必需性：** ⚠️ **Hard Dependency** - 常规改动及以上必须有

**触发条件：**
```
如果项目会做常规改动+ → 必须配置
如果项目只做简单改动 → 不需要
如果不确定 → 应该配置（保守起见）
```

---

### 3️⃣ oil-delegate

**能力：** 派发任务和分配

**具体功能：**
- 将复杂任务分解为可执行的子任务
- 确定执行顺序和依赖关系
- 生成任务清单和进度跟踪
- 分配资源和优先级

**使用场景：**
- 大型功能拆分执行
- 多模块协调
- 长期项目管理
- L3 工作流中必需

**配置方式：**
```yaml
skills:
  oil-delegate:
    enabled: true
    priority: "medium"
    triggers:
      - task-decomposition
      - project-planning
```

**验证方法：**
```bash
# AI 应该能够：
- [ ] 拆分大任务为多个子任务
- [ ] 识别任务之间的依赖
- [ ] 确定合理的执行顺序
- [ ] 分配优先级
```

**必需性：** 
- ✅ L3 工作流：**Mandatory**
- 💡 L2 工作流：**Nice to Have**
- ❌ L1 工作流：不需要

---

### 4️⃣ oil-code-review

**能力：** 代码审查

**具体功能：**
- 检查代码质量和最佳实践
- 识别 bug、性能问题、安全隐患
- 验证是否遵循项目规范
- 提出改进建议

**使用场景：**
- 代码生成后审查
- Pull Request 审查
- 性能优化
- 安全加固

**配置方式：**
```yaml
skills:
  oil-code-review:
    enabled: true
    priority: "critical"  # 建议启用
    triggers:
      - after-implementation
      - code-quality-check
      - before-merge
```

**验证方法：**
```bash
# AI 应该能够：
- [ ] 识别常见的代码问题
- [ ] 检查代码是否遵循规范
- [ ] 发现性能或安全隐患
- [ ] 给出具体的改进建议
```

**必需性：** ⚠️ **Hard Dependency** - L2 及以上工作流强烈推荐

**理由：** L2+ 改动影响范围大，必须有审查。L1 可选但强烈建议

---

### 5️⃣ oil-bug-fix

**能力：** Bug 修复和根因分析

**具体功能：**
- 重现故障
- 追踪根本原因
- 提出修复方案
- 验证修复效果

**使用场景：**
- 线上 bug 修复
- 测试阶段问题排查
- 性能问题诊断
- 未知原因的故障

**配置方式：**
```yaml
skills:
  oil-bug-fix:
    enabled: true
    priority: "high"
    triggers:
      - bug-investigation
      - root-cause-analysis
      - critical-incident
```

**验证方法：**
```bash
# AI 应该能够：
- [ ] 重现问题
- [ ] 追踪问题来源
- [ ] 分析根本原因
- [ ] 提出修复方案
- [ ] 验证修复
```

**必需性：** 💡 **Nice to Have** - 需要时启用

**触发场景：**
```
如果项目处于维护阶段（主要在修bug）→ 推荐启用
如果项目处于开发阶段（主要在新增功能）→ 可以关闭
如果遇到根因不明的bug → 临时启用这个Skill
```

---

### 6️⃣ oil-govern

**能力：** 项目治理

**具体功能：**
- 检查项目规范和标准遵循情况
- 验证代码库健康度
- 生成质量报告
- 推荐改进措施

**使用场景：**
- 定期代码库审计
- 技术债务清理
- 规范遵循检查
- 项目健康评分

**配置方式：**
```yaml
skills:
  oil-govern:
    enabled: true
    priority: "medium"
    triggers:
      - audit
      - quality-check
      - governance-review
```

**验证方法：**
```bash
# AI 应该能够：
- [ ] 评估代码库健康度
- [ ] 识别技术债务
- [ ] 检查规范�遵循
- [ ] 生成改进建议
```

**必需性：** 🎯 **Domain-Specific** - 高成熟度项目推荐

**使用场景：**
```
如果项目是"新项目"或"快速迭代" → 不需要
如果项目是"成熟产品"或"长期维护" → 推荐启用
如果想定期做质量审计 → 启用
```

---

## ✅ 项目初始化 Skill 检查清单 - 按项目类型

### 场景 1：L1 专用项目（只做小改动、typo、文档更新等）

```
✅ 必需
   - oil-explore

❌ 不需要（本项目永远不会用到）
   - oil-plan
   - oil-code-review
   - oil-delegate
   - oil-bug-fix
   - oil-govern
```

**配置方式：**
```yaml
# PROJECT-ADAPT.yaml
project: "my-project"
tech-stack: "..."

skills:
  mandatory:
    - oil-explore
  
  config:
    oil-explore:
      scope: "full"
```

---

### 场景 2：L1 + L2 项目（常规开发，定期做新功能和改进）

```
✅ 必需
   - oil-explore      (理解代码)
   - oil-plan         (L2工作需要方案)
   - oil-code-review  (代码质量控制)

⚠️ 推荐
   - oil-bug-fix      (可能遇到bug)

❌ 可以暂时关闭
   - oil-delegate     (小项目通常不需要）
   - oil-govern       (定期才需要，不是每天用)
```

**配置方式：**
```yaml
# PROJECT-ADAPT.yaml
project: "my-project"
tech-stack: "Node.js / React / PostgreSQL"

skills:
  mandatory:
    - oil-explore
    - oil-plan
    - oil-code-review
  
  recommended:
    - oil-bug-fix
  
  optional:
    - oil-delegate
    - oil-govern
  
  config:
    oil-explore:
      scope: "full"
      output: "understanding-report.md"
    
    oil-plan:
      approach: "collaborative"
      decision-required: true
    
    oil-code-review:
      rules: "vibcoding"
      strictness: "high"
    
    oil-bug-fix:
      approach: "root-cause"
```

---

### 场景 3：L1 + L2 + L3 项目（复杂系统，需要深度设计和分阶段执行）

```
✅ 全部启用
   - oil-explore      (深度理解)
   - oil-plan         (完整设计)
   - oil-code-review  (多轮审查)
   - oil-delegate     (分阶段派发)
   - oil-bug-fix      (问题修复)
   - oil-govern       (治理报告)
```

**配置方式：**
```yaml
# PROJECT-ADAPT.yaml
project: "my-project"
tech-stack: "..."

skills:
  all: enabled
  
  config:
    oil-explore:
      scope: "full"
      depth: "deep"  # L3要求深度
    
    oil-plan:
      approach: "comprehensive"  # 完整设计
      multi-solution: true
      decision-required: true
    
    oil-delegate:
      enable_phased: true  # 支持分阶段
      parallel_capable: true
    
    oil-code-review:
      rules: "vibcoding"
      rounds: "multiple"  # 多轮审查
    
    oil-bug-fix:
      approach: "root-cause"
      system-scan: true
    
    oil-govern:
      report_level: "comprehensive"  # 完整报告
```

---

### 场景 4：维护阶段项目（主要在修bug、优化、维护）

```
✅ 启用这些
   - oil-explore      (理解现有代码)
   - oil-code-review  (质量把关)
   - oil-bug-fix      (bug修复)
   - oil-govern       (定期审计)

⚠️ 有需要时启用
   - oil-plan         (有功能时需要)

❌ 通常不需要
   - oil-delegate     (改动通常较小)
```

**配置方式：**
```yaml
# PROJECT-ADAPT.yaml
project: "legacy-project"
tech-stack: "..."

skills:
  mandatory:
    - oil-explore
    - oil-code-review
    - oil-bug-fix
  
  scheduled:
    - oil-govern       # 定期运行，比如每月
  
  conditional:
    - oil-plan         # 只在有新功能时启用
```

---

## 🔍 Skill 配置验证流程

当 AI 第一次接手项目时，应该运行这个检查流程：

### 步骤 1：加载 PROJECT-ADAPT.yaml
```
检查文件是否存在
检查 skills 配置是否完整
识别缺失的 required Skill
```

### 步骤 2：对比通用 Skill 清单
```
遍历所有 6 个通用 Skill
确认项目配置了哪些
识别"应该有但没配"的 Skill
```

### 步骤 3：生成检查报告
```
✅ 已配置的 Skill
⚠️ 推荐但未配置的 Skill
❌ 缺失的必需 Skill（需要用户决策）
```

### 步骤 4：提醒用户
```
如果有缺失的 Skill：
  → 显示检查报告
  → 解释为什么需要这个 Skill
  → 提示用户在 PROJECT-ADAPT.yaml 中添加
  → 等待用户确认
```

---

## 📋 Skill 配置模板

### 最小 PROJECT-ADAPT.yaml
```yaml
project: "my-project"
tech-stack: "Node.js / React / PostgreSQL"

skills:
  required:
    - oil-explore
  recommended:
    - oil-code-review
  
  config:
    oil-explore:
      scope: "full"  # or "partial" for specific modules
    oil-code-review:
      rules: "vibcoding"  # 使用 vibcoding 规范
```

### 标准 PROJECT-ADAPT.yaml
```yaml
project: "my-project"
tech-stack: "Node.js / React / PostgreSQL"

skills:
  required:
    - oil-explore
    - oil-plan
    - oil-code-review
    - oil-bug-fix
  
  optional:
    - oil-delegate
    - oil-govern
  
  custom:
    # 项目专有的 Skill
    - skill-sql-review
    - skill-performance-audit
  
  config:
    oil-explore:
      scope: "full"
      output: "understanding-report.md"
    
    oil-plan:
      approach: "collaborative"  # or "autonomous"
      decision-required: true    # 需要用户确认方案
    
    oil-code-review:
      rules: "vibcoding"
      strictness: "high"
      checks:
        - performance
        - security
        - best-practices
    
    oil-bug-fix:
      approach: "root-cause"
    
    custom:
      skill-sql-review:
        trigger: "before-merge"
        supplement_to: "oil-code-review"
```

---

## 🎯 Skill 缺失处理流程

### 场景 1：缺失必需 Skill

```
AI 检查：发现缺少 oil-plan
  ↓
提示用户：
  "项目配置缺少 oil-plan Skill。
   L2 以上工作需要方案设计。
   
   是否添加？(Y/N)"
  ↓
用户确认
  ↓
AI 更新 PROJECT-ADAPT.yaml
  ↓
继续工作
```

### 场景 2：缺失推荐 Skill

```
AI 检查：发现缺少 oil-delegate
  ↓
提示用户：
  "建议启用 oil-delegate Skill。
   如果需要分解大任务，会很有用。
   
   是否添加？(Y/N)"
  ↓
用户选择
  ↓
继续工作
```

### 场景 3：首次启用项目

```
AI 第一次接手项目
  ↓
加载 PROJECT-ADAPT.yaml
  ↓
运行 Skill 验证检查
  ↓
显示检查报告
  ↓
"🔍 Skill 初始化检查完成
   
   ✅ 已配置：oil-explore, oil-code-review
   ⚠️ 推荐：oil-plan, oil-bug-fix
   ❌ 缺失必需：（无）
   
   是否按推荐配置补齐？(Y/N)"
  ↓
继续工作
```

---

## 🔄 定期 Skill 审视流程

每月或每个季度，AI 应该运行一次 Skill 审视：

```
1. 检查已配置的 Skill 是否都被用到了
2. 识别"配置了但没用过"的 Skill
3. 识别"经常用到但没配置"的场景
4. 提出改进建议
5. 更新 PROJECT-ADAPT.yaml
```

---

## 📌 最佳实践

```
✅ DO

1. 项目初始化时立即运行 Skill 检查
   - 不要等到需要时才配置
   - 提前识别缺失

2. 根据项目类型选择配置
   - L1 只做小改动：最小配置
   - L2 常规开发：标准配置
   - L3 复杂改造：完整配置

3. 定期审视和更新
   - 随着项目演进，Skill 需求可能变化
   - 每月检查一次

4. 记录配置决策
   - 在 docs/DECISIONS.md 中记录
   - 为什么选择这个配置


❌ DON'T

1. 不要一次启用所有 Skill
   - 过度配置会增加复杂度
   - 只启用项目实际需要的

2. 不要忽略检查报告
   - 如果缺少必需 Skill，会影响工作
   - 及时补齐

3. 不要在中途改变 Skill 配置
   - 应该在项目初始化时确定
   - 中途改变会导致工作流混乱
   - 确实需要改时，要更新文档和通知所有人
```

---

## 🎯 下一步

1. **新项目初始化？** 
   - 看"项目初始化 Skill 检查清单"部分
   - 选择合适的配置（最小/标准/完整）
   - 在 PROJECT-ADAPT.yaml 中填入

2. **需要验证 Skill 配置？**
   - 看"Skill 配置验证流程"部分
   - 运行检查清单

3. **想了解某个 Skill？**
   - 在上面的清单中找到它
   - 了解能力、使用场景、配置方式

---

**现在你拥有了完整的 Skill 配置和验证体系！** 🎉
