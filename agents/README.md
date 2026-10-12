# AXORA Agent Runtime

A small safe first implementation of AXORA's task-based agent framework. It uses Python's standard library only and runs locally or in GitHub Actions.

## Working capabilities
- Research: organizes user-supplied source notes; it does not browse or independently verify URLs.
- Product: creates a product brief and validation plan.
- Coding: creates an implementation plan and acceptance checklist; it does not edit source code.
- Quality: checks report completeness.
- Operations: records task metadata and run status.
- Orchestrator: routes tasks using visible keyword rules.
- Intelligence: creates a cautious decision memo from supplied findings.

This is a task runner, not a continuously running multi-agent service. Each run produces a Markdown report and JSON task record.

## Quick start

Requires Python 3.11+; no third-party packages are needed.

    python -m agents run --agent product --task "Design a digital product that helps beginners write better AI prompts"

For research, provide a JSON array of source notes:

    python -m agents run --agent research --task "Assess this opportunity" --sources-file examples/research_sources.json

Reports are saved under outputs/ by default. Use --output-dir to change the destination. Generated outputs are git-ignored; preserve important deliverables separately or download the Actions artifact.

## GitHub Actions

Open Actions → AXORA Agent Run → Run workflow. Select an agent, enter a task, and optionally provide source notes as JSON. The workflow uploads generated files as an artifact.

GitHub Actions does not send messages directly into this ChatGPT conversation. Email, Airtable, or chat notifications need a separately configured integration and credentials.

## Model integration

This initial version is deterministic and dependency-free: it creates structured deliverables without requiring an API key. It does not yet call a language model. A later adapter can connect to local Ollama or an approved model API. Never put API keys in source files or workflow inputs.

## Safety boundaries

- No external writes, deployments, purchases, publishing, or customer messages.
- No autonomous source-code edits.
- Treat task text and source notes as untrusted input.
- Reports distinguish supplied notes from independently verified facts.
- Human review is required before consequential actions.
- Keep confidential information out of this public repository.
