# Environment Configuration

## Rules
- Commit a safe `.env.example` listing variable names and non-sensitive placeholders, not actual values.
- Keep local `.env` files untracked.
- Store deployment credentials in the platform's secret manager or GitHub Actions Secrets.
- Separate development, test, staging, and production configurations.
- Validate required configuration at application startup and fail with a safe, actionable error.
- Rotate exposed credentials immediately; do not treat deleting a commit as revocation.

## Documentation example
| Variable | Required | Purpose | Example |
|---|---|---|---|
| `APP_ENV` | Yes | Runtime environment | `development` |
| `SERVICE_BASE_URL` | Depends | External service endpoint | `https://example.invalid` |
| `PROVIDER_API_KEY` | Depends | Provider authentication | `<set in secret manager>` |

Only include variables used by the actual project. Never include real production endpoints if confidential, tokens, passwords, private keys, or personal data.
