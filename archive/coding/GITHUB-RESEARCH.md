# GITHUB-RESEARCH.md - GitHub 方案查证指南

在技术决策前，如何在 GitHub 上查找、对比和评估成熟方案。

适用于所有项目和技术栈。

---

## 触发条件

**以下情况必须进行 GitHub 方案查证：**

| 类别 | 具体场景 |
|------|---------|
| **技术选型** | 框架选择、库选择、工具选择 |
| **系统架构** | 微服务 vs 单体、分布式架构、消息队列方案 |
| **核心模块设计** | 认证、缓存、队列、监控、日志、权限 |
| **数据存储** | 数据库选择、ORM 框架、缓存方案 |
| **部署运维** | 容器化、CI/CD、监控告警、基础设施 |
| **性能优化** | 大数据处理、高并发方案、缓存策略 |

---

## 5 步查证流程

### 步骤 1：确定搜索关键词

**格式：** `核心概念 + 技术栈 + ("architecture" / "pattern" / "best practice" / "example")`

**示例：**
```
认证方案：
  - "JWT authentication TypeScript"
  - "OAuth2 Node.js implementation"
  - "auth0 integration example"

缓存策略：
  - "Redis cache layer architecture"
  - "caching strategies Node.js"
  - "distributed caching pattern"

消息队列：
  - "job queue system Node.js"
  - "background task processing"
  - "RabbitMQ vs Redis queue"

监控告警：
  - "monitoring system architecture"
  - "observability stack open source"
  - "prometheus grafana setup"
```

**搜索技巧：**
- 在 GitHub 搜索框输入关键词
- 在描述中加上语言/框架名（如 TypeScript、Node.js）
- 加上"example"或"boilerplate"找参考实现
- 在 GitHub Discussions 或 Issues 中搜索对比讨论

### 步骤 2：筛选高质量项目

**高质量项目的标准：**

| 指标 | 要求 | 检查方法 |
|------|------|---------|
| **社区认可度** | ⭐ stars > 1000 | 看 GitHub 主页右侧的 star 数 |
| **维护活跃度** | 📅 最近 6 个月内有更新 | 看"Commits"标签的时间线 |
| **文档完整性** | 📚 有详细 README 和示例 | 读 README.md，看示例代码 |
| **代码质量** | ✅ 有单元测试和集成测试 | 看 tests/ 或 __tests__/ 目录 |
| **贡献者活跃度** | 👥 有多个活跃贡献者 | 看"Contributors"标签 |

**筛选过程：**

```
搜索关键词 → 看 star 数 → 看最新提交时间 → 读 README 
→ 看代码质量 → 看是否有测试 → 看 Issue 和 Discussion 质量
```

**排除的项目：**
- ❌ stars < 500 且没有特殊理由
- ❌ 最后更新 > 1 年前
- ❌ 没有 README 或文档不清
- ❌ 没有任何测试
- ❌ Issue 堆积，维护者长期无响应

### 步骤 3：对比分析（至少 2-3 个项目）

**对比模板：**

| 项目 | 核心优点 | 核心缺点 | 生态成熟度 | 适配度 |
|------|---------|---------|-----------|--------|
| **项目A** | 功能完整，性能好 | 体积大，学习曲线陡 | ⭐⭐⭐⭐⭐ | 🟢 适配 |
| **项目B** | 轻量易用，文档清 | 功能不够完整 | ⭐⭐⭐ | 🟡 部分适配 |
| **项目C** | 功能全面 | 维护不活跃 | ⭐⭐ | 🔴 不适配 |

**对比要点：**

- **功能覆盖度** - 能否满足需求？有哪些功能是不需要的？
- **性能特性** - 能否满足性能要求？有哪些 trade-off？
- **易用性** - API 设计是否直观？文档是否清晰？
- **社区支持** - 生态活跃度？获取帮助的难度？
- **学习成本** - 学习曲线陡不陡？有没有最佳实践指南？
- **维护成本** - 维护者是否活跃？能否长期依赖？

**对比示例：**

```
任务：选择 CSV 解析库

搜索关键词：CSV parser JavaScript
找到项目：papa-parse, csv-parser, fast-csv

对比分析：

| 项目 | 优点 | 缺点 | 推荐度 |
|------|------|------|--------|
| papa-parse | 功能完整，易用，文档好，1500+ stars | 体积大(5KB) | ⭐⭐⭐⭐⭐ ✅ |
| csv-parser | 轻量(2KB)，速度快，1000+ stars | 功能较少，文档简 | ⭐⭐⭐ |
| fast-csv | 功能全面，性能好 | 文档不清，800 stars，更新慢 | ⭐⭐ |

结论：选 papa-parse
理由：
  1. 功能满足需求（CSV解析 + 验证）
  2. 易用性最好，文档最清楚
  3. 社区最活跃，问题最容易解决
  4. 大型项目的选择，经过验证
```

### 步骤 4：做出决策并记录

**决策记录模板（放在项目的 `docs/decisions.md`）：**

