# DOC-MAINTENANCE-GUIDE.md - 文档维护指南

**当改动规范时，需要同步更新的所有地方。**

---

## 核心原则

```
规范 = 多份文档的集合
一份改动 → 需要同步多个地方

目标：最小化维护负担，最大化一致性
```

---

## 规范改动清单

### 情况 1：修改简单改动/常规改动/复杂改造的定义或条件

**改什么：** 比如"简单改动不能改 API"这个条件

**需要同步：**
```
1. coding/WORKFLOW.md
   - 更新"决策树：判断改动类型"部分
   - 更新简单改动/常规改动/复杂改造的具体流程描述

2. project-adapt/AI-EXECUTION-GUIDE.md
   - 更新"第 1 步：识别改动类型"
   - 更新决策标准中的所有条件

3. QUICK-START-5MIN.md
   - 更新"判断改动类型"部分
   - 更新检查清单

4. skills/SKILLS-INTEGRATION.md
   - 更新"Skill 在工作流中的位置"
   - 更新验证清单（如果涉及Skill的触发条件）

5. docs/DECISIONS.md（项目级）
   - 记录为什么改了这个定义
```

**验证：** 在所有 5 个地方都搜索相关术语，确保一致

---

### 情况 2：增加或修改编码原则

**改什么：** 比如在 Simplicity First 下新增一条深化规则

**需要同步：**
```
1. coding/PRINCIPLES.md
   - 在原则下新增规则
   - 加详细说明和示例

2. coding/WORKFLOW.md
   - 如果新规则影响工作流，更新流程

3. QUICK-START-5MIN.md
   - 如果新规则重要到 5 分钟参考要提，就加进去

4. project-adapt/PROJECT-ADAPT-STRATEGY.md
   - 如果新规则可以被项目覆盖，更新覆盖清单

5. docs/DECISIONS.md
   - 记录新增规则的理由
```

**验证：** 新规则在所有涉及的文件中都被提及，且说法一致

---

### 情况 3：增加或修改 Skill

**改什么：** 比如新增一个 oil-awesome Skill

**需要同步：**
```
1. skills/OIL-DEV-SKILLS-CHECKLIST.md
   - 在清单中新增 oil-awesome
   - 写能力、使用场景、必需性、配置方式、验证方法

2. skills/SKILLS-INTEGRATION.md
   - 在 Skill 在工作流中的位置中更新矩阵
   - 更新简单改动/常规改动/复杂改造对应的 Skill 组合

3. project-adapt/AI-EXECUTION-GUIDE.md
   - 更新"第 4 步：选择合适的 Skill"中的选择矩阵

4. FRAMEWORK-HIERARCHY.md
   - 如果新Skill改变了学习路径，更新分级

5. QUICK-START-5MIN.md
   - 如果新Skill影响快速参考，更新

6. templates/AGENTS.md
   - 更新项目配置模板，包含新Skill
```

**验证：** 在工作流矩阵中确认新Skill出现在正确的级别，所有引用一致

---

### 情况 4：修改 Skills 的"必需"级别

**改什么：** 比如"oil-code-review"从"强烈推荐"改成"必需"

**需要同步：**
```
1. skills/OIL-DEV-SKILLS-CHECKLIST.md
   - 更新该Skill的必需性说明

2. skills/SKILLS-INTEGRATION.md
   - 更新所有工作流中的验证清单
   - 如果改成必需，要加到所有等级的必需列表

3. project-adapt/AI-EXECUTION-GUIDE.md
   - 更新"第 2.5 步：验证 Skill 配置"的检查逻辑

4. 项目的 PROJECT-ADAPT.yaml
   - 现有项目可能需要更新Skill配置
   - 记录到 DECISIONS.md

5. QUICK-START-5MIN.md
   - 更新"Skills 配置"部分
```

**验证：** 在验证清单中确认新的必需Skill被正确地检查

---

### 情况 5：增加或修改检查清单项

**改什么：** 比如在简单改动检查清单中新增一项

