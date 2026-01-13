# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **static archive of conference talks** originally hosted on noti.st, now self-hosted at https://talks.rmoff.net using Hugo and GitHub Pages. The project consists of Python scripts that export data from the noti.st API and a Hugo static site generator setup.

## Architecture

### Data Pipeline (3-stage process)

1. **Export from noti.st API** → `export/` directory (not committed to git)
2. **Transform to Hugo content** → `site/content/*.md` files (committed)
3. **Copy static assets** → `site/static/{images,pdfs}` (committed)
   - **Images**: Only first slide (thumbnail) per talk (~97 files, 37MB)
   - **PDFs**: Full slide decks (~93 files, 3.6GB)

### Hugo Site Structure

- **Content files**: Each talk is a markdown file in `site/content/` named by noti.st ID (e.g., `9GpIYA.md`)
- **Slug format**: `{original-slug}-{notist_id}` to ensure uniqueness (same talk given at multiple events)
- **Theme**: Custom minimal theme in `site/themes/talks/`
- **Layouts**:
  - `index.html` - Homepage with card-based talk listing (reverse chronological)
  - `single.html` - Individual talk page with hero image, abstract, resources, and PDF download
- **Front matter**: YAML with title, date, event, location, thumbnail image, resources array, PDF path
- **Design philosophy**: PDF-centric - full slide decks available for download, title slide shown as hero image

### Deployment

- **CI/CD**: GitHub Actions (`.github/workflows/deploy.yml`) on push to `main`
- **Build environment**: GitHub Actions currently uses `ghcr.io/rmoff/rmoff-blog:0.152.2` (legacy, has other blog dependencies)
- **Domain**: `talks.rmoff.net` configured via `site/static/CNAME`

## Common Commands

### Local Development

Use the native `hugomods/hugo` Docker image for local development:

```bash
# Preview site locally (port 1313)
docker run --rm -v $(pwd)/site:/src -p 1313:1313 hugomods/hugo:latest server --bind 0.0.0.0

# Build site (outputs to site/public/)
docker run --rm -v $(pwd)/site:/src hugomods/hugo:latest
```

### Re-export from noti.st

**Important**: The `export/` directory is `.gitignore`d. Only the generated Hugo content and copied assets are committed.

```bash
# Full export: metadata + assets
python3 export_notist.py

# Re-download assets only (from saved JSON)
python3 export_notist.py --assets-only

# Scrape Twitter/YouTube embeds from HTML pages (supplemental to API)
python3 scrape_embeds.py

# Generate Hugo markdown from exported JSON (includes embeds)
python3 generate_hugo_content.py

# Copy assets to Hugo static folder
python3 copy_assets_to_site.py
```

### File Operations

When working with content:
- Each markdown file in `site/content/` represents one talk presentation
- Filenames use noti.st ID format (6 alphanumeric characters)
- Thumbnail images: `site/static/images/{notist_id}/slide_000.{ext}` (first slide only)
- PDFs: `site/static/pdfs/{notist_id}.pdf`
- Total static assets: ~190 files (97 thumbnails + 93 PDFs)

## Key Technical Details

### Python Scripts

- **`export_notist.py`**:
  - Fetches from `https://noti.st/{USERNAME}.json` and individual presentation endpoints
  - Includes retry logic (3 attempts) and concurrent downloads
  - Saves JSON to `export/presentations/{id}.json`

- **`generate_hugo_content.py`**:
  - Parses noti.st JSON structure (data[0].attributes, relationships.data[])
  - Converts HTML blurbs to plain text (preserves HTML in description for embeds)
  - Creates unique slugs by appending noti.st ID
  - Generates YAML front matter with thumbnail image (first slide only), resources array, PDF path
  - **No slides array** - only references first slide as thumbnail

- **`copy_assets_to_site.py`**:
  - Copies only first slide (slide_000.*) from each presentation as thumbnail
  - Copies all PDFs from export/pdfs to site/static/pdfs
  - Result: ~97 thumbnails + 93 PDFs instead of 7,244 slide images

### Hugo Configuration

- `baseURL`: https://talks.rmoff.net/
- `theme`: "talks" (custom theme in `site/themes/talks/`)
- `markup.goldmark.renderer.unsafe`: true (allows HTML in markdown)
- `permalinks.talks`: "/:slug/" (uses slug from front matter)
- Outputs: HTML and RSS for home and sections

### Content Structure

Markdown front matter example:
```yaml
---
title: "Talk Title"
slug: "talk-slug-9GpIYA"
date: 2024-09-17T08:00:00
event: "Conference Name"
location: "City, State, Country"
image: "/images/9GpIYA/slide_000.jpg"
pdf: "/pdfs/9GpIYA.pdf"
notist_id: "9GpIYA"
resources:
  - title: "Resource Title"
    url: "https://example.com"
    description: "Resource description"
---

<p>Talk abstract/description with HTML preserved (for Twitter embeds, etc.)</p>
```

**Note**: The `slides` array has been removed. Only the `image` field remains, pointing to the first slide thumbnail.

## Theme Design

The site uses a clean, minimal design:

**Homepage** (`index.html`):
- Card-based layout with thumbnail, title, event, date, location
- Reverse chronological order
- Responsive grid

**Talk Pages** (`single.html`):
- Hero image (title slide) displayed prominently at top
- Talk metadata (event, date, location)
- Description/abstract (HTML preserved for Twitter embeds, etc.)
- Resources section (links with descriptions)
- PDF download button

**Styling** (`style.css`):
- Dark header (#1a1a2e) with light content
- Card-based design with hover effects
- Responsive with mobile-friendly breakpoints
- Professional typography and spacing

## Embed Handling

**Twitter Embeds - SOLVED**
- Twitter embeds are NOT available in the noti.st API
- Solution: `scrape_embeds.py` scrapes the live noti.st HTML pages to extract embed codes
- **61 out of 97 presentations** have Twitter embeds (mostly audience feedback tweets)
- Embeds are stored in `export/embeds/{presentation_id}.json`
- `generate_hugo_content.py` reads these and adds them to the front matter
- Hugo template renders them with Twitter's widgets.js for proper display
- No YouTube/Vimeo embeds found (video links are captured as resources instead)

## Important Notes

- Use `hugomods/hugo:latest` for local development (standard Hugo image)
- GitHub Actions workflow still uses the bespoke `ghcr.io/rmoff/rmoff-blog:0.152.2` image but should be updated
- The `export/` directory should never be committed (contains raw downloads)
- Markdown files in `site/content/` use noti.st IDs as filenames, not slugs
- PDFs are large (3.6GB total) but necessary for the archive purpose
- Site uses a PDF-centric approach: full decks available, individual slides not displayed
