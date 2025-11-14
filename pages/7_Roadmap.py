import streamlit as st

# NDIA heading component
def section_heading(text):
    st.markdown(f"### <span style='color:#6D3078;'>{text}</span>", unsafe_allow_html=True)

st.title("Roadmap & Next Steps")

# -------------------------
# High-Level Plan
# -------------------------
section_heading("High-Level Plan")

st.markdown("""
<div class="card">
    <div class="pill">Overview</div>
    <h3>A staged, low-risk pathway</h3>
    <p>
    The intent is not to initiate a large programme immediately, but to proceed in small, 
    well-governed steps. Each phase generates evidence and artefacts that support future 
    decision-making.
    </p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Phase 1
# -------------------------
section_heading("Phase 1 — Enable the Toolset (0–4 weeks)")

st.markdown("""
<div class="card">
    <h3>Establish the foundation</h3>
    <ul>
        <li>Confirm endorsement from Markets Division leadership.</li>
        <li>Submit a formal request to Digital/IT for a controlled prototyping environment.</li>
        <li>Provision:
            <ul>
                <li>VS Code</li>
                <li>GitHub Enterprise / internal Git repository</li>
                <li>Docker</li>
                <li>Python runtime</li>
                <li>Controlled access to AWS Bedrock (LLMs + embeddings)</li>
            </ul>
        </li>
        <li>Agree basic governance settings and IAM roles.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Phase 2
# -------------------------
section_heading("Phase 2 — First Digital PAPL Demonstrator (4–10 weeks)")

st.markdown("""
<div class="card">
    <h3>Build a minimal, functional proof of concept</h3>
    <ul>
        <li>Select a well-bounded section of PAPL or a Code Guide for conversion.</li>
        <li>Transform the section into structured JSON + Markdown.</li>
        <li>Build a simple API/data layer to serve the structured artefact.</li>
        <li>Create:
            <ul>
                <li>a provider-focused view</li>
                <li>a planner decision-support view</li>
                <li>a participant-friendly plain-language view</li>
            </ul>
        </li>
        <li>Demonstrate to leadership within Markets Delivery and Strategy.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Phase 3
# -------------------------
section_heading("Phase 3 — Evaluation & Refinement (10–14 weeks)")

st.markdown("""
<div class="card">
    <h3>Gather insights and iterate</h3>
    <ul>
        <li>Seek feedback from:
            <ul>
                <li>Markets Strategy & Pricing Teams</li>
                <li>Frontline planners or LACs (internal demonstration only)</li>
                <li>Internal advisory groups</li>
            </ul>
        </li>
        <li>Assess improvements to:
            <ul>
                <li>clarity and interpretability</li>
                <li>manual effort reduction</li>
                <li>market monitoring potential</li>
            </ul>
        </li>
        <li>Refine the prototype based on findings.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Phase 4
# -------------------------
section_heading("Phase 4 — Scaling Options (14+ weeks)")

st.markdown("""
<div class="card">
    <h3>Translate insights into strategic decisions</h3>
    <ul>
        <li>Use the prototype and feedback to propose pathways:
            <ul>
                <li>no further action (prototype value only)</li>
                <li>targeted enhancements to internal guidance tools</li>
                <li>a broader digital-first pricing artefact programme</li>
            </ul>
        </li>
        <li>Identify dependencies (ICT capacity, data integration, policy considerations).</li>
        <li>Prepare material for any future business case, if warranted.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Immediate Next Step
# -------------------------
section_heading("Immediate Next Step")

st.markdown("""
<div class="card">
    <div class="pill">Action</div>
    <h3>What we must do first</h3>
    <p>
    The immediate next step is for Markets Division leadership to confirm support for the 
    required toolset and endorse a formal request to Digital/IT.  
    This prototype site itself forms part of that evidence base.
    </p>
</div>
""", unsafe_allow_html=True)
