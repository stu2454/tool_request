import streamlit as st

# =========================================================
# GLOBAL CONFIG — ENABLE WIDE MODE
# =========================================================
st.set_page_config(
    page_title="Digital-First Pricing Artefacts Prototype",
    layout="wide",
)

# =========================================================
# GLOBAL STYLING (NDIA brand, cards, max-width)
# =========================================================
st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1400px;
    margin-left: auto;
    margin-right: auto;
}

.card {
    background: #FFFFFFCC;
    padding: 1.5rem 2rem;
    border-radius: 12px;
    margin-top: 1.25rem;
    margin-bottom: 1.5rem;
    border: 1px solid #E8E8E8;
    max-width: 1200px;
    margin-left: auto;
    margin-right: auto;
}

.pill {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    background-color: #6D3078;
    color: white;
    border-radius: 8px;
    font-size: 0.85rem;
    margin-bottom: 0.75rem;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# NDIA-STYLE SECTION HEADING
# =========================================================
def section_heading(text):
    st.markdown(
        f"### <span style='color:#6D3078;'>{text}</span>",
        unsafe_allow_html=True
    )

# =========================================================
# PAGE CONTENT
# =========================================================

st.title("Start Here — Digital-First Pricing Artefacts Prototype")

# -------------------------
# Welcome Section
# -------------------------
section_heading("Welcome")

st.markdown("""
<div class="card">
<div class="pill">Introduction</div>
<h3>Your starting point</h3>

<p>This prototype demonstrates how NDIA pricing artefacts — such as the PAPL, Code Guides and 
Operational Guidance — can evolve from static PDFs into structured, digital-first information assets.</p>

<p>The site contains:</p>

<ul>
<li>the strategic case for moving to structured artefacts</li>
<li>a demonstration of how these artefacts could be used across audiences</li>
<li>a detailed risk & mitigation annex</li>
<li>a roadmap for an initial 14-week delivery cycle</li>
<li>a full breakdown of how this prototype was built</li>
</ul>

<p>Use the left sidebar to navigate between sections.</p>

</div>
""", unsafe_allow_html=True)

# -------------------------
# Navigation Section
# -------------------------
section_heading("Navigation")

st.markdown("""
<div class="card">
<h3>How to use this prototype</h3>

<p>The sidebar provides access to:</p>

<ul>
<li><b>Executive Summary</b> — the high-level case</li>
<li><b>Evidence Showcase</b> — what we’ve already built</li>
<li><b>Toolset</b> — what is required</li>
<li><b>Detailed Case</b> — the full argument for access</li>
<li><b>Stakeholder Views</b> — how structured artefacts serve each group</li>
<li><b>Risk Mitigation</b> — how risk is managed</li>
<li><b>Roadmap</b> — proposed 14-week phased plan</li>
<li><b>Development Process</b> — how this prototype was built</li>
</ul>

<p>Together, these components demonstrate the value of supporting a controlled prototyping 
environment within the Markets Delivery Branch.</p>

</div>
""", unsafe_allow_html=True)
