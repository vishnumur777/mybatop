import filecmp
import os
import unittest
import subprocess

class TestCycleCount(unittest.TestCase):
    src_file="src/mybatop/analyze/pythonscripts/cycle_counts.py"

    def setUp(self):
        subprocess.run(["cp", "tests/test_files/data.csv", "."])

        os.makedirs(".temp_xml_files", exist_ok=True)
        os.makedirs(".temp_json_files", exist_ok=True)
        
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

    def test_cycle_count_json(self):
        
        expected_output = "tests/test_files/outputs/json/.temp_json_files/cycle_counts.json"

        result=subprocess.run(["python3", self.src_file, "--json"], capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists(".temp_json_files/cycle_counts.json"), "Output file cycle_counts.json was not created")

        if not filecmp.cmp(".temp_json_files/cycle_counts.json", expected_output):
            subprocess.run(["diff", expected_output, ".temp_json_files/cycle_counts.json"], check=True)

        self.assertTrue(
            filecmp.cmp(".temp_json_files/cycle_counts.json", expected_output), "Files are not identical"
        )

    def test_cycle_count_xml(self):
        
        expected_output = "tests/test_files/outputs/xml/.temp_xml_files/cycle_count.xml"

        result=subprocess.run(["python3", self.src_file, "--xml"], capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists(".temp_xml_files/cycle_count.xml"), "Output file cycle_counts.xml was not created")

        if not filecmp.cmp(".temp_xml_files/cycle_count.xml", expected_output):
            subprocess.run(["diff", expected_output, ".temp_xml_files/cycle_count.xml"], check=True)

        self.assertTrue(
            filecmp.cmp(".temp_xml_files/cycle_count.xml", expected_output), "Files are not identical"
        )

    def test_cycle_count_csv(self):
        
        expected_output = "tests/test_files/outputs/csv/cycle_count.csv"

        result=subprocess.run(["python3", self.src_file, "--csv"], capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists("cycle_count.csv"), "Output file cycle_count.csv was not created")

        if not filecmp.cmp("cycle_count.csv", expected_output):
            subprocess.run(["diff", expected_output, "cycle_count.csv"], check=True)

        self.assertTrue(
            filecmp.cmp("cycle_count.csv", expected_output), "Files are not identical"
        )

    def tearDown(self):
        if os.path.exists("data.csv"):
            os.remove("data.csv")
        if os.path.exists("cycle_count.html"):
            os.remove("cycle_count.html")
        if os.path.exists(".temp_json_files/cycle_counts.json"):
            os.remove(".temp_json_files/cycle_counts.json")
        if os.path.exists(".temp_xml_files/cycle_count.xml"):
            os.remove(".temp_xml_files/cycle_count.xml")
        if os.path.exists("cycle_count.csv"):
            os.remove("cycle_count.csv")


