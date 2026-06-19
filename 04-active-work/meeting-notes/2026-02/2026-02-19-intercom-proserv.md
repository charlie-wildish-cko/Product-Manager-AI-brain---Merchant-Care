# Intercom Professional Services — Fin Procedures Scoping

**Date:** 2026-02-19  
**Attendees:** Charlie Wildish, Akbur Ghafoor (Intercom ProServ), Rob King (Intercom)  
**Drive source:** 1zyz_QtCxfIdHfKs92OssSLlL4I0P-iUa4k28WGVa2bU

## Context

Scoping session with Intercom Professional Services to plan Q2 implementation work: Fin Procedures, web form replacement, audience segmentation, and B2C expansion.

## Key Points

**Current state**
- ~40,000–45,000 contacts/year. Email is ~60% of volume; the authenticated dashboard the remainder.
- Email expansion is blocked by: (1) B2B complexity (AMs on CC loops, Fin replying awkwardly); (2) inability to authenticate users over email for secure data connectors.
- Top 10 issues = 60–70% of volume. Payment scenario explanation and debugging estimated at ~50% of all queries.
- Current API connector (built in-house) is triggered by payment ID but doesn't return all data needed to explain every scenario. Full data expected H2 2026.

**Web form replacement**
- The web form handles ~30% of total volume and has zero deflection — it exists only because Fin can't yet capture CC/AM names and append them to Zendesk ticket fields.
- Goal: use Fin Procedures to replicate all web form logic and eliminate it for 90% of use cases. Significant automation opportunity.

**Audience segmentation**
- All merchants currently see all Fin content — sometimes returns incorrect answers (e.g. issuing content delivered to payment merchants, Platform-specific content to direct merchants).
- Plan: use Intercom Audiences feature, pulling business context attributes via API call at conversation start.

**Platform escalation flow**
- Platforms (marketplace vendors) need to raise support on behalf of sub-merchants by providing a seller ID. A second escalation flow to build in Fin.

**Internal query exclusion**
- ~10% of Fin/Zendesk volume is from internal AMs. Fin replying to internal queries is problematic. Plan: dedicated AM form + exclusion rules.

**B2C**
- Fin confirmed as front-line channel for all B2C mobile app traffic from 2027. Phone support will be required in UK for consumer.
- Fin placement on public docs pages shelved — no logged-in state means garbage results and inflated resolution counts.

## Insights

- The web form is the highest-impact near-term automation target: 30% of volume, currently zero deflection.
- Payment scenario handling (~50% of queries) is the core capability gap in Fin. Solving it is the single biggest resolution rate lever.
- The H2 2026 data dependency (API returning incomplete payment data) is a hard ceiling on what Fin can do in H1 — an external constraint, not a product choice.
- Audience segmentation is a prerequisite for scaling Fin across diverse merchant types.
- Charlie is building an internal contact attribution mechanism (stack-ranking analysis tailored to Checkout terminology) — this is the early form of the Reflex product concept.
