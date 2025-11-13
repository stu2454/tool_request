import streamlit as st

# ------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------
st.set_page_config(
    page_title="Digital-First Pricing Artefacts",
    layout="wide",
)

# ------------------------------------------------------------
# Global CSS — Bulletproof Light Mode + NDIA Branding
# ------------------------------------------------------------
st.markdown("""
<style>

    /* -------------------------------------
       FULL LIGHT MODE OVERRIDE (no dark theme)
       ------------------------------------- */
    :root, html, body, .stApp, .stAppViewContainer, .stMain {
        background-color: #F5F5F7 !important;
        color: #2B2B2B !important;
    }

    /* Block containers, markdown bodies, etc. */
    [data-testid="stAppViewContainer"] [class*="block-container"],
    div[data-testid="stBlock"],
    .stMarkdown, .stText, p, span, li {
        color: #2B2B2B !important;
        background-color: #F5F5F7 !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"],
    [data-testid="stSidebarNav"] {
        background-color: #F5F5F7 !important;
        color: #2B2B2B !important;
    }
    [data-testid="stSidebarNav"] a, 
    [data-testid="stSidebarNav"] span {
        color: #2B2B2B !important;
        font-weight: 500 !important;
    }

    /* -------------------------------------
       Typography
       ------------------------------------- */
    html, body {
        font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        font-size: 16px;
    }

    h1, h2, h3 {
        color: #6D3078 !important;
        font-weight: 700 !important;
    }
    h4, h5, h6 {
        color: #6D3078 !important;
        font-weight: 600 !important;
    }

    /* -------------------------------------
       Buttons
       ------------------------------------- */
    .stButton>button {
        background: #6D3078 !important;
        color: #FFFFFF !important;
        padding: 0.6rem 1.2rem !important;
        border-radius: 8px !important;
        border: none !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        transition: 0.2s all ease-in-out !important;
    }
    .stButton>button:hover {
        background: #009CA6 !important;
        transform: translateY(-1px);
    }

    /* -------------------------------------
       Card Component
       ------------------------------------- */
    .card {
        background-color: #FFFFFF !important;
        color: #2B2B2B !important;
        border-radius: 16px !important;
        padding: 20px 24px !important;
        border: 1px solid #E6E6E9 !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04) !important;
        margin-bottom: 24px !important;
    }

    /* Pill label */
    .pill {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 999px;
        background-color: #009CA6;
        color: #FFFFFF;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        margin-bottom: 6px;
    }

    /* -------------------------------------
       Fix for Streamlit container backgrounds
       ------------------------------------- */
    .css-1y4p8pa, .css-1vq4p4l, .css-12ttj6m {
        background-color: #F5F5F7 !important;
        color: #2B2B2B !important;
    }

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# HERO SECTION
# ------------------------------------------------------------

st.markdown("<div class='main-title' style='font-size:48px; font-weight:700; color:#6D3078;'>Digital-First Pricing Artefacts</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle' style='font-size:22px; opacity:0.9;'>A prototype for how NDIA could modernise pricing artefacts to actively steward disability service markets.</div>", unsafe_allow_html=True)

st.markdown("<div style='padding-top:20px'></div>", unsafe_allow_html=True)

col_left, col_right = st.columns([1.1, 0.9])

with col_left:
    st.markdown("""
    <div class="card">
        <div class="pill">Overview</div>
        <h3>From static PDFs to market stewardship tools</h3>
        <p>
        Today, PAPL, the AT & HM Code Guides, and Operational Guidance are published as static documents.
        They are essential, but difficult to search, slow to update, and hard to reuse in digital tools.
        </p>
        <p>
        This prototype shows how those artefacts could evolve into structured, digital-first resources that
        support clearer communication, automated checks, and more active stewardship of the disability 
        support market.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    try:
        st.image(
            "assets/diagram_static_to_structured.png",
            caption="Static → Structured → Stewardship",
            use_container_width=True
        )
    except Exception:
        st.info("Add 'diagram_static_to_structured.png' to the assets folder.")

st.markdown("<div style='padding-top:12px'></div>", unsafe_allow_html=True)

# ------------------------------------------------------------
# QUICK NAVIGATION
# ------------------------------------------------------------
st.markdown("""
<div class="card">
    <div class="pill">What this prototype includes</div>
    <h3>Sections in this demonstration</h3>
    <ul>
        <li><b>Executive Summary</b> – a concise narrative of why this matters now</li>
        <li><b>Evidence Showcase</b> – examples of prototypes already built</li>
        <li><b>Toolset</b> – what tools are needed and why, in plain language</li>
        <li><b>Detailed Case for Access</b> – full justification aligned with APS policy</li>
        <li><b>Stakeholder View Matrix</b> – how digital-first pricing helps different groups</li>
        <li><b>Risk & Mitigation</b> – how we manage security, governance and reputational risks</li>
        <li><b>Roadmap</b> – a pragmatic, low-risk path to start</li>
    </ul>
</div>
""", unsafe_allow_html=True)
