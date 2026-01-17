#!/usr/bin/env python3

import zipfile
import itertools
import string
import argparse
import sys
import time

def build_charset(special_chars):
    return (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        special_chars
    )

def crack_zip(zip_path, min_len, max_len, special_chars):
    charset = build_charset(special_chars)
    attempts = 0
    start_time = time.time()

    try:
        zf = zipfile.ZipFile(zip_path)
    except Exception as e:
        print(f"[!] Cannot open ZIP file: {e}")
        sys.exit(1)

    for length in range(min_len, max_len + 1):
        print(f"[*] Trying passwords of length {length}")
        for combo in itertools.product(charset, repeat=length):
            password = "".join(combo).encode("utf-8")
            attempts += 1
            try:
                zf.extractall(pwd=password)
                elapsed = time.time() - start_time
                print("\n[✔] PASSWORD FOUND")
                print(f"Password : {password.decode()}")
                print(f"Attempts : {attempts}")
                print(f"Time     : {elapsed:.2f} seconds")
                return
            except:
                pass

    print("\n[✘] Password not found in given range.")

def parse_args():
    parser = argparse.ArgumentParser(
        description="ZIP password recovery tool (authorized use only)"
    )
    parser.add_argument("zipfile", help="Target ZIP file")
    parser.add_argument("--minChar", type=int, required=True, help="Minimum password length")
    parser.add_argument("--maxChar", type=int, required=True, help="Maximum password length")
    parser.add_argument(
        "--specialChar",
        default="",
        help="Special characters to include, e.g. '@#$'"
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    crack_zip(
        zip_path=args.zipfile,
        min_len=args.minChar,
        max_len=args.maxChar,
        special_chars=args.specialChar
    )
