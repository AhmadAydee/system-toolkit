import unittest
from unittest.mock import patch

import system_information


class TestSystemInformation(unittest.TestCase):

    def test_returns_dictionary(self):
        result = system_information.get_system_information()
        self.assertIsInstance(result, dict)

    def test_contains_required_fields(self):
        result = system_information.get_system_information()

        expected_fields = [
            "Operating System",
            "OS Version",
            "Machine Architecture",
            "Python Version",
            "Device Hostname",
            "Current User",
            "CPU Count",
            "Report Generated",
        ]

        for field in expected_fields:
            with self.subTest(field=field):
                self.assertIn(field, result)

    def test_display_prints_report_heading(self):
        with patch("builtins.print") as mock_print:
            system_information.display_system_information()

        printed_text = "\n".join(
            str(call.args[0])
            for call in mock_print.call_args_list
        )

        self.assertIn("SYSTEM INFORMATION REPORT", printed_text)


if __name__ == "__main__":
    unittest.main()
