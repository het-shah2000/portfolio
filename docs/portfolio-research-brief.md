# Portfolio website research brief — hetshahbuilds.in

> **Names:** on 13 Nov 2026 Het cleared the three employer names and Armis, Comcast and Splunk for the site, always as Crest Data's customers. §7 items 1 and 2 are still his to check before launch.
>
> **Read this with the 13 Nov 2026 update.** The site is a profile of Het for freelancing, shared through people who represent him to clients. It is not a sales page. That means §3's services, "how I work" engagement types, hours per week and booking link no longer apply, and neither does the pricing talk elsewhere. Still in force: §4 (numbers audit), §5 (design), §6 (domain and hosting: Cloudflare Pages, not Vercel Hobby) and §7 (risks). The current plan is in `docs/content-plan.md`.

Researched 12 Nov 2026. Purpose of the site: show skills and projects to prospective freelance clients.

## 1. Bottom line

1. **Content model:** one page (hero, services, three case studies, how I work, about, proof, contact) plus one page per case study and `/resume`. Three deep case studies beat a long project list.
2. **Your resume numbers are volume numbers, not outcome numbers.** Keep 13 of the 16 figures, drop 3, put only 3 in the hero, and attach each one to the decision that produced it. Details in section 4.
3. **Vercel's free plan does not cover a site that advertises your services.** Use Cloudflare Pages (free) or pay for Vercel Pro (about $20/month). Section 6.
4. **A .in domain needs NIXI e-KYC within 7 days of registration.** Confirm one.com handles it before you buy. Its .in price is $1.99 for year one, then $17.99/year.
5. **Three checks before anything goes public:** your Infocusp contract's outside-work clause, whether you may name Armis/Comcast/Splunk and publish their production metrics, and where your verifiable proof will come from (everything on the resume is employer work a client cannot inspect).

## 2. Reference sites and what to take from each

| Site | Who | Borrow | Skip |
|---|---|---|---|
| brittanychiang.com | Frontend engineer | Single column, four sections (About, Experience, Projects, Writing), one-line positioning, heavy restraint | Nothing to skip; it has no services or contact pitch because it is not a freelance site |
| theburningmonk.com/hire-me | Independent AWS consultant | Headline written as the client's pain, named testimonials, a "why you shouldn't hire me" filter, one clear ask at the end | Courses and workshops |
| vincentschmalbach.com | Freelance developer | Plain, text-led pages; short proof points; engagement models spelled out (fixed price, flat rate, hourly, retainer); the same two CTAs repeated | Blog and book cross-promotion |
| hamel.dev | AI engineer | Dated technical writing as the credibility engine; no service list needed once the writing exists | Course banner |
| nex.is-a.dev, brandon-ogola-platform.vercel.app/services | Backend freelancers | Availability block (status, response time, timezone) and a "how I work" block (typical engagement length, scope agreed upfront) | Generic skill grids |
| jaydarji.in (your friend, reference only) | Tech lead | Outcome stats in the hero, one architecture diagram per system, a skills-to-systems proof matrix instead of self-rated skill bars, testimonials | Tap-to-reveal on almost every section, the dual "personal side" mode, the CV chatbot for v1 |

Patterns that repeat across the "what wins clients" guidance:

- 3 to 5 case studies, each told as problem, decision, outcome. Screenshots or tool lists alone do not count.
- For architecture work, each case study carries: context, the hard part, the approach in plain language, one simple diagram, the tradeoff you rejected, the result.
- When a client cannot be named: describe them by industry, size and region; use ratios instead of raw figures; keep proof available on request.
- An honest qualitative result beats an invented number.

## 3. Recommended structure

**Home (single scroll)**

1. **Hero.** One positioning line, one sentence on who it is for, two CTAs (See the work / Start a conversation), a 3-stat strip, a trust row (certifications, companies if cleared). Example line: "I build production LLM pipelines and event-driven AWS backends for B2B SaaS teams."
2. **What I can do for you.** Three offers in client language:
   - LLM pipelines that survive production: multi-agent stages, evals, tracing, cost control
   - Event-driven AWS backends for multi-tenant SaaS
   - Security and data ingestion pipelines: scanner integration, normalisation, high-volume ingest
