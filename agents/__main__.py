"""Dependency-free task runner for AXORA agents."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

AGENTS = {"orchestrator", "research", "product", "coding", "quality", "operations", "intelligence"}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slugify(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return value[:48].strip("-") or "task"


def load_sources(path: str | None) -> list[dict[str, str]]:
    if not path:
        return []
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError("Sources file must contain a JSON array of objects.")
    sources = []
    for index, item in enumerate(raw, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Source item {index} must be an object.")
        sources.append({
            "title": str(item.get("title", f"Source {index}"))[:200],
            "url": str(item.get("url", ""))[:1000],
            "notes": str(item.get("notes", ""))[:8000],
        })
    return sources


def research_report(task: str, sources: list[dict[str, str]]) -> str:
    lines = [
        "# AXORA Research Report", "",
        f"**Task:** {task}", f"**Generated (UTC):** {utc_now()}", "",
        "## Scope and evidence limits", "",
        "This report organizes the task and source notes supplied to the runner. "
        "The runner did not browse the web or independently verify sources. "
        "Treat unverified statements as hypotheses until checked.", "",
        "## Research question", "", task, "", "## Supplied source notes", ""
    ]
    if not sources:
        lines.extend([
            "No source notes were supplied. This is a research plan, not a completed evidence review.", "",
            "### Suggested next steps", "",
            "1. Define the target audience and the decision this research must support.",
            "2. Collect current, credible sources and record their publication dates.",
            "3. Extract findings, evidence, counter-evidence, and unresolved questions.",
            "4. Re-run this agent with a JSON source file containing title, URL, and notes."
        ])
    else:
        for index, source in enumerate(sources, start=1):
            lines.extend([
                f"### {index}. {source['title']}", "",
                f"- **URL:** {source['url'] or 'Not supplied'}", "",
                "**Supplied notes (not independently verified):**", "",
                source["notes"] or "No notes supplied.", ""
            ])
        lines.extend([
            "## Preliminary synthesis", "",
            "Treat supplied notes as leads, not independently validated conclusions. "
            "Compare sources for date, authority, incentives, and disagreement before deciding.", "",
            "## Gaps to resolve", "",
            "- Which claims are supported by more than one independent source?",
            "- Are the sources recent enough for the decision?",
            "- What evidence would disconfirm the leading interpretation?",
            "- What user or market validation is still needed?"
        ])
    return "\n".join(lines) + "\n"


def product_report(task: str) -> str:
    return f"""# AXORA Product Brief

**Task:** {task}
**Generated (UTC):** {utc_now()}
**Maturity:** Draft hypothesis - not market-validated

## Problem hypothesis
What specific, recurring problem is the intended user trying to solve in the context of: {task}

## Target user
Define one primary user segment. Identify their current workaround, urgency, and ability or willingness to pay.

## Proposed value
Describe the smallest outcome that would make the task meaningfully easier, faster, clearer, or less error-prone. Do not claim demand without evidence.

## MVP scope
- One core user journey
- One clear input and one useful output
- Basic error handling and accessible instructions
- A way to collect feedback

## Out of scope for the first version
- Complex integrations before user demand is validated
- Automated spending, publishing, or external writes
- Claims of guaranteed income or guaranteed results

## Validation plan
1. Interview or observe 5-10 target users where appropriate.
2. Test a landing page, sample output, or clickable prototype.
3. Measure task completion and credible willingness to pay.
4. Record negative feedback and competing alternatives.
5. Continue only if evidence supports the problem and solution.

## Risks and assumptions
- The problem is frequent and costly enough to matter.
- The solution is meaningfully better than existing workarounds.
- Distribution and support costs do not exceed realistic revenue.

## Acceptance criteria
- The target user and problem are specific.
- The MVP can be explained in one sentence.
- Each key assumption has a validation method.
- No unsupported market-size, revenue, or performance claims are presented.
"""


def coding_report(task: str) -> str:
    return f"""# AXORA Implementation Plan

**Task:** {task}
**Generated (UTC):** {utc_now()}
**Status:** Planning output only; no source code was changed.

## Goal
Translate the request into a testable software change: {task}

## Proposed steps
1. Inspect the current architecture and identify the smallest safe change.
2. Define input/output contracts and error states before implementation.
3. Implement the narrowest vertical slice.
4. Add tests for success, invalid input, and failure paths.
5. Run tests and security checks; record exact results.
6. Submit changes for human review before merging or deployment.

## Acceptance checklist
- [ ] Requirements and non-goals are explicit.
- [ ] Existing behavior is preserved unless a change is intended.
- [ ] Tests cover core behavior and edge cases.
- [ ] No credentials or personal data are committed.
- [ ] Dependencies and operating costs are documented.
- [ ] Deployment, publication, and external writes remain approval-gated.

