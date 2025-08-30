import unittest
import os
import subprocess
import filecmp

class Test_Battery_Health(unittest.TestCase):
    src_file="src/mybatop/analyze/pythonscripts/battery_health.py"

    def setUp(self):

        subprocess.run(["cp","tests/test_files/data.csv", "."])

        os.makedirs(".temp_xml_files", exist_ok=True)
        os.makedirs(".temp_json_files", exist_ok=True)
    def test_battery_health_html(self):

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

    def test_battery_health_json(self):

        expected_output = "tests/test_files/outputs/json/.temp_json_files/battery_health.json"

        result=subprocess.run(["python3", self.src_file, "--json"], capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists(".temp_json_files/battery_health.json"), "Output file battery_health.json was not created")

        if not filecmp.cmp(".temp_json_files/battery_health.json", expected_output):
            subprocess.run(["diff", expected_output, ".temp_json_files/battery_health.json"], check=True)

        self.assertTrue(
            filecmp.cmp(".temp_json_files/battery_health.json", expected_output), "Files are not identical"
        )

    def test_battery_health_xml(self):

        expected_output = "tests/test_files/outputs/xml/.temp_xml_files/battery_health.xml"

        result=subprocess.run(["python3", self.src_file, "--xml"], capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists(".temp_xml_files/battery_health.xml"), "Output file battery_health.xml was not created")

        if not filecmp.cmp(".temp_xml_files/battery_health.xml", expected_output):
            subprocess.run(["diff", expected_output, ".temp_xml_files/battery_health.xml"], check=True)

        self.assertTrue(
            filecmp.cmp(".temp_xml_files/battery_health.xml", expected_output), "Files are not identical"
        )

    def test_battery_health_csv(self):

        expected_output = "tests/test_files/outputs/csv/battery_health.csv"

        result=subprocess.run(["python3", self.src_file, "--csv"], capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists("battery_health.csv"), "Output file battery_health.csv was not created")

        if not filecmp.cmp("battery_health.csv", expected_output):
            subprocess.run(["diff", expected_output, "battery_health.csv"], check=True)

        self.assertTrue(
            filecmp.cmp("battery_health.csv", expected_output), "Files are not identical"
        )

    def tearDown(self):
        if os.path.exists("data.csv"):
            os.remove("data.csv")
        if os.path.exists("battery_health.html"):
            os.remove("battery_health.html")
        if os.path.exists(".temp_json_files/battery_health.json"):
            os.remove(".temp_json_files/battery_health.json")
        if os.path.exists(".temp_xml_files/battery_health.xml"):
            os.remove(".temp_xml_files/battery_health.xml")
        if os.path.exists("battery_health.csv"):
            os.remove("battery_health.csv")