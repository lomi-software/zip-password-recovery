import zipfile
import itertools
import string

ZIP_FILE = "protected.zip"
MIN_LEN = 1
MAX_LEN = 6

CHARSET = (
    string.ascii_lowercase +
    string.ascii_uppercase +
    string.digits +
    "@#$_!"
)

def crack_zip():
    with zipfile.ZipFile(ZIP_FILE) as zf:
        for length in range(MIN_LEN, MAX_LEN + 1):
            print(f"[*] Trying length {length}...")
            for combo in itertools.product(CHARSET, repeat=length):
                password = "".join(combo).encode()
                try:
                    zf.extractall(pwd=password)
                    print(f"[✔] Password FOUND: {password.decode()}")
                    return
                except:
                    pass

    print("[✘] Password not found")

if __name__ == "__main__":
    crack_zip()
