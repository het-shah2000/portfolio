# Het Shah portfolio site

## What this site is

This is the personal portfolio of Het Shah, a backend and AI systems engineer based in Ahmedabad with about five years of experience. Het uses it for **freelancing**. He shares the link with people who represent him to clients; they pass it on, and the client's technical lead may check it.

It is **about Het, not a sales page**. It shows his skills, what he has built and the client projects he has worked on. It has **no services list, no prices, no engagement models and no "book a call" funnel** (Het, 13 Nov 2026).

Two readers: the **intermediary**, who skims, is often not technical and decides in 30 seconds, and the **client's engineer**, who reads the detail and checks the claims. Each section's first line must work for the first reader and the detail for the second.

## Where things stand (13 Nov 2026)

- `site/index.html` was restructured on 13 Nov 2026 to match `docs/content-plan.md`: Hero, About, Experience, Work (four cards with client and role), Impact, Skills, Contact. Employers and clients are named (hard rule 1). Later that evening Het had the availability line taken off the hero and the contact block "for now", and the employer names taken out of the About intro (see the build notes).
- A one-page profile PDF exists in `profile/`.
- **Still to come:** the portrait (one tried on 14 Nov 2026 and rejected by Het; see the build notes), the Voices section (waits on Het's LinkedIn recommendations), and launch on hetshahbuilds.in. The build notes list every open item.

## Read order

1. **`docs/content-plan.md`**: the structure section by section (built on 13 Nov 2026), the copy rules, the names Het has cleared, the figures allowed, and the status of each input. Start here for any content work.
2. `docs/site-build-notes.md`: what exists now, departures from the template, decisions in force, open items.
3. `docs/portfolio-study.md`: the evidence, about 30 comparable portfolios and what to borrow or avoid.
4. `docs/portfolio-research-brief.md`: the original research from 12 Nov. §4 (numbers audit), §6 (domain and hosting) and §7 (risks) still apply. Its services, "how I work" engagement and pricing advice does not.

## Files

- `site/index.html`: the whole page (markup, CSS and JS). Static, no build step; `site/` deploys as it is.
- `site/assets/`: the four SVG work-card diagrams and `og-image.png` (the social preview card). `portrait.webp` goes here once Het approves a portrait.
- `site/robots.txt` and `site/sitemap.xml`: bump `<lastmod>` in the sitemap after meaningful content changes.
- `tools/og-image.html`: source for `og-image.png`; the rebuild command is in its top comment.
- `wrangler.jsonc`: tells Cloudflare to deploy only `./site`. Keep it that way.
- `tools/gen_art.py`: regenerates the diagrams with `python3 -I tools/gen_art.py <anton.woff> site/assets`. It needs fontTools and an Anton `.woff` file, which isn't in this folder. Labels become outlines, so edit text in the script, not in the SVGs.
- `profile/profile.html` and `profile/Het_Shah_Profile.pdf`: the one-page profile the intermediaries can forward. Edit the HTML, then rebuild the PDF with the Chrome command in the comment at the top of that file, and check it still fits one A4 page. It follows the same hard rules as the site. It is not in `site/`, so it isn't deployed.
- `docs/`, `Het_Shah_Resume.pdf` and `Het_Shah_Resume.tex`: private working material. Never deploy them. The résumé is the source for experience, projects, skills and figures. Use only the names that hard rule 1 clears.
- A private preview artifact titled "Het Shah | Backend and AI systems engineer" exists. Find it with the Artifact tool's list action and republish to the same URL after changes.

## Hard rules

1. **Name only the companies Het has cleared; no internal product names.** On 13 Nov 2026 Het cleared six names for the site: the employers Infocusp Innovations, Crest Data and LearnElectronics, and the clients Armis, Comcast and Splunk. Present a client as Crest Data's customer ("Armis, through Crest Data") and never imply it was Het's own freelance client. One exception, in Het's own wording: the About intro names Armis, Comcast and Splunk without "through Crest Data" and without naming either employer. Internal product and platform names from the résumé (the LLM pipeline's product name, the Comcast platform's name, the Splunk app and content-pack names, the scan service's name) stay off the site and the profile PDF until Het clears them too. Before any deploy, grep `site/` for those product names.
2. **No invented testimonials, quotes or recommendations.** Voices stays out until Het supplies real ones; then use his exact wording and only the attribution he approves.
3. **No invented, estimated or converted numbers.** Use only the résumé figures that brief §4 keeps (the list is in the content plan), one unit per measure.
4. **No services, prices, rates or engagement terms** on the site.
5. **Analytics must be visible to Het only**: privacy-friendly, nothing shown to visitors. None is added yet. The placeholder comment is at the end of `index.html`.
6. **Deploy only `site/`.** Never deploy the résumé PDF (it has company names and a phone number), `docs/`, `tools/` or this file. If the host deploys from a Git repo, the repo must be private or contain only `site/`. No phone number on the site.

