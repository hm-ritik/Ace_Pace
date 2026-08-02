import streamlit as st
from auth import get_token, save_token
from api import login

st.set_page_config(
    page_title="Ace Pace",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide the default Streamlit sidebar navigation
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if get_token():
    st.switch_page("pages/Dashboard.py")

st.markdown(
    """
    <h1 style='text-align:center;'>🎓 Ace Pace</h1>
    <h4 style='text-align:center;'>Hey buddy Ace Pace Welcomes You .</h4>
    """,
    unsafe_allow_html=True,
)

st.write("")

with st.container(border=True):

    st.subheader("Login")

    email = st.text_input("Email", placeholder="Enter your email")
    password = st.text_input("Password", type="password", placeholder="Enter your password")

    if st.button("Login", use_container_width=True):

        if not email or not password:
            st.warning("Please enter email and password.")
        else:
            response = login(email, password)

            if response.status_code == 200:
                token = response.json()["access_token"]
                save_token(token)
                st.success("Login Successful!")
                st.switch_page("pages/Dashboard.py")
            else:
                try:
                    st.error(response.json()["detail"])
                except Exception:
                    st.error("Login Failed")

st.write("")
st.write("")

st.markdown(
    """
    <div style="text-align:center; color:#888; font-size:14px;">
        Don't have an account? Email
        <a href="mailto:ritiksharma98010@gmail.com" style="color:#7ea6ff;">ritiksharma98010@gmail.com</a>
        to request your login ID and password.
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.link_button("GitHub — hm-ritik", "https://github.com/hm-ritik", use_container_width=True)