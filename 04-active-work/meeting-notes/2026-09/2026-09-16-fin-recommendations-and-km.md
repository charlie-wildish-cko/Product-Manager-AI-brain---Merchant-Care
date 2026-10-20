# Fin Recommendations and Knowledge Management

**Date:** 2026-09-16
**Attendees:** Ashvin Pudaruth, Karan Jagmohansing, Alex Jordan, Joanie Vencatasamy, Charlie Wildish, Francisco Goncalves, Ling Wong, Robert Braam
**Drive source:** 1nZ1oZ82asMEMClq3YcpYIHJRLZQJLV6XnFnP2Jj5X8Q

## Context

Review of how Fin's content performance data should drive the knowledge backlog, plus the new Intercom GitHub sync capability.

## Key Points

**Content performance data**

- Fin's help-centre reporting gives resolution rate at section level, which does not map cleanly to the support taxonomy, and covers external content only. Agreed to add Zendesk solved tickets as a second data point.
- "Understanding payment statuses": **525 citations, 82.7% resolution rate** when used. Top performer.
- "API response codes": **43% resolution rate**. Two named causes: the page is enormous and sometimes does not load, and the response codes lack proper definitions.
- Top performers are consistently guides with videos, produced by the Zendesk/content team.
- Payout-related content has spiked in volume recently.
- Transaction status and refunds have slightly lower match rates but much higher volume, so more phrasing variance. The group's view: volume plus variance is where the real loss sits, not the low-volume misses.
- Some queries retrieve no content at all. Treated as a separate guard-rail metric, distinct from content performance.
- Authentication appears as a topic Fin could not solve from article performance, inconsistent with a different report that framed it as highly repeatable.

**Agent source attribution**

- Robert Braam asked whether agents could be prompted on solve for which documentation they used. Three constraints surfaced: the old Zendesk pin feature produced no metrics and was abandoned; agents search in Glean, which exposes usage and votes but not search queries for privacy reasons; and both Glean and Fin synthesise across sources, so an agent often cannot say which article answered it.
- Alternative proposed: a **golden set** of tickets whose replies QA scored highly, used as the knowledge source.
- Plan to point AI agents at conversations and messages to audit content gaps, intent mismatches and keyword problems. The data exists, the process does not. Framed as "build the workflow as a project, then running it is BAU, not a goal."

**Content hygiene and fragmentation**

- A richer internal version of response codes exists in Fig but is not cleared for public release. Deliberate decision not to maintain a separate internal copy, because it fragments. Even the better internal page is too big: **Fin's context window runs out and it cannot read the codes at the bottom of the page.**
- Fin insights and the API/docs content belong to the technical writing team (John, Rob, tech writers), so Care depends on them to action findings. Current approach is partnership, including co-producing video guides.
- Suggestion to filter internal articles for merchant-facing candidates and hand ~50 to Seb's team where Fin resolution is poor. Seb recently did a comparable SOP pass.
- **80 articles were reviewed and updated ahead of the Mexico launch** as the ones critical to enabling Mexico.
- Metadata mapping is the named critical dependency. Mapping all content to case type across every source gives a clean view of what exists per case type, exposes gaps, and allows internal/external sync. Without it, AI scanning creates ambiguity and false matches.
- Preethy is leaving.

**GitHub sync (new Intercom capability)**

- Fin syncs content directly from the source repo instead of crawling the website. Updates push automatically.
- Bidirectional: accepting a Fin recommendation raises a pull request on the repo. Alex publishes an article to GitHub, a trigger checks it against public content, and if there is an addition to make it raises the request.
- Sequence: infrastructure sign-off (installing an app into Checkout's GitHub org, which holds all company code, so treated as high-stakes), then setup and testing to confirm parity with today's state, then a sandbox test.
- Markdown files are far easier for Fin to ingest than crawling a website.
- Timeline: get GitHub sync done this year. Monthly catch-ups with Intercom continue.
- Joel Petrosino owns the GitHub technical front.

## Decisions

- Incorporate Zendesk solved tickets as an additional content performance data point.
- Any content match scoring **below 50% resolution rate is reviewed as a priority**.
- Publishing will require mandatory metadata values: content without them cannot be published. Data quality gated at publish time.
- GitHub sync needs further discussion, pending infrastructure sign-off and sandbox testing.
- Charlie owns a new project: capture knowledge from highly-scored agent replies and feed it into content. Preference stated for enhancing existing content rather than holding a separate knowledge source, since content is the content team's remit. Possible route: use Joanie's existing system (holds ticket numbers, decides which SOP applies), cross-reference against QA'd tickets to see which SOPs were actually used, and identify which should be enabled externally.

## Insights

- Two reusable numbers for any content or deflection business case: 82.7% resolution on "Understanding payment statuses" across 525 citations against 43% on "API response codes". The delta is page size and missing definitions, not topic difficulty. Strong, cheap argument for chunking large doc pages.
- Fin's context window is an observed production constraint, not theoretical. Page size is an AI-retrieval content requirement.
- GitHub sync is the highest-leverage item and its critical path is internal infrastructure approval, not vendor delivery. It is also the first mechanism that closes the loop between Fin's observed gaps and the docs actually changing. Note it deepens the Intercom dependency, which intersects the Zendesk/Plain platform decision.
- The <50% resolution review threshold is now a standing operating rule.
- Metadata mapping to case type is the unlock for gap analysis, internal/external sync and clean AI retrieval. Now enforced at publish time. Directly relevant to measuring content coverage per case type for contact-rate work.
- Agent source attribution is effectively unsolvable head-on: Zendesk pins gave no metrics, Glean will not expose queries, and both Glean and Fin synthesise. The QA golden-set route is the viable path, worth remembering so it is not re-litigated.
- Fin insights and API/technical content sit with technical writing, not Care. Care can identify gaps but cannot unilaterally fix them.
- Preethy leaving affects the review panel persona set in `01-knowledge-base/processes/review-panel-personas.md`.
