import unittest
import subprocess
import filecmp
import os


class TestTechSpec(unittest.TestCase):
    src_file = "src/mybatop/analyze/pythonscripts/tech_spec.py"

    def setUp(self):
        subprocess.run(["cp", "tests/test_files/data.csv", "."], check=True)

        os.makedirs(".temp_xml_files", exist_ok=True)
        os.makedirs(".temp_json_files", exist_ok=True)

    def test_tech_spec_html(self):
        expected_output = "tests/test_files/outputs/html/b.html"

        result = subprocess.run(
            ["python3", self.src_file, "--html"], capture_output=True, text=True
        )

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists("b.html"), "Output file b.html was not created")

        self.assertTrue(
            filecmp.cmp("b.html", expected_output), "Files are not identical"
        )

        if not filecmp.cmp("b.html", expected_output):
            subprocess.run(["diff", expected_output, "b.html"], check=True)

    def test_tech_spec_json(self):
        expected_output = "tests/test_files/outputs/json/tech_spec.json"

        result = subprocess.run(
            ["python3", self.src_file, "--json"], capture_output=True, text=True
        )

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists(".temp_json_files/tech_spec.json"), "Output file tech_spec.json was not created")

        if not filecmp.cmp(".temp_json_files/tech_spec.json", expected_output):
            subprocess.run(["diff", expected_output, ".temp_json_files/tech_spec.json"], check=True)

        self.assertTrue(
            filecmp.cmp(".temp_json_files/tech_spec.json", expected_output), "Files are not identical"
        )

    def test_tech_spec_xml(self):
        expected_output = "tests/test_files/outputs/xml/tech_spec.xml"

        result = subprocess.run(
            ["python3", self.src_file, "--xml"], capture_output=True, text=True
        )

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists(".temp_xml_files/tech_spec.xml"), "Output file tech_spec.xml was not created")

        if not filecmp.cmp(".temp_xml_files/tech_spec.xml", expected_output):
            subprocess.run(["diff", expected_output, ".temp_xml_files/tech_spec.xml"], check=True)

        self.assertTrue(
            filecmp.cmp(".temp_xml_files/tech_spec.xml", expected_output), "Files are not identical"
        )

    def test_tech_spec_csv(self):
        expected_output = "tests/test_files/outputs/csv/tech_spec.csv"

        result = subprocess.run(
            ["python3", self.src_file, "--csv"], capture_output=True, text=True
        )

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(os.path.exists("tech_spec.csv"), "Output file tech_spec.csv was not created")

        if not filecmp.cmp("tech_spec.csv", expected_output):
            subprocess.run(["diff", expected_output, "tech_spec.csv"], check=True)

        self.assertTrue(
            filecmp.cmp("tech_spec.csv", expected_output), "Files are not identical"
        )

    def tearDown(self):
        if os.path.exists("data.csv"):
            os.remove("data.csv")
        if os.path.exists("b.html"):
            os.remove("b.html")
        if os.path.exists(".temp_json_files/tech_spec.json"):
            os.remove(".temp_json_files/tech_spec.json")
        if os.path.exists(".temp_xml_files/tech_spec.xml"):
            os.remove(".temp_xml_files/tech_spec.xml")
