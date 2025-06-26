#!/usr/bin/env bash
set -e

# 1) Create virtualenv
python3 -m venv venv
source venv/bin/activate

# 2) Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 3) (Optional) Run game in dev mode
echo "Installed. To run in dev mode:"
echo "  source venv/bin/activate && python src/main.py"

# 4) Package with PyInstaller
pip install pyinstaller
pyinstaller --onefile --name StellarDrift src/main.py \
    --add-data "src/assets:assets"

echo "Build complete. Check dist/StellarDrift (or StellarDrift.exe on Windows)."
