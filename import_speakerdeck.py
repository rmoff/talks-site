#!/usr/bin/env python3
"""
Import presentations from SpeakerDeck to Hugo content.
Scrapes metadata, downloads PDFs, generates thumbnails, and creates markdown files.
"""

import json
import os
import re
import time
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser

USERNAME = "rmoff"
BASE_URL = "https://speakerdeck.com"
EXPORT_DIR = Path("export/speakerdeck")
PDFS_DIR = EXPORT_DIR / "pdfs"
IMAGES_DIR = EXPORT_DIR / "images"
SITE_DIR = Path("site")
CONTENT_DIR = SITE_DIR / "content"


class SpeakerDeckParser(HTMLParser):
    """Parse SpeakerDeck HTML to extract presentation data."""

    def __init__(self):
        super().__init__()
        self.presentations = []
        self.current_pres = None
        self.in_title = False
        self.in_description = False
        self.in_date = False
        self.in_event = False
        self.capture_text = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        # Presentation card link
        if tag == 'a' and 'href' in attrs_dict:
            href = attrs_dict['href']
            if href.startswith(f'/{USERNAME}/') and 'class' in attrs_dict:
                if 'deck-preview' in attrs_dict.get('class', ''):
                    self.current_pres = {'slug': href.split('/')[-1], 'href': href}

        # Title
        if tag == 'div' and attrs_dict.get('class') == 'deck-title':
            self.in_title = True
            self.capture_text = 'title'

    def handle_endtag(self, tag):
        if tag == 'div' and self.in_title:
            self.in_title = False
            if self.current_pres and 'title' in self.current_pres:
                self.presentations.append(self.current_pres)
                self.current_pres = None
            self.capture_text = None

    def handle_data(self, data):
        if self.capture_text and self.current_pres:
            data = data.strip()
            if data:
                self.current_pres[self.capture_text] = data


class DetailParser(HTMLParser):
    """Parse individual presentation page for metadata."""

    def __init__(self):
        super().__init__()
        self.title = None
        self.description = ""
        self.date = None
        self.event = None
        self.pdf_url = None
        self.slide_count = None
        self.data_id = None
        self.in_description = False
        self.in_title = False
        self.capture_next = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        # Get deck ID from data attributes
        if tag == 'div' and 'data-id' in attrs_dict:
            self.data_id = attrs_dict['data-id']

        # Title (h1)
        if tag == 'h1' and attrs_dict.get('class') == 'deck-title':
            self.in_title = True

        # Description
        if tag == 'div' and 'deck-description' in attrs_dict.get('class', ''):
            self.in_description = True

        # Date - look for time tag
        if tag == 'time' and 'datetime' in attrs_dict:
            self.date = attrs_dict['datetime']

        # Event name - typically in a link
        if tag == 'a' and '/events/' in attrs_dict.get('href', ''):
            self.capture_next = 'event'

        # PDF download link
        if tag == 'a' and 'download' in attrs_dict.get('class', ''):
            self.pdf_url = attrs_dict.get('href')

    def handle_endtag(self, tag):
        if tag == 'h1' and self.in_title:
            self.in_title = False
        if tag == 'div' and self.in_description:
            self.in_description = False
        if tag == 'a' and self.capture_next == 'event':
            self.capture_next = None

    def handle_data(self, data):
        data = data.strip()
        if not data:
            return

        if self.in_title and not self.title:
            self.title = data
        if self.in_description:
            self.description += data + " "
        if self.capture_next == 'event':
            self.event = data


def fetch_html(url):
    """Fetch HTML from a URL with retry logic."""
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            })
            with urllib.request.urlopen(req, timeout=30) as response:
                return response.read().decode('utf-8')
        except (urllib.error.URLError, urllib.error.HTTPError) as e:
            print(f"  Attempt {attempt + 1} failed for {url}: {e}")
            if attempt < 2:
                time.sleep(2)
    return None


def download_file(url, dest_path):
    """Download a file from URL to destination path."""
    if dest_path.exists():
        print(f"  Already exists: {dest_path.name}")
        return True

    dest_path.parent.mkdir(parents=True, exist_ok=True)

    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            })
            with urllib.request.urlopen(req, timeout=120) as response:
                with open(dest_path, 'wb') as f:
                    f.write(response.read())
            return True
        except Exception as e:
            print(f"  Download attempt {attempt + 1} failed: {e}")
            if attempt < 2:
                time.sleep(2)
    return False


