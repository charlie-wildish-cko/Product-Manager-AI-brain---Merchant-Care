# Support Platform Recommendation: Replace Zendesk with Plain

**Audience**: CPO / COO
**Owner**: Charlie Wildish
**Status**: Content draft. `[X]` / `[Y]` markers are real gaps to fill, not estimates.
**Sources**: `01-knowledge-base/metrics/contact forecasting.md` · `04-active-work/research/zendesk-platform-decision-rfc.md` · `04-active-work/meeting-notes/2026-08/2026-08-20-fin-in-plain-world.md` · `04-active-work/meeting-notes/2026-08/2026-08-05-checkout-plain-workshop.md` · `2026 deliverables.md` (line 425)

---

## 1. Title

**Support Platform Recommendation: Plain**

Subtitle: Replacing Zendesk before the June 2027 renewal, to support 2M contacts a year and an AI architecture we control.

Consider adding a single recommendation line here. A CPO/COO reads better when they know the destination before the argument. The agreed order still holds: full recommendation lands at section 9.

---

## 2. The Scale Problem

**Action title**: Contact volume grows 36x by 2030. The current platform is priced and built for the volume we have now.

| Metric | 2026 | 2030 | Change |
|---|---|---|---|
| **Total contacts** | 60,049 | 2,154,799 | **36x** |
| **B2B contacts** | 60,049 | 445,999 | **7.4x** |
| **B2C contacts** | 0 | 1,708,800 | **79% of 2030 volume, from zero** |
| **Segments served** | 1 (Enterprise) | 4 (Enterprise, Platforms ISV, Platforms SMB, Consumer) | **4x** |

**Number discrepancy to resolve before this goes out**: your notes say 40k to 1-2M. `contact forecasting.md` says 60,049 to 2,154,799. Pick one and use it everywhere. If 40k is the trailing actual rather than the 2026 forecast, say so on the slide, because a CPO will know the current run rate.

### Cost of inaction

**Every percentage point of AI resolution rate is worth $842k a year at 2030 volume.**

1% of 2,154,799 contacts is 21,548 contacts. Fin resolves at $0.90; a human agent costs ~$40. The difference is $39.10 per contact, so 21,548 x $39.10 = $842,527 per point per year.

| AI resolution rate | Human contacts | Total annual cost |
|---|---|---|
| 60% | 861,920 | **$35.6M** |
| 70% | 646,440 | **$27.2M** |
| 80% (strategy target) | 430,960 | **$18.8M** |

A platform that caps AI resolution 10 points below target costs **$8.4M a year by 2030**. That is the cost of inaction, and it is an order of magnitude larger than any licence or migration cost in this deck.

---

## 3. Two Drivers

**Action title**: Two things force a decision now, and only one of them is scale.

**Driver 1: Scale.** 36x contact growth, four segments instead of one, and a consumer business that does not exist on the platform today. This needs high-performance systems and AI agents embedded across the contact lifecycle, not bolted to the side of a ticketing tool.

**Driver 2: Zendesk is strategically closing off third-party AI, and Fin is the named casualty.** This has already been discussed with and is aligned by the CPO and COO — it does not need to be re-argued in the room, only stated and evidenced.

The documented piece: Zendesk's Chief Customer Officer emailed us on 1 April 2026 confirming Zendesk "made the decision to stop partnering with Intercom / Fin going forward." New Fin-on-Zendesk integrations are blocked outright; our existing one is exempted, but only "upon request if ever you need to install a new instance," and Zendesk's stated reason is a breakdown of trust: "the developer declined Zendesk's requests, or we otherwise lost trust in the partnership." Source: `04-active-work/research/evidence/2026-04-01-zendesk-notice-intercom-integration-partnership-ended.pdf`.

The corroborating piece, from the other side of the relationship: Fin confirmed independently, before the Zendesk notice, that it will not keep enhancing the Zendesk integration. In the 11 June 2026 Intercom renewal meeting, Rob King (Fin/Intercom AE) told us "Fin has made a decision to stop supporting the Zendesk integration for new customers" and that Intercom's engineering team is in "lights on" mode on it, deprioritising feature development. Concrete example given: Fin sandbox-to-production linking, already shipped on the Salesforce version, is blocked for Zendesk customers. Source: `04-active-work/meeting-notes/2026-06/2026-06-11-intercom-renewal.md`.

