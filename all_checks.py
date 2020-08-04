import os
import shutil
import sys

def check_reboot():
    """Return true if the computer has a pending reboot."""
    return os.path.exit("/run/reboot-required")

def check_disk_usage(disk, min_gb, min_percent):
	"""Return True if there is enough space,false otherwise."""
	du = shutil.disk_usage(disk)
	# Calculate the percent of free space
	percent_free = 100 * du.free/du.total
	# Calculate how many free gigabytes
	gigabytes_free = du.free/2**30
	if gigabytes_free < min_gb or percent_free < min_percent:
		return True
	return False

def main():
    if check_reboot():
        print("Pending reboot.")
            sys.exit(1)
    if check_disk_usage(disk = "/", min_gb = 2, min_percent = 10):
        print("Disk full.")
        sys.exit(1)

    print("Everything OK.")
    sys.exit(0)

main()
