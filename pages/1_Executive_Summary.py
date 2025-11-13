import streamlit as st

st.title("Executive Summary")

st.markdown("""
<div class="card">
    <div class="pill">Context</div>
    <h3>Why NDIA’s pricing artefacts need to evolve</h3>
    <p>
    NDIA’s pricing artefacts—including the Pricing Arrangements and Price Limits (PAPL), 
    Code Guides and Operational Guidance—are foundational to how participants, providers, 
    planners and auditors engage with the Scheme.
    </p>
    <p>
    Today, these artefacts exist primarily as static documents (PDF, Word, HTML). They are 
    essential, but they are also:
    </p>
    <ul>
        <li>slow and manual to update</li>
        <li>difficult to search and interrogate</li>
        <li>hard to reuse in digital tools or analytics</li>
        <li>not tailored to different audience needs</li>
        <li>limited in their ability to support active market stewardship</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">Strategic Direction</div>
    <h3>Aligning with the Whole-of-Government AI Plan</h3>
    <p>
    Minister Gallagher’s Whole-of-Government AI Plan makes it clear that the APS is expected to modernise 
    how information is structured and delivered. Agencies are encouraged to:
    </p>
    <ul>
        <li>shift towards structured, machine-readable artefacts</li>
        <li>reduce manual, repetitive document handling</li>
        <li>experiment safely with AI and related tools inside secure environments</li>
        <li>prototype and evaluate options before committing to large programmes of work</li>
    </ul>
    <p>
    This prototype is a practical expression of those expectations within the NDIA context.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">Internal Precedent</div>
    <h3>Building on existing NDIA prototypes</h3>
    <p>
    Within NDIA, work led by colleagues such as Daniel Bridgman—using AI to interrogate complex policy 
    documents—has already demonstrated that:
    </p>
    <ul>
        <li>AI-assisted document interrogation can be safe, controlled and audited</li>
        <li>there is clear appetite for tools that improve clarity and reduce manual effort</li>
        <li>senior leaders are prepared to endorse small, well-governed experiments when the benefits are clear</li>
    </ul>
    <p>
    The Markets Delivery Branch is well placed to extend this approach from analysis of documents to 
    modernisation of the pricing artefacts themselves.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">Objective</div>
    <h3>What this prototype is trying to show</h3>
    <p>
    This site is not a production system. It is a demonstration of how pricing artefacts could be structured 
    as digital resources and used to:
    </p>
    <ul>
        <li>provide tailored views for participants, providers, planners and advocates</li>
        <li>support automated checks and decision support</li>
        <li>integrate more directly with market monitoring and analytics</li>
        <li>inform a future business case for more substantial investment</li>
    </ul>
</div>
""", unsafe_allow_html=True)
