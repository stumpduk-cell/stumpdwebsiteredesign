# Stump’d website pre-launch quality check

Checked: 18 September 2026

## Release recommendation

**Not ready to attach the production domain yet.** The content and core static structure are in good shape, but the deployed `main` branch must be consolidated and checked before launch. This checkout does not contain the same Pathway/card files or uploaded photographs that have appeared in the deployed previews, so a successful check here does not prove that the production artifact is correct.

## Must complete before launch

1. **Audit the actual merged `main` artifact.** Previous pull requests introduced alternative Pathway documents, rewrites and stylesheets. Confirm that exactly one Pathway implementation is deployed and that `/pathway/` returns the intended page.
2. **Verify every production image returns HTTP 200.** This checkout references `IMG-20260918-WA0030.jpg`, `IMG-20260918-WA0031.jpg` and `IMG-20260918-WA0032.jpg`, but those files are not present locally. Confirm them in the deployment before changing DNS.
3. **Check all young-person photography permissions.** Confirm appropriate consent covers public website publication, not only session photography.
4. **Exercise the enquiry journey on real devices.** The form opens the visitor’s configured email client rather than submitting online. Test on iPhone, Android, Windows and macOS, and retain the visible email-address fallback.
5. **Confirm domain essentials.** Configure the custom domain, HTTPS redirect, preferred `www`/apex host, DNS records and Cloudflare production branch. Then test both host variants and all redirect rules.

## High-priority improvements

- **Query parameters are not applied to the form.** Links use `?type=school`, `?type=club` and `?type=pathway`, but the script does not select the corresponding enquiry type. Either implement this or remove the parameters.
- **Keyboard focus needs an intentional treatment.** Interactive controls mostly rely on browser defaults. Add a consistent, high-contrast `:focus-visible` outline before launch.
- **Move the homepage media stylesheet into `<head>`.** The current link appears after `<body>` starts. Browsers generally recover, but it is avoidable invalid document structure and can delay styling.
- **Avoid a CSS `@import` for production fonts.** A normal `<link>` in each document, ideally with preconnects or self-hosted font files, avoids an extra render-blocking request.
- **Add discoverability metadata.** The site has useful titles and descriptions, but no canonical URLs, Open Graph/Twitter metadata, favicon references, `robots.txt` or `sitemap.xml` in this checkout.
- **Show the active navigation item.** The CSS supports `[aria-current=page]`, but the HTML does not set it.

## Checks that passed in this checkout

- Every HTML document parses with Python's HTML parser.
- Every content page has a unique title, one `<h1>`, a viewport declaration and a `lang="en-GB"` root language.
- All pages except the intentionally minimal 404 page have a meta description.
- Content pages provide a skip link targeting the main content landmark.
- Form fields have associated labels, required fields are declared and the status message uses `aria-live="polite"`.
- JavaScript passes Node syntax checking.
- CSS braces are balanced.
- Security headers cover MIME sniffing, framing, referrer policy, permissions and a restrictive content security policy.
- Internal page routes referenced in HTML map to documents in this checkout.
- The legal, privacy and safeguarding pages are present and linked from the footer.
- Responsive breakpoints collapse navigation, grids, programmes and the footer for narrow screens.

## Font rationale and recommendation

### Why Manrope works for headings

Manrope is geometric, compact and assertive. Its heavy weights suit short, high-impact phrases such as “Think well. Play better.” and give the site a contemporary sports/editorial character. The tight tracking and large scale make it part of the brand voice rather than ordinary interface text. It is worth retaining for headings.

### Why DM Sans was chosen for body copy

DM Sans has open letterforms, a large x-height and dependable rendering at small sizes. It is neutral enough not to compete with Manrope, offers all the weights used by navigation and forms, and is available from the same font service. Those are practical reasons for the pairing.

The drawback is the one identified in review: DM Sans is now widely used and its neutrality makes the body copy feel like a generic modern product site. It is competent, but it adds little personality.

### Recommended replacement: Hanken Grotesk

Use **Hanken Grotesk** for body copy, navigation, labels and forms while retaining Manrope for headings. It remains clean and highly readable, but its more human proportions and slightly warmer shapes should better support a young-person/coaching brand. It is distinctive without becoming informal or distracting.

**Decision:** this pairing is now implemented in the site stylesheet, using Arial and the generic sans-serif family as fallbacks.

As a final visual check, compare the homepage and a long legal page at desktop and mobile widths. Body-font changes affect line wrapping, section height and navigation fit, so those views should be checked before launch.

### Alternatives

- **Albert Sans:** calm and polished, with more character than DM Sans but still close to a geometric product aesthetic.
- **Atkinson Hyperlegible Next:** strongest accessibility-led option; highly legible, though more functional in tone.
- **Source Sans 3:** exceptionally dependable for long reading, but not substantially less familiar or generic.

## Post-domain smoke test

After attaching the domain, verify:

- HTTP redirects to HTTPS.
- Only the preferred hostname is indexed.
- `/`, `/schools/`, `/clubs/`, `/pathway/`, `/team/`, `/contact/`, policy pages and a nonexistent URL return the expected status and content.
- No browser console errors, mixed-content warnings or CSP violations occur.
- Images, logos and fonts return 200 responses and have correct MIME types.
- Mobile navigation opens, closes and returns keyboard focus predictably.
- The enquiry form opens a correctly addressed email with all entered values.
- Page titles, descriptions and social previews are correct.
- A keyboard-only pass and 200% zoom pass remain usable without horizontal scrolling.