## Conventions

- Plain HTML, CSS and JS in one file. No frameworks, no build step.
- Pin external scripts to exact versions (Lenis 1.3.19 from jsDelivr). Fonts are Anton and Onest from Google Fonts.
- Build new sections (Experience, Skills) from the template's existing styles; don't add a new visual language.
- All content stays visible with JavaScript off. Honour reduced motion.
- Check every change at phone, tablet and desktop widths. The hero name sizing rules are in the build notes.
- When a decision is made or an item is done, update `docs/site-build-notes.md`: decisions, open items, the "Last updated" date. If a rule changes, update this file too.

## Inputs pending from Het

Track their status in the build notes' open items, not here. The content plan lists what each one unblocks.

- **Portrait:** still open. Het rejected the IMG_1992 cut-out on 14 Nov 2026 ("it doesn't look good"); don't reuse it. Next time, show Het the result before wiring it in. To use one, save a transparent cut-out as `site/assets/portrait.webp`, uncomment the portrait block in the hero, add class `has-portrait` to `<section class="hero">`, keep the head near the top of the image, and recheck the hero at phone, tablet and desktop sizes. Headless Chrome won't lay out narrower than about 500px, so check phones inside an iframe of the phone's width.
- **Real recommendations:** Het is collecting LinkedIn recommendations. Then build Voices.
- **Anthropic certifications:** Het answered "keep the AWS Solutions Architect name" and didn't mention these, so the line was removed. Put it back only if he asks.
- **Internal product names:** left out. Ask before using any.
- **What "98.5% success" means** on the LLM pipeline card (brief §4), if Het can say.

Answered on 13 Nov 2026 and done: the availability line (approved, then taken off the page again that evening), the employer and client names, the GitHub link (github.com/het-shah2000; none of its three repos went on the page), the AWS certification, the weekly chart reading, the contact email and the domain, and the profile PDF.

## Hosting and launch

- Host on **Cloudflare Workers with static assets** (free, commercial use allowed), deployed from the private repo github.com/het-shah2000/portfolio; live at hetshahbuilds.hetshah2000.workers.dev since 13 Nov 2026. Cloudflare labels Pages "legacy", so don't move to it. Only `site/` may be served. Don't use Vercel Hobby: the site promotes Het for paid work, which Vercel counts as commercial.
- Deploys happen automatically on every push to `main` of the private GitHub repo. Canonical URL, Open Graph image and sitemap were added on 14 Nov 2026; Cloudflare Web Analytics is on (see the build notes for its open check).
- **Before launch, remind Het of brief §7 items 1 and 2.** Item 1: his current employment contract's outside-work clause; he needs written consent before freelancing publicly. Item 2: client confidentiality.

## Domain and email

- The domain is **hetshahbuilds.in**. Het bought it at one.com (confirmed 13 Nov 2026). Its DNS is on Cloudflare and it serves the site since 14 Nov 2026; `www` redirects to it through a Cloudflare Redirect Rule, not a Worker custom domain.
- The contact email on the site and the profile PDF is **hetshah2000@gmail.com**, as Het asked. There is no address on the domain.