This means both vendors independently confirm the same dead end from opposite sides: Zendesk will not let new Fin integrations in, and Fin will not invest further in the integration it still has. Checkout's own procurement already treated this as material risk, not a hypothetical: the June renewal added a termination clause letting Checkout exit without liability "if the Zendesk integration is turned off or becomes unusable." That clause exists because our own legal and procurement team assessed this as a live risk three months before the Zendesk notice arrived.

The judgment beyond these two data points, already shared with CPO/COO: we read this as one visible instance of a broader strategic move by Zendesk, not an isolated integration dispute, and we do not trust Zendesk to keep honouring the existing-integration exemption indefinitely. Zendesk's own commercial incentive supports that judgment: it acquired Forethought in March 2026 and is terminating legacy AI Agents and bot builder functionality in December 2026 to force customers onto its own generative AI stack (source: `05-archive/2026/investigations/Zendesk Viability_ AI, Pricing, Market.md`). A vendor consolidating its AI ecosystem has a standing reason to narrow or revoke a competitor's exemption over time. State the two documented facts plainly, and label "this is strategic, and the exemption will not hold" as our assessment, not as something either vendor has said outright.

Fin is our entire AI resolution layer. On Zendesk, our ability to keep using it is a discretionary exemption held by a vendor actively trying to replace it, on an integration the AI vendor itself has stopped investing in. Section 2 prices what losing that ceiling costs.

**This is also the documented precedent for section 8.** The Intercom risk case there references "reassurance that broke down last year." This April notice is that breakdown, dated and in writing, not a recollection.

---

## 4. Current State Pain, Quantified

**Action title**: We are already paying for the gap between what we need and what Zendesk does.

| Pain | Today | 2030 | Note |
|---|---|---|---|
| **Config elements** | `[X]` | `[Y]` | Source: Salto IaC repo, per `zendesk-current-config-flow-map.md` |
| **Pick-up to deployment** | `[X]` days | Unchanged without config-as-code | Zendesk supports manual configuration only |
| **Workarounds built to bridge Zendesk's limits** | `[X]` | Multiplies per segment | Agent Consultant is the largest: it exists outside native Zendesk because Zendesk cannot execute agent-triggered actions |
| **Paid add-ons for baseline function** | Sandbox/prod deployment, core apps | Advanced AI $50/agent/mo · QA $35/agent/mo · WFM $25/agent/mo | Governance tooling more than doubles base licence cost |

The pattern: every capability we need beyond ticketing is either an add-on we buy or a workaround we build and then maintain. Both scale with segments, and we own the maintenance cost permanently.

---

## 5. Architecture Vision

**Action title**: Own the layer that makes vendors swappable.

Agreed in the 2026-08-20 architecture session:

- **Abstract data models away from vendors.** One controlled chain: customer identity, routing, AI invocation, data processing, then Reflex. Vendor field requirements do not get baked into our services.
- **AI agents embedded wherever the workflow needs them.** Customer AI handles first contact and hands off to a human or to internal AI when unresolved, with context intact.
- **We control the customer data inputs.** Enrichment and identity are ours, not the platform's fixed schema.
- **Integrations abstracted from vendors.** A gateway service listens to Fin events and creates matching Plain threads, so data stays consistent across channels and survives a vendor change.
- **Config-as-code, AI-assisted deployment.** Centralised taxonomy and attribute sync that auto-propagates to Fin with no redeploy. Zendesk supports manual configuration only, with no AI-assisted deployment path.
- **Hybrid buy/build.** Plain plus Fin for the next year, with a build-in-house bias.

The strategic point for this audience: Fin is itself a constraint. Building the abstraction is what lets us swap any vendor in this stack, including Fin, without another migration. That is the difference between this being the last platform decision of the decade and the first of three.

---

## 6. Vendors Considered

**Action title**: Most of the market is structurally disqualified, not competitively outscored.

**Discounted on structure: Zendesk, Sprinklr, Salesforce, Freshdesk.** All four want end-to-end control of the stack and monetise their own AI. Buying any of them means accepting a vendor-set ceiling on our AI layer, which is the problem we are solving. This is a structural conflict, not a feature gap, so no amount of scoring changes it.

**Discounted on fit: ServiceNow, HubSpot, Jira.** Not built for high-volume multi-segment customer support.

