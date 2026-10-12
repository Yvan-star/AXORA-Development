# Security Policy

## Scope

This repository provides shared AXORA engineering guidance and may contain experiments. A prototype is not production-secure just because it runs.

## Reporting a vulnerability

Please do not disclose exploitable details, credentials, or personal data in a public issue. Use GitHub's private vulnerability reporting feature if enabled, or contact the repository owner privately through an appropriate channel. Include the affected component, impact, and a safe reproduction summary.

## Minimum expectations

- Keep credentials outside version control. Use GitHub Actions Secrets or an approved secret manager.
- Grant the least privilege necessary to users, apps, tokens, and automation.
- Validate input and enforce access control on the server.
- Use secure network transport and session handling where applicable.
- Minimize data collection and define access, retention, deletion, and recovery.
- Review dependency provenance, maintenance, and security advisories.
- Use synthetic or anonymized data in demos and tests by default.
- Add appropriate rate limits, cost ceilings, and abuse protections to public and AI-powered services.

## Exposed-secret response

Revoke or rotate exposed credentials immediately. Removing a file or rewriting history does not make an exposed credential safe again. Assess affected systems, review relevant logs, and document remediation without repeating the secret.

## Limitations

This policy does not certify that code or deployed services are secure. Product-specific risk assessment and specialist review may be necessary.
