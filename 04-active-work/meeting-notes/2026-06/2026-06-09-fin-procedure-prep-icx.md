# Fin Procedure Prep Before ICX

**Date:** 2026-06-09  
**Attendees:** Charlie Wildish, Joel Petrosino, Francisco Goncalves, Imran Khan  
**Drive source:** 170UBO5dGWiMsNAEQZ3jnPN4j-xcw0kiXZe5XPBtasqc

## Context

Planning session for Fin Procedures, with focus on what can be delivered in H2 and confirming the architectural model for payment data explanations.

## Key Points

**Coverage estimate**
- Payment queries alone: 40–50% of Fin coverage.
- Add settlements: ~10% more.
- Add user management: ~5–10% more.
- Total estimated Fin Procedure coverage for complex actions: ~70% — matches the year's target.

**Settlement status gap**
- Merchants misunderstand "Completed" status because it means funds are expected to be sent, not confirmed received. Product update planned to add a new status for when funds leave Checkout's bank account (not when they arrive at the merchant's bank). This will unblock the settlement query Procedure.

**User management via Fin**
- Fin will look up locked-out user account status (inactive, locked, SSO-enabled) and return actionable instructions rather than generic guidance.

**Webhook querying**
- Proposal to query webhook events by payment ID. Dashboard is already well-built for this. Goal: add flexibility rather than rebuild. May initially just direct users to dashboard with guidance.

**Email authentication (recurring blocker)**
- A critical blocker for email-channel Fin: Fin needs a system-level check (dashboard user exists + permission level in Salesforce) before sharing data over email. Agents currently use human judgment — Fin cannot replicate this.

**Outage connector (live)**
- Built and launched. Uses client ID to query the OC team's outage API. Sets a Zendesk conversation attribute ("active outage") and triggers a workflow. Not yet triggered in production. Next step: extend to query outages by payment ID.

**Payment query tool (live, ~1 week)**
- 25 triggers, 19 resolutions, 6 escalations (API failures from wrong context in Dashboard).
- Validates payment IDs and ARNs.

**Payments rule book / backend analytics service**
- Proposed: a centralised "payments rule book" — a table mapping API data fields to English explanations, with Fin summarising subsections dynamically based on what data is returned.
- For payment performance analytics (trending over time, anomaly detection), a dedicated backend service will be built. Fin passes a prompt, the service does all data querying and analysis, returns an English response. Fin stays decoupled — logic is maintainable and the service can be swapped if Fin is replaced.

**Dashboard reconciliation**
- Drives ~30% of FTS tickets. Dashboard UX is the root cause — negative balances, invoice interpretation, multi-currency confusion. Not solvable by AI. UX writing team already engaged.

## Insights

- The 70% coverage estimate is now grounded in specific Procedure areas (payments, settlements, user management), not aspirational. This is the credible H2 target.
- The backend analytics service architecture (Fin as communication layer, backend for domain logic) is the right call — it decouples domain knowledge from Fin and enables vendor switching without re-engineering.
- Email authentication remains the hardest unresolved blocker for email-channel Fin. No system-level solution exists; requires policy decision first (see Jun 2 Stephen/Charlie session).
- The outage connector architecture (client ID → outage API → Zendesk attribute) is a clean pattern that can be extended to other external data sources.
