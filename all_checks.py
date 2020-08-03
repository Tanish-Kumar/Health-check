import os
import sys

def check_reboot():
    """Return true if the computer has a pending reboot."""
    return os.path.exit("/run/reboot-required")
def main():
    if check_reboot():
        print("Pending reboot.")
        sys.exit(1)
    else:
        print("everything is OK.")


main()
