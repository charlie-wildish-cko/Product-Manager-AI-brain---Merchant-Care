# Thomas / Charlie — Centralising Customer Comms & Contacts

**Date:** 2026-06-12  
**Attendees:** Charlie Wildish, Thomas Martindell (Merchant Communications / Marketing)  
**Drive source:** 1oSgxI8J-uJgxU_xbSelRgipDpzSDIc_HgjIyfGbPHF8

## Context

Charlie is building evidence for 2027 planning to justify product teams dedicated to contact management and centralised communications — requested by Miller for Mariano/Jenny. Thomas is the internal counterpart most affected by the current fragmentation.

## Key Points

**Current contact data fragmentation**
- Contacts live across: Salesforce (commercial, communication preferences), Dashboard (portal users), Genesis (authorised signatures — stale since onboarding, never updated), offline Google Sheets (compliance contacts for sanctioned screening payouts, RFI contacts).
- Thomas's team uses Coefficient to download and join dashboard users and Salesforce contacts each morning to auto-build send lists. Dashboard feed into Salesforce is currently stale (BigQuery migration issue) — using a weeks-old snapshot.

**Core problem**
- Merchants cannot update their own contact data. The only way to change comms preferences is to email Merchant Care → Thomas's team. ~1 request per week. Table stakes for SMB — no AMs to manage it manually at scale.

**SMB as the forcing function**
- For enterprise, fragmentation is painful but survivable. For SMB at scale, it breaks: merchants miss critical communications (breaking changes, legal entity changes), driving churn.
- Thomas's real historical example: large migrations resulted in measurable customer loss because contact lists were inaccurate.

**Consumer data**
- Separate CRM planned (Thomas's director: do not mix B2B and B2C data). Consumer records will be entity-based, not email-based.

**Identity problem**
- Email alone is not a robust identifier. One person may have multiple email accounts or change email — doesn't reconcile cleanly. Fraud risk and duplicate records at scale. The right model separates communication contact from identity (modern banking app approach).

**Agreed north star**
- All contact data should live in the dashboard so merchants can self-nominate and self-manage. Salesforce remains the engagement reporting layer via data feed from the dashboard.

**Gap identified**
- The dashboard notification center (Amanda/Irene) covers preference management — but centralised contact storage is unowned. No one is solving this gap.

## Insights

- Genesis is still being used for authorised signatures even though data is stale from onboarding. This is a compliance risk — a field that is never updated but used for access control.
- The SMB argument is the strongest funding justification: without self-serve contact management, SMB cannot be served without disproportionate Care load.
- Thomas explicitly linked this to revenue risk: inaccurate contact lists during large-scale migrations result in churn.
- The gap between preference management (notification center) and contact data storage is the missing piece. It is currently unowned.
