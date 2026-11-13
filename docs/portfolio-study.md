# Portfolio study: sites comparable to yours

Studied 13 Nov 2026. Question: why does the site read as a system-design showcase rather than a portfolio, and what should change? The answer is turned into a plan in `docs/content-plan.md`. This file keeps the evidence.

**Purpose, as you confirmed on 13 Nov 2026:** a profile of you for freelancing. It is shared through people who represent you to clients. It shows skills, things you have built and client projects. It has no services or prices.

## What was studied

- **emmabostian/developer-portfolios:** 2,113 entries. I filtered them by role tag to 167 backend, cloud, distributed-systems, AI and freelance portfolios. I rendered all 167 in headless Chrome, scored each for backend, AI, cloud, client-facing, seniority and outcome language, and read the 21 closest matches section by section.
- **11 independent consultants** outside the list. Two were templates with placeholder content, including invented testimonials, and were dropped.

## Finding 1: the site has the right content but the wrong frame

The strongest senior profiles follow one order: who I am, proof at a glance, experience, selected work, how I work, skills backed by that work, contact. The current site runs Principles, Work, Numbers, then a freelance pitch. It never introduces you as a person, never shows a career line, has no skills section, and the only line about what you do for clients is a services pitch in the footer. So it reads as system design.

The content itself is right: the system cards are strong case studies, and the principles show engineering judgement. What's missing is the frame around them: About, Experience, Skills, and a contact block that doesn't sell.

## Sites worth borrowing from

For each, take the content structure, not the visual theme.

| Site | Who | Borrow |
|---|---|---|
| naman-kumar2397.github.io | Lead SRE, 7+ years | "Impact at a glance" near the top, each figure with one line of context. A career table. Three case studies. "Core capabilities. In priority order, each backed by work described above." This is the model for the Skills section. |
| ayushdoesdev.in | Lead backend engineer | Hero "Engineering reliable backends. Building useful AI systems." "Roles and outcomes": one entry per role, "Metrics are from the work described in each role." |
| faizimam.in | Senior backend developer | "Impact, measured": before and after figures from production systems |
| negiadventures.github.io | AI systems and backend engineer | Hero "Agents that ship. Backends that hold." with a one-line specialty |
| marcuss.pro | Staff backend engineer | A small status block in the hero: role, location, availability |
| swarnava.dev | Lead AI architect | Clients described by industry ("Banking, healthcare, energy, retail"); a short availability block ("Based in India · Remote & hybrid friendly · Response time Within 12 hours") |
| brittanychiang.com | Senior frontend engineer | Restraint: About, Experience, Projects, Writing, nothing else |
| tanayshah.dev | AI infrastructure engineer | Writing as "decision records, not tutorials", if you add writing later |

## Finding 2: anonymity is normal; say it once

Senior engineers who can't name clients say so plainly, and it reads as discretion:

- Naman Kumar: "Client-specific details are intentionally left out."
- Tanay Shah labels his deep dives "NDA-safe" and strips dates from a chart "for confidentiality".
- Ayush Srivastava labels his demos "portfolio simulations ... not employer deliverables".

For you: describe each employer and client by industry (descriptors in the content plan). Optionally add one quiet line, such as "Client names are withheld; details on request." Every employer in the sample is named, so withholding names costs a little credibility. Saying why openly recovers most of it.

## Finding 3: what not to copy

- **Services, pricing and engagement models.** Several freelance sites lead with these; you have decided against them.
- **Terminal, OS and metro-map themes** (marcuss.pro, ashlesh.co.in, faizimam.in, tanayshah.dev's § numbering). An intermediary skimming on a phone has to work past them.
- **Student-level sections:** GPA, LeetCode, coursework, 25-tool skill grids with proficiency bars, walls of entry-level certificates.
- **Phone numbers on the page.** Four sites in the sample do this; the hard rules forbid it.
- **"Ask me" résumé chatbots** (marcuss.pro). Cost and abuse risk.
- **Mixed audiences** ("open to full-time, contract, freelancing"). Keep it to freelance work.
