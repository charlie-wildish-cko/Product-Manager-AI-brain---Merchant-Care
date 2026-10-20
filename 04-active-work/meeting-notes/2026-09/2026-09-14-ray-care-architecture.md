# Ray Care: Target Architecture and Routing

**Date:** 2026-09-14
**Attendees:** Charlie Wildish, Joe Foulds (engineering), Max Rothman, Oliver Westlake-Simm, Fabio Marques (risk/disputes)
**Drive source:** 1yEHrHi1fz4Syxj38dhsmWVYIQl8ZQbYPBEgi0No0jxc

## Context

Settling the Care architecture for Ray: which systems handle inbound, where human agents work, how consumers get replies, and which internal teams migrate.

## Key Points

**Target architecture**

- Zendesk is killed for Ray. **Fin** handles inbound deflection and chat via an embedded SDK. **Plain** is the case management system where human Care agents work. Fin creates a ticket via API and the conversation ends there; Plain handles escalations, not Fin.
- Plain stores the records. Charlie to confirm with engineering whether every record is created in Plain, which would give a full transcript regardless of routing. Minimum Ray-side build is an inbox reading from Care's data to show tickets awaiting a human; Care hosts the conversations and all customer communication.
- Reply channel: async replies go from the Plain ticket back to the consumer, ideally into the in-app inbox thread, alternatively a generic "Ray support" email. Charlie's nuance: reply-by-email is acceptable because the thread is already authenticated; inbound submission by email is the problem. Max wants email off entirely. Fabio opposed email outright as a potential data breach for consumers. Turning email off is not impossible but has not been looked at and is a change from today, where everything is email.

**Routing debate**

- Fabio wants fraud and specialised requests to go straight from Fin to a specialist agent in Plain, not ping-pong via a Care agent, citing the risk of a Care backlog slowing consumer resolution.
- Counter-argument Fabio conceded: consumers frequently cannot tell fraud from non-fraud, so a Care agent often resolves faster anyway.
- System-fragmentation problem: if consumer disputes/fraud stay in Salesforce, those teams reply direct from their own inbox, the thread is invisible to both Care and the consumer, and nothing is trackable in-app.
- Oliver: for Braavos it was agreed disputes sit with Merchant Care in Plain/Zendesk. Disputes are expected to be the largest volume driver, so disputes should be in scope for the Plain go-live.
- Charlie: Salesforce is out of scope, everything routes through one place. A Salesforce-to-Plain integration is doable but does not exist today (it is all email sending).
- **Agreed interim model:** for friends-and-family, everything routes through Care, with Care sitting between other internal teams and consumers. Disputes team migrates to Plain in Q1. Charlie's constraint, stated directly: that model is not feasible for the external launch, as all volume would land on his team. Minimum bar is a traceability pass-through from Care so consumers see outcomes in-app, even if response is slightly slower.
- Migration scope discipline: consumer disputes is a completely delineated team from merchant disputes (Oliver confirmed), so onboarding it to Plain does not drag merchant disputes along and avoids a swivel-chair problem. Care needs a definitive list of which teams onboard to Plain to set timelines.

**Non-inbound and outbound scenarios (Joe)**

- Locked-out users who cannot open the app to raise a ticket: handled via a dedicated authenticated web rescue page, Monzo-style.
- Public social media complaints: handled via Karolina's triage principle, creating an internal ticket linked to the customer and responding through the proper channel.
- Checkout-initiated account changes (e.g. suspension): a push notification flow, not the ticketing system.

**Compliance is the open gap**

- Compliance (Puja's org) merged acquiring and consumer into one team, the opposite of Care's split, so compliance will have a swivel-chair experience. Sphinx stays a separate tool and data has to be passed between teams.
- Unresolved path: Fabio escalates an AML case, Brian decides to terminate an account, and there is no clear route for that decision back to the consumer.
- Oliver's mitigation: license a bare minimum of dedicated TM/compliance seats in Plain.

**SDK architecture**

- Joe strongly prefers Care builds an SDK for Ray to embed, rather than Ray embedding Plain's SDK directly, so Ray stays agnostic to the upstream ticketing system and a future system swap costs Ray nothing. Charlie agreed it fits feature architecture better as an exposed service, but the decision is not made.

**Other**

- Plain has automatic translation, so agents reply in languages they do not speak. Internal native speakers available for testing: Portuguese (Care's lead admin, plus Brazilian Portuguese), Arabic (one agent in Dubai), Filipino (via Dubai). Joe: Checkout has previously sourced native speakers in ~40 languages for translation QA.
- Transaction monitoring: Sardine does TM. Stefan in disputes already builds TM rules with Sardine and was unaware of Ray. Fabio wants to reuse Stefan's expertise and team rather than duplicate, possibly hiring in Mauritius alongside him.

**Numbers**

| Item | Figure |
|---|---|
| Plain pricing | ~$120 per seat per month, seat-based. Charlie: similar to or slightly below Salesforce |
| Fabio's initial headcount (his own "old numbers", being cut) | 12 Ray Care agents, 4 fraud/crypto analysts and disputes, 8 from BPO or Mauritius (leaning Mauritius on cost), ~30 seats maximum at launch |
| Charlie's Q1 compliance addition | ~10 more seats. Total allocation 40-50 seats |
| Plain cost at 50 seats | ~$72k/year for Ray alone |

## Decisions

- **Start integrating Fin into Ray now**, to give self-service on day one. Charlie assessed it as doable and low risk for the end-of-year launch given low initial volumes and Fin's out-of-the-box SDK. Engineering says Fin is easier to integrate than any alternative, including a web form.
- Interim: Care sits between internal teams and consumers for friends-and-family. Other teams migrate to Plain later, disputes in Q1.
- Salesforce out of scope. Ray integrates with one system via Care, not multiple ticketing systems directly.
- Needs further discussion: Care-built SDK against embedded Plain SDK. Plain integration is blocked on this; Fin integration is not.
- Open: whether consumer email replies can be switched off in favour of app-only.

## Insights

- Fin-first, Plain-behind is the agreed Ray Care architecture. Fin is unblocked for immediate integration while Plain waits on the SDK decision, which is the single blocker on the Plain side.
- Charlie's leverage on scope is now on record with Max, Oliver, Fabio and Joe: the Care-in-the-middle model is acceptable for friends-and-family only, breaks at external launch, and Care will need help.
- Consumer disputes being a fully delineated team is what makes the Plain migration tractable. Guard that boundary: any drift toward migrating merchant disputes expands scope massively.
- Compliance's merged acquiring/consumer structure is the one structural conflict with Care's model and will produce a swivel-chair experience regardless of Plain. Needs Puja, Meline and the new FCC hire.
- Plain's auto-translation is a genuine capability advantage for a consumer product launching outside the UK, and it is testable in-house.
- Email as a consumer channel is contested on security grounds by risk, not just experience grounds. Expect pressure to make Ray app-only for both inbound and outbound.
