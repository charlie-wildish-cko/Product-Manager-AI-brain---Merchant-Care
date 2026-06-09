# Customer Communications & Identity — Problem Statement

## The problem

Checkout lacks a unified customer identity and communications layer. Customer contacts, email addresses, roles, and organisations are stored across six systems — Salesforce, Zendesk, OKTA, Genesis, Pardot, and Citadel — with no single view linking them. Communications are sent by Care, Disputes, Fraud, Compliance, and Underwriting independently, with no shared log and no structured handoff between teams.

This creates two connected failures.

**For customers**: Merchants have no central way to track what Checkout has communicated to them or which team is handling their issue. When a query moves between teams, they re-explain from scratch.

**For internal teams**: Agents cannot see what other teams have told a customer. Queries transfer via inbox-to-inbox email forward, losing context at every handoff. There is no audit trail across the full customer relationship.

## Why this is urgent

These failures are manageable today in B2B Enterprise because account managers compensate manually. Three changes in 2027 remove that compensation entirely.

**B2C consumer launch under FCA regulation.** Consumer Duty requires evidencing fair customer outcomes through a complete, auditable comms record. FCA DISP complaints handling requires full cross-team comms history. UK GDPR right to erasure requires knowing where every communication is stored. Vulnerable customer flags must propagate across every team a customer interacts with. These obligations apply from day one of launch — not after a stabilisation period.

**SMB expansion.** No account managers exist to absorb manual coordination at SMB volume. Cross-team handoffs at scale cannot be staffed without structured routing. Comms targeting the wrong contact is a churn risk, not a recoverable escalation.

**Platform/ISV model.** The ISV contact hierarchy — ISV entity and Platform merchants — requires routing logic that does not exist today. A dispute notification or compliance notice sent to the wrong tier causes operational failure.

## Root causes

Two underlying infrastructure gaps drive all symptoms.

- **No unified identity layer**: Checkout cannot reliably link a person to their organisation, roles, and communications across systems. The same merchant has different records in Salesforce, Zendesk, and OKTA with no joins between them.
- **No unified communications record**: There is no shared log of what has been communicated to a customer, by whom, or through which channel. No team can see the full picture.

## What success looks like

- Any internal team can see the complete comms history for a customer in seconds
- Customers can view and manage all Checkout communications in one place
- Queries transfer between teams with full context, not inbox forwards
- Communication preferences are captured once and honoured everywhere
- A complete comms record for any customer can be produced on demand for regulatory purposes

## Next steps

Quantify the scale of the problem before scoping a solution. Data collection targets: Zendesk, Salesforce, OKTA, Legal/Privacy. Target a findings summary within four weeks to inform a solution scoping and ownership decision. See linked data collection tracker.
