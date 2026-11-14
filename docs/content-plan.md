# Content plan: the site as a profile

Written 13 Nov 2026. **Built the same evening:** `site/index.html` now follows this plan, with Het's answers of 13 Nov applied. Those answers changed three things in the plan, marked "13 Nov" below: employers and clients are named, the availability line says part-time, and the contact email is Het's Gmail address. Voices and the portrait are the parts still waiting.

## Purpose and readers

Het uses the site for **freelancing**, but it is **a profile of Het, not a sales page**. Het shares the link with people who represent him to clients. They pass it on, and the client's technical lead may then check it.

- **Shows:** Het's skills, what he has built, and the client projects he has worked on.
- **Leaves out:** services lists, prices, rates, engagement models, packages, "book a call" funnels and sales language. (Het's decision.)

There are two readers. Write every section so its **first line works for reader 1** and **the detail works for reader 2**.

1. **The intermediary.** They skim, are often not technical, and decide in about 30 seconds whether to forward the link. They need to know who Het is, what he is good at and what he has built, in plain words.
2. **The client's engineer.** They read the project detail and check the claims. They need scale, architecture, Het's own role and the stack.

## Tone

- First person, plain and specific. Describe what Het built and what changed, not adjectives about Het.
- About Het's work, never about what a client could buy.
- Each project names Het's own role ("I designed...", "I led the migration..."), not the team's.
- Visible to a reader skimming on a phone. No tap-to-reveal for anything that counts as proof.

## Target section order

| # | Section (nav label) | Status | Job |
|---|---|---|---|
| 1 | Hero | Done | Name, role words, positioning line, availability line |
| 2 | Marquee | Done | The stack from the résumé in two rows (14 Nov 2026; was the five principles) |
| 2b | Impact | Done | Moved up under the marquee on 14 Nov 2026: the four figures with captions linking to their projects |
| 3 | About | Done | Who Het is, how he builds (the four principles stay) |
| 4 | Experience | Done | Short timeline: years, title, employer, what he owned |
| 5 | Work (client projects) | Done | Each card adds the client and Het's role |
| 7 | Skills | Done | Skills grouped by area, each group linked to the project that used it |
| 8 | Voices | Waiting on Het | Only real recommendations from Het |
| 9 | Contact | Done | Availability, email, LinkedIn and GitHub. No pitch. |

New nav: About · Experience · Work · Skills · Contact. Update both the desktop nav and the mobile menu.

## Section by section

### 1. Hero (`<section class="hero">`)
- Keep the role words (Backend / Cloud / AI Systems) and the giant name.
- Keep the positioning line. It is already about Het: "I build LLM pipelines and event-driven backends that hold up when the load arrives all at once. Five years on multi-tenant platforms for enterprise security and data products."
- Availability line, approved by Het on 13 Nov with "part-time" added: **"Available part-time for contract work · Ahmedabad, IST · Remote"**. Don't mention the current full-time role in the hero (see §7 of the brief). **Update, 13 Nov evening:** Het took this line off the hero and the contact block "for now". The hero keeps "Ahmedabad, IST · Remote".
- Portrait when Het approves one (one was tried and rejected on 14 Nov 2026; see the build notes).

### 3. About (now `<section id="approach">`)
- Retitle it "About" and change the anchor to `#about`.
- Rewrite the lead paragraph so it introduces Het as a person before the method: who he is, about five years, where, what he works on now. Keep the existing method sentences after that; they are good.
- Keep the credentials line: AWS Solutions Architect Associate, linked to the Credly badge. 13 Nov: Het kept the AWS name and didn't mention the Anthropic certifications, so that line is out unless he asks for it back.
- Keep the four numbered principles as a "How I build" sub-block. They show engineering judgement, which the technical reader looks for.
- Education is one short line here: B.Tech in Information Technology, Dharmsinh Desai University, 2018 to 2022. No GPA.

### 4. Experience (new, after About)
A compact timeline, three rows at most. Use template styles that already exist; don't invent a new visual language. Source: the résumé's Work Experience. 13 Nov: employers are named.

| Years | Title | Employer | What to say |
|---|---|---|---|
| Oct 2026 to now | Software Engineer 2 | Infocusp Innovations | Team work on a client's AI agent evaluation pipeline: how agent behaviour can be measured and validated reliably |
| Dec 2021 to Oct 2026 | Senior Software Engineer | Crest Data | Architected and delivered AI and application-security platforms for enterprise clients, end to end; mentored junior engineers on system design, code review and pre-commit tooling. Points to the Work cards. |
| May to Jul 2021 | Website Developer Intern | LearnElectronics | Quizzes and event registration portals in FastAPI. Kept: three rows don't look crowded. |

### 5. Work (`<section id="work">`), four cards
Keep the diagrams and the hover behaviour. Add to each card a **client line** and a **role line**. 13 Nov: the client line names the client as Crest Data's customer, for example "Armis, through Crest Data", and a line under the section heading says all four projects come from Het's time at Crest Data. Each card also carries detail bullets and a stack line drawn from the facts column. Give each card an id (`#work-01` to `#work-04`) so Skills can link to it. Card 4 stays, because the site now shows breadth across client projects. That settles the earlier keep-or-remove question unless Het says otherwise.

| Card | Client | Het's role | Facts allowed (all from the résumé) |
|---|---|---|---|
| 01 Multi-tenant AppSec platform | Armis | Backend architect; led the ingest migration | 32 enterprise tenants; 250K findings a day on average, 1.5M+ at the weekly full-scan peak; event-driven microservices (FastAPI, Lambda → SQS → ECS Fargate) with autoscaling and dead-letter alerting; engine running 12 SAST/DAST scanners with unified normalisation and SBOM/VEX; on-demand scan ingest API (S3 uploads, SQS-driven ECS); container scanning across three registries; JWT and Basic auth with rate limiting and tenant isolation; Valkey cache with 4M live keys and an 81% average hit rate (95%+ during full scans); SQS to Kafka migration that ended burst throttling |
| 02 Five-stage LLM fix pipeline | Armis | Built the provider abstraction and the tracing | 5 stages (AST scanning with tree-sitter, cross-scanner dedup, reachability validation with Joern, agentic fix proposal, fix validation); 212K LLM calls a day; 98.5% success; 85% of prompt tokens served from cache; two providers (Cerebras, AWS Bedrock) behind one abstraction with per-stage models and structured output with retries; every call traced in Langfuse. Brief §4: say what "success" means if Het can. |
| 03 Security event ingestion | Comcast | Built the ingestion frameworks and pipelines | API ingestion frameworks; new security data sources; pipelines in Benthos and Bloblang normalising and routing about 2,000 events a minute; external scanner integrations with retries |
| 04 Observability tooling | Splunk | Built the APIs, dashboards and alerting | Django REST APIs and React dashboards; a licence upgrade mechanism; reusable content modules; proactive SLA monitoring and alerting. Leave out the 20% and 30% figures (brief §4: no baseline). |

The pipeline's internal product name appears in the résumé's scanner list. Leave it out everywhere. The same goes for the other internal product and platform names in the résumé (the Comcast platform, the Splunk app and content packs, the scan service): Het cleared company names on 13 Nov, not these.

### 6. Impact (`<section id="impact">`)
Keep the four figures (32 / 1.5M / 212K / 85%). Since 14 Nov 2026 the section sits right after the marquee, is headed "Numbers you can check.", and each figure has a one-line caption built only from kept figures and résumé facts, with a link to its project.

### 7. Skills (new, after Impact)
Grouped lists, no proficiency bars, no logo walls. Each group ends with a link to the card that proves it. Source: the résumé's Technical Skills, minus anything that identifies a client.

| Group | Items | Proof |
|---|---|---|
| Backend and APIs | Python, FastAPI, Django, Pydantic, REST, JWT auth, rate limiting | 01, 04 |
| Distributed and event-driven | Kafka, SQS/SNS, EventBridge, multi-tenant SaaS, dead-letter queues, caching (Valkey/Redis) | 01, 03 |
| AWS | ECS Fargate, Lambda, SQS, S3, ECR, ALB, EventBridge, Secrets Manager, CloudWatch, VPC, IAM; Terraform | 01 |
| AI and LLM systems | Multi-agent pipelines, AWS Bedrock, Cerebras, structured output, prompt caching, RAG, Langfuse tracing, MCP | 02 |
| Data pipelines | Benthos, Bloblang, API ingestion, normalisation and routing | 03 |
| Application security tooling | SAST/DAST, Trivy, Gitleaks, Checkov, OpenGrep, Semgrep, Grype, SBOM/VEX, tree-sitter, Joern | 01, 02 |
| Databases | DocumentDB (MongoDB), DynamoDB, Valkey (Redis) | 01, 04 |
| Observability | CloudWatch, Prometheus, Grafana, Splunk (13 Nov: now allowed) | 01, 04 |
| Delivery and testing | Docker, GitHub Actions, GitLab CI/CD, pre-commit, Pytest, integration and end-to-end suites in containers | all |

**Names to leave out of Skills:** the Splunk app and content-pack names. Splunk itself is listed since 13 Nov. JavaScript, React, Bash, C and C++ sit in a minor "Also" line.

### 9. Contact (`<footer id="contact">`)
- Remove the services sentence ("Fixed-scope builds, architecture reviews, and cost and reliability audits ... one engagement at a time").
- Change the heading so it isn't a pitch. "Let's Build / Have a system that can't go down?" sells. Built as: kicker "Contact", heading "Get in touch.", one line repeating the availability line, then the email and the LinkedIn and GitHub links.
- 13 Nov: the email is hetshah2000@gmail.com and GitHub is github.com/het-shah2000.
- No phone number.

### Also check
- `<title>`, meta description, Open Graph tags and the JSON-LD `Person` block: none should pitch services. `jobTitle` "Backend and AI systems engineer" is fine.
- The private preview artifact "Het Shah | Backend and AI systems engineer" exists. Find it with the Artifact tool's list action and republish to the same URL after changes.

## Inventory of names

**13 Nov: Het cleared the real names, so the site uses them and the descriptors are no longer needed.** They stay in the last column in case a name ever has to come off again.

| Code | Name to use | Fallback descriptor |
|---|---|---|
| E1 | Infocusp Innovations (current employer, Oct 2026 to now) | "an engineering services company in Ahmedabad" |
| E2 | Crest Data (previous employer, Dec 2021 to Oct 2026) | "an engineering services firm building for enterprise security and observability vendors" |
| E3 | LearnElectronics (internship, 2021) | "an electronics-education startup" (or omit the role) |
| C1 | Armis (cards 01 and 02), as Crest Data's customer | "a US asset-security company" (brief §7 wording) |
| C2 | Comcast (card 03), as Crest Data's customer | "a large US telecom company's security data platform" |
| C3 | Splunk (card 04), as Crest Data's customer | "an enterprise observability software vendor" |


## Figures: use and don't use (brief §4)

- **Use:** about 5 years; 32 tenants; 250K a day and 1.5M+ at the peak (a 6x weekly burst); 12 scanners; 4M keys; 81% hit rate (95%+ during full scans); 5 stages; 212K calls a day; 98.5% success; 85% of prompt tokens cached; about 2,000 events a minute.
- **Don't use:** the 20% query-performance and 30% downtime figures (no baseline), GPA, and any converted or extrapolated figure (for example, events a minute turned into events a day).

## Inputs from Het: status on 13 Nov 2026

1. Availability line: approved with "part-time", then **taken off the page** the same evening, for now.
2. Descriptors: **replaced by the real names** (inventory above).
3. Personal projects: **skip for now**. No "Built on my own" row.
4. GitHub: **github.com/het-shah2000**, linked in the footer. Its three repos were checked and none went on the page.
5. Certifications: **keep the AWS name.** The Anthropic line is out; Het didn't mention it.
6. Weekly chart in diagram 1: **confirmed.**
7. Email and domain: **hetshah2000@gmail.com** and **hetshahbuilds.in** (bought).
8. Portrait: **still to come** (IMG_1992 tried and rejected on 14 Nov 2026).
9. Recommendations for Voices: **still to come** (LinkedIn).
10. One-page profile PDF: **built**, `profile/Het_Shah_Profile.pdf`, from `profile/profile.html`. No phone number. It names the cleared companies.

Still open: whether the Anthropic certifications come back, whether any internal product name may be used, and what "98.5% success" means.
