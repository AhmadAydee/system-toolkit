import platform
import os
import getpass
import socket
from datetime import datetime


def get_system_information():
    """Collect basic system information."""

    information = {
        "Operating System": platform.system(),
        "OS Version": platform.release(),
        "Machine Architecture": platform.machine(),
        "Python Version": platform.python_version(),
        "Device Hostname": socket.gethostname(),
        "Current User": getpass.getuser(),
        "CPU Count": os.cpu_count(),
        "Report Generated": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
    }

    return information


def display_system_information():
    """Display the collected information."""

    information = get_system_information()

    print("\n" + "=" * 45)
    print("       SYSTEM INFORMATION REPORT")
    print("=" * 45)

    for key, value in information.items():
        print(f"{key:<24}: {value}")

    print("=" * 45)


if __name__ == "__main__":
    display_system_information()
