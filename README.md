# zip-password-recovery

A Python-based ZIP password recovery tool using constrained brute-force and mask attacks for recovering passwords of files you own or have explicit permission to test.

---

## ⚠️ Legal & Ethical Use

This project is intended **ONLY** for:
- Recovering passwords for **your own** ZIP archives
- Archives you are **explicitly authorized** to test

**Do not use this tool on files you don’t own or don’t have permission to access.** Unauthorized password cracking may be illegal and unethical.

---

## Features (Planned & In Progress)

- ✅ Constrained brute-force using a custom character set (letters, digits, selected symbols)
- ✅ Mask-based attack (fast when you know part of the password)
- ⏳ Progress output (attempt counter + attempts/sec)
- ⏳ Resume / checkpoint support
- ⏳ Multi-process CPU speedup
- ⏳ CLI interface (`argparse`)
- ⏳ Safer test mode (verify password without extracting everything)

---

## How It Works (High-Level)

ZIP encryption isn’t “broken.” The tool:
1. Generates password candidates from your constraints (charset / length / known prefix/suffix)
2. Tries each candidate by attempting to decrypt/extract the ZIP
3. Stops when a valid password is found

Performance depends heavily on:
- Password length
- Character set size
- ZIP encryption type (legacy vs AES)
- CPU speed (Python is CPU-bound)

---

## Project Structure (MVP)

```text
zip-password-recovery/
├── src/
│   ├── cracker.py        # core logic (brute-force + mask)
│   ├── charset.py        # character set helpers
│   └── utils.py          # timing, counters, checkpoints
├── tests/
├── README.md
└── LICENSE
