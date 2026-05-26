# Fin Response Scripts — User Management

Format rules: status → reason → next step → close. 3–4 lines max. No API codes or field names in merchant-facing text.

**Permission requirement:** All actions (unlock, unsuspend, password reset, activation email) require the requesting user to have the "Manage users" permission. Fin must check this before acting. Roles with manage users permission: Account owner, Admin, IAM admin.

---

## 1. User account locked

**API calls:**
1. `GET /umt/users/{userId}` — check `status` field
   `summary` field: `"Account is locked"` / `"Account is active"` / `"Account is suspended"` / `"Password expired"` / `"Account not yet activated"`
2. `GET /umt/clients/{clientId}/members/{requestorUserId}` — check requestor has manage users permission
   `summary` field: `"Requestor can manage users"` / `"Requestor cannot manage users"`
3. `POST /umt/users/{userId}/unlock` — execute unlock (after confirmation)

**Query response — account is locked**

> Your account is locked. This usually happens after too many failed login attempts.
> To unlock it, I'll need to verify that you have permission to manage users on this account. Can you confirm your name and email address?

**Permission check — requestor does not have manage users permission**

> I'm not able to unlock this account — you'll need the "Manage users" permission to do that.
> Please ask your Account owner, Admin, or IAM admin to unlock the account, or to grant you that permission first.

**Action confirmation — before unlocking**

> I'm about to unlock the account for **[name] ([email])**. Can you confirm you'd like me to proceed?

**Action response — after unlock**

> The account for **[name]** has been unlocked. They should be able to log in straight away.
> Anything else I can help with?

**Query response — account is not locked**

> That account is active and not locked. If the user is still unable to log in, the issue may be their password or browser session.
> Let me know what error they're seeing and I can look further.

---

## 2. User account suspended

**API calls:**
1. `GET /umt/users/{userId}` — check `status` field
   `summary` field: `"Account is locked"` / `"Account is active"` / `"Account is suspended"` / `"Password expired"` / `"Account not yet activated"`
2. `GET /umt/clients/{clientId}/members/{requestorUserId}` — check requestor has manage users permission
   `summary` field: `"Requestor can manage users"` / `"Requestor cannot manage users"`
3. `POST /umt/users/{userId}/unsuspend` — execute unsuspend (after confirmation)

**Query response — account is suspended**

> That account has been suspended. This is usually done by an administrator.
> To reactivate it, I'll need to verify that you have permission to manage users on this account. Can you confirm your name and email address?

**Permission check — requestor does not have manage users permission**

> I'm not able to reactivate this account — you'll need the "Manage users" permission to do that.
> Please ask your Account owner, Admin, or IAM admin to reactivate the account.

**Action confirmation — before unsuspending**

> I'm about to reactivate the account for **[name] ([email])**. Can you confirm you'd like me to proceed?

**Action response — after unsuspend**

> The account for **[name]** has been reactivated. They should be able to log in straight away.
> Anything else I can help with?

---

## 3. User password expired

**API calls:**
1. `GET /umt/users/{userId}` — check `status` field
   `summary` field: `"Account is locked"` / `"Account is active"` / `"Account is suspended"` / `"Password expired"` / `"Account not yet activated"`
2. `GET /umt/clients/{clientId}/members/{requestorUserId}` — check requestor has manage users permission
   `summary` field: `"Requestor can manage users"` / `"Requestor cannot manage users"`
3. `POST /umt/users/{userId}/activate` — send password reset email (after confirmation)

**Query response — password is expired**

> That user's password has expired. They'll need to set a new one before they can log in.
> I can send a password reset email to their registered address — would you like me to do that?

**Permission check — requestor does not have manage users permission**

> I'm not able to send a password reset for this account — you'll need the "Manage users" permission to do that.
> Please ask your Account owner, Admin, or IAM admin to send the reset.

**Action confirmation — before sending reset**

> I'll send a password reset email to **[email]**. Can you confirm you'd like me to proceed?

**Action response — after sending reset**

> A password reset email has been sent to **[email]**. They should follow the link to set a new password.
> Reach out again if the email hasn't arrived within a few minutes.

---

## 4. Send new activation email

**API calls:**
1. `GET /umt/users/{userId}` — check `status` is STAGED or PROVISIONED
   `summary` field: `"Account is locked"` / `"Account is active"` / `"Account is suspended"` / `"Password expired"` / `"Account not yet activated"`
2. `GET /umt/clients/{clientId}/members/{requestorUserId}` — check requestor has manage users permission
   `summary` field: `"Requestor can manage users"` / `"Requestor cannot manage users"`
3. `POST /umt/users/{userId}/activate` — send activation email (after confirmation)

Note: Returns 409 if user is already active — handle with the "already active" response below.

**Query response — account not yet activated**

> That account hasn't been activated yet. The original activation link may have expired.
> I can send a new activation link — would you like me to do that?

**Permission check — requestor does not have manage users permission**

