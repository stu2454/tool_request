import streamlit as st

# NDIA heading component
def section_heading(text):
    st.markdown(f"### <span style='color:#6D3078;'>{text}</span>", unsafe_allow_html=True)

st.title("Evidence Showcase")

# -------------------------
# Overview
# -------------------------
section_heading("Overview")

st.markdown("""
<div class="card">
    <div class="pill">Proof of Capability</div>
    <h3>What we have already built</h3>
    <p>
    A range of lightweight, low-cost prototypes have been built outside the formal NDIA environment
    to explore what digital-first approaches can enable. These include:
    </p>
    <ul>
        <li>AI-powered document interrogation tools</li>
        <li>interactive dashboards for Assistive Technology markets</li>
        <li>simulation tools exploring planning and pricing dynamics</li>
        <li>search and retrieval interfaces for PAPL-like artefacts</li>
    </ul>
    <p>
    These prototypes demonstrate:
    </p>
    <ul>
        <li>the feasibility of rapid, high-quality prototyping</li>
        <li>positive colleague response when they can interact with a live concept</li>
        <li>that modern tooling can drastically shorten the idea-to-demonstrator cycle</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Digital PAPL Ecosystem Diagram
# -------------------------
section_heading("Digital PAPL Ecosystem Prototype")

st.markdown("""
<div class="card">
    <p>
    The diagram below shows how structured pricing artefacts can serve multiple user needs at once,
    providing views for participants, providers, planners and internal analytics teams.
    </p>
</div>
""", unsafe_allow_html=True)

try:
    st.image(
        "assets/diagram_ecosystem.png",
        caption="Digital PAPL ecosystem — a single structured source supporting many views.",
        #use_column_width=True,
    )
except:
    st.info("Add diagram_ecosystem.png to assets/ to display this image.")

# -------------------------
# Examples of Prior Work
# -------------------------
section_heading("Examples of Prior Prototypes")

st.markdown("""
<div class="card">
    <div class="pill">Existing Prototypes</div>
    <h3>What previous work demonstrates</h3>
    <p>
    Examples of existing prototypes include:
    </p>
    <ul>
        <li><b>AT Market Dashboard</b> — interactive views of assistive technology spending and supply.</li>
        <li><b>PAPL Q&A tools</b> — semantic search interfaces over pricing rules.</li>
        <li><b>Planner simulation tools</b> — helping explain decision dynamics and key KPIs.</li>
    </ul>
    <p>
    These prototypes show the value of structured content and modern development frameworks.
    </p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Takeaway
# -------------------------
section_heading("Key Takeaway")

st.markdown("""
<div class="card">
    <h3>What this means for NDIA</h3>
    <p>
    These prototypes demonstrate that:
    </p>
    <ul>
        <li>useful tools can be built quickly and safely</li>
        <li>structured artefacts can support new planning, provider and participant tools</li>
        <li>modernisation does not require heavy upfront investment</li>
    </ul>
</div>
""", unsafe_allow_html=True)
