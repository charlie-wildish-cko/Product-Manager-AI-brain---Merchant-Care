# Fin github sync

**Date:** 2026-10-13  
**Attendees:** Charlie Wildish, Sebastian Garcia Cardona (docs and support content engineering)  
**Drive source:** 1kmoRto--HNbwWdwwXd-UA3wKj6UkEia7IV8xwYjC2Mc

## Context

Sync on syncing GitHub content into Fin's knowledge, plus the Landmark escalation, web form removal and support center plan.

## Key Points

**Landmark (MENA) escalation**
- Landmark sent 7 contacts last month asking for Fin to be removed. Charlie's review of all their tickets: all refund related, many about specific refund statuses and likely manual refunds, which cannot be automated now. Charlie: the manual refund gap is "something we've created because we are allowing it to happen".
- Data cannot be shared over email, so Care can only send generic replies.
- Landmark emailed the MENA head. Charlie's position: copy in Jenny with an action plan, hold a call rather than switching Fin off, and push back. Jenny signs off any deactivation and has pushed back on other merchants.
- Landmark is a multi-year customer, high potential, but not providing required info or asking to escalate.
- MENA has very low AI adoption and always asks for a human. Charlie dislikes AI-adoption goals that force experience trade-offs: "The experience is more important, not the AI goal."

**Fin GitHub integration**
- Using the test workspace to sync a sample, validate replication and keep it unavailable to Fin. Sebastian had to do the setup because Charlie lacks repo owner rights.
- Blocker: IT disabled the Fin GitHub app after an earlier approval, pending proof of Intercom procurement (Intercom in use since July 2025). Sebastian replies on the thread and Charlie loops in Steven Miller.
- Separate IT block: Sebastian's Algolia renewal, because Okta shows him as the only assigned user.

**Dashboard bug and escalation rule**
- The dashboard session token that authenticates the Fin data connector expires and is not refreshed before requests, so the connector fails with a bad merchant-facing state. Engineering must refresh it before every request. Interim: a Fin Procedure rule auto-escalates on the third failure.

**Web form deprecation**
- Web form removed today or tomorrow so dashboard requests route through Fin. Platform web forms stay. This can worsen the failure state until the token bug is fixed.
- "Suggest on web form" labels are deprecated for non-platform content. Sebastian scrubs them.
- Charlie adds a workflow rule so users escalating via the form can add other emails (e.g. account manager).

**Documentation impact assessment (Sebastian)**
- A local SQL database maps links between docs and support articles (hard links and matching support labels), flagging support articles likely impacted when docs change, with suggested edits. On a branch, to merge to main. Charlie wants it automatic. Internal support repo auth issues resolved this morning.

**Support center**
- Q2 2027: a NextJS site rendering and syncing all content from GitHub, instead of Plain's help center. Once ready, move away from Zendesk. Check timing against `2026 deliverables.md`.

**SMB dashboard principles**
- SLT is defining one dashboard that evolves with user growth. Docs cannot describe everything as available or merchants file "can't see this feature" tickets. Needs a content filter or tag system. Sebastian meets Sammy tomorrow on content strategy.

## Insights

- Web form removal raises dependence on Fin and the data connector while the token-refresh bug is unfixed. The three-failure auto-escalate is the only mitigation.
- Manual refunds are a known automation gap driving escalations and repeat contacts.
- Support center (Q2 2027) is tied to leaving Zendesk.
- Content tiering by user stage will need a tag or filter model in support content and Fin knowledge.
- Decisions: remove the web form, deprecate the "suggest on web form" label for non-platform content, build the support center in Q2.
