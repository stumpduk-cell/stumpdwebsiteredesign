# Stump’d preview site

Text-only static preview for Stump’d. The official logo and authentic photography are locked assets; labelled HTML/CSS placeholders are used until those assets are supplied.

## Cloudflare Pages

- **Framework preset:** None
- **Build command:** leave blank
- **Output directory:** `site`

No build step or dependencies are required. For local preview, run `python3 -m http.server 8000 --directory site` from the repository root.

The preview intentionally uses `noindex,nofollow` in page metadata and response headers. Replace placeholder policy links and review the Content Security Policy before adding production services or assets.
