# vibcoding - 通用 AI 开发规范体系

**一套通用的编码、工作流、文档和 Scale 管理规范，可应用于任何项目。**

---

## 🎯 核心功能板块

vibcoding 由四个功能板块组成，每个板块独立但协作：

### 1️⃣ 编码规范（Coding Standards）

```
coding/
├─ PRINCIPLES.md              Karpathy四原则 + 4条深化规则
├─ WORKFLOW.md                简单改动/常规改动/复杂改造工作流 + AI自主性范围
└─ GITHUB-RESEARCH.md         技术方案查证指南
```

**核心价值：** 统一的编码哲学和工作流，对所有项目都适用，完全脱离技术栈

---

### 2️⃣ 文档管理（Documentation）

```
documentation/
└─ DOCS-EXTRACTION-GUIDE.md   从现有项目提取和组织文档
```

**核心价值：** 新项目接手时，快速整理现有文档，建立新的知识库

---

### 3️⃣ Scale 管理（Skills Management）

```
skills/
├─ OIL-DEV-SKILLS-CHECKLIST.md           通用 Scale 完整清单
├─ OIL-DEV-SKILLS-EXTENSION.md           在通用 Scale 基础上扩展
├─ PROJECT-CUSTOM-SKILLS-STRATEGY.md     创建项目专属 Scale
├─ SKILLS-GUIDE.md                       Scale 管理总入口
└─ SKILLS-INTEGRATION.md                 Scale 体系总览
```

**核心价值：** 
- 通用 Scale：6个基础 Scale（oil-explore, oil-plan 等），所有项目都可用
- 项目专属 Scale：项目自己维护，扩展通用能力
- 分层清晰，避免重复维护

---

### 4️⃣ 项目适配（Project Adaptation）

```
project-adapt/
├─ PROJECT-ADAPT-STRATEGY.md   把通用规范适配到具体项目
└─ AI-EXECUTION-GUIDE.md        AI 执行的决策树和验证机制
```

**核心价值：** 新项目初始化时，自动识别和解决通用规范与项目现状的冲突

---

## 🚀 快速开始

### 场景 1：我只有 5 分钟（新人快速上手）

```
读 QUICK-START-5MIN.md（约 5 分钟）

✅ 足够开始工作
```

### 场景 2：我是 AI，刚接手项目（15 分钟）

```
1. 读 QUICK-START-5MIN.md          了解核心概念 (5分钟)
2. 读项目的 AGENTS.md              了解项目配置 (5分钟)
3. 读项目的 PROJECT-ADAPT.yaml     了解规范覆盖 (5分钟)

✅ 准备好开始工作
```

### 场景 2：我要启动新项目

```
1. 读 coding/PRINCIPLES.md + coding/WORKFLOW.md
   了解通用规范

2. 读 skills/OIL-DEV-SKILLS-CHECKLIST.md
   选择项目需要的 Scale

3. 读 project-adapt/PROJECT-ADAPT-STRATEGY.md
   识别和解决规范冲突

4. 生成 PROJECT-ADAPT.yaml + AGENTS.md
   配置项目

✅ 项目启动完成
```

### 场景 3：我要接手已开发的项目

```
1. 读 documentation/DOCS-EXTRACTION-GUIDE.md
   提取现有文档

2. 识别现有规范和编码风格
   
3. 读 project-adapt/PROJECT-ADAPT-STRATEGY.md
   把它们融入通用规范

4. 更新 PROJECT-ADAPT.yaml
   
5. 重新组织 docs/
   建立新的知识库

✅ 知识库组织完成
```

### 场景 4：项目需要特殊 Scale

```
1. 读 skills/OIL-DEV-SKILLS-CHECKLIST.md
   确认通用 Scale 不够

2. 选择方式：
   - 扩展？读 skills/OIL-DEV-SKILLS-EXTENSION.md
   - 创建项目 Scale？读 skills/PROJECT-CUSTOM-SKILLS-STRATEGY.md

3. 更新 PROJECT-ADAPT.yaml
   配置新的 Scale

✅ Scale 配置完成
```

---

## 📂 完整文档导航

### 【必读】核心文档

| 文档 | 内容 | 适用 | 更新 |
|------|------|------|------|
| **QUICK-START-5MIN.md** ⭐ | 5分钟快速参考卡 | 所有人首先读这个 | 本轮更新 |
| **coding/PRINCIPLES.md** | Karpathy四原则 + 4条深化规则 | 所有项目 | 本轮更新 |
| **coding/WORKFLOW.md** | L1/L2/L3 工作流 + AI自主性 | 所有项目 | 本轮更新 |

### 【参考】规范库

