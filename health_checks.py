import os
import shutil
import sys
import psutil

def check_reboot():
    """Return true if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
	"""Return True if there is enough space,false otherwise."""
	du = shutil.disk_usage(disk)
	# Calculate the percent of free space
	percent_free = 100 * du.free / du.total
	# Calculate how many free gigabytes
	gigabytes_free = du.free / 2**30
	if gigabytes_free < min_gb or percent_free < min_percent:
		return True
	return False

def check_root_full():
    """Return True if the root partition is full."""
    return check_disk_full(disk = "/", min_gb = 2, min_percent = 10)

def check_cpu_constrained():
	"""Returns True if the cpu is having too much usage,False otherwise"""
	return psutil.cpu_percent(1) > 75

def main():
    checks = [
        (check_reboot, "Pending Rebot"),
        (check_root_full, "Root partition full"),
        (check_cpu_constrained, "cpu is having too much usage")
    ]
    everything_ok = True
    for check,msg in checks:
        if check():
            print(msg)
            everything_ok = False

    if not everything_ok:
        sys.exit(1)

    print("Everything OK.")
    sys.exit(0)

main()

