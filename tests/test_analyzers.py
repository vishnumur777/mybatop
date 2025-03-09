import unittest
import filecmp
import subprocess
import os


class TestAnalyzer(unittest.TestCase):
    src_file = "src/mybatop/analyze/pythonscripts/analyzers.py"

    def setUp(self):
        subprocess.run(["cp", "tests/test_files/data.csv", "."], check=True)

    def test_analyzer_html(self):
        expected_output = "tests/test_files/outputs/html/b.html"

        result = subprocess.run(
            ["python3", self.src_file, "--html"], capture_output=True, text=True
        )

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists("a.html"), "Output file a.html was not created")

        if not filecmp.cmp("a.html", expected_output):
            subprocess.run(["diff", "a.html", expected_output])
        
        self.assertTrue(
            filecmp.cmp("a.html", expected_output), "Files are not identical"
        )

    def tearDown(self):
        if os.path.exists("data.csv"):
            os.remove("data.csv")
        if os.path.exists("a.html"):
            os.remove("a.html")
