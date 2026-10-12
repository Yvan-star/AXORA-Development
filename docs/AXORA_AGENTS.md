# AXORA Agent Operations

## Purpose
The agent runner is an initial low-risk automation layer for structured task deliverables. It is not a fully autonomous business operator and does not currently call an LLM.

## Run locally
From the repository root with Python 3.11 or later:

    python -m agents run --agent orchestrator --task "Research the market for a student study planner"
    python -m agents run --agent research --task "Summarize the evidence" --sources-file examples/research_sources.json
    python -m unittest discover -s tests -v

Each run writes a Markdown report and JSON record. The record includes agent selection, timestamp, quality checks, limitations, and external actions (empty in this version).

## Run in GitHub
1. Open the repository Actions tab.
2. Select AXORA Agent Run.
3. Choose an agent, enter a task, and optionally supply a JSON array of source notes.
4. Run the workflow.
5. Download the axora-agent-output artifact from the completed run.

The workflow is manually triggered; it does not run continuously. Its repository contents permission is read-only.

## Capability matrix
| Agent | Current capability | Not yet implemented |
|---|---|---|
| Orchestrator | Transparent keyword routing | Multi-step delegation and shared memory |
| Research | Structures supplied source notes and flags evidence gaps | Live browsing and source verification |
| Product | Draft product brief and validation plan | User research integrations and publishing |
| Coding | Implementation plan | Repository edits and coding-model execution |
| Quality | Basic completeness checks | Domain-specific evaluation |
| Operations | Run record | Airtable writes, notifications, cross-service retries |
| Intelligence | Cautious memo from supplied notes | Validated forecasting and external data feeds |

## Delivery
GitHub Actions attaches output files as a downloadable artifact and writes a short job summary. It cannot automatically deliver a message into this ChatGPT conversation. For additional delivery, implement and test one supported channel such as email or Airtable, using least-privilege credentials stored as repository secrets, never in source code.

## Security and approval gates
This repository is public. Do not submit confidential data, API keys, customer information, or private plans in workflow inputs or commits. Workflow inputs and artifacts may be visible to repository collaborators.

The initial implementation takes no external actions. Keep external writes, spending, publication, deployments, customer messaging, and autonomous code changes disabled until permission controls, audit trails, rollback plans, and human approval exist.

## Next milestones
1. Run tests and one sample workflow.
2. Add an optional LLM adapter with safe timeouts.
3. Add source retrieval with explicit source policies and citation validation.
4. Add a persistent task queue if recurring jobs are needed.
5. Integrate Airtable or notifications after defining data and permissions.
6. Add a dashboard after task and output contracts are stable.
