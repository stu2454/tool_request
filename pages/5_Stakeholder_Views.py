import streamlit as st

# NDIA heading component
def section_heading(text):
    st.markdown(f"### <span style='color:#6D3078;'>{text}</span>", unsafe_allow_html=True)

st.title("Stakeholder View Matrix")

# -------------------------
# Overview
# -------------------------
section_heading("Overview")

st.markdown("""
<div class="card">
    <h3>How digital-first artefacts support different users</h3>
    <p>
    Structured, digital-first pricing artefacts allow NDIA to present different views for different audiences —
    all derived from the same authoritative rules. This supports transparency, consistency and market stewardship.
    </p>
</div>
""", unsafe_allow_html=True)

try:
    st.image("assets/diagram_matrix.png", caption="Stakeholder View Matrix")
except:
    st.info("Add diagram_matrix.png to assets/ to display this image.")

# -------------------------
# Participants & Families
# -------------------------
section_heading("Participants & Families")

st.markdown("""
<div class="card">
    <h3>Plain language guidance and improved transparency</h3>
    <p>Digital-first artefacts help participants by enabling:</p>
    <ul>
        <li>clear, accessible explanations</li>
        <li>support in planning conversations</li>
        <li>better understanding of reasonable price expectations</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Providers & New Entrants
# -------------------------
section_heading("Providers & New Entrants")

st.markdown("""
<div class="card">
    <h3>Clarity and predictability</h3>
    <p>Providers benefit from:</p>
    <ul>
        <li>consistent interpretation of rules</li>
        <li>simple compliance and quoting tools</li>
        <li>clearer signals to support market entry</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Planners & LACs
# -------------------------
section_heading("Planners & LACs")

st.markdown("""
<div class="card">
    <h3>Decision support and consistency</h3>
    <p>Planners benefit through:</p>
    <ul>
        <li>embedded guidance at point of decision</li>
        <li>less reliance on manual document search</li>
        <li>more consistent application of rules across regions</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Advocacy & Peak Bodies
# -------------------------
section_heading("Advocacy & Peak Bodies")

st.markdown("""
<div class="card">
    <h3>Transparency to support consultation</h3>
    <p>Structured artefacts provide:</p>
    <ul>
        <li>a stable reference point for submissions</li>
        <li>clarity on pricing logic</li>
        <li>better evidence for policy discussions</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Researchers & Analysts
# -------------------------
section_heading("Researchers & Analysts")

st.markdown("""
<div class="card">
    <h3>Data for insight and evaluation</h3>
    <p>Digital-first artefacts allow for:</p>
    <ul>
        <li>longitudinal analysis of pricing settings</li>
        <li>understanding market behaviour</li>
        <li>identifying emerging patterns</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Innovators
# -------------------------
section_heading("Technology Innovators")

st.markdown("""
<div class="card">
    <h3>Support for safe third-party tools</h3>
    <p>Structured, authoritative guidance reduces:</p>
    <ul>
        <li>reliance on scraping static PDFs</li>
        <li>misinterpretation of pricing rules</li>
        <li>risks from unverified “AI NDIS helper” tools</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# -------------------------
# NDIA Internal
# -------------------------
section_heading("NDIA Internal Market Teams")

st.markdown("""
<div class="card">
    <h3>Stronger market stewardship</h3>
    <p>Internal teams gain:</p>
    <ul>
        <li>clearer links between pricing rules and market behaviour</li>
        <li>earlier visibility of market stress</li>
        <li>better signals for stewardship interventions</li>
    </ul>
</div>
""", unsafe_allow_html=True)
