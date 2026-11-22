# DOCS-EXTRACTION-GUIDE.md - 项目文档提取与规范化

**对象：** AI（自动执行）

**目的：** 从现有项目文档中提取信息，映射到 vibcoding 规范体系

---

## 🎯 核心理念

```
老旧项目的现有文档
    ↓
AI 自动扫描和提取
    ↓
标准化为 vibcoding 格式
    ↓
生成 PROJECT-ADAPT.yaml
    ↓
项目立即可用
```

**不手动维护两套文档，而是从现有文档中自动提取。**

---

## 📋 扫描规则

### 要扫描的文件类型

```
优先级 1（高）- 必查
├─ README.md
│   提取：项目名称、目的、技术栈、快速开始
│
├─ CONTRIBUTING.md
│   提取：开发工作流、PR 流程、代码风格要求
│
└─ AGENTS.md（如果有）
    提取：现有的开发配置、高风险目录、do-not-edit 路径

优先级 2（中）- 应查
├─ package.json / pom.xml / Cargo.toml
│   提取：依赖版本、测试框架、构建工具
│
├─ .github/workflows/ 中的 CI/CD 配置
│   提取：测试命令、merge-gate 命令、构建步骤
│
├─ docs/ 目录中的所有 MD 文件
│   提取：架构说明、开发指南、规范文档
│
└─ .eslintrc / .prettier / .flake8 等配置
    提取：代码风格约定

优先级 3（低）- 可查
├─ docs/decision/ 或 docs/adr/
│   提取：已有的决策记录、架构决策
│
└─ 其他 docs 文件
    提取：项目约定和最佳实践
```

---

## 🔍 信息提取规则

### 1. 技术栈信息

```python
def extract_tech_stack():
    """从项目配置中提取技术栈"""
    
    info = {
        'language': None,
        'framework': None,
        'database': None,
        'test_framework': None,
        'build_tool': None,
        'ci_cd': None,
    }
    
    # 从 package.json 提取（Node.js）
    if has_file('package.json'):
        pkg = read_json('package.json')
        info['language'] = 'Node.js ' + pkg.get('engines', {}).get('node', 'unknown')
        info['framework'] = detect_framework(pkg['dependencies'])
        info['test_framework'] = detect_test_framework(pkg['devDependencies'])
    
    # 从 pom.xml 提取（Java）
    elif has_file('pom.xml'):
        info['language'] = 'Java'
        info['build_tool'] = 'Maven'
        # 解析 pom.xml
    
    # 从 Cargo.toml 提取（Rust）
    elif has_file('Cargo.toml'):
        info['language'] = 'Rust'
        info['build_tool'] = 'Cargo'
    
    # ... 其他语言
    
    return info
```

### 2. 工作流信息

```python
def extract_workflow():
    """从 CONTRIBUTING.md 和 CI 配置中提取工作流"""
    
    workflow = {
        'git_strategy': None,
        'branch_naming': None,
        'pr_process': None,
        'review_requirements': None,
        'merge_strategy': None,
        'test_commands': None,
        'deploy_process': None,
    }
    
    # 从 CONTRIBUTING.md 提取
    if has_file('CONTRIBUTING.md'):
        content = read_file('CONTRIBUTING.md')
        
        # 查找 branch 相关说明
        workflow['branch_naming'] = extract_section(content, 'branch', 'naming')
        
        # 查找 PR 流程
        workflow['pr_process'] = extract_section(content, 'pull request', 'pr')
        
        # 查找 review 要求
        workflow['review_requirements'] = extract_section(content, 'review', 'approval')
    
    # 从 GitHub Actions 中提取
    if has_dir('.github/workflows'):
        for workflow_file in list_files('.github/workflows'):
            workflow['test_commands'] = extract_test_commands(workflow_file)
            workflow['merge_strategy'] = extract_merge_strategy(workflow_file)
    
    return workflow
```

### 3. 代码规范信息

