#!/usr/bin/env python3
"""
Export all presentations from noti.st to local files.
Downloads JSON metadata, slide images, and PDFs.
"""

import json
import os
import re
import time
import urllib.request
import urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

USERNAME = "rmoff"
BASE_URL = "https://noti.st"
OUTPUT_DIR = Path("export")
IMAGES_DIR = OUTPUT_DIR / "images"
PDFS_DIR = OUTPUT_DIR / "pdfs"

def fetch_json(url):
    """Fetch JSON from a URL with retry logic."""
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.loads(response.read().decode('utf-8'))
        except (urllib.error.URLError, urllib.error.HTTPError) as e:
            print(f"  Attempt {attempt + 1} failed for {url}: {e}")
            if attempt < 2:
                time.sleep(2)
    return None

def download_file(url, dest_path):
    """Download a file from URL to destination path."""
    if dest_path.exists():
        return True

    dest_path.parent.mkdir(parents=True, exist_ok=True)

    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=60) as response:
                with open(dest_path, 'wb') as f:
                    f.write(response.read())
            return True
        except Exception as e:
            print(f"  Download attempt {attempt + 1} failed for {url}: {e}")
            if attempt < 2:
                time.sleep(2)
    return False

def extract_presentation_id(url_or_id):
    """Extract presentation ID from URL or return as-is if already an ID."""
    # Handle full URLs like https://noti.st/rmoff/9GpIYA/title-slug
    match = re.search(r'/([a-zA-Z0-9]{6})(?:/|$)', str(url_or_id))
    if match:
        return match.group(1)
    # Handle IDs like pr_9GpIYA
    if url_or_id.startswith('pr_'):
        return url_or_id[3:]
    return url_or_id

def get_profile_presentations():
    """Fetch all presentations from the user's profile."""
    print(f"Fetching profile for {USERNAME}...")
    profile_url = f"{BASE_URL}/{USERNAME}.json"
    profile_data = fetch_json(profile_url)

    if not profile_data:
        print("Failed to fetch profile data")
        return []

    # Save profile data
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_DIR / "profile.json", 'w') as f:
        json.dump(profile_data, f, indent=2)

    # Extract presentation info - structure is data[0].relationships.data[]
    presentations = []
    if 'data' in profile_data and len(profile_data['data']) > 0:
        author_data = profile_data['data'][0]
        relationships = author_data.get('relationships', {})
        pres_list = relationships.get('data', [])

        for item in pres_list:
            if item.get('type') == 'presentations':
                pres_id = extract_presentation_id(item.get('id', ''))
                presentations.append({
                    'id': pres_id,
                    'title': item.get('attributes', {}).get('title', 'Untitled'),
                    'url': item.get('links', {}).get('self', ''),
                    'presented_on': item.get('attributes', {}).get('presented_on', ''),
                    'image': item.get('attributes', {}).get('image', {}).get('src', ''),
                    'event_url': item.get('links', {}).get('event', '')
                })

    print(f"Found {len(presentations)} presentations")
    return presentations

def fetch_presentation_details(pres_info):
    """Fetch detailed data for a single presentation."""
    pres_id = pres_info['id']
    print(f"  Fetching: {pres_info['title'][:50]}...")

    detail_url = f"{BASE_URL}/{USERNAME}/{pres_id}.json"
    detail_data = fetch_json(detail_url)

    if not detail_data:
        print(f"  Failed to fetch details for {pres_id}")
        return None

    # Save presentation JSON
    pres_dir = OUTPUT_DIR / "presentations"
    pres_dir.mkdir(parents=True, exist_ok=True)
    with open(pres_dir / f"{pres_id}.json", 'w') as f:
        json.dump(detail_data, f, indent=2)

    return detail_data

def download_presentation_assets(pres_id, detail_data):
    """Download slides and PDF for a presentation."""
    if not detail_data:
        return 0

    pres_images_dir = IMAGES_DIR / pres_id
    pres_images_dir.mkdir(parents=True, exist_ok=True)

    slides = []
    pdf_url = None

    # Navigate the JSON structure: data[0].attributes.slidedeck.data[*].slides
    if 'data' in detail_data and len(detail_data['data']) > 0:
        attrs = detail_data['data'][0].get('attributes', {})

        # Get PDF URL from download attribute
        pdf_url = attrs.get('download')

        # Get slides from slidedeck.data[*].slides
        slidedeck = attrs.get('slidedeck', {})
        if isinstance(slidedeck, dict) and 'data' in slidedeck:
            for deck in slidedeck['data']:
                deck_slides = deck.get('slides', [])
                for idx, slide in enumerate(deck_slides):
                    image_url = slide.get('image')
                    if image_url:
                        slides.append((idx, image_url))

    # Download slides
    for slide_num, image_url in slides:
        ext = os.path.splitext(image_url.split('?')[0])[1] or '.jpg'
        dest = pres_images_dir / f"slide_{slide_num:03d}{ext}"
        if not dest.exists():
            download_file(image_url, dest)

    # Download PDF
    if pdf_url:
        PDFS_DIR.mkdir(parents=True, exist_ok=True)
        pdf_dest = PDFS_DIR / f"{pres_id}.pdf"
        if not pdf_dest.exists():
            print(f"  Downloading PDF for {pres_id}...")
            download_file(pdf_url, pdf_dest)

    return len(slides)

def download_assets_from_saved_json():
    """Download assets from already-saved presentation JSON files."""
    pres_dir = OUTPUT_DIR / "presentations"
    if not pres_dir.exists():
        print("No presentations directory found. Run full export first.")
        return

    json_files = list(pres_dir.glob("*.json"))
    print(f"Found {len(json_files)} saved presentation JSON files")

    total_slides = 0
    for json_file in json_files:
        pres_id = json_file.stem
        print(f"  Processing {pres_id}...")
        with open(json_file) as f:
            detail_data = json.load(f)
        num_slides = download_presentation_assets(pres_id, detail_data)
        if num_slides:
            total_slides += num_slides

    print(f"\nDownloaded {total_slides} total slides")


def main():
    print("=" * 60)
    print("Noti.st Export Tool")
    print("=" * 60)

    # Get all presentations
    presentations = get_profile_presentations()

    if not presentations:
        print("No presentations found!")
        return

    print(f"\nFetching details for {len(presentations)} presentations...")

    # Fetch all presentation details
    all_details = {}
    for pres in presentations:
        detail_data = fetch_presentation_details(pres)
        if detail_data:
            all_details[pres['id']] = detail_data
        time.sleep(0.5)  # Be nice to the server

    print(f"\nDownloading assets for {len(all_details)} presentations...")

    # Download assets
    total_slides = 0
    for pres_id, detail_data in all_details.items():
        print(f"  Processing {pres_id}...")
        num_slides = download_presentation_assets(pres_id, detail_data)
        if num_slides:
            total_slides += num_slides

    print("\n" + "=" * 60)
    print("Export complete!")
    print(f"  Presentations: {len(all_details)}")
    print(f"  Total slides: {total_slides}")
    print(f"  Output directory: {OUTPUT_DIR.absolute()}")
    print("=" * 60)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--assets-only":
        download_assets_from_saved_json()
    else:
        main()
