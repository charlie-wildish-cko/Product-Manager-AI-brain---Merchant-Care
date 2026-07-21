# HBR Jan–Jun 2026 — Redline against Milan's comments

Source: [HBR doc](https://docs.google.com/document/d/1AKfnQZh6GFf6m1s7bymDvTMiZX9Wrlq1Qs7GLxBPn0E/edit)

Format: ~~original~~ → proposed replacement, with Milan's comment quoted.

---

## Exec Summary

**Cost per contact stat**
> Milan: "driven by...."

~~Cost per contact fell 34% from Q4 to end H1, from $45.77 to $30.36, while contact rate held stable and CSAT stayed at ~85%.~~
→ **Cost per contact fell 34% from Q4 to end H1 ($45.77 → $30.36), driven primarily by faster agent handling time from automated routing, with Fin deflection contributing ~$3.55 of the drop (~$68k H1 saving, 3.5x ROI). Contact rate held stable and CSAT stayed at ~85%.**

**Growth framing**
> Milan: "this is important, but i think you need reframe with a clearer [intro] ... it feels a bit lost as an add on to the cost saving"

~~We did this while building the foundations to support 85x contact growth. A Q1 exercise based on forecasted customer growth projects support contacts rising from ~40k per year to ~2m by 2030 on current contact rates and planned TPV, driven by Platforms (incl. SMB) and Consumer.~~
→ **The bigger story this half is scale, not just cost. A Q1 forecasting exercise projects support contacts rising from ~40k/year today to ~2m by 2030 at current contact rates and planned TPV — an 85x increase, driven by Platforms (incl. SMB) and Consumer. Everything below was built with that scale in mind.**

**"Supportable products"**
> Milan: "what does this mean?"

~~Prevent contacts before they happen, through supportable products and self-serve~~
→ **Prevent contacts before they happen — designing products that surface answers before merchants need to ask, plus self-serve content.**
*(Define "supportable products" once, here, if the term is going to recur.)*

**"Build a cost structure ready for scale"**
> Milan: "its not build a cost structure at scale, the outcome is costs do not scale proportionally to contact right?"

~~Build a cost structure ready for scale, where AI resolves most contacts at low cost with a human in the loop where needed.~~
→ **Decouple cost from contact volume — AI resolves most contacts at low cost with a human in the loop where needed, so cost doesn't scale proportionally with growth.**

**80% target**
> Milan: "why 80% why not 99% or 70% - related, is to not lose this is a 2 pronged approach - stop the contact/support in the 1st place (this = x% reduction, then improve automation on the actual support needed)"

~~Target: AI resolves 80% of contacts by 2030, with no compromise on quality or satisfaction.~~
→ **Target: AI resolves 80% of contacts that reach support by 2030, with no compromise on quality or satisfaction. This is the automation side of a two-pronged approach; prevention (reducing contacts that reach support at all) is not yet modeled and is a gap to close in H2.**

**"Expect to decide"**
> Milan: "expect? will?"

~~We expect to decide in Q3 whether to move off Zendesk~~
→ **We will decide in Q3 whether to move off Zendesk**

**Zendesk/Consumer timeline logic**
> Milan: "maybe I'm naive - but even without consumer, wouldn't you be looking to migrate before the end of the contract - on top of that, when does it need to be in place to reduce migrations later?"

~~Our Zendesk contract runs to June 2027, but the Consumer launch has pulled the timeline forward: we would rather launch Consumer directly on the new platform than stand up a temporary Zendesk setup and migrate months later.~~
→ **Our Zendesk contract runs to June 2027 and we'd need to decide on a replacement regardless. The Consumer launch adds urgency: the new platform must be selected and ready by [date] so Consumer launches directly on it, avoiding a second migration a few months later.**
*(Fill in the actual decision-readiness date Milan is asking for.)*

**Fin savings comparison**
> Milan: "vrs.. x"

~~Fin deflection is the clearly attributable driver (~$3.55/contact, ~$68k H1 saving, 3.5x ROI).~~
→ **Fin deflection is the clearly attributable driver (~$3.55/contact saved vs. [baseline cost without Fin], ~$68k H1 saving, 3.5x ROI).**

**Handling time attribution**
> Milan: "not clear what this is saying"

~~Faster handling and routing contributed the larger share but are harder to isolate cleanly, as taxonomy, routing, and agent tooling all landed together.~~
→ **Faster handling and routing contributed the larger share of the 34% drop (~$8 of the ~$15 improvement), but taxonomy, routing, and agent tooling all shipped together, so we can't yet cleanly separate their individual contribution. We'll sharpen this attribution in H2.**

**Manual assignment**
> Milan: "this can be worded better - and why do the items that are manual remain manual assignment?"

~~We switched from manual to automated assignment in May. Manual assignment dropped from 85% to 36-40% (remaining manual by design: Dispatch, Flow migration for Tier 4-5, IM logging in APAC).~~
→ **We switched from manual to automated assignment in May, cutting manual assignment from 85% to 36-40%. The remainder stays manual due to operational process, not a tooling gap: Dispatch runs on a daily rota, and IM logging (e.g. WeChat) requires agents to manually add conversations raised off-Zendesk into the system. Flow migration for Tier 4-5 [confirm reason if different from the above].**

**Outages**
> Milan: "outages?"

~~When Fin cannot resolve, it classifies against our taxonomy, routes to the right agent, and flags potential outages for triage with the OC.~~
→ **When Fin cannot resolve, it classifies against our taxonomy, routes to the right agent, and flags likely payment-system outages [or clarify what kind] to the on-call team for triage.**

**Agent Consultant description**
> Milan: "this is cool, i think you should be clearer what this means - ie agents are given more context to facilitate better and faster resolution (and do we have data on this?)"

~~It diagnoses common payment issues and checks MENA third-party acquirer status (MPGS), a workflow that was ~10% of volume at 15-20 mins/ticket.~~
→ **It gives agents the context to resolve faster: diagnosing common payment issues and checking MENA third-party acquirer status (MPGS) — a workflow that was ~10% of volume at 15-20 mins/ticket [add: and now takes X mins, if data exists].**
*(If no data yet, say so rather than imply it.)*

**Reflex description**
> Milan: "this is not coherent"

~~Reflex is an AI-powered insights app that shows Product teams their top support drivers; opening company-wide post-Beta.~~
→ **Reflex is an AI-powered insights tool that shows Product teams their top support drivers, so they can see what's driving contacts for their product. Currently in Beta; opening company-wide after Beta completes.**

**BigQuery / data access lowlight**
> Milan: "did BQ make this worse - was it not a problem before - i would split these are two points - data access, and semantic layer missing" / "not clear"

~~Most required data now sits in BigQuery, accessible internally but not to third-party tools like Fin, with query latency in minutes that would degrade the chat experience. There is also no single source to look up a payment across pay-in, payout, unreferenced refund, and Issuing, and no semantic layer to explain failures in plain language.~~
→ **Two separate problems, split out:**
**1. Data access:** Most required data sits in BigQuery, accessible internally but not to third-party tools like Fin — query latency runs to minutes, which would degrade the chat experience. [State whether this predates BQ or was introduced/worsened by the BQ migration.]
**2. No semantic layer:** No single source to look up a payment across pay-in, payout, unreferenced refund, and Issuing, and no layer to translate raw failure codes into plain language.

**Action item**
> Milan: "not clear"

~~Action: building an internal AI Agent in H2 to analyse data and return outcomes to Fin; H2 Analytics roadmap items for a unified payment lookup and a semantic data layer.~~
→ **Action: build an internal AI Agent in H2 that queries BigQuery directly and returns structured outcomes to Fin, removing the latency/access problem. In parallel, add two H2 Analytics roadmap items: a unified payment lookup (across pay-in, payout, refund, Issuing) and a semantic data layer for plain-language failure explanations.**

---

## North Star Metrics

**Contact per 1M transactions target**
> Milan: "5% as in 50K per million?"

~~Within +/- 5%~~
→ **Within +/- 5% of [baseline, e.g. 7.5 contacts/1M], i.e. holding between [X] and [Y] contacts per million transactions**

**Tier breakdown / Q1 spike**
> Milan: "so contacts outside tier 1 are going up - and why is q1 busy (tax reports?)"

→ Add one sentence naming the actual Q1 driver (confirm with Imran — tax reporting season, or another cause) before the tier breakdown table.

**Tier table correction (per Imran's thread)**
Replace the Tier 1–3/5/Unmanaged breakdown with the corrected version using official Salesforce Sales Ops Tiering (removes the Zendesk-artifact Tier 5 spike):
- Tier 1: 3.29 → 3.60 → 3.04 (stable)
- Tier 2: 13.91 → 15.90 → 15.03 (stable, contact growth matched by volume growth)
- Tier 3: 33.63 → 42.29 → 35.65 (Q1 contact surge on flat volume, normalized in Q2)
- Unmanaged: 127.85 → 128.88 → 50.35 (Q2 halving is a denominator effect from one merchant, Uber Formosa, ramping 0.5M→12.5M transactions — not an efficiency gain; flag Uber Formosa's mis-tiering to Sales Ops separately)

*(This directly answers your own open comment: "should this be Tier 4 and 5 (unmanaged)?" — yes, replace with Unmanaged per the corrected tiering.)*

---

## Engineering Metrics

**Uptime SLA**
> Milan: "DG? does this matter? (i thought we wanted less datadog use)"

→ Reconsider including this metric as-is, or reframe without the Datadog tie-in given the stated direction of reducing Datadog dependency.

**Median Cycle Time**
> Milan: "not clear"

~~Median Cycle Time~~
→ **Median Cycle Time [add one-line definition, e.g. "time from ticket creation to first resolution"]**

**"Date of 80% Deliverables Completed"**
> Milan: "what does this mean. we deliver 80% of things on time?"

~~Date of 80% Deliverables Completed~~
→ **% of Roadmap Delivered On Time (target: 80% within the quarter)** — reword the metric name so it doesn't need explaining.

---

## H2 Priorities

**"Making teammates more efficient"**
> Milan: "anything more precise than 'more'"

~~Making teammates more efficient, using AI tooling~~
→ **Cut agent handle time by [X]% using AI tooling**

**PM accountability framing**
> Milan: "i would reword this - you are not on the hook for them driving down contacts - you are on the hook for telling them where they can make the biggest impact and identifying the largest problem areas"

~~Help PMs drive down contact reasons root cause using actionable contact data insights~~
→ **Give PMs the data to identify where they can have the biggest impact on contact reasons in their products** — Care surfaces the insight; product PMs own the fix.

**Zendesk replacement row / Consumer consistency**
> Milan: "how does this relate to the consumer comment? isn't your goal to have the new product in place and launch consumer on it in Q4, and then migrate away from zen... by end of H1"

→ Align this row's wording with the corrected Exec Summary Zendesk/Consumer timeline (see above) so the two sections don't read as two different plans.

**Consumer launch deliverable**
> Milan: "of what products?" / "?? what does this mean"

~~Support tooling readiness for Consumer launch in Oct (internal staff) and external in Q1~~
→ **Support tooling readiness for Braavos/Consumer launch: internal staff pilot in Oct, external customer launch in Q1 [specify which products/flows this covers]**

**Fin resolution math (appears 3x — make consistent across all three rows)**
> Milan: "fin resolves 40-50% of all, or of fin engaged?" / "12-15% more than today so ±20-25? or 12-15% in total?"

For each of the three Fin rows, restate explicitly:
→ **"+12-15 percentage points of overall AI resolution (from current [X]% baseline to [X+12–15]%), assuming Fin resolves half of [channel]'s volume."**
Apply the same explicit-baseline pattern to all three Fin deliverable rows (email, Dashboard webform, Payment Diagnostics Agent) so the reader can add them up without guessing.

**Agent Consultant deliverable**
> Milan: "what is that as a deliverable?" / "what does this mean in total - this can be framed better"

~~Agent Consultant: refund reversals, complex diagnostics~~ / ~~Cut handle time on complex tickets 10-20%~~
→ **Deliverable: ship refund-reversal automation and complex payment diagnostics in Agent Consultant. Impact: cuts handle time on complex tickets by 10-20%, equivalent to [X hours/week or $Y] in agent capacity freed up.**

---

## Help Needed

**Accountability framing**
> Milan: "there is NO accountability today"

~~sign-off from Product leadership to require a supportability review before any new product ships, and agreement from pillar leads to own a contact-rate target for their products~~
→ **Today there is no accountability for contact rate at the point of product launch. We need: (1) sign-off from Product leadership to make a supportability review mandatory before any new product ships, and (2) pillar leads to each own a contact-rate target for their products.**

**Has this been asked?**
> Milan: "have they said no, have they been asked?"

→ Add a status line: has this ask actually been raised with Product leadership yet, or is this the first time it's being surfaced? State it plainly either way.

**Sequencing — "why it matters" answered out of order**
> Milan: "and this matters why?" — reply: "i see answered below, but this is not a natural way to read"

→ Move the "Why it matters" sentence (currently: "we are scaling into Platforms, SMB, and Consumer in 2027... embedding Care in the development cycle now is far cheaper than absorbing the volume later") to immediately follow the ask, not several sentences later.

**Second ask clarity**
> Milan: "not clear"

→ Tighten the "Fix the e2e payments experience" ask — currently reads as a list of symptoms (decline reasons, transaction status, settlements) without a clear single ask sentence up top.

---

## Not yet actioned in doc (from your threads with Imran)
- Confirm the Q4→Q2 cost delta (~15%?) is reflected accurately once Imran's final numbers land.
- Consider flagging Uber Formosa's mis-tiering (Premium segment, Unmanaged tier) to Sales Ops as a side action, separate from the HBR narrative.
