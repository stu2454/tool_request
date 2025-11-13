import streamlit as st

st.title("Required Toolset")

st.markdown("""
<div class="card">
    <div class="pill">Overview</div>
    <h3>Why tools matter for digital-first artefacts</h3>
    <p>
    Modernising pricing artefacts is not simply a publishing exercise. It requires the ability to:
    </p>
    <ul>
        <li>convert documents into structured data (JSON, Markdown, YAML)</li>
        <li>build and run small internal APIs and user interfaces</li>
        <li>experiment with semantic search and AI-assisted interrogation</li>
        <li>show senior leaders and colleagues what a digital-first future might look like</li>
    </ul>
    <p>
    To do this quickly, safely and cheaply, the Markets Delivery Branch needs access to a modest, 
    well-governed development environment.
    </p>
</div>
""", unsafe_allow_html=True)

col_eng, col_ai = st.columns(2)

with col_eng:
    st.markdown("""
    <div class="card">
        <div class="pill">Engineering</div>
        <h3>Core development tools</h3>
        <p>These tools are standard, widely used and low-risk:</p>
        <ul>
            <li><b>VS Code</b> – a modern coding environment with good support for Python and Git.</li>
            <li><b>GitHub Enterprise / internal Git</b> – version control, audit trails, collaboration.</li>
            <li><b>Python 3.11+</b> – for data transformation, APIs and back-end logic.</li>
            <li><b>Docker</b> – containerised, reproducible environments.</li>
        </ul>
        <p>
        Together, these provide a foundation for building and sharing prototypes without burdening ICT.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_ai:
    st.markdown("""
    <div class="card">
        <div class="pill">AI & Search</div>
        <h3>Semantic search and interrogation</h3>
        <p>
        For pricing artefacts to be truly digital-first, NDIA needs to support structured search and 
        question-and-answer style interrogation. This requires:
        </p>
        <ul>
            <li><b>AWS Bedrock</b> – access to approved large language models and embeddings.</li>
            <li><b>Embeddings store</b> – to support semantic search across PAPL and related documents.</li>
            <li><b>Internal storage (S3)</b> – for JSON/Markdown versions of artefacts and indexes.</li>
        </ul>
        <p>
        These capabilities build directly on the internal precedent established by the Bridgman/Mane prototype.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">User Interfaces</div>
    <h3>Frameworks for safe internal demonstrators</h3>
    <p>
    To help colleagues and leaders understand what digital-first artefacts can deliver, we need the ability 
    to build simple, internal-only user interfaces:
    </p>
    <ul>
        <li><b>Streamlit</b> – fast, data-centric prototypes and dashboards.</li>
        <li><b>Reflex</b> – modern, app-like interfaces, while still writing in Python.</li>
        <li><b>FastAPI + HTMX + Tailwind</b> – lightweight, accessible web interfaces where needed.</li>
    </ul>
    <p>
    These are not production frameworks in this context; they are tools for thinking, testing and 
    demonstrating possibilities.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">Governance</div>
    <h3>How prototypes flow through governance</h3>
    <p>
    The diagram below illustrates a controlled governance flow for prototypes: from idea, to low-risk 
    experiments, to review, to stewardship assessment and then to recommendations for leadership.
    </p>
</div>
""", unsafe_allow_html=True)

try:
    st.image(
        "assets/diagram_governance_flow.png",
        caption="Prototype Governance Flow – from idea to recommendation.",
        use_container_width=True,
    )
except Exception:
    st.info("Add 'diagram_governance_flow.png' to the assets folder to display this diagram.")