3. **Selected work.** Three cards linking to case study pages.
4. **How I work.** Engagement types, hours per week you can give alongside a full-time job, IST working window, reply time.
5. **About.** Four or five lines, short experience timeline, certifications (AWS Solutions Architect Associate with the Credly link; your Anthropic certifications are not on the resume and belong here given the AI positioning).
6. **Proof.** Testimonials (LinkedIn recommendations or ex-managers), public repo or write-ups.
7. **Contact.** Email on your domain plus a form or booking link. No phone number.

**Case study pages (3)**

1. Multi-tenant AppSec platform (Armis work)
2. Multi-agent LLM pipeline for vulnerability detection and fixes (MooseAI)
3. Security event ingestion pipeline (Databee)

Splunk work becomes one line in the experience timeline. The SQS to Kafka migration is your best story; give it its own section inside case study 1.

**`/resume`** serves the PDF, which gives you one stable link to hand out. Use a web copy without the phone number.

## 4. Resume numbers audit

The resume has 16 figures. Three problems show up when they move to a website.

**Problem 1: almost all are volume, almost none are outcomes.** Tenants, findings per day and calls per day say how much the system handled. A client is buying what changed: cost, speed, incidents. Your friend's hero leads with a cost cut; yours would lead with throughput. The one real outcome on the resume, the Kafka migration ending burst throttling, has no number attached.

**Problem 2: per-day figures shrink when a technical reader converts them.**

| Figure | Per second |
|---|---|
| 250K findings/day | about 2.9 |
| 1.5M findings/day (peak) | about 17 |
| 212K LLM calls/day | about 2.5 |
| 2k events/min | about 33 |

Do not pitch these as raw scale. What is hard here is the 6x weekly burst (250K to 1.5M), tenant isolation across 32 customers, and heavy work per item. Say that.

**Problem 3: mixed units hide your largest number.** 2k events/min is about 2.88M events/day if sustained, which is larger than the 1.5M "peak" you headline. Use one unit across the site.

| Resume figure | Verdict | How to use it |
|---|---|---|
| ~5 years | Keep | About section, not a hero stat |
| 32 enterprise tenants | Keep, hero | Strongest trust number |
| 250K+ findings/day | Keep, reframe | Pair with the peak as "6x weekly burst" |
| 1.5M+ at peak | Keep, hero | The reason autoscaling and Kafka exist |
| 12 scanners | Keep | Case study 1 |
| 4M live cache keys | Keep | Case study 1, minor |
| 81% hit rate, 95%+ in full scans | Keep if you add the effect | Say what it took off the datastore (reads or latency) |
| 5-stage pipeline | Keep | It is the diagram for case study 2 |
| 212K LLM calls/day | Keep, hero | Pair with the next two |
| 98.5% success | Keep, define it | State what "success" means and what happens to the roughly 3,180 calls a day that fail |
| 85% of prompt tokens from cache | Keep, hero for AI clients | Convert to money saved if you can |
| 2k events/min | Reframe | About 2.88M/day if sustained |
| 20% query performance | Drop | No baseline, oldest work |
| 30% less observability downtime | Drop | No baseline, unclear term |
| GPA 8.05 | Drop | Clients do not ask |
| AWS cert, May 2026 | Keep | Trust row |

**Numbers worth digging up** (only you have them; do not estimate):

- Kafka migration: throttling incidents or ingest lag before and after
- Cache: datastore read load or p95 latency before and after
- Prompt caching: LLM spend per finding or per month before and after
- Scanner engine: time to onboard a new scanner
- MooseAI: share of findings removed by reachability validation, or fix acceptance rate

Suggested hero strip: **32 enterprise tenants · 6x weekly burst absorbed (250K to 1.5M findings/day) · 212K LLM calls/day with 85% of prompt tokens cached.**

## 5. Design direction

