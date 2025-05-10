import requests

def run():
    print("\n=== TOR/VPN Checker ===")
    try:
        ip = requests.get("https://api.ipify.org").text
        print(f"[+] IP Publik Kamu: {ip}")
        torlist = requests.get("https://check.torproject.org/torbulkexitlist").text
        if ip in torlist:
            print("[+] TOR Node Terdeteksi")
        else:
            print("[-] Bukan IP TOR")
    except:
        print("[!] Gagal mengecek koneksi.")
