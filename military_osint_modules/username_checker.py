import requests

def run():
    print("\n=== Username Checker ===")
    username = input("Masukkan username >> ")
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Telegram": f"https://t.me/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}"
    }
    for platform, url in sites.items():
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print(f"[+] {platform}: DITEMUKAN ({url})")
            else:
                print(f"[-] {platform}: Tidak ada")
        except:
            print(f"[!] {platform}: Gagal mengakses")
