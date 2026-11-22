#!/usr/bin/env python3
"""只读采集项目客观事实，供 AI 写项目状态时当证据。

用法:
    python scripts/scan_project.py                  # 输出到终端
    python scripts/scan_project.py --out facts.md   # 写入文件
    python scripts/scan_project.py --root ../repo   # 指定项目根目录

原则:
    - 只读。不装依赖、不跑构建/测试、不写业务文件。
    - 只调 git 的只读子命令（status / log / rev-parse）。
    - 采集不到就写"未找到"，不猜。

输出是"事实清单"，不是结论。语义判断交给 prompts/PROJECT-SCAN.md。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

PRUNE_DIRS = {
    ".git", ".hg", ".svn", "node_modules", ".venv", "venv", "env", "__pycache__",
    "dist", "build", "target", "vendor", "coverage", ".next", ".nuxt", ".output",
    ".idea", ".vscode", ".gradle", ".mypy_cache", ".pytest_cache", ".ruff_cache",
    ".tox", ".cache", "bin", "obj", "Pods", ".dart_tool",
}

LANG_EXT = {
    ".py": "Python", ".ts": "TypeScript", ".tsx": "TypeScript", ".js": "JavaScript",
    ".jsx": "JavaScript", ".go": "Go", ".rs": "Rust", ".java": "Java", ".kt": "Kotlin",
    ".cs": "C#", ".rb": "Ruby", ".php": "PHP", ".c": "C", ".cpp": "C++", ".h": "C/C++ 头",
    ".swift": "Swift", ".scala": "Scala", ".vue": "Vue", ".svelte": "Svelte",
    ".sql": "SQL", ".sh": "Shell", ".ps1": "PowerShell", ".md": "Markdown",
    ".yml": "YAML", ".yaml": "YAML", ".json": "JSON", ".toml": "TOML",
}

TEXT_EXT = {
    ".py", ".ts", ".tsx", ".js", ".jsx", ".go", ".rs", ".java", ".kt", ".cs", ".rb",
    ".php", ".c", ".cpp", ".h", ".swift", ".scala", ".vue", ".svelte", ".sql", ".sh",
    ".ps1", ".md", ".txt", ".yml", ".yaml", ".toml", ".ini", ".cfg", ".conf", ".xml",
    ".json", ".gradle", ".properties",
}

TEST_DIR_NAMES = {"test", "tests", "__tests__", "spec", "specs", "e2e", "integration_tests"}

TEST_CONFIGS = [
    "pytest.ini", "tox.ini", "setup.cfg", "jest.config.js", "jest.config.ts",
    "jest.config.mjs", "vitest.config.ts", "vitest.config.js", "playwright.config.ts",
    "cypress.config.ts", "cypress.config.js", ".mocharc.json", ".mocharc.yml",
    "phpunit.xml", "phpunit.xml.dist", "codecov.yml", ".nycrc", ".nycrc.json",
]

LINT_CONFIGS = [
    ".eslintrc", ".eslintrc.js", ".eslintrc.json", ".eslintrc.yml", "eslint.config.js",
    "eslint.config.mjs", "ruff.toml", ".ruff.toml", ".flake8", "mypy.ini",
    ".golangci.yml", ".golangci.yaml", "rustfmt.toml", ".prettierrc", ".prettierrc.json",
    "biome.json", ".editorconfig", "clippy.toml",
]

RISK_PATTERN = re.compile(
    r"(^|[._-])(auth|login|session|payment|billing|checkout|invoice|migration|migrations|"
    r"deploy|infra|terraform|k8s|kubernetes|helm|secret|secrets|security|crypto|"
    r"permission|rbac|oauth)([._-]|$)",
    re.IGNORECASE,
)

SENSITIVE_NAMES = {".env", ".env.local", ".env.production", ".npmrc", ".pypirc", "id_rsa", "id_ed25519"}
SENSITIVE_SUFFIX = {".pem", ".key", ".p12", ".pfx", ".keystore"}

TODO_RE = re.compile(r"\b(TODO|FIXME|HACK|XXX)\b")
SKIP_RE = re.compile(r"\b(it|test|describe|xit|xdescribe)\.(skip|only)\b|@Ignore|@Disabled")


def run_git(root: Path, args):
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=str(root),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=15,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def human_size(size: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024 or unit == "GB":
            return "%.0f %s" % (size, unit) if unit == "B" else "%.1f %s" % (size, unit)
        size /= 1024.0
    return "%d B" % size


def collect(root: Path, max_scan_files: int):
    total_files = 0
    ext_counts = {}
    lang_counts = {}
    top_dirs = {}
    risk_dirs = []
    generated_dirs = []
    large_files = []
    docs = []
    tests = 0
    todo_counts = {}
    skip_hits = []
    scanned = 0

    top_entries = sorted(p.name for p in root.iterdir() if p.name not in PRUNE_DIRS)

    for dirpath, dirnames, filenames in os_walk_safe(root):
        dirnames[:] = sorted(d for d in dirnames if d not in PRUNE_DIRS)

        rel_dir = Path(dirpath).relative_to(root)
        parts = rel_dir.parts
        if parts and parts[0] not in top_dirs:
            top_dirs[parts[0]] = 0

        if parts:
            name = parts[-1].lower()
            if RISK_PATTERN.search(name):
                risk_dirs.append(rel_dir.as_posix())
            if name in {"generated", "gen", "__generated__", "dist", "build", "out"}:
                generated_dirs.append(rel_dir.as_posix())
            if any(part.lower() in TEST_DIR_NAMES for part in parts):
                tests += sum(1 for f in filenames if Path(f).suffix.lower() in TEXT_EXT)

        for filename in filenames:
            path = Path(dirpath) / filename
            total_files += 1
            if parts:
                top_dirs[parts[0]] = top_dirs.get(parts[0], 0) + 1

            suffix = path.suffix.lower()
            ext_counts[suffix] = ext_counts.get(suffix, 0) + 1
            if suffix in LANG_EXT and suffix != ".md":
                lang_counts[LANG_EXT[suffix]] = lang_counts.get(LANG_EXT[suffix], 0) + 1
            if suffix == ".md":
                docs.append(path.relative_to(root).as_posix())

            try:
                size = path.stat().st_size
            except OSError:
                size = 0
            if size > 1024 * 1024:
                large_files.append((path.relative_to(root).as_posix(), size))

            if suffix in TEXT_EXT and size <= 512 * 1024 and scanned < max_scan_files:
                scanned += 1
                try:
                    content = path.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    content = ""
                if TODO_RE.search(content):
                    count = len(TODO_RE.findall(content))
                    key = parts[0] if parts else "(根目录)"
                    todo_counts[key] = todo_counts.get(key, 0) + count
                if suffix in {".py", ".js", ".ts", ".tsx", ".jsx", ".java", ".rb"}:
                    if SKIP_RE.search(content):
                        skip_hits.append(path.relative_to(root).as_posix())

    large_files.sort(key=lambda item: item[1], reverse=True)
    return {
        "total_files": total_files,
        "ext_counts": ext_counts,
        "lang_counts": lang_counts,
        "top_dirs": top_dirs,
        "top_entries": top_entries,
        "risk_dirs": sorted(set(risk_dirs)),
        "generated_dirs": sorted(set(generated_dirs)),
        "large_files": large_files[:10],
        "docs": sorted(docs),
        "test_file_count": tests,
        "todo_counts": todo_counts,
        "skip_hits": skip_hits[:20],
        "scanned_files": scanned,
    }


def os_walk_safe(root: Path):
    """os.walk 的薄包装，避免在权限错误的目录上崩掉。"""

    def onerror(_):
        return

    return os.walk(str(root), onerror=onerror)


def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except (OSError, ValueError):
        return None


def grep_first(path: Path, pattern: str, limit: int = 40):
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()[:limit]
    except OSError:
        return None
    regex = re.compile(pattern)
    for line in lines:
        if regex.search(line):
            return line.strip()
    return None


def manifest_section(root: Path):
    lines = []
    package_json = root / "package.json"
    if package_json.exists():
        data = read_json(package_json)
        if isinstance(data, dict):
            lines.append("- `package.json`：name=`%s`" % data.get("name", "未写"))
            scripts = data.get("scripts") or {}
            if isinstance(scripts, dict) and scripts:
                lines.append("  - scripts: " + ", ".join("`%s`" % k for k in sorted(scripts)))
            deps = data.get("dependencies") or {}
            dev = data.get("devDependencies") or {}
            lines.append("  - 依赖：%d 个运行时，%d 个开发依赖" % (len(deps), len(dev)))
            if data.get("packageManager"):
                lines.append("  - packageManager: `%s`" % data["packageManager"])

    checks = [
        ("pyproject.toml", r"^\s*name\s*="),
        ("Cargo.toml", r"^\s*name\s*="),
        ("go.mod", r"^module\s+"),
        ("composer.json", r'"name"'),
        ("pom.xml", r"<artifactId>"),
        ("Gemfile", r"^ruby\s"),
    ]
    for name, pattern in checks:
        path = root / name
        if path.exists():
            found = grep_first(path, pattern)
            lines.append("- `%s`%s" % (name, "：" + found if found else ""))

    for name in ("requirements.txt", "requirements-dev.txt", "Makefile", "justfile", "Dockerfile", "docker-compose.yml", "docker-compose.yaml", ".python-version", ".nvmrc", ".tool-versions"):
        path = root / name
        if path.exists():
            extra = ""
            if name.startswith("requirements"):
                try:
                    count = len([l for l in path.read_text(encoding="utf-8", errors="replace").splitlines() if l.strip() and not l.strip().startswith("#")])
                    extra = "：%d 条依赖" % count
                except OSError:
                    pass
            if name == "Makefile":
                try:
                    targets = re.findall(r"^([A-Za-z0-9_.-]+):", path.read_text(encoding="utf-8", errors="replace"), re.MULTILINE)
                    if targets:
                        extra = "：targets " + ", ".join(sorted(set(targets))[:20])
                except OSError:
                    pass
            lines.append("- `%s`%s" % (name, extra))

    return lines or ["未找到可识别的清单文件。"]


def ci_section(root: Path):
    found = []
    workflows = root / ".github" / "workflows"
    if workflows.is_dir():
        found.extend(sorted(p.relative_to(root).as_posix() for p in workflows.glob("*.y*ml")))
    for name in (".gitlab-ci.yml", "Jenkinsfile", "azure-pipelines.yml", ".circleci/config.yml", "bitbucket-pipelines.yml", ".drone.yml", ".woodpecker.yml", "appveyor.yml"):
        if (root / name).exists():
            found.append(name)
    return found or ["未找到 CI 配置。"]


def tool_section(root: Path):
    lines = []
    tests = [name for name in TEST_CONFIGS if (root / name).exists()]
    lint = [name for name in LINT_CONFIGS if (root / name).exists()]
    lines.append("- 测试配置：" + (", ".join("`%s`" % t for t in tests) if tests else "未找到"))
    lines.append("- 质量工具配置：" + (", ".join("`%s`" % t for t in lint) if lint else "未找到"))
    lockfiles = [n for n in ("package-lock.json", "pnpm-lock.yaml", "yarn.lock", "bun.lockb", "poetry.lock", "Pipfile.lock", "uv.lock", "Cargo.lock", "go.sum", "composer.lock", "Gemfile.lock") if (root / n).exists()]
    lines.append("- 锁文件：" + (", ".join("`%s`" % l for l in lockfiles) if lockfiles else "未找到"))
    return lines


def git_section(root: Path):
    if run_git(root, ["rev-parse", "--is-inside-work-tree"]) is None:
        return ["不是 git 仓库，或 git 不可用。"]

    lines = []
    branch = run_git(root, ["rev-parse", "--abbrev-ref", "HEAD"])
    lines.append("- 当前分支：`%s`" % (branch or "未取到"))

    status = run_git(root, ["status", "--short"])
    if status is None:
        lines.append("- 工作区：未取到状态")
    elif not status:
        lines.append("- 工作区：干净")
    else:
        entries = status.splitlines()
        lines.append("- 工作区：%d 处未提交改动（前 10 条）" % len(entries))
        lines.extend("  - `%s`" % e for e in entries[:10])

    log = run_git(root, ["log", "-10", "--no-decorate", "--date=short", "--pretty=%h %ad %s"])
    if log:
        lines.append("- 最近提交：")
        lines.extend("  - `%s`" % l for l in log.splitlines())
    else:
        lines.append("- 最近提交：未取到（可能是空仓库）")

    return lines


def sensitive_section(root: Path):
    hits = []
    for dirpath, dirnames, filenames in os_walk_safe(root):
        dirnames[:] = [d for d in dirnames if d not in PRUNE_DIRS]
        for filename in filenames:
            if filename in SENSITIVE_NAMES or Path(filename).suffix.lower() in SENSITIVE_SUFFIX:
                hits.append((Path(dirpath) / filename).relative_to(root).as_posix())
    if not hits:
        return ["未发现常见敏感文件名。"]
    return ["发现以下文件名（**内容未读取**），确认是否应入库："] + ["- `%s`" % h for h in sorted(hits)[:20]]


def build_report(root: Path, data, args):
    lines = []
    lines.append("# 项目事实（只读采集）")
    lines.append("")
    lines.append("- 采集时间：%s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    lines.append("- 根目录：`%s`" % root.as_posix())
    lines.append("- 已排除目录：%s" % ", ".join(sorted(PRUNE_DIRS)))
    lines.append("- 说明：以下是客观事实，不含结论；语义判断见 `prompts/PROJECT-SCAN.md`。")
    lines.append("")

    lines.append("## 1. 规模")
    lines.append("")
    lines.append("- 文件总数（已排除生成物/依赖）：%d" % data["total_files"])
    lang = sorted(data["lang_counts"].items(), key=lambda kv: kv[1], reverse=True)[:10]
    lines.append("- 主要语言：%s" % (", ".join("%s %d" % kv for kv in lang) if lang else "未识别"))
    lines.append("")

    lines.append("## 2. 顶层目录")
    lines.append("")
    lines.append("| 目录/文件 | 文件数 |")
    lines.append("|---|---|")
    for name, count in sorted(data["top_dirs"].items(), key=lambda kv: kv[1], reverse=True)[:25]:
        lines.append("| `%s/` | %d |" % (name, count))
    plain = [e for e in data["top_entries"] if not (root / e).is_dir()]
    if plain:
        lines.append("| 顶层文件 | %s |" % ", ".join("`%s`" % e for e in plain[:20]))
    lines.append("")

    lines.append("## 3. 清单与入口")
    lines.append("")
    lines.extend(manifest_section(root))
    lines.append("")

    lines.append("## 4. CI")
    lines.append("")
    lines.extend("- `%s`" % c if not c.endswith("。") else "- " + c for c in ci_section(root))
    lines.append("")

    lines.append("## 5. 测试与质量工具")
    lines.append("")
    lines.extend(tool_section(root))
    lines.append("- 测试目录内文本文件数：%d" % data["test_file_count"])
    lines.append("")

    lines.append("## 6. 版本控制")
    lines.append("")
    lines.extend(git_section(root))
    lines.append("")

    lines.append("## 7. 文档")
    lines.append("")
    lines.append("- Markdown 文件数：%d" % len(data["docs"]))
    top_docs = [d for d in data["docs"] if "/" not in d][:20]
    if top_docs:
        lines.append("- 顶层文档：%s" % ", ".join("`%s`" % d for d in top_docs))
    docs_dir = [d for d in data["docs"] if d.startswith("docs/")][:20]
    if docs_dir:
        lines.append("- docs/：%s" % ", ".join("`%s`" % d for d in docs_dir))
    lines.append("")

    lines.append("## 8. 未完成迹象")
    lines.append("")
    if data["todo_counts"]:
        lines.append("- TODO/FIXME/HACK 分布（按顶层目录）：")
        for key, count in sorted(data["todo_counts"].items(), key=lambda kv: kv[1], reverse=True):
            lines.append("  - `%s`：%d" % (key, count))
    else:
        lines.append("- 未发现 TODO/FIXME/HACK（扫描了 %d 个文本文件）" % data["scanned_files"])
    if data["skip_hits"]:
        lines.append("- 含 `.skip` / `@Ignore` 的文件（前 20）：")
        lines.extend("  - `%s`" % s for s in data["skip_hits"])
    lines.append("")

    lines.append("## 9. 高危目录候选（需人工确认）")
    lines.append("")
    if data["risk_dirs"]:
        lines.extend("- `%s/`" % d for d in data["risk_dirs"][:25])
    else:
        lines.append("- 未按目录名匹配到候选。认证/支付/迁移等可能藏在别的命名下，需要读代码确认。")
    lines.append("")

    lines.append("## 10. 生成物 / 禁改候选")
    lines.append("")
    if data["generated_dirs"]:
        lines.extend("- `%s/`" % d for d in data["generated_dirs"][:25])
    else:
        lines.append("- 未按目录名匹配到候选。")
    lines.append("")

    lines.append("## 11. 大文件（> 1 MB，前 10）")
    lines.append("")
    if data["large_files"]:
        lines.extend("- `%s`：%s" % (p, human_size(s)) for p, s in data["large_files"])
    else:
        lines.append("- 无。")
    lines.append("")

    lines.append("## 12. 敏感文件")
    lines.append("")
    lines.extend(sensitive_section(root))
    lines.append("")

    lines.append("## 13. 采集限制")
    lines.append("")
    lines.append("- 未运行构建/测试/安装，因此所有命令均属“未验证”。")
    lines.append("- TODO 统计最多扫描 %d 个文本文件，大仓库可能不完整。" % args.max_scan_files)
    lines.append("- 目录职责、模块边界、风险判断需要读代码后补充。")
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="只读采集项目事实（不修改任何文件）")
    parser.add_argument("--root", default=".", help="项目根目录，默认当前目录")
    parser.add_argument("--out", default=None, help="输出文件；默认打印到终端")
    parser.add_argument("--max-scan-files", type=int, default=2000, help="TODO 扫描文件上限")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print("不是有效目录: %s" % root, file=sys.stderr)
        return 2

    data = collect(root, args.max_scan_files)
    report = build_report(root, data, args)

    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report + "\n", encoding="utf-8", newline="\n")
        print("已写入 %s（只读采集，未修改项目文件）" % out)
    else:
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
        print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
