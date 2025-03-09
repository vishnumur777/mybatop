import subprocess
import filecmp
import os
import unittest

class TestBatcaphis(unittest.TestCase):
    src_file="src/mybatop/analyze/pythonscripts/batcaphis.py"

    def setUp(self):

        subprocess.run(["cp", "tests/test_files/data.csv", "."])

    def test_batcaphis(self):

        expected_output = "tests/test_files/outputs/html/d.html"

        result=subprocess.run(["python3", self.src_file , "--html"], capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists("d.html"), "Output file d.html was not created")

        if not filecmp.cmp("d.html", expected_output):
            subprocess.run(["diff", expected_output, "e.html"], check=True)

        self.assertTrue(
            filecmp.cmp("d.html", expected_output), "Files are not identical"
        )

    def tearDown(self):
        if os.path.exists("data.csv"):
            os.remove("data.csv")
            os.remove("batusageact.csv")
        if os.path.exists("d.html"):
            os.remove("d.html")
