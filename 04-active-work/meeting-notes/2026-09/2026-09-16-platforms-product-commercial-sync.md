# Product / Commercial Sync: Platforms

**Date:** 2026-09-16
**Attendees:** ~50 invitees across commercial and product. Milan Jani presenting, Nicolas Maalouf chairing, plus Chirag Thakrar, Maimona Haj Abdullah, Andrey Klochkov, Bilal Malida, Imane Rahmoun Begbeg, Charlie Wildish, AM/revenue/SE/pod leads. Oliver Westlake-Simm declined.
**Drive source:** 1Tz8u95pLEzfoEd98Z24CuMd7Cg7PW-D4OHeWWaEKiGA

## Context

Commercial briefing on the Platforms product line now that ISV is live. Charlie attended as Care.

## Key Points

**ISV is live**

- First ISV product went live ~3-4 weeks ago. Customers began onboarding sellers ~2 weeks ago. **~30K volume processed so far.**
- ISV model: direct seller relationship where the parent takes a commission.
- Three platform flavours: marketplace, pay, ISV. Long-term goal is to retire "IP" terminology and consolidate everything under "platforms". IP has no hard shutdown date, but new customers will be steered off it with incentives such as APM access. Hybrid/cross-region naming unresolved.
- Geography: goal is one unified global platform. Saudi Arabia likely needs a separate build. UAE support and Saudi split payments raised as gaps.

**Onboarding**

- Instant onboarding via third-party system connections automates checks and also benefits legacy IP customers.
- Progressive onboarding (transact before withdrawal permissions) will be an **optional toggle**, because large platforms like Sunday want to avoid it to protect their own merchant proposition.
- Roughly **13 automated verification steps** per seller and UBO (KYC, KYB, business verification), designed to run end-to-end without human intervention. High-risk submissions still trigger manual review.

**Seller experience**

- No third-party dashboard: sellers get transparency and updates via API and webhooks.
- Debate on whether end-sellers should get direct Checkout dashboard access, since that conflicts with the white-label nature of FCA-compliant and ISV products.
- API-first, with embedded components (inline help, localised field formatting) coming, then co-branded or white-label payment pages.

**Money movement and pricing**

- Funds on a negotiated T+X schedule inherited from the platform, landing on accounts with on-demand withdrawal, with a minimum balance requirement to cover refunds for smaller sellers.
- IC++ buy rates to parents, who can resell blended or IC++. Multiple seller pricing profiles and tiered pricing supported.
- Sweet spot: scaled businesses with ~30,000 existing customers and multi-billion volumes. Smaller platforms accommodated.

**Care model**

- ISVs must front customer care. Checkout stays behind the scenes. Standard VAS included: vault, intelligent acceptance, tokenization.
- **The two Gemini renderings conflict:** the quick notes record "ISV partners will front customer care and handle 90% of contact volume"; the detailed notes record Milan saying ISVs handle "approximately 25 percent of inquiries regarding fund status and failed payments". Verify with Milan before citing either.

**Compliance**

- Chirag Thakrar: applying enterprise-grade ongoing submerchant compliance review cycles to tens of thousands of sellers is unsustainable.
- Response: default policies set the schedule, but cycles can be adjusted or automated by risk profile once migrated to the **ARC** risk and compliance framework.

**Payment splitting and APMs**

- ISV transactions are direct purchases, not multi-entity basket splitting. Migrating merchants from IP Light to ISV will be hard because of KYB/KYC requirements. Remember Me and the payment flow will be supported.
- APMs supported only where they can be added and managed at scale by partners. In progress: PayPal, Klarna, UK open banking, Benelux and German bank methods. Niche/unsupported APMs excluded on resource grounds. UAE/MENA teams flagged Tabby and Tamara as critical gaps. Parents control checkout display and display logic.

## Decisions

- **Net settlement is the default**, not gross settlement.
- Submerchant ongoing compliance review frequency deferred, needs the compliance team.

## Roadmap dates stated

| Item | Date |
|---|---|
| European ISV solution | Q1 |
| UK marketplace solution | Summer / start of H2 |
| PSD3 compliance solution | End of this year |
| Scaled UAE platform | End of Q3 |
| ARC risk/compliance framework global rollout | Complete by summer next year (prerequisite for global rollout) |

## Insights

- ISV is live and generating real volume, so the Care model is not hypothetical. The ISV-fronts-care assumption is the load-bearing premise behind Platform Embedded AI, and contact-rate forecasts for Platforms ISV depend on which figure is right (90% handled by ISV, or ISV handling only fund-status/failed-payment queries at ~25%).
- ARC rollout completing summer 2027 gates the global platform rollout, and by extension the pace of Platform contact growth.
- Sellers get no dashboard, only API and webhooks. Any Care self-service proposition for Platform merchants has to be delivered through the ISV's own surface, not Checkout's.
- Compliance review cadence for tens of thousands of submerchants is unresolved and is a plausible future contact driver.
