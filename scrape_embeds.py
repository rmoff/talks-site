#!/usr/bin/env python3
"""
Scrape Twitter embeds and other embedded content from noti.st HTML pages.
This supplements the API export which doesn't include embedded content.
Uses only standard library - no external dependencies required.
"""

import json
import re
import urllib.request
import urllib.error
from pathlib import Path
import time

USERNAME = "rmoff"
BASE_URL = "https://noti.st"
EXPORT_DIR = Path("export")
EMBEDS_DIR = EXPORT_DIR / "embeds"

def fetch_html(url):
    """Fetch HTML from a URL with retry logic."""
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=30) as response:
                return response.read().decode('utf-8')
        except (urllib.error.URLError, urllib.error.HTTPError) as e:
            print(f"  Attempt {attempt + 1} failed for {url}: {e}")
            if attempt < 2:
                time.sleep(2)
    return None

def extract_twitter_embeds(html):
    """Extract Twitter embed blockquotes from HTML using regex."""
    twitter_embeds = []

    # Pattern to match Twitter blockquote embeds
    # Looks for: <blockquote class="twitter-tweet"...>...</blockquote>
    pattern = r'<blockquote[^>]*class="twitter-tweet"[^>]*>.*?</blockquote>'
    matches = re.findall(pattern, html, re.DOTALL)

    for match in matches:
        twitter_embeds.append(match)

    return twitter_embeds

def extract_youtube_embeds(html):
    """Extract YouTube iframes from HTML using regex."""
    youtube_embeds = []

    # Pattern to match YouTube iframes
    pattern = r'<iframe[^>]*(?:src="[^"]*(?:youtube\.com|youtu\.be)[^"]*")[^>]*>.*?</iframe>'
    matches = re.findall(pattern, html, re.DOTALL | re.IGNORECASE)

    for match in matches:
        youtube_embeds.append(match)

    return youtube_embeds

def extract_vimeo_embeds(html):
    """Extract Vimeo iframes from HTML using regex."""
    vimeo_embeds = []

    # Pattern to match Vimeo iframes
    pattern = r'<iframe[^>]*(?:src="[^"]*vimeo\.com[^"]*")[^>]*>.*?</iframe>'
    matches = re.findall(pattern, html, re.DOTALL | re.IGNORECASE)

    for match in matches:
        vimeo_embeds.append(match)

    return vimeo_embeds

def extract_notist_video_embeds(html):
    """Extract notist.ninja video iframes from HTML using regex."""
    notist_embeds = []

    # Pattern to match notist.ninja video iframes
    pattern = r'<iframe[^>]*(?:src="[^"]*notist\.ninja/embed/[^"]*")[^>]*>.*?</iframe>'
    matches = re.findall(pattern, html, re.DOTALL | re.IGNORECASE)

    for match in matches:
        notist_embeds.append(match)

    return notist_embeds

def scrape_presentation_embeds(pres_id, slug):
    """Scrape embeds from a single presentation page."""
    url = f"{BASE_URL}/{USERNAME}/{pres_id}/{slug}"
    print(f"  Scraping {pres_id}...")

    html = fetch_html(url)
    if not html:
        print(f"  Failed to fetch {url}")
        return None

    # Extract all types of embeds
    twitter_embeds = extract_twitter_embeds(html)
    youtube_embeds = extract_youtube_embeds(html)
    vimeo_embeds = extract_vimeo_embeds(html)
    notist_video_embeds = extract_notist_video_embeds(html)

    # Only return if we found something
    total_embeds = len(twitter_embeds) + len(youtube_embeds) + len(vimeo_embeds) + len(notist_video_embeds)
    if total_embeds > 0:
        return {
            'presentation_id': pres_id,
            'url': url,
            'twitter_embeds': twitter_embeds,
            'youtube_embeds': youtube_embeds,
            'vimeo_embeds': vimeo_embeds,
            'notist_video_embeds': notist_video_embeds,
            'embed_count': total_embeds
        }

    return None

def main():
    print("=" * 60)
    print("Noti.st Embed Scraper")
    print("=" * 60)

    # Load all presentations from JSON files
    pres_dir = EXPORT_DIR / "presentations"
    if not pres_dir.exists():
        print("No presentations directory found. Run export_notist.py first.")
        return

    json_files = list(pres_dir.glob("*.json"))
    print(f"Found {len(json_files)} presentation JSON files")

    # Create embeds directory
    EMBEDS_DIR.mkdir(parents=True, exist_ok=True)

    # Scrape each presentation
    presentations_with_embeds = []
    for json_file in sorted(json_files):
        pres_id = json_file.stem

        # Load presentation metadata to get slug
        with open(json_file) as f:
            pres_data = json.load(f)

        if 'data' not in pres_data or not pres_data['data']:
            continue

        slug = pres_data['data'][0]['attributes'].get('slug', '')
        if not slug:
            continue

        # Scrape embeds
        embeds = scrape_presentation_embeds(pres_id, slug)
        if embeds:
            presentations_with_embeds.append(embeds)

            # Save individual embed file
            embed_file = EMBEDS_DIR / f"{pres_id}.json"
            with open(embed_file, 'w') as f:
                json.dump(embeds, f, indent=2)

            print(f"    ✓ Found {embeds['embed_count']} embeds")

        # Be nice to the server
        time.sleep(1)

    # Save summary
    summary_file = EMBEDS_DIR / "embeds_summary.json"
    with open(summary_file, 'w') as f:
        json.dump({
            'total_presentations_checked': len(json_files),
            'presentations_with_embeds': len(presentations_with_embeds),
            'embeds': presentations_with_embeds
        }, f, indent=2)

    print("\n" + "=" * 60)
    print(f"Scraping complete!")
    print(f"  Total presentations checked: {len(json_files)}")
    print(f"  Presentations with embeds: {len(presentations_with_embeds)}")
    print(f"  Output directory: {EMBEDS_DIR.absolute()}")
    print("=" * 60)

if __name__ == "__main__":
    main()
