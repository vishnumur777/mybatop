import unittest
import filecmp
import subprocess
import os


class TestAnalyzer(unittest.TestCase):
    src_file = "src/mybatop/analyze/pythonscripts/analyzers.py"

    def setUp(self):
        subprocess.run(["cp", "tests/test_files/data.csv", "."], check=True)

    def test_analyzer_html(self):
        expected_output = "tests/test_files/outputs/html/a.html"

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

    def test_analyzer_json(self):
        expected_output = "tests/test_files/outputs/json/.temp_json_files/recent_usage.json"

        result = subprocess.run(
            ["python3", self.src_file, "--json"], capture_output=True, text=True
        )

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists(".temp_json_files/recent_usage.json"), "Output file recent_uage.json was not created")

        if not filecmp.cmp(".temp_json_files/recent_usage.json", expected_output):
            subprocess.run(["diff", ".temp_json_files/recent_usage.json", expected_output])
        
        self.assertTrue(
            filecmp.cmp(".temp_json_files/recent_usage.json", expected_output), "Files are not identical"
        )

    def test_analyzer_xml(self):
        expected_output = "tests/test_files/outputs/xml/.temp_xml_files/recent_usage.xml"

        result = subprocess.run(
            ["python3", self.src_file, "--xml"], capture_output=True, text=True
        )

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists(".temp_xml_files/recent_usage.xml"), "Output file .temp_xml_files/recent_usage.xml was not created")

        if not filecmp.cmp(".temp_xml_files/recent_usage.xml", expected_output):
            subprocess.run(["diff", ".temp_xml_files/recent_usage.xml", expected_output])
        
        self.assertTrue(
            filecmp.cmp(".temp_xml_files/recent_usage.xml", expected_output), "Files are not identical"
        )

    def test_analyzer_csv(self):
        expected_output = "tests/test_files/outputs/csv/recent_usage.csv"

        result = subprocess.run(
            ["python3", self.src_file, "--csv"], capture_output=True, text=True
        )

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists("recent_usage.csv"), "Output file recent_usage.csv was not created")

        if not filecmp.cmp("recent_usage.csv", expected_output):
            subprocess.run(["diff", "recent_usage.csv", expected_output])
        
        self.assertTrue(
            filecmp.cmp("recent_usage.csv", expected_output), "Files are not identical"
        )

    def tearDown(self):
        if os.path.exists("data.csv"):
            os.remove("data.csv")
        if os.path.exists("a.html"):
            os.remove("a.html")
        if os.path.exists(".temp_json_files/recent_usage.json"):
            os.remove(".temp_json_files/recent_usage.json")
        if os.path.exists(".temp_xml_files/recent_usage.xml"):
            os.remove(".temp_xml_files/recent_usage.xml")
        if os.path.exists("recent_usage.csv"):
            os.remove("recent_usage.csv")