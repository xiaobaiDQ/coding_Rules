# archive/ - 重构前留档

**归档日期：** 2026-11-22

**原因：** 重构前这一套文档存在死链、同一规则重复多份、术语混用（`specs/`、`Skill/Scale`、
`L1/L2/L3`）、以及一套没有实现也无法执行的配置协议（`PROJECT-ADAPT.yaml`）。
直接修补会制造第三套版本，因此整体归档，只把仍然有效的内容迁到新结构。

**状态：** 只作追溯，不维护、不修正、不被在用文档引用。其中的旧路径和旧术语不要照抄。

---

## 对应关系

| 归档文件 | 现在去哪看 |
|---|---|
| `AGENTS.old.md` | `AGENTS.md`（重写为导航入口） |
| `README.old.md` | `README.md`（重写定位与适用范围） |
| `FRAMEWORK-HIERARCHY.md` | 取消文档分级，入口改为 `README.md` |
| `GETTING-STARTED.md` | `project-setup/GUIDE.md` |
| `QUICK-START-5MIN.md` | `README.md` 的"5 分钟开始" |
| `CHECKLIST-UNIFIED.md` | 清单回到 `coding/PRINCIPLES.md`、`coding/WORKFLOW.md` 各自的自查节 |
| `DOC-MAINTENANCE-GUIDE.md` | `CONTRIBUTING.md` + `scripts/check_docs.py` |
| `coding/GITHUB-RESEARCH.md` | `coding/RESEARCH.md`（不再把 GitHub 当唯一证据源） |
| `documentation/DOCS-EXTRACTION-GUIDE.md` | `project-setup/GUIDE.md` 第三节（老项目） |
| `project-adapt/AI-EXECUTION-GUIDE.md` | `coding/WORKFLOW.md` + `project-setup/GUIDE.md` |
| `project-adapt/PROJECT-ADAPT-STRATEGY.md` | 协议废弃，改为项目 `AGENTS.md` |
| `skills/OIL-DEV-SKILLS-CHECKLIST.md` | `skills/README.md`（用法指向官方仓库） |
| `skills/OIL-DEV-SKILLS-EXTENSION.md` | `skills/README.md` 第六节 |
| `skills/PROJECT-CUSTOM-SKILLS-STRATEGY.md` | `skills/README.md` 第六节（去掉评分模型） |
| `skills/SKILLS-GUIDE.md` | `skills/README.md` |
| `skills/SKILLS-INTEGRATION.md` | `skills/README.md` |
| `skills/UNIVERSAL-SKILLS-REGISTRY.md` | 依赖官方 Skill 清单，不再本地维护 |
| `templates/PROJECT-INIT-CHECKLIST.md` | `project-setup/GUIDE.md` 验收清单 |

---

## 什么时候可以删

确认以下条件后再考虑删除，并在提交信息里说明：

- 新结构已经在一个以上真实项目里跑过
- 没有需要从旧文档里再取的内容
- 团队里没人再引用旧路径

在此之前保留原样即可，不要"顺手清理"。