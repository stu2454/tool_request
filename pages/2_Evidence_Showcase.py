import streamlit as st
from auth import password_gate

password_gate()

# ---------------------------------
# NDIA heading component
# ---------------------------------
def section_heading(text: str):
    st.markdown(
        f"<div class='section-header'>{text}</div>",
        unsafe_allow_html=True,
    )

st.title("Evidence Showcase")

# -------------------------
# Evidence Section
# -------------------------
section_heading("What we have already demonstrated")

st.markdown(
    """<div class="card">
<div class="pill">Showcase</div>
<h3>Prototype capabilities already proven</h3>

<p>
The Markets Delivery Branch has already demonstrated that NDIA pricing artefacts can be
transformed from static PDFs into structured, digital-first content. This includes working
prototypes that show how rules, prices, codes, constraints and audience-specific guidance
can be represented as queryable information assets.
</p>

<p><b>Examples include:</b></p>

<ul>
<li>machine-readable versions of support items and price limits</li>
<li>a structured representation of claiming conditions</li>
<li>search and filter interfaces for complex pricing content</li>
<li>audience-specific views (planner, provider, participant)</li>
<li>automated cross-referencing between artefacts</li>
<li>LLM-powered question-answering over structured content</li>
</ul>

<p>
These small proofs-of-concept demonstrate that NDIA artefacts do not need to remain
trapped in PDFs and Word documents – they can be represented in modern information
formats suitable for automation, search, and safe AI tooling.
</p>
</div>""",
    unsafe_allow_html=True,
)

# -------------------------
# Example Tools
# -------------------------
section_heading("Tools already built")

st.markdown(
    """<div class="card">
<div class="pill">Demonstration tools</div>
<h3>Early prototypes showing what is possible</h3>

<p>The following tools illustrate the practical value of structured, digital-first artefacts:</p>

<ul>
<li><b>PAPL Search &amp; Query Tool</b> – enables real-time querying of support items, price limits,
units, claiming notes and conditions.</li>
<li><b>AT Lookup Tool</b> – maps AT codes, categories, descriptions, and pricing constraints
into a structured dataset that supports planners and market analysts.</li>
<li><b>AT Market Dashboard</b> – demonstrates how structured AT information can power
automated market insights, anomaly detection and pricing analysis.</li>
<li><b>Operational Guidance Parser</b> – early trial converting OG content into
machine-readable components suitable for LLM retrieval.</li>
<li><b>LLM Q&amp;A Prototype</b> – shows how structured content allows far more accurate, safe
AI-powered assistance compared to reading static PDFs.</li>
</ul>

<p>
These prototypes are deliberately lightweight, demonstrating the feasibility of building
structured, queryable NDIA artefacts without disrupting existing workflows.
</p>
</div>""",
    unsafe_allow_html=True,
)

# -------------------------
# Impact
# -------------------------
section_heading("What this enables")

st.markdown(
    """<div class="card">
<div class="pill">Impact</div>
<h3>Why digital-first artefacts matter</h3>

<p>Early prototypes have demonstrated benefits that cannot be achieved with static documents:</p>

<ul>
<li>instant search, filtering and comparison</li>
<li>automated consistency checks across artefacts</li>
<li>reduced ambiguity for planners and providers</li>
<li>streamlined market stewardship workflows</li>
<li>structured data ready for calculators and validation tools</li>
<li>foundation for safe, explainable AI assistants</li>
</ul>

<p>
This is a practical, achievable example of the type of digital-first capability the
Markets Delivery Branch could embed – dramatically improving stewardship,
clarity and operational efficiency.
</p>
</div>""",
    unsafe_allow_html=True,
)

