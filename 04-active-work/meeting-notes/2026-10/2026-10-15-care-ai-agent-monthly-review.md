# Care AI agent monthly review

**Date:** 2026-10-15  
**Attendees:** Charlie Wildish, Sebastian Garcia Cardona (content/knowledge), Janny Chow (ticket reviewer). Preethy Sundaresan and Ling Wong invited, absent.  
**Drive source:** 1kGkaBz-LqfCMS36VwLTEutkdeZMpLXsnuD2SEEDI1vA

## Context

Monthly review of Fin conversations and tickets. Janny reviewed the last 30 days of tickets for transaction-related themes, sampling 3 to 5 per category. Linked doc: Chatbot Escalation Analysis. A 07:34 false start of the same meeting produced no content and is discarded.

## Key Points

**Manual refunds and attachments**
- After Landmark escalations (manual refund requests mishandled by Fin), Charlie updated rules to escalate on "manual refund" (and "pilot") keywords, plus conversations mentioning attachments or customer service.
- Interim workflow for manual refunds and refund reversals: Fin human-in-the-loop. Fin messages the merchant while the team does the backend action and confirms.
- Merchants send large-dataset attachments Fin cannot read. This frustrates them and must be solved.
- Charlie is removing the web form for the merchant platform this week, which will raise Fin traffic. He will verify Fin handles attachments and CSV.
- Goal next year: automate manual refunds via backend service calls.

**Ticket review findings**
- One interaction produced three sequential tickets. Zendesk AI agent tickets spawn secondary tickets on escalation. To be reported to engineering.
- Ticket 176466: a merchant terminated in August still used Fin and logged a ticket. Dashboard access is not revoked for soft-terminated merchants.
- Ticket 176249: refund failed for negative balance (error 503), Fin did not state the reason. Cause: missing refund-failed event in the data payload. Data source changes this quarter fix it. Five or six support articles already cover the topic.
- Ticket 175896: merchant asked how to raise a ticket and Fin handed to a human without answering. Fin should answer first, then offer escalation.

**Disputes routing**
- Lost-dispute queries still arrive via Merchant Care. Mentions of the disputes email were removed from the support site at the Disputes team's request.
- Ideal: a single entry point with auto-routing. For now content tells merchants to supply payment ID or dispute ID upfront.

## Insights

- Attachment and CSV handling becomes a larger gap once the web form is removed.
- Data payload gaps cause wrong Fin answers. The refund-failed fix lands this quarter.
- Soft-terminated merchants keep dashboard and Fin access: a control gap.
- Zendesk AI-agent ticket spawning inflates ticket counts and can distort contact rate.
- Disputes routing depends on content and an organisational decision by the Disputes team.
