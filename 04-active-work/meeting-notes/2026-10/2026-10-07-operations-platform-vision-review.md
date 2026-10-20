# Operations Platform Vision: initial review with Ops

**Date:** 2026-10-07
**Attendees:** Charlie Wildish (PM, Care), Oliver Westlake-Simm (process), Joel Petrosino (Ops, configuration work), Sebastian Chmielinski (Risk), Malcolm Higenyi. Roles are inferred from the transcript.
**Source:** Gemini transcript, `Downloads/Operations platform vision - initial chat & plan - 2026_10_07 13_15 BST - Notes by Gemini.md` (Charlie appears as "LON-04-13"). "Plane" = Plain. Several tool and team names are garbled and omitted.

## Context

Charlie played back the draft current-state and future-state model (front stage, back stage, orchestration, underlying systems) to get Ops feedback. Plan: play it back to Jenny and the wider group at the end of October to agree "a stake in the ground", then validate bottom-up with each team.

## Key Points

**Current state (confirmed, with additions)**
- Teams use different email inboxes. Care is the only team with an alternative to email (Dashboard request form and Fin). An email to an inbox may land in Salesforce or an actual Gmail account.
- Internal requests move by email and Slack, manually assigned. AI exists only on the Care side.
- Customers are bounced between teams with no joint view. Account managers act as the glue and get pinged by several teams about the same issue.
- Tracking a request outside Care means crawling an email inbox. Reporting is stitched together by hand: Jenny said a complaints record can take hours to assemble when the case left Care (take with a pinch of salt on accuracy).
- No linkage between a piece of work and the tool used to do it, except loosely in Fin Crime and transaction monitoring. Joel confirmed the configuration team still manually copies Salesforce cases into CAT.
- Tool sprawl: Retool (tens of apps), RA Tool, Sardine, Fircosoft, Genesis, CAT and others.
- New (Joel): commercial and account managers talk to merchants in Slack and WhatsApp. Example: Care was messaging a merchant about goodwill remediation while commercial had already given a fee reduction. Visibility is needed both ways, and part of it is a process and accountability gap (commercial sign-offs).
- Consumer Duty: reporting SLAs and exposure is a small problem today but would be "a huge problem" for consumer, and SMB brings Consumer Duty obligations in the UK arguably.

**Future model (four parts)**
1. **One front door.** Structured intake for work from any source. Retire team inboxes. Customers still get email, but one unified address, and the work is triaged and routed behind it. Top-tier merchants who email account managers need a dedicated channel for AMs to submit work, or the means to solve it themselves. Charlie: "no regret", little downside.
2. **Self-serve, then AI, then human.** Already partly in place for Care. Depends on product building self-service (for example MCRs and configuration changes are not self-service today). SMB must be self-service heavy from day one.
3. **One case system of record (Plain).** Receives, creates and distributes all work to AI or humans: audit log, assignment, routing, SLAs, escalation routes, workflows, reporting base. It replaces Salesforce, email inboxes and any other case systems for work. More than one case system breaks the principle and makes stitching harder. Plain is not necessarily the tool that does the work, and integrating every tool into it is complex.
4. **Consolidate the tools that solve the case.** One portal for humans, and an AI interface to the same data (not necessarily the same tasks). A shared tool that product teams contribute to and maintain, like the Checkout Dashboard model, but better governed for the interfaces. One central team building everything will not work.

**Hypotheses and principles**
- Hypothesis to test: about 80% of case load could be done end to end by AI, with 20% sensitive work staying human-in-the-loop. Charlie: "I don't know if that is true."
- Work does not have to happen in Plain: some tasks use another tool or a data query. The outcome always goes back to the case system of record.
- Most tools are a UI wrapper on data. UIs stay where a human-validated, audited interaction is needed. Sebastian: the RA Tool does two things (a rule engine and third-party integrations), both still required. Its front end could be wrapped by the portal and its risk information ingested, with RFIs sent from RA to Plain to the merchant.
- Permissions: one global permission set across portal, case system and AI agents, needed for BPOs. Applies both ways: someone in Plain should not be able to invoke an AI agent to retrieve data they cannot see. Joel's prior platform used team-level profiles with work queues, and cases tracked across teams "like a DHL delivery", so Care could see where a case sat.
- Standardise: every team works to a consistent mechanism, with no exceptional workflows. Oliver agreed: a central framework with a few variables (for example taxonomy) and everything else structured and the same, which also makes distributed governance and tech implementation easier.

**Salesforce and onboarding**
- Joel: many risk work items start in Salesforce, initiated by commercial (MCRs, net new onboarding, underwriting, then configuration in CAT). Commercial treats Salesforce as its record of truth.
- Oliver: quote to cash is being built outside Salesforce. The onboarding process needs redesign (merchants receive a 46-page spreadsheet). Discovery should include the Salesforce owners and their plans so the case system integrates long term.
- Charlie: assumes everything integrates from sources of truth, and the onboarding process is being re-architected next year because it causes problems for platforms.

**Prioritisation and ownership**
- Charlie: parts 1 and 3 add the most value first. Part 2 is already partly done in Support. Solving the human workflow has more value than pushing everything through AI, which needs back-end work.
- Oliver challenged: part 4 has the biggest impact but the biggest lift. Example: the periodic review team moves through CAT, Genesis, the RA Tool, Looker and another tool just to decide whether a review is needed.
- Agreed direction: a prioritisation model per team (easy to automate vs complex tooling), moving teams and optimising tools in a mix.
- Oliver wants one owner for the whole thing, end to end across the merchant lifecycle, and offered Charlie as his preference. Charlie: governance would sit within EP, enforced at product launch (provide the service and the UI, designed holistically). Structured intake based on MCAP or the product process, tied to the product catalogue. Charlie to add product introduction to the front of the model.
- Sebastian: link work items to related recently closed ones and prefill, so a risk alert already reviewed by another team is not re-checked. Charlie: falls under AI procedures, with SOPs plus past solutions as the golden source, which needs one trackable system.

## Action Items

- Charlie: add product introduction and the product catalogue to the front of the model.
- Charlie: bottom-up work with merchant ops, risk ops and compliance to inventory work types, using the SOPs to find similar, different and automatable work, and build the automation business case.
- Charlie: play the model back to Jenny and the wider group at the end of October.
- Charlie and Oliver: discuss the SMB piece of work.
- Oliver and Charlie: discovery conversation with the Salesforce owners on their plans.
- Oliver: pick up the agent performance dashboard duplication with Ashin.

## Insights

- The core review feedback supports the model. The open arguments are sequencing (Charlie: parts 1 and 3 first, Oliver: part 4 has the biggest impact) and ownership (one owner end to end).
- Specialist tools are mostly UI wrappers on data. That supports consolidating their functionality into one portal, and it confirms the contribution model.
- Salesforce is the hardest dependency: commercial's record of truth, with quote to cash moving out of it.
- Charlie's 80/20 AI figure is a hypothesis, not data. Do not put it on a slide as a number.
