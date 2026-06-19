# Payments and Technical Issue Content Opportunities

**Date:** 2026-06-03  
**Attendees:** Charlie Wildish, Preethy Sundaresan  
**Drive source:** 1Ynrr3HDzy2uRJr5MimF5wogoj_IVZ1KVb-eErZ2M9gY

## Context

Review of content gaps for payment and technical issues, and planning for Q3 knowledge coverage improvements.

## Key Points

**Fin deployment status**
- Fin just deployed to Tier 2 emails. Escalation logic now uses a "taxonomy complexity" field (high/medium/low) applied to issue types and reasons — replaced an unworkable large rules set.
- Rollout plan: expand gradually from Tier 2 to Tier 1, then broaden taxonomy coverage. Email resolution rate expected to drop temporarily during this phase.

**Content gaps identified (from L2 ticket review)**
- Integration issues: WordPress plugin region settings causing 404s.
- Undocumented APM response codes (20000-series).
- AFT declines doc (well-written in internal Confluence, response code 2012 scenarios) — Keziah (internal SME) available to help fill external gaps.
- Test cards documentation gap: undocumented amount-based response code triggers existed in the codebase. Agents discovered this only via a payment performance bot that scanned the codebase.

**Docs-from-code**
- Charlie proposed: all documentation should be generated from code changes (PR-triggered doc updates) to prevent desync. Ideally, engineering repos send PRs to the docs repo automatically.
- API PR documentation is partially AI-generated already (engineers reviewing AI drafts). Product docs side is the gap.
- This is a cross-team conviction — also raised independently in the Jun 4 session with Patrick.

**Q3 plan: knowledge coverage tool**
- Build a graph/knowledge coverage tool to give a quantitative view of which topic areas have content gaps. Replaces qualitative PM intuition with data-driven prioritisation.

**Zendesk migration**
- New Zendesk help centre section in progress. Content team now owns 100% of data in the repo (images, formatting). Zendesk being used purely as a publishing tool in the meantime.

**Fin Procedures**
- Charlie deployed a new payment Fin Procedure providing fuller upfront explanations rather than referencing multiple separate docs. Goal: single consolidated payment rules document.
- Fin sub-agents: not currently supported. Claude sub-agents dramatically improve context window performance — Charlie expects Intercom to add this capability.

## Insights

- The test cards incident is a strong case for automated doc generation from code changes — a feature shipped with undocumented behaviour and generated avoidable support contacts.
- The Q3 knowledge coverage tool is a significant step toward systematic content management — directly relevant to Reflex and the knowledge management workstream.
- The taxonomy complexity field for Fin escalation is a cleaner architecture than large rules sets — generalises well as Fin expands to more issue types.