```markdown
## [决策-XXX] 选择了YYY方案处理ZZZ问题

**日期**: 2026-11-22
**参与者**: @dev-name, @tech-lead
**背景**: 需要解析 CSV 文件导入用户

**参考项目**:
- [papa-parse](https://github.com/mholt/papaparse) 
  - ⭐ 2000+ stars
  - 📅 最新更新: 2026-11
  - 📚 文档完整，有丰富示例
  
- [csv-parser](https://github.com/mafintosh/csv-parser)
  - ⭐ 1000+ stars
  - 📅 最新更新: 2026-10
  - 📚 文档简洁但功能较少
  
- [fast-csv](https://github.com/C2FO/fast-csv)
  - ⭐ 800+ stars
  - 📅 最新更新: 2026-08
  - ⚠️ 更新频率较低

**对比分析**:

| 项目 | 功能覆盖度 | 易用性 | 文档 | 性能 | 推荐度 |
|------|-----------|--------|------|------|--------|
| papa-parse | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ✅ 选择 |
| csv-parser | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 备选 |
| fast-csv | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | 不推荐 |

**选择理由**:
papa-parse 是最好的选择，因为：
1. **完整的功能覆盖** - 支持 CSV、TSV、自定义分隔符、动态类型等
2. **易用的 API** - 一行代码即可解析，配置直观
3. **清晰的文档** - 有详细的 API 文档和实战示例
4. **活跃的社区** - 2000+ stars，Issue 有人及时回复
5. **实战验证** - 被大量生产环境使用，可靠性有保证

**权衡**:
- papa-parse 体积比 csv-parser 大（5KB vs 2KB）
- 但我们的场景是服务端而非浏览器，体积不是关键
- 功能完整和易用性的收益大于体积劣势

**成本**:
- 集成时间：~2 小时
- 学习成本：低（API 简单）
- 维护成本：低（社区活跃）

**关键假设**:
- 假设文件大小不超过 100MB（papa-parse 在此范围内表现良好）
- 如果后期需要处理超大文件，需要重新评估（可能用 streaming 方式）

**参考链接**:
- [Papa Parse 官方文档](https://papaparse.com/)
- [Papa Parse GitHub](https://github.com/mholt/papaparse)
- [对标项目讨论](链接到相关 GitHub Issue 或 Discussion)

**后续**:
- [ ] 在项目中集成 papa-parse
- [ ] 编写单元测试验证解析功能
- [ ] 如果后期有性能问题，考虑迁移到 fast-csv
```

### 步骤 5：标记参考来源

**代码中标记：**

```typescript
// 参考: papa-parse (https://github.com/mholt/papaparse)
// 官方文档: https://papaparse.com/docs
import Papa from 'papaparse';

export function parseCSV(file: File): Promise<any[]> {
  return new Promise((resolve, reject) => {
    Papa.parse(file, {
      header: true,
      complete: (results) => resolve(results.data),
      error: (error) => reject(error)
    });
  });
}
```

**架构文档中标记：**

```markdown
## CSV 导入模块

**参考项目**: papa-parse (GitHub)
**文档**: https://papaparse.com/
**决策记录**: 见 docs/decisions.md 中的"选择CSV解析库"

### 实现思路

基于 papa-parse 库，实现了以下功能：
1. CSV 文件解析
2. 数据验证
3. 错误处理
4. 进度跟踪
```

---

## 🚫 禁止清单

**这些做法会导致重复造轮子或技术债：**

| 禁止 | 原因 | 后果 |
|------|------|------|
| ❌ 看到问题直接自己设计，不查GitHub | 可能忽视已有的成熟方案 | 重复造轮子，浪费时间 |
| ❌ 只看一个项目就决策 | 没有对比，可能选错 | 后期发现更好方案，需要迁移 |
| ❌ 选择低质量项目（stars少、不维护） | 质量无法保证 | 后期维护困难，社区支持差 |
| ❌ 自主发明轮子，除非有明确理由 | 增加复杂度 | 维护成本高，容易出 bug |
| ❌ 决策不记录，参考链接不保存 | 后期无法追溯 | 下次遇到同样问题又要查一遍 |

---

## 常见问题

**Q: 什么时候需要查证GitHub方案？**
A: L2 和 L3 涉及技术决策时必查。L1 不需要。

**Q: 一定要查3个项目吗？**
A: 至少2个。如果第一个项目确实是绝对领导者（stars远超其他，明显最优），1个也可以。但一般还是建议查2-3个对比。

**Q: 一定要查github吗？会不会有更好的方案？**
A: GitHub 是开源项目最集中的地方。主要方案都在那里。除非是商业产品或内部方案，否则 GitHub 上的选择通常已经足够了。

**Q: 怎么判断一个项目是不是活跃维护？**
A: 看"Commits"标签，查看最近的提交日期。如果最新提交在6个月内，说明有人在维护。同时看 Issue 的回复速度。

**Q: 决策记录要写得很详细吗？**
A: 至少要包含：参考项目、对比分析、选择理由。详细程度可以根据决策的重要性调整。小决策可简洁，大决策要详细。

**Q: 参考项目要加到代码里吗？**
A: 不一定要在代码里，但要在某个地方（如docs或决策记录中）清楚地标注参考来源。这样后期维护者能理解为什么选了这个方案。

---

## 更新日志

**2026-11-22** - 初始版本
- 触发条件（什么时候查证）
- 5 步查证流程（详细步骤）
- 高质量项目筛选标准
- 决策记录模板
- 禁止清单和常见问题

