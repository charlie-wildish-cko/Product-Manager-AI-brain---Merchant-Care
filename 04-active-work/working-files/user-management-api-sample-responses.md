# User Management API — Sample Response Payloads

Generated from: `user-management-api-endpoints.csv`

---

## Users

### `GET /umt/users/self`
```json
{
  "userId": "usr_abc123def456",
  "email": "jane.smith@acme.com",
  "firstName": "Jane",
  "lastName": "Smith",
  "status": "ACTIVE",
  "createdAt": "2024-03-15T10:22:00Z",
  "lastLoginAt": "2026-05-30T08:45:00Z"
}
```

### `GET /api/cat/users/{userId}` · `GET /api/internal/users/{userId}`
```json
{
  "userId": "usr_abc123def456",
  "email": "jane.smith@acme.com",
  "firstName": "Jane",
  "lastName": "Smith",
  "status": "ACTIVE",
  "clients": [
    {
      "clientId": "cli_9f8e7d6c5b4a",
      "roles": ["DEVELOPER", "ANALYST"]
    }
  ],
  "createdAt": "2024-03-15T10:22:00Z"
}
```

### `GET /api/cat/users/{userId}/members` · `GET /api/internal/users/{userId}/members`
```json
{
  "members": [
    {
      "clientId": "cli_9f8e7d6c5b4a",
      "clientName": "Acme Payments Ltd",
      "roles": ["DEVELOPER"],
      "entityAccess": ["ent_001", "ent_002"],
      "status": "ACTIVE"
    }
  ],
  "total": 1
}
```

---

## Members

### `GET /umt/clients/{clientId}/members` · `GET /api/cat/clients/{clientId}/members` · `GET /api/internal/clients/{clientId}/members`
```json
{
  "data": [
    {
      "userId": "usr_abc123def456",
      "email": "jane.smith@acme.com",
      "firstName": "Jane",
      "lastName": "Smith",
      "roles": ["DEVELOPER"],
      "status": "ACTIVE",
      "invitedAt": "2024-03-10T09:00:00Z",
      "joinedAt": "2024-03-15T10:22:00Z"
    },
    {
      "userId": "usr_xyz789ghi012",
      "email": "bob.jones@acme.com",
      "firstName": "Bob",
      "lastName": "Jones",
      "roles": ["OWNER"],
      "status": "ACTIVE",
      "invitedAt": "2023-11-01T11:00:00Z",
      "joinedAt": "2023-11-01T11:30:00Z"
    }
  ],
  "total": 2,
  "skip": 0,
  "limit": 20
}
```

### `GET /api/cat/clients/{clientId}/members/{userId}` · `GET /api/internal/clients/{clientId}/members/{userId}`
```json
{
  "userId": "usr_abc123def456",
  "email": "jane.smith@acme.com",
  "firstName": "Jane",
  "lastName": "Smith",
  "roles": ["DEVELOPER"],
  "customRoles": [],
  "entityAccess": [
    {
      "entityId": "ent_001",
      "entityName": "Acme EU",
      "segments": ["seg_retail", "seg_online"]
    }
  ],
  "status": "ACTIVE",
  "mfaEnrolled": true
}
```

### `GET /umt/clients/{clientId}/members/users-manage`
```json
{
  "data": [
    {
      "userId": "usr_abc123def456",
      "email": "jane.smith@acme.com",
      "firstName": "Jane",
      "lastName": "Smith",
      "roles": ["ADMIN"],
      "canManageUsers": true
    }
  ],
  "total": 1
}
```

---

## Custom Roles

### `GET /umt/clients/{clientId}/custom-roles`
```json
{
  "data": [
    {
      "customRoleId": "crole_aaa111bbb222",
      "name": "Fraud Analyst",
      "description": "Read-only access to disputes and risk dashboards",
      "permissions": ["disputes:read", "risk:read", "reporting:read"],
      "clientId": "cli_9f8e7d6c5b4a",
      "memberCount": 4,
      "createdAt": "2025-01-20T14:00:00Z"
    }
  ],
  "total": 1
}
```

