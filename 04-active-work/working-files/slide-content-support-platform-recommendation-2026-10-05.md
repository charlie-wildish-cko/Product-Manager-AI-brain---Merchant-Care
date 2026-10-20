# Slide content: Support platform recommendation (restructure after Milan's review)

**Source of truth**: Google Slides deck "Merchant Care: Support platform recommendation" (file ID `1ndQCgRdGvEXKwRYlCFgrFnUh2DcMCq01i9n2aVOgp24`). Numbers and wording follow the deck. New figures (group scores, weight sensitivity, build vs buy) are calculated from the deck's Appendix A scores and Appendix B costs.
**Review**: Milan Jani (VP Product), 2026-10-05: core story in 3 slides, the rest in the appendix. Hélder Gonçalves comments, 2026-10-02.
**Deliverable**: Help Desk Platform Evaluation (Q4 2026 decision and approval), `2026 deliverables.md`.
**Strategy tie-in**: Merchant CSAT (the customer experience we want at scale), with cost per contact as the scale pressure ($20 human vs $1 AI).

---

## The argument (agreed 2026-10-06)

**Thesis**: Control of the stack is how we manage the changes needed at scale for our desired customer experience.

- **Scale brings constant change**: 30x+ volume, new segments each served differently, and a shift of volume to AI because a $20 human contact does not scale.
- **We own the layer that connects everything**, so we can make those changes ourselves and swap vendors underneath.
- **So the core vendor must be flexible first** (API-first, config as code, any AI), then deliver agent and customer experience, then be a partner we can rely on.
- **Plain is the only vendor built that way.** It leads every criteria group, the result holds under any weighting, and the POC proved it.

**Weights**: set by how much each area mattered to the outcome. Flexibility is the main driver (60%). Customer and agent experience remain important (27%). Partner and cost carry 13%. The eight scored criteria roll up into these three groups:

| Group | Criteria | Weight | Plain | Intercom | Pylon | Zendesk |
|---|---|---|---|---|---|---|
| Flexibility | Channels, data model and routing (20%) · Integration ease (15%) · AI compatibility (15%) · Config as code (10%) | 60% | **2.59** | 2.02 | 1.85 | 1.52 |
| Experience | Agent experience (20%) · Customer-facing experience (7%) | 27% | **2.10** | 1.79 | 1.77 | 1.56 |
| Partner and cost | Partnership and reliability (10%) · Pricing (3%) | 13% | **2.43** | 1.87 | 1.75 | 1.45 |
| **Total** | | 100% | **2.44** | 1.94 | 1.81 | 1.52 |

**Answer to "7% customer experience, really?"**: customer experience is the goal of the whole deck. The 7% criterion scores only the vendor's native portals, which we would build ourselves. The experience outcomes that matter most (one thread from AI to human, the right routing per segment, live context for agents) are delivered through flexibility and agent experience, and are scored there.

---

## Restructure map: where each current slide goes

