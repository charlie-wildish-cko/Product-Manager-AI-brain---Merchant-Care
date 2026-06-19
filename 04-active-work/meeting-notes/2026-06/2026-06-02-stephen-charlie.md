# Stephen / Charlie — Email Authentication & Fin over Email

**Date:** 2026-06-02  
**Attendees:** Charlie Wildish, Stephen Adams  
**Drive source:** 1Y-pbW_KoLtRZXSKSErZsbA4kaLGbPGIhlbQHgATdh6g

## Context

Problem scoping discussion on email authentication — a blocker for enabling Fin to share payment data securely over the email channel.

## Key Points

- Email handles 50–60% of support volume. Large merchants prefer it over the dashboard because they manage multiple proprietary support portals and don't want another.
- Current human agents share payment data over email without authentication validation — this sets a precedent that complicates adding friction.
- Checkout cannot verify that an email sender belongs to a merchant. No authentication exists for email contacts.

**Fin over email — proposed mechanism**
- Verification code step: Fin sends a unique code to the requester's inbox; they reply with it to confirm inbox ownership.
- "Phantom/ghost token": derived from email address — check if user exists in dashboard or Salesforce, derive permissions from that, then gate data sharing.

**Disputes/RFI gap**
- Dashboard dispute and RFI flows exist for initial submissions but have no mechanism for follow-up evidence — falls back to email.
- Disputes team lacks the user validation tables (Salesforce + user management) that Care has — cannot enforce the same security validation.

**Zendesk API constraint**
- The Zendesk API only allows attachment uploads in the context of a specific support reply — not as a general-purpose file portal.
- Email attachments cannot be screened by the Files API, creating uncontrolled security risk (CSVs, PDFs flow in unscreened).

**Decision**
- No product decision reached. The core question (whether to mandate dashboard) must be decided at leadership level (Adrian). Solution design is secondary.
- Stephen to draft an overview of document upload use cases and email challenges for Adrian.
- Charlie to seek ARB sign-off on the mechanism for sharing data over email via Fin.

## Insights

- Adding friction to Fin's email authentication would create a worse merchant experience than the current human agent process — unless human agent behaviour also changes simultaneously. Policy decision must precede product decision.
- Merchants avoid the dashboard because they use centralised third-party support tooling (their own Zendesk/Salesforce Service Cloud). Checkout has no visibility into which tools merchants use — making bespoke integrations very hard to scope.
- The email authentication problem is the same structural gap that appeared in the Feb 19 Intercom ProServ session. It remains unresolved.
