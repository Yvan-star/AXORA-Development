# AXORA Development

**The shared engineering hub for AXORA's software ecosystem.**

Use this repository to organize product briefs, architecture standards, reusable templates, development workflows, and small experiments. Production applications should generally live in their own repositories when they need independent access controls, deployments, secrets, or release cycles.

> [!IMPORTANT]
> **This repository is public.** Do not commit secrets, API keys, access tokens, private customer data, production exports, confidential roadmaps, or credentials. For confidential AXORA work, use a private repository. A `.gitignore` does not remove a secret already committed.

## Quick start

1. Browse the [project registry](projects/README.md).
2. Create a copy of the [project brief](templates/PROJECT_BRIEF.md) and complete the problem, audience, evidence, scope, and acceptance criteria.
3. Use the [project README template](templates/PROJECT_README.md) in each new app repository.
4. Follow the [development workflow](docs/DEVELOPMENT_WORKFLOW.md).
5. Record major technical choices using the [ADR process](docs/decisions/README.md).
6. Review the [security policy](SECURITY.md) and [project security checklist](docs/SECURITY.md) before demos or releases.

## Workspace map

| Path | Purpose |
|---|---|
| `.github/` | Pull request/issue templates and GitHub Actions |
| `docs/` | Architecture, engineering standards, privacy, operations, release and AI guidance |
| `docs/decisions/` | Architecture Decision Records |
| `projects/` | Central project registry and portfolio planning |
| `templates/` | Reusable project briefs, READMEs and checklists |
| `apps/` | Optional prototypes intentionally housed in this repository |
| `packages/` | Reusable components, only when there is a real consumer |

The `apps/` and `packages/` directories are reserved conventions; each project should add a README and implementation-specific setup when used.

## Repository strategy

- **This repository:** shared standards, templates, records, and small experiments.
- **Separate product repository:** default for applications with independent deployment, dependencies, permissions, secrets, or data.
- **Reusable package:** split out only when multiple projects actually need it.
- **Private repository:** required for confidential source, internal product plans, and private operational data.

## Development principles

- Solve an evidenced problem, not just an interesting technical problem.
- Separate facts, assumptions, and decisions.
- Build a narrow end-to-end slice and test with representative users.
- Use readable code, repeatable setup, small changes, and honest test results.
- Treat security, privacy, accessibility, operating cost, and maintainability as product requirements.
- Review AI-generated code and never let model output alone authorize sensitive actions.
- Label maturity honestly: idea, discovery, prototype, beta, or production.

## Branch, commit, and review conventions

- Branches: `feat/short-name`, `fix/short-name`, `docs/short-name`, `chore/short-name`.
- Commit prefixes: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`.
- Use a pull request for meaningful code and policy changes.
- Include motivation, verification evidence, risk/data changes, and rollback notes.
- Do not claim checks passed unless they were run.

## Quality and release gates

The included workflow performs a limited workspace-structure check. It is **not** a secret scanner, dependency audit, application test suite, or security certification. Each implementation repository must add the checks appropriate to its stack and risk.

Before a production release, verify tests, access controls, secret configuration, data retention/deletion, monitoring, backups, incident response, and rollback.

## Core guides

- [Architecture](docs/ARCHITECTURE.md)
- [Engineering standards](docs/ENGINEERING_STANDARDS.md)
- [Development workflow](docs/DEVELOPMENT_WORKFLOW.md)
- [Security policy](SECURITY.md)
- [Project security checklist](docs/SECURITY.md)
- [Privacy principles](docs/PRIVACY.md)
- [AI system guidelines](docs/AI_SYSTEMS.md)
- [Testing strategy](docs/TESTING_STRATEGY.md)
- [Release management](docs/RELEASE_MANAGEMENT.md)
- [Operations and incident response](docs/OPERATIONS.md)
- [Project registry](projects/README.md)
- [Project brief template](templates/PROJECT_BRIEF.md)

## Current status

This repository provides documentation, workflow conventions, and templates. It does not, by itself, deploy an app, provision cloud resources, connect production services, or constitute a finished AXORA product. Each such capability must be implemented, configured, and verified for the specific project.
