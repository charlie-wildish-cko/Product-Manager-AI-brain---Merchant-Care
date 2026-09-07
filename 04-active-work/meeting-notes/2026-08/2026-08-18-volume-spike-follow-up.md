# Merchant Care Volume Spike Follow Up

**Date:** 2026-08-18
**Attendees:** Karan Jagmohansing, Ashvin Pudaruth, Joanie Vencatasamy, Charlie Wildish, Joel Petrosino, Francisco Goncalves, Ling Wong
**Drive source:** 1HVUBzyhXiABKEtglVe_h_Matl-QZCfQQpdFMSC3iUdk

## Context

Called in response to a sharp August deterioration in time-to-assignment versus June and July. Agent handle time per ticket is falling, so agents are not sitting on tickets, yet they are not picking up the next one quickly.

## Key Points

- Remitly has roughly doubled daily inbound. All Remitly tickets are Enterprise, so they outrank everything else and push Tier 5 down. Tier 5 has the highest breach count. Remitly cases are excluded from routing but still consume capacity because seniors assign them manually or agents pick them up.
- Joel's correction: the metric decline started before the Remitly surge. Remitly compounds the problem but is not the root cause. Handle Remitly in isolation and fix the underlying issue separately.
- Queue snapshot from Joanie: 357 tickets in queue, 0 new, only 21 open. The queue is old backlog and routing serves the oldest ticket first, so the backlog perpetuates itself.
- Routing history: the one-ticket-at-a-time rule was introduced to force focus and produce accurate handle-time data. Under the previous multi-ticket setup agents parked a simple ticket while working a hard one, distorting handle time. Ling could not identify a mechanism by which 1 versus 2 concurrent tickets would cause degradation at this scale.
- Francisco reported a strong correlation between the single-ticket routing change and the assignment-time increase, a 10x jump rather than a few points. His hypothesis: agents now effectively control when they receive work via play mode, so the queue is not flushing.
- Charlie's candidate causes: team at capacity, shift pattern and online-status coverage, skills-match availability, priority-based deprioritisation of lower tiers, and the capacity rule itself. The one-at-a-time rule applies only to tickets in open status, not pending or on-hold.
- Volume by hour: peak inbound 18:00-23:00 averaging 185 tickets, versus 70 tickets in the 09:00-15:00 window. Remitly dumps overnight (20-40 tickets by end of the Mauritius day, 100+ by morning), so those tickets are already aged when the team logs on. Overnight is the thinnest coverage.
- Routing is not tiered. Tier segregation was removed because some tiers saw no cases while others were flooded. Enterprise is prioritised via SLO (24h versus 48h standard) plus an automation escalating priority at 8-12 hours to breach.
- Capacity losses: roughly four FTE over two months to L2 and Config role moves, plus training absences.
- Mexico team enters week four and starts working tickets at simple-to-medium complexity. Their BAU hours align with the peak window, adding night coverage and letting Mauritius pull one person back to the weekday shift.

## Decisions

- Do not change ticket routing. Keep one-ticket-at-a-time pending a data-driven analysis. Increasing the concurrency allowance is the only change on the table, and only under close monitoring.
- Fine-tune staffing capacity per shift against the confirmed arrival profile.
- Point the Mexico team at Remitly cases as a priority, with standardised Remitly guidance, templates and macros built by Joel with Alex and Annette.
- Ashvin to commission urgent analysis from Tim's team on assignment-delay drivers.

## Insights

- The 10x assignment-time correlation with the single-ticket routing change is the most actionable unresolved lead, currently blocked on Tim's team's analysis.
- Built-in tension: one-ticket-at-a-time exists to make handle time measurable, and reverting would restore throughput at the cost of the metric.
- Live example of Enterprise SLO priority starving Tier 5, and of a single merchant doubling inbound with no capacity model to absorb it.
