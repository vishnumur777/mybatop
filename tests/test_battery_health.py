import unittest
import os
import subprocess
import filecmp

class Test_Battery_Capacity(unittest.TestCase):
    src_file="src/mybatop/analyze/pythonscripts/battery_health.py"

    def setUp(self):

        subprocess.run(["cp","tests/test_files/data.csv", "."])

    def test_battery_capacity_html(self):

        expected_output = "tests/test_files/outputs/html/battery_health.html"

        result=subprocess.run(["python3", self.src_file, "--html"], capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists("battery_health.html"), "Output file battery_health.html was not created")

        if not filecmp.cmp("battery_health.html", expected_output):
            subprocess.run(["diff", expected_output, "battery_health.html"], check=True)

        self.assertTrue(
            filecmp.cmp("battery_health.html", expected_output), "Files are not identical"
        )

    def tearDown(self):
        if os.path.exists("data.csv"):
            os.remove("data.csv")
        if os.path.exists("battery_health.html"):
            os.remove("battery_health.html")
