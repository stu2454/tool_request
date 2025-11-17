import streamlit as st

from auth import password_gate
password_gate()

# ---------------------------------
# NDIA heading component (purple #6D3078)
# ---------------------------------
def section_heading(text):
    st.markdown(
        f"### <span style='color:#6D3078;'>{text}</span>",
        unsafe_allow_html=True
    )

st.title("Detailed Case for Access")

# -------------------------
# Purpose
# -------------------------
section_heading("Purpose")

st.markdown(
r"""
<div class="card">
<div class="pill">Purpose</div>
<h3>Why we are seeking a controlled prototyping environment</h3>
<p>
The Markets Delivery Branch is seeking access to a lightweight, well-governed development environment 
to prototype digital-first versions of NDIA’s pricing artefacts. This will help explore how structured 
content, modern search tools and simple internal user interfaces can:
</p>
<ul>
    <li>reduce manual effort</li>
    <li>improve clarity and consistency</li>
    <li>support planners, providers and participants more effectively</li>
    <li>strengthen NDIA’s stewardship of disability service markets</li>
</ul>
</div>
""",
unsafe_allow_html=True
)

# -------------------------
# Strategic Alignment
# -------------------------
section_heading("Strategic Alignment")

st.markdown(
r"""
<div class="card">
<h3>Alignment with Whole-of-Government and internal direction</h3>
<p>
Minister Gallagher’s Whole-of-Government AI Plan emphasises:
</p>
<ul>
    <li>developing structured, machine-readable government information</li>
    <li>using AI to reduce low-value administrative work</li>
    <li>encouraging safe experimentation within secure APS environments</li>
    <li>prototyping before investing in major programs</li>
</ul>
<p>
Work by colleagues such as Daniel Bridgman — endorsed by Martin Mane — already shows that NDIA can 
safely explore AI-assisted document interrogation. This request builds on that precedent and extends it 
toward <b>modernising the artefacts themselves</b>.
</p>
</div>
""",
unsafe_allow_html=True
)

# -------------------------
# Limitations of Current Artefacts
# -------------------------
section_heading("Limitations of Current Artefact Format")

st.markdown(
r"""
<div class="card">
<h3>Why static documents are no longer sufficient</h3>
<p>
PAPL, Code Guides and Operational Guidance are currently maintained as static documents. This creates:
</p>
<ul>
    <li>slow, manual updates and reviews</li>
    <li>difficulty searching or interrogating rules</li>
    <li>limited reuse in digital tools or analytics</li>
    <li>inconsistent interpretation by planners and providers</li>
    <li>barriers to active market stewardship</li>
</ul>
<p>
These limitations make it harder for NDIA to deliver on its stewardship responsibilities.
</p>
</div>
""",
unsafe_allow_html=True
)

# ================================================================
# Digital PAPL Ecosystem Prototype
# ================================================================
section_heading("Digital PAPL Ecosystem Prototype")

st.markdown(
r"""
<div class="card">
<div class="pill">Future State</div>
<h3>What a structured, digital-first PAPL ecosystem could enable</h3>

<p>
Once pricing artefacts are maintained in structured formats — Markdown, JSON or schemas — 
they can serve as a <b>single authoritative source</b> for multiple internal and external needs.  
Instead of separate PDFs, the same structured content can underpin:
</p>

<ul>
    <li>planner-facing guidance tools</li>
    <li>participant-friendly explainers and calculators</li>
    <li>provider decision-support tools</li>
    <li>market monitoring dashboards</li>
    <li>search and interrogation interfaces</li>
    <li>automated validation workflows</li>
    <li>semantic search and AI assistants</li>
</ul>

<p>
The diagram below illustrates how structured artefacts enable a more dynamic, connected 
ecosystem — one update to the core artefact immediately flows through to every dependent tool.
</p>
</div>
""",
unsafe_allow_html=True
)

try:
    st.image(
        "assets/diagram_ecosystem.png",
        caption="Digital PAPL ecosystem — one structured source powering multiple tools.",
        use_container_width=True
    )
except:
    st.info("Add diagram_ecosystem.png to assets/ to display this image.")

# -------------------------
# Why a Toolset is Needed
# -------------------------
section_heading("Why This Work Requires the Toolset")

st.markdown(
r"""
<div class="card">
<h3>Capabilities that standard office tools cannot provide</h3>
<p>
Modernising pricing artefacts requires:
</p>
<ul>
    <li>running small APIs and servers for prototype UIs</li>
    <li>converting content into structured formats automatically</li>
    <li>containerised environments for reproducibility</li>
    <li>connecting to approved AI endpoints for semantic search</li>
</ul>
<p>
These capabilities require a lightweight development environment composed of VS Code, Git, Docker, Python 
and controlled access to AWS Bedrock.
</p>
</div>
""",
unsafe_allow_html=True
)

# -------------------------
# Governance and Safeguards
# -------------------------
section_heading("Governance and Safeguards")

st.markdown(
r"""
<div class="card">
<h3>How we ensure safety and control</h3>
<ul>
    <li>access limited to named Markets Delivery Branch staff</li>
    <li>only publicly available documents are used in prototypes</li>
    <li>no participant or provider identifying data is included</li>
    <li>all code stored in internal GitHub for traceability</li>
    <li>prototypes clearly labelled as non-production</li>
    <li>model usage controlled through IAM permissions</li>
</ul>
</div>
""",
unsafe_allow_html=True
)