### `GET /umt/custom-roles/{customRoleId}`
```json
{
  "customRoleId": "crole_aaa111bbb222",
  "name": "Fraud Analyst",
  "description": "Read-only access to disputes and risk dashboards",
  "permissions": ["disputes:read", "risk:read", "reporting:read"],
  "clientId": "cli_9f8e7d6c5b4a",
  "memberCount": 4,
  "etag": "\"v2-abc123\"",
  "createdAt": "2025-01-20T14:00:00Z",
  "updatedAt": "2025-06-01T09:15:00Z"
}
```

---

## SSO

### `GET /api/clients/{clientId}/sso`
```json
{
  "clientId": "cli_9f8e7d6c5b4a",
  "status": "CONFIGURED",
  "idpType": "SAML",
  "idpMetadata": {
    "entityId": "https://idp.acme.com/saml/metadata",
    "ssoUrl": "https://idp.acme.com/saml/sso",
    "certificate": {
      "fingerprint": "AB:CD:EF:12:34:56:...",
      "expiresAt": "2027-03-15T00:00:00Z"
    }
  },
  "roleMapping": {
    "defaultRole": "DEVELOPER",
    "attributeName": "groups",
    "mappings": [
      { "idpValue": "checkout-admins", "role": "ADMIN" },
      { "idpValue": "checkout-devs", "role": "DEVELOPER" }
    ]
  },
  "enforceSso": false,
  "createdAt": "2025-04-10T12:00:00Z"
}
```

### `GET /api/clients/{clientId}/sso/status`
```json
{
  "clientId": "cli_9f8e7d6c5b4a",
  "status": "ENABLED",
  "verified": true,
  "enforceSso": false
}
```

### `GET /api/clients/{clientId}/sso/routing/domain-verification-token`
```json
{
  "clientId": "cli_9f8e7d6c5b4a",
  "token": "checkout-domain-verify-xK9mQ2pL7nRv",
  "instructionsUrl": "https://docs.checkout.com/sso/domain-verification"
}
```

### `GET /api/clients/{clientId}/sso/entity-mapping-entities`
```json
{
  "entities": [
    {
      "entityId": "ent_001",
      "entityName": "Acme EU",
      "idpGroupAttribute": "acme-eu-users",
      "mapped": true
    },
    {
      "entityId": "ent_002",
      "entityName": "Acme US",
      "idpGroupAttribute": null,
      "mapped": false
    }
  ]
}
```

### `GET /api/clients/{clientId}/sso/certificate`
```json
{
  "clientId": "cli_9f8e7d6c5b4a",
  "certificate": {
    "subject": "CN=acme.com",
    "issuer": "CN=Acme Internal CA",
    "fingerprint": "AB:CD:EF:12:34:56:78:90:AB:CD:EF:12:34:56:78:90",
    "validFrom": "2025-03-15T00:00:00Z",
    "expiresAt": "2027-03-15T00:00:00Z"
  }
}
```

---

## Entities & Segments

### `GET /umt/clients/{clientId}/entities`
```json
{
  "data": [
    {
      "entityId": "ent_001",
      "entityName": "Acme EU",
      "defaultCurrency": "EUR",
      "status": "ACTIVE"
    },
    {
      "entityId": "ent_002",
      "entityName": "Acme US",
      "defaultCurrency": "USD",
      "status": "ACTIVE"
    }
  ],
  "total": 2
}
```

### `GET /api/cat/clients/{clientId}/entities/{entityId}/segments/{segmentId}`
```json
{
  "segmentId": "seg_retail",
  "entityId": "ent_001",
  "clientId": "cli_9f8e7d6c5b4a",
  "name": "Retail",
  "description": "Online retail processing channel",
  "status": "ACTIVE",
  "createdAt": "2024-06-01T00:00:00Z"
}
```

---

## User Entitlements

### `GET /api/user-entitlements`
```json
{
  "data": [
    {
      "userId": "usr_abc123def456",
      "email": "jane.smith@acme.com",
      "entityId": "ent_001",
      "entityScope": "ENTITY",
      "entitlements": ["payments:read", "disputes:write", "reporting:read"],
      "grantedAt": "2024-03-15T10:22:00Z"
    }
  ],
  "total": 1
}
```

