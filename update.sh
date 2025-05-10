#!/bin/bash

REPO_URL="https://github.com/BCEVM/military_osint.git"
INSTALL_DIR="$HOME/tools/military_osint"

echo "[*] Memulai proses update..."

if [ -d "$INSTALL_DIR/.git" ]; then
    echo "[+] Repo sudah ada. Melakukan git pull..."
    cd "$INSTALL_DIR" || { echo "[!] Gagal masuk ke direktori $INSTALL_DIR"; exit 1; }
    git reset --hard HEAD
    git pull origin main
    echo "[+] Update selesai."
else
    echo "[!] Git repo belum ada. Mengkloning ulang dari awal..."
    rm -rf "$INSTALL_DIR"
    git clone "$REPO_URL" "$INSTALL_DIR" || { echo "[!] Gagal meng-clone repo."; exit 1; }
    echo "[+] Clone selesai."
fi
