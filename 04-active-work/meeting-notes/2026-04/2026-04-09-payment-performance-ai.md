# Payment Performance and AI

**Date:** 2026-04-09  
**Attendees:** Charlie Wildish (Care PM), Fraser Bryant, Guillaume Merindol, Etienne Herlaut  
**Drive source:** 1_zvqzZVDVY_vcK3AdmEdDJsn1K-8QHfakmJ5Rv-HSeM

## Context

Discovery meeting between Care PM and the payment performance/Magic team (Guillaume, Etienne), who had built significant AI automation capability around payment investigation. Explored whether to integrate, share, or build in parallel.

## Key Points

- Guillaume's team built a Slack-bot-based transaction analyser that fetches extensive payment information including ISO events, authentication events, and Datadog logs to build a timeline. Currently in limited access — restricted to users with deep payments knowledge who can provide feedback.
- Care's current tooling: static Zendesk interface that pulls a payment ID and displays a timeline and metadata, but provides no explanation of events. Goal: dynamic retrieval and explanation from multiple sources, including Datadog logs.
- The key gap in Care's current setup: Datadog log access. Without it, agents spend significant time filtering for relevant entries manually.
- Options discussed: (1) reuse some or all of the Slack bot features, (2) hybrid model where specialist bot handles complex cases, internal tools handle 80% of needs.
- Guillaume's recommendation: hybrid approach is the long-term answer. Specialist bots for deep answers; internal tools for the majority.

## Insights

- Two teams independently building AI-powered payment investigation tooling is an overlap risk — the hybrid model aligns both efforts without requiring full integration.
- Datadog access is a practical blocker for Care's payment explanation capability — agents currently work around it manually.
- Guillaume's Slackbot is technically more sophisticated than Care's current tools but requires payment domain expertise to use effectively. The "Care for 80%, specialist bot for complex 20%" pattern mirrors the L1/L2 structure.
- Senior agents were identified as the beta testers — appropriate, given the domain knowledge required to evaluate output quality.
