import os
import platform
import shutil
import subprocess
from datetime import datetime


def get_command_output(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip() or "Information unavailable"
    except (OSError, subprocess.TimeoutExpired):
        return "Information unavailable"


def main():
    print("=" * 40)
    print("       SYSTEM DIAGNOSTICS TOOL")
    print("=" * 40)

    print("\n[1] Date and Time")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    print("\n[2] Operating System")
    print(platform.system())

    print("\n[3] Python Version")
    print(platform.python_version())

    print("\n[4] Machine Architecture")
    print(platform.machine())

    print("\n[5] Current Directory")
    print(os.getcwd())

    print("\n[6] Storage Information")
    usage = shutil.disk_usage(os.path.expanduser("~"))

    print(f"Total: {usage.total / (1024**3):.2f} GB")
    print(f"Used:  {usage.used / (1024**3):.2f} GB")
    print(f"Free:  {usage.free / (1024**3):.2f} GB")

    print("\n[7] Git Version")
    print(get_command_output(["git", "--version"]))

    print("\n[8] Curl Version")
    print(get_command_output(["curl", "--version"]).split("\n")[0])

    print("\n" + "=" * 40)
    print("Diagnostics completed.")
    print("=" * 40)


if __name__ == "__main__":
    main()

