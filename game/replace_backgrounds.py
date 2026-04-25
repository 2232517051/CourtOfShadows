"""
Replace original SD backgrounds with HD versions resized to 1280x720.
- Backs up originals to images/backup_sd/
- Resizes HD (2560x1440) images to 1280x720 webp quality=95
- Keeps HD originals in images/hd/ untouched
"""

import os
import shutil
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE, "images")
HD_DIR = os.path.join(IMAGES_DIR, "hd")
BACKUP_DIR = os.path.join(IMAGES_DIR, "backup_sd")

TARGET_SIZE = (1280, 720)
WEBP_QUALITY = 95

os.makedirs(BACKUP_DIR, exist_ok=True)

hd_files = [f for f in os.listdir(HD_DIR) if f.startswith("bg_") and f.endswith(".webp")]
hd_files.sort()

print(f"Found {len(hd_files)} HD backgrounds to process.\n")

replaced = 0
skipped = 0

for fname in hd_files:
    hd_path = os.path.join(HD_DIR, fname)
    original_path = os.path.join(IMAGES_DIR, fname)
    backup_path = os.path.join(BACKUP_DIR, fname)

    if not os.path.exists(original_path):
        print(f"  SKIP {fname} - no matching original found")
        skipped += 1
        continue

    # Back up original (only if not already backed up)
    if not os.path.exists(backup_path):
        shutil.copy2(original_path, backup_path)

    # Open HD image, resize to 1280x720 with high-quality resampling, save as webp
    with Image.open(hd_path) as img:
        hd_size = img.size
        resized = img.resize(TARGET_SIZE, Image.LANCZOS)
        resized.save(original_path, "WEBP", quality=WEBP_QUALITY)

    new_size = os.path.getsize(original_path)
    old_size = os.path.getsize(backup_path)
    print(f"  OK {fname}: {hd_size} -> {TARGET_SIZE}, {old_size//1024}KB -> {new_size//1024}KB")
    replaced += 1

print(f"\nDone! Replaced: {replaced}, Skipped: {skipped}")
print(f"Backups saved to: {BACKUP_DIR}")
