import streamlit as st

st.title("Roadmap & Next Steps")

st.markdown("""
<div class="card">
    <div class="pill">High-Level Plan</div>
    <h3>How we could progress this work in low-risk stages</h3>
    <p>
    The intent is not to launch a large programme immediately, but to proceed in small, controlled steps. 
    Each phase generates evidence and artefacts that can be used to decide whether and how to proceed.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">Phase 1</div>
    <h3>Enable the toolset (0–4 weeks)</h3>
    <ul>
        <li>Confirm support from Markets Division leadership (GM, Branch Manager, Director).</li>
        <li>Submit formal request to Digital/IT for the controlled prototyping environment.</li>
        <li>Provision:
            <ul>
                <li>VS Code and GitHub Enterprise / internal Git repositories</li>
                <li>Docker for containerised prototypes</li>
                <li>Python runtime and core libraries</li>
                <li>Controlled AWS Bedrock access (LLMs + embeddings)</li>
            </ul>
        </li>
        <li>Agree basic governance settings (IAM roles, logging, coding standards).</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">Phase 2</div>
    <h3>First digital PAPL demonstrator (4–10 weeks)</h3>
    <ul>
        <li>Select a well-bounded section of PAPL or a code guide as a pilot.</li>
        <li>Convert that section into structured formats (e.g. JSON + Markdown).</li>
        <li>Build a simple API or data layer to serve the structured artefact.</li>
        <li>Create:
            <ul>
                <li>a provider-focused view (compliance and quoting)</li>
                <li>a planner-focused view (decision support)</li>
                <li>a participant-friendly view (plain-language explanation)</li>
            </ul>
        </li>
        <li>Demonstrate the prototype to Markets Division leadership and key stakeholders.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">Phase 3</div>
    <h3>Evaluation and refinement (10–14 weeks)</h3>
    <ul>
        <li>Gather feedback from:
            <ul>
                <li>Markets Strategy and Pricing teams</li>
                <li>frontline planners / LACs</li>
                <li>selected providers and internal advisory groups (where appropriate)</li>
            </ul>
        </li>
        <li>Assess:
            <ul>
                <li>clarity improvements compared to static documents</li>
                <li>potential reductions in manual effort</li>
                <li>opportunities for better market monitoring and stewardship</li>
            </ul>
        </li>
        <li>Refine the prototype based on feedback.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">Phase 4</div>
    <h3>Options for scaling and formal investment (14+ weeks)</h3>
    <ul>
        <li>Use the evidence from the prototype to outline options:
            <ul>
                <li>no further action (learning only)</li>
                <li>targeted enhancements to internal tools (e.g. planner guidance)</li>
                <li>a broader digital-first pricing artefact programme, if justified</li>
            </ul>
        </li>
        <li>Identify dependencies (ICT capacity, policy changes, data integration).</li>
        <li>Prepare input into any future business case or strategic initiative.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">Immediate Next Step</div>
    <h3>What we need to do first</h3>
    <p>
    The immediate next step is for Markets Division leadership to confirm support for a controlled 
    prototyping environment and to endorse a request to Digital/IT for the required tools. 
    This prototype site can be used as part of that conversation to show what is possible.
    </p>
</div>
""", unsafe_allow_html=True)
