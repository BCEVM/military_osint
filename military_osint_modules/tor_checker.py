import requests

def run():
    print("\n=== TOR/VPN Checker + IP Info ===")
    try:
        ip = requests.get("https://api.ipify.org").text
        print(f"[+] IP Publik Kamu: {ip}")

        # Cek apakah IP TOR
        torlist = requests.get("https://check.torproject.org/torbulkexitlist").text
        if ip in torlist:
            print("[+] TOR Node Terdeteksi")
        else:
            print("[-] Bukan IP TOR")

        # Info Geolokasi IP
        print("\n=== Informasi Lokasi & ISP ===")
        response = requests.get(f"https://ipapi.co/{ip}/json/").json()
        if "error" in response:
            print("[!] Gagal mengambil data geolokasi.")
            return

        keys = [
            "ip", "city", "region", "region_code", "country", "country_name",
            "continent_code", "postal", "latitude", "longitude", "timezone",
            "utc_offset", "org", "asn", "version", "currency", "languages"
        ]

        for key in keys:
            print(f"{key}: {response.get(key)}")

        print(f"[+] Maps: https://www.google.com/maps?q={response.get('latitude')},{response.get('longitude')}")
    except Exception as e:
        print(f"[!] Terjadi error: {e}")
