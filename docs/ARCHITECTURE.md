# AXORA Workspace Architecture

## Repository strategy

This repository is the shared engineering hub, not automatically the home of every production application.

Prefer a **separate repository** when a project has independent deployment, access permissions, release cadence, secrets, or a distinct technology stack. Use `apps/<project-slug>/` for small demos, experiments, or tightly related prototypes. Put truly reusable code in `packages/<package-name>/` only when there is a real consumer.

## Suggested project layers

1. **Experience:** web UI, mobile UI, or API interface.
2. **Application:** use cases, workflows, validation, and authorization.
3. **Integration:** third-party APIs, payment, email, AI providers, and automation tools.
4. **Data:** persistence, migrations, retention, and backup.
5. **Operations:** logs, health checks, monitoring, release and rollback steps.

Use only the layers a project needs. Avoid premature microservices.

## Architecture decisions

Record consequential choices in `docs/decisions/` with context, options, trade-offs, and consequences. Examples include a database choice, hosting model, authentication design, or a decision to split a service into another repository.

## Standard project README

Every project should describe:
- Purpose and intended users
- Current maturity: concept, prototype, beta, or production
- Features and known limitations
- Stack and prerequisites
- Local installation and run instructions
- Configuration variables (names and safe examples only)
- Test, lint, and build commands
- Deployment and rollback process
- Data flows, external providers, and security considerations
