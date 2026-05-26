# Reflex UI — Recommended Contact Fields

Source tables:
- QA: `cko-data-oca-qa-8961.merchant_support_experience.temp_fct_support_contact_snapshot`
- Prod: `cko-data-oca-prod-8038.merchant_support_experience.fct_support_contact`

This document replaces the earlier ticket-grain field list. The contact mart unifies Zendesk + Fin at contact grain — one row per `contact_id`. Fin-only contacts (no Zendesk ticket) are now in scope.

---

## Schema decisions (open questions resolved)

| Question | Recommendation |
|---|---|
| **Pipeline grain** | Switch to contact grain. Keeping ticket grain loses Fin-only resolutions — a growing share of contacts as Fin deflection improves. KB doc key: `contacts/{yyyy}/{MM}/{dd}/{contact_id}.json`. |
| **Closed filter** | Coalesce: `zendesk_status = 'closed'` OR `fin_is_solved = TRUE`. Zendesk-only filter silently drops Fin-resolved contacts. |
| **Test contact filter** | `zendesk_is_test_ticket = FALSE OR zendesk_is_test_ticket IS NULL` — Fin-only contacts won't carry this flag. |
| **Canonical classification** | Use top-level coalesced `case_type` / `issue_type` / `reason` as the primary values. Retain `zendesk_*` and `fin_*` source versions as secondary fields for debugging and attribution. |

---

## Include

### Contact identifiers
- `contact_id` — KB doc key; always present
- `ticket_id` — nullable (null for Fin-only); needed to link back to Zendesk comments
- `conversation_id` — links to Fin conversation
- `contact_type` — contact cluster key; needed for segmentation
- `contact_created_at` — partition key; required for trend analysis and spike detection
- `contact_first_platform`, `contact_last_platform` — journey signal (did this start in Fin, escalate to ZD?)
- `handoff_lag_mins` — time from Fin to Zendesk; signals handoff quality and Fin containment

### Coalesced classification (use these as canonical)
- `case_type`, `issue_type`, `reason` — taxonomy backbone for all PM filters and drill-downs
- `channel`, `sub_channel` — canonical channel values across both platforms

### Zendesk — classification
- `zendesk_sentiment` — VoC signal; correlates with NPS in Phase 3
- `zendesk_priority`, `zendesk_impact` — severity weighting for stack-ranking contact drivers
- `zendesk_subject` — high semantic signal for theme clustering; input to LLM summarisation
- `zendesk_is_classified_by_fin`, `zendesk_fin_ticket_type` — records Fin involvement on ZD-backed contacts
- `zendesk_is_agent_consultant_involved` — tracks Agent Consultant usage; useful for agent efficiency analysis

### Zendesk — client / company
- `zendesk_client_id`, `zendesk_entity_id` — NPS join keys; links contacts to merchant for VoC view
- `zendesk_company_tier` — segment filter (replaces both `organization_tier` and `zendesk_tier` from old schema)

### Zendesk — timestamps
- `zendesk_solved_at` — lookback filter for closed ZD-backed contacts

### Zendesk — lifecycle
- `zendesk_was_escalated_l1_to_l2` — L1→L2 escalation; complexity and cost signal
- `zendesk_was_reopened` — recurrence signal; repeated reopens flag unresolved root causes

### Zendesk — effort
- `zendesk_agent_touches` — multi-touch contacts signal unresolved root causes
- `zendesk_total_resolution_time_days` — effort proxy; skip hrs/mins variants
- `zendesk_dependent_team`, `zendesk_dependent_team_grouping` — secondary; useful for routing Jira issues to non-Care teams

### Zendesk — product taxonomy
- `zendesk_product_feature`, `zendesk_product_category`, `zendesk_product_name`, `zendesk_product_state`, `zendesk_product_pillar`
- `zendesk_product_teams`, `zendesk_product_team_mc`, `zendesk_product_team_2`

### Zendesk — CSAT
- `zendesk_csat_score`

### Fin — classification (secondary; keep for attribution and debugging)
- `fin_case_type`, `fin_issue_type`, `fin_reason`

### Fin — company
- `fin_company_client_id` — primary merchant identifier for Fin-only contacts (where `zendesk_client_id` is null)
- `fin_company_tier` — segment filter for Fin-only contacts

### Fin — lifecycle
- `fin_is_solved` — closure flag for Fin-only contacts; required for the coalesced closed filter
- `fin_was_escalated_ai_to_human` — key signal; marks whether Fin failed to contain the contact

### Fin — AI agent
- `fin_ai_agent_resolution_state` — what outcome Fin reached (resolved, escalated, abandoned, etc.)
- `fin_ai_agent_last_answer_type` — how Fin responded (AI answer, workflow, handoff, etc.)
- `fin_ai_agent_rating`, `fin_ai_agent_rating_remark` — merchant's explicit rating of Fin's answer; `fin_ai_agent_rating_remark` is free-text, high signal for content gap identification
- `fin_count_ai_touches` — AI effort; analogous to `zendesk_agent_touches`

### Fin — CX score / CSAT
- `fin_cx_score_rating` — Fin's internal CX quality score
- `fin_cx_score_explanation` — free-text; replaces `csat_comment` (dropped in new schema); high signal for AI engine
- `fin_csat_score`

---

## Secondary (include if data is clean)
- `zendesk_language` — enables regional breakdowns
- `zendesk_ticket_channel` — channel detail below the coalesced `channel`; useful for email vs webform splits
- `contact_workflow` — may surface routing pattern differences; validate what values are populated

---

## Exclude

| Category | Reason |
|---|---|
| PII fields (`fin_contact_name`, `fin_contact_email`, `zendesk_client_name`, `zendesk_company_name`, `fin_company_name`, `fin_company_client_name`) | No PM use case; data minimisation |
| All SLA detail flags | Operational metrics for Ops, not PM-actionable |
| Per-agent time breakdowns (`zendesk_agent_work_time_l1`, `zendesk_l1_open_time_mins`, etc.) | `agent_touches` + `total_resolution_time_days` is sufficient |
| `zendesk_requester_id`, `zendesk_assignee_id`, `zendesk_submitter_id` | PII; no PM use case |
| Peer review fields | Internal quality workflow |
| Vault approval fields | Internal approval workflow |
| OCR / assignment event counts | Routing mechanics, not insight |
| Boolean lifecycle flags (`zendesk_is_solved`, `zendesk_is_deleted`, `zendesk_is_unassigned`, etc.) | Constant in closed-contact dataset |
| `zendesk_legacy_case_type`, `fin_legacy_case_type` | Superseded; use coalesced top-level values |
| `fin_is_ai_one_touch`, `fin_is_ai_two_touch`, `fin_is_ai_multi_touch` | Redundant with `fin_count_ai_touches` |
| `fin_contact_external_id`, `fin_source_url` | Internal system IDs; no analytical value |
| `zendesk_is_qa_review`, `zendesk_is_qa_eligible`, `is_qa_review` | QA workflow flags; not relevant to PM insight |

---

## Note on `description` fields

Both `zendesk_description` and `fin_description` should be used as input to `SummaryGenerator` (feeding `issue_summary` / `resolution_summary`) but not persisted in the KB doc. `zendesk_subject` and `fin_subject` are sufficient for semantic matching and cheaper to store at scale. `fin_subject` is particularly important for Fin-only contacts where there is no `zendesk_subject`.
