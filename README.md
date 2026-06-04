# Log File Integrity Monitoring Tool

## Overview

The Log File Integrity Monitoring Tool is a Python-based cybersecurity utility designed to detect unauthorized modifications to log files using SHA-256 cryptographic hashing.

The tool creates a baseline hash for log files and compares future hashes against the stored values to identify potential tampering. It supports monitoring both individual log files and entire directories.

---

## Features

* SHA-256 cryptographic hashing
* Monitor a single log file or an entire directory
* Detect modified log files
* Detect newly added files
* Store baseline hashes in a JSON database
* Manual hash update functionality
* Command-line interface (CLI)
* Lightweight and easy to use

---

## Technologies Used

* Python 3
* hashlib
* json
* argparse
* os

---

## Project Structure

```text
LogIntegrityTool/
│
├── integrity_check.py
├── hashes.json
├── sample_logs/
│   └── test.log
├── README.md
```

---

## How It Works

### Initialization

The tool calculates SHA-256 hashes for the specified files and stores them as a trusted baseline.

```bash
python3 integrity_check.py init test.log
```

Example Output:

```text
Hashes stored successfully.
```

---

### Integrity Check

The tool recalculates file hashes and compares them with the stored baseline.

```bash
python3 integrity_check.py check test.log
```

Example Output:

```text
test.log : Unmodified
```

If a file has been changed:

```text
test.log : Modified (Hash mismatch)
```

---

### Update Stored Hash

If changes to a file are legitimate, update the stored baseline hash.

```bash
python3 integrity_check.py update test.log
```

Example Output:

```text
Hash updated successfully.
```

---

## Example Workflow

1. Create a log file.

```bash
echo "User logged in" > test.log
```

2. Initialize baseline hashes.

```bash
python3 integrity_check.py init test.log
```

3. Modify the file.

```bash
echo "Failed login attempt" >> test.log
```

4. Check integrity.

```bash
python3 integrity_check.py check test.log
```

Output:

```text
test.log : Modified (Hash mismatch)
```

---

## Cybersecurity Concepts Demonstrated

* File Integrity Monitoring (FIM)
* Cryptographic Hashing
* SHA-256 Algorithm
* Security Monitoring
* Tamper Detection
* Log File Protection

---

## Future Improvements

* SQLite database support
* Real-time file monitoring
* Email alert notifications
* HMAC-based hash protection
* PDF security reports
* Web dashboard for monitoring

---

## Learning Outcomes

This project helped develop practical knowledge in:

* Python scripting
* Cybersecurity fundamentals
* File handling
* Hashing algorithms
* Command-line application development
* Security monitoring techniques

---

## Author

Gayathri Silva

Cyber Security Undergraduate | Security Enthusiast
