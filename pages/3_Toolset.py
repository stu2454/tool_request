import streamlit as st

# NDIA heading component
def section_heading(text):
    st.markdown(f"### <span style='color:#6D3078;'>{text}</span>", unsafe_allow_html=True)

st.title("Required Toolset")

# -------------------------
# Overview
# -------------------------
section_heading("Overview")

st.markdown("""
<div class="card">
    <div class="pill">Why tools matter</div>
    <h3>Why modern tooling is essential</h3>
    <p>
    Modernising pricing artefacts is not simply a publishing task. It requires:
    </p>
    <ul>
        <li>converting documents into structured formats (JSON, Markdown, YAML)</li>
        <li>building lightweight APIs and interfaces</li>
        <li>experimenting with semantic search</li>
        <li>demonstrating concepts to leadership</li>
    </ul>
    <p>
    A modest, well-governed set of tools enables all of this safely and efficiently.
    </p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Engineering Tools
# -------------------------
section_heading("Core Development Tools")

st.markdown("""
<div class="card">
    <div class="pill">Engineering</div>
    <h3>Standard development tools</h3>
    <p>These tools are common across the APS and low-risk:</p>
    <ul>
        <li><b>VS Code</b> — modern, accessible coding environment.</li>
        <li><b>GitHub Enterprise / internal Git</b> — version control and audit trail.</li>
        <li><b>Python 3.11+</b> — for transformation, APIs and back-end logic.</li>
        <li><b>Docker</b> — ensures clean, reproducible environments.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# -------------------------
# AI & Search Tools
# -------------------------
section_heading("AI & Search")

st.markdown("""
<div class="card">
    <div class="pill">AI & Semantic Search</div>
    <h3>Tools enabling structured interrogation</h3>
    <p>
    For pricing artefacts to become digital-first, NDIA needs controlled access to:
    </p>
    <ul>
        <li><b>AWS Bedrock</b> — secure access to large language models.</li>
        <li><b>Embedding models</b> — enabling semantic search across structured artefacts.</li>
        <li><b>Internal storage (S3)</b> — hosting structured artefact sources.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# -------------------------
# User Interface Tools
# -------------------------
section_heading("User Interface Frameworks")

st.markdown("""
<div class="card">
    <div class="pill">UI Frameworks</div>
    <h3>Tools for demonstrating ideas</h3>
    <p>
    These frameworks help prototype internal-only tools:
    </p>
    <ul>
        <li><b>Streamlit</b> — fast, accessible prototypes and dashboards.</li>
        <li><b>Reflex</b> — app-like UI using only Python.</li>
        <li><b>FastAPI + Tailwind/HTMX</b> — flexible lightweight interfaces.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Governance Flow
# -------------------------
section_heading("Prototype Governance Flow")

st.markdown("""
<div class="card">
    <p>
    The diagram below illustrates how low-risk prototypes flow through governance into evidence for 
    leadership decision-making.
    </p>
</div>
""", unsafe_allow_html=True)

try:
    st.image(
        "assets/diagram_governance_flow.png",
        caption="Prototype Governance Flow",
        #use_column_width=True,
    )
except:
    st.info("Add diagram_governance_flow.png to assets/ to display the image.")