def get_presentation_list():
    """Fetch list of all presentations from SpeakerDeck profile."""
    presentations = []

    for page in range(1, 5):  # Check up to 4 pages
        url = f"{BASE_URL}/{USERNAME}" if page == 1 else f"{BASE_URL}/{USERNAME}?page={page}"
        print(f"Fetching page {page}: {url}")

        html = fetch_html(url)
        if not html:
            break

        # Parse using regex (more reliable than HTML parser for this structure)
        # Look for deck links: /rmoff/slug
        pattern = rf'href="/{USERNAME}/([^"/?]+)"[^>]*class="[^"]*deck-preview'
        matches = re.findall(pattern, html)

        if not matches:
            # Try alternate pattern
            pattern = rf'<a[^>]*href="/{USERNAME}/([^"/?]+)"[^>]*>'
            all_links = re.findall(pattern, html)
            # Filter to actual deck slugs (not empty, not pagination)
            matches = [m for m in all_links if m and m not in ['', 'followers', 'following']]

        # Get titles
        title_pattern = r'class="deck-title[^"]*"[^>]*>([^<]+)<'
        titles = re.findall(title_pattern, html)

        # Combine - dedupe
        for slug in matches:
            if slug and not any(p['slug'] == slug for p in presentations):
                presentations.append({'slug': slug, 'title': None})

        # Check for next page
        if 'page=' + str(page + 1) not in html and page > 1:
            break

        time.sleep(1)  # Be nice to the server

    print(f"Found {len(presentations)} presentations")
    return presentations


def get_presentation_details(slug):
    """Fetch detailed metadata for a single presentation."""
    url = f"{BASE_URL}/{USERNAME}/{slug}"
    print(f"  Fetching details: {slug}")

    html = fetch_html(url)
    if not html:
        return None

    details = {
        'slug': slug,
        'url': url
    }

    # Extract title
    title_match = re.search(r'<h1[^>]*class="[^"]*deck-title[^"]*"[^>]*>([^<]+)</h1>', html)
    if title_match:
        details['title'] = title_match.group(1).strip()
    else:
        # Alternate: og:title
        og_title = re.search(r'<meta[^>]*property="og:title"[^>]*content="([^"]+)"', html)
        if og_title:
            details['title'] = og_title.group(1).strip()

    # Extract description
    desc_match = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]+)"', html)
    if desc_match:
        details['description'] = desc_match.group(1).strip()
    else:
        details['description'] = ''

    # Extract date
    date_match = re.search(r'<time[^>]*datetime="([^"]+)"', html)
    if date_match:
        details['date'] = date_match.group(1)

    # Extract deck ID for PDF download
    deck_id_match = re.search(r'data-id="([^"]+)"', html)
    if deck_id_match:
        details['deck_id'] = deck_id_match.group(1)

    # Try to find slide count
    slide_match = re.search(r'(\d+)\s*slides?', html, re.IGNORECASE)
    if slide_match:
        details['slide_count'] = int(slide_match.group(1))

    # Look for PDF download URL
    # SpeakerDeck uses: https://files.speakerdeck.com/presentations/{deck_id}/{slug}.pdf
    if 'deck_id' in details:
        details['pdf_url'] = f"https://files.speakerdeck.com/presentations/{details['deck_id']}/{slug}.pdf"

    # Also try to find direct download link in page
    pdf_link_match = re.search(r'href="([^"]+\.pdf)"', html)
    if pdf_link_match:
        details['pdf_url'] = pdf_link_match.group(1)

    # Extract event name if present
    event_match = re.search(r'presented at[^<]*<a[^>]*>([^<]+)</a>', html, re.IGNORECASE)
    if event_match:
        details['event'] = event_match.group(1).strip()

    return details


def slugify(text):
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def load_existing_titles():
    """Load existing talk titles from Hugo content."""
    titles = set()
    if CONTENT_DIR.exists():
        for md_file in CONTENT_DIR.glob("*.md"):
            with open(md_file) as f:
                content = f.read()
                match = re.search(r'^title:\s*["\']?([^"\'\n]+)["\']?', content, re.MULTILINE)
                if match:
                    titles.add(match.group(1).strip())
    return titles


def generate_hugo_content(details, existing_titles):
    """Generate Hugo markdown content for a presentation."""
    title = details.get('title', details['slug'])

    # Check for duplicates
    if title in existing_titles:
        return None, "duplicate"

    # Generate unique slug with -sd suffix
    slug = f"{slugify(title)}-sd"

    # Parse date
    date_str = details.get('date', '')
    if date_str:
        try:
            # Handle various date formats
            if 'T' in date_str:
                dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            else:
                dt = datetime.strptime(date_str, '%Y-%m-%d')
            date_formatted = dt.strftime('%Y-%m-%dT08:00:00')
        except:
            date_formatted = '2015-01-01T08:00:00'  # Default for old talks
    else:
        date_formatted = '2015-01-01T08:00:00'

    # Build front matter
    front_matter = {
        'title': title,
        'slug': slug,
        'date': date_formatted,
        'event': details.get('event', ''),
        'location': '',
        'image': f"/images/{details['slug']}/slide_000.jpg",
        'pdf': f"/pdfs/{details['slug']}.pdf",
        'source': 'speakerdeck',
        'speakerdeck_slug': details['slug'],
    }

    # Build markdown
    lines = ['---']
    for key, value in front_matter.items():
        if isinstance(value, str) and ('"' in value or ':' in value):
            lines.append(f'{key}: "{value}"')
        else:
            lines.append(f'{key}: "{value}"' if isinstance(value, str) else f'{key}: {value}')
    lines.append('---')
    lines.append('')
    lines.append(details.get('description', ''))
    lines.append('')

    return '\n'.join(lines), details['slug']


