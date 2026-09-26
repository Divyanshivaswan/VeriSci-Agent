# VeriSci Platform: Autonomous Research & Patent Verification Suite

> An enterprise-grade, multi-agent computational verification engine designed for real-time claim consistency checking, prior art novelty profiling, and biosafety compliance auditing.

---

## Executive Overview
**VeriSci Platform** automates the rigorous, time-consuming manual workflows required in scientific research, clinical trial protocol evaluation, and intellectual property (IP) patent auditing. By leveraging a multi-agent orchestration architecture integrated with live **NCBI PubMed REST APIs**, VeriSci cross-references user-submitted research abstracts against real-world literature in real time.

---

## Core Architecture & Agents

1. **Fact-Checker Agent**: Extracts structural assertions and performs dynamic literature retrieval via NCBI PubMed E-utilities to evaluate logical consistency.
2. **Patent & Prior Art Auditor**: Scans text for priority scientific markers (e.g., *engineered, CRISPR, recombinant, monoclonal*) to compute an intellectual property novelty index.
3. **Protocol Safety & Compliance Analyst**: Flags high-containment biosafety elements (*pathogens, toxins, BSL-3 markers*) to ensure strict adherence to regulatory safety standards.
4. **Certified PDF Report Exporter**: Generates formal, publication-ready compliance audit records and certificates using ReportLab.

---

## Technology Stack
* **Python** (Core Logic & Orchestration)
* **Streamlit** (Enterprise Research Console Interface)
* **Requests & XML** (Live NCBI PubMed REST API Integration)
* **ReportLab** (Certified Compliance PDF Generation)
* **Pandas** (Structured Data Management)

---

## 📂 Project Directory Structure

```text
VeriSci-Agent/
│
├── agents/
│   ├── __init__.py
│   ├── audit_subagents.py    # Houses Fact-Checker, Patent Auditor, & Safety Analyst agents
│   └── orchestrator.py       # Multi-agent coordination and execution pipeline
│
├── utils/
│   ├── __init__.py
│   └── pdf_exporter.py       # Certified compliance PDF report generation module
│
├── app.py                    # Main Streamlit enterprise research console
├── rag_engine.py             # Live NCBI PubMed REST API retrieval client
└── README.md                 # System documentation

```
---


## **1. Clone the Repository**
'''bash
git clone [https://github.com/Divyanshivaswan/VeriSci-Agent.git](https://github.com/Divyanshivaswan/VeriSci-Agent.git)
cd VeriSci-Agent

**2. Create and Activate Virtual Environment** \
python -m venv venv 

 On Windows PowerShell: \
.\venv\Scripts\Activate

 On macOS / Linux: \
source venv/bin/activate

**3. Install Dependencies**
'''bash
pip install streamlit pandas reportlab requests

**4. Launch the Console**
'''bash
streamlit run app.py