---

## MFA

### `GET /umt/users/self/mfa/authenticators`
```json
{
  "authenticators": [
    {
      "id": "auth_mfa_001",
      "type": "TOTP",
      "name": "Authenticator App",
      "enrolled": true,
      "enrolledAt": "2025-01-10T09:00:00Z",
      "lastUsedAt": "2026-05-30T08:44:00Z"
    },
    {
      "id": "auth_mfa_002",
      "type": "SMS",
      "name": "+44 7700 *** 123",
      "enrolled": false,
      "enrolledAt": null,
      "lastUsedAt": null
    }
  ]
}
```

### `GET /api/mfa/enrollment/progress`
```json
{
  "clientId": "cli_9f8e7d6c5b4a",
  "totalMembers": 42,
  "enrolled": 38,
  "notEnrolled": 4,
  "enrollmentRate": 0.905,
  "enforcementActive": true,
  "enforceByDate": "2026-06-30T00:00:00Z"
}
```

---

## Well-Known / Discovery

### `GET /.well-known/client-roles`
```json
{
  "roles": [
    { "id": "OWNER", "displayName": "Owner", "description": "Full administrative access" },
    { "id": "ADMIN", "displayName": "Admin", "description": "Manage users and settings" },
    { "id": "DEVELOPER", "displayName": "Developer", "description": "API access and integration management" },
    { "id": "ANALYST", "displayName": "Analyst", "description": "Read-only reporting and analytics" }
  ]
}
```

### `GET /.well-known/custom-roles/permissions`
```json
{
  "permissions": [
    { "id": "payments:read", "group": "Payments", "description": "View payment transactions" },
    { "id": "payments:write", "group": "Payments", "description": "Initiate and manage payments" },
    { "id": "disputes:read", "group": "Disputes", "description": "View dispute cases" },
    { "id": "disputes:write", "group": "Disputes", "description": "Respond to and manage disputes" },
    { "id": "reporting:read", "group": "Reporting", "description": "Access reports and analytics" },
    { "id": "risk:read", "group": "Risk", "description": "View risk and fraud data" }
  ]
}
```

### `GET /.well-known/permission-groups`
```json
{
  "groups": [
    { "id": "Payments", "permissions": ["payments:read", "payments:write"] },
    { "id": "Disputes", "permissions": ["disputes:read", "disputes:write"] },
    { "id": "Reporting", "permissions": ["reporting:read"] },
    { "id": "Risk", "permissions": ["risk:read"] }
  ]
}
```

### `GET /api/supported-idps`
```json
{
  "idps": [
    { "id": "SAML", "displayName": "SAML 2.0", "supported": true },
    { "id": "OIDC", "displayName": "OpenID Connect", "supported": true },
    { "id": "OKTA", "displayName": "Okta (native)", "supported": true },
    { "id": "AZURE_AD", "displayName": "Microsoft Entra ID", "supported": true },
    { "id": "GOOGLE", "displayName": "Google Workspace", "supported": true }
  ]
}
```

---

## Providers

### `GET /api/cat/clients/{clientId}/providers` (via POST response)
```json
{
  "clientId": "cli_9f8e7d6c5b4a",
  "providers": [
    {
      "providerId": "prov_okta_001",
      "providerType": "OKTA",
      "displayName": "Acme Okta",
      "status": "ACTIVE",
      "createdAt": "2025-02-01T00:00:00Z"
    }
  ]
}
```

---

## Migration

### `GET /api/migration/sso-service-init/mismatches`
```json
{
  "data": [
    {
      "clientId": "cli_9f8e7d6c5b4a",
      "userId": "usr_abc123def456",
      "email": "jane.smith@acme.com",
      "mismatchType": "DUPLICATE_EMAIL",
      "details": "User exists in both old and new SSO service with conflicting external IDs"
    }
  ],
  "total": 1,
  "pageIndex": 0,
  "pageLimit": 20
}
```

---

## Error Response (all endpoints)
```json
{
  "requestId": "req_7f3a2c1d9e8b",
  "errorCode": "user_not_found",
  "message": "No user found with the specified userId",
  "statusCode": 404
}
```
