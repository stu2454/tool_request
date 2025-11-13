import streamlit as st

st.title("Detailed Case for Access")

st.markdown("""
<div class="card">
    <div class="pill">Purpose</div>
    <h3>Why we are seeking access to a controlled prototyping environment</h3>
    <p>
    The Markets Delivery Branch is seeking access to a small, well-governed development environment in order 
    to prototype digital-first versions of NDIA’s pricing artefacts. This will allow us to explore how structured 
    content, modern search tools and simple internal user interfaces can:
    </p>
    <ul>
        <li>reduce manual, repetitive work</li>
        <li>improve consistency and clarity</li>
        <li>support participants, providers and planners more effectively</li>
        <li>strengthen NDIA’s stewardship of disability support markets</li>
    </ul>
</div>
""", unsafe_allow_html=True)

with st.expander("Strategic alignment and precedent", expanded=True):
    st.markdown("""
    <div class="card">
        <h3>Alignment with Government and NDIA direction</h3>
        <p>
        Minister Gallagher’s Whole-of-Government AI Plan emphasises that:
        </p>
        <ul>
            <li>government information should progressively become structured and machine-readable</li>
            <li>AI and related tools should be used to reduce low-value manual work</li>
            <li>experimentation should occur inside secure government environments with clear guardrails</li>
        </ul>
        <p>
        Within NDIA, work by Daniel Bridgman, endorsed by Martin Mane, has already demonstrated that AI-enabled 
        interrogation of complex documents can be safe, controlled and valuable. 
        </p>
        <p>
        The proposed prototyping environment builds directly on this precedent, extending the approach from 
        analysis of existing documents to modernisation of the artefacts themselves.
        </p>
    </div>
    """, unsafe_allow_html=True)

with st.expander("Why the current approach is not sufficient", expanded=True):
    st.markdown("""
    <div class="card">
        <h3>Limitations of static pricing artefacts</h3>
        <p>
        Today, PAPL and related artefacts are maintained as static documents. This creates challenges:
        </p>
        <ul>
            <li>updates require time-consuming manual editing and cross-checking</li>
            <li>version control can be complex, particularly across multiple channels</li>
            <li>stakeholders must interpret rules themselves, increasing inconsistency</li>
            <li>integration with digital tools (for planners, providers or participants) is limited</li>
            <li>market monitoring is one step removed from the logic encoded in the artefacts</li>
        </ul>
        <p>
        These constraints make it harder for NDIA to act as an effective steward of the disability support market.
        </p>
    </div>
    """, unsafe_allow_html=True)

with st.expander("What the requested toolset enables (non-technical view)", expanded=True):
    st.markdown("""
    <div class="card">
        <h3>Practical benefits of access</h3>
        <ul>
            <li><b>Fewer manual updates</b> – rules change in one central structured source and flow through.</li>
            <li><b>Clearer market signals</b> – providers better understand price expectations and constraints.</li>
            <li><b>Consistent planner decisions</b> – decision support tools can present the same rules to all planners.</li>
            <li><b>Improved participant experience</b> – simpler, tailored views that explain what the pricing settings mean.</li>
            <li><b>Better compliance and oversight</b> – structured rules support automated checks and analytics.</li>
        </ul>
        <p>
        All of this can be explored on a small scale using prototypes before any commitment to larger programmes.
        </p>
    </div>
    """, unsafe_allow_html=True)

with st.expander("Why this work requires a development environment", expanded=False):
    st.markdown("""
    <div class="card">
        <h3>Why existing desktop tools are not enough</h3>
        <p>
        Modernising pricing artefacts requires capabilities that are not available through standard office tools:
        </p>
        <ul>
            <li>running local APIs and servers for prototype user interfaces</li>
            <li>containerising environments so they are repeatable and sharable</li>
            <li>integrating with approved AI endpoints for semantic search</li>
            <li>automatically converting documents into structured formats</li>
        </ul>
        <p>
        These activities are standard in public-sector digital teams, but they require a light-weight engineering 
        environment with access to VS Code, Docker, Git and managed AI services.
        </p>
    </div>
    """, unsafe_allow_html=True)

with st.expander("Governance and safeguards", expanded=False):
    st.markdown("""
    <div class="card">
        <h3>How we ensure this is safe, controlled and auditable</h3>
        <ul>
            <li>access is restricted to named individuals in the Markets Delivery Branch</li>
            <li>only publicly available artefacts (e.g. PAPL) are used in prototypes</li>
            <li>no participant or provider-identifying data is included</li>
            <li>all code lives in NDIA GitHub Enterprise / internal Git for auditability</li>
            <li>prototypes are clearly flagged as non-production</li>
            <li>model usage is controlled via IAM permissions and logging</li>
        </ul>
        <p>
        This keeps risk low while allowing the Branch to explore options and generate evidence.
        </p>
    </div>
    """, unsafe_allow_html=True)
