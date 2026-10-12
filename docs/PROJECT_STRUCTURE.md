# Recommended Project Structure

Adapt this example to the selected stack; do not create every directory by default.

```text
project-name/
├── README.md
├── LICENSE                 # only when licensing intent is clear
├── .gitignore
├── .env.example            # safe variable names/placeholders only
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DATA_FLOWS.md
│   ├── OPERATIONS.md
│   └── decisions/
├── src/
│   ├── app/                # framework-specific entry points
│   ├── domain/             # core business rules
│   ├── integrations/       # third-party service adapters
│   └── shared/             # only genuinely shared app code
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
└── .github/
    ├── workflows/
    └── pull_request_template.md
```

## Rules of thumb
- Follow established conventions of the chosen framework.
- Keep secrets, local databases, generated builds, and test artifacts out of Git.
- Do not create abstraction layers without a concrete use case.
- Keep migrations and data recovery instructions close to the data layer.
- Document external services and data flows before adding real credentials.
