import streamlit as st

st.title("Stakeholder View Matrix")

st.markdown("""
<div class="card">
    <div class="pill">Overview</div>
    <h3>How digital-first pricing artefacts support different stakeholders</h3>
    <p>
    A key advantage of structured, digital-first pricing artefacts is the ability to present 
    different views from a single source of truth. The same underlying rules can be expressed 
    differently for participants, providers, planners, advocates, analysts and innovators.
    </p>
</div>
""", unsafe_allow_html=True)

try:
    st.image(
        "assets/diagram_matrix.png",
        caption="Stakeholder View Matrix – different audiences, one structured source.",
        use_column_width=True,
    )
except Exception:
    st.info("Add 'diagram_matrix.png' to the assets folder to display the matrix diagram.")

# Detailed cards per stakeholder
st.markdown("""
<div class="card">
    <div class="pill">Participants & Families</div>
    <h3>Plain language and transparency</h3>
    <p>
    Participants and their families often encounter pricing information through layers of interpretation. 
    Digital-first artefacts allow NDIA to present:
    </p>
    <ul>
        <li>clear, accessible explanations of what price limits mean</li>
        <li>context about typical ranges and what is considered reasonable</li>
        <li>better support during planning conversations and reviews</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">Providers & New Entrants</div>
    <h3>Clarity, predictability and compliance</h3>
    <p>
    Providers need to understand not just the price limits, but the logic behind them. Digital-first artefacts can:
    </p>
    <ul>
        <li>reduce ambiguity and conflicting interpretations</li>
        <li>enable simple self-check tools for quotes and claims</li>
        <li>support new entrants to understand pricing expectations quickly</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">Planners & LACs</div>
    <h3>Decision support and consistency</h3>
    <p>
    Planners and LACs make daily decisions that depend on accurate, consistent interpretation of pricing rules. 
    Digital-first artefacts can support:
    </p>
    <ul>
        <li>embedded guidance and prompts at the point of decision</li>
        <li>more consistent application of rules across regions</li>
        <li>reduced need to manually hunt through long documents</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">Advocacy & Peak Bodies</div>
    <h3>Transparency and engagement</h3>
    <p>
    Advocacy organisations and peak bodies need a clear understanding of how pricing works in order to represent 
    participants and providers effectively. Structured artefacts provide:
    </p>
    <ul>
        <li>a stable reference point for policy submissions and feedback</li>
        <li>greater transparency around the logic of pricing decisions</li>
        <li>better tools to test scenarios and highlight issues</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">Researchers & Analysts</div>
    <h3>Structured data for insight and evaluation</h3>
    <p>
    Pricing artefacts expressed as structured data enable richer analysis. This can support:
    </p>
    <ul>
        <li>evaluation of pricing settings over time</li>
        <li>identification of patterns in utilisation and access</li>
        <li>better understanding of how pricing influences market behaviour</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">Technology Innovators</div>
    <h3>Safe, authoritative foundations for tools</h3>
    <p>
    When NDIA provides structured, authoritative guidance, innovators can build:
    </p>
    <ul>
        <li>planning aids and calculators</li>
        <li>accessibility-focused tools for participants with complex needs</li>
        <li>compliance-support tools for providers</li>
    </ul>
    <p>
    This reduces the risk of third parties scraping or re-interpreting static PDFs inappropriately.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">NDIA Internal Market Teams</div>
    <h3>Stewardship and early warning</h3>
    <p>
    Finally, digital-first artefacts support NDIA’s own stewardship responsibilities by:
    </p>
    <ul>
        <li>making it easier to connect pricing rules to claims and market data</li>
        <li>providing clearer signals of stress or distortion in the market</li>
        <li>supporting quicker, more targeted interventions when issues arise</li>
    </ul>
</div>
""", unsafe_allow_html=True)
