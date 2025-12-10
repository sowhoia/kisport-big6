#!/bin/bash
# Termux setup script for BIG6 game
# Run this in Termux on Android

echo "=== BIG6 Termux Setup ==="

# Update packages
pkg update -y

# Install Python
pkg install python -y

# Run the game
python big6.py
