from .audit_subagents import (
    FactCheckerAgent,
    PatentAuditorAgent,
    ProtocolSafetyAgent,
)


class VeriSciOrchestrator:
  """Orchestrates multi-agent analysis for research claims and patent audits."""

  def __init__(self):
    self.fact_checker = FactCheckerAgent()
    self.patent_auditor = PatentAuditorAgent()
    self.safety_agent = ProtocolSafetyAgent()

  def run_audit(self, research_text: str) -> dict:
    # Execute sub-agents
    fact_result = self.fact_checker.analyze(research_text)
    patent_result = self.patent_auditor.analyze(research_text)
    safety_result = self.safety_agent.analyze(research_text)

    # Aggregate executive summary
    summary = (
        "Multi-agent verification completed successfully. "
        f"Consistency score: {fact_result['consistency_score']}, "
        f"Novelty index: {patent_result['novelty_score']}, "
        f"Safety status: {safety_result['risk_status']}."
    )

    return {
        "orchestrator_framework": (
            "IBM Bob Multi-Agent Framework (VeriSci Core)"
        ),
        "executive_summary": summary,
        "agent_reports": [fact_result, patent_result, safety_result],
    }
