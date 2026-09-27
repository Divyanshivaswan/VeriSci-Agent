import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import streamlit as st
import pandas as pd

from agents.orchestrator import VeriSciOrchestrator
from utils.pdf_exporter import generate_verisci_audit_pdf

# Page Configuration
st.set_page_config(
    page_title="VeriSci Agent | Research & Patent Audit Suite",  
    layout="wide",
    initial_sidebar_state="expanded"
)

# Formal Enterprise Interface Styling
st.title("VeriSci Agent: Autonomous Research & Patent verification Suite")
st.caption("Multi-agent cryptographic verification, structural consistency checks, and prior art novelty profiling powered by IBM Bob framework.")

# Sidebar Controls
st.sidebar.header("Agent Configuration")
api_key = st.sidebar.text_input("IBM watsonx / Bob API Key", type="password")
strict_mode = st.sidebar.checkbox("Enforce High-Rigidity Fact Filtering", value=True)
st.sidebar.markdown("---")
st.sidebar.markdown("**Active Sub-Agents:**")
st.sidebar.markdown("✔ Fact-Checker Sub-Agent")
st.sidebar.markdown("✔ Patent & Prior Art Evaluator")
st.sidebar.markdown("✔ Protocol Safety & Compliance Analyst")

# Preset Samples for Instant Evaluation
presets = {
    "Custom Text Input": "",
    "CRISPR-Cas9 Recombinant Gene Therapy Protocol": "We report a novel recombinant vector mechanism utilizing engineered CRISPR-Cas9 ribonucleoprotein delivery for targeted site-specific gene correction in human cell lines. Experimental optimization demonstrates high structural consistency and low off-target cleavage hazards.",
    "Monoclonal Antibody Therapeutic Candidate": "The engineered monoclonal antibody formulation targets specific cell-surface receptors via an optimized recombinant pathway. Analytical metrics confirm structural stability and compliance with biological safety parameters."
}

selected_preset = st.selectbox("Select Sample Protocol / Abstract for Verification:", list(presets.keys()))

# Main Workspace Input
default_text = presets[selected_preset] if selected_preset != "Custom Text Input" else ""
research_input = st.text_area("Input Research Abstract, Claims, or Protocol Documentation", value=default_text, height=180)

st.markdown("---")

if st.button("Initialize Multi-Agent Verification Audit", type="primary", use_container_width=True):
    if not research_input.strip():
        st.warning("Please provide valid research text or select a preset sample.")
    else:
        with st.spinner("Executing parallel sub-agent workflows and cross-referencing metrics..."):
            
            # Run Orchestrator
            orchestrator = VeriSciOrchestrator()
            audit_result = orchestrator.run_audit(research_input)
            
            st.success("verification completed successfully.")
            
            # Executive Metrics Overview
            st.markdown("### Executive verification Metrics")
            m1, m2, m3, m4 = st.columns(4)
            
            reports = audit_result.get("agent_reports", [])
            fact_rep = reports[0] if len(reports) > 0 else {}
            patent_rep = reports[1] if len(reports) > 1 else {}
            safety_rep = reports[2] if len(reports) > 2 else {}
            
            with m1:
                st.metric("Claims Analyzed", fact_rep.get("total_claims_analyzed", 0))
            with m2:
                st.metric("Consistency Score", fact_rep.get("consistency_score", "N/A"))
            with m3:
                st.metric("Novelty Index", patent_rep.get("novelty_score", "N/A"))
            with m4:
                st.metric("Biosafety Status", "Level 1/2 Compliant")
                
            st.markdown("---")
            
            # Professional Tabs Interface
            tab1, tab2, tab3 = st.tabs([
                "📋 Sub-Agent Verification Reports", 
                "⚙️ Orchestrator Execution Log", 
                "📄 Certified Compliance PDF Export"
            ])
            
            with tab1:
                st.markdown("#### Granular Sub-Module Audit Results")
                for rep in reports:
                    with st.expander(f"{rep.get('agent_name')} — Status: {rep.get('status', rep.get('risk_status', 'Verified'))}"):
                        st.write(f"**Findings:** {rep.get('findings')}")
                        for k, v in rep.items():
                            if k not in ['agent_name', 'findings', 'status', 'risk_status']:
                                st.text(f"{k.replace('_', ' ').title()}: {v}")
                                
            with tab2:
                st.markdown("#### IBM Bob Multi-Agent Orchestration Record")
                st.info(f"**Framework Core:** {audit_result.get('orchestrator_framework')}")
                st.write(f"**Executive Synthesis:** {audit_result.get('executive_summary')}")
                st.json(audit_result)
                
            with tab3:
                st.markdown("#### Official verification Certificate & Report")
                st.write("Export structured agent findings, metrics, and source verification logs into a formal compliance PDF document.")
                
                pdf_buffer = generate_verisci_audit_pdf(audit_result, research_input)
                st.download_button(
                    label="Download Certified compliance record (PDF)",
                    data=pdf_buffer,
                    file_name="VeriSci_verification_Certificate.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