```python
def extract_code_conventions():
    """从 linter 配置和文档中提取代码规范"""
    
    conventions = {
        'code_style': None,
        'naming_convention': None,
        'test_coverage': None,
        'documentation': None,
        'git_commit_style': None,
    }
    
    # 从 .eslintrc 提取（JavaScript）
    if has_file('.eslintrc.json'):
        eslint = read_json('.eslintrc.json')
        conventions['code_style'] = eslint.get('rules', {})
    
    # 从 README 中查找约定
    if has_file('README.md'):
        readme = read_file('README.md')
        
        # 查找"编码规范"或"开发规范"部分
        conventions['code_style'] = extract_section(readme, 'coding', 'convention', 'style')
        conventions['naming_convention'] = extract_section(readme, 'naming', 'convention')
        conventions['test_coverage'] = extract_number(readme, r'coverage.*(\d+)%')
    
    return conventions
```

### 4. 高风险和禁区

```python
def extract_risk_areas():
    """提取高风险目录和 do-not-edit 路径"""
    
    risk_areas = {
        'high_risk': [],
        'do_not_edit': [],
        'sensitive_files': [],
    }
    
    # 从现有 AGENTS.md 提取
    if has_file('AGENTS.md'):
        agents = read_file('AGENTS.md')
        
        # 查找"高风险"或"high-risk"
        risk_areas['high_risk'] = extract_paths(agents, 'high-risk', 'risky')
        
        # 查找"禁区"或"do-not-edit"
        risk_areas['do_not_edit'] = extract_paths(agents, 'do-not-edit', 'forbidden')
    
    # 从常见模式推断
    risk_areas['sensitive_files'] = infer_sensitive_files([
        'migrations/',
        'scripts/',
        'config/',
        'auth/',
        'security/',
    ])
    
    return risk_areas
```

---

## 📊 信息标准化

### 提取的信息映射到 vibcoding

```python
def normalize_info_to_vibcoding():
    """将提取的信息标准化为 vibcoding 格式"""
    
    # 【步骤 1】扫描所有信息
    tech_stack = extract_tech_stack()
    workflow = extract_workflow()
    conventions = extract_code_conventions()
    risk_areas = extract_risk_areas()
    
    # 【步骤 2】对比通用规范
    vibcoding_principles = load('vibcoding-rules/specs/PRINCIPLES.md')
    vibcoding_workflow = load('vibcoding-rules/specs/WORKFLOW.md')
    
    conflicts = []
    
    # 【步骤 3】识别冲突
    for principle in vibcoding_principles:
        project_practice = extract_practice(conventions, principle.name)
        
        if project_practice and project_practice != principle.standard:
            conflicts.append({
                'type': 'principle_conflict',
                'principle': principle.name,
                'project': project_practice,
                'universal': principle.standard,
                'impact': principle.impact,
            })
    
    # 【步骤 4】生成标准化输出
    normalized = {
        'tech_stack': tech_stack,
        'workflow': workflow,
        'conventions': conventions,
        'risk_areas': risk_areas,
        'conflicts': conflicts,
        'extraction_summary': {
            'files_scanned': len(scanned_files),
            'info_extracted': len(extracted_info),
            'conflicts_found': len(conflicts),
            'confidence': calculate_confidence(conflicts),
        }
    }
    
    return normalized
```

---

## 🔄 冲突映射规则

### 识别冲突的规则

```python
def map_conflicts_to_adapt_yaml():
    """将识别的冲突映射到 PROJECT-ADAPT.yaml 格式"""
    
    adapt_config = {
        'project_name': None,
        'tech_stack': {},
        'principles_adapt': [],
        'workflow_adapt': [],
        'oil_skills_handling': {},
    }
    
    for conflict in conflicts:
        
        if conflict['type'] == 'principle_conflict':
            # 冲突示例：项目做法 vs 通用原则
            adapt_config['principles_adapt'].append({
                'rule': conflict['principle'],
                'decision': 'keep_project',  # 或 'adopt_universal' 或 'custom'
                'reason': 'extracted from ' + conflict['source_file'],
                'project_practice': conflict['project'],
            })
        
        elif conflict['type'] == 'workflow_conflict':
            # 冲突示例：项目工作流 vs L1/L2/L3
            adapt_config['workflow_adapt'].append({
                'area': conflict['area'],
                'project_way': conflict['project'],
                'universal_way': conflict['universal'],
                'decision': 'map_to_L2',  # 映射到哪一级
            })
        
        elif conflict['type'] == 'skill_needed':
            # 冲突示例：项目需要特殊 skill
            adapt_config['oil_skills_handling'].append({
                'base_skill': conflict['base_skill'],
                'type': 'supplement',
                'with': conflict['needed_skill'],
                'reason': conflict['reason'],
            })
    
    return adapt_config
```

