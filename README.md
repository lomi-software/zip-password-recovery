# zip-password-recovery

A Python-based CLI tool for recovering forgotten ZIP passwords using constrained brute-force and mask-style attacks.
Designed for **educational purposes and authorized password recovery only**.

---

## ⚠️ Legal & Ethical Notice

This tool is intended **ONLY** for:
- ZIP files you **own**
- ZIP files you are **explicitly authorized** to test

Unauthorized password recovery may be illegal and unethical.
Use responsibly.

---

## Key Characteristics

- ✔ CLI-first (bash-style command)
- ✔ Uses Python standard library (`zipfile`)
- ✔ Constrained brute-force (letters + digits + chosen symbols)
- ✔ Prints recovered password in plain text
- ❌ Does NOT crack hashes
- ❌ Does NOT bypass strong encryption
- ❌ Not suitable for modern AES-256 ZIPs with long random passwords

---

## How It Works (High Level)

1. Generate password candidates using:
   - length range
   - custom character set
2. Try each candidate against the ZIP
3. Stop when extraction succeeds

> ZIP encryption is not broken — passwords are **tested**, not decrypted.

---

## Project Structure

```text
zip-password-recovery/
├── crack_zip            # executable CLI command
├── cracker.py           # Python core logic
├── test/
│   ├── sample.zip       # test archive (password protected)
│   └── README.md
├── requirements.txt
├── README.md
└── .gitignore
