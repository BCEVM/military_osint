import subprocess
import os

def run():
    print("\n=== EXIF Analyzer (ExifTool) ===")
    path = input("Path ke file gambar >> ")
    if not os.path.isfile(path):
        print("[!] File tidak ditemukan.")
        return

    try:
        result = subprocess.run(["exiftool", path], capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print("[!] Gagal mengeksekusi exiftool.")
    except FileNotFoundError:
        print("[!] exiftool tidak ditemukan. Install dengan 'sudo apt install libimage-exiftool-perl'")
