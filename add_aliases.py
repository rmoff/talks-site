#!/usr/bin/env python3
"""Add Hugo aliases to content files for redirects from old noti.st URLs."""

import os
import re
from pathlib import Path

CONTENT_DIR = Path("site/content")

def extract_front_matter(content):
    """Extract front matter and body from markdown content."""
    if not content.startswith("---"):
        return None, content

    # Find the closing ---
    end_match = re.search(r'\n---\n', content[3:])
    if not end_match:
        return None, content

    end_pos = end_match.start() + 3
    front_matter = content[4:end_pos]
    body = content[end_pos + 5:]

    return front_matter, body

def parse_yaml_value(front_matter, key):
    """Extract a value from YAML front matter."""
    match = re.search(rf'^{key}:\s*["\']?([^"\'\n]+)["\']?\s*$', front_matter, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None

def add_alias_to_front_matter(front_matter, alias):
    """Add an alias to front matter if not already present."""
    # Check if aliases already exist
    if 'aliases:' in front_matter:
        # Check if this alias is already there
        if alias in front_matter:
            return front_matter, False
        # Add to existing aliases array
        front_matter = re.sub(
            r'(aliases:\s*\[)',
            rf'\1"{alias}", ',
            front_matter
        )
        return front_matter, True

    # Add new aliases field after slug
    front_matter = re.sub(
        r'(slug:\s*["\'][^"\']+["\'])\n',
        rf'\1\naliases: ["{alias}"]\n',
        front_matter
    )
    return front_matter, True

def process_file(filepath):
    """Process a single content file."""
    with open(filepath, 'r') as f:
        content = f.read()

    front_matter, body = extract_front_matter(content)
    if not front_matter:
        return None, "No front matter found"

    notist_id = parse_yaml_value(front_matter, 'notist_id')
    slug = parse_yaml_value(front_matter, 'slug')

    if not notist_id:
        return None, "No notist_id"

    if not slug:
        return None, "No slug"

    # Calculate original slug (without notist_id suffix)
    orig_slug = re.sub(rf'-{notist_id}$', '', slug)

    # Old noti.st URL format
    old_url = f"/{notist_id}/{orig_slug}"

    # Add alias
    new_front_matter, changed = add_alias_to_front_matter(front_matter, old_url)

    if changed:
        new_content = f"---\n{new_front_matter}\n---\n{body}"
        with open(filepath, 'w') as f:
            f.write(new_content)
        return old_url, "Added alias"
    else:
        return old_url, "Already has alias"

def main():
    added = 0
    skipped = 0
    errors = 0

    for filepath in sorted(CONTENT_DIR.glob("*.md")):
        result, status = process_file(filepath)

        if result:
            if status == "Added alias":
                print(f"✓ {filepath.name}: {result}")
                added += 1
            else:
                print(f"- {filepath.name}: {status}")
                skipped += 1
        else:
            print(f"✗ {filepath.name}: {status}")
            errors += 1

    print(f"\nSummary: {added} added, {skipped} skipped, {errors} errors")

if __name__ == "__main__":
    main()
