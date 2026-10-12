# AXORA Testing Strategy

Choose test depth based on product risk and complexity.

## Test layers
- **Unit:** pure business rules and edge cases.
- **Integration:** database, filesystem, external provider wrappers, queues, and internal service boundaries.
- **Contract:** API schemas and integration assumptions.
- **End-to-end:** key user workflows through the real application boundary.
- **Security:** authorization boundaries, input validation, abuse limits, secret handling, and dependency review.
- **Accessibility/usability:** keyboard flows, focus, labels, contrast, responsive layouts, and clear recovery from errors.

## Minimum expectations
- Tests must be repeatable and independent of production data.
- Use synthetic data and test credentials.
- Do not call paid APIs in ordinary tests unless deliberately configured and cost-bounded.
- Test failures, timeouts, permission denial, invalid input, and partial success.
- Keep flaky tests visible and fix or quarantine them intentionally.
- Test migrations and backup/restore procedures when data risk warrants it.

## Pull request test report
State:
- Commands executed
- Pass/fail results
- Tests not run and why
- Remaining risks or manual checks
- Any test data or environment requirements

Never claim that a build, test suite, penetration test, or deployment succeeded unless the action actually completed.
