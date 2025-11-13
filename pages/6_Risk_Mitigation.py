import streamlit as st

st.title("Risk & Mitigation Annex")

st.markdown("""
<div class="card">
    <div class="pill">Overview</div>
    <h3>Managing risk in a controlled prototyping environment</h3>
    <p>
    Any work involving new tools or AI requires careful consideration of security, governance 
    and reputational risk. The approach proposed here is deliberately conservative: low-risk 
    activities, strong guardrails and clear separation between prototypes and production.
    </p>
    <p>
    The table below summarises the main risk domains and how they are managed.
    </p>
</div>
""", unsafe_allow_html=True)

with st.expander("Security & Data Protection", expanded=True):
    st.markdown("""
    <div class="card">
        <h3>Security & Data Protection</h3>
        <p><b>Key risks</b></p>
        <ul>
            <li><b>Unauthorised access to tools or model endpoints</b> – if access is not tightly controlled.</li>
            <li><b>Inadvertent exposure of sensitive data</b> – if prototypes accidentally use information that should not be sent to models.</li>
            <li><b>Prototypes being mistaken for production systems</b> – if they look polished but lack the formal assurances of live NDIA services.</li>
        </ul>
        <p><b>Mitigations</b></p>
        <ul>
            <li>Access restricted to named staff in the Markets Delivery Branch via NDIA IAM roles.</li>
            <li>Only publicly available artefacts (e.g. PAPL, Code Guides, OG) are used in prototypes.</li>
            <li>No participant- or provider-identifying data is handled in this environment.</li>
            <li>All prototypes clearly labelled as “Prototype – Not Production” in the UI.</li>
            <li>Environments are internal-only; no public URLs or external exposure.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with st.expander("Governance & Compliance", expanded=True):
    st.markdown("""
    <div class="card">
        <h3>Governance & Compliance</h3>
        <p><b>Key risks</b></p>
        <ul>
            <li><b>Perceived misalignment with the APS AI Plan</b> if work is not clearly documented.</li>
            <li><b>Uncontrolled proliferation of tools (shadow IT)</b> if prototypes are not visible to ICT.</li>
        </ul>
        <p><b>Mitigations</b></p>
        <ul>
            <li>Explicit alignment with Minister Gallagher’s Whole-of-Government AI Plan is documented.</li>
            <li>All code is stored in NDIA GitHub Enterprise / internal Git with clear repository naming.</li>
            <li>Digital/IT are informed of the environment and can review configurations and dependencies.</li>
            <li>Prototypes remain clearly separate from any production channels or systems.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with st.expander("Operational & Quality", expanded=False):
    st.markdown("""
    <div class="card">
        <h3>Operational & Quality Risks</h3>
        <p><b>Key risks</b></p>
        <ul>
            <li><b>Misinterpretation of prototype outputs</b> – users treating early concepts as final policy.</li>
            <li><b>Over-reliance on a single developer</b> – knowledge concentrated in one person.</li>
            <li><b>Inconsistent coding practices</b> – making prototypes hard to review or extend.</li>
        </ul>
        <p><b>Mitigations</b></p>
        <ul>
            <li>Clear disclaimers: prototypes do not represent agreed NDIA policy settings.</li>
            <li>Branch leadership (Director and Branch Manager) briefed early to manage expectations.</li>
            <li>Use of Git for code review and collaborative development.</li>
            <li>Simple internal documentation of each prototype’s purpose, assumptions and limitations.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with st.expander("Technical & Infrastructure", expanded=False):
    st.markdown("""
    <div class="card">
        <h3>Technical & Infrastructure Risks</h3>
        <p><b>Key risks</b></p>
        <ul>
            <li><b>Introduction of unapproved dependencies</b> – software libraries not aligned with ICT standards.</li>
            <li><b>Unexpected load on internal infrastructure</b> – poorly configured prototypes consuming resources.</li>
        </ul>
        <p><b>Mitigations</b></p>
        <ul>
            <li>Use of a short, controlled list of libraries (Streamlit, FastAPI, etc.), agreed with ICT.</li>
            <li>Containerisation via Docker so dependencies are well-defined and isolated.</li>
            <li>Use of lightweight hosting with monitoring of resource usage.</li>
            <li>Model usage throttled / capped, with logging where possible.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with st.expander("Reputational & Policy", expanded=False):
    st.markdown("""
    <div class="card">
        <h3>Reputational & Policy Risks</h3>
        <p><b>Key risks</b></p>
        <ul>
            <li><b>Prototype interfaces showing features not aligned with final NDIA policy</b>.</li>
            <li><b>External misunderstanding</b> if prototypes were ever shared outside the Agency.</li>
        </ul>
        <p><b>Mitigations</b></p>
        <ul>
            <li>All prototypes treated as internal working tools, never as external communications channels.</li>
            <li>Content and logic reviewed with Markets Strategy / Pricing before broader internal demonstrations.</li>
            <li>Any future external-facing tools would undergo normal NDIA approvals and publishing processes.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with st.expander("Ethical & Accessibility", expanded=False):
    st.markdown("""
    <div class="card">
        <h3>Ethical & Accessibility Considerations</h3>
        <p><b>Key risks</b></p>
        <ul>
            <li><b>Interfaces that are not accessible</b> for participants or staff using assistive technologies.</li>
            <li><b>AI-supported explanations that may oversimplify or miss important nuance</b>.</li>
        </ul>
        <p><b>Mitigations</b></p>
        <ul>
            <li>Use of accessible UI frameworks and colour choices aligned with WCAG principles.</li>
            <li>Human-in-the-loop review of any AI-generated explanatory text for participants.</li>
            <li>Adherence to APS ethical AI principles, with focus on transparency and accountability.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="pill">Summary</div>
    <h3>Overall risk position</h3>
    <p>
    With these mitigations in place, the overall risk of providing a small, controlled prototyping 
    environment to the Markets Delivery Branch is low and manageable. The potential benefits—in terms 
    of improved clarity, reduced manual effort and stronger market stewardship—are significant.
    </p>
</div>
""", unsafe_allow_html=True)
