# hetshahbuilds.in site build notes

Last updated 14 Nov 2026 (13 Nov: page restructured, names cleared, profile PDF added, availability line and About employer names taken off, site deployed on Cloudflare Workers; 14 Nov: hetshahbuilds.in connected, launch extras added). Read `CLAUDE.md` and `docs/content-plan.md` first, then this.

## What exists

- **Template:** GetLayers "Marcus Vane" (free tier, commercial licence), rebuilt as a static single page with Het's content.
- **Files, in the Portfolio folder on Het's computer:**
  - `site/index.html` (the whole page: markup, CSS, JS)
  - `site/assets/work-01-platform.svg`, `work-02-llm-pipeline.svg`, `work-03-ingestion.svg`, `work-04-observability.svg`
  - `tools/gen_art.py` regenerates the four visuals: `python3 gen_art.py <anton.woff> <out_dir>` (needs fontTools; labels are converted to outlines)
  - `profile/profile.html` and `profile/Het_Shah_Profile.pdf`: the one-page profile for intermediaries to forward
- **Preview:** private artifact titled "Het Shah | Backend and AI systems engineer". Republished on 13 Nov 2026 with the restructured page. Its four diagram files were left as they were; they are the same drawings as the local ones.
- **Stack:** plain HTML, CSS and JS, no build step. Fonts Anton and Onest from Google Fonts. Lenis 1.3.19 from jsDelivr. `site/` deploys as it is.

## Decisions in force

- **Purpose (Het, 13 Nov 2026):** a profile of Het for freelancing, shared through people who represent him to clients. It is about Het (skills, what he has built, client projects), **not a sales page**: no services, prices or engagement terms. Structure: `docs/content-plan.md`.
- **Names (Het, 13 Nov 2026):** the site names Infocusp Innovations, Crest Data, LearnElectronics, Armis, Comcast and Splunk. Clients are always shown as Crest Data's customers ("Armis, through Crest Data"). Internal product and platform names stay out until Het clears them. Later that evening Het had Infocusp Innovations and Crest Data taken out of the About intro, in wording he supplied, so that paragraph names Armis, Comcast and Splunk without "through Crest Data". The Experience rows, the Work cards and the profile PDF still name the employers; he hasn't asked to change them.
- **Availability line: removed (Het, 13 Nov 2026, evening).** He approved "Available part-time for contract work" earlier that day, then asked for it off the hero and the contact block "for now". The hero keeps "Ahmedabad, IST · Remote" and the contact block keeps "Based in Ahmedabad (IST), working remotely." The profile PDF still carries the availability line, because the request named the site's header and footer. Put the line back in the same places if he asks.
- **Contact:** hetshah2000@gmail.com, LinkedIn and GitHub (github.com/het-shah2000). No phone number.
- **Domain:** hetshahbuilds.in, bought at one.com, nameservers moved to Cloudflare. Connected 14 Nov 2026: `hetshahbuilds.in` is a custom domain on the Worker; `www` is a proxied placeholder A record (192.0.2.1) plus a Redirect Rule that 301s `https://www.*` to the bare domain with the query string kept. Don't add `www` as a Worker custom domain. Checked 14 Nov: the bare domain serves the site, `www` redirects, and the résumé, `docs/` and `CLAUDE.md` return 404.
- **Certifications:** the AWS Solutions Architect Associate line stays and links to the Credly badge from the résumé. The Anthropic certifications line was removed, because Het's answer kept only the AWS name. Restore it if he asks.
- **Personal projects:** no "Built on my own" row. Het said to skip it for now. His GitHub has three repos (a 2025 Flask and React weather app with placeholder demo links, a 2021 college project and a fork); none shows the work this site is about.
- **Hosting:** Cloudflare Workers with static assets (13 Nov 2026), deployed from the private GitHub repo github.com/het-shah2000/portfolio on every push to `main`. Live at hetshahbuilds.hetshah2000.workers.dev. Cloudflare now labels Pages "legacy", so Workers was chosen instead. Checked on 13 Nov 2026: only `site/` is served; the résumé, `docs/`, `tools/`, `profile/` and `CLAUDE.md` return 404. `wrangler.jsonc` at the repo root pins `assets.directory` to `./site`. Not Vercel Hobby, because the site promotes paid work.
- **Git:** the résumé PDF and `.tex` are in `.gitignore` and not committed.
- **Product-name check (14 Nov 2026):** `site/` and `profile/profile.html` carry none of the résumé's internal product names. Generic phrases the content plan uses ("Multi-tenant AppSec platform", "content pack modules", "observability suite") are fine.
- Analytics must be visible to Het only. Not added yet; there is a placeholder comment at the end of `index.html` for the host's snippet.
- The résumé PDF and `.tex` must not be deployed: they carry a phone number.
- No invented testimonials. The Voices section stays out until real recommendations arrive.
- The weekly chart in diagram 1 (six days near 250K, one day at 1.5M) is confirmed by Het.

## Section map (as built, 13 Nov 2026)

