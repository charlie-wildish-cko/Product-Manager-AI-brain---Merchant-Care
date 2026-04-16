# Fin Response Scripts — Outage Check

Format rules: status → reason → next step → close. 3–4 lines max. No API field names in merchant-facing text.

---

## 1. Is my account affected by an outage?

**API calls:**
1. `GET /client/incidents?status=open` — returns `incidents[]` and `total_count`
   `summary` field: `"Active incident affecting [impacted_service_id] / [impacted_sub_service_id] since [start_time], severity [severity]"` / `"No open incidents affecting this account"`

---

**Query response — no open incidents**

> There are no known incidents affecting your account right now.
> If you're seeing an issue, let me know what's happening and I can look further.

---

**Query response — one open incident**

> There is an active incident affecting **[impacted_service_id]** ([impacted_sub_service_id]), open since **[start_time in readable format, e.g. "10 June at 11:00 UTC"]**.
> Our team is actively investigating — you don't need to raise a new ticket.
> Reach out again if the issue persists once the incident is resolved.

---

**Query response — multiple open incidents**

> There are **[total_count]** active incidents affecting your account:
>
> - **[impacted_service_id]** ([impacted_sub_service_id]) — open since [start_time]
> - **[impacted_service_id]** ([impacted_sub_service_id]) — open since [start_time]
>
> Our team is actively investigating all of these — you don't need to raise a new ticket for each one.
> Let me know if you'd like me to connect you with an agent for a live update.

---

**Note for Fin:** Severity should only be mentioned if SEV1 or SEV2. Do not surface severity level for SEV3 or below unless the merchant asks directly.
