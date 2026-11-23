import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from scripts import scan_project


class ScanProjectTests(unittest.TestCase):
    def test_reports_root_and_nested_project_files_but_skips_dependencies_and_builds(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            files = {
                "package.json": '{"name":"workspace"}',
                "apps/frontend/package.json": '{"name":"ui","scripts":{"start":"vite"}}',
                "apps/frontend/package-lock.json": "{}",
                "backend/requirements.txt": "# dependencies\nflask\n",
                "apps/frontend/node_modules/widget/package.json": "{}",
                "backend/build/requirements.txt": "ignored",
            }
            for name, content in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")

            facts = scan_project.collect(root, max_scan_files=0)
            manifests = scan_project.manifest_section(root, facts["manifests"])
            tools = scan_project.tool_section(root, facts["lockfiles"])
            self.assertIn("- `package.json`：name=`workspace`", manifests)
            self.assertIn("- `apps/frontend/package.json`：name=`ui`", manifests)
            self.assertIn("  - scripts: `start`", manifests)
            self.assertIn("- `backend/requirements.txt`：1 条依赖", manifests)
            self.assertIn("- 锁文件：`apps/frontend/package-lock.json`", tools)
            self.assertEqual(len(facts["manifests"]), 3)

    def test_counts_text_files_at_any_depth_under_a_test_directory(self):
        root = Path(__file__).resolve().parent
        walk = [
            (root / "app", [], ["main.py"]),
            (root / "app/tests", [], ["test_api.py"]),
            (root / "app/tests/fixtures/nested", [], ["input.json", "photo.png"]),
            (root / "app/tests/other/tests", [], ["test_nested.py"]),
        ]
        with patch.object(scan_project, "os_walk_safe", return_value=walk):
            result = scan_project.collect(root, max_scan_files=0)
        self.assertEqual(result["test_file_count"], 3)
