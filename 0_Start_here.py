import streamlit as st

# =========================================================
# GLOBAL CONFIG — WIDE MODE + PAGE TITLE
# =========================================================
st.set_page_config(
    page_title="Start Here — Digital-First Pricing Artefacts Prototype",
    layout="wide",
)

# =========================================================
# GLOBAL STYLING — NDIA BRAND
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

/* Card Style */
.card {
    background: #FFFFFFEE;
    padding: 1.75rem 2rem;
    border-radius: 14px;
    margin-top: 1.25rem;
    margin-bottom: 1.75rem;
    border: 1px solid #E4E2E6;
}

/* Purple Pill Label */
.pill {
    display: inline-block;
    padding: 0.3rem 0.85rem;
    background-color: #6D3078;
    color: white;
    border-radius: 8px;
    font-size: 0.8rem;
    margin-bottom: 0.5rem;
}

/* Section Headings */
.section-header {
    color: #6D3078;
    font-size: 1.65rem;
    font-weight: 600;
    margin-top: 1.5rem;
    margin-bottom: 0.25rem;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SECTION HEADING HELPER
# =========================================================
def section_heading(text):
    st.markdown(f"<div class='section-header'>{text}</div>", unsafe_allow_html=True)


# =========================================================
# PAGE CONTENT
# =========================================================

st.title("Start Here — Digital-First Pricing Artefacts Prototype")

# -------------------------
# WELCOME SECTION
# -------------------------
section_heading("Welcome")

st.markdown(
"""
<div class="card">
    <div class="pill">Introduction</div>
    <h3>Your starting point</h3>

    <p>
    This prototype demonstrates how NDIA pricing artefacts — including the Pricing 
    Arrangements and Price Limits (PAPL), Code Guides, and Operational Guidance — 
    can evolve from static PDFs into structured, digital-first information assets designed 
    for reuse, interrogation, and active stewardship of disability support markets.
    </p>

    <p>
    Today, these artefacts are essential but constrained: slow to update, hard to 
    interrogate, difficult to reuse programmatically, and unable to provide dynamic or 
    audience-specific guidance. Translating them into structured formats (Markdown, 
    JSON, schemas) unlocks the potential to:
    </p>

    <ul>
        <li>improve accessibility and usability for participants, providers and planners</li>
        <li>enable real-time search, filtering and validation</li>
        <li>integrate artefacts into calculators, decision tools and AI assistants</li>
        <li>reduce duplicated effort across NDIA teams</li>
        <li>provide analysts and policy teams with reusable data assets</li>
        <li>deliver on Minister Gallagher’s whole-of-government AI readiness expectations</li>
    </ul>

    <p>This site contains:</p>

    <ul>
        <li>the strategic case for moving to structured artefacts</li>
        <li>a demonstration of what digital artefacts enable</li>
        <li>a risk & mitigation annex</li>
        <li>a 14-week roadmap for controlled prototyping</li>
        <li>a breakdown of how this prototype was rapidly built</li>
    </ul>

    <p>
    Use the sidebar to navigate between sections. This prototype illustrates what becomes 
    possible when NDIA teams have access to contemporary development environments 
    (LLMs, embeddings, VS Code, Docker, and rapid prototyping frameworks).
    </p>
</div>
""",
    unsafe_allow_html=True
)


# -------------------------
# NAVIGATION SECTION
# -------------------------
section_heading("Navigation")

st.markdown(
"""
<div class="card">
    <h3>How to use this prototype</h3>

    <p>
    The sidebar provides access to eight sections that collectively outline the strategic 
    opportunity, the evidence already generated, and the practical requirements for enabling 
    a digital-first approach to pricing artefacts within the Markets Delivery Branch.
    </p>

    <ul>
        <li><b>Executive Summary</b> — the high-level strategic case</li>
        <li><b>Evidence Showcase</b> — demonstrations already built</li>
        <li><b>Toolset</b> — what environments and tools are required</li>
        <li><b>Detailed Case</b> — full justification and benefits</li>
        <li><b>Stakeholder Views</b> — value for participants, providers, planners, policy</li>
        <li><b>Risk Mitigation</b> — safeguards and governance</li>
        <li><b>Roadmap</b> — proposed 14-week phased delivery model</li>
        <li><b>Development Process</b> — how the prototype and site were built</li>
    </ul>

    <p>
    Together, these components demonstrate how a structured, digital-first approach can 
    support modern market stewardship and deliver clearer guidance to the disability community.
    </p>
</div>
""",
    unsafe_allow_html=True
)
