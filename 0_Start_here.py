import os
from urllib.parse import urlencode

import requests
from jose import jwt
import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# PAGE CONFIG — MUST BE FIRST STREAMLIT CALL
# =========================================================
st.set_page_config(
    page_title="Start Here — Digital-First Pricing Artefacts Prototype",
    layout="wide",
)

# =========================================================
# AUTH0 CONFIG
# =========================================================
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")              # e.g. "your-tenant-region.auth0.com"
AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")
APP_URL = os.getenv("APP_URL")                        # e.g. "https://yourapp.onrender.com"

REDIRECT_URI = APP_URL                                # Must match Auth0 callback URL exactly


def auth_config_valid() -> bool:
    return all(
        [
            AUTH0_DOMAIN,
            AUTH0_CLIENT_ID,
            AUTH0_CLIENT_SECRET,
            APP_URL,
        ]
    )


def auth0_login_url() -> str:
    params = {
        "client_id": AUTH0_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": "openid profile email",
    }
    return f"https://{AUTH0_DOMAIN}/authorize?{urlencode(params)}"


def get_auth_code_from_query() -> str | None:
    # Use experimental_get_query_params for broad Streamlit compatibility
    params = st.experimental_get_query_params()
    if not params:
        return None
    code_list = params.get("code")
    if not code_list:
        return None
    return code_list[0]


def exchange_code_for_token(code: str) -> dict:
    token_url = f"https://{AUTH0_DOMAIN}/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": AUTH0_CLIENT_ID,
        "client_secret": AUTH0_CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }
    resp = requests.post(token_url, json=data, timeout=10)
    if not resp.ok:
        raise RuntimeError(f"Token request failed: {resp.status_code} {resp.text}")
    return resp.json()


def decode_id_token(id_token: str) -> dict:
    # We skip signature verification here because this is a front-end style app.
    # Identity + domain restriction are enforced by Auth0 (and your @ndis.gov.au Action).
    return jwt.decode(id_token, options={"verify_signature": False})


def show_login_page(error_msg: str | None = None):
    st.markdown("### 🔒 Secure NDIA Access")
    st.markdown(
        "This prototype is restricted to NDIA staff. "
        "Please log in with your **@ndis.gov.au** email address."
    )
    if error_msg:
        st.error(error_msg)

    st.write("")  # spacing
    st.link_button("Login via Auth0", auth0_login_url())
    st.stop()


def require_login():
    """
    Gate this page behind Auth0 login.
    """
    if not auth_config_valid():
        st.error(
            "Authentication is not configured correctly.\n\n"
            "Missing one or more of: AUTH0_DOMAIN, AUTH0_CLIENT_ID, "
            "AUTH0_CLIENT_SECRET, APP_URL.\n\n"
            "Set these environment variables in Render and redeploy."
        )
        st.stop()

    # Already logged in during this browser session
    if "user" in st.session_state:
        return

    # Handle Auth0 callback with ?code=...
    code = get_auth_code_from_query()
    if code:
        try:
            tokens = exchange_code_for_token(code)
            id_token = tokens.get("id_token")
            if not id_token:
                show_login_page("Login failed: missing ID token from Auth0.")
            user_info = decode_id_token(id_token)
            st.session_state["user"] = user_info
            return
        except Exception as exc:
            show_login_page(f"Login failed: {exc}")

    # No existing session and no auth code: show login
    show_login_page()


# =========================================================
# ENFORCE LOGIN FOR THIS PAGE
# =========================================================
require_login()

# At this point, we should always have a user dict in session
user_email = st.session_state.get("user", {}).get("email", "unknown user")
st.sidebar.markdown(f"**Logged in as:** {user_email}")

# =========================================================
# GLOBAL STYLING — NDIA BRAND
# =========================================================
st.markdown(
    """
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
""",
    unsafe_allow_html=True,
)


# Section Heading Helper
def section_heading(text: str):
    st.markdown(f"<div class='section-header'>{text}</div>", unsafe_allow_html=True)


# =========================================================
# PAGE CONTENT
# =========================================================

st.title("Start Here — Digital-First Pricing Artefacts Prototype")

# -------------------------
# WELCOME SECTION
# -------------------------
section_heading("Welcome")

components.html(
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
        <li>align with whole-of-government AI readiness expectations</li>
    </ul>

    <p>This site contains:</p>

    <ul>
        <li>the strategic case for moving to structured artefacts</li>
        <li>a demonstration of early digital prototypes</li>
        <li>a risk & mitigation annex</li>
        <li>a 14-week roadmap for controlled prototyping</li>
        <li>a summary of how this prototype was rapidly built</li>
    </ul>

    <p>
    Use the sidebar to navigate between sections. This prototype illustrates what becomes 
    possible when NDIA teams have access to contemporary development environments 
    (LLMs, embeddings, VS Code, Docker, modern APIs).
    </p>
</div>
    """,
    height=520,
)

# -------------------------
# NAVIGATION SECTION
# -------------------------
section_heading("Navigation")

components.html(
    """
<div class="card">
    <h3>How to use this prototype</h3>

    <p>
    The sidebar provides access to eight sections that collectively outline the strategic 
    opportunity, evidence already generated, and the practical requirements for enabling 
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
    height=480,
)