**Shortlisted: Plain, Intercom, Pylon.** All three permit an external AI layer, which is the entry condition.

**Standing vendor rule applied throughout**: avoid tools owned by large conglomerates, because absorption forces a future migration. This rule is why the shortlist looks the way it does, and it is worth stating explicitly to this audience since it also explains section 8.

**Presentation note**: the weighted scorecard in `support-platform-vendor-scorecard.md` is still unpopulated. The recommendation rests on the Plain POC, the August workshop, and the structural logic above, which is defensible for a CPO/COO. Do not claim a scored 11-category evaluation on the slide, because the instrument is empty and someone may ask to see it.

---

## 7. Vendor Landscape Chart

**Action title**: Only one shortlisted vendor is both lean enough to embed and open enough to run our AI.

Chart spec for Gemini:

- **X-axis**: Fit for use case. Left = Enterprise / complex. Right = Lean / embeddable.
- **Y-axis**: AI embedding flexibility. Bottom = Vendor's own AI only. Top = Bring your own AI.

| Quadrant | Label | Occupants |
|---|---|---|
| Bottom-left | **Closed suites**: buy the whole stack, use their AI | Zendesk, Salesforce, Freshdesk, Sprinklr, ServiceNow (tight cluster) |
| Bottom-right | **Lean but locked**: light footprint, still their AI | empty |
| Top-left | **Open but heavy**: flexible AI, enterprise weight | empty |
| Top-right | **Headless and AI-agnostic**: our target | **Plain** (isolated) |

Intercom and Pylon sit mid-right, between quadrants: open enough on AI, not structurally headless.

Label the quadrants, not just the axes. The chart has to make the section 8 argument before it is spoken.

---

## 8. Why Not Intercom, Why Not Pylon

**Action title**: Both shortlisted alternatives fail on architecture before they fail on anything else.

**Intercom.** Excellent at support, poor at integrating outside its own ecosystem. Our architecture depends on abstracting integrations away from any single vendor, and Intercom's model pulls the opposite way. Second, the Salesforce deal: Salesforce signed a definitive agreement on 15 June 2026 to acquire Intercom, renamed Fin the prior month, for $3.6bn. Not yet closed. Expected close is Salesforce's fiscal Q4 2027, roughly October 2026 to January 2027, pending regulatory clearance (source: Salesforce press release, 15 June 2026). That close window lands inside this decision's own timeline, which is the point to make to a CPO/COO: this is not a distant hypothetical, it is a live acquisition closing within one to four months of this pitch. It triggers our standing rule on conglomerate acquisition regardless of the platform decision, since we retain Fin as the AI layer either way. The precedent for treating this as real risk, not speculation, is documented: both the Zendesk CCO's 1 April 2026 email and Fin's own AE in the 11 June 2026 renewal meeting confirm the Zendesk integration is a dead end from each side (section 3, both sources cited there). The judgment here is that Intercom/Fin is not the case platform, not that Fin is wrong as the AI layer.

**Pylon.** Strong on B2B and agentic use cases. Built for large, complex enterprise setups, which is the wrong shape for an embeddable layer. No config-as-code, manual deployment only, which fails the deployment velocity requirement in section 5 outright.

---

## 9. Recommendation: Plain

**Action title**: Plain is the only shortlisted vendor that is headless, API-first, and config-as-code.

**Structural fit:**

1. **Config-as-code.** The only shortlisted vendor that has it. This is what turns four-segment configuration from hand-built work into deployment, and it is the direct answer to the `[X]`-day pick-up-to-deployment number in section 4.
2. **Fully headless and API-first.** Plain is a platform we compose, not a suite we adopt. This is what makes the section 5 abstraction possible.
3. **No AI of its own to defend.** Plain has no commercial reason to cap our AI layer, which is precisely where Zendesk now conflicts with us.
4. **Flexible data model.** Custom objects and fields sufficient to model our org hierarchy and Platform merchant relationships, rather than a fixed schema we integrate around.

**Then, commercial and relationship factors:**

5. **Partnership access.** Direct access to C-level, head of product, and head of engineering. Material for a platform we are composing rather than configuring, because roadmap influence is part of what we are buying.
6. **Funding runway confirmed through `[X]`.** Vendor continuity is a real risk on a smaller vendor and it needs stating plainly rather than omitted.

