#!/bin/bash

read -r password
echo "$password" | sudo -S -v

#Remove the above two line if running directly. Added that for automating sudo password entry when prompted.

echo "=== Starting System Cleanup ==="
echo "Free space before cleaning:"
df -h /
echo ""

echo "[1/7] Cleaning Apt package cache..."
sudo apt autoclean

echo "[2/7] Removing unused dependencies..."
sudo apt autoremove --purge -y

echo "[3/7] Clearing thumbnail cache..."
rm -rf ~/.cache/thumbnails/*

echo "[4/7] Vacuuming systemd journal logs (keeping last 2 days)..."
sudo journalctl --vacuum-time=2d

echo "[5/7] Checking for Snap..."
if command -v snap &> /dev/null; then
    echo "Configuring snap retention..."
    sudo snap set system refresh.retain=2
else
    echo "Snap is not installed, skipping."
fi

echo "[6/7] Checking for uv..."
if command -v uv &> /dev/null; then
    echo "Cleaning uv cache..."
    uv cache clean
else
    echo "uv is not installed, skipping."
fi

echo "[7/7] Cache folder size breakdown:"
du -h --max-depth=1 ~/.cache/ | sort -hr

echo ""
echo "--------------------------------------------------------"
echo "TIP: If you spot any unusually large folders in ~/.cache/"
echo "above, you can remove them manually using:"
echo "  rm -rf ~/.cache/<folder_name>"
echo "--------------------------------------------------------"

echo ""
echo "=== Cleanup Complete! ==="
echo "Free space after cleaning:"
df -h /
