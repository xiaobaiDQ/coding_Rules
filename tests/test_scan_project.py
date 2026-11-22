import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import scan_project


class ScanProjectTests(unittest.TestCase):
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