> I'm not able to send an activation email for this account — you'll need the "Manage users" permission to do that.
> Please ask your Account owner, Admin, or IAM admin to resend the activation.

**Action confirmation — before sending**

> I'll send a new activation email to **[email]**. Can you confirm you'd like me to proceed?

**Action response — after sending**

> A new activation email has been sent to **[email]**. They should follow the link to activate their account.
> Reach out again if the email hasn't arrived within a few minutes.

**Query response — account already active (409)**

> That account is already active, so a new activation email isn't needed.
> If they're having trouble logging in, let me know what error they're seeing and I can look further.

---

## 5. User permissions — what can this user do

**API calls:**
1. `GET /umt/clients/{clientId}/members/{userId}` — returns `roles[]` and `permissions[]`
   `summary` field: `"User has [role name] role: [one-line capability description]"` / `"User has no role assigned"`

Map returned role names against the roles reference table below.

**Query response — role found**

> That user has the **[role name]** role. Here's what that includes:
>
> - [permission summary for that role, e.g. "View payments and analytics, manage API keys, create notifications"]
>
> If they need access to something else, a user with the Admin, Account owner, or IAM admin role can update their permissions from **Dashboard > Settings > Team**.
> Anything else I can help with?

**Roles reference (for Fin to use internally):**

| Role | Summary |
|---|---|
| Account owner | Full access including account structure, processing settings, SSO, and ownership transfer |
| Admin | Full access across all modules including user management, payments, disputes, vault, and settings |
| IAM admin | Manage team permissions, SSO, users, and custom roles |
| Compliance operator | View account settings and payments, manage compliance requests |
| Developer | Manage API keys, view payments and analytics, create notifications |
| Disputes manager | View payments, manage disputes and evidence |
| Disputes operator | Manage disputes only |
| Identities manager | Process identity checks, manage configurations |
| Risk manager | Manage fraud rules, decline payments, view reports and disputes |
| Support manager | View and manage payments and disputes, card creation, sub-entity onboarding |
| Read only | View-only access across all modules |
| Account application only | Manage onboarding and account activation |

**Query response — no role assigned**

> That user doesn't currently have a role assigned, which means they won't have access to the Dashboard.
> A user with the Admin, Account owner, or IAM admin role can assign them a role from **Dashboard > Settings > Team**.
> Anything else I can help with?

---

## 6. SSO enabled check

**API calls:**
1. `GET /api/clients/{clientId}/sso/status` — returns `enabled`, `enforce_sso_sign_in`
   `summary` field: `"SSO is enabled and required"` / `"SSO is enabled but optional"` / `"SSO is not enabled"`

**Query response — SSO is enabled and enforced**

> Your organisation uses Single Sign-On (SSO) and all users must log in through your company's identity provider.
> If you're having trouble logging in, contact your IT team — they manage SSO access.
> Anything else I can help with?

**Query response — SSO is enabled but not enforced**

> Your organisation has SSO configured, but it's optional — users can log in through SSO or with their Checkout.com username and password.
> Anything else I can help with?

**Query response — SSO is not enabled**

> Your organisation doesn't use Single Sign-On. Users log in with their Checkout.com username and password.
> Anything else I can help with?

---

## 7. User is federated (individual SSO check)

**API calls:**
1. `GET /umt/users/{userId}` — check `is_federated` field
   `summary` field: `"User authenticates via SSO"` / `"User authenticates with Checkout.com login"`

Note: Same call as account status lookup (scenarios 1–3) — no additional API call needed if already retrieved.

**Query response — user is federated**

> That user's account is linked to your organisation's identity provider. They'll need to log in through your company's SSO portal, not directly on the Checkout.com Dashboard.
> If they're having trouble, they should contact your IT team to check their SSO access.
> Anything else I can help with?

**Query response — user is not federated**

> That user's account uses standard Checkout.com login — they're not connected to an SSO provider.
> Anything else I can help with?

---

## 8. User MFA status

**API calls:**
1. `GET /umt/users/self/mfa/authenticators` — returns authenticators with `type` and `enrolled` per entry
   `summary` field: `"MFA enrolled: [type, e.g. authenticator app / security key]"` / `"MFA not enrolled"`

**Query response — MFA is enrolled**

> That user has multi-factor authentication set up using **[authenticator type, e.g. "an authenticator app" / "a security key"]**. They'll be asked to verify their identity when they log in.
> Anything else I can help with?

**Query response — MFA is not enrolled**

> That user doesn't have multi-factor authentication set up. If your organisation requires MFA, they won't be able to complete login until it's enrolled.
> They can set up MFA from their account security settings on next login.
> Anything else I can help with?

---

## 9. Get user's account administrator

**API calls:** None — point to Dashboard.

**Response**

> To find out who manages your team's account, go to **Dashboard > Settings > Team**. Users with the Account owner, Admin, or IAM admin role can manage users and permissions.
> If you don't have access to that page, ask a colleague who does to check on your behalf.
> Anything else I can help with?
