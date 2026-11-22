#!/usr/bin/env python3
"""vibcoding 文档自检。

用法:
    python scripts/check_docs.py

检查项:
    1. 相对 Markdown 链接的目标是否存在
    2. 是否出现已废弃的路径 / 术语 / 配置协议
    3. 同一文件内是否存在重复的二级标题
    4. AGENTS.md 是否超过体积预算
    5. 是否存在乱码替换字符 U+FFFD
    6. 在用文档是否链接到了 archive/ 内的具体文件

退出码: 0 无问题, 1 有问题。输出格式: 文件:行号: 说明
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {"archive", "scripts", ".git", "node_modules", ".idea", ".vscode"}
MAX_AGENTS_BYTES = 8 * 1024

FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
HEADING_RE = re.compile(r"^##\s+(.*\S)\s*$")
EXTERNAL_RE = re.compile(r"^(?:[A-Za-z][A-Za-z0-9+.-]*:|#)")

# (正则, 说明)。只检查正文，不检查代码块和行内代码。
FORBIDDEN = [
    (re.compile(r"(?<![\w./-])specs/"), "旧路径 specs/，应为 coding/"),
    (re.compile(r"vibcoding-skills"), "旧路径 vibcoding-skills/，应为 skills/ 或官方链接"),
    (re.compile(r"\bScale\b"), "旧术语 Scale，应为 Skill"),
    (
        re.compile(r"\bskill-(?:explore|plan|delegate|code-review|bug-fix|govern)\b"),
        "本库不定义该 Skill 名称，应写实际安装的工具名称",
    ),
    (re.compile(r"\bL[0-4]\b"), "旧分级编号 L0-L4，应为绿灯/黄灯/红灯"),
    (re.compile(r"PROJECT-ADAPT"), "已废弃的配置协议，项目约定写在 AGENTS.md"),
]


def iter_docs():
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        if rel.parts and rel.parts[0] in SKIP_DIRS:
            continue
        yield path, rel


def is_inside_archive(target: Path) -> bool:
    try:
        target.relative_to(ROOT / "archive")
        return True
    except ValueError:
        return False


def check_file(path: Path, rel: Path):
    issues = []
    rel_text = rel.as_posix()
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    if not lines:
        issues.append((rel_text, 1, "空文件"))
        return issues

    in_fence = False
    headings = {}

    for no, line in enumerate(lines, 1):
        if "\ufffd" in line:
            issues.append((rel_text, no, "出现乱码替换字符 U+FFFD"))

        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        for match in LINK_RE.finditer(line):
            raw = unquote(match.group(1).strip())
            if not raw or EXTERNAL_RE.match(raw):
                continue
            raw = raw.split("#", 1)[0].split("?", 1)[0].strip()
            if not raw:
                continue
            target = (path.parent / raw).resolve()
            if not target.exists():
                issues.append((rel_text, no, "链接目标不存在: %s" % raw))
            elif is_inside_archive(target) and target != (ROOT / "archive" / "README.md"):
                issues.append((rel_text, no, "在用文档引用了归档文件: %s" % raw))

        visible = INLINE_CODE_RE.sub("", line)
        for pattern, message in FORBIDDEN:
            if pattern.search(visible):
                issues.append((rel_text, no, message))

        heading = HEADING_RE.match(line)
        if heading:
            name = " ".join(heading.group(1).split())
            headings.setdefault(name, []).append(no)

    for name, numbers in headings.items():
        if len(numbers) > 1:
            issues.append(
                (
                    rel_text,
                    numbers[1],
                    "二级标题重复: ## %s（行 %s）"
                    % (name, ", ".join(str(n) for n in numbers)),
                )
            )

    return issues


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    docs = list(iter_docs())
    issues = []

    for path, rel in docs:
        issues.extend(check_file(path, rel))

    agents = ROOT / "AGENTS.md"
    if agents.exists():
        size = agents.stat().st_size
        if size > MAX_AGENTS_BYTES:
            issues.append(
                ("AGENTS.md", 1, "超过体积预算: %d 字节 > %d" % (size, MAX_AGENTS_BYTES))
            )
    else:
        issues.append(("AGENTS.md", 1, "文件缺失"))

    issues.sort(key=lambda item: (item[0], item[1]))
    for rel_text, no, message in issues:
        print("%s:%d: %s" % (rel_text, no, message))

    print("")
    print("检查 %d 个 Markdown 文件，发现 %d 个问题。" % (len(docs), len(issues)))
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())