- You have no UI to screenshot. The architecture diagram is your visual: one clean diagram per case study.
- Typography-led, one accent colour, generous spacing. Pick your own palette; the realtimecolors link in your notes is your friend's.
- Animation budget of two or three moments (hero entrance, diagram flow, stat count-up). Content must be visible without JavaScript and must honour reduced-motion settings. When I scrolled jaydarji.in in an automated browser, two full screens rendered empty until animations fired. That may be an artefact of the tool, but it shows the risk of gating content on scroll animation.
- Keep proof visible by default. Tap-to-reveal hides it from someone skimming on a phone.
- Design for mobile first; most outreach links are opened from LinkedIn, WhatsApp or email.
- Target Lighthouse 90+ on mobile.

**Libraries from your friend's list** (all assume React/Next.js, Tailwind and mostly the shadcn CLI). Pick one:

| Library | Finding |
|---|---|
| Vengeance UI | Open source, installs through the shadcn CLI. Safest choice. |
| Skiper UI | 24+ free components; premium tier is a $129 one-time payment |
| Motion Primitives | Could not be read; the site blocks automated fetches |
| Animmaster Lib | Paid ($4.99 to $8), sold with WhatsApp/Telegram contact. Verify the seller before paying. |

AI-generated hero images or video add page weight and read as decoration on a backend engineer's site. Real diagrams do more.

## 6. Domain and hosting

**Domain (one.com)**

- one.com lists .in at $1.99 for the first year and $17.99/year on renewal. Three years: about $38. For comparison, Domain India lists ₹575 then ₹625/year before GST: about ₹2,150 over three years including GST.
- NIXI requires KYC/e-KYC for every .in within 7 days of registration, and the registrant details must match your ID. At least one European registrar has said it cannot support the e-KYC step. one.com is European, so ask their support how they handle .in e-KYC before paying. A NIXI-accredited Indian registrar removes the question.
- WHOIS privacy is not offered on .in.
- Buy "domain only"; one.com will push a hosting bundle you do not need.

**Hosting**

| Option | Cost | Note |
|---|---|---|
| Cloudflare Pages + Cloudflare DNS | Free | Commercial use allowed, unlimited bandwidth, 500 builds/month. Needs your nameservers pointed at Cloudflare. Free email forwarding comes with it. Build as a static export. |
| Vercel Pro | About $20/month | Compliant, least friction with Next.js |
| Vercel Hobby | Free | Restricted to non-commercial personal use. Vercel's definition includes advertising a service, and Vercel staff told a self-employed user that a static site promoting their services is commercial. Many portfolios run on Hobby anyway; the risk is a paused site. |

Given "cheapest and easiest", Cloudflare Pages fits. Switching hosts later is a DNS change.

**If you do use Vercel with one.com DNS**

- one.com control panel, Advanced settings, DNS settings, DNS records
- A record on `@` with the value on your Vercel domain card (general-purpose value 76.76.21.21)
- CNAME on `www` with the project-specific target from the same card
- Delete one.com's default A records on `@` and `www` first; a leftover record is the usual cause of a domain that never verifies

**Email:** (13 Nov 2026: Het chose his Gmail address for the site, so this is optional.) An address on the domain, such as hello@hetshahbuilds.in, via free forwarding (Cloudflare Email Routing if DNS is on Cloudflare). Forwarding is receive-only; replying from the address needs an SMTP relay or a paid mailbox.

## 7. Factors not in the original plan

Ordered by how much damage they can do.

