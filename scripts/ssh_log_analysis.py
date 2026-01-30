from collections import defaultdict
import re

log_file = "/var/log/auth.log"
failed_logins = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            if match:
                ip = match.group(1)
                failed_logins[ip] += 1

print("Suspicious IP addresses:")
for ip, count in failed_logins.items():
    if count >= 2:
        print(f"{ip} had {count} failed login attempts")

