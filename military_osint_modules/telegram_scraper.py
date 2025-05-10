import requests

def run():
    print("\n=== Telegram Scraper (Public only) ===")
    print("Note: Gunakan Telethon untuk scrape lebih dalam")
    link = input("Masukkan link channel/grup Telegram (public) >> ")
    print(f"[*] Silakan cek via webview: https://t.me/s/{link.split('/')[-1]}")
