# Project Ray: Blockchain Infrastructure and Consumer Care

**Date:** 2026-08-18
**Attendees:** Ben Leah, Sarah Edmonds, Joel Petrosino, Oliver Westlake-Simm, Max Rothman, Mana Majboor, Charlie Wildish, Brian Weir, Joe Foulds, Helder Goncalves
**Drive source:** 1NFV1SB9qCKDBoXJAEInqnKVf8zYNfyoobxf9iHslD4Y

## Context

Scoping how Care supports Ray, the non-custodial stablecoin wallet, held the same day Braavos was paused. Note: Gemini transcribed several year references as 2025; the relative sequence is sound but the years are unreliable.

## Key Points

- Product scope: Ray shares 60-70% of functionality with Braavos. First six months limited to onboarding, KYC, deposit, send and card transactions. No full trading app.
- Divergence is exactly where Care is hardest. "Where's my money" means something entirely different on-chain versus card rails. Card-side flows (lost or stolen card, verification failure, lockout, unrecognised transaction) are near-identical to Braavos and reusable.
- Non-custodial changes the support model. Max's position: because funds are non-custodial, troubleshooting can be pushed to the user by pointing them at on-chain data. Brian Weir and Charlie noted the flip side: Checkout has far less visibility than in the fiat and acquiring world, and there are no SOPs, Looker queries or APIs for these flows yet.
- Charlie set the sequencing: the taxonomy is the design input for everything downstream. Draft the top 10-20 query types, tag each self-serve or not, and the self-serve share gives a defensible AI resolution target. Max Rothman to add blockchain-specific scenarios to the Braavos base.
- Hard scenarios raised: funds visible on-chain but not reflected in the wallet (could be a technical incident rather than a Care query), top-ups screened or held by compliance review, AML alerts on the blockchain side. AML tipping-off rules still apply, so responses stay generic. Proposed handling for a blockchain-side alert: display the balance as normal, suspend the card and payout ability, let the user export their keys.
- Consumer fraud sits with Fabio's team, structurally separate from merchant Care and disputes, on conflict-of-interest grounds: the same disputes team cannot represent the merchant against the consumer and the consumer against the merchant.
- Staffing model: AI first, then a small internal team purely to build content and playbooks, then BPO for scale, then hybrid (Malaysia for Care, Mauritius for fraud). Ray markets include UAE and the Philippines; 24/7 native-language coverage would need a floor of 4-10 people, so AI translation is the interim answer.
- AI resolution target: 60% by Fin. Fin costs 99 cents per resolution and is already in the consumer business cost model. Fin has been live over a year but never in a consumer context. The only net-new engineering is wrapping the Fin web SDK for mobile plus content sync and config.
- Compliance stance: non-custodial and unregulated in practice, but the team operates as if regulated to stay defensible. Cards issued via Checkout SAS, not the UK entity (Nick Taylor's call), to avoid inviting UK and Consumer Duty scrutiny. ACPR scrutiny risk called out. MI reporting and audit will exist at Braavos-equivalent standard, phased later. Vulnerable-customer and Consumer Duty workstreams are explicitly not required, unlike Braavos.
- Licensing: starts non-custodial, licences acquired over time including a possible MiCA licence for Europe, moving to custodial or hybrid. Visa first, Mastercard later. Card issuance to expand to US and UAE.
- Timeline: internal test around October, friends and family in December with roughly 50 testers and no regulatory build. Max's timelines run ahead of Braavos.

## Decisions

- No Zendesk for Ray. Go straight to Plain, targeted Q1, to avoid building on a stack that will be migrated off next year. If Plain is not ready for December, a sub-one-day lightweight setup covers friends and family.
- Ray app design mirrors Braavos unless there is a functional reason to diverge.
- Mandatory disclaimers on every fund-movement action: on-chain errors mean permanent loss, do not contact support. Also into T&Cs and an FAQ.
- Internal, then BPO, then hybrid staffing. Consumer fraud stays separate.

## Insights

- Ray is the first Care deployment with no Zendesk, which makes it the validation ground for Plain.
- The 60% AI resolution target is derived bottom-up from the self-serve share of the taxonomy. That method is reusable.
- The non-custodial "point them at the chain" posture is a deflection lever unavailable anywhere else in Care, offset by near-zero troubleshooting visibility.
