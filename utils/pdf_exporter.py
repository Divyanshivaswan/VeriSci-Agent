from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_verisci_audit_pdf(audit_data: dict, research_text: str) -> BytesIO:
  """Generates a formal, publication-ready audit certificate and compliance PDF."""
  buffer = BytesIO()
  c = canvas.Canvas(buffer, pagesize=letter)

  # Header Branding
  c.setFont("Helvetica-Bold", 15)
  c.drawString(
      50, 750, "VERISCI AGENT | Autonomous Research & Patent Audit Record"
  )

  c.setFont("Helvetica", 9)
  c.drawString(
      50,
      735,
      "Enterprise Compliance & Multi-Agent Verification Framework (IBM Bob"
      " Orchestrated)",
  )

  # Divider Line
  c.setLineWidth(0.75)
  c.line(50, 725, 560, 725)

  # Executive Summary Section
  c.setFont("Helvetica-Bold", 11)
  c.drawString(50, 700, "1. Executive Audit Overview:")
  c.setFont("Helvetica", 10)

  summary_text = audit_data.get("executive_summary", "")
  c.drawString(50, 683, summary_text[:95])
  if len(summary_text) > 95:
    c.drawString(50, 668, summary_text[95:190])

  # Sub-Agent Findings Breakdown
  c.setFont("Helvetica-Bold", 11)
  c.drawString(50, 635, "2. Multi-Agent Verification Sub-Module Reports:")

  y_pos = 615
  for report in audit_data.get("agent_reports", []):
    c.setFont("Helvetica-Bold", 10)
    c.drawString(60, y_pos, f"• {report.get('agent_name', 'Agent')}:")
    y_pos -= 16

    c.setFont("Helvetica", 9)
    findings = report.get("findings", "")
    c.drawString(75, y_pos, f"Findings: {findings[:85]}")
    y_pos -= 16

    status = (
        report.get("status")
        or report.get("risk_status")
        or report.get("novelty_score")
    )
    c.drawString(75, y_pos, f"Primary Metric Status: {status}")
    y_pos -= 24

  # Input Snippet Reference
  c.setFont("Helvetica-Bold", 11)
  c.drawString(50, y_pos - 10, "3. Audited Source Text Segment:")
  c.setFont("Helvetica-Oblique", 8)
  c.drawString(50, y_pos - 25, f'"{research_text[:110]}..."')

  c.save()
  buffer.seek(0)
  return buffer