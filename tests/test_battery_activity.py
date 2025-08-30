import filecmp
import unittest
import os
import subprocess

class TestBatteryActivity(unittest.TestCase):
    src_file="src/mybatop/analyze/pythonscripts/battery_activity.py"
    def setUp(self):
        
        subprocess.run(["cp","tests/test_files/data.csv","."])

        subprocess.run(["cp", "tests/test_files/batusageact.csv","."])

        os.makedirs(".temp_xml_files", exist_ok=True)
        os.makedirs(".temp_json_files", exist_ok=True)

    def test_battery_activity_html(self):

        expected_output = "tests/test_files/outputs/html/g.html"

        result=subprocess.run(["python3",self.src_file, "--html"],capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}"
        )

        self.assertTrue(os.path.exists("g.html"),"File g.html does not exists")

        if not filecmp.cmp("g.html",expected_output):
            subprocess.run(["diff", "g.html", expected_output])

        self.assertTrue(filecmp.cmp("g.html",expected_output),"Files are not identical.")

    def test_battery_activity_json(self):

        expected_output = "tests/test_files/outputs/json/battery_activity.json"

        result=subprocess.run(["python3",self.src_file, "--json"],capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}"
        )

        self.assertTrue(os.path.exists(".temp_json_files/battery_activity.json"),"File battery_activity.json does not exists")

        if not filecmp.cmp(".temp_json_files/battery_activity.json",expected_output):
            subprocess.run(["diff", expected_output, ".temp_json_files/battery_activity.json"], check=True)

        self.assertTrue(filecmp.cmp(".temp_json_files/battery_activity.json",expected_output),"Files are not identical.")

    def test_battery_activity_xml(self):

        expected_output = "tests/test_files/outputs/xml/battery_activity.xml"

        result=subprocess.run(["python3",self.src_file, "--xml"],capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}"
        )

        self.assertTrue(os.path.exists(".temp_xml_files/battery_activity.xml"),"File battery_activity.xml does not exists")

        if not filecmp.cmp(".temp_xml_files/battery_activity.xml",expected_output):
            subprocess.run(["diff", expected_output, ".temp_xml_files/battery_activity.xml"], check=True)

        self.assertTrue(filecmp.cmp(".temp_xml_files/battery_activity.xml",expected_output),"Files are not identical.")

    def test_battery_activity_csv(self):

        expected_output = "tests/test_files/outputs/csv/battery_activity.csv"

        result=subprocess.run(["python3",self.src_file, "--csv"],capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}"
        )

        self.assertTrue(os.path.exists("battery_activity.csv"),"File battery_activity.csv does not exists")

        if not filecmp.cmp("battery_activity.csv",expected_output):
            subprocess.run(["diff", expected_output, "battery_activity.csv"], check=True)

        self.assertTrue(filecmp.cmp("battery_activity.csv",expected_output),"Files are not identical.")

    def tearDown(self):
        if os.path.exists("data.csv"):
            os.remove("data.csv")
        if os.path.exists("batusageact.csv"):
            os.remove("batusageact.csv")
        if os.path.exists("g.html"):
            os.remove("g.html")
        if os.path.exists(".temp_json_files/battery_activity.json"):
            os.remove(".temp_json_files/battery_activity.json")
        if os.path.exists(".temp_xml_files/battery_activity.xml"):
            os.remove(".temp_xml_files/battery_activity.xml")
        if os.path.exists("battery_activity.csv"):
            os.remove("battery_activity.csv")
