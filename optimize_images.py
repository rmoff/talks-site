#!/usr/bin/env python3
"""
Image optimization script for talks.rmoff.net
- Generates responsive sizes (400w, 800w, 1600w)
- Converts all images to WebP format
- Preserves original files as fallback
"""

import os
import subprocess
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

IMAGES_DIR = Path("site/static/images")
SIZES = [400, 800]  # 1600 is original size, keep as-is
WEBP_QUALITY = 85

def get_image_files():
    """Find all slide_000 images."""
    images = []
    for img_dir in IMAGES_DIR.iterdir():
        if img_dir.is_dir():
            for img_file in img_dir.glob("slide_000.*"):
                if img_file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
                    images.append(img_file)
    return images

def resize_image(src: Path, dest: Path, width: int):
    """Resize image using sips (macOS)."""
    try:
        # Copy original first
        subprocess.run(['cp', str(src), str(dest)], check=True, capture_output=True)
        # Resize copy
        subprocess.run([
            'sips', '--resampleWidth', str(width), str(dest)
        ], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  Error resizing {src}: {e}")
        return False

def convert_to_webp(src: Path, dest: Path):
    """Convert image to WebP using cwebp."""
    try:
        subprocess.run([
            'cwebp', '-q', str(WEBP_QUALITY), str(src), '-o', str(dest)
        ], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  Error converting {src} to WebP: {e}")
        return False

def process_image(img_path: Path):
    """Process a single image: generate sizes and WebP versions."""
    img_dir = img_path.parent
    stem = img_path.stem  # slide_000
    ext = img_path.suffix  # .jpg or .png

    results = {'original': str(img_path), 'generated': []}

    # Convert original to WebP (1600w)
    webp_1600 = img_dir / f"{stem}.webp"
    if not webp_1600.exists():
        if convert_to_webp(img_path, webp_1600):
            results['generated'].append(f"{stem}.webp")

    # Generate smaller sizes
    for width in SIZES:
        # Resized JPG/PNG
        resized_path = img_dir / f"{stem}_{width}w{ext}"
        if not resized_path.exists():
            if resize_image(img_path, resized_path, width):
                results['generated'].append(f"{stem}_{width}w{ext}")

        # WebP version of resized
        webp_path = img_dir / f"{stem}_{width}w.webp"
        if not webp_path.exists():
            # Use resized image if it exists, otherwise resize and convert
            source = resized_path if resized_path.exists() else img_path
            if source == img_path:
                # Need to create temp resized first
                temp_resized = img_dir / f"temp_{width}w{ext}"
                resize_image(img_path, temp_resized, width)
                convert_to_webp(temp_resized, webp_path)
                temp_resized.unlink()
            else:
                convert_to_webp(source, webp_path)
            results['generated'].append(f"{stem}_{width}w.webp")

    return results

def main():
    images = get_image_files()
    print(f"Found {len(images)} images to process")

    total_generated = 0

    # Process images with progress indicator
    for i, img in enumerate(images, 1):
        print(f"[{i}/{len(images)}] Processing {img.parent.name}/{img.name}...")
        result = process_image(img)
        if result['generated']:
            total_generated += len(result['generated'])
            for f in result['generated']:
                print(f"  + {f}")

    print(f"\nDone! Generated {total_generated} new files")

    # Show size comparison
    print("\nCalculating size savings...")
    original_size = sum(f.stat().st_size for f in IMAGES_DIR.rglob("slide_000.jpg")) + \
                    sum(f.stat().st_size for f in IMAGES_DIR.rglob("slide_000.png"))
    webp_size = sum(f.stat().st_size for f in IMAGES_DIR.rglob("slide_000.webp"))

    print(f"Original images: {original_size / 1024 / 1024:.1f} MB")
    print(f"WebP (1600w): {webp_size / 1024 / 1024:.1f} MB")
    print(f"Savings: {(1 - webp_size / original_size) * 100:.1f}%")

if __name__ == "__main__":
    main()
