# AI Assistant and Fin Alignment

**Date:** 2026-09-15
**Attendees:** Veronika Galkina, Andrew Stager, Charlie Wildish, Joseph El Choueiri, Gbemi Abijo, Aman Khare
**Drive source:** 1EtCokyrm5cNOUtXAbo-lSgOPeZ_aPTq8mDgIdeI2QTQ

## Context

Resolving Charlie's objection to two competing AI assistants in the Dashboard: Fin plus the new analytics assistant.

## Key Points

- Gbemi framed the problem: Fin already does most of what the planned dashboard agent would do, minus analytics. She floated the inverse: make Fin the dashboard assistant with orchestration handovers, since building a Fin equivalent in-house would take substantial time and effort.
- Charlie's position: the ideal is a Checkout-owned, vendor-independent AI experience. He is not attached to Fin specifically ("Fin is a vendor, they're all kind of the same"), but does not want to be tied to a vendor solving Checkout's problems long-term.
- Charlie's diagnostic frame: split Fin conversations into support and non-support. Non-support usage (acceptance rate, auth rate queries) is a **feature gap in the Dashboard**, not a support need, and should be solved elsewhere. Andrew has already bucketed Fin conversations this way ("what is the status of X", "why did this happen to me", "how do I do this"), and most need no human.
- Volume reality check: acceptance-rate queries are ~1% of volume, payments ~60%. Fin's dashboard traffic is mostly payment and transaction lookups from operational users, not payment-performance analysts. Andrew confirmed Fin handles payment ID lookups at meaningful volume.
- **Key technical unlock: Fin has an unused API product.** Checkout uses the Intercom widget only for ease of integration, not by decision. Fin can be hidden under the hood and invoked from Checkout's own UI, with orchestration deciding which agent answers. Charlie has asked the Fin solution engineer for recommendations. Caveats: capacity for his team, and response-tone consistency across agents.
- Prioritisation constraint (Aman): capability depends on which MCPs exist. Disputes is building one, fraud may build its own. Day-zero capability will be limited, hence the launch-anyway-or-pause question.
- Consistency risk: the Checkout MCP and Fin draw on the same underlying sources with different nuances, so they can return different answers to the same question.
- Branding: Veronika proposed visually distinguishing Fin (question-mark icon, support framing) from the in-house analytical assistant. Charlie is indifferent to the icon but insists on extreme clarity, visual and textual: the analytics sidebar is called "analytics assistant", never "AI assistant".
- On Fin answering analytics questions later: technically possible via MCP, but Charlie prefers an in-house fine-tuned model from Joseph's team for better quality and lower cost.
- Andrew asked for a clear roadmap delineation of what is designed and delivered now against later. Each meeting keeps adding decision layers.

## Decisions

- Q4 short term: release the side-drawer experience for the analytics assistant only, confined to analytics pages. No homepage change. Develops into a full sidenav next year.
- Present the north-star concept to Mark at crit as a **single consolidated assistant with Fin operating behind the scenes**: the support agent still exists, the experience is unified.
- Three-tier phasing: (1) short term, redesign the analytics-page side drawer; (2) mid term, homepage entry point wired only to the analytics assistant, no MCPs; (3) long term, full orchestration.
- Open: v1/MVP scope and whether Fin integration lands in the first version. Aman owns the MVP definition with Jalian, due end of the following week. The 23 September sign-off date is optimistic and can slip 1-2 weeks.

## Insights

- The Fin API product is the lever that makes vendor abstraction possible without a rebuild. It is the mechanism for swapping the vendor with zero customer impact.
- Fin's dashboard usage works as a product-gap detector: non-support questions Fin happens to answer are unmet Dashboard needs, and that classification should drive where AI capability gets built.
- The real unresolved risk is not UI coexistence but **answer divergence** between the Checkout MCP and Fin over shared data sources.
- The hard question is not the north star (single assistant, Fin hidden) but how Fin and the analytics assistant coexist in the interim.