| Current slide | New home |
|---|---|
| Title ("Replace Zendesk with Plain") | Rewrite: prompt 0 |
| Context: Zendesk is our ticketing and agent UX | Cut. Replaced by "what the core must do" on core slide 1 |
| Exec summary ("Zendesk won't meet our scaling...") | Replaced by core slides 1-3 |
| Scaling into new territory (30x+) | Folded into core slide 1, card 1. Full slide moves to the appendix |
| Using AI is how we afford growth | Folded into core slide 1, card 1 ($20 vs $1). Full slide moves to the appendix |
| Zendesk will not support our AI ambitions | Appendix (evidence behind Zendesk's AI compatibility score) |
| We already pay for what Zendesk cannot do | Appendix. Its blocks become the unnamed "Today" strip on core slide 1 |
| Investing in a new architecture is no regret | Merged into core slide 1, card 2 (the owned connection layer) |
| Case/ticketing vendor landscape | Appendix, rewritten: prompt A1 |
| Buy the core now | Appendix, rewritten: prompt A2 |
| How we scored vendors | Replaced by core slides 1 and 2. Category descriptions stay in Appendix A |
| Plain were top | Replaced by core slide 2 |
| Vendor cost comparison | Appendix |
| Who are Plain? · Why not Intercom or Pylon · POC proved · User experiences · Customer references · Known feature gaps | Appendix, in that order |
| Target Care architecture | Appendix, straight after the core (detailed version of slide 1, card 2) |
| Mitigated risks · Migration plan | Appendix |
| Key decisions | Replaced by core slide 3 |
| Appendix A-E | Unchanged. Add the grouped score table above to Appendix A, and Hélder's FAQ line (end of this file) |

---

## Appendix order (agreed 2026-10-06, sets the order for every slide the map above moves to the appendix)

Grouped by the core slide each section backs up. Titles move away from "Zendesk bad" framing, since readers open the appendix too. Prompts are below for the slides marked **new prompt**. The rest only need moving, retitling or merging by hand.

| # | Slide | Source | Action |
|---|---|---|---|
| 0 | Appendix index | New | **New prompt** (Appendix index) |
| **1** | **Backs core slide 1: why we need control** | | |
| 1.1 | Scale: 30x+ by 2030 | Current scaling slide | Keep |
| 1.2 | A $20 human contact doesn't scale to ~2m contacts | Current AI slide | **New prompt** (Appendix 1.2) |
| 1.3 | Most of today's constraints are flexibility gaps | Current "we already pay for..." slide | **New prompt** (Appendix 1.3) |
| 1.4 | AI openness: our Fin integration runs on an exemption | Current Zendesk AI timeline | Retitle only |
| 1.5 | Target architecture | Target Care architecture + Appendix D | Merge into one slide. Add the 6 architecture principles from the old architecture slide |
| **2** | **Backs core slide 2: how vendors scored** | | |
| 2.1 | Only Plain is both customisable and open to any AI | Current landscape slide | Prompt A1 |
| 2.2 | Flexibility carries 60% because it drives everything else | Current "how we scored" slide | **New prompt** (Appendix 2.2) |
| 2.3 | Detailed scores | Appendix A | Add the grouped table and the stress test from "The argument" above |
| 2.4 | Why not Intercom or Pylon | Current slide | Keep. Check the Intercom acquisition wording (open items) |
| **3** | **Backs core slide 3: why Plain** | | |
| 3.1 | The experiences this enables | Current user experiences slide | Keep, moved to the front of the section |
| 3.2 | POC results | Current slide | Keep |
| 3.3 | Who are Plain | Current slide | Keep |
| 3.4 | References | Customer references + Appendix C customer list | Keep both: our calls first, then Plain's list labelled "vendor-supplied" |
| 3.5 | Known gaps | Current slide | Keep |
| 3.6 | Cost | Cost comparison + Appendix B | Merge: summary on top, five-year table below |
| 3.7 | Building the core costs $5.8M by 2030, buying $1.8M | Current build vs buy slide | Prompt A2 |
| 3.8 | Risks | Current slide | Keep |
| 3.9 | Migration plan | Current slide | Keep |
| 3.10 | Demos | Appendix E | Keep |
| 4 | The four questions this decision raises, answered | New | **New prompt** (Appendix 4) |

---

## Overview prompt

```text
Role: Expert Google Slides designer.
Task: Create a 4-slide presentation on choosing a support platform for Checkout.com Merchant Care.
Audience: VP Product, CPO, COO | Tone: direct, minimal, executive
Grounding: text below only

Slide breakdown:
- Slide 1: "A support platform fit for 30x+ growth" | Layout: Minimal Title
- Slide 2: "Scale means constant change, so we must control the stack" | Layout: 3-Card Grid
- Slide 3: "Plain leads on flexibility, experience and partnership" | Layout: Single Chart + Callout
- Slide 4: "Plain fits our stack, proven in a four-week POC" | Layout: 4-Tile Matrix

Global constraints: Headline fragments only. Max 3-4 items per card/column. Max 8 words per item. Bold 2-3 word lead-ins. No paragraphs, no filler, no added statistics. Same fonts, colours and spacing on every slide. Plain in the accent colour throughout. Zendesk in muted grey.
```

---

## 0. Title

```text
Role: Expert Google Slides designer.
Task: Create one title slide for a support platform recommendation.
Audience: VP Product, CPO, COO | Tone: direct, minimal
Slide title: "A support platform fit for 30x+ growth"
Layout: Minimal Title. Title plus one-line subtitle, no bullets

Content:
- Subtitle: Recommendation: Plain, live before Zendesk ends June 2027
- Footer: Charlie Wildish | Product, Merchant Care | Oct 2026

Constraints: Use only the text above, verbatim. Fragment grammar, no periods. No added statistics, taglines, or intro/outro text. No vendor logos. Clean, minimal, consistent spacing. Visual: none
```

---

## 1. What matters

Answers Milan on: "what matters" first, capability-led rather than "Zendesk bad", AI framed as a change scale forces (not "AI is great"), the connection layer visualised, and pain points shown as where the criteria came from. The middle card is the architecture: it shows why the core must be API-first.

```text
Role: Expert Google Slides designer.
Task: Create one slide explaining what a support platform must do at Checkout.com scale.
Audience: VP Product, CPO, COO | Tone: direct, minimal
Slide title: "Scale means constant change, so we must control the stack"
Layout: 3-Card Grid, read left to right as a flow with arrows between cards. One-line subtitle under the title. One-line strip across the foot

Content:
- Subtitle: Control is how we keep customer and agent experience right

- Card 1 header: Scale brings change
  - Volume: 30x+ contacts by 2030, 70-80% consumer
  - Segments: Enterprise, SMB, Consumer served differently
  - AI shift: $20 per human contact vs $1 AI
- Card 2 header: We own the connection layer
  - Orchestration: human and AI flows
  - Our data: identity, taxonomy, knowledge
  - Swappable vendors: case platform and AI agent plug in
- Card 3 header: So the core vendor must offer
  - Flexibility (60%): API-first, config as code, any AI
  - Experience (27%): live context, one AI-to-human thread
  - Partner and cost (13%): roadmap we shape, predictable cost

- Foot strip, label "Today": weeks per change, 500+ manual config items, AI on an exemption

Constraints: Use only the text above, verbatim. Fragment grammar, no full sentences, no periods. Max 8 words per item excluding lead-in. Bold lead-ins and card headers. Card 2 in the accent colour and drawn as a connecting layer, with the two swappable vendors as detachable grey blocks beneath it. Foot strip in muted grey, smaller text. No vendor names in the foot strip. No added statistics, taglines, or intro/outro text. Visual: the three-card flow only
```

---

## 2. How vendors scored

Uses slide 1's group names exactly, so the criteria visibly come from what matters. Answers the four weighting comments: flexibility carries the weight because it is the main driver, and the result holds under any weighting.

```text
Role: Expert Google Slides designer.
Task: Create one slide showing vendor scores for a support platform decision.
Audience: VP Product, CPO, COO | Tone: direct, minimal
Slide title: "Plain leads on flexibility, experience and partnership"
Layout: Single Chart + Callout. Chart on the left two-thirds, callout column on the right

Chart: horizontal bar chart, weighted total score out of 3.0, sorted high to low
- Plain: 2.44
- Intercom: 1.94
- Pylon: 1.81
- Zendesk: 1.52
X axis: score, 0 to 3.0. Plain bar in accent colour, others grey. Data labels on bars

Callout (right column), header "Plain vs Intercom by group":
- Flexibility (60%): 2.59 vs 2.02
- Experience (27%): 2.10 vs 1.79
- Partner and cost (13%): 2.43 vs 1.87
- Any weighting: Intercom ties only at 72% integration

Footnote: Vendors discounted on flexibility first. 4-week POC, 3 reference calls

Constraints: Use only the text above, verbatim. Fragment grammar, no full sentences, no periods. Max 8 words per item excluding lead-in. Bold lead-ins. No added statistics, taglines, or intro/outro text. Clean, minimal, consistent spacing. Visual: the bar chart only
```

**Speaker notes**:
- Weights reflect how much each area mattered to the outcome. Flexibility is the main driver, so it carries 60%.
- Customer experience is the goal, but the 7% criterion only scores native portals, which we would build ourselves. The experience outcomes that matter are scored under flexibility and agent experience.
- Stress test, from deck Appendix A scores: equal weights give Plain 2.42 vs Intercom 1.88. Raising AI, config as code, reliability and customer experience gives 2.48 vs 1.84. Intercom draws level only if integration ease carries 72% of the weight.

---

## 3. Recommendation and ask

Cost moves off the headline: the deck's position is that cost does not decide this. Build vs buy sits in the appendix (A2) as the answer to a challenge.

```text
Role: Expert Google Slides designer.
Task: Create one slide with the recommendation and decisions for a support platform choice.
Audience: VP Product, CPO, COO | Tone: direct, minimal
Slide title: "Plain fits our stack, proven in a four-week POC"
Layout: 4-Tile Matrix. 2x2, bold header plus 2 fragments per tile

Content:
- Tile 1 header: Why Plain
  - Architecture fit: API-first, not embedded, full control
  - Any AI: Fin today, our own models later
- Tile 2 header: Proof
  - POC: 11 config-as-code tests passed, week 1
  - References: Vercel, Tines, Fyxer run custom stacks
- Tile 3 header: Cost and risk
  - Cost: not the decider, seat prices similar
  - Runway to 2028: investor diligence before signing
- Tile 4 header: Decisions by [TBC: Q4 date]
  - Approve Plain: as our support platform
  - Approve procurement: ~$500k over 2 years

Constraints: Use only the text above, verbatim. Fragment grammar, no full sentences, no periods. Max 8 words per item excluding lead-in. Bold lead-ins and tile headers. Tile 4 in the accent colour. No added statistics, taglines, or intro/outro text. Clean, minimal, consistent spacing. Visual: none
```

**Speaker notes**: "Our own models later" answers Hélder: Plain's machine users let any AI agent work threads, so resolution can route to our own or open-source models. Budget: Year 1 ~$200k, mostly Care. Year 2 ~$300k+ if teams beyond Care join (deck, key decisions slide).

---

## Appendix A1. Vendor landscape

Answers Milan: unclear axes, "enterprise focused isn't a reason to discount", flexibility was the first filter. Both axes are forms of flexibility, which matches slide 2.

```text
Role: Expert Google Slides designer.
Task: Create one slide placing support platform vendors on two axes.
Audience: VP Product, CPO, COO | Tone: direct, minimal
Slide title: "Only Plain is both customisable and open to any AI"
Layout: 4-Tile Matrix. 2x2 with labelled axes
Y axis: Customisation, low (UI config) to high (API-first, config as code)
X axis: AI openness, low (vendor AI only) to high (any AI agent)

Content:
- Top right (high, high): Plain | Shortlisted, winner
- Bottom right (low customisation, partly open AI): Intercom, Pylon | Shortlisted
- Top left (high customisation, vendor AI only): ServiceNow | Discounted
- Bottom left (low, low): Zendesk, Salesforce, Sprinklr, Freshservice | Discounted

- Footnote: Discounted on flexibility first, AI openness second

Constraints: Use only the text above, verbatim. Fragment grammar, no full sentences, no periods. Bold vendor names. Plain in the accent colour, discounted vendors in light grey. No added statistics, taglines, or intro/outro text. Visual: the 2x2 only
```

---

## Appendix A2. Build vs buy over time

Answers Milan: "how does this cost scale... proper ROI... at what point is that not the case, and at what point should you have started sooner". Also answers "100K is when for us?" and Hélder's parallel-running point. The "started sooner" answer reframes the question: we are starting now, on the part we own.

```text
Role: Expert Google Slides designer.
Task: Create one slide comparing cumulative build and buy cost for a support platform.
Audience: VP Product, CPO, COO | Tone: direct, minimal
Slide title: "Building the core costs $5.8M by 2030, buying $1.8M"
Layout: Single Chart + Callout. Chart on the left two-thirds, callout column on the right

Chart: line chart, cumulative cost in $M, 2027 to 2030
- Buy (Plain): 2027 0.2, 2028 0.6, 2029 1.1, 2030 1.8
- Build (incl. Zendesk in parallel): 2027 1.6, 2028 3.4, 2029 4.6, 2030 5.8
X axis: year. Y axis: cumulative cost, $M. Buy line in accent colour, Build in grey. Data labels at 2030 only

Callout (right column), header "When build wins":
- Crossover: ~720 seats, we model 400 in 2030
- Our 2030 peak: ~41k contacts a week
- Started sooner: we are, on the owned layer

Constraints: Use only the text above, verbatim. Fragment grammar, no full sentences, no periods. Max 8 words per item excluding lead-in. Bold lead-ins. No added statistics, taglines, or intro/outro text. Visual: the line chart only
```

**Speaker notes**: Build = 2-year build then run, $1.2M a year throughout [TBC: attribution], plus Zendesk seats and add-ons for 2027 ($398k) and 2028 ($584k). Plain costs $1,668 a seat a year (deck Appendix B), so its bill passes $1.2M at ~720 seats. In 2026 the Plain bill is ~$200k against a $1.2M team, so building earlier would have been worse. The part worth building, the owned connection layer, is being built now. Volume: 100k contacts a year is crossed in 2027 (160k). The 2030 peak is 2.15m a year, ~41k a week or ~5,900 a day. **Fix on the current slide**: "projected peak of 40k daily tickets in 2030" should read "~41k a week". The Uber/Meta threshold also needs consistent units [TBC: Uber's engineering blog describes hundreds of thousands a day, not a week].

---

## Appendix index

```text
Role: Expert Google Slides designer.
Task: Create one appendix index slide for a support platform recommendation.
Audience: VP Product, CPO, COO | Tone: direct, minimal
Slide title: "Appendix: the evidence behind each core slide"
Layout: 3-Card Grid. Equal cards, bold header, 3 fragments each

Content:
- Card 1 header: 1. Why we need control
  - Scale and AI: 30x+ volume, $20 human contacts
  - Today: constraints by criteria group, Fin exemption
  - Architecture: target design and principles
- Card 2 header: 2. How vendors scored
  - Landscape: customisation vs AI openness
  - Weights: three groups, flexibility 60%
  - Scores: detail, stress test, Intercom and Pylon
- Card 3 header: 3. Why Plain
  - Proof: experiences, POC, company, references
  - Trade-offs: known gaps, cost, build vs buy
  - Delivery: risks, migration plan, demos

- Footer: Anticipated questions at the end

Constraints: Use only the text above, verbatim. Fragment grammar, no full sentences, no periods. Max 8 words per item excluding lead-in. Bold lead-ins and card headers. No added statistics, taglines, or intro/outro text. Clean, minimal, consistent spacing. Visual: none
```

---

## Appendix 1.2. AI economics

Answers Milan: "not framing why AI is needed... the $20 per human contact is the problem, AI is still expensive". Ends on what it means for the vendor choice, which is what ties the slide to the recommendation.

```text
Role: Expert Google Slides designer.
Task: Create one slide on why support cost forces a shift to AI, and what that means for the platform.
Audience: VP Product, CPO, COO | Tone: direct, minimal
Slide title: "A $20 human contact doesn't scale to ~2m contacts"
Layout: Single Chart + Callout. Chart on the left two-thirds, callout column on the right

Chart: horizontal bar chart, total annual support cost in 2030 by AI resolution rate
- 60% AI resolution: $18M
- 70% AI resolution: $14M
- 80% AI resolution (target): $10M
X axis: annual cost, $M. 80% bar in accent colour, others grey. Data labels on bars

Callout (right column), header "What it means for the platform":
- Each AI point: ~$400k a year by 2030
- AI isn't free: ~$1 a contact, model choice matters
- So the core must: let us choose and change AI

Footnote: $20 per human contact, $1 per AI contact, ~2m contacts in 2030, Q1 2026 forecast

Constraints: Use only the text above, verbatim. Fragment grammar, no full sentences, no periods. Max 8 words per item excluding lead-in. Bold lead-ins. No added statistics, taglines, or intro/outro text. Visual: the bar chart only
```

---

## Appendix 1.3. Today's constraints by criteria group

Answers Milan: "sounds bad AI... your bottom blocks, if they were part of your scoring mechanism would be so much more powerful". Same blocks as the current add-ons slide, sorted under the three groups so they read as inputs to the scoring. Flexibility holds most of them, which supports its 60% weight.

```text
Role: Expert Google Slides designer.
Task: Create one slide mapping today's support platform constraints to the three scoring groups.
Audience: VP Product, CPO, COO | Tone: direct, minimal
Slide title: "Most of today's constraints are flexibility gaps"
Layout: 3-Card Grid. Equal cards, bold header with weight, 2-4 fragments each

Content:
- Card 1 header: Flexibility (60%)
  - Config: 500+ items, all manual UI changes
  - Change speed: 1-2 days simple, 2+ weeks complex
  - Integrations: Jira app deprecated, Salesforce via BigQuery workaround
  - AI: Fin on exemption, features behind AI add-ons
- Card 2 header: Experience (27%)
  - Agent context: customer data in sidebar apps
  - AI for agents: a side panel, not in the thread
- Card 3 header: Partner and cost (13%)
  - Bolt-ons: $130k a year (Salto, SweetHawk, sandbox)
  - Roadmap: black box, focused on its own AI
  - Feature requests: minimal visibility or feedback

Constraints: Use only the text above, verbatim. Fragment grammar, no full sentences, no periods. Max 8 words per item excluding lead-in. Bold lead-ins and card headers. Card 1 visibly the largest, in the accent colour. No added statistics, taglines, or intro/outro text. Visual: none
```

**Source note**: "AI for agents: a side panel" comes from `04-active-work/meeting-notes/2026-09/2026-09-15-plain-vision-architecture.md`. "Customer data in sidebar apps" is the inverse of the deck's Plain claim ("eliminating sidebar apps"). Everything else is from the current deck slide.

---

## Appendix 2.2. How we weighted

Answers the four weighting comments (AI 15%, config as code 10%, customer experience 7%, and Hélder's reliability 10%) by showing the groups behind the weights.

```text
Role: Expert Google Slides designer.
Task: Create one slide explaining the vendor scoring weights.
Audience: VP Product, CPO, COO | Tone: direct, minimal
Slide title: "Flexibility carries 60% because it drives everything else"
Layout: 3-Card Grid. Equal-height cards, card width proportional to group weight. One-line subtitle under the title. Footnote

Content:
- Subtitle: Weights set by impact on the outcome, before scoring

- Card 1 header: Flexibility (60%)
  - Channels, data model, routing: 20%
  - Integration ease: 15%
  - AI compatibility: 15%
  - Config as code: 10%
- Card 2 header: Experience (27%)
  - Agent experience: 20%
  - Customer-facing portals: 7%
- Card 3 header: Partner and cost (13%)
  - Partnership and reliability: 10%
  - Pricing and terms: 3%

- Footnote: Scored 0 to 3 from the POC, demos, vendor docs and reference calls. Customer-facing scores native portals only, which we build ourselves

Constraints: Use only the text above, verbatim. Fragment grammar, no full sentences, no periods. Max 8 words per item excluding lead-in. Bold lead-ins and card headers. Card 1 in the accent colour. No added statistics, taglines, or intro/outro text. Visual: none
```

**Speaker notes (Hélder, reliability at 10%)**: partnership scores how well a claim is verified, so Plain's funding claim scores 1 until investors confirm it. Vendor continuity is handled as a flagged risk with investor diligence before signing. Raise partnership and reliability to 15% and Plain still leads, 2.48 vs 1.84 (stress test, slide 2 notes).

---

## Appendix 4. Anticipated questions

Milan's and Hélder's comments preview the room's questions. "When do we hit 100k?" is answered on slide 3.7 (build vs buy) and in its notes.

```text
Role: Expert Google Slides designer.
Task: Create one slide answering the four questions a support platform decision raises.
Audience: VP Product, CPO, COO | Tone: direct, minimal
Slide title: "The four questions this decision raises, answered"
Layout: 4-Tile Matrix. 2x2, tile header is the question, 1 fragment answer each

Content:
- Tile 1 header: Customer experience only 7%?
  - Answer: portals only, we build those ourselves
- Tile 2 header: Our own AI models?
  - Answer: yes, Plain machine users run any agent
- Tile 3 header: What if Plain fails?
  - Answer: runway to 2028, diligence first, owned layer eases exit
- Tile 4 header: Why not build?
  - Answer: $5.8M vs $1.8M to 2030, crossover ~720 seats

Constraints: Use only the text above, verbatim. Fragment grammar, no full sentences, no periods. Max 8 words per item excluding lead-in. Bold tile headers. No added statistics, taglines, or intro/outro text. Clean, minimal, consistent spacing. Visual: none
```

---

## Open items

- [TBC] Decision date in Q4 (core slide 3, tile 4)
- [TBC] $1.2M a year build cost: cite as Milan's estimate, or Finance to confirm (A2)
- [TBC] Uber/Meta threshold units, day vs week (A2 speaker notes)
- [TBC] ServiceNow placement in the top-left quadrant (A1): the original slide doesn't make its customisation level clear
- [TBC] Intercom acquisition wording (Appendix 2.4): the deck says Salesforce "acquired" Intercom. Earlier notes say the deal was signed 15 June 2026 and closes October 2026 to January 2027. Check whether it has closed
- [TBC] Appendix 1.2 says "$1 per AI contact" while Fin's benchmark is $0.90 per resolution. Fine as a rounded figure, but say "~$1" if challenged
