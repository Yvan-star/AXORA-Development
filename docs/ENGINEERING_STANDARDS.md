# Engineering Standards

## General

- Choose the simplest architecture that meets the current, demonstrated need.
- Prefer explicit types, clear names, small modules, and predictable error handling.
- Validate input at trust boundaries and handle failures without leaking sensitive details.
- Avoid hard-coded credentials, environment-specific URLs, and hidden dependencies.
- Pin and update dependencies deliberately; review release notes and security advisories.
- Make setup reproducible with lockfiles and documented commands when the chosen stack supports them.

## Testing

- Test important behavior and failure paths, not only happy paths.
- Include regression tests for fixed bugs where practical.
- Use synthetic or anonymized data by default.
- Never claim a test passed unless it was actually run.

## API and data

- Document API contracts and error responses.
- Authenticate and authorize on the server for protected actions.
- Apply least privilege to database and service accounts.
- Keep personal data collection minimal and define purpose, retention, export, and deletion behavior.
- Add migrations and recovery guidance for persisted data changes.

## AI features

- Document provider, expected input/output, limitations, and fallback behavior.
- Treat user content and retrieved documents as untrusted input.
- Do not allow model output alone to authorize sensitive actions.
- Consider prompt injection, data leakage, cost limits, rate limits, and evaluation cases.
- Provide human review for consequential or irreversible operations.

## Accessibility and usability

- Use semantic structure, keyboard accessibility, visible focus, and readable contrast.
- Provide useful error states and loading states.
- Test responsive behavior on practical screen sizes.

## Releases

- Record version, major changes, known issues, and rollback steps.
- Use staging or a limited beta before production where feasible.
- Verify monitoring, backups, permissions, and secret configuration before launch.
