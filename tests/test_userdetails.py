import unittest
import filecmp
import os
import subprocess

expected_output = "tests/test_files/outputs/html/a0.html"
src_file = "src/mybatop/analyze/pythonscripts/userdetails.py"


class TestUserDetails(unittest.TestCase):
    def setUp(self):
        subprocess.run(["cp", "tests/test_files/details.csv", "."], check=True)

    def test_userdetails(self):
        result = subprocess.run(["python3", src_file], capture_output=True, text=True)

        self.assertEqual(
            result.returncode,
            0,
            f"Script execution failed with error:\n{result.stderr}",
        )

        self.assertTrue(
            os.path.exists("a0.html"), "Output file a0.html was not created"
        )

        if not filecmp.cmp("a0.html", expected_output):
            subprocess.run(["diff", "a0.html", expected_output])

        self.assertTrue(
            filecmp.cmp("a0.html", expected_output), "Files are not identical"
        )

    def tearDown(self):
        if os.path.exists("details.csv"):
            os.remove("details.csv")
        if os.path.exists("a0.html"):
            os.remove("a0.html")


if __name__ == "__main__":
    unittest.main()
