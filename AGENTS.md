# AGENTS.md - vibcoding 规范库

本仓库是**文档库**，不是程序，也不会被其他项目自动加载。
人读入口：[README.md](README.md)。

给 AI 的定位：**这里是"怎么做"的规范；"这个项目是什么"在你自己项目的状态文档里。**

---

## 三块结构

| 块 | 放哪 | 谁维护 |
|---|---|---|
| 路由 + 红线 | 项目根目录 `AGENTS.md`（用 [templates/AGENTS.md](templates/AGENTS.md)） | 一次写好，很少动 |
| 规范（怎么做） | 本库 `coding/` 等 | 只维护这一份，所有项目共用 |
| 状态（项目是什么） | 项目 `docs/PROJECT-STATE.md` | 扫描自动生成，随时重跑 |

---

## 按任务路由

| 当你要…… | 读这个 | 不用读的情况 |
|---|---|---|
| 了解一个项目现状 | [prompts/PROJECT-SCAN.md](prompts/PROJECT-SCAN.md) | 只改一行文案 |
| 写代码、改代码 | [coding/PRINCIPLES.md](coding/PRINCIPLES.md) | 单行 typo |
| 判断能不能自己干、何时必须问人 | [coding/WORKFLOW.md](coding/WORKFLOW.md) | 已确定是绿灯小修 |
| 技术选型、架构、加依赖 | [coding/RESEARCH.md](coding/RESEARCH.md) | 用项目已有的库和模式 |
| 新项目 / 老项目接入 | [project-setup/GUIDE.md](project-setup/GUIDE.md) | 只想用编码原则 |
| 接 Skill（可选，任何实现） | [skills/README.md](skills/README.md) | 不装 Skill |
| 跨会话交接 | [templates/docs/HANDOVER.md](templates/docs/HANDOVER.md) | — |
| 改本库文档 | [CONTRIBUTING.md](CONTRIBUTING.md) | — |

**停止条件**：按任务读对应的**一份**就动手，不要通读全库；读完仍不确定，问用户。

---

## 遇到不一致时怎么分流

| 情况 | 去哪找答案 | 不要做 |
|---|---|---|
| 文档说的和代码做的不一样 | 看代码、测试、CI 配置 | 不要上外网找"标准做法" |
| 某个库/接口行为不确定 | 官方文档、变更日志 | 不要看博客就下结论 |
| 要选型 / 定架构 | `coding/RESEARCH.md` | 不要只看 star 数 |
| 规范和项目现状冲突 | 以项目现状为准，记录并报告 | 不要自行裁决后静默继续 |

---

## 全局红线

1. **不擅自扩大授权。** 同意方案 ≠ 同意合并主干、发布、改数据结构、删数据；这些逐个确认。
2. **不宣称未验证的完成。** 见 [coding/WORKFLOW.md](coding/WORKFLOW.md) 的验证要求。
3. **不超出被要求的范围。** 不顺手重构、不顺手改格式、不顺手加推测性抽象。
4. **不假设。** 不确定就问；推测必须标注。
5. **不伪造证据。** 没查过、没跑过、没读过的东西，不能写成"已确认"。

高风险目录（认证、支付、迁移、发布配置等）默认按最高风险处理，
直到项目在自己的 `AGENTS.md` 里明确写了规则。

---

## 在本仓库里工作时

- 纯文档库。改文档等于改规则：先说清改什么、影响哪些文件。
- **一个概念只有一个权威出处。** 发现同一规则写两处，删一处并留指针。
- 术语：风险分级用"绿灯 / 黄灯 / 红灯"；Skill 名称以实际安装的工具为准。
  不再使用 `specs/`、`vibcoding-skills/`、`Scale`、`L0`–`L4`、`PROJECT-ADAPT.yaml`。
- 不抄第三方工具的文档，只留入口。
- `archive/` 是重构前留档：不维护、不修正、不被在用文档引用。

改完运行：

```bash
python scripts/check_docs.py
```

---

## 扫描一个项目时

```bash
python scripts/scan_project.py --root <项目路径> --out <项目>/docs/PROJECT-FACTS.md
```

脚本只读，只采集客观事实（规模、清单、CI、git 状态、风险目录候选）。
结论由 [prompts/PROJECT-SCAN.md](prompts/PROJECT-SCAN.md) 按证据规则写出，
产物是 `docs/PROJECT-STATE.md`。**不执行构建、测试、安装。**

---

## 完成标准

- 需求范围内的行为已实现，未改动无关部分
- 快测通过；涉及合并/发布时门禁通过
- 受影响的文档只改了权威出处
- `python scripts/check_docs.py` 通过