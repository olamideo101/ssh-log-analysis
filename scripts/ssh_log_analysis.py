from collections import defaultdict
import re

LOG_FILE = "/var/log/auth.log"

failed_logins = defaultdict(int)
successful_logins = defaultdict(int)

ip_pattern = re.compile(r"from (\d+\.\d+\.\d+\.\d+)")

def extract_ip(line: str):
    match = ip_pattern.search(line)
    return match.group(1) if match else None

with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
        ip = extract_ip(line)
        if not ip:
            continue

        # Failed SSH password attempts
        if "Failed password" in line:
            failed_logins[ip] += 1

        # Successful SSH logins
        # Common log text includes: "Accepted password for ..." or "Accepted publickey for ..."
        if "Accepted password" in line or "Accepted publickey" in line:
            successful_logins[ip] += 1

print("\n=== SSH Log Summary ===")

if failed_logins:
    print("\nSuspicious IP addresses (failed attempts >= 2):")
    flagged = False
    for ip, count in sorted(failed_logins.items(), key=lambda x: x[1], reverse=True):
        if count >= 2:
            print(f"- {ip}: {count} failed attempts")
            flagged = True
    if not flagged:
        print("- None based on the current threshold")
else:
    print("\nNo failed login attempts found.")

if successful_logins:
    print("\nSuccessful login IP addresses:")
    for ip, count in sorted(successful_logins.items(), key=lambda x: x[1], reverse=True):
        print(f"- {ip}: {count} successful logins")
else:
    print("\nNo successful logins found.")