| # | Section | What is in it |
|---|---|---|
| 1 | Preloader, fixed nav, mobile menu | Nav: About, Experience, Work, Skills, Contact |
| 2 | Hero | Location line (Ahmedabad, IST · Remote); Backend / Cloud / AI Systems / Reliability; positioning line; HET / SHAH |
| 3 | Marquee | Five operating principles |
| 4 | About (`#about`) | Heading, an intro paragraph (who, where, what he builds, how he works, what he is on now; no employer names), the method paragraph, AWS certification and education, then "How I build" with the four numbered principles |
| 5 | Experience (`#experience`) | Three rows: Infocusp Innovations, Crest Data, LearnElectronics |
| 6 | Work (`#work`, cards `#work-01` to `#work-04`) | Each card: diagram, numbered title, blurb, scale and outcome, client, my role, detail bullets, stack |
| 7 | Impact (`#impact`) | 32, 1.5M, 212K, 85%. Unchanged. |
| 8 | Skills (`#skills`) | Nine rows, each linking to the cards that used it, plus an "Also" line |
| 9 | Voices | Left out for now |
| 10 | Contact (`#contact`) and footer | "Get in touch.", location line, email, then LinkedIn, GitHub and Email links |

## Deliberate departures from the template prompt

- **No portrait or hero video yet.** The hero runs name-only. The portrait block is commented out in `index.html`; to switch it on, add a transparent cut-out at `site/assets/portrait.webp`, uncomment the block, and add class `has-portrait` to the hero section. That class also restores the template's tighter name stack and deeper bottom fade.
- **Hero status block placement.** It now holds only the location ("Ahmedabad, IST · Remote"); it held the availability line until the evening of 13 Nov. On phones it is a small block to the right of the role words. From 640px it is one line above the top row, in the gap under the nav. Both spots were empty, so the roles, the description and the name did not move.
- **Name sizing.** The name is capped by viewport height so it never runs into the top row, and the two lines get a hairline gap when there is no portrait. Phone size is at most 10.5rem so SHAH fits inside the gutters. Since 13 Nov, on phones without a portrait the name is also capped by the room left under the description (the top block is 24.4rem tall at every phone width). On very short screens it stops shrinking at 6rem and the hero grows past one screen instead. Before this, the description overlapped the name by about 22px on a 375 by 548 viewport (iPhone SE in Safari).
- **Rem breakpoint.** The phone font-size rule now ends at 639.98px. At exactly 640px wide both the phone and tablet rules used to apply, which broke the layout at that one width.
- **Work visuals are diagrams, not photos.** The hover distortion passes through as a ripple and settles so labels stay readable. On touch devices, where hover does not exist, each diagram takes its colour once it scrolls into view.
- **Card anchors.** Skills links scroll to a card with an offset for the fixed nav. Lenis 1.3.19 ignores CSS `scroll-margin-top`, so the script reads that value and passes it as Lenis's `offset`.
- **Contact email size.** The Gmail address is longer than the old one, so it is set smaller on phones and tablets to stay on one line.
- **Smaller fixes:** the scroll cue shows only above 1024px; card metadata stacks under the title on phones; all content is visible with JavaScript off; the preloader waits for fonts.

## Checked on 13 Nov 2026

Rendered in headless Chrome at 16 sizes: 320, 360, 375, 390, 412 and 430 wide phones; 640, 641, 768, 820 and 1024 wide tablets; 1180, 1280, 1366, 1440 and 1920 wide desktops. No horizontal scroll, no overlap between the hero's top row and the name, and the email on one line at every size. `site/` contains none of the internal product names, no phone number, none of the dropped figures and no trace of the old domain.

## Open items

1. Portrait cut-out from Het (he will send it).
2. Real recommendations from Het (he is collecting LinkedIn ones), then build the Voices section.
3. **Before launch, remind Het of research brief §7 items 1 and 2.** They matter more now that the page names his current employer next to "available part-time for contract work", and names Crest Data's customers.
4. Het to say whether the Anthropic certifications line should come back.
5. Het to say whether any internal product name may be used.
6. What "98.5% success" means on the LLM pipeline card, if Het can define it (brief §4).
7. Domain connected and launch extras added (14 Nov 2026): Always Use HTTPS on, workers.dev and preview URLs off, `wrangler.jsonc` pins `./site`, canonical URL, Open Graph and Twitter tags, `assets/og-image.png` (source `tools/og-image.html`), `robots.txt`, `sitemap.xml`. Still open: Cloudflare Web Analytics was turned on with automatic setup, but its beacon wasn't in the page on 14 Nov. Check the Web Analytics dashboard for visits; if none show, paste its JS snippet at the analytics comment at the end of `index.html`. Bump `<lastmod>` in `sitemap.xml` when the page changes meaningfully.
8. Het's GitHub profile is thin for a link on this page: no bio, and the newest repo's README has placeholder demo links. Worth tidying before launch, or drop the link.
9. The four local SVGs each carry a content-credentials block in `<metadata>` saying Claude provided the file. It is harmless and visible only in the file source. Running `tools/gen_art.py` again writes files without it.
10. Optional: link the profile PDF from the site. It would need a copy inside `site/`.
11. Later: case-study pages with before and after numbers (research brief §4).
12. Het to say whether the profile PDF should drop the availability line too, and whether the employer names should also come off the Experience rows, the Work cards and the PDF. Those rows need something in their place, so ask before changing them.
