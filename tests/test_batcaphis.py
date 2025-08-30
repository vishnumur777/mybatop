import subprocess
import filecmp
import os
import unittest

class TestBatcaphis(unittest.TestCase):
    src_file="src/mybatop/analyze/pythonscripts/batcaphis.py"

    def setUp(self):

        subprocess.run(["cp", "tests/test_files/data.csv", "."])

        os.makedirs(".temp_xml_files", exist_ok=True)
        os.makedirs(".temp_json_files", exist_ok=True)

    def test_batcaphis_html(self):

        expected_output = "tests/test_files/outputs/html/d.html"

        result=subprocess.run(["python3", self.src_file , "--html"], capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists("d.html"), "Output file d.html was not created")

        if not filecmp.cmp("d.html", expected_output):
            subprocess.run(["diff", expected_output, "d.html"], check=True)

        self.assertTrue(
            filecmp.cmp("d.html", expected_output), "Files are not identical"
        )

    def test_batcaphis_json(self):

        expected_output = "tests/test_files/outputs/json/batcaphis.json"

        result=subprocess.run(["python3", self.src_file , "--json"], capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists(".temp_json_files/batcaphis.json"), "Output file .temp_json_files/batcaphis.json was not created")

        if not filecmp.cmp(".temp_json_files/batcaphis.json", expected_output):
            subprocess.run(["diff", expected_output, ".temp_json_files/batcaphis.json"], check=True)

        self.assertTrue(
            filecmp.cmp(".temp_json_files/batcaphis.json", expected_output), "Files are not identical"
        )

    def test_batcaphis_xml(self):

        expected_output = "tests/test_files/outputs/xml/batcaphis.xml"

        result=subprocess.run(["python3", self.src_file , "--xml"], capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists(".temp_xml_files/batcaphis.xml"), "Output file .temp_xml_files/batcaphis.xml was not created")

        if not filecmp.cmp(".temp_xml_files/batcaphis.xml", expected_output):
            subprocess.run(["diff", expected_output, ".temp_xml_files/batcaphis.xml"], check=True)

        self.assertTrue(
            filecmp.cmp(".temp_xml_files/batcaphis.xml", expected_output), "Files are not identical"
        )

    def test_batcaphis_csv(self):

        expected_output = "tests/test_files/outputs/csv/batcaphis.csv"

        result=subprocess.run(["python3", self.src_file , "--csv"], capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists("batcaphis.csv"), "Output file batcaphis.csv was not created")

        if not filecmp.cmp("batcaphis.csv", expected_output):
            subprocess.run(["diff", expected_output, "batcaphis.csv"], check=True)

        self.assertTrue(
            filecmp.cmp("batcaphis.csv", expected_output), "Files are not identical"
        )

    def tearDown(self):
        if os.path.exists("data.csv"):
            os.remove("data.csv")
        if os.path.exists("d.html"):
            os.remove("d.html")
        if os.path.exists(".temp_json_files/batcaphis.json"):
            os.remove(".temp_json_files/batcaphis.json")
        if os.path.exists(".temp_xml_files/batcaphis.xml"):
            os.remove(".temp_xml_files/batcaphis.xml")
        if os.path.exists("batcaphis.csv"):
            os.remove("batcaphis.csv")
