# Ray Care content

**Date:** 2026-08-24
**Attendees:** Charlie Wildish, Sebastian Garcia Cardona, Max Rothman (Ray, Dubai), Oliver Westlake-Simm (invited)
**Drive source:** 1PKVVYaxK8u4kf7qm_Ak70dMT7jbymlRj-a0LA78tF8M

## Context

First working session on Ray support content after the Braavos pivot: how much content is needed, how it gets drafted, and which platform Care support for Ray is built on.

## Key Points

**Content scope**
- Rule: every taxonomy issue and sub-issue has a matching content piece. Fin uses that content as the primary answer, then either resolves or applies a rule routing to a human for the action.
- Compliance workflow sections of the taxonomy likely need no customer-facing content. Anything a customer would ask does.
- Max estimates the taxonomy covers 80-85% of foreseeable cases. More surfaces at launch and gets added over time.
- Scale: ~180 content items, of which Max estimates only ~30 are genuinely sensitive and need strict sign-off. Sanctions hits are the example of what must never be surfaced.
- The Braavos-era taxonomy still underpins content needs and carries over for content mapping, even though the Braavos regulatory framing does not.

**Content pipeline**
- Sebastian's existing pipeline, built for Braavos: a Slack workflow lets anyone submit a new article request or update in one button press. Submissions are picked up automatically, Claude generates drafts against the style guide and tone of voice, and output goes to Google Docs for collaboration or as pull requests on the support repository, ending in a tech-writer approval gate.
- Removes the single-team bottleneck and lets other product teams (disputes, authentication) contribute.
- Still to build: additional review gates for teams like legal, who wanted final say on language for Braavos.
- Max pushed back on heavy guardrails. Ray does not carry Braavos's Consumer Duty verbiage constraints, so sign-off is "does this make sense" rather than exact regulated wording. Brand and marketing supply flexible tone of voice.
- Two exclusion flags agreed for the first Claude generation pass: highly sensitive items needing expert review first, and app-journey-driven items, since Claude would hallucinate in-app steps before designs exist.
- Source material: Max cleaned up the PRD so it is accurate as of now, including which tools are used (Fin everywhere, Zendesk as the agent fallback, Ray's compliance tooling). PRD plus go-to-market docs are enough for solid first drafts.

**App journeys**
- MANA produces app direction and wireframes on Wednesdays. Wireframes differ from Braavos visually but action locations are broadly the same.
- Sebastian will get code-base access to infer journeys from the HTML wireframes, needing only minor manual review.
- Charlie flagged that MANA needs to review the Care taxonomy items against the app flows, so support paths are accommodated in the designs rather than Care and app design being built for two different things.
- FAQ content may sit on a web-hosted page rather than in-app. For Braavos V1 everything was markdown hosted in-app while Zendesk infrastructure was built.

**Timeline (per Max)**
- October: internal testing, ~50 people. December: friends and family. GA phased toward end of Q1. Waitlists likely, to manage KYC and verification delays, since ID reading quality is a constraint. Roughly a six-month gated ramp.

**Channel and platform**
- Everything runs through Fin. Email only as a last resort, deliberately placed behind several steps. Support is intentionally harder to find than a default fallback. Content rules will avoid over-inviting contact.
- Max wants engineering buy-in for a front-end layer before Fin, handling cases like terminated accounts directly so they never generate a Zendesk escalation or a Fin loop. Joe may say no.
- Charlie's team is assessing whether to build Care support for Ray on the new platform in time for December, rather than building on Zendesk and rebuilding twice (which is what Braavos would have forced). Bare-minimum scope is a ticket pass-through for 50-100 users, no Fin needed at that size, launched separately to test. Merchant-facing experience is unchanged either way: the benefit is Care team scalability.

**Content owners**
- Mainly Ray compliance, risk and fraud. Max and Brian Weer cover compliance. Joe Foss knows the architecture well. Fraud and Ray are effectively the same team as on the Braavos side, with fewer people now.

**Decisions**
- Relax content review guardrails versus Braavos: general sense-checking, not rigid Consumer Duty verbiage.
- Use Claude to generate first drafts from the PRD, go-to-market docs, and the current taxonomy spreadsheet fed in as CSV.
- Apply the two exclusion flags to skip initial drafting.
- Work in one shared document: taxonomy plus content-owner column plus first-draft-review columns.
- Everything routes through Fin. Email deliberately de-prioritised.

## Insights

- Removing Consumer Duty constraints is what makes AI-drafted content viable for Ray. ~180 pieces with only ~30 sensitive is a tractable content programme, where Braavos was not.
- Sebastian's Slack-to-Claude-to-PR pipeline is a reusable Care content capability, not a Ray-specific build. Treat it as a knowledge-domain asset.
- Live open question for Charlie: build Ray Care support on the new platform for December, or on Zendesk and rebuild. December scope (50-100 users, no Fin) is small enough that a bare-minimum pass-through is a viable hedge.
- Max's "front end before Fin" proposal is a genuine deflection-architecture idea: handle known terminal states such as account terminated before the AI layer, so they never enter the support funnel at all.
- The taxonomy-to-content one-to-one rule makes taxonomy quality the gating item for Ray content, not content production capacity.
