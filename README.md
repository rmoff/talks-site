# Talks Archive

Static archive of Robin Moffatt's conference talks, originally hosted on [noti.st](https://noti.st/rmoff).

**Live site:** https://talks.rmoff.net

## Structure

- `site/` - Hugo site source
- `export/` - Raw export from noti.st (not committed)
- `export_notist.py` - Script to export data from noti.st API
- `generate_hugo_content.py` - Script to generate Hugo content from exported JSON
- `copy_assets_to_site.py` - Script to copy downloaded assets to Hugo static folder

## Local Development

Requires Docker.

```bash
# Build the site
docker run --rm -v $(pwd)/site:/src ghcr.io/rmoff/rmoff-blog:0.152.2

# Serve locally with live reload
docker run --rm -it -v $(pwd)/site:/src -p 1313:1313 ghcr.io/rmoff/rmoff-blog:0.152.2 server --bind 0.0.0.0
```

## Re-exporting from noti.st

If you need to re-export from noti.st:

```bash
# Export all presentation metadata
python3 export_notist.py

# Download all slides and PDFs
python3 export_notist.py --assets-only

# Generate Hugo content files
python3 generate_hugo_content.py

# Copy assets to Hugo static folder
python3 copy_assets_to_site.py
```

## Deployment

The site automatically deploys to GitHub Pages when pushing to the `main` branch via GitHub Actions.

## License

Content is copyright Robin Moffatt. Site code is MIT licensed.
