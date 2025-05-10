import os
from military_osint_modules import username_checker, exif_analyzer, geo_locator, reverse_image, tor_checker, telegram_scraper, pdf_metadata, satellite_viewer

def banner():
    print("""
=====================================
      MILITARY OSINT INTELLIGENCE TOOLKIT
=====================================
    """)

def menu():
    print("""
[1] Cek Username di Sosmed
[2] Analisis EXIF Gambar
[3] Geolokasi Berdasarkan Gambar
[4] Reverse Image Search
[5] Cek Mode Anonim (TOR/VPN)
[6] Telegram Group/Channel Scraper
[7] PDF Metadata Extractor
[8] Download Citra Satelit Lokasi
[0] Keluar
    """)

def main():
    banner()
    while True:
        menu()
        choice = input("Pilih opsi >> ")
        if choice == "1":
            username_checker.run()
        elif choice == "2":
            exif_analyzer.run()
        elif choice == "3":
            geo_locator.run()
        elif choice == "4":
            reverse_image.run()
        elif choice == "5":
            tor_checker.run()
        elif choice == "6":
            telegram_scraper.run()
        elif choice == "7":
            pdf_metadata.run()
        elif choice == "8":
            satellite_viewer.run()
        elif choice == "0":
            print("Keluar dari toolkit.")
            break
        else:
            print("[!] Input tidak valid.")

if __name__ == "__main__":
    main()