1. **Employment contract.** Indian IT contracts commonly restrict outside work, in-employment exclusivity clauses are generally enforceable, and courts have mostly upheld terminations for undisclosed dual employment. A public "hire me" site under your name is visible to Infocusp. Read the clause and get written consent first. (Not legal advice.)
2. **Client confidentiality.** Armis, Comcast and Splunk were Crest Data's customers. A public commercial site is more exposed than a resume sent privately. Check your Crest confidentiality terms; if unsure, anonymise ("a US asset-security company") and use ratios. Never imply they were your freelance clients. Your current engagement is already anonymised on the resume; keep it that way.
3. **Verifiable proof.** Nothing on the resume can be inspected by a stranger. Add at least two of: LinkedIn recommendations as testimonials, one public repo (for example a small multi-provider LLM abstraction with retries and tracing), one technical write-up (the SQS to Kafka decision is the obvious one).
4. **Positioning and capacity.** The resume summary is a generalist one. The site needs a niche line and an honest statement of availability.
5. **Contact path.** Form or booking link, email on the domain, no phone number.
6. **Link previews and SEO.** Open Graph image and title (your links will be pasted into LinkedIn and WhatsApp), Person schema, sitemap, the domain added to your LinkedIn and GitHub profiles.
7. **Analytics.** One privacy-friendly counter so you know whether outreach links get opened.
8. **Before the first invoice.** A simple contract template that includes permission to describe the work anonymously, and a decision on how you will invoice and receive foreign payments.
9. **CV chatbot.** Costs money per message and is an abuse surface. Version 2 at the earliest, with rate limits.

## 8. Open items

- LinkedIn could not be read: it showed a sign-in wall to both the web fetch and Claude's browser. Sign in to LinkedIn in the Claude browser pane, or save the profile as a PDF into the Portfolio folder, and the headline, About text and recommendations can be checked against the site copy.
- Before/after numbers listed in section 4.
- Answers on the Infocusp clause and on naming Crest's customers.

## Sources

- [Vercel Fair Use Guidelines](https://vercel.com/docs/limits/fair-use-guidelines)
- [Vercel community: Fair Use of the Hobby Plan (staff answer)](https://community.vercel.com/t/fair-use-of-the-hobby-plan/2725)
- [Vercel community: can a freelance portfolio use Hobby (unanswered)](https://community.vercel.com/t/can-a-personal-screenwriter-portfolio-use-the-hobby-plan/50298)
- [Vercel: using a domain with A records](https://vercel.com/kb/guide/use-domain-vercel-a-records)
- [Cloudflare Pages vs Vercel vs Netlify, April 2026](https://hostfleet.pages.dev/cf-pages-vs-vercel-vs-netlify-2026/)
- [Vercel pricing explainer](https://www.supadrop.host/blog/vercel-pricing-free-tier-limits/)
- [one.com domain prices](https://www.one.com/en/domain/prices)
- [one.com: create a CNAME record](https://help.one.com/hc/en-us/articles/360000803517)
- [Netlify forum: one.com default www record](https://answers.netlify.com/t/a-record-and-need-ip-address/108476)
- [Domain India registration fees](https://domainindia.com/support/kb/domain-registration-fees)
- [GoDaddy: about .in domains (KYC, privacy)](https://www.godaddy.com/en/help/about-in-domains-5835)
- [Realtime Register: .in policy update](https://realtimeregister.com/blog/in-domain-policy-update-realtime-register-signs-new-raa-with-operational-limitations)
- [Cloudflare Email Routing guide](https://mecanik.dev/en/posts/cloudflare-email-routing-free-custom-domain-email/)
- [How to build a technical architecture portfolio for freelance clients](https://giguphq.com/blog/how-to-build-a-technical-architecture-portfolio-for-freelance-clients)
- [Freelance case studies when you can't name the client](https://www.9am.works/freelancer-academy/blog/freelance-case-studies-portfolio-that-wins-projects)
- [Moonlighting: legal considerations (Cyril Amarchand Mangaldas summary)](https://echai.ventures/startingup/r/moonlighting-legal-considerations-and-contractual-regulation--i1-r024)
- [Moonlighting in India overview](https://www.pockethrms.com/?p=84983)
- [brittanychiang.com](https://brittanychiang.com/) · [theburningmonk.com/hire-me](https://theburningmonk.com/hire-me/) · [vincentschmalbach.com](https://www.vincentschmalbach.com/portfolio/) · [hamel.dev](https://hamel.dev/) · [jaydarji.in](https://www.jaydarji.in/)
- [Skiper UI](https://skiper-ui.com/) · [Vengeance UI](https://www.vengenceui.com/) · [Animmaster Lib](https://animmasterlib.dev/)
