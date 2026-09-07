#!/bin/bash

read -r password
echo "$password" | sudo -S -v

#Remove the above two line if running directly. Added that for automating sudo password entry when prompted.

echo "=== Starting System Upgrade ==="
echo ""

echo "[1/3] Updating apt package lists..."
sudo apt update

echo ""
echo "[2/3] Upgrading system packages..."
sudo apt upgrade -y

echo ""
echo "[3/3] Checking for Snap..."
if command -v snap &> /dev/null; then
    echo "Refreshing Snap packages..."
    sudo snap refresh
else
    echo "Snap is not installed, skipping."
fi

echo ""
echo "[4/3] Checking for Flatpak..."
if command -v flatpak &> /dev/null; then
    echo "Updating Flatpak packages..."
    flatpak update -y
else
    echo "Flatpak is not installed, skipping."
fi

echo ""
echo "=== Upgrade Complete! ==="
