from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import os

# === GANTI DENGAN MILIKMU ===
api_id = 29941352
api_hash = "1f112c546dd69be79de2d51f597b75fa"
phone = "+6281993261212"

# === LOGIN (auto session file) ===
client = TelegramClient("telegram_scraper_session", api_id, api_hash)

def run():
    print("\n=== Telegram Scraper (Chat Messages) ===")
    target = input("Masukkan username atau link channel/grup >> ").strip()
    if target.startswith("https://t.me/"):
        target = target.split("/")[-1]

    try:
        client.start(phone)
        print("[+] Berhasil login Telegram.")
        entity = client.get_entity(target)
        messages = client(GetHistoryRequest(
            peer=entity,
            limit=50,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0
        ))

        print(f"\n=== {len(messages.messages)} Pesan Terakhir dari {target} ===")
        for msg in messages.messages:
            if msg.message:
                print(f"[{msg.date}] {msg.sender_id}: {msg.message}")
    except Exception as e:
        print(f"[!] Gagal: {e}")
