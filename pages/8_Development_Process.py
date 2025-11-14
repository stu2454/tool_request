import streamlit as st

st.title("How This Prototype Was Built: End-to-End Development Process")

# --- INTRO CARD ---
st.markdown("""
<div class="card">
    <div class="pill">Overview</div>
    <h3>A transparent, repeatable, APS-aligned development workflow</h3>
    <p>
    This section explains the complete process used to design, build and deploy the 
    Digital-First Pricing Artefacts Prototype. It illustrates how modern, low-risk tools 
    (AI assistants, VS Code, Docker, GitHub, Streamlit Cloud) can enable rapid experimentation 
    while maintaining strong governance, security and transparency.
    </p>
</div>
""", unsafe_allow_html=True)

# =====================================================================
# 1. PROBLEM FRAMING & PROMPT ENGINEERING
# =====================================================================
with st.expander("1. Problem Framing and Prompt Engineering", expanded=True):

    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.markdown("### Framing the challenge")
    st.write("""
    The project began by articulating a clear problem statement:  
    **How might NDIA’s pricing artefacts evolve from static PDFs into structured, digital-first resources that better support participants, providers, planners and market stewardship?**
    """)

    st.markdown("### Using AI to accelerate conceptual development")
    st.write("""
    Through iterative prompting, we generated:
    - an executive summary  
    - a detailed justification aligned with the APS AI Plan  
    - a multi-page site structure  
    - a stakeholder matrix  
    - a risk and mitigation annex  
    - a detailed roadmap  
    - four polished diagrams  
    - and UI design patterns aligned to NDIA branding  

    This enabled rapid concept development **before writing any code**.
    """)

    st.markdown("</div>", unsafe_allow_html=True)


# =====================================================================
# 2. CODE SCAFFOLD GENERATION
# =====================================================================
with st.expander("2. Generating the Code Scaffold with AI", expanded=False):

    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.markdown("### From concept to working prototype")
    st.write("""
    Once the conceptual architecture was defined, AI was used to generate the full code scaffold:
    - `app.py` (homepage)  
    - seven full content pages under `/pages`  
    - NDIA-aligned CSS  
    - `requirements.txt`  
    - `Dockerfile`  
    - `docker-compose.yml`  
    - placeholders for all diagrams  

    The scaffold required no manual writing and ran immediately.
    """)

    st.markdown("</div>", unsafe_allow_html=True)


# =====================================================================
# 3. LOCAL DEVELOPMENT
# =====================================================================
with st.expander("3. Local Development in VS Code & Docker", expanded=False):

    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.markdown("### Why VS Code + Docker?")
    st.write("""
    This approach ensured a clean, reproducible development environment aligned with modern APS engineering practices:
    - **VS Code** for editing  
    - **Docker** for isolation and dependency consistency  
    - **Streamlit** for rapid, reactive UI iteration  
    """)

    st.markdown("### Steps performed")
    st.markdown("""
    1. Downloaded the generated ZIP into a local workspace.  
    2. Opened the project in VS Code.  
    3. Placed the four generated diagrams into the `/assets` folder.  
    4. Ran the app locally using `docker-compose up --build`.  
    5. Refined layouts and content using Streamlit’s live reload.  
    """)

    st.markdown("</div>", unsafe_allow_html=True)


# =====================================================================
# 4. ITERATIVE REFINEMENT
# =====================================================================
with st.expander("4. Iterative Refinement (Human + AI Loop)", expanded=False):

    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.markdown("### A rapid idea → prototype cycle")
    st.write("""
    With the scaffold in place, improvements were added through a fast feedback loop:
    1. Describe desired changes in plain language.  
    2. AI generates updated code or UI components.  
    3. Paste into VS Code, Streamlit reloads instantly.  

    This accelerated:
    - UI refinement  
    - card layout consistency  
    - page hierarchy  
    - image integration  
    - dark-mode-proof styling  
    """)

    st.markdown("</div>", unsafe_allow_html=True)


# =====================================================================
# 5. GITHUB DEPLOYMENT
# =====================================================================
with st.expander("5. Preparing and Publishing to GitHub", expanded=False):

    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.markdown("### Version control and auditability")
    st.write("""
    Publishing to GitHub ensured:
    - code versioning  
    - full audit trails  
    - reproducibility  
    - easy sharing with NDIA colleagues  
    """)

    st.markdown("### Commands used")
    st.code("""
git init
git add .
git commit -m "Initial commit"
git remote add origin <repo_url>
git push -u origin main
    """)

    st.markdown("</div>", unsafe_allow_html=True)


# =====================================================================
# 6. STREAMLIT CLOUD DEPLOYMENT
# =====================================================================
with st.expander("6. Deployment to Streamlit Cloud", expanded=False):

    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.markdown("### A safe, fast deployment for non-sensitive prototypes")
    st.write("""
    Streamlit Cloud enabled instantaneous deployment for internal demonstration.
    """)

    st.markdown("### Steps")
    st.markdown("""
    1. Logged into Streamlit Cloud using GitHub.  
    2. Selected the repository.  
    3. Accepted default build settings.  
    4. Deployed automatically within minutes.  
    5. Verified the prototype in the cloud environment.  
    """)

    st.write("Because the project contains **no participant or provider identifying data**, it is suitable for Streamlit Cloud.")

    st.markdown("</div>", unsafe_allow_html=True)


# =====================================================================
# 7. DEMONSTRATION IMPACT
# =====================================================================
with st.expander("7. Demonstration and Impact", expanded=False):

    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.markdown("### Showing leadership the possibilities")
    st.write("""
    The prototype clearly demonstrated:
    - how quickly modern tools can produce value  
    - how structured artefacts improve clarity and consistency  
    - how this work aligns with the APS AI Plan  
    - how digital-first artefacts support NDIA’s market stewardship role  

    This strengthened the case for a controlled prototyping environment within NDIA.
    """)

    st.markdown("</div>", unsafe_allow_html=True)


# =====================================================================
# 8. REPRODUCIBILITY & FUTURE USE
# =====================================================================
with st.expander("8. Why This Workflow Is Reproducible", expanded=False):

    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.markdown("### A reusable pattern for future NDIA prototypes")
    st.write("""
    This workflow can be reused for:
    - planner decision-support prototypes  
    - participant-facing explanation tools  
    - operational guidance digitisation  
    - market intelligence dashboards  
    - structured AT and DRHS rule engines  
    - provider compliance tooling  

    It provides a low-risk, high-value method for evidence-driven innovation.
    """)

    st.markdown("</div>", unsafe_allow_html=True)


# =====================================================================
# SUMMARY
# =====================================================================
st.markdown("""
<div class="card">
    <div class="pill">Summary</div>
    <h3>A safe, fast, APS-aligned approach to digital innovation</h3>
    <p>
    This end-to-end workflow demonstrates how the Markets Delivery Branch can responsibly 
    explore digital-first pricing artefacts using a modern toolset, strong governance and 
    transparent methods. The process is replicable, auditable, and fully aligned with both 
    internal NDIA expectations and the APS Whole-of-Government AI Plan.
    </p>
</div>
""", unsafe_allow_html=True)
