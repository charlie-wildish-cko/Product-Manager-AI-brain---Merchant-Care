# KM AI Community of Practice

**Date:** 2026-08-17
**Attendees:** Alex Jordan (convener), Robert Braam, Joel Petrosino, Orrin Ward, Charles Forson, Anett Nickmann, Charlie Wildish, Angus Dickson, Simon Bataille-Vandereecken, Preethy Sundaresan, Sebastian Garcia Cardona, plus others invited
**Drive source:** 1jjl4t4G85nF90HPkos8Lup-7qwAT7_B55LGPfjCsPkY

## Context

Relaunch of the knowledge management community of practice, monthly cadence, covering project updates, Glean experiences and initiative spotlights.

## Key Points

- Glean is surfacing outdated and incorrect information. Two named incidents: wrong answers on corporate card support sourced from an outdated draft Google Doc, and a staff member using Glean-supplied incorrect information in a client communication.
- Root cause: Glean prioritises old documents buried in Google Drive over current verified sources. The group wants Glean to recognise active hubs, but concluded global source prioritisation is hard to configure today.
- Orrin Ward's case: Glean does not treat the Airtable product catalogue as canonical, defaulting to stale Confluence pages.
- Three separate auditing efforts under way: a KM auditor agent scanning Confluence for duplicate, redundant, outdated pages and pages with deactivated owners; Angus Dickson's unified content auditor across Confluence and Google Drive with content health metrics and a freshness score; Simon Bataille-Vandereecken migrating research knowledge to a central GitHub repository with a Glean agent replicating existing research tooling.
- Charlie's contribution: Merchant Care has a dedicated agent instructed to pull only from verified sources, with instructions ranking preferred sources first. The group noted the behavioural catch: purpose-built agents require users to seek them out, where Glean is embedded in the browser.
- Governance is the consensus blocker. No named owner or governing body sets org-wide knowledge hygiene or retention rules. Charles Forson: without enforceable rules and a named owner, cleanup regenerates the same mess within months. The Centre of Excellence restructure complicates finding that owner.
- Glean usage analytics are not accessible, so agent usage versus general Glean usage cannot be measured and knowledge gaps cannot be identified.
- Prior art to revisit: the self-maintaining "Hello Checkout" Confluence space, and earlier self-healing knowledge page work.

## Decisions

- Ownership and governance is the primary strategic focus for KM. Monthly cadence set, Slack channel to be created.
- All participants to collect concrete examples of incorrect Glean results to build the business case.

## Insights

- Care's verified-sources-only, ranked-preference agent is being cited as one of the better patterns in the org. Care's approach to source hierarchy is ahead of central Glean configuration.
- The failure mode Care manages for Fin (stale content producing wrong merchant answers) is org-wide with Glean and unowned. Any Care dependency on centrally governed content is a live risk to Fin answer quality.
- Two active internal auditor builds are worth reusing rather than rebuilding for Care KB hygiene.
- No Glean analytics means no measurable internal knowledge-gap signal, in contrast to Fin where deflection and gap data exist.
