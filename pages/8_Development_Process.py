import streamlit as st

from auth import password_gate
password_gate()


# NDIA heading component
def section_heading(text):
    st.markdown(f"### <span style='color:#6D3078;'>{text}</span>", unsafe_allow_html=True)

st.title("How This Prototype Was Built: End-to-End Development Process")

# =========================================================
# OVERVIEW
# =========================================================
section_heading("Overview")

st.markdown("""
<div class="card">
    <div class="pill">Overview</div>
    <h3>A transparent, repeatable, APS-aligned development workflow</h3>
    <p>
    This page outlines the complete, end-to-end process used to design, structure, build and deploy the 
    Digital-First Pricing Artefacts Prototype. The workflow demonstrates how a small, controlled set of modern 
    tools—including AI assistants, version control, Docker and Streamlit—can deliver safe, fast, 
    evidence-driven innovation fully aligned with APS expectations.
    </p>
    <p>
    Importantly, the process is <i>repeatable</i>. It establishes a pattern NDIA can use for future internal prototypes, 
    including decision-support tools, structured operational guidance, or digital-first versions of pricing products.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 1. PROBLEM FRAMING & PROMPT ENGINEERING
# =========================================================
section_heading("1. Problem Framing & Prompt Engineering")

with st.expander("Problem Framing & Concept Development", expanded=True):
    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.markdown("#### Defining the challenge")
    st.write("""
    The work began with a focused problem statement:  
    **How can NDIA shift its core pricing artefacts from static PDFs to structured, digital-first formats**  
    that support participants, providers, planners and internal market stewardship?
    """)

    st.markdown("#### Using AI to accelerate early thinking")
    st.write("""
    Through iterative prompt engineering, we generated:
    - a detailed executive summary  
    - a fully reasoned justification for the work  
    - alignment with the APS Whole-of-Government AI Plan  
    - a set of structural diagrams covering the journey from static → structured → actionable data  
    - a stakeholder matrix  
    - a full risk and mitigation annex  
    - a roadmap from 0–14+ weeks  
    - the full multi-page site information architecture  

    This early conceptual work avoided premature coding and ensured alignment with strategic direction.
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# 2. CODE SCAFFOLD GENERATION
# =========================================================
section_heading("2. Code Scaffold Generation")

with st.expander("Transforming concepts into a running prototype", expanded=False):
    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.markdown("""
    Once the conceptual architecture was validated, the entire code scaffold was generated through structured 
    AI prompting. This included:
    - a homepage (`0_Start_here.py`)  
    - seven structured content pages under `/pages`  
    - NDIA-aligned CSS and colour palette  
    - an assets folder for imagery  
    - `requirements.txt`  
    - `Dockerfile` and `docker-compose.yml`  
    - page-to-page navigation patterns  
    """)

    st.write("""
    This meant the prototype could be run immediately without manual boilerplate coding.  
    The scaffolding was modular, readable, and aligned with accessibility expectations.
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# 3. LOCAL DEVELOPMENT (VS CODE + DOCKER)
# =========================================================
section_heading("3. Local Development Environment")

with st.expander("Building and refining locally", expanded=False):
    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.markdown("#### Why VS Code + Docker?")
    st.write("""
    This combination ensured a fully reproducible, isolated environment that avoids dependency issues 
    and reflects APS-aligned engineering patterns.
    - **VS Code** provided a modern, accessible coding interface.  
    - **Docker** ensured the app behaves consistently across machines.  
    - **Streamlit** offered live reload and very fast iteration.  
    """)

    st.markdown("#### Steps performed")
    st.markdown("""
    1. Unzipped the AI-generated scaffold.  
    2. Opened the folder in VS Code.  
    3. Added the four generated diagrams into `/assets`.  
    4. Ran the app locally using `docker-compose up --build`.  
    5. Used Streamlit’s autoreload to adjust UI layout, content and components in real time.  
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# 4. ITERATIVE HUMAN–AI DEVELOPMENT LOOP
# =========================================================
section_heading("4. Iterative Refinement with Human-AI Loop")

with st.expander("High-speed iteration mode", expanded=False):
    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.write("""
    After the scaffold was running, a rapid refinement process followed:
    """)

    st.markdown("""
    - describe the change needed in plain English  
    - AI generates refined or rewritten components  
    - copy the new code into VS Code  
    - Streamlit reloads instantly  
    """)

    st.write("""
    This accelerated:
    - page layout refinement  
    - card consistency  
    - heading hierarchy  
    - image placement  
    - dark-mode proof styling  
    - structural consistency across the site  

    This loop reduced hours of manual work to minutes.
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# 5. VERSION CONTROL (GITHUB)
# =========================================================
section_heading("5. Version Control & Traceability")

with st.expander("Using GitHub for auditability", expanded=False):
    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.write("""
    Once the prototype stabilised, the codebase was committed to a GitHub repository to ensure:
    - versioning  
    - traceability  
    - audit trails  
    - collaboration  
    - safe branching and rollback  
    """)

    st.markdown("#### Commands used")
    st.code("""
git init
git add .
git commit -m "Initial commit"
git remote add origin <repo_url>
git push -u origin main
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# 6. STREAMLIT CLOUD DEPLOYMENT
# =========================================================
section_heading("6. Deployment to Streamlit Cloud")

with st.expander("Instant internal sharing", expanded=False):
    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.write("""
    Streamlit Cloud enabled the prototype to be shared with leadership immediately through a secure link.
    Deployment steps:
    """)

    st.markdown("""
    1. Sign in with GitHub  
    2. Select the repository  
    3. Allow the platform to build the container  
    4. Test the deployed version  
    """)

    st.write("""
    Because the prototype contains **no participant or provider identifying data**, this is a 
    safe environment for internal demonstration.
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# 7. DEMONSTRATION IMPACT
# =========================================================
section_heading("7. Demonstration to Leadership")

with st.expander("What the Director saw", expanded=False):
    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.write("""
    Demonstrating this prototype to the Director showed:
    - how quickly a high-quality digital artefact can be created  
    - how structured content improves interpretability  
    - how the work directly aligns with the APS AI Plan  
    - how digital-first pricing artefacts strengthen NDIA’s market stewardship  
    - how small, safe experiments help inform future investment decisions  
    """)

    st.write("This strengthened support for a controlled prototyping environment in the branch.")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# 8. WHY THIS WORKFLOW IS REPRODUCIBLE
# =========================================================
section_heading("8. Why This Workflow Is Reproducible")

with st.expander("Reusable pattern for NDIA prototyping", expanded=False):
    st.markdown("""<div class="card">""", unsafe_allow_html=True)

    st.write("""
    The workflow can be reused to prototype:
    - digital-first operational guidance  
    - pricing explanation tools  
    - planner decision-support utilities  
    - market intelligence dashboards  
    - structured AT or DRHS rule engines  
    - participant-facing explanatory tools  
    """)

    st.write("""
    The pattern is safe, repeatable, auditable, and aligned with best practice.  
    It provides **evidence**, not speculation.
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# SUMMARY
# =========================================================
section_heading("Summary")

st.markdown("""
<div class="card">
    <h3>A safe, fast, APS-aligned approach to digital innovation</h3>
    <p>
    This workflow demonstrates how the Markets Delivery Branch can responsibly explore 
    digital-first pricing artefacts using modern tooling, controlled access, and transparent methods.  
    It aligns with both internal NDIA expectations and the APS Whole-of-Government AI Plan.
    </p>
</div>
""", unsafe_allow_html=True)
