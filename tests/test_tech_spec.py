import unittest
import subprocess
import filecmp
import os


class TestTechSpec(unittest.TestCase):
    src_file = "src/mybatop/analyze/pythonscripts/tech_spec.py"

    def setUp(self):
        subprocess.run(["cp", "tests/test_files/data.csv", "."], check=True)

    def test_tech_spec_html(self):
        expected_output = "tests/test_files/outputs/html/c.html"

        result = subprocess.run(
            ["python3", self.src_file, "--html"], capture_output=True, text=True
        )

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists("b.html"), "Output file b.html was not created")

        self.assertTrue(
            filecmp.cmp("b.html", expected_output), "Files are not identical"
        )

        if not filecmp.cmp("b.html", expected_output):
            subprocess.run(["diff", expected_output, "b.html"], check=True)

    def tearDown(self):
        if os.path.exists("data.csv"):
            os.remove("data.csv")
        if os.path.exists("b.html"):
            os.remove("b.html")
