import unittest
import os
import subprocess
import filecmp

class TestDchar(unittest.TestCase):
    src_file = "src/mybatop/analyze/pythonscripts/dchar.py"

    def setUp(self):

        subprocess.run(["cp", "tests/test_files/data.csv", "."], check=True)

    def test_dchar_html(self):
        expected_output = "tests/test_files/outputs/html/Average_capacity.html"

        result=subprocess.run(["python3", self.src_file, "--html"],capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists("Average_capacity.html"), "Output file Average_capacity.html was not created")

        if not filecmp.cmp("Average_capacity.html", expected_output):
            subprocess.run(["diff", expected_output, "Average_capacity.html"], check=True)

        self.assertTrue(
            filecmp.cmp("Average_capacity.html", expected_output), "Files are not identical"
        )

    def tearDown(self):
        if os.path.exists("data.csv"):
            os.remove("data.csv")
        if os.path.exists("Average_capacity.html"):
            os.remove("Average_capacity.html")
