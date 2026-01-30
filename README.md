Objectives

The main objectives of this project were to:

Understand how SSH authentication events are recorded on Linux systems

Practice reading and interpreting authentication logs

Detect repeated failed login attempts that may indicate brute force activity

Identify successful SSH logins and their source IP addresses

Automate log analysis using Python to reduce manual effort

Environment

This project was completed in the following environment:

Ubuntu Linux

OpenSSH server

Authentication logs located in /var/log/auth.log

Tools and Technologies

Python

Linux and Unix command line

OpenSSH

Regular expressions for log parsing

Git and GitHub for version control

Approach

The project followed a structured investigation and automation process:

Inspected the SSH service status and configuration to understand how the service was running

Analyzed authentication logs manually using Linux commands to identify patterns and log structure

Identified key log entries related to failed and successful SSH authentication

Developed a Python script to automatically parse logs and summarize activity

Validated results by comparing script output with manual log inspection

This approach demonstrates both foundational system knowledge and the ability to automate repetitive security tasks.

Script Functionality

The Python script performs the following actions:

Reads the SSH authentication log file

Extracts IP addresses associated with authentication attempts

Counts failed login attempts per IP address

Tracks successful SSH logins

Flags IP addresses with repeated failed login attempts based on a threshold

Outputs a readable summary of SSH activity

The script is designed to be simple, readable, and easy to extend with additional detection logic.

Sample Output

A typical execution of the script produces a summary similar to the following:

=== SSH Log Summary ===

Suspicious IP addresses (failed attempts >= 2):
- X.X.X.X: 3 failed attempts

No successful logins found.


A full example of script output is available in:

notes/sample_output.txt

Project Structure
ssh-log-analysis/
├─ README.md
├─ scripts/
│  └─ ssh_log_analysis.py
└─ notes/
   ├─ commands.md
   └─ sample_output.txt

Documentation Notes

The notes directory contains supporting documentation for the project:

commands.md documents the Linux commands used during manual analysis

sample_output.txt contains captured output from the Python script

This documentation helps explain the investigation process and provides transparency into how conclusions were reached.

Security Context

SSH log analysis is a common task in security operations, system administration, and incident response. Reviewing authentication logs helps detect:

Brute force login attempts

Unauthorized access attempts

Misconfigured services

Unusual authentication behavior

This project demonstrates foundational skills used in security monitoring and defensive security roles.

What I Learned

Through this project, I learned how to:

Navigate and analyze Linux authentication logs

Understand SSH authentication behavior

Identify suspicious patterns in login activity

Automate log analysis using Python

Document technical work clearly for others to understand

Future Improvements

Potential future enhancements include:

Adding alerting when failed login thresholds are exceeded

Exporting results to CSV for reporting

Supporting log analysis from multiple systems

Integrating log ingestion from cloud environments

Conclusion

This project demonstrates hands on experience with Linux systems, SSH authentication, and basic security monitoring techniques. It highlights the ability to combine manual investigation with automation, which is a core skill in cybersecurity and IT roles.
