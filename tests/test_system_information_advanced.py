import re
import unittest
from unittest.mock import patch

import system_information


class TestSystemInformationAdvanced(unittest.TestCase):

    @patch("system_information.platform.system", return_value="Android")
    @patch("system_information.platform.release", return_value="12")
    @patch("system_information.platform.machine", return_value="aarch64")
    @patch("system_information.platform.python_version", return_value="3.12.0")
    @patch("system_information.socket.gethostname", return_value="test-device")
    @patch("system_information.getpass.getuser", return_value="test-user")
    @patch("system_information.os.cpu_count", return_value=8)
    @patch("system_information.datetime")
    def test_returns_controlled_system_information(
        self,
        mock_datetime,
        mock_cpu_count,
        mock_getuser,
        mock_hostname,
        mock_python_version,
        mock_machine,
        mock_release,
        mock_system,
    ):
        mock_datetime.now.return_value.strftime.return_value = (
            "2026-10-24 12:30:00"
        )

        result = system_information.get_system_information()

        self.assertEqual(result["Operating System"], "Android")
        self.assertEqual(result["OS Version"], "12")
        self.assertEqual(result["Machine Architecture"], "aarch64")
        self.assertEqual(result["Python Version"], "3.12.0")
        self.assertEqual(result["Device Hostname"], "test-device")
        self.assertEqual(result["Current User"], "test-user")
        self.assertEqual(result["CPU Count"], 8)
        self.assertEqual(
            result["Report Generated"],
            "2026-10-24 12:30:00",
        )

    @patch("system_information.os.cpu_count", return_value=None)
    def test_handles_unknown_cpu_count(self, mock_cpu_count):
        result = system_information.get_system_information()

        self.assertIsNone(result["CPU Count"])

    def test_report_timestamp_has_expected_format(self):
        result = system_information.get_system_information()

        timestamp = result["Report Generated"]

        self.assertRegex(
            timestamp,
            re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"),
        )

    @patch("system_information.get_system_information")
    @patch("builtins.print")
    def test_display_uses_collected_information(
        self,
        mock_print,
        mock_get_information,
    ):
        mock_get_information.return_value = {
            "Operating System": "TestOS",
            "CPU Count": 4,
        }

        system_information.display_system_information()

        mock_get_information.assert_called_once()

        printed_text = "\n".join(
            str(call.args[0])
            for call in mock_print.call_args_list
            if call.args
        )

        self.assertIn("SYSTEM INFORMATION REPORT", printed_text)
        self.assertIn("TestOS", printed_text)
        self.assertIn("CPU Count", printed_text)


if __name__ == "__main__":
    unittest.main()
