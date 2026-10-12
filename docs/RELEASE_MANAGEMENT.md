# AXORA Release Management

## Release levels
- **Internal experiment:** limited to developers; can change frequently.
- **Prototype:** proves a concept; known gaps are documented.
- **Beta:** limited user group, support/feedback path, and rollback plan.
- **Production:** required security, privacy, reliability, support, and recovery practices are operational.

## Before release
- [ ] Acceptance criteria and relevant tests pass
- [ ] Dependency and configuration changes reviewed
- [ ] Secrets are configured outside the repository
- [ ] Data migration and compatibility risks reviewed
- [ ] Privacy/security review complete for the release risk
- [ ] Monitoring, error reporting, and support owner identified
- [ ] Backup and rollback/recovery steps tested where relevant
- [ ] User-facing notes and known limitations prepared

## Release notes
Include version/date, user-visible changes, fixes, known issues, migration/configuration changes, and any action required from users or operators.

## Rollback
Define the rollback trigger, accountable operator, prior version or recovery point, data compatibility concerns, communications, and post-rollback verification. A code rollback may not reverse a data migration or external side effect.
