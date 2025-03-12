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

    def test_dchar_json(self):
        expected_output = "tests/test_files/outputs/json/average_capacity.json"

        result=subprocess.run(["python3", self.src_file, "--json"],capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists("average_capacity.json"), "Output file average_capacity.json was not created")

        if not filecmp.cmp("average_capacity.json", expected_output):
            subprocess.run(["diff", expected_output, "average_capacity.json"], check=True)

        self.assertTrue(
            filecmp.cmp("average_capacity.json", expected_output), "Files are not identical"
        )
    
    def test_dchar_xml(self):
        expected_output = "tests/test_files/outputs/xml/Average_capacity.xml"

        result=subprocess.run(["python3", self.src_file, "--xml"],capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists("Average_capacity.xml"), "Output file Average_capacity.xml was not created")

        if not filecmp.cmp("Average_capacity.xml", expected_output):
            subprocess.run(["diff", expected_output, "Average_capacity.xml"], check=True)

        self.assertTrue(
            filecmp.cmp("Average_capacity.xml", expected_output), "Files are not identical"
        )

    def test_dchar_csv(self):
        expected_output = "tests/test_files/outputs/csv/Average_capacity.csv"

        result=subprocess.run(["python3", self.src_file, "--csv"],capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists("Average_capacity.csv"), "Output file Average_capacity.csv was not created")

        if not filecmp.cmp("Average_capacity.csv", expected_output):
            subprocess.run(["diff", expected_output, "Average_capacity.csv"], check=True)

        self.assertTrue(
            filecmp.cmp("Average_capacity.csv", expected_output), "Files are not identical"
        )

    def tearDown(self):
        if os.path.exists("data.csv"):
            os.remove("data.csv")
        if os.path.exists("Average_capacity.html"):
            os.remove("Average_capacity.html")
        if os.path.exists("average_capacity.json"):
            os.remove("average_capacity.json")
        if os.path.exists("Average_capacity.xml"):
            os.remove("Average_capacity.xml")
        if os.path.exists("Average_capacity.csv"):
            os.remove("Average_capacity.csv")