**The honest risk to state on this slide**: Plain is the smallest vendor on the shortlist and several capabilities were committed rather than demonstrated at the August workshop. Name the mitigation, which is that Ray is the validation deployment before any B2B migration commitment. That is the plan in section 11, and stating the risk first makes the plan land as risk management rather than optimism.

---

## 10. Cost

**Action title**: Cost is a gate, not the reason to move.

| Line | Amount |
|---|---|
| **Zendesk today** | `[X]` |
| **Plain quote, undiscounted, including AI credits** | `[Y]` |
| **Difference** | Roughly equivalent |

State the two real numbers before the conclusion, so "roughly equivalent" reads as a finding rather than a claim.

The cost argument that matters is in section 2, not here. Licence cost is roughly equivalent; the AI resolution ceiling is worth $8.4M a year at 10 points. Say that explicitly, because a CPO/COO will otherwise assume a platform migration is being justified on licence savings and price the migration against the wrong number.

Add-on note for the comparison: Zendesk's governance tooling is separately priced at $50/agent/month Advanced AI, $35 QA, $25 WFM. Confirm which of these are in the current contract before quoting `[X]`.

---

## 11. Plan

**Action title**: Ray proves Plain before any B2B migration commitment.

| Phase | When | Scope |
|---|---|---|
| **Internal alpha** | December 2026 | Ray consumer support, 50-100 friends and family users. Deliberately not the full architecture: a pass-through web form with taxonomy and a few fields. Not on Zendesk. |
| **Full build, external launch** | Q1 2027 | Ray external beta on Plain with the full architecture |
| **B2B migration decision** | Post-Ray, before June 2027 renewal | Informed by a live deployment rather than a POC |

Ray is the first Care deployment with no Zendesk, which makes it the validation ground for Plain at real, if small, volume. Zendesk-first for Ray was dropped specifically to avoid building on a stack Care migrates off (source: `2026 deliverables.md` line 425).

Sequencing point worth making to this audience: this plan de-risks the platform decision at consumer scale before betting the B2B operation on it, and it does so on a timeline that still clears the June 2027 renewal.

---

## 12. Ask

**Action title**: [Set once the ask is chosen]

Your notes flag this as undefined. The blocker is already documented: Fraser's dependency is that the Plain roadmap and estimates cannot be produced until the architecture vision is signed off by business and ops. The outstanding gate on the build is estimates, roadmap, and business sign-off, and that is itself blocked on architecture sign-off (`2026 deliverables.md` line 425, `2026-08-20-fin-in-plain-world.md`).

Three candidate asks, ranked:

**1. Recommended: approve the decoupled Fin/Plain architecture direction, so engineering can produce estimates and a roadmap.** This is the actual blocker, it is specific, it is cheap to say yes to, and it unblocks everything downstream. Frame it as approving a direction, not a contract.

**2. Approve Plain as the platform for Ray consumer support, December alpha and Q1 2027 external launch.** Largely already the plan, so this converts an operating assumption into a decision with executive backing.

**3. Approve entering commercial negotiation with Plain ahead of the June 2027 Zendesk renewal.** The heaviest ask. Hold this one unless you want the renewal decision settled in the same meeting.

Ask 1 plus ask 2 is the strongest combination: it clears the engineering blocker and confirms the validation path without asking for a B2B migration commitment the Ray alpha has not yet earned.

Whichever you pick, name the owner and the date on the slide. Decision model is consultative consensus, so name who signs: VP of Product, Director of Operations, Director of Operations Excellence, plus this CPO/COO audience for the architecture direction.

---

## Open items before this is presentable

1. ~~Driver 2 evidence.~~ Closed: 1 April 2026 email from Zendesk's CCO, saved at `04-active-work/research/evidence/2026-04-01-zendesk-notice-intercom-integration-partnership-ended.pdf`. Note the precise scope when presenting: new Fin integrations blocked, existing one exempted on request, framed by Zendesk as a partner-trust breakdown, not a blanket "no third-party AI" policy.
2. **Section 4 measurements.** Config element count, pick-up-to-deployment days, workaround count. All available from the Salto repo and the admin queue.
3. **Section 10 numbers.** Current Zendesk cost including which add-ons are contracted, and the Plain quote.
4. **Plain funding runway** date.
5. **Ask selected**, with owner and date.
