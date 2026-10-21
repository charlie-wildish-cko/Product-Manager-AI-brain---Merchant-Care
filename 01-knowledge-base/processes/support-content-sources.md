# Support content sources (GitHub, org: cko-web)

All four content sets referenced in `CLAUDE.md`'s Key Reference Files table are docs-as-code repos in the `cko-web` GitHub org. `gh api` works for reading (tarball/contents endpoints); `git clone` over HTTPS is blocked by the org's SAML SSO enforcement on the GitHub CLI OAuth app — pull via tarball instead (see below).

| Content | Repo | Path in repo | Local copy |
|---|---|---|---|
| External support articles (public, support.checkout.com) | [cko-web/checkout-support-site](https://github.com/cko-web/checkout-support-site) | `Support articles/` | `01-knowledge-base/Support content/checkout-support-site-main/Support articles/` |
| Internal support articles (Care Agent KB, canonical) | [cko-web/checkout-support-site-internal](https://github.com/cko-web/checkout-support-site-internal) | `Support articles/` | `01-knowledge-base/Support content/checkout-support-site-internal/Support articles/` |
| Tech Docs | [cko-web/checkout-docs-site](https://github.com/cko-web/checkout-docs-site) | `docs/NAS/` (Articles, GetStarted, Home) | `01-knowledge-base/Support content/Tech Docs/` |
| API reference (OpenAPI spec) | [cko-web/checkout-api-reference](https://github.com/cko-web/checkout-api-reference) | `nas_spec/` (swagger.yaml, paths/, components/) | `01-knowledge-base/Support content/API reference/` |

## How the source repos work

Both support-site repos (external and internal) are the same docs-as-code setup: content is authored in Zendesk, synced automatically to the repo's `staging` branch every day at 7AM, and edits flow back to Zendesk via PR merge into `staging`. `staging` — not `main` — is the branch that reflects current published content; `main` has branch protection and nothing deploys from it.

- External repo syncs from the public Zendesk help center (support.checkout.com).
- Internal repo syncs from the internal Zendesk help center (Care Agent KB). The tracked copy under `01-knowledge-base/Support content/checkout-support-site-internal/` is the canonical internal support content (decision 2026-10-21). Organise lookups by its `Support articles/<Category>/...` folders, for example "Case Management" or "Access and Permissions". It has no index file.
- `01-knowledge-base/processes/Care Agent SOPs/` is a deprecated, untracked, flattened copy of the same Zendesk KB (526 articles in 125 topic folders under `zendesk-kb/`, plus `INDEX.md`). It stays on disk and is no longer maintained or synced. Do not cite it in new work. 511 of its article ids exist in the canonical copy. 15 exist only in the old copy, so a reader who needs one of those reads the old folder until it is deleted.

## Re-pulling content

`git clone` fails with a 403 (SSO re-authorization required for the OAuth app). Use the tarball API instead, which works with the existing `gh` keyring auth:

```bash
gh api repos/cko-web/<repo>/tarball/staging > /tmp/pull.tar.gz
mkdir -p /tmp/pull && tar -xzf /tmp/pull.tar.gz -C /tmp/pull --strip-components=1
```

Then copy the relevant subfolder over the local copy. If `GITHUB_TOKEN` is set in the environment, `unset GITHUB_TOKEN` first — `gh` prefers a stale env token over the working keyring credential.

Last pulled: 2026-08-10 (external: 908 articles, internal: 528 articles).
