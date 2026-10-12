# AXORA Security Checklist

Use this checklist during design, before public demos, and before production release.

## Design
- [ ] Identify sensitive data, trust boundaries, external APIs, and abuse cases.
- [ ] Choose the minimum authentication and authorization model that fits the product.
- [ ] Set data minimization, retention, deletion, and backup expectations.

## Implementation
- [ ] Secrets are held in environment configuration or a secret manager, never in source.
- [ ] Server-side authorization protects every sensitive operation.
- [ ] Inputs are validated; outputs are safely encoded for their context.
- [ ] Dependencies are known, maintained, and reviewed.
- [ ] Logs do not contain credentials, session tokens, or unnecessary personal data.
- [ ] Rate limits and cost controls protect public-facing and AI-powered endpoints.

## Release
- [ ] Production configuration is separate from local and test configuration.
- [ ] Access is least-privilege and recovery contacts are known.
- [ ] Relevant tests and dependency/security checks have been run.
- [ ] Backups, monitoring, incident response, and rollback have been considered.
- [ ] Privacy notice and user-facing claims match actual behavior.

This is a practical checklist, not a formal security certification or substitute for specialist review where risk warrants it.
