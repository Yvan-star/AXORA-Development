# Security Policy

## Scope

This repository supports AXORA development. Security expectations apply to prototypes and production services; prototypes must not be represented as production-secure without a relevant review.

## Reporting a vulnerability

Please do not publish exploitable details, credentials, personal data, or attack instructions in a public issue. Use GitHub's private vulnerability reporting feature if it is enabled for this repository, or contact the repository owner privately through an appropriate channel. Include the affected component, impact, reproduction summary, and suggested mitigation where safe.

## Required practices

- Do not commit secrets. Use GitHub Actions Secrets or an approved secret manager.
- Keep permissions and tokens to the minimum necessary scope.
- Validate input, enforce authorization on the server, and avoid trusting client-side checks.
- Use HTTPS for network traffic and secure cookie/session settings where applicable.
- Store only data required for the product; set retention and deletion expectations.
- Review dependencies and lockfiles; remove packages that are unused or untrusted.
- Do not use real customer information in demos or tests unless explicitly authorized and appropriately protected.
- Back up important data and document recovery steps before production launch.

## Incident response

If a secret is exposed, revoke or rotate it immediately; deleting the file or commit alone is not enough. Assess logs and affected systems, then document remediation without reproducing the secret.
