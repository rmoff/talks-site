#!/usr/bin/env python3
"""
Copy downloaded images and PDFs to the Hugo site static folder.
Run this after export_notist.py has downloaded all assets.
"""

import shutil
from pathlib import Path

EXPORT_DIR = Path("export")
STATIC_DIR = Path("site/static")

def main():
    print("=" * 60)
    print("Copying assets to Hugo static folder")
    print("=" * 60)

    # Copy only first slide (thumbnail) from each presentation
    src_images = EXPORT_DIR / "images"
    dst_images = STATIC_DIR / "images"

    if src_images.exists():
        print(f"\nCopying thumbnails from {src_images} to {dst_images}...")
        if dst_images.exists():
            shutil.rmtree(dst_images)
        dst_images.mkdir(parents=True, exist_ok=True)

        # Copy only slide_000.* (first slide) from each presentation
        thumbnail_count = 0
        for pres_dir in src_images.iterdir():
            if pres_dir.is_dir():
                # Find the first slide (slide_000 with any extension)
                first_slides = list(pres_dir.glob("slide_000.*"))
                if first_slides:
                    # Create destination directory
                    dst_pres_dir = dst_images / pres_dir.name
                    dst_pres_dir.mkdir(parents=True, exist_ok=True)
                    # Copy only the first slide
                    shutil.copy2(first_slides[0], dst_pres_dir / first_slides[0].name)
                    thumbnail_count += 1

        print(f"  Copied {thumbnail_count} thumbnail images")
    else:
        print("No images directory found")

    # Copy PDFs
    src_pdfs = EXPORT_DIR / "pdfs"
    dst_pdfs = STATIC_DIR / "pdfs"

    if src_pdfs.exists():
        print(f"\nCopying PDFs from {src_pdfs} to {dst_pdfs}...")
        if dst_pdfs.exists():
            shutil.rmtree(dst_pdfs)
        shutil.copytree(src_pdfs, dst_pdfs)

        pdf_count = sum(1 for _ in dst_pdfs.glob("*.pdf"))
        print(f"  Copied {pdf_count} PDF files")
    else:
        print("No PDFs directory found")

    print("\n" + "=" * 60)
    print("Done!")
    print("=" * 60)

if __name__ == "__main__":
    main()