---

## 📝 生成冲突报告

### 报告结构

```markdown
# 文档提取冲突报告

## 提取总结
- 扫描文件：15 个
- 提取信息项：38 个
- 冲突发现：5 个
- 信心度：92%（基于匹配程度）

## 识别的冲突

### 冲突 #1：编码风格
**源文件：** README.md, .eslintrc.json
**项目做法：** 严格的 2-space 缩进
**通用规范：** PRINCIPLES.Simplicity First（无特殊要求）
**映射结果：** 不冲突，属于项目细节

---

### 冲突 #2：测试覆盖率
**源文件：** CONTRIBUTING.md
**项目要求：** 新代码需要 > 80% 覆盖
**通用规范：** WORKFLOW.L2（没有明确覆盖率要求）
**映射结果：** 项目级约束，添加到 TECH-STACK.md

---

### 冲突 #3：Review 流程
**源文件：** CONTRIBUTING.md
**项目做法：** 只有 > 100 行需要 review
**通用规范：** PRINCIPLES（所有代码都应 review）
**映射结果：** 高影响冲突，需要用户决策

---

## 下一步
1. 请审核这些冲突
2. 对冲突 #3 做出决策（保留项目做法 vs 采用通用规范）
3. AI 将生成 PROJECT-ADAPT.yaml
```

---

## ✅ 执行检查清单

```
【步骤 1】文档扫描
- [ ] 读了 README.md
- [ ] 读了 CONTRIBUTING.md
- [ ] 读了 AGENTS.md（如果有）
- [ ] 读了所有 package.json / pom.xml 等配置
- [ ] 读了 CI/CD 配置文件
- [ ] 读了 linter 配置文件

【步骤 2】信息提取
- [ ] 提取了技术栈信息
- [ ] 提取了工作流信息
- [ ] 提取了代码规范信息
- [ ] 提取了高风险和禁区信息
- [ ] 生成了提取总结

【步骤 3】标准化
- [ ] 对比了通用规范
- [ ] 识别了所有冲突
- [ ] 评估了每个冲突的影响
- [ ] 映射到了 vibcoding 格式

【步骤 4】生成报告
- [ ] 生成了冲突报告
- [ ] 显示给用户审核
- [ ] 等待用户决策

【步骤 5】生成配置
- [ ] 生成了 PROJECT-ADAPT.yaml
- [ ] 生成了 RULES-OVERRIDE.md
- [ ] 生成了 TECH-STACK.md
- [ ] 生成了 WORKFLOW-ADAPT.md

【步骤 6】完成
- [ ] 项目准备完毕
- [ ] 可以开始使用 vibcoding
```

---

## 🎯 信息提取的优先级

```
【必须有】
- 技术栈（语言、框架、版本）
- 测试命令（quick-test）
- 合并门槛（merge-gate）
- 高风险目录

【应该有】
- 分支命名规范
- PR 流程
- 代码风格约定
- 测试覆盖率要求

【可以没有】
- 详细的架构文档
- 历史决策记录
- 其他最佳实践
```

---

## 💡 信息提取的注意事项

```
1. 不要过度解读
   如果文档中说"推荐用 X"，不代表强制要求
   → 在报告中标记为"建议"而不是"冲突"

2. 处理不完整的信息
   如果某些信息缺失
   → 用项目推断（例如：有 Jest 配置 → 测试框架是 Jest）
   → 标记为"推断"，让用户确认

3. 避免误判
   同一个概念可能有不同的表述
   "review" = "审查" = "code review"
   → 建立同义词映射

4. 记录提取过程
   每个信息来自哪个文件、哪一行
   → 用户需要验证时，能快速找到

5. 信心度评估
   提取的信息有多可靠？
   - 明确写在文档中：95% 信心
   - 从代码推断：70% 信心
   - 猜测：40% 信心
```

