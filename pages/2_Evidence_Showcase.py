import streamlit as st

from auth import password_gate
password_gate()

# ---------------------------------
# NDIA heading component (fixed)
# ---------------------------------
def section_heading(text):
    st.markdown(
        f"<div class='section-header'>{text}</div>",
        unsafe_allow_html=True
    )

st.title("Evidence Showcase")

# -------------------------
# Overview
# -------------------------
section_heading("Overview")

st.markdown(
r"""
<div class="card">
<div class="pill">Proof of Capability</div>
<h3>A Single Prototype with Broad Implications</h3>
<p>
This section highlights one prototype that captures the essence of what a 
digital-first approach to pricing artefacts can enable: the 
<b>Assistive Technology Lookup Tool</b>, developed as part of the 
<b>Build a Bureaucrat Bot</b> competition.
</p>

<p>
By transforming static artefacts into structured, queryable information, this tool 
demonstrates how modern development environments allow useful, interactive 
products to be built rapidly and safely — even outside formal NDIA infrastructure.
</p>

<p>
The example below represents not just a single prototype, but a signal of what the 
Markets Delivery Branch could unlock through structured artefacts and 
contemporary development practices.
</p>
</div>
""",
    unsafe_allow_html=True
)

# -------------------------
# The AT Lookup Tool
# -------------------------
section_heading("The Assistive Technology Lookup Tool")

st.markdown(
r"""
<div class="card">
<div class="pill">Live Prototype</div>
<h3>AT Lookup Tool — Built for the “Build a Bureaucrat Bot” Challenge</h3>

<p>
The <b>AT Lookup Tool</b> is a semantically searchable interface that lets users explore 
AT items, descriptors and related metadata using natural language. Built using 
LLMs, embeddings, Streamlit and Docker, it shows how quickly the Agency could 
prototype interactive tools if key pricing artefacts were maintained in structured formats 
rather than static PDFs.
</p>

<p><b>Key capabilities include:</b></p>

<ul>
<li>semantic search over AT descriptions</li>
<li>instant retrieval of item information</li>
<li>suggestions and clarifications based on user intent</li>
<li>a clean interface usable by planners, providers and participants</li>
<li>a demonstration of how structured artefacts can support AI-driven tools</li>
</ul>

<p>View the live prototype here:</p>

<p style="margin-top:1rem;">
<a href="https://atlookuptool.streamlit.app" target="_blank" style="
background-color:#6D3078;
padding:0.6rem 1rem;
color:white;
border-radius:8px;
text-decoration:none;
">
🔗 Open the AT Lookup Tool
</a>
</p>
</div>
""",
    unsafe_allow_html=True
)

# -------------------------
# Billy-T Image
# -------------------------
section_heading("Illustrative Concept — 'Billy-T'")

st.markdown(
r"""
<div class="card">
<p>
The visual concept below represents the idea of a friendly, intelligent helper that 
guides users through structured pricing artefacts. While the AT Lookup Tool is 
a technical demonstration, the <b>Billy-T</b> character illustrates how such tools could 
evolve into approachable, assistant-style interfaces for planners, providers and 
participants.
</p>
</div>
""",
    unsafe_allow_html=True
)

st.image(
    "assets/billy-t.png",
    caption="Billy-T — a friendly helper for navigating structured Assistive Technology information.",
    width=420
)

# -------------------------
# Why It Matters
# -------------------------
section_heading("Why This Prototype Matters")

st.markdown(
r"""
<div class="card">
<div class="pill">Insights</div>
<h3>What this prototype demonstrates</h3>

<p>
Although built rapidly for a challenge, the AT Lookup Tool demonstrates several 
important insights relevant to NDIA’s digital future:
</p>

<ul>
<li><b>Static artefacts constrain innovation</b> — structured formats unlock search, filtering, validation and automation.</li>
<li><b>Modern tooling accelerates delivery</b> — the prototype was built in hours, showing the potential of contemporary environments.</li>
<li><b>Colleagues engage more deeply</b> when interacting with a working tool rather than a concept deck.</li>
<li><b>Structured artefacts align with whole-of-government AI readiness</b>, enabling safer, more responsible use of AI systems.</li>
</ul>
</div>
""",
    unsafe_allow_html=True
)

# -------------------------
# Key Takeaway
# -------------------------
section_heading("Key Takeaway")

st.markdown(
r"""
<div class="card">
<h3>The Strategic Signal</h3>
<p>
The AT Lookup Tool shows what becomes possible when NDIA pricing artefacts are 
treated as structured, reusable data assets instead of static PDFs. A single prototype 
— built quickly, at low cost — highlights a clear pathway toward:
</p>

<ul>
<li>faster development of internal tools</li>
<li>clearer guidance for planners and providers</li>
<li>greater consistency across pricing artefacts</li>
<li>a modern platform for safe, explainable AI use</li>
</ul>

<p>
This is a practical, achievable example of the type of digital-first capability NDIA 
could embed within the Markets Delivery Branch.
</p>
</div>
""",
    unsafe_allow_html=True
)