## Missing information
Inspect the target repository, stack, existing tests, and deployment constraints before coding.
"""


def intelligence_report(task: str, sources: list[dict[str, str]]) -> str:
    evidence = "\n".join(
        f"- **{source['title']}** ({source['url'] or 'no URL'}): "
        f"{source['notes'] or 'No notes supplied.'}"
        for source in sources
    ) or "- No findings or source notes supplied."
    return f"""# AXORA Decision Memo

**Question:** {task}
**Generated (UTC):** {utc_now()}

## Evidence provided
{evidence}

## What can be concluded
Only supplied notes are available to this run. No independent verification or live research was performed.

## Decision
Do not treat this as a final recommendation until the evidence gaps below are resolved.

## Evidence gaps
- Source credibility, recency, and independence are not verified.
- Alternative explanations and disconfirming evidence are not provided.
- Success criteria and downside risks should be defined before committing resources.

## Next action
Gather current evidence, compare at least one alternative, and define a low-cost test that can invalidate the leading hypothesis.
"""


def route_agent(task: str) -> str:
    lowered = task.lower()
    if any(word in lowered for word in ("research", "market", "competitor", "industry", "evidence", "trend")):
        return "research"
    if any(word in lowered for word in ("code", "software", "app", "website", "bug", "implement", "feature")):
        return "coding"
    if any(word in lowered for word in ("product", "mvp", "customer", "sell", "digital product", "business idea")):
        return "product"
    if any(word in lowered for word in ("decision", "recommend", "compare", "strategy", "prioritize")):
        return "intelligence"
    return "product"


def quality_check(task: str, report: str) -> dict[str, Any]:
    checks = {
        "task_present": bool(task.strip()),
        "report_nonempty": bool(report.strip()),
        "has_heading": report.lstrip().startswith("# "),
        "has_generated_timestamp": "Generated (UTC):" in report,
        "has_limitations": any(word in report.lower() for word in (
            "not independently verified", "not market-validated", "planning output only",
            "no independent verification", "did not browse"
        )),
    }
    return {"passed": all(checks.values()), "checks": checks}


def run_agent(agent: str, task: str, sources: list[dict[str, str]]) -> tuple[str, str]:
    if agent == "orchestrator":
        routed = route_agent(task)
        _, report = run_agent(routed, task, sources)
        return f"orchestrator->{routed}", report
    if agent == "research":
        return agent, research_report(task, sources)
    if agent == "product":
        return agent, product_report(task)
    if agent == "coding":
        return agent, coding_report(task)
    if agent == "intelligence":
        return agent, intelligence_report(task, sources)
    if agent == "quality":
        report = research_report(task, sources)
        return agent, "# AXORA Quality Report\n\n" + json.dumps(quality_check(task, report), indent=2) + "\n\n" + report
    if agent == "operations":
        return agent, (
            "# AXORA Operations Run\n\n"
            f"**Task:** {task}\n**Generated (UTC):** {utc_now()}\n\n"
            "This run creates a status report only. No external systems were changed.\n"
        )
    raise ValueError(f"Unsupported agent: {agent}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run an AXORA task agent.")
    parser.add_argument("command", choices=["run"], help="Run an agent task.")
    parser.add_argument("--agent", choices=sorted(AGENTS), default="orchestrator")
    parser.add_argument("--task", required=True, help="Task to process.")
    parser.add_argument("--sources-file", help="Optional JSON array of source note objects.")
    parser.add_argument("--output-dir", default="outputs", help="Directory for reports and task records.")
    args = parser.parse_args(argv)

    try:
        if not args.task.strip():
            raise ValueError("Task must not be empty.")
        sources = load_sources(args.sources_file)
        agent_used, report = run_agent(args.agent, args.task.strip(), sources)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    stem = f"{stamp}-{slugify(args.task)}"
    report_path = output_dir / f"{stem}.md"
    record_path = output_dir / f"{stem}.json"
    checks = quality_check(args.task, report)
    report_path.write_text(report, encoding="utf-8")
    record = {
        "task_id": stem,
        "requested_agent": args.agent,
        "agent_used": agent_used,
        "task": args.task,
        "status": "completed" if checks["passed"] else "needs_review",
        "created_at_utc": utc_now(),
        "sources_supplied": len(sources),
        "quality_checks": checks,
        "report_path": str(report_path),
        "record_path": str(record_path),
        "external_actions_taken": [],
        "model_used": None,
        "limitations": ["No live browsing or LLM call is performed by this version."]
    }
    record_path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2))
    return 0 if checks["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
