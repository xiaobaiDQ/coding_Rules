# vibcoding - AI 开发协作约定

一套面向常规 Git 软件项目的轻量约定：**先理解再动手、最小实现、只改必需、以验证收尾。**

方法是跨技术栈通用的；目录结构、测试命令、合并方式必须按项目实际情况填写。它不替代项目自身规范，也不承诺适用于所有项目。

---

## 5 分钟开始

| 你想做什么 | 从这里开始 |
|---|---|
| 只用编码原则 | [coding/PRINCIPLES.md](coding/PRINCIPLES.md)（5 分钟读完） |
| 知道什么时候必须停下来问人 | [coding/WORKFLOW.md](coding/WORKFLOW.md) |
| 接入一个新项目或老项目 | [project-setup/GUIDE.md](project-setup/GUIDE.md) |
| 让 AI 摸清一个已有项目 | [prompts/PROJECT-SCAN.md](prompts/PROJECT-SCAN.md) |
| 选技术方案时怎么查证据 | [coding/RESEARCH.md](coding/RESEARCH.md) |
| 接 Agent Skill（可选，任意实现） | [skills/README.md](skills/README.md) |
| 给 AI 看的项目入口 | [templates/AGENTS.md](templates/AGENTS.md) |

只需要原则的人，读第一份就够，不必接入其余部分。

---

## 目录

```text
README.md                 定位、适用范围、入口
AGENTS.md                 给 AI 的导航入口（只做路由，不重复规则）
CONTRIBUTING.md           本库自身的维护规则

coding/
  PRINCIPLES.md           四条编码原则 + 例外条件
  WORKFLOW.md             风险分级、权限边界、验证分层
  RESEARCH.md             技术方案查证

project-setup/
  GUIDE.md                新项目 / 老项目接入步骤

prompts/
  PROJECT-SCAN.md         一句话让 AI 摸清项目、生成状态文档

skills/
  README.md               如何选择和使用 Agent Skill（不绑定实现）
  OIL-DEV-SKILLS.md       可选示例：我目前用的一套（换掉不影响规范）

templates/
  AGENTS.md               项目级 AGENTS.md 模板（路由 + 边界 + 命令）
  docs/PROJECT-STATE.md   项目状态模板（扫描产物，自动生成）
  docs/HANDOVER.md        精简交接模板

scripts/
  check_docs.py           本库文档自检（链接、术语、重复章节）
  scan_project.py         只读采集项目事实（规模、清单、CI、git 状态）

archive/                  重构前的旧文档，仅作追溯，不再维护
```

---

## 四条原则（摘要，权威说明在 coding/PRINCIPLES.md）

1. **Think Before Coding** — 不假设，不隐瞒困惑，把权衡说清楚。
2. **Simplicity First** — 能解决问题的最小实现，拒绝推测性设计。
3. **Surgical Changes** — 只改必需，只清理自己造成的问题。
4. **Goal-Driven Execution** — 先定义成功标准和验证方式，再动手。

---

## 适用范围

**适合：**

- 有 Git 版本控制、能跑自动化测试的软件项目
- 人在环路中、由 AI 辅助或主导编码的协作方式
- 希望统一"什么时候可以自己改、什么时候必须停下来确认"的团队

**需要额外适配，不能直接套用：**

- 无版本控制、无自动化测试的项目
- 强监管、安全关键、医疗/金融等需专门流程的领域
- 离线或内网环境（无法访问外部文档与包源）
- 非 Git 的版本控制、非分支式的发布流程

**不适用：**

- 无人监督的自动合并、自动发布
- 需要凭本库替代行业合规流程的场景

---

## 本库明确不承诺的事

- 不承诺"适用于任何项目"，也不替代项目自身的架构与安全评审。
- 不定义任何机器可读的配置文件格式（没有 `PROJECT-ADAPT.yaml` 之类的协议）。
  项目约定统一写在项目自己的 `AGENTS.md` 里，人读即可执行。
- 不绑定任何 Skill 实现。不装 Skill，整套规范照样完整可用。
- 不内置脚本化的强制门禁。本库只提供文档自检和只读扫描脚本；分支保护、CI、hooks
  需要各项目按自己的平台自行配置。
- 不重复抄写第三方工具的文档，只给入口。

---

## 维护

文档一致性由 `python scripts/check_docs.py` 检查；扫描项目时用
`python scripts/scan_project.py`（只读）。改规则前请先读
[CONTRIBUTING.md](CONTRIBUTING.md)：**一个概念只有一个权威出处。**