def generate_thumbnail_from_pdf(pdf_path, output_dir):
    """Generate thumbnail image from first page of PDF."""
    try:
        from pdf2image import convert_from_path

        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "slide_000.jpg"

        if output_path.exists():
            return True

        # Convert first page only
        images = convert_from_path(pdf_path, first_page=1, last_page=1, dpi=150)
        if images:
            images[0].save(output_path, 'JPEG', quality=85)
            return True
    except ImportError:
        print("  Warning: pdf2image not installed, skipping thumbnail generation")
    except Exception as e:
        print(f"  Error generating thumbnail: {e}")
    return False


def main():
    """Main import function."""
    print("=" * 60)
    print("SpeakerDeck Import")
    print("=" * 60)

    # Create directories
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    PDFS_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    # Load existing titles to avoid duplicates
    existing_titles = load_existing_titles()
    print(f"Found {len(existing_titles)} existing talks in Hugo content")

    # Get presentation list
    presentations = get_presentation_list()

    # Fetch details for each
    print("\nFetching presentation details...")
    detailed_presentations = []
    for pres in presentations:
        details = get_presentation_details(pres['slug'])
        if details:
            detailed_presentations.append(details)
        time.sleep(0.5)  # Rate limiting

    # Save metadata
    with open(EXPORT_DIR / "presentations.json", 'w') as f:
        json.dump(detailed_presentations, f, indent=2)
    print(f"\nSaved metadata for {len(detailed_presentations)} presentations")

    # Process each presentation
    print("\nProcessing presentations...")
    imported = []
    skipped = []
    failed = []

    for details in detailed_presentations:
        slug = details['slug']
        title = details.get('title', slug)
        print(f"\n[{slug}] {title}")

        # Generate Hugo content
        content, result = generate_hugo_content(details, existing_titles)
        if result == "duplicate":
            print(f"  Skipping: duplicate of existing talk")
            skipped.append(slug)
            continue

        # Download PDF
        pdf_path = PDFS_DIR / f"{slug}.pdf"
        if 'pdf_url' in details:
            print(f"  Downloading PDF...")
            if not download_file(details['pdf_url'], pdf_path):
                print(f"  Failed to download PDF")
                # Try alternate URL formats
                alt_urls = [
                    f"https://speakerdeck.com/{USERNAME}/{slug}/download",
                    f"https://files.speakerdeck.com/presentations/{slug}.pdf",
                ]
                downloaded = False
                for alt_url in alt_urls:
                    if download_file(alt_url, pdf_path):
                        downloaded = True
                        break
                if not downloaded:
                    failed.append(slug)
                    continue

        # Generate thumbnail
        if pdf_path.exists():
            print(f"  Generating thumbnail...")
            img_dir = IMAGES_DIR / slug
            generate_thumbnail_from_pdf(pdf_path, img_dir)

        # Save markdown
        md_path = EXPORT_DIR / "content" / f"{slug}.md"
        md_path.parent.mkdir(parents=True, exist_ok=True)
        with open(md_path, 'w') as f:
            f.write(content)
        print(f"  Created: {md_path.name}")

        imported.append(slug)
        existing_titles.add(title)  # Prevent duplicates within this run

    # Summary
    print("\n" + "=" * 60)
    print("Import Summary")
    print("=" * 60)
    print(f"Imported: {len(imported)}")
    print(f"Skipped (duplicates): {len(skipped)}")
    print(f"Failed: {len(failed)}")

    if imported:
        print(f"\nNew content saved to: {EXPORT_DIR / 'content'}")
        print(f"PDFs saved to: {PDFS_DIR}")
        print(f"Images saved to: {IMAGES_DIR}")
        print("\nTo complete import, run:")
        print(f"  cp {EXPORT_DIR}/content/*.md {CONTENT_DIR}/")
        print(f"  cp -r {PDFS_DIR}/* {SITE_DIR}/static/pdfs/")
        print(f"  cp -r {IMAGES_DIR}/* {SITE_DIR}/static/images/")


if __name__ == "__main__":
    main()
