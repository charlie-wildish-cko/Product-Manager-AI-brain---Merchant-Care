# Reduce Agent Effort on Dispatch and Email Clean Up Rules

**Quarter**: Q2 2026
**Type**: Zendesk configuration + engineering
**Flywheel**: Agent Experience
**Strategic goal**: Reduce cost of support (agent time on manual triage)

---

## Problem

Agents spend daily time (~2 hour shifts) on dispatch tasks that should be automated: tickets from unknown merchants require manual lookup and re-routing, non-business emails create noise in the queue (primarily cardholder data removal requests that belong with the DPO), Account Manager and Technical Account Manager records in Zendesk are stale, and there is no scheduled sync from Salesforce to keep them current.

---

## Scope

| Item                                                | Type           | Description                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Domain mapping for merchants with missing org links | Eng/ZD config  | Use Zendesk's domain mapping feature to associate inbound email domains to the correct Zendesk organisation when they reach Zendesk. Pilot with high-volume merchants with known email record gaps:<br /><br />Exness, Bytedance, MAF Holding, Yango. Run quarterly thereafter based on Dispatch team review.<br /><br />We have list of emails for this pilot. We should also design a quarterly approach for this. |
| Close rules on non-business emails                  | ZD config      | Auto-close tickets submitted from personal email domains (gmail, hotmail, etc.) with a targeted auto-reply. Cardholder data removal requests: direct to dpo@checkout.com (confirm routing with Joel). Test account contacts: direct to their Sales Manager or Solutions Engineer. Exception: documented shared mailbox senders are excluded from this rule.                                                          |
| Enforce internal form for Commercial                | ZD config      | Block ad hoc internal ticket creation. Require Commercial to use the existing internal form. Exception: documented shared mailbox senders are excluded.                                                                                                                                                                                                                                                              |
| Enrich internally created tickets with client ID    | ZD config/Eng? | Enrich internally created tickets when client ID is added.                                                                                                                                                                                                                                                                                                                                                           |
| Weekly AM/TAM record sync from Salesforce           | Eng            | Scheduled sync from Salesforce accounts to keep Account Manager and Technical Account Manager fields current in Zendesk.                                                                                                                                                                                                                                                                                             |

---

## Out of scope

- Changes to SLA routing or priority rules
- Agent toolkit UI changes (covered under Agent Productivity Tools, MCD-570)

---

## Goals

- Reduce Dispatch queue volume (fewer tickets that require manual re-routing or rejection)
- Reduce agent-reported incidents of missing or incorrect AM/TAM in Zendesk

---

## Dependencies

- Eng resource for Salesforce sync (1 eng item; domain mapping is ZD config only)
- Salesforce API access for AM/TAM sync
- Confirmation from Joel on DPO routing for cardholder data removal requests

---

## Open questions

1. Confirm with Joel: should cardholder data removal requests from personal email domains be auto-replied with dpo@checkout.com, or does the DPO team need a heads-up before this rule goes live?
