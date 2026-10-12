import json
import tempfile
import unittest
from pathlib import Path

from agents.__main__ import load_sources, quality_check, research_report, route_agent, run_agent


class AgentTests(unittest.TestCase):
    def test_orchestrator_routes_research(self):
        self.assertEqual(route_agent("Research market trends"), "research")

    def test_product_report_is_explicitly_a_hypothesis(self):
        _, report = run_agent("product", "A study planner for students", [])
        self.assertIn("not market-validated", report)
        self.assertIn("Validation plan", report)

    def test_research_report_discloses_missing_sources(self):
        report = research_report("Compare options", [])
        self.assertIn("No source notes were supplied", report)
        self.assertIn("did not browse", report)

    def test_quality_checks_pass_for_generated_report(self):
        report = research_report("Research question", [])
        self.assertTrue(quality_check("Research question", report)["passed"])

    def test_sources_file_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            source_file = Path(tmp) / "sources.json"
            source_file.write_text(json.dumps([{
                "title": "Example", "url": "https://example.com", "notes": "Sample note"
            }]), encoding="utf-8")
            sources = load_sources(str(source_file))
            self.assertEqual(sources[0]["title"], "Example")
            self.assertEqual(len(sources), 1)

    def test_empty_task_is_rejected_by_cli(self):
        from agents.__main__ import main
        self.assertEqual(main(["run", "--task", "   "]), 2)


if __name__ == "__main__":
    unittest.main()