**需要同步：**
```
1. coding/WORKFLOW.md / project-adapt/AI-EXECUTION-GUIDE.md / QUICK-START-5MIN.md
   - 找到检查清单所在的文件
   - 添加新项

2. 相关的流程描述
   - 如果新项涉及新流程，更新对应步骤说明

3. docs/DECISIONS.md
   - 记录为什么加了这一项
```

**验证：** 新项被所有涉及的文档都包含

---

## 文档位置索引 - 快速查找

### 规范性文档（通用，所有项目都读）

| 内容 | 位置 | 修改频率 |
|------|------|--------|
| 四大编码原则 | `coding/PRINCIPLES.md` | 低（核心稳定） |
| 简单改动/常规改动/复杂改造工作流 | `coding/WORKFLOW.md` | 低（框架稳定） |
| 技术方案查证 | `coding/GITHUB-RESEARCH.md` | 低 |
| Skill 清单 | `skills/OIL-DEV-SKILLS-CHECKLIST.md` | 中（增加Skill时改） |
| Skill 集成 | `skills/SKILLS-INTEGRATION.md` | 中（工作流更新时改） |
| AI 执行指南 | `project-adapt/AI-EXECUTION-GUIDE.md` | 中（工作流更新时改） |
| 项目适配策略 | `project-adapt/PROJECT-ADAPT-STRATEGY.md` | 低 |

### 适配文档（项目级，每个项目不同）

| 内容 | 位置 | 修改频率 |
|------|------|--------|
| 项目适配配置 | `PROJECT-ADAPT.yaml` | 高（项目启动时） |
| 项目级配置 | `AGENTS.md` | 中（需求变化时） |
| 决策记录 | `docs/DECISIONS.md` | 高（每个任务都记） |
| 进度记录 | `docs/progress.md` | 高（每次完成都更新） |

### 参考文档

| 内容 | 位置 | 修改频率 |
|------|------|--------|
| 快速参考卡 | `QUICK-START-5MIN.md` | 低（核心稳定） |
| 分级结构 | `FRAMEWORK-HIERARCHY.md` | 低（框架稳定） |
| 文档维护指南 | `DOC-MAINTENANCE-GUIDE.md` | 低（这个文件） |

---

## 修改流程（规范库维护者）

**每次修改规范时：**

```
1. 明确你要改什么
   - 是L1/L2/L3定义吗？
   - 是编码原则吗？
   - 是Skill吗？
   - 是检查清单吗？

2. 查上面的"情况 X"
   - 找到对应的修改场景
   - 看需要同步哪些文件

3. 在所有需要的文件中进行修改
   - 保持说法一致
   - 相同的概念用相同的词

4. 验证一致性
   - 搜索关键词，确保所有地方都改了
   - 检查新旧版本有无矛盾

5. 更新 docs/DECISIONS.md
   - 记录这次规范改动
   - 说明原因和影响范围

6. 通知所有项目
   - 如果改动影响现有项目，要通知
   - 建议在下次项目启动时更新
```

---

## 最小化维护成本的建议

### 现在能做的

✅ 创建规范改动的检查清单（已做，就是这个文件）
✅ 统一术语（已做，全文统一用"oil-explore"而不是混用昵称）
✅ 在每个文档顶部注明"如果改了这个，还要改哪些"

### 长期可以做的

🔮 生成式文档：从单一源文档生成多份输出
  - 比如 L1/L2/L3 的定义只在一个地方写
  - 其他文档自动引用生成
  
🔮 自动验证：写个脚本检查一致性
  - 搜索所有文件中的关键词
  - 确保没有遗漏或矛盾

🔮 版本管理：给规范添加版本号
  - 比如 vibcoding v1.1 → v1.2
  - 文档和代码都能追踪规范版本

---

## 检查清单 - 修改规范后要验证

修改完成后，运行这个检查清单：

```
[ ] 我在情况 1-5 中找到了对应场景
[ ] 我在所有需要的文件中都进行了修改
[ ] 我用搜索工具验证了关键词都被更新了
[ ] 我检查了新旧说法有无矛盾
[ ] 我在 docs/DECISIONS.md 中记录了这次改动
[ ] 我通知了所有相关的项目（如果有）
```

---

**目标：** 通过明确的维护指南，降低规范维护的成本，提高一致性。
