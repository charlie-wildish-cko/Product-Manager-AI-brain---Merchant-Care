# Consumer Flow Mapping Session

**Date:** 2026-08-11
**Attendees:** Charlie Wildish, Joel Petrosino, Oliver Westlake-Simm, Fabio Marques, Bernard Ryan, Daniel Kliza, Sarah Edmonds, Sunil Mudaliar, Wes Nolan
**Drive source:** 1CC2epVm4VGFRlKy6--_5U3KZRbyHgAwy0kU7KwQO0g8

## Context

Session convened to map every consumer journey that could generate a contact (care, non-fraud disputes, fraud, ATO, transaction monitoring, sanctions screening) and identify per flow the data needed, the system of record, and whether that system exists. No flow map was produced: Oliver's laptop failed mid-call, no product stakeholders attended. Decisions still landed.

## Key Points

**Scope and timing**
- Braavos external launch moved to end of March. Daniel: discovery in September plus build in Nov/Dec is "cutting this very short."
- Ray will not launch in the UK. Targets UAE, Philippines, Brazil, with UK internal testing only. Ray described as a side-of-desk project; Braavos was the mapping priority.

**Compliance and tooling**
- Bernard listed seven Braavos compliance workflows: onboarding/CDD, EDD, screening alert review, AML transaction monitoring, periodic and event-driven review, consumer changes and reverification, restriction/suspension/offboarding. Process is roughly 90% defined, tooling close to zero.
- Tooling fragmentation across Zendesk, Salesforce, Retool apps, Citadel, and a risk assessment tool. Daniel: "the only common denominator between every single team in operations is Gmail."
- A transaction-monitoring RFI raised in Salesforce is invisible to a consumer care agent in Zendesk.
- Fabio flagged SOP obsolescence: Care moves off Zendesk around the same time as consumer launch, so Zendesk-step SOPs (also shared with partner banks) may be dead on arrival.

**Product gaps that become contacts**
- Funds cannot be transferred out to a non-own account.
- A user cannot unblock their own card after a suspicious-activity flag.
- Consumer disputes is the biggest risk: PRD unresolved, no product build commitment, ownership moving from Karolina to Issuing. Oliver: "we either hire people, which is costly, or we create a product that allows us to scale."

**Charlie's positions**
- The triage model (AI to L1 care to specialist) is an assumption, not evidence-based.
- Escalations may bypass the agent but not the system: log the record in the care system, then bypass downstream, preserving the creation timestamp for SLA.
- End state is one or two case management systems maximum. Step one is removing email as a work-intake channel.
- Do not build operational apps into case management. It is a CRM and data storage problem, solved with field-level segregation.
- Consumer channels: Fin (AI chat), phone, complaints email, majority via Fin. Fin installed identically across Braavos and Ray with source abstraction so origin drives content and treatment. Lower AI resolution expected on crypto.

## Decisions

- Vulnerable customers flagged via a CRM attribute and routed to a vulnerable-customer specialist inside Care, mirroring existing tiering.
- All frontline agents must be able to identify and flag vulnerability; only trained specialists handle the case. The flag can gate AI eligibility so a vulnerable customer routes straight to a human.
- Fin will perform suspected-vulnerability detection from defined signals, surfacing a verify prompt to the agent.
- Two-layer procedure writing adopted: tool-independent process now, in-tool click steps later.
- Roles and responsibilities must be settled before flows can be mapped. Reconvene with product stakeholders present.

## Insights

- The existing Figma flows are already a taxonomy artefact. Two known defects: Care shown as the only human actor, and outbound/proactive contact (RFIs, notifications) unmodelled.
- "Log but bypass" is a reusable routing pattern for merchant flows: every escalation writes a care-system record for traceability and SLA, then routes downstream.
- Fin vulnerability detection is now a concrete capability request with no owner. It needs signal definitions, an agent verify prompt, a CRM attribute contract, and an AI-eligibility gate.
- Missing self-service features are identifiable contact generators before launch. Card unblock is the worked example. Frame flow mapping as contact reduction.
- The Zendesk migration timeline collides with consumer launch. Two-layer procedures are the mitigation.
