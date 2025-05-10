import exifread

def run():
    print("\n=== EXIF Analyzer ===")
    path = input("Path ke file gambar >> ")
    try:
        with open(path, 'rb') as f:
            tags = exifread.process_file(f)
            if not tags:
                print("[!] Tidak ada data EXIF ditemukan.")
            for tag in tags:
                print(f"{tag}: {tags[tag]}")
    except:
        print("[!] Gagal membaca file atau tidak ditemukan.")
