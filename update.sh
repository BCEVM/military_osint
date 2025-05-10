#!/bin/bash

REPO_URL="https://github.com/USERNAME/military_osint.git"
INSTALL_DIR="$HOME/tools/military_osint"

if [ -d "$INSTALL_DIR/.git" ]; then
    echo "[+] Mengambil update dari repository..."
    cd "$INSTALL_DIR" && git pull
    echo "[+] Update selesai."
else
    echo "[!] Folder tidak terdeteksi sebagai git repo. Clone ulang:"
    git clone "$REPO_URL" "$INSTALL_DIR"
fi
