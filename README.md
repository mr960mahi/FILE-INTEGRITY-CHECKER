# 🔐 FILE-INTEGRITY-CHECKER

**Company**: CodTech IT Solutions
**Intern Name**: Kasagoni Mahesh
**Intern ID**: CT06DM1440
**Domain**: Cyber Security & Ethical Hacking
**Duration**: 4 Weeks
**Mentor**: Neela Santosh

---

## 📌 Project Overview

This File Integrity Checker is a Python-based tool designed to monitor and track changes in files by calculating and comparing their **cryptographic hash values** (SHA-256). It ensures file authenticity by detecting unauthorized additions, deletions, or modifications.

This tool was built as part of a cybersecurity internship at **CodTech IT Solutions**, under the guidance of domain experts, and follows practical, real-world use cases commonly found in enterprise-grade intrusion detection and system auditing solutions.

---

## ⚙️ How It Works

* On the first run, the script prompts the user to **input the folder path** they want to monitor.
* It recursively scans all files within the specified folder, calculates SHA-256 hashes, and stores them in a local JSON file (`file_hashes.json`) for future comparison.
* On subsequent runs, it compares the newly generated hashes with the saved ones and highlights:

  * 🆕 **New files added**
  * ❌ **Files deleted**
  * ✏️ **Files modified**

This process helps detect unauthorized file activity and provides a lightweight form of file integrity monitoring.

---

## 🚀 Running the Tool

1. Clone this repository or download the script.

2. Run the script using Python:

   ```bash
   python file_integrity_checker.py
   ```

3. Enter the full path to the folder you want to monitor when prompted.

4. The script will:

   * Display each file's path and corresponding hash.
   * Save these hash values in `file_hashes.json`.
   * Show differences if any changes are detected in future runs.

---

## 📸 Sample Output Screenshots

### 🔍 First Run — Initial Hash Calculation

The tool scans the directory and prints each file’s SHA-256 hash:

![Initial Scan](https://github.com/user-attachments/assets/b7b8410b-055f-4e1e-a4ca-a811deed334b)

---

### ✏️ Second Run — After Adding, Modifying, and Deleting Files

The tool highlights any changes:

* New files detected
* Modified files identified via changed hash values
* Deleted files flagged

![Changes Detected](https://github.com/user-attachments/assets/5008bee4-0813-4ba5-9244-513893b4d4f4)

---

### ✅ Third Run — No Changes Detected

If no changes are made, the tool confirms that all files are intact:

![No Changes](https://github.com/user-attachments/assets/22e2f5e8-14ec-4eb8-b763-f38b8cc5defb)

---

## 🔒 Why This Matters in Cybersecurity

File integrity monitoring (FIM) is a critical layer in cyber defense. Unauthorized changes to files may indicate:

* Malware infection
* Insider threats
* Data corruption
* Unauthorized access

By monitoring file hashes, we can ensure system integrity, detect anomalies early, and enforce compliance with security standards like **PCI-DSS**, **HIPAA**, and **ISO/IEC 27001**.

---

## 📁 Output File

* Hashes are stored in:

  ```
  file_hashes.json
  ```

* You can inspect or reset this file as needed to redefine your baseline.

---

## 👨‍💻 Technologies Used

* `Python 3`
* `hashlib` for secure SHA-256 hashing
* `os` and `json` for file operations and data persistence

---

## 📢 Author's Note

This project reflects a simplified yet powerful implementation of real-world FIM tools. It is designed to be extensible and can serve as a base for integrating advanced features such as:

* Email alerts
* Real-time file system hooks
* Scheduled scans via task schedulers or CRON jobs
* GUI or web-based dashboards

---

## 📜 License

This tool is developed as part of a learning project and is free to use for educational and non-commercial purposes.

---
