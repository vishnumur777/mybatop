import filecmp
import os
import unittest
import subprocess

class TestCycleCount(unittest.TestCase):
    src_file="src/mybatop/analyze/pythonscripts/cycle_counts.py"

    def setUp(self):
        subprocess.run(["cp", "tests/test_files/data.csv", "."])

    def test_cycle_count_html(self):
        
        expected_output = "tests/test_files/outputs/html/cycle_count.html"

        result=subprocess.run(["python3", self.src_file, "--html"], capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists("cycle_count.html"), "Output file cycle_count.html was not created")

        if not filecmp.cmp("cycle_count.html", expected_output):
            subprocess.run(["diff", expected_output, "cycle_count.html"], check=True)

        self.assertTrue(
            filecmp.cmp("cycle_count.html", expected_output), "Files are not identical"
        )

    def tearDown(self):
        if os.path.exists("data.csv"):
            os.remove("data.csv")
        if os.path.exists("cycle_count.html"):
            os.remove("cycle_count.html")


    