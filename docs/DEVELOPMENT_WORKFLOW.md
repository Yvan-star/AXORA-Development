# AXORA Development Workflow

## 1. Discover
Write the problem statement, target user, evidence, constraints, and measurable outcome. Validate risky assumptions early.

## 2. Plan
Create a project brief, define a small first milestone, list acceptance criteria, and identify data/privacy/security concerns. Record major technical decisions in ADRs.

## 3. Build
Use feature branches and small commits. Keep credentials out of source. Add tests as behavior is implemented and make setup repeatable.

## 4. Verify
Run project-specific format, lint, unit/integration tests, and build checks. Review dependencies and test failure and permission boundaries, not only successful flows.

## 5. Review
Open a pull request describing motivation, changes, test evidence, risks, data flows, and migration/deployment needs. Do not merge unreviewed AI-generated code into sensitive paths.

## 6. Release
Record version and release notes. Check configuration, permissions, monitoring, rollback, backups, and support ownership according to risk. Use a limited rollout when appropriate.

## 7. Learn
Collect proportionate user feedback and product metrics. Track defects and revisit assumptions based on evidence.

## Release maturity
- **Prototype:** demonstrates a concept; may lack hardening and should be labeled accordingly.
- **Beta:** limited users, known limitations, and a feedback path.
- **Production:** reviewed security/privacy, testing, monitoring, recovery, maintenance, and support practices are in place at a level appropriate to risk.
