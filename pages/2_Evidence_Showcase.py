import streamlit as st

st.title("Evidence Showcase")

st.markdown("""
<div class="card">
    <div class="pill">Proof of Capability</div>
    <h3>What we have already built</h3>
    <p>
    Outside the formal NDIA environment, and using minimal tooling, a number of prototypes have already 
    been developed to explore what digital-first approaches can deliver. These include:
    </p>
    <ul>
        <li>AI-powered document interrogation of complex policy and pricing artefacts</li>
        <li>interactive dashboards for Assistive Technology markets</li>
        <li>simulation tools to explain policy and pricing scenarios</li>
        <li>search and retrieval tools for pricing information</li>
    </ul>
    <p>
    These prototypes are important because they demonstrate that:
    </p>
    <ul>
        <li>useful tools can be built quickly and cheaply</li>
        <li>colleagues respond positively when they can <em>see</em> and <em>use</em> a concept</li>
        <li>modern tooling significantly shortens the idea-to-demonstrator cycle</li>
    </ul>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <div class="pill">Concept Diagram</div>
        <h3>Digital PAPL ecosystem</h3>
        <p>
        The diagram below illustrates how a structured pricing artefact can sit at the centre of multiple 
        tools: provider views, participant views, planner decision support and internal analytics.
        </p>
    </div>
    """, unsafe_allow_html=True)
    try:
        st.image(
            "assets/diagram_ecosystem.png",
            caption="Digital PAPL ecosystem – one structured source, many views.",
            use_container_width=True,
        )
    except Exception:
        st.info("Add 'diagram_ecosystem.png' to the assets folder to display this diagram.")

with col2:
    st.markdown("""
    <div class="card">
        <div class="pill">Existing Prototypes</div>
        <h3>Examples of prior work</h3>
        <p>
        Examples of existing prototypes include:
        </p>
        <ul>
            <li><b>AT Market Dashboard</b> – interactive visualisation of AT markets.</li>
            <li><b>PAPL search tools</b> – question-and-answer interfaces for pricing rules.</li>
            <li><b>Simulation tools</b> – exploring the impact of pricing rules on planners and markets.</li>
        </ul>
        <p>
        These demonstrate the value of having clean, structured data and modern frameworks for 
        rapid prototyping.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">Takeaway</div>
    <h3>Why this matters for NDIA</h3>
    <p>
    The key point is not the specific prototypes themselves, but what they show:
    </p>
    <ul>
        <li>there is strong potential to improve clarity, efficiency and stewardship</li>
        <li>these improvements can be explored safely using small, contained experiments</li>
        <li>a modest, well-governed toolset is enough to demonstrate meaningful value</li>
    </ul>
</div>
""", unsafe_allow_html=True)
