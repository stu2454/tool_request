import streamlit as st

# NDIA heading component
def section_heading(text):
    st.markdown(f"### <span style='color:#6D3078;'>{text}</span>", unsafe_allow_html=True)

st.title("Risk & Mitigation Annex")

# -------------------------
# Overview
# -------------------------
section_heading("Overview")

st.markdown("""
<div class="card">
    <h3>Managing risk in a controlled prototyping environment</h3>
    <p>
    This work follows a deliberately conservative approach: low-risk activities, strong guardrails and 
    clear separation between prototypes and production systems.
    </p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Security & Data Protection
# -------------------------
section_heading("Security & Data Protection")

with st.expander("Security & Data Protection — Risks and Mitigations", expanded=False):
    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.markdown("#### Key Risks")
    st.markdown("""
    - Unauthorised access to tools or model endpoints  
    - Accidental use of sensitive data  
    - Prototypes being mistaken for production systems  
    """)

    st.markdown("#### Mitigations")
    st.markdown("""
    - IAM-restricted access  
    - Only publicly available artefacts used  
    - No identifying data included  
    - Clear prototype labelling  
    - Internal-only access  
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# Governance & Compliance
# -------------------------
section_heading("Governance & Compliance")

with st.expander("Governance & Compliance — Risks and Mitigations", expanded=False):
    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.markdown("#### Key Risks")
    st.markdown("""
    - Misalignment with APS AI Plan  
    - Shadow IT if work is not transparent  
    """)

    st.markdown("#### Mitigations")
    st.markdown("""
    - Clear alignment with whole-of-government guidance  
    - Code stored in NDIA GitHub Enterprise  
    - Digital/IT informed and able to review  
    - Prototypes kept separate from production pathways  
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# Operational & Quality
# -------------------------
section_heading("Operational & Quality")

with st.expander("Operational & Quality — Risks and Mitigations", expanded=False):
    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.markdown("#### Key Risks")
    st.markdown("""
    - Misinterpretation of prototype outputs  
    - Over-reliance on a single developer  
    - Inconsistent coding practices  
    """)

    st.markdown("#### Mitigations")
    st.markdown("""
    - Clear disclaimers on non-production status  
    - Regular alignment with Branch leadership  
    - Use of Git for review and version control  
    - Lightweight documentation  
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# Technical & Infrastructure
# -------------------------
section_heading("Technical & Infrastructure")

with st.expander("Technical & Infrastructure — Risks and Mitigations", expanded=False):
    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.markdown("#### Key Risks")
    st.markdown("""
    - Introduction of unapproved dependencies  
    - Unexpected resource load  
    """)

    st.markdown("#### Mitigations")
    st.markdown("""
    - Short, approved library list  
    - Containerised environments  
    - Resource monitoring  
    - Throttled model usage where possible  
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# Reputational & Policy
# -------------------------
section_heading("Reputational & Policy")

with st.expander("Reputational & Policy — Risks and Mitigations", expanded=False):
    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.markdown("#### Key Risks")
    st.markdown("""
    - Prototype features misaligned with final policy  
    - External misunderstanding if prototypes are shared  
    """)

    st.markdown("#### Mitigations")
    st.markdown("""
    - Strictly internal demonstrations  
    - Consultation with Pricing/Strategy teams  
    - Production tools follow formal approvals  
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# Ethical & Accessibility
# -------------------------
section_heading("Ethical & Accessibility")

with st.expander("Ethical & Accessibility — Risks and Mitigations", expanded=False):
    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.markdown("#### Key Risks")
    st.markdown("""
    - Interfaces not being accessible  
    - AI oversimplifying or misrepresenting guidance  
    """)

    st.markdown("#### Mitigations")
    st.markdown("""
    - WCAG-aligned UI decisions  
    - Human-in-the-loop review  
    - APS Ethical AI Principles followed  
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# Summary
# -------------------------
section_heading("Summary")

st.markdown("""
<div class="card">
    <h3>Overall Risk Position</h3>
    <p>
    With the mitigations outlined above, the overall risk of enabling a controlled prototyping 
    environment is low, while the potential benefits for clarity, stewardship and internal efficiency 
    are significant.
    </p>
</div>
""", unsafe_allow_html=True)
