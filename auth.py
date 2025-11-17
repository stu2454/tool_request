import streamlit as st
import os

# --- CSS TO HIDE SIDEBAR ---
HIDE_SIDEBAR_CSS = """
<style>
/* Hide main sidebar */
[data-testid="stSidebar"] {
    display: none;
}
/* Hide the 'hamburger' menu */
[data-testid="collapsedControl"] {
    display: none;
}
</style>
"""

SHOW_SIDEBAR_CSS = """
<style>
[data-testid="stSidebar"] {
    display: block;
}
[data-testid="collapsedControl"] {
    display: block;
}
</style>
"""

def password_gate():
    correct_password = os.getenv("APP_PASSWORD")
    if correct_password is None:
        st.error("APP_PASSWORD is not configured in Render environment variables.")
        st.stop()

    # Hide sidebar until authenticated
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        st.markdown(HIDE_SIDEBAR_CSS, unsafe_allow_html=True)
    else:
        st.markdown(SHOW_SIDEBAR_CSS, unsafe_allow_html=True)
        return  # Already authenticated → show sidebar and full content

    # Login screen
    st.markdown("### 🔒 Restricted Access")
    st.write("Enter the access password to continue.")

    password = st.text_input("Password", type="password")

    if st.button("Submit"):
        if password == correct_password:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Incorrect password.")
            st.stop()

    st.stop()
