#!/usr/bin/env python3
"""
Generate Hugo content pages from exported noti.st JSON files.
"""

import json
import os
import re
from pathlib import Path
from datetime import datetime

EXPORT_DIR = Path("export")
EMBEDS_DIR = EXPORT_DIR / "embeds"
SITE_DIR = Path("site")
CONTENT_DIR = SITE_DIR / "content"

def load_embeds(pres_id):
    """Load embedded content (Twitter, YouTube, etc.) for a presentation."""
    embed_file = EMBEDS_DIR / f"{pres_id}.json"
    if embed_file.exists():
        with open(embed_file) as f:
            return json.load(f)
    return None

def slugify(text):
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')

def parse_date(date_str):
    """Parse date string to datetime."""
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            return None

def extract_text(html_content):
    """Extract plain text from HTML, preserving some structure."""
    if not html_content:
        return ""
    # Simple HTML tag removal
    text = re.sub(r'<[^>]+>', ' ', html_content)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def generate_markdown(pres_data, pres_id):
    """Generate Hugo markdown content from presentation data."""
    if 'data' not in pres_data or not pres_data['data']:
        return None

    pres = pres_data['data'][0]
    attrs = pres.get('attributes', {})
    relationships = pres.get('relationships', {}).get('data', [])

    # Extract basic info
    title = attrs.get('title', 'Untitled')
    slug = attrs.get('slug', slugify(title))
    blurb = attrs.get('blurb', {}).get('html', '')
    download_url = attrs.get('download', '')

    # Extract event info
    event_name = ''
    event_location = ''
    event_date = None

    for rel in relationships:
        if rel.get('type') == 'events':
            event_attrs = rel.get('attributes', {})
            event_name = event_attrs.get('title', '')
            event_location = event_attrs.get('address', '')
            event_date_str = event_attrs.get('starts_on', '')
            if event_date_str:
                event_date = parse_date(event_date_str)

    # Get presentation date from profile data if available
    # (we'll use the relationship event date as fallback)

    # Extract resources
    resources = []
    resource_data = attrs.get('resources', {}).get('data', [])
    for res in resource_data:
        resources.append({
            'title': res.get('title', ''),
            'url': res.get('url', ''),
            'description': extract_text(res.get('desc', {}).get('html', ''))
        })

    # Get thumbnail image (first slide only)
    thumbnail = ''
    slidedeck = attrs.get('slidedeck', {})
    if isinstance(slidedeck, dict) and 'data' in slidedeck:
        for deck in slidedeck['data']:
            deck_slides = deck.get('slides', [])
            if deck_slides:
                # Only get first slide for thumbnail
                first_slide = deck_slides[0]
                original_url = first_slide.get('image', '')
                # Determine file extension from URL
                ext = os.path.splitext(original_url.split('?')[0])[1] or '.jpg'
                # Use local path for thumbnail
                thumbnail = f"/images/{pres_id}/slide_000{ext}"
                break

    # Use local PDF path
    local_pdf = f"/pdfs/{pres_id}.pdf" if download_url else ''

    # Load embeds (Twitter, YouTube, etc.)
    embeds_data = load_embeds(pres_id)
    embeds = []
    if embeds_data:
        # Add Twitter embeds
        for tweet_html in embeds_data.get('twitter_embeds', []):
            embeds.append({
                'type': 'twitter',
                'html': tweet_html
            })
        # Add YouTube embeds
        for youtube_html in embeds_data.get('youtube_embeds', []):
            embeds.append({
                'type': 'youtube',
                'html': youtube_html
            })
        # Add Vimeo embeds
        for vimeo_html in embeds_data.get('vimeo_embeds', []):
            embeds.append({
                'type': 'vimeo',
                'html': vimeo_html
            })

    # Build front matter (without slides array, with embeds)
    front_matter = {
        'title': title,
        'slug': slug,
        'date': event_date.isoformat() if event_date else '',
        'event': event_name,
        'location': event_location,
        'description': blurb,
        'image': thumbnail,
        'pdf': local_pdf,
        'original_pdf': download_url,  # Keep original for reference
        'notist_id': pres_id,
        'resources': resources,
        'embeds': embeds
    }

    return front_matter

def write_content_file(front_matter, pres_id):
    """Write Hugo content file."""
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    # Create unique filename using the noti.st ID to avoid collisions
    # (same talk given at different events has same slug)
    filename = f"{pres_id}.md"
    filepath = CONTENT_DIR / filename

    # Build YAML front matter
    # Use ID as slug suffix to ensure unique URLs
    unique_slug = f"{front_matter['slug']}-{pres_id}"
    lines = ['---']
    lines.append(f'title: "{front_matter["title"]}"')
    lines.append(f'slug: "{unique_slug}"')
    if front_matter['date']:
        lines.append(f'date: {front_matter["date"]}')
    if front_matter['event']:
        lines.append(f'event: "{front_matter["event"]}"')
    if front_matter['location']:
        lines.append(f'location: "{front_matter["location"]}"')
    if front_matter['image']:
        lines.append(f'image: "{front_matter["image"]}"')
    if front_matter['pdf']:
        lines.append(f'pdf: "{front_matter["pdf"]}"')
    lines.append(f'notist_id: "{front_matter["notist_id"]}"')

    # Resources as YAML array
    if front_matter['resources']:
        lines.append('resources:')
        for res in front_matter['resources']:
            lines.append(f'  - title: "{res["title"]}"')
            lines.append(f'    url: "{res["url"]}"')
            if res['description']:
                # Escape quotes in description
                desc = res['description'].replace('"', '\\"')
                lines.append(f'    description: "{desc}"')

    # Embeds as YAML array with literal block scalars for HTML
    if front_matter['embeds']:
        lines.append('embeds:')
        for embed in front_matter['embeds']:
            lines.append(f'  - type: "{embed["type"]}"')
            # Use YAML literal block scalar (|) for HTML content
            lines.append('    html: |')
            # Indent the HTML by 6 spaces for proper YAML block scalar
            html_lines = embed['html'].split('\n')
            for html_line in html_lines:
                lines.append(f'      {html_line}')

    lines.append('---')
    lines.append('')

    # Add description as content body
    if front_matter['description']:
        lines.append(front_matter['description'])

    content = '\n'.join(lines)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath

def main():
    print("=" * 60)
    print("Hugo Content Generator")
    print("=" * 60)

    pres_dir = EXPORT_DIR / "presentations"
    if not pres_dir.exists():
        print("No presentations directory found. Run export first.")
        return

    json_files = list(pres_dir.glob("*.json"))
    print(f"Found {len(json_files)} presentation JSON files")

    created = 0
    skipped = 0

    for json_file in sorted(json_files):
        pres_id = json_file.stem
        try:
            with open(json_file, encoding='utf-8') as f:
                pres_data = json.load(f)

            front_matter = generate_markdown(pres_data, pres_id)
            if front_matter:
                filepath = write_content_file(front_matter, pres_id)
                print(f"  Created: {filepath.name}")
                created += 1
            else:
                print(f"  Skipped: {pres_id} (no data)")
                skipped += 1
        except Exception as e:
            print(f"  Error processing {pres_id}: {e}")
            skipped += 1

    print("\n" + "=" * 60)
    print(f"Content generation complete!")
    print(f"  Created: {created}")
    print(f"  Skipped: {skipped}")
    print(f"  Output: {CONTENT_DIR.absolute()}")
    print("=" * 60)

if __name__ == "__main__":
    main()