| 文档 | 内容 | 阶段 | 更新 |
|------|------|------|------|
| **CHECKLIST-UNIFIED.md** ⭐ | 所有检查清单的中央索引 | 任何时候 | 本轮新增 |
| **DOC-MAINTENANCE-GUIDE.md** | 文档维护指南（规范改动时读） | 维护规范时 | 本轮新增 |
| **project-adapt/AI-EXECUTION-GUIDE.md** | AI 执行决策树 | 执行工作时 | 本轮更新 |
| **project-adapt/PROJECT-ADAPT-STRATEGY.md** | 项目适配策略 | 项目初始化时 | 本轮更新 |
| **skills/OIL-DEV-SKILLS-CHECKLIST.md** | 通用 Skill 清单 | 项目初始化时 | 本轮更新 |
| **skills/SKILLS-INTEGRATION.md** | Skill 与工作流的关系 | 理解 Skill 结构时 | 本轮更新 |
| **coding/GITHUB-RESEARCH.md** | 技术方案查证指南 | 需要技术决策时 | - |

### 【导航】文档分类总表

#### 【L0】最小启动
```
📄 QUICK-START-5MIN.md
📄 项目的 AGENTS.md
📄 项目的 PROJECT-ADAPT.yaml
```

#### 【L1】核心规范
```
📄 coding/PRINCIPLES.md
📄 coding/WORKFLOW.md
```

#### 【L2】应用框架
```
📄 coding/GITHUB-RESEARCH.md
📄 skills/OIL-DEV-SKILLS-CHECKLIST.md

📄 project-adapt/PROJECT-ADAPT-STRATEGY.md
📄 project-adapt/AI-EXECUTION-GUIDE.md
```

#### 【L3】扩展深化
```
📄 skills/OIL-DEV-SKILLS-EXTENSION.md
📄 skills/PROJECT-CUSTOM-SKILLS-STRATEGY.md
📄 project-adapt/DOCS-EXTRACTION-GUIDE.md
```

#### 【L4】项目专有
```
📄 你的项目/AGENTS.md
📄 你的项目/PROJECT-ADAPT.yaml
📄 你的项目/docs/HANDOVER.md
📄 你的项目/skills/*/SKILL.md
```

#### 【工具】维护和参考
```
📄 CHECKLIST-UNIFIED.md         ← 所有检查清单的中央索引 ⭐ 本轮新增
📄 DOC-MAINTENANCE-GUIDE.md     ← 文档维护指南 ⭐ 本轮新增
📄 FRAMEWORK-HIERARCHY.md       ← 分级结构说明
📄 AGENTS.md                    ← 文档导航和快速查询
```

---

## 🔄 工作流概览

```
接到需求
  ↓
【编码规范】coding/ 决定怎么做
  ↓
【项目适配】project-adapt/ 检查是否符合项目规范
  ↓
【Scale管理】skills/ 选择合适的 Scale
  ↓
执行工作
  ↓
【文档管理】documentation/ 更新和组织文档
```

---

## 🎓 核心设计原则

### 1. 完全通用

- 不依赖特定技术栈
- 不依赖特定项目规模
- 不依赖特定工作流程
- 适用于后端、前端、AI、基础设施、数据等

### 2. 功能独立，协作清晰

每个板块可以独立使用，但一起使用时功能完整：
- 只用编码规范？可以
- 只管理 Scale？可以
- 全套使用？更好

### 3. 最小化重复维护

- 通用规范 vibcoding 维护
- 项目配置项目维护
- 项目 Scale 项目维护
- 避免多个地方维护同一个规范

### 4. Scale 分层清晰

- 通用 Scale = 多个项目都能用的基础能力
- 项目 Scale = 项目自己的特殊需求
- 明确界限，避免混乱

---

## 📌 约定

### 文档位置

```
vibcoding-rules/     规范库（通用）
  ├─ coding/         编码规范（通用）
  ├─ documentation/  文档管理（通用）
  ├─ skills/         Scale 库（通用）
  ├─ project-adapt/  适配框架（通用）
  └─ templates/      项目模板（通用）

your-project/        你的项目（项目专属）
  ├─ AGENTS.md       项目配置
  ├─ PROJECT-ADAPT.yaml
  ├─ skills/         项目 Scale（如果有）
  └─ docs/
     ├─ HANDOVER.md
     ├─ DECISIONS.md
     └─ ...
```

### 维护权限

```
vibcoding-rules/     → vibcoding 团队维护
your-project/        → 项目团队维护
```

### 文件命名

```
功能描述.md           通用规范、指南
PROJECT-ADAPT.yaml   项目配置（YAML）
AGENTS.md            项目级配置（Markdown）
HANDOVER.md          交接文档
```

---

## ✅ 现在你拥有

```
✅ 通用编码规范       对所有项目都适用
✅ 文档管理指南       快速整理现有文档和建立知识库
✅ Scale 管理系统     通用 Scale + 项目专属 Scale
✅ 项目适配框架       新项目初始化和老项目迁移
✅ AI 执行指南        AI 自动决策和验证机制

结果：
   一个完整、通用、可扩展的 AI 开发规范体系
```

---

## 🚀 下一步

- **新项目？** 看场景2：我要启动新项目
- **接手项目？** 看场景3：我要接手已开发的项目
- **需要查詢？** 看 AGENTS.md 的快速导航
