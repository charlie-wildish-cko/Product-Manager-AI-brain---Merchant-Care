# Meetup Talk: Reflex — AI-Powered Support Insights — 5 Slide Outline

10 minutes. ~2 min/slide. Single topic: Reflex, why AI makes it possible, live demo.

---

## Slide 1 — "Support Tickets Are a Signal Nobody Reads at Scale"

**Concept:** Open on the problem, stated as a single sharp insight. No AI mentioned yet — let the pain land before the fix.

**Talking point (from `01-knowledge-base/products/reflex.md`):**
- No direct line from merchants to the PMs whose products cause the contact — the signal is buried in ticket queues PMs never read
- No accountability — product teams aren't measured on the contacts their features generate, so support data isn't a prioritisation input
- Qualitative (why merchants are upset) and quantitative (what they contact about) data never get joined — Zendesk tells you *what*, NPS tells you *how they feel*, and today that join doesn't exist at scale

**One line, stated plainly:** "A human agent contact costs ~$40. Eliminating the reason for it costs $0. That gap is the business case."

**Audience interaction:** Open with a hands-up question before the talking points above, so the room is primed for the problem rather than told it cold.
- Hands-up prompt: "Hands up — who here has personally read a customer support ticket in the last month?" (pause, gauge the room — expect very few hands, that's the point)
- Or, if Slido/Mentimeter is set up for the event: poll question "How does your product team currently learn about issues customers are contacting support about?" with options like *Dashboards/reports* · *Someone forwards me examples* · *I don't have visibility* · *Other* — display live results for 15-20 seconds before moving on
- Use whichever the room supports — hands-up needs zero setup and works in any room size; Slido needs the event's poll infra confirmed in advance

**Speaker note:** This is the only pure-problem slide. Don't rush it — the rest of the talk only lands if the audience feels this first. Budget an extra ~30-45 seconds for the interaction itself (see updated timing guide).

---

## Slide 2 — "AI Turns Ticket Noise Into a Ranked, Attributable Fix List"

**Concept:** The "why AI, why now" — this is the Promise beat. AI is what makes reading every ticket, at scale, possible for the first time.

**Talking point:**
- Before: thousands of unstructured tickets a quarter, no human team has time to read them all
- The AI enrichment layer (Reflex's "whale"): per-ticket root cause summary → theme aggregation → product team mapping, at a volume no human team could match
- The result isn't a bigger dashboard of raw counts — it's a ranked list of contact drivers by cost and volume, each attributable to a specific product team

**Speaker note:** This is the pivot slide — problem to mechanism. Keep it to the one idea: AI is the only way to read *everything*, not a sample.

---

## Slide 3 — "One Path From Raw Tickets to a Prioritised Fix"

**Concept:** Make the mechanism concrete by walking the actual PM journey through the product, step by step — this is the Proof beat before the live demo.

**Visual:** Five-step horizontal flow, from `reflex.md`:
1. **Filter** — scope to your product area and time period
2. **Overview** — biggest issue clusters, ranked by business impact
3. **Select a cluster** — drill into the themes within it
4. **Investigate a theme** — individual contacts: summaries, examples, underlying conversations
5. **Deep dive** — granular sub-clusters, synthesised view of what merchants are experiencing

**Talking point:** "This is the same five steps every time, for any product, any quarter — filter, see what's biggest, drill in, read the actual merchant voice, go as deep as you need. That's what I'm about to show you."

**Speaker note:** Don't demo all five steps live — this slide sets up the map, the demo shows the walk.

---

## Slide 4 — Live Demo

**Concept:** Show, don't describe. Walk one real path through the product.

**Demo (pre-loaded, not live-typed):** Filter → Overview → Select a cluster → Investigate a theme. Stop there — only go to the sub-cluster deep dive if time is in hand.

**Fallback:** Pre-recorded screen capture of the same path, ready to play if the live environment misbehaves.

**Speaker note:** This is the slide with the least script and the most risk — rehearse the click path at least twice beforehand so narration doesn't outrun the screen.

---

## Slide 5 — "What's Planned for Reflex" (Closing Slide)

**Concept:** Close on where this goes — the Proposal beat. A clean bullet list of what's next, then one forward-looking line. End on the vision, not a metrics recap.

**What's planned (bullet points for the slide):**
- **Now — Q1 2026:** BQ data foundation + per-ticket LLM root cause summaries
- **Q2 2026:** Theme aggregation + product team mapping + self-serve Insights Query Interface
- **Q3 2026:** Reflex MCP — programmatic API so other teams and tools can query insights directly
- **Q4 2026:** Voice-of-Customer correlation, spike detection, governance automation
- **Q4 2026 / Q1 2027 (TBC):** Jira integration — auto-creates stack-ranked contact drivers as Jira issues, pre-populated with volume, cost, trend, and example tickets
- **2030 vision:** Reflex works like Stripe's internal coding agents ("Minions") — surfacing not just the problem but a drafted action plan (and potentially a fix PR), for a human to review and ship

**Close line:** "Every fix compounds across every future transaction. That's why this is worth building."

**Speaker note:** Protect the close line above all else if you're cut short — it's the takeaway the audience should leave with. Keep the bullets on screen as a leave-behind while you say the close line; don't read every bullet aloud verbatim.

---

## Timing Guide (10 min)
| Slide | Time | Cut first if short |
|---|---|---|
| 1 (incl. audience interaction) | 2.5 min | shorten hands-up pause; skip Slido if room isn't set up |
| 2 | 1.5 min | — |
| 3 | 1 min | shorten to 3 steps (Filter → Overview → Investigate) |
| 4 | 3.5 min | shorten demo path, keep the "investigate a theme" step |
| 5 | 1.5 min | drop roadmap bullets to headline phases only, keep close line |

## Pre-talk checklist
- [ ] Demo pre-loaded and screen-recorded as backup (live demos fail; see `presentation-best-practices.md` delivery tips)
- [ ] Practice out loud once with a timer before the talk
- [ ] Confirm the $40/contact and north-star metric figures are current before presenting
